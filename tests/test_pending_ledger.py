"""Tier 3 — named pending stubs: the outstanding-proof ledger.

Every test category the corpus requires but nothing can yet run lands
here as an explicitly skipped stub with an owner (a role or phase,
never a person) and an unblocking condition. a skipped test is honest;
a missing test is invisible. run `python -m unittest discover -s tests -v`
to review the ledger.
"""

import unittest


def pending(owner, unblocks_when):
    return unittest.skip(f"PENDING — owner: {owner}; unblocks when: {unblocks_when}")


class DeterministicPendingImplementation(unittest.TestCase):
    @pending("w3 build phase", "the vault data layer and transition engine exist")
    def test_D3_transitions_enforced_by_real_engine(self):
        """the real transition engine refuses every illegal path the
        grammar refuses on paper (extends tier 2 to running code)."""

    @pending("w3 build phase", "the residue policy record is accepted and decrypting code exists")
    def test_D5_T01_plaintext_residue_none_after_task(self):
        """create, use, terminate: no readable governed content remains
        outside encrypted stores."""

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
