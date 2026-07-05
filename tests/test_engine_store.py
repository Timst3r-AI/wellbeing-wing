"""Engine milestone 1 — store skeleton tests.

Synthetic data only (grammar placeholders; no clinical meaning).
Keys are test-supplied random keys: no derivation, custody, or
persistence exists in this milestone by decision. Failure output
never prints key material or content.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    HEADER_SIZE, HeaderError, StoreIntegrityError,
    build_header, parse_header, seal, unseal,
)
from engine.ports import KEY_SIZE, FileStorage, PyNaClCrypto  # noqa: E402

SYNTHETIC = (b"SYNTHETIC engine test content. Persona-K9. Allergen-X "
             b"placeholder. Corresponds to no real person.")


class HeaderBaseline(unittest.TestCase):
    def test_header_is_sixteen_bytes_with_zero_reserved(self):
        h = build_header()
        self.assertEqual(len(h), HEADER_SIZE)
        self.assertEqual(h[:4], b"WBWG")
        self.assertEqual(h[6:], bytes(10), "reserved bytes must be zero in v1")

    def test_unknown_version_and_bad_magic_refuse_cleanly(self):
        with self.assertRaises(HeaderError):
            parse_header(b"WBWG" + (9).to_bytes(2, "big") + bytes(10) + b"x")
        with self.assertRaises(HeaderError):
            parse_header(b"NOPE" + (1).to_bytes(2, "big") + bytes(10) + b"x")
        with self.assertRaises(HeaderError):
            parse_header(b"short")


class StoreRoundtrip(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.storage = FileStorage(Path(self.tmp.name) / "store.bin")
        self.crypto = PyNaClCrypto()
        self.key = self.crypto.random_key()

    def test_roundtrip_byte_identity(self):
        seal(self.storage, self.crypto, self.key, SYNTHETIC)
        self.assertEqual(unseal(self.storage, self.crypto, self.key), SYNTHETIC)

    def test_tamper_is_rejected(self):
        seal(self.storage, self.crypto, self.key, SYNTHETIC)
        blob = bytearray(self.storage.read_blob())
        blob[-1] ^= 0xFF
        self.storage.write_blob(bytes(blob))
        with self.assertRaises(StoreIntegrityError):
            unseal(self.storage, self.crypto, self.key)

    def test_wrong_key_fails_clean_with_no_partial_plaintext(self):
        seal(self.storage, self.crypto, self.key, SYNTHETIC)
        try:
            unseal(self.storage, self.crypto, self.crypto.random_key())
            self.fail("wrong key was accepted")
        except StoreIntegrityError as e:
            msg = str(e).encode()
            self.assertNotIn(SYNTHETIC[:20], msg)
            self.assertNotIn(self.key, msg)

    def test_no_key_material_in_store_file(self):
        seal(self.storage, self.crypto, self.key, SYNTHETIC)
        self.assertEqual(len(self.key), KEY_SIZE)
        self.assertNotIn(self.key, self.storage.read_blob())


class ResidueDiscipline(unittest.TestCase):
    """ADR 0004's test class: operate, terminate, prove nothing remains."""

    def _workspace_files(self, ws):
        return sorted(p.name for p in Path(ws).rglob("*") if p.is_file())

    def test_normal_termination_leaves_only_the_store(self):
        with tempfile.TemporaryDirectory() as ws:
            storage = FileStorage(Path(ws) / "store.bin")
            crypto = PyNaClCrypto()
            key = crypto.random_key()
            seal(storage, crypto, key, SYNTHETIC)
            unseal(storage, crypto, key)
            self.assertEqual(self._workspace_files(ws), ["store.bin"])

    def test_kill_termination_leaves_only_the_store(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import seal; from engine.ports import "
                "FileStorage, PyNaClCrypto; c = PyNaClCrypto();"
                "seal(FileStorage(sys.argv[2] + '/store.bin'), c, "
                "c.random_key(), b'SYNTHETIC kill-path content, Persona-K9');"
                "print('sealed', flush=True); time.sleep(30)"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"sealed", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            self.assertEqual(self._workspace_files(ws), ["store.bin"])

    def test_engine_emits_nothing_and_logs_nothing(self):
        engine_sources = list((ROOT / "engine").rglob("*.py"))
        self.assertTrue(engine_sources)
        for src in engine_sources:
            text = src.read_text(encoding="utf-8")
            self.assertNotIn("print(", text,
                             f"engine source emits output: {src.name}")
            self.assertNotIn("import logging", text,
                             f"engine source logs: {src.name}")


class PostureAssertions(unittest.TestCase):
    """ADR 0010: the application tree carries no review or approval."""

    def _engine_text(self):
        return {src: src.read_text(encoding="utf-8")
                for src in (ROOT / "engine").rglob("*.py")}

    def test_no_simulated_review_caller_outside_tests(self):
        for src, text in self._engine_text().items():
            for token in ("simulate", "review_act", "approve("):
                self.assertNotIn(token, text,
                                 f"review-shaped token in application tree: {src.name}")

    def test_no_approved_status_anywhere_in_application_tree(self):
        for src, text in self._engine_text().items():
            self.assertNotIn("Approved", text,
                             f"approved-status vocabulary in application tree: "
                             f"{src.name} (no profile layer exists in this milestone)")


if __name__ == "__main__":
    unittest.main()
