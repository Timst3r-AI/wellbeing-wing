# 0020 — Unknown/Stale/Contradicted Behaviour Standard

**Status:** Accepted by human reviewer, 2026-07-11. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (fifth doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — the states, labels, and floors are already sealed in W1-D3; this record decides their uniform transmission into the four contracts.
**Controlling law:** W1-D3 (the accepted authority/staleness model — the controlling source); W0 Laws 6, 7, 8, 11; W1-D1 (edges); W1-D2 (grants; grants decay too).
**Blocks:** the Unknown/stale/contradicted behaviour section of every room contract (W4-D2 … W4-D5), which carries this record's shared table.

## Decision question

Every room will sometimes stand on ground that is unknown, stale, expired, or contradicted. **How does each room behave in that moment — one shared standard, not four hand-rolled answers?** The states, labels, and floors are already decided in the sealed W1-D3; this record decides the transmission and uniformity mechanism: one authoritative table, carried into every contract without drift, instantiated in room wording only where the source permits wording — and resolving nothing W1-D3 left open.

## Context

W4 is open for governed doctrine and brief work only; this is the proposed fifth of six W4-D1 doctrine records. ADR 0016 fixed the contract slot ("uncertainty carried in the output itself, never only beside it"); ADR 0018 supplied the fidelity mechanism (exact reference plus complete verbatim quotation); ADR 0019 closed the speculation path (uncertainty is never an inference licence). What remains is the behaviour standard itself: the one table all four rooms answer to when their ground is weak, whose floor W1-D3 §6.4 already seals — *no room may present stale or unknown health context as stable truth, ever.* This record transmits that standard; it builds nothing and resolves no sealed open question.

## Controlling law

- **W1-D3 — the controlling source.** §2 (staleness label semantics — the six states); §5 (contradiction handling — disagreement held honestly, never resolved cleverly); §6 (room consumption rules — surface age always, degrade with freshness, most-protective where safety-relevant, the §6.4 floor); §7 (staleness as governance — renewal is a review act, not a refresh); §10.6 (the block-vs-warn open question, which remains open).
- **W0 Law 6 and Law 8** — most-protective framing never becomes diagnosis, inference, or a new recorded claim.
- **W0 Law 7** — the last-reviewed timestamp every confirmed item carries; staleness runs on it.
- **W0 Law 11** — the user is the final authority over their own record; no room resolves an authority dispute.
- **W1-D1 / W1-D2** — rooms read only through their edges under grants; grants decay too (D2 §3.2); a room cannot enlarge its scope to cure uncertainty.

## Decision

1. **W1-D3 is the controlling source.** Every state, label, floor, and precedence rule below is W1-D3's; where any other document differs, W1-D3 wins.
2. **One shared behaviour table governs all four rooms.** It is never re-derived independently per room, paraphrased, simplified, modernised, expanded through examples, or narrowed through room-specific interpretation.
3. **Every contract carries the table through exact reference plus complete verbatim quotation** (the ADR 0018 paired form applied to this table). A quotation/reference mismatch fails review.
4. **Rooms instantiate wording, not rules.** Room-register wording may realise the shared rule only where the source permits wording; it may not alter the underlying behaviour. Final strings route to the future governed string catalogue (W6).
5. **Unknown means unknown.** Absence is not confirmation; missing information may not be filled from another room, an earlier interaction, or a behavioural pattern; no claim, warning, restriction, or recommendation is minted from an absence.
6. **The six W1-D3 states bind as sealed:** current information carries its authority label and age; review-due information carries its visible flag; stale information is usable only with explicit uncertainty in every output that relies on it; expired information is not usable as truth and is treated as unknown until re-reviewed; superseded information is history only; unknown freshness is treated as stale until reviewed.
7. **Contradiction is held honestly, not resolved cleverly.** Both sources, dates, provenance, and relevant staleness are surfaced; competing claims are never collapsed, averaged, merged, or reconciled without an authorised review transition; **newer is not truer until the user says so**; no room resolves an authority dispute.
8. **For the safety-relevant set, the inline uncertainty sentence is always shown.** The always rule is not grace-conditioned. No percentages, thresholds, durations, cadence, or room-specific grace values are invented; intervals per data type remain W1-D3 §10.1's own open decision.
9. **Most-protective framing is surfacing and verbal only.** It mints no claim, diagnosis, inference, restriction, recommendation, unsupported warning, new status, substituted value, consent state, or authority state.
10. **The acknowledgement-before-continuing rule (source-anchored):** for safety-relevant expired, contradicted, or unknown context, **the room must acknowledge the state and the reason inline before continuing under the W1-D3 §6.4 floor.** **This is a surfacing-order requirement, not a functional block, refusal, interruption, or answer to the block-versus-warn question.** For non-safety context, uncertainty is named in the output; no pause, interruption, or acknowledgement gate exists.
11. **Hard-block versus warn remains open under W1-D3 §10.6.** Every relevant table row carries the §6.4 floor without assigning blocking behaviour; this record does not resolve, and does not recommend an answer to, the sealed open question.
12. **Room tone may not soften, hide, or reinterpret the truth state.** The shared semantic content remains controlling in every register.
13. **The slots and walls compose:** ADR 0016 supplies the contract slot; ADR 0018 supplies the fidelity mechanism; ADR 0019 prevents uncertainty from becoming an inference licence; W6 owns final strings and catalogue IDs later.

## Constitutional check

- **Law 6 and Law 8 are served:** most-protective framing is fixed as display-and-framing only — it can never become diagnosis, inference, or a new recorded claim, and a gap can never be filled by cross-room or pattern inference (ADR 0019 binds alongside).
- **Law 7 is served:** age and review status surface at every use; nothing automatically becomes more trusted.
- **Law 11 is served:** contradictions resolve only by the user's review act; no room adjudicates.
- **No new authority:** no new label, class, threshold, transition, or consent rule is minted; the sealed §10.6 question is carried, not answered.
- **No law required reinterpretation**, and **no amendment to W1-D3 or the Constitution is proposed or required.**

## Shared behaviour table

The foundation is the **verbatim W1-D3 §2 label semantics** — all six states:

| State (W1-D3 §2) | Meaning (verbatim) | Working use (verbatim) |
|---|---|---|
| **Current** | "Within its review interval" | "Normal use, age surfaced" |
| **Review due** | "Interval passed; renewal surfaces at next relevant use" | "Usable, with a visible review-due flag" |
| **Stale** | "Past the renewal grace period" | "Usable only with explicit uncertainty surfacing in any output that relies on it" |
| **Expired** | "Past the hard limit for its type" | "Not usable as truth. Treated as **unknown** until re-reviewed" |
| **Superseded** | "Replaced; permanent terminal state" | "History only" |
| **Unknown freshness** | "No reliable review date (e.g., imported material)" | "Treated as stale until reviewed" |

The behaviour rows, anchored on W1-D3 §6; cells a source does not specify are marked, never filled by interpretation:

| # | Context state | Surfaced | May continue | Must not occur | Authority/age display | Uncertainty sentence | Review route | Hard-block/warn |
|---|---|---|---|---|---|---|---|---|
| 1 | **Current** | Age (the honesty floor) | Normal use | Presenting without age (§6.1) | Label and age on every use (§6.1) | Not required | Renewal at next relevant use (§7) | Not applicable |
| 2 | **Review due** (non-safety) | Visible review-due flag (§2) | Use, flagged | Hiding the flag | Label and age carried | Not required by §2; flag required | Renewal surfaces at next relevant use (§2, §7) | **Open (§10.6)** — floor only |
| 3 | **Review due / stale + safety-relevant + relied-on** | Inline sentence; output carries explicit uncertainty (**always** — not grace-conditioned) | Use, with uncertainty in the output itself | Output without the inline sentence | Label and age carried | **Always** | Re-review trigger (§7) | **Open (§10.6)** — floor only |
| 4 | **Stale** (non-safety) | Uncertainty named in the output itself (§2) | Use, with uncertainty in-output | Output that omits the uncertainty | Label and age carried | Required (§2) | Re-review trigger (§7) | **Open (§10.6)** — floor only |
| 5 | **Expired / contradicted / unknown + safety-relevant** | Treated as **unknown**; the state and the reason acknowledged inline before continuing (decision 10); most-protective framing with the reason stated (§6.2–6.3) | Only in the most protective reasonable way, saying why (§6.3) | Treating as truth (§6.2); converting silence into a negative claim (§5.5); manufacturing any claim, restriction, or recommendation (§6.3) | Both labels honoured on every read (§6); contradiction: staleness of the older item surfaced alongside (§5.4) | Required — the reason stated | Re-review / user review; contradiction queues per §5 (both versions visible; prepared question where clinically material) | **Open (§10.6)** — floor: never present as stable truth |
| 6 | **Expired / contradicted / unknown** (non-safety) | Treated as unknown; uncertainty named in the output | Use with uncertainty named | Treating as truth | Labels honoured; status surfaced | Required | Re-review route | **Open (§10.6)** — floor only |

**Coverage note (not a contradiction):** the planning record's behaviour rows do not restate the **Superseded** and **Unknown freshness** labels; the shared table inherits them from §2 unchanged — superseded items are history only, and unknown-freshness items take the stale row's behaviour.

**Source-fidelity note (reported, not harmonised):** the planning record's row 5 used a pause phrase with no W1-D3 anchor; per accepted ruling it is replaced by the source-anchored acknowledgement wording of decision 10, which is explicitly a surfacing-order requirement and not a functional block. Neither source is amended.

## Unknown behaviour

When relied-on information is **unknown**: state that it is unknown; do not infer the missing value; do not fill the gap from another room, prior interaction, or behavioural pattern; do not treat absence as confirmation; do not silently proceed as though a value were known; do not mint a claim, warning, restriction, or recommendation from the absence. The controlling language is **W1-D3 §5.5**, verbatim: *"No record of an allergy is not no allergy. … rooms and agents consuming profile context receive either a confirmed negative ('no known allergies — confirmed by user, current'), or **unknown** — and must behave according to which (§6.3). No layer may ever convert silence into a negative claim."*

## Stale behaviour

When relied-on information is **stale** (§2: "past the renewal grace period"), it is *"usable only with explicit uncertainty surfacing in any output that relies on it"* (verbatim §2). Its age is surfaced; the uncertainty lives **in the output itself, never only beside it** — the artifact stays honest after the surfacing moment passes. It is never described as current; never silently refreshed, reinterpreted, or upgraded (§2, verbatim: *"Renewal is a review act, not a refresh. No agent may silently re-confirm, re-date, or 'touch' an item to reset its clock"*); never inferred to remain true; and no replacement value is invented.

## Expired behaviour

When relied-on information is **expired** (§2: "past the hard limit for its type"), it is *"not usable as truth. Treated as **unknown** until re-reviewed"* (verbatim §2). The unknown behaviour then governs, with the expiry status surfaced. Nothing automatically becomes more trusted (§2, verbatim: *"Nothing ever automatically becomes more trusted; things may only automatically become less"*).

## Contradicted behaviour

The controlling source is **W1-D3 §5** — verbatim: *"Contradiction is information, not error. The Wing's job is to hold disagreement honestly, not to resolve it cleverly."* The room surfaces the contradiction with both sources, dates, and provenance; preserves the authority/provenance labels and timing information; does not silently select the more convenient statement; does not collapse competing claims into a new synthetic claim; does not average, merge, or reconcile them without an authorised review transition; and — verbatim §5.3 — *"**Newer is not truer until the user says so.**"* "Most recent" is not automatically most authoritative. **No room resolves an authority dispute** — resolution is the user's (§5.2, Law 11), with the prepared-question pattern where clinically material; §5.4 adds that the staleness of the older item is surfaced alongside the conflict. Contracts carry §5's exact precedence language; no new conflict algorithm is derived.

## Safety-relevant always rule

**For the safety-relevant set, the inline uncertainty sentence is always shown** — not conditioned on a numerical or proportional grace threshold. The safety-relevant set is **W1-D3 §6.3's, verbatim**: *"a safety-relevant item (allergy, medication, condition, injury)"* — no new category list is invented. Also not invented here: percentages; elapsed-time thresholds; room-specific grace values; severity levels; expiration durations; warning cadence. Review intervals and grace periods per data type remain W1-D3 §10.1's own open decision; any mechanism belongs to a later record or catalogue decision.

## Most-protective framing

**Most-protective framing is surfacing and verbal only** (W1-D3 §6.3, verbatim: *"Most-protective is a display and framing rule — it never becomes diagnosis, inference, or a new recorded claim (Law 8 and W0 Law 6 both bind)"*). It **may**: make uncertainty prominent; state that relied-on context is missing, old, expired, or contradicted; state the room's lawful limitation; direct the user toward an already-governed review or confirmation route; avoid presenting uncertain material as established fact. It **must never manufacture**: a new claim; a diagnosis or health conclusion; an inference; a restriction; a recommendation; a warning not supported by accepted authority; a new status; a substituted value; a new consent state; a new authority state. **"Most protective" does not mean "invent the safest-sounding conclusion."** The source's own register examples, quoted as source quotations: Kitchen — *"allergy status is unknown for this profile — this plan doesn't account for allergies; verify before relying on it"*; Gym — *"the injury note this would rely on has expired — treated as unknown, so this plan doesn't assume it's resolved."*

## Hard-block-versus-warn open question

**This record does not resolve W1-D3 §10.6.** The question, verbatim from its accepted source: *"**Block vs warn.** Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor)."* The paired floor clause (W1-D3 §6.4, verbatim): *"Whether staleness ever hard-blocks room functionality (rather than warns and degrades) is left open (§10.6) — but the floor is fixed here: **no room may present stale or unknown health context as stable truth, ever.**"*

The question was sealed open by an accepted W1 record; resolving it requires its own decision record with a constitutional check. Every relevant table row therefore carries the floor and marks its block/warn cell **Open (§10.6)**; no state is assigned to blocking behaviour, and no preferred answer is recommended. **Relevant precedent, consulted but not controlling:** ADR 0002 (safety surfacing) rejected hard blocking within its own Law-12 surfacing scope ("overrides user authority, converts governance into gatekeeping"); its reasoning must be consulted by any future record resolving §10.6, but it does not resolve §10.6 — a rejected alternative inside one record's scope is not a resolution of another record's named open question. The acknowledgement rule of decision 10 is likewise explicitly **not** an answer to this question.

## Room wording and semantic fidelity

Room-register wording keeps honesty legible — but **a room-specific tone may not soften or obscure the shared truth state.** Friendly, concise, calm, or room-themed wording must not: omit "unknown"; disguise staleness; hide expiry; collapse contradiction; remove authority labels; remove age information; turn uncertainty into reassurance; or turn caution into an unsupported warning. **The shared semantic content remains controlling.** Rooms instantiate wording, not rules; wording routes to the governed string catalogue (below). **The Meditation Room's instantiation is structurally different and says so:** it relies on no health context (M1–M2 its complete edge list); the table applies only to its own records' freshness.

## W6 governed-string dependency

Final room-register strings and catalogue IDs belong to **W6** (the governed string catalogue). **W4 decides the semantic wording requirements now** — what every instantiation must say (state, reason, uncertainty in-output) and must never do. **Until the governed string catalogue exists, this record is review of record** for its wording, on the established ADR 0009 / 0011 / 0012 precedent. This dependency does not block doctrine acceptance, and this record creates **no** catalogue files, IDs, routing, or interface infrastructure.

## Alternatives considered

- **One shared table + room-register wording (chosen).** Uniform semantics, legible honesty. Chosen because the truth states are the same in every room; only the voice differs.
- **Per-room behaviour design (rejected).** Four hand-rolled answers diverge — the same staleness would mean different things in different rooms, and the walls would drift.
- **Generic wording everywhere (rejected).** Boilerplate gets ignored; room-register wording keeps honesty legible without altering the rule.
- **Resolving block-vs-warn here (rejected).** The question is sealed open in W1-D3 §10.6; answering it inside a transmission standard would resolve a source question by the back door. It waits for its own record.

## Consequences

- **Easier:** every contract's Unknown/stale/contradicted section has one table to quote; a reviewer compares the quotation against the cited source and passes or fails on an exact match.
- **Easier (honesty):** uncertainty lives in the output itself, so the artifact stays honest after the surfacing moment passes — downstream copies carry their own caveats.
- **Harder (deliberately):** a room cannot soften a truth state with tone, cure uncertainty by widening scope, fill a gap by inference, adjudicate a contradiction, or reset a clock without a user review act.
- **Constrains future work:** block-vs-warn resolution requires its own record consulting ADR 0002's reasoning; intervals and thresholds await §10.1's own decision; final strings await W6.
- **Preserved honesty:** the §6.4 floor stands in every row — no room may present stale or unknown health context as stable truth, ever.

## Non-goals

This record does not decide: hard-block versus warn (§10.6 stays open); new authority labels; new staleness classes; new time thresholds; new grace percentages; new expiry periods; new precedence algorithms; new review transitions; new consent rules; room-specific contract wording; catalogue IDs; adapter behaviour; prompts; payload schemas; session mechanics; UI or review surfaces; validators; or any W5 or W6 implementation. It builds no behaviour-table implementation, catalogue, fixture, adapter, session, prompt, payload, validator, surface, or engine code, and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples beyond the source's own quoted register sentences.

## Public-safety considerations

Role-generic and structural wording throughout — user, room, contract, profile context, authority label, section age, human reviewer, architect, model. No private names, no model names, no private or project lineage, no realistic condition pairs, no diagnosis or treatment examples, no medical recommendations. The category words appearing here (allergy, medication, condition, injury) are **W1-D3 §6.3's own safety-relevant set, quoted verbatim as structural source language**, and the Kitchen/Gym register sentences are the source's own examples, clearly identified as quotations — not new wording and not clinical examples about any person. No companion framing except where a sentence names a prohibition. No positive implementation claims — this record is table-driven and builds nothing.

## Dependencies

W0 (Laws 6, 7, 8, 11); W1-D1 (edges); W1-D2 (grants; grants decay too); W1-D3 (the controlling source — states, labels, floors, contradiction handling, §10.6); ADR 0003 (ceremony); ADR 0016 (the contract slot); ADR 0018 (the fidelity mechanism); ADR 0019 (uncertainty is never an inference licence); and the W4 runway (W4-AR). ADR 0002 is discussed as relevant precedent for the §10.6 question but is not a governing reliance of this record. All named dependencies are landed and resolvable. This record does **not** depend on W5 or W6.

## Open questions

**One inherited question, carried forward by name — deliberately not resolved by this record:**

1. **Block vs warn (W1-D3 §10.6, verbatim):** *"Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor)."* Sealed open by the accepted W1-D3; resolvable only by its own future decision record with a constitutional check, consulting ADR 0002's reasoning; the shared table carries the §6.4 floor in every row without assigning any state to blocking behaviour.

The grace-fraction question is closed ("always," for the safety-relevant set) and does not appear here.

---

*A room that doesn't know must say so — plainly, in the output itself, where the honesty survives the moment. The table is one because the truth states are one: what differs by room is only the voice, never the ground.*
