"""W3-D4 milestone 1 - transition catalogue, matrix, and validator tests.

The whitelist proven by enumeration, not sampling: the exhaustive
sweep classifies every constructible proposal and asserts the
accepted set equals exactly the runnable matrix. The anti-grammar
rows are additionally asserted by name. No application, no acts, no
events exist in this milestone; nothing here executes anything.
"""

import inspect
import json
import sys
import unittest
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    AUTHORITY_LABELS, CLASSIFICATION_STATUSES, REASONS,
    RUNNABLE_MATRIX, STALENESS_DECAY_ORDER, TRANSITION_CATALOGUE,
    TRUTH_LABELS, classify_transition,
)

GRAMMAR = json.loads(
    (ROOT / "tests" / "grammar" / "d3-transitions.json")
    .read_text(encoding="utf-8"))

ALL_IDS = sorted(TRANSITION_CATALOGUE)
ALL_ACTORS = sorted({entry["actor"]
                     for entry in TRANSITION_CATALOGUE.values()})
ALL_LABELS = sorted(AUTHORITY_LABELS | set(STALENESS_DECAY_ORDER)) + [None]


class CatalogueShape(unittest.TestCase):
    def test_catalogue_contains_exactly_t1_through_t8(self):
        self.assertEqual(ALL_IDS, [f"D3-T{i}" for i in range(1, 9)])

    def test_catalogue_actors_align_with_the_transcription(self):
        for tid, entry in TRANSITION_CATALOGUE.items():
            self.assertEqual(entry["actor"],
                             GRAMMAR["transitions"][tid]["allowed_actor"],
                             f"{tid}: actor diverges from transcription")

    def test_output_labels_align_with_the_transcription(self):
        for tid in ("D3-T1", "D3-T3"):
            self.assertEqual(TRANSITION_CATALOGUE[tid]["output_label"],
                             GRAMMAR["transitions"][tid]["output_label"])

    def test_agent_forbidden_transitions_have_no_agent_rows(self):
        for tid in GRAMMAR["agent_forbidden_transitions"]:
            for row in RUNNABLE_MATRIX:
                if row[0] == tid:
                    self.assertNotIn("agent", row[3],
                                     f"{tid}: agent-flavoured actor row")

    def test_decay_rows_follow_the_transcription_order(self):
        order = GRAMMAR["staleness_order"]
        pairs = list(zip(order, order[1:]))
        for tid, f, t, _, _ in RUNNABLE_MATRIX:
            if tid == "D3-T5":
                self.assertIn((f, t), pairs, "decay row out of order")

    def test_t1_contributes_zero_runnable_rows(self):
        self.assertEqual([r for r in RUNNABLE_MATRIX if r[0] == "D3-T1"], [])


class ExhaustiveSweep(unittest.TestCase):
    """Every constructible proposal classified; accepted == matrix."""

    def test_accepted_set_equals_the_matrix_exactly(self):
        accepted = set()
        for tid, f, t, actor in product(ALL_IDS, ALL_LABELS,
                                        ALL_LABELS, ALL_ACTORS):
            result = classify_transition(tid, f, t, actor)
            self.assertIn(result["status"], CLASSIFICATION_STATUSES)
            if result["status"] in ("runnable", "gated"):
                accepted.add((tid, f, t, actor))
        expected = {(tid, f, t, actor)
                    for tid, f, t, actor, _ in RUNNABLE_MATRIX}
        self.assertEqual(accepted, expected,
                         "accepted set diverges from the runnable matrix")


class ClassificationBehaviour(unittest.TestCase):
    def test_every_ungated_row_is_runnable(self):
        for tid, f, t, actor, gated in RUNNABLE_MATRIX:
            if not gated:
                with self.subTest(row=(tid, f, t)):
                    self.assertEqual(
                        classify_transition(tid, f, t, actor)["status"],
                        "runnable")

    def test_every_gated_row_is_gated_not_runnable(self):
        for tid, f, t, actor, gated in RUNNABLE_MATRIX:
            if gated:
                with self.subTest(row=(tid, f, t)):
                    result = classify_transition(tid, f, t, actor)
                    self.assertEqual(result["status"], "gated")

    def test_t1_is_dormant_by_name_never_illegal_never_runnable(self):
        well_formed = classify_transition(
            "D3-T1", None, "agent-extracted, pending review",
            "agent-under-e2-grant")
        self.assertEqual(well_formed["status"], "dormant")
        self.assertIn("dormant", well_formed["reason"])
        arbitrary = classify_transition("D3-T1", "current", "expired",
                                        "time-automatic")
        self.assertEqual(arbitrary["status"], "dormant",
                         "any T1-shaped request must be dormant")

    def test_unknown_transition_is_illegal(self):
        for tid in ("D3-T9", "remove-history", "", None):
            with self.subTest(transition=tid):
                self.assertEqual(
                    classify_transition(tid, "user-reported",
                                        "confirmed by user",
                                        "user-review-only")["status"],
                    "illegal")


class AntiGrammar(unittest.TestCase):
    """The named prohibitions, asserted over and above refusal-by-absence."""

    def test_no_agent_mints_truth(self):
        for tid, f, truth in product(ALL_IDS, ALL_LABELS, TRUTH_LABELS):
            status = classify_transition(
                tid, f, truth, "agent-under-e2-grant")["status"]
            self.assertNotIn(status, ("runnable", "gated"),
                             f"agent path to truth via {tid}")

    def test_no_system_mints_truth(self):
        for actor in ("system-on-user-entry", "system-flags-user-resolves"):
            for tid, f, truth in product(ALL_IDS, ALL_LABELS, TRUTH_LABELS):
                status = classify_transition(tid, f, truth, actor)["status"]
                self.assertNotIn(status, ("runnable", "gated"),
                                 f"system path to truth via {tid}/{actor}")

    def test_time_only_lowers_staleness(self):
        order = list(STALENESS_DECAY_ORDER)
        pairs = set(zip(order, order[1:]))
        for f, t in product(order, order):
            if (f, t) in pairs:
                continue
            with self.subTest(pair=(f, t)):
                self.assertEqual(
                    classify_transition("D3-T5", f, t,
                                        "time-automatic")["status"],
                    "illegal", "time moved staleness other than one "
                               "step downward")

    def test_no_automatic_promotion(self):
        for tid, f, t in product(ALL_IDS, ALL_LABELS,
                                 sorted(AUTHORITY_LABELS)):
            status = classify_transition(tid, f, t,
                                         "time-automatic")["status"]
            self.assertNotIn(status, ("runnable", "gated"),
                             "the time actor touched an authority label")

    def test_no_unsupersession(self):
        for tid, t, actor in product(ALL_IDS, ALL_LABELS, ALL_ACTORS):
            status = classify_transition(tid, "outdated / superseded",
                                         t, actor)["status"]
            self.assertNotIn(status, ("runnable", "gated"),
                             "a superseded item left its terminal state")

    def test_no_silent_history_removal(self):
        removal_ids = [tid for tid, entry in TRANSITION_CATALOGUE.items()
                       if "remov" in entry["kind"] or "delet" in entry["kind"]]
        self.assertEqual(removal_ids, [],
                         "the catalogue contains a removal transition")
        self.assertEqual(
            classify_transition("remove-history", "confirmed by user",
                                None, "system-on-user-entry")["status"],
            "illegal")


class ValidatorDiscipline(unittest.TestCase):
    def test_status_vocabulary_is_exact(self):
        self.assertEqual(CLASSIFICATION_STATUSES,
                         {"runnable", "gated", "dormant", "illegal"})

    def test_reasons_are_fixed_and_content_free(self):
        seen = set()
        for tid, f, t, actor in product(ALL_IDS, ALL_LABELS[:4],
                                        ALL_LABELS[:4], ALL_ACTORS[:3]):
            seen.add(classify_transition(tid, f, t, actor)["reason"])
        seen.add(classify_transition("D3-T9", None, None, None)["reason"])
        self.assertTrue(seen <= REASONS,
                        "a reason escaped the fixed vocabulary")

    def test_signature_has_no_content_or_item_parameter(self):
        params = list(inspect.signature(classify_transition).parameters)
        self.assertEqual(params,
                         ["transition_id", "from_label", "to_label", "actor"])

    def test_results_are_fresh_data_and_nothing_is_mutated(self):
        first = classify_transition("D3-T3", None, "user-reported",
                                    "system-on-user-entry")
        second = classify_transition("D3-T3", None, "user-reported",
                                     "system-on-user-entry")
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        first["status"] = "tampered"
        self.assertEqual(
            classify_transition("D3-T3", None, "user-reported",
                                "system-on-user-entry")["status"],
            "runnable", "a caller mutated shared state")


if __name__ == "__main__":
    unittest.main()
