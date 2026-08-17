"""Wellbeing Wing runtime composition root (W5-D2-M07).

The lawful external composition root of ADR 0024 decision 4: it may
invoke the public interfaces of the runtime pieces, and it is the
only place where they meet. It is deliberately stateless — module
functions only, no class, no module-level container — so it can never
become a standing model handle, an ambient session, or a cache: it
holds no grant, no context, and no content between operations.

Isolation is realised here end-to-end: one operation is one grant,
one context, one payload, at most one crossing, ended always. No
function anywhere in the runtime accepts two contexts, and the
composition root offers no second route around itself.

Meditation is stricter, not smoothed: per W1-D1 section 5, the M2
edge carries CM content and nothing else, and CM travels on no other
edge — enforced structurally here, with the no-output-elsewhere rule
held by the global absence of any room-write path plus M2's only
egress being its own governed crossing.

Content-free ledger frames are appended only through this root, via a
caller-supplied append callable: individual runtime modules produce
events and never append them. No clock is read; as-of markers are
injected; nothing here is a scheduler, a background job, or a path
outward beyond the single governed crossing mechanic.
"""

from runtime.context import GrantBoundContent, ProcessingContext
from runtime.payload import (
    assemble_payload, compare_at_last_controllable_point,
    serialise_payload)
from runtime.transmission import TransmissionAuthorisation, cross

from dataclasses import dataclass

# Doctrine-derived data-class lawfulness per processing edge
# (W1-D1 sections 4-5): the Vault extraction context reads C4
# evidence; the room edges carry their rooms' own classes; and the
# Meditation edge carries CM and only CM, while CM travels on no
# other edge at all (W0 Law 9 made structural).
LAWFUL_DATA_CLASSES_BY_EDGE = {
    "E2": frozenset({"C4"}),
    "E11-W": frozenset({"C2", "C3"}),
    "E11-K": frozenset({"C1"}),
    "E11-G": frozenset({"C1", "C2"}),
    "M2": frozenset({"CM"}),
}


class CompositionRefused(Exception):
    """Content-free refusal: a fixed reason code, never held content."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class CompositionOutcome:
    """The honest result of one composed operation: outcome, the
    content-free event trail, and the disclosure record where a
    crossing occurred. The root retains none of it."""

    outcome: str
    events: tuple
    disclosure: object


def compose_context(lifecycle):
    """The single context door at composition level, with the
    edge/data-class lawfulness rule enforced before construction:
    CM only on M2, and M2 only CM."""
    grant = getattr(lifecycle, "grant", None)
    if grant is None:
        raise CompositionRefused("no_grant_no_operation")
    lawful = LAWFUL_DATA_CLASSES_BY_EDGE.get(grant.edge)
    if lawful is None:
        raise CompositionRefused("not_a_processing_edge")
    if grant.data_class not in lawful:
        raise CompositionRefused("data_class_not_lawful_for_edge")
    if grant.data_class == "CM" and grant.edge != "M2":
        raise CompositionRefused("contemplative_content_off_its_edge")
    return ProcessingContext(lifecycle)


def run_granted_operation(lifecycle, bound_items, recipient, as_of,
                          invalidated_refs=(), ledger_append=None):
    """One whole governed operation: one grant, one context, one
    payload, at most one crossing, ended always — with every
    content-free event appended through this root and nothing
    retained afterwards."""
    context = compose_context(lifecycle)
    disclosure = None
    outcome = "refused"
    crossing_events = ()
    try:
        for item in bound_items:
            if not isinstance(item, GrantBoundContent):
                raise CompositionRefused("no_free_content_interface")
            context.receive(item)
        payload = assemble_payload(
            context, invalidated_refs=invalidated_refs)
        equality = compare_at_last_controllable_point(
            payload, serialise_payload(payload))
        authorisation = TransmissionAuthorisation(
            context, payload, equality, as_of,
            invalidated_payload_ids=())
        result = cross(authorisation, payload, recipient, as_of)
        outcome = result.outcome
        disclosure = result.disclosure
        crossing_events = result.events
    finally:
        if not context.ended:
            context.end()
    events = tuple(context.events) + tuple(crossing_events)
    if ledger_append is not None:
        for event in events:
            ledger_append(event)
    return CompositionOutcome(outcome=outcome, events=events,
                              disclosure=disclosure)
