# 0031 — Payload Assembly and Payload Equality (DR-W5-04)

**Status:** Accepted by human reviewer, 2026-08-15. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D1**
**Position:** the **fourth of the seven W5-D1 doctrine records**. It creates no additional deliverable, no additional planning slot, and no eighth record identity.
**Decision mode:** one governed record in three parts — **Part A: Payload constructability and authorised assembly** · **Part B: Payload equality and comparison discipline** · **Part C: Runtime consequence, audit, Z4 disposition and boundaries.**
**Constitutional references:** W0 Laws 1, 4, 8, 10, 11, 13. **No law is amended.**
**Owns:** the **Z4 disposition seam** named by W5-AR §6.7.

---

**A grant says what may be sent. It does not say what gets assembled. Between those two facts is the gap where every real system leaks: one more field for context, one more turn of history for coherence, one device identifier the library adds without asking. This record closes the gap by refusing to treat the payload as a separate object with its own judgment. The granted scope is the whole payload, and if the Wing cannot prove that, the operation does not run.**

## Decision question

A valid grant exists. **What exactly may be assembled into a payload, and how does the Wing prove that the payload it assembled, used, compared, recorded, or presented at a boundary is exactly the payload authorised** — not merely similar, useful, adjacent, equivalent in intention, or productive of the same visible output?

## Controlling law

- **W1-D6 §4.J**, the naming source: *"Prove what the grant displayed equals what crossed the boundary — **granted scope == transmitted scope, byte-level where applicable** — with no SDK extras, no helpful context, no room state, no history beyond the grant."*
- **W1-D6 failure example 15**: *"A prompt assembler attempts to include extra context 'to be helpful' — payload equality fails the test; **granted scope is the whole payload**."*
- **W1-D6 §9.5** — a VendorAdapter ADR is required *"before any Z4 integration beyond the E10 grocery-list edge; payload-equality tests are its acceptance gate."*
- **W1-D5 D5-T23** (severity **C**) — *"AI payload over-disclosure (prompt scope creep)"*; the residual named in terms: *"Implementation assembles 'context' beyond the granted scope (system prompts, room state, history)."*
- **W1-D5 D5-T15** — *"Vendor/adapter receives broader payload than disclosed"*; residual *"SDK/integration defaults exfiltrate extras (device IDs, context)"*; mitigation *"byte-level discipline at implementation."*
- **W1-D2 §1** — the thirteen required grant elements, including **scope**, **source zone → destination zone**, **plaintext flag** and **vendor involvement**; **one edge, one purpose, one grant**; grants **non-transferable and non-delegable**.
- **W1-D2 §3** — the anti-blanket rules: no class-wide scopes, no generic AI consent, **no background authority**.
- **W1-D2 §4** — the disclosure form and its rule that *"Nothing else is included."*
- **W1-D2 §5, §6** — revocation's immediate effects; grant and audit records are **C0**, privacy-sensitive by pattern, with **no processing edges**.
- **W1-D1** — the declared edges (E2, E6, E7, E9, E10, E11-W/K/G, M2), the sensitivity classes, and the zones; **E11 is a rule, not a flow**.
- **ADR-0024** — the processing-context boundary; **structural, content-free refusal** writing no user, room, profile or vault state; **nameable recipient**; four-surface observability; *"absence must be demonstrated, not presumed."*
- **ADR-0029** — the freshness axis and its vocabulary; label travel; the dependent-operation fail-closed boundary.
- **ADR-0030** — grants as **immutable delegations**; the material-change attributes; dependent-operation-only refusal; **no ambient trusted or granted state**.
- **ADR-0001** — *"AI access to health content requires explicit, scoped, user-approved disclosure"*; **no background AI processing**; disclosure events logged with **actor, scope, recipient class, purpose and time**, the audit trail never containing health content.
- **W5-AR §5 item 4 and §6.7** — the assignment, and the Z4 seam with its *"no silent third state"* rule.

---

# Part A — Payload constructability and authorised assembly

## A1. What a payload is here

1. **A payload is the content and governed metadata assembled for one operation under one grant, at one boundary.** This record governs its **construction** and its **equality**. It governs no boundary crossing, no transmission mechanism, and no recipient behaviour.

2. **A payload has no independent judgment.** It is not a context, a working set, a prompt, a session, or a place where a runtime may exercise discretion about what would help. **It is a derived object whose permitted content is fully determined by the grant.**

## A2. The north star

3. **Permission is not enough. The assembled payload must match the authorised scope.**

4. **A payload is lawful only if assembled from the exact authorised scope for the exact grant** — matching its **edge · actor · recipient or processing class · purpose · operation · duration · source zone · destination zone · plaintext status · vendor-involvement posture**. These are ADR-0030's material attributes, and a payload that does not match every one of them is not a payload under that grant.

5. **The granted scope is the whole payload.** W1-D6's own words. There is no residue, no envelope, no accompanying context, and no *"and also"*.

6. **Nothing may be added for helpfulness, safety, convenience, continuity, room coherence, model quality, SDK defaults or implementation ease.** Each of these is a real pressure and each is barred by name, because *"to be helpful"* is precisely the reason W1-D6's failure example 15 exists.

## A3. Forbidden inclusion

7. **The following may never enter a payload:** SDK extras · device identifiers · helpful context · room state · conversation history beyond the grant · cross-room context · cached context · adjacent context · inferred enrichment · derived enrichment · **system prompts or hidden instructions carrying user, room or content state beyond the grant** · **and anything included merely because it is already available.**

8. **Availability is not authorisation.** That a datum is loaded, cached, in memory, in the same room, in the same session, or otherwise reachable creates no permission to include it. **Available ≠ permitted** (ADR-0030 C4).

9. **No enrichment may be reintroduced as a transformation.** Summarising, re-describing, expanding, normalising into a richer form, or attaching an explanation that carries information beyond the granted scope are all inclusion, whatever they are called.

10. **A payload assembled from more than one grant is unconstructable.** One edge, one purpose, one grant (W1-D2 §1) carries through to assembly: two grants produce two payloads, never one combined payload.

## A4. Governed metadata

11. **Metadata may be included only where it is governed payload metadata required to enforce scope, freshness, authority, refusal, audit or equality.** It is included because doctrine requires it, never because it is available.

12. **The permitted categories are:** authority labels · ADR-0029 freshness, staleness and unknown labels · grant identity · edge · purpose · operation · actor · recipient or processing class · source and destination zone · plaintext status · vendor-involvement posture · and comparison or audit metadata that contains no payload content.

13. **Metadata must never become hidden enrichment.** A metadata field carrying content, or carrying enough to reconstruct content, is content.

14. **Barred outright**, unless a future governed record explicitly authorises a narrow non-content use: device identifiers · SDK defaults · behavioural-profiling metadata · room-state metadata · user-scoring metadata · authority-scoring metadata · consent-pressure metadata · ambient shadow-profile metadata.

15. **W1-D6 §4.G's label-travel obligation is honoured, not widened.** Authority and staleness labels travel with content because the corpus requires it; **that obligation adds labels, never subject matter.**

## A5. No background or ambient assembly

16. **No payload may be assembled outside a user-initiated, granted operation.** ADR-0001's no-background-processing rule and W1-D2 §3.4's no-background-authority rule both bind at assembly, not merely at transmission.

17. **No payload is pre-assembled, warmed, speculatively built, or retained for reuse.** ADR-0030's bar on ambient permission applies to the artefact as well as the authority: **there is no standing payload.**

---

# Part B — Payload equality and comparison discipline

## B1. What equality means

18. **Payload equality means the authorised and displayed grant scope and the assembled or used payload are equal under the governed comparison form for that boundary.** It is a **directional, scope-anchored identity claim**, not a resemblance judgment.

19. **Where the payload is serialised at the last controllable point, byte-level equality applies where applicable** — W1-D6 §4.J's own standard, and the pending obligation's own words, *"granted scope equals transmitted bytes at the last controllable point, per boundary edge."*

20. **Where byte equality is not meaningful, the comparison must be canonical, structural, field-level and deterministic.** Two runs over the same grant and the same authorised content must produce the same comparison outcome.

21. **None of the following ever satisfies payload equality:** semantic similarity · intention-equivalence · output-equivalence · *"same effect"* · *"same visible answer"* · *"close enough"* · *"equivalent for this purpose"* · or any argument that the difference does not matter. **A difference in governed payload content, required metadata, authorised scope, boundary-relevant field or comparison surface does not become lawful because it is said not to matter. Representation differences may be ignored only where the governed canonical comparison form says they are irrelevant, never by runtime discretion.**

22. **This record chooses no serialisation format, canonicalisation algorithm, hash function, comparison mechanism, schema, table or storage mechanism.** Those are W5-D2's or later, and choosing one here would resolve an implementation question by doctrine.

## B2. The governed comparisons

23. **Three comparisons are doctrinal obligations:**
   - **grant or displayed scope ↔ assembled payload** — that what was authorised is what was built;
   - **assembled payload ↔ the payload at the last controllable point** — that nothing was added between assembly and the boundary;
   - **pre-adapter ↔ post-adapter payload, wherever an adapter transformation exists** — that the transformation preserved scope and added nothing.

24. **Equality is not an assembly-time check alone.** It binds **at the last controllable point, per boundary edge**. A payload that was equal at assembly and unequal at the boundary has failed, and the later measurement governs.

25. **The last controllable point is the last point at which the Wing can observe and refuse.** Beyond it the Wing makes no equality claim, and ADR-0024's bound applies: **the Wing can demonstrate what it did with a payload and does not claim to prove what a recipient does internally.**

## B3. Scope of the boundaries governed now

26. **This record governs the local controllable payload boundary and the last controllable point before any boundary the Wing controls.** That is the Z3 processing-context limb, and it is governed now.

27. **Any later vendor or external boundary remains future-owned while Z4 is dormant** (C3). The equality doctrine here is written so that such a boundary, if ever activated by its own governed record, must satisfy it — **but this record activates nothing.**

## B4. Audit and fingerprints

28. **A content-free comparison result or fingerprint may be recorded only if all five hold:** it does not reveal payload content · it does not become a processing edge · **it does not permit reconstruction of content** · it is used only to prove equality, refusal, lifecycle or audit discipline · and it remains **C0 governance metadata** under W1-D2 §6.

29. **This record prescribes no hash function, storage field, schema, table, index, retention period or query mechanism.**

30. **A fingerprint is never a substitute for the prohibition.** Recording that a payload was over-broad does not make it lawful; the comparison exists to refuse, not to document.

---

# Part C — Runtime consequence, audit, Z4 disposition and boundaries

## C1. Refusal when equality cannot be proven

31. **If payload equality cannot be proven, the dependent delegated operation does not proceed.** Unproven is not presumed-equal. ADR-0024's discipline governs: **absence must be demonstrated, not presumed.**

32. **The refusal is structural and content-free.** It echoes no refused content, carries a fixed reason, and **writes no user, room, profile or vault state.** A content-free governance event may still be recorded.

33. **Only the dependent operation is withheld or degraded** — never block the person · never close the room · **never gate a right** · never withdraw unrelated lawful functionality. This is ADR-0030 C1's rule, unchanged and unextended.

34. **A refusal is never resolved by narrowing the proof.** Where equality cannot be established, the lawful responses are to assemble a payload that does match the grant, or to obtain a grant that matches what is needed — **never to weaken the comparison until it passes.**

## C2. Audit discipline

35. **Payload lifecycle events recorded are:** assembly under a named grant · each comparison and its outcome · refusal · and completion. Per **ADR-0001**, disclosure events record **actor, scope, recipient class, purpose and time**, and **the audit trail never contains health content**.

36. **These records are C0 governance metadata with no processing edges** (W1-D2 §6), and must never become analytics, behavioural profiling, cross-room inference, user scoring, authority scoring or ambient shadow profiling.

## C3. The Z4 disposition — dormant

37. **Z4 remains dormant.** This record does not activate it, and **W5-AR §6.7's "no silent third state" is satisfied by stating the choice rather than leaving it implied.**

38. **The Z4 limb of the payload-equality obligation remains visibly pending.** **W5 may not claim the Z4 obligation discharged.** A W5 that proved equality at Z3 and reported the obligation as met would be the precise failure W5-AR §6.7 names.

39. **Consequently this record does not:** activate E10 · require, author or pre-empt a VendorAdapter ADR · authorise vendor-hosted access · authorise any vendor disclosure · or imply that a vendor boundary currently exists.

40. **The equality doctrine of Part B is written to be boundary-general.** A future Z4 or vendor boundary, if ever activated by its own governed record, **must satisfy it** — and W1-D6 §9.5's rule stands that payload-equality tests are that record's acceptance gate. **Stating the standard a future boundary must meet is not activating the boundary.**

## C4. Freshness interaction

41. **ADR-0029 labels travel with content where the corpus requires it, and freshness never justifies payload expansion.** **Fresh ≠ authorised. Authorised ≠ fresh.**

42. **Unknown and stale labels are payload metadata only where governed.** They create no permission and widen no payload, and a freshness state is never a reason to include additional material to compensate.

## C5. Deterministic obligations for W5-D2, claiming no behavioural result

43. **Structural obligations, provable without a model:** a payload assembled from more than one grant is unconstructable · a payload containing any A3 category is refused · metadata outside A4's permitted categories is refused · the three B2 comparisons are performed and their outcomes recorded · an unproven comparison refuses the dependent operation · refusal writes no state and echoes no content · no payload is assembled outside a user-initiated granted operation · no payload is retained for reuse.

44. **Nothing here is behavioural proof.** Whether a running system, once built, resists the pressure to enrich is **DR-W5-07's architecture and W5-D3/W5-D4's execution.**

45. **This record is a prerequisite for the pending test `test_D5_T15_T23_payload_equality_at_z3_z4`, and does not unblock it.** The live condition reads *"the payload-equality standard record is accepted **and an assembler exists**"* — the second half is implementation. **No pending-ledger change, no stub conversion, no test enablement, and no claim that runtime proof now exists.** The Z4 limb additionally remains pending under C3.

## C6. Boundaries against later records

46. **This record governs what a payload may contain and how its identity is proven, and nothing downstream.** **DR-W5-05** governs transmission and disclosure mechanics; **DR-W5-06** governs model access; **DR-W5-07** governs behavioural evaluation architecture. **Their doctrine is not pulled in merely because each consumes payloads.**

---

## Alternatives considered

- **One record in three parts (chosen).** Assembly and equality are one question: an equality standard with no assembly rule polices nothing, and an assembly rule with no equality standard cannot be proven.
- **Byte equality everywhere (rejected).** W1-D6 says *"byte-level where applicable"*, not always; mandating it would decide a serialisation question this record must not decide.
- **Semantic or output equality (rejected firmly).** It is the exact failure mode D5-T23 describes at severity C, and it would make the standard unfalsifiable.
- **Equality at assembly time only (rejected).** The pending obligation says *"at the last controllable point"*, and an assembler that is honest at build time and an SDK that appends afterwards is precisely D5-T15.
- **Activating Z4 to discharge the obligation cleanly (rejected, ruled).** It would require a VendorAdapter ADR and an E10 activation this record has no authority to make. **Dormant with the limb visibly pending is the honest state.**
- **Reporting the payload-equality obligation as met once Z3 is proven (rejected).** W5-AR §6.7 names this as the failure the pending ledger exists to prevent.
- **Allowing a narrow "operational context" allowance (rejected).** Every leak in D5-T15 and D5-T23 is a narrow allowance that was reasonable when written.
- **Choosing a hash function so fingerprints are well-defined (rejected).** Doctrine sets the five conditions; the mechanism is W5-D2's.

## Consequences

- **W5-D2 may build an assembler against a governed standard** rather than inventing one, and the standard is falsifiable.
- **The payload-equality obligation stays visibly half-open**, because Z4 is dormant. That is uncomfortable and correct, and it is the state W5-AR requires rather than tolerates.
- **Harder, deliberately:** a runtime that could produce a better answer with one more field must not, and will sometimes refuse instead. That is the whole point of the record.
- **Every comparison is a place a system can fail loudly** rather than leak quietly.
- **No capability is authorised.** Nothing here assembles, serialises, transmits, discloses or contacts anything.

## Constitutional check

- **Law 1** — no background or speculative assembly; every payload sits inside a user-initiated granted operation.
- **Law 4** — minimum necessary becomes enforceable at the artefact: the granted scope is the whole payload, so *least data* is not an aspiration but a comparison.
- **Law 8** — no inferred or cross-room material may enter a payload; the assembly path cannot become the inference path Law 8 closes elsewhere.
- **Law 10** — consent stays scoped and explicit: what the grant displayed is what the payload contains, per W1-D2 §4's *"Nothing else is included."*
- **Law 11** — no person is blocked and no right is gated by a failed comparison.
- **Law 13** — comparisons, refusals and lifecycle events are ledger entries, and C2 keeps the ledger from becoming a dataset.
- **No new authority.** No edge, zone, class, grant type, authority state or freshness state is minted; **Z4 is not activated and E10 is not opened.**
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: a payload-assembler implementation · a runtime directory · a software or package dependency · a serialisation format · a canonicalisation algorithm · a hash function · a comparison mechanism · a schema, table, index or storage mechanism · UI or a copy catalogue · model access · vendor-hosted access · transmission mechanics · any actual disclosure · **E10 activation** · **a VendorAdapter ADR** · fixture execution · a pending-ledger change · W5-D2 implementation · DR-W5-05, DR-W5-06 or DR-W5-07 doctrine · Lane C · or W6. It amends no record. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — payload, grant, scope, edge, boundary, comparison, adapter, recipient class, metadata. **No vendor is named and no vendor is contacted.** **No real health data may enter a payload, a fixture, a log, a transcript, an evaluation record or a harness artefact** — W5-AR's synthetic-only discipline extends to runtime, unchanged. No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person. No private names, no model names, no URLs.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D2` · `W1-D5` · `W1-D6` · `ADR-0001` · `ADR-0003` · `ADR-0024` · `ADR-0029` · `ADR-0030` · `W5-AR`

**`W1-D5` is direct here**, unlike in DR-W5-03: **D5-T15 and D5-T23 are the named source of this record's obligation**, and decisions 7, 21 and the alternatives rest on their residual text. **`ADR-0001` is direct**: decision 35's audit-element content and the no-background rule of A5 come from it, not through W1-D2. **`ADR-0003` is direct** as operative Tier J ceremony authority, on the ADR-0029 / ADR-0030 footing.

## Open boundaries and later ownership

1. **The Z4 limb of the payload-equality obligation** — **remains pending**; owner is a future governed record, with W1-D6 §9.5's VendorAdapter gate. **Not discharged here.**
2. **Serialisation, canonicalisation, hashing, comparison mechanism, storage** — **W5-D2.**
3. **Transmission and disclosure mechanics** — **DR-W5-05.** **Model access** — **DR-W5-06.** **Behavioural proof** — **DR-W5-07 / W5-D3–D4.**
4. **Whether any narrow non-content use of a currently barred metadata category is ever permitted** — a future governed record only, per decision 14.
5. **Disclosure wording and surfaces** — **W6.**

---

*The hardest sentence in this record is the one that refuses a better answer. A system that may add one field to be helpful will add it, and the field will be defensible every single time, and the sum of those defensible additions is the thing the user never agreed to. So the rule is not "add only what helps" — it is that the grant already said, and the payload does not get a second opinion.*
