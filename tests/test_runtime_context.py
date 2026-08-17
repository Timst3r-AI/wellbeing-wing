"""Tier 1 — W5-D2-M04 processing-context structural proofs.

Structure only, never behaviour: construction, binding, lifetime,
observability, refusal, and the ADR 0035 residue lifecycle for the
first boundary operation that transiently holds governed-shaped
synthetic plaintext. All values are grammar placeholders; no proof
requires medical plausibility, and no residue failure output ever
prints the content it swept for.
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
from runtime.context import (  # noqa: E402
    CONTEXT_DOMAIN_BY_EDGE, ContextRefused, GrantBoundContent,
    ProcessingContext, ProcessingLedgerEvent)
from runtime.grants import GrantLifecycle, construct_grant  # noqa: E402

MARKER = b"SYNTHETIC-CONTEXT-MARKER-Persona-K9-Section-X"


def processing_elements(**overrides):
    base = dict(
        edge="E11-K", requesting_actor="kitchen-room-agent",
        recipient_class="local_model", data_class="C1",
        scope=("Section-Recipes-X", "Section-Staples-Y"),
        zones=("Z1", "Z3"), purpose="organise scoped placeholder records",
        operation="process", plaintext_flag=True,
        vendor_involvement="none", duration="single_task_session_max",
        revocation_behaviour="w1-d2-section-5-immediate-effects",
        audit_reference="ledger-ref-placeholder")
    base.update(overrides)
    return base


def active_context(**overrides):
    lifecycle = GrantLifecycle(construct_grant(**processing_elements(
        **overrides)))
    lifecycle.activate()
    return ProcessingContext(lifecycle)


def bound_for(context, section="Section-Recipes-X", content=MARKER):
    return GrantBoundContent(grant_id=context.grant.grant_id,
                             section=section, content=content)


class Construction(unittest.TestCase):
    def test_no_grant_no_context_and_inactive_refused(self):
        with self.assertRaises(ContextRefused) as ctx:
            ProcessingContext(object())
        self.assertEqual(ctx.exception.reason, "no_grant_no_context")
        lifecycle = GrantLifecycle(construct_grant(**processing_elements()))
        with self.assertRaises(ContextRefused) as ctx:
            ProcessingContext(lifecycle)
        self.assertEqual(ctx.exception.reason, "grant_not_active")

    def test_non_processing_edge_refused(self):
        lifecycle = GrantLifecycle(construct_grant(**processing_elements(
            edge="E6", recipient_class="internal", data_class="C3",
            zones=("Z1", "Z1"), operation="read", plaintext_flag=False,
            duration="standing_180_days")))
        lifecycle.activate()
        with self.assertRaises(ContextRefused) as ctx:
            ProcessingContext(lifecycle)
        self.assertEqual(ctx.exception.reason, "not_a_processing_edge")

    def test_vendor_hosted_recipient_refused(self):
        lifecycle = GrantLifecycle(construct_grant(**processing_elements(
            recipient_class="vendor_hosted_model")))
        lifecycle.activate()
        with self.assertRaises(ContextRefused) as ctx:
            ProcessingContext(lifecycle)
        self.assertEqual(ctx.exception.reason,
                         "recipient_class_not_processable")

    def test_room_is_a_function_of_the_edge_never_a_parameter(self):
        params = list(inspect.signature(
            ProcessingContext.__init__).parameters)
        self.assertEqual(params, ["self", "lifecycle"])
        self.assertEqual(CONTEXT_DOMAIN_BY_EDGE["E11-K"], "kitchen")
        self.assertEqual(CONTEXT_DOMAIN_BY_EDGE["M2"], "meditation")
        self.assertEqual(active_context().domain, "kitchen")

    def test_no_method_accepts_a_second_context_or_grant(self):
        for name, member in inspect.getmembers(
                ProcessingContext, predicate=inspect.isfunction):
            if name == "__init__":
                continue
            for param in inspect.signature(member).parameters.values():
                self.assertNotIn(param.name,
                                 ("context", "other", "grant", "lifecycle"),
                                 f"composition-shaped parameter on {name}")


class ContentBinding(unittest.TestCase):
    def test_free_content_refused(self):
        context = active_context()
        with self.assertRaises(ContextRefused) as ctx:
            context.receive(b"raw synthetic bytes")
        self.assertEqual(ctx.exception.reason, "no_free_content_interface")

    def test_content_bound_to_another_grant_refused(self):
        context_a = active_context()
        context_b = active_context()
        stray = bound_for(context_b)
        with self.assertRaises(ContextRefused) as ctx:
            context_a.receive(stray)
        self.assertEqual(ctx.exception.reason,
                         "content_not_bound_to_this_grant")

    def test_out_of_scope_section_has_no_path_in(self):
        context = active_context()
        with self.assertRaises(ContextRefused) as ctx:
            context.receive(bound_for(context, section="Section-Other-Z"))
        self.assertEqual(ctx.exception.reason,
                         "content_outside_grant_scope")

    def test_lawful_bound_content_held_by_section_name(self):
        context = active_context()
        context.receive(bound_for(context))
        self.assertEqual(context.report().presented_sections,
                         ("Section-Recipes-X",))


class Lifecycle(unittest.TestCase):
    def test_end_clears_holdings_and_absence_is_demonstrable(self):
        context = active_context()
        context.receive(bound_for(context))
        self.assertEqual(len(context.post_context_state()), 1)
        context.end()
        self.assertEqual(context.post_context_state(), ())

    def test_ended_context_refuses_receive_and_double_end(self):
        context = active_context()
        context.end()
        with self.assertRaises(ContextRefused):
            context.receive(bound_for(context))
        with self.assertRaises(ContextRefused):
            context.end()

    def test_revocation_ends_the_context(self):
        context = active_context()
        context.receive(bound_for(context))
        context.revoke()
        self.assertTrue(context.ended)
        self.assertEqual(context.post_context_state(), ())
        self.assertEqual(context.events[-1].event, "context-ended")

    def test_unknown_end_cause_refused(self):
        context = active_context()
        with self.assertRaises(ContextRefused):
            context.end(cause="timeout-like-thing")

    def test_no_reuse_a_fresh_context_holds_nothing_of_an_earlier_one(self):
        first = active_context()
        first.receive(bound_for(first))
        first.end()
        second = active_context()
        self.assertEqual(second.report().presented_sections, ())
        self.assertEqual(second.post_context_state(), ())


class Observability(unittest.TestCase):
    def test_spoken_output_surface_reports_by_section_name(self):
        context = active_context()
        context.receive(bound_for(context))
        report = context.report()
        self.assertEqual(report.presented_sections, ("Section-Recipes-X",))
        self.assertEqual(report.returned, "nothing-returned-no-output-path")

    def test_destination_enumeration_is_empty_by_construction(self):
        context = active_context()
        context.receive(bound_for(context))
        self.assertEqual(context.destinations_written(), ())

    def test_paired_variant_construction_is_supported(self):
        with_bait = active_context()
        with_bait.receive(bound_for(with_bait))
        with_bait.receive(bound_for(with_bait, section="Section-Staples-Y",
                                    content=b"SYNTHETIC-BAIT-B7"))
        without_bait = active_context()
        without_bait.receive(bound_for(without_bait))
        delta = (set(with_bait.report().presented_sections)
                 - set(without_bait.report().presented_sections))
        self.assertEqual(delta, {"Section-Staples-Y"})

    def test_ledger_events_are_content_free(self):
        context = active_context()
        context.receive(bound_for(context))
        context.end()
        self.assertEqual([e.event for e in context.events],
                         ["context-created", "context-ended"])
        for event in context.events:
            self.assertIsInstance(event, ProcessingLedgerEvent)
            for value in dataclass_values(event):
                self.assertNotIn(MARKER.decode(), str(value))

    def test_refusal_writes_no_state_and_echoes_no_content(self):
        context = active_context()
        context.receive(bound_for(context))
        events_before = context.events
        held_before = context.post_context_state()
        try:
            context.receive(bound_for(context, section="Section-Other-Z",
                                      content=MARKER))
        except ContextRefused as exc:
            self.assertNotIn(MARKER.decode(), str(exc))
        self.assertEqual(context.events, events_before)
        self.assertEqual(context.post_context_state(), held_before)


def dataclass_values(instance):
    import dataclasses
    return dataclasses.asdict(instance).values()


class StructuralAbsences(unittest.TestCase):
    def test_no_io_clock_logging_or_engine_import(self):
        tree = ast.parse((ROOT / "runtime" / "context.py").read_text(
            encoding="utf-8"))
        banned_modules = {"time", "datetime", "sched", "threading",
                          "asyncio", "logging", "os", "pathlib", "io",
                          "engine", "subprocess"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.assertNotIn(alias.name.split(".")[0],
                                     banned_modules)
            elif isinstance(node, ast.ImportFrom) and node.module:
                self.assertNotIn(node.module.split(".")[0], banned_modules)
            elif isinstance(node, ast.Call) and isinstance(
                    node.func, ast.Name):
                self.assertNotIn(node.func.id, ("open", "print", "exec",
                                                "eval"))

    def test_no_fetch_store_queue_or_outward_name_exists(self):
        banned_stems = ("fetch", "load", "read_store", "notice", "flag",
                        "queue", "review_store", "merge", "extend_context",
                        "chain", "combine", "compose", "registry", "cache",
                        "pool", "notify", "notification", "remind", "push",
                        "email", "sms", "webhook", "subscribe", "dispatch",
                        "deliver", "write_to")
        tree = ast.parse((ROOT / "runtime" / "context.py").read_text(
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
                                 "barred vocabulary in defined name: "
                                 + name)

    def test_boundary_operation_registered_by_record(self):
        self.assertIn(("processing-context-lifecycle", "W5-D2-M04"),
                      REGISTERED_BOUNDARY_OPERATIONS)


class ResidueLifecycle(unittest.TestCase):
    def test_normal_termination_leaves_no_readable_residue(self):
        with tempfile.TemporaryDirectory() as workspace:
            context = active_context()
            context.receive(bound_for(context, content=MARKER))
            context.end()
            self.assertEqual(context.post_context_state(), ())
            files = [p for p in Path(workspace).rglob("*") if p.is_file()]
            self.assertEqual(files, [],
                             "context lifecycle wrote a file")
            self.assertEqual(sweep_locations(workspace, MARKER), [])

    def test_kill_termination_leaves_no_readable_residue(self):
        child = (
            "import sys, time\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "sys.path.insert(0, sys.argv[1] + '/tests')\n"
            "from tests.test_runtime_context import (active_context, "
            "bound_for, MARKER)\n"
            "context = active_context()\n"
            "context.receive(bound_for(context, content=MARKER))\n"
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
            self.assertEqual(names, ["ready.txt"],
                             "kill path left unexpected files")
            self.assertEqual(sweep_locations(workspace, MARKER), [])


if __name__ == "__main__":
    unittest.main()
