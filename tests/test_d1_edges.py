"""Tier 2 — D1 edge whitelist against synthetic fixtures.

Validator authority rule: the validator below is a conformance check
derived from the accepted source document. It is not doctrine. If it
conflicts with its source, the validator is defective. Future
implementation must match the governed behaviour; it does not inherit
this function, and runtime reuse would require future-phase review.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR = json.loads((ROOT / "tests" / "grammar" / "d1-edges.json").read_text(encoding="utf-8"))
FIXTURE = json.loads((ROOT / "fixtures" / "SYNTHETIC-d1-flow-boundaries.json").read_text(encoding="utf-8"))


def flow_permitted(source, destination):
    """Conformance check: a flow is permitted iff a whitelisted edge
    matches its source and destination. default-deny: everything else
    is refused, including everything on the anti-map, by absence."""
    for edge_id, spec in GRAMMAR["permitted_edges"].items():
        if spec["source"] == source and spec["destination"] == destination:
            return True, edge_id
    return False, None


class PermittedFlows(unittest.TestCase):
    def test_every_permitted_fixture_case_matches_a_whitelisted_edge(self):
        for case in FIXTURE["permitted_flow_cases"]:
            flow = case["flow"]
            ok, edge_id = flow_permitted(flow["source"], flow["destination"])
            self.assertTrue(ok, f"{case['case']}: expected permitted, was refused")
            self.assertEqual(edge_id, case["edge"],
                             f"{case['case']}: matched {edge_id}, fixture says {case['edge']}")
            self.assertTrue(case["expected"].startswith("valid"),
                            f"{case['case']}: fixture expectation is not a valid-class outcome")

    def test_grant_required_edges_are_marked_in_grammar(self):
        for case in FIXTURE["permitted_flow_cases"]:
            if "grant" in case["flow"]:
                spec = GRAMMAR["permitted_edges"][case["edge"]]
                self.assertTrue(spec.get("grant_required"),
                                f"{case['case']}: fixture carries a grant but grammar "
                                f"does not mark {case['edge']} grant-required")


class AntiMap(unittest.TestCase):
    def test_every_anti_map_case_is_refused_by_absence(self):
        for case in FIXTURE["anti_map_cases"]:
            attempt = case["attempt"]
            ok, edge_id = flow_permitted(attempt["source"], attempt["destination"])
            self.assertFalse(ok,
                             f"{case['case']}: anti-map attempt matched edge {edge_id}; "
                             f"a forbidden flow must not be expressible")
            self.assertEqual(case["expected"], "refused-no-edge", case["case"])

    def test_e12_is_reserved_not_permitted(self):
        self.assertIn("E12", GRAMMAR["reserved_edges"])
        self.assertNotIn("E12", GRAMMAR["permitted_edges"])

    def test_default_deny_rule_is_transcribed(self):
        self.assertIn("default_deny", GRAMMAR["rules"])
        self.assertTrue(GRAMMAR["rules"]["key_material_has_no_outbound_edges"])
        self.assertTrue(GRAMMAR["rules"]["ledger_has_no_processing_edges"])


if __name__ == "__main__":
    unittest.main()
