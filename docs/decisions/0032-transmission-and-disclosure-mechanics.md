# 0032 — Transmission and Disclosure Mechanics (DR-W5-05)

**Status:** Accepted by human reviewer, 2026-08-15. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D1**
**Position:** the **fifth of the seven W5-D1 doctrine records**. It creates no additional deliverable, no additional planning slot, and no eighth record identity.
**Decision mode:** one governed record in three parts — **Part A: Transmission and disclosure constructability** · **Part B: Boundary, event and honesty discipline** · **Part C: Runtime consequence, audit, Z4 carry-forward and boundaries.**
**Constitutional references:** W0 Laws 1, 4, 8, 10, 11, 13. **No law is amended.**
**Carries unsoftened:** **W1-D5 OR-2**, per W5-AR §5.5.

---

**Everything before this record could be proved. A grant either has its thirteen elements or it does not; a payload either equals the authorised scope or it does not. This record governs the one boundary where proof runs out. Past it the Wing cannot verify what a recipient does, and the corpus is explicit that the mitigation is honesty rather than control. So the discipline here is different in kind: not "prove it is safe", but "say exactly what is happening, refuse what cannot be authorised, and never claim what cannot be known."**

## Decision question

A valid grant exists and a lawful payload has been assembled and proved equal. **What counts as a transmission or a disclosure, what must be true before anything crosses, what must be recorded, what must be refused — and how is crossing prevented from becoming a second, ungoverned decision point?**

## Controlling law

- **W5-AR §5 item 5** — the assignment, and its instruction that this record is **kept separate from DR-W5-04** because *"assembly and crossing govern different questions, carry different evidence, and fail in different ways."*
- **W5-AR §5.5** — OR-2 *"carried and unsoftened."*
- **W1-D5 OR-2**, verbatim: *"Vendor-hosted model retention is a trust dependency. The grant prohibits retention; **the Wing cannot verify a vendor's compliance from outside.** Mitigation is **disclosure honesty** (the vendor is named in the grant; local models exist as the default preference), **not technical control.**"*
- **W1-D2 §4** — the required user-facing disclosure form, **already fixed and binding**: *"This will send **[the named scoped content]** to **[a model running on this device / a model hosted by VENDOR-NAME]** to **[purpose]**. Nothing else is included. This permission ends **[duration]**."* — with its three rules, including *"If the honest sentence sounds alarming, the sentence is working."*
- **W1-D2 §1** — recipient/processing class **with the vendor named**; source zone → destination zone; **plaintext flag**; **vendor involvement**.
- **W1-D2 §5.2** — on revocation, *"any in-flight event aborts where technically severable, and no new transmission begins."*
- **W1-D2 §6** — grant and audit records are **C0**, privacy-sensitive by pattern, **no processing edges**.
- **W1-D2 §0.3** — **rights are not grants**: export, self-access, erasure and ledger viewing are never consent-gated.
- **W1-D6 §4.G** — the disclosure sentence *"must plainly say what content is sent, to whom, for what purpose, ending when"*, checked against the actual grant.
- **W1-D6 §4.H** — vendor-hosted processing *"must name the vendor/service class in the grant language and state retention uncertainty honestly."*
- **W1-D1** — the declared edges and zones; **E11 is a rule, not a flow**.
- **W1-D5 D5-T15** — *"SDK/integration defaults exfiltrate extras (device IDs, context)"*. **D5-T23** — over-disclosure by assembled context.
- **ADR-0031** — payload equality, the **last controllable point**, and the standing bound that the Wing *"can demonstrate what it did with a payload and does not claim to prove what a recipient does internally."*
- **ADR-0030** — immutable grants; the material-change attributes; **no ambient granted, trusted or authenticated flag**; dependent-operation-only refusal.
- **ADR-0024** — **nameable recipient**, *"a crossing whose recipient cannot be named is refused"*; structural content-free refusal writing no state; four-surface observability.
- **ADR-0029** — freshness kept separate from permission.
- **ADR-0001** — *"Vendor disclosure is part of consent, not documentation"*; disclosure events logged with **actor, scope, recipient class, purpose and time**, the audit trail never containing health content; **no background processing**.

---

# Part A — Transmission and disclosure constructability

## A1. Three gates

1. **Grant permitted, payload equality proved, and transmission authorised are three separate gates.** A lawful grant does not assemble a payload. **A lawful payload does not authorise transmission.** Payload equality does not authorise crossing.

2. **This record governs the third gate only.** ADR-0030 governs the first, ADR-0031 the second. **None of the three substitutes for another**, and passing two is never evidence of the third.

3. **There is no ambient transmission authority.** Per ADR-0030, no flag — granted, trusted, authenticated, recently-verified, session-active — may stand in for a proved transmission gate. **Having a valid session is not transmission authority. Having passed Z3 equality is not transmission authority.**

## A2. What transmission means

4. **Transmission means any deliberate movement, presentation, handoff, send, export delivery, adapter handoff, model call, vendor call, or metadata-bearing transfer by which payload content or governed payload metadata crosses from the Wing's controlled processing context into a distinct recipient, recipient class, file or export artefact, adapter, model, service, vendor, log, telemetry channel, or other boundary context.**

5. **Naming a category as transmission does not activate that category.** This record classifies; it opens nothing. **E10 is not opened, Z4 is not activated, model access is not authorised, and no vendor path is created** by a category appearing in decision 4.

## A3. What disclosure means

6. **Disclosure occurs when payload content, governed payload metadata, or a content-derived representation becomes visible, available, inspectable, retained, transmitted to, or processable by a recipient or recipient class outside the authorised internal assembly context.**

7. **Disclosure is broader than external network send.** A model call, vendor call, adapter handoff, export artefact, logging stream, telemetry channel, or metadata-only transfer **can be disclosure** where it exposes governed payload material or content-derived material.

8. **The two terms are not interchangeable.** Transmission is the act; disclosure is the exposure it produces. **An act may be a transmission that produces no disclosure, and an exposure may be a disclosure without a deliberate send** — both are governed here.

## A4. Recipient and recipient class

9. **The recipient class must be nameable, inspectable, and matched to the grant.** ADR-0024 binds: *"a crossing whose recipient cannot be named is refused."* W1-D2 §4 binds the display side: *"A cloud AI service" is not a valid recipient description.*

10. **A transmission to a different recipient, recipient class, adapter, service, model, vendor, log channel or telemetry channel from the grant is unconstructable or refused.** **No hidden recipient expansion**, and no fan-out to a second recipient under one grant.

11. **Source zone, destination zone, plaintext status and vendor-involvement posture must each match the grant** at the moment of crossing. Any divergence is a material change under ADR-0030 and requires a new grant, never an adjustment at the boundary.

---

# Part B — Boundary, event and honesty discipline

## B1. OR-2, carried unsoftened

12. **The Wing cannot verify vendor retention compliance from outside. The mitigation is disclosure honesty, not technical control.** W1-D5 OR-2 is carried here **unsoftened**, as W5-AR §5.5 requires.

13. **The following claims are barred**, in surfaces, records, doctrine and implementation alike: verified vendor deletion · guaranteed non-retention · technically controlled retention · *private because encrypted in transit* · *safe because contractual* · *harmless because common SDK behaviour* · *not disclosure because automated* · *controlled after boundary crossing*.

14. **If the Wing cannot prove recipient behaviour, it must not claim it.** Where retention is uncertain, the uncertainty is stated honestly, per W1-D6 §4.H.

15. **No comfort language may be added to make a true statement easier to accept.** Softening the honest sentence is consent-shaping, and W1-D2 §4 already bars it.

## B2. The disclosure sentence

16. **W1-D2 §4's disclosure form is fixed and binding.** This record **restates and operationalises it; it does not redesign, soften, narrow or improve it.** Its three rules bind in full: the vendor name is part of the sentence; the plaintext flag renders in words a non-technical reader understands; **and if the honest sentence sounds alarming, the sentence is working.**

17. **The sentence must match the actual crossing, not the intended one.** W1-D6 §4.G checks it against the grant; **a sentence that was true at grant time and false at crossing time has failed**, and the crossing is refused rather than the sentence adjusted.

18. **Exact user-facing wording, localisation, reading level and catalogue form are not decided here.** They are W6's, and W1-D6 §9.10's hosted-mode disclosure language is its own future record.

## B3. The last controllable point, and the limit of claims

19. **The last controllable point is the last point at which the Wing can observe and refuse.** Its meaning is ADR-0031's and is carried forward unchanged.

20. **Beyond that point the Wing makes no claim.** It can demonstrate what it did with a payload; **it does not and may not claim to prove what a recipient does internally.** ADR-0024's bound and OR-2 agree, and neither is weakened here.

## B4. Refused and aborted attempts

21. **A refused or aborted attempt does not create a disclosure event if nothing crossed.** It creates a **content-free governance and refusal event only.**

22. **If anything crossed before the abort, the crossing is a disclosure event and must be recorded honestly.** **The system must not erase the disclosure fact because the operation later failed**, and a partial crossing is a crossing.

23. **A failed outcome never retroactively unmakes an exposure.** No record may describe a crossing that occurred as though it had not.

## B5. Retries, resumptions and duplicate sends

24. **A retry, resumption, duplicate send or replay is a new transmission attempt** unless it is **mechanically proven** to be the same bounded event under **all seven**: the same grant · the same recipient or recipient class · the same payload-equality proof · the same boundary · the same plaintext posture · the same vendor posture · the same user-authorised operation.

25. **Absolutely barred:** silent resend · background retry · **retry after expiry or revocation** · and any retry that changes recipient, payload, governed metadata, plaintext posture, vendor posture or purpose.

26. **This record chooses no retry mechanism, timeout, queue semantics, backoff or transport design.** Those are implementation, and decision 24 constrains their outcome rather than their form.

## B6. Telemetry, logging and error reporting

27. **Logging, telemetry, diagnostics, SDK defaults, crash reports, traces, analytics, monitoring and error reporting are possible transmission and disclosure surfaces.** **They are not exempt because they are operational.**

28. **Content-bearing or content-derived telemetry is disclosure**, and is governed exactly as any other crossing.

29. **Metadata-only telemetry can also be disclosure** where it carries governed metadata, recipient or payload identity, sensitivity class, room or person linkage, or reconstruction risk.

30. **SDK defaults create no authority.** That a library sends something by default is not permission, and D5-T15 names this exact failure — *"SDK/integration defaults exfiltrate extras (device IDs, context)."* **A default is a thing to be refused, not a thing to be inherited.**

## B7. Metadata-only transfer

31. **Metadata-only transfer can be disclosure.** If metadata identifies, describes, classifies, links, reconstructs, profiles or exposes the payload, grant, person, room, edge, sensitivity class or recipient relationship in a governed way, **it is not harmless because the content body is absent.**

32. **Absence of a content body is not a safe harbour**, and no crossing may be justified on the ground that only metadata moved.

## B8. Disclosure records and fingerprints

33. **ADR-0031's content-free fingerprint rule is carried forward.** A disclosure or governance record may contain a content-free comparison result or fingerprint only if **all five hold**: it reveals no payload content · it becomes no processing edge · **it permits no reconstruction** · it is used only for equality, refusal, lifecycle, audit or disclosure accountability · and it remains **C0 governance metadata**.

34. **No hash function, storage field, schema, table, index, retention period, query mechanism or event-store design is prescribed.**

35. **A disclosure record never contains payload content.** ADR-0001 binds: the audit trail never contains health content.

## B9. Revocation and expiry

36. **If revocation, expiry, material mismatch, a missing grant, failed equality or missing transmission authority is detected before crossing, the transmission does not proceed.**

37. **In-flight events abort where technically severable**, per W1-D2 §5.2, and **no new transmission begins.**

38. **If crossing already occurred, the disclosure is recorded honestly and is not claimed to have been undone.** Revocation stops future use; it does not reach backwards through a boundary the Wing does not control.

---

# Part C — Runtime consequence, audit, Z4 carry-forward and boundaries

## C1. Refusal

39. **If transmission authority cannot be proven, the dependent transmission does not proceed.** Unproven is not presumed-authorised.

40. **Refusal is structural and content-free** — it echoes no refused content, carries a fixed reason, and **writes no user, room, profile or vault state** (ADR-0024).

41. **Only the dependent operation is withheld or degraded** — never block the person · never close the room · **never gate a right** · never withdraw unrelated lawful functionality.

42. **A refusal is never resolved by weakening the check.** The lawful responses are to obtain authority that matches, or not to cross.

## C2. Audit

43. **The recorded events are:** transmission attempt · the authority checks and their outcomes · disclosure where a crossing occurred · refusal · abort · and completion. Per **ADR-0001**, disclosure events record **actor, scope, recipient class, purpose and time**.

44. **These records are C0 governance metadata with no processing edges** (W1-D2 §6), and must never become analytics, behavioural profiling, cross-room inference, or any form of scoring.

45. **The record's job is accountability, not reassurance.** It exists so a user can see what left, to whom, and when — including where the answer is uncomfortable.

## C3. Z4 — carried forward, not re-decided

46. **Z4 remains dormant because ADR-0031 made that disposition.** **This record carries that state forward and does not reopen, activate, discharge or supersede it.**

47. **Accordingly:** **no E10 activation** · **no VendorAdapter ADR** authored, required or pre-empted · no vendor-hosted access · no vendor disclosure · and **no claim that the Z4 obligation is discharged.**

48. **Naming vendor categories in decisions 4, 6 and 13 is classification, not activation.** The doctrine is written so that a future governed vendor boundary must satisfy it; **stating a standard is not opening a path.**

## C4. Model access

49. **A model call, if ever authorised, would be a transmission and disclosure surface** and would be governed by this record's mechanics.

50. **Whether model access is permitted at all is DR-W5-06's, and nothing here implies it exists.** **No model call, no model-access doctrine, and no hosted-mode disclosure language is decided here.**

## C5. Export

51. **E9 export is a right, not a grant** (W1-D2 §0.3), and **no right is ever consent-gated by this record.**

52. **Export delivery is classified as a boundary category** where payload content or governed metadata leaves the controlled processing context, so that the crossing is recorded and honest — **not so that it may be blocked.**

53. **Export-warning wording, export implementation, file format and packaging are not decided here.** W1-D6 §9.9's export-warning language is its own future record.

## C6. Freshness

54. **Freshness does not authorise transmission.** **Fresh ≠ authorised. Authorised ≠ fresh. An equal payload is not thereby a transmissible payload.**

55. **ADR-0029 labels travel only as governed metadata** and widen no recipient, purpose, plaintext posture or vendor posture.

## C7. Deterministic obligations for W5-D2, claiming no behavioural result

56. **Structural obligations, provable without a model:** a crossing whose recipient cannot be named is refused · a recipient, class, zone, plaintext or vendor mismatch against the grant is refused · a retry not proven identical on all seven attributes is a new attempt requiring authority · a retry after expiry or revocation is refused · a crossing detected as unauthorised before the boundary does not proceed · a partial crossing is recorded as a disclosure · refusal writes no state and echoes no content · disclosure records contain no payload content.

57. **Nothing here is behavioural proof.** Whether a running system, once built, keeps its telemetry honest is **DR-W5-07's architecture and W5-D3/W5-D4's execution.**

58. **This record unblocks no pending stub.** **No pending-ledger change, no stub conversion, no test enablement, and no claim that transmission or disclosure proof now exists.**

## C8. Boundaries

59. **DR-W5-06** governs model access · **DR-W5-07** governs behavioural evaluation architecture · **W5-D2** implements · **W6** governs surfaces and wording. **Their doctrine is not pulled in merely because each touches a crossing.**

---

## Alternatives considered

- **One record in three parts, kept separate from DR-W5-04 (chosen).** W5-AR requires the separation in terms: assembly and crossing *"fail in different ways."*
- **Treating a proved payload as transmissible (rejected).** It would collapse the third gate into the second and is the failure decision 1 exists to prevent.
- **Defining transmission as external network send only (rejected).** It would exempt model calls, adapter handoffs, exports and telemetry — the surfaces where real leakage happens.
- **Exempting telemetry as operational (rejected firmly).** D5-T15 names SDK defaults as the exfiltration path; an operational exemption would reopen it by another name.
- **Treating metadata-only transfer as harmless (rejected).** Metadata that links a person to a room to an edge is governed material.
- **Softening OR-2 with assurance language (rejected).** W5-AR §5.5 carries it *"unsoftened"*, and every candidate softening in decision 13 is a claim the Wing cannot support.
- **Redesigning W1-D2 §4's sentence for clarity (rejected).** It is fixed and binding; improving it is W6's question at most, and softening it is barred outright.
- **Making a new Z4 ruling (rejected).** ADR-0031 decided it yesterday; re-deciding would reopen a settled disposition without cause.
- **Waiting for DR-W5-06 before writing transmission doctrine (rejected).** W5-AR sequences them separately, and the mechanics are needed whether or not model access is ever permitted.
- **Treating a failed operation as unmaking its partial crossing (rejected).** It is the one form of dishonesty the audit record exists to prevent.

## Consequences

- **W5-D2 may build a transmission path against governed gates** rather than inventing them at the boundary.
- **The Wing will sometimes record an uncomfortable fact** — that something crossed and then failed — and will not be permitted to tidy it away.
- **Harder, deliberately:** telemetry and error reporting now require governance, which is friction exactly where systems normally have none.
- **The record ends with a residual it cannot close.** OR-2 stays open, honestly, because the Wing cannot see past a boundary it does not own.
- **No capability is authorised.** Nothing here sends, calls, exports, logs or contacts anything.

## Constitutional check

- **Law 1** — no background retry, no proactive send, no unattended crossing.
- **Law 4** — minimum necessary is enforced at the boundary as well as at assembly: the recipient, zone and posture must match, not merely be plausible.
- **Law 8** — no crossing may carry cross-room material or become an inference channel.
- **Law 10** — consent stays scoped and explicit: the disclosure sentence must match the actual crossing, and vendor naming is part of consent, not documentation.
- **Law 11** — rights are never gated; export remains a right and no person is blocked by a refused crossing.
- **Law 13** — every attempt, refusal, abort and disclosure is a ledger event, and C2 keeps the ledger from becoming a dataset.
- **No new authority.** No edge, zone, class, grant type, recipient class or namespace is minted; **Z4 stays dormant, E10 stays unopened, and no model path is created.**
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: transmission implementation · a runtime directory · a network client, library or protocol · SDK integration · a retry mechanism, timeout or queue semantics · a payload assembler · model access or any model call · vendor-hosted access · **E10 activation** · **a VendorAdapter ADR** · a schema, table, index or storage mechanism · UI or a copy catalogue · **export-warning wording** · **hosted-mode disclosure language** · fixture execution · a pending-ledger change · W5-D2 implementation · DR-W5-06 or DR-W5-07 doctrine · Lane C · or W6. It amends no record. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — payload, grant, recipient class, boundary, crossing, adapter, channel, posture. **No real vendor is named and no vendor is contacted**; W1-D2 §4's fixed disclosure form is quoted once because it is controlling law, and `VENDOR-NAME` is a template placeholder, not a vendor identity. **No real health data may enter a payload, a log, a transcript, a disclosure record or a telemetry channel** — W5-AR's synthetic-only discipline extends to runtime, unchanged. No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D2` · `W1-D5` · `W1-D6` · `ADR-0001` · `ADR-0003` · `ADR-0024` · `ADR-0029` · `ADR-0030` · `ADR-0031` · `W5-AR`

**`W1-D5` is direct** — OR-2 is a named assigned source and D5-T15 still bears on decision 30. **`W1-D6` is direct** — §4.G and §4.H are the honesty-grading obligations, and §9.9/§9.10 fix boundaries this record must not cross. **`ADR-0031` is direct and required** — the last controllable point and the equality proof are the preconditions this record starts from. **`ADR-0001` is direct** — decision 43's audit elements and decision 35's no-health-content rule come from it, and *"vendor disclosure is part of consent"* underpins B1. **`ADR-0003` is direct** as operative Tier J ceremony authority.

## Open boundaries and later ownership

1. **OR-2 remains an open residual** — unfixable by this or any record while the boundary is not the Wing's. **Owner: none; it is carried, not closed.**
2. **The Z4 limb of the payload-equality obligation** — remains pending under ADR-0031; **not touched here.**
3. **Model access** — **DR-W5-06.** **Behavioural proof** — **DR-W5-07 / W5-D3–D4.**
4. **Transport, retry, queue, timeout, logging mechanism, event store** — **W5-D2.**
5. **Export-warning wording (W1-D6 §9.9) · hosted-mode disclosure language (§9.10) · surfaces, localisation and reading level** — **W6 or their own records.**

---

*Every other record in this phase ends by proving something. This one ends by admitting what cannot be proved, and then refusing to let that admission be quietly reworded into comfort. The Wing does not get to say the data is safe once it has left. It gets to say exactly what left, and to whom, and that it cannot see what happens next — which is worth more than a reassurance that would not have been true.*
