"""Engine milestone 4 - residue at scale and format-seam confirmation.

A realistic synthetic vault: one envelope, ~30 records across all five
accepted forms, mixed operations, a sweep after every phase. All data
is synthetic and grammar-placeholder only. The standing assertion is
the all-ciphertext property: at no checkpoint does any plaintext
marker byte appear anywhere on disk. Failure output identifies
location and category, never content.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    EnvelopeError, HeaderError, RecordError, StoreIntegrityError,
    change_passphrase, create_vault_key, decode_envelope, decode_record,
    encode_envelope, encode_record, import_record, parse_header,
    seal, unlock, unseal,
)
from engine.core.envelope import ENVELOPE_MAGIC  # noqa: E402
from engine.core.header import MAGIC  # noqa: E402
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

PASSPHRASE = b"SYNTHETIC-throwaway-passphrase-Persona-K9"
SECOND_PASSPHRASE = b"SYNTHETIC-second-throwaway-passphrase-Persona-K9"
# The marker every record's plaintext carries; it must never appear in
# any file on disk - everything at rest is ciphertext.
MARKER = b"SYNTHETIC-PLAINTEXT-MARKER-Persona-K9-Allergen-X"

FORM_SHAPES = {
    "pdf": b"%PDF-1.4\n% " + MARKER + b" record body.\n%%EOF\n",
    "png": b"\x89PNG\r\n\x1a\n" + MARKER + b" image placeholder bytes.",
    "jpeg": b"\xff\xd8\xff\xe0" + MARKER + b" image placeholder bytes.\xff\xd9",
    "text": MARKER + b" plain note. Corresponds to no real person.",
    "markdown": b"# SYNTHETIC\n\n" + MARKER + b" markdown note.\n",
}
RECORDS_PER_FORM = 6  # 6 x 5 forms = 30 records


class FixedClock:
    def now_iso(self) -> str:
        return "2026-01-01T00:00:00+00:00"


class VaultAtScale(unittest.TestCase):
    """One full vault lifecycle: create, populate, operate, re-key, reopen."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.crypto = PyNaClCrypto()
        self.clock = FixedClock()
        self.envelope = FileStorage(self.ws / "key.envelope")

    def files(self):
        return sorted(p.name for p in self.ws.rglob("*") if p.is_file())

    def assert_no_plaintext_on_disk(self, phase):
        for p in self.ws.rglob("*"):
            if p.is_file():
                self.assertNotIn(MARKER, p.read_bytes(),
                                 f"plaintext marker on disk after {phase}: "
                                 f"{p.name}")

    def test_vault_lifecycle_at_scale(self):
        # Phase A - create the envelope.
        master = create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        self.assertEqual(self.files(), ["key.envelope"])
        self.assert_no_plaintext_on_disk("create")

        # Phase B - import 30 records across all five accepted forms.
        expected = {}
        for form, shape in FORM_SHAPES.items():
            for i in range(RECORDS_PER_FORM):
                name = f"record-{form}-{i}.bin"
                payload = shape + b" #" + str(i).encode()
                import_record(FileStorage(self.ws / name), self.crypto,
                              self.clock, master, payload, form,
                              source="SYNTHETIC source")
                expected[name] = payload
        self.assertEqual(len(expected), 30)
        self.assertEqual(self.files(), sorted(["key.envelope"] + list(expected)))
        self.assert_no_plaintext_on_disk("import")

        # Phase C - unlock and unseal a sample of records.
        opened = unlock(self.envelope, self.crypto, PASSPHRASE)
        self.assertEqual(opened, master)
        sample = sorted(expected)[::5]
        for name in sample:
            provenance, payload = decode_record(
                unseal(FileStorage(self.ws / name), self.crypto, opened))
            self.assertEqual(payload, expected[name],
                             f"payload mismatch: {name}")
            self.assertEqual(provenance["system"]["verified_type"],
                             name.split("-")[1])
        self.assertEqual(self.files(), sorted(["key.envelope"] + list(expected)),
                         "reads must write nothing")
        self.assert_no_plaintext_on_disk("read")

        # Phase D - change the passphrase; every record stays byte-identical.
        record_bytes = {name: (self.ws / name).read_bytes()
                        for name in expected}
        envelope_before = self.envelope.read_blob()
        change_passphrase(self.envelope, self.crypto,
                          PASSPHRASE, SECOND_PASSPHRASE)
        for name in expected:
            self.assertEqual((self.ws / name).read_bytes(), record_bytes[name],
                             f"record bytes changed by custody event: {name}")
        self.assertNotEqual(self.envelope.read_blob(), envelope_before)
        self.assertEqual(self.files(), sorted(["key.envelope"] + list(expected)))
        self.assert_no_plaintext_on_disk("passphrase change")

        # Phase E - reopen with the new passphrase and read again.
        reopened = unlock(self.envelope, self.crypto, SECOND_PASSPHRASE)
        self.assertEqual(reopened, master)
        for name in sample:
            _, payload = decode_record(
                unseal(FileStorage(self.ws / name), self.crypto, reopened))
            self.assertEqual(payload, expected[name])
        self.assert_no_plaintext_on_disk("reopen")


class KillAtScale(unittest.TestCase):
    """A process killed mid-population leaves ciphertext and nothing else."""

    def test_kill_during_batch_import_leaves_no_plaintext(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import create_vault_key, import_record;"
                "from engine.ports import FileStorage, PyNaClCrypto,"
                " SystemClock;"
                "c = PyNaClCrypto(); clock = SystemClock();"
                "m = create_vault_key(FileStorage(sys.argv[2] +"
                " '/key.envelope'), c,"
                " b'SYNTHETIC-throwaway-passphrase-Persona-K9');"
                "marker = b'SYNTHETIC-PLAINTEXT-MARKER-Persona-K9-Allergen-X';"
                "[import_record(FileStorage(sys.argv[2] + '/record-%d.bin'"
                " % i), c, clock, m, marker + b' batch record', 'text',"
                " source='SYNTHETIC source') for i in range(10)];"
                "print('populated', flush=True);"
                "[import_record(FileStorage(sys.argv[2] + '/record-%d.bin'"
                " % i), c, clock, m, marker + b' late record', 'text',"
                " source='SYNTHETIC source') or time.sleep(0.2)"
                " for i in range(10, 200)]"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"populated", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            leftover = [f for f in Path(ws).rglob("*") if f.is_file()]
            self.assertGreaterEqual(len(leftover), 11)
            for f in leftover:
                self.assertNotIn(MARKER, f.read_bytes(),
                                 f"plaintext marker after kill: {f.name}")


class PartialWriteBlastRadius(unittest.TestCase):
    """The documented non-atomic-write finding: a truncated record
    refuses cleanly and touches nothing beside itself."""

    def test_truncated_record_refuses_cleanly_one_record_blast_radius(self):
        with tempfile.TemporaryDirectory() as ws:
            crypto = PyNaClCrypto()
            key = crypto.random_key()
            stores = []
            for i in range(3):
                store = FileStorage(Path(ws) / f"record-{i}.bin")
                seal(store, crypto, key, MARKER + b" record %d" % i)
                stores.append(store)
            damaged = stores[1]
            blob = damaged.read_blob()
            damaged.write_blob(blob[:len(blob) // 2])  # simulated partial write
            try:
                unseal(damaged, crypto, key)
                self.fail("truncated record was accepted")
            except StoreIntegrityError as e:
                self.assertNotIn(MARKER.decode(), str(e))
            for intact in (stores[0], stores[2]):
                payload = unseal(intact, crypto, key)
                self.assertIn(MARKER, payload,
                              "intact record damaged by neighbour truncation")


class FormatSeam(unittest.TestCase):
    """The three versioned formats stay distinct and refuse each other."""

    def setUp(self):
        crypto = PyNaClCrypto()
        key = crypto.random_key()
        self.store_blob = None
        with tempfile.TemporaryDirectory() as ws:
            store = FileStorage(Path(ws) / "store.bin")
            seal(store, crypto, key, b"SYNTHETIC seam payload, Persona-K9")
            self.store_blob = store.read_blob()
        self.record_blob = encode_record(
            {"note": "SYNTHETIC"}, b"SYNTHETIC seam payload bytes")
        self.envelope_blob = encode_envelope(
            "light-test", 1, 8192, bytes(16), b"S" * 72)

    def test_store_and_envelope_magics_are_distinct(self):
        self.assertNotEqual(MAGIC, ENVELOPE_MAGIC)

    def test_cross_decoder_refusal_matrix(self):
        cases = {
            "store bytes into envelope decoder":
                (decode_envelope, self.store_blob, EnvelopeError),
            "store bytes into record decoder":
                (decode_record, self.store_blob, RecordError),
            "envelope bytes into header decoder":
                (parse_header, self.envelope_blob, HeaderError),
            "envelope bytes into record decoder":
                (decode_record, self.envelope_blob, RecordError),
            "record bytes into header decoder":
                (parse_header, self.record_blob, HeaderError),
            "record bytes into envelope decoder":
                (decode_envelope, self.record_blob, EnvelopeError),
        }
        for name, (decoder, blob, error) in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(error):
                    decoder(blob)

    def test_consolidated_refusal_matrix(self):
        header_ok = self.store_blob
        cases = {
            "header: bad magic":
                (parse_header, b"NOPE" + header_ok[4:], HeaderError),
            "header: unknown version":
                (parse_header,
                 header_ok[:4] + (9).to_bytes(2, "big") + header_ok[6:],
                 HeaderError),
            "header: truncated":
                (parse_header, header_ok[:8], HeaderError),
            "record: unknown version":
                (decode_record,
                 (9).to_bytes(2, "big") + self.record_blob[2:], RecordError),
            "record: truncated":
                (decode_record, self.record_blob[:-3], RecordError),
            "record: trailing bytes":
                (decode_record, self.record_blob + b"x", RecordError),
            "envelope: bad magic":
                (decode_envelope, b"NOPE" + self.envelope_blob[4:],
                 EnvelopeError),
            "envelope: unknown version":
                (decode_envelope,
                 self.envelope_blob[:4] + (9).to_bytes(2, "big")
                 + self.envelope_blob[6:], EnvelopeError),
            "envelope: truncated":
                (decode_envelope, self.envelope_blob[:-3], EnvelopeError),
            "envelope: trailing bytes":
                (decode_envelope, self.envelope_blob + b"x", EnvelopeError),
        }
        for name, (decoder, blob, error) in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(error):
                    decoder(blob)


if __name__ == "__main__":
    unittest.main()
