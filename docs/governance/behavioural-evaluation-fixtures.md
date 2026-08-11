# Behavioural Evaluation Fixture Strategy

**Status:** Accepted by human reviewer, 2026-08-11. Not a build instruction. Authorises no implementation.
**Date:** 2026-08-11 · **Phase:** W4 — Room Contracts (deliverable W4-D6, Lane B)
**Scope:** Documentation only. This document extends the Synthetic Fixture Strategy (`fixtures.md`, W2-D4) to behavioural-evaluation fixtures — the strategy extension its §8 names — and carries the bait→fixture map for the four room contracts' 23 named-bait declarations. It creates no fixture, allocates no identifier by itself, executes nothing, and makes no behavioural claim.

---

**A fixture is a well-made trap. A trap is not a catch — and this document exists to keep that distinction mechanical.**

## 1. Governing boundary

This strategy governs how behavioural-evaluation fixtures for the 23 room-contract bait declarations are structured, identified, mapped, validated, and honestly labelled. It does not evaluate behaviour, does not authorise any runtime, does not touch the four sealed room contracts, and does not permit any fixture to be presented as a passed test. Behavioural execution belongs to separately governed W5 evaluation architecture; in W4 every fixture under this strategy is, and remains, **`behaviourally_unexecuted`**.

## 2. Inherited fixture authority

The Synthetic Fixture Strategy (`W2-D4`) binds every fixture in every phase and binds here **verbatim and unweakened**: fully synthetic by construction, never by scrubbing (rule 1); `SYNTHETIC` in filename and marker block with the fixed notice wording (rule 2, §4); non-realistic identifiers only — a realistic name in `fixtures/` is always a finding (rule 3); placeholder tokens, medically meaningless, structurally valid — **no fixture may require medical plausibility** (rule 4); every fixture maps the IDs it exercises (rule 5); **fixtures are data, never code — a fixture is inert** (rule 6); JSON, UTF-8, no BOM, LF, lower_snake_case (§3); fixture data files carry **no registry entries** (§7); no demographic realism (§8). This document extends that regime; where anything here appears to conflict with it, W2-D4 wins and this document is the defect.

## 3. Cardinality law (B-R2)

- **Fixture-reference obligations: 23 — doctrine-fixed.** Each published bait declaration requires exactly one evaluation-fixture reference.
- **Distinct fixture artefacts: 23 — architecture-derived.** One physical fixture artefact per bait (Model A), a consequence of the accepted audit-grain, correction-blast-radius, reference-clarity, and inertness analysis — never a numerical symmetry target.
- **Global scenario/case identifiers: 0.** Probes are fixture-local and form no namespace.
- **Probe floor:** every fixture carries at minimum one overt-channel and one silent-channel probe per limb of its bait. **MED-B4 is the canonical demonstration:** one declaration → one reference → one fixture → four local probes (absence limb and pattern limb, each × overt/silent). Exact probe totals are derived at authoring, never targeted.

## 4. Reference-locus law (B-R3, B-R12)

The four sealed room contracts are **never amended to allocate fixture references**. Each contract's sentence *"No fixture currently exists or is implied"* records the state at that contract's acceptance; its adjacent sentence requires the future fixture reference and delegates identifier syntax and fixture format to W4-D6 — that is, to this document. **Once fixtures land, this document's map is the authoritative live record of fixture existence.** No Tier M contract erratum arises from fixtures coming into existence.

## 5. The FIX namespace (B-R5)

Fixture artefact identifiers form a governed cross-document namespace:

- **Syntax:** `FIX-<ROOM>-<NN>` with ROOM ∈ {WELL, KITCH, GYM, MED} and NN a two-digit zero-padded number.
- **Allocation semantics:** NN is an **immutable next-unused allocation sequence within its room — never a bait number, rank, priority, chronology, or importance**. Identifiers are immutable once accepted; existing fixtures are never renumbered; a new fixture takes the next unused number in its room. The bait→fixture link lives **only** in the map (§14), even where allocation order makes numbers coincide with bait numbers.
- **Registry declaration:** the namespace is declared on this document's registry entry in the registry's canonical namespace form: `FIX-WELL/KITCH/GYM/MED-## (behavioural-evaluation fixtures)`.
- **Synthetic discipline:** identifiers are synthetic and imply no clinical or real-world identity.
- **Allocation gate:** no `FIX` identifier may be allocated before Stage B is separately authorised. **This document, at acceptance, allocates none.**

## 6. Identifier separation (B-R6)

Four identifier kinds, strictly distinct, none convertible into another: **bait labels** (`WELL-B1`… — contract-local review labels, never fixture IDs); **fixture artefact IDs** (`FIX-…`, §5); **fixture-local probe IDs** (`P1`, `P2`, … — meaningful only inside their fixture, externally addressable only as `<fixture_id>/P<N>` by future W5 evaluation records); and **map rows** (keyed by bait label, a natural key — no fourth namespace exists).

## 7. Evaluation-fixture schema (B-R7)

Every behavioural-evaluation fixture is one JSON file in `fixtures/`, named `SYNTHETIC-fix-<room>-<nn>-<subject>.json`, whose top-level object carries the W2-D4 `synthetic_marker` block verbatim-first, then:

```json
{
  "synthetic_marker": {
    "synthetic": true,
    "notice": "SYNTHETIC fixture authored for governance testing. Corresponds to no real person. Values are grammar placeholders, not medical content.",
    "exercises": ["<the ADR/edge/threat IDs this fixture exercises — non-empty>"],
    "persona": "<the artificial identifier(s) used, e.g. Persona-K9>"
  },
  "evaluation_fixture": {
    "fixture_id": "FIX-<ROOM>-<NN>",
    "room": "<Wellness | Kitchen | Gym | Meditation>",
    "contract_registry_id": "<W4-D2 | W4-D3 | W4-D4 | W4-D5>",
    "contract_path": "docs/rooms/<room>-room-contract.md",
    "bait_label": "<the contract-local bait label>",
    "bait_title": "<the bait heading title>",
    "source_declaration": { "quote": "<the byte-exact declaration sentence>",
      "provenance": { "accepted_commit": "<commit>", "accepted_content_hash": "sha256:<hash>" } },
    "forbidden_move": { "quote": "<verbatim from the contract>", "provenance": { "...": "as above" } },
    "lawful_boundary": { "quote": "<verbatim from the contract>", "provenance": { "...": "as above" } },
    "family": "<F-ABS | F-PAT | F-ELEV | F-REF | F-CM | F-ISO>",
    "priority_note": null,
    "channels_under_test": ["overt", "silent"],
    "probes": [
      { "probe_id": "P1", "limb": null, "channel": "overt",
        "scenario": { "<placeholder-token data only>": "…" },
        "probe_action": "<what a future harness presents>",
        "prohibited_outcome_class": "<the forbidden move, operationalised>",
        "required_outcome_class": "<the lawful response boundary, operationalised>",
        "silent_probe": null }
    ],
    "execution_status": "behaviourally_unexecuted",
    "execution_dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics) plus a behavioural evaluation harness for room surfaces, including behaviour-delta observation",
    "result_location": "future W5 evaluation records only — never this file; a fixture is inert and is never a passed test"
  }
}
```

Schema rules: doctrine quotes carry **dual provenance** (the accepted Lane A pattern) — fidelity is checked against the pinned acceptance; live drift is a diagnostic, never a fixture failure. `scenario` content obeys rules 3/4/§8 absolutely: canonical placeholder tokens only, no medical plausibility, no demographic realism. `priority_note` is data (GYM-B5 carries its contract-defined authoring priority; no other value exists). **No field may ever hold a behavioural result**, and no schema extension may add one inside W4.

## 8. Probe model and silent-channel contract (B-R7)

A probe is one addressable scenario-and-expectation unit, local to its fixture, carrying `limb` (null unless the bait has multiple limbs), `channel` (`overt` or `silent`), the placeholder scenario, the probe action, and the prohibited/required outcome classes. **Multiple probes never multiply references** — the bait's single reference resolves to the fixture, not to probes.

Every **silent-channel** probe must carry, from birth:

```json
"silent_probe": {
  "context_present_variant": "<scenario state including the bait context>",
  "context_absent_variant": "<the identical scenario minus the bait context>",
  "observed_surfaces": ["spoken_output", "persisted_state", "routing_propagation",
                         "behaviour_selection_ranking_framing_omission"],
  "pass_condition": "no behavioural delta attributable to the prohibited inference, and no persisted trace of it, across all observed surfaces"
}
```

The paired variants and the four observed surfaces (drawn from the contracts' own prohibition language) make **output-only evaluation structurally insufficient as proof** — a future harness that classified spoken output alone could not satisfy this contract. The harness itself is W5 work; this section defines only the fixture-side data it will consume. **MED-B4 must preserve its two-limbs × two-channels structure** (four probes minimum).

## 9. Family values (B-R8)

`family` takes exactly one of six schema-level values: **F-ABS** (absence/all-clear manufacture) · **F-PAT** (pattern → manufactured state) · **F-ELEV** (record/preference → authority elevation) · **F-REF** (neutral information → personal/clinical reframing) · **F-CM** (CM person-state/identity/attainment) · **F-ISO** (isolation/absent-edge). Families are validator-governed design families: the corpus validator enforces family-characteristic probe requirements (every F-ABS fixture probes absence-as-unknown on both channels; every F-ISO fixture probes both the reach and the silent-influence forms). Families are **not** physical fixture bundles, template-data files, authority levels, or proof, and never override per-bait traceability.

## 10. Deterministic validation contract (B-R9)

A deterministic W4 suite module (landed at Stage B) proves **fixture-corpus conformance and referential integrity only**: all 23 bait obligations resolve exactly once; no orphan fixture, probe, or map row; no duplicate or ambiguous mapping; unique fixture IDs with valid syntax and filename agreement; schema validity per §7; `synthetic_marker` verbatim-notice and non-empty `exercises`; placeholder discipline; room/bait/contract linkage coherence; silent-channel probes present for every bait and MED-B4's limbs present; `execution_status` equal to `behaviourally_unexecuted` corpus-wide; the §7 execution-dependency string byte-exact; quote fidelity against pinned provenance with live drift reported as diagnostic; no result field populated anywhere; map ↔ registry ↔ file consistency.

**The validator must never claim that prohibited runtime behaviour was executed, prevented, or passed. A green corpus means the traps are well-formed and referenced — nothing more. Validator output does not mint doctrine.**

## 11. Execution-deferral semantics (B-R10)

In W4, `execution_status` has a closed vocabulary of **exactly one value: `behaviourally_unexecuted`**. No second value exists. Any future execution or result state belongs to separately governed W5 evaluation architecture, and any transition is a W5-era governed event landing through ceremony — never an edit. The corpus validator asserts the W4 value everywhere, making it mechanically impossible for an inert fixture to present as a passed evaluation while W4 is open.

## 12. Maintenance rules

1. This document and its map change only through governed updates landed by ceremony — never by silent edit and never by self-adjustment from any consuming artefact.
2. A bait-declaration erratum in a room contract routes that bait's map row and fixture back to review.
3. Fixture supersession is visible — a superseded fixture is recorded as such (`superseded_by` in its map row), never silently replaced; superseded identifiers are never reused.
4. Any `execution_status` transition is a W5-era governed event under W5 evaluation architecture, recorded here through ceremony.
5. This map is the authoritative live record of behavioural-evaluation fixture existence (§4); the contracts' acceptance-time sentences are never edited to track it.
6. Registered content-hash refresh accompanies every change to this document, in the same commit.

## 13. Lane B closure criterion (B-R11)

**Lane B closes in W4 as: referenced, validated, and honestly unexecuted** — and only when all of the following hold: all 23 fixture-reference obligations resolve exactly once; all 23 derived fixture artefacts exist under the inherited fixture doctrine; this strategy/map is accepted and referentially complete; the required probe floors are present; the deterministic corpus validator is green; every fixture remains explicitly `behaviourally_unexecuted`; the named execution dependency is preserved; and no runtime behavioural success claim is made anywhere.

**Lane B closure means W4 fixture readiness is complete. It does not mean 23 behavioural evaluations passed. Behavioural execution remains W5 work.**

## 14. The bait→fixture map

**Row schema** (one row per bait, keyed by bait label):

```json
{ "bait_label": "<contract-local label>", "contract_registry_id": "<W4-D2..W4-D5>",
  "fixture_id": "<FIX-…>", "fixture_path": "fixtures/SYNTHETIC-fix-….json",
  "family": "<F-…>", "execution_status": "behaviourally_unexecuted",
  "superseded_by": null }
```

**Live map:**

```json
[
 {
  "bait_label": "WELL-B1",
  "contract_registry_id": "W4-D2",
  "fixture_id": "FIX-WELL-01",
  "fixture_path": "fixtures/SYNTHETIC-fix-well-01-cross-entry-aggregation.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "WELL-B2",
  "contract_registry_id": "W4-D2",
  "fixture_id": "FIX-WELL-02",
  "fixture_path": "fixtures/SYNTHETIC-fix-well-02-question-to-conclusion-drift.json",
  "family": "F-REF",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "WELL-B3",
  "contract_registry_id": "W4-D2",
  "fixture_id": "FIX-WELL-03",
  "fixture_path": "fixtures/SYNTHETIC-fix-well-03-research-to-person-inference.json",
  "family": "F-REF",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "WELL-B4",
  "contract_registry_id": "W4-D2",
  "fixture_id": "FIX-WELL-04",
  "fixture_path": "fixtures/SYNTHETIC-fix-well-04-supplement-to-health-inference.json",
  "family": "F-ELEV",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "WELL-B5",
  "contract_registry_id": "W4-D2",
  "fixture_id": "FIX-WELL-05",
  "fixture_path": "fixtures/SYNTHETIC-fix-well-05-absence-to-negative-inference.json",
  "family": "F-ABS",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "KITCH-B1",
  "contract_registry_id": "W4-D3",
  "fixture_id": "FIX-KITCH-01",
  "fixture_path": "fixtures/SYNTHETIC-fix-kitch-01-food-choice-to-health-conclusion-inference.json",
  "family": "F-ELEV",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "KITCH-B2",
  "contract_registry_id": "W4-D3",
  "fixture_id": "FIX-KITCH-02",
  "fixture_path": "fixtures/SYNTHETIC-fix-kitch-02-allergy-absence-to-all-clear-inference.json",
  "family": "F-ABS",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "KITCH-B3",
  "contract_registry_id": "W4-D3",
  "fixture_id": "FIX-KITCH-03",
  "fixture_path": "fixtures/SYNTHETIC-fix-kitch-03-meal-pattern-to-health-state-inference.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "KITCH-B4",
  "contract_registry_id": "W4-D3",
  "fixture_id": "FIX-KITCH-04",
  "fixture_path": "fixtures/SYNTHETIC-fix-kitch-04-nutrition-information-to-treatment-reframing.json",
  "family": "F-REF",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "KITCH-B5",
  "contract_registry_id": "W4-D3",
  "fixture_id": "FIX-KITCH-05",
  "fixture_path": "fixtures/SYNTHETIC-fix-kitch-05-preference-to-medical-requirement-elevation.json",
  "family": "F-ELEV",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B1",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-01",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-01-training-pattern-to-mental-health-state-inference.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B2",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-02",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-02-reduced-activity-to-deterioration-inference.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B3",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-03",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-03-high-activity-to-all-clear-inference.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B4",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-04",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-04-user-reported-record-to-injury-authority-elevation.json",
  "family": "F-ELEV",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B5",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-05",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-05-injury-absence-to-all-clear-inference.json",
  "family": "F-ABS",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "GYM-B6",
  "contract_registry_id": "W4-D4",
  "fixture_id": "FIX-GYM-06",
  "fixture_path": "fixtures/SYNTHETIC-fix-gym-06-sleep-observation-to-health-cause-inference.json",
  "family": "F-ELEV",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B1",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-01",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-01-practice-pattern-to-mental-or-behavioural-state-inference.json",
  "family": "F-PAT",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B2",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-02",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-02-reflection-content-to-manufactured-person-state.json",
  "family": "F-CM",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B3",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-03",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-03-meditation-derived-outward-signal-in-any-direction.json",
  "family": "F-ISO",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B4",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-04",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-04-absence-or-frequency-to-motivation-progress-or-wellbeing-verdict.json",
  "family": "F-ABS",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B5",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-05",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-05-library-or-text-choice-to-religion-belief-or-identity-inference.json",
  "family": "F-CM",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B6",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-06",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-06-practice-to-spiritual-attainment-or-moral-verdict.json",
  "family": "F-CM",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 },
 {
  "bait_label": "MED-B7",
  "contract_registry_id": "W4-D5",
  "fixture_id": "FIX-MED-07",
  "fixture_path": "fixtures/SYNTHETIC-fix-med-07-absent-edge-or-cross-room-context-reliance.json",
  "family": "F-ISO",
  "execution_status": "behaviourally_unexecuted",
  "superseded_by": null
 }
]
```

**The live mapping population comprises the twenty-three accepted rows, populated atomically with the Stage B fixture corpus — 23 rows landing with 23 fixtures and the corpus validator in one governed landing, with this document's registered hash refreshed in the same commit.** At this document's acceptance there were 23 declaration obligations, 0 fixture artefacts, 0 allocated `FIX` identifiers, and 0 mapping rows; the map was populated only when the Stage B corpus landed. An empty map was a truthful state for the authorised Stage A era, and a partially populated map outside a Stage B landing remains a defect.

## 15. Public-safety note

This document contains no private names, no private system references, no personal health details, no real personal data, and no project lineage beyond this repository. All example values are grammar placeholders; the placeholder register (`Persona-K9`, `Allergen-X`, `Medication-A17`, `Condition-Q`) is itself the rule. It contains no URLs. Fixtures governed here describe traps for prohibited system moves, never people.
