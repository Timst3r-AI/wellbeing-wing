# 0038 — Display-Vocabulary and Label Law (DR-W6-01)

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D1**
**Position:** the first W6-D1 doctrine record, carrying laws 1–3 of the accepted W6-D1 brief: the display-vocabulary law, the stored-versus-derived law, and the prohibited-label and prohibited-visual law. It renders nothing, creates no catalogue, allocates no identifier, and grades no string. DR-W6-04 will consume it whole; DR-W6-02, DR-W6-03, DR-W6-05 and DR-W6-06 consume the parts named in decision 27.
**Constitutional references:** W0 Laws 1, 3, 6, 11, 13; W0 Non-Goal 7. **No law is amended.**
**North star carried:** governed truth must survive display without becoming authority.
**Resolves:** none.

---

**Before the Wing may show a single word, this record decides which words exist to be shown. The vocabulary is closed, like every Wing vocabulary; every label knows whether it is a stored truth or a derived presentation; the words that could ever outrank their sources are barred by name and by stem; and the same law reaches the pixels — because a checkmark is a verdict whether or not anyone typed it.**

## Decision question

**What labels may the Wing ever display, in what classes, from what sources — and which words and visual forms are barred outright, in mechanically checkable terms, so that no later catalogue, grading, or surface can show more certainty than the governed record behind it holds?**

## Controlling law

- **The accepted W6-D1 brief** — laws 1–3 assigned here; the six-record sequence; the visual-semantics doctrine; the DR-W4-06 decidability discipline for proof obligations.
- **The W6 runway (`W6-AR`)** — questions Q1–Q3; the ten risk bindings, of which labels-minting-authority, visual overclaim, and unknowns-hidden land here first.
- **ADR-0034** — the anti-collapse chain (executed ≠ passed · observed ≠ proven), decision 39's closed status vocabulary and its barred values, decision 26's honest-unknown calibration; **ADR-0037 decision 11** — the closed record-outcome vocabulary and its named mechanical exception.
- **W4-D6-PHDAR §2, §5, §8** — the stored `evidence_status` and `applicability_status` vocabularies and **the six-word presentation vocabulary "derived at presentation, never stored"** — this record's founding precedent for the stored/derived seam.
- **ADR-0029** — the engine ladder as the single label calculator for freshness states, and the exact provisional-governance label carried unbroken.
- **W0 Law 3** — confidence creates no authority; **W0 Non-Goal 7** — no certification-style claim of any kind, which this record extends to display forms.

## Decisions

### Part A — The display-vocabulary law

1. **This record decides display doctrine and displays nothing.** No label is rendered, no catalogue exists, no identifier is allocated, and no surface is authorised by anything here.

2. **The display vocabulary is closed.** A Wing surface may display only labels belonging to the seven classes of decision 3. A label belonging to no class does not display; extending the class set, or the membership rules of any class, is a future governed record — never an implementation choice, never a design refresh.

3. **Seven vocabulary classes, exhaustive:**
   - **Source-state labels** — states a governed source already holds (`behaviourally_unexecuted`, `behaviourally_executed`; `evidenced`, `not_evidenced`, `deferred_named_dependency`, `external_evidence_required`; `unresolved`; the pending ledger's pending state; the engine ladder's freshness states including stale and expired; the evaluation outcome classes `no-delta-observed`, `routed-to-review`, `unknown-not-absent`). Displayed verbatim or through a registered derived label — never through an invented synonym.
   - **Derived presentation labels** — labels computed at presentation time from source states by a deterministic, recorded rule (the Lane C six-word vocabulary is the founding member and the pattern: *applicability unresolved · deferred — named dependency · evidenced · not evidenced · external evidence required*, plus the class this record leaves room for DR-W6-02 to define per state).
   - **Routing labels** — labels that say where a matter goes (*awaiting human review*, *routed to review*), naming a destination and never a judgement.
   - **Non-authority labels** — the standing non-claims, displayed as first-class content: the observation-never-proof statement, the provisional-governance label carried byte-exact from ADR-0029, the Lane C safe wordings, and the executed-is-not-passed accompaniment of decision 19.
   - **Review labels** — human review-only assessments, always attributed to human review and never to the system (*under human review*, *human judgement recorded*), per the DR-W4-06 line between mechanical and judged.
   - **Prohibition labels** — text naming what is barred or refused, permitted only in negation or refusal form (*no result here means passed*, refusal reason codes).
   - **Future-owned labels** — labels naming dormant or future-owned matters as exactly that (*generative-era work, future-owned*, *dormant — requires its own governed record*), never as absent and never as coming-soon marketing.

4. **Every displayed label carries its class**, and the class assignment is data, not convention: whatever artefact later carries display strings (the W6-D2 catalogue) must record each string's class, so class membership is mechanically checkable.

### Part B — The stored-versus-derived law

5. **Stored source states display verbatim or not at all.** No source state may be renamed into a friendlier or safer-looking display alias: `behaviourally_executed` may not display as *tested*, *checked*, *verified* or *run successfully*; `deferred_named_dependency` may not display as *in progress* or *coming soon*; `not_evidenced` may not display as *n/a*, *pending*, or a blank; `unknown-not-absent` may not display as an empty cell. **Renaming a state is minting authority by thesaurus**, and it is barred.

6. **Derived presentation labels are derived at presentation, never stored** — the Lane C rule promoted to Wing-wide law. No governed source may hold a derived presentation label in any field; no write path may persist one; and a derived label found stored anywhere is a defect in whatever wrote it. Every derived label carries a deterministic derivation rule recorded in an accepted record, and the derivation is recomputable from the source at any time.

7. **Review-only assessments are human and say so.** Tone, register, dignity and adequacy judgements are review-only under the DR-W4-06 discipline; where displayed, they display as review labels (decision 3), attributed to human review, and are never presented as machine findings.

8. **Barred labels are barred in every class.** Nothing in decision 3 admits a barred word (Part C) as a display label — not as a source alias, not as a derived label, not inside a routing or review label. Barred words may appear on a surface only inside prohibition labels: the negation register the whole corpus already uses.

9. **Explanatory text is bounded by its sources.** Free prose on a surface may state only what a governed source supports, cites its source where the subject is execution, evidence or applicability, and carries the relevant non-authority label alongside. Explanatory text that outruns its source is an overclaim in sentence form, and the same scan-and-review discipline that governs repository documents governs displayed prose.

### Part C — The prohibited-label law

10. **The barred display list, closed and extendable only by record** — none of the following may ever appear as a display label, in any vocabulary class, on any Wing surface: **passed · safe · clinically safe · medically safe · legally satisfied · production-ready · approved by the system · validated as correct · behaviourally proven · proof of safety · diagnosis · therapy · treatment advice · readiness · all-green status · success verdict** — together with **every word formed from the `certif-` stem and every word formed from the `complian-` stem** (barred as stems so no suffix variant survives the ban). The list may grow by governed record; it may never shrink.

11. **Two register boundaries, stated so the ban stays honest:** a stored schema key is not a display label (the Lane C `safe_wording` field name is a schema key whose *value* is the cautious wording — the key itself never renders as a label); and barred words remain lawful inside prohibition labels and governed negations, exactly as the repository's own documents use them. The ban governs what a surface may *assert*, not what doctrine may *forbid*.

12. **The barred list is mechanically checkable, by design.** The list of decision 10 is consumable as data: whatever artefact later holds display strings must be scannable against the exact words and stems above, and the deterministic validator obligation lands with the artefact that first holds strings (the catalogue-ID validator class W6-D2 wakes), consuming this record's list verbatim. Until such an artefact exists there is nothing to scan, and no claim is made that scanning has occurred.

### Part D — The prohibited-visual law

13. **The visual axioms are law:** a rendered word is a claim · colour is a sentence · a checkmark is a verdict · grouping, sort order, dashboard position, icon choice, and interaction affordance are all possible claims · visual language must never mint authority the governed source does not hold · **and omission of an honest state is an overclaim** — the quietest one.

14. **Six prohibited visual classes, stated in checkable terms for any future rendering artefact:**
    - **V1 — verdict glyphs:** no checkmark, tick, cross-as-failure, trophy, shield, seal, badge or equivalent success/failure glyph may attach to any execution, evidence, or applicability state.
    - **V2 — grading colour semantics:** no green-as-pass / red-as-fail traffic-light mapping on execution, evidence, or applicability states. Colour may distinguish states; colour may never grade them.
    - **V3 — aggregate verdicts:** no all-green summary, safety meter, readiness score, percentage-complete-toward-safe, or any single visual that aggregates governed states into one implied verdict.
    - **V4 — concealment grouping:** no default view, filter, collapse or grouping that hides deferred, unknown, `not_evidenced`, or unresolved states while displaying their siblings. The honest states ship visible by default.
    - **V5 — ceremony-bypassing affordances:** no button, toggle, swipe or control whose label or behaviour implies conversion, approval, retirement, or resolution of any governed state without its ceremony — no *convert*, no *mark resolved*, no *approve all* (the pending ledger's no-bulk-approve obligation, carried into visual law).
    - **V6 — confidence by prominence:** no ordering, sizing, or placement rule that presents one state as more trustworthy, more finished, or more true than its source records — sort orders over governed states are declared, deterministic, and never named after quality.

15. **Checkability obligation:** any future rendering artefact must declare its glyph inventory, its colour-semantic mapping, its default-view state coverage, and its affordance inventory **as data**, so that V1–V5 become deterministic checks over declarations and V6 becomes a declared-rule review. The declaration obligation is decided here; the checking machinery arrives with the artefacts it checks, under DR-W6-04 and the deliverables that build surfaces.

### Part E — Treatment of the known state families

16. **Every known honest state family has a home in the vocabulary, and none may be omitted from a surface that shows its siblings:** *pending* (source-state; surfaced per DR-W6-03, conversion never an affordance) · *deferred* (source-state, with its named dependency; derived form per Lane C) · *unknown* (source-state, including `unknown-not-absent`; never an empty cell, never an error) · *stale* and *expired* (the engine ladder's own labels, verbatim; the ladder remains the single calculator) · *review-routed* (routing label; destination, never judgement) · *`behaviourally_executed`* (source-state, verbatim, with decision 19's accompaniment) · *evidenced / not_evidenced* (source-state with the standing non-claim) · *applicability-unresolved* (derived label from stored `unresolved`; never *not applicable*) · *external_evidence_required* (source-state; external means external) · *non-authority notices* (their own class, first-class content) · *carried open questions* (future-owned/review labels; surfaced as carried) · *dormant and future-owned surfaces* (future-owned labels; dormant means dormant).

17. **Detailed per-state rendering semantics remain DR-W6-02's** — this record fixes each family's vocabulary class and verbatim-or-derived path; how each renders (layout, accompaniment, interaction) is decided there, inside these classes.

### Part F — Non-authority accompaniments

18. **The non-authority label class is load-bearing, not decorative.** Wherever an execution, evidence, or applicability state displays, the applicable standing non-claim displays with it, in the forms later records make concrete.

19. **The executed-is-not-passed accompaniment is mandatory:** `behaviourally_executed` never displays without its meaning — one governed run happened — being available in place; and no display of `evidenced` occurs without the standing statement that an evidence pointer locates evidence and never asserts a requirement satisfied.

### Part G — Boundaries

20. **This record does not decide:** per-state rendering semantics in detail (DR-W6-02) · review-routed delta presentation (DR-W6-03) · the label-authority firewall as a whole (DR-W6-04, consuming this record) · catalogue identity and the catalogue-ID namespace (DR-W6-05) · the review-surface boundary contract (DR-W6-06) · any catalogue artefact · any final catalogue ID · any string grading · any rendered label · any UI or surface.

21. **Consumers, named:** DR-W6-02 consumes Parts A, B and E; DR-W6-03 consumes the routing and future-owned classes and V5; DR-W6-04 consumes this record whole as firewall material; DR-W6-05 consumes decisions 4, 10 and 12 as catalogue validation obligations; DR-W6-06 consumes V4 and V5 as surface-contract obligations.

22. **W6-D1 remains open; W6-D2 through W6-D6 remain unopened; W7 remains unopened.** Nothing here converts a stub, changes a status, touches a fixture, an evaluation record, Lane C, Tier 3 or applicability, contacts a model, or adds a dependency.

## Alternatives considered

- **An open display vocabulary with review-time policing (rejected).** Review does not scale to every string a surface will ever show; a closed vocabulary with classes makes the honest path the only path.
- **Allowing curated display aliases for stored states (rejected firmly).** Every alias is a translation, and translation is where authority leaks in — the thesaurus is the attack surface. Verbatim or registered-derived, nothing else.
- **Barring words but not stems (rejected).** Suffix variants would survive a word ban; the two highest-risk families are barred at the stem.
- **Barring visuals by taste rather than class (rejected).** Taste is review-only and unenforceable; the six classes are stated so that declarations make them checkable.
- **Treating omission as a layout choice (rejected, ruled).** A surface that hides its uncomfortable states is making a claim about them. Omission is an overclaim, in ink.

## Consequences

- Every later W6 record inherits a closed vocabulary to build inside, and the catalogue arrives already knowing which words can never be in it.
- Surfaces become boring in exactly the right way: states appear in their own names, doubts appear at full size, and nothing glows green.
- The two hardest audits of the phase — barred wording and barred visuals — are pre-shaped into data-plus-scan problems rather than judgement calls.

## Constitutional check

- **Law 1** — nothing here contacts or notifies anyone; display of review routing is an invitation surface, never a push.
- **Law 3** — the whole record is Law 3 at the pixel: no rename, alias, glyph, colour, aggregate, affordance or omission may create authority a source does not hold.
- **Law 6** — the clinical line holds: diagnosis, therapy and treatment advice are barred display labels outright.
- **Law 11** — no person is gated: labels describe system states, never people, and no display state conditions anyone's rights.
- **Law 13** — class assignments, derivation rules and declarations are data, auditable like everything else.
- **W0 Non-Goal 7** — extended to display: no certification-style claim can be spelled, coloured, grouped, or implied.
- **No new authority, no new namespace** — the catalogue-ID namespace remains DR-W6-05's; nothing is allocated here.

## Non-goals

This record authorises no catalogue, no catalogue ID, no string grading, no D5-T24 execution, no rendered label, no UI, no CLI, no review surface, no write-back, no runtime, fixture, evaluation-record, pending-ledger, Lane C, Tier 3 or applicability change, no model contact, no generative evaluation, no dependency, no E10/vendor, Z4, E12/Z5 or hosted movement, no W6-D2 through W6-D6 opening, and no W7 opening. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording — label, class, state, surface, source, reviewer. Barred vocabulary is named only to bar it, and the two scan-sensitive families are carried as stems by design. No real user data, no vendor or model names, no URLs, no claim of any kind about any person or any deployment.

## Dependencies

`W6-D1-SDB` (direct — laws 1–3 assigned here) · `W6-AR` (direct — Q1–Q3 and the risk bindings) · `ADR-0034` (direct — the anti-collapse chain and closed status vocabulary) · `ADR-0037` (direct — the record-outcome vocabulary) · `W4-D6-PHDAR` (direct — the stored vocabularies and the derived-never-stored precedent) · `ADR-0029` (direct — the ladder labels and the provisional-governance label) · `ADR-0003` (operative ceremony authority).

## Open boundaries and later ownership

1. **Per-state rendering semantics** — DR-W6-02, inside Parts A/B/E.
2. **The firewall's whole-system guarantee** — DR-W6-04, consuming this record.
3. **Catalogue validation machinery** — W6-D2, waking the dormant validator class against decisions 4, 10 and 12.
4. **Rendering-artefact declarations** — the deliverables that build surfaces, under decision 15.
5. **Barred-list extension** — future governed records; growth only.

---

*The Wing's first display law, and not one thing displays. That is the point. When a screen finally exists, every word on it will have been legal before it was visible — and the words that could have lied will have been dead for a phase already.*
