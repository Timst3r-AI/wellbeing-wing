"""Engine milestone 3 - key derivation, envelope, and custody tests.

Synthetic throwaway passphrases only; no real passphrase, key, or
content anywhere. Failure output never prints passphrases or key
material. True-moderate tests exercise the product path at the
ADR-selected profile; light-parameter tests exercise the
parameter-agnostic envelope encoding and the recorded-parameters
migration property using the library's minimum-cost parameters.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import nacl.pwhash  # noqa: E402

from engine.core import (  # noqa: E402
    CustodyError, EnvelopeError, change_passphrase, create_vault_key,
    decode_envelope, encode_envelope, seal, unlock, unseal,
)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

PASSPHRASE = b"SYNTHETIC-throwaway-passphrase-Persona-K9"
SECOND_PASSPHRASE = b"SYNTHETIC-second-throwaway-passphrase-Persona-K9"
SYNTHETIC = (b"SYNTHETIC engine test content. Persona-K9. Allergen-X "
             b"placeholder. Corresponds to no real person.")
LIGHT_OPS = nacl.pwhash.argon2id.OPSLIMIT_MIN
LIGHT_MEM = nacl.pwhash.argon2id.MEMLIMIT_MIN


class CustodyCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.envelope = FileStorage(self.ws / "key.envelope")
        self.crypto = PyNaClCrypto()

    def workspace_files(self):
        return sorted(p.name for p in self.ws.rglob("*") if p.is_file())


class TrueModerateProductPath(CustodyCase):
    """End-to-end at the ADR-selected profile. Each derivation is real."""

    def test_create_unlock_and_store_end_to_end(self):
        master = create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        self.assertEqual(self.workspace_files(), ["key.envelope"],
                         "create must write exactly one file")
        blob = self.envelope.read_blob()
        self.assertNotIn(master, blob, "plaintext master in envelope file")
        self.assertNotIn(PASSPHRASE, blob, "passphrase in envelope file")
        env = decode_envelope(blob)
        name, ops, mem = self.crypto.KDF_MODERATE
        self.assertEqual((env["profile"], env["opslimit"], env["memlimit"]),
                         (name, ops, mem),
                         "product path must record the moderate profile")
        before = self.workspace_files()
        unlocked = unlock(self.envelope, self.crypto, PASSPHRASE)
        self.assertEqual(unlocked, master)
        self.assertEqual(self.workspace_files(), before,
                         "unlock must write nothing")
        record = FileStorage(self.ws / "store.bin")
        seal(record, self.crypto, unlocked, SYNTHETIC)
        self.assertEqual(unseal(record, self.crypto, unlocked), SYNTHETIC)

    def test_wrong_passphrase_fails_clean_and_content_free(self):
        master = create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        try:
            unlock(self.envelope, self.crypto, SECOND_PASSPHRASE)
            self.fail("wrong passphrase was accepted")
        except CustodyError as e:
            msg = str(e).encode()
            self.assertNotIn(PASSPHRASE, msg)
            self.assertNotIn(SECOND_PASSPHRASE, msg)
            self.assertNotIn(master, msg)

    def test_passphrase_change_reseals_envelope_only(self):
        master = create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        record = FileStorage(self.ws / "store.bin")
        seal(record, self.crypto, master, SYNTHETIC)
        record_before = record.read_blob()
        envelope_before = self.envelope.read_blob()
        salt_before = decode_envelope(envelope_before)["salt"]

        change_passphrase(self.envelope, self.crypto,
                          PASSPHRASE, SECOND_PASSPHRASE)

        self.assertEqual(record.read_blob(), record_before,
                         "record bytes changed by a custody event")
        envelope_after = self.envelope.read_blob()
        self.assertNotEqual(envelope_after, envelope_before,
                            "envelope must be re-sealed")
        self.assertNotEqual(decode_envelope(envelope_after)["salt"],
                            salt_before, "salt must be fresh on change")
        self.assertEqual(self.workspace_files(),
                         ["key.envelope", "store.bin"],
                         "change must rewrite only the envelope")
        self.assertEqual(
            unlock(self.envelope, self.crypto, SECOND_PASSPHRASE), master,
            "new passphrase must return the same master")
        with self.assertRaises(CustodyError):
            unlock(self.envelope, self.crypto, PASSPHRASE)

    def test_fresh_salt_and_master_per_create(self):
        other = FileStorage(self.ws / "other.envelope")
        m1 = create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        m2 = create_vault_key(other, self.crypto, PASSPHRASE)
        self.assertNotEqual(m1, m2)
        self.assertNotEqual(decode_envelope(self.envelope.read_blob())["salt"],
                            decode_envelope(other.read_blob())["salt"])

    def test_create_refuses_to_overwrite_an_existing_envelope(self):
        create_vault_key(self.envelope, self.crypto, PASSPHRASE)
        blob_before = self.envelope.read_blob()
        with self.assertRaises(CustodyError):
            create_vault_key(self.envelope, self.crypto, SECOND_PASSPHRASE)
        self.assertEqual(self.envelope.read_blob(), blob_before,
                         "refused create must write nothing")


class LightParameterEnvelope(CustodyCase):
    """Parameter-agnostic encoding and the recorded-parameters property,
    at the library's minimum-cost parameters."""

    def light_envelope(self, passphrase, profile="light-test"):
        salt = self.crypto.random_salt()
        kek = self.crypto.derive_key(passphrase, salt, LIGHT_OPS, LIGHT_MEM)
        master = self.crypto.random_key()
        self.envelope.write_blob(encode_envelope(
            profile, LIGHT_OPS, LIGHT_MEM, salt,
            self.crypto.encrypt(kek, master)))
        return master, salt, kek

    def test_recorded_parameters_are_honoured_on_open(self):
        master, _, _ = self.light_envelope(PASSPHRASE)
        self.assertEqual(unlock(self.envelope, self.crypto, PASSPHRASE),
                         master,
                         "unlock must derive with the recorded parameters")

    def test_envelope_records_profile_parameters_and_salt(self):
        _, salt, _ = self.light_envelope(PASSPHRASE)
        env = decode_envelope(self.envelope.read_blob())
        self.assertEqual(env["profile"], "light-test")
        self.assertEqual(env["opslimit"], LIGHT_OPS)
        self.assertEqual(env["memlimit"], LIGHT_MEM)
        self.assertEqual(env["salt"], salt)

    def test_no_secret_bytes_in_envelope_file(self):
        master, _, kek = self.light_envelope(PASSPHRASE)
        blob = self.envelope.read_blob()
        self.assertNotIn(PASSPHRASE, blob)
        self.assertNotIn(master, blob)
        self.assertNotIn(kek, blob)

    def test_unknown_envelope_version_is_refused(self):
        self.light_envelope(PASSPHRASE)
        blob = bytearray(self.envelope.read_blob())
        blob[4:6] = (9).to_bytes(2, "big")
        with self.assertRaises(EnvelopeError):
            decode_envelope(bytes(blob))

    def test_malformed_envelopes_are_refused(self):
        self.light_envelope(PASSPHRASE)
        good = self.envelope.read_blob()
        for name, bad in {"truncated": good[:-3],
                          "trailing bytes": good + b"x",
                          "too short": good[:8],
                          "bad magic": b"NOPE" + good[4:]}.items():
            with self.subTest(case=name):
                with self.assertRaises(EnvelopeError):
                    decode_envelope(bad)


class CustodyResidue(unittest.TestCase):
    """ADR 0004 on the derivation and envelope paths: however the
    process ends, only the intended files remain."""

    def _workspace_files(self, ws):
        return sorted(p.name for p in Path(ws).rglob("*") if p.is_file())

    def test_normal_termination_leaves_only_envelope_and_record(self):
        with tempfile.TemporaryDirectory() as ws:
            envelope = FileStorage(Path(ws) / "key.envelope")
            crypto = PyNaClCrypto()
            master = create_vault_key(envelope, crypto, PASSPHRASE)
            master = unlock(envelope, crypto, PASSPHRASE)
            record = FileStorage(Path(ws) / "store.bin")
            seal(record, crypto, master, SYNTHETIC)
            self.assertEqual(self._workspace_files(ws),
                             ["key.envelope", "store.bin"])

    def test_kill_termination_leaves_only_the_envelope(self):
        with tempfile.TemporaryDirectory() as ws:
            script = (
                "import sys, time; sys.path.insert(0, sys.argv[1]);"
                "from engine.core import create_vault_key;"
                "from engine.ports import FileStorage, PyNaClCrypto;"
                "create_vault_key(FileStorage(sys.argv[2] + '/key.envelope'),"
                " PyNaClCrypto(),"
                " b'SYNTHETIC-throwaway-passphrase-Persona-K9');"
                "print('created', flush=True); time.sleep(30)"
            )
            p = subprocess.Popen(
                [sys.executable, "-c", script, str(ROOT), ws],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ws)
            try:
                line = p.stdout.readline()
                self.assertIn(b"created", line)
            finally:
                p.kill()
                p.wait()
                p.stdout.close()
                p.stderr.close()
            self.assertEqual(self._workspace_files(ws), ["key.envelope"])


if __name__ == "__main__":
    unittest.main()
