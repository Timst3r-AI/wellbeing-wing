# W6-D5-F — Assurance Findings and Correction Paths

**Status:** Accepted by human reviewer, 2026-08-17.
**Date:** 2026-08-17 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D5** (landing **F**)
**Position:** the findings landing of the W6-D5 programme: the audit evidence published at `W6-D5-AER` consolidated into classified findings, with the smallest governed correction path named for each — **and every correction stopped here, unexecuted, awaiting its own authorisation.** This record lands separately from closure so that anything correction-needed is visible to Tara and Ari before completeness is declared over it.
**Governed by:** `W6-D5-PAB` and `W6-D5-AER`; ADR-0043's declarability and source-trace law; ADR-0040 and ADR-0041's rendering and routing laws.
**Tier at landing:** J — full ceremony.

---

**The showing stayed honest. On five hundred and thirty-one checks, every rendered state said exactly what its source says, every trace led home in both directions, and nothing in the words, the colours, the ordering or the silence claimed more than the records hold. Two findings stand — and neither is a lie the surface told. Both are places where a true thing is held true by habit rather than by fixing, and this record names them, sizes their smallest repairs, and touches neither.**

## 1. Did the showing stay honest?

**Yes — on the checks performed, on the day performed.** No rendered state drifted from its source; no honest state was omitted, softened, aggregated away, or hidden behind a default; no colour, glyph, ordering, prominence, grouping, or absence implied approval, completion, safety, correctness, conformance, or readiness; the page's own silence carries the four aphorisms, so a surface without controls cannot be misread as a review already performed; and the mandatory per-item trace is complete, bijective in both directions, and individually accountable — **state-family reasoning explained the sections and excused no item from answering for itself.**

**This finding of honesty is bounded exactly as the opening brief bound it: it is not certification, not safety, not clinical validity, not legal conformance, not correctness, not production readiness, and not approval of anything.** It says the presentation remained faithful to its sources under the W6 rules, and nothing further about the world, any person, or fitness for any use.

## 2. Classified findings

| ID | Finding | Class | Current accuracy | Risk if uncorrected |
|---|---|---|---|---|
| **F-1** | The per-entry grading disposition renders from a generator literal rather than a per-entry read of a declared source | **correction-needed** | Accurate — verified against `W6-D3-GR`, where all thirty-three entries are `lawful-as-worded`, and supported by the declarations file's grading summary with its citation | A future grading landing could change an entry's disposition and the surface would continue rendering the old one, silently |
| **F-2** | The four applicability records render as a family statement without individual rendered rows or trace rows | **correction-needed** | Accurate — all four are `unresolved` with no role or basis asserted, and the page says exactly that | Alone among the surface's governed states they carry no per-item accountability; a future divergence (one record resolving) could hide inside an unchanged family sentence |
| **O-1** | The catalogue's own `governance_note` is not rendered | **satisfied (observation)** | The surface renders its identity statement from the declarations; the note is the register's self-description, not a governed state | None — no honest state is omitted |
| **O-2** | Section sequence is not named in the declared ordering rules | **satisfied (observation)** | Section order is document structure and carries no priority language or claim | None — the declared ordering rules govern item ordering, which is where a priority claim could live |
| — | All other checks: 188 rendered-state, 14 implied-claim, 321 trace-and-mapping, 4 stub-reassessment | **satisfied** | — | — |

**No finding is classified deferred, out-of-scope, or requires-separate-ceremony**, except the stub postures of §4, which are ceremony-bound by standing law rather than by any finding here.

## 3. Smallest governed correction paths — named, not taken

**Nothing below is executed by this record.** Each path is sized for a future landing that would require its own authorisation, its own bounded scope, its own proofs, and its own publication.

- **P-1, for F-1 — the smallest repair is a pinning proof.** Add one deterministic proof to the surface's proof module asserting that the rendered per-entry disposition matches the dispositions the governed W6-D3 record states; any future divergence then fails the suite loudly rather than rendering stale. *Cost: one proof, no artefact regeneration.* **The fuller alternative** — moving the per-entry disposition into the declarations file as a declared per-entry mapping the generator reads — is architecturally cleaner and costs a declarations change, a generator change, a regeneration, and proof updates. **Recommendation: P-1 first**, because it removes the drift risk immediately and at least cost; the fuller path remains available whenever a grading change actually approaches.
- **P-2, for F-2 — render the four applicability records as their own items.** The generator already parses them (it reads the assurance record's first JSON array and uses only the second); the repair renders a four-row table with their unresolved states and emits four trace rows, taking the trace from 188 to 192. *Cost: a small generator change, one regeneration, and an update to the proof module's expected section counts.*
- **P-3, optional and separate — land the audit as a standing proof module.** The five hundred and thirty-one checks of `W6-D5-AER` ran from a script that is not a repository artefact, so their execution is packet-reported (see §5). A future landing could make the audit re-runnable by anyone, converting it permanently to independently verifiable. **Named as an option, recommended but not required, and outside anything authorised here.**

**Neither P-1 nor P-2 is a defect repair — both are accountability repairs.** The surface is not currently saying anything untrue, and no correction is urgent.

## 4. W6-owned pending stubs — reassessed, unconverted

Three stubs are W6-owned, each on the ledger's own `w6 surface phase` owner: **language-law grading both directions** · **no bulk-approve path in UI** · **label legibility**. After W6-D3 and W6-D4, each has evidence bearing on its condition that it did not have before — grading executed, a surface built with no bulk path and no affordance at all, governance information carried inline in every rendered state. **Each is therefore recorded as *eligible for future conversion consideration*, and none is converted.** Eligibility is not conversion; conversion is its own governed ceremony against the stub's own condition, and **no stub becomes convertible merely because a later deliverable exists.** **The pending ledger is byte-identical**, proven, and this record proposes no edit to it.

## 5. Packet-reported versus independently verifiable

Stated honestly so Ari can label the packet precisely:

- **Independently verifiable from repository records today:** the two findings themselves — the generator literal is readable in `scripts/generate_review_surface.py` and the absence of applicability ids is checkable in the page and trace; and every property covered by the twenty-six standing structural proofs, which anyone can re-run: trace bijection both ways, the seven mandatory fields, ceilings and accompaniments rendered, aphorisms present, uncomfortable states at full size, palette neutrality, absence of glyphs, controls, links and barred affirmatives, byte-identical regeneration, and declared-input conformance.
- **Packet-reported:** the five hundred and thirty-one checks *as a single executed audit run* — specifically the per-item cell-by-cell comparison of every rendered state against its governed source. The results are reproducible by anyone from the declared sources, and the tables in `W6-D5-AER` record them item by item, but the script that executed them is not a repository artefact. **P-3 exists precisely to close that gap, and closing it is optional and unauthorised here.**

## 6. What this record did not do

It corrected nothing, redesigned nothing, regenerated nothing, converted nothing, and touched no artefact, source, or ledger byte. It performed no certification, safety validation, legal-conformance assessment, clinical validation, production-readiness assessment, or approval. It did not declare W6-D5 complete — that is W6-D5-G's, landing separately after these findings are published and independently reviewable. **W6-D6 and W7 remain unopened.**

## Public-safety note

Generic and structural wording throughout. Barred vocabulary appears only inside prohibitions. No real health data, no clinical examples, no URLs, no claim about any person or any readiness.

---

*Two findings, both of them the same shape: something true, held in place by a hand rather than a bolt. The audit's job was to notice the difference, and the discipline's job is to leave the tightening to a day that has been authorised for it. The window is honest today, and now it is honest on the record about how it is honest.*
