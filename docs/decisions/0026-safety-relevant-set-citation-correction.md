# 0026 — Safety-Relevant Set Citation Correction (ADR 0002)

**Status:** Accepted by human reviewer, 2026-08-14. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 · **Deliverable:** none — **this record is not a W5 deliverable and creates no W5 planning slot.**
**Decision mode:** correction record, on the ADR 0021 / ADR 0022 / ADR 0023 precedent — an accepted record was found to assert a fact about another accepted record that is not true, discovered by drafting rather than by review, and corrected through ceremony rather than by edit.
**Constitutional references:** **none amended.** W0 §7 is untouched in body, registry entry and hash.
**Corrects:** one clause in **ADR 0002 §"The intensity ladder"**, at its `Safety-relevant means, initially:` definition.
**Holds:** the safety-set reconciliation record, and every unit downstream of it, until this record is published and independently remote-verified.

---

**One record said its list was the same as the Constitution's. It is not — six members against five. This record corrects the sentence that claimed sameness. The list itself is neither touched nor judged.**

## Decision question

ADR 0002 defines its safety-relevant set as *"allergies, medications, diagnosed conditions, injuries, pregnancy status, and clinician instructions — the same high-stakes set W0 §7 requires individual confirmation for."*

**W0 §7's high-stakes list has five members and does not include injuries.**

**Is ADR 0002's set wrong, or is the claim about its provenance wrong — and what is the minimal governed correction?**

## Context

The defect surfaced while drafting the safety-set reconciliation record, which had to establish what each accepted use of "safety-relevant" governs before DR-W5-02 could express runtime consequence for expired safety-relevant items. **Drafting could not reconcile the sets while one record asserted they were identical.** Work stopped for a correction rather than reading the claim into something more convenient. **That is the ADR 0022 and ADR 0023 pattern exactly.**

The measured facts, read live from the published corpus:

| Fact | Finding |
|---|---|
| W0 §7's high-stakes list | *"**High-stakes fields require individual confirmation**, one item at a time: allergies, medications, diagnoses/conditions, pregnancy status, and clinician instructions."* — **five members** |
| Where it sits in W0 | **Review-fatigue controls (binding)**, item 2 — a control on **approval** |
| ADR 0002's list | allergies, medications, diagnosed conditions, **injuries**, pregnancy status, clinician instructions — **six members** |
| Relationship | ADR 0002's six is **W0 §7's five plus injuries** — a proper superset, not an identity |
| Occurrences of the claim in ADR 0002 | **Exactly one**, in the `Safety-relevant means, initially:` definition |
| Occurrences anywhere else in the corpus | **None.** A sweep of `docs/`, `governance/` and `scripts/` for `same high-stakes` and `high-stakes set` returns no other instance. **The defect does not propagate** |
| ADR 0002's registry `role` field | Does not restate the claim — **no registry role edit is required** |
| ADR 0002's current errata | `[]` — this would be its first |

## Controlling law

- **Checklist rule 2** — material or semantic changes require a decision record, never an edit; non-semantic corrections require a logged erratum in the affected document's registry entry, in the same commit as the correction; **the semantic judgment belongs to the human reviewer, and when in doubt it is material.**
- **Checklist rule 3 — registry atomicity.** Document change, registry entry, and hash recomputation move together.
- **ADR 0003** — ceremony tiers; this is **Tier J**.
- **ADR 0021 / ADR 0022 / ADR 0023 precedent** — a correction record restating the corrected text, the corrected source keeping a narrow edit with a logged erratum, and dependent work suspended until publication.
- **W0 §7** — the high-stakes list and its review-fatigue framing, **quoted here and amended nowhere.**

## Decision

1. **The defect is confirmed and named.** ADR 0002 asserts that its six-member safety-relevant set is *"the same high-stakes set W0 §7 requires individual confirmation for."* **W0 §7's list has five members and does not include injuries.** The assertion is false as written.

2. **ADR 0002's six-member set is not adjudicated by this correction and is not changed.** Its membership remains exactly as accepted. This record neither validates nor re-justifies any member; it corrects only the false statement that the six-member set is identical to W0 §7's five-member list.

3. **W0 §7 is not amended, and amending it is expressly forbidden here.** Adding injuries to the Constitution's review-fatigue control to make a later record's citation true would be **editing the Constitution to fit a footnote**, and would silently change what the user must individually confirm at approval. **The citation is the thing that is wrong.**

4. **Exactly one correction is authorised, and no other.**

   **`docs/decisions/0002-safety-surfacing.md`, the `Safety-relevant means, initially:` definition**

   | | |
   |---|---|
   | From | `injuries, pregnancy status, and clinician instructions — the same high-stakes set W0 §7 requires individual confirmation for.` |
   | To | `injuries, pregnancy status, and clinician instructions — W0 §7's five high-stakes fields for individual confirmation, together with injuries.` |

   **No other clause, sentence, table, row, doctrine, or word in ADR 0002 is touched.** The following sentence — *"Extending the set is a future decision, not a runtime judgment"* — stands unchanged.

5. **The pointer `W0 §7` is correct and must not be "sharpened".** **W0 §7 has no numbered subsections.** Its `## 7. Health Profile Agent Boundary` contains an unnumbered *"Review-fatigue controls (binding)"* list, and the high-stakes sentence is item 2 of it. **The whole corpus — W1-D3, W1-D5, the W1 data-boundary map, and ADR 0002 itself — addresses this material as `W0 §7`.**
   **A `§7.2` address does not exist**, and an earlier draft of the reconciliation work used one. **Changing `§7` to `§7.2` would replace a correct pointer with a fabricated one, and is forbidden.** Where finer precision is wanted, the lawful form is *W0 §7, review-fatigue control 2*.

6. **Explicitly forbidden, and forbidden permanently:**
   - **No member may be added to or removed from ADR 0002's set** by this record.
   - **No change to the L0–L3 ladder, the per-case table, the four doctrines, or the language law.**
   - **No amendment to W0 §7 or to W1-D3 §6.3**, in body, registry entry, erratum or hash.
   - **No canonical merged set is created**, and no statement is made here about which set governs which layer. **That is the reconciliation record's question, and this record deliberately does not answer it.**
   - **No sharpening of the `W0 §7` pointer**, per decision 5.
   - **No silent reinterpretation.** The claim is not read into meaning "overlapping"; the defect is named and corrected in ink.

7. **The correction is material, and the source edit is narrow.** **Ruled: the change is material**, so under checklist rule 2 it lands as a **correction decision record**, with ADR 0002 receiving the single narrow edit above, **logged as an erratum in its registry entry with the content hash recomputed atomically in the same commit.** ADR 0002 currently carries `errata: []` and gains its first.
   **The basis for materiality, recorded so it is not re-argued.** ADR 0023's source edits relocated a pointer; **this edit corrects a factual claim about another document's content.** It imposes no obligation and removes none, and it changes no set, ladder, doctrine or table — but a reader relying on the original sentence understood the surfacing set to be constitutionally fixed, and after correction understands it to differ from the constitutional list. **That is a change in what the record conveys**, and rule 2's tiebreak — *when in doubt it is material* — resolves it accordingly.

8. **Atomicity.** Per checklist rule 3, this record, the ADR 0002 source correction, its registry erratum, its recomputed content hash, and the registry index update land as **one atomic landing**, enumerated and authorised by its own landing-scope pass.

9. **Dependent work is held until publication and remote verification.** **The safety-set reconciliation record remains unaccepted and unlanded**, and **DR-W5-02 remains undrafted**, until this record is published on `origin/main` and that authority is independently verified against the remote. The ordering is settled: **correction first, reconciliation second, separate ceremonies.**

10. **No wider citation audit is opened.** This defect was found by drafting, and **a sweep of the corpus for other records asserting identity between lists is expressly not authorised here.** The targeted sweep reported in the context table establishes only that *this* claim does not propagate. Any broader audit is its own authorised unit with its own brief.

11. **Classification is frozen: `phase: W5`, `deliverable: null`, `implementation_permission: none`** — the ADR 0023 shape. **This record is not a W5 deliverable, creates no W5 planning slot, and authorises no capability.** W5 is already open, so no opening question arises.

12. **No decision-record number is reserved.** This record takes the next global ADR number derived from the live registry at landing-scope time. **ADR 0025 is occupied; nothing is reserved for the reconciliation record**, which is numbered afterwards from the then-live registry.

## Governance and constitutional check

- **No law is touched, reinterpreted, or amended.** The record corrects a claim about a law, not the law.
- **No new authority.** No set member, label, class, authority state, edge, permission or namespace is minted.
- **No substance changes in ADR 0002.** Every doctrine, ladder level, per-case row, prohibition and open question stands exactly as accepted.
- **Checklist rule 2 is honoured in both directions:** treated as material and landed as a decision record; the source receives one narrow edit with a logged erratum.
- **Checklist rule 3 is honoured** by the atomic landing of decision 8.
- **Checklist rule 8 is untouched** — not a phase-entry document, satisfies no gate leg.
- **The W1 corpus remains binding baseline.** ADR 0002 is a W1 record; this record corrects one clause within it under the governance W1 itself established, exactly as ADR 0023 did for W1-D5 and W1-D6.

## Alternatives considered

- **A correction record with one narrow authorised erratum (chosen).** Matches the established shape for this failure class, keeps the substantive restatement reviewable, and leaves ADR 0002 minimally touched.
- **Erratum alone, no correction record (rejected, ruled).** Defensible, since no obligation moves — but a published record currently asserts something false about the Constitution, and rule 2's tiebreak resolves doubt toward material.
- **Amending W0 §7 to add injuries (rejected firmly).** It would edit the Constitution to make a later record's sentence true, and would silently widen what the user must confirm individually at approval.
- **Altering ADR 0002's membership in either direction (rejected).** Adding to or removing from the set to make a citation true would be **changing an accepted safety mechanism to fit a sentence about it**, and unlike the citation fix it would carry behavioural consequence, since the set drives the surfacing ladder. **This is a reason not to touch membership here — not a finding about what the membership should be.**
- **Also stating the layering in the corrected clause (rejected, ruled).** A fuller wording — *"The sets are related, not identical: W0 §7's governs approval, this one governs surfacing"* — is accurate, and would close the category conflation in the same act. **It is rejected as pre-emptive of the reconciliation record**, which is ruled to come second and has not been accepted. **The category conflation therefore survives this correction and is closed only when the reconciliation record lands** — a known and accepted cost of the ordering.
- **Leaving it and letting the reconciliation record note the discrepancy (rejected).** It would publish a reconciliation resting on a source it simultaneously reports as false, for as long as that lasted.

## Consequences

- **The reconciliation record becomes writable** without having to argue against an accepted sentence.
- **One landing is inserted before it**, delaying the reconciliation and DR-W5-02. Accepted deliberately: publishing on top of a known-false claim to save a ceremony round is the trade the corpus has consistently refused.
- **ADR 0002 gains its first erratum**, and its content hash moves for the first time since acceptance — which is what the hash discipline exists to make visible.
- **The corrected sentence is more informative than the original**, since it names the difference (injuries) instead of asserting sameness.
- **No behavioural, evaluative, or capability consequence whatsoever.** No set changes; nothing about the Wing's behaviour moves.

## Non-goals

This record does not: add to or remove from any safety-relevant or high-stakes set; amend W0, W1-D3, ADR 0020 or ADR 0025; alter ADR 0002's ladder, per-case table, doctrines, language law or open questions; create a canonical merged set; decide which set governs which layer; sharpen the `W0 §7` pointer; open any wider citation audit; accept, land or pre-decide the reconciliation record; draft DR-W5-02; touch the pending ledger, Lane C, the fixture corpus, or the engine; open W6; or authorise any implementation, directory, dependency, model contact, payload, transmission, harness or fixture execution. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — user, Wing, room, record, set, ladder, human reviewer, architect. **The item names appearing here are the accepted corpus's own governance vocabulary**, quoted from W0 §7 and ADR 0002. **No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person.** No private names, no model or vendor names, no project lineage beyond this repository, no URLs, no placeholder tokens.

## Dependencies

**W0** (§7's high-stakes list, quoted and unamended); **ADR 0002** (the corrected source); W2-D3 (checklist rules 2 and 3); ADR 0003 (ceremony tiers); ADR 0021, ADR 0022 and ADR 0023 (the correction-record and erratum precedent). **The safety-set reconciliation record depends on this one and may not proceed past it until it is published.**

## Open questions

**None at acceptance.** The three points previously put to the reviewer are now ruled: **the wording** is decision 4's, with the fuller layering wording rejected as pre-emptive; **materiality** is settled at material, per decision 7; and **the classification** is frozen, per decision 11. The decision-record number remains derived from the live registry at landing scope, and the exact atomic file set is derived by measured landing scope — both are landing-scope mechanics rather than open questions.

---

*The pointer was right and the list is left exactly where it was found. The only thing corrected is a claim of sameness that nobody had counted — six against five, sitting in the corpus since W1, in the one record that decides how loudly the Wing may say it is unsure.*
