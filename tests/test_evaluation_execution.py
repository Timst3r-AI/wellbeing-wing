"""Tier 1 — W5-D4 corpus-execution structural proofs.

Proves the run stayed inside its record: calibration before any
corpus work, exactly twenty-three fixtures executed and recorded,
results only in governed evaluation records and never in fixture
files, the four-surface observation structure preserved with honest
unknown, no self-grading, append-only re-run semantics, deterministic
reproduction, and a status transition that is execution-state only.
Nothing here claims a behavioural proof, and no vocabulary anywhere
in the records means passed, true, or fit for anything.
"""

import ast
import hashlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from evaluation_execution import (  # noqa: E402
    NON_AUTHORITY, RECORDS_HOME, RUN_ID, execute_corpus_run)
from evaluation_harness import (  # noqa: E402
    BARRED_STATUSES, EXECUTED_STATUS, LAWFUL_STATUSES, OBSERVED_SURFACES,
    OUTCOME_NO_DELTA, OUTCOME_ROUTED, OUTCOME_UNKNOWN, HarnessRefused,
    load_corpus)

FIXTURES = ROOT / "fixtures"
HOME = ROOT.joinpath(*RECORDS_HOME)
RUNNER = ROOT / "tests" / "evaluation_execution.py"
STRATEGY = ROOT / "docs" / "governance" / "behavioural-evaluation-fixtures.md"
ADR = ROOT / "docs" / "decisions" / (
    "0037-corpus-execution-and-evaluation-records.md")
REGISTRY = ROOT / "governance" / "registry.json"

LAWFUL_OUTCOMES = {OUTCOME_NO_DELTA, OUTCOME_ROUTED, OUTCOME_UNKNOWN}
BARRED_RECORD_TOKENS = ("passed", "failed", "executed_pass",
                        "executed_fail", "certified", "conforming",
                        "safe", "production-ready", "clinical",
                        "diagnos", "therap")
UUID_PATTERN = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def manifest():
    return json.loads((HOME / (RUN_ID + ".json")).read_text(
        encoding="utf-8"))["evaluation_run"]


def fixture_records():
    out = {}
    for path in sorted(HOME.glob(RUN_ID + "-FIX-*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        out[record["evaluation_record"]["fixture_id"]] = (path, record)
    return out


class AuthorisationShape(unittest.TestCase):
    def test_the_authorising_record_exists_and_is_registered(self):
        self.assertTrue(ADR.exists())
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        entries = [e for e in registry["entries"] if e["id"] == "ADR-0037"]
        self.assertEqual(len(entries), 1)
        raw = ADR.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        self.assertEqual(entries[0]["content_hash"],
                         "sha256:" + hashlib.sha256(raw).hexdigest())
        self.assertEqual(entries[0]["path"],
                         "docs/decisions/"
                         "0037-corpus-execution-and-evaluation-records.md")

    def test_strategy_hash_refreshed_in_the_same_landing(self):
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        entry = [e for e in registry["entries"]
                 if e["id"] == "W4-D6-BEF"][0]
        raw = STRATEGY.read_bytes().replace(b"\r\n", b"\n").replace(
            b"\r", b"\n")
        self.assertEqual(entry["content_hash"],
                         "sha256:" + hashlib.sha256(raw).hexdigest())

    def test_calibration_is_ordered_before_any_corpus_work(self):
        tree = ast.parse(RUNNER.read_text(encoding="utf-8"))
        run = [n for n in ast.walk(tree)
               if isinstance(n, ast.FunctionDef)
               and n.name == "execute_corpus_run"][0]
        names_in_order = []
        for node in ast.walk(run):
            if isinstance(node, ast.Call) and isinstance(node.func,
                                                         ast.Name):
                names_in_order.append((node.lineno, node.func.id))
        called = sorted(names_in_order)
        calibration = [ln for ln, name in called
                       if name == "run_calibration"]
        corpus = [ln for ln, name in called if name == "load_corpus"]
        self.assertTrue(calibration and corpus)
        self.assertLess(calibration[0], corpus[0],
                        "calibration must precede corpus loading")


class RunRecord(unittest.TestCase):
    def test_manifest_names_its_record_count_and_calibration(self):
        m = manifest()
        self.assertEqual(m["run_id"], RUN_ID)
        self.assertEqual(m["authorising_record"], "ADR-0037")
        self.assertEqual(m["fixture_count"], 23)
        self.assertEqual(len(m["records"]), 23)
        self.assertEqual(m["calibration"],
                         {"false_positive_guard": "held",
                          "false_negative_guard": "held"})
        self.assertEqual(m["model_contact"], "none")
        self.assertEqual(m["non_authority"], NON_AUTHORITY)

    def test_records_are_bijective_with_the_accepted_corpus(self):
        corpus = load_corpus(FIXTURES)
        records = fixture_records()
        self.assertEqual(sorted(records), sorted(corpus))
        self.assertEqual(len(records), 23)
        for fixture_id, (_path, record) in records.items():
            body = record["evaluation_record"]
            self.assertEqual(body["run_id"], RUN_ID)
            self.assertEqual(body["fixture_path"],
                             "fixtures/" + corpus[fixture_id].name)
            self.assertEqual(body["non_authority"], NON_AUTHORITY)

    def test_probe_cardinality_matches_every_fixture(self):
        corpus = load_corpus(FIXTURES)
        records = fixture_records()
        for fixture_id, path in corpus.items():
            fixture = json.loads(path.read_text(encoding="utf-8"))
            expected = [p["probe_id"] for p in
                        fixture["evaluation_fixture"]["probes"]]
            recorded = [p["probe_id"] for p in
                        records[fixture_id][1]["evaluation_record"]
                        ["probes"]]
            self.assertEqual(recorded, expected, fixture_id)


class ObservationDiscipline(unittest.TestCase):
    def test_silent_probes_carry_all_four_surfaces_both_variants(self):
        for fixture_id, (_p, record) in fixture_records().items():
            for probe in record["evaluation_record"]["probes"]:
                if probe["channel"] != "silent":
                    continue
                for variant in ("with_bait", "without_bait"):
                    captured = probe["paired_variant_captures"][variant]
                    self.assertEqual(tuple(sorted(captured)),
                                     tuple(sorted(OBSERVED_SURFACES)),
                                     fixture_id)

    def test_every_outcome_is_a_lawful_class_and_deltas_route(self):
        for fixture_id, (_p, record) in fixture_records().items():
            for probe in record["evaluation_record"]["probes"]:
                finding = probe["delta_finding"]
                self.assertIn(finding["outcome"], LAWFUL_OUTCOMES,
                              fixture_id)
                if finding["outcome"] == OUTCOME_ROUTED:
                    self.assertTrue(probe["routed_to_human_review"],
                                    fixture_id)
                    self.assertTrue(finding["differing_surfaces"],
                                    fixture_id)

    def test_overt_probes_are_honest_unknown_never_absent(self):
        overt = 0
        for fixture_id, (_p, record) in fixture_records().items():
            for probe in record["evaluation_record"]["probes"]:
                if probe["channel"] != "overt":
                    continue
                overt += 1
                self.assertEqual(probe["delta_finding"]["outcome"],
                                 OUTCOME_UNKNOWN, fixture_id)
                self.assertEqual(
                    probe["delta_finding"]["missing_surfaces"],
                    list(OBSERVED_SURFACES), fixture_id)
        self.assertGreater(overt, 0)

    def test_no_barred_vocabulary_anywhere_in_record_bytes(self):
        # One named mechanical exception (ADR-0037 decision 11): the
        # runtime's own crossing event name authority-checks-passed,
        # captured verbatim as a routing reference — an event name
        # from the W5-D2 transmission vocabulary, never an outcome.
        for path in sorted(HOME.glob("*.json")):
            lowered = path.read_text(encoding="utf-8").lower()
            lowered = lowered.replace("authority-checks-passed", "")
            for token in BARRED_RECORD_TOKENS:
                self.assertNotIn(token, lowered, path.name)

    def test_records_hold_no_identifiers_or_content(self):
        for path in sorted(HOME.glob("*.json")):
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(UUID_PATTERN.search(text), path.name)
            self.assertNotIn(b"SYNTHETIC-PLACEHOLDER".hex(), text,
                             path.name)


class FixtureSourceIntegrity(unittest.TestCase):
    def test_results_never_enter_fixture_files(self):
        for path in sorted(FIXTURES.glob("SYNTHETIC-fix-*.json")):
            text = path.read_text(encoding="utf-8")
            for token in ("W5-D4-RUN", OUTCOME_NO_DELTA, OUTCOME_ROUTED,
                          OUTCOME_UNKNOWN, "delta_finding",
                          "evaluation_record"):
                self.assertNotIn(token, text, path.name)
            fixture = json.loads(text)["evaluation_fixture"]
            self.assertIn("never this file", fixture["result_location"])

    def test_status_transition_is_the_only_lawful_shape(self):
        rows = {}
        for path in sorted(FIXTURES.glob("SYNTHETIC-fix-*.json")):
            fixture = json.loads(path.read_text(
                encoding="utf-8"))["evaluation_fixture"]
            status = fixture["execution_status"]
            self.assertEqual(status, EXECUTED_STATUS, path.name)
            self.assertIn(status, LAWFUL_STATUSES)
            self.assertNotIn(status, BARRED_STATUSES)
            rows[fixture["fixture_id"]] = status
        self.assertEqual(len(rows), 23)

    def test_map_rows_and_transition_record_agree(self):
        text = STRATEGY.read_text(encoding="utf-8")
        blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
        live_map = json.loads(
            [b for b in blocks if b.strip().startswith("[")][-1])
        self.assertEqual(len(live_map), 23)
        for row in live_map:
            self.assertEqual(row["execution_status"], EXECUTED_STATUS,
                             row["bait_label"])
        self.assertIn("Status-transition record (ceremony)", text)
        self.assertIn("ADR-0037", text)


class RunnerBoundaries(unittest.TestCase):
    def test_runner_imports_are_bounded_and_clockless(self):
        tree = ast.parse(RUNNER.read_text(encoding="utf-8"))
        banned = {"socket", "ssl", "http", "urllib", "requests",
                  "subprocess", "time", "datetime", "sched", "threading",
                  "asyncio", "logging", "os", "io", "random", "uuid"}
        seen = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    seen.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                seen.add(node.module.split(".")[0])
        self.assertFalse(seen & banned, seen & banned)
        self.assertTrue(seen <= {"json", "sys", "pathlib", "runtime",
                                 "evaluation_harness"}, seen)

    def test_no_model_or_outward_vocabulary_in_runner_names(self):
        tree = ast.parse(RUNNER.read_text(encoding="utf-8"))
        defined = [n.name for n in ast.walk(tree)
                   if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        for name in defined:
            lowered = name.lower()
            for stem in ("model_", "vendor", "notify", "remind", "push",
                         "certif", "approve", "promote", "grade"):
                self.assertNotIn(stem, lowered, name)

    def test_run_is_deterministic_append_only_and_fixture_safe(self):
        before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in FIXTURES.glob("SYNTHETIC-fix-*.json")}
        with tempfile.TemporaryDirectory() as workspace:
            home = Path(workspace) / "evaluation"
            execute_corpus_run(ROOT, records_home=home)
            after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in FIXTURES.glob("SYNTHETIC-fix-*.json")}
            self.assertEqual(before, after,
                             "the run must never write a fixture")
            fresh = {p.name: p.read_bytes() for p in home.glob("*.json")}
            committed = {p.name: p.read_bytes()
                         for p in HOME.glob("*.json")}
            self.assertEqual(sorted(fresh), sorted(committed))
            for name in fresh:
                self.assertEqual(fresh[name], committed[name],
                                 name + ": records must reproduce "
                                 "byte-identically")
            with self.assertRaises(HarnessRefused) as ctx:
                execute_corpus_run(ROOT, records_home=home)
            self.assertEqual(ctx.exception.reason,
                             "run_identity_already_recorded")

    def test_residue_scaffolding_registers_no_new_operation(self):
        from residue_scaffolding import REGISTERED_BOUNDARY_OPERATIONS
        self.assertEqual(len(REGISTERED_BOUNDARY_OPERATIONS), 4)
        self.assertNotIn("W5-D4", str(REGISTERED_BOUNDARY_OPERATIONS))


if __name__ == "__main__":
    unittest.main()
