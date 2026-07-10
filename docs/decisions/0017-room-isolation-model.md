# 0017 — Room Isolation Model

**Status:** Accepted by human reviewer, 2026-07-10. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (second doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — the doctrine is decided now; the two mechanism-and-evidence questions it raises are deferred by name to W5.
**Constitutional references:** W0 Law 8 (inference prohibition); the W0 no-new-authority discipline; W1-D1 (the absent room→room edges); W1-D2 (the grant model; processing grants bind to one room); W1-D5 (threat model — cross-room isolation, D5-T12).
**Blocks:** the Processing Boundary section of every room contract (W4-D2 … W4-D5), which instantiates this record's isolation standard; the adapter/processing layer (W5), which must realise the property this record states.

## Decision question

ADR 0016 fixed a Processing Boundary section in every room contract and assigned its content standard to this record. The question it left: **is room separation enforced architecturally — each room's processing interaction occurring in a context that has never held another room's content — or merely by policy, a shared context kept apart by instruction?** And, since W4 must not design W5: **what does "architectural isolation" mean at doctrine level — statable now, enforceable later — without specifying the adapter, the session, or any mechanism?** This record answers both: architectural, stated as a mechanism-independent property.

## Context

W4 is open for governed doctrine and brief work only; ADR 0016 (the Room Contract Template) is the first landed W4 doctrine record, and this is the proposed second. The Wing's differentiation is restraint: rooms are separate jurisdictions with no room→room edge in the sealed data-boundary map, and Law 8 forbids cross-room inference. The engine spine holds, shapes, and moves a person's record with no model anywhere near it. The processing layer that will one day let a model assist inside a single room is W5's, and it is not yet built. This record decides, before that layer exists, the property it must satisfy — so the wall is designed into the architecture rather than left to the model's discipline. It designs no session, names no adapter, and builds nothing.

## Controlling law

- **W0 Law 8 (inference prohibition):** no room may use another room's content. Architectural isolation is the structural enforcement of Law 8 — it removes the channel rather than policing it.
- **W0 no-new-authority discipline:** this record introduces no new edge, class, or authority state; it constrains how a future processing context may be composed, nothing more.
- **W1-D1 (data-boundary map):** there is no room→room edge; the absence is the design. Isolation makes that absence a property of the processing context, not merely of the map.
- **W1-D2 (grant model):** a processing grant is scoped (who, what, why, how long); this record adds that a processing grant binds to exactly one room and the session derives from the grant — a constraint on grant use, not a new grant type.
- **W1-D5 (threat model):** cross-room isolation is a named threat (D5-T12: one model serving multiple rooms carrying context across); this record answers it structurally, with behavioural evals as the complementary control.

## Decision

1. **Architectural isolation is required — it is doctrine, not policy.** Room separation is a property of the structure, not a rule the model is trusted to keep.
2. **Each room's processing interaction must occur in a context that has never contained another room's content.** No shared conversational state across rooms; no reuse of processing state across rooms.
3. **Cross-room content is unreachable, not merely forbidden.** The design goal is the absence of a path, not the presence of a rule against using one.
4. **One processing grant binds exactly one room.** The processing context derives from the grant; a grant that named two rooms could not be constructed.
5. **No interface accepts content from two rooms.** There is no composition point at which two rooms' content could meet.
6. **Processing state is not reused across rooms, including within one sitting.** *"Within one sitting"* means **within any sequence of interactions in which processing state could otherwise be reused, regardless of timing or interface.** ("Session" is deliberately not the controlling term — session mechanics belong to W5.)
7. **Filtering or output controls alone are insufficient.** Suppressing a statement while the underlying context still holds cross-room content leaves the behaviour change intact and launders the violation. Isolation closes the channel; controls on output cannot substitute for a closed channel.
8. **Grant scoping and architectural isolation are separate, complementary walls.** Grant scoping limits *what* enters a room's lawful context; isolation ensures *nothing from another room* is ever in that context. The second wall is not a substitute for the first.
9. **W5 must later realise this property; W4 specifies no mechanism.** This record states the property (unreachability, one-room-per-context, grant-bound derivation) and names the processing/adapter layer as obliged to realise it. It specifies no adapter, session, prompt, payload, or context-window machinery.
10. **Behavioural evaluations still apply.** Structure reduces the channel; it cannot remove model-side inference *within* a lawful channel. Architectural isolation and cross-room inference evals (DR-W4-04's territory) are complementary, not alternatives.
11. **Any future exception requires its own accepted record.** If a case ever makes full architectural isolation genuinely infeasible, it returns as its own decision record — never a silent relaxation. That record must state, at minimum: (a) the affected room or rooms; (b) the precise, evidence-backed infeasibility; (c) the exact bounded scope of the exception; (d) its duration, review date, or sunset condition; (e) the context that remains strictly prohibited; (f) the compensating structural controls and behavioural evaluations; and (g) explicit human-reviewer acceptance. **No silent downgrade from architectural isolation to policy isolation is permitted.**
12. **Meditation receives the uniform isolation standard.** The Meditation Room's Processing Boundary section instantiates the same architectural-isolation standard as every other room. Its *additional* no-outward-signal property is not decided here — it belongs to DR-W4-04 and the Meditation Room's inference-prohibitions section; this record cross-references that boundary but neither duplicates nor pre-decides it.

**Two questions are handed to W5, named as deferred dependencies (not unresolved doctrine questions for this record):** the *display-context-versus-processing-context split* for the room that reads Approved Profile sections, and *per-room context-cost evidence*. The doctrine above is decided now; these two mechanism-and-evidence matters are the adapter era's, and this record neither assumes nor pre-empts them.

## Constitutional check

- **Law 8 is served, not bypassed:** isolation makes the no-cross-room-inference rule a structural property of the processing context rather than a discipline the model must sustain — it fails safe where policy isolation fails open.
- **No new authority:** no new edge, class, or authority state is minted; the record constrains the composition of a future processing context and the binding of an existing grant type, nothing more.
- **The grant model is respected:** W1-D2's grant object is unchanged; this record adds the one-room-per-grant binding as a use constraint, consistent with the scoped-grant design.
- **No law required reinterpretation**, and **no amendment to the Constitution is proposed or required.**

## Alternatives considered

- **Architectural isolation (chosen).** A processing context that has never held another room's content; grant-bound, single-room, unreachable cross-room content. Chosen because it makes Law 8 a property of the structure — the wall holds precisely when the model would otherwise fail.
- **Policy-only separation in a shared context (rejected).** One shared context kept apart by instruction. Rejected: it converts Law 8 from architecture into model discipline and fails exactly when models fail — the case it exists to protect against.
- **Shared context plus filtering / output controls (rejected).** Cross-room content suppressed at input or output within a shared context. Rejected: filtering the statement while the context still holds the content leaves the behaviour change intact; the violation is laundered, not prevented.
- **Hybrid — architectural for high-sensitivity rooms, policy for the rest (rejected).** Rejected: the low-sensitivity rooms are the inference *sources*; a hybrid protects the wrong asset, relaxing exactly the wall that must hold.

## Consequences

- **Easier:** every room contract's Processing Boundary section now has a single, uniform isolation standard to instantiate; the four contracts cannot diverge on what isolation means.
- **Easier (later):** the W5 adapter layer inherits a clear, testable obligation — single-room grant binding, grant-derived context, no two-room interface — rather than a vague instruction to "keep rooms apart."
- **Harder (deliberately):** processing state cannot be reused across rooms even within one sitting; a future design that wants cross-room reuse cannot have it without a full, accepted exception record carrying the ruled minimum contents.
- **Constrains future decisions:** W5 must realise this property; any infeasibility is an exception record, never a silent downgrade; and the two named W5 questions (display-vs-processing split, per-room cost) are the adapter era's to answer within this doctrine, not against it.
- **Preserved honesty:** behavioural evals remain required — the record does not claim structure removes model-side inference within a lawful channel; it claims structure removes the cross-room channel.

## Non-goals

This record does not decide: the adapter vendor or the model; session implementation or lifecycle; prompt construction; payload schema; context-window mechanics; UI or display architecture; persistence; the hosted-versus-local adapter choice; or any W5 implementation. It builds no adapter, session, prompt, payload, validator, surface, or engine code, and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples.

## Public-safety considerations

Generic wording throughout — user, repository, Wing, room, contract, processing context, grant, human reviewer, architect, model. No private names, no model names, no private or project lineage. No real health data and no clinical examples appear; where the room contracts later populate their inference-prohibition sections, grammar placeholders only (Persona-K9, Condition-Q, Allergen-X, Medication-A17) and no realistic clinical pairs. No companion framing appears except where a sentence names a prohibition itself, allowlisted individually per corpus precedent if the wording trips the scan at landing. No implementation claims: this record states a property to be realised later, never a built mechanism.

## Dependencies

W0 Law 8 and the no-new-authority discipline; W1-D1 (the absent room→room edges); W1-D2 (the grant model); W1-D5 (cross-room isolation threat); ADR 0003 (ceremony); ADR 0016 (the room-contract template whose Processing Boundary section this standard fills); and the W4 runway (W4-AR). Two matters are handed forward to W5 as **deferred dependencies, not open questions for this record:** the display-versus-processing-context split, and per-room context-cost evidence. This record does **not** depend on W5 — it constrains it.

## Open questions

**None at acceptance.** The three DR-W4-02-level questions raised in the deliverable brief are resolved in the decisions above: the future-exception record's minimum contents are fixed (decision 11, with no silent downgrade permitted); "within one sitting" is defined once, in plain language, without making "session" the controlling term (decision 6); and the Meditation Room receives the uniform isolation standard while its no-outward-signal property is left to DR-W4-04 (decision 12). The two W5-carried matters are named as deferred dependencies (above), not unresolved questions for this doctrine decision.

---

*Isolation is the wall you don't have to trust anyone to keep. Decide it as architecture now, and no later session, prompt, or model is ever asked to remember which room it is in.*
