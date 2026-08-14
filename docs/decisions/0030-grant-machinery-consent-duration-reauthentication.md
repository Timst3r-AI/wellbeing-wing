# 0030 — Grant Machinery, Consent Duration and Re-authentication (DR-W5-03)

**Status:** Accepted by human reviewer, 2026-08-15. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D1**
**Position:** the **third of the seven W5-D1 doctrine records**. It creates no additional deliverable, no additional planning slot, and no eighth record identity.
**Decision mode:** one governed record in three parts — **Part A: Grant construction and lifecycle** · **Part B: Duration, session and re-authentication** · **Part C: Runtime consequence**.
**Constitutional references:** W0 Laws 1, 3, 4, 8, 9, 10, 11, 13. **No law is amended.**
**Resolves:** **W1-D2 §8.1** (consent duration defaults) and **W1-D2 §8.2 / W1-D3 §10.7** (re-authentication for high-stakes grants) — the questions W5-AR §5 assigns here. **Registry `resolves` identifiers to be confirmed at landing-scope time.**

---

**A grant is a bounded, inspectable delegation over one already-declared edge, for one actor, one purpose, one operation and one duration. It can authorise action within that scope and nothing else: it cannot make an edge, make a claim true, make old information new, or quietly become permission for something adjacent. This record gives the grammar its numbers, its lifecycle and its runtime consequence — and keeps every one of those from collapsing into a single ambient flag that says "trusted".**

## Decision question

W1-D2 fixed the consent grammar and left its numbers open. **What are the durations, what does a session mean, when must the user prove present control, and what happens at runtime when a grant cannot be constructed, activated, or continued?**

## Controlling law

- **W0 Law 4** — minimum necessary access: *"the least data, narrowest scope, and shortest duration required for its declared purpose."*
- **W0 Law 10** — consent is scoped, explicit and revocable, per purpose, per scope, per agent, never blanket.
- **W0 Law 11** — the user owns the data; export and erasure are first-class and never gated.
- **W0 Laws 1, 3, 8, 9, 13** — no proactive activity; nothing self-promotes; no inferred cross-room conditions; the Meditation Room's single grantable surface; auditability.
- **W1-D2 §0** — *"Consent authorises edges; it cannot create them"*; consent is the **third axis**, independent of sensitivity and authority; **rights are not grants**.
- **W1-D2 §1** — the **thirteen required grant elements**; *"a grant missing any element is not a valid grant"*; grants are **non-transferable and non-delegable**; **one edge, one purpose, one grant**.
- **W1-D2 §2** — the five grant types and their duration norms.
- **W1-D2 §3** — the six anti-blanket rules, including *"Every grant ends"* and *"declining a grant degrades only the specific delegated task, nothing else."*
- **W1-D2 §4** — the required user-facing disclosure form and its three rules.
- **W1-D2 §5** — revocation's five immediate effects; cascade deferred to W0 OQ 2.
- **W1-D2 §6** — grant and audit records are **C0**, privacy-sensitive by pattern, with **no processing edges**.
- **W1-D1 §5** — the declared edges: E2, E6, E7, E9, E10, E11-W/K/G, M2. **E11 is *"not itself a permitted flow"***.
- **ADR 0001** — *"AI access to health content requires explicit, scoped, user-approved disclosure"*; **no background AI processing of Vault data**; processing disclosure events logged with **actor, scope, recipient class, purpose and time**, the audit trail never containing health content; **vendor disclosure is part of consent, not documentation**.
- **ADR 0024** — structural, content-free refusal that writes no user, room, profile or vault state; nameable recipient; four-surface observability.
- **ADR 0029** — the freshness axis, its vocabulary, and the dependent-operation fail-closed boundary.
- **W5-AR §5 item 3** — the assignment, recording the re-authentication posture as *"proposed, never decided."*

---

# Part A — Grant construction and lifecycle

## A1. Constructability

1. **A grant is constructable only if it expresses all thirteen W1-D2 §1 elements and references one already-declared W1-D1 edge.** The elements are structurally normative, not advisory: **a grant missing any required element is unconstructable**, not merely irregular.

2. **An undeclared edge makes a grant unconstructable.** Consent cannot conjure a flow. A user's "yes" to an unlisted flow is a request for a new edge, which requires its own decision record and constitutional check before a consent question may even be posed. **E11 is a rule, not a flow**; only E11-W, E11-K, E11-G and the other named edges are grantable.

3. **A blanket scope makes a grant unconstructable.** No class-wide scope, no "everything", no generic AI consent. Scope names sections, records or categories.

4. **One edge, one actor, one purpose, one operation, one duration.** Multiple independent purposes or edges may not be combined into one grant for convenience. **The single exception is where W1-D2 already defines a flow as one governed flow** — E2→E3 extraction landing as pending-review drafts is one flow, and E4 approval is the user's own act needing no grant.

5. **A grant can never:** create an edge · establish truth · refresh information · raise authority · transfer itself · delegate itself · widen itself · mutate into another grant · silently reactivate · become ambient permission.

## A2. A grant's meaning is immutable

6. **A grant is an immutable delegation.** Its thirteen elements fix what was delegated, to whom, over what, for how long. **Nothing may alter those elements in place.** A grant's governed meaning at the moment of consent is the meaning it keeps for the rest of its existence and in the audit record forever after.

7. **The governing identity rule.** **Same grant = same immutable delegation. Continued permission after re-affirmation = successor grant. Changed delegation = new grant.**

## A3. Lifecycle

8. **The lifecycle states are:** **`proposed`** · **`declined`** · **`active`** · **`awaiting required re-authentication`** · **`review-due`** · **`expired`** · **`revoked`**.

   The ordinary path is **proposal → activation and use → review and re-affirmation where applicable → expiry or revocation**, with `declined`, `awaiting required re-authentication` and `review-due` as side states.

9. **No freshness vocabulary is used for grants, and `stale` is barred.** `stale` belongs to the information-freshness axis governed by ADR 0029 and has no grant meaning. **W1-D2 §3.2 and §7 use the phrase "a stale grant" and "stale grants"; that is inherited wording, reported and not reproduced.** This record neither amends W1-D2 nor restates its noun; it adopts §3.2's *mechanism* — a standing grant weakens visibly past its review point and does not continue by silence — under governed vocabulary.

10. **`review-due` never extends a grant and is never a freshness label.** It is a **surfacing state** indicating that continued permission beyond the grant's current validity interval requires explicit review and re-affirmation. **It does not itself shorten the already-governed validity interval, confer additional time or scope, or make an otherwise-active grant unusable before expiry.**

11. **`suspended` is deliberately omitted.** W1-D2's only grant-lifecycle use of the word sits inside the inherited stale-grant mechanism, whose terminal outcome this record governs as **expiry** (decision 21). W1-D3's separate use of "suspended" describes **contradicted information items**, which is the other axis entirely. **No distinct, source-grounded grant meaning remains that `proposed`, `declined`, `active`, `awaiting required re-authentication`, `review-due`, `expired` and `revoked` do not already carry**, so the state is not retained by inheritance.

## A4. Successor grants

12. **Re-affirmation never extends, refreshes, touches, mutates or silently renews an existing grant in place.** **Duration is a governed grant element** (W1-D2 §1); altering it would alter the delegation itself.

13. **Explicit review and re-affirmation creates a successor grant**, carrying: **a new grant identity** · **a new validity interval** · **an auditable lineage relationship to the predecessor**.

14. **The predecessor grant retains its original scope, duration and lifecycle history**, and passes to its own terminal state. It is not rewritten, re-dated or reopened.

15. **A successor grant is new permission arising from new explicit consent. It is not resurrection of the predecessor.** **An expired grant never reactivates. A revoked grant never reactivates.**

16. **The lineage relationship must be representable and inspectable** so that a user or auditor can see that this permission continues an earlier one and on what terms each stood. **This record prescribes no field, schema, table, identifier format or storage mechanism** — those are W5-D2's within this meaning.

## A5. Material change requires a new grant

17. **A material change requires a newly constructed grant, never a mutation of the existing one.** The changed request is not authorised by the old grant for the changed part.

18. **The material attributes are:** edge · requesting actor · recipient or processing class · data class or scope · source zone · destination zone · purpose · allowed operation · plaintext status · vendor involvement · **and duration where the changed duration would alter the delegation.**

19. **The old grant is not amended, re-scoped or superseded in place.** It remains recorded with its original meaning and its own lifecycle outcome.

## A6. Revocation

20. **W1-D2 §5's five immediate effects are preserved in full and unaltered:** no future access under the revoked grant · no further processing disclosure events, with in-flight events aborting where technically severable and no new transmission beginning · no new derived outputs · **the audit record remains** · existing derived artefacts flagged as *derived under revoked consent*, acquiring no new uses.

21. **Revocation is terminal for that grant, and revocation is a right, not a request.** It requires no justification and takes effect without negotiation. **A revoked grant never reactivates**; later permission is a new grant under A5. **Revocation is not a review trigger.**

22. **The derived-artefact revocation cascade is not decided here.** It remains W0 Open Question 2 and W1-D2 §5.5's own deferral.

---

# Part B — Duration, session and re-authentication

## B1. Duration defaults

23. **No grant may be unbounded.** W1-D2 §1 and §3.2 already bar it; this record supplies the numbers W1-D2 §8.1 left open, and adds no duration type beyond single-task, session and standing-with-review.

24. **Duration by grant type**, confirming W1-D2 §2's norms and making them operative:

   | Grant type | Edges | Governed duration |
   |---|---|---|
   | **Vault extraction** | E2 | **Single-task only.** Never standing, never background. **Fresh re-authentication at grant time** (B4) |
   | **Profile scoped read** | E6, E7 | **Standing permitted, maximum validity 180 days** (B2) |
   | **AI processing disclosure** | E11-W, E11-K, E11-G, M2 | **Single-task default; session maximum** (B3) |
   | **Vendor disclosure** | E10 | **Per transmission** |
   | **Export preparation** | E9 (preparation step only) | **Single-task** |

25. **Single-task means the one declared operation for the one declared purpose, ending when that operation ends** — whether it completes, fails, or is abandoned. It does not persist to a second operation of the same kind.

## B2. Standing profile-read validity

26. **A standing profile-read grant has a maximum validity of 180 days. This is a hard validity ceiling, not a reminder interval.**

27. **The grant may be reviewed and explicitly re-affirmed before or at that boundary**, which creates a successor grant under A4.

28. **If no explicit review and re-affirmation occurs by the end of the governed validity interval, the grant expires**: it is no longer active or usable; **silence does not renew it; silence does not create a successor**; later permission requires a new lawful grant.

29. **Grant validity and information freshness remain separate axes** (C4). A permission-valid grant does not make the underlying information fresh, and fresh information does not create permission.

## B3. Session

30. **A session is a narrow, user-initiated active authority window.** It is **not** same-day permission, **not** ambient consent, **not** permanent authorisation, and **not** a grant that silently survives later inactivity.

31. **A session may end through:** explicit close or end · logout · **governed inactivity termination, if and only if such a threshold has been lawfully supplied** · expiry · revocation.

32. **A session cannot silently revive.** Once ended by any means, it is ended; a later window is a new session, and any grant bounded by the old session does not extend into it.

33. **Inactivity-based session termination is non-operative.** **No accepted source supplies a numeric inactivity threshold** — W1-D2 §8.1 asks for the session definition and gives no number — and this record does not invent one. **Inactivity-based termination therefore remains non-operative until a later governed decision supplies the threshold.**
   Until that decision exists: **W5-D2 may not invent the number · may not choose a timeout by implementation discretion · and may not claim or implement inactivity expiry.** The other termination causes in decision 31 — explicit close or end, logout, expiry, revocation — are fully operative and unaffected. **A session that has not ended by one of those causes has not ended**, and no implementation may treat elapsed idle time as though it had.

## B4. Re-authentication

34. **Re-authentication proves present user control for the exact grant proposal being activated, and proves nothing else.** It creates **no consent, no scope, no edge, no duration, no permission, and no authority beyond that proof.**

35. **The governed order is fixed, and each step precedes the next:**
   1. **construct the exact grant proposal**;
   2. **make the proposed delegation inspectable to the user**;
   3. **perform fresh re-authentication**;
   4. **obtain or confirm consent for that exact proposal** as required;
   5. **activate only that exact delegation.**

36. **Any material change after re-authentication invalidates that activation path.** The attributes are A5's, together with **duration where the changed duration would alter the delegation**. The changed request requires **a newly constructed grant proposal and fresh re-authentication again** where that grant class requires it.

37. **A successful re-authentication must never become a reusable ambient "recently authenticated" flag capable of activating a differently scoped grant.** It binds to one proposal and expires with that activation path.

38. **E2 / Vault extraction requires fresh re-authentication at grant time. An already-open authenticated session is not sufficient by itself.** The re-authentication binds to the exact E2 grant proposal under decision 35. **Re-authentication does not authorise extraction; the grant does.**

39. **Vendor-hosted C3/C4 plaintext disclosure — conditional only.** **If** later governed model-access doctrine lawfully authorises vendor-hosted processing involving C3/C4 plaintext disclosure, **then** fresh re-authentication is required before that exact disclosure grant may activate. **This record does not authorise vendor-hosted model access, does not authorise C3/C4 disclosure, decides no model-access architecture and no transmission mechanics, and does not imply that any such path currently exists.**

40. **Where a grant class requires re-authentication and it is absent, the grant does not activate.** Its state is `awaiting required re-authentication`, and the consequence is C1's — the dependent operation only.

## B5. Re-authentication provenance

41. **Recorded as governance provenance, not as a defect and not as an amendment.** **W1-D2 §8.2** routed the re-authentication question toward the threat model; **W1-D3 §10.7** routed it toward the threat model likewise; **W1-D5 expressly placed authentication flows out of scope** and therefore did not decide it; and **W5-AR §5 lawfully re-homes the still-open question to this record**, recording that the posture was *"proposed, never decided."* **W1-D5 is not amended, criticised, or treated as defective** — it declined a question that was within its stated exclusions.

---

# Part C — Runtime consequence

## C1. Structural refusal and the dignity rule

42. **A dependent delegated operation does not proceed where:** the grant is unconstructable (A1) · the grant was declined · the grant has expired · the grant has been revoked · required re-authentication is absent · **or the requested scope differs in any material attribute from the grant held** (A5).

43. **Only the dependent delegated operation is withheld or degraded.** This extends W1-D2 §3.5's rule — *"declining a grant degrades only the specific delegated task, nothing else"* — to every condition in decision 42.

44. **Never: block the person · close the room · withdraw unrelated lawful functionality · make consent a condition of access to unrelated services.** The room remains available, the person remains unblocked, and every operation not depending on the missing authority remains available. **Declining permission is not punishment**, and no consequence may be arranged so that declining feels like one.

45. **Rights are never gated.** W1-D2 §0.3 binds in full: the user reading and editing their own records, initiating an export, demanding erasure, or viewing the ledger exercises rights, not grants. **No condition in decision 42 may withhold a right.**

46. **The refusal is structural and content-free**, on ADR 0024's discipline: it echoes no refused content, writes no user, room, profile or vault state, and carries a fixed reason. **A content-free governance event is still recorded** where doctrine requires one.

## C2. Audit and C0 discipline

47. **The recorded lifecycle events are:** grant creation · each use · activation · the re-authentication event where one was required · **review and re-affirmation** · **successor-grant creation** · **the predecessor-lineage link between a successor and the grant it continues** · decline · expiry · revocation · end-of-life. Per **ADR 0001**, processing disclosure events record **actor, scope, recipient class, purpose and time**, and **the audit trail never contains health content**.

48. **Grant and audit records are C0 governance metadata, privacy-sensitive by pattern**, with **no processing edges** (W1-D2 §6). **Grant history must never become** analytics · behavioural profiling · cross-room inference · user scoring · authority scoring · consent-pressure scoring · ambient shadow profiling.

49. **This record establishes what must be recorded and inspectable. It prescribes no storage architecture** — no schema, table, index, retention mechanism or query surface.

## C3. No background authority

50. **Nothing here authorises unattended, scheduled or proactive activity.** Per ADR 0001 and W1-D2 §3.4, **Vault data is never decrypted for AI processing outside a user-initiated, granted task**, and no grant duration — including a standing profile-read grant — creates background authority. **A standing grant means permission persists; it never means activity persists.**

## C4. Axis separation

51. **These distinctions are normative and may not be collapsed:** **authentication ≠ consent · consent ≠ trust · trust ≠ truth · grant ≠ authority beyond its declared edge.**

52. **And equally:** **available ≠ permitted · permitted ≠ true · true-once ≠ true-now · fresh ≠ authorised · authorised ≠ fresh · re-authenticated ≠ consented · consented ≠ universally trusted.**

53. **No runtime may collapse these into one boolean or one ambient "trusted" or "granted" state.** Consent state and authority state remain independent; a grant never raises authority (W1-D2 §0.2, W0 Law 3), and freshness is ADR 0029's alone.

## C5. Boundaries against later records

54. **This record defines lawful grant construction, lifecycle and activation, and nothing downstream of it.** **DR-W5-04** governs payload assembly and payload equality; **DR-W5-05** governs transmission and disclosure mechanics; **DR-W5-06** governs model access. **Their doctrine is not pulled into this record merely because each consumes grants.**

## C6. Deterministic obligations for W5-D2, claiming no behavioural result

55. **Structural obligations, provable without a model:** a grant missing any required element is unconstructable · an undeclared edge is unconstructable · a blanket scope is unconstructable · re-affirmation produces a successor with new identity, new interval and inspectable lineage, leaving the predecessor unaltered · an expired or revoked grant cannot activate · a material change invalidates an activation path · re-authentication cannot activate a differently scoped proposal · refusal writes no state and echoes no content · consent state and authority state remain independent fields.

56. **Nothing here is behavioural proof.** Whether a running system, once built, actually keeps these independent under pressure is **DR-W5-07's architecture and W5-D3/W5-D4's execution**. **`test_D5_T04_granted_and_trusted_never_merge` remains pending on `grant machinery exists`, which is implementation; this record is a prerequisite, not the unblocking event, and no pending-ledger change is proposed.**

---

## Alternatives considered

- **One record in three parts (chosen).** Construction, duration and consequence are one question — a runtime cannot decide what to do at refusal time without knowing what a grant is and how long it lives.
- **Modelling re-affirmation as extending the existing grant (rejected).** Duration is a governed element; extending it in place would silently alter an immutable delegation and destroy the audit meaning of the original consent.
- **Retaining `suspended` from W1-D2 §3.2 (rejected).** Its only grant-lifecycle use sits inside the inherited stale-grant mechanism whose outcome is now governed as expiry; keeping the state by inheritance would carry vocabulary with no distinct meaning.
- **Using freshness vocabulary for grants (rejected firmly).** It would merge the two axes at exactly the point ADR 0029 and W1-D2 §0.2 keep apart.
- **Choosing an inactivity threshold by drafting (rejected).** No accepted source supplies one; inventing it here would resolve a governance question by writing, which is the failure the W5-AR obligations exist to prevent.
- **Deciding the derived-artefact revocation cascade (rejected).** W0 OQ 2 and W1-D2 §5.5 own it.
- **Treating a prior successful re-authentication as reusable within a window (rejected).** It would become an ambient flag able to activate a differently scoped grant — the precise collapse decision 37 bars.

## Consequences

- **W1-D2 §8.1 and §8.2 close**, and W5-D2 may build grant machinery against governed numbers rather than choosing them.
- **A standing profile-read permission now genuinely ends at 180 days.** Users who want continuity must act; the system will not carry them by silence. That is friction, and it is the point.
- **Every continuation produces a new grant record.** Grant history becomes longer and more legible, and §C2's C0 discipline becomes more load-bearing as a result.
- **Harder, deliberately:** an operation will sometimes stop because a grant expired, and the user will meet that. The alternative is permission that quietly outlives the consent that created it.
- **No capability is authorised.** Nothing here builds, stores, authenticates, transmits or contacts a model.

## Constitutional check

- **Law 1** — no background or proactive authority; review surfacing remains an internal flag at next relevant use, never outreach (C3).
- **Law 3** — no grant raises authority; E2 output still lands pending-review regardless of consent wording.
- **Law 4** — minimum necessary is sharpened: shortest duration becomes a governed number, and one-edge-one-grant remains the only expressible request.
- **Law 8** — no grant type exists for cross-room flows or ledger processing; consent cannot invent a channel.
- **Law 9** — M2 remains the Meditation Room's only grantable surface, with its no-output-elsewhere rule intact.
- **Law 10** — scoped, explicit, revocable, per purpose, audited: this record makes each operative at runtime.
- **Law 11** — rights are never gated (C1 decision 45); the user is never blocked.
- **Law 13** — every lifecycle event is a ledger entry, and C2 keeps the ledger from becoming a dataset.
- **No new authority.** No edge, grant type, sensitivity class, authority state, freshness state or namespace is minted. **No existing grant type's duration norm is changed** — the numbers realise W1-D2 §2 rather than replacing it.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: implementation of any kind · a runtime directory · a software or package dependency · UI or consent surfaces · a final copy catalogue or localisation · **an authentication mechanism** · a session-manager implementation · model access · vendor-hosted access · payload construction · transmission mechanics · **the derived-artefact revocation cascade** · an emergency or break-glass pathway · child, dependent or household consent · multi-device grant state · a numeric inactivity threshold · a pending-ledger change or stub conversion · fixture execution · Lane C · W6 · or any W5-D2 milestone. It amends no record. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — user, room, agent, adapter, grant, edge, actor, purpose, operation, duration, recipient class. **No vendor is named**; where W1-D2 §4's disclosure form is referenced it is described, not reproduced with its placeholder. **No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person.** No private names, no model names, no URLs, no project lineage beyond this repository.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D2` · `W1-D3` · `ADR-0001` · `ADR-0003` · `ADR-0024` · `ADR-0029` · `W5-AR`

**`ADR-0001` is retained as direct authority**, not by ancestry: it independently supplies the audit-element content of decision 47, the no-background-processing rule of decision 50, and the requirement that vendor disclosure live in the grant rather than in documentation. **`W1-D5` is deliberately excluded** — it is cited in decision 41 as provenance for a question it declined, which is evidence of routing, not authority relied upon.

## Open boundaries and later ownership

1. **The numeric inactivity threshold.** **Decided in the body at decision 33: inactivity-based termination is non-operative** until a later governed decision supplies the number. **What remains open is the threshold itself, not what happens without one.** **Owner: a later governed decision**, which may sit with the consent-surface design or its own short record. Until it exists the mechanism does not run, and **W5-D2 may not supply the number by implementation discretion.**
2. **Derived-artefact revocation cascade** — W0 OQ 2 / W1-D2 §5.5.
3. **Break-glass and emergency access** — W1-D2 §8.3; no pathway exists and that absence is the current decision.
4. **Child, dependent and household users** — W1-D2 §8.4; constitutionally untreated.
5. **Multi-device grant state** — W1-D2 §8.5; lands with key distribution.
6. **Vendor disclosure wording, localisation and reading level** — W1-D2 §8.6 → **W6**.
7. **Consent fatigue versus review integrity** — W1-D2 §8.7; behavioural, → **DR-W5-07 / W5-D3–D4**.
8. **Payload assembly, transmission mechanics, model access** — **DR-W5-04, DR-W5-05, DR-W5-06.**

---

*The whole record is an argument against one small convenience: a single flag that means "this person is fine, let it through." Every distinction here — authenticated from consented, consented from trusted, trusted from true, permitted from fresh — exists because that flag is what a runtime will build if nobody writes down why it must not.*
