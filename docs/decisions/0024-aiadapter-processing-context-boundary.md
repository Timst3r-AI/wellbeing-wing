# 0024 — AIAdapter / Processing-Context Boundary

**Status:** Accepted by human reviewer, 2026-08-13. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation (first doctrine record; deliverable W5-D1)
**Decision mode:** doctrine-derived. The boundary is decided now, as a mechanism-independent property; every question of vendor, model, protocol, credential store, transport, and code is named and handed forward.
**Constitutional references:** W0 Law 1 (the Wing holds; it does not push); Law 4 (minimum necessary); Law 6 (never decides or prescribes); Law 8 (inference prohibition); Law 9 (the Meditation wall); Law 10 (consent); Law 13 (the ledger); W0 §10 (agent boundaries, including impersonation); W0 Open Question 10 (identity verification for connected AI systems).
**Blocks:** every later W5-D1 record (DR-W5-02 … DR-W5-07); **every W5-D2 implementation milestone that depends on it**; the behavioural evaluation harness, whose observation surfaces this record makes possible or impossible. **It is controlling architecture for the W5-D2 brief; it does not gate that brief's drafting, which the accepted W5 runway already authorises** — runway acceptance authorises briefs, and accepted doctrine gates capability.

---

**Four phases built a Wing that no model has ever been inside. This record decides what the inside of that room is — how it comes into being, what it can never contain, what it may never pretend to be, and how anyone standing outside could tell whether the wall held. It builds nothing. It is the shape the first door must have before anyone is allowed to cut it.**

## Decision question

**What is the processing boundary — the object a grant creates, a model sees into, and no processing-side state survives — such that ADR 0017's declared isolation property can be realised at runtime, grants can bind to it, payloads can be assembled into it, transmission can leave it, and its behaviour is observable on all four surfaces the behavioural-evaluation corpus requires?**

Three sub-questions the corpus has left open since W1, and which this record must not leave implicit: **what an adapter is and where it sits**; **how a processing context is constructed and destroyed**; and **what must be true of it for anyone to check that it held.**

W1-D1 has reserved edge E12 since W1, on this record's account: *"No Z5 flows exist until the AIAdapter ADR (OQ 10) specifies authentication, scoping, and impersonation prevention."* This record specifies all three, and dispositions E12 explicitly.

## Context

**All three W5 entry-gate documents are accepted** — the W4 closure record, the W5 runway, and the W5-D1 first-deliverable brief — **and W5 nonetheless remains unopened.** It becomes effectively open only when this record is landed, published on `origin/main`, and independently remote-verified. No W5 capability exists, and none is authorised by the acceptance of any of the three. The room contracts declare architectural isolation and each disclaims runtime enforcement in its own words; ADR 0017 states the property and assigns its realisation here. Twenty-three behavioural-evaluation fixtures sit published and honestly unexecuted, every one carrying a named dependency on a runtime that does not exist and a harness that does not exist.

The engine spine holds, shapes, moves, and remembers a person's records with no model anywhere near them, and it is sealed: `engine/core` may import only `json` and itself, `engine/ports` only its declared libraries, and both caps are test-enforced. Nothing in this repository has ever contacted a model.

This record is the first that describes the channel through which health content could one day reach one. It describes the channel's constraints. It opens nothing.

## Controlling law

- **W1-D1 §0 rule 1 — the map is a whitelist.** *"A flow that does not appear in §5 does not exist. Absence of an edge is a prohibition, not an oversight."* The boundary may never widen the whitelist.
- **W1-D1 §1 — the trust zones.** Z1 (plaintext yes); Z2 (ciphertext only); **Z3 — granted processing**: *"A live, consent-scoped processing disclosure event (ADR 0001): local model or named vendor model, for a named purpose and duration. Yes — scoped payload only, for the grant's duration"*; Z4 (minimum task payload only; never health, profile, or contemplative content); **Z5 — connected AI systems**: *"Only via Z3 rules; connection model deferred to the AIAdapter ADR (resolves OQ 10)."* **Key material lives in Z1 only and has no outbound edges at all.**
- **W1-D1 §3 — transient processing payloads.** *"Exist only for a grant's duration; never persisted by the processing side; retention prohibited."*
- **W1-D1 §5 — the declared processing edges.** *"E11 is not itself a permitted flow"*; the declared family is E11-W, E11-K, E11-G; **M2 remains the only Meditation Room processing edge; E12 remains reserved.** *"Any future AI processing flow not on this list requires a new declared edge via decision record — the generic edge is deliberately absent so that it can never become the back door."*
- **W1-D1 §5 anti-map** — room→room in any direction; ledger→any processing; key material→anywhere.
- **W1-D1 §6 — plaintext exists in exactly two places: Z1 and Z3.**
- **W1-D2 §0.1 — consent authorises edges; it cannot create them.**
- **W1-D2 §1 — the thirteen required grant elements**, and the two structural rules: **grants are non-transferable and non-delegable**; **one edge, one purpose, one grant**.
- **W1-D2 §2** — AI processing disclosure grants (E11-W/K/G, M2): *"Single-task default; session maximum … Always user-initiated. M2 grants additionally bind to the Meditation Room's no-output-elsewhere rule."*
- **W1-D2 §3.4 — no background authority.** **§5 — revocation's immediate effects**, including *"any in-flight event aborts where technically severable, and no new transmission begins."*
- **W1-D5 §4 — the Z3 boundary row, imported wholesale:** *"AI processing boundary (Z3) | Scoped plaintext under grant | Over-disclosure; retention by vendor-hosted models (OR-2)."* With it, the threat rows **D5-T05, D5-T06, D5-T12, D5-T13, D5-T15, D5-T23** and the residuals **OR-1, OR-2, OR-3**.
- **W1-D6 §3 — the evaluation grammar, imported wholesale**, in particular §3.1 (*"No new room, edge, adapter, or capability ships ahead of the tests that would catch its failure modes"*), §3.2 (deterministic before generative), §3.3 (*"A test's ground truth is the governed record … never a model's opinion"*), §3.8 (*"Passing tests must not mint authority"*), §3.9 (*"Tests prove behaviour, not truth"*).
- **W0 §10 — agent boundaries.** Agents may not *"impersonate the user, or impersonate the user's own AI system to other services"*, may not *"override user consent, exceed granted scope, or extend their own permissions"*, and the **agent-to-agent rule**: *"One agent's output is another agent's unverified input, never its evidence."*
- **ADR 0001** — local-first, user-held keys; processing disclosure events; local models as the default preference.
- **ADR 0009** — the import boundary's structural cap: the path cannot parse what it cannot import.
- **ADR 0015** — the durable ledger: sealed under the master-key custody boundary, append-only, **doctrine-wide event scope with v1 implementation limited to the events that exist today**, and further emission classes named as explicit future extensions.
- **ADR 0017 decisions 1–12** — binding inputs, not open questions. Decision 9 assigns realisation here.
- **ADR 0018, 0019, 0020** — scope fidelity; the inference prohibition and its no-lawful-destination rule; the shared uncertainty behaviour table.
- **The four room contracts, section 6** — each a specification this boundary must satisfy, including Meditation's structurally different instantiation.
- **W4-D6-BEF §8** — the four observed surfaces and the paired-variant pass condition.

**Source fidelity — resolved by ADR 0023, and imported here against the corrected authority.** The AIAdapter import obligation formerly named rows that one of its sources did not contain. **ADR 0023 corrected W1-D5 §8 and W1-D6 §9.4**, and this record imports against the corrected wording, which is now authoritative.

**The mandatory import is:** **W1-D5 §4's Z3 boundary row, wholesale**; **W1-D1 §1's Z5 zone definition, wholesale**; and, where W1-D6 requires it, **W1-D6's evaluation grammar, wholesale**.

Four distinctions ADR 0023 fixed and this record preserves: **no Z5 row was invented** in W1-D5; **the Z4 row was not substituted** for a Z5 row; **OR-1, OR-2 and OR-3 are not newly mandatory** under ADR 0023 — the Z3 row's reference to OR-2 travels with that row, but the residual texts are not thereby added to the mandatory import; and **this record remains free to cite the W1-D5 §4 Z4 row for its adjacent limb, and OR-1, OR-2 and OR-3 independently, on its own authority**, as any record may import more than it is required to. It does so throughout, deliberately. **No source is amended by this record.**

## Decision

### The boundary itself

1. **The AIAdapter is the single governed seam between the Wing's own memory and any model, and there is exactly one of it.** No second processing path exists, and none may be added without its own accepted record. Every crossing of that seam is a **processing disclosure event** under ADR 0001.

2. **The boundary accepts no content independently of a grant.** There is **no free-content and no free-text interface** — no interface on the boundary takes room content, profile content, vault content, or caller-supplied text as an independent parameter. Content may enter a processing context **only as a governed payload produced from, and inseparably bound to, the same grant that created the context**; a payload with no grant, or a payload separable from its grant, is not a lawful input and there is no interface that would receive one. **The boundary also never fetches**: it has no read path of its own into the vault, the profile store, a room store, or the ledger (decision 4). Payload construction itself is DR-W5-04's, not this record's.

3. **The boundary is not a session, a connection, a conversation, an assistant, a room, or a cache.** *"Session"* is deliberately not the controlling term (ADR 0017 decision 6): a session is something a user has and a duration a grant may name (W1-D2 §2), while a **processing context** is something a grant creates and ends. The boundary holds no relationship, accumulates no impression of the person, and has no memory of its own.

4. **The boundary sits outside the sealed engine, and the structural separation runs both ways.** ADR 0009's structural cap is not relaxed: `engine/core` and `engine/ports` remain closed to it. **The engine must not import or call the adapter, and the adapter must not reach into engine internals.**
   **This is a separation, not a prohibition on composition.** A future **external composition root or orchestrator**, itself outside the sealed engine, **may lawfully invoke the public interfaces of both** — that is how any real runtime is assembled, and nothing here forbids it. **The exact orchestration belongs to W5-D2** and is not decided by this record.
   **The boundary has no read path of its own** — it may not open the vault, the profile store, a room store, or the ledger. It receives; it never fetches. Where it needs content, that content arrives because a grant put it in scope, which is W1-D1's whitelist doing its work rather than a convenience being added beside it.

### Construction and binding

5. **A processing context exists only as the product of a valid grant, and "derives from the grant" is a construction rule, not a description.** Every field that determines what a context may hold — edge, room, data class, scope, purpose, allowed operation, zone pair, recipient class, plaintext flag, duration — is read from the grant object and from nowhere else. **A context with no grant is unconstructable, not merely invalid**, because no constructor exists that does not take a grant.

6. **One processing grant binds exactly one room, structurally.** A grant names exactly one edge (W1-D2 §1), and each processing edge belongs to exactly one room: E11-W → Wellness, E11-K → Kitchen, E11-G → Gym, M2 → Meditation. **The room is therefore a function of the grant, never an argument to the context.** A grant naming two rooms could not be constructed, because there is no room parameter to widen and no second edge slot to fill. This is ADR 0017 decision 4 made structural.

7. **No composition point exists, in any direction.** No operation on the boundary unions, merges, concatenates, extends, chains, or otherwise combines two contexts, two grants, or two rooms' content. **A second grant produces a second, separate context — never an extension of the first.** The enforcement is the absence of the operation, not a check inside it: there is no interface at which two rooms' content could meet, so there is no interface to guard.

8. **Processing state is not reused across contexts, including within one sitting.** *"Within one sitting"* carries ADR 0017 decision 6's definition verbatim: **within any sequence of interactions in which processing state could otherwise be reused, regardless of timing or interface.** **What is forbidden is hidden or direct continuity** — caches, handles, summaries, embeddings, conversational or context state, and any other processing-side reuse — carried from one context into another in either direction. **A later context has no name by which an earlier context's processing state could be referred to.**
   **This is not a prohibition on lawful retrieval.** A governed artefact that was lawfully produced and lawfully stored may later be retrieved **normally, under a fresh grant that names it in scope**, and may enter a later context that way. The difference is the whole point: **the second path is grant-derived, disclosed, and auditable; the forbidden one is a side channel that skips all three.**

### Lifetime

9. **A context's lifetime is bounded by its grant, and when the grant ends the context ends** — by completion, by expiry, or by revocation.

10. **No processing-side state survives a processing context.** This carries W1-D1 §3 exactly: transient processing payloads *"exist only for a grant's duration; never persisted by the processing side; retention prohibited."* **Lawful output and governed records may leave the context only through an authorised edge or governed artefact, and once they have, they are no longer part of the processing context.** Which such outputs exist, and through which edges, is **not decided here** — it belongs to DR-W5-04 and DR-W5-05.

11. **Revocation must be expressible at the boundary.** W1-D2 §5 binds without softening: no future access, **no further processing disclosure events with any in-flight event aborting where technically severable**, no new transmission, no new derived outputs, the audit record remaining. The boundary must therefore be able to name an in-flight crossing and attempt its abort. **Where a crossing proves not technically severable, that limitation is recorded honestly and never described as an abort** (see Open questions 3).

### Display and processing

12. **A display is not a processing input, and the two contexts are separate.** E5, E6 and E7 are display and scoped-read edges; the E11 family and M2 are processing edges. **Content that entered under a display edge does not enter a processing context by virtue of having been displayed.** A processing context is built from its grant's scope, never from what the user is looking at, has recently looked at, or has open.
    This answers **ADR 0017's first carried question** as a separation: *displayed context and processing context do not share a runtime context, and no path composes one into the other.* The Wellness contract's constraint is satisfied in its own terms — *"E5 display authority and E11-W processing authority are distinct — displayed context (E5) does not become processing input by that display"* — and the Kitchen contract's *"declared W5 dependency"* is discharged. The split is **live for Wellness (E5), Kitchen (E6) and Gym (E7), and structurally absent for Meditation**, which has no inbound read edge at all.

### Observability

13. **The boundary is observable by construction on all four surfaces, and observability is a property of the boundary rather than an ability of a later harness.** The four surfaces are W4-D6-BEF's: **spoken output · persisted state · routing and propagation · behaviour selection, ranking, framing, and omission.** Specifically:
    - **Spoken output** — the boundary can report what it presented and what was returned, for a given context, without a second data channel.
    - **Persisted state** — the observable is *the absence of persistence*, and **absence must be demonstrated, not presumed**: the boundary exposes its own post-context state for inspection rather than asserting emptiness.
    - **Routing and propagation** — the observable is *the absence of propagation*, demonstrated the same way: the boundary can **enumerate every Wing-controlled destination it wrote to** for a given context, so that absence is proven by enumeration rather than assumed from a design intention. **The claim is bounded at the recipient boundary and no further: the Wing can demonstrate what it did with a context, and it cannot and does not claim to prove what a recipient does internally beyond that boundary** — OR-2 governs that residual and is not weakened here.
    - **Behaviour selection, ranking, framing, omission** — the boundary must support **paired-variant execution**: the same scenario constructed with and without the bait context, which is a construction-and-control requirement on the boundary, not a feature of the instrument that later reads it.

14. **Observation never becomes a second data channel.** Observation records are governed artefacts under the same synthetic-only discipline and the same public-safety scan as every other governed artefact. **Governed evaluation may read, analyse and score them for the authorised W5 evaluation purpose** — that is what they exist for, and a record no one may examine would prove nothing.
    **They must never become any of the following:** input to any processing context; a profiling source; cross-room analytics; a behavioural dataset about the person; or an authority source of any kind. W1-D1's ledger rule states the danger this bounds: *"The record of activity must not become a behavioral dataset — that would be cross-room inference through the back door."*
    **This record does not classify observation records as C0**, and their artefact class, home, retention and lifecycle are **DR-W5-07's** (Open question 2).

### Zones, and the three E12 prerequisites

15. **W5 activates no Z5 flow, and E12 remains reserved.** Every processing crossing W5 needs occurs on the already-declared E11-family and M2 edges, all of which are Z3 processing disclosure events. Whether the model runs on the user's own device or is hosted by a named vendor is a property of the **recipient class inside the grant** (W1-D2 §1) — not a different boundary and not a different set of rules.
    **Z5 remains a distinct trust zone and is not collapsed into Z3 by this record.** W1-D1 defines it separately, and that separation stands. What W1-D1 already imposes is that **any future Z5 flow inherits the Z3 grant and scoping rules** — *"Only via Z3 rules"* — so a future Z5 connection would arrive already bound by decisions 5 through 8 and 16 through 18, and would still require its own declared edge through its own decision record. **ADR 0001's local-model default preference is preserved and not foreclosed by any part of this record.**

16. **E12 prerequisite — scoping.** **Scope is carried entirely by the grant and never by the connection.** A connected system holds no standing, ambient, inherited, or accumulated scope; it receives exactly what one grant put in scope, for that grant's duration, and nothing else persists on the Wing's side of the seam. **Identity never widens scope.** Class-wide scopes, unbounded durations, generic AI consent, background authority and bundled consent remain unexpressible (W1-D2 §3), and the boundary adds no mechanism by which any of them could be reconstructed.

17. **E12 prerequisite — authentication.** The required **properties**, decided here; the mechanism is not:
    - **(a) Nameable recipient.** For every crossing, the Wing must be able to state *which* recipient received the payload, in the same terms the grant displayed to the user. W1-D2 §4 binds the display side already — *"The vendor name is part of the sentence, not a footnote. 'A cloud AI service' is not a valid recipient description."* **A crossing whose recipient cannot be named is refused.**
    - **(b) Recipient binding, on the Wing's side of the seam.** A payload assembled under a grant may be delivered only to the recipient that grant displayed. **The Wing may not redirect a grant, or a payload assembled under it, to another recipient without a lawful edge, a lawful grant, and its own disclosure. Re-targeting requires a new grant**, never a substitution inside an existing one. **This binds what the Wing does; it makes no claim about a recipient's own subprocessors, onward routing, or downstream behaviour**, which OR-2 already records as beyond the Wing's verification.
    - **(c) Authentication authorises nothing.** Identity establishes *who*; the grant authorises *what*. **No authenticated system acquires scope by being authenticated**, and no failure of authentication may be compensated by a broader grant.
    - **(d) Credentials never enter a payload or an observation record.** Whatever credential material a future mechanism requires follows the key-material discipline's spirit: it lives on the Wing's side, is never part of an assembled payload, is never logged, and is never observable through the observation surfaces of decision 13.
    - Protocol, credential storage, transport, and rotation are **DR-W5-06 and W5-D2**, and are not decided here.

18. **E12 prerequisite — impersonation prevention.** From W0 §10, which forbids an agent to *"impersonate the user, or impersonate the user's own AI system to other services"*:
    - **(a) The boundary never speaks as the person.** Every outbound payload is attributable to the Wing acting under a named grant. **No crossing is ever presented as originating from the user.**
    - **(b) The boundary never presents itself as the user's own AI system to any other service**, and never presents another system's output as the Wing's own.
    - **(c) Origin labelling survives the crossing.** Anything returning from a model is **agent-origin by construction**, carries no authority, and cannot be relabelled at the boundary. The agent-to-agent rule binds in full: *"One agent's output is another agent's unverified input, never its evidence"* — and D5-T06's authority laundering is exactly the failure this decision exists to make structurally hard and behaviourally testable.
    - **(d) No delegation, on the Wing's side of the seam.** Grants are non-transferable and non-delegable (W1-D2 §1). **The boundary may not pass a grant, or content obtained under one, to any further system**, and there is no interface by which it could. **What lies beyond the recipient boundary is the recipient's own conduct: this record constrains the Wing and claims no control over a vendor's internal subprocessors or downstream behaviour.** That residual is OR-2's, permanently, and disclosure honesty rather than technical control is its only mitigation.

19. **E12 disposition: E12 REMAINS RESERVED.** Stated explicitly, because silence would be unlawful here.
    W1-D1 conditions any Z5 flow on this record specifying scoping, authentication, and impersonation prevention. **Decisions 16–18 specify all three**, so the condition is now met — but meeting the condition is not the same as opening the edge, and this record declines to open it. **W5 contemplates no Z5 connection**: every processing crossing W5 needs occurs on the already-declared E11-family and M2 edges. Defining E12 now would mint a live flow into the W1-D1 whitelist **with no use for it**, which is precisely the back door W1-D1 says the generic edge's absence exists to prevent.
    **Therefore: E12 stays reserved. Its doctrinal prerequisites are satisfied and recorded, so a future record that genuinely needs a Z5 connection inherits them and need only decide the flow itself — through its own decision record, its own constitutional check, and an amendment to W1-D1 that lands in W1-D1 first.** This record proposes no such amendment and creates no edge.

### Ledger, refusal, and exceptions

20. **Every processing crossing is a governed event, and the boundary emits it.** W1-D1's L1 covers *"grants, revocations, disclosure events, authority transitions, Vault access, adapter payloads (by reference)"*; ADR 0015 makes the ledger doctrine-wide in scope. The boundary emits at **context creation** and at **context end**, and the entries are **C0 and content-free**: *"entries reference categories and scopes, never contents."* **No payload text, no model output, no excerpt, no fragment.**
    **Implementation note carried as doctrine, not softened:** ADR 0015's v1 implementation scope is the transition events that existed at its acceptance, with further emission classes named as *"an explicit future extension."* Processing-event emission **is** such an extension. This record states the obligation; **W5-D2 implements it under ADR 0015's own extension clause, and until it does, no claim may be made that processing events are ledgered.**

21. **The boundary refuses structurally, and never by policy alone.** Where a prohibition can be made unconstructable it is made unconstructable; where it cannot, it is a fixed, content-free refusal:
    - no grant → no context;
    - two rooms → unexpressible;
    - content outside the grant's scope → no path by which it could enter;
    - a recipient that cannot be named → refused (decision 17a);
    - **a room's out-of-scope noticing → no lawful destination.** ADR 0019 binds verbatim: *"a room that notices something outside its granted authority has nowhere lawful to place the noticing."* **The boundary provides no pattern-flag, no queue, no note, no "for review" pathway, and no store of any kind for such a noticing. The absence is deliberate architecture, not a missing feature**, and this record creates no new queue or route.
    - **A refusal echoes no refused content and writes no user, room, profile, or vault state**, on the ADR 0009 import-refusal precedent, and refusal reasons are fixed and content-free, on the transition-engine precedent. **A content-free governance or audit event may still be emitted where doctrine requires one** — "writes nothing" bounds content and user-visible state, never the ledger, whose obligation is decision 20's.

22. **Future-exception discipline binds this whole record.** ADR 0017 decision 11's minimum contents extend to any exception to any decision above, and **no silent downgrade from architectural to policy enforcement is permitted.** An exception returns as its own accepted record stating, at minimum: the affected rooms or edges; the precise, evidence-backed infeasibility; the exact bounded scope of the exception; its duration, review date, or sunset condition; the context that remains strictly prohibited; the compensating structural controls and behavioural evaluations; and explicit human-reviewer acceptance. **If implementation finds any decision here genuinely infeasible, the lawful response is an exception record or a correction record on the ADR 0022 precedent — never an accommodation written quietly into the boundary.**

23. **Structure does not remove model-side inference, and this record claims no such thing.** ADR 0017 decision 10 is restated rather than inherited silently: *"Behavioural evaluations still apply. Structure reduces the channel; it cannot remove model-side inference within a lawful channel."* Everything above closes channels. **None of it is evidence that a model behaves**, and no green structural proof may ever be presented as one.

## What this record leaves to later W5-D1 records

Stated so that no later reader mistakes silence for a decision.

| Left to | Question |
|---|---|
| **DR-W5-02** — Runtime Freshness and Unknown/Stale Behaviour | Default review intervals by data type (W1-D3 §10.1) and block versus warn (W1-D3 §10.6). The §6.4 floor binds until then, and no interval or blocking behaviour may be settled by implementation default |
| **DR-W5-03** — Grant Machinery, Consent Duration and Re-authentication | The grant object at runtime; consent-duration defaults (W1-D2 §8.1); the re-authentication posture (W1-D2 §8.2, W1-D3 §10.7); revocation mechanics beyond §5's immediate effects. **This record says a context derives from a grant; it does not build the grant** |
| **DR-W5-04** — Payload Assembly and Payload Equality | Payload assembly, the payload-equality standard, byte-level equality at Z3 and Z4, and **the Z4 disposition seam** |
| **DR-W5-05** — Transmission and Disclosure Mechanics | Transmission mechanics; the W1-D2 §4 disclosure sentence in operation; the OR-2 residual in disclosure language |
| **DR-W5-06** — Model Access | Which model class; local versus vendor-hosted; vendor, SDK, credential implementation, network mechanism, protocol, transport |
| **DR-W5-07** — Behavioural Evaluation Architecture | Harness boundary; behaviour-delta observation method; `execution_status` vocabulary and transition governance; re-run semantics; false-positive and false-negative controls; the T12 condition-seam disposition |
| **A W5-D1 doctrine and applicability check** | Whether ADR 0004's plaintext-residue doctrine reaches this transient Z3 boundary (Open question 6). **Must complete before any W5-D2 implementation; a brief may not settle it** |
| Trigger-bound | The revocation-cascade record (W0 OQ 2), which must be accepted before the first W5 capability produces a derived artefact under a grant; a VendorAdapter ADR, conditional on actual E10 activation |
| Evidence, not doctrine | Per-room context-cost evidence (ADR 0017's second carried question) — a disposable out-of-repository spike under ADR 0007, findings only, **no reserved record number** |

## Constitutional check

- **Law 1 holds.** Nothing here authorises proactive, background, scheduled, or unattended processing; every context is user-initiated through a grant (W1-D2 §2), and the boundary contacts no one.
- **Law 4 is served structurally.** Scope is the grant's and only the grant's (decision 16); minimum-necessary becomes the only expressible request because there is no wider one to express.
- **Law 6 is untouched.** The boundary decides nothing about a person, diagnoses nothing, and recommends nothing; it carries content and returns unlabelled-as-truth output.
- **Law 8 is served, not bypassed.** Decisions 6, 7 and 8 remove the cross-room channel rather than policing it, and decision 21 denies the room layer any destination for an out-of-scope noticing.
- **Law 9 holds.** Meditation receives the uniform standard with no exception; M2 remains its only processing edge, its no-output-elsewhere binding is carried by the grant type, and no bridge is created.
- **Law 10 holds.** The grant grammar is unchanged; this record constrains how a context may be composed from a grant, and adds no grant type.
- **Law 13 holds.** Decision 20 puts every crossing in the ledger, content-free, and decision 14 keeps the record of activity from becoming a dataset.
- **W0 §10 is implemented rather than restated:** decisions 17 and 18 give the impersonation and scope-extension prohibitions structural form.
- **No new authority.** No new edge, class, authority state, consent form, or permission is minted. **E12 remains reserved** (decision 19), and W1-D1's whitelist is not widened by a single flow.
- **No law required reinterpretation, and no amendment to the Constitution is proposed or required.**

## Alternatives considered

- **A grant-derived, single-room, non-reusable, observable context (chosen).** Makes ADR 0017's property a construction rule rather than an instruction, and makes the corpus's own silent-channel prohibitions testable rather than merely stated.
- **A general-purpose adapter taking room content directly, with the grant as a check (rejected).** Rejected: it makes the grant a validation step rather than the constructor, and every validation step is one bug away from being skipped. The corpus's whole design preference is unconstructability over checking.
- **One long-lived context per room, reused across grants (rejected).** Rejected: it reintroduces exactly the reuse ADR 0017 decision 6 forbids, and its convenience is entirely on the implementer's side of the wall.
- **Defining E12 now, so the adapter has a general external path (rejected).** Rejected as the back door W1-D1 names: an edge minted with no use for it becomes the path of least resistance for the first feature that wants one.
- **Deferring authentication and impersonation prevention to the model-access record (rejected).** Rejected because W1-D1 conditions E12 on *this* record specifying them, and because both are properties of the boundary rather than of whichever vendor is later chosen. Deferring them would leave the reservation's own precondition unmet.
- **Output-first observability, with the harness recovering the rest (rejected).** Rejected as structurally impossible: three of the four observed surfaces cannot be recovered from outside a boundary that never exposed them, and W4-D6-BEF forecloses the fallback in terms — *"a future harness that classified spoken output alone could not satisfy this contract."*

## Consequences

- **Easier (later):** the W5-D2 milestones inherit a construction rule rather than an aspiration, and the deterministic proofs the phase owes — a two-room grant that cannot be constructed, a composition point that does not exist, state that is not reused — are proofs about structure, which is the kind a machine can check.
- **Easier (later):** the harness inherits a boundary that can already be watched on four surfaces, so DR-W5-07 designs an instrument rather than a retrofit.
- **Harder, deliberately:** no context may be reused, extended, or composed, and every processing need is expressed as its own grant. A design that wants a long-lived assistant cannot have one without a full exception record.
- **Harder, deliberately:** the boundary cannot fetch. Anything it needs must have been put in scope by a grant, which pushes work onto the grant machinery — where the corpus wants it.
- **Constrains future decisions:** DR-W5-04's payload is assembled *into* this context and cannot exceed it; DR-W5-05's transmission leaves *from* it; DR-W5-06's model choice cannot alter the boundary's shape; and any infeasibility is an exception record, never a silent downgrade.
- **Preserved honesty:** this record closes channels and claims nothing about behaviour. Every fixture remains unexecuted, every behavioural stub remains pending, and the phase is no closer to a safety claim than it was before.

## Non-goals

This record does not decide, and its acceptance does not authorise: any implementation, code, or scaffolding; any directory or dependency (each remains a Tier F fence crossing named at its own landing); any model contact; any payload, prompt, or assembler; any grant implementation; any transmission; any harness; any fixture execution or `execution_status` transition; any pending-stub edit, flip, rename, or condition amendment; any Lane C row change, applicability resolution, evidence claim, or certification claim of any kind; any amendment to a sealed W1, W3, or W4 record; any new edge, including E12; any notification layer or background behaviour; any review surface, catalogue, label rendering, UI, or CLI; hosted mode, sync, or multi-device state; and **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.** It contains no real health data and no clinical examples.

## Public-safety considerations

Generic wording throughout — user, Wing, room, contract, grant, processing context, boundary, adapter, recipient, human reviewer, architect, model. No private names, no model or vendor names, no private or project lineage, no URLs, no real health data, no clinical examples, and no placeholder tokens: this record needs none, and the safest example register is the empty one.

**Watch item, named because this is the record where it becomes live.** This document describes the exact channel through which health content could one day reach a model. It describes the channel's **constraints** and never demonstrates its **use**: there is no worked payload, no example prompt, no sample content, and no clinical pairing anywhere in it — real, synthetic, or placeholder-dressed. **A document that teaches a boundary must never model a crossing.** Companion framing appears only where a sentence names the prohibition itself, per corpus precedent, and any such line is individually authorised at landing.

## Dependencies

W0 (Laws 1, 4, 6, 8, 9, 10, 13; §10; Open Question 10); W1-D1 (zones, homes, the whitelist, the E11 family, M2, E12's reservation, the anti-map, the plaintext summary); W1-D2 (the grant grammar, grant types, anti-blanket rules, disclosure language, revocation's immediate effects); W1-D3 (the labels that travel with any content entering a context); W1-D5 (the Z3 boundary row, D5-T05/T06/T12/T13/T15/T23, OR-1/OR-2/OR-3); W1-D6 (the evaluation grammar); ADR 0001; ADR 0002; ADR 0003 (ceremony); ADR 0009 (the structural cap this record does not relax); ADR 0015 (the ledger and its extension clause); ADR 0016; ADR 0017 (the property this record realises); ADR 0018; ADR 0019; ADR 0020; ADR 0021; ADR 0022; **ADR 0023 (the correction that made the inherited AIAdapter import citation dischargeable, and the authority this record imports against)**; the four room contracts (W4-D2 … W4-D5, section 6 in each); W4-D6-BEF (the four observed surfaces); W4-CR; and the W5 runway (W5-AR).

**This record depends on no prior W5 deliverable. ADR 0023 is a phase-W5 correction record with `deliverable: null`, and is depended on solely as the authority correcting the inherited W1 citation. This record remains the first W5 deliverable doctrine and constrains all later W5 deliverables.**

## Open questions

Genuine architecture questions this record cannot close, each named with its owner rather than left implicit.

1. **Determinism for paired-variant execution.** Decision 13 requires the boundary to support running the same scenario with and without the bait context. **Whether the responses are comparable at all depends on the determinism of whatever model is later chosen**, and a non-deterministic model turns *"no behavioural delta"* from an equality into a statistical claim — which changes what a fixture pass means. **Owner: DR-W5-06 (model access) and DR-W5-07 (evaluation architecture), jointly.** The boundary must be able to hold whatever answer they reach; it does not pre-empt it.

2. **Where observation records live.** Decision 13 requires observation and decision 14 constrains it, but **the artefact class is undecided**: ledger frames are content-free and append-only by ADR 0015, while observation records may need to be richer than the ledger permits, and W4-D6-BEF already routes fixture results to *"future W5 evaluation records only."* Whether observation records are ledger frames, a separate governed class, or evaluation-record-only is genuinely open. **Owner: DR-W5-07**, which owns result storage.

3. **Whether an in-flight crossing is technically severable.** Decision 11 carries W1-D2 §5's *"aborts where technically severable"* honestly, but **whether a vendor-hosted crossing can in fact be aborted mid-flight is a mechanism question that may well answer "no"** — in which case the honest response is to record the limitation, not to describe a best-effort cancellation as an abort. **Owner: DR-W5-05 (transmission) and DR-W5-06 (model access).**

4. **The user-facing consequence of decision 12.** Separating display from processing is right and is now decided; the consequence is that a user looking at a profile section and asking about it must have that content re-scoped through a grant rather than picked up from the screen. **That is friction by design, and the surface era will meet it.** Named here so it is inherited rather than rediscovered. **Owner: the W6 surface era**, with no W5 obligation.

5. **Whether context-cost evidence disturbs anything decided here.** The per-room context-cost spike (ADR 0017's second carried question) may show that one-context-per-room is costly. **The doctrine does not bend to cost** — an infeasibility returns as an exception record under decision 22 — but the evidence may legitimately inform DR-W5-06's model-access choice. **Owner: the spike, then DR-W5-06.**

6. **Whether the Wing's side of the seam needs its own residue doctrine.** ADR 0004 governs plaintext residue; decision 10 forbids processing-side survival, and decision 13 requires that absence be demonstrable. **Whether ADR 0004 reaches a boundary that holds plaintext transiently in Z3, or whether an extension is needed, is not obvious from the sealed corpus.**
   **Owner: a W5-D1 doctrine and applicability check, which must complete before any W5-D2 implementation.** A brief is not doctrine and may not settle this. **If ADR 0004 clearly reaches this transient Z3 boundary, that finding is recorded as such; if it does not, an extension or correction record must be accepted before implementation begins.** Whether the check lands inside an existing W5-D1 record or as its own is a sequencing question for review.

---

*A wall is not the part you can see. It is everything the room cannot do: cannot remember, cannot reach sideways, cannot keep what passed through, cannot speak in the voice of the person whose records it briefly held. This record writes those inabilities down while they are still cheap — before a single line of the thing that must have them exists.*
