"""Wellbeing Wing runtime freshness wiring (W5-D2-M03).

ADR 0029 at the runtime boundary: governed R/G/H policy keys for the
seven accepted freshness data types, the derived stale boundary
S = R + G, the engine-representation bridge, and the consequence
layer — bounded unknown, acknowledgement-as-surfacing-only, trigger
consumption, and the safeguard-14 fail-closed predicate.

This module re-implements no engine law: the label ladder lives in
the sealed engine's public staleness function, which consumes the
absolute interval triple this module derives (ADR 0029 decision 10 —
where a runtime supplies review due, stale and expired as absolute
values, stale there IS the computed S). This module imports nothing
from the engine; composition happens outside both, and the boundary
tests verify the wiring through the engine's own public function.

No clock is read anywhere; elapsed measures arrive injected, in
fixed-duration days of exactly 24 elapsed hours. A freshness policy
key is a governance policy, never a clinical taxonomy, and implies
nothing about membership of any safety-relevant set (ADR 0027).
"""

from dataclasses import dataclass

# The seven accepted freshness policy keys (ADR 0029 decision 13) —
# the corpus's own governance vocabulary. The set is closed; an
# eighth key is a future decision record's, never a runtime's.
FRESHNESS_POLICY_KEYS = (
    "medication", "allergy", "condition", "injury", "pregnancy status",
    "clinician instructions", "preference")

# Governed values (R, G, H) per key, from ADR 0029 decision 14.
# Every number below carries the exact governed label, unbroken:
# provisional governance default — not clinically validated
# Six keys carry identical values: that equality is a uniform
# provisional governance simplification and is not evidence of
# clinical equivalence (the non-equivalence rule, ADR 0029 decision
# 15). Unit: fixed-duration days.
_GOVERNED_VALUES = {
    "medication": (365, 91, 730),
    "allergy": (365, 91, 730),
    "condition": (365, 91, 730),
    "injury": (365, 91, 730),
    "pregnancy status": (365, 91, 730),
    "clinician instructions": (365, 91, 730),
    "preference": (730, 182, 1460),
}


class UnconstructablePolicy(Exception):
    """Content-free refusal: a fixed reason code, never submitted values."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


class AssertionWithheld(Exception):
    """Content-free refusal: the Wing declines to assert; nothing else."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class FreshnessPolicy:
    """One governance policy key. S is derived and only derived."""

    key: str
    review_interval_days: int
    renewal_grace_days: int
    hard_limit_days: int

    @property
    def stale_boundary_days(self):
        # S = R + G, computed always, governed never (ADR 0029 d7-d9).
        return self.review_interval_days + self.renewal_grace_days


def construct_policy(key, review_interval_days=None, renewal_grace_days=None,
                     hard_limit_days=None):
    """The only policy door. A key without a complete, strictly
    increasing R/G/H triple is unconstructable; no parameter for S
    exists anywhere."""
    if key not in FRESHNESS_POLICY_KEYS:
        raise UnconstructablePolicy("unknown_policy_key")
    named = {"review_interval_days": review_interval_days,
             "renewal_grace_days": renewal_grace_days,
             "hard_limit_days": hard_limit_days}
    for name, value in named.items():
        if value is None:
            raise UnconstructablePolicy("missing_" + name)
        if not isinstance(value, int) or value <= 0:
            raise UnconstructablePolicy("unlawful_" + name)
    if hard_limit_days <= review_interval_days + renewal_grace_days:
        raise UnconstructablePolicy("non_increasing_thresholds")
    return FreshnessPolicy(key=key, **named)


def governed_policy(key):
    """The governed default policy for one accepted key."""
    if key not in _GOVERNED_VALUES:
        raise UnconstructablePolicy("unknown_policy_key")
    r, g, h = _GOVERNED_VALUES[key]
    return construct_policy(key, review_interval_days=r,
                            renewal_grace_days=g, hard_limit_days=h)


def engine_intervals(policy):
    """The ADR 0029 decision-10 bridge: the absolute triple the sealed
    engine's public staleness function consumes. 'stale' here IS the
    computed S; nothing supplies it independently."""
    return {"review due": policy.review_interval_days,
            "stale": policy.stale_boundary_days,
            "expired": policy.hard_limit_days}


# Consequence treatments per ADR 0029 B1: expired stays the label,
# unknown is the treatment; stale is assertable only with explicit
# uncertainty in the output that relies on it.
TREATMENTS = {
    "current": "assertable",
    "review due": "assertable",
    "stale": "assertable_with_explicit_uncertainty",
    "expired": "unknown_treatment",
}


def assert_as_stable_truth(label):
    """The section 6.4 floor, structurally: only a current or
    review-due item may be asserted as stable truth; stale and
    expired refuse, content-free, always."""
    treatment = TREATMENTS.get(label)
    if treatment == "assertable":
        return treatment
    raise AssertionWithheld("not_assertable_as_stable_truth")


@dataclass(frozen=True)
class BoundedUnknown:
    """Unknown, first-class and bounded — never absence, never
    resolution, never reassurance. References only: last_known_ref
    and provenance_ref are opaque references, never content."""

    scope: str
    source_set: tuple
    as_of: str
    origin: str  # "expiry" or "at_source"
    last_known_ref: str = None
    provenance_ref: str = None
    age_days: int = None


def unknown_from_expiry(scope, source_set, as_of, last_known_ref,
                        provenance_ref, age_days):
    """Expiry-decayed unknown retains the last-known assertion by
    reference, with provenance and age — withdrawn from settled-truth
    use, never erased (ADR 0029 decision 32)."""
    if not (last_known_ref and provenance_ref) or age_days is None:
        raise UnconstructablePolicy("expiry_unknown_requires_retention_refs")
    return BoundedUnknown(scope=scope, source_set=tuple(source_set),
                          as_of=as_of, origin="expiry",
                          last_known_ref=last_known_ref,
                          provenance_ref=provenance_ref, age_days=age_days)


def unknown_at_source(scope, source_set, as_of):
    """Unknown with nothing to retain — bounded by scope, source set
    and as-of time, and never presented as the expiry kind."""
    return BoundedUnknown(scope=scope, source_set=tuple(source_set),
                          as_of=as_of, origin="at_source")


@dataclass(frozen=True)
class ItemGovernanceState:
    """The freshness-adjacent governance state an acknowledgement may
    never write (the exhaustive ADR 0029 decision-27 list)."""

    review_timestamp: str
    freshness_label: str
    authority_label: str
    provenance_ref: str
    contradiction_flag: bool
    supersession_link: str
    pending_review: bool


@dataclass(frozen=True)
class AcknowledgementEvent:
    """Surfacing only: a governance event, never a state change."""

    item_ref: str


def acknowledge(state, item_ref):
    """Acknowledgement is surfacing only. The state is frozen and is
    returned untouched by construction; the event is the only
    product, and no timestamp moves."""
    assert isinstance(state, ItemGovernanceState)
    return AcknowledgementEvent(item_ref=item_ref)


@dataclass(frozen=True)
class ReviewAct:
    """An explicit user review act — the only thing that renews."""

    item_ref: str
    reviewed_timestamp: str


def renew(state, review_act):
    """Renewal is a review act, not a refresh: without an explicit
    ReviewAct nothing re-dates, and with one the renewal is a new
    state, never a mutation of the old."""
    if not isinstance(review_act, ReviewAct):
        raise AssertionWithheld("renewal_requires_review_act")
    return ItemGovernanceState(
        review_timestamp=review_act.reviewed_timestamp,
        freshness_label="current",
        authority_label=state.authority_label,
        provenance_ref=state.provenance_ref,
        contradiction_flag=state.contradiction_flag,
        supersession_link=state.supersession_link,
        pending_review=False)


# The five re-review triggers, W1-D3 section 7, retained unaltered.
RE_REVIEW_TRIGGERS = (
    "interval_lapse", "new_upload_touching_section", "contradiction_flag",
    "supersession_proposal", "user_request")


@dataclass(frozen=True)
class ConsumedTrigger:
    """A consumed governance signal: structural consequence for later
    surfaces, never an edit of anything."""

    trigger: str
    item_ref: str


def consume_trigger(pending_triggers, trigger, item_ref):
    """Consume one pending trigger before a later reliance (ADR 0029
    decision 22). Pure: returns the remaining pending tuple and the
    consumed signal; rewrites no source record and moves no
    timestamp."""
    if trigger not in RE_REVIEW_TRIGGERS:
        raise UnconstructablePolicy("unknown_trigger")
    if trigger not in pending_triggers:
        raise UnconstructablePolicy("trigger_not_pending")
    remaining = tuple(t for t in pending_triggers if t != trigger)
    return remaining, ConsumedTrigger(trigger=trigger, item_ref=item_ref)


def safeguard14_fires(*, fact_uncertain,
                      completion_requires_assuming_absent_or_resolved,
                      safety_relevant, consulted_set_name):
    """The ADR 0025 safeguard-14 predicate, expressed and not
    performed: it fires when safe completion of a dependent operation
    would require assuming an uncertain safety-relevant fact absent
    or resolved — on that predicate alone, never on a label name.

    Membership is the caller's, consulted from a NAMED accepted set
    (ADR 0027): this module stores no set, adjudicates no membership,
    creates no canonical set, and makes no precedence between
    accepted surfacing mechanisms."""
    if not consulted_set_name or not isinstance(consulted_set_name, str):
        raise UnconstructablePolicy("consulted_set_must_be_named")
    return bool(fact_uncertain
                and completion_requires_assuming_absent_or_resolved
                and safety_relevant)


def withhold_dependent_assertion():
    """Fail closed: withhold exactly the dependent Wing assertion,
    content-free — never the user, never the room."""
    raise AssertionWithheld(
        "completion_would_require_assuming_uncertain_fact_absent_or_resolved")
