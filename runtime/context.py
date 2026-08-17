"""Wellbeing Wing runtime processing context (W5-D2-M04).

ADR 0024's room made real: the processing context is the product of
one active grant, holds exactly one domain's scoped content, composes
with nothing, reuses nothing, fetches nothing, survives nothing, and
is observable by construction on the four required surfaces.

Content enters only as grant-bound material inseparable from the
grant that created the context (ADR 0024 decision 2); there is no
free-content interface, no read path, and no output path — payload
assembly is W5-D2-M05's and transmission is W5-D2-M06's. Ledger
emission happens here as content-free event production at the
boundary (ADR 0024 decision 20, under ADR 0015's extension clause);
appending events to the sealed ledger is composition-root work.

This module performs no file or network I/O of any kind, reads no
clock, imports nothing from the engine, and writes no log. Its
transient holdings exist in process memory only and are cleared at
context end; the residue proofs sweep for exactly that.
"""

import uuid
from dataclasses import dataclass

from runtime.grants import GrantLifecycle

# The processing crossings and their domains: the room is a function
# of the grant's edge, never an argument (ADR 0024 decision 6). E2 is
# the Health Profile Agent's extraction context; the E11 family and
# M2 are the four rooms' declared processing edges. No other edge is
# a processing edge, and no generic entry exists.
CONTEXT_DOMAIN_BY_EDGE = {
    "E2": "health-profile-agent",
    "E11-W": "wellness",
    "E11-K": "kitchen",
    "E11-G": "gym",
    "M2": "meditation",
}

# ADR 0033: the local model class is the only doctrinally
# constructable model recipient; vendor-hosted remains unopened and
# is refused here structurally. Internal agent processing is lawful.
PROCESSING_RECIPIENT_CLASSES = frozenset({"internal", "local_model"})

CONTEXT_END_CAUSES = frozenset({"completion", "expiry", "revocation"})


class ContextRefused(Exception):
    """Content-free refusal: a fixed reason code, never held content."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class GrantBoundContent:
    """Scoped content inseparably bound to one grant: the grant_id is
    part of the object, the section must sit inside that grant's
    scope, and no constructor exists that takes content alone."""

    grant_id: str
    section: str
    content: bytes


@dataclass(frozen=True)
class ProcessingLedgerEvent:
    """C0 and content-free (ADR 0024 decision 20): categories and
    scope names only, never contents, produced at the boundary for
    the composition root to append under ADR 0015."""

    event: str
    context_id: str
    grant_id: str
    edge: str
    domain: str
    scope_sections: tuple


@dataclass(frozen=True)
class ContextReport:
    """The spoken-output surface: what was presented and what was
    returned, by section name, without a second data channel."""

    presented_sections: tuple
    returned: str


class ProcessingContext:
    """One grant's room. Constructable only from an ACTIVE grant
    lifecycle; ended exactly once; observable throughout."""

    def __init__(self, lifecycle):
        if not isinstance(lifecycle, GrantLifecycle):
            raise ContextRefused("no_grant_no_context")
        if lifecycle.state != "active":
            raise ContextRefused("grant_not_active")
        grant = lifecycle.grant
        if grant.edge not in CONTEXT_DOMAIN_BY_EDGE:
            raise ContextRefused("not_a_processing_edge")
        if grant.recipient_class not in PROCESSING_RECIPIENT_CLASSES:
            raise ContextRefused("recipient_class_not_processable")
        self.context_id = str(uuid.uuid4())
        self.grant = grant
        self.domain = CONTEXT_DOMAIN_BY_EDGE[grant.edge]
        self._held = []
        self._presented = []
        self._ended = False
        self._end_cause = None
        self.events = (self._event("context-created"),)

    def _event(self, name):
        return ProcessingLedgerEvent(
            event=name, context_id=self.context_id,
            grant_id=self.grant.grant_id, edge=self.grant.edge,
            domain=self.domain, scope_sections=tuple(self._presented))

    def receive(self, bound):
        """Grant-bound content only: wrong grant, out-of-scope
        section, or an ended context all refuse with no path in."""
        if self._ended:
            raise ContextRefused("context_ended")
        if not isinstance(bound, GrantBoundContent):
            raise ContextRefused("no_free_content_interface")
        if bound.grant_id != self.grant.grant_id:
            raise ContextRefused("content_not_bound_to_this_grant")
        if bound.section not in self.grant.scope:
            raise ContextRefused("content_outside_grant_scope")
        self._held.append(bound)
        self._presented.append(bound.section)

    def report(self):
        """Spoken-output surface. Section names only; at W5-D2-M04
        nothing is ever returned because no model and no output path
        exist."""
        return ContextReport(presented_sections=tuple(self._presented),
                             returned="nothing-returned-no-output-path")

    def destinations_written(self):
        """Routing-and-propagation surface: every Wing-controlled
        destination this context wrote to. No write API exists at
        W5-D2-M04, so the enumeration is empty by construction and
        absence is proven by enumeration, not assumption."""
        return ()

    def post_context_state(self):
        """Persisted-state surface: the transient holdings, exposable
        for inspection so that absence after end is demonstrated,
        never presumed (ADR 0024 decision 13)."""
        return tuple(self._held)

    def end(self, cause="completion"):
        """The grant's end is the context's end: completion, expiry,
        or revocation. Holdings are cleared; nothing survives; ending
        twice refuses."""
        if self._ended:
            raise ContextRefused("context_already_ended")
        if cause not in CONTEXT_END_CAUSES:
            raise ContextRefused("unknown_end_cause")
        self._held.clear()
        self._ended = True
        self._end_cause = cause
        self.events = self.events + (self._event("context-ended"),)

    def revoke(self):
        """Revocation expressed at the boundary (ADR 0024 decision
        11). No crossing exists at W5-D2-M04, so there is nothing
        in-flight to sever; severability honesty for real crossings
        arrives with W5-D2-M06."""
        self.end(cause="revocation")

    @property
    def ended(self):
        return self._ended
