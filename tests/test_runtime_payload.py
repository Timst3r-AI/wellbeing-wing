"""Tier 1 — W5-D2-M05 payload assembly and equality structural proofs.

Structure only, never behaviour: assembly refusal shapes, the three
governed comparisons, content-free fingerprints, the ADR 0036 cascade
obligations at the assembly door, and the ADR 0035 residue lifecycle
for the payload-assembly boundary operation. All values are grammar
placeholders; residue output reports locations only, never content.
"""

import ast
import inspect
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from residue_scaffolding import (  # noqa: E402
    REGISTERED_BOUNDARY_OPERATIONS, sweep_locations)
from runtime.payload import (  # noqa: E402
    ComparisonRecord, Payload, PayloadRefused, assemble_payload,
    compare_across_transformation, compare_at_last_controllable_point,
    compare_scope_to_payload, payload_fingerprint, require_equal,
    serialise_payload)
from tests.test_runtime_context import (  # noqa: E402
    MARKER, active_context, bound_for)


def assembled(**overrides):
    context = active_context(**overrides)
    context.receive(bound_for(context, section="Section-Recipes-X"))
    context.receive(bound_for(context, section="Section-Staples-Y",
                              content=b"SYNTHETIC-Staples-B2"))
    return context, assemble_payload(context)


class AssemblyConstructability(unittest.TestCase):
    def test_assembly_only_from_a_live_processing_context(self):
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(object())
        self.assertEqual(ctx.exception.reason, "no_context_no_payload")
        context = active_context()
        context.receive(bound_for(context))
        context.end()
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(context)
        self.assertEqual(ctx.exception.reason, "context_ended")

    def test_nothing_held_refused(self):
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(active_context())
        self.assertEqual(ctx.exception.reason, "nothing_held_to_assemble")

    def test_scope_subset_is_a_mismatch(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X"))
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(context)
        self.assertEqual(ctx.exception.reason, "payload_scope_mismatch")

    def test_duplicate_section_refused(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X"))
        context.receive(bound_for(context, section="Section-Recipes-X"))
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(context)
        self.assertEqual(ctx.exception.reason, "duplicate_section")

    def test_multi_grant_payload_is_unexpressible(self):
        params = list(inspect.signature(assemble_payload).parameters)
        self.assertEqual(params[0], "context")
        self.assertNotIn("contexts", params)
        self.assertNotIn("other", params)
        self.assertNotIn("grant", params)

    def test_granted_scope_is_the_whole_payload(self):
        _context, payload = assembled()
        self.assertEqual([name for name, _ in payload.sections],
                         ["Section-Recipes-X", "Section-Staples-Y"])

    def test_label_outside_payload_refused(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X"))
        context.receive(bound_for(context, section="Section-Staples-Y"))
        with self.assertRaises(PayloadRefused):
            assemble_payload(context, freshness_labels=(
                ("Section-Other-Z", "stale"),))


class CascadeObligations(unittest.TestCase):
    def test_invalidated_input_refused_by_reference(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X"))
        context.receive(bound_for(context, section="Section-Staples-Y"))
        with self.assertRaises(PayloadRefused) as ctx:
            assemble_payload(context,
                             invalidated_refs=("Section-Recipes-X",))
        self.assertEqual(ctx.exception.reason, "invalidated_input")

    def test_payload_records_grant_lineage_at_creation(self):
        context, payload = assembled()
        self.assertEqual(payload.grant_id, context.grant.grant_id)
        self.assertEqual(payload.predecessor_grant_id, "")

    def test_no_deletion_api_and_no_rederivation_api_exists(self):
        import runtime.payload as module
        tree = ast.parse((ROOT / "runtime" / "payload.py").read_text(
            encoding="utf-8"))
        defined = [n.name for n in ast.walk(tree)
                   if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        for name in defined:
            for stem in ("delete", "remove", "erase", "purge_user",
                         "rederive", "derive_from_payload"):
                self.assertNotIn(stem, name.lower())
        for name, member in inspect.getmembers(module,
                                               inspect.isfunction):
            for param in inspect.signature(member).parameters.values():
                self.assertNotIn(param.name, ("payload_source",
                                              "source_payload"))

    def test_marks_are_content_free_references(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X",
                                  content=MARKER))
        context.receive(bound_for(context, section="Section-Staples-Y"))
        try:
            assemble_payload(context,
                             invalidated_refs=("Section-Recipes-X",))
        except PayloadRefused as exc:
            self.assertNotIn(MARKER.decode(), str(exc))


class GovernedEquality(unittest.TestCase):
    def test_serialisation_is_deterministic(self):
        _context, payload = assembled()
        self.assertEqual(serialise_payload(payload),
                         serialise_payload(payload))

    def test_comparison_one_scope_to_payload(self):
        context, payload = assembled()
        record = compare_scope_to_payload(context.grant, payload)
        self.assertTrue(record.outcome)
        other_context, other_payload = assembled()
        cross = compare_scope_to_payload(context.grant, other_payload)
        self.assertFalse(cross.outcome)

    def test_comparison_two_byte_level_at_last_controllable_point(self):
        _context, payload = assembled()
        presented = serialise_payload(payload)
        self.assertTrue(compare_at_last_controllable_point(
            payload, presented).outcome)
        tampered = presented[:-2] + b"x}"
        self.assertFalse(compare_at_last_controllable_point(
            payload, tampered).outcome)

    def test_comparison_three_across_transformation(self):
        _context, payload = assembled()
        before = serialise_payload(payload)
        self.assertTrue(compare_across_transformation(
            before, bytes(before)).outcome)
        self.assertFalse(compare_across_transformation(
            before, before + b" ").outcome)

    def test_similarity_never_satisfies_equality(self):
        context_a, payload_a = assembled()
        context_b = active_context()
        context_b.receive(bound_for(context_b,
                                    section="Section-Recipes-X",
                                    content=b"SYNTHETIC-DIFFERENT-K1"))
        context_b.receive(bound_for(context_b,
                                    section="Section-Staples-Y"))
        payload_b = assemble_payload(context_b)
        self.assertEqual(
            [n for n, _ in payload_a.sections],
            [n for n, _ in payload_b.sections])
        self.assertFalse(compare_across_transformation(
            serialise_payload(payload_a),
            serialise_payload(payload_b)).outcome)

    def test_unproven_refuses_the_dependent_operation(self):
        _context, payload = assembled()
        bad = compare_at_last_controllable_point(
            payload, b"not-the-payload")
        with self.assertRaises(PayloadRefused) as ctx:
            require_equal(bad)
        self.assertEqual(ctx.exception.reason, "equality_unproven")
        with self.assertRaises(PayloadRefused):
            require_equal(None)

    def test_fingerprints_are_content_free_fixed_length(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X",
                                  content=MARKER))
        context.receive(bound_for(context, section="Section-Staples-Y"))
        payload = assemble_payload(context)
        record = compare_at_last_controllable_point(
            payload, serialise_payload(payload))
        for fp in (record.fingerprint_a, record.fingerprint_b):
            self.assertEqual(len(fp), 64)
            self.assertNotIn(MARKER.decode(), fp)


class NoStandingPayload(unittest.TestCase):
    def test_no_module_level_mutable_container(self):
        tree = ast.parse((ROOT / "runtime" / "payload.py").read_text(
            encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.Assign):
                self.assertNotIsInstance(node.value,
                                         (ast.List, ast.Dict, ast.Set),
                                         "module-level mutable container")

    def test_assembling_twice_yields_distinct_payloads(self):
        context = active_context()
        context.receive(bound_for(context, section="Section-Recipes-X"))
        context.receive(bound_for(context, section="Section-Staples-Y"))
        first = assemble_payload(context)
        second = assemble_payload(context)
        self.assertNotEqual(first.payload_id, second.payload_id)


class StructuralAbsences(unittest.TestCase):
    def test_imports_and_calls_are_pure(self):
        tree = ast.parse((ROOT / "runtime" / "payload.py").read_text(
            encoding="utf-8"))
        banned = {"time", "datetime", "sched", "threading", "asyncio",
                  "logging", "os", "pathlib", "io", "engine",
                  "subprocess", "socket"}
        allowed = {"hashlib", "json", "uuid", "dataclasses", "runtime"}
        seen = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    seen.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                seen.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call) and isinstance(
                    node.func, ast.Name):
                self.assertNotIn(node.func.id, ("open", "print",
                                                "exec", "eval"))
        self.assertFalse(seen & banned, seen & banned)
        self.assertTrue(seen <= allowed, seen - allowed)

    def test_no_outward_or_crossing_name_exists(self):
        banned_stems = ("transmit", "send", "crossing", "deliver",
                        "dispatch", "notify", "notification", "remind",
                        "push", "email", "sms", "webhook", "subscribe",
                        "vendor_call", "model_call", "fetch", "registry",
                        "cache", "pool")
        tree = ast.parse((ROOT / "runtime" / "payload.py").read_text(
            encoding="utf-8"))
        defined = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                 ast.ClassDef)):
                defined.append(node.name)
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
                                 "barred vocabulary: " + name)

    def test_boundary_operation_registered_by_record(self):
        self.assertIn(("payload-assembly", "W5-D2-M05"),
                      REGISTERED_BOUNDARY_OPERATIONS)


class ResidueLifecycle(unittest.TestCase):
    def test_normal_termination_leaves_no_readable_residue(self):
        with tempfile.TemporaryDirectory() as workspace:
            context = active_context()
            context.receive(bound_for(context,
                                      section="Section-Recipes-X",
                                      content=MARKER))
            context.receive(bound_for(context,
                                      section="Section-Staples-Y"))
            payload = assemble_payload(context)
            serialise_payload(payload)
            context.end()
            del payload
            files = [p for p in Path(workspace).rglob("*")
                     if p.is_file()]
            self.assertEqual(files, [])
            self.assertEqual(sweep_locations(workspace, MARKER), [])

    def test_kill_termination_leaves_no_readable_residue(self):
        child = (
            "import sys, time\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "sys.path.insert(0, sys.argv[1] + '/tests')\n"
            "from tests.test_runtime_context import (active_context, "
            "bound_for, MARKER)\n"
            "from runtime.payload import assemble_payload, "
            "serialise_payload\n"
            "context = active_context()\n"
            "context.receive(bound_for(context, "
            "section='Section-Recipes-X', content=MARKER))\n"
            "context.receive(bound_for(context, "
            "section='Section-Staples-Y'))\n"
            "payload = assemble_payload(context)\n"
            "serialise_payload(payload)\n"
            "open('ready.txt', 'w').write('ready')\n"
            "time.sleep(60)\n")
        with tempfile.TemporaryDirectory() as workspace:
            env = dict(os.environ)
            env["PYTHONPATH"] = str(ROOT)
            process = subprocess.Popen(
                [sys.executable, "-c", child, str(ROOT)],
                cwd=workspace, env=env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            try:
                deadline = time.time() + 30
                sentinel = Path(workspace) / "ready.txt"
                while not sentinel.exists():
                    self.assertLess(time.time(), deadline,
                                    "child never reached ready state")
                    time.sleep(0.1)
            finally:
                process.kill()
                process.wait(timeout=30)
            names = sorted(p.name for p in Path(workspace).rglob("*")
                           if p.is_file())
            self.assertEqual(names, ["ready.txt"])
            self.assertEqual(sweep_locations(workspace, MARKER), [])


if __name__ == "__main__":
    unittest.main()
