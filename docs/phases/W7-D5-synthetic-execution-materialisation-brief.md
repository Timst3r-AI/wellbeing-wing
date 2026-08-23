# W7-D5 - Synthetic Execution Records and First Materialisation: Full Architecture Brief

**Status:** Accepted by human reviewer, 2026-08-23. **Effective on publication and remote verification**, at which point it opens W7-D5 and governs the bounded D5 implementation cycle under the full-development mode in section 4, and nothing beyond W7-D5. It is not itself an implementation: it begins no run, allocates no `GER-####` identifier, and creates no generated-evaluation home, manifest or stop report. `W7-D5-RUN-01` begins only after Tara and Ari receive and accept the remotely verified Landing A publication state.

**Date prepared:** 2026-08-23  
**Revision:** v1.3 - v1.2 reconciled by the accepted manifest registry classification amendment `W7-D5-MRA`; v1.1 reconciled by the accepted proof-succession scope amendment `W7-D5-PSA`; the accepted architecture revision, incorporating the read-only eight-item / four-drift-check review  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D5 - Synthetic execution records and first generated-evaluation materialisation  
**Identity:** `W7-D5-SEB`, type `phase-brief`  
**Architect:** Ari  
**Builder/executor after acceptance:** Eli  
**Human authority:** Tara  
**Source baseline for this candidate:** `6cd6235d6d8af3fd9754bc66289564f89cc5dd0f` - `W7-D4: Bind the synthetic harness and exam paper`  
**Expected baseline registry state:** 112 entries, last `W7-D4-SHR`, to be re-verified before any landing  
**Proposed implementation permission after publication:** `w7-d5-synthetic-execution-materialisation`

---

## 1. The decision this brief makes

W7-D5 is the first deliverable permitted to turn the generated-evaluation class from an empty, governed shape into a materialised public repository class.

It does **not** contact a model. ADR-0051 Option D remains binding: public W7 does not contact a model. The D5 execution is therefore an execution of the accepted D4 synthetic harness over the accepted D4 authored-synthetic exam. The result is a governed run of authored synthetic specimen records, not evidence about model behaviour.

This brief fixes, before any first `GER-####` allocation:

1. the lifecycle and persistence semantics of `GER-####`;
2. identifier non-reuse;
3. the authority for the first creation of `governance/generated-evaluation/`;
4. run identity and run retry semantics;
5. the exact record and manifest materialisation order;
6. retention, archival and withdrawal-from-view posture;
7. the D2-E S1 proof succession and the post-materialisation invariant;
8. the real-subject binding of S2;
9. the stop-and-report artefact form;
10. the separation between run authority and specimen-authoring authority;
11. the final human P4b act required before publication;
12. the boundary between D5 acceptance and the later D6 human-review disposition.

This brief is intended to be the **separate published pre-materialisation governed act** required by the W7-D4 handoff. Once accepted and published, Eli may perform the bounded D5 implementation cycle described here without further design decisions. Any hard-stop condition still returns control to Tara and Ari.

The brief does not itself create the home, a GER, a run manifest, a stop report, a generated output, a model contact, a human-review disposition, or any new dependency.

---

## 2. Governing authority chain

The following are fixed inputs and are consumed rather than reopened.

### 2.1 W7 runway

`docs/phases/W7-runway-first-contact-governance-synthetic-evaluation.md`

The W7 north star remains: generated text may enter the public Wing only as synthetic, governed evaluation evidence, never as authority, advice, truth, safety evidence, approval, or a decision about any person.

The runway assigns W7-D5 the execution-record deliverable and reserves human review and disposition law to W7-D6.

### 2.2 ADR-0046, as amended by ADR-0052

`docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md`  
`docs/decisions/0052-exclusion-list-conformance-p4-decomposition.md`

Binding here:

- exactly three lawful input origins and no fourth;
- no recirculation;
- the eleven-family exclusion list remains wholly prohibited;
- the non-authority ceiling travels with the record;
- P4a is bounded mechanical surface-guard evidence only;
- P4b is complete exclusion-list conformance and is review-only in full;
- P4a green is no evidence for P4b.

### 2.3 ADR-0047

`docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md`

Current first-contact state after D4 publication:

- precondition 2: **DISCHARGED**;
- precondition 3: **OUTSTANDING**;
- precondition 6: **DISCHARGED**;
- precondition 7: **DISCHARGED**.

Precondition 3 remains outstanding because Option D performs no contact act. D5 does not waive, fail, satisfy, or reinterpret it.

### 2.4 ADR-0048

`docs/decisions/0048-generated-evaluation-record-shape-doctrine.md`

Binding here:

- home: `governance/generated-evaluation/`;
- JSON, UTF-8, LF, lower_snake_case, line-oriented diffs;
- one evaluation record per probe with both captures whole;
- one registered run manifest per run;
- one registry entry per run, never one per GER;
- manifest is an integrity index and run inventory only;
- captured text is immutable after landing;
- retention, archival and withdrawal-from-view are D5-owned.

### 2.5 ADR-0049

`docs/decisions/0049-generated-evaluation-field-law.md`

Binding here:

- wrapper `generated_evaluation_record`;
- exactly fifteen top-level fields in canonical order;
- exactly five capture fields in canonical order;
- `GER-####` record identity;
- `human_review.routed` is a creation-time fact;
- `human_review.disposition` and `human_review.disposition_record` are later human-act slots and remain null in D5;
- `generated_output` and `authored_synthetic_specimen` are provenance classes, never appearance classes;
- specimen captures require a non-null authoring record;
- `non_authority` remains the final field.

### 2.6 ADR-0050

`docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md`

Binding here:

- capture-time scanning precedes assembly and landing;
- no finding-bearing GER is landable under current W7 law;
- no D5 allowlist exception exists;
- `open`, `routed_for_public_safety_review`, and `withheld_from_publication` are finding-disposition values, and none is landable;
- finding disposition is distinct from W7-D6 human-review disposition;
- a capture is never edited, truncated, paraphrased, summarised or sanitised to make it landable;
- stop-and-report form belongs to D5;
- Part Q remains unresolved even though its current narrowing is accepted for W7 execution.

### 2.7 ADR-0051

`docs/decisions/0051-model-boundary-no-public-contact.md`

Binding here:

**PUBLIC W7 WILL NOT CONTACT A MODEL.**

No adapter, provider, SDK, client, credential, model binary, manual model import, generated output or dependency is introduced by D5.

### 2.8 W7-D2-E

`docs/phases/W7-D2-E-proof-completion-record.md`  
`tests/test_w7_generated_evaluation_shape.py`

D5 inherits nineteen proof obligations. Before real records existed they stood as:

- 5 LIVE: S1, T1, T2, T3, U1;
- 10 READY-DEBT: S2, T4, T5, T7, T8, T9, U2, U3, U4, U5;
- 4 REVIEW-ONLY: S3, S4, T6, U6.

D2-E explicitly found that S3 could become mechanically decidable if a later governed act fixed identity non-reuse together with deletion/lifecycle semantics. D5 owns those semantics and uses that opening rather than carrying avoidable review debt forward.

### 2.9 W7-D4

`docs/phases/W7-D4-synthetic-harness-binding-brief.md`  
`docs/phases/W7-D4-synthetic-harness-binding-record.md`  
`fixtures/SYNTHETIC-w7-d4-exam.json`  
`tests/w7_synthetic_evaluation_harness.py`  
`tests/test_w7_synthetic_harness.py`

D5 receives a frozen exam and harness. It may execute them. It may not redesign them by momentum.

---

## 3. D5 opens in two governed landings, not one blurred act

### Landing A - this architecture brief

Landing A settles the D5-owned lifecycle and materialisation law and opens D5 implementation under that law.

Expected scope:

1. new `docs/phases/W7-D5-synthetic-execution-materialisation-brief.md`;
2. modify `governance/registry.json` with one `W7-D5-SEB` entry;
3. modify `docs/phases/README.md` to record D5 as open for this brief only.

No home, GER, manifest, execution code, test change, specimen change or run occurs in Landing A.

**Proposed Landing A subject:**

`W7-D5: Govern first synthetic execution materialisation`

Landing A must be accepted by Tara, published by plain fast-forward, and remotely verified before D5 execution begins.

### Landing B - the D5 implementation and first successful run

Landing B may materialise the first public generated-evaluation run only after the entire external development and review cycle is green and Tara accepts the exact candidate bytes.

D5 is complete only after Landing B is published and remotely verified.

---

## 4. Full-development operating mode

D5 adopts D4's full-development model with a stricter payload boundary.

After Landing A is published:

- Ari's architecture is fixed by this brief;
- Eli may build the bounded D5 implementation end-to-end;
- no subpart requires routine relay approval;
- payload-bearing candidate work occurs in a disposable clone or workspace **outside the authoritative repository working tree**;
- Eli returns one reconciled final packet;
- Ari performs architecture and engineering review;
- Tara performs the required human P4b act over the exact final candidate;
- only after acceptance are the exact approved bytes transferred into the authoritative working tree for the landing ceremony.

Hard-stop conditions are exceptions to independent execution and return control immediately.

---

## 5. What D5 is, and what it is not

### D5 is

- the first lawful materialisation of the generated-evaluation home;
- one governed execution of the frozen D4 synthetic exam;
- one run manifest;
- one GER per D4 probe, if and only if the entire run is clean;
- proof succession from vacancy to materialised-class invariants;
- lifecycle and identity law for the GER class;
- an integrity and provenance exercise.

### D5 is not

- model execution;
- model contact;
- a behavioural test of any model;
- evidence that either variant is better;
- a pass/fail judgement on any trap;
- a safety claim;
- a clinical, legal, regulatory or production-readiness claim;
- W7-D6 human review;
- a Part Q resolution;
- a `local-wordlist` coordinate resolution;
- a private adoption step;
- an opening of W7-D6, W7-D7 or W8.

The runway's older phrase "synthetic model execution records" must be read through ADR-0051: under Option D, D5 executes synthetic specimen handling, not a model.

---

## 6. Frozen D4 input contract

Before any D5 run begins, Eli must re-read the published D4 bytes and prove the following three hashes against the current published baseline:

| Artefact | Required SHA-256 |
|---|---|
| `fixtures/SYNTHETIC-w7-d4-exam.json` | `9755cca1e8f9e41d7c89d532abb2f674a0189ec58935e3a5763fd641c90406a7` |
| `tests/w7_synthetic_evaluation_harness.py` | `e50172f5393a8753c9f4a93e29ef52e50cd366c0539a7c483787c085ea31f1fb` |
| `tests/test_w7_synthetic_harness.py` | `6da85d5b2b745e6156d7317f8859fde393489fee8b6df963310a9ebac747d860` |

**Hash basis is canonical repository bytes.** These three SHA-256 values are over the published Git bytes in their governed LF form. A platform checkout that presents a `.py` file with CRLF line endings must not hash those converted working-tree bytes and call the result drift. The verification must hash the canonical Git blob or an exact LF-normalised byte reconstruction of that blob. A mismatch **after** that canonicalisation is a hard stop.

The D4 exam must still resolve to:

- 26 probes;
- 23 source traps;
- 52 captures;
- exactly `variant_a` and `variant_b`;
- 52 distinct authored synthetic specimen texts;
- no result, verdict, winner, ranking or disposition field.

The exam and the harness are permanently byte-frozen at these hashes. The D4 proof-module hash is the D5 pre-succession baseline pin fixed by `W7-D5-PSA`: only H12 may receive the bounded successful-materialisation succession edit, and only in the successful Landing B candidate. Any other byte drift in these three D4 artefacts is a hard stop. D5 does not repair D4.

---

## 7. Run identity

The first authorised D5 execution attempt is:

`W7-D5-RUN-01`

### 7.1 Run-start boundary

Preflight is not the run.

The run begins only after all preflight checks are green, the scan-environment branch has been sampled, and the first probe begins specimen admission/capture handling.

A failure before that boundary may be corrected and preflight repeated without consuming a run identity because no capture act occurred.

Once the first capture begins, `W7-D5-RUN-01` is consumed as an execution-attempt identity whether the run ultimately succeeds or stops.

### 7.2 No silent retry

If `W7-D5-RUN-01` stops after run start, Eli must not silently rerun it.

A later attempt requires a new run identity, beginning with `W7-D5-RUN-02`, and a small separately accepted run-authority amendment stating why the first run stopped and authorising the next attempt. This is not a redesign of D5, but it is a new governed execution act.

The purpose is evidentiary honesty: a clean second attempt must never erase the fact that the first governed run stopped.

### 7.3 `as_of`

Every successful record and the manifest carry one identical `as_of` date: the **UTC calendar date on which the governed run begins**.

UTC is used deliberately because the run date needs a stable public temporal reference and does not need to publish a city-level location fact. No local timezone, city, machine locale or operator location is encoded in `as_of`.

No test or helper reads the current clock to manufacture this value. The governed run act supplies the UTC date once as run metadata and it is then held fixed.

---

## 8. Run cardinality and atomicity

The accepted exam fixes the successful run cardinality:

- 26 probes;
- 2 captures per probe;
- 52 captures total;
- 26 candidate records;
- 26 final GERs;
- 1 run manifest.

D5 is **run-atomic at publication**.

There is no lawful successful publication of 25 of 26 probes, a hand-selected subset, only reference variants, only bait-bearing variants, or only records whose deltas look convenient.

If any one probe cannot produce a lawful clean candidate, the successful-run publication path stops for the whole run. This prevents selective omission from becoming an invisible evaluation result.

---

## 9. Probe-to-record identity mapping

At the current baseline the `GER-####` namespace is empty. Subject to the live pre-publication namespace check in section 13, the first successful D5 run binds probe order to the first contiguous GER block:

| Probe | Expected final record |
|---|---|
| `D4-P01` | `GER-0001` |
| `D4-P02` | `GER-0002` |
| `D4-P03` | `GER-0003` |
| `D4-P04` | `GER-0004` |
| `D4-P05` | `GER-0005` |
| `D4-P06` | `GER-0006` |
| `D4-P07` | `GER-0007` |
| `D4-P08` | `GER-0008` |
| `D4-P09` | `GER-0009` |
| `D4-P10` | `GER-0010` |
| `D4-P11` | `GER-0011` |
| `D4-P12` | `GER-0012` |
| `D4-P13` | `GER-0013` |
| `D4-P14` | `GER-0014` |
| `D4-P15` | `GER-0015` |
| `D4-P16` | `GER-0016` |
| `D4-P17` | `GER-0017` |
| `D4-P18` | `GER-0018` |
| `D4-P19` | `GER-0019` |
| `D4-P20` | `GER-0020` |
| `D4-P21` | `GER-0021` |
| `D4-P22` | `GER-0022` |
| `D4-P23` | `GER-0023` |
| `D4-P24` | `GER-0024` |
| `D4-P25` | `GER-0025` |
| `D4-P26` | `GER-0026` |

The mapping carries identity only. The number does not encode room, trap family, quality, severity, rank, outcome or review status.

---

## 10. GER lifecycle and no-reuse law

D5 fixes the lifecycle semantics that ADR-0049 deliberately left unstated.

### 10.1 Stable identity

Once a `GER-####` identifier is published on the repository's authoritative history, it is permanently bound to that record identity.

### 10.2 Never reused

A published GER identifier is **never reused**, including after correction, supersession, future withdrawal-from-view, branch repair, revert or deletion from the current tree.

Git history, not the current directory listing alone, is the source for whether an identifier has ever been allocated.

### 10.3 Canonical path

A live GER's canonical path is:

`governance/generated-evaluation/<record_id>.json`

For example, `GER-0001` lives at `governance/generated-evaluation/GER-0001.json`.

D5 authorises no rename, relocation or alternate-path alias for a GER.

### 10.4 Allocation event

A GER identifier becomes **allocated** when the identifier first appears in a successfully published authoritative commit.

Before publication, a candidate package may carry a proposed GER binding so its exact final bytes can be reviewed and hashed, but that proposed binding has no repository authority and is not a published allocation.

This distinction is bounded by a pre-push namespace lock: immediately before staging and again immediately before push, the authoritative branch must still show the same empty or next-available namespace state used to build the candidate. If it does not, the candidate identities are invalidated and the landing stops.

### 10.5 No gaps manufactured for meaning

The first successful D5 run uses the next contiguous block of 26 available identifiers. At the current baseline that block is `GER-0001` through `GER-0026`.

A gap may exist only because a future governed publication history actually consumed an identifier. No gap is inserted to separate rooms, traps or perceived importance.

---

## 11. Retention, archival and withdrawal-from-view

ADR-0048 deliberately assigns this decision to D5. D5 resolves it as follows.

### 11.1 Retention

A published GER is retained in the active generated-evaluation home with no automatic expiry.

There is no time-based pruning, age threshold, count threshold or cleanup job.

### 11.2 Hard deletion

D5 authorises no hard-delete mechanism and no removal of a GER from current state.

### 11.3 Archival

D5 creates no separate archive tree, archive status, archived manifest or archive migration.

A future archival design requires its own governed authority and may not mutate captured text or recycle identifiers.

### 11.4 Withdrawal-from-view

D5 creates no withdrawal-from-view mechanism.

A future governed act may decide whether a public surface should stop presenting a GER, but it must preserve the original repository history and may not make an old identifier reusable.

### 11.5 Corrections

Captured text is never corrected in place. Any future correction, erratum or supersession must preserve original capture bytes and make the corrective act separately visible.

---

## 12. The D5 authority-split seam

The frozen D4 harness uses one `authorising_record` argument when it assembles a candidate. In that D4 context, the same authority could legitimately appear both as the candidate's run authority and as each authored specimen's `authoring_record`.

D5 has two different facts and must not collapse them:

- **run authority:** `W7-D5-SEB`;
- **specimen authoring authority:** `W7-D4-SHB`.

The exam itself declares `W7-D4-SHB` as its authoring authority. D5 did not write the 52 specimens and must not claim that it did.

### 12.1 No D4 harness edit

The D4 harness remains byte-frozen. D5 does not add a parameter to it and does not change its assembler.

### 12.2 D5 binding layer

D5 adds one small, pure, write-free binding module:

`tests/w7_generated_evaluation_binding.py`

It accepts an in-memory clean candidate produced by the frozen D4 harness and returns the final D5 record object/bytes after applying only the D5-owned bindings.

**Invocation is fixed, not left to implementation discretion:** D5 invokes the frozen D4 harness with `authorising_record = W7-D4-SHB`, so the harness-created candidate carries the true specimen-authoring authority into every capture. The D5 binder then changes **only the top-level run authority** to `W7-D5-SEB` while preserving every capture's `authoring_record = W7-D4-SHB`. The temporary in-memory top-level D4 value is never a published D5 claim; the binder is the governed step that separates the two facts before canonical D5 bytes exist.

The binding layer may:

1. bind the proposed `GER-####` `record_id`;
2. bind `run_id = W7-D5-RUN-01`;
3. bind the actual run `as_of` date;
4. set the **top-level** `authorising_record = W7-D5-SEB`;
5. preserve every capture's `authoring_record = W7-D4-SHB`;
6. serialise the canonical JSON bytes with UTF-8, no BOM, LF, repository indentation and final newline.

It may not:

- change either capture text;
- change a capture digest except by refusing a mismatch;
- change `text_class` or origin;
- change pairing labels;
- add a finding or remove one;
- write a human-review disposition;
- create a winner, rank, score, verdict or selected variant;
- write to the repository;
- contact anything;
- allocate identifiers by itself.

The module exposes no filesystem materialisation function. It is a pure authority-and-identity binder, not a writer.

---

## 13. Namespace preflight and publication lock

Before proposed GER identities are bound, D5 must inspect the authoritative published history and current tree.

It must prove:

1. the current published branch descends from the accepted D5 brief landing;
2. no `GER-####` exists in the current generated-evaluation home;
3. no `GER-####` has previously been published anywhere in the authoritative history;
4. no other D5 run manifest exists;
5. no generated-evaluation home artefact exists before the D5 creation candidate;
6. the authoritative branch has not moved unexpectedly since the execution baseline was taken.

At the expected baseline, the next block is therefore `GER-0001` through `GER-0026`.

The same namespace/history check is repeated immediately before staging and immediately before push. Any disagreement is a hard stop, not an auto-renumber-on-the-fly event.

---

## 14. Exact successful record contract

Each of the 26 final GERs must satisfy all of ADR-0049 plus the D5-specific bindings below.

### 14.1 Required run-level values

- `record_id`: the expected GER mapped from probe order;
- `run_id`: `W7-D5-RUN-01`;
- `authorising_record`: `W7-D5-SEB`;
- `as_of`: one shared actual run date;
- `model_contact.occurred`: `false`;
- `model_contact.contact_class`: `none`;
- `model_contact.authorising_record`: `null`;
- `pairing.variant_labels`: exactly `variant_a`, `variant_b`;
- `findings`: `[]`;
- `exclusion_check.checked`: `true`;
- `exclusion_check.result`: `no_listed_item_present`;
- `no_recirculation.capture_terminal`: `true`;
- `human_review.routed`: `true`;
- `human_review.disposition`: `null`;
- `human_review.disposition_record`: `null`;
- `non_authority`: exact governed ceiling, final field.

### 14.2 Required capture-level values

For both variants:

- `text_class = authored_synthetic_specimen`;
- `authoring_record = W7-D4-SHB`;
- `text` byte-equivalent as Unicode content to the exact corresponding D4 exam specimen;
- `text_digest` exactly hashes that text under ADR-0049;
- `scan_status = no_findings`.

### 14.3 No reinterpretation

D5 does not author a semantic finding from the prose. `delta` remains structural only and is carried as D4's harness derives it. No record says bait-bearing is worse, reference is better, or either side passed anything.

---

## 15. Home shape after a successful D5 publication

The first successful home contains exactly 27 files:

- `GER-0001.json` through `GER-0026.json`;
- `W7-D5-RUN-01-manifest.json`.

No README, scratch file, stop report, temporary capture, backup, cache, lock file, local wordlist artefact, review note or generated summary lives under this home.

The post-materialisation home is a closed governed class, not a scratch directory.

---

## 16. Run manifest

The D4-fixed manifest shape is consumed unchanged:

```text
generated_evaluation_run_manifest
  run_id
  authorising_record
  as_of
  exam            { reference, content_hash }
  scan_environment{ local_wordlist }
  records         [ { record_id, path, content_hash }, ... ]
```

### 16.1 Required D5 values

- `run_id = W7-D5-RUN-01`;
- `authorising_record = W7-D5-SEB`;
- `as_of` equals every GER's `as_of`;
- `exam.reference = SYNTHETIC-w7-d4-exam.json`;
- `exam.content_hash` equals the exact published D4 exam hash;
- `scan_environment.local_wordlist` is exactly `active` or `inactive`, sampled from the effective scanner branch used for this run;
- `records` contains exactly 26 entries in GER/probe order;
- every path is the canonical repository-relative GER path;
- every `content_hash` is the SHA-256 of the exact corresponding final record bytes.

### 16.2 Manifest non-authority

The manifest remains an integrity index only. It carries no:

- result;
- summary;
- conclusion;
- pass/fail count;
- finding count;
- winner;
- score;
- ranking;
- disposition;
- selected variant;
- capture text;
- model/provider/runtime metadata.

### 16.3 Hash direction

GER hashes flow into the manifest. The manifest's own hash flows into the governance registry. No record contains its own whole-file hash and no manifest self-hash is introduced.

---

## 17. Registry mechanics

ADR-0048 requires one registry entry per run and no per-GER registry entries.

A successful D5 final landing therefore adds exactly two registry entries:

### 17.1 `W7-D5-RUN-01`

A `governed-register` entry pointing to:

`governance/generated-evaluation/W7-D5-RUN-01-manifest.json`

The manifest is a JSON data artefact and cannot carry a prose acceptance header, so it is registered under the live `governed-register` type on the `W6-CAT` precedent (`W7-D5-MRA`): its human acceptance is recorded in its governing phase-record `W7-D5-SEC`, and `W7-D5-RUN-01.depends_on` names `W7-D5-SEC` as that governing record. `W7-D5-SEC.depends_on` does not name `W7-D5-RUN-01`, so the registry carries no circular authority dependency; the completion record still cites and verifies the manifest as evidence, because citation is not authority dependency.

It carries:

- accepted date of the D5 final landing;
- role limited to run-manifest integrity/index function;
- `implementation_permission: "none"`;
- no new identifier namespace;
- content hash of the exact manifest bytes.

It does not claim a model run, safety result or D6 disposition.

### 17.2 `W7-D5-SEC`

A `phase-record` entry pointing to:

`docs/phases/W7-D5-synthetic-execution-materialisation-record.md`

It records D5 completion, verification and open boundaries. It carries `implementation_permission: "none"` and does not open D6.

No `GER-####` receives a registry row.

### 17.3 Existing `GER-####` namespace declaration must advance with first allocation

The live ADR-0049 registry entry currently declares exactly:

`GER-#### (generated-evaluation records; grammar defined only — no identifier allocated)`

That sentence is true before D5 materialisation and becomes false the moment Landing B publishes `GER-0001` through `GER-0026`. The successful Landing B therefore updates **that one existing `id_namespaces` value in the ADR-0049 registry entry**, in the same already-counted `governance/registry.json` edit, to exactly:

`GER-#### (generated-evaluation records; allocation begun under W7-D5; lifecycle and no-reuse governed by W7-D5-SEB)`

This is a registry-state correction at the allocation event, not an amendment to ADR-0049 and not a new namespace minted by D5. ADR-0049 remains the authority that minted the grammar; `W7-D5-SEB` is the later authority for lifecycle and non-reuse. The `W7-D5-SEB` registry entry itself therefore declares **no new identifier namespace**.

The namespace wording must not change in Landing A, because at that point no identifier has been allocated and the existing wording remains true.

---

## 18. Capture-time execution sequence

D5 executes the frozen harness in the accepted order.

For each probe `D4-P01` through `D4-P26`:

1. load the exact published exam through the D4 loader and invoke the frozen D4 harness with `authorising_record = W7-D4-SHB`;
2. admit `variant_a` under its declared authored-synthetic provenance;
3. assert scan-environment branch stability;
4. capture-scan `variant_a` through the live scanner with no allowlist route;
5. delete temporary capture working state;
6. admit `variant_b`;
7. assert branch stability again;
8. capture-scan `variant_b`;
9. delete temporary capture working state;
10. only if both are clean, assemble the in-memory candidate through the frozen D4 harness;
11. retain the candidate only in the external D5 run workspace.

No repository home is created during this execution phase.

---

## 19. Scan-environment posture

The run records exactly one public environment fact:

`local_wordlist = active | inactive`

It is derived from the effective filtered list the live scanner actually uses.

D5 must never record or print:

- the local terms;
- term count;
- term hashes;
- fingerprints;
- backing-file path;
- backing-file presence as a separate field;
- username;
- hostname;
- machine path;
- any machine-identifying value.

An inactive branch means inactive for this run only. It does not mean the seam is solved.

D5 must not manufacture inactivity by disabling, emptying, renaming, bypassing or ignoring a wordlist.

If the branch changes between run start and any capture, the run stops.

---

## 20. Part Q and run-failure law

Part Q remains unresolved and its current W7 narrowing remains binding.

### 20.1 Any finding stops the successful run

If any capture returns any scan finding:

- no final GER for that probe is materialised;
- no later probe is used to complete a successful publication set;
- no run manifest is materialised;
- no generated-evaluation home is landed;
- no capture is edited to try again;
- no allowlist entry is added;
- the successful-run path ends.

### 20.2 Local-wordlist finding without lawful locus

If the active local-wordlist branch produces a finding for which current law cannot supply a lawful `character_start`, D5 must not fabricate one. The run stops and the stop report records that a lawful coordinate was unavailable under the carried seam.

This does not resolve the coordinate seam.

### 20.3 Finding disposition is not D6 disposition

A finding may require Tara's pre-landing public-safety judgement under ADR-0050. That act uses ADR-0050's finding-disposition vocabulary.

It is **not** `human_review.disposition` on a GER. D6 remains the only owner of that later field vocabulary.

---

## 21. Stop-and-report artefact form

If a governed run stops after run start, D5 owns one content-free report form:

`docs/phases/W7-D5-RUN-01-stop-report.md`

The report is outside `governance/generated-evaluation/` because it is not a GER and not a run manifest.

### 21.1 Finding-triggered report

After Tara performs the required ADR-0050 public-safety review, the report may contain only:

- `run_id`;
- proposed/candidate record identifier if one had already been bound, otherwise `not_allocated`;
- affected variant label;
- scan category, using the scanner's lawful public category name only;
- lawful `character_start` if one exists;
- otherwise the statement that no lawful locus was available under the current local-wordlist seam and no coordinate was fabricated;
- finding disposition, ordinarily `withheld_from_publication` for the terminal report;
- outcome: `record_not_landed`;
- outcome: `run_not_materialised`;
- confirmation that capture text was not retained in the repository.

It must never contain matched text, capture text, a fingerprint, excerpt, paraphrase, local term, local-term count, or enough derived detail to reconstruct the payload.

### 21.2 Branch-change report

If the run stops because the scanner branch changes, the report may state:

- run id;
- that the effective scan-environment branch changed during the run;
- that no GER and no manifest landed;
- that no capture payload was retained in the repository.

No wordlist content appears.

### 21.3 The stop report is itself subject to public law

The form does not guarantee that a stop report can be published. The report itself must pass the ordinary public-safety scan and every standing W7 boundary before it may land.

ADR-0050 requires the actual finding category among the content-free minimum facts. D5 must not rename, alias, encode or soften that category merely to make the report scan-clean. If the required category, the required locus fact, or any other mandatory minimum makes the stop report itself non-landable, the report remains outside the repository and D5 hard-stops for Tara/Ari review. No weakened report is substituted and no allowlist route is created.

This is an honest extension of Part Q's current cost: in the strictest case the evidence cannot land and the content-free report about why it could not land may itself be unable to land. D5 records that limitation rather than routing around it.

### 21.4 Publication effect and registry mechanics of a landable stop report

A stop-report landing does **not** complete D5. It closes that run attempt honestly and leaves D5 open.

If the stop report is itself lawful to publish, it receives the stable governed identity **`W7-D5-RUN-01-STOP`**, type `phase-record`, pointing to `docs/phases/W7-D5-RUN-01-stop-report.md`. Its registry entry carries the human-accepted date of that stop-report landing, `implementation_permission: "none"`, no identifier namespace, a content hash of the exact stop-report bytes, and a role limited to recording that the governed `W7-D5-RUN-01` attempt stopped without materialising a GER run. It depends at minimum on `W7-D5-SEB` and ADR-0050. It is **not** the run manifest entry and creates no GER allocation.

A landable `RUN-01` stop is therefore an **alternate three-path landing**, atomic as one governed act:

1. new `docs/phases/W7-D5-RUN-01-stop-report.md`;
2. modify `governance/registry.json` with exactly the `W7-D5-RUN-01-STOP` entry;
3. modify `docs/phases/README.md` to state that `RUN-01` was consumed and stopped, D5 remains open, and no `RUN-02` is authorised yet.

No successful-run manifest entry, completion entry, GER namespace allocation-state rewrite, generated-evaluation home, GER file or D5 completion claim enters that alternate landing. If section 21.3 makes the stop report itself non-landable, none of these three paths lands.

A second execution requires a separately authorised `RUN-02` act.

---

## 22. External development and candidate-state boundary

All payload-bearing development and first-run materialisation must occur outside the authoritative repository working tree until final acceptance.

Recommended implementation environment:

1. create a disposable clone of the published D5-brief baseline outside the authoritative checkout;
2. build the D5 binding module and tests in that clone;
3. execute the run with capture scratch under a separate external temporary workspace;
4. construct the 26 proposed GER files and manifest in the disposable clone only after all captures are clean;
5. construct the completion record, registry delta and board delta there;
6. run the complete proposed tracked-state verification there;
7. produce hashes of every proposed final path;
8. perform Ari review and Tara P4b review against those exact candidate bytes;
9. only after acceptance, transfer the exact approved bytes into the authoritative checkout;
10. prove the transferred bytes match the accepted hashes before staging.

The authoritative checkout remains clean during the payload-bearing development cycle.

No payload-bearing scratch file is ever committed merely to make testing convenient.

---

## 23. Exact materialisation order

For a successful run, the order is fixed.

### Stage 0 - published D5 authority

The D5 brief is already accepted, published and remotely verified.

### Stage 1 - preflight

Verify:

- authoritative baseline and clean state;
- frozen D4 hashes;
- 26/23/52 exam arithmetic;
- no existing generated-evaluation home;
- empty GER namespace in published history;
- no run manifest;
- current scanner and allowlist unchanged from the accepted boundary unless a separately governed change exists;
- current branch-state bit sampled honestly.

### Stage 2 - governed external run

Execute all 26 probes in order. Any stop condition aborts the successful-run path.

### Stage 3 - clean candidate set

Only after 52 clean captures exist in the external run:

- assert exactly 26 in-memory candidates;
- prove no finding event exists;
- prove no missing or duplicate probe;
- prove capture texts and digests match the accepted exam.

### Stage 4 - D5 final binding

Bind proposed GER identities and the D5/D4 split authorities through `w7_generated_evaluation_binding.py`.

No capture text changes.

### Stage 5 - record validation

Validate all 26 exact final GER byte candidates against ADR-0049, ADR-0050, Option D, the D4 exam and D5 lifecycle law.

### Stage 6 - manifest assembly

Hash the exact 26 record bytes. Build the single run manifest from those hashes. Validate the manifest against the exact candidate directory.

### Stage 7 - proof succession and full candidate tree

Apply the D2-E proof transition and new materialised-state proof module in the disposable clone. Add the completion record, registry delta and phase-board delta.

### Stage 8 - full verification and P4a

Run focused tests, negative controls/mutations, full deterministic suite, normal scan, landing scan, P4a mechanical guards and residue checks over the proposed final tracked tree.

### Stage 9 - Ari engineering review

Ari reviews the complete final packet and exact hashes. Engineering acceptance is not P4b.

### Stage 10 - Tara P4b

Tara reviews the exact final D5 candidate against all eleven exclusion families. P4b is landing-specific and must be an explicit human act.

### Stage 11 - transfer to authoritative checkout

Transfer only the accepted bytes. Hash-compare every transferred path to the accepted candidate.

### Stage 12 - pre-stage verification

Re-run the bounded authoritative-checkout verification and namespace lock.

### Stage 13 - stage and commit

Stage exactly the accepted final scope. No unrelated path.

### Stage 14 - push and remote verification

Plain fast-forward only. Then independently prove remote publication and clean sync.

---

## 24. D2-E proof succession

D5 must not delete D2-E history or pretend its vacancy proof failed.

### 24.1 S1 reaches its lawful endpoint

S1 says the reserved home remains vacant until a landing authorised to create it has occurred.

D5 Landing B is that authorised landing.

Therefore S1 becomes **ENDPOINT / HISTORICAL**, not failed and not erroneous.

The original D2-E record requires no erratum.

### 24.2 The three present-state assertions

The current D2-E module contains three assertions whose present-state form cannot remain after authorised materialisation:

- `test_s1_reserved_home_is_vacant`;
- `test_no_generated_evaluation_record_exists`;
- `test_absence_does_not_discharge_record_dependent_debts`.

D5 may modify `tests/test_w7_generated_evaluation_shape.py` only to perform explicit proof succession:

- preserve the historical obligation and its original meaning;
- assert from git history that the parent of the first authorised materialisation commit had no generated-evaluation home or GER;
- state that S1's protected interval ended lawfully;
- remove no other D2-E law or proof merely because D5 now has real subjects;
- replace absent-subject assertions with the new current-state obligation matrix.

This is proof succession, not an erratum and not deletion of history.

### 24.3 New post-materialisation invariant

D5 fixes the current-state invariant as:

> **After authorised materialisation, `governance/generated-evaluation/` contains only authorised GER records and their registered run manifest; every GER occupies its canonical identity path, belongs to its declared governed run, is listed exactly once by that run's manifest, matches the manifest hash, and carries no unlanded working-state artefact beside it. No stray, undeclared, moved, duplicated, recycled or scratch artefact may exist in the home.**

This is the successor to vacancy. It is not a reinterpretation of S1.

### 24.4 Adjacent present-state successions (W7-D5-PSA)

The accepted `W7-D5-PSA` amendment brings two further present-state vacancy assertions, outside the D2-E module, inside the succession design:

- **H12 in `tests/test_w7_synthetic_harness.py`**, pre-succession pin `6da85d5b2b745e6156d7317f8859fde393489fee8b6df963310a9ebac747d860`: the vacancy limb becomes a from-published-history proof - the reserved home had no tracked artefact at any commit up to and including the parent of the first authorised materialisation commit - and H12 retains its disposable-home successor checks unchanged. Current real-home conformance is owned by D5's materialised-state proof module, never by H12.
- **M6 in `tests/test_w7_model_boundary_decision.py`**, pre-succession pin `3748a16b219404fcd8d3686431adecc3713850aa3d2983f52d38a2970a45e722`: the home limbs become a from-published-history proof of the ADR-0051 landing-era condition - no home and no GER allocation existed at the ADR-0051 landing or at any commit up to and including the parent of the first authorised materialisation commit - rather than an assertion of current vacancy. M6's registry limb, that no registry entry id begins `GER-`, remains a current-state assertion and remains true after D5.

Neither succession edit occurs on a stopped `W7-D5-RUN-01`; both may enter only the successful Landing B candidate, each bounded to its named test with every other byte of its module identical to the pre-succession pin. No other D3 or D4 proof, decision, exam, harness, engineering or doctrine byte changes.

---

## 25. S2 becomes real

S2 is no longer a predicate biting on neutral placeholders after D5 materialisation.

The new materialised-state proof must bind the D4 manifest validator to the real home and prove against actual repository bytes:

- every GER is listed;
- every listed GER exists;
- no extra GER exists;
- no record is listed twice;
- every record content hash matches;
- every record's own `run_id` equals the manifest run;
- every path is inside the home and canonical;
- the manifest does not list itself as a GER;
- exam hash equals the executed exam;
- scan-environment block is exactly the one-bit closed shape.

On a successful D5 publication, S2 becomes **LIVE**, not merely READY-DEBT.

---

## 26. S3 lifecycle closure and candidate reclassification

D2-E kept S3 review-only for a precise reason: without no-reuse and deletion law, an ID-scoped history check could not distinguish an unlawful edit from a delete-and-reuse lifecycle.

D5 now fixes:

- published GER IDs never reused;
- no D5 deletion;
- canonical identity path fixed;
- no rename/relocation;
- captured text immutable;
- original history retained.

That removes the ambiguity D2-E identified.

### 26.1 Required S3 history proof

The D5 materialised-state module must implement an ID-scoped history proof that:

1. finds every published historical GER under the authoritative history;
2. indexes it by `record_id`, not path similarity;
3. records the capture texts and capture text digests from the identifier's first published version;
4. asserts that every later version carrying that ID preserves both capture texts byte-for-byte as decoded strings and preserves their `text_digest` values;
5. asserts the identifier never appears bound to a different capture pair;
6. asserts every current D5-era GER remains at its canonical path under the no-deletion/no-move rule;
7. permits only later fields that governance has separately authorised to change, such as the future D6 human-review fields.

### 26.2 Classification discipline

This brief makes S3 **candidate-mechanical under D5's new lifecycle law**. It is not called mechanical merely because the architecture now makes a proof possible.

D5 completion may reclassify S3 from REVIEW-ONLY to LIVE only after:

- the history proof has been run against real D5 subjects;
- a rename-plus-capture-edit mutant is detected;
- a delete-and-reuse mutant is detected;
- an allowed future-style review-metadata-only mutation is accepted without changing capture bytes;
- a duplicate-ID/different-capture mutant is detected.

If the proof cannot demonstrate those controls without interpretation, D5 stops for architecture review rather than silently keeping or changing the classification.

### 26.3 Target post-D5 nineteen-obligation matrix

If S3 demonstration succeeds, the honest target is:

| Status | Count | Obligations |
|---|---:|---|
| **ENDPOINT / HISTORICAL** | 1 | S1 |
| **LIVE** | 11 | S2, S3, T1, T2, T3, T4, T5, T7, T8, T9, U1 |
| **READY-DEBT** | 4 | U2, U3, U4, U5 |
| **REVIEW-ONLY** | 3 | S4, T6, U6 |

`1 + 11 + 4 + 3 = 19`.

U2-U5 remain debts because current Part Q law prevents a finding-bearing GER from becoming a landed real subject. Their rule machinery remains live and mutation-tested, but absence of a finding event is not used to claim their subject has existed.

---

## 27. W7-D6 boundary

Every D5 GER is intentionally born with:

```text
human_review.routed = true
human_review.disposition = null
human_review.disposition_record = null
```

D5 human acceptance means:

- the record is lawfully materialised;
- its provenance and integrity posture are accepted;
- its exclusion-list P4b review for publication is complete.

D5 acceptance does **not** mean:

- either variant is preferred;
- the delta was substantively judged;
- a trap was passed;
- a behavioural conclusion was reached;
- the GER received a W7-D6 disposition.

**Acceptance != disposition.**

Only a later accepted W7-D6 law may define `human_review.disposition` members or write those fields.

---

## 28. Future D6 hash consequence

ADR-0048 permits the later human-review fields to be written as a subsequent governed act. That changes whole-record bytes even though capture text stays frozen.

Therefore any future D6 landing that fills a GER's later review fields must, in the same atomic landing:

1. preserve both capture texts and their `text_digest` values;
2. update the affected GER whole-file hash in the run manifest;
3. update the manifest content hash in the governance registry;
4. keep S2 green before commit and after publication;
5. keep the S3 history proof green;
6. never reuse or renumber the GER.

D6 decides its disposition vocabulary and batching strategy. D5 decides only that integrity updates travel with any lawful later byte change.

---

## 29. P4a in D5

D5 must reuse the accepted ADR-0052 P4a guard architecture. It must not create a second semantic exclusion engine.

### 29.1 One governed guard inventory

The D5 proof module source-reads or imports the existing D4 governed eleven-row `GUARD_INVENTORY` and its detector/control declarations from `tests/test_w7_synthetic_harness.py` without copying the inventory into a second independently maintained declaration.

If direct import is technically awkward, use a read-only `importlib` load. Do not refactor or change the D4 proof module merely for convenience.

### 29.2 D5 P4a class scope

P4a is applied to the materialised generated-evaluation class artefacts:

- all 26 GER files;
- the one run manifest.

P4a must show:

- live eleven-family reconciliation still holds;
- eight guarded and three explicitly unguarded families remain the governed inventory state unless a later ADR has changed it;
- all positive controls still trigger;
- all clean controls still stay clean;
- no guarded surface is present in the D5 class artefacts;
- the five P4a non-claims remain intact.

A P4a green result makes no claim about P4b.

---

## 30. P4b in D5

P4b remains review-only in full across all eleven ADR-0046 Decision 11 families.

Before final D5 landing, Tara must review the **exact final candidate** against all eleven families and perform a named human act specific to that landing.

The review covers the complete proposed D5 landing, with particular attention to the 26 GERs and manifest.

Mechanical byte identity with the accepted D4 specimens is useful for locating what changed and what did not, but it does not replace human semantic judgement. P4a contributes no evidence of P4b conformance.

The D5 completion record may state P4b clear only after Tara has actually performed that review.

No stage, commit or push before that act.

---

## 31. Standing review-only duties

At final review, the following remain genuinely human questions unless later law has changed them:

### S4

Does the home still visibly signal its risk class, and has the manifest remained an integrity index rather than turning into a summary or scoreboard?

### T6

Has a lawful field name been used to perform a barred semantic function such as winner selection, verdict, hidden reuse or recirculation? Has captured text been copied, paraphrased, summarised or re-authored into a new input? Has provenance been laundered in practice?

### U6

If a finding occurred and a stop report is being considered, was the human public-safety disposition substantively sound?

A successful clean D5 run does not manufacture a U6 act. U6 remains review-only, and no finding means there was no U6 subject in the successful landing.

---

## 32. Proposed D5 materialised-state proof module

New file:

`tests/test_w7_generated_evaluation_materialised.py`

Recommended proof families:

1. **M1 - Frozen D4 source binding**  
   Required exam/harness/proof hashes, 26/23/52 arithmetic, exact pair labels.

2. **M2 - Home closed-set invariant**  
   Exactly 26 GERs plus exactly one run manifest, no other file.

3. **M3 - GER identity and path law**  
   Grammar, expected contiguous block, uniqueness, path equals ID, no duplicate or gap under the first-run plan.

4. **M4 - Canonical ADR-0049 record shape**  
   Reuse D2-E source-derived field expectations, canonical order and nullability.

5. **M5 - Option D and authority split**  
   Contact false/none/null, top-level D5 run authority, capture-level D4 specimen authority, authored-specimen class only.

6. **M6 - Exam-to-GER capture fidelity**  
   Every GER probe maps to the correct D4 exam probe, both variant texts match exactly, digests match, nothing compressed or reused.

7. **M7 - Run cardinality and atomic completeness**  
   26 unique probes, 52 captures, no missing/extra/duplicate pair.

8. **M8 - Real S2 manifest relation**  
   Set, hash, path, run membership, exam hash, closed manifest shapes and one-bit scan environment against real home bytes.

9. **M9 - Part Q and no-recirculation**  
   Every landed GER has empty findings, no allowlist entry under home, no input resolves to a GER/home, human-review disposition remains null.

10. **M10 - S3 lifecycle/history proof**  
    ID-scoped historical capture immutability, no deletion/reuse, no rename/path drift under D5 law.

11. **M11 - P4a class application**  
    Reuse governed D4 inventory; no duplicated guard law.

12. **M12 - Registry/run integrity**  
    Exactly one manifest registry entry of exact type `governed-register` with `implementation_permission: "none"`, its governing-record dependency on `W7-D5-SEC`, its canonical manifest path and a content hash matching the exact manifest bytes; no per-GER registry rows; completion record separately registered as `phase-record` (`W7-D5-SEC`).

13. **M13 - Boundary contract**  
    Green proves materialisation integrity only, not model contact, model behaviour, trap success, safety, correctness, D6 disposition, Part Q resolution, local-wordlist resolution, p3 discharge, D6 opening or W8 opening.

The proof-family count is architecture, not a target for artificial test-count padding. Test/subtest counts are reported from live execution.

---

## 33. Mutation and negative-control ceremony

Every hard mechanical invariant must be shown to bite at least once in a disposable clone or in-memory mutant. The mutation count is derived from coverage, not pre-selected as a trophy number.

At minimum the ceremony must include mutations for:

- one frozen D4 hash drift;
- omitted GER;
- extra GER;
- duplicate GER ID;
- wrong GER path;
- wrong probe-to-GER mapping;
- wrong `run_id`;
- wrong top-level D5 run authority;
- wrong capture-level D4 authoring authority;
- `model_contact.occurred = true`;
- capture text altered;
- capture digest altered;
- one missing variant;
- one extra variant;
- ceiling altered or followed by another field;
- non-null D6 disposition;
- non-empty findings on a landed GER;
- `findings_present` scan state on a landed GER;
- GER/home recirculation through `inputs`;
- manifest unlisted-present record;
- manifest listed-absent record;
- manifest hash mismatch;
- foreign-run record;
- duplicate manifest record entry;
- manifest self-listing;
- manifest forbidden summary-like extra key;
- manifest extra scan-environment key;
- invalid scan-environment value;
- path traversal/absolute/backslash/drive-root escape;
- allowlist entry under generated-evaluation home;
- later capture edit under same ID;
- rename plus capture edit;
- deletion plus same-ID reappearance with different capture;
- same ID bound to another capture pair;
- registry manifest hash mismatch;
- per-GER registry row planted;
- P4a guarded surface planted in a GER;
- a boundary claim that says D6 is open or p3 is discharged.

Scan-sensitive mutation/control strings must be assembled at run time or held only in disposable untracked state. A negative control must never plant a complete prohibited payload in a tracked source file merely to prove that a detector bites.

Every mutant is isolated and reverted. The unmutated candidate is proven green before and after the ceremony.

---

## 34. Hard-stop conditions

Eli stops and reports without improvising if any of the following occurs:

1. D5 brief is not yet published and remotely verified.
2. Authoritative baseline is not the expected descendant of the D5 brief landing.
3. Working tree is unexpectedly dirty at the final transfer stage.
4. Any frozen D4 hash differs.
5. Exam no longer derives 26 probes, 23 traps or 52 captures.
6. Pair vocabulary differs from `variant_a`/`variant_b`.
7. A model contact path, generated-output branch, provider, SDK, credential or binary appears.
8. A D4 harness or exam edit appears in the D5 implementation diff, or any D4 proof-module edit beyond the bounded H12 succession authorised by `W7-D5-PSA`.
9. The GER namespace is not empty when RUN-01 expects the first block.
10. Any GER ID exists in authoritative history unexpectedly.
11. Any capture scan finds anything.
12. Scan-environment branch changes during the run.
13. A local-wordlist finding lacks a lawful locus.
14. Any probe returns something other than a clean candidate.
15. Candidate count is not exactly 26.
16. Any specimen text or digest differs from its D4 exam source.
17. D5 binding cannot separate run authority from specimen authoring authority without changing D4.
18. Any final GER has a non-empty findings array.
19. Any final GER has a non-null D6 disposition.
20. S2 fails against the real candidate home.
21. The S3 target proof cannot demonstrate its required negative controls.
22. Any generated-evaluation allowlist entry is proposed.
23. P4a is red.
24. Tara raises any P4b concern.
25. Normal scan introduces a new unsuppressed finding.
26. Suppression count increases without a separately governed reason.
27. Any payload-bearing working state appears in the authoritative checkout before final acceptance.
28. Any unrelated file enters the proposed landing.
29. Registry or board wording claims model evidence, safety, a winner, D6 disposition, Part Q resolution, p3 discharge or D6 opening.
30. Authoritative branch moves between final candidate lock and push.
31. A required stop-report minimum cannot itself be represented as a landable public artefact without alteration.

A hard stop does not authorise a repair outside this brief's scope.

---

## 35. Successful final landing scope

Assuming the live source inspection reveals no new hard dependency, the successful D5 implementation landing is exactly **35 paths**:

### 35.1 Generated-evaluation home: 27 new files

1. `governance/generated-evaluation/GER-0001.json`
2. `governance/generated-evaluation/GER-0002.json`
3. `governance/generated-evaluation/GER-0003.json`
4. `governance/generated-evaluation/GER-0004.json`
5. `governance/generated-evaluation/GER-0005.json`
6. `governance/generated-evaluation/GER-0006.json`
7. `governance/generated-evaluation/GER-0007.json`
8. `governance/generated-evaluation/GER-0008.json`
9. `governance/generated-evaluation/GER-0009.json`
10. `governance/generated-evaluation/GER-0010.json`
11. `governance/generated-evaluation/GER-0011.json`
12. `governance/generated-evaluation/GER-0012.json`
13. `governance/generated-evaluation/GER-0013.json`
14. `governance/generated-evaluation/GER-0014.json`
15. `governance/generated-evaluation/GER-0015.json`
16. `governance/generated-evaluation/GER-0016.json`
17. `governance/generated-evaluation/GER-0017.json`
18. `governance/generated-evaluation/GER-0018.json`
19. `governance/generated-evaluation/GER-0019.json`
20. `governance/generated-evaluation/GER-0020.json`
21. `governance/generated-evaluation/GER-0021.json`
22. `governance/generated-evaluation/GER-0022.json`
23. `governance/generated-evaluation/GER-0023.json`
24. `governance/generated-evaluation/GER-0024.json`
25. `governance/generated-evaluation/GER-0025.json`
26. `governance/generated-evaluation/GER-0026.json`
27. `governance/generated-evaluation/W7-D5-RUN-01-manifest.json`

### 35.2 D5 implementation/proof: 5 paths

28. new `tests/w7_generated_evaluation_binding.py`
29. modify `tests/test_w7_generated_evaluation_shape.py` for explicit proof succession
30. new `tests/test_w7_generated_evaluation_materialised.py`
31. modify `tests/test_w7_synthetic_harness.py` - the bounded H12 succession edit only (`W7-D5-PSA`)
32. modify `tests/test_w7_model_boundary_decision.py` - the bounded M6 succession edit only (`W7-D5-PSA`)

### 35.3 Governance/reporting: 3 paths

33. new `docs/phases/W7-D5-synthetic-execution-materialisation-record.md`
34. modify `governance/registry.json`
35. modify `docs/phases/README.md`

No other path is part of the successful landing.

Specifically excluded unless a new governed act says otherwise:

- D4 exam;
- D4 harness;
- D4 proof module, beyond the bounded H12 succession edit;
- ADR-0046 through ADR-0052;
- `scripts/public-safety-scan.py`;
- `scripts/scan-allowlist.txt`;
- `requirements.txt`;
- `tests/test_pending_ledger.py`;
- all 23 trap fixtures;
- `engine/`;
- `runtime/`.

---

## 36. Final completion record requirements

`docs/phases/W7-D5-synthetic-execution-materialisation-record.md` must report, without overclaiming:

### 36.1 Authority and baseline

- D5 brief commit and hash;
- D4 source commit and frozen hashes;
- exact UTC execution date used as `as_of`;
- exact run identity.

### 36.2 Run accounting

- 26/26 probes;
- 52/52 captures;
- 26 GERs;
- no missing, extra or duplicate probe;
- no finding-bearing capture;
- one stable scan-environment bit for the whole run.

### 36.3 Provenance

- all captures are authored synthetic specimens;
- no generated output;
- no model contact;
- top-level D5 run authority separated from D4 specimen-authoring authority.

### 36.4 Identity/lifecycle

- first GER block used;
- no previous GER in history;
- no-reuse law now fixed;
- no deletion, archive or withdrawal mechanism created;
- retention is no automatic expiry.

### 36.5 Manifest/S2

- exact manifest path and hash;
- 26 listed GER hashes all match;
- no stray or unlisted home artefact;
- S2 now live against real subjects.

### 36.6 Proof succession

- S1 reached lawful endpoint;
- D2-E not erroneous and no erratum needed;
- post-materialisation invariant exact;
- S3 result and whether candidate-mechanical reclassification was successfully demonstrated;
- nineteen-obligation matrix after D5.

### 36.7 Part Q/local-wordlist

- Part Q still unresolved;
- no finding occurred, if successful;
- no allowlist change;
- local-wordlist seam still unresolved even if branch was inactive;
- inactivity was not manufactured.

### 36.8 Human boundaries

- P4a result with all non-claims;
- Tara's exact P4b act and date;
- S4 and T6 review dispositions;
- `human_review.disposition` remains null in every GER;
- D5 acceptance is not D6 disposition.

### 36.9 Verification

- focused proof results;
- mutation results derived from actual executed matrix;
- landing scan;
- normal scan and suppression before/after;
- full deterministic suite;
- pending ledger unchanged;
- authoritative remote verification after publication.

### 36.10 What completion does not establish

- no model behaviour claim;
- no trap behavioural pass;
- no safety/correctness/clinical/legal/production claim;
- no Part Q resolution;
- no local-wordlist seam resolution;
- no p3 discharge;
- no D6 opening;
- no W8 opening.

---

## 37. Verification ceremony before Tara's final acceptance

Eli's final packet must include measured results for all of the following against the exact proposed tracked state in the disposable clone:

1. frozen D4 hash check;
2. D4 focused proof module, complete and green after its authorised H12 succession edit;
3. D2-E shape proof after succession edit;
4. D5 materialised-state proof module;
5. D3 model-boundary proof, complete and green after its authorised M6 succession edit;
6. first-contact doctrine proof;
7. boundary invariant proof;
8. repo-state proof;
9. pending-ledger proof, with no row touched;
10. P4a guard application;
11. mutation/negative-control ceremony;
12. landing-mode scan over **all 35 proposed paths**;
13. normal scan across the complete proposed tracked state;
14. suppression count comparison;
15. full deterministic suite;
16. generated-evaluation home closed-set listing;
17. registry consistency and content hashes;
18. no model/dependency/credential/binary/provider path;
19. no generated output;
20. no payload residue outside the accepted final files in the disposable candidate clone.

Measured numbers are reported from execution. The brief does not pre-invent a passing test count.

---

## 38. Tara's final D5 human acts

Two distinct human acts must not be collapsed.

### 38.1 P4b publication review

Tara reviews all eleven ADR-0046 exclusion families against the exact 35-path final candidate and records CLEAR or concern family by family.

This is the publication-conformance act.

### 38.2 D5 packet acceptance

After P4b is clear and Ari has accepted the engineering, Tara explicitly accepts the exact D5 final packet and authorises its landing.

This is the implementation-landing act.

Neither act writes a W7-D6 `human_review.disposition` into a GER.

---

## 39. Final authoritative landing ceremony

Only after section 38 is complete:

1. verify authoritative checkout still clean at the D5 brief baseline;
2. verify remote main has not moved unexpectedly;
3. re-run GER namespace/history lock;
4. transfer the exact 35 accepted candidate files/edits into the authoritative checkout;
5. compare every resulting path hash to the accepted packet;
6. prove no extra untracked or modified path exists;
7. run focused D5 proofs;
8. run landing-mode scan over exactly the 35 paths;
9. run normal scan and suppression comparison;
10. run repo-state and pending-ledger checks;
11. run full deterministic suite;
12. stage exactly the 35 paths;
13. show staged path list and nothing unstaged/untracked;
14. commit once;
15. push by plain fast-forward only;
16. verify HEAD = local `main` = `origin/main` = independent `ls-remote`;
17. verify ahead/behind 0/0;
18. verify working tree clean;
19. read back the published 27 home artefacts and governance files from the remote ref and recompute hashes;
20. report the publication packet and stop.

**Proposed final Landing B subject:**

`W7-D5: Materialise the first synthetic evaluation run`

No amend, force push, rebase, squash or merge as part of the ceremony.

---

## 40. Publication effect of successful D5 completion

Only after final Landing B is published and remotely verified may the repository state say:

- **W7-D5 COMPLETE AND SEALED**;
- first generated-evaluation home materialised lawfully;
- `W7-D5-RUN-01` published as the first synthetic specimen run;
- 26 GERs exist and are integrity-bound by one registered manifest;
- GER lifecycle and no-reuse law are fixed;
- S1 reached its lawful endpoint;
- S2 is live and green against real subjects;
- S3 may be reclassified LIVE only if the required D5 history proof was demonstrated as specified;
- Part Q remains unresolved and unchanged;
- the `local-wordlist` coordinate seam remains unresolved and unchanged;
- ADR-0047 precondition 3 remains outstanding;
- no model was contacted;
- no generated output exists;
- every GER remains routed to later human review with null D6 disposition;
- W7-D6 remains unopened.

D5 completion does not itself open D6.

---

## 41. D6 handoff contract

D6 receives:

- 26 immutable capture pairs;
- one run manifest whose current hashes describe the D5 bytes;
- 26 records with `human_review.routed = true` and both later disposition fields null;
- a live S2 relation;
- an S3 lifecycle/history proof if D5 successfully reclassifies it;
- no model claim and no machine winner.

Before D6 writes any `human_review.disposition`, D6 must separately settle and publish:

- the closed disposition vocabulary;
- what each value means and does not mean;
- whether a disposition may later change;
- the human review procedure over deltas;
- the integrity update ceremony for modified record hashes and manifest/registry hashes;
- any later comparison/reporting surface.

D6 may not edit captured text and may not reinterpret D5 acceptance as a pre-existing disposition.

---

## 42. Open boundaries carried beyond D5

Successful D5 deliberately leaves these unresolved:

1. ADR-0047 precondition 3;
2. Part Q's publication seam;
3. the `local-wordlist` coordinate-production seam;
4. W7-D6 human-review vocabulary and change semantics;
5. any later evaluation summary or comparison surface;
6. any private adoption;
7. any real-person evaluation;
8. any model contact;
9. W8.

No unresolved boundary becomes resolved by repeated clean runs or by elapsed time.

---

## 43. Constitutional and public/private boundary check

D5 remains entirely public-safe and synthetic-only.

It introduces no:

- real-person data;
- identified person's wellbeing material;
- real wearable or device data;
- private relationship or lived-interaction material;
- private model transcript;
- credential, secret or private configuration;
- machine-identifying detail beyond allowed OS-class posture;
- model binary;
- real-person evaluation channel;
- private adoption implementation detail;
- public live personal instrument.

**Any real-person adoption is a separate governed authority outside this repository.**

The generated-evaluation home is evidence storage for synthetic governance evaluation only. It is not a health record store, Memory, Profile, personal journal, device history, room history or live user instrument.

---

## 44. Architecture acceptance criteria for this brief

Before Landing A, Tara and Ari should be satisfied that this brief answers, without leaving an implementation-time choice:

- what starts and consumes a run identity;
- whether a failed run can be silently repeated;
- how GER IDs are allocated and whether they can ever be reused;
- where each GER lives;
- how long it remains;
- whether it can be archived, deleted or withdrawn under D5;
- which record authorises the run;
- which record authored the specimens;
- exactly which authority value is passed into the frozen D4 harness before the binder separates the top-level run authority;
- how the frozen D4 harness is used without falsely collapsing those authorities;
- how S1 ends;
- what replaces vacancy;
- how S2 binds to real bytes;
- how S3 can now become mechanically decidable;
- exactly what happens on any finding;
- what a stop report contains and never contains;
- how a landable stop report is identified, registered and board-recorded;
- how the live ADR-0049 `GER-####` registry declaration changes when first allocation actually occurs;
- what public date basis is used without publishing an unnecessary location fact;
- how local-wordlist uncertainty is handled;
- what D5 may publish;
- what D5 acceptance means;
- what remains exclusively D6's;
- exact expected successful landing scope;
- exact final publication ceremony.

If any of those remains materially open, the brief is not ready to land.

---

## 45. Instruction to Eli after this brief is accepted and published

After Tara accepts this brief and its Landing A is remotely verified, the implementation instruction is:

> Implement W7-D5 exactly under `W7-D5-SEB` in full-development mode. Re-ground on the published brief baseline; freeze the accepted D4 exam and harness bytes permanently, hold the D4 proof and D3 model-boundary proof modules at their `W7-D5-PSA` pre-succession pins, and apply only the bounded H12 and M6 succession edits, in the successful Landing B candidate alone. Work payload-bearing candidate state only in a disposable external clone/workspace. Execute only `W7-D5-RUN-01`, once, over the 26-probe D4 exam, with no model contact and no generated output. Any capture finding, branch-state change, provenance mismatch, cardinality mismatch or other hard stop ends the successful-run path and must be reported without retry.
>
> Keep the D4 harness byte-identical. Invoke it with `authorising_record = W7-D4-SHB`, then add only the pure D5 authority/identity binding layer required to replace the top-level run authority with `W7-D5-SEB` while preserving `W7-D4-SHB` on every capture. On a wholly clean run, construct exactly 26 candidate GERs, the one D4-shaped run manifest, the D2-E proof succession, the materialised-state proof module, the completion record, registry delta and phase-board delta in the disposable candidate clone.
>
> Implement the GER lifecycle law in this brief: published identity is stable, no ID reuse ever, canonical path fixed, no D5 deletion, no D5 archive, no D5 withdrawal mechanism, no automatic expiry. Demonstrate the ID-scoped S3 history proof and its required mutants before claiming S3 mechanical. In successful Landing B, change the existing ADR-0049 registry namespace text from `grammar defined only — no identifier allocated` to the exact successor wording fixed in section 17.3; do not change it in Landing A.
>
> Return one final packet containing exact path scope, bytes, hashes, run accounting, manifest relation, nineteen-obligation matrix, P4a report, mutation results, scans, suite results, registry delta, board delta and all open-boundary statements. Do not stage, commit or push. Do not write any GER `human_review.disposition`. Do not open W7-D6.
>
> Ari reviews the engineering. Tara then performs P4b against the exact candidate and separately accepts the final packet. Only after that explicit authority may the exact accepted bytes be transferred to the authoritative checkout, verified, staged, committed and pushed by the bounded ceremony in this brief.

---

## 46. Resting state if this brief alone is published

After Landing A and before execution, the lawful state is:

- W7-D5 is open for this brief-governed implementation only;
- the D5 lifecycle/materialisation law is in force;
- no GER exists;
- no GER identifier is allocated;
- no generated-evaluation home exists;
- no run manifest exists;
- `W7-D5-RUN-01` is the sole authorised first execution identity but has not begun;
- D4 exam/harness/proof remain frozen;
- S1 is still live until the authorised creation landing occurs;
- S2 remains READY-DEBT until real subjects exist;
- S3 remains review-only until D5 demonstrates the new history proof over real subjects;
- Part Q remains unresolved;
- local-wordlist seam remains unresolved;
- p3 remains outstanding;
- no model contact;
- no generated output;
- W7-D6 through W7-D7 remain unopened;
- W8 remains unopened.

That is the correct pause point if implementation does not begin immediately.

---

## 47. Final architecture statement

W7-D5 is the phase where the Wing stops proving that it **could** govern a text-bearing evaluation record and proves that it can govern a real materialised set without letting materialisation become authority.

The key discipline is not the creation of 26 JSON files. It is the preservation of every distinction that earlier W7 landings worked to make explicit:

- authored specimen is not generated output;
- run authority is not specimen authorship;
- capture is not conclusion;
- difference is not winner;
- record identity is not authority;
- allocation is not reuse permission;
- manifest is not summary;
- publication review is not D6 disposition;
- a clean scan is not P4b;
- a green harness is not model evidence;
- a first materialisation is not an invitation to keep expanding the class.

D5 succeeds when the class becomes real **without any of those boundaries becoming softer because files now exist**.
