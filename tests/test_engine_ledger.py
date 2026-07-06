"""Durable-ledger store tests (the ADR 0015 implementation milestone).

Synthetic events only - grammar-placeholder refs, no content anywhere,
because the event shape itself refuses content by construction. The
properties under proof: append-only bytewise, torn-tail honesty with
one-event blast radius, sealed-at-rest, explicit whole-ledger erasure,
and the caller-side boundary that keeps the appliers pure.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    EnvelopeError, HeaderError, LedgerEvent, RecordError,
    append_event, apply_user_entry, decode_envelope, decode_record,
    erase_ledger, parse_header, read_events, seal,
)
from engine.core.ledger_store import (  # noqa: E402
    LEDGER_HEADER_SIZE, LEDGER_MAGIC, LedgerError,
)
from engine.core.header import MAGIC  # noqa: E402
from engine.core.envelope import ENVELOPE_MAGIC  # noqa: E402
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

MARKER = "SYNTHETIC-LEDGER-MARKER-Persona-K9-Allergen-X"
AT = "2026-01-02T00:00:00+00:00"


def synthetic_event(n=0):
    return LedgerEvent("D3-T3", (f"{MARKER}-section-{n}",), AT)


class LedgerCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.storage = FileStorage(self.ws / "ledger.bin")
        self.crypto = PyNaClCrypto()
        self.key = self.crypto.random_key()

    def files(self):
        return sorted(p.name for p in self.ws.rglob("*") if p.is_file())


class RoundtripAndOrder(LedgerCase):
    def test_multi_event_append_reads_back_in_order(self):
        for n in range(5):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        events, tail_intact = read_events(self.storage, self.crypto,
                                          self.key)
        self.assertTrue(tail_intact)
        self.assertEqual([e.refs[0] for e in events],
                         [f"{MARKER}-section-{n}" for n in range(5)],
                         "append order must be read order")
        self.assertTrue(all(e.kind == "D3-T3" for e in events))

    def test_real_applier_event_appends_and_reads_back(self):
        emitted = apply_user_entry("Condition-Q",
                                   "SYNTHETIC note, Persona-K9",
                                   AT)["event"]
        append_event(self.storage, self.crypto, self.key, emitted)
        events, tail_intact = read_events(self.storage, self.crypto,
                                          self.key)
        self.assertTrue(tail_intact)
        self.assertEqual(len(events), 1)
        self.assertEqual(vars(events[0]), vars(emitted),
                         "the stored event must equal the emitted event")

    def test_header_only_ledger_reads_as_zero_events(self):
        append_event(self.storage, self.crypto, self.key, synthetic_event())
        erase_ledger(self.storage)
        append_event(self.storage, self.crypto, self.key, synthetic_event())
        erase_ledger(self.storage)
        self.storage.write_blob(
            LEDGER_MAGIC + (1).to_bytes(2, "big") + bytes(10))
        events, tail_intact = read_events(self.storage, self.crypto,
                                          self.key)
        self.assertEqual(events, ())
        self.assertTrue(tail_intact)


class HeaderDiscipline(LedgerCase):
    def test_bad_magic_refuses(self):
        self.storage.write_blob(b"NOPE" + (1).to_bytes(2, "big") + bytes(10))
        with self.assertRaises(LedgerError):
            read_events(self.storage, self.crypto, self.key)
        with self.assertRaises(LedgerError):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event())

    def test_unknown_version_refuses(self):
        self.storage.write_blob(
            LEDGER_MAGIC + (9).to_bytes(2, "big") + bytes(10))
        with self.assertRaises(LedgerError):
            read_events(self.storage, self.crypto, self.key)

    def test_missing_or_short_header_refuses(self):
        self.storage.write_blob(b"WB")
        with self.assertRaises(LedgerError):
            read_events(self.storage, self.crypto, self.key)


class AppendOnly(LedgerCase):
    def test_prior_bytes_are_identical_after_every_append(self):
        append_event(self.storage, self.crypto, self.key, synthetic_event(0))
        for n in range(1, 4):
            before = self.storage.read_blob()
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
            after = self.storage.read_blob()
            self.assertGreater(len(after), len(before))
            self.assertEqual(after[:len(before)], before,
                             "an append rewrote prior history")


class TornTail(LedgerCase):
    def _write_three_then_truncate(self, cut):
        for n in range(3):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        blob = self.storage.read_blob()
        self.storage.write_blob(blob[:cut])

    def test_truncation_mid_frame_keeps_intact_history(self):
        full = None
        for n in range(3):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        full = self.storage.read_blob()
        self.storage.write_blob(full[:-7])  # tear inside the last frame
        events, tail_intact = read_events(self.storage, self.crypto,
                                          self.key)
        self.assertFalse(tail_intact, "torn tail must be reported")
        self.assertEqual(len(events), 2,
                         "intact prior events must remain available")

    def test_truncation_mid_length_prefix_keeps_intact_history(self):
        for n in range(2):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        two = self.storage.read_blob()
        append_event(self.storage, self.crypto, self.key, synthetic_event(2))
        self.storage.write_blob(self.storage.read_blob()[:len(two) + 2])
        events, tail_intact = read_events(self.storage, self.crypto,
                                          self.key)
        self.assertFalse(tail_intact)
        self.assertEqual(len(events), 2)


class SealedAtRest(LedgerCase):
    def test_wrong_key_refuses_clean_and_content_free(self):
        append_event(self.storage, self.crypto, self.key, synthetic_event())
        try:
            read_events(self.storage, self.crypto, self.crypto.random_key())
            self.fail("wrong key was accepted")
        except LedgerError as e:
            self.assertNotIn(MARKER, str(e))

    def test_plaintext_marker_absent_from_ledger_bytes(self):
        for n in range(3):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        self.assertNotIn(MARKER.encode(), self.storage.read_blob(),
                         "governance metadata readable at rest")

    def test_non_ledger_event_input_refuses(self):
        for bad in ({"kind": "D3-T3"}, "event", None, 7):
            with self.subTest(input=type(bad).__name__):
                with self.assertRaises(LedgerError):
                    append_event(self.storage, self.crypto, self.key, bad)
        self.assertFalse(self.storage.exists(),
                         "refused input must write nothing")


class Erasure(LedgerCase):
    def test_erase_removes_the_ledger_file_and_nothing_else(self):
        append_event(self.storage, self.crypto, self.key, synthetic_event())
        other = FileStorage(self.ws / "store.bin")
        seal(other, self.crypto, self.key, b"SYNTHETIC record, Persona-K9")
        self.assertEqual(self.files(), ["ledger.bin", "store.bin"])
        erase_ledger(self.storage)
        self.assertEqual(self.files(), ["store.bin"],
                         "erasure touched something beside the ledger")
        self.assertFalse(self.storage.exists())


class LedgerResidue(LedgerCase):
    def test_normal_termination_exact_file_set(self):
        for n in range(3):
            append_event(self.storage, self.crypto, self.key,
                         synthetic_event(n))
        read_events(self.storage, self.crypto, self.key)
        self.assertEqual(self.files(), ["ledger.bin"])

    def test_kill_during_append_loop_leaves_no_plaintext(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import LedgerEvent, append_event;"
                "from engine.ports import FileStorage, PyNaClCrypto;"
                "c = PyNaClCrypto(); k = c.random_key();"
                "s = FileStorage(sys.argv[2] + '/ledger.bin');"
                "marker = 'SYNTHETIC-LEDGER-MARKER-Persona-K9-Allergen-X';"
                "[append_event(s, c, k, LedgerEvent('D3-T3',"
                " (marker + '-' + str(i),), 'T0')) for i in range(10)];"
                "print('appended', flush=True);"
                "[ (append_event(s, c, k, LedgerEvent('D3-T3',"
                " (marker + '-late-' + str(i),), 'T0')),"
                " time.sleep(0.2)) for i in range(10, 200)]"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"appended", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            leftover = [f for f in Path(ws).rglob("*") if f.is_file()]
            self.assertEqual([f.name for f in leftover], ["ledger.bin"])
            blob = leftover[0].read_bytes()
            self.assertEqual(blob[:4], LEDGER_MAGIC)
            self.assertNotIn(MARKER.encode(), blob,
                             "plaintext governance metadata after kill")


class LedgerFormatSeam(LedgerCase):
    def test_ledger_magic_is_distinct_and_formats_refuse_each_other(self):
        self.assertEqual(len({MAGIC, ENVELOPE_MAGIC, LEDGER_MAGIC}), 3)
        append_event(self.storage, self.crypto, self.key, synthetic_event())
        ledger_blob = self.storage.read_blob()
        with self.assertRaises(HeaderError):
            parse_header(ledger_blob)
        with self.assertRaises(EnvelopeError):
            decode_envelope(ledger_blob)
        with self.assertRaises(RecordError):
            decode_record(ledger_blob)
        store = FileStorage(self.ws / "store.bin")
        seal(store, self.crypto, self.key, b"SYNTHETIC, Persona-K9")
        foreign = FileStorage(self.ws / "store.bin")
        with self.assertRaises(LedgerError):
            read_events(foreign, self.crypto, self.key)


if __name__ == "__main__":
    unittest.main()
