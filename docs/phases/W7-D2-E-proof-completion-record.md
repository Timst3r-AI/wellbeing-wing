# W7-D2-E — Proof Completion Record

**Status:** **Accepted by human reviewer, 2026-08-20.** Not a build instruction. Authorises no implementation.
**Phase:** W7 · **Deliverable:** **W7-D2** (landing **W7-D2-E**, the fifth and final)
**Registry identity:** `W7-D2-E`, type `phase-record`. **ADR-0051 is neither allocated nor reserved.**
**Baseline:** `6c8a0e6c35eb58beb190bc50793ecf55948ec6d1`
**Governed by:** the W7-D2 opening brief (`W7-D2-RSB`), whole; **ADR-0048**, **ADR-0049** and **ADR-0050**, consumed as fixed inputs and reopened nowhere; ADR-0046 and ADR-0047 proof discipline and standing review duties; the W7 proof-module precedent; `tests/README.md`'s three-tier convention.

---

**Nineteen obligations were inherited and nineteen are accounted for. Five could be proved today. Ten have machinery that runs and bites against subjects that do not exist, and calling those satisfied would have been the most comfortable lie available. Four need a person. The proofs are written; the debts are still owed; and the record says which is which in the same breath as the green result.**

## 1. Baseline and authority chain

Verified before implementation, all ten facts exact: HEAD = local main = origin/main = `6c8a0e6c…` · ahead/behind 0/0 · working tree clean · registry **106** · W7-D2-E absent · no `0051` file · **ADR-0051 neither allocated nor reserved** · `governance/generated-evaluation/` **absent** · the proof module absent · no W7-D3 artefact.

**Re-verified at the landing pre-flight and unchanged**, with the two accepted implementation files matching their accepted SHA-256 digests byte for byte, no W7-D2-E board row present, and the pending ledger, scanner and allowlist byte-identical to the baseline.

**Authority chain:** `W7-D2-RSB` opened W7-D2 for record-shape work only → **ADR-0048** fixed home, format, granularity, integrity posture and immutability → **ADR-0049** fixed the field law, 46 positions across twelve shapes, and minted `GER-####` → **ADR-0050** fixed finding identity, the `character_start` locus, the closed disposition vocabulary, the allowlist prohibition and the landing predicate → **this record proves what can be proved and refuses to imply the rest.**

## 2. The nineteen-obligation matrix

| Status | Count | Obligations |
|---|---|---|
| **LIVE** — subject exists; the proof establishes the obligation | **5** | S1 · T1 · T2 · T3 · U1 |
| **READY / DEBT** — predicate runs and bites; **subject absent, obligation outstanding** | **10** | S2 · T4 · T5 · T7 · T8 · T9 · U2 · U3 · U4 · U5 |
| **REVIEW-ONLY** — human duty in full | **4** | S3 · S4 · T6 · U6 |

**5 + 10 + 4 = 19. No twentieth obligation was invented.**

**The governing rule, carried into the module docstring verbatim:** *absence may prove dormancy; absence may not discharge a debt whose subject does not exist.*

## 3. S3 — feasibility evidence and disposition

**S3 remains REVIEW-ONLY.** ADR-0048 declined to call it mechanical and assigned the decision here.

**Spike method:** a disposable throwaway git repository created **outside** `wellbeing-wing`, neutral placeholder tokens, **no GER, specimen, fixture or payload created anywhere**, nothing written under the reserved home.

**Evidence:**

- a **path-scoped** history check passes correctly when only review metadata changes, and bites when captured text changes at the same path;
- **but in clean isolation — rename the record, then edit the capture at the new path — the path-scoped check PASSES while the law is broken.** A record's identity is its `record_id`, not its path;
- an **id-scoped** check over all historical blobs catches that case, **but cannot distinguish an unlawful edit from deletion followed by reappearance of the same identifier, whose lifecycle status is unresolved under the current `GER-####` identity law**;
- `git log --follow` tracks renames by **similarity heuristic**, not guarantee.

**The identifier-precedent question was resolved from the accepted text rather than assumed.** ADR-0042 does contain a no-reuse semantic (decision 6, *"identifiers never reused — the W4-D6-BEF rule carried"*). **ADR-0049 did not import it**: decision 57's invocation is scoped by its own appositive to the registry-entry posture *"grammar defined only — no identifier allocated"*; its exhaustive "what the namespace is and is not" omits stability and reuse entirely; ADR-0042's rule is itself a carried import ADR-0049 did not carry; and the operative *"no ID reuse, ever"* lifecycle rule lives in **ADR-0045**, which ADR-0049 invoked only for the byte-fixed-sentence precedent.

**Absence of a no-reuse rule is not affirmative permission to reuse.** The sources establish only that the question is ungoverned, and **this record resolves it in neither direction and invents no identity or lifecycle doctrine.**

**S3 remains review-only until a later governed act supplies sufficient identity or lifecycle semantics for a complete mechanical proof. This record does not pre-decide which later rule or combination of rules will be sufficient.**

## 4. S2's narrower READY boundary

**S2 carries a limitation the other record-level debts do not.** ADR-0048 fixes the semantic obligation — every record listed · content hash present · listed file exists · hash matches — but **no manifest artefact and no governed manifest file shape exists.**

**READY therefore means exactly this and no more:** the **set-and-hash relation** is implemented and negatively controlled across all four failure forms. **It does not mean a repository-bound manifest parser is complete.** Binding the predicate to an actual artefact remains dependent on the later governed manifest shape. **This is not a twentieth obligation and not a new seam** — it is the honest boundary of what could be implemented before a manifest exists.

**The predicate therefore encodes no manifest shape at all.** It takes **two neutral mappings** — a listing and what is present — each from a **neutral identity token** to a hash or to a *no-hash-stated* sentinel. **It names no manifest key, no manifest-entry object, no manifest field and no final field name, and it is not a parser.** A subtest proves this mechanically: **the predicate's body indexes no string literal at all**, so no artefact position can be hiding inside it. All four ADR-0048 failure forms are still exercised — unlisted record · listed record absent · missing hash · hash mismatch.

## 5. Proof module and source-derived methodology

**Path:** `tests/test_w7_generated_evaluation_shape.py` — Python standard library only, **five test classes**, **exactly eighteen test functions**, control limbs carried by subtests. A sixth class exists and is not a test class: **a small non-test sentinel class representing ‘no hash stated’**, used by S2's neutral inputs.

**The landed records are the source of truth and are parsed, not re-expressed.** The eight nested shapes are derived from **ADR-0049's accepted `Holds` cells**; the record- and capture-level sets from its accepted field tables; the wrapper from its decision-4 anchor; the finding-event set from its "exactly the five fields" anchor. **No canonical expected field name or expected object shape is independently declared by the module. Synthetic mutant keys used solely as negative controls do not become schema authority.**

**Every governed constant is derived from landed source at import, not transcribed.** The **reserved home** is read from **ADR-0048 decision 7**; the **non-authority ceiling** from **ADR-0049 Part L**; the **disposition set and its own landability column** from **ADR-0050 Part F**; the **`locus` field** from **ADR-0050 Part D**. **Where landed law states the same fact in two authoritative places, the two are reconciled against each other rather than trusted singly** — the ceiling against **ADR-0046 decision 23**, the barred allowlist prefix against **ADR-0050 decision 32**, the finding-event set against ADR-0050's carried copy. **Where a predicate addresses a governed field name or value in its own logic, a subtest cross-checks that token against the source-derived map**, so no retained copy can silently become a second authority.

**T1 reconciles the record against itself through one checker.** The same function judges the live source-derived structure and every mutant, across six statement families: the **per-level counts** (wrapper 1 · record 15 · nested 20 · capture 5 · finding-event 5 · total 46), the **per-shape counts the counting row states in its own label**, the **three canonical-order claims** parsed from Part C decision 9, the **nullable positions resolved against the shapes that declare them**, and the **four vocabularies ADR-0049 states twice**. **Compensating errors cannot survive it**: a position moved between levels preserves the total and is caught by the per-level checks; a field moved between nested shapes preserves the nested level and is caught by the label counts. Both are demonstrated as controls, each asserting the exact disagreement set.

**T3's graph is derived, not constructed.** Its nodes and their direction are parsed from **decision 41's literal chain** — `text → text_digest → record bytes → manifest hash` — with the positions the record's bytes depend on read from the field tables, and **decision 40** and **decision 42** carried as source facts: the record holds no own content hash, the manifest hash lies outside the record, and the four identity positions decision 42 keeps in the record are present in the field table. **The planted self-hash is injected into that same derived graph.**

**Source-drift guards** are asserted for every anchored extraction, so a moved anchor fails rather than silently retaining a stale transcription.

### 5.1 One source-fidelity discrepancy found during implementation

**The accepted design said to anchor the finding-event shape on ADR-0050 decision 33. Implementation showed the law does not sit there.** The phrase *"carries exactly the five fields … and no sixth"* is in **ADR-0049**; **ADR-0050 carries the set as a quoted fixed input** in its Controlling law.

**The module therefore anchors on ADR-0049, where the law actually is, and asserts that ADR-0050 carries the identical set** — a cross-record agreement check that did not exist in the design. **No governing law was repaired inside the test**; only the design's citation of where the law sits was corrected, and it is reported here rather than absorbed.

## 6. The eighteen proof functions

| Class | Functions | Obligations |
|---|---|---|
| **`LiveShapeLaw`** | `test_t1_schema_statement_integrity` · `test_t2_canonical_field_sets_over_twelve_shapes` · `test_t3_integrity_graph_is_acyclic` | T1 T2 T3 — **LIVE** |
| **`LiveHomeAndAllowlist`** | `test_s1_reserved_home_is_vacant` · `test_u1_no_allowlist_entry_under_reserved_home` | S1 U1 — **LIVE** |
| **`ReadyPredicatesForAbsentSubjects`** | `test_s2_listing_and_hash_relation_predicate` · `test_t4_pair_bijection_predicate` · `test_t5_ceiling_verbatim_and_last_predicate` · `test_t7_delta_routing_predicate` · `test_t8_scan_status_predicate` · `test_t9_input_source_predicate` · `test_u2_exclusion_override_predicate` · `test_u3_locus_predicate` · `test_u4_disposition_predicate` · `test_u5_finding_reference_predicate` | S2 T4 T5 T7 T8 T9 U2 U3 U4 U5 — **READY / DEBT** |
| **`DebtsRemainOutstanding`** | `test_no_generated_evaluation_record_exists` · `test_absence_does_not_discharge_record_dependent_debts` | anti-vacuity |
| **`WhatGreenDoesNotMean`** | `test_module_states_its_boundary` | the boundary contract |

**The debt class is named for what it is, and its methods end `_predicate`, never `_holds`** — the obligation does not hold yet and no name in the module suggests it does.

## 7. Final landing results

**Measured at the four-path landing, with the registry entry and the board row present.**

| Check | Result |
|---|---|
| **Focused module** | **18 passed, 108 subtests passed** |
| **Full deterministic suite** | **527 passed, 9 skipped, 577 subtests passed** — from a 509 / 9 / 469 baseline |
| **Test delta** | **+18, exactly as designed.** Subtest delta **+108**; the design estimated roughly +30, and **the actual figure is reported rather than the estimate** |
| **Landing-mode public-safety scan, the four landing paths** | **4 files, 0 findings, 0 allowlist suppressions** |
| **Normal public-safety scan** | **241 tracked files, 0 findings, 123 allowlist suppressions — none new** |
| **Repo-state / registry integrity** | **14 passed** |
| **Registry** | **106 → 107** — one entry added, `W7-D2-E`, type `phase-record` |
| **Landing scope** | **exactly four paths**; no fifth path touched |
| **Reserved home** | **absent** |
| **Pending ledger** | **byte-identical** |
| **Scanner and allowlist** | **byte-identical** |

### 7.1 A pre-landing observation, kept because it is instructive

**At candidate stage — this record on disk, registry mutation deliberately forbidden — the suite failed exactly once.** `tests/test_repo_state.py::RegistryConsistency::test_every_in_scope_governance_file_has_an_entry` globs **on-disk** `.md` files under the in-scope governance directories and requires each to carry a registry entry. **A governance record present without its entry is precisely what that check exists to catch**, so it fired correctly. Isolation confirmed it was the only cause: with this record set aside, the candidate suite was **527 passed, 9 skipped, 577 subtests, zero failures**.

**No check was weakened, suppressed, skipped, allowlisted or edited to hide it.** It was reported and left failing until the registry entry landed **with the record in this same commit**, which is where the check is designed to be satisfied. **The table above is the governing result; the candidate-stage figures are history and are not the final state.**

## 8. Negative controls — every accepted limb exercised

**Every negative control is asserted in a direction that causes the test to fail if the mutant is accepted; the assertion form varies according to the predicate.** A boolean predicate is controlled with `assertFalse`; **T1's checker is controlled by asserting that the mutant produces the specific disagreement** — and in the two compensating-error cases, the exact disagreement set; **T3's is controlled by asserting a cycle appears.** **Green therefore proves the controls bite.**

| Obligation | Limbs exercised |
|---|---|
| **T1** | nine mutants, every one fed through the **same** integrity checker: stated total diverges · **compensating level errors that preserve the total** · **compensating nested errors that preserve the level** · final field displaced · precedence claim contradicted · standing check moved out of place · nullable row dropped · nullable position naming no declared field · vocabulary enumerated twice differently |
| **T2** | six unlisted mutant keys rejected by the closed set · both source-drift anchors |
| **T3** | planted self-hash injected into the **source-derived** graph and detected |
| **S1 / U1** | planted path under the home · planted allowlist row |
| **S2** | unlisted record · listed record absent · missing hash · hash mismatch — all four over **neutral relation inputs**, plus a structural check that the predicate indexes no named field |
| **T4** | one capture missing · undeclared extra capture |
| **T5** | ceiling absent · ceiling changed · a field after the ceiling |
| **T7** | routed outcome with routing false; reverse confirmed lawful |
| **T8** | says clean but carries a finding · says flagged with none |
| **T9** | GER identifier · class-home path · capture address · finding address |
| **U2** | breach non-landable under **each** of the three dispositions |
| **U3** | extra key · non-integer · bool rejected as int · non-positive · string-bearing shape · out-of-range coordinate |
| **U4** | `open` · `routed_for_public_safety_review` · `withheld_from_publication` **each** non-landable, **and** an out-of-set value rejected |
| **U5** | reference absent |

**T9's re-authoring and paraphrase limb is deliberately not mechanised.** It remains **T6, review-only.**

**No negative control is an example GER or specimen.** No capture-payload prose, no local wordlist term, no generated-evaluation directory. Controls are variant-label sets, field-name sequences, disposition tokens, capture references, integer lengths, booleans and enum values.

## 9. Anti-vacuity contract

**A green run of the module never establishes:** that a generated-evaluation record exists · that a manifest exists · **that any record-dependent debt has been discharged merely because there are no records** · that model contact occurred or is authorised · that a specimen exists or is authorised · that generated output was imported · that a harness exists · that any evaluation result is correct · that anything is safe, clinically valid, approved, production-ready or authoritative · **that Part Q has been resolved** · that W7-D3 is open.

**Two tests make the distinction mechanically visible:** one asserts the record count under the reserved home is **zero**, the other asserts the module's own docstring still carries the debt language — so the distinction cannot be quietly deleted while the suite stays green.

## 10. Tier 3 reconciliation

**The convention's trigger is *"required-but-not-yet-runnable"***, and its stubs are `@pending`-decorated and body-less. **E's ten debt predicates run**: they test rule machinery and control behaviour, not an absent subject.

**Live precedent confirms this is the corpus's practice.** ADR-0046's P3–P6, ADR-0047's Q4, ADR-0049's T4/T5/T7/T8/T9 and ADR-0050's U2–U5 are all landed record-level debts and **none acquired a ledger row**; the ledger's nine skips are the W1–W6 lineage. **W7 obligation debts are carried in their records' proof tables.**

**Accordingly: the debts remain outstanding · the predicate tests are runnable tests of rule machinery, not passing tests of an absent subject · they do not masquerade as discharged obligations · review-only duties become neither tests nor skips · and no existing pending-ledger row is converted, removed or touched.** `tests/test_pending_ledger.py` is **byte-identical**.

## 11. Review-only duty register

**Carried forward as human duties. This record closes none of them.**

| Duty | Source | The question no machine answers |
|---|---|---|
| **P2** | ADR-0046 | Was the external authority named anywhere? |
| **Q3** | ADR-0047 | Did model contact occur? |
| **R7** | C lineage | Was a permitted field abused to perform a barred function? |
| **S3** | ADR-0048, disposed here | Did a landed capture's text change after landing? |
| **S4** | ADR-0048 | Does the home still signal its risk class; is the manifest still an index? |
| **T6** | ADR-0049 | Semantic absence and laundering, including T9's re-authoring limb |
| **U6** | ADR-0050 | Was a human public-safety judgement substantively right? |

**None is a test, a skipped test, a TODO, a failing placeholder or a pending-ledger row.**

## 12. Unresolved seams, carried and not closed

1. **ADR-0050's Part Q publication seam — untouched and unresolved.** Under the resulting law a capture producing a scan finding cannot be published as a GER. **No predicate here resolves, narrows or implies resolution of it, and no fourth disposition was added.**
2. **The `local-wordlist` coordinate seam — untouched.** U3 validates a `character_start` when one is supplied; it neither supplies nor can supply one for a `local-wordlist` finding. **The seam stays exactly where ADR-0050 left it.**
3. **S3's dependence on unresolved identity/lifecycle semantics** — §3, newly characterised with evidence, not newly created.

## 13. What this landing does and does not do

**All five W7-D2 components are accepted in this local landing:** the opening brief (`W7-D2-RSB`), **ADR-0048**, **ADR-0049**, **ADR-0050**, and this proof completion record. **W7-D2's five landings are complete in the local accepted sense.**

**Completion becomes effective on publication and remote verification, and not before.** On publication and remote verification of this landing, **W7-D2 satisfies its opening brief's completion condition**, and ADR-0047 **precondition 6** — *the generated-output record shape exists and is accepted* — **is thereby discharged.** **This record claims no remote completion**: at the time of writing, this landing is local and unpushed, and publication is a separate governed act.

**Preconditions 2, 3 and 7 remain outstanding**: the applicable Tier F crossing is W7-D3's, the named first-contact gate belongs to the brief of whichever deliverable would perform contact and **no such gate is named anywhere**, and the harness binding is W7-D4's.

**W7-D3 remains unopened and no model may be contacted.**

**Completion of W7-D2 is SHAPE COMPLETION, not class activation.** A reserved home, a field law, a finding mechanism and a green proof module authorise nothing: no directory, no schema, no manifest, no record, no identifier, no specimen, no contact.

## 14. What does not exist

**No `governance/generated-evaluation/` directory · no schema file · no manifest · no generated-evaluation record · no `GER-####` identifier allocated · no authored specimen · no generated output produced or imported · no harness built or bound · no dependency added · no model contacted · no ADR-0051 allocated or reserved · no W7-D3 artefact.** The pending ledger, the scanner and the allowlist are byte-identical to the baseline.

---

*The proofs are green and the debts are still owed, and this record refuses to let the first fact be read as the second. Five obligations had subjects and were proved. Ten have machinery that bites at nothing, because there is nothing yet to bite. Four are waiting on a person — and one of those, S3, is waiting because a throwaway repository showed a check passing while the law it claimed to enforce was being broken.*
