# 0037 — Corpus Execution Authorisation and Evaluation Records (W5-D4)

**Status:** Accepted by human reviewer, 2026-08-17.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D4**
**Position:** the governed execution-authorisation record the W5-D3 landing named — the record whose acceptance flips the corpus-execution interlock, defines what one execution event is under the deterministic instrument, assigns the evaluation-record home and retention that ADR-0034 decision 35 deliberately deferred here, and authorises the one `execution_status` transition ceremony ADR-0034 decisions 38–41 govern. It authorises exactly one execution event and opens no later deliverable.
**Constitutional references:** W0 Laws 1, 3, 6, 8, 9, 10, 11, 13; W0 §10; W0 Non-Goal 7. **No law is amended.**
**Resolves:** none. ADR-0024's open questions are answered in substance across ADR-0034 and this record, but no registered identifier is squarely closed here; the conservative `resolves` discipline holds.

---

**The instrument was built and proven unable to run. This record is the governed act that lets the run happen — once, bounded, deterministic, and honest about what a deterministic run can and cannot see. Twenty-three traps are sprung against walls with no model inside them. What that observes is the walls. What it does not observe — a model erring inside a lawful channel — stays honestly unknown, waiting behind its own gate.**

## Decision question

**How may W5-D4 execute the accepted twenty-three-fixture corpus and record evaluation observations — flipping the W5-D3 structural interlock by record, without a model, without touching fixture scenario content, without writing any result into any fixture file, and without letting any observation collapse into proof, safety, truth, or certification?**

## Controlling law

- **ADR-0034, whole** — the behavioural evaluation architecture: the harness boundary contract (A5), ground truth and calibration (B3), what a pass means and never means (B4), the evaluation artefact class and its never-become rules (B6), the closed two-value `execution_status` vocabulary and its transition governance (C1, decisions 38–41), and the W5-D4 ownership assignment (C4, decision 46). Decision 35 assigns evaluation-record home, retention and lifecycle to this landing in terms.
- **W5-AR §3** — W5-D4 executes; *"results never enter fixture files."*
- **W4-D6-BEF** — the fixture strategy whole: §7 (no result field, `result_location` fixed), §8 (paired variants, four surfaces), §12 rules 4 and 6 (transitions recorded in the map through ceremony; registered hash refreshed same commit).
- **ADR-0033** — no model contact is opened here: the local class remains doctrinally constructable only, the hosted class unopened, and model output is never ground truth. **ADR-0024 decision 13** — four-surface observability is a boundary property. **W1-D6 §3** — deterministic before generative; honest unknown rewarded; passing tests mint no authority.
- **The W5-D3 landing** — `CORPUS_EXECUTION_AUTHORISED = False` with its amendment named as a W5-D4-era governed act by record. This is that record.

## Decisions

### Part A — The execution authorisation

1. **Exactly one governed execution event is authorised: `W5-D4-RUN-01`**, over exactly the twenty-three accepted fixtures, under the deterministic in-process instrument defined in Part B. Nothing else is authorised: no second run (a re-run is a new governed event under ADR-0034 decision 41 and needs its own authorisation), no model contact, no fixture edit beyond decision 12, no pending-ledger conversion.

2. **The interlock flip is this record's act.** `CORPUS_EXECUTION_AUTHORISED` in the harness is amended `False` → `True` in the same landing as this record, with the amendment citing this record in place. The W5-D3 proofs that asserted the shut interlock and the unexecuted corpus are amended by record in the same landing to assert the new truths — the same amend-by-record pattern every fence in this repository follows.

3. **The instrument still never runs.** Execution machinery lives in a distinct runner module; the harness's own execution door keeps refusing in every era. Instrument and run remain structurally separate — the W5-D3 boundary is preserved, not consumed.

4. **Calibration is a precondition, not a formality.** The false-positive and false-negative guards run before any corpus work in the same process; an unfit instrument stops the run before the first fixture. This ordering is a structural proof obligation.

### Part B — What one deterministic execution is

5. **The instrument class is named honestly: a deterministic in-process runtime instrument.** No model is contacted; no network exists; the system under observation is the W5-D2 governed runtime driven through its composition root. A deterministic run observes the walls — the bounded system path of ADR-0034 decision 27 — under stated conditions. It does not and cannot observe model discretion inside a lawful channel; that observation belongs to a generative-era execution behind the ADR-0034 first-contact gate, which this record does not open.

6. **Silent-channel probes execute as paired variants, mechanically:** one composed governed operation per variant on the fixture room's processing edge, the bait bound as one additional granted section in the present variant and absent in the other, all other elements identical. The four observed surfaces are captured as content-free references — spoken output as the crossed payload's section references, persisted state as the write-destination event set, routing and propagation as the governed event sequence, and behaviour selection/ranking/framing/omission as outcome plus item ordering. The W5-D3 instrument computes the delta; **every observed delta routes to human review; the harness grades nothing.**

7. **Overt-channel probes are honestly unknown.** An overt probe addresses a question to a generative respondent; the deterministic instrument has none. Their recorded outcome is `unknown-not-absent` with its basis stated — never an absence claim, never a quiet skip, never a smuggled pass. Honest unknown is the governed answer here (W1-D6 §3.5; ADR-0034 decision 26), and the record structure preserves it.

8. **Uniform semantics, disclosed.** Every fixture executes under decisions 6–7 identically; fixture-specific generative scenario aspects beyond the structural path are not silently approximated — they surface as the honest unknowns of decision 7. No result is tidied, and an uncomfortable or weak observation is recorded as exactly that.

### Part C — Evaluation records: home, shape, retention

9. **The evaluation-record home is `governance/evaluation/`** — discharging ADR-0034 decision 35. Records are governed artefacts of the ADR-0034 B6 class: not C0, never inside fixture files, scanned exactly as documents are, synthetic-only throughout.

10. **One run manifest plus one record per fixture.** Each record carries: run and record identity, this record as its authorising record, the instrument-class statement of decision 5, `model_contact: none`, the per-probe observations of decisions 6–7 with the four-surface structure intact, the status-transition note, and a verbatim non-authority statement. Records are content-free: references and outcome classes only — no grant identifiers, no content bytes, no fixture scenario text.

11. **Retention is append-only and permanent.** A run identity that already exists refuses; later runs never overwrite, erase or amend earlier records (ADR-0034 decision 41). The manifest is written last, so an interrupted run is visibly incomplete — a manifest-less run directory is a detectable partial state, never a plausible-looking completion. **Outcome vocabulary in records is closed to the three W5-D3 classes** (`no-delta-observed`, `routed-to-review`, `unknown-not-absent`); the barred result vocabulary of ADR-0034 decision 39 is barred from record bytes entirely, and a structural proof enforces the absence — with one named mechanical exception: the runtime's own crossing event name `authority-checks-passed`, captured verbatim as a routing reference, is an event name from the W5-D2 transmission vocabulary and never an outcome claim.

### Part D — The status transition ceremony

12. **All twenty-three fixtures transition `behaviourally_unexecuted` → `behaviourally_executed` in this landing — the one authorised edit, in exactly one field per file.** The value is execution-state only and never a result (ADR-0034 decision 38); the transition is recorded in the W4-D6-BEF §14 map through ceremony (rule 4) with the map rows updated and a transition record stated in place; the strategy document's registered content hash is refreshed in the same commit (rule 6). Fixture scenario content, schema keys, provenance, the execution-dependency string and `result_location` are untouched, and structural proofs pin all of that.

13. **The W4 Lane B corpus validator is amended by record in this landing** — its single-value W4 assertion becomes the closed two-value W5 assertion with map↔file agreement and barred values refused. The W4-era statement it enforced was true in W4 and remains true as history; the validator now enforces the W5 truth.

### Part E — Non-authority, unchanged and total

14. **The anti-collapse chain binds every record, summary and sentence this landing produces:** executed ≠ passed · observed ≠ proven · a sprung trap ≠ a caught move · a deterministic no-delta ≠ behavioural proof · an honest unknown ≠ a gap to be filled by assumption · and no evaluation output is a safety claim, a health claim, a clinical claim, or a certification of any kind, anywhere, ever (W0 Non-Goal 7; ADR-0034 B4). `behaviourally_executed` means one thing: this governed run happened.

15. **The pending ledger is untouched.** No stub converts; the T12 condition amendment (ADR-0034 C2) is assigned to the first W5-era landing that touches the pending ledger through ceremony, and this landing does not touch it — the assignment stands, undischarged, visible.

16. **Nothing else opens.** No W5-D5, W5-D6 or W6; no model contact, no vendor, no hosted class, no E10 activation, no Z4 discharge, no E12/Z5 activation; no new boundary operation registers (the run composes the already-registered composed-operation-lifecycle with synthetic placeholders only, and evaluation records are governed artefacts created deliberately, not residue).

## Alternatives considered

- **Waiting for model access before any execution (rejected).** Deterministic before generative is the standing law (W1-D6 §3.2); the deterministic run is the era-one execution the runway names, and its honest unknowns document exactly what remains for the generative era rather than deferring the whole deliverable to it.
- **Marking overt probes as executed-with-no-delta (rejected firmly).** That would be an absence claim manufactured from an instrument's blindness — the precise dishonesty the unknown-not-absent class exists to prevent.
- **A result-bearing status or per-fixture pass marks (rejected, ruled already).** ADR-0034 decision 39 closed this; nothing here reopens it.
- **Deleting or regenerating records on re-run (rejected).** ADR-0034 decision 41: later executions never overwrite earlier evaluation records.
- **A new top-level directory for records (rejected).** `governance/` already holds governed live artefacts (the registry); a new top-level crossing needs its own fence authorisation and adds nothing.

## Consequences

- The corpus is executed and honestly recorded: the walls were observed while watched, deterministically; the model-era question remains open and is now precisely documented per probe as unknown-not-absent.
- The status vocabulary did its job: twenty-three transitions happened in ceremony, in one field, with the map and hash discipline intact — and not one status value says anything about a result.
- W5-D4 closes with evaluation records that can be examined, a runner that refuses its own repetition, and no sentence anywhere that converts observation into proof.

## Constitutional check

- **Law 1** — no person is contacted, notified or evaluated; the run is a governed, human-authorised act over synthetic data.
- **Law 3** — no authority is minted: records observe, route to review, and claim nothing.
- **Law 6** — the clinical line holds: no record contains or implies any clinical statement about any person.
- **Law 8 / Law 9** — inference paths and the Meditation wall are the subjects observed, never crossed: M2 fixtures execute under the Meditation edge's own stricter rules.
- **Law 10 / Law 11** — no real grant exists in evaluation and no person's access is conditioned by any result.
- **Law 13** — every execution, record and transition is a governed, auditable event; the records cannot become a behavioural dataset about a person (ADR-0034 B6, carried).
- **W0 §10** — no model output exists in this run at all; nothing is laundered into evidence.
- **W0 Non-Goal 7** — no regulatory, safety or certification claim arises from any of it.

## Non-goals

This record does not authorise, decide or design: model contact · a model binary · a vendor account · an SDK, client, API or credential · hosted access · E10 activation · Z4 discharge · E12/Z5 activation · a second execution run · pending-ledger edits or test conversion · fixture creation, deletion or scenario amendment · W5-D5, W5-D6 or W6 work · surface or copy wording · or medical, therapeutic, diagnostic or crisis behaviour of any kind. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording throughout — fixture, probe, run, record, instrument, surface, reviewer. No model or vendor is named and none is contacted. No real user data, no real room state, no real grants; every executed scenario is synthetic placeholder grammar validated at load. Evaluation records carry references and outcome classes only, are scanned as documents, and contain no scenario text, no names, and no claims about any person.

## Dependencies

`ADR-0034` (direct and required — the whole architecture this record executes under) · `W4-D6-BEF` (direct and required — §12 rules 4 and 6 and the §7 schema discipline are performed here) · `W5-AR` (direct — the D4 assignment and the results-never-in-fixtures rule) · `ADR-0033` (direct — the no-model-contact boundary held) · `ADR-0024` (direct — four-surface observability at the boundary) · `W1-D6` (direct — deterministic-before-generative and honest unknown) · `W2-D4` (direct — the synthetic discipline binding every artefact) · `ADR-0035` (direct — the residue framing of decision 16) · `ADR-0003` (direct — operative ceremony authority).

## Open boundaries and later ownership

1. **Generative-era execution** — a future governed act behind ADR-0034's first-contact gate and its Tier F crossings; the per-probe unknowns of this run are its precise work order.
2. **Any second run** — a new governed event with its own authorisation and identity, never an overwrite.
3. **The T12 pending-ledger amendment** — the first W5-era landing that touches the pending ledger through ceremony, unchanged.
4. **`execution_status` vocabulary extension** — its own future governed record, unchanged from ADR-0034.

---

*The traps were sprung and the walls held still — but the record says only that, and the difference between those two sentences is the whole discipline. Twenty-six questions wait for a respondent that does not yet exist here. When it does, they will be asked behind their own gate, and the answer will be written down whether or not it is comfortable.*
