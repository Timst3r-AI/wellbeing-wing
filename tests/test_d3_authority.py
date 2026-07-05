"""Tier 2 — D3 authority and staleness grammar against synthetic fixtures.

Validator authority rule: conformance checks only; not doctrine; a
conflict with the source document is a validator defect; no runtime
reuse without future-phase review.

Grader-calibration note (W1-D6 §3.5): no assertion in this module
penalises a correct "unknown". where the grammar says unknown is the
required answer, unknown asserted as required is the passing outcome.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR = json.loads((ROOT / "tests" / "grammar" / "d3-transitions.json").read_text(encoding="utf-8"))
LADDER = json.loads((ROOT / "fixtures" / "SYNTHETIC-d3-staleness-ladder.json").read_text(encoding="utf-8"))
CONFLICTS = json.loads((ROOT / "fixtures" / "SYNTHETIC-d3-authority-conflicts.json").read_text(encoding="utf-8"))

ORDER = GRAMMAR["staleness_order"]
AGENT_FORBIDDEN = set(GRAMMAR["agent_forbidden_transitions"])


def transition_allowed(transition_id, actor):
    """Conformance check: agents never perform the user-only
    transitions; nothing outside the transcribed table exists."""
    if transition_id not in GRAMMAR["transitions"]:
        return False
    if actor == "agent" and transition_id in AGENT_FORBIDDEN:
        return False
    return True


def decay_path_valid(path):
    """Conformance check: staleness moves strictly downward in trust."""
    idx = [ORDER.index(s) for s in path]
    return all(b > a for a, b in zip(idx, idx[1:]))


def label_assignable_by_agent(label):
    return label in GRAMMAR["agent_assignable_labels"]


def served_as(staleness_label):
    return GRAMMAR["treated_as"].get(staleness_label, "as-labelled")


class StalenessLadder(unittest.TestCase):
    def test_ladder_walk_is_monotonic_decay(self):
        case = next(c for c in LADDER["transition_cases"]
                    if c["case"] == "decay-only-direction")
        self.assertTrue(decay_path_valid(case["path"]))
        self.assertEqual(case["path"], ORDER)

    def test_no_automatic_promotion(self):
        self.assertFalse(decay_path_valid(["expired", "current"]),
                         "time moved an item toward more trust")
        self.assertTrue(GRAMMAR["rules"]["automatic_transitions_only_lower_trust"])

    def test_expired_is_served_as_unknown(self):
        self.assertEqual(served_as("expired"), "unknown")
        case = next(c for c in LADDER["ladder_cases"] if c["case"] == "state-expired")
        self.assertIn("unknown", case["expected_working_use"])

    def test_unknown_freshness_is_treated_as_stale(self):
        self.assertEqual(served_as("unknown freshness"), "stale")

    def test_agent_refresh_is_refused(self):
        self.assertTrue(GRAMMAR["rules"]["renewal_is_a_review_act_not_a_refresh"])
        case = next(c for c in LADDER["transition_cases"]
                    if c["case"] == "agent-refresh-refused")
        self.assertIn("refused", case["expected"])

    def test_every_ladder_state_has_a_fixture_case(self):
        states = {c["staleness_label"] for c in LADDER["ladder_cases"]}
        for s in ORDER + GRAMMAR["terminal_states"] + ["unknown freshness"]:
            self.assertIn(s, states, f"no fixture case for staleness state: {s}")


class ProhibitedTransitions(unittest.TestCase):
    def test_agents_cannot_perform_user_only_transitions(self):
        for case in CONFLICTS["prohibited_transition_cases"]:
            if "transition" not in case:
                continue
            self.assertFalse(transition_allowed(case["transition"], "agent"),
                             f"{case['case']}: agent performed {case['transition']}")

    def test_unlisted_transitions_do_not_exist(self):
        self.assertFalse(transition_allowed("D3-T9", "user"),
                         "a transition not listed must not exist")

    def test_agent_cannot_assign_truth_labels(self):
        for label in GRAMMAR["truth_labels"]:
            self.assertFalse(label_assignable_by_agent(label),
                             f"agent assigned truth label: {label}")
        for label in GRAMMAR["agent_assignable_labels"]:
            self.assertTrue(label_assignable_by_agent(label))

    def test_model_output_is_never_evidence(self):
        self.assertFalse(GRAMMAR["rules"]["model_output_is_evidence"])
        case = next(c for c in CONFLICTS["prohibited_transition_cases"]
                    if c["case"] == "chained-output-as-evidence")
        self.assertIn("suggestion", case["expected"])


class Contradictions(unittest.TestCase):
    def test_contradicted_items_suspend_visibly_never_hidden(self):
        self.assertEqual(GRAMMAR["treated_as"]["contradicted"],
                         "suspended-from-settled-truth-use-visible")
        for case in CONFLICTS["contradiction_cases"]:
            expected = case["expected"]
            if case["case"] == "suspension-not-hidden":
                self.assertIn("remain-visible", expected.replace(" ", "-"))
            else:
                # visible or surfaced: both sides remain in view, never hidden
                self.assertTrue("visible" in expected or "surfaced" in expected,
                                f"{case['case']}: expectation shows neither side kept in view")
                self.assertNotIn("auto-resolve", expected)

    def test_neither_side_auto_wins(self):
        case = next(c for c in CONFLICTS["contradiction_cases"]
                    if c["case"] == "user-vs-record")
        self.assertIn("neither auto-wins", case["expected"])
        self.assertIn("user decides", case["expected"])


class UnknownVersusNegative(unittest.TestCase):
    def test_bounded_unknown_carries_scope_source_set_and_as_of(self):
        case = next(c for c in CONFLICTS["unknown_vs_negative_cases"]
                    if c["case"] == "bounded-unknown")
        for field in GRAMMAR["rules"]["bounded_unknown_requires"]:
            self.assertIn(field, case["item"],
                          f"bounded unknown missing required bound: {field}")

    def test_absence_never_becomes_a_negative_claim(self):
        self.assertFalse(GRAMMAR["rules"]["absence_is_negative_evidence"])
        case = next(c for c in CONFLICTS["unknown_vs_negative_cases"]
                    if c["case"] == "silence-is-not-absence")
        self.assertIn("refused", case["expected"])

    def test_confirmed_negative_is_distinct_and_usable(self):
        case = next(c for c in CONFLICTS["unknown_vs_negative_cases"]
                    if c["case"] == "confirmed-negative")
        self.assertIn(case["item"]["authority_label"], GRAMMAR["truth_labels"])
        self.assertIn("usable", case["expected"])


class RepetitionAndUserAuthority(unittest.TestCase):
    def test_repetition_never_promotes(self):
        self.assertFalse(GRAMMAR["rules"]["repetition_promotes_authority"])
        case = CONFLICTS["repetition_cases"][0]
        self.assertGreaterEqual(len(case["events"]), 3)
        self.assertIn("user-reported", case["expected"])
        self.assertIn("frequency is not evidence", case["expected"])

    def test_user_entry_and_correction_transitions_are_allowed(self):
        self.assertTrue(transition_allowed("D3-T3", "system-on-user-entry"))
        self.assertTrue(transition_allowed("D3-T7", "user"))
        self.assertTrue(GRAMMAR["rules"]["only_the_user_mints_truth"])


if __name__ == "__main__":
    unittest.main()
