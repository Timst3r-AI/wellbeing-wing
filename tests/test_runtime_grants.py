"""Tier 1 — W5-D2-M02 grant-machinery structural proofs.

Structure only, never behaviour: constructability, lifecycle,
lineage, and refusal shapes. All values are synthetic grammar
placeholders (W2-D4); no fixture requires medical plausibility.
"""

import copy
import dataclasses
import unittest
from pathlib import Path

import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.grants import (  # noqa: E402
    DECLARED_EDGES, GOVERNED_DURATIONS, LIFECYCLE_STATES,
    REQUIRED_ELEMENTS, STANDING_VALIDITY_DAYS, ActivationRefused, Grant,
    GrantLifecycle, ReAuthProof, UnconstructableGrant, construct_grant,
    create_successor, standing_validity_exceeded)


def lawful_elements(**overrides):
    base = dict(
        edge="E6", requesting_actor="kitchen-room-agent",
        recipient_class="internal", data_class="C3",
        scope=("Section-Allergies-X",), zones=("Z1", "Z1"),
        purpose="display scoped placeholder section", operation="read",
        plaintext_flag=False, vendor_involvement="none",
        duration="standing_180_days",
        revocation_behaviour="w1-d2-section-5-immediate-effects",
        audit_reference="ledger-ref-placeholder")
    base.update(overrides)
    return base


class Constructability(unittest.TestCase):
    def test_thirteen_elements_are_exactly_thirteen(self):
        self.assertEqual(len(REQUIRED_ELEMENTS), 13)

    def test_each_missing_element_is_unconstructable(self):
        for name in REQUIRED_ELEMENTS:
            elements = lawful_elements()
            del elements[name]
            with self.assertRaises(UnconstructableGrant) as ctx:
                construct_grant(**elements)
            self.assertEqual(ctx.exception.reason, "missing_element:" + name)

    def test_undeclared_edge_is_unconstructable(self):
        for bad in ("E11", "E12", "E99", "M3"):
            with self.assertRaises(UnconstructableGrant) as ctx:
                construct_grant(**lawful_elements(
                    edge=bad, duration="single_task"))
            self.assertEqual(ctx.exception.reason, "undeclared_edge")

    def test_blanket_scope_is_unconstructable(self):
        for bad in (("*",), ("all",), ("everything",), ("  ",), ()):
            with self.assertRaises(UnconstructableGrant):
                construct_grant(**lawful_elements(scope=bad))

    def test_ungoverned_duration_is_unconstructable(self):
        with self.assertRaises(UnconstructableGrant) as ctx:
            construct_grant(**lawful_elements(duration="unbounded"))
        self.assertEqual(ctx.exception.reason, "ungoverned_duration")

    def test_refusal_reason_echoes_no_submitted_value(self):
        marker = "SYNTHETIC-Scope-Marker-Q7"
        try:
            construct_grant(**lawful_elements(edge="E99", duration="x",
                                              scope=(marker,)))
        except UnconstructableGrant as exc:
            self.assertNotIn(marker, str(exc))

    def test_refusal_mutates_no_input(self):
        elements = lawful_elements(edge="E99")
        snapshot = copy.deepcopy(elements)
        with self.assertRaises(UnconstructableGrant):
            construct_grant(**elements)
        self.assertEqual(elements, snapshot)


class ImmutabilityAndLineage(unittest.TestCase):
    def test_grant_is_immutable(self):
        grant = construct_grant(**lawful_elements())
        with self.assertRaises(dataclasses.FrozenInstanceError):
            grant.scope = ("widened",)

    def test_successor_identity_distinct_and_lineage_inspectable(self):
        predecessor = construct_grant(**lawful_elements())
        successor = create_successor(predecessor)
        self.assertNotEqual(successor.grant_id, predecessor.grant_id)
        self.assertEqual(successor.predecessor_id, predecessor.grant_id)

    def test_predecessor_unaltered_by_succession(self):
        predecessor = construct_grant(**lawful_elements())
        snapshot = dataclasses.asdict(predecessor)
        create_successor(predecessor)
        self.assertEqual(dataclasses.asdict(predecessor), snapshot)

    def test_grant_carries_no_authority_field(self):
        grant = construct_grant(**lawful_elements())
        names = {f.name for f in dataclasses.fields(grant)}
        for forbidden in ("authority", "trusted", "truth", "freshness"):
            self.assertFalse(any(forbidden in n for n in names))


class Lifecycle(unittest.TestCase):
    def test_governed_states_exactly_seven(self):
        self.assertEqual(len(LIFECYCLE_STATES), 7)
        self.assertNotIn("stale", LIFECYCLE_STATES)
        self.assertNotIn("suspended", LIFECYCLE_STATES)

    def test_expired_grant_refuses_activation(self):
        lc = GrantLifecycle(construct_grant(**lawful_elements()))
        lc.expire()
        with self.assertRaises(ActivationRefused):
            lc.activate()
        self.assertEqual(lc.state, "expired")

    def test_revoked_grant_refuses_activation_permanently(self):
        lc = GrantLifecycle(construct_grant(**lawful_elements()))
        lc.revoke()
        for _ in range(2):
            with self.assertRaises(ActivationRefused):
                lc.activate()
        self.assertEqual(lc.state, "revoked")

    def test_reauthentication_binds_to_exact_proposal(self):
        vault = lawful_elements(
            edge="E2", data_class="C4", zones=("Z1", "Z3"),
            operation="extract", duration="single_task",
            recipient_class="local_model", plaintext_flag=True)
        grant_a = construct_grant(**vault)
        grant_b = construct_grant(**vault)
        lc = GrantLifecycle(grant_a)
        with self.assertRaises(ActivationRefused) as ctx:
            lc.activate()
        self.assertEqual(ctx.exception.reason, "reauthentication_required")
        with self.assertRaises(ActivationRefused) as ctx:
            lc.activate(ReAuthProof(proposal_id=grant_b.grant_id))
        self.assertEqual(ctx.exception.reason,
                         "reauthentication_scope_mismatch")
        lc.activate(ReAuthProof(proposal_id=grant_a.grant_id))
        self.assertEqual(lc.state, "active")

    def test_material_change_invalidates_old_activation_path(self):
        original = construct_grant(**lawful_elements(
            edge="E2", data_class="C4", zones=("Z1", "Z3"),
            operation="extract", duration="single_task",
            recipient_class="local_model", plaintext_flag=True))
        proof = ReAuthProof(proposal_id=original.grant_id)
        changed = construct_grant(**lawful_elements(
            edge="E2", data_class="C4", zones=("Z1", "Z3"),
            operation="extract", duration="single_task",
            recipient_class="local_model", plaintext_flag=True,
            scope=("Section-Different-Y",)))
        with self.assertRaises(ActivationRefused):
            GrantLifecycle(changed).activate(proof)


class GovernedNumbers(unittest.TestCase):
    def test_duration_table_matches_adr_0030(self):
        self.assertEqual(GOVERNED_DURATIONS["E2"], "single_task")
        self.assertEqual(GOVERNED_DURATIONS["E6"], "standing_180_days")
        self.assertEqual(GOVERNED_DURATIONS["E10"], "per_transmission")
        self.assertEqual(set(GOVERNED_DURATIONS), set(DECLARED_EDGES))
        self.assertEqual(STANDING_VALIDITY_DAYS, 180)

    def test_standing_validity_is_a_pure_injected_predicate(self):
        self.assertFalse(standing_validity_exceeded(179))
        self.assertTrue(standing_validity_exceeded(180))

    def test_no_inactivity_timeout_code_path_exists(self):
        source = (ROOT / "runtime" / "grants.py").read_text(
            encoding="utf-8").lower()
        for token in ("inactiv", "idle", "timeout"):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
