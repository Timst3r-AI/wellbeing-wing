"""W3-D4 milestone 1 - transition catalogue, matrix, and validator tests.

The whitelist proven by enumeration, not sampling: the exhaustive
sweep classifies every constructible proposal and asserts the
accepted set equals exactly the runnable matrix. The anti-grammar
rows are additionally asserted by name. No application, no acts, no
events exist in this milestone; nothing here executes anything.
"""

import ast
import inspect
import json
import sys
import tempfile
import unittest
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    AUTHORITY_LABELS, CLASSIFICATION_STATUSES, REASONS,
    RUNNABLE_MATRIX, STALENESS_DECAY_ORDER, TRANSITION_CATALOGUE,
    TRANSITION_REFUSALS, TRUTH_LABELS, LedgerEvent, ProfileRecordError,
    ProvenanceRef, TransitionError, apply_confirm_by_record,
    apply_confirm_by_user, apply_contradiction_flag, apply_correction,
    apply_staleness_decay, apply_supersession, apply_user_entry,
    authorise_transition, classify_transition, persist_item,
)
from engine.core.transitions import UserAct  # noqa: E402  (test tree only)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402

SYNTHETIC_INTERVALS = {"review due": 10, "stale": 20, "expired": 40}
AT = "2026-01-02T00:00:00+00:00"

ALL_APPLIERS = (apply_user_entry, apply_staleness_decay,
                apply_contradiction_flag, apply_confirm_by_record,
                apply_confirm_by_user, apply_correction, apply_supersession)


def pending_item():
    from engine.core import ProfileItem
    return ProfileItem("Allergen-X status", "SYNTHETIC extract, Persona-K9",
                       "agent-extracted, pending review", "agent",
                       "unknown freshness",
                       provenance=ProvenanceRef("vault-record",
                                                "SYNTHETIC-record-7"))


def reported_item():
    from engine.core import ProfileItem
    return ProfileItem("Condition-Q", "SYNTHETIC note, Persona-K9",
                       "user-reported", "system-on-user-entry",
                       "unknown freshness")

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


class ApplierSuccessPaths(unittest.TestCase):
    def test_t3_user_entry(self):
        result = apply_user_entry("Condition-Q",
                                  "SYNTHETIC note, Persona-K9", AT)
        self.assertEqual(result["item"].authority, "user-reported")
        self.assertEqual(result["event"].kind, "D3-T3")

    def test_t5_single_step_and_multi_step_by_repetition(self):
        from engine.core import ProfileItem
        item = ProfileItem("Condition-Q", "SYNTHETIC", "confirmed by user",
                           "user-review", "current", last_reviewed=AT,
                           provenance=ProvenanceRef("user-statement", "S-1"))
        first = apply_staleness_decay(item, 500, SYNTHETIC_INTERVALS)
        self.assertEqual(first["item"].staleness, "review due",
                         "decay must be one adjacent step per application")
        self.assertEqual(first["item"].authority, "confirmed by user",
                         "authority touched by time")
        second = apply_staleness_decay(first["item"], 500,
                                       SYNTHETIC_INTERVALS)
        third = apply_staleness_decay(second["item"], 500,
                                      SYNTHETIC_INTERVALS)
        self.assertEqual(third["item"].staleness, "expired")
        with self.assertRaises(TransitionError):
            apply_staleness_decay(third["item"], 500, SYNTHETIC_INTERVALS)

    def test_t5_refuses_when_no_decay_is_due(self):
        from engine.core import ProfileItem
        item = ProfileItem("Condition-Q", "SYNTHETIC", "confirmed by user",
                           "user-review", "current", last_reviewed=AT,
                           provenance=ProvenanceRef("user-statement", "S-1"))
        with self.assertRaises(TransitionError):
            apply_staleness_decay(item, 1, SYNTHETIC_INTERVALS)

    def test_t6_contradiction_flag_keeps_both_sides_visible(self):
        from engine.core import ProfileItem
        confirmed = ProfileItem("Allergen-X status", "SYNTHETIC",
                                "confirmed by user", "user-review",
                                "current", last_reviewed=AT,
                                provenance=ProvenanceRef("user-statement",
                                                         "S-1"))
        other = reported_item()
        result = apply_contradiction_flag(confirmed, other, AT)
        self.assertEqual(result["item"].authority, "contradicted")
        self.assertIs(result["contradiction"].first, confirmed)
        self.assertIs(result["contradiction"].second, other)
        self.assertEqual(result["contradiction"].first.authority,
                         "confirmed by user",
                         "the original side must stay visible, unmutated")

    def test_t2_and_t4_confirm_with_act(self):
        act = UserAct("user-review-only", AT, "Allergen-X status")
        by_record = apply_confirm_by_record(
            pending_item(), act,
            ProvenanceRef("vault-record", "SYNTHETIC-record-7"), AT)
        self.assertEqual(by_record["item"].authority, "confirmed by record")
        self.assertEqual(by_record["event"].kind, "D3-T2")
        by_user = apply_confirm_by_user(
            reported_item(), act,
            ProvenanceRef("user-statement", "SYNTHETIC-statement-1"), AT)
        self.assertEqual(by_user["item"].authority, "confirmed by user")

    def test_t7_composite_supersede_mint_link_one_event(self):
        from engine.core import ProfileItem
        confirmed = ProfileItem("Condition-Q", "SYNTHETIC old",
                                "confirmed by user", "user-review",
                                "current", last_reviewed=AT,
                                provenance=ProvenanceRef("user-statement",
                                                         "S-1"))
        act = UserAct("user-only", AT, "Condition-Q")
        result = apply_correction(
            confirmed, "SYNTHETIC corrected, Persona-K9", act,
            ProvenanceRef("user-statement", "SYNTHETIC-statement-2"))
        self.assertEqual(result["superseded"].authority,
                         "outdated / superseded")
        self.assertEqual(result["superseded"].content, "SYNTHETIC old",
                         "predecessor content must be retained")
        self.assertEqual(result["correction"].authority, "confirmed by user")
        self.assertIs(result["supersession"].predecessor,
                      result["superseded"])
        self.assertIs(result["supersession"].successor, result["correction"])
        events = [k for k in result if k == "event"]
        self.assertEqual(len(events), 1)

    def test_t8_supersession_retains_and_never_reactivates(self):
        from engine.core import ProfileItem
        old = ProfileItem("Condition-Q", "SYNTHETIC old",
                          "confirmed by record", "user-review", "current",
                          last_reviewed=AT,
                          provenance=ProvenanceRef("vault-record", "R-1"))
        act = UserAct("user-review", AT, "Condition-Q")
        result = apply_supersession(old, reported_item(), act)
        self.assertEqual(result["superseded"].authority,
                         "outdated / superseded")
        self.assertEqual(result["superseded"].content, "SYNTHETIC old")
        with self.assertRaises(TransitionError):
            apply_supersession(result["superseded"], reported_item(), act)


class ApplierRefusals(unittest.TestCase):
    def test_gated_appliers_refuse_without_an_act(self):
        prov_r = ProvenanceRef("vault-record", "R-1")
        prov_u = ProvenanceRef("user-statement", "S-1")
        from engine.core import ProfileItem
        confirmed = ProfileItem("Condition-Q", "SYNTHETIC",
                                "confirmed by user", "user-review",
                                "current", last_reviewed=AT,
                                provenance=prov_u)
        cases = {
            "T2": lambda: apply_confirm_by_record(pending_item(), None,
                                                  prov_r, AT),
            "T4": lambda: apply_confirm_by_user(reported_item(), None,
                                                prov_u, AT),
            "T7": lambda: apply_correction(confirmed, "SYNTHETIC", None,
                                           prov_u),
            "T8": lambda: apply_supersession(confirmed, reported_item(),
                                             None),
        }
        for name, attempt in cases.items():
            with self.subTest(transition=name):
                with self.assertRaises(TransitionError):
                    attempt()

    def test_wrong_capacity_act_refused(self):
        act = UserAct("user-only", AT, "Allergen-X status")  # not review
        with self.assertRaises(TransitionError):
            apply_confirm_by_record(pending_item(), act,
                                    ProvenanceRef("vault-record", "R-1"), AT)

    def test_malformed_act_refused_at_construction(self):
        for bad in (("agent", AT, "scope"), ("user-review", "", "scope"),
                    ("user-review", AT, "")):
            with self.subTest(act=bad):
                with self.assertRaises(TransitionError):
                    UserAct(*bad)

    def test_t1_application_attempt_raises_dormant(self):
        try:
            authorise_transition("D3-T1", None,
                                 "agent-extracted, pending review",
                                 "agent-under-e2-grant")
            self.fail("dormant transition was authorised")
        except TransitionError as e:
            self.assertIn("dormant", str(e))

    def test_illegal_row_raises(self):
        with self.assertRaises(TransitionError):
            authorise_transition("D3-T4", "user-reported",
                                 "confirmed by user", "agent-under-e2-grant")

    def test_refusal_messages_are_fixed_and_content_free(self):
        attempts = (
            lambda: authorise_transition("D3-T1", None, None, None),
            lambda: authorise_transition("D3-T9", None, None, None),
            lambda: apply_confirm_by_user(reported_item(), None,
                                          ProvenanceRef("user-statement",
                                                        "S-1"), AT),
            lambda: UserAct("agent", AT, "scope"),
        )
        for attempt in attempts:
            try:
                attempt()
                self.fail("attempt was accepted")
            except TransitionError as e:
                self.assertIn(str(e), TRANSITION_REFUSALS)


class ApplierDiscipline(unittest.TestCase):
    def test_appliers_take_no_ports_storage_crypto_or_files(self):
        for applier in ALL_APPLIERS:
            params = inspect.signature(applier).parameters
            for name in params:
                for banned in ("storage", "crypto", "clock", "ledger",
                               "path", "file", "port"):
                    self.assertNotIn(banned, name,
                                     f"{applier.__name__} touches the world")

    def test_inputs_are_never_mutated(self):
        item = pending_item()
        before = dict(vars(item))
        act = UserAct("user-review-only", AT, item.section)
        apply_confirm_by_record(item, act,
                                ProvenanceRef("vault-record", "R-1"), AT)
        self.assertEqual(dict(vars(item)), before, "input item mutated")

    def test_every_success_emits_exactly_one_well_formed_event(self):
        act_r = UserAct("user-review-only", AT, "s")
        results = [
            apply_user_entry("Condition-Q", "SYNTHETIC", AT),
            apply_confirm_by_record(pending_item(), act_r,
                                    ProvenanceRef("vault-record", "R-1"),
                                    AT),
        ]
        collected = []
        for result in results:
            events = [v for v in result.values()
                      if isinstance(v, LedgerEvent)]
            self.assertEqual(len(events), 1)
            self.assertIn(events[0].kind, TRANSITION_CATALOGUE)
            collected.append(events[0])
        self.assertEqual(len(collected), 2,
                         "events collect in memory only, nothing stored")

    def test_applier_confirmed_item_still_refuses_to_persist(self):
        act = UserAct("user-review-only", AT, "Condition-Q")
        confirmed = apply_confirm_by_user(
            reported_item(), act,
            ProvenanceRef("user-statement", "S-1"), AT)["item"]
        with tempfile.TemporaryDirectory() as ws:
            storage = FileStorage(Path(ws) / "profile.bin")
            crypto = PyNaClCrypto()
            with self.assertRaises(ProfileRecordError):
                persist_item(storage, crypto, crypto.random_key(),
                             confirmed)
            self.assertFalse(storage.exists(),
                             "refused persistence wrote something")


class UserActPostureGuards(unittest.TestCase):
    """Repository-scoped, mechanical: the application tree cannot
    construct a UserAct; the suite fails if a construction appears."""

    def _engine_sources(self):
        return [p for p in (ROOT / "engine").rglob("*.py")]

    def test_no_application_tree_useract_construction(self):
        for src in self._engine_sources():
            tree = ast.parse(src.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func = node.func
                    name = getattr(func, "id", getattr(func, "attr", ""))
                    self.assertNotEqual(
                        name, "UserAct",
                        f"UserAct constructed in application tree: "
                        f"{src.name}")

    def test_useract_is_bound_exactly_once_in_the_engine_tree(self):
        bindings = 0
        for src in self._engine_sources():
            tree = ast.parse(src.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "UserAct":
                    bindings += 1
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if getattr(target, "id", "") == "UserAct":
                            bindings += 1
        self.assertEqual(bindings, 1,
                         "UserAct must be bound exactly once (its class)")

    def test_useract_is_not_exported_from_the_package(self):
        init_text = (ROOT / "engine" / "core" / "__init__.py").read_text(
            encoding="utf-8")
        self.assertNotIn("UserAct", init_text,
                         "UserAct must not be re-exported")


if __name__ == "__main__":
    unittest.main()
