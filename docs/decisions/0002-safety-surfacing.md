# 0002 — Safety Surfacing Doctrine

**Status:** Accepted by human reviewer, 2026-06-12 **Date:** 2026-06-12 **Constitutional references:** Laws 1, 6, 8, 11, 12, 13; W0 §3 (not a crisis tool), §11 failure mode 7 (the held-harm tension); resolves W0 Open Question 1; consumes W1-D1 (edges), W1-D2 (grants), W1-D3 (authority and staleness labels); constrains W1-D5, W1-D6, and any future notification layer.

## Context

W0 Law 12 set the posture: the Wing never initiates contact, but within user-initiated interactions it may gently surface safety-relevant information and must not bury it. That left the hardest question in the building open: **when governed labels indicate something safety-relevant needs attention, what may the Wing say, how strongly, and what must it never do?**

The tension is real on both sides. A Wing that surfaces too eagerly becomes a diagnosis engine, a nag, or a coercion machine — everything W0's non-goals exclude. A Wing that stays silent while assisting a task that relies on expired allergy data fails differently and worse. The doctrine must let the Wing say *"this may matter; please review it"* without ever saying *"I know what this means and you must act."*

One constraint shapes everything: by W1-D3, surfacing may not mint authority states, and by W1-D1, no inference pipelines exist to feed it. **Surfacing therefore has nothing to work with except governance labels** — and that limitation is the design.

## Decision

The Wing adopts the **speech-integrity model** of safety surfacing, defined by four doctrines, an intensity ladder, and a language law.

### Doctrine 1 — Surfacing reads labels, never bodies

A surfacing trigger is a **governance state**, not a health judgment: *stale*, *expired*, *contradicted*, *unknown*, *review due*, *pending review*, *possible pattern (queued)* — attached to data the current user-initiated task actually relies on. The Wing never computes risk, never analyses content for danger, never aggregates signals into concern scores, and never monitors in the background. If no D3 label says attention is needed, surfacing has no trigger — by construction, not restraint.

### Doctrine 2 — The subject of every safety sentence is the data, not the person

The Wing speaks about *its records*: their age, their provenance, their conflicts, their gaps. It never speaks about the user's body, condition, or risk. *"Your allergy list was last reviewed 18 months ago"* — allowed. *"Your allergies may have changed"* — not allowed: that is a claim about the person, inferred. This single rule prevents diagnosis, prediction, and paternalism at the grammatical level: a sentence whose subject is the data cannot overclaim about the human.

### Doctrine 3 — The Wing governs its own speech, never the user's actions

Nothing in this doctrine blocks the user from doing anything within the Wing's scope. What can be "blocked" is exactly one thing: **the Wing presenting unsound data as settled truth.** The Wing may decline to assert unsound data as settled truth; it does not use surfacing to block otherwise-permitted user action. The user may always acknowledge and proceed; the acknowledgment is recorded (C0) and the Wing proceeds with degraded claims, honestly framed. User authority is never overridden because the only thing ever withheld is the Wing's own overclaiming.

**Scope limit:** this doctrine governs surfacing behaviour inside the Wing's permitted scope. It does not override W0 non-goals, clinical boundaries (Law 6), the crisis-tool exclusion (W0 §3), or any refusal of out-of-scope requests — diagnosis, treatment instruction, medication changes, crisis handling, or other prohibited territory. The user may proceed with their own actions; the Wing is never obligated by this record to generate prohibited outputs. Anti-paternalism is not an answer-everything clause.

### Doctrine 4 — Surfacing happens only inside user-initiated interactions

Law 1 holds in full. No proactive outreach, no notifications, no reminders. Flags accumulate quietly (internal holding, per Law 1's clarification) and surface when the user arrives and acts somewhere they're relevant. A future opt-in notification layer, if ever built, requires its own decision record and may not inherit anything from this one by default.

### The intensity ladder

| Level | Name | When | Form |
| :---- | :---- | :---- | :---- |
| **L0** | Ambient honesty | Always | Authority and staleness labels visible wherever data is displayed (already required by D3 §6.1). Non-configurable — this is the honesty floor |
| **L1** | Queued | Item needs review but the current task doesn't rely on it | Appears in the review queue and room views; waits |
| **L2** | Inline | The current task *relies on* safety-relevant context that is review-due, stale, or user-vs-record conflicted | One plain sentence, before the output, with label, age, and provenance; output proceeds with uncertainty framing |
| **L3** | Pause-and-acknowledge | The current task relies on safety-relevant context that is **expired, contradicted, or unknown** (the D3 treat-as-unknown states) | The Wing pauses, states the governance fact, and asks the user to acknowledge before producing output that would otherwise rest on unsound ground. Proceeding is always available; the output then carries most-protective framing (D3 §6.3) |

**Safety-relevant** means, initially: allergies, medications, diagnosed conditions, injuries, pregnancy status, and clinician instructions — the same high-stakes set W0 §7 requires individual confirmation for. Extending the set is a future decision, not a runtime judgment.

Per-case treatment, mapping the governed states to the ladder:

| State (D3) | Surfacing |
| :---- | :---- |
| Stale safety-relevant item, task relies on it | L2; output carries explicit uncertainty |
| Expired safety-relevant item | L3; treated as unknown; most-protective framing |
| Contradicted safety-relevant item | L3; both sides shown with provenance and dates; never hidden (D3 T6); prepared clinician question offered |
| Unknown / absent evidence in a relied-on scope | L3 where safety-relevant; the scope and as-of time stated plainly; "unknown" never silently treated as "none" |
| Review-due items | L1; L2 only if relied on |
| User-reported vs record-confirmed conflict | L2; presented as two sourced statements with dates; the user resolves (D3 §5.2); no side endorsed |
| Agent *possible pattern* flags | **L1 only — never inline.** Pattern flags live in the review queue exclusively; surfacing patterns mid-task is ambient diagnosis pressure, and the queue is where review belongs |
| Kitchen / Gym room-level uncertainty | The room states what it relied on and how warm it was: most-protective framing for unknowns (D3 §6.3), uncertainty named in the plan or suggestion itself, never buried in a footnote |

### The language law

**Allowed:** descriptive, label-grounded, scoped, provenance-cited speech. *"X is contradicted by Y (March record vs May entry)." "Last reviewed 14 months ago." "Status unknown for the documents reviewed, as of January." "This may matter; please review it." "Worth verifying with your clinician/pharmacist before relying on this."*

**Prohibited:**

- Diagnosis or interpretation: "this suggests…", "this could indicate…"
- Prediction of harm or risk claims about the person: "you may be at risk of…"
- Imperatives about the user's body or actions: "you must…", "you need to…"
- Emotional leverage: fear framing, urgency theatre, guilt, "before it's too late"
- False reassurance: "you're probably fine" — reassurance is a truth-claim too, and an ungrounded one
- Softening that hides uncertainty to appear helpful — the D2 §4 rule extends here: *if the honest sentence sounds concerning, the sentence is working*; it is never reworded to lower acknowledgment friction, and never dramatised to raise it
- Repetition within an interaction: once acknowledged, an item does not re-surface in the same interaction
- Escalation over time: there is no "user ignored three flags, intensify" ladder. Ignoring a flag is a user decision, recorded once, respected thereafter until a new trigger (new evidence, new conflict, new expiry) occurs. Escalation-on-noncompliance is coercion with patience, and it is barred

### What remains user-controlled

Acknowledgments persist per item until a *new* trigger arises. L2/L3 sensitivity for non-safety-relevant items is user-configurable. The safety-relevant set's L3 behaviour and the L0 honesty floor are not configurable — not as paternalism, but as integrity: the user commands their actions and their data; the Wing's own speech staying honest is the one thing that is the Wing's. **The user controls what they do; the Wing controls only what it claims.**

## Constitutional check

- **Law 1:** all surfacing is within user-initiated interaction; flags hold, never push; the future notification layer is explicitly fenced off (Doctrine 4).
- **Law 6:** the clinical line holds at the grammar level — Doctrine 2 makes diagnosis grammatically impossible, and prepared-questions remain the only clinical-adjacent output. Doctrine 3's scope limit makes explicit that anti-paternalism never obligates the Wing to cross this line: declining out-of-scope requests is a W0 boundary, untouched by this record.
- **Law 8:** no inference, no aggregation, no risk scoring; triggers are labels the system already lawfully holds (Doctrine 1). Surfacing creates no new knowledge about the person.
- **Law 11 / W0 §3 (capable adult):** proceeding is always available; acknowledgment, not permission (Doctrine 3).
- **Law 12:** this record is the mechanics Law 12 promised: gentle, relevant, never buried, never outreach.
- **Law 13:** surfacing events, acknowledgments, and proceed-decisions are C0 ledger entries — and, per D1/D3, that metadata is pattern-sensitive: no analytics, no profiling, no "which warnings does this user ignore" datasets, ever.
- **W1-D3:** consumes labels; mints none. The treat-as-unknown and most-protective rules are applied, not extended.

No law is amended. This record resolves W0 Open Question 1 within existing constitutional bounds.

## Alternatives considered

**1. Silence (labels only, no surfacing).** Maximal anti-paternalism; rejected: it re-opens failure mode 7 — a system that quietly holds known-unsound safety context while helping someone act on it is complicit in the failure it watched. L0 alone buries uncertainty in ambient detail.

**2. Proactive safety notifications.** Surface immediately, push when important; rejected: violates Law 1, converts the Wing into an engagement product wearing a safety badge, and creates the monitoring infrastructure W0's non-goals exclude. Held, not pushed — even for safety. The narrow cost of waiting until the user arrives is the price of a Wing that never reaches into a life uninvited.

**3. Hard blocking.** Refuse to operate on expired/contradicted safety data until reviewed; rejected: overrides user authority, converts governance into gatekeeping, and teaches users to game reviews to unlock function — corroding the review gate it claims to protect. Doctrine 3 takes the defensible core (the Wing won't *assert* unsound data) and discards the coercive shell.

**4. Configurable everything (user may disable all surfacing).** Respects autonomy maximally; rejected for the honesty floor only: a Wing that can be configured to misrepresent its own data quality isn't offering a preference, it's offering to lie. Everything above the floor is configurable.

## Consequences

**Easier:** D6 gains a deterministically testable language law (prohibited constructions are gradeable — the "negation is not overclaim" lesson applies directly: correctly saying "unknown" must never be penalised as alarmism). Future surface design has a complete doctrine to implement rather than invent. The held-harm tension (failure mode 7) is closed with a named mechanism.

**Harder — named costs:** No dramatic safety theatre — the Wing will sometimes watch a user proceed against an L3 acknowledgment, record it once, and respect it; that restraint is a feature and will occasionally feel like one only in retrospect. The language law puts real discipline on every future string of UI text; wording is now governed surface, not copywriting. And the safety-relevant set is fixed small to start — some users will want more items covered, and extending the set is a decision-record process, deliberately slower than a config flag.

**Constrains:** W1-D5 must threat-model surfacing suppression and forgery (hiding a real flag; faking an acknowledgment). W1-D6 must grade both overclaim *and* underclaim in surfacing language. Any future notification layer starts from zero inheritance. The revocation cascade record must keep *derived under revoked consent* flags compatible with this ladder.

## Open questions created

1. **Acknowledgment persistence defaults** — per item forever-until-new-trigger, or time-bounded for the safety-relevant set?
2. **Wording standardisation and reading level** — the language law needs a vetted phrase set before any surface exists (joint with D2 §8.6).
3. **The safety-relevant set's governance** — who proposes extensions, and does extension need clinical-adjacent input?
4. **L3 and accessibility** — pause-and-acknowledge must be designed so it cannot become a dark pattern in reverse (an acknowledgment users click blind); evaluation should measure this (D6).
5. **Interaction with multi-device state** — acknowledgments are C0; whether they sync across devices lands with the key-distribution design (ADR 0001 consequence).
