"""W3-D3 milestone 1 - profile object model tests.

The grammar as construction rules: every legal shape constructs,
every illegal state refuses. Synthetic grammar placeholders only.
Staleness intervals in these tests are synthetic numbers proving
behaviour; they are not clinical values and the product code holds
no defaults, by decision.
"""

import inspect
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    AGENT_ASSIGNABLE_LABELS, AUTHORITY_LABELS, STALENESS_DECAY_ORDER,
    STALENESS_LABELS, TRUTH_LABELS, BoundedUnknown, Contradiction,
    LedgerEvent, ProfileItem, ProfileModelError, ProvenanceRef,
    Supersession, staleness_of,
)
from engine.core.profile import ApprovedProfile  # noqa: E402

GRAMMAR = json.loads(
    (ROOT / "tests" / "grammar" / "d3-transitions.json")
    .read_text(encoding="utf-8"))

SYNTHETIC_INTERVALS = {"review due": 10, "stale": 20, "expired": 40}


def user_reported(section="Condition-Q", content="SYNTHETIC note, Persona-K9"):
    return ProfileItem(section, content, "user-reported",
                       "system-on-user-entry", "unknown freshness")


def confirmed_by_user(section="Allergen-X status"):
    return ProfileItem(
        section, "SYNTHETIC statement, Persona-K9", "confirmed by user",
        "user-review", "current", last_reviewed="2026-01-01T00:00:00+00:00",
        provenance=ProvenanceRef("user-statement", "SYNTHETIC-statement-1"))


class GrammarAlignment(unittest.TestCase):
    """The model's vocabulary matches the Tier 2 transcription
    (which itself matches the source document, which wins)."""

    def test_label_sets_match_the_transcription(self):
        self.assertEqual(TRUTH_LABELS, set(GRAMMAR["truth_labels"]))
        self.assertEqual(AGENT_ASSIGNABLE_LABELS,
                         set(GRAMMAR["agent_assignable_labels"]))
        self.assertEqual(list(STALENESS_DECAY_ORDER),
                         GRAMMAR["staleness_order"])
        self.assertTrue(set(GRAMMAR["terminal_states"]) <= STALENESS_LABELS)


class LegalConstruction(unittest.TestCase):
    def test_valid_user_reported_item_constructs(self):
        item = user_reported()
        self.assertEqual(item.authority, "user-reported")
        self.assertEqual(item.staleness, "unknown freshness")

    def test_valid_confirmed_shapes_construct_with_review_provenance(self):
        # Shape validation only: no review path exists in this
        # milestone; these values are synthetic test constructions.
        by_user = confirmed_by_user()
        self.assertEqual(by_user.provenance.kind, "user-statement")
        by_record = ProfileItem(
            "Medication-A17", "SYNTHETIC extract", "confirmed by record",
            "user-review", "current",
            last_reviewed="2026-01-01T00:00:00+00:00",
            provenance=ProvenanceRef("vault-record", "SYNTHETIC-record-7"))
        self.assertEqual(by_record.provenance.kind, "vault-record")


class IllegalConstruction(unittest.TestCase):
    def test_item_without_authority_label_refuses(self):
        for bad in (None, "", "settled truth"):
            with self.subTest(authority=bad):
                with self.assertRaises(ProfileModelError):
                    ProfileItem("Condition-Q", "SYNTHETIC", bad,
                                "user-review", "current")

    def test_item_without_staleness_label_refuses(self):
        for bad in (None, "", "fresh"):
            with self.subTest(staleness=bad):
                with self.assertRaises(ProfileModelError):
                    ProfileItem("Condition-Q", "SYNTHETIC", "user-reported",
                                "system-on-user-entry", bad)

    def test_agent_path_to_confirmed_labels_refuses(self):
        for label in sorted(TRUTH_LABELS):
            for actor in ("agent", "system", "system-on-user-entry"):
                with self.subTest(label=label, actor=actor):
                    with self.assertRaises(ProfileModelError):
                        ProfileItem(
                            "Condition-Q", "SYNTHETIC", label, actor,
                            "current",
                            last_reviewed="2026-01-01T00:00:00+00:00",
                            provenance=ProvenanceRef(
                                "user-statement", "SYNTHETIC-1"))

    def test_confirmed_item_without_review_provenance_refuses(self):
        with self.assertRaises(ProfileModelError):
            ProfileItem("Condition-Q", "SYNTHETIC", "confirmed by user",
                        "user-review", "current",
                        last_reviewed="2026-01-01T00:00:00+00:00")
        with self.assertRaises(ProfileModelError):  # wrong provenance kind
            ProfileItem("Condition-Q", "SYNTHETIC", "confirmed by user",
                        "user-review", "current",
                        last_reviewed="2026-01-01T00:00:00+00:00",
                        provenance=ProvenanceRef("vault-record",
                                                 "SYNTHETIC-record-1"))
        with self.assertRaises(ProfileModelError):  # no review timestamp
            ProfileItem("Condition-Q", "SYNTHETIC", "confirmed by user",
                        "user-review", "current",
                        provenance=ProvenanceRef("user-statement",
                                                 "SYNTHETIC-1"))


class UnknownsAreBounded(unittest.TestCase):
    def test_bounded_unknown_constructs_with_all_three_bounds(self):
        u = BoundedUnknown("Allergen-X status",
                           ("SYNTHETIC-record-1", "SYNTHETIC-record-2"),
                           "2026-01-01T00:00:00+00:00")
        self.assertEqual(u.scope, "Allergen-X status")
        self.assertEqual(len(u.source_set), 2)

    def test_unbounded_unknown_refuses(self):
        good = ("scope", ("src",), "2026-01-01T00:00:00+00:00")
        for i, name in enumerate(("scope", "source set", "as-of")):
            bad = list(good)
            bad[i] = None
            with self.subTest(missing=name):
                with self.assertRaises(ProfileModelError):
                    BoundedUnknown(*bad)


class DisagreementAndHistory(unittest.TestCase):
    def test_contradiction_holds_both_sides_with_dates(self):
        first = confirmed_by_user()
        second = user_reported(section="Allergen-X status")
        c = Contradiction(first, second, "2026-02-01T00:00:00+00:00")
        self.assertIs(c.first, first)
        self.assertIs(c.second, second)
        self.assertTrue(c.detected_at)
        with self.assertRaises(ProfileModelError):
            Contradiction(first, None, "2026-02-01T00:00:00+00:00")

    def test_supersession_preserves_predecessor_and_successor(self):
        old = confirmed_by_user()
        new = confirmed_by_user()
        s = Supersession(old, new, "2026-03-01T00:00:00+00:00")
        self.assertIs(s.predecessor, old)
        self.assertIs(s.successor, new)
        with self.assertRaises(ProfileModelError):
            Supersession(old, None, "2026-03-01T00:00:00+00:00")


class StalenessDecay(unittest.TestCase):
    def test_decay_is_deterministic_with_injected_intervals(self):
        cases = {0: "current", 9: "current", 10: "review due",
                 19: "review due", 20: "stale", 39: "stale",
                 40: "expired", 400: "expired"}
        for elapsed, expected in cases.items():
            with self.subTest(elapsed=elapsed):
                self.assertEqual(
                    staleness_of(elapsed, SYNTHETIC_INTERVALS), expected)

    def test_decay_is_monotonic_downward_only(self):
        order = {label: i for i, label in enumerate(STALENESS_DECAY_ORDER)}
        previous = 0
        for elapsed in range(0, 60):
            stage = order[staleness_of(elapsed, SYNTHETIC_INTERVALS)]
            self.assertGreaterEqual(
                stage, previous,
                "time passing may never raise warmth")
            previous = stage

    def test_no_default_intervals_exist(self):
        param = inspect.signature(staleness_of).parameters["intervals"]
        self.assertIs(param.default, inspect.Parameter.empty,
                      "intervals must be injected, never defaulted")
        with self.assertRaises(ProfileModelError):
            staleness_of(5, None)
        with self.assertRaises(ProfileModelError):
            staleness_of(5, {"review due": 10, "stale": 5, "expired": 40})
        with self.assertRaises(ProfileModelError):
            staleness_of(5, {"review due": 10})

    def test_module_holds_no_interval_constants(self):
        source = (ROOT / "engine" / "core" / "profile.py").read_text(
            encoding="utf-8")
        for token in ("86400", "3600", "days", "months", "weeks"):
            self.assertNotIn(token, source,
                             "interval-like constant in product code")


class ApprovedLayerShape(unittest.TestCase):
    def test_shape_accepts_only_truth_label_items(self):
        profile = ApprovedProfile(
            {"Allergen-X status": [confirmed_by_user()]})
        self.assertEqual(len(profile.sections["Allergen-X status"]), 1)

    def test_shape_refuses_anything_below_the_truth_labels(self):
        with self.assertRaises(ProfileModelError):
            ApprovedProfile({"Condition-Q": [user_reported()]})
        agent_item = ProfileItem(
            "Condition-Q", "SYNTHETIC", "agent-extracted, pending review",
            "agent", "unknown freshness")
        with self.assertRaises(ProfileModelError):
            ApprovedProfile({"Condition-Q": [agent_item]})


class LedgerEventShape(unittest.TestCase):
    def test_event_is_data_only_and_mutates_nothing(self):
        item = confirmed_by_user()
        before = dict(vars(item))
        event = LedgerEvent("SYNTHETIC-transition-flag",
                            [item.section], "2026-01-02T00:00:00+00:00")
        self.assertEqual(dict(vars(item)), before,
                         "event construction mutated an item")
        self.assertEqual(vars(event),
                         {"kind": "SYNTHETIC-transition-flag",
                          "refs": ("Allergen-X status",),
                          "recorded_at": "2026-01-02T00:00:00+00:00"},
                         "event holds exactly its identifiers and time")

    def test_event_requires_kind_and_time(self):
        with self.assertRaises(ProfileModelError):
            LedgerEvent("", ["ref"], "2026-01-02T00:00:00+00:00")
        with self.assertRaises(ProfileModelError):
            LedgerEvent("kind", ["ref"], None)


if __name__ == "__main__":
    unittest.main()
