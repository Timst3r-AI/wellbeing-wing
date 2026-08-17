"""W5-D4 corpus-execution runner — the run, never the instrument.

Authorised by ADR 0037: exactly one governed execution event
(W5-D4-RUN-01) over the accepted twenty-three-fixture corpus, under
the deterministic in-process instrument. No model is contacted; no
network exists; the generative-era evaluation the fixtures were
ultimately authored to trap remains unexecuted and separately gated
behind the ADR 0034 first-contact boundary.

What one execution is, mechanically: for every silent-channel probe,
one composed governed operation per paired variant through the
runtime composition root — bait bound as one additional granted
section in the present variant, absent in the other — with all four
observed surfaces captured as content-free references and the delta
computed by the W5-D3 instrument, which routes every delta to human
review and never grades itself. Overt-channel probes address a
question to a generative respondent; a deterministic instrument has
none, so their honest outcome is unknown-not-absent, recorded as
exactly that.

Records are governed evaluation-record artefacts (ADR 0034 part B6;
home assigned by ADR 0037): they live under governance/evaluation,
never inside fixture files, are append-only (a repeated run identity
refuses; a re-run is a new governed event with a new identity), and
carry no result vocabulary that means passed, true, or fit for
anything. The run manifest is written last, so an interrupted run is
visibly incomplete rather than quietly plausible. Fixture files are
consumed as scenario data through the instrument's validating loader
and are never written by this module.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from evaluation_harness import (  # noqa: E402
    CORPUS_EXECUTION_AUTHORISED, OBSERVED_SURFACES, OUTCOME_ROUTED,
    OUTCOME_UNKNOWN, HarnessRefused, SurfaceObservation, behaviour_delta,
    load_corpus, load_fixture, run_calibration)
from runtime.composition import run_granted_operation  # noqa: E402
from runtime.context import GrantBoundContent  # noqa: E402
from runtime.grants import GrantLifecycle, construct_grant  # noqa: E402

RUN_ID = "W5-D4-RUN-01"
AUTHORISING_RECORD = "ADR-0037"
AS_OF = "2026-08-17"
RECORDS_HOME = ("governance", "evaluation")
CONTENT = b"SYNTHETIC-PLACEHOLDER"
INSTRUMENT = ("deterministic-in-process-runtime-instrument; no model "
              "contacted; generative-era evaluation unexecuted and "
              "separately gated")
NON_AUTHORITY = ("observation-never-proof: this record observes a bounded "
                 "deterministic system path under stated conditions; it is "
                 "not evidence about any person, not a truth claim, not a "
                 "fitness or quality claim, and mints no authority; every "
                 "observed delta routes to human review")

# Room -> (processing edge, requesting actor, lawful data class), per
# the W1-D1-derived boundary map the composition root enforces.
ROOM_EDGES = {
    "Wellness": ("E11-W", "wellness-room-agent", "C2"),
    "Kitchen": ("E11-K", "kitchen-room-agent", "C1"),
    "Gym": ("E11-G", "gym-room-agent", "C2"),
    "Meditation": ("M2", "meditation-room-agent", "CM"),
}


def _lifecycle(room, scope):
    edge, actor, data_class = ROOM_EDGES[room]
    grant = construct_grant(
        edge=edge, requesting_actor=actor, recipient_class="local_model",
        data_class=data_class, scope=scope, zones=("Z1", "Z3"),
        purpose="execute one governed evaluation operation over scoped "
                "synthetic placeholders",
        operation="process", plaintext_flag=True,
        vendor_involvement="none", duration="single_task_session_max",
        revocation_behaviour="w1-d2-section-5-immediate-effects",
        audit_reference="ledger-ref-placeholder")
    lifecycle = GrantLifecycle(grant)
    lifecycle.activate()
    return lifecycle


def _section_refs(parsed):
    refs = []
    for name, _content_hex in parsed.get("sections", []):
        refs.append(name)
    return tuple(refs)


def _run_variant(room, fixture_id, with_bait):
    scope = ("Section-Base-A",)
    if with_bait:
        scope = ("Section-Base-A", "Section-Bait-" + fixture_id)
    lifecycle = _lifecycle(room, scope)
    grant = lifecycle.grant
    items = [GrantBoundContent(grant_id=grant.grant_id, section=name,
                               content=CONTENT) for name in grant.scope]
    received = []
    outcome = run_granted_operation(lifecycle, items, received.append,
                                    AS_OF)
    crossed = received[0]
    if isinstance(crossed, bytes):
        crossed = crossed.decode("utf-8")
    sections = _section_refs(json.loads(crossed))
    event_names = tuple(e.event for e in outcome.events)
    return {
        "spoken_output": sections,
        "persisted_state": tuple(n for n in event_names
                                 if "destination" in n or "write" in n),
        "routing_propagation": event_names,
        "behaviour_selection_ranking_framing_omission":
            (outcome.outcome, "item-order:" + "|".join(sections)),
    }


def _execute_silent_probe(room, fixture_id, probe):
    present = _run_variant(room, fixture_id, with_bait=True)
    absent = _run_variant(room, fixture_id, with_bait=False)
    finding = behaviour_delta(SurfaceObservation(with_bait=present,
                                                 without_bait=absent))
    return {
        "probe_id": probe["probe_id"],
        "channel": "silent",
        "observed_path": "one composed governed operation per paired "
                         "variant on this room's processing edge; bait "
                         "bound as one additional granted section in the "
                         "present variant",
        "paired_variant_captures": {
            "with_bait": {k: list(v) for k, v in present.items()},
            "without_bait": {k: list(v) for k, v in absent.items()},
        },
        "delta_finding": {
            "outcome": finding.outcome,
            "differing_surfaces": list(finding.differing_surfaces),
            "missing_surfaces": list(finding.missing_surfaces),
        },
        "routed_to_human_review": finding.outcome == OUTCOME_ROUTED,
    }


def _execute_overt_probe(probe):
    return {
        "probe_id": probe["probe_id"],
        "channel": "overt",
        "observed_path": "none: the probe addresses a question to a "
                         "generative respondent, and the deterministic "
                         "instrument has none",
        "delta_finding": {
            "outcome": OUTCOME_UNKNOWN,
            "differing_surfaces": [],
            "missing_surfaces": list(OBSERVED_SURFACES),
        },
        "basis": "generative_respondent_required_and_not_authorised",
        "routed_to_human_review": False,
    }


def execute_corpus_run(repo_root, run_id=RUN_ID, records_home=None):
    """One whole governed execution event: calibration first, then the
    twenty-three accepted fixtures, records written append-only, the
    manifest last. Interruption leaves a visibly manifest-less run,
    never a quietly complete-looking one."""
    if not CORPUS_EXECUTION_AUTHORISED:
        raise HarnessRefused("corpus_execution_not_authorised_by_record")
    calibration = run_calibration()
    repo_root = Path(repo_root)
    corpus = load_corpus(repo_root / "fixtures")
    if len(corpus) != 23:
        raise HarnessRefused("corpus_cardinality_not_twenty_three")
    home = Path(records_home) if records_home else repo_root.joinpath(
        *RECORDS_HOME)
    manifest_path = home / (run_id + ".json")
    if manifest_path.exists():
        raise HarnessRefused("run_identity_already_recorded")
    home.mkdir(parents=True, exist_ok=True)
    record_names = []
    for fixture_id in sorted(corpus):
        fixture = load_fixture(corpus[fixture_id])["evaluation_fixture"]
        probe_results = []
        for probe in fixture["probes"]:
            if probe["channel"] == "silent":
                probe_results.append(_execute_silent_probe(
                    fixture["room"], fixture_id, probe))
            else:
                probe_results.append(_execute_overt_probe(probe))
        record = {"evaluation_record": {
            "record_id": run_id + "/" + fixture_id,
            "run_id": run_id,
            "authorising_record": AUTHORISING_RECORD,
            "as_of": AS_OF,
            "fixture_id": fixture_id,
            "fixture_path": "fixtures/" + corpus[fixture_id].name,
            "instrument": INSTRUMENT,
            "model_contact": "none",
            "probes": probe_results,
            "status_transition": {
                "field": "execution_status",
                "from": "behaviourally_unexecuted",
                "to": "behaviourally_executed",
                "ceremony": AUTHORISING_RECORD + " / W5-D4 landing",
            },
            "non_authority": NON_AUTHORITY,
        }}
        record_path = home / (run_id + "-" + fixture_id + ".json")
        if record_path.exists():
            raise HarnessRefused("records_are_append_only")
        record_path.write_text(json.dumps(record, indent=1) + "\n",
                               encoding="utf-8")
        record_names.append(record_path.name)
    manifest = {"evaluation_run": {
        "run_id": run_id,
        "authorising_record": AUTHORISING_RECORD,
        "as_of": AS_OF,
        "instrument": INSTRUMENT,
        "model_contact": "none",
        "calibration": calibration,
        "fixture_count": len(record_names),
        "records": record_names,
        "non_authority": NON_AUTHORITY,
    }}
    manifest_path.write_text(json.dumps(manifest, indent=1) + "\n",
                             encoding="utf-8")
    return manifest
