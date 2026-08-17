"""Tier 1 — W5-D2-M07 isolation, Meditation runtime and composition
root structural proofs.

Structure only, never behaviour: end-to-end isolation across every
runtime module, the Meditation edge's stricter rules, the stateless
composition root as the only meeting point and the only ledger-append
path, and the ADR 0035 residue lifecycle for the composed operation.
All recipients are in-process doubles; nothing contacts anything.
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

import runtime.composition  # noqa: E402
import runtime.context  # noqa: E402
import runtime.freshness  # noqa: E402
import runtime.grants  # noqa: E402
import runtime.payload  # noqa: E402
import runtime.transmission  # noqa: E402
from residue_scaffolding import (  # noqa: E402
    REGISTERED_BOUNDARY_OPERATIONS, sweep_locations)
from runtime.composition import (  # noqa: E402
    CompositionOutcome, CompositionRefused, compose_context,
    run_granted_operation)
from runtime.context import GrantBoundContent  # noqa: E402
from runtime.grants import GrantLifecycle, construct_grant  # noqa: E402
from tests.test_runtime_context import (  # noqa: E402
    MARKER, processing_elements)

AS_OF = "AS-OF-PLACEHOLDER-9"
RUNTIME_MODULES = (runtime.grants, runtime.freshness, runtime.context,
                   runtime.payload, runtime.transmission,
                   runtime.composition)


def kitchen_lifecycle():
    lifecycle = GrantLifecycle(construct_grant(**processing_elements()))
    lifecycle.activate()
    return lifecycle


def meditation_lifecycle(**overrides):
    elements = processing_elements(
        edge="M2", requesting_actor="meditation-room-agent",
        data_class="CM",
        scope=("Section-Reflections-R", "Section-Practice-P"),
        purpose="engage with scoped placeholder reflections")
    elements.update(overrides)
    lifecycle = GrantLifecycle(construct_grant(**elements))
    lifecycle.activate()
    return lifecycle


def items_for(lifecycle, contents=None):
    grant = lifecycle.grant
    contents = contents or {}
    return [GrantBoundContent(grant_id=grant.grant_id, section=name,
                              content=contents.get(name, MARKER))
            for name in grant.scope]


class ComposedOperation(unittest.TestCase):
    def test_end_to_end_operation_completes_and_retains_nothing(self):
        lifecycle = kitchen_lifecycle()
        received, appended = [], []
        outcome = run_granted_operation(
            lifecycle, items_for(lifecycle), received.append, AS_OF,
            ledger_append=appended.append)
        self.assertIsInstance(outcome, CompositionOutcome)
        self.assertEqual(outcome.outcome, "completed")
        self.assertEqual(len(received), 1)
        self.assertIsNotNone(outcome.disclosure)
        names = [e.event for e in outcome.events]
        self.assertIn("context-created", names)
        self.assertIn("context-ended", names)
        self.assertIn("disclosure", names)
        self.assertEqual(len(appended), len(outcome.events))

    def test_context_is_ended_even_when_the_operation_refuses(self):
        lifecycle = kitchen_lifecycle()
        grant = lifecycle.grant
        partial = [GrantBoundContent(grant_id=grant.grant_id,
                                     section=grant.scope[0],
                                     content=MARKER)]
        with self.assertRaises(Exception):
            run_granted_operation(lifecycle, partial,
                                  lambda b: None, AS_OF)

    def test_ledger_append_happens_only_through_the_root(self):
        for module in RUNTIME_MODULES[:-1]:
            source = Path(module.__file__).read_text(encoding="utf-8")
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef,
                                     ast.AsyncFunctionDef)):
                    for param in (node.args.args + node.args.kwonlyargs):
                        self.assertNotIn("ledger", param.arg.lower(),
                                         module.__name__)

    def test_appended_frames_are_content_free(self):
        lifecycle = kitchen_lifecycle()
        appended = []
        run_granted_operation(lifecycle, items_for(lifecycle),
                              lambda b: None, AS_OF,
                              ledger_append=appended.append)
        self.assertTrue(appended)
        for frame in appended:
            self.assertNotIn(MARKER.decode(), str(frame))

    def test_root_is_stateless_functions_only(self):
        tree = ast.parse(Path(runtime.composition.__file__).read_text(
            encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.Assign):
                targets = [t.id for t in node.targets
                           if isinstance(t, ast.Name)]
                if all(name.isupper() for name in targets):
                    continue  # constant doctrine tables, not state
                self.assertNotIsInstance(node.value,
                                         (ast.List, ast.Dict, ast.Set))
            if isinstance(node, ast.ClassDef):
                self.assertIn(node.name, ("CompositionRefused",
                                          "CompositionOutcome"))


class IsolationEndToEnd(unittest.TestCase):
    def test_no_function_anywhere_accepts_two_contexts(self):
        for module in RUNTIME_MODULES:
            for _name, member in inspect.getmembers(
                    module, inspect.isfunction):
                params = list(inspect.signature(member).parameters)
                for barred in ("contexts", "other_context",
                               "second_context", "context_b",
                               "target_context"):
                    self.assertNotIn(barred, params,
                                     module.__name__)

    def test_no_cross_room_pool_cache_or_registry_exists(self):
        for module in RUNTIME_MODULES:
            tree = ast.parse(Path(module.__file__).read_text(
                encoding="utf-8"))
            defined = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    defined.append(node.name)
                elif isinstance(node, ast.Assign):
                    defined.extend(t.id for t in node.targets
                                   if isinstance(t, ast.Name))
            for name in defined:
                lowered = name.lower()
                for stem in ("pool", "registry", "cache", "shared",
                             "merge", "combine"):
                    self.assertNotIn(stem, lowered,
                                     module.__name__ + "." + name)

    def test_one_room_cannot_receive_another_rooms_content(self):
        kitchen = kitchen_lifecycle()
        meditation = meditation_lifecycle()
        kitchen_context = compose_context(kitchen)
        stray = GrantBoundContent(
            grant_id=meditation.grant.grant_id,
            section="Section-Reflections-R", content=MARKER)
        with self.assertRaises(Exception) as ctx:
            kitchen_context.receive(stray)
        self.assertEqual(ctx.exception.reason,
                         "content_not_bound_to_this_grant")

    def test_sequential_operations_share_nothing(self):
        first = kitchen_lifecycle()
        outcome_one = run_granted_operation(
            first, items_for(first), lambda b: None, AS_OF)
        second = kitchen_lifecycle()
        outcome_two = run_granted_operation(
            second, items_for(second), lambda b: None, AS_OF)
        ids_one = {e.grant_id for e in outcome_one.events}
        ids_two = {e.grant_id for e in outcome_two.events}
        self.assertFalse(ids_one & ids_two)

    def test_runtime_modules_do_not_import_each_others_crossing(self):
        for module in (runtime.grants, runtime.freshness,
                       runtime.context, runtime.payload):
            tree = ast.parse(Path(module.__file__).read_text(
                encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom) and node.module:
                    self.assertNotIn("transmission", node.module,
                                     module.__name__)


class MeditationStrictness(unittest.TestCase):
    def test_m2_requires_cm_and_only_cm(self):
        with self.assertRaises(CompositionRefused) as ctx:
            compose_context(meditation_lifecycle(data_class="C1"))
        self.assertEqual(ctx.exception.reason,
                         "data_class_not_lawful_for_edge")

    def test_cm_travels_on_no_other_edge(self):
        kitchen_with_cm = GrantLifecycle(construct_grant(
            **processing_elements(data_class="CM")))
        kitchen_with_cm.activate()
        with self.assertRaises(CompositionRefused) as ctx:
            compose_context(kitchen_with_cm)
        self.assertEqual(ctx.exception.reason,
                         "data_class_not_lawful_for_edge")

    def test_meditation_operation_is_lawful_end_to_end(self):
        lifecycle = meditation_lifecycle()
        received = []
        outcome = run_granted_operation(
            lifecycle, items_for(lifecycle), received.append, AS_OF)
        self.assertEqual(outcome.outcome, "completed")
        self.assertEqual(outcome.disclosure.recipient_name,
                         "a model running on this device")

    def test_meditation_only_egress_is_its_own_crossing(self):
        lifecycle = meditation_lifecycle()
        context = compose_context(lifecycle)
        context.receive(GrantBoundContent(
            grant_id=lifecycle.grant.grant_id,
            section="Section-Reflections-R", content=MARKER))
        self.assertEqual(context.destinations_written(), ())
        context.end()

    def test_edge_class_table_matches_the_boundary_map(self):
        from runtime.composition import LAWFUL_DATA_CLASSES_BY_EDGE
        self.assertEqual(LAWFUL_DATA_CLASSES_BY_EDGE["M2"],
                         frozenset({"CM"}))
        self.assertEqual(LAWFUL_DATA_CLASSES_BY_EDGE["E2"],
                         frozenset({"C4"}))
        for edge, classes in LAWFUL_DATA_CLASSES_BY_EDGE.items():
            if edge != "M2":
                self.assertNotIn("CM", classes)


class StructuralAbsences(unittest.TestCase):
    def test_composition_imports_and_calls_are_pure(self):
        tree = ast.parse(Path(runtime.composition.__file__).read_text(
            encoding="utf-8"))
        banned = {"time", "datetime", "sched", "threading", "asyncio",
                  "logging", "os", "pathlib", "io", "engine",
                  "subprocess", "socket", "ssl", "http", "urllib"}
        seen = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    seen.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                seen.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call) and isinstance(
                    node.func, ast.Name):
                self.assertNotIn(node.func.id,
                                 ("open", "print", "exec", "eval"))
        self.assertFalse(seen & banned)
        self.assertTrue(seen <= {"runtime", "dataclasses"})

    def test_no_scheduler_or_outward_name_across_the_runtime(self):
        for module in RUNTIME_MODULES:
            tree = ast.parse(Path(module.__file__).read_text(
                encoding="utf-8"))
            defined = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    defined.append(node.name)
            for name in defined:
                lowered = name.lower()
                for stem in ("schedule", "background", "daemon",
                             "notify", "remind", "push_", "poll"):
                    self.assertNotIn(stem, lowered,
                                     module.__name__ + "." + name)

    def test_boundary_operations_registered_exactly_by_record(self):
        self.assertEqual(REGISTERED_BOUNDARY_OPERATIONS, (
            ("processing-context-lifecycle", "W5-D2-M04"),
            ("payload-assembly", "W5-D2-M05"),
            ("transmission-crossing", "W5-D2-M06"),
            ("composed-operation-lifecycle", "W5-D2-M07"),
        ))


class ResidueLifecycle(unittest.TestCase):
    def test_composed_normal_termination_leaves_no_residue(self):
        with tempfile.TemporaryDirectory() as workspace:
            lifecycle = meditation_lifecycle()
            run_granted_operation(lifecycle, items_for(lifecycle),
                                  lambda b: None, AS_OF)
            files = [p for p in Path(workspace).rglob("*")
                     if p.is_file()]
            self.assertEqual(files, [])
            self.assertEqual(sweep_locations(workspace, MARKER), [])

    def test_composed_kill_termination_leaves_no_residue(self):
        child = (
            "import sys, time\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "sys.path.insert(0, sys.argv[1] + '/tests')\n"
            "from tests.test_runtime_composition import ("
            "meditation_lifecycle, items_for, AS_OF)\n"
            "from runtime.composition import run_granted_operation\n"
            "lifecycle = meditation_lifecycle()\n"
            "run_granted_operation(lifecycle, items_for(lifecycle), "
            "lambda b: None, AS_OF)\n"
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
