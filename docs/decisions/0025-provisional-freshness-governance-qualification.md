# 0025 — Provisional Freshness-Governance Qualification (Clinical-Adjacent Input Unavailable)

**Status:** Accepted by human reviewer, 2026-08-13. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** none — this record qualifies deliverable content rather than constituting it
**Decision mode:** governance qualification. It decides **how** a later record may lawfully set numbers whose requested input could not be obtained; it sets no number itself.
**Constitutional references:** W0 Laws 3, 6, 7, 11; W0 §2 non-goal 7 (no certified-compliance claim). No law is amended.
**Qualifies:** DR-W5-02 (Runtime Freshness and Unknown/Stale Behaviour), which owns W1-D3 §10.1 and §10.6.

---

**W1-D3 asked for clinical-adjacent input before anyone set a freshness number. That input could not be obtained. This record does not pretend it was, does not substitute something else for it, and does not let the absence quietly become permission. It states what was actually collected, what each thing is worth, and the conditions under which numbers may be set anyway — provisionally, labelled, and reviewable if the input ever arrives.**

## Decision question

W1-D3 §10.1 states that default review intervals *"deserve a short, focused decision record with clinical-adjacent input."* **That input is not available.** Three non-clinical inputs were collected, and one clinical-adjacent consultation packet was prepared but remained unanswered; **none satisfies the requested input.**

**May DR-W5-02 set freshness thresholds without the requested input — and if so, under what binding conditions, and carrying what honest label?**

## Context

The freshness ladder cannot function without numbers. `staleness_of` in the published engine refuses to produce any label at all — including `current` — unless all three thresholds are supplied, by deliberate design: interval numbers are clinical judgment that no code may pre-empt. **Without a decision, W5 cannot proceed to any runtime that surfaces freshness, and W1-D3 §10.6 cannot be meaningfully answered, because the state it asks about is unreachable.**

Four process elements are recorded, in sequence, each at its true weight:

1. **A disposable out-of-repository literature evidence spike.** It found partial external support for a review cadence in specific contexts; **no external support for a grace period; no external support for a hard limit of any kind, for any data type; and no external evidence for any threshold axis.** It also found that the sources answer *when a person should be seen*, not *when a record should stop being relied upon* — a different question. **The spike was performed by a language model. It is a survey, it is disposable, and it does not satisfy W1-D3 §10.1.**
2. **A clinical-adjacent consultation packet, prepared and unanswered.** A packet, response-capture table and provenance note were drafted for a clinically-qualified reviewer. **No qualified human clinical reviewer was available to answer them.** The packet remains available for use if one becomes available.
3. **An independent AI-reviewer challenge.** A challenge was collected from an independent AI reviewer and is held as process evidence outside the repository. **It is not clinical evidence, it is not clinical-adjacent input, and no part of it is treated as either.** Machine review of machine reasoning does not become domain expertise by being independent.
4. **A human project-authority governance review.** The human project authority reviewed the direction and approved it **explicitly as a governance decision** — *"not clinical validation; does not satisfy or impersonate clinical-adjacent review; does not convert model research or AI-reviewer input into clinical evidence."*

**Waiting indefinitely adds no authority.** It does not produce the missing input; it only stops the phase while the gap stays exactly as wide. **Proceeding without saying so would be worse.** This record is the third option: proceed, and carry the gap in ink.

## Controlling law

- **W1-D3 §10.1** — the request for clinical-adjacent input, unsatisfied.
- **W1-D3 §2** — the six freshness labels; decay downward-only and label-only; *"Renewal is a review act, not a refresh."*
- **W1-D3 §5.5, §8.7** — absence is never a negative claim; *"No record found in the reviewed documents"* must never become *"not present."*
- **W1-D3 §6.3** — the closed safety-relevant set, and most-protective framing as a display-and-framing rule that *"never becomes diagnosis, inference, or a new recorded claim."*
- **W1-D3 §6.4** — the floor: *"no room may present stale or unknown health context as stable truth, ever."*
- **W1-D3 §7** — re-review triggers: interval lapse, new Vault upload touching the section, contradiction flag, supersession proposal, user request.
- **ADR 0002** — the settled surfacing doctrine, and decisively for safeguard 14: *"Nothing in this doctrine blocks the user from doing anything within the Wing's scope. What can be 'blocked' is exactly one thing: **the Wing presenting unsound data as settled truth.**"* Its rejection of hard blocking is scoped to *"refuse to operate … until reviewed"* — a user-facing refusal, which safeguard 14 is not.
- **ADR 0020** — the shared behaviour table; the always-shown inline uncertainty for the safety-relevant set; §10.6 left open and not answered.
- **ADR 0024** — the processing boundary: grant-derived context, no read path of its own, no hidden fetch, no background authority.
- **W1-D2 §3.4** — nothing in the grant grammar may authorise proactive or background activity.
- **ADR 0007, ADR 0013, ADR 0009** — the precedent for evidence-based provisional decisions: ADR 0013's KDF profile entered as *"the v1 **review-dated provisional**"* on disposable-spike evidence; ADR 0009's accepted format list entered *"provisional at this landing."* **Provisional-and-labelled is an established corpus move, not an invention.**

## Decision

### The qualification

1. **The requested input is recorded as unavailable, not as satisfied.** W1-D3 §10.1's request for clinical-adjacent input stands **open**. Nothing collected — spike, AI-reviewer challenge, or human governance approval — is recorded as discharging it, and no later record may cite any of them as having done so.

2. **Each input is recorded at its true weight, and the weights do not compound.** A literature survey by a model is a survey. An independent AI reviewer is a second model. A human project-authority approval is a governance decision by the person whose archive this is. **Three non-clinical inputs do not sum to a clinical one**, and this record exists partly to make that arithmetic impossible to perform later by accident.

3. **DR-W5-02 may set numeric thresholds, provisionally, under the ten safeguards below.** They enter as **provisional governance defaults** — the ADR 0013 review-dated-provisional pattern — and never as clinical guidance.

4. **Every provisional threshold carries its label wherever the threshold value is reproduced or summarised.** In DR-W5-02, and in any later governed artefact that quotes or summarises a threshold value, that value must be accompanied by **`provisional governance default — not clinically validated`**. The registry entry need not duplicate threshold values or invent a new field; it carries the accepted record's normal governed metadata and content hash. **A threshold value reproduced without its provisional label is a defect.**

5. **Provisional status does not expire into permanence.** It ends only by a governed act: either qualified clinical-adjacent input is obtained and a successor record supersedes the defaults, or a later record re-affirms them explicitly, on the record, with reasons. **Silence never converts provisional into settled.**

6. **The re-review trigger is named:** the availability of qualified clinical-adjacent input, or any credible indication that a provisional threshold is producing unsafe or misleading reliance. **Either obliges a return to this decision.** The consultation packet is retained and remains usable unchanged.

7. **No claim of validation, certification, endorsement or clinical support may be made anywhere, for any threshold, on the strength of this record.** W0 §2 non-goal 7 binds; nothing here is evidence of safety.

### The ten binding safeguards

Approved by the human project authority as conditions on DR-W5-02, and binding on it.

8. **Event-triggered review is primary; calendar review is secondary and a backstop.** This follows the evidence rather than the convenience: for at least one data type the external guidance is explicitly event-based, and for another no validated calendar interval exists at all. **Triggers are W1-D3 §7's, and they fire only inside a user-initiated interaction** — W1-D2 §3.4 forbids background authority and ADR 0024 gives the boundary no read path of its own, so a trigger may never become a background process that reaches out to look.

9. **Numeric thresholds are governance defaults, not clinical guidance** (decisions 3–4).

10. **`expired → unknown` preserves the last-known assertion, its provenance and its age.** *"Treated as unknown"* is a statement about **reliance**, not about **retention**: the item, what it said, where it came from and how old it is all persist and remain visible. What changes is that the Wing may no longer lean on it. **This is a clarification of what W1-D3 §2 already implies, read together with T8's "nothing authoritative is ever silently deleted" — it mints no label, no state and no new authority.**

11. **Unknown never collapses into absence, resolution or reassurance.** W1-D3 §5.5 and §8.7 restated at runtime level, unweakened. **An expired assertion becomes uncertain, never negative.**

12. **Freshness thresholds are governed by data type**, per the accepted axis ruling. No confidentiality- or sensitivity-derived class becomes a threshold axis.

13. **Runtime consequence may additionally consider assertion posture** — whether the item is a *positive safety constraint*, an *ordinary positive fact*, or an *explicit absence assertion*. This is grounded in W1-D3 §5.5, which already requires consumers to receive *"either a confirmed negative … or unknown — and must behave according to which."* **Posture is derived at evaluation and never stored**, on the Lane C precedent where the assurance vocabulary is derived at presentation and never stored. **It mints no label, no class and no authority state.** Its sharpest case is the expired explicit absence assertion, which is the single most dangerous item in the system and must degrade to *unknown*, never persist as a negative.

14. **Fail-closed on required assumption.** **If safe completion of a function would require assuming that an uncertain safety-relevant fact is absent or resolved, the affected function fails closed.**
    **What fails closed is the Wing's output, not the user.** The Wing declines to produce a result that would depend on an assumption it is not entitled to make. It does not prevent the person from doing anything within the Wing's scope, does not gate their access to their own records, and does not require review before they may act. **This is precisely the one thing ADR 0002 permits to be blocked — *"the Wing presenting unsound data as settled truth"* — and is distinct from the *"refuse to operate … until reviewed"* pattern ADR 0002 rejected.**
    **This safeguard is a partial disposition of W1-D3 §10.6.** It decides one case — that where safe completion would require assuming an uncertain safety-relevant fact is absent or resolved, the Wing's output fails closed — and leaves every other part of the block-versus-warn question to DR-W5-02. **The disposition is made under this record's own constitutional check and with ADR 0002's reasoning consulted in full, which is what ADR 0020 requires of any record resolving any part of §10.6.** DR-W5-02 owns the remainder and must consult ADR 0002 again when it answers it.

15. **Renewal must represent meaningful review, not a timestamp reset.** W1-D3 §2 and §8.2 restated: no agent, and no user action that is merely an acknowledgement, may re-date an item. **A mechanism whose effect is to clear a flag without a review having occurred is prohibited**, however it is labelled.

16. **Alert-fatigue risk is carried, not solved.** More conservative behaviour produces more prompting, and prompting that becomes ritual defeats the purpose (W0 failure mode 3; W1-D2 §8.7; D5-T20). **This is a surface-era design constraint, named here and owned there.** No W5 record may treat it as solved, and none may quietly reduce conservatism to avoid it.

17. **A safeguard may not be relaxed by a later W5 record.** Any change returns as its own accepted record on the ADR 0017 decision-11 pattern, stating the affected scope, the evidence-backed reason, the bounded exception, its review or sunset condition, the compensating controls, and explicit human-reviewer acceptance. **No silent relaxation.**

## Constitutional check

- **Law 3 holds.** Nothing here promotes anything. Provisional thresholds lower confidence over time; they never raise it.
- **Law 6 holds.** No threshold, and no fail-closed behaviour, asserts anything clinical. Fail-closed is a refusal to assert, which is the opposite of an opinion.
- **Law 7 is served.** *Approved is not current* becomes operable, which it cannot be while the ladder has no numbers.
- **Law 11 holds, and safeguard 14 is where it was at risk.** The user is never gated from their own data or their own decisions; only the Wing's assertion is withheld. Had safeguard 14 blocked the person rather than the output, it would have breached Law 11 and contradicted ADR 0002.
- **No new authority.** No label, class, authority state, freshness state, edge, or grant type is minted. Assertion posture is derived, never stored (decision 13).
- **W0 §2 non-goal 7 holds** — no certified-compliance or validation claim is made anywhere.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Alternatives considered

- **Proceed provisionally, labelled, with binding safeguards and a named re-review trigger (chosen).** Keeps the phase moving and keeps the gap visible. The corpus has done this before, with ADR 0013 and ADR 0009.
- **Wait for clinical-adjacent input (rejected, with regret).** It is the ideal, and it is unavailable. Waiting adds no authority, produces no input, and blocks W5 indefinitely while the gap remains identical. **Rejected as a decision, not as an aspiration** — decision 6 keeps the door open.
- **Set thresholds without qualification (rejected).** It would let a model's literature survey and a second model's review harden into apparent clinical support. **The exact failure this record exists to prevent.**
- **Abandon numeric thresholds; rely on event triggers alone (rejected, narrowly).** Attractive, and closest to the evidence — but `staleness_of` requires three thresholds to produce any label, `expired` would stay unreachable, and §10.6 would stay undischargeable. **Event-triggering becomes primary instead (safeguard 8), which captures most of the benefit lawfully.**
- **Treat the human governance approval as sufficient (rejected).** It is sufficient as *governance*, which is what it claims to be, and insufficient as *clinical input*, which it explicitly disclaims. Decision 2 records exactly that.

## Consequences

- **DR-W5-02 becomes writable** — under ten binding constraints and a permanent label.
- **The corpus carries a visible, dated admission that a requested input was not obtained.** That is the point, not a side effect.
- **Harder, deliberately:** every downstream artefact citing a threshold must carry the provisional label; safeguard 17 blocks quiet relaxation; and safeguard 14 partially disposes of §10.6 before DR-W5-02 opens it, leaving that record a narrower question than the one W1-D3 sealed.
- **The consultation packet retains value.** If a qualified reviewer becomes available, decision 6 already names the route back.
- **No behavioural or capability consequence.** Nothing is built, no model is contacted, no fixture executes.

## Non-goals

This record does not: set any threshold value; answer W1-D3 §10.1; answer W1-D3 §10.6 **beyond the partial disposition made in safeguard 14**; decide the freshness axis, which is already ruled; design the fail-closed mechanism, its surfacing, or any wording; decide rendering, labels, catalogue IDs or copy of any kind; claim clinical validation, certification, endorsement or safety; convert any collected input into clinical evidence; authorise implementation, a directory, a dependency, model contact, payload construction, transmission, harness work or fixture execution; touch the pending ledger, Lane C, or any W6 matter; or amend W1-D3, ADR 0002, ADR 0020, ADR 0024 or any room contract. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic wording throughout — user, Wing, room, record, item, data type, review, threshold, human project authority, clinical-adjacent reviewer, AI reviewer, model. **No named drugs, diagnoses, allergens or clinical examples appear**, and none may be added: the underlying evidence material contains them and is disposable and out-of-repository for that reason. **No model or vendor name appears**, including for the independent AI reviewer, whose identity is held as out-of-repository process evidence only. No URLs. No private names, and no project lineage beyond this repository.

## Dependencies

W0 (Laws 3, 6, 7, 11; §2 non-goal 7); W1-D3 (§2, §5.5, §6.3, §6.4, §7, §8.2, §8.7, §10.1); W1-D2 (§3.4); ADR 0002 (the surfacing doctrine and its scoped rejection of hard blocking); ADR 0003 (ceremony); ADR 0007 (development-artifact policy, under which the spike was disposable); ADR 0009 and ADR 0013 (the provisional-decision precedent); ADR 0020 (the shared behaviour table); ADR 0024 (the processing boundary); and the W5 runway.

## Open questions

1. **Whether qualified clinical-adjacent input will become available**, and through what route. **Owner: the human project authority.** Decision 6 names the trigger; it does not schedule it.
2. **Whether the five governance data types remain the right grouping.** The clinical-adjacent consultation packet tested the four clinically relevant types and deliberately excluded preference; it remained unanswered. **Owner: DR-W5-02**, which may adopt the five-type grouping provisionally under the same qualification, or split it through an explicit governed decision.
3. **Whether a provisional threshold should carry an explicit review date**, as ADR 0013's KDF profile did, or only the named trigger of decision 6. **Owner: DR-W5-02.**

---

*A record that says "we asked for something and could not get it" is worth more than a record that quietly proceeds as though it had. The numbers this qualifies are honest only for as long as the label survives — which is why the label, and not the numbers, is the thing this record actually protects.*
