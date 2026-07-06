"""W3-D3 milestone 2 - sealed profile persistence tests.

Synthetic grammar placeholders only. The two guards under test:
truth-label items refuse to persist (the minimal-review-posture
record enforced at the only write path), and illegal persisted
states refuse at load (the constructors gate the way out too).
Failure output never prints content or key material.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    PROFILE_PAYLOAD_VERSION, BoundedUnknown, ProfileItem, ProfileModelError,
    ProfileRecordError, ProvenanceRef, StoreIntegrityError, decode_record,
    encode_record, import_record, load_item, load_unknown, persist_item,
    persist_unknown, seal,
)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

MARKER = "SYNTHETIC-PROFILE-MARKER-Persona-K9-Allergen-X"


class FixedClock:
    def now_iso(self) -> str:
        return "2026-01-01T00:00:00+00:00"


def draft_item(content=MARKER + " observed placeholder note"):
    return ProfileItem(
        "Allergen-X status", content, "agent-extracted, pending review",
        "agent", "unknown freshness",
        provenance=ProvenanceRef("vault-record", "SYNTHETIC-record-7",
                                 stated_at="2026-01-01T00:00:00+00:00"))


def confirmed_item(label="confirmed by user"):
    kind = "user-statement" if label == "confirmed by user" else "vault-record"
    return ProfileItem(
        "Allergen-X status", MARKER + " confirmed placeholder", label,
        "user-review", "current", last_reviewed="2026-01-01T00:00:00+00:00",
        provenance=ProvenanceRef(kind, "SYNTHETIC-ref-1"))


class ProfileRecordCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ws = Path(self.tmp.name)
        self.storage = FileStorage(self.ws / "profile-000.bin")
        self.crypto = PyNaClCrypto()
        self.key = self.crypto.random_key()

    def files(self):
        return sorted(p.name for p in self.ws.rglob("*") if p.is_file())


class RoundtripFidelity(ProfileRecordCase):
    def test_profile_item_roundtrip(self):
        item = draft_item()
        persist_item(self.storage, self.crypto, self.key, item)
        self.assertEqual(self.files(), ["profile-000.bin"])
        loaded = load_item(self.storage, self.crypto, self.key)
        for name in ("section", "content", "authority", "assigned_by",
                     "staleness", "last_reviewed"):
            self.assertEqual(getattr(loaded, name), getattr(item, name), name)

    def test_provenance_reference_survives_roundtrip(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        loaded = load_item(self.storage, self.crypto, self.key)
        self.assertEqual(loaded.provenance.kind, "vault-record")
        self.assertEqual(loaded.provenance.reference, "SYNTHETIC-record-7")
        self.assertEqual(loaded.provenance.stated_at,
                         "2026-01-01T00:00:00+00:00")

    def test_bounded_unknown_roundtrip(self):
        unknown = BoundedUnknown(
            "Allergen-X status", ("SYNTHETIC-record-1", "SYNTHETIC-record-2"),
            "2026-01-01T00:00:00+00:00")
        persist_unknown(self.storage, self.crypto, self.key, unknown)
        loaded = load_unknown(self.storage, self.crypto, self.key)
        self.assertEqual(loaded.scope, unknown.scope)
        self.assertEqual(loaded.source_set, unknown.source_set)
        self.assertEqual(loaded.as_of, unknown.as_of)


class SelfDeclaration(ProfileRecordCase):
    def test_profile_record_declares_itself_in_record_provenance(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        blob = self.crypto.decrypt(self.key, self.storage.read_blob()[16:])
        provenance, _ = decode_record(blob)
        self.assertEqual(provenance,
                         {"record_class": "profile-item",
                          "profile_payload_version": PROFILE_PAYLOAD_VERSION})

    def test_evidence_record_is_unchanged_and_has_no_record_class(self):
        evidence = FileStorage(self.ws / "evidence.bin")
        import_record(evidence, self.crypto, FixedClock(), self.key,
                      b"SYNTHETIC evidence bytes, Persona-K9", "text",
                      source="SYNTHETIC source")
        blob = self.crypto.decrypt(self.key, evidence.read_blob()[16:])
        provenance, _ = decode_record(blob)
        self.assertEqual(set(provenance),
                         {"user", "unprovenanced_by_user", "system"},
                         "published evidence schema changed")
        self.assertNotIn("record_class", provenance)

    def test_evidence_fed_to_profile_loader_refuses(self):
        evidence = FileStorage(self.ws / "evidence.bin")
        import_record(evidence, self.crypto, FixedClock(), self.key,
                      b"SYNTHETIC evidence bytes, Persona-K9", "text",
                      source="SYNTHETIC source")
        with self.assertRaises(ProfileRecordError):
            load_item(evidence, self.crypto, self.key)

    def test_record_classes_refuse_each_other(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        with self.assertRaises(ProfileRecordError):
            load_unknown(self.storage, self.crypto, self.key)
        other = FileStorage(self.ws / "unknown.bin")
        persist_unknown(other, self.crypto, self.key, BoundedUnknown(
            "scope", ("src",), "2026-01-01T00:00:00+00:00"))
        with self.assertRaises(ProfileRecordError):
            load_item(other, self.crypto, self.key)


class TruthLabelRefusal(ProfileRecordCase):
    def test_truth_labels_refuse_to_persist_and_write_nothing(self):
        for label in ("confirmed by user", "confirmed by record"):
            with self.subTest(label=label):
                try:
                    persist_item(self.storage, self.crypto, self.key,
                                 confirmed_item(label))
                    self.fail("a confirmed item was persisted")
                except ProfileRecordError as e:
                    self.assertNotIn(MARKER, str(e))
                self.assertFalse(self.storage.exists())
        self.assertEqual(self.files(), [], "refusal must write nothing")


class ContentDiscipline(ProfileRecordCase):
    def test_non_string_content_refuses_and_writes_nothing(self):
        for bad in (b"SYNTHETIC bytes", 7, {"note": "SYNTHETIC"}):
            with self.subTest(content=type(bad).__name__):
                item = ProfileItem("Condition-Q", bad, "user-reported",
                                   "system-on-user-entry", "unknown freshness")
                with self.assertRaises(ProfileRecordError):
                    persist_item(self.storage, self.crypto, self.key, item)
        self.assertEqual(self.files(), [])


class PayloadRefusals(ProfileRecordCase):
    def _seal_raw(self, provenance, body_bytes):
        seal(self.storage, self.crypto, self.key,
             encode_record(provenance, body_bytes))

    def _profile_prov(self):
        return {"record_class": "profile-item",
                "profile_payload_version": PROFILE_PAYLOAD_VERSION}

    def test_illegal_persisted_state_refuses_at_load(self):
        payload = {"profile_payload_version": 1, "kind": "profile-item",
                   "section": "Condition-Q", "content": "SYNTHETIC",
                   "authority": "confirmed by user", "assigned_by": "agent",
                   "staleness": "current", "last_reviewed": None,
                   "provenance": None}
        self._seal_raw(self._profile_prov(),
                       json.dumps(payload).encode("utf-8"))
        with self.assertRaises(ProfileModelError):
            load_item(self.storage, self.crypto, self.key)

    def test_unknown_payload_version_refuses(self):
        payload = {"profile_payload_version": 9, "kind": "profile-item"}
        self._seal_raw(self._profile_prov(),
                       json.dumps(payload).encode("utf-8"))
        with self.assertRaises(ProfileRecordError):
            load_item(self.storage, self.crypto, self.key)

    def test_malformed_payload_matrix_refuses(self):
        good = {"profile_payload_version": 1, "kind": "profile-item",
                "section": "Condition-Q", "content": "SYNTHETIC",
                "authority": "user-reported",
                "assigned_by": "system-on-user-entry",
                "staleness": "unknown freshness", "last_reviewed": None,
                "provenance": None}
        missing = dict(good)
        del missing["staleness"]
        cases = {
            "unreadable bytes": b"\xff\xfenot json",
            "trailing bytes": json.dumps(good).encode("utf-8") + b"x",
            "wrong kind": json.dumps(
                dict(good, kind="bounded-unknown")).encode("utf-8"),
            "missing field": json.dumps(missing).encode("utf-8"),
        }
        for name, body in cases.items():
            with self.subTest(case=name):
                storage = FileStorage(self.ws / f"bad-{len(name)}.bin")
                seal(storage, self.crypto, self.key,
                     encode_record(self._profile_prov(), body))
                with self.assertRaises(ProfileRecordError):
                    load_item(storage, self.crypto, self.key)


class SealDiscipline(ProfileRecordCase):
    def test_wrong_key_fails_clean_and_content_free(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        try:
            load_item(self.storage, self.crypto, self.crypto.random_key())
            self.fail("wrong key was accepted")
        except StoreIntegrityError as e:
            self.assertNotIn(MARKER, str(e))

    def test_corrupted_record_fails_clean_and_content_free(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        blob = bytearray(self.storage.read_blob())
        blob[-1] ^= 0xFF
        self.storage.write_blob(bytes(blob))
        try:
            load_item(self.storage, self.crypto, self.key)
            self.fail("corrupted record was accepted")
        except StoreIntegrityError as e:
            self.assertNotIn(MARKER, str(e))

    def test_profile_plaintext_never_on_disk(self):
        persist_item(self.storage, self.crypto, self.key, draft_item())
        persist_unknown(FileStorage(self.ws / "unknown.bin"), self.crypto,
                        self.key, BoundedUnknown(
                            MARKER + " scope", ("src",),
                            "2026-01-01T00:00:00+00:00"))
        for f in self.ws.rglob("*"):
            if f.is_file():
                self.assertNotIn(MARKER.encode(), f.read_bytes(),
                                 f"profile plaintext on disk: {f.name}")
        self.assertEqual(self.files(), ["profile-000.bin", "unknown.bin"])


if __name__ == "__main__":
    unittest.main()
