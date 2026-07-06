"""Profile object model: the authority/staleness grammar as data shapes.

This module implements W3-D3 (this deliverable) from W1-D3, the
authority and staleness model - note the distinction: "D3-T1..T8" in
the corpus names W1-D3's *transitions*; this file is the W3-D3
*object model*. Shapes only: nothing here signs, reviews, approves,
extracts, persists, or transitions anything. The structures make
illegal states unconstructable; the acts that move items between
states belong to a later deliverable behind its own gates.

Per W1-D3 section 8a, binding here: everything these shapes describe
is governance metadata - content-free with respect to health content
but privacy-sensitive by pattern. It has no processing edges: never
analytics, never behavioural profiling, never inference input. It may
support governance, audit, review, and user-visible export only.

Per the minimal-review-posture record: the Approved layer exists here
as a *shape* because the grammar is incomplete without it; no
Approved instance may exist in any non-test store, and this module
provides no path by which one could. Staleness intervals are injected
parameters - no clinical judgment is encoded as a constant anywhere
in this module, by decision.

No I/O, no clock, no imports: values in, shapes or refusals out.
"""

# Vocabulary is verbatim from the accepted grammar and matches the
# Tier 2 transcription (tests/grammar/d3-transitions.json).
TRUTH_LABELS = frozenset({"confirmed by record", "confirmed by user"})
AGENT_ASSIGNABLE_LABELS = frozenset({
    "agent-extracted, pending review",
    "possible pattern, not confirmed",
})
AUTHORITY_LABELS = TRUTH_LABELS | AGENT_ASSIGNABLE_LABELS | frozenset({
    "user-reported",
    "contradicted",
    "outdated / superseded",
    "unknown / absent evidence",
})

STALENESS_DECAY_ORDER = ("current", "review due", "stale", "expired")
STALENESS_LABELS = frozenset(STALENESS_DECAY_ORDER) | frozenset({
    "superseded",
    "unknown freshness",
})

# Who may assign which authority label (W1-D3 section 1, column 3).
_ASSIGNABLE_BY = {
    "confirmed by record": frozenset({"user-review"}),
    "confirmed by user": frozenset({"user-review"}),
    "user-reported": frozenset({"system-on-user-entry"}),
    "agent-extracted, pending review": frozenset({"agent"}),
    "possible pattern, not confirmed": frozenset({"agent"}),
    "contradicted": frozenset({"system"}),
    "outdated / superseded": frozenset({"user-review", "user"}),
    "unknown / absent evidence": frozenset({"system", "user"}),
}

PROVENANCE_KINDS = frozenset({"vault-record", "user-statement"})
_CONFIRMED_PROVENANCE = {
    "confirmed by record": "vault-record",
    "confirmed by user": "user-statement",
}


class ProfileModelError(ValueError):
    """The requested shape would violate the grammar; nothing was built."""


class ProvenanceRef:
    """Where an item's content came from: a vault record or the user."""

    def __init__(self, kind, reference, stated_at=None):
        if kind not in PROVENANCE_KINDS:
            raise ProfileModelError(f"unknown provenance kind: {kind!r}")
        if not reference:
            raise ProfileModelError("provenance requires a reference")
        self.kind = kind
        self.reference = reference
        self.stated_at = stated_at


class ProfileItem:
    """One governed item: content plus its inseparable label pair.

    An item without an authority label, without a staleness label, or
    with a label its actor may not assign, cannot be constructed.
    Confirmed items additionally require user-review provenance of the
    matching kind and a last-reviewed timestamp - the grammar's rule
    that only the user mints truth, enforced at the constructor.
    """

    def __init__(self, section, content, authority, assigned_by,
                 staleness, last_reviewed=None, provenance=None):
        if not section:
            raise ProfileModelError("item requires a section")
        if content is None:
            raise ProfileModelError("item requires content")
        if authority not in AUTHORITY_LABELS:
            raise ProfileModelError(
                f"item requires a known authority label, got: {authority!r}")
        if staleness not in STALENESS_LABELS:
            raise ProfileModelError(
                f"item requires a known staleness label, got: {staleness!r}")
        allowed = _ASSIGNABLE_BY[authority]
        if assigned_by not in allowed:
            raise ProfileModelError(
                f"actor {assigned_by!r} may not assign {authority!r}")
        if authority in TRUTH_LABELS:
            if last_reviewed is None:
                raise ProfileModelError(
                    "a confirmed item requires a last-reviewed timestamp")
            required_kind = _CONFIRMED_PROVENANCE[authority]
            if (not isinstance(provenance, ProvenanceRef)
                    or provenance.kind != required_kind):
                raise ProfileModelError(
                    f"{authority!r} requires {required_kind} provenance "
                    f"from user review")
        self.section = section
        self.content = content
        self.authority = authority
        self.assigned_by = assigned_by
        self.staleness = staleness
        self.last_reviewed = last_reviewed
        self.provenance = provenance


class BoundedUnknown:
    """Honest ignorance, always bounded: scope, source set, as-of time.

    'No record found in the reviewed documents' must never quietly
    become 'not present' - an unknown without all three bounds cannot
    be constructed.
    """

    def __init__(self, scope, source_set, as_of):
        if not scope:
            raise ProfileModelError("an unknown requires a named scope")
        if not source_set:
            raise ProfileModelError("an unknown requires its source set")
        if not as_of:
            raise ProfileModelError("an unknown requires an as-of time")
        self.scope = scope
        self.source_set = tuple(source_set)
        self.as_of = as_of


class Contradiction:
    """Disagreement held honestly: both sides, with dates, neither hidden."""

    def __init__(self, first, second, detected_at):
        if first is None or second is None:
            raise ProfileModelError("a contradiction requires both sides")
        if not detected_at:
            raise ProfileModelError("a contradiction requires a detection time")
        self.first = first
        self.second = second
        self.detected_at = detected_at


class Supersession:
    """Succession with history: predecessor retained, successor linked."""

    def __init__(self, predecessor, successor, superseded_at):
        if predecessor is None or successor is None:
            raise ProfileModelError(
                "a supersession requires predecessor and successor")
        if not superseded_at:
            raise ProfileModelError("a supersession requires a time")
        self.predecessor = predecessor
        self.successor = successor
        self.superseded_at = superseded_at


class ApprovedProfile:
    """The Approved layer's shape: confirmed items only, by section.

    Shape, not instance: per the minimal-review-posture record no
    Approved instance may exist in any non-test store, and no
    persistence or review path exists in this module or milestone.
    The constructor refuses any item below the truth labels, so even
    the shape cannot hold what the user has not confirmed.
    """

    def __init__(self, sections):
        held = {}
        for section, items in dict(sections).items():
            for item in items:
                if not isinstance(item, ProfileItem):
                    raise ProfileModelError(
                        "the approved layer holds profile items only")
                if item.authority not in TRUTH_LABELS:
                    raise ProfileModelError(
                        f"the approved layer refuses authority "
                        f"{item.authority!r}: only the user mints truth")
            held[section] = tuple(items)
        self.sections = held


class LedgerEvent:
    """A governance event's shape: identifiers and times, never content.

    Data only - carries category, references, and a timestamp;
    holds no content field by construction and mutates nothing.
    Durable ledger storage belongs to a later deliverable.
    """

    def __init__(self, kind, refs, recorded_at):
        if not kind:
            raise ProfileModelError("an event requires a kind")
        if not recorded_at:
            raise ProfileModelError("an event requires a recorded-at time")
        self.kind = str(kind)
        self.refs = tuple(str(r) for r in refs)
        self.recorded_at = recorded_at


def staleness_of(elapsed, intervals):
    """Pure staleness decay: elapsed time in, label out. Downward only.

    Intervals are injected - there is no default and no constant in
    this module, because interval numbers are clinical judgment that
    no code may pre-empt. The mapping must provide strictly
    increasing positive thresholds for 'review due', 'stale', and
    'expired'. Larger elapsed never yields an earlier label.
    """

    try:
        review_due = intervals["review due"]
        stale = intervals["stale"]
        expired = intervals["expired"]
    except (TypeError, KeyError):
        raise ProfileModelError(
            "staleness requires injected intervals for "
            "'review due', 'stale', and 'expired'") from None
    if not (0 < review_due < stale < expired):
        raise ProfileModelError(
            "staleness intervals must be positive and strictly increasing")
    if elapsed < 0:
        raise ProfileModelError("elapsed time cannot be negative")
    if elapsed < review_due:
        return "current"
    if elapsed < stale:
        return "review due"
    if elapsed < expired:
        return "stale"
    return "expired"
