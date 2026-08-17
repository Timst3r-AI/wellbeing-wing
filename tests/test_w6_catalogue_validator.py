"""W6 — the catalogue-ID validator, woken at the W6-D2-C+D landing.

This is the wake of the dormant catalogue-ID validator class, by record:
it implements the thirteen ADR-0042 Part F obligations and the ADR-0045
validation specification against the real populated catalogue at
`governance/string-catalogue.json`, in the same commit that created it.

Boundary: this validator checks shape, vocabulary, metadata, lifecycle
and registry integrity only. A green run means the register conforms to
its accepted schema and law — never that any string is graded, approved,
renderable, or fit for display. Catalogue membership is necessary where
later law requires it, never sufficient for display, and no validator
result authorises anything.

Named mechanical exception (the ADR-0037 decision 11 pattern): the
barred word "passed" appears lawfully inside exactly two source
collocations quoted verbatim from the W1-D3 freshness ladder — "review
interval has passed" and "renewal grace period has passed" — temporal
statements about intervals, never claims that anything passed a test.
"""

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE_PATH = ROOT / "governance" / "string-catalogue.json"
REGISTRY_PATH = ROOT / "governance" / "registry.json"

TOP_KEYS = ["catalogue_version", "status", "governance_note", "entries"]
ENTRY_KEYS = ["id", "string", "vocabulary_class", "source_authority",
              "derivation_reference", "accompaniment_linkage",
              "prohibition_register", "source_citation_requirement",
              "supersession_retirement_posture", "proof_obligations",
              "display_authorisation_statement"]
CLASSES = {"source_state_label", "derived_presentation_label",
           "routing_label", "non_authority_label", "review_label",
           "prohibition_label", "future_owned_label"}
OBLIGATION_TOKENS = ["barred_word_check", "class_check",
                     "derivation_check", "accompaniment_check",
                     "source_check", "lifecycle_check",
                     "no_display_authorisation_check"]
CEILING = ("catalogue membership is necessary where later law requires "
           "it, never sufficient for display; entry presence, id "
           "presence, registry hash, and validator results do not "
           "authorise display")
ID_RE = re.compile(r"^CAT-\d{4}$")
CITATION_RE = re.compile(r"^(ADR-\d{4}|W\d-D\d|W\d-AR|W0)")
BARRED_WORDS = ["passed", "safe", "unsafe", "readiness", "diagnosis",
                "therapy", "failed"]
BARRED_PHRASES = ["clinically safe", "medically safe",
                  "legally satisfied", "production-ready",
                  "approved by the system", "validated as correct",
                  "behaviourally proven", "proof of safety",
                  "treatment advice", "all-green status",
                  "success verdict"]
BARRED_STEMS = ["certif", "complian"]
LAWFUL_PASSED = ["review interval has passed",
                 "renewal grace period has passed"]


def catalogue():
    return json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))


def entries():
    return catalogue()["entries"]


class FileAndTopLevel(unittest.TestCase):
    def test_file_exists_and_parses_deterministically(self):
        self.assertTrue(CATALOGUE_PATH.exists())
        data = catalogue()
        self.assertIsInstance(data, dict)

    def test_top_level_keys_exact_and_in_canonical_order(self):
        self.assertEqual(list(catalogue().keys()), TOP_KEYS)

    def test_status_value(self):
        self.assertEqual(catalogue()["status"],
                         "governed_register_active")

    def test_entries_is_a_list(self):
        self.assertIsInstance(entries(), list)


class EntryShape(unittest.TestCase):
    def test_entry_keys_exact_order_no_extra_no_missing(self):
        for e in entries():
            self.assertEqual(list(e.keys()), ENTRY_KEYS, e.get("id"))

    def test_nullability_exactly_as_adr_0045(self):
        nullable = {"derivation_reference", "prohibition_register"}
        for e in entries():
            for key in ENTRY_KEYS:
                if e[key] is None:
                    self.assertIn(key, nullable, e["id"])

    def test_id_grammar_uniqueness_no_reuse_and_sort_order(self):
        ids = [e["id"] for e in entries()]
        for i in ids:
            self.assertRegex(i, ID_RE)
        self.assertEqual(len(set(ids)), len(ids), "no duplicate ids")
        self.assertEqual(ids, sorted(ids), "entries sorted by id")

    def test_no_meaning_encoded_in_ids(self):
        # flat numeric allocation only: strip CAT- and require digits
        for e in entries():
            suffix = e["id"][4:]
            self.assertTrue(suffix.isdigit(), e["id"])


class VocabularyAndSources(unittest.TestCase):
    def test_class_within_closed_seven_value_set(self):
        for e in entries():
            self.assertIn(e["vocabulary_class"], CLASSES, e["id"])

    def test_source_authority_non_empty_citation_shaped(self):
        for e in entries():
            self.assertIsInstance(e["source_authority"], list)
            self.assertTrue(e["source_authority"], e["id"])
            for cite in e["source_authority"]:
                self.assertRegex(cite, CITATION_RE)

    def test_derivation_reference_rules(self):
        for e in entries():
            ref = e["derivation_reference"]
            if e["vocabulary_class"] == "derived_presentation_label":
                self.assertIsInstance(ref, str, e["id"])
                self.assertRegex(ref, CITATION_RE)
            if ref is not None:
                self.assertIn("derivation_check",
                              e["proof_obligations"], e["id"])

    def test_accompaniment_linkage_rules(self):
        for e in entries():
            linkage = e["accompaniment_linkage"]
            self.assertIsInstance(linkage, list)
            for cite in linkage:
                self.assertRegex(cite, CITATION_RE)
            has_check = "accompaniment_check" in e["proof_obligations"]
            self.assertEqual(bool(linkage), has_check,
                             e["id"] + ": accompaniment_check must "
                             "match linkage presence")


class BarredWordingGate(unittest.TestCase):
    def _lawful_text(self, entry):
        text = entry["string"].lower()
        if entry["prohibition_register"] is None:
            for coll in LAWFUL_PASSED:
                text = text.replace(coll, " ")
        return text

    def test_barred_words_absent_outside_prohibition_register(self):
        for e in entries():
            if e["prohibition_register"] is not None:
                self.assertIn("basis", e["prohibition_register"])
                continue
            text = self._lawful_text(e)
            for word in BARRED_WORDS:
                self.assertIsNone(
                    re.search(r"\b%s\b" % word, text), (e["id"], word))
            for phrase in BARRED_PHRASES:
                self.assertNotIn(phrase, text, e["id"])
            for stem in BARRED_STEMS:
                self.assertNotIn(stem, text, e["id"])

    def test_named_passed_exception_is_exactly_bounded(self):
        # every raw occurrence of "passed" sits inside a named
        # collocation — the exception cannot widen silently
        for e in entries():
            raw = e["string"].lower()
            occurrences = len(re.findall(r"\bpassed\b", raw))
            covered = sum(raw.count(c) for c in LAWFUL_PASSED)
            self.assertEqual(occurrences, covered, e["id"])


class LifecycleAndObligations(unittest.TestCase):
    def test_lifecycle_object_grammar(self):
        for e in entries():
            posture = e["supersession_retirement_posture"]
            self.assertIn(posture["state"],
                          ("active", "superseded", "retired"), e["id"])
            if posture["state"] == "superseded":
                self.assertIn("by", posture)
                self.assertIn("record", posture)
            if posture["state"] == "retired":
                self.assertIn("record", posture)

    def test_proof_obligations_closed_set_non_empty_canonical_order(self):
        for e in entries():
            tokens = e["proof_obligations"]
            self.assertTrue(tokens, e["id"])
            self.assertTrue(set(tokens) <= set(OBLIGATION_TOKENS),
                            e["id"])
            order = [OBLIGATION_TOKENS.index(t) for t in tokens]
            self.assertEqual(order, sorted(order), e["id"])

    def test_source_citation_requirement_values(self):
        for e in entries():
            self.assertIn(e["source_citation_requirement"],
                          ("required", "not_required"), e["id"])


class CeilingAndAuthority(unittest.TestCase):
    def test_ceiling_sentence_byte_identical_in_every_entry(self):
        for e in entries():
            self.assertEqual(e["display_authorisation_statement"],
                             CEILING, e["id"])

    def test_governance_note_carries_the_identity_law(self):
        note = catalogue()["governance_note"]
        self.assertIn("never a source of authority", note)
        self.assertIn("never sufficient for display", note)

    def test_no_display_authorisation_claim_anywhere(self):
        text = CATALOGUE_PATH.read_text(encoding="utf-8").lower()
        for claim in ("authorises display", "authorized for display",
                      "approved for display", "display permitted",
                      "renderable"):
            self.assertNotIn(claim, text)


class RegistryIntegrity(unittest.TestCase):
    def test_catalogue_registered_with_exact_hash(self):
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        matches = [e for e in registry["entries"]
                   if e["path"] == "governance/string-catalogue.json"]
        self.assertEqual(len(matches), 1)
        raw = CATALOGUE_PATH.read_bytes().replace(b"\r\n", b"\n").replace(
            b"\r", b"\n")
        self.assertEqual(matches[0]["content_hash"],
                         "sha256:" + hashlib.sha256(raw).hexdigest())

    def test_seed_corpus_cardinality(self):
        self.assertEqual(len(entries()), 33)
        by_source = {}
        for e in entries():
            key = e["source_authority"][0].split(" ")[0]
            by_source[key] = by_source.get(key, 0) + 1
        self.assertEqual(by_source,
                         {"W4-D2": 11, "W4-D3": 11, "W4-D4": 11})


if __name__ == "__main__":
    unittest.main()
