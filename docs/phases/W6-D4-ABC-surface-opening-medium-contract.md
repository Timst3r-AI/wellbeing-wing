# W6-D4-A/B/C — Review Surfaces: Opening Brief, Medium Decision, and Exposure Contract

**Status:** Accepted by human reviewer, 2026-08-17.
**Date:** 2026-08-17 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D4** (merged landings **A**, **B**, **C**)
**Position:** the opening landing of the W6-D4 programme. **W6-D4 opens at this record's acceptance and publication, for brief-governed work only.** Part A opens the deliverable and binds its risks; Part B decides the surface medium and scope; Part C fixes the read-only source exposure contract. **Nothing renders at this landing**; the surface, its declarations, its traces, and its proofs are the D+E+F landing's, behind this framework.
**Merge justification:** A, B and C are three docs-only decisions with no artefact mutation; an opened-but-mediumless D4 and a medium-without-contract D4 are half-states, and the reviewable unit is the **complete surface framework before anything renders** — the same discipline the D3 opening used, with the build kept separate and reviewable on its own.
**Governed by:** ADR-0043 consumed whole; ADR-0038 through ADR-0042, ADR-0044, ADR-0045; the W6-D3 records (`W6-D3-LLG`, `W6-D3-GR`, `W6-D3-CR`); the W6 runway. The W6-D3–D6 delivery brief is planning context only, never repository authority.
**Tier at landing:** J — full ceremony.

---

**The words are lawful; now the question the whole era was named for: can they be shown without minting authority? This record decides how the first showing will be built — and the answer is the most restrained artefact this repository can produce: a static page, generated deterministically from declared sources by a dependency-free script, with no button, no script, no state, and no way to do anything except be read. A window with no handles, made of glass all the way through.**

## Part A — Opening brief

1. **W6-D4 is open for brief-governed work only.** The programme question is exactly: **can the words be shown without minting authority?** D4 does not audit the showing (W6-D5's) and does not close the phase (W6-D6's). W6-D5, W6-D6 and W7 remain unopened, and no D4 landing opens them.

2. **ADR-0043 is consumed whole**: the surface to be built is a bounded reader over governed sources and governed catalogue entries — a presentation boundary, never an authority boundary; its sixteen non-identities, read law, write law, state law, channel law, declarability law, no-bulk law, human-review boundary, and all twenty proof obligations bind every later D4 landing without exception.

3. **The D4 sequence:** this record (A+B+C) → **W6-D4-D+E+F** as one merged materialisation landing — the honest-state rendering surface, the human-routing surface, and the structural proofs, merged because **a surface and its proofs are same-commit-coupled** (the W6-D2-C+D ruling's logic exactly: publishing a surface unproven, or proofs with nothing real to prove, are both half-states) → **W6-D4-G** closure posture, separate, after the materialisation is published and reviewable. D4 closure is never merged with D5 opening.

4. **Seven risks, bound at opening:** *viewing becoming review* → the medium of Part B makes it structural: nothing on a static page can perform anything, and the four ADR-0043 aphorisms render on the surface itself · *clicking becoming decision* → there is nothing to click that acts; the page contains no forms, no scripts, no action affordances · *selecting becoming approval* → no selection mechanism exists · *closing becoming retirement* → closing a static page changes no governed state, and the surface says so · *ordering becoming priority* → every ordering is declared, deterministic, and non-quality-named (id order, source order) · *filtering becoming concealment* → the surface has no filters; coverage is total by construction, and every uncomfortable state renders at full size · *surface prominence becoming authority* → one neutral typographic register, no colour-as-state, no glyph-as-verdict, declared as data and proven.

5. **The state-family rendering directive is carried whole and binds the D+E+F landing:** rendering law is reasoned **once per genuinely shared state family**, each shared law tied to its source authority (ADR-0040's per-state laws; ADR-0041's routing laws; ADR-0043's contract) — and **every rendered item carries its own mandatory trace row**: source · catalogue entry / CAT id where applicable · governed state · accompaniment linkage · rendered wording · proof result · non-authority confirmation. **A state-family proof is explanatory; the per-item trace is mandatory.** Family reasoning never replaces individual accountability, and a family law passing is never evidence that item N passed — item N's row is.

## Part B — Surface medium and scope decision

6. **The medium is decided: a static generated review surface** — one HTML artefact at `docs/surface/review-surface.html`, generated deterministically by a **Python-stdlib-only generator** at `scripts/generate_review_surface.py`, from declared inputs only, accompanied by two data artefacts: `docs/surface/surface-declarations.json` (the ADR-0043 fifteen declarations, as data) and `docs/surface/surface-trace.json` (the complete per-item trace, as data). **The page contains no JavaScript, no forms, no interactive controls, and no external references of any kind** — its entire capability is to be read.

7. **Options compared, decided as the brief required:**
   - **Documentation-only prototype (rejected as insufficient):** safest on paper, but it answers the programme question only in theory — no rendering exists to prove, no trace rows bind real wording, and W6-D5 would have nothing to audit. The era's question deserves a real, bounded answer.
   - **Static generated page (chosen):** deterministic, diffable, reviewable as bytes, regenerated only by ceremony; **zero interactivity makes the no-affordance, no-bulk, no-workflow, and viewing-is-not-reviewing obligations structural rather than behavioural**; no server, no process, no state, no cache by construction; stdlib generation adds no dependency; and byte-identical regeneration gives the same integrity proof the evaluation records use.
   - **Local preview server (rejected):** a running process is a runtime surface with request handling, implicit state, and a channel — three whole classes of proof obligation acquired for zero rendering benefit.
   - **CLI preview (rejected):** transient output is unreviewable and untraceable after the fact; a surface whose rendering vanishes cannot carry per-item trace accountability or feed the W6-D5 audit.
   - **Any richer medium (premature):** anything interactive arrives, if ever, behind its own future brief, its own affordance declarations, and the full ADR-0043 proof set — nothing here forecloses it, and nothing here needs it.

8. **Implementation is permitted inside D+E+F under this medium** — the generator, the three artefacts, and their proofs may be built, because the medium's whole risk surface has been bounded here and the twenty ADR-0043 obligations plus the per-item trace duty attach at that landing in the same commit.

9. **Scope — what the surface shows (and all of it, always):** the **governed string register** (all thirty-three catalogue entries with their metadata, ceilings, and D3 grading dispositions — each grade rendered with its own ceiling: a grade is not approval and not display permission) · the **evidence map** (all sixty-five Lane C rows in their derived presentation states — applicability-unresolved at full size, `not_evidenced` with the same dignity as its siblings) · the **evaluation posture** (all twenty-three fixtures `behaviourally_executed` with the executed-is-not-passed accompaniment inline; all twenty-six overt unknowns as standing truths with their basis; the routed silent-probe deltas with **both variant captures whole** and no machine conclusion) · the **pending ledger** (all nine stubs with owner and unblocking condition, no affordance of any kind) · and the **carried open questions** (still alive, never retired). **Omission of any honest state where its siblings render is the V4 overclaim, and coverage is proven per item.**

10. **Registry posture for the surface artefacts, explicit because silence is not lawful:** the three generated artefacts are **deliberately excluded from the registry**, for the evaluation-records reason exactly — their integrity is proven mechanically by **deterministic byte-identical regeneration** in the suite, and hash-registration of artefacts that lawfully regenerate would turn every authorised regeneration into registry churn without adding integrity. The D4 *records* are registered as always; the generator and proofs are code, governed as all code is.

## Part C — Read-only source exposure contract

11. **The surface may read exactly six declared inputs, and nothing else, ever:** `governance/string-catalogue.json` (the register) · `docs/governance/privacy-health-data-assurance-record.md` (the Lane C rows, parsed from its own JSON blocks) · `governance/evaluation/` (the manifest and twenty-three records) · `tests/test_pending_ledger.py` (the pending ledger, read as the stub source of record) · `governance/registry.json` (record titles and identities for citation rendering only) · `docs/surface/surface-declarations.json` (the authored declarations: carried-question rows and D3 grading summary with their record citations, the accompaniment texts with theirs, and the glyph, colour-semantic, coverage, ordering, and affordance inventories). **The declarations file is itself a declared input, human-authored at the materialisation landing, reviewed as content, and cross-checked by proof against the governed records it cites.**

12. **Undeclared input fails, structurally.** The generator holds its declared-input allowlist as data, opens nothing outside it, and hard-fails on any attempted access beyond the list; the proofs verify by AST that no discovery mechanism exists — **no path walk, no glob beyond the one declared evaluation-records pattern, no search convenience, no metadata sweep, no inferred source merge, no hidden source, no cache, no local store, no environment reading, no network, no clock.** What is not declared is not read, and what is not read cannot leak into a rendering.

13. **Source-trace requirement, binding every rendered row:** every item the surface renders must be traceable — in `surface-trace.json` and provable against the page — to its governed source, its catalogue entry where applicable, its governed state, its accompaniment linkage, its rendered wording, its proof result, and its non-authority confirmation. **A rendered row without a trace row is a proof failure**, and the D+E+F landing's suite enforces the bijection both ways: nothing rendered untraced, nothing traced unrendered.

## Boundaries

14. **This record does not:** render anything · create the generator, the artefacts, or the proofs (D+E+F's) · declare D4 complete (G's) · open W6-D5, W6-D6, or W7 · change the catalogue, the grading records, the runtime, fixtures, evaluation records, the pending ledger, Lane C, Tier 3, or applicability · contact any model · add any dependency. The nine stubs remain untouched; conversion remains its own ceremony.

## Public-safety note

Generic and structural wording. Barred vocabulary appears only inside prohibitions; the scan-sensitive families appear as stems only. No real health data, no clinical examples, no URLs, no claim about any person or any readiness.

---

*The window is designed: glass all the way through, no handles, no hinges, no latch — and behind it, everything the Wing honestly holds, at full size, in its own words. What remains is to build it exactly as drawn, prove every pane, and then ask the only question that ever mattered here: does looking through it leave the truth exactly where it was?*
