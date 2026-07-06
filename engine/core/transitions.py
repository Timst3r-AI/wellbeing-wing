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

This milestone classifies; it executes nothing. There is no
application, no user-act handling, no event production, no
persistence, and no mutation. Gated transitions (T2/T4/T7/T8) are
recognised as legal in shape and refused for execution until the
application milestone supplies act handling under its own guards.
The validator is content-free by signature: it receives labels,
actors, and a transition id - never an item, never content - and
every reason it returns is drawn from the fixed vocabulary below.
"""

from engine.core.profile import STALENESS_DECAY_ORDER, TRUTH_LABELS

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
