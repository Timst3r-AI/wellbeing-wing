# W7-D4 Full-Development Brief: Synthetic Harness Binding, Exam Paper and Traps

**Status:** Accepted by human reviewer, 2026-08-22. **Effective on publication and remote verification**, at which point it authorises W7-D4 development under the full-development mode in section 3, and nothing beyond W7-D4. It is not itself an implementation, it authorises no landing of that implementation, and it discharges no precondition: **ADR-0047 precondition 7 is discharged only by the final published W7-D4 landing** (section 4).

**Date:** 2026-08-22  
**Revision:** v1.1 - pre-acceptance factual reconciliation after read-only source validation  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D4 - Synthetic Harness Binding: Exam Paper and Traps  
**Public baseline:** `e1dd86d561e458babdcfa56e6923aba9fb6f63b2`  
**Baseline subject:** `W7-D3: Select no-public-model-contact boundary`  
**Baseline registry:** 109 entries; ADR-0051 last  
**Model posture:** ADR-0051 Option D is effective. Public W7 will not contact a model.  
**Precondition posture entering D4:** p2 DISCHARGED; p3 OUTSTANDING; p6 DISCHARGED; p7 OUTSTANDING.  
**Public/private invariant:** **Any real-person adoption is a separate governed authority outside this repository.**

---

## 1. Purpose

W7-D4 builds and binds the synthetic evaluation instrument that W7-D5 may later execute. It turns the accepted W7-D2 record law and the accepted W7-D3 no-contact posture into a concrete, deterministic, reviewable harness over authored synthetic generated-text specimens.

The deliverable has one job: **prove that the Wing can govern the handling of generated-like text without contacting a model, without allowing the harness to become authority, and without materialising a generated-evaluation record before its remaining gates are satisfied.**

D4 is not a model test. It is not an evaluation run. It is not D5. It does not prove model quality, correctness, safety, behaviour, runtime reliability, provider behaviour, adapter reliability, or anything else that can only be learned by contacting a model.

The W7 north star remains controlling:

> Generated text may enter the public Wing only as synthetic, governed evaluation evidence. It may be observed, preserved, compared, routed, and reviewed. It may not become authority, advice, truth, safety evidence, approval, or a decision about any person.

---

## 2. Controlling authority

Eli must re-read the live published versions of the following before changing any file, and must work from their current bytes rather than from this brief's summaries:

1. `docs/phases/W7-runway-first-contact-governance-synthetic-evaluation.md`
2. `docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md`
3. `docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md`
4. `docs/decisions/0048-generated-evaluation-record-shape-doctrine.md`
5. `docs/decisions/0049-generated-evaluation-field-law.md`
6. `docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md`
7. `docs/phases/W7-D2-E-proof-completion-record.md`
8. `docs/decisions/0051-model-boundary-no-public-contact.md`
9. `docs/decisions/0034-behavioural-evaluation-architecture.md`
10. the W4-D6 fixture strategy and its live fixture corpus
11. `scripts/public-safety-scan.py`
12. `tests/test_repo_state.py`
13. `tests/test_w7_generated_evaluation_shape.py`
14. `tests/test_w7_model_boundary_decision.py`
15. the current registry and phase board.

Where this brief and a landed source differ, the landed source wins. Eli must report the discrepancy and stop if the difference changes scope, authority, schema, public/private law, Part Q, model-contact posture, or the D5 handoff.

---

## 3. Full-development operating mode

This deliverable deliberately does **not** use the Ari/Eli relay for each internal subpart.

Once this brief is accepted, landed and remotely verified, Eli may complete the whole D4 development cycle independently, including source grounding, design, fixture authoring, implementation, tests, negative controls, mutation work, scans and final packaging.

The operating rule is:

**one accepted architecture -> one independent development cycle -> one final review and acceptance ceremony.**

During development Eli does not need to return to Ari after every internal decision that is already settled by this brief. He may repair implementation defects, strengthen tests, reconcile counts to measured results, and make narrow design choices that stay inside the fixed boundaries below.

Eli may use disposable clones, temporary directories and scratch artefacts outside the repository. He may not publish, push, merge, allocate a GER identifier, create the generated-evaluation home, or open W7-D5 while developing D4.

The preferred working posture is an unstaged local working tree or disposable clone until the final review. Temporary development commits are permitted only in a disposable local branch or clone and must not be pushed or treated as governed publication.

The final D4 implementation must return to Tara and Ari as one review packet. **No final implementation commit or push is authorised by this brief alone.** Final publication requires explicit human approval after the end-of-development ceremony in section 24.

---

## 4. D4 completion condition

W7-D4 may be called complete only when all of the following are true together:

- the synthetic exam paper is fixed and source-traceable;
- the existing twenty-three trap fixtures are completely accounted for, with no silent omission;
- the twenty-six recorded generative-era unknowns are completely accounted for, with no invented twenty-seventh and no collapsed pair of questions unless the mapping is explicit;
- `pairing.variant_labels` is fixed;
- the authored-specimen contract is implemented;
- the harness exists and is mechanically bounded to Option D;
- the manifest artefact shape is fixed and its validator exists;
- the one-bit scan-environment representation exists;
- Part Q's current narrowing is explicitly accepted for W7 execution and the proposed execution is proven lawful under that narrowing;
- the `local-wordlist` seam has a complete pre-capture and capture-time posture;
- the D2-E proof succession is designed and negatively controlled;
- the working-state-outside-repository invariant is mechanically protected;
- every D4-owned mechanical obligation is live or honestly classified as later-owned debt;
- every review-only obligation is named as review-only;
- the full end-of-development validation is green;
- the final D4 landing is accepted, published and remotely verified.

**Only the final published D4 landing discharges ADR-0047 precondition 7.** The opening of D4, this brief's acceptance, local development, green tests, or a finished candidate do not discharge p7 by themselves.

---

## 5. Fixed no-contact architecture

ADR-0051 is not reopened.

D4 has no model adapter, no model runtime, no provider, no SDK, no client, no credential, no secret, no model binary and no model dependency. `requirements.txt` must remain unchanged.

Every D4 specimen is `authored_synthetic_specimen`. Every candidate generated-evaluation record produced in memory or in a disposable external workspace must therefore carry:

- `model_contact.occurred: false`
- `model_contact.contact_class: "none"`
- `model_contact.authorising_record: null`
- `text_class: "authored_synthetic_specimen"` for every capture
- a non-null specimen `authoring_record` that resolves to the accepted D4 authoring authority.

No D4 code path may accept `generated_output` as an input class. No hidden, manual, interactive or file-import route may bring model-produced text into the harness. A string's appearance is irrelevant; provenance controls the class.

If development reveals that any proposed D4 function needs actual model output, that is a **HARD STOP**. Do not substitute manual import, because ADR-0047 defines contact by the act, including contact performed by hand.

---

## 6. Part Q decision for W7-D4

### 6.1 Decision proposed by this brief

**W7-D4 ACCEPTS ADR-0050 Part Q's current narrowing for W7 execution. It does not amend or relax Part Q.**

The acceptance is deliberately narrow:

- a finding-bearing GER remains non-landable;
- no disposition value makes a finding-bearing GER landable;
- no generated-evaluation capture receives an allowlist exception;
- no test or harness code creates a new suppression route;
- an interesting failure may therefore cost W7 the ability to publish that GER;
- this limitation is accepted as the price of current law rather than hidden or routed around.

Part Q is therefore **accepted as a carryable limitation for W7**, not architecturally resolved for all future phases.

Tara's acceptance of this brief is acceptance of that D4 posture. If Tara does not accept this section, D4 does not open.

### 6.2 Lawful execution consequence

The D5 execution path designed by D4 is lawful under current Part Q only if:

1. capture-time scan produces no finding, in which case assembly may continue with `findings: []` and capture `scan_status: "no_findings"`; or
2. capture-time scan produces one or more findings, in which case **no GER is materialised or landed** and the run enters stop-and-report handling owned by W7-D5.

D4 may test the stop path using injected synthetic scanner results or disposable external state. It must not create a governed stop-report artefact, because ADR-0050 leaves that artefact's form to D5.

No D4 test should need to commit scan-sensitive payload text merely to prove the stop path. Prefer mutation or injected finding structures over planting a banned phrase in a tracked source file.

---

## 7. `local-wordlist` seam

D4 does **not** change the scanner's `local-wordlist` semantics and does **not** claim to solve the unresolved `character_start` production seam.

Instead it binds this complete posture:

- determine the effective filtered local-wordlist branch state from the scanner actually used;
- represent that state as exactly one public provenance bit: `active` or `inactive`;
- record no term count, no term, no hash, no fingerprint, no backing-file presence, no machine identity and no path;
- `inactive` means dormant for that run only;
- inactivity must never be manufactured by deleting, renaming, emptying, bypassing, ignoring or disabling an active list;
- `active` plus no finding may continue;
- `active` plus a finding requires stop-and-report, with no GER landing;
- a local-wordlist finding must never be assigned a fabricated `character_start`.

### 7.1 Run-state stability rule

Because the run manifest carries one scan-environment bit, **the effective branch state must remain stable across the run.** The harness must sample the branch at the governed start of a run and confirm the same state before each capture. If it changes, the run stops before a GER is materialised.

This rule prevents one manifest bit from pretending to describe captures made under different scanner states.

The harness must never expose the local wordlist's contents in errors, logs, test output, records, manifests or summaries.

---

## 8. Pairing vocabulary

W7-D4 closes its owned `pairing.variant_labels` vocabulary at exactly:

```json
["variant_a", "variant_b"]
```

The labels are deliberately neutral and meaning-free. They carry no winner, control, treatment, bait, expected answer, safer answer, preferred answer, temporal ordering or authority.

Every generated-evaluation unit has exactly two distinct labels and exactly two captures. The `captures` key set must equal the `pairing.variant_labels` set exactly.

A fixture or exam definition may map its scenario-specific present/absent or challenge/reference structure onto `variant_a` and `variant_b`, but the GER-facing labels remain the two neutral tokens above.

No `other`, `custom`, free-text label or extension point exists. A future change requires a new governed D4 amendment.

---

## 9. Exam-paper sources

D4's exam has two inherited source sets.

### 9.1 The twenty-six recorded unknowns

The twenty-six generative-era unknowns must be **source-derived from the current published corpus**, not reconstructed from memory and not copied from a conversational summary.

The canonical extraction has now been demonstrated read-only against the accepted W5-D4 evaluation records under `governance/evaluation/`: select probes whose `channel` is `overt`, whose `delta_finding.outcome` is `unknown-not-absent`, and whose `basis` is `generative_respondent_required_and_not_authorised`. That extraction yields **exactly 26** source unknowns across the 23 W5-D4 fixture records. Twenty fixtures contribute one overt unknown and three fixtures - `FIX-KITCH-05`, `FIX-MED-04` and `FIX-MED-07` - contribute two. The same corpus partitions cleanly as 26 overt / 25 silent and 26 `unknown-not-absent` / 25 `routed-to-review`.

Each D4 source row must retain a stable citation of the form `W5-D4-RUN-01/FIX-...` plus its `probe_id`. D4 must re-derive this extraction from the live published bytes before authoring specimens rather than trusting the count in this brief.

Before authoring a single D4 specimen, the following source gate must pass:

- exactly 26 source unknowns found by the governed extraction above;
- every row has a stable record citation plus `probe_id`;
- no duplicate source identity;
- no row silently merged with another;
- no wording strengthened into a claim the source did not make;
- no unknown marked resolved merely because D4 can construct a specimen around it.

If the live corpus no longer yields exactly twenty-six under that source-derived extraction, **STOP AND REPORT**. Do not invent, drop or merge to force the count.

### 9.2 The twenty-three existing synthetic trap fixtures

The existing trap corpus is already public and must be consumed as source, not rewritten in place. The current corpus contains:

**Gym, 6**

- `SYNTHETIC-fix-gym-01-training-pattern-to-mental-health-state-inference.json`
- `SYNTHETIC-fix-gym-02-reduced-activity-to-deterioration-inference.json`
- `SYNTHETIC-fix-gym-03-high-activity-to-all-clear-inference.json`
- `SYNTHETIC-fix-gym-04-user-reported-record-to-injury-authority-elevation.json`
- `SYNTHETIC-fix-gym-05-injury-absence-to-all-clear-inference.json`
- `SYNTHETIC-fix-gym-06-sleep-observation-to-health-cause-inference.json`

**Kitchen, 5**

- `SYNTHETIC-fix-kitch-01-food-choice-to-health-conclusion-inference.json`
- `SYNTHETIC-fix-kitch-02-allergy-absence-to-all-clear-inference.json`
- `SYNTHETIC-fix-kitch-03-meal-pattern-to-health-state-inference.json`
- `SYNTHETIC-fix-kitch-04-nutrition-information-to-treatment-reframing.json`
- `SYNTHETIC-fix-kitch-05-preference-to-medical-requirement-elevation.json`

**Meditation, 7**

- `SYNTHETIC-fix-med-01-practice-pattern-to-mental-or-behavioural-state-inference.json`
- `SYNTHETIC-fix-med-02-reflection-content-to-manufactured-person-state.json`
- `SYNTHETIC-fix-med-03-meditation-derived-outward-signal-in-any-direction.json`
- `SYNTHETIC-fix-med-04-absence-or-frequency-to-motivation-progress-or-wellbeing-verdict.json`
- `SYNTHETIC-fix-med-05-library-or-text-choice-to-religion-belief-or-identity-inference.json`
- `SYNTHETIC-fix-med-06-practice-to-spiritual-attainment-or-moral-verdict.json`
- `SYNTHETIC-fix-med-07-absent-edge-or-cross-room-context-reliance.json`

**Wellbeing, 5**

- `SYNTHETIC-fix-well-01-cross-entry-aggregation.json`
- `SYNTHETIC-fix-well-02-question-to-conclusion-drift.json`
- `SYNTHETIC-fix-well-03-research-to-person-inference.json`
- `SYNTHETIC-fix-well-04-supplement-to-health-inference.json`
- `SYNTHETIC-fix-well-05-absence-to-negative-inference.json`

**6 + 5 + 7 + 5 = 23.**

These files remain unchanged. D4 may cite, map and consume them. It may not add behavioural results to them, alter their historical execution state, convert a fixture into a result, or treat a green fixture validator as behavioural evidence.

### 9.3 Coverage, not artificial cardinality

D4 must account for all 26 unknowns and all 23 traps, but it must **not invent a fixed number of unique probes before source mapping**.

One well-formed paired probe may lawfully cover both a recorded unknown and a trap where the mapping is explicit and defensible. Conversely, one source item may require more than one probe if the source itself contains separable surfaces.

The exam therefore records:

- source coverage count: exactly 26 unknowns accounted for;
- trap coverage count: exactly 23 traps accounted for;
- unique probe count: derived from the completed mapping, never assumed;
- expected capture count: exactly `2 * unique_probe_count`.

No compression of the exam is permitted merely to produce a smaller number.

---

## 10. Authored synthetic specimen contract

Every D4 specimen must be written from nothing inside the public synthetic regime. It must not be a paraphrase of private material, a transformed real-person record, a copied model answer, a remembered transcript, or a reconstruction of lived content.

Every specimen must satisfy all of these:

- public-safe by construction;
- generic and synthetic;
- no identified person;
- no real health, device, movement, food, relationship, contemplative or journal data;
- no private model transcript;
- no credential, secret, private configuration or machine path;
- no claim that the specimen is representative of a model;
- no winner or preferred answer encoded in the specimen metadata;
- no recirculation from a GER, capture or finding;
- no model contact involved in its creation;
- traceable to the accepted D4 authoring authority;
- scan-clean before it becomes a committed fixture.

The specimen corpus must use the existing `fixtures/` home unless live repository precedent at implementation time establishes a narrower already-approved sub-home that does not require a new top-level fence crossing.

A proposed D4 fixture may carry authoring metadata, source references, pair mapping and the two specimen texts, but **it is not a GER** and must not mimic the full generated-evaluation record wrapper.

The fixture may state what governance property a probe is designed to exercise. It may not state that one variant is correct, passed, safe or better.

---

## 11. Exam fixture shape

Eli may refine field names during implementation, but the D4 exam artefact must encode the following semantics and no more:

- exam format version;
- D4 authoring authority;
- source coverage map for all 26 unknowns;
- trap coverage map for all 23 trap fixtures;
- ordered probe definitions;
- each probe's local `probe_id`, meaning-free outside the exam;
- exactly `variant_a` and `variant_b`;
- per-variant source inputs using only ADR-0046 lawful origins;
- per-variant authored synthetic specimen text or a reference to a D4-authored specimen object in the same governed fixture set;
- declared handling surfaces the probe is intended to exercise;
- claim-scope marker stating that the probe is **handling-only** and supplies no evidence about model behaviour;
- no result field;
- no pass/fail field;
- no machine verdict field;
- no GER identifier;
- no human disposition.

`probe_id` is local exam addressing, not a governed identifier namespace. It may not enter the registry or be cited as independent authority.

---

## 12. Harness architecture

The D4 harness is a deterministic, standard-library-only instrument. It must be reusable by D5 without D5 having to reinterpret D4's law.

The preferred architecture has seven separable responsibilities:

### 12.1 Source loader

Loads and validates the accepted D4 exam fixture. It refuses unknown versions, missing source coverage, duplicate source references, omitted traps, invalid pair labels and any result-bearing field.

### 12.2 Specimen admission validator

Proves the specimen's declared provenance shape is lawful for Option D and rejects any generated-output class, missing authoring authority, real-person-shaped field, unapproved origin or generated-evaluation recirculation reference.

### 12.3 Scan gateway

Uses the live public-safety scanner's actual logic rather than copying its pattern catalogue into a second authority.

The gateway must:

- scan capture text at capture time;
- use no allowlist for generated-evaluation capture payloads;
- derive the effective local-wordlist branch from the scanner actually used;
- reveal only categories and content-free control state needed for governance;
- never print or retain matched terms;
- return a clean/no-clean decision without treating it as a safety verdict.

If reuse of the scanner requires a narrow adapter around `scripts/public-safety-scan.py`, prefer import or invocation of the existing logic over copied regexes. A change to the scanner itself is not the default D4 design. Any proposed scanner edit must be justified as unavoidable, must preserve normal and landing mode byte-for-byte behaviour for existing cases, and must be called out separately in the final review packet.

### 12.4 Candidate record assembler

Builds the ADR-0049 record shape **in memory or in an external disposable workspace only**. It does not allocate a real `GER-####` identifier and does not write under `governance/generated-evaluation/`.

For D4 proof runs it uses neutral non-governed placeholder identities that cannot be mistaken for allocated GER identifiers.

It enforces the complete 46-position field law, canonical order, pair bijection, ceiling position, no-recirculation, Option D contact posture and nullability.

### 12.5 Delta and routing mechanics

The harness may mechanically state only what the accepted record law permits it to state mechanically: structural differences, declared differing surfaces, missing surfaces, routing facts and schema coherence.

It must not infer a semantic verdict from specimen prose. It must not classify one specimen as better, safer, correct or preferred. A judgment-bearing difference routes to human review and remains undispositioned until W7-D6.

### 12.6 Manifest candidate builder and validator

Builds and validates the future run-manifest shape in memory or a disposable external directory. It does not land a manifest in D4.

### 12.7 Materialisation fence

The D4 harness must contain no function that writes a GER or run manifest into the repository. If a reusable writer is needed later, D5 owns it.

A D4 call may return candidate bytes to its caller. The caller may place those bytes only in a disposable path outside the repository during D4 testing.

---

## 13. Future run-manifest shape

D4 fixes the manifest shape before any real run manifest exists.

The manifest is JSON, UTF-8, no BOM, LF, lower_snake_case keys, line-oriented indentation. It is an integrity index and run inventory only.

The proposed canonical shape is:

```json
{
  "generated_evaluation_run_manifest": {
    "run_id": "<D5-owned opaque run token>",
    "authorising_record": "<D5 run authority>",
    "as_of": "<run date>",
    "exam": {
      "reference": "<accepted D4 exam artefact>",
      "content_hash": "sha256:<exact exam bytes>"
    },
    "scan_environment": {
      "local_wordlist": "active"
    },
    "records": [
      {
        "record_id": "<future GER id>",
        "path": "<path under governance/generated-evaluation/>",
        "content_hash": "sha256:<exact record bytes>"
      }
    ]
  }
}
```

`scan_environment.local_wordlist` is the closed two-value set `active` / `inactive`.

The manifest may not contain:

- model name, provider, SDK or runtime information;
- local wordlist contents, count, hash, file presence, path or machine identity;
- capture text;
- finding text;
- finding count;
- pass count;
- fail count;
- a winner;
- a score;
- a ranking;
- a safety, correctness or readiness statement;
- a human disposition;
- a summary of the run.

The `records` array is non-empty in an actual D5 materialisation, contains every GER belonging to the run exactly once, contains no file from another run, and is ordered deterministically by the run's accepted exam order or another single D5-governed deterministic order fixed before first execution.

Each hash is over exact file bytes. No normalisation is performed for hashing.

One registry entry per run will later register the manifest, per ADR-0048. D4 does not mint the run identity syntax or create that registry entry.

---

## 14. Manifest proof binding

D4 must turn W7-D2-E S2's neutral set-and-hash predicate into a real manifest-aware validator without falsely claiming the debt is discharged before a real manifest exists.

D4's correct classification is:

- manifest **shape validation**: LIVE against the accepted D4 manifest contract and test fixtures;
- manifest **set-and-hash relation machinery**: LIVE as a predicate with negative controls;
- S2 over a real generated-evaluation home and real run manifest: READY / DEBT until D5 materialises the subject.

The validator must catch, at minimum:

- an unlisted GER file;
- a listed file that does not exist;
- missing content hash;
- hash mismatch;
- duplicate record listing;
- record from a different run;
- record path outside the reserved home;
- manifest self-listing as a GER;
- extra manifest field;
- forbidden summary or verdict field;
- invalid scan-environment vocabulary;
- exam hash mismatch.

---

## 15. D2-E proof succession

D4 designs the transition from the current vacancy proof to the future materialised-class proof. D5 performs that transition before the first real GER is allocated.

### 15.1 Current proof

Today S1 lawfully proves that `governance/generated-evaluation/` is absent. D4 must keep that proof green. D4 does not create the reserved home.

### 15.2 Successor invariant

Before the first D5 GER materialises, the vacancy proof's role must be succeeded by a proof that establishes at least:

- the home exists only because a D5 materialisation authority created it;
- every GER file in the home belongs to exactly one registered run manifest;
- every manifest-listed GER exists;
- every manifest hash matches exact bytes;
- no unlisted GER exists;
- no record is silently edited after landing;
- every actual record validates against ADR-0049 and ADR-0050;
- no finding-bearing GER lands under accepted Part Q;
- no generated-evaluation capture becomes a later input;
- no model contact is represented under Option D;
- the D4 exam reference and hash match the executed exam.

D4 must implement and negatively control the **successor predicate** now, against disposable fake homes outside the repository. D5 later binds it to the real home in the same governed act that ends vacancy.

The D4 record must say explicitly: **S1 reaching its lawful endpoint in D5 is state evolution, not a failed proof and not an erratum to W7-D2-E.**

---

## 16. Working-state boundary

The invariant remains literal:

> **UNLANDED AND UNDISPOSITIONED CAPTURE WORKING STATE MUST REMAIN OUTSIDE THE REPOSITORY.**

The harness must make this mechanical rather than advisory.

Required design:

- no default workspace inside the repository;
- caller-supplied or securely created temporary workspace must resolve outside the repository root;
- reject a workspace equal to or nested under the repository;
- reject a workspace under the reserved generated-evaluation home;
- no raw capture, candidate GER, finding-bearing candidate, temporary manifest or transient scan copy may be written under the repository;
- tests compare repository tracked and untracked state before and after a harness proof run and require no D4 runtime residue;
- cleanup failure is reported content-free and never causes fallback into the repository;
- no payload text is printed on error.

D4 tests may use `tempfile` outside the repository and may use in-memory bytes whenever practical.

---

## 17. Capture-time scan sequence

The harness sequence is fixed:

1. receive one D4-authored specimen as working-state text;
2. confirm run scan-environment bit still matches the run's opening state;
3. scan the capture using the live scanner logic with no generated-evaluation allowlist route;
4. if any finding exists, return stop-required state and do not assemble a GER candidate;
5. if no finding exists, mark the capture `scan_status: "no_findings"`;
6. assemble the candidate record in memory/external scratch;
7. run schema, pairing, no-recirculation, ceiling and manifest-candidate validations;
8. return candidate bytes to the caller without repository materialisation.

D4 does not perform pre-landing human finding review, because a finding path stops before a landable GER exists and the persisted stop-report form is D5's.

---

## 18. Handling of the twenty-three traps under Part Q

The traps are primarily semantic and structural traps, not an instruction to manufacture scanner findings.

For each trap, D4 must answer two separate questions in its coverage map:

1. **Can this trap be represented with public-safe authored specimen text that remains scan-clean?**
2. **What handling property does the pair exercise without making a claim about model behaviour?**

If yes, author the pair and include it in the executable D4 exam.

If a trap can only be represented by committing text that the active public scanner would bar, do not weaken the scanner, do not allowlist the specimen, and do not rewrite the trap into a different claim while pretending it is the same trap. Mark it **lawfully non-executable under current Part Q**, preserve its source mapping, and explain the narrowing.

That classification is not a failure of D4. The runway already says the twenty-three traps are included **where lawful**.

---

## 19. What D4 may prove

D4 may prove:

- exam-source completeness;
- fixture and specimen structural law;
- pair completeness;
- deterministic capture-count arithmetic;
- exact Option D contact posture;
- specimen provenance requirements;
- no-recirculation structural rules;
- capture-time scan gating;
- Part Q stop behaviour;
- scan-environment bit representation and stability;
- manifest shape and set/hash logic;
- D2-E proof-succession mechanics;
- working-state externality;
- canonical GER assembly against the existing field law;
- no machine winner or disposition;
- routing coherence;
- absence of a repository materialisation path in D4.

D4 may **not** prove:

- any model behaves well;
- any model resists inference;
- any model respects room boundaries;
- any model avoids authority laundering;
- any model is safe, correct or suitable;
- any provider or runtime is reliable;
- any trap has been behaviourally passed;
- any of the twenty-six unknowns has been answered about a real model.

The twenty-six unknowns become **exam questions about governed handling**, not model findings. W7-D7 must later preserve that distinction.

---

## 20. Review-only obligations

D4 must not mechanise semantic questions merely to obtain a larger green count.

At minimum the following remain human-review duties:

- **R5:** specimen evidence must never be generalised into model evidence;
- whether the twenty-six source unknowns were mapped fairly rather than rewritten into easier questions;
- whether each of the twenty-three traps retained its source meaning;
- whether a specimen quietly encodes a preferred answer, winner or expected conclusion;
- whether an allowed field is being used to smuggle verdict, recirculation or authority under a lawful name;
- whether authored specimen text was derived from private or model-produced material despite a structurally valid declaration;
- whether a non-executable trap was honestly classified rather than softened to become executable;
- whether Part Q's accepted narrowing is described candidly in the final record;
- whether any prose summary overclaims what D4 proves.

These duties do not become ownerless debt merely because they cannot be tests. They are review-only by nature.

---

## 21. Required mechanical proof families

The final D4 proof module should be source-derived wherever landed law states the expected value. It should not become a second copy of the doctrine.

The proof suite must cover at least these families:

### H1. Exam source completeness

Exactly twenty-six unknown source rows and twenty-three trap source rows accounted for; source identities unique; every declared mapping resolves.

### H2. Pair vocabulary and bijection

Exactly `variant_a` and `variant_b`; distinct; captures key set identical; no third label; no missing capture.

### H3. Option D provenance

Every capture is authored specimen; authoring authority non-null; model contact false/none/null; no generated-output route.

### H4. Synthetic-only construction

Fixture shape has no real-person intake field, no private source type, no free-form provenance escape, no GER source origin, and no path that accepts an existing generated-evaluation capture as input.

### H5. Scanner binding

Capture-time scan uses live scanner logic; no capture allowlist; branch bit source-derived; no term leakage; findings stop before candidate GER assembly.

### H6. Part Q

Clean capture can proceed; finding-bearing capture cannot produce a landable candidate; no disposition changes that; no suppression path is introduced.

### H7. Local-wordlist posture

Active/inactive only; no extra environment detail; state changes during run stop; no manufactured inactivity; no fake locus for local-wordlist finding.

### H8. Working-state fence

Every transient path outside repo; repo workspace rejected; reserved home rejected; no residue after proof run; content-free errors.

### H9. GER shape assembly

All ADR-0049 fields, order, nullability, ceiling and pair rules hold; `findings: []` for landable candidate; human review disposition remains null before D6.

### H10. Manifest shape

Closed shape; exact one-bit scan environment; exam ref/hash; record triplets; no summary/verdict fields.

### H11. Manifest relation

Unlisted, absent, missing-hash, mismatch, duplicate, wrong-run and out-of-home mutants all fail.

### H12. Proof succession

Vacancy still holds in live D4 repo; successor invariant runs and bites against disposable materialised homes; no claim that successor is yet live over a real home.

### H13. No D4 materialisation capability

No production code path writes under `governance/generated-evaluation/`; no `GER-####` allocation; no real run manifest; no D5 artefact.

### H14. Boundary contract

The module states what green does not mean, including no model contact, no model behaviour evidence, no Part Q resolution, no p3 discharge and no D5 opening.

---

## 22. Mutation and negative-control ceremony

Do not pick a mutation count in advance and then weaken or combine tests to preserve it. The final number is whatever the complete proof set requires.

At minimum plant independent controls for:

- one unknown source omitted;
- one trap omitted;
- duplicate source identity;
- variant label changed;
- third variant added;
- one capture missing;
- `model_contact.occurred` flipped true;
- `contact_class` changed from `none`;
- authored specimen missing authoring authority;
- specimen relabelled `generated_output`;
- recirculation reference into generated-evaluation class;
- synthetic marker weakened;
- scanner allowlist accidentally supplied;
- a finding allowed to continue to candidate GER;
- local-wordlist bit omitted;
- local-wordlist extra metadata added;
- branch state changed mid-run and ignored;
- repository path accepted as scratch workspace;
- generated-evaluation home accepted as scratch workspace;
- non-authority ceiling altered or displaced;
- human disposition pre-filled;
- manifest record unlisted;
- manifest record missing;
- hash mismatch;
- duplicate manifest record;
- record path outside reserved home;
- manifest summary/verdict key added;
- a `GER-####` identifier planted in D4 state;
- generated-evaluation home planted before D5.

Each mutant must be shown to make the relevant proof red. A control that merely proves the mutant string exists is not a mutation proof.

Report the actual mutation total in the final packet.

---

## 23. Expected D4 implementation artefacts

The exact final file set is determined at end-of-development diff review, but the intended shape is:

1. the published full-development brief that opens D4;
2. a final W7-D4 binding/completion record reporting the actual implementation and proof classifications;
3. one D4 synthetic exam/specimen fixture or a small, clearly justified fixture set under `fixtures/`;
4. one reusable deterministic harness module under `tests/`, following the established W5 precedent `tests/evaluation_harness.py`; preferred new path `tests/w7_synthetic_evaluation_harness.py`; no D4 harness code is added to `engine/` or `runtime/` absent a hard-stop review;
5. one D4 proof module under `tests/`;
6. registry updates required for governed D4 records and any governed fixture set that current registry law requires;
7. phase-board update;
8. only those README/test-index changes that existing repository convention actually requires.

The implementation should prefer a small number of coherent files over a file per probe. The 26/23 accountability belongs in structured rows, not forty-nine tiny documents.

### 23.1 Files that must not change without a hard-stop review

- `requirements.txt`
- `scripts/scan-allowlist.txt`
- the twenty-three existing `SYNTHETIC-fix-*` fixture files
- W7-D2 law records
- ADR-0051
- `tests/test_pending_ledger.py`
- `engine/` and `runtime/` for D4 harness code, unless a hard-stop review establishes a source-grounded necessity
- any private or external file
- any model/provider configuration.

A scanner change is not absolutely forbidden, but is outside the preferred design and requires a specific necessity finding in the final packet before acceptance.

---

## 24. End-of-development ceremony

Eli returns **one final packet** only after the complete development is ready.

The packet must contain:

### 24.1 Baseline and scope

- HEAD/local main/origin main/ls-remote baseline before work;
- ahead/behind and clean-tree state;
- exact changed paths;
- confirmation no unexpected file, cache, binary, `.pyc`, `__pycache__`, `.pytest_cache`, scratch output or generated-evaluation home exists.

### 24.2 Source inventory

- 26/26 unknown source extraction table;
- 23/23 trap table;
- unique probe count;
- capture-count formula and actual expected count;
- every non-executable trap, if any, with source-grounded reason.

### 24.3 Proof report

- D4 focused tests and subtests, actual numbers;
- existing W7-D2 and W7-D3 focused tests;
- repo-state tests;
- full deterministic suite;
- mutation ceremony, actual detected/total;
- no skipped new D4 test unless the brief explicitly classifies it as later-owned debt;
- proof-classification table: LIVE / READY-DEBT / REVIEW-ONLY.

### 24.4 Safety and boundary report

- landing-mode scan over every proposed path;
- normal scan over the proposed final tracked state;
- suppressions before and after, proving no new suppression unless separately authorised;
- synthetic-only audit;
- no real-person content;
- no credential/secret/config/binary;
- no model contact;
- no generated output;
- no GER allocation;
- generated-evaluation home absent;
- requirements unchanged;
- local wordlist never printed or persisted;
- working-state residue check.

### 24.5 D2-E succession report

- current S1 vacancy still green;
- successor predicate demonstrated against disposable materialised state;
- S2 real-manifest debt still honestly outstanding until D5;
- GER lifecycle/reuse seam still D5-owned;
- no obligation falsely discharged because its real subject does not exist.

### 24.6 Part Q report

- explicit statement that current narrowing is accepted for W7;
- proof that a finding-bearing capture cannot produce a landable GER candidate;
- proof no allowlist route was added;
- list of any trap narrowed by current law;
- statement that Part Q is accepted for W7 execution, not universally resolved.

### 24.7 Final proposed landing

- exact candidate hashes for every new/modified governed artefact;
- registry delta and dependency resolution;
- board patch;
- proposed single final D4 commit subject;
- statement of what publication would and would not change.

Only after Tara and Ari accept that packet may Eli stage, commit and push the final D4 implementation.

---

## 25. Publication effect of the final D4 landing

If the final D4 package is accepted, published and remotely verified, it may state:

- **W7-D4 COMPLETE AND SEALED**
- **ADR-0047 p7 DISCHARGED**
- p2 remains DISCHARGED
- p3 remains OUTSTANDING under the lawful no-contact posture
- p6 remains DISCHARGED
- Part Q narrowing is explicitly accepted for W7 execution, not universally resolved
- `local-wordlist` coordinate seam remains unresolved but lawfully bounded by stop-and-report
- D2-E successor machinery is ready; D5 must perform the transition before first GER
- no GER exists yet
- no generated-evaluation home exists yet
- no model was contacted
- no generated output exists
- W7-D5 remains unopened until its own accepted brief.

D4 completion **does not itself open D5**.

---

## 26. W7-D5 handoff contract

D5 receives a frozen harness and exam. It may execute them; it may not redesign them by momentum.

Before D5 allocates the first `GER-####`, D5 must separately settle and publish:

- GER lifecycle and identifier persistence;
- reuse semantics;
- first materialisation authority for `governance/generated-evaluation/`;
- the live proof transition from vacancy to materialised-class invariant;
- retention, archival and withdrawal-from-view;
- the stop-and-report artefact form;
- run identity and registry-entry mechanics;
- exact record/manifest materialisation order.

D5 then executes the accepted D4 harness only.

If a D5 capture scans clean, it may proceed toward a GER under the D2 schema. If it produces any finding, the GER does not land. If the local-wordlist branch is active and produces a finding without a lawful locus, stop-and-report is mandatory. If the branch state changes during the run, stop-and-report is mandatory.

D5 may not contact a model because ADR-0051 Option D continues to govern.

D5 may route a record to human review where the schema requires, but it may not write `human_review.disposition` before W7-D6 law exists.

---

## 27. Hard-stop conditions

Eli must stop development and return to Tara/Ari if any of the following becomes necessary or is discovered:

- baseline public head no longer matches the authorised starting authority and the intervening change touches D4 law or scope;
- the canonical unknown inventory cannot be derived as exactly 26;
- the trap corpus is not exactly the expected 23 under live source;
- any specimen would require real-person material;
- any proposed input derives from private material or a model transcript;
- any model contact is required;
- any new dependency is required;
- any credential, secret, provider configuration or binary is required;
- a new top-level directory is required;
- a new governed identifier namespace is required;
- the scanner must be weakened or an allowlist entry must be added to make the exam work;
- a finding-bearing GER would need to land;
- a local-wordlist finding would need a fabricated locus;
- a D4 test can pass only by creating the generated-evaluation home or a real GER identifier;
- the D4 harness cannot keep working state outside the repository;
- a requirement can be satisfied only by modifying W7-D2 law or ADR-0051;
- a semantic judgement is being presented as a mechanical proof;
- a test result is tempting to summarise as a model having passed, being safe, being correct, or being ready;
- a final implementation change falls outside the scope fixed by this brief.

A hard stop is not a failed deliverable. It is the correct outcome when the brief's authority is insufficient.

---

## 28. Non-goals

W7-D4 does not:

- contact a model;
- create generated output;
- build an adopter-facing model adapter;
- choose a provider;
- create a website or demo product;
- build an agent layer;
- create real-person adoption machinery;
- process real-person data;
- implement D5 record publication;
- allocate a GER identifier;
- create the generated-evaluation home;
- create human review dispositions;
- resolve GER lifecycle/reuse;
- resolve the `local-wordlist` coordinate seam;
- relax Part Q;
- convert pending-ledger stubs;
- repair unrelated W6 findings;
- make a clinical, safety, correctness, legal, conformance, certification, approval or production-readiness claim;
- open W8.

The later website/model-adapter/agent-layer work belongs to separate adoption/demo architecture. It is not pulled into W7-D4 merely because the eventual public demonstration will need it.

---

## 29. Acceptance criteria for this brief

Tara's acceptance of this full-development brief means she accepts all of the following D4 architecture choices together:

1. full-development mode instead of subpart relay;
2. Option D no-contact carried unchanged;
3. D4 may author and land public synthetic specimen fixtures;
4. Part Q's current narrowing is explicitly accepted for W7 execution, not relaxed;
5. `local-wordlist` remains an unresolved seam with the stated active/inactive stop posture;
6. run branch state must remain stable if one manifest bit represents the run;
7. `pairing.variant_labels` is exactly `variant_a` / `variant_b`;
8. the 26 unknowns are re-derived from the W5-D4 evaluation records through the demonstrated overt / `unknown-not-absent` / `generative_respondent_required_and_not_authorised` extraction, and all 23 existing traps are source-accounted;
9. the reusable D4 harness lives under `tests/` by W5 precedent, with preferred path `tests/w7_synthetic_evaluation_harness.py`; `engine/` and `runtime/` are not D4 harness homes absent a separately reported hard-stop necessity;
10. unique probe count is derived from mapping, not pre-decided;
11. expected captures equal two times the final probe count;
12. D4 builds the harness and manifest validator but creates no real GER, no run manifest and no generated-evaluation home;
13. D4 designs D2-E proof succession, D5 performs it;
14. no final D4 publication occurs until one end-of-development review packet is accepted;
15. D4 final publication discharges p7 only and opens no D5.

If accepted, this document should be landed as W7-D4's accepted full-development opening brief before Eli starts repository-resident implementation.

---

## 30. Instruction to Eli after acceptance

**Proceed independently through W7-D4 under this brief. Do not relay subparts back for approval. Re-ground every source from the published baseline, build the complete synthetic harness and exam, keep every transient capture outside the repository, preserve Option D, accept Part Q's current narrowing exactly as written here, add no model path and no dependency, create no GER and no generated-evaluation home, prove every mechanical obligation with negative controls, keep semantic duties review-only, run the complete final ceremony, and return one final development packet for Tara and Ari's review. Do not stage, commit or push the final D4 implementation until that final packet is explicitly accepted.**

---

*The point of W7-D4 is not to make synthetic prose look like a model. It is to make the governance unable to care where lawful evaluation prose came from once its provenance is honestly declared. D4 binds the instrument; D5 will later use it. If the instrument can stop cleanly, keep both halves whole, refuse findings under current law, preserve uncertainty and leave no residue in the repository before authority exists, then W7 has the harness it actually needs.*
