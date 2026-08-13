# 0023 — AIAdapter Import-Citation Correction (W1-D5 §8, W1-D6 §9.4)

**Status:** Accepted by human reviewer, 2026-08-13. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 · **Deliverable:** none — **this record is not a W5 deliverable, and its publication does not open W5.**
**Decision mode:** correction record, on the ADR 0022 precedent — an accepted requirement was found unsatisfiable as written, by drafting work rather than by review, and is corrected through ceremony rather than by edit.
**Constitutional references:** none amended. W0 Open Question 10 (identity verification for connected AI systems) is the question the corrected obligation serves; no law is touched.
**Corrects:** the AIAdapter import citation in **W1-D5 §8** and **W1-D6 §9 item 4**.
**Holds:** DR-W5-01 and every dependent W5 unit, until this record is published and independently remote-verified.

---

**A citation promised two rows and the shelf held one. The missing row turns out never to have been needed — the zone it would have described was bound to another zone's rules from the first day — but the corpus was still telling a future record to fetch something that is not where it says it is. This record moves the pointer and touches nothing else.**

## Decision question

Two accepted W1 records instruct the future AIAdapter ADR to import *"Z3/Z5 rows"* from the threat model. **The threat model contains a Z3 row and no Z5 row.** The obligation is therefore partly unsatisfiable as written.

**Is a threat-analysis row missing, or is the pointer wrong — and what is the minimal governed correction either way?**

## Context

The defect surfaced while drafting DR-W5-01, the AIAdapter / Processing-Context Boundary record, which is the record both citations address. Drafting could not discharge the obligation as literally written, and stopped rather than reading the citation into something more convenient. **That is the ADR 0022 pattern exactly:** implementation meeting doctrine, doctrine turning out to be defective, and the work halting for a correction instead of coding around it.

The measured facts, read live from the published corpus:

| Fact | Finding |
|---|---|
| Literal `Z5` in W1-D5 | **Exactly one occurrence**, at §8 — **inside the citation itself** |
| Literal `Z5` in W1-D6 | **Exactly one occurrence**, at §9 item 4 — **inside the citation itself** |
| W1-D5 §4 rows naming a zone | Z1 edge, Z2, **Z3**, **Z4** — **no Z5 row** |
| W1-D5 §3 assets naming a zone | *"AI processing payloads (transient, **Z3**)"*; *"Vendor/adapter disclosure payloads (**Z4**)"* — **no Z5 asset** |
| Where Z5 is defined | **W1-D1 §1** — *"**Z5 — Connected AI systems** \| External AI systems behind an `AIAdapter` \| Only via Z3 rules; connection model deferred to the AIAdapter ADR (resolves OQ 10)"* |

## Controlling law

- **Checklist rule 2** — material or semantic changes require a decision record, never an edit; non-semantic corrections require a logged erratum in the affected document's registry entry, in the same commit as the correction; **the semantic judgment belongs to the human reviewer, and when in doubt it is material.**
- **Checklist rule 3 — registry atomicity.** Document change, registry entry, and hash recomputation move together.
- **ADR 0003** — ceremony tiers; this is Tier J.
- **ADR 0021 / ADR 0022 precedent** — a correction record restating the corrected requirement, with the corrected source keeping a non-semantic pointer and a logged erratum, and dependent work suspended until publication.
- **W1-D1 §1 and §5** — the Z5 zone definition and E12's reservation, both correct and both unamended by this record.

## Decision

1. **The defect is confirmed and named.** W1-D5 §8 and W1-D6 §9 item 4 each instruct the AIAdapter ADR to import *"Z3/Z5 rows"* from W1-D5. **W1-D5 contains no Z5 row and never has.** The obligation cannot be discharged as literally written.

2. **No Z5 threat-analysis row is missing. The corpus is substantively complete, and the defect is confined to the pointer.** Four independent reasons, each from the live sources:
   - **W1-D1 §1 gives Z5 no independent plaintext regime** — its permission column reads *"Only via Z3 rules."* A zone with no rules of its own presents no distinct boundary behaviour for a boundary table to describe.
   - **W1-D5 §4 is a table of boundaries, not of zones.** Its rows are crossings, and **a Z5 crossing is an AI-processing crossing** — already described by the Z3 row it inherits.
   - **W1-D5 §3's asset list is consistent with that**: transient Z3 payloads and Z4 disclosure payloads are named; no Z5 asset exists, because there is no distinct Z5 payload class.
   - **W1-D5 §2 places AIAdapter work out of scope** in terms, so the document deliberately declined to model the connection.
   **No gap is being papered over. Nothing is added to the threat model by this correction.**

3. **The corrected import obligation, restated in full.** The AIAdapter ADR must **import the following wholesale**: **W1-D5 §4's Z3 boundary row**, and **the Z5 zone definition in W1-D1 §1**. **The obligation's strength and subjects are unchanged** — the same two zones are named; only the location of the second is corrected. Nothing is added to the obligation and nothing is removed from it.
   **The corrected wording places *wholesale* ahead of the list so that it governs every item unambiguously**, closing a reading in which a trailing *wholesale* might be taken to qualify only the last-named subject. That is a clarity correction to the same obligation, not a change of scope.
   **The residuals OR-1, OR-2 and OR-3 are deliberately not added to the obligation.** Adding them would widen it. The Z3 boundary row's reference to OR-2 travels with that row wholesale; **the OR-2 residual text itself is not thereby added to the corrected mandatory import.** **DR-W5-01 may cite OR-1, OR-2 and OR-3 independently**, as any record may import more than it is required to.

4. **Exactly two corrections are authorised, and no others.**

   **(a) `docs/architecture/W1-D5-threat-model.md` §8**
   | | |
   |---|---|
   | From | `the AIAdapter ADR (E12 — which must import this threat model's Z3/Z5 rows wholesale)` |
   | To | `the AIAdapter ADR (E12 — which must import the following wholesale: this threat model's Z3 boundary row and the Z5 zone definition in W1-D1 §1)` |

   **(b) `docs/architecture/W1-D6-evaluation-plan-skeleton.md` §9 item 4**
   | | |
   |---|---|
   | From | `imports D5's Z3/Z5 rows and this document's grammar wholesale` |
   | To | `imports the following wholesale: D5's Z3 boundary row, the Z5 zone definition in W1-D1 §1, and this document's grammar` |

   **No other clause, sentence, table, row, or word in either document is touched.**

5. **Explicitly forbidden, and forbidden permanently:**
   - **No Z5 row may be invented in W1-D5.** A row minted to make a pointer true would be threat analysis written backwards from a citation, and would be a worse defect than the one being corrected.
   - **No Z4 substitution.** Z4 is the non-AI vendor boundary with a different payload rule — *"Minimum task payload only … never health, profile, or contemplative content."* It is not a stand-in for Z5, and treating it as one would blur two boundaries the corpus deliberately separates.
   - **No widening or narrowing of the obligation**, and no weakening of *wholesale*.
   - **No silent reinterpretation.** The citation is not read into meaning something else; the defect is named and corrected in ink.

6. **W1-D1 is not amended.** Its Z5 zone definition and its E12 reservation are correct, are what the corrected citations now point at, and are untouched by this record.

7. **The W5 runway's quotation is preserved intentionally, and `W5-AR` is not touched.** The published W5 runway quotes W1-D5 §8's then-current wording in its authority list. **That quotation is accurate acceptance-time evidence of what the source said when the runway was accepted — it is historical evidence, not a defective source instruction**, and it carries no obligation of its own. **No `W5-AR` body edit, no registry erratum, and no content-hash change is made or authorised**, and none is required: the runway is not a source of the import obligation, and correcting a quotation of the past would falsify the record of what was quoted. This preservation is deliberate, and it follows the corpus's established treatment of acceptance-time statements — the room contracts' *"No fixture currently exists or is implied"* sentences were likewise never edited to track later state.

8. **The two source edits are non-semantic pointer corrections, authorised by this record.** Following the ADR 0021 / ADR 0022 pattern: **the correction lands as a decision record; the sources receive only the narrow pointer edits above, each logged as an erratum in its own registry entry, with the content hash recomputed in the same commit.** Both `W1-D5` and `W1-D6` currently carry `errata: []`; each gains its first.

9. **Atomicity.** Per checklist rule 3, this record, both source corrections, both registry errata, both recomputed content hashes, and the registry index update land as **one atomic landing**, enumerated and authorised by its own landing-scope pass.

10. **Dependent work is held until publication and remote verification.** **DR-W5-01 remains unaccepted and unlanded**, and no dependent W5 unit proceeds, until this record is published on `origin/main` and that authority is independently verified against the remote. This carries the ADR 0022 precedent, where the dependent lane *"remained suspended until this record was published."*

11. **This record does not open W5, and it is not a W5 deliverable.** It authorises no capability, no implementation, no directory, no dependency, no model contact, no payload, no fixture execution. **W5 becomes effectively open only when the first W5 deliverable is published and remote-verified**, and this record is not that deliverable. **Its classification is frozen: `phase: W5`, `deliverable: null`, `implementation_permission: none`.** The precedent supports each part precisely and no further: **`W5-AR` proves that `phase: W5` with `deliverable: null` may publish without opening W5** — and nothing more, since **`W5-AR` itself carries `implementation_permission: future-governed`, not `none`.** **`none` follows instead from this record authorising no implementation, and from the ADR and correction-record treatment** — ADR 0021 and ADR 0022 both carry `none`.

12. **No wider citation audit is opened.** This defect was found by drafting rather than by review, and **a sweep of the corpus for other citations naming containers that do not exist is expressly not authorised here.** Such a sweep, if ever wanted, is its own authorised unit with its own brief and ceremony — never a side effect of a correction.

13. **No decision-record number is reserved for anything.** This record takes the next global ADR number as derived from the live registry at landing-scope time. **`ADR-0023` is not reserved for DR-W5-01**, and if this correction consumes it, DR-W5-01 is renumbered afterwards from the then-live registry.

## Governance and constitutional check

- **No law is touched, reinterpreted, or amended**, and no constitutional amendment is proposed or required. The record corrects a reference.
- **No new authority.** No edge, class, authority state, consent form, permission, or namespace is minted. **E12 remains reserved.**
- **No substance changes in either corrected source.** Every threat row, residual, asset, principle, category and test obligation stands exactly as accepted.
- **Checklist rule 2 is honoured in both directions:** the change is treated as **material** and lands as a decision record rather than an edit; the source edits it authorises are **non-semantic pointer corrections** with logged errata, which is the shape rule 2 provides for.
- **Checklist rule 3 is honoured** by the atomic landing of decision 9.
- **Checklist rule 8 is untouched** — this is not a phase-entry document and satisfies no gate leg.
- **The W1 corpus remains binding baseline.** This record does not reopen W1; it corrects two pointers within it under the same governance W1 itself established.

## Alternatives considered

- **A correction record with narrow authorised errata (chosen).** Matches ADR 0022's shape for the same failure class, keeps the substantive restatement in a reviewable record, and leaves the sources minimally touched.
- **Errata alone, with no correction record (rejected, on the reviewer's ruling).** Defensible — the change is referential — but the current text imposes an obligation that **cannot be discharged as written**, and making an unsatisfiable requirement satisfiable is close enough to substantive that rule 2's own tiebreak resolves it toward material.
- **Adding a Z5 row to W1-D5 (rejected).** It would invent threat analysis to satisfy a citation, and W1-D1 already explains why no such row is needed.
- **Reading the citation as meaning the Z4 row (rejected).** Z4 is a different boundary with a different payload rule; the substitution would blur a separation the corpus makes deliberately.
- **Letting DR-W5-01 carry the discrepancy and correcting later (rejected).** It would publish a record asserting it discharged an obligation whose text it simultaneously reports as defective — a known inconsistency in the corpus for as long as it lasted.
- **Correcting W1-D5 only, letting W1-D6 inherit (rejected as unsafe).** W1-D6 `depends_on` W1-D5, so an inheritance reading is arguable — but W1-D6 states the obligation in its own words and would keep stating it wrongly. **Both are corrected explicitly.**

## Consequences

- **The obligation becomes dischargeable**, and DR-W5-01 can cite it without also reporting it as defective.
- **One landing is inserted before DR-W5-01**, which **delays the moment W5 becomes open**. That cost is accepted deliberately: publishing a known-defective citation to save a ceremony round is the trade the corpus has consistently refused.
- **Two W1 documents gain their first errata**, and their content hashes move for the first time since acceptance — which is exactly what the registry's hash discipline exists to make visible.
- **A precedent is reinforced, not created:** a defect found by drafting is corrected by record, and the dependent work waits.
- **No behavioural, evaluative, or capability consequence whatsoever.** Nothing about the Wing's behaviour changes; a pointer now points where the material is.

## Non-goals

This record does not: add, remove, or alter any threat row, residual, asset, principle, or test obligation; amend W1-D1; **touch `W5-AR` in body, registry entry, erratum, or hash**; **open any wider citation audit**; invent a Z5 row; substitute Z4 for Z5; **add OR-1, OR-2 or OR-3 to the corrected obligation**; change the strength or subjects of the import obligation; accept, land, or pre-decide DR-W5-01; open W5 or W6; authorise any implementation, directory, dependency, model contact, payload, transmission, harness, or fixture execution; touch the pending ledger, Lane C, the fixture corpus, or the engine; or reserve any decision-record number for any future record. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic wording throughout — user, Wing, room, zone, boundary, adapter, recipient, human reviewer, architect, model. No private names, no model or vendor names, no project lineage beyond this repository, no URLs, no real health data, no clinical examples, and no placeholder tokens. The record discusses a citation and two document locations; it describes no person and no content.

## Dependencies

W0 (Open Question 10, as the question the corrected obligation serves); W1-D1 (the Z5 zone definition and E12's reservation, both unamended); **W1-D5** and **W1-D6** (the corrected sources); W2-D3 (checklist rules 2 and 3); ADR 0003 (ceremony tiers); ADR 0021 and ADR 0022 (the correction-record and pointer-erratum precedent). **This record depends on no W5 record, and no W5 record may proceed past it until it is published.**

## Open questions

**None at acceptance.** The three questions this record raised in draft are resolved by the decisions above: the published W5 runway's quotation is **preserved intentionally as acceptance-time evidence** and `W5-AR` is untouched (decision 7); the **classification is frozen** at `phase: W5`, `deliverable: null`, `implementation_permission: none` (decision 11); and **no wider citation audit is opened** (decision 12). The decision-record number remains derived from the live registry at landing scope, which is a landing-scope mechanic rather than an open question.

---

*The smallest correction in the corpus so far: two clauses, same subjects, same strength, one location fixed. It costs a landing and a delay to the phase's opening, and it is still cheaper than a published record that cites an obligation it cannot meet.*
