"""Behavioural evaluation harness (W5-D3) — the instrument, never the run.

ADR 0034's boundary contract made real: the harness consumes fixture
data as its sole scenario source, supports paired-variant observation
across all four required surfaces, distinguishes the mechanical from
the judged, carries false-positive and false-negative guards as
fitness conditions, preserves honest unknown, and never grades
itself — every observed delta routes to human review, and no outcome
vocabulary here means passed, safe, or true.

The corpus-execution interlock is structural and record-governed:
CORPUS_EXECUTION_AUTHORISED was False for the whole of W5-D3 and was
amended to True by ADR 0037, the W5-D4 corpus-execution authorisation
— exactly the governed act the W5-D3 landing named. Even authorised,
the instrument itself never runs the corpus: execution machinery
lives in the runner (evaluation_execution), and every in-instrument
execution request still refuses. The instrument observes; the run is
a separately governed act.

This module imports nothing from the runtime, contacts nothing, and
writes nothing: it reads repository fixture data (synthetic grammar
placeholders only, validated at load) and produces in-memory,
content-free shapes. Fixture execution_status is read and validated
against the ADR 0034 decision 39 closed two-value vocabulary, never
changed — transitions are governed ceremony events, and W5-D4-RUN-01
performed exactly one, by record.
"""

import json
from dataclasses import dataclass
from pathlib import Path

# Amended False -> True by ADR 0037 (W5-D4 corpus-execution
# authorisation) — the governed act the W5-D3 landing named. The
# instrument still never runs: execution lives in the runner.
CORPUS_EXECUTION_AUTHORISED = True

REQUIRED_NOTICE = ("SYNTHETIC fixture authored for governance testing. "
                   "Corresponds to no real person. Values are grammar "
                   "placeholders, not medical content.")

# ADR 0034 decision 39: the closed two-value vocabulary. Status is
# execution-state only and never encodes a result; the barred values
# are refused by name so a status field can never smuggle an outcome.
BIRTH_STATUS = "behaviourally_unexecuted"
EXECUTED_STATUS = "behaviourally_executed"
LAWFUL_STATUSES = (BIRTH_STATUS, EXECUTED_STATUS)
BARRED_STATUSES = ("executed_pass", "executed_fail", "passed", "failed",
                   "conforming", "nonconforming", "safe", "unsafe")

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

    Loading validates the synthetic discipline and the closed
    execution-status vocabulary; a fixture that fails either is
    refused, and nothing here ever writes a fixture back."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    marker = data.get("synthetic_marker", {})
    if marker.get("synthetic") is not True:
        raise HarnessRefused("fixture_not_marked_synthetic")
    if marker.get("notice") != REQUIRED_NOTICE:
        raise HarnessRefused("fixture_notice_not_verbatim")
    fixture = data.get("evaluation_fixture", {})
    if fixture.get("execution_status") not in LAWFUL_STATUSES:
        raise HarnessRefused("fixture_status_not_in_closed_vocabulary")
    return data


def load_corpus(fixtures_dir):
    """Reference the whole corpus, validated, executed never by the
    instrument — the run belongs to the governed runner alone."""
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
    """The instrument's non-door, held shut in every era. Corpus
    execution is authorised by record (ADR 0037), and even so the
    instrument never runs it: the run is the governed runner's
    (evaluation_execution), which observes through this instrument
    and answers to its own proofs. Instrument and run stay distinct
    — that separation is the discipline, not a limitation."""
    if not CORPUS_EXECUTION_AUTHORISED:
        raise HarnessRefused("corpus_execution_not_authorised_by_record")
    raise HarnessRefused("execution_lives_in_the_runner_never_the_instrument")
