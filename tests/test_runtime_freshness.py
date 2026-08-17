"""Tier 1 — W5-D2-M03 freshness-wiring structural proofs.

Structure only, never behaviour. Label boundaries are verified
through the sealed engine's own public staleness function consuming
this module's derived absolute triple — engine law consumed at the
boundary, never duplicated. All values are synthetic grammar
placeholders; no proof requires medical plausibility.
"""

import ast
import dataclasses
import unittest
from pathlib import Path

import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import staleness_of  # noqa: E402
from runtime.freshness import (  # noqa: E402
    FRESHNESS_POLICY_KEYS, RE_REVIEW_TRIGGERS, TREATMENTS,
    AcknowledgementEvent, AssertionWithheld, BoundedUnknown,
    FreshnessPolicy, ItemGovernanceState, ReviewAct,
    UnconstructablePolicy, acknowledge, assert_as_stable_truth,
    construct_policy, consume_trigger, engine_intervals, governed_policy,
    renew, safeguard14_fires, unknown_at_source, unknown_from_expiry)


def lawful_state():
    return ItemGovernanceState(
        review_timestamp="AS-OF-PLACEHOLDER-1", freshness_label="stale",
        authority_label="confirmed-by-record", provenance_ref="REF-P1",
        contradiction_flag=False, supersession_link="",
        pending_review=True)


class PolicyConstructability(unittest.TestCase):
    def test_seven_keys_exactly(self):
        self.assertEqual(len(FRESHNESS_POLICY_KEYS), 7)
        for key in FRESHNESS_POLICY_KEYS:
            governed_policy(key)

    def test_eighth_key_refused(self):
        for door in (governed_policy, construct_policy):
            with self.assertRaises(UnconstructablePolicy) as ctx:
                door("wellness-score")
            self.assertEqual(ctx.exception.reason, "unknown_policy_key")

    def test_missing_r_g_or_h_unconstructable(self):
        complete = dict(review_interval_days=365, renewal_grace_days=91,
                        hard_limit_days=730)
        for name in complete:
            partial = dict(complete)
            partial[name] = None
            with self.assertRaises(UnconstructablePolicy) as ctx:
                construct_policy("allergy", **partial)
            self.assertEqual(ctx.exception.reason, "missing_" + name)

    def test_non_increasing_thresholds_refused(self):
        with self.assertRaises(UnconstructablePolicy) as ctx:
            construct_policy("allergy", review_interval_days=365,
                             renewal_grace_days=91, hard_limit_days=456)
        self.assertEqual(ctx.exception.reason, "non_increasing_thresholds")

    def test_s_is_computed_and_never_accepted_as_input(self):
        with self.assertRaises(TypeError):
            construct_policy("allergy", review_interval_days=365,
                             renewal_grace_days=91, hard_limit_days=730,
                             stale_boundary_days=456)
        names = {f.name for f in dataclasses.fields(FreshnessPolicy)}
        self.assertNotIn("stale_boundary_days", names)

    def test_g_change_moves_s_automatically_and_h_independent(self):
        one = construct_policy("allergy", review_interval_days=365,
                               renewal_grace_days=91, hard_limit_days=730)
        two = construct_policy("allergy", review_interval_days=365,
                               renewal_grace_days=120, hard_limit_days=730)
        self.assertEqual(one.stale_boundary_days, 456)
        self.assertEqual(two.stale_boundary_days, 485)
        self.assertEqual(one.hard_limit_days, two.hard_limit_days)


class LabelBoundaries(unittest.TestCase):
    def test_boundaries_exact_via_engine_function(self):
        policy = governed_policy("allergy")
        intervals = engine_intervals(policy)
        self.assertEqual(intervals["stale"], policy.stale_boundary_days)
        for elapsed, label in ((0, "current"), (364, "current"),
                               (365, "review due"), (455, "review due"),
                               (456, "stale"), (729, "stale"),
                               (730, "expired"), (731, "expired")):
            self.assertEqual(staleness_of(elapsed, intervals), label)

    def test_monotonicity_via_engine_function(self):
        intervals = engine_intervals(governed_policy("preference"))
        order = ("current", "review due", "stale", "expired")
        last = 0
        for elapsed in range(0, 1600, 5):
            rank = order.index(staleness_of(elapsed, intervals))
            self.assertGreaterEqual(rank, last)
            last = rank


class UnknownPreservation(unittest.TestCase):
    def test_unknown_is_bounded(self):
        u = unknown_at_source("Section-Placeholder-X",
                              ("Source-Set-A",), "AS-OF-PLACEHOLDER-2")
        self.assertEqual((u.scope, u.source_set, u.as_of, u.origin),
                         ("Section-Placeholder-X", ("Source-Set-A",),
                          "AS-OF-PLACEHOLDER-2", "at_source"))

    def test_absence_not_inferred(self):
        names = {f.name for f in dataclasses.fields(BoundedUnknown)}
        for forbidden in ("absent", "negative", "resolved", "confirmed"):
            self.assertFalse(any(forbidden in n for n in names))

    def test_expiry_unknown_retains_reference_provenance_and_age(self):
        u = unknown_from_expiry("Section-Placeholder-X", ("Source-Set-A",),
                                "AS-OF-PLACEHOLDER-2",
                                last_known_ref="REC-REF-K9",
                                provenance_ref="REF-P1", age_days=740)
        self.assertEqual((u.last_known_ref, u.provenance_ref, u.age_days),
                         ("REC-REF-K9", "REF-P1", 740))
        with self.assertRaises(UnconstructablePolicy):
            unknown_from_expiry("Section-Placeholder-X", ("Source-Set-A",),
                                "AS-OF-PLACEHOLDER-2", last_known_ref=None,
                                provenance_ref=None, age_days=None)

    def test_stale_and_expired_never_stable_truth(self):
        self.assertEqual(assert_as_stable_truth("current"), "assertable")
        for label in ("stale", "expired"):
            with self.assertRaises(AssertionWithheld) as ctx:
                assert_as_stable_truth(label)
            self.assertEqual(ctx.exception.reason,
                             "not_assertable_as_stable_truth")
        self.assertEqual(TREATMENTS["expired"], "unknown_treatment")


class AcknowledgementAndRenewal(unittest.TestCase):
    def test_acknowledgement_writes_no_freshness_state(self):
        state = lawful_state()
        snapshot = dataclasses.asdict(state)
        event = acknowledge(state, "ITEM-REF-1")
        self.assertIsInstance(event, AcknowledgementEvent)
        self.assertEqual(dataclasses.asdict(state), snapshot)

    def test_renewal_requires_explicit_review_act(self):
        state = lawful_state()
        with self.assertRaises(AssertionWithheld) as ctx:
            renew(state, None)
        self.assertEqual(ctx.exception.reason, "renewal_requires_review_act")
        renewed = renew(state, ReviewAct(item_ref="ITEM-REF-1",
                                         reviewed_timestamp="AS-OF-3"))
        self.assertEqual(renewed.review_timestamp, "AS-OF-3")
        self.assertEqual(state.review_timestamp, "AS-OF-PLACEHOLDER-1")


class TriggerConsumption(unittest.TestCase):
    def test_five_triggers_exactly(self):
        self.assertEqual(len(RE_REVIEW_TRIGGERS), 5)

    def test_consumption_writes_no_source_state_and_no_timestamp(self):
        state = lawful_state()
        snapshot = dataclasses.asdict(state)
        pending = ("interval_lapse", "user_request")
        remaining, consumed = consume_trigger(pending, "user_request",
                                              "ITEM-REF-1")
        self.assertEqual(remaining, ("interval_lapse",))
        self.assertEqual(consumed.trigger, "user_request")
        self.assertEqual(pending, ("interval_lapse", "user_request"))
        self.assertEqual(dataclasses.asdict(state), snapshot)
        self.assertFalse(hasattr(consumed, "timestamp"))

    def test_unknown_or_unpending_trigger_refused(self):
        with self.assertRaises(UnconstructablePolicy):
            consume_trigger(("user_request",), "calendar_ping", "ITEM-REF-1")
        with self.assertRaises(UnconstructablePolicy):
            consume_trigger((), "user_request", "ITEM-REF-1")


class Safeguard14(unittest.TestCase):
    def test_predicate_fires_only_on_all_three_conditions(self):
        for uncertain in (True, False):
            for requires in (True, False):
                for relevant in (True, False):
                    fired = safeguard14_fires(
                        fact_uncertain=uncertain,
                        completion_requires_assuming_absent_or_resolved=requires,
                        safety_relevant=relevant,
                        consulted_set_name="w1-d3-section-6.3-set")
                    self.assertEqual(fired,
                                     uncertain and requires and relevant)

    def test_consulted_set_must_be_named(self):
        with self.assertRaises(UnconstructablePolicy):
            safeguard14_fires(
                fact_uncertain=True,
                completion_requires_assuming_absent_or_resolved=True,
                safety_relevant=True, consulted_set_name="")

    def test_refusal_is_content_free_and_blocks_assertion_only(self):
        from runtime.freshness import withhold_dependent_assertion
        marker = "SYNTHETIC-Fact-Marker-Q9"
        try:
            withhold_dependent_assertion()
        except AssertionWithheld as exc:
            self.assertNotIn(marker, str(exc))
            self.assertIn("absent_or_resolved", exc.reason)


class StructuralAbsences(unittest.TestCase):
    def test_no_clock_or_scheduler_import(self):
        tree = ast.parse((ROOT / "runtime" / "freshness.py").read_text(
            encoding="utf-8"))
        banned = {"time", "datetime", "sched", "threading", "asyncio"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.assertNotIn(alias.name.split(".")[0], banned)
            elif isinstance(node, ast.ImportFrom) and node.module:
                self.assertNotIn(node.module.split(".")[0], banned)

    def test_provisional_label_present_and_no_validation_claim(self):
        source = (ROOT / "runtime" / "freshness.py").read_text(
            encoding="utf-8")
        self.assertIn("provisional governance default", source)
        self.assertIn("not clinically validated", source)
        self.assertIn("non-equivalence", source)
        self.assertNotIn("clinically proven", source)

    def test_no_notification_or_reminder_api_exists(self):
        """Structural absence: no defined name in the freshness module
        carries notification, reminder, or outward-push vocabulary.
        Names only — comments and docstrings may lawfully name the
        prohibition itself."""
        banned_stems = ("notify", "notification", "remind", "reminder",
                        "push", "email", "sms", "webhook", "subscribe",
                        "subscription", "schedule_send", "dispatch")
        tree = ast.parse((ROOT / "runtime" / "freshness.py").read_text(
            encoding="utf-8"))
        defined = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                 ast.ClassDef)):
                defined.append(node.name)
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    defined.extend(a.arg for a in node.args.args)
                    defined.extend(a.arg for a in node.args.kwonlyargs)
            elif isinstance(node, ast.Assign):
                defined.extend(t.id for t in node.targets
                               if isinstance(t, ast.Name))
            elif isinstance(node, ast.AnnAssign) and isinstance(
                    node.target, ast.Name):
                defined.append(node.target.id)
        self.assertTrue(defined)
        for name in defined:
            lowered = name.lower()
            for stem in banned_stems:
                self.assertNotIn(stem, lowered,
                                 "outward-facing vocabulary in defined "
                                 "name: " + name)


if __name__ == "__main__":
    unittest.main()
