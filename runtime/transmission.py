"""Wellbeing Wing runtime transmission and disclosure mechanics
(W5-D2-M06).

ADR 0032 made real: the third gate, enforced separately from the
first two. A lawful grant does not assemble a payload; a lawful,
proven-equal payload does not authorise crossing; transmission
authority is proven per attempt, is never ambient, and is consumed by
exactly one crossing. Every attempt, check, refusal, abort,
disclosure and completion is a content-free governed event; a partial
crossing is a crossing and is never unmade; a refusal before the
boundary produces no disclosure at all.

No recipient exists in this milestone. Crossings terminate at
in-process structural doubles — plain callables handed the governed
canonical bytes — and this module is provably network-free: no
socket, client, SDK, vendor path, or model-contact path exists, and
no comfort claim about anything beyond the last controllable point is
made anywhere. Vendor-hosted recipients are refused upstream at
context construction; E10 stays unopened; the Z4 limb stays visibly
pending. Time is an injected as-of marker; no clock is read.
"""

import uuid
from dataclasses import dataclass

from runtime.context import ProcessingContext
from runtime.payload import (
    Payload, PayloadRefused, compare_at_last_controllable_point,
    payload_fingerprint, require_equal, serialise_payload)

# The nameable recipients of this milestone, in the grant's own
# display terms (W1-D2 section 4's local branch; ADR 0024 d17a).
# A crossing whose recipient cannot be named is refused.
NAMEABLE_RECIPIENTS = {
    "internal": "an internal room agent on this device",
    "local_model": "a model running on this device",
}

BOUNDARY_NAME = "in-process-structural-double"


class TransmissionRefused(Exception):
    """Content-free refusal: a fixed reason code, never payload content."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class TransmissionEvent:
    """C0 and content-free: category, references and outcomes only."""

    event: str
    attempt_id: str
    grant_id: str
    payload_fingerprint: str
    detail: str


@dataclass(frozen=True)
class DisclosureRecord:
    """ADR 0001's disclosure elements — actor, scope, recipient
    class, purpose, time — as references only, never content. The
    record exists so a person can see what left, to whom, and when,
    including where the answer is uncomfortable."""

    attempt_id: str
    actor: str
    scope_sections: tuple
    recipient_class: str
    recipient_name: str
    purpose: str
    as_of: str
    payload_fingerprint: str


class TransmissionAuthorisation:
    """Proven transmission authority for exactly one attempt.

    Derived per attempt from the live grant lifecycle, the assembled
    payload, and a passing equality record — and consumed by exactly
    one crossing. No flag, session, or prior success substitutes for
    it, and it never becomes ambient (ADR 0032 decisions 1-3)."""

    def __init__(self, context, payload, equality_record, as_of,
                 invalidated_payload_ids=()):
        if not isinstance(context, ProcessingContext):
            raise TransmissionRefused("no_context_no_authority")
        if context.ended:
            raise TransmissionRefused("context_ended")
        if not isinstance(payload, Payload):
            raise TransmissionRefused("no_payload_no_transmission")
        if payload.grant_id != context.grant.grant_id:
            raise TransmissionRefused("payload_not_bound_to_this_grant")
        if payload.payload_id in frozenset(invalidated_payload_ids):
            raise TransmissionRefused("invalidated_payload")
        try:
            require_equal(equality_record)
        except PayloadRefused:
            raise TransmissionRefused("equality_unproven") from None
        grant = context.grant
        for field in ("recipient_class", "vendor_involvement",
                      "plaintext_flag", "operation", "purpose", "edge"):
            if getattr(payload, field) != getattr(grant, field):
                raise TransmissionRefused("posture_mismatch_at_crossing")
        if tuple(payload.zones) != tuple(grant.zones):
            raise TransmissionRefused("posture_mismatch_at_crossing")
        if grant.recipient_class not in NAMEABLE_RECIPIENTS:
            raise TransmissionRefused("recipient_not_nameable")
        self.attempt_id = str(uuid.uuid4())
        self.grant_id = grant.grant_id
        self.payload_id = payload.payload_id
        self.payload_fingerprint = payload_fingerprint(
            serialise_payload(payload))
        self.recipient_class = grant.recipient_class
        self.recipient_name = NAMEABLE_RECIPIENTS[grant.recipient_class]
        self.actor = grant.requesting_actor
        self.purpose = grant.purpose
        self.operation = grant.operation
        self.plaintext_flag = grant.plaintext_flag
        self.vendor_involvement = grant.vendor_involvement
        self.boundary = BOUNDARY_NAME
        self.as_of = as_of
        self.consumed = False


def bounded_event_identity(authorisation):
    """The seven attributes of ADR 0032 decision 24. A retry is the
    same bounded event only if all seven are mechanically identical;
    otherwise it is a new attempt requiring its own authority."""
    return (authorisation.grant_id,
            (authorisation.recipient_class, authorisation.recipient_name),
            authorisation.payload_fingerprint,
            authorisation.boundary,
            authorisation.plaintext_flag,
            authorisation.vendor_involvement,
            (authorisation.operation, authorisation.as_of))


def same_bounded_event(one, other):
    return bounded_event_identity(one) == bounded_event_identity(other)


@dataclass(frozen=True)
class CrossingResult:
    """The honest outcome of one attempt: its events, its disclosure
    record where a crossing occurred, and nothing erasable."""

    outcome: str
    events: tuple
    disclosure: object


def cross(authorisation, payload, recipient, as_of):
    """The one crossing mechanic. Re-proves equality at the last
    controllable point, records the disclosure with the hand-off, and
    reports partial crossings as crossings — a failed outcome never
    retroactively unmakes an exposure (ADR 0032 decisions 21-23)."""
    if not isinstance(authorisation, TransmissionAuthorisation):
        raise TransmissionRefused("no_authority_no_crossing")
    if authorisation.consumed:
        raise TransmissionRefused("authority_not_reusable")
    authorisation.consumed = True
    events = [TransmissionEvent(
        event="transmission-attempt", attempt_id=authorisation.attempt_id,
        grant_id=authorisation.grant_id,
        payload_fingerprint=authorisation.payload_fingerprint,
        detail=authorisation.boundary)]
    presented = serialise_payload(payload)
    record = compare_at_last_controllable_point(payload, presented)
    if (not record.outcome
            or record.fingerprint_a != authorisation.payload_fingerprint):
        events.append(TransmissionEvent(
            event="transmission-refusal",
            attempt_id=authorisation.attempt_id,
            grant_id=authorisation.grant_id,
            payload_fingerprint=authorisation.payload_fingerprint,
            detail="equality_unproven_at_boundary"))
        return CrossingResult(outcome="refused-before-boundary",
                              events=tuple(events), disclosure=None)
    events.append(TransmissionEvent(
        event="authority-checks-passed",
        attempt_id=authorisation.attempt_id,
        grant_id=authorisation.grant_id,
        payload_fingerprint=authorisation.payload_fingerprint,
        detail="equality-reproved-at-last-controllable-point"))
    disclosure = DisclosureRecord(
        attempt_id=authorisation.attempt_id,
        actor=authorisation.actor,
        scope_sections=tuple(name for name, _ in payload.sections),
        recipient_class=authorisation.recipient_class,
        recipient_name=authorisation.recipient_name,
        purpose=authorisation.purpose,
        as_of=as_of,
        payload_fingerprint=authorisation.payload_fingerprint)
    try:
        recipient(presented)
    except Exception:
        events.append(TransmissionEvent(
            event="disclosure", attempt_id=authorisation.attempt_id,
            grant_id=authorisation.grant_id,
            payload_fingerprint=authorisation.payload_fingerprint,
            detail="partial-crossing-is-a-crossing"))
        events.append(TransmissionEvent(
            event="transmission-abort",
            attempt_id=authorisation.attempt_id,
            grant_id=authorisation.grant_id,
            payload_fingerprint=authorisation.payload_fingerprint,
            detail="recipient-failed-after-hand-off"))
        return CrossingResult(outcome="aborted-after-crossing",
                              events=tuple(events), disclosure=disclosure)
    events.append(TransmissionEvent(
        event="disclosure", attempt_id=authorisation.attempt_id,
        grant_id=authorisation.grant_id,
        payload_fingerprint=authorisation.payload_fingerprint,
        detail="crossing-completed"))
    events.append(TransmissionEvent(
        event="transmission-completion",
        attempt_id=authorisation.attempt_id,
        grant_id=authorisation.grant_id,
        payload_fingerprint=authorisation.payload_fingerprint,
        detail="completed"))
    return CrossingResult(outcome="completed", events=tuple(events),
                          disclosure=disclosure)
