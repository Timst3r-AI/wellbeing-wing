"""Engine milestone 2 - import path tests.

Synthetic data only: every file byte-string below is constructed in
this file from grammar placeholders; no on-disk binary fixtures exist
and none may be added. Keys remain test-supplied random keys. Failure
output never prints key material or file content.
"""

import ast
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    MAX_IMPORT_BYTES, ImportRefused, RecordError, StoreIntegrityError,
    decode_record, encode_record, import_record, unseal,
)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402


class FixedClock:
    """Deterministic clock double for provenance assertions."""

    def now_iso(self) -> str:
        return "2026-01-01T00:00:00+00:00"


SYNTHETIC_FORMS = {
    "pdf": (b"%PDF-1.4\n% SYNTHETIC document. Persona-K9. Corresponds to"
            b" no real person.\n%%EOF\n"),
    "png": (b"\x89PNG\r\n\x1a\n"
            b"SYNTHETIC image placeholder bytes. Persona-K9."),
    "jpeg": (b"\xff\xd8\xff\xe0"
             b"SYNTHETIC image placeholder bytes. Persona-K9.\xff\xd9"),
    "text": ("SYNTHETIC note. Persona-K9 states Allergen-X placeholder. "
             "Corresponds to no real person.").encode("utf-8"),
    "markdown": ("# SYNTHETIC\n\nPersona-K9 — Medication-A17 "
                 "placeholder. Corresponds to no real person.\n"
                 ).encode("utf-8"),
}


class ImportCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.storage = FileStorage(self.ws / "store.bin")
        self.crypto = PyNaClCrypto()
        self.clock = FixedClock()
        self.key = self.crypto.random_key()

    def do_import(self, data, claimed_type, **provenance):
        import_record(self.storage, self.crypto, self.clock, self.key,
                      data, claimed_type, **provenance)

    def read_back(self):
        return decode_record(unseal(self.storage, self.crypto, self.key))


class AcceptedForms(ImportCase):
    def test_roundtrip_byte_identity_on_every_accepted_form(self):
        for form, data in SYNTHETIC_FORMS.items():
            with self.subTest(form=form):
                storage = FileStorage(self.ws / f"{form}.bin")
                import_record(storage, self.crypto, self.clock, self.key,
                              data, form, source="SYNTHETIC source")
                provenance, payload = decode_record(
                    unseal(storage, self.crypto, self.key))
                self.assertEqual(payload, data)
                self.assertEqual(provenance["system"]["verified_type"], form)


class TypeVerification(ImportCase):
    def test_mistyped_bytes_are_refused_for_every_magic_form(self):
        wrong = b"SYNTHETIC bytes of no declared shape"
        for form in ("pdf", "png", "jpeg"):
            with self.subTest(form=form):
                with self.assertRaises(ImportRefused):
                    self.do_import(wrong, form)

    def test_undeclared_type_is_refused(self):
        with self.assertRaises(ImportRefused):
            self.do_import(SYNTHETIC_FORMS["pdf"], "docx")

    def test_invalid_utf8_is_refused_for_text_forms(self):
        for form in ("text", "markdown"):
            with self.subTest(form=form):
                with self.assertRaises(ImportRefused):
                    self.do_import(b"\xff\xfe\xfa broken", form)

    def test_empty_bytes_are_refused_for_magic_forms(self):
        for form in ("pdf", "png", "jpeg"):
            with self.subTest(form=form):
                with self.assertRaises(ImportRefused):
                    self.do_import(b"", form)

    def test_refusal_message_never_echoes_file_content(self):
        marker = b"ZZDISTINCTIVEMARKERZZ"
        try:
            self.do_import(marker + b" synthetic bytes", "pdf")
            self.fail("mistyped import was accepted")
        except ImportRefused as e:
            self.assertNotIn(marker.decode(), str(e))


class SizeCap(ImportCase):
    def test_over_cap_is_refused_and_writes_nothing(self):
        data = b"%PDF-" + bytes(MAX_IMPORT_BYTES)
        with self.assertRaises(ImportRefused):
            self.do_import(data, "pdf")
        self.assertFalse(self.storage.exists())

    def test_at_cap_is_accepted(self):
        data = (b"%PDF-" + bytes(MAX_IMPORT_BYTES))[:MAX_IMPORT_BYTES]
        self.do_import(data, "pdf")
        self.assertTrue(self.storage.exists())


class RefusalResidue(ImportCase):
    def test_refused_import_writes_nothing_at_all(self):
        with self.assertRaises(ImportRefused):
            self.do_import(b"SYNTHETIC mistyped bytes", "png")
        self.assertFalse(self.storage.exists())
        self.assertEqual(list(self.ws.rglob("*")), [])


class Provenance(ImportCase):
    def test_user_provenance_is_stored_verbatim(self):
        odd_date = "sometime around the second visit, maybe spring — 26"
        self.do_import(SYNTHETIC_FORMS["text"], "text",
                       source="SYNTHETIC clinic letter", date=odd_date,
                       note="SYNTHETIC note text")
        provenance, _ = self.read_back()
        self.assertEqual(provenance["user"]["date"], odd_date)
        self.assertEqual(provenance["user"]["source"],
                         "SYNTHETIC clinic letter")
        self.assertEqual(provenance["user"]["note"], "SYNTHETIC note text")

    def test_unprovenanced_label_is_stored_inside_the_sealed_record(self):
        cases = {
            "nothing": ({}, True),
            "note only": ({"note": "SYNTHETIC"}, True),
            "source given": ({"source": "SYNTHETIC"}, False),
            "date given": ({"date": "SYNTHETIC date"}, False),
        }
        for name, (prov, expected) in cases.items():
            with self.subTest(case=name):
                storage = FileStorage(self.ws / f"{name}.bin")
                import_record(storage, self.crypto, self.clock, self.key,
                              SYNTHETIC_FORMS["text"], "text", **prov)
                provenance, _ = decode_record(
                    unseal(storage, self.crypto, self.key))
                self.assertIs(provenance["unprovenanced_by_user"], expected)

    def test_system_facts_come_from_ports_not_content(self):
        data = SYNTHETIC_FORMS["markdown"]
        self.do_import(data, "markdown")
        provenance, _ = self.read_back()
        system = provenance["system"]
        self.assertEqual(system["imported_at"], self.clock.now_iso())
        self.assertEqual(system["byte_size"], len(data))
        self.assertEqual(system["verified_type"], "markdown")
        self.assertEqual(set(system), {"imported_at", "byte_size",
                                       "verified_type"},
                         "system facts beyond the decided three")


class RecordEncoding(unittest.TestCase):
    def test_unknown_record_version_is_refused(self):
        blob = bytearray(encode_record({"k": "v"}, b"SYNTHETIC"))
        blob[0:2] = (9).to_bytes(2, "big")
        with self.assertRaises(RecordError):
            decode_record(bytes(blob))

    def test_malformed_records_are_refused(self):
        good = encode_record({"k": "v"}, b"SYNTHETIC")
        for name, bad in {"truncated": good[:-3],
                          "trailing bytes": good + b"x",
                          "too short": b"\x00\x01"}.items():
            with self.subTest(case=name):
                with self.assertRaises(RecordError):
                    decode_record(bad)


class KeyDiscipline(ImportCase):
    def test_wrong_key_fails_clean_on_an_imported_record(self):
        self.do_import(SYNTHETIC_FORMS["text"], "text")
        with self.assertRaises(StoreIntegrityError):
            unseal(self.storage, self.crypto, self.crypto.random_key())

    def test_no_key_material_in_the_record_file(self):
        self.do_import(SYNTHETIC_FORMS["text"], "text")
        self.assertNotIn(self.key, self.storage.read_blob())


class NoInterpretationStructure(unittest.TestCase):
    """ADR 0009's structural cap: the import path cannot parse what it
    cannot import. The core may reach only json and itself; ports may
    reach only their declared worldly libraries."""

    def _imports_of(self, src):
        tree = ast.parse(src.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    yield alias.name.split(".")[0]
            elif isinstance(node, ast.ImportFrom):
                yield (node.module or "").split(".")[0]

    def test_core_imports_only_json_and_itself(self):
        for src in (ROOT / "engine" / "core").rglob("*.py"):
            for name in self._imports_of(src):
                self.assertIn(name, {"json", "engine"},
                              f"core module {src.name} imports {name}")

    def test_ports_import_only_their_declared_libraries(self):
        allowed = {"nacl", "pathlib", "typing", "datetime", "engine"}
        for src in (ROOT / "engine" / "ports").rglob("*.py"):
            for name in self._imports_of(src):
                self.assertIn(name, allowed,
                              f"port module {src.name} imports {name}")


class ImportResidue(unittest.TestCase):
    """ADR 0004 on the import path: the point of maximal sensitivity
    leaves exactly one file behind, however the process ends."""

    def _workspace_files(self, ws):
        return sorted(p.name for p in Path(ws).rglob("*") if p.is_file())

    def test_normal_termination_leaves_only_the_record(self):
        with tempfile.TemporaryDirectory() as ws:
            storage = FileStorage(Path(ws) / "store.bin")
            crypto = PyNaClCrypto()
            key = crypto.random_key()
            import_record(storage, crypto, FixedClock(), key,
                          SYNTHETIC_FORMS["pdf"], "pdf",
                          source="SYNTHETIC source")
            unseal(storage, crypto, key)
            self.assertEqual(self._workspace_files(ws), ["store.bin"])

    def test_kill_termination_leaves_only_the_record(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import import_record;"
                "from engine.ports import FileStorage, PyNaClCrypto,"
                " SystemClock; c = PyNaClCrypto();"
                "import_record(FileStorage(sys.argv[2] + '/store.bin'), c,"
                " SystemClock(), c.random_key(),"
                " b'%PDF- SYNTHETIC kill-path bytes, Persona-K9', 'pdf',"
                " source='SYNTHETIC source');"
                "print('stored', flush=True); time.sleep(30)"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"stored", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            self.assertEqual(self._workspace_files(ws), ["store.bin"])


if __name__ == "__main__":
    unittest.main()
