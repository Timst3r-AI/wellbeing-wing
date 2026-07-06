"""Transition catalogue, runnable matrix, and pure validator (W3-D4 M1).

W1-D3 section 4 supplies the central transition law here - note the
naming convention: "D3-T1..T8" are W1-D3's transitions; this module
is the W3-D4 deliverable. The closing rule every row below serves:
no transition skips review; no agent performs T2, T4, or T7; no
sequence of transitions can launder an agent suggestion into truth
without a user act in the chain.

Two different things, kept separate by design:

- **The catalogue names all eight transitions.** It is understanding,
  never permission - the grammar is incomplete without T1, so the
  engine must know every transition shape, including ones it may not
  run.
- **The runnable matrix permits only currently executable rows.**
  Refusal by absence applies to the matrix. T1 is catalogued but
  contributes zero runnable rows: any T1-shaped request is refused
  as dormant - a distinct status, not illegal - until grant
  machinery exists by its own future authority.

The validator classifies (data-only); the appliers act, and refusal
to act raises TransitionError with a message from the fixed
content-free vocabulary. Every applier validates through the
classifier first, so the runnable matrix stays the single source of
legality. Gated transitions (T2/T4/T7/T8) require a UserAct - a data
shape, not a surface. Within this repository the only place a
UserAct is ever constructed is the test tree: the suite walks the
application tree's syntax and fails on any construction site, no
production factory exists, and the shape is not re-exported. These
are repository-scoped guarantees; the project guards its own tree.

Appliers are in-memory only: they take no storage, crypto, port, or
file arguments, mutate nothing, build every successor through the
object-model constructors (the grammar re-validates at every step),
and return exactly one data-only LedgerEvent per success - emitted,
never stored. Durable ledger storage is deferred to its own future
decision. Truth-label persistence remains refused at the profile
write path regardless of what an applier computes in memory.
"""

from engine.core.profile import (
    STALENESS_DECAY_ORDER,
    TRUTH_LABELS,
    Contradiction,
    LedgerEvent,
    ProfileItem,
    Supersession,
    staleness_of,
)

CLASSIFICATION_STATUSES = frozenset(
    {"runnable", "gated", "dormant", "illegal"})

REASON_RUNNABLE = "legal transition"
REASON_GATED = "legal transition requiring a user act"
REASON_DORMANT = ("catalogued but dormant until grant machinery exists "
                  "by its own authority")
REASON_UNKNOWN = "unknown transition"
REASON_NO_ROW = "no runnable-matrix row permits this combination"
REASONS = frozenset({REASON_RUNNABLE, REASON_GATED, REASON_DORMANT,
                     REASON_UNKNOWN, REASON_NO_ROW})

# The catalogue: all eight W1-D3 transitions, named and understood.
# Actor strings are verbatim from the accepted grammar transcription.
TRANSITION_CATALOGUE = {
    "D3-T1": {"actor": "agent-under-e2-grant", "kind": "extraction",
              "output_label": "agent-extracted, pending review",
              "dormant": True},
    "D3-T2": {"actor": "user-review-only", "kind": "authority",
              "dormant": False},
    "D3-T3": {"actor": "system-on-user-entry", "kind": "entry",
              "output_label": "user-reported", "dormant": False},
    "D3-T4": {"actor": "user-review-only", "kind": "authority",
              "dormant": False},
    "D3-T5": {"actor": "time-automatic", "kind": "staleness-decay",
              "dormant": False},
    "D3-T6": {"actor": "system-flags-user-resolves", "kind": "flag",
              "dormant": False},
    # T7 is composite in the source grammar: the corrected item is
    # superseded AND the correction enters as confirmed. The runnable
    # matrix carries only the relabelling row in this milestone, by
    # ruling; the correction-entry side is application semantics for
    # the next milestone. No truth-label correction entry is minted
    # here.
    "D3-T7": {"actor": "user-only", "kind": "correction",
              "composite": True, "dormant": False},
    "D3-T8": {"actor": "user-review", "kind": "supersession",
              "dormant": False},
}

# The runnable matrix: (transition id, from-label, to-label, actor,
# requires_user_act). Every row restates a W1-D3 section 4 sentence;
# nothing here invents doctrine. T1 contributes zero rows.
RUNNABLE_MATRIX = (
    ("D3-T2", "agent-extracted, pending review", "confirmed by record",
     "user-review-only", True),
    ("D3-T3", None, "user-reported", "system-on-user-entry", False),
    ("D3-T4", "user-reported", "confirmed by user",
     "user-review-only", True),
    ("D3-T5", "current", "review due", "time-automatic", False),
    ("D3-T5", "review due", "stale", "time-automatic", False),
    ("D3-T5", "stale", "expired", "time-automatic", False),
    ("D3-T6", "confirmed by record", "contradicted",
     "system-flags-user-resolves", False),
    ("D3-T6", "confirmed by user", "contradicted",
     "system-flags-user-resolves", False),
    ("D3-T7", "confirmed by record", "outdated / superseded",
     "user-only", True),
    ("D3-T7", "confirmed by user", "outdated / superseded",
     "user-only", True),
    ("D3-T8", "confirmed by record", "outdated / superseded",
     "user-review", True),
    ("D3-T8", "confirmed by user", "outdated / superseded",
     "user-review", True),
)

# Sanity anchors, checked by the suite: decay rows follow the decay
# order; truth labels are reachable only through user-review actors.
_DECAY_PAIRS = tuple(zip(STALENESS_DECAY_ORDER, STALENESS_DECAY_ORDER[1:]))
assert all((f, t) in _DECAY_PAIRS
           for tid, f, t, _, _ in RUNNABLE_MATRIX if tid == "D3-T5")
assert all(gated for tid, _, t, _, gated in RUNNABLE_MATRIX
           if t in TRUTH_LABELS)


def classify_transition(transition_id, from_label, to_label, actor):
    """Classify a transition proposal. Pure, content-free, data-only.

    Returns {"status", "transition", "reason"} with status one of
    CLASSIFICATION_STATUSES and reason drawn from REASONS. Nothing is
    executed, mutated, persisted, or produced. Any T1-shaped request
    is dormant regardless of its labels or actor.
    """

    if transition_id in TRANSITION_CATALOGUE and \
            TRANSITION_CATALOGUE[transition_id]["dormant"]:
        return {"status": "dormant", "transition": transition_id,
                "reason": REASON_DORMANT}
    if transition_id not in TRANSITION_CATALOGUE:
        return {"status": "illegal", "transition": transition_id,
                "reason": REASON_UNKNOWN}
    for tid, row_from, row_to, row_actor, gated in RUNNABLE_MATRIX:
        if (tid == transition_id and row_from == from_label
                and row_to == to_label and row_actor == actor):
            if gated:
                return {"status": "gated", "transition": transition_id,
                        "reason": REASON_GATED}
            return {"status": "runnable", "transition": transition_id,
                    "reason": REASON_RUNNABLE}
    return {"status": "illegal", "transition": transition_id,
            "reason": REASON_NO_ROW}


# --- The applier layer (W3-D4 M2) ---------------------------------

USER_CAPACITIES = frozenset({"user-review-only", "user-only", "user-review"})

REFUSE_DORMANT = REASON_DORMANT
REFUSE_ILLEGAL = "transition is not a runnable-matrix row"
REFUSE_NO_ACT = "gated transition requires a user act"
REFUSE_WRONG_CAPACITY = "user act capacity does not match the transition actor"
REFUSE_BAD_ACT = "a user act requires a known capacity, an acted-at time, and a scope"
REFUSE_NO_DECAY = "no staleness decay is due"
TRANSITION_REFUSALS = frozenset({
    REFUSE_DORMANT, REFUSE_ILLEGAL, REFUSE_NO_ACT,
    REFUSE_WRONG_CAPACITY, REFUSE_BAD_ACT, REFUSE_NO_DECAY,
})


class TransitionError(ValueError):
    """The transition may not be applied. Messages are drawn from the
    fixed vocabulary above and never contain item content."""


class UserAct:
    """A user act as data - never a surface, never a command.

    Constructed, within this repository, only in the test tree: the
    suite fails on any application-tree construction site. No
    production factory exists and the shape is not re-exported.
    """

    def __init__(self, capacity, acted_at, scope):
        if capacity not in USER_CAPACITIES or not acted_at or not scope:
            raise TransitionError(REFUSE_BAD_ACT)
        self.capacity = capacity
        self.acted_at = acted_at
        self.scope = scope


def authorise_transition(transition_id, from_label, to_label, actor,
                         act=None):
    """The raising bridge from classification to application.

    Dormant and illegal proposals raise; gated proposals raise
    without a matching act. Returns the classification on success.
    """
    result = classify_transition(transition_id, from_label, to_label, actor)
    if result["status"] == "dormant":
        raise TransitionError(REFUSE_DORMANT)
    if result["status"] == "illegal":
        raise TransitionError(REFUSE_ILLEGAL)
    if result["status"] == "gated":
        if not isinstance(act, UserAct):
            raise TransitionError(REFUSE_NO_ACT)
        if act.capacity != actor:
            raise TransitionError(REFUSE_WRONG_CAPACITY)
    return result


def apply_user_entry(section, content, entered_at):
    """T3: user entry becomes a user-reported item. One event."""
    authorise_transition("D3-T3", None, "user-reported",
                         "system-on-user-entry")
    item = ProfileItem(section, content, "user-reported",
                       "system-on-user-entry", "unknown freshness")
    return {"item": item,
            "event": LedgerEvent("D3-T3", (section,), entered_at)}


def apply_staleness_decay(item, elapsed, intervals):
    """T5: one adjacent staleness step, label-only. One event.

    Multi-step decay is repeated application. Authority is untouched
    by construction. The engine core has no clock, so time-automatic
    events record the elapsed measure they were computed from.
    """
    target = staleness_of(elapsed, intervals)
    order = STALENESS_DECAY_ORDER
    if item.staleness not in order:
        authorise_transition("D3-T5", item.staleness, target,
                             "time-automatic")  # raises: no such row
    position = order.index(item.staleness)
    if position + 1 >= len(order) or order.index(target) <= position:
        raise TransitionError(REFUSE_NO_DECAY)
    next_label = order[position + 1]
    authorise_transition("D3-T5", item.staleness, next_label,
                         "time-automatic")
    successor = ProfileItem(item.section, item.content, item.authority,
                            item.assigned_by, next_label,
                            last_reviewed=item.last_reviewed,
                            provenance=item.provenance)
    return {"item": successor,
            "event": LedgerEvent(
                "D3-T5", (item.section, item.staleness, next_label),
                f"elapsed-{elapsed}")}


def apply_contradiction_flag(confirmed_item, other_side, detected_at):
    """T6: flag and visibly suspend. Both sides retained. One event."""
    authorise_transition("D3-T6", confirmed_item.authority, "contradicted",
                         "system-flags-user-resolves")
    flagged = ProfileItem(confirmed_item.section, confirmed_item.content,
                          "contradicted", "system",
                          confirmed_item.staleness,
                          last_reviewed=confirmed_item.last_reviewed,
                          provenance=confirmed_item.provenance)
    contradiction = Contradiction(confirmed_item, other_side, detected_at)
    return {"item": flagged, "contradiction": contradiction,
            "event": LedgerEvent("D3-T6", (confirmed_item.section,),
                                 detected_at)}


def apply_confirm_by_record(item, act, provenance, reviewed_at):
    """T2: confirmed by record, in memory only. Gated. One event."""
    authorise_transition("D3-T2", item.authority, "confirmed by record",
                         "user-review-only", act)
    successor = ProfileItem(item.section, item.content,
                            "confirmed by record", "user-review", "current",
                            last_reviewed=reviewed_at,
                            provenance=provenance)
    return {"item": successor,
            "event": LedgerEvent("D3-T2", (item.section,), reviewed_at)}


def apply_confirm_by_user(item, act, provenance, reviewed_at):
    """T4: confirmed by user, in memory only. Gated. One event."""
    authorise_transition("D3-T4", item.authority, "confirmed by user",
                         "user-review-only", act)
    successor = ProfileItem(item.section, item.content,
                            "confirmed by user", "user-review", "current",
                            last_reviewed=reviewed_at,
                            provenance=provenance)
    return {"item": successor,
            "event": LedgerEvent("D3-T4", (item.section,), reviewed_at)}


def apply_correction(confirmed_item, correction_content, act, provenance):
    """T7, the composite: supersede the corrected item and mint the
    correction as confirmed by user, in memory only. Gated. One event.
    The predecessor is retained and relabelled - nothing is removed."""
    authorise_transition("D3-T7", confirmed_item.authority,
                         "outdated / superseded", "user-only", act)
    superseded = ProfileItem(confirmed_item.section, confirmed_item.content,
                             "outdated / superseded", "user", "superseded",
                             last_reviewed=confirmed_item.last_reviewed,
                             provenance=confirmed_item.provenance)
    correction = ProfileItem(confirmed_item.section, correction_content,
                             "confirmed by user", "user-review", "current",
                             last_reviewed=act.acted_at,
                             provenance=provenance)
    link = Supersession(superseded, correction, act.acted_at)
    return {"superseded": superseded, "correction": correction,
            "supersession": link,
            "event": LedgerEvent("D3-T7", (confirmed_item.section,),
                                 act.acted_at)}


def apply_supersession(old_item, successor_item, act):
    """T8: supersession only - no reactivation, no undo, no removal.
    The old item is retained and relabelled; the successor is linked.
    Gated. One event."""
    authorise_transition("D3-T8", old_item.authority,
                         "outdated / superseded", "user-review", act)
    superseded = ProfileItem(old_item.section, old_item.content,
                             "outdated / superseded", "user-review",
                             "superseded",
                             last_reviewed=old_item.last_reviewed,
                             provenance=old_item.provenance)
    link = Supersession(superseded, successor_item, act.acted_at)
    return {"superseded": superseded, "successor": successor_item,
            "supersession": link,
            "event": LedgerEvent("D3-T8", (old_item.section,),
                                 act.acted_at)}
