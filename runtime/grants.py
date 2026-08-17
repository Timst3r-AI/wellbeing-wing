"""Wellbeing Wing runtime grant machinery (W5-D2-M02).

ADR 0030 at runtime: a grant is an immutable delegation constructable
only from the thirteen governed elements over one already-declared
edge. Missing elements, undeclared edges, and blanket scopes are
unconstructable, not merely invalid. Consent is not authority: no
authority vocabulary exists anywhere in this module, by design.

Structure only. Nothing here holds governed plaintext, persists
anything, reads a clock, evaluates behaviour, or contacts anything.
Grant and lifecycle records are C0 governance metadata shapes.
"""

import uuid
from dataclasses import dataclass

# --- governed vocabularies: doctrine-derived data, no invented values ---

# W1-D1 section 5 — the grantable declared edges. Bare E11 is a rule,
# not a flow, and is deliberately absent.
DECLARED_EDGES = frozenset(
    {"E2", "E6", "E7", "E9", "E10", "E11-W", "E11-K", "E11-G", "M2"})

# W1-D2 section 1 — recipient / processing classes.
RECIPIENT_CLASSES = frozenset(
    {"none", "internal", "local_model", "vendor_hosted_model",
     "external_vendor"})

DATA_CLASSES = frozenset({"C0", "C1", "C2", "C3", "C4", "CM"})
ZONES = frozenset({"Z1", "Z2", "Z3", "Z4", "Z5"})
OPERATIONS = frozenset(
    {"read", "extract", "process", "transmit", "prepare_for_export"})

# Scope names sections, records, or categories — never a class-wide
# wildcard (W1-D2 section 3.1).
WILDCARD_SCOPE_TOKENS = frozenset({"*", "all", "everything"})

# ADR 0030 decision 24 — governed duration kinds per edge. E10 appears
# as table data only: E10 remains unopened and no crossing exists.
GOVERNED_DURATIONS = {
    "E2": "single_task",
    "E6": "standing_180_days",
    "E7": "standing_180_days",
    "E9": "single_task",
    "E10": "per_transmission",
    "E11-W": "single_task_session_max",
    "E11-K": "single_task_session_max",
    "E11-G": "single_task_session_max",
    "M2": "single_task_session_max",
}

# ADR 0030 decision 26 — a hard validity ceiling, not a reminder.
STANDING_VALIDITY_DAYS = 180

# ADR 0030 decision 38. Decision 39 is conditional doctrine for a
# vendor-hosted path that does not exist; no entry is minted for it.
REAUTH_REQUIRED_EDGES = frozenset({"E2"})

# ADR 0030 decision 8 — the seven governed lifecycle states.
LIFECYCLE_STATES = (
    "proposed", "declined", "active", "awaiting_required_reauthentication",
    "review_due", "expired", "revoked")
TERMINAL_STATES = frozenset({"declined", "expired", "revoked"})

# The thirteen required elements (W1-D2 section 1; zones is the single
# "source zone -> destination zone" element expressed as a pair).
REQUIRED_ELEMENTS = (
    "edge", "requesting_actor", "recipient_class", "data_class", "scope",
    "zones", "purpose", "operation", "plaintext_flag",
    "vendor_involvement", "duration", "revocation_behaviour",
    "audit_reference")


class UnconstructableGrant(Exception):
    """Content-free refusal: a fixed reason code, never submitted values."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


class ActivationRefused(Exception):
    """Content-free refusal: a fixed reason code, never submitted values."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class Grant:
    """One immutable delegation. No authority field exists, by design."""

    grant_id: str
    edge: str
    requesting_actor: str
    recipient_class: str
    data_class: str
    scope: tuple
    zones: tuple
    purpose: str
    operation: str
    plaintext_flag: bool
    vendor_involvement: str
    duration: str
    revocation_behaviour: str
    audit_reference: str
    predecessor_id: str = None


def construct_grant(**elements):
    """Return a Grant only if all thirteen elements are lawful.

    Refusal raises before any object exists: a grant missing any
    element, naming an undeclared edge, or carrying a blanket scope is
    unconstructable, not merely irregular (ADR 0030 decision 1).
    """
    for name in REQUIRED_ELEMENTS:
        if name not in elements or elements[name] in (None, "", ()):
            raise UnconstructableGrant("missing_element:" + name)
    unknown = set(elements) - set(REQUIRED_ELEMENTS)
    if unknown:
        raise UnconstructableGrant("unknown_element")
    edge = elements["edge"]
    if edge not in DECLARED_EDGES:
        raise UnconstructableGrant("undeclared_edge")
    scope = tuple(elements["scope"])
    if not scope or any(
            not isinstance(item, str) or not item.strip()
            or item.strip().lower() in WILDCARD_SCOPE_TOKENS
            for item in scope):
        raise UnconstructableGrant("blanket_or_empty_scope")
    if elements["recipient_class"] not in RECIPIENT_CLASSES:
        raise UnconstructableGrant("unknown_recipient_class")
    if elements["data_class"] not in DATA_CLASSES:
        raise UnconstructableGrant("unknown_data_class")
    zones = tuple(elements["zones"])
    if len(zones) != 2 or any(z not in ZONES for z in zones):
        raise UnconstructableGrant("unlawful_zone_pair")
    if elements["operation"] not in OPERATIONS:
        raise UnconstructableGrant("unknown_operation")
    if elements["duration"] != GOVERNED_DURATIONS[edge]:
        raise UnconstructableGrant("ungoverned_duration")
    if not isinstance(elements["plaintext_flag"], bool):
        raise UnconstructableGrant("plaintext_flag_not_stated")
    return Grant(grant_id=str(uuid.uuid4()), scope=scope, zones=zones,
                 **{k: elements[k] for k in REQUIRED_ELEMENTS
                    if k not in ("scope", "zones")})


def create_successor(predecessor):
    """Explicit re-affirmation: a new identity with inspectable lineage.

    The predecessor is never altered, re-dated, or reopened
    (ADR 0030 decisions 12-16); succession is new permission.
    """
    return Grant(
        grant_id=str(uuid.uuid4()),
        predecessor_id=predecessor.grant_id,
        **{name: getattr(predecessor, name) for name in REQUIRED_ELEMENTS})


@dataclass(frozen=True)
class ReAuthProof:
    """Proof of present control for exactly one grant proposal.

    Binds to one grant_id and activates nothing else (ADR 0030
    decisions 34-38). A materially changed request is a new grant with
    a new identity, so an old proof can never activate it.
    """

    proposal_id: str


class GrantLifecycle:
    """The governed state of one immutable Grant.

    Holds exactly (grant, state). Terminal states are terminal:
    expired and revoked grants never activate and never revive.
    """

    def __init__(self, grant):
        self.grant = grant
        self.state = "proposed"

    def decline(self):
        self._require_not_terminal()
        self.state = "declined"

    def activate(self, reauth_proof=None):
        if self.state in TERMINAL_STATES:
            raise ActivationRefused("terminal_state")
        if self.grant.edge in REAUTH_REQUIRED_EDGES:
            if reauth_proof is None:
                self.state = "awaiting_required_reauthentication"
                raise ActivationRefused("reauthentication_required")
            if reauth_proof.proposal_id != self.grant.grant_id:
                raise ActivationRefused("reauthentication_scope_mismatch")
        self.state = "active"

    def mark_review_due(self):
        self._require_not_terminal()
        self.state = "review_due"

    def expire(self):
        self._require_not_terminal()
        self.state = "expired"

    def revoke(self):
        # Revocation is a right, not a request: terminal, unconditional.
        self.state = "revoked"

    def _require_not_terminal(self):
        if self.state in TERMINAL_STATES:
            raise ActivationRefused("terminal_state")


def standing_validity_exceeded(elapsed_days):
    """Pure predicate over an injected elapsed measure — no clock is
    read anywhere in this module, and expiry is an explicit governed
    event, never a background act."""
    return elapsed_days >= STANDING_VALIDITY_DAYS
