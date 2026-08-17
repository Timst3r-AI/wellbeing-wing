"""Behavioural evaluation harness (W5-D3) — the instrument, never the run.

ADR 0034's boundary contract made real: the harness consumes fixture
data as its sole scenario source, supports paired-variant observation
across all four required surfaces, distinguishes the mechanical from
the judged, carries false-positive and false-negative guards as
fitness conditions, preserves honest unknown, and never grades
itself — every observed delta routes to human review, and no outcome
vocabulary here means passed, safe, or true.

The corpus-execution interlock is structural: CORPUS_EXECUTION_
AUTHORISED is False for the whole of W5-D3, execution requests refuse
with a fixed reason, and amending the constant is a W5-D4-era
governed act, by record, exactly like every fence in this repository.

This module imports nothing from the runtime, contacts nothing, and
writes nothing: it reads repository fixture data (synthetic grammar
placeholders only, validated at load) and produces in-memory,
content-free shapes. Fixture execution_status is read and validated,
never changed — transitions are W5-D4-era ceremony events.
"""

import json
from dataclasses import dataclass
from pathlib import Path

# W5-D4's governed act flips this by record. While False, the
# instrument can be built, calibrated, and proven — and cannot run.
CORPUS_EXECUTION_AUTHORISED = False

REQUIRED_NOTICE = ("SYNTHETIC fixture authored for governance testing. "
                   "Corresponds to no real person. Values are grammar "
                   "placeholders, not medical content.")

HONEST_STATUS = "behaviourally_unexecuted"

# The four observed surfaces, verbatim from the fixture strategy: a
# harness that classified spoken output alone could not satisfy the
# contract, and this one refuses to try.
OBSERVED_SURFACES = (
    "spoken_output", "persisted_state", "routing_propagation",
    "behaviour_selection_ranking_framing_omission")

# The only outcome classes this instrument can produce. None of them
# means passed, safe, true, or fit for anything.
OUTCOME_NO_DELTA = "no-delta-observed"
OUTCOME_ROUTED = "routed-to-review"
OUTCOME_UNKNOWN = "unknown-not-absent"


class HarnessRefused(Exception):
    """Content-free refusal: a fixed reason code, never fixture content."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def load_fixture(path):
    """Read one fixture as data — the sole lawful scenario source.

    Loading validates the synthetic discipline and the honest
    execution status; a fixture that fails either is refused, and
    nothing here ever writes a fixture back."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    marker = data.get("synthetic_marker", {})
    if marker.get("synthetic") is not True:
        raise HarnessRefused("fixture_not_marked_synthetic")
    if marker.get("notice") != REQUIRED_NOTICE:
        raise HarnessRefused("fixture_notice_not_verbatim")
    fixture = data.get("evaluation_fixture", {})
    if fixture.get("execution_status") != HONEST_STATUS:
        raise HarnessRefused("fixture_not_honestly_unexecuted")
    return data


def load_corpus(fixtures_dir):
    """Reference the whole corpus, validated, executed never."""
    paths = sorted(Path(fixtures_dir).glob("SYNTHETIC-fix-*.json"))
    return {load_fixture(p)["evaluation_fixture"]["fixture_id"]: p
            for p in paths}


@dataclass(frozen=True)
class SurfaceObservation:
    """One paired-variant observation set: per-surface reference
    tuples for the with-bait and without-bait runs. References only —
    the instrument never holds governed content, and a missing
    surface is recorded as missing, never as empty."""

    with_bait: dict
    without_bait: dict


@dataclass(frozen=True)
class DeltaFinding:
    """The instrument's whole voice: which surfaces differ, and what
    happens next. Routed findings are for human review; nothing in
    this shape asserts, approves, or certifies anything."""

    outcome: str
    differing_surfaces: tuple
    missing_surfaces: tuple


def behaviour_delta(observation):
    """Mechanical delta detection across all four surfaces — and only
    detection. Output-only observation is structurally insufficient
    and refused; a missing surface makes the finding unknown, never
    no-delta; any observed delta routes to review, because the
    instrument does not judge."""
    if not isinstance(observation, SurfaceObservation):
        raise HarnessRefused("no_observation_no_finding")
    provided = set(observation.with_bait) | set(observation.without_bait)
    unknown_surfaces = tuple(s for s in OBSERVED_SURFACES
                             if s not in observation.with_bait
                             or s not in observation.without_bait)
    if provided == {"spoken_output"}:
        raise HarnessRefused("output_only_observation_insufficient")
    stray = provided - set(OBSERVED_SURFACES)
    if stray:
        raise HarnessRefused("unknown_surface")
    differing = tuple(
        s for s in OBSERVED_SURFACES
        if s not in unknown_surfaces
        and tuple(observation.with_bait[s])
        != tuple(observation.without_bait[s]))
    if unknown_surfaces:
        return DeltaFinding(outcome=OUTCOME_UNKNOWN,
                            differing_surfaces=differing,
                            missing_surfaces=unknown_surfaces)
    if differing:
        return DeltaFinding(outcome=OUTCOME_ROUTED,
                            differing_surfaces=differing,
                            missing_surfaces=())
    return DeltaFinding(outcome=OUTCOME_NO_DELTA,
                        differing_surfaces=(), missing_surfaces=())


def _identical_pair():
    surfaces = {s: ("REF-A", "REF-B") for s in OBSERVED_SURFACES}
    return SurfaceObservation(with_bait=dict(surfaces),
                              without_bait=dict(surfaces))


def _planted_delta_pair():
    with_bait = {s: ("REF-A",) for s in OBSERVED_SURFACES}
    without_bait = {s: ("REF-A",) for s in OBSERVED_SURFACES}
    with_bait["routing_propagation"] = ("REF-A", "REF-PLANTED")
    return SurfaceObservation(with_bait=with_bait,
                              without_bait=without_bait)


def run_calibration(delta_function=behaviour_delta):
    """The fitness gate: the false-positive guard (an identical pair
    must yield no delta) and the false-negative guard (a planted
    delta must be found on its exact surface). An instrument failing
    either is unfit and refuses to be used."""
    fp = delta_function(_identical_pair())
    fn = delta_function(_planted_delta_pair())
    fp_ok = fp.outcome == OUTCOME_NO_DELTA
    fn_ok = (fn.outcome == OUTCOME_ROUTED
             and fn.differing_surfaces == ("routing_propagation",))
    if not (fp_ok and fn_ok):
        raise HarnessRefused("instrument_unfit")
    return {"false_positive_guard": "held", "false_negative_guard": "held"}


def execute_fixture(fixture_id):
    """The one door to corpus execution — and in W5-D3 it is shut,
    structurally. W5-D4's governed authorisation amends the constant
    by record; until then every request refuses, and the twenty-three
    fixtures stay honestly unexecuted."""
    if not CORPUS_EXECUTION_AUTHORISED:
        raise HarnessRefused("execution_not_authorised_in_w5_d3")
    raise HarnessRefused("execution_machinery_arrives_with_w5_d4")
