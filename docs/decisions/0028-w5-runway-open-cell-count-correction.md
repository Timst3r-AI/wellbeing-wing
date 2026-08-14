# 0028 — W5 Runway Open-Cell Count Source-Fidelity Correction

**Status:** Accepted by human reviewer, 2026-08-14. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 · **Deliverable:** none — **not a W5 deliverable, and it creates no W5 planning slot and no W5-D1 identity.**
**Decision mode:** correction record, on the ADR 0021 / ADR 0022 / ADR 0023 / ADR 0026 precedent — an accepted record was found to assert a countable fact about other accepted records that is not true, discovered by drafting rather than by review, and corrected through ceremony rather than by silent or unlogged edit.
**Constitutional references:** **none amended.** No law is engaged, touched or reinterpreted.
**Corrects:** one sentence in **`W5-AR` §6.1**.

---

**A runway said six where the table holds five. The miscount is one word old, it has been wrong since the day the runway was accepted, and it sits in the sentence that tells a future record how much of the corpus it must answer for. Nothing about behaviour changes here. A number that never matched anything is made to match.**

## Decision question

W5-AR §6.1 states that **six** behaviour-table cells in every room contract read `Open (§10.6)`. **The shared behaviour table carries that token on five of its six rows.**

**Is a cell missing, or is the count wrong — and what is the minimal governed correction?**

## Context

The defect surfaced while drafting **DR-W5-02**, the record W5-AR §6.1 assigns the §10.6 question to. DR-W5-02 needed to say which cells its disposition governs, and the count could not be reconciled with the contracts. Drafting stopped rather than reading the number into something more convenient. **That is the ADR 0022, ADR 0023 and ADR 0026 pattern exactly:** work meeting doctrine, doctrine turning out to be defective, and the work halting for a correction instead of writing around it.

**A corpus-wide sweep was run before this record was drafted**, over all 141 tracked files plus every `registry.json` field. `Six behaviour-table cells` returns **exactly one occurrence**, at `W5-AR` §6.1. `six behaviour-table cells`, `six cells in every room contract` and `six room-contract cells` return **zero**. **No registry role, room contract, ADR or test fixture repeats the false count.** The correction scope is therefore one sentence in one file, and no other governed copy is silently left behind.

## Controlling law

- **Checklist rule 2** — material or semantic changes require a decision record, never an edit; non-semantic corrections require a logged erratum in the affected document's registry entry, **in the same commit as the correction**; the semantic judgment belongs to the human reviewer, and when in doubt it is material.
- **Checklist rule 3 — registry atomicity.** Document change, registry entry, and hash recomputation move together.
- **Checklist rule on landing enumeration** — *"Discovering a needed file mid-landing is a review question, not an improvisation."*
- **ADR 0003** — ceremony tiers; this is **Tier J**.
- **ADR 0021 / ADR 0022 / ADR 0023 / ADR 0026 precedent** — a correction record restating the corrected text, the corrected source taking a narrow edit with a logged erratum, and dependent work suspended until publication.
- **ADR 0020** — the shared behaviour table, whose row structure is the evidence, and which is **not amended**.

## The evidence

| Measurement | Value | Source |
|---|---|---|
| ADR 0020 shared-table numbered rows | **6** | `docs/decisions/0020-…` |
| Rows containing `Open (§10.6)` | **5** — rows **2, 3, 4, 5, 6** | same |
| Row 1, **Current** | **does not** contain it | same |
| Gym contract behaviour-table cells | **5** | `docs/rooms/gym-room-contract.md` |
| Kitchen contract behaviour-table cells | **5** | `docs/rooms/kitchen-room-contract.md` |
| Meditation contract behaviour-table cells | **5** | `docs/rooms/meditation-room-contract.md` |
| Wellness contract behaviour-table cells | **5** | `docs/rooms/wellness-room-contract.md` |
| **Total behaviour-table cells** | **20** | 5 × 4 |
| Wellness additional **prose** occurrence | **1** — a fidelity-note line, not a table cell | `docs/rooms/wellness-room-contract.md` |
| **Total textual occurrences** | **21** | 20 cells + 1 prose |

1. **Row 1 carries no `Open (§10.6)` cell because a current item raises no block-versus-warn question.** The token appears only where context is review-due, stale, expired, contradicted or unknown. **Five affected rows, propagated verbatim into all four contracts.**

2. **Twenty cells and twenty-one textual occurrences are different measurements, and this record keeps them apart.** The corrected sentence counts **behaviour-table cells per contract** — five, true of every contract. It does not count textual occurrences, which are twenty-one because the Wellness contract additionally mentions the token in a fidelity note. **A future reader who greps for the string will find twenty-one and must not read that as contradicting five-per-contract.**

3. **The likely origin of the error, recorded so it does not recur.** ADR 0020's table has **six states** — current, review due, stale, expired, contradicted, unknown — and that correct six appears throughout the corpus, including in two room contracts' fidelity notes and two test-grammar entries. **The runway's sentence appears to have carried the six states across to the cells.** Six states, five cells: both counts are right about different things.

4. **The sentence was already false when W5-AR was accepted.** The four contracts were measured at W5-AR's own landing commit and at current authority: **5 / 5 / 5 / 6 occurrences in both cases, identical.** **This is not later drift, and no intervening change made a true statement false.**

## Decision

1. **The defect is confirmed and named.** W5-AR §6.1 asserts six behaviour-table cells per room contract; there are five. The assertion is false as written, and was false at acceptance.

2. **No cell is missing, and the room contracts are correct.** The five-row structure is ADR 0020's, deliberately excludes row 1, and is reproduced faithfully in all four contracts. **Nothing is added to any table, and no cell is invented to make a sentence true.**

3. **Exactly one correction is authorised, and no other.**

   **`docs/phases/W5-runway-runtime-enforcement-evaluation.md` §6.1**

   | | |
   |---|---|
   | From | Six behaviour-table cells in every room contract read `Open (§10.6)` and carry the floor only. |
   | To | Five behaviour-table cells in every room contract read `Open (§10.6)` and carry the floor only. |

   **One word. No other clause, sentence, table, row, assignment or obligation in W5-AR is touched.**

4. **This corrects count fidelity only, and nothing else changes.** Explicitly:
   - **ADR 0020's behaviour semantics are unchanged, and ADR 0020 is not amended.**
   - **No room contract is amended**, in body, registry entry, erratum or hash.
   - **W5-AR's assignment of W1-D3 §10.1 and §10.6 to DR-W5-02 is unchanged**, as are its four obligations on that record.
   - **W5-AR's phase structure, deliverable set, and implementation permissions are unchanged**, including its own `future-governed` permission.
   - **The §6.4 floor is unchanged and still binding.**

5. **§10.6 remains open in the historical room-contract cells under current repository authority.** **DR-W5-02 has been accepted in Downloads but is not repository authority**, and acceptance in Downloads is not publication. **This record does not resolve §10.6, does not anticipate its resolution, and confers no authority on any unpublished record.**

6. **This correction does not reverse or contradict ADR 0023, and the distinction is recorded so it is not re-argued.** ADR 0023 decision 7 declined to touch W5-AR, on two stated grounds: that *"the runway is not a source of the import obligation"*, and that *"correcting a quotation of the past would falsify the record of what was quoted."*
   - **That fence was scoped to ADR 0023's own import-citation correction**, not made permanent. Its words are *"no `W5-AR` body edit … is made or authorised"* — an authorisation boundary for that landing.
   - **W5-AR was not the source of that defect.** It **is** the source of this one: the false sentence is W5-AR's own §6.1 text, inside the section that assigns §10.6.
   - **ADR 0023 protected a faithful quotation of another document's then-current wording.** **The present defect is not a quotation at all** — it is W5-AR's own factual assertion about the contracts.
   - **ADR 0023's preservation principle turns on the statement having been accurate when made.** This one was **not**: the contracts read 5 / 5 / 5 / 6 at W5-AR's landing commit, exactly as they do now. **Preserving it would preserve an error, not evidence.**

7. **Explicitly forbidden, and forbidden permanently:**
   - **No cell may be added to any room contract** to make the original count true. A cell minted to satisfy a sentence would be a worse defect than the one being corrected.
   - **No change to ADR 0020's table**, its six states, its row order, or its semantics.
   - **No broadening or narrowing of W5-AR's §10.6 or §10.1 assignment**, and no change to its four obligations on DR-W5-02.
   - **No silent reinterpretation.** The number is not read as meaning something else; the defect is named and corrected in ink.

8. **This is treated as material, and the source edit as narrow.** Under checklist rule 2 the correction lands as a **decision record**, with W5-AR receiving the single one-word edit above, **logged as an erratum in its registry entry with the content hash recomputed atomically in the same commit.** **W5-AR currently carries `errata: []` and gains its first.**
   **This correction applies the governed correction pattern to a `phase-record` body for the first time.** That document type is **not immune from correction**: where its own factual assertion was false when accepted, the correction does not change the governing phase direction, and the source edit, erratum, recomputed hash and correction record move atomically, **in-place correction is lawful**. This record therefore **extends the existing correction ceremony to `phase-record` without creating a special exemption or a new mutation class.**

9. **Atomicity.** Per checklist rule 3, this record, the W5-AR source correction, its registry erratum, its recomputed content hash, the new registry entry, and the registry index update land as **one atomic landing**, enumerated and authorised by its own landing-scope pass.

10. **Measured source-mutation mechanics, recorded for that landing and re-derived here rather than copied.**

    | | |
    |---|---|
    | W5-AR current hash | `sha256:3511e886de883d5adc9fbdf78150bb9ff43c47ef84be1c21d46c662bbfc9a340` |
    | W5-AR corrected hash | `sha256:eb59a69cc8939ebf8506c2c237f1b8052127933d36060fd75633d1a7d38eb295` |
    | Bytes | 36,191 → **36,192** (+1) |
    | Lines changed | **1** (§6.1) · newline count unchanged |

    **Both hashes were recomputed from live bytes while drafting**, and the current hash was confirmed to match W5-AR's live registry entry. **They are re-derived at landing-scope time regardless.**

11. **No implementation, runtime behaviour, model contact, fixture execution or evaluation is authorised**, and no capability of any kind is created.

12. **No wider count audit is opened.** The targeted sweep reported above establishes only that **this** assertion does not propagate. **A general sweep of the corpus for other countable claims is expressly not authorised here**; it would be its own unit with its own brief.

13. **No decision-record number is reserved.** This correction takes the next global ADR number derived from the live registry **and decision directory** at its own landing-scope pass. **Per the governed correction-first sequence, DR-W5-02 does not compete for that number:** after this correction is published and independently remote-verified, DR-W5-02 receives a fresh landing-scope pass and derives its own number from the then-live repository authority.

## Governance and constitutional check

- **No law is touched, reinterpreted, or amended**, and no constitutional amendment is proposed or required. The record corrects a count.
- **No new authority.** No label, class, authority state, freshness state, edge, grant type, namespace or set membership is minted.
- **No substance changes in W5-AR.** Every deliverable, assignment, obligation, gate, seam and permission stands exactly as accepted.
- **Checklist rule 2 honoured in both directions:** treated as **material** and landed as a decision record; the source receives one narrow edit with a logged erratum.
- **Checklist rule 3 honoured** by decision 9's atomic landing.
- **Checklist rule 8 untouched** — not a phase-entry document, satisfies no gate leg.
- **W5 is not reopened, and no phase state changes.** W5 remains open for governed doctrine and brief work; this record neither advances nor retards it.

## Alternatives considered

- **A correction record with one narrow authorised erratum (chosen).** Matches the established shape for this failure class, keeps the restatement reviewable, and leaves W5-AR minimally touched.
- **Erratum alone, no correction record (rejected).** Defensible — a count is referential — but a published record asserts something false about four other accepted records, and rule 2's tiebreak resolves doubt toward material.
- **Leave it, and let DR-W5-02 avoid the number (rejected).** The count would stay false in the corpus, and the next reader would re-derive the same defect. DR-W5-02 has already dropped its own count; the source should not keep one that matches nothing.
- **Adding a sixth cell to each contract (rejected firmly).** It would invent behaviour-table content to satisfy a sentence, and ADR 0020's row 1 correctly carries no such cell.
- **Correcting the sentence to say twenty, or twenty-one (rejected).** The sentence counts cells **per contract**, and "in every room contract" is the accurate frame. Twenty is the cross-contract total and twenty-one is a textual-occurrence count including a prose mention; neither belongs in this sentence.
- **Opening a general count audit (rejected).** Out of scope, and the targeted sweep already establishes non-propagation.

## Consequences

- **DR-W5-02 can cite W5-AR §6.1 without also reporting it as defective.**
- **One correction landing is inserted before DR-W5-02.** No number is reserved for either record; after this correction is published and remote-verified, DR-W5-02 derives its own number from the new repository authority.
- **W5-AR gains its first erratum**, and its content hash moves for the first time since acceptance — which is what the hash discipline exists to make visible.
- **A precedent is extended, not created:** the correction-record pattern reaches a `phase-record` for the first time.
- **No behavioural, evaluative, or capability consequence whatsoever.** Nothing about the Wing changes; a number now matches what it counts.

## Non-goals

This record does not: add, remove or alter any behaviour-table row, cell, state or semantic; amend ADR 0020, W1-D3, any room contract, or any other record; change W5-AR's assignments, obligations, deliverables, gates or permissions; resolve W1-D3 §10.6 or §10.1; confer authority on DR-W5-02 or any unpublished record; open a wider count or citation audit; reserve a decision-record number; touch the pending ledger, Lane C, the fixture corpus, the engine or the tests; open W6; or authorise any implementation, directory, dependency, model contact, payload, transmission, harness or fixture execution. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — record, runway, contract, table, row, cell, state, human reviewer, architect. The record discusses a count and a sentence; **it describes no person, no health content and no clinical example.** No private names, no model or vendor names, no project lineage beyond this repository, no URLs, no placeholder tokens.

## Dependencies

**Proposed direct set, derived from the evidence actually used — marked for landing-time verification, each to be resolved individually against the live registry:**

| Id | Why it is direct |
|---|---|
| `W5-AR` | **the corrected source** |
| `ADR-0020` | **the five-row structure that is the evidence**, and the record whose semantics must be shown unchanged |
| `W4-D2` · `W4-D3` · `W4-D4` · `W4-D5` | **the four contracts actually measured.** The corrected sentence asserts a count *in every room contract*, so all four are direct evidence, not background |
| `ADR-0023` | **substantive, not merely precedent.** Decision 6 must actively distinguish its decision 7; without that reasoning this correction would appear to contradict an accepted record |
| `ADR-0003` | ceremony tiers |
| `W2-D3` | checklist rules 2, 3 and landing enumeration |

**Deliberately excluded, with reasons:**
- **`ADR-0021` and `ADR-0022`** — cited as **correction-record precedent only**. Nothing in this record turns on their content, and ADR 0023 already carries the pattern this one follows. **Precedent is not a dependency.**
- **`W0`** — no law is engaged. ADR 0026 depended on W0 because W0 §7 was the subject of its correction; here no constitutional text is involved.
- **`W1-D3`** — §10.6's text is quoted by W5-AR, not by this record, and this record does not touch the question. **Historically upstream is not the same as directly relied on.**
- **`DR-W5-02` / its future ADR** — unpublished, and this record confers it no authority.

**Not final. The registry dependency set is fixed at landing scope, not here.**

## Open questions

**None at acceptance.** The materiality judgment is made in decision 8, the applicability of the correction pattern to a `phase-record` is decided here, and the ADR number remains a landing-scope derivation rather than an open doctrinal question.

---

*The cheapest correction in the corpus: one word, one line, one file. It exists because a runway counted six states and wrote six cells, and because the record it was instructing had to count them to do its job. Six and five were both true — of different things.*
