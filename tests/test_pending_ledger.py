"""Tier 3 — named pending stubs: the outstanding-proof ledger.

Every test category the corpus requires but nothing can yet run lands
here as an explicitly skipped stub with an owner (a role or phase,
never a person) and an unblocking condition. a skipped test is honest;
a missing test is invisible. run `python -m unittest discover -s tests -v`
to review the ledger.
"""

import json
import sys
import tempfile
import unittest
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.core import (  # noqa: E402
    AUTHORITY_LABELS, classify_transition, seal, unseal,
)
from engine.ports import FileStorage, PyNaClCrypto  # noqa: E402


def pending(owner, unblocks_when):
    return unittest.skip(f"PENDING — owner: {owner}; unblocks when: {unblocks_when}")


class DeterministicPendingImplementation(unittest.TestCase):
    # Converted from the pending ledger, 2026-07-06: the vault data
    # layer and transition engine exist (W3-D3, W3-D4 M1/M2), so the
    # stub's promise is now a running proof.
    def test_D3_transitions_enforced_by_real_engine(self):
        """the real transition engine refuses every illegal path the
        grammar refuses on paper (extends tier 2 to running code)."""
        grammar = json.loads(
            (ROOT / "tests" / "grammar" / "d3-transitions.json")
            .read_text(encoding="utf-8"))
        labels = sorted(AUTHORITY_LABELS) + [None]
        truth = grammar["truth_labels"]
        # paper: agents are forbidden T2/T4/T7 — the running engine
        # refuses every agent-actored shape of those transitions.
        for tid in grammar["agent_forbidden_transitions"]:
            for f, t in product(labels, labels):
                status = classify_transition(
                    tid, f, t, "agent-under-e2-grant")["status"]
                self.assertNotIn(status, ("runnable", "gated"),
                                 f"paper forbids agents {tid}; engine allowed it")
        # paper: only the user mints truth — no agent, system, or time
        # actor reaches a truth label through any catalogued transition.
        self.assertTrue(grammar["rules"]["only_the_user_mints_truth"])
        self.assertTrue(grammar["rules"]["automatic_transitions_only_lower_trust"])
        for actor in ("agent-under-e2-grant", "system-on-user-entry",
                      "system-flags-user-resolves", "time-automatic"):
            for tid, f, t in product(grammar["transitions"], labels, truth):
                status = classify_transition(tid, f, t, actor)["status"]
                self.assertNotIn(status, ("runnable", "gated"),
                                 f"paper truth label reached by {actor} via {tid}")

    # Converted from the pending ledger, 2026-07-06: the residue
    # policy record is accepted (ADR 0004) and decrypting code exists
    # (the sealed store, since W3-D2). Heavyweight residue proofs live
    # in the engine suites; this is the ledger's own compact promise.
    def test_D5_T01_plaintext_residue_none_after_task(self):
        """create, use, terminate: no readable governed content remains
        outside encrypted stores."""
        marker = b"SYNTHETIC-RESIDUE-MARKER-Persona-K9-Allergen-X"
        with tempfile.TemporaryDirectory() as ws:
            storage = FileStorage(Path(ws) / "store.bin")
            crypto = PyNaClCrypto()
            key = crypto.random_key()
            seal(storage, crypto, key,
                 marker + b" governed synthetic content")   # create
            self.assertIn(marker, unseal(storage, crypto, key))   # use
            files = [p for p in Path(ws).rglob("*") if p.is_file()]
            self.assertEqual([p.name for p in files], ["store.bin"],
                             "task left more than the sealed store")
            for f in files:                                   # terminate: sweep
                self.assertNotIn(marker, f.read_bytes(),
                                 "readable governed content outside the store")

    @pending("w5 adapter phase", "the payload-equality standard record is accepted and an assembler exists")
    def test_D5_T15_T23_payload_equality_at_z3_z4(self):
        """granted scope equals transmitted bytes at the last
        controllable point, per boundary edge."""

    @pending("w5 adapter phase", "grant machinery exists")
    def test_D5_T04_granted_and_trusted_never_merge(self):
        """consent state and authority state remain independent fields
        in the running system."""


class BehaviouralPendingModelAccess(unittest.TestCase):
    @pending("w5 evaluation era", "model access is decided and behavioural harness exists")
    def test_D5_T05_repetition_resistance_behavioural(self):
        """a model told a claim three times treats the third mention
        with no more certainty than the first."""

    @pending("w5 evaluation era", "model access is decided and behavioural harness exists")
    def test_D5_T06_authority_laundering_resistance(self):
        """downstream context treats upstream model summaries as
        suggestions, never as facts."""

    @pending("w5 evaluation era", "room isolation model implemented at the adapter layer")
    def test_D5_T12_cross_room_isolation_behavioural(self):
        """bait from one room's records is unreachable and unused in
        another room's context (fixture: cross-room bait cases)."""

    @pending("w5 evaluation era", "room contracts accepted and behavioural harness exists")
    def test_D5_T13_in_room_silent_inference_resistance(self):
        """a room does not derive or act on health conclusions from its
        own ordinary records (fixture: in-room bait cases)."""


class SurfacePendingUiPhase(unittest.TestCase):
    @pending("w6 surface phase", "governed string catalogue exists and surfaces render")
    def test_language_law_grading_both_directions(self):
        """surfacing text graded for overclaim and underclaim
        symmetrically; honest unknown never penalised."""

    @pending("w6 surface phase", "review surfaces exist")
    def test_D5_T02_no_bulk_approve_path_in_ui(self):
        """no ui path promotes drafts without per-section user acts."""

    @pending("w6 surface phase", "surfaces render governance labels")
    def test_D5_T24_label_legibility(self):
        """authority and staleness labels are legible, not merely
        present, at every display site."""


if __name__ == "__main__":
    unittest.main()
