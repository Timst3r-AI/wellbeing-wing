"""Tier 1 — W5-D2-M06 transmission and disclosure structural proofs.

Structure only, never behaviour: the third gate, per-attempt consumed
authority, boundary re-proof, honest partial crossings, content-free
disclosure records, the seven-attribute retry identity, and the ADR
0035 residue lifecycle for the crossing operation. All recipients are
in-process structural doubles; nothing here contacts anything.
"""

import ast
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
    assemble_payload, compare_at_last_controllable_point,
    serialise_payload)
from runtime.transmission import (  # noqa: E402
    CrossingResult, DisclosureRecord, TransmissionAuthorisation,
    TransmissionRefused, cross, same_bounded_event)
from tests.test_runtime_context import (  # noqa: E402
    MARKER, active_context, bound_for)

AS_OF = "AS-OF-PLACEHOLDER-7"


def ready_pair(**overrides):
    context = active_context(**overrides)
    context.receive(bound_for(context, section="Section-Recipes-X",
                              content=MARKER))
    context.receive(bound_for(context, section="Section-Staples-Y",
                              content=b"SYNTHETIC-Staples-B2"))
    payload = assemble_payload(context)
    record = compare_at_last_controllable_point(
        payload, serialise_payload(payload))
    return context, payload, record


def authorised(**overrides):
    context, payload, record = ready_pair(**overrides)
    return context, payload, TransmissionAuthorisation(
        context, payload, record, AS_OF)


class ThirdGate(unittest.TestCase):
    def test_no_payload_no_transmission(self):
        context, payload, record = ready_pair()
        with self.assertRaises(TransmissionRefused) as ctx:
            TransmissionAuthorisation(context, b"raw", record, AS_OF)
        self.assertEqual(ctx.exception.reason,
                         "no_payload_no_transmission")

    def test_no_equality_proof_no_transmission(self):
        context, payload, _record = ready_pair()
        bad = compare_at_last_controllable_point(payload, b"other")
        for record in (None, bad):
            with self.assertRaises(TransmissionRefused) as ctx:
                TransmissionAuthorisation(context, payload, record, AS_OF)
            self.assertEqual(ctx.exception.reason, "equality_unproven")

    def test_ended_context_and_foreign_payload_refused(self):
        context_a, payload_a, record_a = ready_pair()
        context_b, _payload_b, _record_b = ready_pair()
        with self.assertRaises(TransmissionRefused) as ctx:
            TransmissionAuthorisation(context_b, payload_a, record_a,
                                      AS_OF)
        self.assertEqual(ctx.exception.reason,
                         "payload_not_bound_to_this_grant")
        context_a.end()
        with self.assertRaises(TransmissionRefused) as ctx:
            TransmissionAuthorisation(context_a, payload_a, record_a,
                                      AS_OF)
        self.assertEqual(ctx.exception.reason, "context_ended")

    def test_invalidated_payload_refused(self):
        context, payload, record = ready_pair()
        with self.assertRaises(TransmissionRefused) as ctx:
            TransmissionAuthorisation(
                context, payload, record, AS_OF,
                invalidated_payload_ids=(payload.payload_id,))
        self.assertEqual(ctx.exception.reason, "invalidated_payload")

    def test_recipient_is_nameable_in_grant_terms(self):
        _context, _payload, authorisation = authorised()
        self.assertEqual(authorisation.recipient_name,
                         "a model running on this device")


class CrossingMechanics(unittest.TestCase):
    def test_lawful_crossing_delivers_exactly_the_canonical_bytes(self):
        _context, payload, authorisation = authorised()
        received = []
        result = cross(authorisation, payload, received.append, AS_OF)
        self.assertEqual(result.outcome, "completed")
        self.assertEqual(received, [serialise_payload(payload)])

    def test_disclosure_record_produced_with_crossing_content_free(self):
        _context, payload, authorisation = authorised()
        result = cross(authorisation, payload, lambda b: None, AS_OF)
        record = result.disclosure
        self.assertIsInstance(record, DisclosureRecord)
        self.assertEqual(record.scope_sections,
                         ("Section-Recipes-X", "Section-Staples-Y"))
        self.assertEqual(record.recipient_class, "local_model")
        self.assertEqual(record.as_of, AS_OF)
        for value in (record.actor, record.purpose,
                      record.payload_fingerprint, str(record)):
            self.assertNotIn(MARKER.decode(), str(value))

    def test_no_authority_and_consumed_authority_refused(self):
        _context, payload, authorisation = authorised()
        with self.assertRaises(TransmissionRefused) as ctx:
            cross(object(), payload, lambda b: None, AS_OF)
        self.assertEqual(ctx.exception.reason, "no_authority_no_crossing")
        cross(authorisation, payload, lambda b: None, AS_OF)
        with self.assertRaises(TransmissionRefused) as ctx:
            cross(authorisation, payload, lambda b: None, AS_OF)
        self.assertEqual(ctx.exception.reason, "authority_not_reusable")

    def test_refusal_before_boundary_produces_no_disclosure(self):
        context, payload, record = ready_pair()
        authorisation = TransmissionAuthorisation(context, payload,
                                                  record, AS_OF)
        tampered_context = active_context()
        tampered_context.receive(bound_for(tampered_context,
                                           section="Section-Recipes-X"))
        tampered_context.receive(bound_for(tampered_context,
                                           section="Section-Staples-Y"))
        other_payload = assemble_payload(tampered_context)
        result = cross(authorisation, other_payload,
                       lambda b: None, AS_OF)
        self.assertEqual(result.outcome, "refused-before-boundary")
        self.assertIsNone(result.disclosure)
        self.assertEqual([e.event for e in result.events],
                         ["transmission-attempt", "transmission-refusal"])

    def test_partial_crossing_is_a_crossing_recorded_honestly(self):
        _context, payload, authorisation = authorised()

        def failing_recipient(data):
            failing_recipient.received = data
            raise RuntimeError("synthetic recipient failure")

        result = cross(authorisation, payload, failing_recipient, AS_OF)
        self.assertEqual(result.outcome, "aborted-after-crossing")
        self.assertIsNotNone(result.disclosure)
        names = [e.event for e in result.events]
        self.assertIn("disclosure", names)
        self.assertIn("transmission-abort", names)
        details = [e.detail for e in result.events]
        self.assertIn("partial-crossing-is-a-crossing", details)

    def test_events_are_content_free_and_immutable(self):
        _context, payload, authorisation = authorised()
        result = cross(authorisation, payload, lambda b: None, AS_OF)
        self.assertIsInstance(result, CrossingResult)
        self.assertIsInstance(result.events, tuple)
        for event in result.events:
            self.assertNotIn(MARKER.decode(), str(event))


class RetryIdentity(unittest.TestCase):
    def test_identical_seven_attributes_is_the_same_bounded_event(self):
        context, payload, record = ready_pair()
        one = TransmissionAuthorisation(context, payload, record, AS_OF)
        two = TransmissionAuthorisation(context, payload, record, AS_OF)
        self.assertTrue(same_bounded_event(one, two))

    def test_any_changed_attribute_is_a_new_attempt(self):
        context, payload, record = ready_pair()
        one = TransmissionAuthorisation(context, payload, record, AS_OF)
        two = TransmissionAuthorisation(context, payload, record,
                                        "AS-OF-PLACEHOLDER-8")
        self.assertFalse(same_bounded_event(one, two))

    def test_retry_after_revocation_or_expiry_refused(self):
        for terminal in ("revoke", "end"):
            context, payload, record = ready_pair()
            getattr(context, terminal)()
            with self.assertRaises(TransmissionRefused):
                TransmissionAuthorisation(context, payload, record,
                                          AS_OF)


class StructuralAbsences(unittest.TestCase):
    def test_imports_and_calls_are_pure_and_network_free(self):
        tree = ast.parse((ROOT / "runtime" / "transmission.py").read_text(
            encoding="utf-8"))
        banned = {"time", "datetime", "sched", "threading", "asyncio",
                  "logging", "os", "pathlib", "io", "engine",
                  "subprocess", "socket", "ssl", "http", "urllib",
                  "requests"}
        allowed = {"uuid", "dataclasses", "runtime"}
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
        self.assertFalse(seen & banned, seen & banned)
        self.assertTrue(seen <= allowed, seen - allowed)

    def test_no_vendor_comfort_claim_in_source(self):
        source = (ROOT / "runtime" / "transmission.py").read_text(
            encoding="utf-8").lower()
        for phrase in ("verified deletion", "guaranteed non-retention",
                       "safe because", "controlled after",
                       "deleted remotely"):
            self.assertNotIn(phrase, source)

    def test_no_model_contact_or_outward_name_exists(self):
        banned_stems = ("notify", "notification", "remind", "push",
                        "email", "sms", "webhook", "subscribe",
                        "vendor_call", "model_call", "sdk", "client",
                        "http", "fetch", "registry", "cache", "pool")
        tree = ast.parse((ROOT / "runtime" / "transmission.py").read_text(
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
        self.assertIn(("transmission-crossing", "W5-D2-M06"),
                      REGISTERED_BOUNDARY_OPERATIONS)


class ResidueLifecycle(unittest.TestCase):
    def test_normal_termination_leaves_no_readable_residue(self):
        with tempfile.TemporaryDirectory() as workspace:
            context, payload, authorisation = authorised()
            cross(authorisation, payload, lambda b: None, AS_OF)
            context.end()
            files = [p for p in Path(workspace).rglob("*")
                     if p.is_file()]
            self.assertEqual(files, [])
            self.assertEqual(sweep_locations(workspace, MARKER), [])

    def test_kill_termination_leaves_no_readable_residue(self):
        child = (
            "import sys, time\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "sys.path.insert(0, sys.argv[1] + '/tests')\n"
            "from tests.test_runtime_transmission import authorised, "
            "AS_OF\n"
            "from runtime.transmission import cross\n"
            "_c, payload, authorisation = authorised()\n"
            "cross(authorisation, payload, lambda b: None, AS_OF)\n"
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
