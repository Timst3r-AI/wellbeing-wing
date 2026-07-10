# 0016 — Room Contract Template

**Status:** Accepted by human reviewer, 2026-07-10. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (first doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — nothing here turns on measurement.
**Constitutional references:** W0 Law 8 (inference prohibition); the W0 no-new-authority discipline; W1-D1 (edges, classes, grant types); W1-D3 (authority/staleness labels; labels-on-entry, D3-T3).
**Blocks:** the four room contracts (W4-D2 … W4-D5), each written against this template; the contract-conformance validator (DR-W4-06 / W4-D6), which checks contracts against this template's structure.

## Decision question

Four room contracts will be written — Wellness, Kitchen, Gym, Meditation — for four separate jurisdictions. Written freely, four contracts authored separately **cannot be trusted to cover the same ground**: one omits an inference-prohibition list, another buries its processing boundary, a third never states what a validator may check. **What fixed shape must every room contract take, so that coverage parity is structural rather than a matter of authorial diligence — and so that a later validator has a decidable target?** This record decides the template only. It fills no section for any room.

## Context

W3 is complete and sealed; the engine spine holds, shapes, moves, remembers, travels, and gives back, every behaviour under a standing test. W4 is the phase that draws the walls: rooms as jurisdictions, each bound by a written contract before any capability may act inside it. The W4 runway names six doctrine records that make the four contracts writable and testable; this is the first of them, and it is first by necessity — the template is the one wall all four rooms share, and the other five records fill standards *into* sections this record creates. No contract may be drafted until this template is accepted.

## Controlling law

- **W0 Law 8:** no cross-room inference; the template dedicates a required section to naming each room's prohibitions so the law is stated, not assumed.
- **W0 no-new-authority discipline:** a room contract may implement existing laws, edges, and classes; it may never mint a new edge, class, or authority state. The template's final required section is the constitutional check that confirms this.
- **W1-D1 (data-boundary map):** the read- and write-scope sections reference the map's edges, classes, and grant types — the map remains source of truth; the contract restates, never re-decides.
- **W1-D3 (authority and staleness):** write scope assigns labels on entry (D3-T3); the unknown/stale/contradicted section instantiates the authority/staleness behaviour in room terms.
- **ADR 0003 (ceremony tiers):** this record lands, if authorised, through full Tier J ceremony like every doctrine record before it.

## Decision

1. **A fixed room-contract template is adopted.** Every room contract is written against one skeleton — the same required sections, in the same fixed order, under the same fixed numbering, each with a non-blank body. Structural uniformity is the mechanism by which coverage parity becomes checkable rather than hoped for.
2. **Fixed order and fixed numbering are required.** Contracts use the identical section list, identical order, and identical numbering set out below. This is not stylistic: it gives the later contract-conformance validator (DR-W4-06 / W4-D6) a clear, decidable structural target — "section N is present, numbered N, non-blank" is checkable without interpretation.
3. **Every section is present and non-blank.** A section is never omitted and never left empty.
4. **"Not applicable" is written with its reason.** Where a section does not apply to a room, the body reads "Not applicable —" followed by the reason, so an inapplicability is always a stated judgement, never a silent gap. The **Meditation Room is the worked case**: it has no inbound health-context read edge from other rooms, so its read-scope cross-room clause is written exactly as *"Not applicable — this room has no authorised inbound read edge from other rooms."* No bespoke Meditation exception is created; the standard N/A-with-reason rule carries it.
5. **An eleventh "Open questions" section is required.** Each contract carries its own genuine unresolved questions in a mandatory final section, in the same honesty spirit as N/A-with-a-reason. The section is present even when empty; **when empty its body reads exactly "None at acceptance."** so an omission can never be mistaken for an oversight.

## The template — required sections

Every room contract contains exactly these eleven sections, in this order, under these numbers, each present and non-blank:

1. **Identity and purpose** — the room in W0 terms; one paragraph; no feature promises.
2. **Read scope** — the D1 edges the room reads, quoted **verbatim from D1** or cited by edge identifier, with governing grant types (never paraphrased — the load-bearing words *confirmed*, *only*, *scoped sections*, *user-initiated* are preserved; blur-words are banned here). *Worked N/A case (Meditation): "Not applicable — this room has no authorised inbound read edge from other rooms."*
3. **Write scope** — own records only, at their D1 classes, with authority/staleness labels assigned on entry (D3-T3).
4. **Inference prohibitions** — the general Law 8 rule plus this room's **named-bait list**, each bait bound to a future eval fixture. *(Highest-public-safety section: grammar placeholders only; no realistic clinical pairs.)*
5. **Unknown/stale/contradicted behaviour** — the shared behaviour standard (owned by DR-W4-05) instantiated in this room's wording; uncertainty carried in the output itself, never only beside it.
6. **Processing boundary** — the room's processing edge (its E11-family edge, or M2, or none) with grant type, duration norms, and the architectural-isolation requirement (one grant binds one room; the session derives from the grant).
7. **Speech rules** — the surfacing doctrine applied in room terms.
8. **Forbidden list** — the room's anti-map, named for emphasis though default-deny already excludes it.
9. **Validator hooks** — which of this contract's terms are mechanically checkable and which are review-only, stated explicitly per the decidability line (DR-W4-06); no term floats in the ambiguous middle.
10. **Constitutional check** — the laws this contract implements, and confirmation that it introduces no new edge, class, or authority state.
11. **Open questions** — this room's genuine unresolved questions; mandatory even when empty; when empty, the body reads exactly "None at acceptance."

Sections 4, 5, 6, and 9 carry *slots* whose *content standards* are owned by sibling W4 records (inference → DR-W4-04; unknown/stale → DR-W4-05; isolation → DR-W4-02; validator line → DR-W4-06). This template creates the slots and fixes their order and numbering; it does not pre-empt those standards.

## Constitutional check

- **Law 8** is served, not bypassed: the template *requires* an inference-prohibitions section in every contract, making the prohibition explicit per room rather than implicit.
- **No new authority:** the template mints no edge, class, or authority state; it is a documentation skeleton. It requires each contract to end with its own constitutional check, propagating the discipline downward.
- **No law required reinterpretation.** The template restates existing scopes by reference and defers every content standard to the map and the sibling records; it decides shape, not substance.
- **No amendment to the Constitution is proposed or required.**

## Alternatives considered

- **Full fixed template (chosen).** Fixed sections, fixed order, fixed numbering, non-blank bodies, mandatory open-questions section. Coverage parity becomes a mechanical property and validators gain a decidable target. Chosen because it is the only option under which "did this contract cover everything?" is answerable without interpretation.
- **Minimal skeleton / guidance checklist (rejected).** A loose list of topics contracts "should" address, with structure left to each author. Rejected: structural freedom is exactly where coverage divergence hides; four authors under delivery pressure will diverge, and no validator can catch a divergence the format permits.
- **Per-room freeform contracts (rejected).** Each room writes in its own shape with no shared skeleton. Rejected: without a shared structure the contracts are not comparable and the conformance validator is impossible — freeform defeats the phase's own testability goal.
- **One combined rooms document (rejected).** A single document covering all four rooms. Rejected: rooms are separate jurisdictions with separate grants; one document blurs the very walls the phase exists to draw. The answer is four contracts, one skeleton.

## Consequences

- **Easier:** the four room contracts (W4-D2 … W4-D5) can be written consistently, each against the same known shape; a reviewer compares like with like.
- **Easier:** the later contract-conformance validator (DR-W4-06 / W4-D6) has a **decidable structural target** — section presence, order, numbering, and non-blankness are checkable without interpreting doctrine.
- **Harder (deliberately):** room authors cannot silently omit a hard section — an inapplicable section must be argued as "Not applicable — <reason>", and the open-questions section must be present even when empty.
- **Preserved honesty:** unresolved matters stay visible in each contract through the mandatory open-questions section, rather than disappearing.
- **Constrains future decisions:** any change to the required section set, order, or numbering is an amendment to this record; the four contracts and the validator all inherit from it, so the template is the single point at which contract shape is decided.

## Non-goals

This record does not: draft any room contract; open or define any adapter; issue any prompt or model payload; create any UI or review surface; implement the governed string catalogue (a W6 structure — the wording sections route to it, and until it exists that routing is review-of-record only, on the ADR 0009 / 0011 / 0012 precedent); build any validator (DR-W4-06 / W4-D6 owns the validator plan; any validator *build* is gated until all four contracts are accepted); implement anything in W5 or W6; and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples.

## Public-safety considerations

Generic wording throughout — user, repository, Wing, room, contract, human reviewer, architect, model. No private names, no private system or project lineage, no model names. No clinical examples appear in this record; where the four contracts later populate their inference-prohibition sections, **grammar placeholders only** (Persona-K9, Condition-Q, Allergen-X, Medication-A17) and **no realistic clinical pairs** — a named-bait list written with real clinical mappings would itself be a small inference engine in documentation form, and the inference-prohibitions section is named here as the highest-public-safety surface of the contract-drafting work to come. No companion framing appears except where a sentence names a prohibition itself, allowlisted individually per corpus precedent if required.

## Dependencies

W0 Law 8 and the no-new-authority discipline; W1-D1 (edges, classes, grant types); W1-D3 (labels-on-entry, staleness); ADR 0003 (ceremony). At landing this record's registry entry is expected to depend additionally on the **landed W4 runway record** (gate document two), which must be accepted and published before this record lands. The sibling W4 doctrine records (DR-W4-02 … DR-W4-06) own the content standards for sections 4/5/6/9 but do not gate this template's acceptance; the template creates the slots they later fill.

## Open questions

**None at acceptance.** The three template-level questions raised in the deliverable brief are resolved in the decisions above: section order and numbering are fixed (decision 2); the eleventh open-questions section is mandatory-even-when-empty with the body "None at acceptance." (decision 5); the Meditation reads-nothing case is the worked N/A example, with no bespoke exception (decision 4).

---

*The template is the one wall all four rooms share. Decide its shape once, honestly, and the four jurisdictions that follow cannot quietly differ in what they promise not to do.*
