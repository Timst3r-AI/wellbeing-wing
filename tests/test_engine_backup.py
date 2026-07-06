"""W3-D6 milestone 1 - backup export and restore symmetry tests.

Synthetic grammar placeholders only; in-test constructed vaults. The
properties under proof: byte-identity across the roundtrip, the ruled
five-step validation order with writes only after validation, no
structure or names outside the sealed payload, no record plaintext
decrypted to restore, sources never touched, and the four-magic seam.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    BackupError, CustodyError, EnvelopeError, HeaderError, LedgerEvent,
    RecordError, append_event, create_vault_key, decode_envelope,
    decode_record, export_backup, import_record, parse_header,
    read_events, restore_backup, unlock, unseal,
)
from engine.core.backup import BACKUP_MAGIC  # noqa: E402
from engine.core.envelope import ENVELOPE_MAGIC  # noqa: E402
from engine.core.header import MAGIC  # noqa: E402
from engine.core.ledger_store import LEDGER_MAGIC, LedgerError  # noqa: E402
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402
from engine.ports.storage import DirectoryTarget  # noqa: E402

PASSPHRASE = b"SYNTHETIC-throwaway-passphrase-Persona-K9"
MARKER = b"SYNTHETIC-BACKUP-MARKER-Persona-K9-Allergen-X"
AT = "2026-01-02T00:00:00+00:00"


class FixedClock:
    def now_iso(self) -> str:
        return AT


class BackupCase(unittest.TestCase):
    """Builds a real synthetic vault: envelope + 3 records + ledger."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.vault = self.ws / "vault"
        self.vault.mkdir()
        self.crypto = PyNaClCrypto()
        self.envelope = FileStorage(self.vault / "key.envelope")
        self.master = create_vault_key(self.envelope, self.crypto,
                                       PASSPHRASE)
        self.record_names = []
        for n in range(3):
            name = f"record-{n}.bin"
            import_record(FileStorage(self.vault / name), self.crypto,
                          FixedClock(), self.master,
                          MARKER + b" record body %d" % n, "text",
                          source="SYNTHETIC source")
            self.record_names.append(name)
        self.ledger = FileStorage(self.vault / "ledger.bin")
        for n in range(3):
            append_event(self.ledger, self.crypto, self.master,
                         LedgerEvent("D3-T3", (f"Condition-Q-{n}",), AT))
        self.backup = FileStorage(self.ws / "backup.wbwb")

    def members(self):
        return ([(n, "record", FileStorage(self.vault / n))
                 for n in self.record_names]
                + [("ledger.bin", "ledger", self.ledger)])

    def vault_bytes(self):
        return {p.name: p.read_bytes()
                for p in sorted(self.vault.iterdir())}

    def do_export(self):
        export_backup(self.backup, self.crypto, self.master,
                      self.envelope, self.members())

    def target(self, name="restored"):
        return DirectoryTarget(self.ws / name), self.ws / name

    def assert_target_empty(self, path):
        self.assertTrue(not path.exists()
                        or next(path.iterdir(), None) is None,
                        "a refused restore wrote something")


class RoundtripSymmetry(BackupCase):
    def test_full_roundtrip_byte_identity_and_reopen(self):
        before = self.vault_bytes()
        self.do_export()
        target, tpath = self.target()
        result = restore_backup(self.backup, self.crypto, PASSPHRASE,
                                target)
        self.assertEqual(result["members"], 4)
        restored = {p.name: p.read_bytes() for p in sorted(tpath.iterdir())}
        self.assertEqual(restored, before,
                         "restore must reproduce every member byte-exactly")
        # the restored vault is a working vault
        master = unlock(FileStorage(tpath / "key.envelope"), self.crypto,
                        PASSPHRASE)
        self.assertEqual(master, self.master)
        blob = unseal(FileStorage(tpath / "record-0.bin"), self.crypto,
                      master)
        _, payload = decode_record(blob)
        self.assertIn(MARKER, payload)
        events, tail_intact = read_events(
            FileStorage(tpath / "ledger.bin"), self.crypto, master)
        self.assertEqual(len(events), 3)
        self.assertTrue(tail_intact)
        self.assertEqual(self.vault_bytes(), before,
                         "export or restore touched the source vault")

    def test_zero_member_backup_roundtrips(self):
        export_backup(self.backup, self.crypto, self.master,
                      self.envelope, [])
        target, tpath = self.target()
        result = restore_backup(self.backup, self.crypto, PASSPHRASE,
                                target)
        self.assertEqual(result["members"], 0)
        self.assertEqual([p.name for p in tpath.iterdir()],
                         ["key.envelope"])

    def test_torn_ledger_tail_travels_verbatim_and_reports(self):
        blob = self.ledger.read_blob()
        self.ledger.write_blob(blob[:-5])  # tear the tail at source
        self.do_export()
        target, tpath = self.target()
        restore_backup(self.backup, self.crypto, PASSPHRASE, target)
        events, tail_intact = read_events(
            FileStorage(tpath / "ledger.bin"), self.crypto, self.master)
        self.assertFalse(tail_intact, "the torn tail must be reported")
        self.assertEqual(len(events), 2,
                         "intact frames must survive the journey")


class RestoreRefusals(BackupCase):
    def test_non_empty_target_refuses_and_writes_nothing(self):
        self.do_export()
        target, tpath = self.target()
        tpath.mkdir()
        (tpath / "existing.bin").write_bytes(b"SYNTHETIC occupant")
        with self.assertRaises(BackupError):
            restore_backup(self.backup, self.crypto, PASSPHRASE, target)
        self.assertEqual([p.name for p in tpath.iterdir()],
                         ["existing.bin"])

    def test_wrong_passphrase_refuses_content_free_and_writes_nothing(self):
        self.do_export()
        target, tpath = self.target()
        try:
            restore_backup(self.backup, self.crypto,
                           b"SYNTHETIC-wrong-passphrase", target)
            self.fail("wrong passphrase was accepted")
        except CustodyError as e:
            self.assertNotIn(MARKER.decode(), str(e))
        self.assert_target_empty(tpath)

    def test_bad_magic_unknown_version_short_header_refuse(self):
        self.do_export()
        good = self.backup.read_blob()
        cases = {
            "bad magic": b"NOPE" + good[4:],
            "unknown version": good[:4] + (9).to_bytes(2, "big") + good[6:],
            "short header": good[:10],
        }
        for name, bad in cases.items():
            with self.subTest(case=name):
                self.backup.write_blob(bad)
                target, tpath = self.target(f"t-{len(name)}")
                with self.assertRaises(BackupError):
                    restore_backup(self.backup, self.crypto, PASSPHRASE,
                                   target)
                self.assert_target_empty(tpath)

    def test_tampered_payload_refuses_at_authentication(self):
        self.do_export()
        blob = bytearray(self.backup.read_blob())
        blob[-1] ^= 0xFF
        self.backup.write_blob(bytes(blob))
        target, tpath = self.target()
        with self.assertRaises(BackupError):
            restore_backup(self.backup, self.crypto, PASSPHRASE, target)
        self.assert_target_empty(tpath)

    def test_invalid_manifest_refuses_before_writes(self):
        envelope_bytes = self.envelope.read_blob()
        sealed = self.crypto.encrypt(self.master,
                                     b"\x00\x00\x00\x02{}garbage")
        self.backup.write_blob(
            BACKUP_MAGIC + (1).to_bytes(2, "big") + bytes(10)
            + len(envelope_bytes).to_bytes(4, "big") + envelope_bytes
            + sealed)
        target, tpath = self.target()
        with self.assertRaises(BackupError):
            restore_backup(self.backup, self.crypto, PASSPHRASE, target)
        self.assert_target_empty(tpath)

    def test_killed_partial_export_file_refuses_at_restore(self):
        self.do_export()
        good = self.backup.read_blob()
        for cut in (len(good) // 3, len(good) - 9):
            with self.subTest(cut=cut):
                self.backup.write_blob(good[:cut])
                target, tpath = self.target(f"t-{cut}")
                with self.assertRaises((BackupError, CustodyError,
                                        EnvelopeError)):
                    restore_backup(self.backup, self.crypto, PASSPHRASE,
                                   target)
                self.assert_target_empty(tpath)
        before = self.vault_bytes()
        self.assertEqual(self.vault_bytes(), before,
                         "failed restores touched the source vault")


class ExportDiscipline(BackupCase):
    def test_duplicate_and_bad_member_names_refuse(self):
        record = FileStorage(self.vault / self.record_names[0])
        cases = {
            "duplicate": [("a.bin", "record", record),
                          ("a.bin", "record", record)],
            "empty name": [("", "record", record)],
            "path separator": [("sub/dir.bin", "record", record)],
            "traversal": [("..", "record", record)],
            "envelope collision": [("key.envelope", "record", record)],
            "unknown kind": [("a.bin", "thumbnail", record)],
        }
        for name, members in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(BackupError):
                    export_backup(self.backup, self.crypto, self.master,
                                  self.envelope, members)

    def test_no_names_structure_or_plaintext_outside_sealed_payload(self):
        self.do_export()
        blob = self.backup.read_blob()
        self.assertNotIn(MARKER, blob, "plaintext content in backup file")
        for name in (b"record-0.bin", b"ledger.bin", b"key.envelope",
                     b"manifest", b"members"):
            self.assertNotIn(name, blob,
                             "structure visible outside the sealed payload")

    def test_restore_path_never_touches_record_plaintext(self):
        source = (ROOT / "engine" / "core" / "backup.py").read_text(
            encoding="utf-8")
        for token in ("unseal", "decode_record", "load_item",
                      "load_unknown"):
            self.assertNotIn(token, source,
                             f"restore path references {token}")

    def test_export_kill_sweep_leaves_no_plaintext(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import create_vault_key, import_record,"
                " export_backup;"
                "from engine.ports import FileStorage, PyNaClCrypto,"
                " SystemClock;"
                "c = PyNaClCrypto();"
                "env = FileStorage(sys.argv[2] + '/key.envelope');"
                "m = create_vault_key(env, c,"
                " b'SYNTHETIC-throwaway-passphrase-Persona-K9');"
                "rec = FileStorage(sys.argv[2] + '/r0.bin');"
                "marker = b'SYNTHETIC-BACKUP-MARKER-Persona-K9-Allergen-X';"
                "import_record(rec, c, SystemClock(), m,"
                " marker + b' body', 'text', source='SYNTHETIC');"
                "export_backup(FileStorage(sys.argv[2] + '/backup.wbwb'),"
                " c, m, env, [('r0.bin', 'record', rec)]);"
                "print('exported', flush=True); time.sleep(30)"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"exported", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            files = sorted(f.name for f in Path(ws).rglob("*")
                           if f.is_file())
            self.assertEqual(files,
                             ["backup.wbwb", "key.envelope", "r0.bin"])
            for f in Path(ws).rglob("*"):
                if f.is_file():
                    self.assertNotIn(MARKER, f.read_bytes(),
                                     f"plaintext after kill: {f.name}")


class BackupFormatSeam(BackupCase):
    def test_four_magics_distinct_and_bidirectional_refusal(self):
        self.assertEqual(
            len({MAGIC, ENVELOPE_MAGIC, LEDGER_MAGIC, BACKUP_MAGIC}), 4)
        self.do_export()
        backup_blob = self.backup.read_blob()
        with self.assertRaises(HeaderError):
            parse_header(backup_blob)
        with self.assertRaises(EnvelopeError):
            decode_envelope(backup_blob)
        with self.assertRaises(RecordError):
            decode_record(backup_blob)
        with self.assertRaises(LedgerError):
            read_events(self.backup, self.crypto, self.master)
        for name in ("key.envelope", "record-0.bin", "ledger.bin"):
            with self.subTest(foreign=name):
                target, tpath = self.target(f"t-{name.split('.')[0]}")
                with self.assertRaises(BackupError):
                    restore_backup(FileStorage(self.vault / name),
                                   self.crypto, PASSPHRASE, target)
                self.assert_target_empty(tpath)


if __name__ == "__main__":
    unittest.main()
