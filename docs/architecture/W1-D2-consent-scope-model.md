# W1-D2 — Consent & Scope Model

**Status:** Accepted by human reviewer, 2026-06-12 · **Date:** June 2026
**Phase:** W1 — Governance Architecture and Data Boundary Design (deliverable 2 of 6)
**Governed by:** W0 Constitution (esp. Laws 1, 4, 8, 9, 10, 11, 13); ADR 0001 (processing disclosure events); W1-D1 Data Boundary Map (edges, zones, classes)
**Scope:** Documentation only. This document defines the consent grammar — how consent is granted, scoped, displayed, limited, revoked, audited, and prevented from becoming broad or permanent authority. No schema, code, UI, or implementation is authorised by this document.

---

## 0. Core posture

1. **Consent authorises edges; it cannot create them.** A grant references a permitted flow from W1-D1 by its edge ID. If no edge exists, consent cannot conjure one — default-deny binds the consent layer exactly as it binds the map. A user saying "yes" to an unlisted flow is not a grant; it is a request for a new edge, which requires a decision record and a constitutional check before any consent question can even be asked.
2. **Consent is the third axis.** Sensitivity (D1) governs what may touch data. Authority (W0 §7) governs what may be treated as true. Consent (this document) governs what the user has delegated permission to do. The three are independent: a grant never raises authority, never lowers sensitivity, and expires without affecting either.
3. **Rights are not grants.** The user acting on their own data — reading and editing their records (E8), initiating a clinician export (E9), demanding erasure, viewing the ledger (L2) — exercises rights. Rights require no permission, cannot be revoked by the system, and are recorded but never gated. Consent exists only where the user *delegates*: to an agent, a processing event, or an adapter. This document governs delegation and nothing else.

## 1. The grant

Every grant must express all of the following. These are the required elements of the consent grammar, not schema fields — later phases implement them however they like, but a grant missing any element is not a valid grant.

| Element | Meaning |
|---|---|
| **Edge** | The W1-D1 edge ID this grant authorises (E2, E6, E7, E9, E10, E11-W, E11-K, E11-G, M2). One edge per grant. |
| **Requesting actor** | The room or agent that will act under the grant |
| **Recipient / processing class** | None, internal room/agent, local model, vendor-hosted model, or external vendor/service — **with the vendor/service named** whenever non-user infrastructure receives the payload |
| **Data class** | The D1 sensitivity class(es) of the payload (C0–C4, CM) |
| **Scope** | The named records, sections, or categories included — never a class-wide wildcard |
| **Source zone → destination zone** | Per D1 §1 (e.g., Z1 → Z3) |
| **Purpose** | One declared purpose, in user-facing language |
| **Allowed operation** | Read, extract, process, transmit, or prepare-for-export — one or an explicit enumerated set |
| **Plaintext flag** | Whether plaintext leaves the user trust boundary (Z1), stated as a fact, not implied |
| **Vendor involvement** | Whether any non-user infrastructure sees the payload, and in what form (ciphertext / plaintext) |
| **Duration** | A bounded lifetime: single-task, session, or standing-with-review-date. Unbounded is not a valid duration |
| **Revocation behaviour** | Reference to §5 immediate effects |
| **Audit record** | The C0 ledger entry created at grant, at each use, and at end-of-life |

Two structural rules complete the grammar:

- **Grants are non-transferable and non-delegable.** An agent holding a grant cannot pass it, or the data obtained under it, to another agent, room, or process. Chained work requires its own edge and its own grant — consistent with the W0 agent-to-agent rule: one agent's output is another's unverified input, and one agent's permission is nobody else's permission.
- **One edge, one purpose, one grant.** Compound requests ("extract my records *and* update my profile *and* prepare questions") decompose into separate grants the user sees separately, except where W0 already defines them as a single governed flow (E2→E3 extraction landing as pending-review drafts is one flow; E4 approval is the user's own act and needs no grant).

## 2. Grant types

The grammar recognises exactly these delegation types, each bound to its D1 edges:

| Type | Edges | Duration norm | Notes |
|---|---|---|---|
| **Vault extraction** | E2 | Single-task only. Never standing, never background | The most consequential grant in the Wing. Scope names the records or record categories the Health Profile Agent may read. Output lands only as *agent-extracted, pending review* (E3) |
| **Profile scoped read** | E6, E7 | Standing permitted, with mandatory review date | The only standing grants over health context. Scope is section-named (e.g., *allergies*; *confirmed dietary requirements*), never "the profile." Section age surfaces on every use (Law 7) |
| **AI processing disclosure** | E11-W, E11-K, E11-G, M2 | Single-task default; session maximum | Per ADR 0001. Always user-initiated. M2 grants additionally bind to the Meditation Room's no-output-elsewhere rule |
| **Vendor disclosure** | E10 | Per transmission | Payload is the list, full stop. The grant displays the actual payload before transmission |
| **Export preparation** | E9 (preparation step only) | Single-task | The export itself is a user right; a grant covers only agent *preparation* of the export artifact, if requested |

There is no grant type for cross-room flows, ledger processing, Meditation Room bridges, or E12 — because no such edges exist. The absence is the design.

## 3. Anti-blanket rules

Consent must never quietly become broad or permanent authority. Binding prohibitions:

1. **No class-wide scopes.** "All health data," "everything in my Vault," "my whole profile" are not grantable scopes. Scope names sections, records, or categories.
2. **No unbounded durations.** Every grant ends. Standing grants carry a review date and weaken visibly past it: a stale grant is surfaced for renewal at next relevant use and is suspended if not renewed — the consent-layer analogue of Law 7. *Approved is not current* applies to permissions exactly as it applies to data.
3. **No generic AI consent.** "Let the AI help with my health" is not a grant. Every processing grant names its edge, payload scope, recipient class, and purpose.
4. **No background authority.** Nothing in this grammar can authorise unattended Vault processing, scheduled extraction, or proactive agent activity — those would violate Law 1 and ADR 0001 regardless of any consent wording.
5. **No consent bundling.** A grant request is never attached to unrelated functionality ("accept to continue"), and declining a grant degrades only the specific delegated task, nothing else.
6. **The narrow path is the easy path** (W0 §8.3). Where consent is presented, the most scoped option is the default option. "Allow everything" is not offered, so it cannot be chosen.

## 4. Processing disclosure language

Per ADR 0001, when plaintext crosses the user trust boundary for AI processing, the grant must say so in plain words — in the grant itself, not in linked documentation. The required user-facing form:

> *"This will send **[the named scoped content]** to **[a model running on this device / a model hosted by VENDOR-NAME]** to **[purpose]**. Nothing else is included. This permission ends **[duration]**."*

Three rules about this language:

- The vendor name is part of the sentence, not a footnote. "A cloud AI service" is not a valid recipient description.
- The plaintext flag renders as words a non-technical user understands: *"the content itself leaves your device"* vs *"only encrypted data leaves your device."*
- If the honest sentence sounds alarming, the sentence is working. Disclosure language is never softened to improve acceptance rates — that is consent-shaping, and it converts Law 10 into theatre.

## 5. Revocation — immediate effects

Full cascade behaviour for derived artefacts is deferred to its own decision record (W0 Open Question 2). D2 defines only the immediate, non-negotiable effects, which apply the moment revocation is expressed:

1. **No future access** under the revoked grant.
2. **No further processing disclosure events** — any in-flight event aborts where technically severable, and no new transmission begins.
3. **No new derived outputs** from data obtained under the grant.
4. **The audit record remains.** Revocation is itself a C0 ledger event; history is never unwritten (Law 13).
5. **Existing derived artefacts are flagged for user review** — visibly marked as *derived under revoked consent* — and their final disposition (retain / quarantine / cascade-delete) is governed by the later revocation cascade decision. They acquire no new uses in the interim.

Revocation is a right, not a request: it requires no justification, takes effect without negotiation, and is exercisable from the same surface where grants are visible.

## 6. C0 discipline for consent records

Grant and audit records are C0 — governance metadata: plaintext-free with respect to health, personal, and contemplative content, but privacy-sensitive by pattern. The D1 ledger rules bind in full: **no processing, no analytics, no behavioural profiling, no cross-room inference over grant history.** The pattern of what a user consents to — which rooms, how often, around which dates — is itself a sensitive signal, and the ledger's no-processing-edges rule exists precisely so that signal is never mined. Consent history is for the user's eyes and the user's governance, nothing else.

## 7. Constitutional check

- **Law 10** is implemented by this entire document: scoped (§1, §3.1), explicit (§4), revocable (§5), per-purpose (§1), audited (§1, §6).
- **Law 4** is reinforced: scope-naming plus one-edge-one-grant makes minimum-necessary the only expressible request.
- **Law 1** holds: nothing in the grammar can authorise proactive or background activity (§3.4); review-date surfacing for stale grants is an internal flag at next use, not outreach.
- **Law 3** holds: no grant raises authority; E2 output lands pending-review regardless of any consent wording (§2).
- **Law 8** holds: no grant type exists for cross-room flows or ledger processing (§2); consent cannot invent the channels Law 8 prohibits (§0.1).
- **Law 9** holds: the Meditation Room's grantable surface is exactly M2, with its no-output-elsewhere rule carried into the grant type (§2).
- **Law 11** is sharpened by the rights/grants distinction (§0.3): the user's own access, export, and erasure are never consent-gated.
- **Law 13** is satisfied: grant lifecycle events are ledger entries, and §6 keeps the ledger from becoming a dataset.
- **ADR 0001** is incorporated: processing disclosure events are a grant type with mandatory plain-language vendor disclosure (§4).
- **W1-D1** is binding: every grant references an edge ID; default-deny is restated as a consent-layer rule (§0.1).

No law required amendment or reinterpretation. One design judgment to flag for review: **the rights/grants distinction (§0.3).** Treating user self-access, export, and erasure as rights outside the consent system — recorded but never gated — is a deliberate choice; the alternative (modelling everything as self-granted consent) was rejected as both philosophically wrong (Law 11: the user owns the data; owners don't petition) and practically dangerous (a system that can gate "self-consent" can malfunction into gating it).

## 8. Open questions created by D2

1. **Consent duration defaults.** What are the actual numbers — single-task TTL, session definition, standing-grant review intervals (90 days? 180?)? Defaults shape behaviour more than rules do; they deserve their own short decision record.
2. **Re-authentication for high-stakes grants.** Should E2 (Vault extraction) and any vendor-hosted disclosure of C3/C4 content require fresh authentication at grant time, not just an active session? Proposed posture: yes for E2 and vendor-hosted C3/C4; to be decided with the threat model (W1-D5).
3. **Break-glass / emergency exceptions.** D2 takes no position. Any emergency-access concept inherits ADR 0001's "no escrow by default" and W0 Open Question 9, and requires its own ADR argued against both. Until then: no emergency pathway exists in the consent grammar, and that absence is the current decision.
4. **Child, dependent, and household users.** Out of scope per W0 §3. Consent-on-behalf is constitutionally untreated; if ever pursued, it needs its own constitutional amendment process, not a grant type.
5. **Multi-device grant state.** Grants live where keys live (ADR 0001); syncing grant state across devices is part of the key-distribution problem and lands with the multi-device design, not before.
6. **Vendor disclosure wording standardisation.** §4 gives the form; exact standardised phrasing, localisation, and reading-level requirements need definition before any consent surface is designed.
7. **Consent fatigue vs review integrity** (W0 failure mode 9). Standing-grant review surfacing must be rare, specific, and consequential; the mechanism for keeping renewal prompts from becoming ritual yes-clicking should be designed alongside the consent surface, with input from the evaluation plan (W1-D6).

## 9. Feeds into

- **Revocation cascade decision record** (resolves W0 OQ 2): final disposition of derived artefacts (§5.5).
- **Safety surfacing decision (W1-D4):** any surfacing mechanism reads only what edges and grants permit; D2 gives it no special access, and D4 must not create any.
- **Threat model (W1-D5):** consent surfaces and grant storage join the attack surface; re-authentication question (§8.2) lands here.
- **AIAdapter ADR (OQ 10 / E12):** must adopt this grammar wholesale; connected AI systems get no consent shortcuts.
- **Evaluation plan (W1-D6):** anti-blanket rules (§3) and disclosure language (§4) are deterministically testable; consent-fatigue dynamics (§8.7) need behavioural evaluation.
