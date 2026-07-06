"""W3-D6 milestone 2 - export-as-right tests.

Synthetic grammar placeholders only. The properties under proof: the
import/export byte symmetry, provenance as structured return always
and sidecar only-when-explicit, destination validation before any
write, the profile-class refusal, and sources untouched throughout.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    ExportError, HeaderError, LedgerEvent, ProfileItem,
    StoreIntegrityError, append_event, create_vault_key, export_backup,
    export_record, import_record, persist_item,
)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

PASSPHRASE = b"SYNTHETIC-throwaway-passphrase-Persona-K9"
MARKER = b"SYNTHETIC-EXPORT-MARKER-Persona-K9-Allergen-X"
IMPORTED = MARKER + b" the user's own bytes, Persona-K9"
AT = "2026-01-02T00:00:00+00:00"


class FixedClock:
    def now_iso(self) -> str:
        return AT


class ExportCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.crypto = PyNaClCrypto()
        self.key = self.crypto.random_key()
        self.record = FileStorage(self.ws / "record.bin")
        import_record(self.record, self.crypto, FixedClock(), self.key,
                      IMPORTED, "text", source="SYNTHETIC source",
                      date="SYNTHETIC user-stated date")
        self.source_bytes = self.record.read_blob()
        self.out = FileStorage(self.ws / "out.bin")
        self.sidecar = FileStorage(self.ws / "out.provenance.json")

    def files(self):
        return sorted(p.name for p in self.ws.rglob("*") if p.is_file())

    def assert_source_untouched(self):
        self.assertEqual(self.record.read_blob(), self.source_bytes,
                         "export touched the source record")

    def assert_nothing_written(self):
        self.assertEqual(self.files(), ["record.bin"],
                         "a refusal wrote something")


class ExportRight(ExportCase):
    def test_payload_exports_byte_identically(self):
        result = export_record(self.record, self.crypto, self.key, self.out)
        self.assertEqual(self.out.read_blob(), IMPORTED,
                         "the bytes that entered must leave identical")
        self.assertEqual(result["provenance"]["user"]["date"],
                         "SYNTHETIC user-stated date",
                         "provenance must return as structured data")
        self.assert_source_untouched()

    def test_default_call_writes_exactly_one_file(self):
        export_record(self.record, self.crypto, self.key, self.out)
        self.assertEqual(self.files(), ["out.bin", "record.bin"],
                         "default export must write only the payload")

    def test_sidecar_only_with_explicit_destination(self):
        result = export_record(self.record, self.crypto, self.key,
                               self.out, provenance_destination=self.sidecar)
        self.assertEqual(self.files(),
                         ["out.bin", "out.provenance.json", "record.bin"])
        written = json.loads(self.sidecar.read_blob().decode("utf-8"))
        self.assertEqual(written, result["provenance"],
                         "sidecar must match the stored provenance exactly")
        self.assertEqual(written["system"]["byte_size"], len(IMPORTED))
        self.assert_source_untouched()


class ExportRefusals(ExportCase):
    def test_wrong_key_refuses_content_free_and_writes_nothing(self):
        try:
            export_record(self.record, self.crypto,
                          self.crypto.random_key(), self.out)
            self.fail("wrong key was accepted")
        except StoreIntegrityError as e:
            self.assertNotIn(MARKER.decode(), str(e))
        self.assert_nothing_written()
        self.assert_source_untouched()

    def test_foreign_formats_refuse(self):
        envelope = FileStorage(self.ws / "key.envelope")
        master = create_vault_key(envelope, self.crypto, PASSPHRASE)
        ledger = FileStorage(self.ws / "ledger.bin")
        append_event(ledger, self.crypto, master,
                     LedgerEvent("D3-T3", ("Condition-Q",), AT))
        backup = FileStorage(self.ws / "backup.wbwb")
        export_backup(backup, self.crypto, master, envelope,
                      [("r.bin", "record", self.record)])
        for name in ("key.envelope", "ledger.bin", "backup.wbwb"):
            with self.subTest(foreign=name):
                out = FileStorage(self.ws / f"out-{name}.bin")
                with self.assertRaises(HeaderError):
                    export_record(FileStorage(self.ws / name),
                                  self.crypto, master, out)
                self.assertFalse(out.exists())

    def test_profile_class_record_refuses_content_free(self):
        profile = FileStorage(self.ws / "profile.bin")
        item = ProfileItem("Condition-Q",
                           MARKER.decode() + " profile note",
                           "user-reported", "system-on-user-entry",
                           "unknown freshness")
        persist_item(profile, self.crypto, self.key, item)
        try:
            export_record(profile, self.crypto, self.key, self.out)
            self.fail("a profile-class record was exported")
        except ExportError as e:
            self.assertNotIn(MARKER.decode(), str(e))
        self.assertFalse(self.out.exists(),
                         "profile refusal must write nothing")

    def test_existing_payload_destination_refuses_before_any_write(self):
        self.out.write_blob(b"SYNTHETIC occupant")
        with self.assertRaises(ExportError):
            export_record(self.record, self.crypto, self.key, self.out,
                          provenance_destination=self.sidecar)
        self.assertEqual(self.out.read_blob(), b"SYNTHETIC occupant",
                         "an existing destination was overwritten")
        self.assertFalse(self.sidecar.exists(),
                         "a refusal wrote the sidecar")
        self.assert_source_untouched()

    def test_existing_provenance_destination_refuses_both_writes(self):
        self.sidecar.write_blob(b"SYNTHETIC occupant")
        with self.assertRaises(ExportError):
            export_record(self.record, self.crypto, self.key, self.out,
                          provenance_destination=self.sidecar)
        self.assertFalse(self.out.exists(),
                         "the payload was written despite the sidecar refusal")
        self.assertEqual(self.sidecar.read_blob(), b"SYNTHETIC occupant")
        self.assert_source_untouched()


if __name__ == "__main__":
    unittest.main()
