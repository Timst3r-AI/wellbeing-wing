# 0019 — Cross-Room Inference Prohibition Standard

**Status:** Accepted by human reviewer, 2026-07-11. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (fourth doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — the standard is decided now; fixtures and evals are named as future requirements, not designed here.
**Controlling law:** W0 Law 8 (inference prohibition); the W0 no-new-authority discipline; W1-D1 (the absent room→room edges); W1-D2 §0.1 (consent authorises edges, it cannot create them); W1-D3 (the "possible pattern, not confirmed," queue-only profile pathway); ADR 0002 (the settled safety-surfacing refusal doctrine).
**Blocks:** the Inference Prohibitions section of every room contract (W4-D2 … W4-D5), which enumerates its room's named baits under this standard.

## Decision question

ADR 0016 fixed an Inference Prohibitions section in every room contract; ADR 0017 made another room's content structurally unreachable; ADR 0018 fixed exactly what a room may read and write. The residual and hardest question remains: **what does "must never infer" mean *operationally* — such that a contract can state it and a test can catch it?** Model derivation is internal and not directly inspectable, so the standard must both prohibit the inference *constitutionally* and give an *evaluable* breach standard grounded in observable consequence, without letting "nothing visible happened" become a licence to infer silently.

## Context

W4 is open for governed doctrine and brief work only; this is the proposed fourth of six W4-D1 doctrine records. The engine spine holds a person's record with no model anywhere near it, and no adapter is authorised. This standard is decided before any model may enter a room, so that the prohibition is a property the later processing layer is held to, not a discipline it is trusted to keep. It states the standard and one canonical-placeholder example; it authors no room's actual bait list, designs no fixtures, and builds nothing.

## Controlling law

- **W0 Law 8 — inference prohibition.** No room may use another room's content, and no room may derive a health-relevant conclusion beyond its granted context. This standard is the operational form of Law 8 at the room boundary.
- **W0 no-new-authority discipline.** The standard mints no edge, class, consent form, or authority state.
- **W1-D1** — the map is a whitelist; there is no room→room edge; absence of an edge is a prohibition.
- **W1-D2 §0.1** — consent authorises edges, it cannot create them; a user request is not a grant and cannot conjure an absent flow.
- **W1-D3** — the governed Profile pathway may surface "possible pattern, not confirmed" only within its existing queue-only authority; nothing in the room layer inherits that pathway.
- **ADR 0002** — the settled safety-surfacing refusal doctrine, whose scope-limit refusal shape user-requested speculation inherits.

## Decision

1. **Constitutional prohibition.** A room must not derive a health-relevant or room-jurisdiction conclusion outside its granted context. The prohibition binds **even when requested by the user**, whether the inference is volunteered or requested, stated directly or phrased as uncertainty, kept unstated but used to change behaviour, or carried into a later interaction. **A user request cannot create an absent edge, widen a grant, or authorise a forbidden inference.**
2. **The constitutional prohibition and the observable test are distinct.** The room is prohibited from making the inference *at all*; observable consequence is how a breach becomes *testable*. **Observable consequence is evidence of a breach, not permission to infer silently so long as nothing visible happens.**
3. **Silent behavioural change is the primary target** — the case where nothing is said but behaviour changes because of a forbidden conclusion.
4. **No laundering through uncertainty language.** Hedging, uncertainty phrasing, questions, and user attribution do not legalise the inference; a hedged, questioned, or user-attributed forbidden inference remains a forbidden inference. The illustrative hedge phrases are **not** a complete governed string catalogue.
5. **Named-bait requirement.** Every future room contract requires a room-specific named-bait list — **a floor, not a ceiling**; each future bait **maps one-to-one to a future evaluation fixture**; **Law 8 binds beyond the named list.** DR-W4-04 does **not** author any room's actual bait list (those are W4-D2 … W4-D5), and designs no fixture, ID, schema, harness, scoring, or prompt.
6. **Highest public-safety surface.** The named-bait lists are the highest public-safety surface in W4 drafting; realistic clinical pairs are prohibited; canonical placeholders only.
7. **User-requested speculation inherits the settled refusal shape** (ADR 0002). The refusal declines to infer or confirm the out-of-scope conclusion, avoids repeating or strengthening the suspected pattern, states the room's lawful boundary, continues only within authorised context, offers a governed review/confirmation route where one already exists, and **mints no claim, restriction, recommendation, warning, or authority state.**
8. **No room-level pattern-flag pathway.** Room processing has no pattern-flag or "for review" pathway; **a room that notices something outside its granted authority has nowhere lawful to place the noticing.** The absence is deliberate architecture, not a missing feature.
9. **Violation handling.** A confirmed breach is the highest public-safety defect class: the case becomes a permanent regression fixture, the causal path must be corrected, and **output filtering alone is never an adequate remedy** where the forbidden inference still changes behaviour.
10. **Complementary walls.** ADR 0017 (isolation), ADR 0018 (scope), and this standard are complementary — isolation reduces the channel, scope fixes what is on the table, inference prohibition governs what may be concluded or acted upon inside the lawful channel. **The Meditation Room receives the uniform standard**, with its stricter outward-signal prohibition instantiated only in its own contract.

## Constitutional check

- **Law 8 is served, not bypassed:** the standard makes the no-out-of-scope-inference rule operational and evaluable, and it fails safe — a room that cannot lawfully hold a conclusion also has nowhere to put it.
- **No new authority:** no edge, class, consent form, or authority state is minted; the room layer is denied the queue-only pattern-flag pathway the Profile layer alone holds.
- **User autonomy respected without laundering:** a user may ask, but a request does not create permission; the lawful response redirects to an already-governed route rather than minting a claim.
- **No law required reinterpretation**, and **no amendment to the Constitution is proposed or required.**

## Observable-consequence standard

Internal derivation is not inspectable; therefore a breach is **evidenced** when a conclusion outside granted context produces any observable consequence, including:

- direct statement of the conclusion;
- implication through framing or wording;
- changed tone or caution;
- selection, ranking, suppression, or omission of content;
- changed recommendation, refusal, warning, escalation, or routing;
- durable writing, or queue/audit effects, in any record or location;
- later-turn retention or influence;
- any other behaviour that would not have occurred without the forbidden conclusion.

The governing line, restated so it cannot be misread: **observable consequence is evidence of a breach, not permission to infer silently. "Acts on it silently" is the primary target.**

## Named-bait requirement

Every future room contract carries a room-specific named-bait list — the minimum test inventory, composed only of temptations relevant to that room's lawful context (structurally: deriving a condition from food-pattern data; deriving injury from activity data; aggregating self-reported records toward a diagnosis; emitting an outward-facing signal — named here as *categories of temptation*, never as authored pairs). Each list is **a floor, not a ceiling**, each future bait **maps one-to-one to a future evaluation fixture**, and **Law 8 binds beyond the enumeration.** This record decides the *requirement*; it authors no Wellness, Kitchen, Gym, or Meditation bait list, and designs no fixture contents or code.

## User-requested speculation

The previously open question is **closed**: user-requested speculation inherits the settled safety-surfacing refusal shape (ADR 0002). When a user asks a room to speculate toward an out-of-scope conclusion, the room must: decline to infer or confirm it; avoid repeating or strengthening the suspected pattern; state its lawful boundary; continue only within authorised context; offer a governed review/confirmation route where one exists; and mint no claim, restriction, recommendation, warning, or authority state. **A user request does not create permission**, and the observable-consequence standard applies to a user-prompted inference exactly as to a volunteered one.

## Required single refusal example

Exactly one doctrine example, in canonical placeholders — this is **doctrine-review wording, not final W6 catalogue copy**:

> **User request:** "Does Allergen-X mean Persona-K9 has Condition-Q?"
>
> **Correct room response:** "I can't infer or confirm Condition-Q from this room's authorised context. I can only work with the confirmed information this room is permitted to use. The relevant information can be reviewed or confirmed through the governed profile process."

The lawful shape, without adding another pair: **no *yes*; no *no*; no "possible pattern"; no tentative restatement; no behavioural change based on the suspected association; the boundary is stated; the redirect is only to an already-governed route** (the profile process). No second clinical, pseudo-clinical, diagnostic, food-to-condition, symptom-to-condition, activity-to-injury, medication-to-condition, or equivalent example appears.

## No room-level pattern-flag pathway

The lawful-boundary contrast is architectural: the governed Profile pathway may surface "possible pattern, not confirmed" **only within its existing queue-only authority** (W1-D3); room processing has **no** equivalent pathway. A room cannot write a candidate, note, warning, observation, queue item, profile suggestion, or "for review" inference merely because it noticed something. **A room that notices something outside its granted authority has nowhere lawful to place the noticing** — and that absence is deliberate architecture, not a missing feature. This record creates no new queue or route.

## Violation handling

A confirmed inference-prohibition breach is the **highest public-safety defect class.** The case becomes a **permanent regression fixture**; the **causal path is corrected** and the fixture remains; the defect is **not** closed merely because visible wording was filtered; **output filtering alone is never an adequate remedy** where the forbidden inference still changes behaviour — any remedy must remove or constrain the causal path, not merely conceal its expression. No defect tracker, fixture code, severity enum, or process is designed here.

## Alternatives considered

- **Consequence-based standard + named baits (chosen).** Prohibit the inference constitutionally; make a breach testable by observable consequence; require a per-room named-bait floor mapped to future evals. Chosen because it catches the primary case — acting silently — while remaining falsifiable and buildable.
- **Statement-only standard (rejected).** Treat only an explicit stated conclusion as a breach. Rejected: the core case is *acting without saying*, which a statement-only rule cannot catch.
- **Unenumerated prohibition (rejected).** State "never infer" with no named baits or observable test. Rejected: unfalsifiable — nothing to build a fixture against, and no way to prove the wall holds.
- **Output-filtering remedy (rejected).** Cure breaches by filtering visible wording. Rejected: filtering the statement while the behaviour change persists launders the violation.

## Consequences

- **Easier:** every contract's Inference Prohibitions section has one standard to instantiate; a reviewer can require a named-bait floor and a mapped fixture for each.
- **Easier (evaluation):** the observable-consequence categories give behavioural evals concrete channels to probe, including the silent-action case.
- **Harder (deliberately):** a room may not "helpfully" answer a user's speculative question, hedge a forbidden inference, or quietly change behaviour on a noticing; each fails review.
- **Constrains future work:** the room layer is permanently denied a pattern-flag pathway; violation remedies must correct the causal path; bait lists must stay in canonical placeholders.
- **Preserved honesty:** the standard does not claim structure removes model-side inference within a lawful channel; it makes the prohibition operational and the breach catchable, and keeps the highest-defect posture explicit.

## Non-goals

This record does not decide: the actual Wellness, Kitchen, Gym, or Meditation bait lists; fixture content or code; eval IDs, schemas, harnesses, scoring, or prompts; adapter behaviour; model selection; session mechanics; payload schemas; UI or review surfaces; validator implementation; or any W5 or W6 implementation. It builds no bait list, fixture, adapter, session, prompt, payload, validator, surface, or engine code, and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples beyond the single required placeholder example.

## Public-safety considerations

Role-generic, structural wording throughout — user, room, contract, granted context, inference, profile process, human reviewer, architect, model. No private names, no model names, no private or project lineage. **The named-bait lists are the highest public-safety surface of the contract-drafting work to come:** a bait list written with realistic clinical pairs would itself become a small inference engine in documentation form — a document that teaches the association it exists to prohibit. Therefore, here and in every later contract: **canonical grammar placeholders only** (Persona-K9, Condition-Q, Allergen-X, Medication-A17); no real health data; no realistic clinical pair; no realistic food-to-condition, symptom-to-diagnosis, activity-to-injury, medication-to-condition, or equivalent mapping. The non-canonical ingredient placeholder used in the planning pack is not accepted vocabulary and must not appear; only the canonical set may be used. The single required example (Allergen-X / Condition-Q) is the only placeholder pair in the record; the room-temptation descriptions are structural categories, not authored pairs. No companion framing except where a sentence names a prohibition. No implementation claims — this record states a standard to be realised later, never a built mechanism.

## Dependencies

W0 Law 8 and the no-new-authority discipline; W1-D1 (the absent room→room edges); W1-D2 (consent authorises edges, cannot create them); W1-D3 (the queue-only "possible pattern, not confirmed" Profile pathway); ADR 0002 (the settled safety-surfacing refusal doctrine); ADR 0003 (ceremony); ADR 0016 (the Inference Prohibitions slot this standard fills); ADR 0017 (isolation — the complementary wall); ADR 0018 (scope — the complementary wall); and the W4 runway (W4-AR). All landed and resolvable. This record does **not** depend on W5 or W6.

## Open questions

None at acceptance.

---

*Isolation closes the door between rooms; scope fixes what is on the table inside one. This is the last of the three walls before a model may enter: even a conclusion a room could reach from what it lawfully holds — spoken, hedged, or only acted upon in silence — it may not reach, because a room that notices something forbidden has, by design, nowhere lawful to put the noticing.*
