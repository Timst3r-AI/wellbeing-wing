# W0 — Wellbeing Wing Constitution

**Status:** Draft for review · **Version:** 0.1.1 (W0.1 cleanup pass) · **Date:** June 2026
**Scope:** Governing document. No code, schema, or UI is authorised by this document. W0 defines what the Wellbeing Wing is, what it must never become, and the laws every later phase must satisfy.

---

> **The user initiates. The wing holds. Nothing is pushed.**

---

## 1. Purpose

The Wellbeing Wing is a modular, AI-assisted personal wellbeing environment composed of four rooms — the **Wellness Room**, **The Kitchen**, **The Gym**, and the **Meditation Room** — built on a single governing idea: personal health context is sensitive evidence that must be governed, not raw material to be mined.

The Wing exists to help a user **hold** their own wellbeing information: organise health records, prepare questions for clinicians, plan meals and groceries, track movement and recovery, and support contemplative practice. AI agents inside the Wing prepare, organise, summarise, compare, and surface. They do not decide, diagnose, advise treatment, or act on the user's behalf without explicit confirmation.

The Wing is deliberately the inverse of the dominant wellness-app model. It does not nag, streak, gamify, score, guilt, or engagement-optimise. It is a quiet environment that responds when the user arrives and holds steady when the user is away.

This document is the constitution for that environment. Every subsequent phase — architecture, schema, agents, UI — must demonstrate compliance with the laws and boundaries defined here before it is built.

## 2. Non-Goals

The Wellbeing Wing **is not**, and must not drift toward becoming:

1. **A medical device.** It performs no diagnosis, screening, triage, or clinical decision support.
2. **A treatment platform.** It does not prescribe, recommend treatment changes, adjust medication context, or substitute for clinical care.
3. **An AI therapist or counsellor.** The Meditation Room supports practice and reflection; it does not provide mental-health treatment.
4. **A health-data marketplace.** User data is never sold, shared for advertising, or used to train models without separate, explicit, revocable consent.
5. **An engagement product.** No external push notifications, proactive outreach, streaks, scores, leaderboards, re-engagement campaigns, or behavioural nudging. (Internal, user-visible flags and review queues are not notifications — see Law 1.)
6. **A commerce engine.** Vendor integrations (via generic `VendorAdapter` interfaces) may prepare lists and surface options. There is no auto-ordering and no preferred-vendor steering.
7. **A claim of regulatory compliance.** The Wing is designed to *privacy-by-design principles aligned with* HIPAA, the Australian Privacy Principles, and GDPR. It does not claim certified compliance with any regime unless and until legally reviewed and operationally supported.
8. **A surveillance or inference system.** The Wing does not profile the user beyond what the user has explicitly reviewed and approved (see Law 8).

## 3. Target Users

- **Primary:** Adults managing their own everyday wellbeing — health records, nutrition, movement, and contemplative practice — who want organisation and preparation support without surrendering authority over their own health context.
- **Secondary:** Adults preparing for clinical interactions — organising history, pathology trends, medication and supplement lists, and questions — so that time with clinicians and pharmacists is better used.
- **Explicitly out of scope for the initial version:** minors; users in acute medical or psychiatric crisis (the Wing is not a crisis tool and must say so plainly); carers managing another person's health data (multi-profile delegation raises consent questions deferred to Open Questions, §12).

The Wing assumes a capable adult who is the final authority on their own information. Every design decision flows from that assumption.

## 4. Core Laws

These laws bind every room, agent, integration, and later phase. Where any later design conflicts with a law, the law wins or the law is formally amended — never silently bypassed.

**Law 1 — Initiation.** *The user initiates. The wing holds. Nothing is pushed.* No external push notifications, proactive outreach, reminders, or unsolicited interventions, by default. *Holding* is permitted and expected: internal flags, review queues, stale-profile indicators, and user-visible pending items may accumulate quietly inside the Wing and be visible when the user arrives — they wait; they do not reach out. Any future notification layer would require explicit user opt-in and its own separate governance treatment before design. (See Law 12 for the sole, narrow qualification on surfacing.)

**Law 2 — Evidence and context are different things.** *The Health Vault is evidence. The Health Profile is derived context. The user decides what becomes active.* Raw records never function as working context; working context is never mistaken for source evidence.

**Law 3 — Nothing self-promotes.** No agent output — extraction, summary, pattern, suggestion, or draft — becomes active, authoritative, or persistent working context without explicit user review and approval. Repetition, retrieval frequency, model confidence, and apparent relevance do not create authority.

**Law 4 — Minimum necessary access.** Every room, agent, and adapter receives the least data, narrowest scope, and shortest duration required for its declared purpose. Access is consent-gated, scoped, and auditable. Default is no access.

**Law 5 — Agents prepare; the user decides.** Agents may retrieve, extract, organise, compare, summarise, flag, and queue for review. Decisions — what becomes profile, what is acted on, what is ordered, what is shared — belong to the user.

**Law 6 — The clinical line.** No diagnosis. No prescription. No treatment recommendations or treatment-change suggestions. No overriding or second-guessing of clinician advice. No auto-ordering. No irreversible action of any kind without explicit, specific user confirmation.

**Law 7 — Approved is not current.** Approval confers authority, not freshness. Every section of the Approved Health Profile carries a last-reviewed date. Agents acting on health context must surface its age, and re-review triggers must exist so approved data cannot silently go stale. (See §11, *Staleness Drift*.)

**Law 8 — No inferred conditions.** Agents must not derive, record, persist, or act on inferred health conditions or sensitive states — including but not limited to pregnancy, disordered-eating patterns, mental-health states, substance use, or reproductive and sexual health status — from cross-room signals, aggregation, or pattern analysis, unless the user has explicitly confirmed that information into the Approved Health Profile or a relevant approved record. Inference is treated as an access path and is governed like one.

**Law 9 — The Meditation Room stands apart.** Meditation, reflection, spiritual, and contemplative data is structurally walled off from the Wellness Room, The Kitchen, and The Gym by default. It does not inform wellness, nutrition, supplement, or fitness suggestions. Any bridge between the Meditation Room and other rooms must be a separate, explicit, user-created, revocable construct — never a default, never an inference.

**Law 10 — Consent is scoped, explicit, and revocable.** Consent is granted per purpose, per scope, and per agent — never as a blanket grant. Revocation takes effect going forward immediately and triggers review of derived context (see §12, Open Questions, on revocation cascade). All consent grants and revocations are recorded in the audit trail.

**Law 11 — The user owns the data.** Export (in usable, portable formats) and deletion/erasure are first-class operations available at all times, not support tickets. Deletion of vault evidence and deletion of derived context are both supported and clearly distinguished.

**Law 12 — Safety surfacing, not safety outreach.** *(Design decision — see §11 and §12.)* The Wing never initiates contact, escalates externally, or intervenes unsolicited. However, if previously logged information is directly safety-relevant to what the user is doing *in a user-initiated interaction*, the system may gently surface it in that interaction and must not bury it. The wall is against *pushing*, not against *honesty when asked to act*.

**Law 13 — Auditability.** Every access to the Health Vault, every profile change, every consent event, every agent action on health context, and every status transition is logged with actor, scope, time, and reason. The audit trail records activity; it is not itself evidence or working context, and it is visible to the user.

## 5. Room Boundaries

Each room has a declared purpose, a default data scope, and explicit prohibitions. Rooms read from the **Approved Health Profile** where health context is needed — never directly from the Health Vault (see §6).

### 5.1 Wellness Room

**Purpose:** The user's health-context home. Hosts the Health Vault (see §6), the Health Profile (Draft and Approved), symptom logs, supplement records, and health research notes.

**May:** organise records; display profile sections with their authority labels and last-reviewed dates; hold symptom logs as user-entered records; organise supplement information; hold research notes with source attribution; prepare clinician/pharmacist question lists.

**Must not:** interpret symptom logs into diagnoses or condition suggestions; trend symptoms into clinical conclusions; treat research notes as medical guidance; promote any record into the Approved Health Profile without the user's section-level review.

**Supplement boundary (tightened):** Supplement tools may organise the user's supplement records, source and compare product label information, surface *published* interaction information with citations to its sources, and prepare questions for a clinician or pharmacist. They may **not** recommend supplements against the user's health profile, advise starting, stopping, or changing anything, rank products by clinical suitability, or imply medical endorsement. The system prepares the conversation; it never has the conversation.

### 5.2 The Kitchen

**Purpose:** Nutrition, recipes, grocery planning, food preferences, and refill/staple tracking.

**May:** hold recipes and preferences; plan meals and groceries at the user's request; display neutral nutrition information where the user requests it; track staples and refills as user-maintained lists; read *relevant, scoped sections* of the Approved Health Profile (e.g., confirmed allergies, confirmed dietary requirements) under minimum necessary access; surface the age of any profile section it relies on.

**Must not:** read the Health Vault; infer dietary conditions, restriction patterns, or health states from food logs (Law 8); create deficit targets, weight-loss programmes, restriction loops, or moralised food scoring; auto-order anything; pass food data to any other room or external adapter without scoped consent.

**Harm-pattern guard:** The Kitchen may display neutral nutrition information where user-requested, but must not create deficit targets, weight-loss programmes, restriction loops, or moralised food scoring. It must not be usable as a restriction engine or reinforce disordered-eating patterns: no intake-reduction feedback loops, no "good/bad" food framing, no adherence tracking against targets. If the user requests such mechanics, The Kitchen declines that mechanic specifically and remains otherwise available.

### 5.3 The Gym

**Purpose:** Workouts, hikes, movement logs, rest and recovery.

**May:** record user-entered workouts and movement; hold plans the user creates or requests; track rest and recovery as user-maintained records; read scoped, confirmed profile sections where the user grants it (e.g., a confirmed injury note), surfacing profile age when doing so.

**Must not:** read the Health Vault; infer health or mental-health states from training patterns (Law 8); generate compulsive-exercise feedback loops (streaks, escalating targets, guilt mechanics); frame movement guidance as injury rehabilitation or treatment (Law 6).

### 5.4 Meditation Room

**Purpose:** Meditation, reflection, contemplative and spiritual practice, and — if the user chooses — a teaching or scripture library.

**May:** hold practice records, reflections, and contemplative notes; hold a user-curated library; support practice timers and study at the user's initiation.

**Must not:** share any data with any other room, agent, or adapter by default (Law 9); have its data used for wellness, nutrition, supplement, or fitness suggestions; be mined for mood, mental-health, or behavioural inference (Law 8 applies with full force); receive health, food, or fitness data by default. Contemplative and religious data is treated as a maximally sensitive category in its own right.

**Bridges:** If the user later wants a connection (e.g., "show meditation streaks alongside recovery days" — noting the Wing does not do streaks), it must be designed as an explicit, named, separately consented, revocable bridge in a later phase. W0 establishes the wall; bridges are exceptions to be individually constituted.

## 6. Health Vault Boundary

The **Health Vault** is the protected evidence layer: raw uploaded health records — clinical letters, pathology results, imaging reports, discharge summaries, prescriptions, and similar source documents.

**Core Health Vault law:** *The Health Vault is evidence. The Health Profile is derived context. The user decides what becomes active.*

Boundary rules:

1. **The Vault is not the working layer.** Rooms and agents normally read from the Approved Health Profile, never directly from the Vault.
2. **Vault access is exceptional.** Only the Health Profile Agent (see §7) may read Vault records, and only with explicit, scoped, per-purpose user permission. Each grant names what may be read and why.
3. **Raw records never leave.** Vault contents are not shared with other rooms, agents, adapters, or external services. Derived context moves (after approval); evidence does not.
4. **Provenance is preserved.** Every Profile entry derived from a Vault record retains a reference to its source record.
5. **Every Vault access is audited** with agent, scope, purpose, and timestamp, visible to the user (Law 13).
6. **Vault deletion is real deletion.** When the user deletes a Vault record, derived Profile entries citing it are flagged for the user's review (their evidence basis has changed), and the record itself is erased, not soft-hidden.
7. **Security posture.** The Vault is encrypted at rest and in transit, isolated at the storage layer from all working-layer data, and treated in threat modelling as the system's highest-value target (see §11, *The Vault as honeypot*).

## 7. Health Profile Agent Boundary

The **Health Profile Agent** is the single governed agent permitted to read the Health Vault. Its sole role is to turn evidence into reviewable draft context.

**Flow (central governance pattern of the Wing):**

> **Health Vault (evidence)** → **Draft Health Profile (agent-extracted, no authority)** → **user review, section by section** → **Approved Health Profile (active working context)**

**The Health Profile Agent may:**

- extract information from Vault records it has been explicitly permitted to read
- summarise health history
- organise conditions, medications, supplements, allergies, symptoms, pathology trends, procedures, and relevant notes
- flag contradictions and missing information across records
- identify outdated or superseded information and propose supersession
- prepare questions for the user or their clinician
- create draft updates to the Health Profile, each labelled with provenance and authority status

**The Health Profile Agent may not:**

- diagnose, prescribe, or recommend treatment changes
- override, reinterpret, or editorialise on clinician advice found in records
- auto-update the Approved Health Profile in any way
- share raw Vault records, excerpts, or reconstructions with other rooms or agents
- treat its own extractions as confirmed without user review
- retain Vault content beyond the scope and duration of the permitted task

**Authority labels.** Every Health Profile entry carries exactly one authority label:

| Label | Meaning |
|---|---|
| Confirmed by record | Supported by a cited Vault record and approved by the user |
| Confirmed by user | Asserted and approved by the user without a record source |
| User-reported | Entered by the user, not yet reviewed into approved status |
| Agent-extracted, pending review | Drafted by the Health Profile Agent; carries no authority |
| Possible pattern, not confirmed | A flagged observation; never used as working context |
| Outdated or superseded | Retained for history; excluded from working context |

**Review-fatigue controls (binding):**

1. Draft Profile approval happens **section by section**. There is no bulk "approve all."
2. **High-stakes fields require individual confirmation**, one item at a time: allergies, medications, diagnoses/conditions, pregnancy status, and clinician instructions.
3. Each approval records what was approved, its source reference, and the timestamp — which becomes that section's last-reviewed date (Law 7).
4. Review surfaces must show the *source excerpt beside the extraction*, so approval is a comparison, not an act of faith.

**Staleness controls (binding):**

1. Every Profile section carries a **last-reviewed timestamp**, displayed wherever the section is displayed or used.
2. **Re-review triggers** must exist for: section age exceeding a configurable threshold; a new Vault upload touching an existing section; a contradiction flag; and supersession proposals.
3. Any agent acting on Profile context must **surface the age** of the sections it relied on ("based on your medication list, last reviewed 14 months ago").
4. Stale sections are not silently dropped or silently trusted; they are visibly flagged and the user decides.

## 8. Privacy and Consent Principles

1. **User-owned by default.** The user is the data controller of their own Wing in every meaningful sense. The system is custodian, never owner.
2. **Consent is the only access path.** No room, agent, or adapter has standing access to anything. Grants are explicit, scoped (what), purposed (why), bounded (how long), and revocable (Law 10).
3. **No blanket consent.** "Allow everything" is not an offered option. Consent UI must make narrow grants the easy path.
4. **Sensitive categories get stricter treatment.** Health information, and separately contemplative/religious data, are treated as maximally sensitive categories with their own walls (Laws 8 and 9), consistent with the strictest treatment under the privacy regimes in §9.
5. **No secondary use.** Data collected for one purpose is not reused for another without a new, separate consent. No advertising use. No model training on user data without separate, explicit, revocable opt-in consent — never bundled with terms of use.
6. **Third parties are adapters, not partners.** External non-AI services — grocery, supplement, shopping, delivery, and similar vendors — operate through generic `VendorAdapter` interfaces receiving the minimum necessary payload (e.g., a grocery list — never the profile that shaped it). Connected AI systems and interfaces operate through the separate `AIAdapter` layer, which is consent-scoped and authenticated in its own right (§10; Open Question 10). The two adapter types are never overloaded into one. Whatever crosses either adapter boundary is logged and user-visible.
7. **Transparency.** The user can always see: what data exists, where it came from, what has access to what, what every agent did, and when. The audit trail (Law 13) is a user-facing feature, not an internal log.
8. **Erasure and portability are features.** Export in portable formats and genuine deletion are always available (Law 11), including separate handling for evidence (Vault) and derived context (Profile).

## 9. Privacy-by-Design Principles

The Wing does not claim HIPAA, APP, GDPR, or any other legal or regulatory compliance (Non-Goal 7). It is designed to privacy-by-design and healthcare-grade governance principles, adopting the **strictest common denominator** of three reference frameworks — each regime's most protective relevant principles, as alignment rather than compliance:

**HIPAA-aligned principles:**
- *Minimum necessary* access as a structural rule, not a guideline (Law 4)
- Administrative, technical, and physical safeguards proportionate to data sensitivity (encryption at rest and in transit, access controls, audit controls)
- Audit trails for all access to protected health context (Law 13)
- No disclosure of health information beyond consented scope

**APP-aligned principles (Australian Privacy Principles — sensitive health information):**
- Health information treated as a *sensitive information* category requiring consent for collection (APP 3 alignment)
- Collection limited to what is reasonably necessary for declared functions
- Use and disclosure limited to the primary, consented purpose (APP 6 alignment); no secondary use without fresh consent
- User access to, and correction of, their own information as a built-in capability (APP 12/13 alignment)
- Reasonable steps to protect from misuse, interference, loss, and unauthorised access (APP 11 alignment), and genuine destruction when no longer needed

**GDPR-style principles:**
- *Purpose limitation* and *data minimisation* as architecture, not policy
- *Explicit consent* as the lawful basis for special-category (health; religious/philosophical) data, with the Meditation Room's contemplative data recognised as special-category in its own right
- *Right to erasure* and *right to data portability* as first-class operations (Law 11)
- *Privacy by design and by default*: the most protective setting is always the default setting
- *Storage limitation*: retention defaults and user-controlled retention settings (see §12)

Where these frameworks differ, the Wing adopts the stricter requirement. The language throughout is deliberately *aligned*, not *compliant*: any formal compliance claim would require legal review and operational support, and is explicitly deferred (Non-Goal 7).

## 10. Agent Boundaries

These boundaries apply to **every** agent in the Wing — the Health Profile Agent (§7), room agents, research helpers, and any future agent — and to any connected AI system (AI_1, AI_2, or a user's external AI via an `AIAdapter`).

**Agents may:**
- retrieve, extract, and organise material within their consented scope
- compare options, prepare lists, and summarise with source attribution
- suggest *for review*, flag contradictions, identify missing or outdated information
- queue items for user review and prepare questions for professionals
- surface the authority label and age of any health context they rely on

**Agents may not:**
- decide, diagnose, prescribe, or recommend treatment changes (Law 6)
- override user consent, exceed granted scope, or extend their own permissions
- auto-update the Approved Health Profile or any approved record (Law 3)
- derive, record, or act on inferred sensitive conditions or states (Law 8)
- impersonate the user, or impersonate the user's own AI system to other services
- auto-order, auto-purchase, auto-book, or take any irreversible action through any `VendorAdapter` or otherwise without explicit, specific confirmation (Law 6)
- turn retrieved information, their own summaries, or other agents' outputs into authority without user review (Law 3)
- communicate across the Meditation Room wall (Law 9) or move data between rooms outside consented scope
- initiate contact with the user (Law 1), subject only to Law 12's surfacing rule within user-initiated interactions

**Agent-to-agent rule.** One agent's output is another agent's *unverified input*, never its evidence. Chained agents do not launder authority: a summary of a summary carries the authority of neither.

## 11. Risks and Failure Modes

These are the failure modes W0 exists to prevent. Each later phase must show, concretely, how its design addresses the failure modes it touches.

**1. Staleness drift.** *Approved health data silently becomes outdated and therefore unsafe.* An Approved Profile with a superseded medication or a missing new allergy is more dangerous than an empty one, because approval confers false freshness. Mitigation: Law 7 and the staleness controls in §7 — last-reviewed timestamps, section-level review dates, re-review triggers, and mandatory age-surfacing by agents.

**2. Cross-room inference leakage.** Individually innocuous data (food logs, training patterns, symptom entries) aggregates into inferred sensitive conditions the user never disclosed. Mitigation: Law 8 treats inference as an access path; room boundaries (§5) prohibit pattern-mining across scopes; the Meditation Room wall (Law 9) removes the most sensitive signal source entirely.

**3. Review fatigue and rubber-stamping.** The user bulk-approves their own Draft Profile, hollowing out the review gate. Mitigation: section-by-section approval, individual confirmation of high-stakes fields, and source-beside-extraction review surfaces (§7).

**4. Authority creep.** Agent summaries, repeated retrievals, or confident phrasing gradually get treated as confirmed context without anyone deciding they should be. Mitigation: Law 3, authority labels on every Profile entry, and the agent-to-agent rule (§10).

**5. Clinical-line creep.** Helpful features drift across the clinical line — supplement comparison becomes supplement advice; movement plans become rehabilitation; symptom organisation becomes triage. Mitigation: Law 6, the tightened supplement boundary (§5.1), and the prepare-the-conversation rule. Each release is reviewed specifically for clinical-line drift.

**6. Harmful-pattern reinforcement.** Tracking mechanics enable restriction, over-exercise, or compulsive monitoring. Mitigation: The Kitchen's harm-pattern guard (§5.2) — neutral nutrition information on request, never deficit targets, weight-loss programmes, restriction loops, or moralised food scoring — The Gym's prohibition on compulsive feedback loops (§5.3), and the Wing-wide absence of streaks, scores, and targets (Non-Goal 5).

**7. The held-harm tension.** The hardest tension in the Wing: Law 1 says nothing is pushed, yet a system that silently holds safety-relevant information while assisting a related task fails differently. **Design decision (Law 12):** no proactive outreach, no unsolicited intervention, no external escalation — but gentle, relevant safety surfacing is permitted *within user-initiated interactions*, and safety-relevant context must not be buried when the user is acting in its domain. The precise triggers, wording posture, and limits of surfacing are an open question for the next phase (§12) and must be designed deliberately, not emerge from prompt behaviour.

**8. The Vault as honeypot.** Centralising raw health records creates the system's highest-value attack target. Mitigation: storage-layer isolation, encryption, the single-agent access rule (§6), no raw-record egress, and threat modelling that treats the Vault as the crown jewels in every security review.

**9. Consent fatigue.** Over-asking trains the user to click yes, converting explicit consent into ritual. Mitigation: scoped grants that persist for their declared purpose (so the same question is not re-asked), clear consent dashboards, and a design rule that consent prompts are rare, specific, and consequential.

**10. Adapter leakage.** Third-party integrations receive more context than the task requires (a grocery vendor learning dietary medical context). Mitigation: the minimum-payload rule (§8.6), logged and user-visible adapter traffic, generic `VendorAdapter` interfaces with no vendor-specific data coupling, and a strict separation between `VendorAdapter` (non-AI services) and `AIAdapter` (connected AI systems), so neither adapter type inherits the other's scope.

**11. Wall erosion by convenience.** Incremental "wouldn't it be nice if The Kitchen knew about your meditation schedule" requests erode Laws 8 and 9 one small bridge at a time. Mitigation: bridges are individually constituted, named, consented, and revocable (§5.4); defaults never change; convenience is not an amendment process.

**12. Scope creep toward minors and crisis use.** The Wing drifts into use by minors or as a crisis-support tool, both excluded in §3. Mitigation: explicit positioning, honest in-product language about what the Wing is not, and clear signposting to professional and crisis resources where appropriate — provided as information, consistent with Law 1.

## 12. Open Questions Before Architecture

To be resolved (or explicitly deferred with rationale) before W1:

1. **Safety surfacing mechanics.** Law 12 sets the posture; the next phase must define triggers, scope, and wording discipline: What qualifies as "directly safety-relevant"? How is surfacing kept gentle and non-clinical? How does the system avoid the surfacing rule itself becoming an inference engine (tension with Law 8)? This is the Wing's hardest design problem and deserves its own decision document.
2. **Consent revocation cascade.** When consent is revoked, what happens to *derived* context created under that consent? Options: flag for review, quarantine, or cascade-delete. Each has safety and usability implications.
3. **Multi-profile and carer scenarios.** Households, carers, and parents are excluded from v1 (§3). If ever supported, delegation, consent-on-behalf, and the ethics of holding another person's health context need their own constitutional treatment.
4. **Retention defaults.** What are the default retention periods for symptom logs, movement logs, and reflections? Storage limitation (§9) requires defaults, not just user controls.
5. **Clinician export format.** What does "prepare for a clinician" produce — a structured summary, a question list, a profile extract with authority labels? Should it follow any existing health-summary convention?
6. **Local-first versus hosted.** Does the Vault live on user-controlled storage with the application as a client, or in hosted infrastructure with strong isolation? This decision shapes the entire security posture and should be made before schema design.
7. **Data residency.** If hosted: where, under which jurisdiction, and with what implications for the §9 frameworks?
8. **Audit trail surface.** What does the user-facing audit view actually look like, and how is it kept comprehensible rather than overwhelming (which would defeat its transparency purpose)?
9. **Break-glass access.** Is there any emergency-access concept (e.g., user incapacity), or is the absence of break-glass itself the design decision? Either answer must be explicit.
10. **Identity verification for connected AI systems.** When an external AI system (AI_1, AI_2) connects via an `AIAdapter`, how is it scoped and authenticated, and how is impersonation (§10) technically prevented?
11. **Units, localisation, terminology.** Health terminology, units, and medication naming differ across jurisdictions; extraction and display must handle this without introducing interpretation (which would brush Law 6).
12. **Evaluation harness scope.** Which laws are deterministically testable (access boundaries, label handling, staleness surfacing) and which require behavioural sandbox evaluation (clinical-line drift, inference prohibition)? Evaluation design should begin alongside architecture, not after it.

## 13. Recommended Next Phase After W0

**W1 — Governance Architecture and Data Boundary Design.** Still no UI and no production code. W1 should deliver:

1. **Data boundary map.** Every data category in the Wing, its sensitivity class, its home (Vault / Profile / room records / audit), and every permitted flow between them — with Laws 4, 8, and 9 expressed as explicit edges that do or do not exist.
2. **Consent and scope model.** The grant object: what a consent records (who, what, why, how long), how revocation works, and the resolution of Open Question 2.
3. **Authority and staleness model.** Schema-level design for authority labels, last-reviewed timestamps, re-review triggers, and supersession (Laws 3 and 7) — defined before any table is created, so governance is structural rather than retrofitted.
4. **Safety surfacing decision document.** Resolution of Open Question 1 as its own reviewed design decision.
5. **Threat model.** Vault-centred security analysis (failure mode 8) and the local-first versus hosted decision (Open Question 6).
6. **Evaluation plan skeleton.** Which constitutional laws map to deterministic tests versus behavioural evaluation (Open Question 12), so the Wing's compliance with its own constitution is testable from the first build phase.

Only after W1 is reviewed should schema, agents, or UI be designed. The build pattern is deliberate: **capability follows governance, not the other way around.**

---

*End of W0 — Wellbeing Wing Constitution (Draft 0.1). This document governs all subsequent phases. Amendments are explicit, versioned, and reviewed; the constitution is never silently bypassed.*
