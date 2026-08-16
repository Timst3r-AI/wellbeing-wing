# 0033 — Model Access (DR-W5-06)

**Status:** Accepted by human reviewer, 2026-08-16. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D1**
**Position:** the **sixth of the seven W5-D1 doctrine records**. It creates no additional deliverable, no additional planning slot, and no eighth record identity.
**Decision mode:** one governed record in three parts — **Part A: Model-access constructability** · **Part B: Model-output authority, storage and refusal** · **Part C: Local/hosted boundary, residuals and future ownership.**
**Constitutional references:** W0 Laws 1, 3, 4, 6, 8, 9, 10, 11, 13; W0 §10. **No law is amended.**
**Carries unsoftened:** **W1-D5 OR-2**, per W5-AR §5.5 and §5.3.
**Resolves:** none. W0 Open Question 10 was resolved by ADR-0024; the pending ledger's *"model access is decided"* is a condition string, not a registered identifier. **Registry `resolves` to be confirmed empty at landing-scope time.**

---

**Five records built everything around this decision and each one declined to make it. ADR-0024 built the only room a model could ever be in; ADR-0030 the only authority it could run under; ADR-0031 the only thing it could be handed; ADR-0032 the only way anything reaches it — and every one ended by saying the door itself was not theirs to open. This is the door decision. It opens one class of door, in doctrine only, on the user's own device, under every gate already built — and it leaves every other door exactly as it found it, including the ones whose standards it writes down.**

## Decision question

**Under what governed conditions may the Wing access a model at all — what kinds of model access are allowed or barred, what must be true before access can be attempted — and how is "model access" prevented from silently becoming vendor disclosure, background processing, diagnosis, authority, or implementation permission?**

## Controlling law

- **W5-AR §5 item 6** — the assignment, verbatim: *"DR-W5-06 — Model Access. The pending ledger's condition 'model access is decided' gates two behavioural stubs. A decision, not an implementation — and any model SDK it implies is a separate Tier F dependency crossing (§5.2)."*
- **W5-AR §5.3** — the model-access fence: *"No model has ever been contacted by this repository, and none may be until a record decides model access."* ADR-0001's local-first posture and local-model preference are *"the starting position, not a formality to be argued past."*
- **W5-AR §5.5** — OR-2 *"carried and unsoftened."* **W1-D5 OR-2**, verbatim: *"The grant prohibits retention; the Wing cannot verify a vendor's compliance from outside. Mitigation is disclosure honesty (the vendor is named in the grant; local models exist as the default preference), not technical control."*
- **ADR-0032 decisions 49–50** — a model call, if ever authorised, is a transmission and disclosure surface under ADR-0032's mechanics, and *"whether model access is permitted at all is DR-W5-06's."*
- **ADR-0031** — the lawful payload, payload equality, the last controllable point; **Z4 dormant with the equality limb visibly pending.**
- **ADR-0030** — immutable grants; decision 24's duration table (AI processing disclosure: **single-task default, session maximum**); decision 39's **conditional** vendor-hosted C3/C4 re-authentication; **no ambient granted, trusted or authenticated flag**; no background authority.
- **ADR-0024** — the single AIAdapter seam; every crossing a processing disclosure event; **decision 15: whether the model runs on the user's own device or is hosted by a named vendor is a property of the recipient class inside the grant, "not a different boundary and not a different set of rules"**; decision 17a's nameable recipient; decision 18c's agent-origin labelling; **decision 19: E12 remains reserved.**
- **ADR-0029** — freshness kept separate from authority and permission; unknown is never absence.
- **W1-D1** — the whitelist; **Z3** (*"local model or named vendor model"*), **Z4** (*"non-AI external services behind a VendorAdapter"*), **Z5** (*"only via Z3 rules"*); the declared processing edges E2, E11-W, E11-K, E11-G, M2; **E11 is a rule, not a flow**; E12 reserved; plaintext in Z1 and Z3 only.
- **W1-D2 §1** — the thirteen grant elements, including **recipient / processing class**: *"local model, vendor-hosted model … with the vendor/service named whenever non-user infrastructure receives the payload."* **§3.3** — no generic AI consent. **§3.4** — no background authority. **§4** — the fixed disclosure form, whose local branch reads *"a model running on this device."*
- **W1-D5** — D5-T05 (repetition treated as confirmation), **D5-T06 (AI output becomes authority — severity C)**, OR-3 (*"a model can still err within a lawful channel"*).
- **W1-D6 §3.3** — a test's ground truth is the governed record, *"never a model's opinion"*; **§3.8** — passing tests must not mint authority; **§3.9** — tests prove behaviour, not truth; §6 example 13 — local presented as the default preference; **§9.10 — hosted-mode disclosure language is its own future record.**
- **ADR-0001** — *"AI access to health content requires explicit, scoped, user-approved disclosure"*; **no background AI processing of Vault data**; disclosure events logged with actor, scope, recipient class, purpose and time, the audit trail never containing health content; **vendor disclosure is part of consent, not documentation.**
- **W0 Law 3** — *"model confidence"* does not create authority; **Law 6** — the Wing never decides or prescribes; **§10** — no impersonation, and *"one agent's output is another agent's unverified input, never its evidence."*

---

# Part A — Model-access constructability

## A1. The door decision

1. **Model access is its own authority question, and nothing else answers it.** It is not created by a valid grant, a lawful payload, payload equality, transmission authority, model availability, session activity, authentication, or evaluation need. **Each of those can be present, together, and model access still not exist.**

2. **A model is not a mind, not a clinician, not a companion, not a source of truth, and not an authority.** Model access, where permitted, is a **bounded processing act** under a declared edge, a valid grant, a lawful payload, payload equality, and transmission and disclosure mechanics — never a relationship, a presence, or a standing capability.

3. **This record decides whether and on what conditions the model recipient class is constructable at all.** It is doctrine only: it opens no physical path, contacts nothing, and authorises no artefact.

## A2. What model access means

4. **Model access occurs wherever an operation's grant carries the recipient / processing class *local model* or *vendor-hosted model*** (W1-D2 §1). The definition is anchored in the grant grammar, never in an edge list or an implementation: **the governed term is the recipient class.**

5. **Every model access is a Z3 processing disclosure event through the single AIAdapter seam** (ADR-0024 decision 1), and **every model call is a transmission and a disclosure surface under ADR-0032** — including on the user's own device. The local case differs in what the disclosure sentence says and in vendor posture, never in whether the mechanics apply.

6. **The declared edges that can carry a model recipient class are E2, E11-W, E11-K, E11-G and M2 — and no other.** The W1-D1 whitelist binds; naming these edges activates nothing and widens nothing. **M2 access additionally carries the Meditation Room's no-output-elsewhere rule in full** (W0 Law 9).

7. **Model access is an act under one grant, never a state.** There is no standing connection, no "connected model", no warm model, no ambient availability, and no access that outlives the grant that authorised it.

## A3. The local model class — doctrinally constructable

8. **The local model class is doctrinally constructable.** The class means exactly the *"a model running on this device"* branch of W1-D2 §4's fixed disclosure form: **no non-user infrastructure receives the payload**, which is also why W1-D2 §1's vendor-naming trigger does not fire for it.

9. **A local model access is lawful in doctrine only under all of the following, together:** a valid **activated** grant under ADR-0030 whose recipient class says so · a lawful payload under ADR-0031 · **proven payload equality** under ADR-0031 · **proven transmission and disclosure authority** under ADR-0032 · the ADR-0024 processing-context boundary whole and undiminished · **no background processing** · **no ambient model permission** · single-task default and session maximum where ADR-0030's duration table applies. **A local model access missing any of these is unconstructable or refused, never degraded into.**

10. **Doctrinally constructable does not mean a runtime exists.** This record installs, calls, selects, configures and contacts **nothing**. No model runs, no model is chosen, and the repository remains a repository that has never contacted a model.

11. **Every physical artefact remains separately fenced.** Any runtime, SDK, client, directory, provider, model binary, credential, transport, prompt or implementation of any kind is **W5-D2's, behind its own Tier F crossing with its zero-dependency alternative stated** (W5-AR §5.2) — never implied into existence by this record.

## A4. The vendor-hosted model class — not opened

12. **Vendor-hosted model access is not opened.** No hosted model path exists, none is created, and none is scheduled, required or pre-empted by this record.

13. **The conditions any future opening must already meet are stated now, in ink:** it arrives only by its own governed record with its own constitutional check · it **carries OR-2 unsoftened into its own text and its disclosure language, permanently** · the vendor or service is **named in the grant itself** (W1-D2 §1, §4; ADR-0001) · W1-D2 §4's disclosure form binds, unredesigned and unsoftened · **fresh re-authentication applies where ADR-0030 decision 39's condition is met** · every grant, payload, equality, transmission and model-access gate applies in full · **retention uncertainty is stated honestly** (W1-D6 §4.H) · and **no claim is made about vendor behaviour beyond what the Wing can prove** — ADR-0032 decision 13's barred claims bind every description of hosted processing.

14. **Stating the standard is not opening the path** (ADR-0032 decision 48's rule, applied here). A future record that seeks to open the class inherits these conditions; nothing inherits an opening.

15. **ADR-0030 decision 39 remains conditional.** Its *"if"* is not converted into a *"when"* by this record, and nothing here implies that a vendor-hosted path is expected, planned or inevitable.

## A5. Z3 / Z4 non-conflation

16. **Vendor-hosted model access is a Z3 recipient-class question, not a Z4 / E10 / VendorAdapter question.** W1-D1 defines Z4 as **non-AI** external services behind a VendorAdapter; ADR-0024 decision 15 places local-versus-hosted inside the grant's recipient class. **This distinction is stated as mandatory doctrine because the word "vendor" appears in both places and conflation in either direction is a live failure mode.**

17. **Accordingly, in both directions:** Z4 dormancy is **not** the reason vendor-hosted model access is closed, and no model-access ruling here touches Z4. **Z4 remains dormant · E10 remains unopened · no VendorAdapter ADR is authored, required, pre-empted or discharged · no claim is made that any Z4 obligation is satisfied · and the Z4 limb of the payload-equality obligation remains visibly pending under ADR-0031.**

## A6. E12 / Z5 — reserved, not reopened

18. **E12 remains reserved and Z5 is not opened.** Connected AI systems are a different question from model access and are not reopened, advanced or foreclosed here. **This record governs model access inside the W5 AIAdapter / Z3 grammar — the declared E2, E11-family and M2 crossings — and nothing beyond it.** ADR-0024's recorded E12 prerequisites remain available to any future record that genuinely needs a Z5 connection; none is needed for anything decided here.

## A7. Relationship to the gates, and the anti-collapse chain

19. **Grant, payload equality, transmission authority and model access are four separate questions.** ADR-0030 governs the first, ADR-0031 the second, ADR-0032 the third, this record the fourth. **Passing any three is never evidence of the fourth**, and no flag — granted, trusted, authenticated, recently-verified, session-active, model-available — may stand in for proven model-access authority.

20. **No background model processing and no ambient model permission exist under any reading of this record.** Every runtime model access sits inside a user-initiated, granted operation (ADR-0001; W1-D2 §3.4; ADR-0030 decision 50), and no duration, including a standing profile-read grant, creates background model authority.

21. **The anti-collapse chain, normative and non-collapsible:** **grant ≠ consent · consent ≠ trust · trust ≠ truth · payload equality ≠ permission to call · transmission authority ≠ permission to use a model · model output ≠ evidence · model output ≠ clinical advice · model availability ≠ implementation authority · local class doctrinally constructable ≠ runtime exists · hosted standard stated ≠ hosted path opened.** No runtime, record or summary may collapse any link of this chain into another.

---

# Part B — Model-output authority, storage and refusal

## B1. Model-output status

22. **Model output is agent-origin by construction** (ADR-0024 decision 18c). It carries no authority, cannot be relabelled at or after the boundary, and arrives everywhere as *"unverified input, never … evidence"* (W0 §10).

23. **Model output is never evidence, never clinical truth, never diagnosis, never authority, and never ground truth for any test** (W1-D6 §3.3). **It is never proof that an uncertain health-relevant fact is present, absent, resolved or safe.**

24. **Model output may be a proposal or suggestion only, and only inside the edge and grant that authorised the processing.** It leaves its processing context only through an authorised edge or governed artefact (ADR-0024 decision 10), and it never self-promotes: repetition, retrieval frequency, model confidence and apparent relevance create no authority (W0 Law 3).

25. **Model output never mints authority for any datum, label, record or person.** A green result, a fluent summary, or a confident restatement changes no authority state and no freshness state, anywhere, ever.

## B2. The stored-state rule

26. **Model output may not write directly to the Vault, the health profile, room state, the user profile, memory, or any persisted state.** No such write interface exists, and none is created.

27. **Model output may reach stored state only through an already-declared edge and the governed act that edge requires:** extracted output lands only as **agent-extracted, pending review** where an existing edge permits that landing (E3) · **promotion is the user's act** (E4) · **saving is the user's act** (E8). **No model-to-vault, model-to-profile, model-to-room or model-to-memory write edge is created**, and the W1-D1 anti-map continues to exclude them all.

28. **No processing-side state survives the context** (ADR-0024 decision 10, carried unchanged). Output that did not lawfully leave is not retained, cached, summarised or carried forward by any mechanism.

## B3. The freshness boundary

29. **Freshness does not authorise model access, and model access does not touch freshness.** Fresh ≠ authorised; authorised ≠ fresh (ADR-0029; ADR-0032 C6). ADR-0029's labels travel with payload content as governed metadata only, and widen nothing.

30. **Unknown does not mean absent, and stale does not mean safe.** A model given degraded, expired or unknown context acquires no licence to treat the uncertain fact as absent or resolved — and **whether it nevertheless behaves that way is DR-W5-07's question, not this record's claim.**

31. **Model output does not refresh anything.** Renewal is a review act (W1-D3 §2, as carried by ADR-0029); no model restatement re-dates, re-confirms or renews any item, and **a model cannot convert unknown into known by fluent wording** (W1-D6 §3.6's rule that fluency is not correctness, applied at the boundary).

## B4. Runtime processing and evaluation-era instrument access

32. **Two categories of model access are separated, and neither implies the other:**
    - **Granted runtime processing** — a person's content · one declared edge · a valid activated grant · the Z3 model recipient class · every gate in decision 9.
    - **Evaluation-era instrument access** — **synthetic and public-safe content only · no person · no user grant · no health content · no real room state** · governed by DR-W5-07's harness architecture before any execution exists.

33. **Evaluation-era instrument access is decided to be a lawful category, and only that.** Harness method, prompts, providers, fixtures, execution, observation records and test conversion are **DR-W5-07's and W5-D3/W5-D4's**, and none is designed, scheduled or implied here.

34. **Instrument access is never a channel to a person.** It receives no user content, holds no real grants, sees no real room state; its artefacts are governed artefacts under the synthetic-only discipline and the public-safety scan (W5-AR §10), exactly as documents are.

35. **Neither category authorises the other.** Instrument access confers no runtime permission over user content, and runtime doctrine confers no execution of any evaluation.

## B5. The pending ledger

36. **Acceptance of this record satisfies exactly one conjunct of exactly two pending conditions** — the *"model access is decided"* half of `test_D5_T05_repetition_resistance_behavioural` and `test_D5_T06_authority_laundering_resistance` — **and both stubs remain pending, because the behavioural harness does not exist.**

37. **No pending-ledger change, no stub conversion, no test enablement, and no claim that behavioural proof exists.** This record is a prerequisite, never the unblocking event, on the ADR-0030/0031/0032 pattern.

## B6. Refusal

38. **If model-access authority cannot be proven, the dependent model access does not proceed.** Unproven is not presumed-authorised.

39. **Refusal is structural and content-free:** it echoes no refused content, carries a fixed reason, and **writes no user, room, profile, vault or memory state** (ADR-0024). A content-free governance event may still be recorded where doctrine requires one.

40. **Only the dependent operation is withheld or degraded** — never block the person · never close the room · **never gate a right** · never withdraw unrelated lawful functionality. **A refusal is never resolved by weakening the check**; the lawful responses are to obtain authority that matches, or not to access.

## B7. Audit and governance metadata

41. **The recorded events are:** model-access attempt · the authority checks and their outcomes · refusal · abort · disclosure where a crossing occurred · completion · and the **agent-origin status of any output**. Per ADR-0001, disclosure events record **actor, scope, recipient class, purpose and time**, and the audit trail never contains health content.

42. **The model recipient class must be nameable and inspectable in the grant's own terms** (ADR-0024 decision 17a; W1-D2 §4). **Where determinable, model identity, model class, locality and hosting posture, and vendor or service identity are recorded as C0 governance metadata sufficient for audit and refusal.** This is a property requirement on the record, not a new grant element: **the thirteen W1-D2 §1 elements are fixed and this record adds none.**

43. **No schema, field name, versioning mechanism, SDK identifier, model registry, table or storage design is prescribed.** Those are W5-D2's, within these meanings.

44. **These records are C0 governance metadata with no processing edges** (W1-D2 §6), and must never become analytics, behavioural profiling, cross-room inference, or any form of scoring.

---

# Part C — Local/hosted boundary, residuals and future ownership

## C1. The local-first posture

45. **ADR-0001's local-first posture and its local-model default preference are carried as the starting position** (W5-AR §5.3), and the local class is the **only** class this record makes constructable. **Where a choice between a local and a vendor-hosted model is ever presented, local is the default preference** (W1-D6 §6 example 13) — the presentation itself is W6's.

## C2. OR-2 — carried, not triggered

46. **OR-2 is carried unsoftened and remains unclosable by design.** While no vendor-hosted class is open, **OR-2 is carried, not triggered**: the Wing runs no boundary it cannot see past. Any future hosted opening carries the residual into its own text and disclosure language, permanently, and every softening ADR-0032 decision 13 bars stays barred.

## C3. The ADR-0004 residue boundary

47. **This record does not resolve ADR-0024 open question 6.** Whether ADR-0004's plaintext-residue doctrine reaches the transient Z3 boundary **remains a mandatory check before any W5-D2 implementation**, handled as its own pre-W5-D2 gate or separate governed record after the W5-D1 doctrine set is complete. **A brief may not settle it, and this record's silence on its answer is deliberate boundary, not disposition.**

## C4. The context-cost evidence spike

48. **No context-cost evidence spike is required before this record.** A class-level doctrine decision does not depend on cost evidence; the spike (ADR-0017's second carried question, under the ADR-0007 discipline) **remains available to W5-D2 and implementation planning**, findings only, with no reserved record number.

## C5. Observability and determinism — the joint seam held open

49. **Nothing decided here forecloses four-surface observability or paired-variant execution** (ADR-0024 decision 13). Any model class later implemented must be able to satisfy the boundary's observability by construction, and **what a fixture pass means under a non-deterministic model remains DR-W5-07's half of the jointly held question** (ADR-0024 open question 1). This record holds its half by constraining no answer.

## C6. Deterministic obligations for W5-D2, claiming no behavioural result

50. **Structural obligations, provable without a model:** a grant carrying a model recipient class outside the doctrinally constructable class is unconstructable or refused · a model access missing any decision-9 gate does not proceed · no interface exists by which model output writes directly to vault, profile, room, or memory state · model output is labelled agent-origin by construction · refusal writes no state and echoes no content · model-access events are recorded content-free · no standing model connection exists · instrument access has no path to user content.

51. **Nothing here is behavioural proof.** Whether a model, once one exists and is lawfully reachable, resists repetition, laundering, or silent inference is **DR-W5-07's architecture and W5-D3/W5-D4's execution** — and OR-3 stands: *"a model can still err within a lawful channel."*

## C7. Boundaries

52. **W5-D2** implements, behind its own briefs and Tier F crossings · **DR-W5-07** governs behavioural evaluation architecture, observation records, `execution_status` and the T12 seam · **W6** governs surfaces, presentation and wording · **hosted-mode disclosure language is its own future record** (W1-D6 §9.10) · **Lane C** is untouched. **Their doctrine is not pulled in merely because each touches a model.**

---

## Alternatives considered

- **One record in three parts (chosen).** Constructability, output status and residuals are one decision: a door ruling with no output doctrine would open a channel with ungoverned contents, and output doctrine with no door ruling would govern the contents of a channel nobody lawfully has.
- **Deciding conditions only, with no class ruling (rejected).** It would satisfy *"model access is decided"* in name while deciding nothing, and the door decision would then be made by the first W5-D2 milestone that needed it — resolving a sealed question by building.
- **Opening both classes now (rejected firmly).** No source requires a hosted opening; OR-2's obligations would attach to a capability the Wing cannot describe honestly because it does not exist; and the corpus's local default preference is the starting position, not a tie-breaker.
- **Gating vendor-hosted model access on Z4 / the VendorAdapter ADR (rejected as a category error).** W1-D1 makes Z4 non-AI and ADR-0024 decision 15 makes locality a recipient-class property; borrowing Z4's dormancy as the closure mechanism would entrench the exact conflation A5 exists to prevent.
- **Defining model access by an edge list rather than the grant grammar (rejected).** The recipient class is the governed term; an edge-enumerated definition would invite a future edge to smuggle access past the definition.
- **Requiring fresh re-authentication for every model call (rejected).** No accepted source supplies it; ADR-0030's postures govern; minting a stricter blanket rule here would invent authority doctrine outside the assignment.
- **Making model identity a fourteenth grant element (rejected).** The thirteen elements are fixed; identity and posture belong to governance metadata, per decision 42.
- **Placing the ADR-0004 residue applicability check inside this record (rejected, ruled).** It is a scope addition the assignment does not contain; it remains its own mandatory pre-W5-D2 gate.
- **Waiting for context-cost evidence before deciding (rejected).** The class-level decision does not depend on cost, and the spike remains available to the deliverable whose decisions do.

## Consequences

- **The door has a doctrine.** W5-D2 may design for the local class against governed conditions rather than assumptions, and the evaluation era may name its instrument category lawfully.
- **The hosted door stays closed with its standard visible.** A future record that wants it open inherits the conditions in ink rather than negotiating them at the boundary.
- **Harder, deliberately:** a runtime cannot acquire a model by convenience. Every physical artefact — runtime, SDK, directory, credential — arrives behind its own Tier F authorisation or it does not arrive.
- **Both behavioural stubs remain pending**, half-unblocked and honestly so, until a harness exists.
- **No capability is authorised.** Nothing here runs, installs, selects, configures, calls or contacts any model, and the repository has still never contacted one.

## Constitutional check

- **Law 1** — no background, ambient, scheduled or standing model access; every runtime access sits inside a user-initiated granted operation, and the Wing still contacts no one.
- **Law 3** — nothing self-promotes: model output is agent-origin forever until a user act, and confidence, repetition and fluency mint nothing.
- **Law 4** — minimum necessary carried whole: access exists only under one grant's scope, through a boundary that cannot fetch and a payload that cannot exceed the grant.
- **Law 6** — the Wing never decides or prescribes: output is never clinical truth or diagnosis, and a refusal asserts nothing about anyone.
- **Law 8** — no new channel: model access adds no cross-room path, instrument access carries no user content, and the anti-map's absences all stand.
- **Law 9** — M2 remains the Meditation Room's only processing edge; its no-output-elsewhere rule is carried inside the grant type this record consumes unchanged.
- **Law 10** — consent stays scoped and explicit: the recipient class is named in the grant's own terms, no generic AI consent is expressible, and vendor naming binds any future hosted opening.
- **Law 11** — rights are never gated: no refusal blocks the person, closes a room, or withholds export, erasure, self-access or ledger view.
- **Law 13** — every attempt, check, refusal, crossing and completion is a content-free C0 ledger event, and B7 keeps the ledger from becoming a dataset.
- **W0 §10** — impersonation prevention and the agent-to-agent rule are consumed through ADR-0024 decisions 17–18, unweakened.
- **No new authority.** No edge, zone, class, grant type, grant element, authority state, freshness state or namespace is minted; **E12 stays reserved, Z5 stays unopened, Z4 stays dormant, E10 stays unopened**, and no model path physically exists.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: model implementation · model provider selection · model binary selection · a model API · a client · an SDK · a vendor account · credential acquisition · credential storage · a network mechanism · a protocol · a transport · rotation · a runtime directory · a payload assembler · transmission implementation · a retry mechanism · a timeout · queue semantics · a prompt template · a system prompt · an output parser · a schema · a table · a storage mechanism · an event store · UI · a copy catalogue · fixture execution · observation records · a pending-ledger change · W5-D2 implementation · DR-W5-07 behavioural proof · hosted-mode disclosure language · export-warning wording · Lane C · W6 · **E10 activation** · **Z4 discharge** · **a VendorAdapter ADR** · **E12 activation** · **Z5 activation** · companion behaviour · or **medical, therapeutic, diagnostic or crisis behaviour of any kind**. It amends no record. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording throughout — user, Wing, room, grant, edge, recipient class, boundary, processing context, model, human reviewer, architect. **No model is named, no vendor is named, and no model or vendor is contacted.** W1-D2 §4's local branch is quoted once because it is controlling law defining the class. **No real health data may enter a payload, a fixture, a log, a transcript, an evaluation record or a harness artefact** — the synthetic-only discipline extends to runtime, unchanged. No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person. Companion framing appears only where a sentence names the prohibition itself. No private names, no URLs, no project lineage beyond this repository.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D2` · `W1-D5` · `W1-D6` · `ADR-0001` · `ADR-0003` · `ADR-0024` · `ADR-0029` · `ADR-0030` · `ADR-0031` · `ADR-0032` · `W5-AR`

**`ADR-0032` is direct and required** — decisions 49–50 are the handoff this record answers, and its mechanics classify every model call. **`ADR-0031` is direct and required** — the lawful payload and the last controllable point are the preconditions any model call starts from, and the Z4 dormancy carried in A5 is its disposition. **`ADR-0030` is direct and required** — the grant is the only authority a model access can run under, and decisions 24 and 39 are relied on in terms. **`ADR-0024` is direct and required** — the boundary itself, and decision 15 is load-bearing for the whole of Part A. **`ADR-0001` is direct** — decisions 4 and 6 and the local default preference are controlling law here, not background. **`ADR-0029` is direct** — B3's freshness boundary relies on its separation in terms. **`ADR-0003` is direct** as operative Tier J ceremony authority. **Deliberately excluded:** ADR-0002, ADR-0020, ADR-0025, ADR-0027 and ADR-0023 (each reaches this record, if at all, transitively through ADR-0029 or ADR-0024, and `depends_on` is direct authority, never lineage); **W1-D3 is excluded** because its authority-laundering and renewal rules arrive here through W0 §10, ADR-0024 decision 18c and ADR-0029, and no W1-D3 passage is quoted directly.

## Open boundaries and later ownership

1. **OR-2** — carried, not closed; unclosable by design while any boundary is not the Wing's. **Owner: none.**
2. **The vendor-hosted model class** — unopened; its conditions are stated in A4. **Owner: a future governed record, if ever, with Tara's explicit ruling.**
3. **The ADR-0004 residue applicability check** — mandatory before any W5-D2 implementation; not resolved here. **Owner: its own pre-W5-D2 gate or separate governed record.**
4. **Determinism and paired-variant semantics** — the jointly held question. **Owner: DR-W5-07**, with this record's half held open by constraint-free carriage (C5).
5. **Harness method, observation records, `execution_status`, the T12 seam** — **DR-W5-07.**
6. **Runtime, SDK, credential, protocol, transport, rotation, and every physical artefact** — **W5-D2, behind Tier F crossings.**
7. **Hosted-mode disclosure language** (W1-D6 §9.10) · **export-warning wording** (§9.9) · **presentation, wording and surfaces** — **their own records, or W6.**

---

*The rest of this phase proved things: a grant is whole or it is not, a payload is equal or it is not, a crossing is authorised or it is not. This record decides a smaller and heavier thing — that there is a door at all. It opens exactly one, in ink only, on the person's own device, behind every wall already built; it writes down what any other door would cost; and it leaves the repository as it found it: a place where no model has ever been, now with a law for the day one arrives.*
