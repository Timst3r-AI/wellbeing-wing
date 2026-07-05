"""Tier 2 — D2 grant grammar against synthetic fixtures.

Validator authority rule: conformance check only; not doctrine; a
conflict with the source document is a validator defect; no runtime
reuse without future-phase review.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR = json.loads((ROOT / "tests" / "grammar" / "d2-grant-elements.json").read_text(encoding="utf-8"))
FIXTURE = json.loads((ROOT / "fixtures" / "SYNTHETIC-d2-consent-grants.json").read_text(encoding="utf-8"))

REQUIRED = GRAMMAR["required_elements"]
VALID_DURATIONS = set(GRAMMAR["valid_durations"])
BLANKET_TERMS = [t.lower() for t in GRAMMAR["blanket_scope_terms"]]


def missing(grant, key):
    return key not in grant or grant[key] is None or grant[key] == "" or grant[key] == []


def validate_grant(grant):
    """Conformance check: (valid, reasons). a grant missing any grammar
    element, carrying a blanket scope, or an unbounded duration is
    invalid — unconstructable in any conforming implementation."""
    reasons = []
    for key in REQUIRED:
        if missing(grant, key):
            reasons.append(f"missing-element:{key}")
    if not missing(grant, "scope"):
        for item in grant["scope"]:
            if str(item).lower() in BLANKET_TERMS:
                reasons.append("blanket-scope")
    if not missing(grant, "duration") and grant["duration"] not in VALID_DURATIONS:
        reasons.append("invalid-duration")
    return (not reasons), reasons


def use_allowed(grant_id, revoked_ids):
    """Conformance check: no future access under a revoked grant."""
    return grant_id not in revoked_ids


class ValidGrant(unittest.TestCase):
    def test_complete_grant_is_valid(self):
        ok, reasons = validate_grant(FIXTURE["valid_grant"]["grant"])
        self.assertTrue(ok, f"complete grant rejected: {reasons}")

    def test_grammar_requires_exactly_thirteen_elements(self):
        self.assertEqual(len(REQUIRED), 13)


class MissingElements(unittest.TestCase):
    def test_each_missing_element_grant_is_rejected_for_the_right_reason(self):
        base = FIXTURE["valid_grant"]["grant"]
        cases = FIXTURE["missing_element_grants"]
        self.assertEqual(len(cases), 13, "fixture must cover every element once")
        for case in cases:
            grant = {k: v for k, v in base.items() if k != case["omit"]}
            ok, reasons = validate_grant(grant)
            self.assertFalse(ok, f"{case['case']}: grant missing "
                                 f"{case['omit']} was accepted")
            self.assertIn(f"missing-element:{case['omit']}", reasons,
                          f"{case['case']}: rejected, but not for the omitted element")
            self.assertEqual(case["expected"], "invalid-unconstructable")

    def test_fixture_omits_every_required_element_exactly_once(self):
        omitted = sorted(c["omit"] for c in FIXTURE["missing_element_grants"])
        self.assertEqual(omitted, sorted(REQUIRED))


class AntiBlanket(unittest.TestCase):
    def _built(self, fragment):
        grant = dict(FIXTURE["valid_grant"]["grant"])
        grant.update(fragment)
        return grant

    def test_blanket_scope_attempts_rejected(self):
        for case in FIXTURE["anti_blanket_cases"]:
            if "blanket-scope" not in case["case"]:
                continue
            ok, reasons = validate_grant(self._built(case["grant_fragment"]))
            self.assertFalse(ok, case["case"])
            self.assertIn("blanket-scope", reasons, case["case"])

    def test_unbounded_duration_rejected(self):
        case = next(c for c in FIXTURE["anti_blanket_cases"]
                    if c["case"] == "unbounded-duration")
        ok, reasons = validate_grant(self._built(case["grant_fragment"]))
        self.assertFalse(ok, "unbounded duration accepted")
        self.assertIn("invalid-duration", reasons)

    def test_generic_ai_consent_unconstructable(self):
        case = next(c for c in FIXTURE["anti_blanket_cases"]
                    if c["case"] == "generic-ai-consent")
        ok, reasons = validate_grant(self._built(case["grant_fragment"]))
        self.assertFalse(ok, "generic consent accepted")
        self.assertIn("missing-element:edge", reasons)
        self.assertIn("missing-element:scope", reasons)


class RevocationMidTask(unittest.TestCase):
    def test_no_use_after_revocation(self):
        rev = FIXTURE["revocation_mid_task"]
        grant_id = rev["setup"]["grant"]
        self.assertTrue(use_allowed(grant_id, revoked_ids=set()))
        self.assertFalse(use_allowed(grant_id, revoked_ids={grant_id}),
                         "access allowed under a revoked grant")

    def test_fixture_carries_all_five_immediate_effects(self):
        effects = FIXTURE["revocation_mid_task"]["expected_immediate_effects"]
        self.assertEqual(len(effects), GRAMMAR["revocation_immediate_effects_count"])
        joined = " ".join(effects).lower()
        for needle in GRAMMAR["revocation_effects_must_include"]:
            self.assertIn(needle.lower(), joined,
                          f"immediate effect not represented: {needle}")


if __name__ == "__main__":
    unittest.main()
