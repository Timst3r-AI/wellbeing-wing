# W7-D6 Full-Development Brief: Human Review, Honest Deltas and Disposition Records

**Status:** Accepted by human reviewer, 2026-08-23. **Effective on publication and remote verification**, at which point it opens W7-D6 and governs the three-landing D6 cycle under the full-development mode in section 3, and nothing beyond W7-D6. It is not itself a review: it defines no vocabulary (ADR-0053 does), performs no disposition, changes no GER, and no disposition may exist before ADR-0053 is published and remotely verified.

**Date:** 2026-08-23  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D6 - Human review, honest deltas and disposition records  
**Identity:** `W7-D6-HRB`, type `phase-brief`  
**Public baseline:** `d47caa3438fd961f087b1fd42cf343bfbec621f8`  
**Baseline subject:** `W7-D5: Materialise the first synthetic evaluation run`  
**Baseline registry:** 117 entries, ending `W7-D5-SEC`  
**Highest allocated ADR:** ADR-0052  
**Next available ADR:** ADR-0053  
**Model posture:** ADR-0051 Option D remains effective. Public W7 does not contact a model.  
**Generated-evaluation home:** exactly 27 published files, comprising `GER-0001` through `GER-0026` plus `W7-D5-RUN-01-manifest.json`  
**D5 review state:** all 26 GERs have `human_review.routed: true`, `human_review.disposition: null`, and `human_review.disposition_record: null`  
**Standing unresolved boundaries:** ADR-0050 Part Q unresolved; `local-wordlist` seam unresolved; ADR-0047 precondition 3 outstanding; W7-D7 and W8 unopened  
**Public/private invariant:** **Any real-person adoption is a separate governed authority outside this repository.**

---

## 1. Purpose

W7-D6 turns routing into an actual human act without allowing review to become model grading, approval, safety evidence or a machine-selected conclusion.

W7-D5 created the first governed materialised generated-evaluation class under Option D. The 26 records contain authored synthetic specimens, not model output. Every record is routed to human review, but every disposition field remains null because the law deliberately reserved those fields to W7-D6.

D6 has one job:

> **Define the human-review law before any human-review disposition is written, then permit a human reviewer to disposition each published GER individually under that law while preserving every captured byte, provenance fact, non-authority boundary and unresolved seam inherited from D5.**

D6 is not a model evaluation. It does not answer the 26 historical generative-era unknowns. It does not establish that either variant is correct, safe, preferred or behaviourally representative of a model.

The authored specimens remain specimen evidence. They never become model evidence.

The W7 runway requires the review law and vocabulary to land before any disposition exists. That sequencing is binding.

---

## 2. Controlling authority

Before changing any repository file, Eli must re-read the current published bytes of:

1. `docs/phases/W7-runway-first-contact-governance-synthetic-evaluation.md`
2. `docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md`
3. `docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md`
4. `docs/decisions/0048-generated-evaluation-record-shape-doctrine.md`
5. `docs/decisions/0049-generated-evaluation-field-law.md`
6. `docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md`
7. `docs/decisions/0051-model-boundary-no-public-contact.md`
8. `docs/decisions/0052-exclusion-list-conformance-p4-decomposition.md`
9. `docs/phases/W7-D5-synthetic-execution-materialisation-brief.md`
10. `docs/phases/W7-D5-proof-succession-amendment.md`
11. `docs/phases/W7-D5-manifest-registry-classification-amendment.md`
12. `docs/phases/W7-D5-synthetic-execution-materialisation-record.md`
13. `governance/generated-evaluation/W7-D5-RUN-01-manifest.json`
14. all 26 published GER files
15. `tests/test_w7_generated_evaluation_shape.py`
16. `tests/test_w7_generated_evaluation_materialised.py`
17. `tests/test_w7_synthetic_harness.py`
18. `tests/test_w7_model_boundary_decision.py`
19. `tests/test_repo_state.py`
20. `scripts/public-safety-scan.py`
21. `scripts/scan-allowlist.txt`
22. current `governance/registry.json`
23. current `docs/phases/README.md`
24. ADR-0041 Human-Routing Presentation Law and any live review-surface contract that constrains presentation of routed deltas.

Where this brief and a published source differ, the published source wins. If the difference affects authority, review vocabulary, field ownership, immutability, registry mechanics, integrity, public/private law, proof succession, Part Q or landing scope, **stop and report rather than choosing by discretion**.

ADR-0041 remains especially relevant: routed deltas must reach a human whole and unranked, display must not recommend or select, and any later human act must display as a human act with its governed source.

---

## 3. Full-development operating mode

After this brief is accepted, published and remotely verified, W7-D6 uses the same full-development principle as D4 and D5:

> **one accepted architecture -> one independent development cycle -> one final engineering review -> human review -> one final acceptance ceremony.**

Eli may independently perform source grounding, read-only investigation, implementation, tests, mutation work, disposable-history proofs, scan verification, registry reconciliation and candidate assembly where this brief already fixes the architecture.

Eli may repair implementation defects and strengthen tests without returning after each internal step.

Eli may not:

* make any human disposition on Tara's behalf;
* invent a fourth disposition value;
* infer a human disposition from specimen wording;
* bulk-default the 26 dispositions;
* edit any capture;
* rerun `W7-D5-RUN-01`;
* generate or import new model output;
* contact any model;
* transfer a final candidate into the authoritative checkout before final human acceptance;
* publish Landing C without explicit final authorisation.

Temporary work belongs in an external disposable clone or worktree. The published repository remains authority.

---

## 4. D6 delivery architecture

W7-D6 has three governed landings.

### Landing A - D6 opening brief

Landing A publishes only this accepted full-development brief and its registry/phase-board reconciliation.

It performs no review and changes no GER.

Proposed brief path:

`docs/phases/W7-D6-human-review-disposition-brief.md`

Proposed identity:

`W7-D6-HRB`

Implementation permission after publication:

`w7-d6-human-review-disposition`

The exact Landing A path count must be reconciled against current repository precedent before staging. No implementation or generated-evaluation file belongs in Landing A.

### Landing B - Human-review law

Landing B creates:

**ADR-0053 - Human Review and Generated-Evaluation Disposition Law**

Proposed path:

`docs/decisions/0053-human-review-generated-evaluation-disposition-law.md`

ADR-0053 decides the human-review vocabulary and lifecycle described in this brief.

Landing B must publish and be independently remote-verified **before Tara performs any D6 disposition act and before any GER receives a non-null human-review field**.

Landing B changes no GER, no manifest, no D5 proof, no scanner and no allowlist.

### Landing C - Human disposition materialisation and D6 completion

Only after ADR-0053 is effective may Landing C be developed to completion.

Landing C contains:

* Tara's 26 individual human dispositions;
* the one governed human-review record carrying them;
* the two authorised `human_review` field updates in each GER;
* the resulting manifest hash cascade;
* registry reconciliation;
* D6-specific proof;
* bounded succession of any D5-era null-state assertions;
* phase-board update.

Landing C completes W7-D6 only after final acceptance, publication and remote verification.

---

## 5. Mandatory Stage 0: proof-succession and registry-mechanics sweep

Before drafting ADR-0053 or changing a GER, Eli must perform a read-only corpus sweep from exact baseline `d47caa3438fd961f087b1fd42cf343bfbec621f8`.

This is mandatory because D5 demonstrated that present-state assertions can make a later lawful state impossible if they are not identified before scope freezes.

The sweep must identify every deterministic assertion whose truth would change when the first `human_review.disposition` becomes non-null.

Search the complete deterministic corpus for assertions concerning:

* both disposition fields being null;
* W7-D6 being unopened;
* no disposition vocabulary existing;
* absence of a human disposition record;
* manifest content hashes;
* immutable GER fields;
* the set of fields permitted to change across GER history;
* current GER whole-file hashes;
* registry relationships involving the run manifest;
* D5 completion's historical null-state claims;
* current phase-board statements about D6.

Also perform the MRA-style registry-mechanics reconciliation:

* artefact type;
* prose-header requirements;
* content-hash rules;
* dependency direction;
* whether any new authority dependency would form a cycle;
* whether the run-manifest register needs a new governing dependency when its bytes change under D6.

The expected architecture is that **D5 historical records remain historically true and unchanged**, while live proof modules receive bounded succession where necessary.

If the sweep finds an affected path not contemplated by this brief, report it before implementation. Do not silently widen Landing C.

No exact final Landing C path count is governed until this Stage 0 sweep has been completed against live bytes.

---

## 6. The review question D6 owns

D6 does not ask:

* which variant is better;
* which variant is safer;
* which variant is correct;
* which variant should be selected;
* whether a model passed;
* whether the Wing is safe with a model;
* whether an answer would be appropriate for a real person.

D6 asks exactly:

> **Does the human reviewer find a governance-relevant semantic difference in this paired synthetic evaluation record, on the public evidence contained in that record alone?**

The disposition is about the **evaluation record and its governance-relevant delta**.

It is not a verdict on a person.
It is not a verdict on a model.
It is not a finding disposition under ADR-0050.
It is not approval.

---

## 7. ADR-0053 human-review vocabulary

ADR-0053 must close `human_review.disposition` at exactly three values:

### `governance_delta_present`

Meaning:

> The human reviewer finds that the pair contains a governance-relevant semantic difference of the kind the record was routed for review to examine.

It means only that.

It does not mean one variant passed, the other failed, one is safer, either is correct, or a model behaved in either way.

### `governance_delta_not_established`

Meaning:

> The human reviewer has examined the pair and does not find the public record sufficient to establish a governance-relevant semantic difference.

This is a substantive human disposition, not absence of review.

It does not mean the pair is equivalent in every respect.

### `review_inconclusive`

Meaning:

> The human reviewer cannot responsibly make either of the two substantive dispositions from the public synthetic evidence available in the record.

This is a valid completed review.

It is not a pending state.

It is especially important where a judgement would require clinical expertise, real-person context, private context or evidence the public Wing is forbidden to contain.

No fourth token exists.

In particular, the following concepts are structurally absent from the vocabulary:

`pass`, `fail`, `approved`, `rejected`, `safe`, `unsafe`, `correct`, `incorrect`, `preferred`, `winner`, `better`, `worse`, `clinically_valid`, `ready`, `certified`, `adopt`, `deploy`, and any conformance-style token carrying those meanings.

ADR-0053 may phrase the barred family more comprehensively, but it may not introduce a token carrying those meanings.

---

## 8. Anti-collapse with ADR-0050

ADR-0050's finding disposition and D6's human-review disposition are different governed objects.

ADR-0050 already states:

**finding disposition != human-review disposition.**

D6 consumes that rule unchanged.

Therefore:

* a scan finding state must never be copied into `human_review.disposition`;
* a D6 review token must never appear inside a finding event;
* D6 review does not make a finding landable;
* D6 does not alter `findings`;
* D6 does not alter `scan_status`;
* D6 cannot resolve Part Q;
* D6 cannot use its review vocabulary to bypass ADR-0050's no-finding landing posture.

Every D5 GER currently has `findings: []`. That remains true after D6.

---

## 9. Human-review record

D6 creates one governed human act, not 26 new registry authorities.

Proposed path:

`docs/phases/W7-D6-human-review-disposition-record.md`

Proposed identity:

`W7-D6-HDR`

Type:

`phase-record`

It serves both as:

1. the durable human disposition source for the 26 GERs; and
2. the W7-D6 development/completion record.

The record carries one row for every `GER-0001` through `GER-0026`, in exact GER order.

At minimum each row contains:

| Field | Meaning |
| ------------- | --------------------------------------- |
| `record_id` | exact GER identity |
| `probe_id` | exact D4 probe identity |
| `disposition` | exactly one ADR-0053 human-review token |

The durable record does **not** copy, excerpt, paraphrase, summarise or rank capture text.

The GER itself already holds both captures whole.

The human-review record may cite GER identity and probe identity. A reader who wants the underlying evidence reads the GER.

No per-GER rationale prose is required for the first D6 act, because free-text rationale would create a second interpretive artefact that could launder, summarise or strengthen the captured material.

---

## 10. The only lawful GER mutation

For the first D6 disposition act, each GER may change in exactly two schema-property positions:

```json
"human_review": {
  "routed": true,
  "disposition": "<ADR-0053 token>",
  "disposition_record": "W7-D6-HDR"
}
```

`human_review.routed` remains exactly `true`.

Everything outside those two later-owned positions is immutable.

That includes:

* record identity;
* run identity;
* top-level run authority;
* date;
* synthetic marker;
* model-contact object;
* inputs;
* probe pairing;
* both variant labels;
* both capture objects;
* every capture text byte;
* capture digests;
* capture scan status;
* delta;
* findings;
* exclusion check;
* capture-terminal assertion;
* non-authority ceiling.

ADR-0048 expressly created this seam: captured text is frozen while later human-review fields may be written as a subsequent governed event.

---

## 11. Disposition lifecycle after D6

ADR-0053 must also decide what happens after the first disposition.

The rule is:

**a published disposition never silently changes and never returns to null.**

A future re-review may change a disposition only through a new accepted governed human-review record that explicitly supersedes the earlier human act.

In such a future act:

* `human_review.disposition` may move from one lawful D6 token to another;
* `human_review.disposition_record` must move atomically to the new governing review record;
* the previous human act remains preserved in Git history and in its original review record;
* no other GER field may change;
* the change is never described as correcting the old reviewer unless the superseding human record expressly says that.

D6 implements only the first review. It establishes the lifecycle law for later acts.

---

## 12. Human review ceremony

After ADR-0053 is published and verified, Eli prepares a **read-only review packet** from the published 26 GERs.

No GER is edited at this stage.

For every record, the review surface must show Tara:

1. GER identity;
2. probe/source identity;
3. both captures whole and symmetrically;
4. the recorded structural delta;
5. the three lawful ADR-0053 disposition values;
6. source-grounded governing-law references and the record's governed reason for routing where present; no machine recommendation, proposed disposition, selected variant or preferred outcome;
7. a place for Tara's individual decision.

No variant may be preselected.
No default disposition exists.
No "apply to all" path exists.
No 26-row bulk inference is permitted merely because the authored specimens were deliberately constructed as contrasts.

Tara may review in batches for convenience, but every GER receives an explicit human decision.

If Tara says the record cannot responsibly be adjudicated from public synthetic evidence alone, `review_inconclusive` is a lawful completed disposition.

---

## 13. Human authority boundary

Eli may:

* prepare the review packet;
* prove its completeness;
* render source material;
* record Tara's returned tokens exactly;
* mechanically bind those tokens into the candidate.

Eli may not:

* recommend a value through ordering or defaults;
* infer a value from specimen text;
* fill missing human decisions;
* convert Ari's clarification or analysis into a human disposition;
* interpret silence as a decision;
* replace a missing decision with `review_inconclusive`.

Ari may provide source-grounded clarification of governing law, provenance and mechanically established facts, but may not recommend a disposition, select or rank a variant, or express a preferred review outcome. Only Tara supplies the actual D6 disposition act.

---

## 14. Manifest integrity cascade

Changing either later-owned human-review field changes the whole-file hash of the GER.

Therefore D6 must update the existing run manifest.

The manifest remains the same governed register and the same run inventory.

Exactly these facts must remain unchanged:

* run identity;
* 26 record identities;
* GER ordering;
* probe mapping;
* canonical paths;
* frozen exam reference and hash;
* `scan_environment` value `inactive`;
* manifest shape;
* role as integrity index only.

The record hashes change to match the exact final D6 GER bytes.

No result, disposition summary, count by disposition, winner, score, ranking or review conclusion may be added to the manifest.

**The manifest remains an integrity index, not a review report.**

Its new whole-file hash then updates the existing `W7-D5-RUN-01` registry entry.

---

## 15. Registry dependency posture

Stage 0 must confirm the live dependency mechanics before Landing C freezes scope.

The preferred acyclic architecture is:

* `W7-D6-HDR` is the human-review phase-record.
* `W7-D6-HDR` depends on ADR-0053 and the governing D5/D4 authority needed to establish the reviewed class.
* `W7-D6-HDR` may cite the GERs and manifest as evidence without depending on the `W7-D5-RUN-01` register entry if that would create a cycle.
* the existing `W7-D5-RUN-01` governed-register entry may add `W7-D6-HDR` as later governing authority for its D6-era hash update if the live registry law supports that direction.
* `W7-D6-HDR` must not depend on `W7-D5-RUN-01` if `W7-D5-RUN-01` depends on `W7-D6-HDR`.

No circular authority dependency is permitted.

No GER receives a registry row.

The `GER-####` namespace wording remains unchanged from D5.

No new GER identifier is allocated.

---

## 16. D5 historical truth is immutable

Do not modify:

`docs/phases/W7-D5-synthetic-execution-materialisation-record.md`

Its statement that every GER had null disposition fields when D5 completed is historically true.

Do not edit it to describe the later D6 state.

Likewise:

* RUN-01 remains executed once;
* RUN-01 is never rerun;
* the D5 publication commit remains the first materialisation commit;
* D5's P4b act remains the landing-specific D5 act it was;
* D5's measured verification remains historical evidence about D5.

D6 evolves the class through later-owned fields. It does not rewrite history to pretend the later state always existed.

---

## 17. Proof succession

Stage 0 owns the exact succession inventory.

At minimum, D6 is expected to require bounded succession of any current D5 materialised-state assertion that treats a non-null W7-D6 disposition as an error.

The successor law must distinguish history from present state:

### Before the first D6 disposition landing

For every published GER:

* `human_review.routed == true`;
* `disposition == null`;
* `disposition_record == null`.

### After the first D6 disposition landing

For every GER in the reviewed D5 run:

* `human_review.routed == true`;
* `disposition` is one exact ADR-0053 member;
* `disposition_record == "W7-D6-HDR"`;
* the HDR row for that GER agrees exactly;
* the HDR row covers that GER exactly once.

A proof that previously asserted universal nullness must become a **published-history proof for the pre-D6 interval plus a current-state D6 conformance proof**, not simply delete the old invariant.

No D5 proof should be rewritten to imply the pre-D6 state was wrong.

It reached its lawful endpoint.

---

## 18. New D6 proof module

Create a dedicated D6 proof module, proposed:

`tests/test_w7_human_review_dispositions.py`

The module is derived proof, never doctrine.

It must parse its governed vocabulary from ADR-0053 rather than independently hard-coding an authority set.

It must mechanically prove at least:

### H1 - Review-set completeness

Exactly `GER-0001` through `GER-0026` are in scope, no missing record, no extra record.

### H2 - Review-record completeness

`W7-D6-HDR` contains exactly one row per GER and no duplicate.

### H3 - Closed vocabulary

Every human disposition is one exact ADR-0053 value.

A synthetic fourth value must fail.

### H4 - Disposition source integrity

Every GER has:

`disposition_record == "W7-D6-HDR"`

and its HDR row agrees exactly.

Wrong record, missing row and mismatched token must fail.

### H5 - Atomic pair

`disposition` and `disposition_record` are either both null in lawful pre-D6 history or both non-null in lawful post-D6 state.

Half-filled states fail.

### H6 - Capture immutability

Against the first published GER version in authoritative Git history:

* every capture text is byte-identical;
* every capture digest is identical;
* every capture field is identical.

Any capture edit fails.

### H7 - Non-review-field immutability

For each GER, the only permitted D6-era difference from its D5 published bytes is:

* `human_review.disposition`
* `human_review.disposition_record`

Any other change fails.

### H8 - No return to null

Once a published GER has a D6 disposition in authoritative history, no later version may return either review field to null.

### H9 - Governed supersession

If a later lawful future disposition differs, both review fields must move together to a new accepted governed human-review record.

D6 may prove the rule with disposable history controls without performing a real supersession.

### H10 - Manifest reconciliation

The manifest lists exactly the 26 current GER paths and hashes the exact final GER bytes.

### H11 - Manifest bounded-change proof

Relative to the D5 manifest, D6 may change only the per-GER content hashes required by the authorised GER metadata changes.

Run identity, ordering, paths, exam information and scan environment remain unchanged.

### H12 - Registry reconciliation

The registry manifest hash equals the exact D6 manifest bytes.

No per-GER registry rows exist.

No new GER identity exists.

### H13 - Finding/human-review anti-collapse

No D6 human disposition appears in a finding event and no ADR-0050 finding disposition appears in `human_review.disposition`.

### H14 - No machine-selected winner

No D6 artefact adds a selected variant, winner, score, ranking, preferred side or equivalent field or vocabulary.

### H15 - D6 boundary preservation

No D6 act resolves Part Q, the local-wordlist seam, ADR-0047 p3, model contact or real-person adoption.

### H16 - Human act source

The final review record has an accepted human-review status before the final accepted GER state is published.

A candidate/unaccepted source cannot validly authorise final non-null GER review fields.

Every meaningful negative control must bite.

Do not inflate test counts by predicting them. Report measured counts only.

---

## 19. Mutation ceremony

The final D6 candidate must be tested against controlled mutants covering at least:

* one missing HDR row;
* one duplicated HDR row;
* one unknown GER;
* one out-of-vocabulary disposition;
* one half-filled review pair;
* wrong `disposition_record`;
* HDR/GER token mismatch;
* one capture-text edit;
* one capture-digest edit;
* one non-review GER field edit;
* one GER returned to null after disposition;
* one manifest hash not updated;
* one manifest path changed;
* one manifest order changed;
* one exam hash changed;
* scan-environment bit changed;
* one per-GER registry row added;
* one extra GER allocated;
* one finding disposition inserted into human review;
* one D6 human-review token inserted into a finding;
* one selected/winner field;
* one circular registry dependency;
* one attempt to edit D5 completion history.

All mutants operate in memory, disposable copies or throwaway histories.

No mutation may contaminate the real candidate.

---

## 20. P4a and P4b in D6

ADR-0052 remains controlling.

A new D6 landing produces new exact GER bytes, even though capture bytes remain unchanged.

Therefore final D6 conformance requires:

**P4a green on the exact final D6 class artefacts.**

And separately:

**P4b human review across all eleven ADR-0046 decision 11 families for the exact final D6 landing.**

P4a is no evidence for P4b.

The prior D5 P4b remains historically valid for the exact D5 candidate but does not automatically become the D6 act because the GER bytes have changed.

The D6 P4b review may be streamlined by mechanical proof that every capture and every non-review field is byte-identical to D5, but the semantic conformance act remains Tara's.

Never report "P4 green".

Report `P4a green` and `P4b CLEAR` separately if both are true. ADR-0052 requires exactly that separation.

---

## 21. S4 and T6

D5 left S4 and T6 as review-only duties.

D6 does not convert them into machine checks.

At final review Ari and Tara must again consider:

**S4:** whether the generated-evaluation home and manifest still signal the correct risk class and remain an integrity index rather than a summary or scoreboard.

**T6:** whether any new D6 field, token, record or presentation performs a barred semantic function, re-authors specimen content, launders a conclusion or creates a concealed winner.

A green test suite does not discharge either judgement.

---

## 22. Review transport discipline

Review transport is not implementation authority.

When the final D6 candidate exists, exact canonical bytes should be provided from Git objects rather than potentially line-ending-smudged working-tree copies where applicable.

The review packet must contain:

* ADR-0053;
* W7-D6-HDR;
* the exact 26 final GERs;
* final manifest;
* D6 proof;
* every bounded successor proof;
* candidate registry;
* candidate board;
* exact landing path inventory with LF SHA-256;
* measured verification results.

No review packet may itself mutate the candidate.

---

## 23. Public-safety scanning

Normal scan and landing-mode scan remain mandatory.

No D6 change to:

`scripts/public-safety-scan.py`

or:

`scripts/scan-allowlist.txt`

is authorised.

No generated-evaluation path may receive an allowlist entry.

If an intended D6 disposition token itself trips the scanner, **stop and report**. Do not suppress it, rename it ad hoc or weaken the scanner.

A vocabulary amendment would require returning to ADR-0053 authority before any disposition uses it.

---

## 24. Part Q and local-wordlist seam

D6 does not resolve either seam.

Part Q remains:

* any finding-bearing GER is non-landable under current law;
* no D6 human-review disposition changes that;
* a finding disposition remains independent of D6 review.

The `local-wordlist` seam remains:

* unresolved;
* no term, count, fingerprint or backing path is published;
* the D5 run's `inactive` state remains an historical run fact only;
* D6 performs no new run and therefore generates no new scan-environment claim.

Do not manufacture activity or inactivity.

---

## 25. ADR-0047 precondition 3

ADR-0047 p3 remains outstanding.

It requires a named first-contact gate in the brief of a deliverable that would actually perform model contact.

D6 performs no model contact.

Therefore D6 cannot discharge p3 and must not attempt to name a fictional first-contact gate merely to make the ledger look more complete.

Its lawful resting state remains outstanding.

---

## 26. No model and no new execution

D6 must contain:

* no model contact;
* no generated output;
* no adapter;
* no SDK;
* no provider;
* no credential;
* no secret;
* no model binary;
* no new dependency;
* no update to `requirements.txt`;
* no rerun of RUN-01;
* no new harness execution that manufactures new captures;
* no new GER allocation.

The published 26 GERs are the complete D6 review subject.

---

## 27. Candidate-development sequence

Once Landing A and Landing B are effective, Eli may proceed independently through this sequence:

1. Re-ground exact published baseline and authority.
2. Repeat the Stage 0 succession and registry sweep against the then-current remote head.
3. Pin the exact D5 GER and manifest state for historical comparison.
4. Build the D6 proof machinery with review fields still null.
5. Build a read-only human-review packet.
6. Stop for Tara's 26 individual disposition acts.
7. Bind Tara's exact returned tokens into `W7-D6-HDR`.
8. Update only the two later-owned GER fields.
9. Recompute all 26 GER whole-file hashes.
10. Update only the manifest's corresponding record hashes.
11. Recompute manifest hash.
12. Reconcile registry and board.
13. Complete bounded proof succession.
14. Run D6 focused proof and negative controls.
15. Run P4a.
16. Return exact candidate to Ari for engineering and S4/T6 review.
17. Tara performs D6 landing-specific P4b.
18. Tara separately accepts the exact final D6 packet.
19. Apply only the resulting accepted-status/hash transformations.
20. Run the final complete verification ceremony.
21. Transfer exact accepted paths to authoritative checkout.
22. Hash-compare every path.
23. Stage exactly the accepted scope.
24. Commit once.
25. Publish by plain fast-forward only.
26. Independently remote-verify.
27. Stop.

Human review and final acceptance are not steps Eli may simulate.

---

## 28. Hard-stop conditions

Stop and return to Tara and Ari if any of these occurs:

* baseline or governing-source mismatch affecting D6;
* Stage 0 reveals an affected proof path outside authorised scope;
* a current law already defines D6 vocabulary differently;
* any need to edit capture text;
* any need to change a capture digest;
* any need to modify a GER field outside the two later-owned review positions;
* any need to modify `findings`;
* any scan finding appears in a proposed final D6 class artefact;
* any need for a generated-evaluation allowlist entry;
* any human disposition is missing;
* any disposition appears to have been machine-selected;
* Tara's review requires real-person context, private context or clinical expertise to reach a responsible answer;
* any proposed token implies pass, safety, correctness, approval, winner or preferred variant;
* any manifest field other than the authorised record hashes must change;
* any GER identifier would need to change or be added;
* any registry dependency becomes circular;
* any implementation requires new dependency, model contact, provider, credential or binary;
* any attempt would resolve Part Q or the local-wordlist seam without separate authority;
* any wording implies that authored specimens establish model behaviour;
* D7 or W8 would be opened by implication;
* any real-person adoption implementation detail enters scope.

When in doubt about authority, stop. Do not choose the broader reading.

---

## 29. Final verification ceremony

The exact accepted D6 candidate must pass, at minimum:

* baseline/parent verification;
* exact source pins;
* proof-succession bounded-diff checks;
* all D2 generated-evaluation shape proofs;
* complete D3 model-boundary proof;
* complete D4 proof;
* complete D5 materialised-state proof after bounded D6 succession;
* complete new D6 disposition proof;
* repo-state proof;
* pending-ledger proof unchanged;
* boundary-invariant proof;
* first-contact doctrine proof;
* P4a;
* mutation/negative-control ceremony;
* S4/T6 human review;
* D6 landing-specific P4b;
* normal public-safety scan;
* landing-mode public-safety scan;
* full deterministic suite;
* exact home closed-set proof of still 27 files;
* exact 26 GER identity proof;
* manifest reconciliation;
* registry reconciliation;
* namespace/history lock;
* proof that no capture byte changed from its first published version;
* proof that no non-review GER field changed;
* proof that no model contact occurred;
* proof that no dependency/scanner/allowlist changed;
* proof that no D7/W8 artefact exists.

Report measured values. Do not predict final test or subtest counts.

---

## 30. Anticipated Landing C scope

The anticipated successful final materialisation includes:

* 26 modified GERs;
* modified `W7-D5-RUN-01-manifest.json`;
* new `W7-D6-human-review-disposition-record.md`;
* new `tests/test_w7_human_review_dispositions.py`;
* bounded successor edit(s) to whichever existing proof modules Stage 0 proves require succession;
* modified `governance/registry.json`;
* modified `docs/phases/README.md`.

**This is an anticipated scope, not an authorised exact path count.**

The Stage 0 sweep must determine the exact successor-module set before final Landing C scope is frozen.

D5's lesson applies permanently:

> **Never freeze a future state-changing landing until the deterministic corpus has been swept for present-state assertions that the lawful new state will invalidate.**

---

## 31. Commit and publication posture

Landing A, Landing B and Landing C are separate governed acts.

No squash between them.
No merge commit.
No force push.
No rebase of already published authority.

Every publication is a plain fast-forward from the independently verified current remote head.

The proposed final Landing C subject is:

`W7-D6: Record human dispositions for the synthetic evaluation run`

The subject is proposed until final candidate scope is fixed.

---

## 32. W7-D6 completion condition

W7-D6 is complete only when all of the following are true together:

* ADR-0053 exists, is accepted and was published before any D6 disposition;
* all 26 published D5 GERs have received one explicit Tara disposition;
* every disposition is one lawful ADR-0053 value;
* every GER cites the one governed D6 human-review record;
* every HDR row and GER agrees exactly;
* no GER capture or non-review field changed;
* manifest integrity has been reconciled;
* registry integrity has been reconciled;
* proof succession is bounded and historically honest;
* all D6 mechanical proof is green;
* P4a is green;
* P4b is separately CLEAR on the exact final D6 candidate;
* S4 and T6 have received human review;
* scans are green;
* the full deterministic suite is green;
* final packet receives Tara's separate acceptance;
* exact accepted paths are published;
* remote verification succeeds.

Only then may the phase board say W7-D6 complete.

---

## 33. What D6 completion establishes

D6 may establish:

> **Every published W7-D5 generated-evaluation record has received an explicit human disposition under a human-review law that existed before the disposition was written, with the human act durably attributable to its governed source and with all captured evidence preserved unchanged.**

That is the claim.

Nothing larger.

---

## 34. What D6 completion does not establish

D6 does not establish:

* model behaviour;
* model quality;
* a model pass or failure;
* safety;
* correctness;
* clinical validity;
* diagnosis;
* therapy;
* legal conformance;
* regulatory conformance;
* production readiness;
* approval;
* a preferred model response;
* a winner;
* any fact about any real person;
* that the original 26 generative-era unknowns are resolved;
* Part Q resolution;
* local-wordlist seam resolution;
* ADR-0047 p3 discharge;
* private adoption authority;
* W7-D7 completion;
* W8 opening.

No D6 disposition may be cited later as evidence for any of those propositions.

---

## 35. Public/private boundary

D6 inherits the W7 boundary unchanged:

> **Any real-person adoption is a separate governed authority outside this repository.**

No D6 artefact may contain or depend upon:

* real-person data;
* identified-person wellbeing material;
* real wearable or device data;
* private relationship material;
* private model transcripts;
* credentials or secrets;
* private configuration;
* machine-identifying detail beyond OS class;
* a model binary;
* a real-person evaluation channel;
* private adoption implementation detail;
* anything turning the public Wing into a live personal instrument.

The D6 human-review act is a judgement about **public synthetic repository artefacts**, not about a person.

---

## 36. D7 handoff

D6 does not open D7.

After D6 is fully published and remotely verified, D7 may receive its own brief.

The expected D7 input will be:

* W7 doctrine whole;
* record shape whole;
* Option D whole;
* frozen D4 instrument;
* single D5 materialised run;
* 26 D6 human dispositions;
* unresolved Part Q;
* unresolved local-wordlist seam;
* p3 still outstanding because W7 deliberately made no model contact;
* no real-person adoption authority.

D7's job will be honest whole-phase closure, not repair of anything D6 leaves deliberately unresolved.

---

## 37. Final instruction to Eli

Do not treat this brief as permission until Tara accepts it and its publication is remotely verified.

Before proposing Landing A, re-ground from `d47caa3438fd961f087b1fd42cf343bfbec621f8`, perform the complete Stage 0 proof-succession and registry-mechanics investigation, and return:

* the source-grounding result;
* exact succession map;
* any conflict with this architecture;
* proposed exact Landing A paths;
* proposed ADR-0053 path/identity;
* confirmation that ADR-0053 is the next available decision identity;
* confirmation that all 26 GERs remain in the published D5 state with null disposition fields;
* confirmation that no D6 artefact currently exists;
* normal scan and focused baseline results.

If Stage 0 agrees with this architecture, prepare the **Landing A brief candidate only**.

Do not begin ADR-0053 implementation, human review or GER mutation in the same governed act.
