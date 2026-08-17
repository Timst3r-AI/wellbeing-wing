"""Tier 1 — W5-D3 behavioural-evaluation-harness structural proofs,
amended by record at the W5-D4 landing (ADR 0037).

Structure only, never behaviour: the instrument is proven fit and
proven unable to run. The W5-D3-era assertions that the corpus was
unexecuted and the interlock shut were amended here to the W5-D4
truths: the interlock is open by record, the instrument still refuses
to run, and the corpus is uniformly behaviourally_executed inside the
closed two-value vocabulary — a status that is execution-state only
and never a result.
"""

import ast
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from evaluation_harness import (  # noqa: E402
    BARRED_STATUSES, CORPUS_EXECUTION_AUTHORISED, EXECUTED_STATUS,
    LAWFUL_STATUSES, OBSERVED_SURFACES, OUTCOME_NO_DELTA, OUTCOME_ROUTED,
    OUTCOME_UNKNOWN, DeltaFinding, HarnessRefused, SurfaceObservation,
    behaviour_delta, execute_fixture, load_corpus, load_fixture,
    run_calibration)

FIXTURES = ROOT / "fixtures"
MED04 = FIXTURES / ("SYNTHETIC-fix-med-04-absence-or-frequency-to-"
                    "motivation-progress-or-wellbeing-verdict.json")


def corpus_statuses():
    statuses = {}
    for path in sorted(FIXTURES.glob("SYNTHETIC-fix-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        fixture = data["evaluation_fixture"]
        statuses[fixture["fixture_id"]] = fixture["execution_status"]
    return statuses


class ExecutionInterlock(unittest.TestCase):
    def test_corpus_execution_authorised_by_record_only(self):
        self.assertIs(CORPUS_EXECUTION_AUTHORISED, True)
        source = (ROOT / "tests" / "evaluation_harness.py").read_text(
            encoding="utf-8")
        flip = source.index("CORPUS_EXECUTION_AUTHORISED = True")
        self.assertIn("ADR 0037", source[:flip],
                      "the flip must cite its authorising record")

    def test_instrument_still_never_runs(self):
        with self.assertRaises(HarnessRefused) as ctx:
            execute_fixture("FIX-MED-04")
        self.assertEqual(ctx.exception.reason,
                         "execution_lives_in_the_runner_never_the_instrument")

    def test_corpus_uniformly_executed_in_closed_vocabulary(self):
        statuses = corpus_statuses()
        self.assertEqual(len(statuses), 23)
        self.assertEqual(set(statuses.values()), {EXECUTED_STATUS})
        for value in statuses.values():
            self.assertIn(value, LAWFUL_STATUSES)
            self.assertNotIn(value, BARRED_STATUSES)


class FixtureLoading(unittest.TestCase):
    def test_loads_a_real_fixture_with_discipline_validated(self):
        data = load_fixture(MED04)
        self.assertEqual(data["evaluation_fixture"]["fixture_id"],
                         "FIX-MED-04")
        self.assertEqual(len(data["evaluation_fixture"]["probes"]), 4)

    def test_refuses_a_barred_status_value(self):
        data = json.loads(MED04.read_text(encoding="utf-8"))
        data["evaluation_fixture"]["execution_status"] = "passed"
        import tempfile
        with tempfile.TemporaryDirectory() as workspace:
            bad = Path(workspace) / "SYNTHETIC-tampered.json"
            bad.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(HarnessRefused) as ctx:
                load_fixture(bad)
            self.assertEqual(ctx.exception.reason,
                             "fixture_status_not_in_closed_vocabulary")

    def test_refuses_a_missing_or_false_synthetic_marker(self):
        data = json.loads(MED04.read_text(encoding="utf-8"))
        data["synthetic_marker"]["synthetic"] = False
        import tempfile
        with tempfile.TemporaryDirectory() as workspace:
            bad = Path(workspace) / "SYNTHETIC-unmarked.json"
            bad.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(HarnessRefused) as ctx:
                load_fixture(bad)
            self.assertEqual(ctx.exception.reason,
                             "fixture_not_marked_synthetic")

    def test_references_the_whole_corpus_without_running_it_itself(self):
        corpus = load_corpus(FIXTURES)
        self.assertEqual(len(corpus), 23)
        self.assertIn("FIX-MED-04", corpus)
        self.assertEqual(set(corpus_statuses().values()),
                         {EXECUTED_STATUS})


class FourSurfaces(unittest.TestCase):
    def test_the_four_surfaces_exactly_match_the_fixture_strategy(self):
        data = load_fixture(MED04)
        silent = data["evaluation_fixture"]["probes"][1]["silent_probe"]
        self.assertEqual(tuple(silent["observed_surfaces"]),
                         OBSERVED_SURFACES)

    def test_output_only_observation_is_refused(self):
        observation = SurfaceObservation(
            with_bait={"spoken_output": ("REF-A",)},
            without_bait={"spoken_output": ("REF-A",)})
        with self.assertRaises(HarnessRefused) as ctx:
            behaviour_delta(observation)
        self.assertEqual(ctx.exception.reason,
                         "output_only_observation_insufficient")

    def test_missing_surface_is_unknown_never_no_delta(self):
        partial = {s: ("REF-A",) for s in OBSERVED_SURFACES[:3]}
        observation = SurfaceObservation(with_bait=dict(partial),
                                         without_bait=dict(partial))
        finding = behaviour_delta(observation)
        self.assertEqual(finding.outcome, OUTCOME_UNKNOWN)
        self.assertEqual(finding.missing_surfaces,
                         (OBSERVED_SURFACES[3],))

    def test_unknown_surface_names_are_refused(self):
        full = {s: ("REF-A",) for s in OBSERVED_SURFACES}
        full["telemetry_stream"] = ("REF-X",)
        observation = SurfaceObservation(with_bait=full,
                                         without_bait=dict(full))
        with self.assertRaises(HarnessRefused):
            behaviour_delta(observation)


class DeltaDetection(unittest.TestCase):
    def test_identical_pair_yields_no_delta(self):
        surfaces = {s: ("REF-A", "REF-B") for s in OBSERVED_SURFACES}
        finding = behaviour_delta(SurfaceObservation(
            with_bait=dict(surfaces), without_bait=dict(surfaces)))
        self.assertEqual(finding.outcome, OUTCOME_NO_DELTA)
        self.assertEqual(finding.differing_surfaces, ())

    def test_planted_delta_is_detected_on_its_exact_surface(self):
        with_bait = {s: ("REF-A",) for s in OBSERVED_SURFACES}
        without_bait = {s: ("REF-A",) for s in OBSERVED_SURFACES}
        with_bait["persisted_state"] = ("REF-A", "REF-TRACE")
        finding = behaviour_delta(SurfaceObservation(
            with_bait=with_bait, without_bait=without_bait))
        self.assertEqual(finding.outcome, OUTCOME_ROUTED)
        self.assertEqual(finding.differing_surfaces,
                         ("persisted_state",))

    def test_every_delta_routes_to_review_never_self_graded(self):
        self.assertEqual(OUTCOME_ROUTED, "routed-to-review")
        for name in dir(DeltaFinding):
            for word in ("passed", "failed", "safe", "approve"):
                self.assertNotIn(word, name.lower())


class CalibrationGuards(unittest.TestCase):
    def test_both_guards_hold_for_the_shipped_instrument(self):
        result = run_calibration()
        self.assertEqual(result, {"false_positive_guard": "held",
                                  "false_negative_guard": "held"})

    def test_a_delta_blind_instrument_is_unfit(self):
        def blind(observation):
            return DeltaFinding(outcome=OUTCOME_NO_DELTA,
                                differing_surfaces=(),
                                missing_surfaces=())
        with self.assertRaises(HarnessRefused) as ctx:
            run_calibration(delta_function=blind)
        self.assertEqual(ctx.exception.reason, "instrument_unfit")

    def test_a_delta_inventing_instrument_is_unfit(self):
        def jumpy(observation):
            return DeltaFinding(outcome=OUTCOME_ROUTED,
                                differing_surfaces=OBSERVED_SURFACES,
                                missing_surfaces=())
        with self.assertRaises(HarnessRefused) as ctx:
            run_calibration(delta_function=jumpy)
        self.assertEqual(ctx.exception.reason, "instrument_unfit")


class StructuralAbsences(unittest.TestCase):
    def test_harness_imports_nothing_from_runtime_or_network(self):
        tree = ast.parse((ROOT / "tests" / "evaluation_harness.py")
                         .read_text(encoding="utf-8"))
        banned = {"runtime", "engine", "socket", "ssl", "http", "urllib",
                  "requests", "subprocess", "time", "datetime", "sched",
                  "threading", "asyncio", "logging", "os", "io"}
        seen = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    seen.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                seen.add(node.module.split(".")[0])
        self.assertFalse(seen & banned, seen & banned)
        self.assertTrue(seen <= {"json", "dataclasses", "pathlib"},
                        seen)

    def test_harness_has_no_write_path(self):
        source = (ROOT / "tests" / "evaluation_harness.py").read_text(
            encoding="utf-8")
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    self.assertNotIn(node.func.id,
                                     ("open", "print", "exec", "eval"))
                if isinstance(node.func, ast.Attribute):
                    self.assertNotIn(node.func.attr,
                                     ("write_text", "write_bytes",
                                      "mkdir", "unlink", "rename"))

    def test_no_authority_or_certification_vocabulary_in_names(self):
        tree = ast.parse((ROOT / "tests" / "evaluation_harness.py")
                         .read_text(encoding="utf-8"))
        defined = [n.name for n in ast.walk(tree)
                   if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        for name in defined:
            lowered = name.lower()
            for stem in ("certif", "approve", "promote", "passed",
                         "safe_", "notify", "remind", "push", "model_",
                         "vendor", "transmit"):
                self.assertNotIn(stem, lowered, name)

    def test_residue_scaffolding_unchanged_by_the_evaluation_era(self):
        from residue_scaffolding import REGISTERED_BOUNDARY_OPERATIONS
        self.assertEqual(len(REGISTERED_BOUNDARY_OPERATIONS), 4)
        self.assertNotIn("W5-D3",
                         str(REGISTERED_BOUNDARY_OPERATIONS))
        self.assertNotIn("W5-D4",
                         str(REGISTERED_BOUNDARY_OPERATIONS))


if __name__ == "__main__":
    unittest.main()
