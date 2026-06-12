# W1-D3 — Authority & Staleness Model

**Status:** Accepted by human reviewer, 2026-06-12 · **Date:** June 2026
**Phase:** W1 — Governance Architecture and Data Boundary Design (deliverable 3 of 6)
**Governed by:** W0 Constitution (esp. Laws 3, 7, 8, 11, 13); ADR 0001; W1-D1 Data Boundary Map; W1-D2 Consent & Scope Model
**Scope:** Documentation only. This document defines the authority grammar: how the Wing decides what may be treated as true, what is merely evidence, what is derived, what is stale, what is contradicted, and what must never become authority without review. No schema, code, UI, scoring logic, or medical logic is authorised by this document.

---

## 0. Core posture

1. **Three axes, never collapsed.** D1 governs movement (what may flow where). D2 governs permission (what the user has delegated). D3 governs truth and freshness (what may be *believed*, and how warmly). The axes are orthogonal and none implies another: **available is not permitted; permitted is not true; true-once is not true-now.** A grant may allow access; it never raises truth status. Sensitive data may be unverified; trivial data may be stale or wrong.
2. **Every governed item carries two labels.** An authority label (how its truth status was earned — §1) and a staleness label (whether that status is still warm — §2). The pair travels with the item through every read, every display, and every use. An item missing either label is not usable as working context.
3. **Only the user mints truth.** Agents extract, propose, flag, and compare. Evidence supports. Review confirms. Nothing in the Wing — no agent, no model output, no retrieval frequency, no consent grant, no passage of time — can promote an item to confirmed status except a user review act.

## 1. Authority labels

| Label | Meaning | Assigned by | Working context? |
|---|---|---|---|
| **Confirmed by record** | Supported by a cited Vault record and approved by the user in section review | User review only | Yes (subject to staleness) |
| **Confirmed by user** | Asserted by the user and approved, with no record source; provenance is the user's own statement | User review only | Yes (subject to staleness) |
| **User-reported** | Entered by the user (logs, notes) but not reviewed into approved status | System, on user entry | Room-scoped use only; never profile truth |
| **Agent-extracted, pending review** | Drafted by an agent from evidence; awaiting review | Agent | No. Zero authority |
| **Possible pattern, not confirmed** | A flagged observation (e.g., a contradiction cluster, a recurring trend) | Agent, as a flag only | No. Never working context; exists only to be reviewed or to expire |
| **Contradicted** | Conflicting evidence or assertion exists; item is suspended from settled-truth use — visibly, never hidden — pending resolution | System flags on detection; user resolves | Not as settled truth, while flagged; remains visible as unresolved conflict |
| **Outdated / superseded** | Replaced by a newer authoritative item; retained as history with its succession recorded | User review (or user correction, §4 T7) | No. History only |
| **Unknown / absent evidence** | An explicit record that the Wing has no information on a point | System or user | Yes — *as unknownness*. See §5.5: absence of evidence is never evidence of absence |

Three rules complete the label set:

- **Only the top two labels are truth.** Everything else is evidence, draft, flag, history, or honest ignorance.
- **Agents may assign only their own two labels** (agent-extracted; possible pattern) and may *propose* contradiction or supersession flags. They may never assign, remove, or alter a confirmed label.
- **"Unknown" is a first-class state, not an empty cell — and it is always bounded.** Unknown / absent evidence is always scoped by a named scope, source set, and review time. It means the Wing has no confirmed information *in that scope, as of that time*; it never means the fact is false, and it never means no evidence exists anywhere. "No record found in the reviewed documents" must never quietly become "not present." The difference between "no allergies confirmed" and "allergy status unknown" is a safety boundary, and the Wing records which one it actually has — and for what scope.

## 2. Staleness labels

Staleness runs on the last-reviewed timestamp every confirmed item carries (W0 Law 7). Intervals are per data type (numbers are an open question, §10.1); the label semantics are fixed here:

| Label | Meaning | Working use |
|---|---|---|
| **Current** | Within its review interval | Normal use, age surfaced |
| **Review due** | Interval passed; renewal surfaces at next relevant use | Usable, with a visible review-due flag |
| **Stale** | Past the renewal grace period | Usable only with explicit uncertainty surfacing in any output that relies on it |
| **Expired** | Past the hard limit for its type | Not usable as truth. Treated as **unknown** until re-reviewed |
| **Superseded** | Replaced; permanent terminal state | History only |
| **Unknown freshness** | No reliable review date (e.g., imported material) | Treated as stale until reviewed |

Two structural rules:

- **Staleness transitions are the only automatic transitions in the Wing.** Time may move an item from current → review due → stale → expired, label-only, no content change. Authority transitions (§4) always require the user. Nothing ever automatically becomes *more* trusted; things may only automatically become *less*.
- **Renewal is a review act, not a refresh.** No agent may silently re-confirm, re-date, or "touch" an item to reset its clock (§8.2). The user re-reviews; the timestamp follows.

## 3. What each layer may do

| Layer | Is | May | May never |
|---|---|---|---|
| **Health Vault** | Evidence | Anchor provenance; be read by the Health Profile Agent under an E2 grant | Be working context; be read by rooms; have its contents treated as profile truth without extraction and review |
| **Draft Health Profile** | Derived context, pending review | Hold agent extractions with provenance and labels; queue section-by-section review | Be read by rooms; be treated as context by any agent; gain authority by waiting |
| **Approved Health Profile** | Working context | Serve scoped sections to allowed rooms via E6/E7 under D2 grants — with both labels attached | Be assumed current (Law 7); be extended by agents; serve suspended (contradicted) or expired items as truth |
| **Room records** | Room-scoped context | Inform activity inside their own room; be processed under that room's E11 edge on request | Become profile truth automatically; cross rooms; be mined for patterns that raise authority anywhere (Law 8) |
| **AI / agent outputs** | Suggestions | Create review candidates, flags, comparisons, and prepared questions | Be authority; be evidence; be input to another agent as either (W0 agent-to-agent rule); promote anything |

## 4. Authority transitions

These are the only legal transitions. As with D1's edges: a transition not listed does not exist.

- **T1. Vault record → agent extraction.** Under an E2 grant. Output lands as *agent-extracted, pending review*, with provenance reference. (D1 E2→E3.)
- **T2. Pending review → confirmed by record.** User section review, high-stakes fields individually (W0 §7). Review timestamp set; staleness clock starts.
- **T3. User entry → user-reported.** Automatic on entry into room records; carries no profile authority.
- **T4. User-reported → confirmed by user.** User review promotes their own report into the Approved Profile, recorded as user-provenance.
- **T5. Confirmed → review due → stale → expired.** Automatic, time-driven, label-only (§2). The only self-acting transitions, and they only ever lower warmth.
- **T6. Conflict detected → contradicted.** When new evidence, a new extraction, or a user statement materially conflicts with a confirmed item, the system flags both sides and records the conflict. **The confirmed item is suspended from settled-truth use, not hidden.** Both sides remain visible as unresolved conflict, with provenance and dates attached. For safety-relevant use, rooms must apply most-protective framing (§6.3) until the user resolves the conflict. Suspension is automatic; resolution never is. Automated systems may lower trust, never raise it — but they may not make important uncertainty disappear. (Design judgment flagged in §9.)
- **T7. User correction → immediate override.** The user's correction takes effect at once: the corrected item becomes *superseded*, the correction enters as *confirmed by user* (or re-anchored to record if one exists). The user is the final authority and is never queued behind their own system (Law 11).
- **T8. Supersession.** An obsolete item becomes *superseded*: retained, linked to its successor, visible in history. **Nothing authoritative is ever silently deleted.** Removal of history is exclusively the user's erasure right (D2 §0.3), exercised knowingly — never a side effect of an update.

No transition skips review. No agent performs T2, T4, or T7. No sequence of T1–T8 can launder an agent suggestion into truth without a user act in the chain.

## 5. Contradiction handling

Contradiction is information, not error. The Wing's job is to *hold disagreement honestly*, not to resolve it cleverly.

1. **Record vs record.** Both records stand as evidence; any profile item derived from either is flagged *contradicted* and suspended; the conflict is presented with both sources, dates, and provenance; a clinician question is auto-prepared (as a draft, E9-preparable). The system never adjudicates which clinical document is right.
2. **User report vs record.** Neither auto-wins. Both are surfaced with provenance ("your record from March says X; you reported Y in May"). The user decides what enters their profile — it is their profile (Law 11) — and the resolution is recorded with the user's note. Where the conflict is clinically material, the prepared-question pattern applies: the Wing prepares the conversation with the clinician; it never has it.
3. **Extraction vs approved profile.** The new extraction does not displace the approved item — it triggers T6: flag, suspend, queue for review with both versions visible. Newer is not truer until the user says so.
4. **Newer data vs older approved context.** Same as above, with one addition: the staleness of the older item is surfaced alongside the conflict, since "old and contradicted" resolves differently than "fresh and contradicted."
5. **Absence vs negative evidence.** The deepest trap in health context. *No record of an allergy* is not *no allergy*. The Wing maintains the distinction structurally: rooms and agents consuming profile context receive either a confirmed negative ("no known allergies — confirmed by user, current"), or **unknown** — and must behave according to which (§6.3). No layer may ever convert silence into a negative claim.

## 6. Room consumption rules

Rooms read approved sections only through their D1 edges (E6, E7) under D2 grants — and must additionally honour both labels on every read:

1. **Surface age always.** Every use of profile context carries its authority label and section age into the interaction ("based on your allergy list — confirmed by record, last reviewed 14 months ago").
2. **Degrade with freshness.** *Review due*: use with visible flag. *Stale*: use only with explicit uncertainty surfacing in the output itself. *Expired or contradicted*: do not treat as truth — treat as **unknown**.
3. **Unknown means most-protective, where safety-relevant.** When a safety-relevant item (allergy, medication, condition, injury) is unknown, expired, or suspended, the room behaves in the most protective reasonable way and says why: The Kitchen treats allergy-status-unknown as "verify before relying on this plan," not as all-clear. The Gym treats an expired injury note as "this may still apply," not as healed. Most-protective is a *display and framing* rule — it never becomes diagnosis, inference, or a new recorded claim (Law 8 and W0 Law 6 both bind).
4. **Whether staleness ever hard-blocks room functionality** (rather than warns and degrades) is left open (§10.6) — but the floor is fixed here: no room may present stale or unknown health context as stable truth, ever.

## 7. Staleness as governance

"Approved" must not mean "forever current." Staleness is not an inconvenience to be minimised; it is the honest decay of confidence over time, made visible and governed:

- Review intervals are set **per data type**, not globally — medications and allergies decay faster than dietary preferences (intervals: open question §10.1).
- Re-review triggers, inherited from W0 §7 and extended: interval lapse; a new Vault upload touching the section; a contradiction flag; a supersession proposal; a user request.
- Renewal prompts are internal flags surfaced at next relevant use (Law 1 — the Wing holds; it does not push), batched to respect review fatigue (W0 failure mode 3, D2 §8.7).
- The consent layer mirrors this (D2 §3.2): grants go stale too. A Wing where permissions decay but "facts" don't — or vice versa — has a hole; both decay, both visibly.

## 8. Prohibitions (the anti-grammar)

No agent, model, room, or automated process may:

1. Promote extracted data to approved truth.
2. Silently refresh, re-date, or re-confirm stale data.
3. Delete superseded data without governance — history removal is the user's erasure right alone.
4. Treat consent as truth — a grant authorises access, never belief.
5. Treat repeated mention as confirmation — frequency is not evidence (this is recursive evidence inflation, named and barred).
6. Treat a pattern as a diagnosis — patterns flag for review; they never conclude (Laws 6, 8).
7. Treat absence as negative evidence (§5.5).
8. Use cross-room signals to raise authority anywhere (Law 8 — inference is not provenance).
9. Turn AI reasoning into evidence — model output is suggestion at birth and suggestion forever, until a user review act says otherwise.

### 8a. D3 records are governance metadata (C0)

The authority labels, staleness labels, review timestamps, contradiction flags, supersession links, and transition logs that D3 creates are **C0 governance metadata** under W1-D1: content-free with respect to health, personal, and contemplative content, but **privacy-sensitive by pattern**. The pattern of what gets reviewed, contradicted, or superseded — and when — is itself a sensitive signal. Accordingly, D3 records must not become analytics, behavioural profiling, cross-room inference, authority scoring, or ambient shadow profiling. They may support governance, audit, review, and user-visible export only. The D1 ledger rule binds in full: governance metadata has no processing edges.

## 9. Constitutional check

- **Law 3 (nothing self-promotes)** is this document's spine: §0.3, §4 (no agent performs T2/T4/T7), §8.1, §8.9.
- **Law 7 (approved is not current)** is expanded from a principle into a label system with semantics (§2), per-type decay (§7), and room-level consequences (§6).
- **Law 8** is reinforced at the authority layer: cross-room signals and patterns cannot raise truth status (§8.6, §8.8), closing the inference path D1 closed at the movement layer.
- **Law 11** governs T7: the user's correction is immediate and unqueued; their erasure right is the only path to history removal (§4 T8, §8.3).
- **Law 13**: every transition, flag, suspension, and resolution is a ledger event; contradiction resolutions record the user's rationale.
- **ADR 0001 and D1/D2** bind throughout: extraction happens only under E2 grants; labels travel only along permitted edges; consent never raises authority (§8.4 — the explicit anti-collapse of axis two into axis three).

Two design judgments flagged for review: **(a) automatic suspension on contradiction (T6).** Suspending a confirmed item the moment material conflict is detected is safety-conservative but means an agent flag can *remove* working context (never add it). The asymmetry is deliberate — automated processes may lower trust, never raise it — but it gives flags real teeth, and review should confirm that's intended. **(b) Expired-means-unknown plus most-protective framing (§2, §6.3).** This makes time alone capable of converting "no allergies" into "verify before relying" — strict, and arguably the entire point of the document, but it has UX consequences worth naming before anyone designs surfaces.

## 10. Open questions

1. **Default review intervals by data type.** Medications, allergies, conditions, injuries, preferences — each needs a number and a grace period. Deserves a short, focused decision record with clinical-adjacent input.
2. **Class-differentiated expiry rules.** Should expiry hard-limits differ by D1 sensitivity class as well as by data type, or is type alone the right axis?
3. **Emergency / safety flags.** Whether any authority state can carry a safety flag that alters surfacing behaviour is deferred to D4 — with the note that D4 must consume the labels defined here and may not mint new authority states.
4. **Clinician-confirmed vs user-confirmed conflicts.** §5.2 gives the default (neither auto-wins; user decides; conversation prepared). Whether clinician-sourced records deserve a distinct provenance tier within *confirmed by record* is open.
5. **History depth after supersession.** How much superseded lineage stays visible by default — full chain, last predecessor, or user-configured?
6. **Block vs warn.** Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor).
7. **Re-authentication for authority changes.** Should high-stakes confirmations (allergies, medications, pregnancy status, clinician instructions) require fresh authentication at review time, aligned with D2 §8.2? Lands with the threat model (W1-D5).
8. **Pattern hygiene.** Should *possible pattern, not confirmed* items auto-expire if never reviewed within an interval, so unconfirmed flags cannot accumulate into an ambient shadow-profile?

## 11. Feeds into

- **W1-D4 (safety surfacing):** consumes these labels; may not create authority states; the unknown/most-protective rules (§6.3) are its raw material.
- **W1-D5 (threat model):** authority forgery — anything that could fake a confirmed label or a fresh timestamp — joins the attack surface; re-authentication questions land there.
- **W1-D6 (evaluation plan):** label assignment, transitions, suspension, and surfacing are deterministically testable; "negation is not overclaim" class lessons apply to grading unknown-handling.
- **Revocation cascade decision:** artefacts derived under revoked consent (D2 §5.5) need an authority disposition consistent with this grammar.
