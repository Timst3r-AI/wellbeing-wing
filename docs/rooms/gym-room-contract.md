# W4-D4 — Gym Room Contract

**Status:** Accepted by human reviewer, 2026-08-09. Not a build instruction. Authorises no implementation or transmission.
**Date:** 2026-08-07 · **Phase:** W4 · **Deliverable:** W4-D4 · **Room:** Gym
**Authorises no implementation, transmission, or device integration.** W5 (adapter/isolation enforcement) and W6 (governed string catalogue) dependencies remain **deferred and unread**. This contract is a governed document: it declares what the Gym Room may and may not do, in the exact accepted words of its sources; it mints no authority, builds nothing, ingests nothing, and transmits nothing.

---

## 1. Identity and purpose

The Gym Room is an honest room for **organising the user's own movement, rest, and recovery records** — a governed surface for the workout and movement plans, movement logs, rest and recovery records, and user-reported non-clinical sleep observations the user maintains themselves. It is **manual-first and fully useful without any device.** It is **not** a coach, a personal trainer, a physiotherapist, a rehabilitation service, a treatment service, a clinical monitor, a diagnostic system, a wearable or device authority, an autonomous exercise optimiser, or a companion; it is **not** authorised to reach medical, therapeutic, or diagnostic conclusions, and it is **not** authorised to promise any capability this contract does not establish. Its usefulness is its restraint: it holds a person's own movement and rest in their own words and helps them plan — it never turns a hard week into a diagnosis or a device's guess into a truth. It may hold **sleep only as an instance of rest and recovery**; it is not clinical sleep monitoring, sleep diagnosis, automated tracking, device ingestion, or health interpretation. Its exact read, write, outward, and processing authority is fixed in sections 2, 3, and 6, not in this paragraph.

## 2. Read scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation.

**Reference:** W1-D1 §5 · E7.

**Verbatim quotation (W1-D1 §5 · E7):**

> - **E7. Approved Profile (confirmed injury/physical notes only) → Gym.** Same conditions as E6.

*Declaration.* Gym reads exactly one inbound edge: **E7**, a **standing scoped read** of the **Approved Profile**, limited to **confirmed injury/physical notes only**, under standing consent with the authority label and **section age surfaced on every use** (E7's "same conditions as E6"). The words **confirmed**, **injury/physical notes**, and **only** are load-bearing and are not widened. Gym reads **no other Profile material** — no Health Vault; no Wellness records generally; no conditions generally; no medications; no allergies; no Kitchen or food records; no reproductive or cycle records; no Meditation records; nothing beyond E7. Gym has **no cycle ownership, no cycle read, and no cycle-context edge**.

## 3. Write and outward scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation for every source unit.

**Reference:** W1-D1 §3 (home), §4 (categories #12–#13); W1-D3 §2 (User-reported), D3-T3.

**Verbatim quotations:**

> | **Gym records** | C1 + C2 | Z1 / Z2 ciphertext | Plans (C1); movement/rest logs (C2) |
>
> | 12 | Workout plans | C1 | Gym | |
> | 13 | Movement / rest / recovery logs | C2 | Gym | |
>
> - **T3. User entry → user-reported.** Automatic on entry into room records; carries no profile authority.
>
> | **User-reported** | Entered by the user (logs, notes) but not reviewed into approved status | System, on user entry | Room-scoped use only; never profile truth |

*Write declaration.* Gym is the mixed-class room: it writes its **own records only** — **Workout plans (#12, C1)** and **Movement / rest / recovery logs (#13, C2)**. User-entered records receive the **User-reported** label on entry (D3-T3): **room-scoped use only, never profile truth**, carrying **no approved-profile authority**. This contract mints no new authority state.

*User-reported sleep.* User-entered, **non-clinical sleep observations are accepted instances of category #13 rest/recovery** — an interpretation of the existing *rest / recovery* words, **not** a new category, class, edge, or clinical-sleep authority. Accepted fields: **sleep duration; sleep timing; perceived sleep quality; awakenings the user remembers or deliberately enters; rest/recovery observations and notes.** Each remains **C2, category #13, User-reported on entry, room-scoped, and never profile truth.**

*Manual device-display notes.* A user may manually write a note about what a device displayed. That record is **User-reported because the user entered it**; it gains **no device authority**, is **not device ingestion**, and is **not device verification.** Device-originated data is never relabelled User-reported merely because device provenance is absent.

*Device exclusion (current).* Gym admits **no device-originated data.** There is: no device-originated ingestion; no synchronisation; no device-file import; no background device collection; no device adapter; no device provenance label; no automatic sleep-data import; no device-imported sleep duration or timing; no device-detected awakenings; no sleep-stage data; no readiness, recovery, or sleep scores; no cross-device comparison; and no device-originated processing under E11-G. **`Unknown freshness` is a state, not intake authority.** These exclusions hold unless separately authorised future doctrine changes the source law.

*Outward.* **Gym has no outward edge** — no vendor, commerce, upload, coach, trainer, clinician, platform, or device-disclosure edge of any kind. A future inbound device path, if ever created, would confer no outward-disclosure authority.

## 4. Inference prohibitions

The general rule (W0 Law 8; ADR-0019): the Gym Room must not derive, record, act on, or change its behaviour on the basis of a health-relevant, mental-health, or room-jurisdiction conclusion outside its granted context — not from workout or movement plans, movement logs, rest or recovery records, user-reported sleep, or the E7 confirmed-injury context it lawfully reads. **Lawful reliance is distinct from inference:** Gym may rely on an established E7 confirmed injury/physical note within E7's exact accepted scope when organising a plan; lawful reliance on that accepted record is not itself a newly derived conclusion. Such reliance does not widen E7, and an accepted E7 item cannot become evidence for another unsupported health conclusion. A user request cannot create an absent edge or authorise a forbidden inference. Observable consequence makes a breach testable; it is never permission to infer silently, and silent behaviour change is the primary target.

**The named-bait list below is a floor, not a ceiling.** It is subordinate to W0 Law 8 and ADR-0019, which bind beyond every enumeration; it is not a risk ontology and not an inference engine. The labels `GYM-B1`…`GYM-B6` are **contract-local review labels only** — not registry IDs, global namespaces, fixture IDs, or catalogue IDs. Two device-contingent reasoning risks (a derived device score treated as health truth; a device sleep or recovery estimate treated as recovery certainty) are **deferred to future device-data doctrine** and are **not** baits here, because no device data is currently writable Gym data. Compulsive-exercise mechanics and rehabilitation/treatment framing are carried by sections 7 and 8, not as baits.

### GYM-B1 — Training-pattern-to-mental-health-state inference
- **Forbidden system move:** using an aggregate pattern across movement, exercise, rest, or recovery records to manufacture an unsupported mental-health state or mental-health conclusion about the user.
- **Lawful response boundary:** preserve the records as organisational Gym data; state only what was recorded; refuse the mental-health conclusion; route a genuine concern through the governed process.
- **Doctrine anchor:** W0 §5.3 (infer no health or mental-health states from training patterns); W0 Law 8; ADR-0019.
- **Note:** kept generic — no particular mental-health state is named, and no particular training pattern is mapped to one.
- **Classification:** review-only for aptness and association-teaching; fixture and runtime deferred to evaluation.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### GYM-B2 — Reduced-activity-to-deterioration inference
- **Forbidden system move:** using reduced, interrupted, or absent activity to manufacture deterioration in the user's physical health, capacity, or condition.
- **Lawful response boundary:** keep reduced or absent activity a neutral record fact; never infer deterioration; absence or reduction is not decline; surface only what is recorded.
- **Doctrine anchor:** W0 Law 8; W0 §5.3; ADR-0019.
- **Note:** fences a physical-health/capacity/condition deterioration conclusion only; it does not infer a mental-health state, motivation, intent, character, or willingness.
- **Classification:** review-only for aptness; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### GYM-B3 — High-activity-to-all-clear inference
- **Forbidden system move:** using frequent, sustained, or increased activity to manufacture wellness, safety, recovery, uninjured status, or health as an all-clear conclusion.
- **Lawful response boundary:** keep high activity a neutral record fact; never infer wellness, safety, or recovery; high activity is not health truth; surface only what is recorded.
- **Doctrine anchor:** W0 Law 8; W0 §5.3; ADR-0019.
- **Note:** the reassuring-conclusion counterpart of GYM-B2's adverse conclusion; an all-clear minted from activity can mask injury or illness.
- **Classification:** review-only for aptness; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### GYM-B4 — User-reported-record-to-injury-authority elevation
- **Forbidden system move:** using a User-reported body-feeling, movement, or recovery record to manufacture an injury diagnosis, condition, or clinical explanation.
- **Lawful response boundary:** keep the note a User-reported C2 record (room-scoped, never profile truth); refuse the injury/clinical conclusion; surface the note as the user's own words; route a real concern to the governed process.
- **Doctrine anchor:** W0 Law 6; W0 Law 8; W0 §5.3; ADR-0019; category #13 C2 limits; the User-reported authority limit.
- **Note:** the input is a single User-reported record and the harm is authority elevation of that record — the record remains User-reported and never profile truth.
- **Classification:** review-only for ordinary-record medicalisation risk; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### GYM-B5 — Injury-absence-to-all-clear inference
- **Forbidden system move:** converting the absence of a confirmed injury note into a confirmed negative injury finding, a healed status, a clearance, or permission to proceed as though safety had been established.
- **Lawful response boundary:** preserve the distinction between unknown and confirmed negative; an expired injury note may still apply and is not healed; absence is never all-clear; surface the uncertainty; never manufacture a negative from silence; route a genuine status question through the governed process.
- **Doctrine anchor:** W1-D3 §5.5 (absence-vs-negative); §6.3 (the Gym worked example — expired injury may still apply, not healed); W0 Law 8; ADR-0019; ADR-0020 (unknown handling).
- **Note:** **highest priority. Complementary to section 5, not duplicative** — section 5 displays the unknown/stale/expired/contradicted injury context honestly; this bait forbids overwriting it with an invented negative or all-clear.
- **Classification:** review-only for aptness; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### GYM-B6 — Sleep-observation-to-health-cause inference
- **Forbidden system move:** using a User-reported sleep observation to manufacture a sleep disorder, a medical cause, a hormonal explanation, a psychiatric explanation, or another unsupported health conclusion.
- **Lawful response boundary:** keep the sleep observation a non-clinical C2 #13 rest/recovery record; refuse any disorder, cause, or clinical explanation; surface only what the user recorded; route a real concern to the governed process.
- **Doctrine anchor:** W0 Law 8; W0 Law 6; W0 §5.3; ADR-0019; category #13 C2 limits; the User-reported authority limit; the accepted non-clinical-sleep basis.
- **Note:** kept entirely generic — no realistic sleep-to-diagnosis association, threshold, likelihood, or cause is stated. Device sleep estimates are excluded and out of scope.
- **Classification:** review-only for aptness and clinical-line risk; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

## 5. Unknown/stale/contradicted behaviour

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation of the shared behaviour standard.

**Reference:** ADR-0020 (Unknown/Stale/Contradicted Behaviour Standard), § Shared behaviour table.

**Verbatim quotation (ADR-0020, § Shared behaviour table):**

> The foundation is the **verbatim W1-D3 §2 label semantics** — all six states:
>
> | State (W1-D3 §2) | Meaning (verbatim) | Working use (verbatim) |
> |---|---|---|
> | **Current** | "Within its review interval" | "Normal use, age surfaced" |
> | **Review due** | "Interval passed; renewal surfaces at next relevant use" | "Usable, with a visible review-due flag" |
> | **Stale** | "Past the renewal grace period" | "Usable only with explicit uncertainty surfacing in any output that relies on it" |
> | **Expired** | "Past the hard limit for its type" | "Not usable as truth. Treated as **unknown** until re-reviewed" |
> | **Superseded** | "Replaced; permanent terminal state" | "History only" |
> | **Unknown freshness** | "No reliable review date (e.g., imported material)" | "Treated as stale until reviewed" |
>
> The behaviour rows, anchored on W1-D3 §6; cells a source does not specify are marked, never filled by interpretation:
>
> | # | Context state | Surfaced | May continue | Must not occur | Authority/age display | Uncertainty sentence | Review route | Hard-block/warn |
> |---|---|---|---|---|---|---|---|---|
> | 1 | **Current** | Age (the honesty floor) | Normal use | Presenting without age (§6.1) | Label and age on every use (§6.1) | Not required | Renewal at next relevant use (§7) | Not applicable |
> | 2 | **Review due** (non-safety) | Visible review-due flag (§2) | Use, flagged | Hiding the flag | Label and age carried | Not required by §2; flag required | Renewal surfaces at next relevant use (§2, §7) | **Open (§10.6)** — floor only |
> | 3 | **Review due / stale + safety-relevant + relied-on** | Inline sentence; output carries explicit uncertainty (**always** — not grace-conditioned) | Use, with uncertainty in the output itself | Output without the inline sentence | Label and age carried | **Always** | Re-review trigger (§7) | **Open (§10.6)** — floor only |
> | 4 | **Stale** (non-safety) | Uncertainty named in the output itself (§2) | Use, with uncertainty in-output | Output that omits the uncertainty | Label and age carried | Required (§2) | Re-review trigger (§7) | **Open (§10.6)** — floor only |
> | 5 | **Expired / contradicted / unknown + safety-relevant** | Treated as **unknown**; the state and the reason acknowledged inline before continuing (decision 10); most-protective framing with the reason stated (§6.2–6.3) | Only in the most protective reasonable way, saying why (§6.3) | Treating as truth (§6.2); converting silence into a negative claim (§5.5); manufacturing any claim, restriction, or recommendation (§6.3) | Both labels honoured on every read (§6); contradiction: staleness of the older item surfaced alongside (§5.4) | Required — the reason stated | Re-review / user review; contradiction queues per §5 (both versions visible; prepared question where clinically material) | **Open (§10.6)** — floor: never present as stable truth |
> | 6 | **Expired / contradicted / unknown** (non-safety) | Treated as unknown; uncertainty named in the output | Use with uncertainty named | Treating as truth | Labels honoured; status surfaced | Required | Re-review route | **Open (§10.6)** — floor only |
>
> **Coverage note (not a contradiction):** the planning record's behaviour rows do not restate the **Superseded** and **Unknown freshness** labels; the shared table inherits them from §2 unchanged — superseded items are history only, and unknown-freshness items take the stale row's behaviour.
>
> **Source-fidelity note (reported, not harmonised):** the planning record's row 5 used a pause phrase with no W1-D3 anchor; per accepted ruling it is replaced by the source-anchored acknowledgement wording of decision 10, which is explicitly a surfacing-order requirement and not a functional block. Neither source is amended.

**Gym room-register wording (review of record — proposed, not final).** These are the Gym voice for the states quoted above; each is bracketed with generic placeholders (never real health content) and instantiates the shared rule without altering it. Gym's **live safety-relevant read is injury** (E7 confirmed injury/physical notes); the Gym safety framing is **retrospective** — an **expired injury note may still apply and is not healed**, **absence is not all-clear**, contradiction is held rather than silently resolved, newer is not automatically truer, and both accounts remain visible where required. Applying the most-protective posture mints no new injury fact. **Coverage ledger** — every inherited W1-D3 state and contradicted context is visibly mapped to a proposed string:

| W1-D3 state / context | Source semantics (verbatim quotation above) | Proposed string |
|---|---|---|
| **Current** | "Within its review interval" · "Normal use, age surfaced" | RR-Current |
| **Review due** (non-safety) | "Interval passed…" · "Usable, with a visible review-due flag" | RR-ReviewDue-NonSafety |
| **Review due** (injury-safety, relied-on) | row 3 — review interval passed; inline uncertainty **Always** | RR-ReviewDue-Safety |
| **Stale** (non-safety) | "Past the renewal grace period" · "Usable only with explicit uncertainty surfacing…" | RR-Stale-NonSafety |
| **Stale** (injury-safety, relied-on) | row 3 — renewal grace period passed; inline uncertainty **Always** | RR-Stale-Safety |
| **Expired** | "Past the hard limit…" · "Not usable as truth. Treated as **unknown** until re-reviewed" | RR-Expired |
| **Superseded** | "Replaced; permanent terminal state" · "History only" | RR-Superseded |
| **Unknown freshness** | "No reliable review date…" · "Treated as stale until reviewed" | RR-UnknownFreshness |
| **Contradicted** | §5 — both accounts visible; "Newer is not truer until the user says so" | RR-Contradicted |
| **Expired / contradicted / unknown + injury-safety** | row 5 — acknowledged inline before continuing; most-protective | RR-Unknown-Safety |
| **Expired / contradicted / unknown + non-safety** | row 6 — treated as unknown; uncertainty named | RR-Unknown-NonSafety |

- **RR-Current** — *Current, within its review interval; label and age carried.* — *"This plan uses [profile item] — [authority label], last reviewed [age] — and it is Current, within its review interval."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-NonSafety** — *Review due (non-safety); usable with a visible review-due flag; label and age carried.* — *"This plan uses [profile item] — [authority label], last reviewed [age] — whose review is due because its review interval has passed; usable, with this review-due flag shown."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-Safety** — *Review due, injury-safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This plan relies on an injury note — [authority label], last reviewed [age] — whose review is due because its review interval has passed; because it is safety-relevant, this output carries that uncertainty inline: the note may still apply, so please review it when you can."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-NonSafety** — *Stale (non-safety); usable only with uncertainty named in the output; label and age carried.* — *"This plan uses [profile item] — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; this output names that uncertainty wherever it relies on it."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-Safety** — *Stale, injury-safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This plan relies on an injury note — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; because it is safety-relevant, this output carries that uncertainty inline: the note may still apply, so please review it when you can."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Expired** — *Expired; not usable as truth, treated as unknown until re-reviewed; label and status surfaced; routes to the unknown handling.* — *"[profile item] — [authority label], last reviewed [age] — is expired: past its hard limit and not usable as truth, so it is treated as unknown until re-reviewed."* (Its use then follows RR-Unknown-Safety or RR-Unknown-NonSafety according to the source-authorised safety classification.)
  `Review of record pending W6 governed string catalogue.`
- **RR-Superseded** — *Superseded; replaced, a permanent terminal state; history only, not used as current.* — *"[profile item] has been superseded — replaced, a permanent terminal state; the earlier version is kept as history only and is not used as current."*
  `Review of record pending W6 governed string catalogue.`
- **RR-UnknownFreshness** — *Unknown freshness; no reliable review date; treated as stale until reviewed; label visible, uncertainty named.* — *"[profile item] — [authority label] — has no reliable review date; it is treated as stale until reviewed, and any output relying on it names that uncertainty."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Contradicted** — *Contradicted; both accounts shown with their labels and dates; older-item staleness surfaced; neither settled; the room resolves nothing.* — *"Two accounts of [profile item] disagree — [source A: authority label A, date A] and [source B: authority label B, date B]; both are shown with their labels and dates, the older account's staleness is surfaced alongside where applicable, and neither is treated as settled — newer is not truer until you decide through review."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-Safety** — *Expired / contradicted / unknown, injury-safety use; state, reason, label, and age/status carried; acknowledged inline before continuing, most-protective verbal.* — *"The injury note this plan would rely on — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; the state and the reason are acknowledged here before continuing, this output carries that uncertainty, and it does not assume the item — the note may still apply and is not treated as healed; that uncertainty remains visible, and you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-NonSafety** — *Expired / contradicted / unknown, non-safety use; state, reason, label, and status carried; treated as unknown, uncertainty named.* — *"The [profile item] here — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; this output names that uncertainty, does not treat it as settled, and you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`

Each string names its state and its source-grounded reason, visibly carries the authority label and age/status where the shared table requires it, and carries uncertainty inline where required. **Gym-specific rule:** the injury framing is **retrospective** — **expired injury information may still apply and is never treated as healed; absence of an injury record is never an all-clear.** This is a **verbal / surfacing posture only** — no unsupported warning, restriction, recommendation, injury-clearance, or functional block is minted, and no new injury fact is created. W1-D3 §10.6 (block-versus-warn) remains **inherited and open** under the §6.4 floor. None of these strings diagnoses, clears an injury, or gives medical advice.

## 6. Processing boundary

Carried under ADR-0018's paired form for the processing edge, with the ADR-0017 architectural-isolation requirement.

**Reference:** W1-D1 §5 · E11-G; ADR-0017 (Room Isolation Model).

**Verbatim quotation (W1-D1 §5 · E11-G):**

> - **E11-G. Gym → Z3.** AI assistance on C1/C2 Gym records only. Approved Profile sections enter exclusively through E7.

*Declaration.* Gym AI assistance is a **user-initiated processing disclosure event** (Law 1; ADR 0001) on **C1/C2 Gym records only**; its grant is single-task by default, session at maximum (W1-D2). **Approved Profile content enters exclusively through E7**; **user-reported sleep may be processed because it is an authorised C2 #13 Gym record**; **device-originated data does not currently enter** (section 3 exclusion). Under **ADR-0017**: Gym processing occurs in a context that has never contained another room's content; **one grant binds one room; the session derives from the grant**; cross-room content is **unreachable, not merely forbidden**; **operational enforcement belongs to W5** and this contract claims no runtime enforcement exists. **E11-G is inbound processing, not an outward edge**, and this contract claims **no device adapter, connector, runtime filter, or enforcement implementation** — it establishes none, claims none has been implemented or verified, and authorises none.

## 7. Speech rules

Gym applies the safety-surfacing doctrine (ADR-0002) with the clinical line (W0 Law 6) and the Gym purpose and guards (W0 §5.3) in room terms. The room **may**: organise user-requested movement plans; organise the user's own movement, rest, and recovery records; organise user-reported sleep records; describe what a record says; surface governance labels, age, and uncertainty; and remain neutral about the meaning of a user's movement amount. The room **must not**: diagnose; treat; prescribe rehabilitation; frame movement as physiotherapy; provide medical-recovery direction; provide injury clearance; turn sleep into a clinical conclusion; claim health optimisation; infer health or mental-health status from movement patterns; treat a device estimate as health truth; prescribe movement based on cycle context; or adopt companion, therapeutic, or clinical framing. Surfacing reads governance labels only (ADR-0002 Doctrine 1); the only thing ever withheld is the room's own overclaiming, never the user's own action (Doctrine 3).

*Compulsive-exercise guard.* Gym must **never** create streaks, escalating targets, guilt mechanics, leaderboards, adherence pressure, compulsive monitoring, training-load optimisation that reinforces compulsion, or any framing that equates more movement with moral or health success (W0 §5.3; Non-Goal 5). If the user requests such a mechanic, Gym declines that mechanic specifically and remains otherwise available. These remain speech and behavioural guards, not section-4 baits.

## 8. Forbidden list

The Gym anti-map, named for emphasis though default-deny already excludes each item. Gym must not:

- read the Health Vault;
- read Wellness records generally, or perform any cross-room read or cross-room inference;
- widen E7, or read any unconfirmed injury/physical Profile content or any Profile content beyond E7;
- ingest device-originated data; synchronise with a device or platform; import a device file; collect device data in the background;
- invent a device provenance label, or claim a device adapter, connector, or runtime adapter exists;
- hold device sleep data, sleep-stage data, or derived device scores (readiness, recovery, sleep, or similar); compare across devices;
- make any outward disclosure to a vendor, coach, trainer, clinician, platform, social, or commerce recipient;
- reach a clinical conclusion, provide treatment, prescribe rehabilitation or physiotherapy, or make an injury-clearance claim;
- apply compulsive-exercise mechanics;
- own, read, write, or infer cycle/period context, or prescribe movement based on cycle context;
- claim that W5 enforcement, a connector, or a runtime adapter already exists.

Every prohibition here restates existing law; none mints a new authority.

## 9. Validator hooks

Per ADR-0021's decidability line, every governed term is **mechanically checkable** or **review-only**, with runtime/enforcement matters separately **deferred to evaluation**. No term floats in the ambiguous middle. A validator inspects deterministic repository artefacts only; **a validator must never judge fitness, training quality, recovery adequacy, sleep adequacy, injury status, clinical adequacy, or movement appropriateness** — that would be a judging validator (doctrine minting by machinery), which is prohibited.

**Mechanically checkable (document-decidable):**

- eleven-section structure, order, numbering, and non-blank bodies;
- Gym identity present (section 1);
- byte-level verbatim quotation fidelity for E7, the Gym home row, categories #12/#13, W1-D3 T3, the User-reported row, E11-G, and the complete ADR-0020 shared-table quotation;
- C1 + C2 class fidelity for the Gym home and categories;
- preservation of the load-bearing E7 words `confirmed` and `only`;
- the accepted user-reported sleep fields present;
- no device-intake, device-provenance, device-adapter, or device-sleep claim; no outward-edge or connector claim;
- the six `GYM-B` labels present and unique;
- exactly six future-fixture declarations, one per bait; no fixture identifiers; no catalogue identifiers; no placeholder token; no realistic clinical/movement pair;
- ADR-0020 quotation fidelity; all six W1-D3 states present; exactly eleven Gym room-register strings; one W6 review-of-record mark per string;
- the section 11 open-questions body present.

**Review-only (human judgement):**

- identity fitness and that no unearned capability is advertised;
- E7-narrowing quality (confirmed injury/physical notes only);
- bait aptness and association-teaching risk;
- indirect medicalisation of movement;
- compulsive-exercise reinforcement risk; rehabilitation creep;
- sleep clinical-line quality;
- whether any wording implies device authority;
- whether any prohibition accidentally creates authority.

**Evaluation / later enforcement (deferred, not a contract-validator target):** fixture existence and behaviour; runtime inference; model obedience; operational isolation; W5 enforcement; W6 catalogue binding; any future device-intake behaviour.

## 10. Constitutional check

This contract implements existing law and mints nothing new. It **implements** W0 Law 6 (the clinical line), Law 8 (no cross-room, food-, movement-, or pattern-derived inference), and Law 9 (the Meditation wall); it **preserves** manual-first sufficiency and the E7 closed read (confirmed injury/physical notes only). It **creates no new data class, no new edge, no new provenance label, no device authority, no outward transmission, no cycle authority, no runtime-enforcement claim, no fixture, and no implementation permission.** Every scope clause is carried in ADR-0018 paired form from W1-D1 and W1-D3; the shared behaviour standard is carried verbatim from ADR-0020; the wording strings route to the future W6 governed string catalogue as review-of-record. Gym states only its own present boundary on cycle context (no ownership, read, write, edge, inference, or prescriptive authority); the separate future Wellness-domain cycle/period feature is entirely outside this contract.

## 11. Open questions

None at acceptance.

*(Inherited matters, carried but not owned by this contract: W1-D3 §10.6 block-versus-warn remains inherited and open, carried only through the verbatim shared-table quotation in section 5 under the §6.4 floor; device-originated intake, provenance, and epistemic-status handling are deferred external future doctrine that this manual-first contract excludes and does not own; the W6 room-register catalogue binding is deferred. No inherited matter becomes a Gym-owned open decision, and period/cycle doctrine is not a Gym matter at all.)*

---

*A contract is the room's laws gathered into one place, in the exact accepted words. The Gym may hold a person's own movement and rest in their own words — a plan made, a walk taken, a night's rest noted, an injury the profile confirms and whose age is always shown — and it may never turn a hard week into a diagnosis, a device's guess into a truth, or the silence where an injury note would be into "healed."*
