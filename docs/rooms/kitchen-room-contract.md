# W4-D3 — Kitchen Room Contract

**Status:** Accepted by human reviewer, 2026-08-04. Not a build instruction. Authorises no implementation or transmission.
**Date:** 2026-08-04 · **Phase:** W4 · **Deliverable:** W4-D3 · **Room:** Kitchen
**Authorises no implementation or transmission.** W5 (adapter/isolation enforcement) and W6 (governed string catalogue) dependencies remain **deferred and unread**. This contract is a governed document: it declares what the Kitchen Room may and may not do, in the exact accepted words of its sources; it mints no authority, builds nothing, and transmits nothing.

---

## 1. Identity and purpose

The Kitchen Room is an honest room for **organising and preparing the user's own Kitchen records** — a governed food-planning and record surface for the recipes, food preferences, grocery and staples lists, and meal plans the user maintains themselves, and for planning meals and groceries at the user's request within its accepted scope. It is **not** a nutrition adviser, a personalised-medical-nutrition service, a therapeutic meal planner, an allergy-safety guarantee, a weight-loss or optimisation tool, an autonomous shopping or ordering system, a vendor selector, a recommendation engine, a connector, an agent, or a companion; it is **not** authorised to reach medical, therapeutic, or diagnostic conclusions, to draw any unsupported health conclusion, or to convert preferences, food choices, or meal data into health facts, and it is **not** authorised to promise any capability this contract does not establish. Its usefulness is its restraint: it organises a person's own food records honestly — including confirmed dietary requirements it lawfully reads through E6 — and helps them plan, and it never turns a food choice into a health verdict. Its exact read, write, outward, and processing authority is fixed in sections 2, 3, and 6, not in this paragraph.

## 2. Read scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation.

**Reference:** W1-D1 §5 · E6.

**Verbatim quotation (W1-D1 §5 · E6):**

> - **E6. Approved Profile (allergies, confirmed dietary requirements only) → Kitchen.** Scoped read under standing consent; section age surfaced on every use.

*Declaration.* Kitchen reads exactly one inbound edge: **E6**, a **standing scoped read** of the **Approved Profile**, limited to **allergies, confirmed dietary requirements only**, with the authority label and **section age surfaced on every use**. The word **only** is load-bearing and is not widened: W0 §5.2's broader *relevant* / *e.g.* wording is not the scope authority and is not imported here. **Allergies are safety-relevant** under W1-D3 §6.3. **Confirmed dietary requirements are non-safety by default** unless another accepted source explicitly classifies a particular item as safety-relevant; Kitchen infers no medical significance from a dietary requirement merely because it is confirmed. Kitchen reads **no conditions generally, no medications, no injuries, no supplements**, and **no Wellness, Gym, or Meditation records** — no edge admits them.

## 3. Write and outward scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation for every source unit.

**Reference:** W1-D1 §3 (home), §4 (categories #9–#11), §5 · E10; W1-D3 §2 (User-reported), D3-T3; W1-D2 §2 (Vendor disclosure grant).

**Verbatim quotations:**

> | **Kitchen records** | C1 | Z1 / Z2 ciphertext | Recipes, preferences, grocery/staples, meal plans |
>
> | 9 | Recipes, food preferences | C1 | Kitchen | Inference source — protected by edge restrictions |
> | 10 | Grocery & staples lists | C1 | Kitchen | Only category with a VendorAdapter edge (E10) |
> | 11 | Meal plans | C1 | Kitchen | May embed scoped Profile reads (E6); inherits C3 handling when it does |
>
> - **T3. User entry → user-reported.** Automatic on entry into room records; carries no profile authority.
>
> | **User-reported** | Entered by the user (logs, notes) but not reviewed into approved status | System, on user entry | Room-scoped use only; never profile truth |
>
> - **E10. Kitchen (grocery/staples list only) → VendorAdapter (Z4).** Minimum payload: the list. Never preferences-as-rationale, never Profile content, never the dietary context that shaped the list. Logged; user-visible.
>
> | **Vendor disclosure** | E10 | Per transmission | Payload is the list, full stop. The grant displays the actual payload before transmission |

*Write declaration.* Kitchen writes its **own C1 records only** — recipes and food preferences (#9), grocery and staples lists (#10), and meal plans (#11) — at their D1 class. User-entered records receive the **User-reported** label on entry (D3-T3): **room-scoped use only, never profile truth**, carrying **no profile authority**. This contract mints no new authority state.

*Meal-plan (#11) handling rule.* A meal plan **remains a C1 record**. Per its exact source — *"May embed scoped Profile reads (E6); inherits C3 handling when it does"* — a meal plan **may embed only E6-scoped content** (the E6 closed list: **allergies and confirmed dietary requirements only**), and that embedded content **inherits C3 handling** (authority label, staleness, and §6.3 treatment for the allergy portion). This is a **handling rule, not a new record class**: the meal plan does not become a C3 record, no general Profile-copy authority is created, and **no conditions, medications, injuries, supplements, or other-room content may be embedded**.

*E10 outward declaration.* Kitchen's single outward edge is **E10**: **Kitchen grocery/staples list only → VendorAdapter / Z4**, a **minimum payload** — **the list, full stop** — **per transmission**, with the **actual payload displayed before transmission**, **logged and user-visible**. The payload carries **never preferences-as-rationale, never Profile content, never the dietary context that shaped the list**. E10 is not a commerce grant and confers no ordering authority.

*Accepted E10 payload authority (current).* The lawful payload is **bare item identity only** — ordinary neutral item wording, with **no reason and no context**. **Excluded** from payload authority: quantities or amounts; free text; notes; annotations; substitutions or explanations; preference or rationale; E6 or Profile content; health or room context; identifiers of every class; metadata; commerce information; and semantic grouping or priority. An incidental serial order may exist but **carries no semantic authority**. **Bare item identity does not override the disclosure prohibition:** if an item name itself would necessarily communicate E6, Profile, preference, dietary, or health context, it **cannot cross** under current authority. No payload field, schema, or example is defined by this contract.

## 4. Inference prohibitions

The general rule (W0 Law 8; ADR-0019). **Kitchen may lawfully rely on an established E6 item — an accepted allergy or confirmed dietary-requirement record — within the exact accepted scope when organising a meal plan; lawful reliance on such an accepted record is not itself a newly derived health conclusion.** What is prohibited is different in kind: the Kitchen Room must never **derive, state, imply, record, silently act on, or change its behaviour because of a new unsupported health or room-jurisdiction conclusion** drawn from its Kitchen C1 records, food choices, exclusions, recipes, meal patterns, or E6 context. An E6 item must remain what its accepted source establishes — it cannot become evidence for another health conclusion. A user request cannot create an absent edge or make a forbidden inference lawful, and E6 is not widened. Observable consequence makes a breach testable; it is never permission to infer silently, and silent behaviour change is the primary target.

**The named-bait list below is a floor, not a ceiling.** It is subordinate to W0 Law 8 and ADR-0019, which bind beyond every enumeration; it is not a risk ontology and not an inference engine. The labels `KITCH-B1`…`KITCH-B5` are **contract-local review labels only** — not registry IDs, global namespaces, fixture IDs, or catalogue IDs. Two assessed candidates were **routed, not made baits**: deficit / weight-loss / moralised-food-scoring mechanics are carried by the W0 §5.2 harm-pattern guard in sections 7 and 8; comparative "safer / healthier" authority-minting is carried by the section 7 speech rules (Law 6; ADR-0020's most-protective-mints-nothing).

### KITCH-B1 — Food-choice-to-health-conclusion inference
- **Forbidden system move:** treating a food choice, exclusion, omission, or preference in a Kitchen record as if it establishes a health conclusion — an allergy, a condition, or any other health fact — about the user.
- **Lawful response boundary:** keep the item as a food choice or preference in a C1 record; preserve any genuinely unknown health status as unknown; refuse the health conclusion; route a real profile-status question through the governed profile review process, never a Kitchen inference.
- **Doctrine anchor:** W0 Law 8; W0 §5.2; ADR-0019; W1-D1 category #9 ("inference source — protected by edge restrictions").
- **Kitchen-specific because:** it operates on Kitchen's own C1 food data as the input — the archetypal Kitchen inference the category-#9 note exists to prevent.
- **Relation to section 5 / harm guard:** not section-5 state behaviour (it manufactures a new conclusion, not handles a known item's staleness) and not the §5.2 harm guard (an inference, not a mechanic).
- **Classification:** review-only for aptness and association-teaching risk; the fixture and any runtime check are deferred to evaluation.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### KITCH-B2 — Allergy-absence-to-all-clear inference
- **Forbidden system move:** converting the absence of a recorded allergy into a confirmed negative ("no allergy") or into permission to proceed as though an all-clear had been established.
- **Lawful response boundary:** preserve the distinction between unknown and confirmed negative; treat allergy-status-unknown as verify-before-relying, never all-clear; surface the uncertainty; never manufacture a negative claim from silence; route a genuine status question through the governed review process.
- **Doctrine anchor:** W1-D3 §5 (absence-vs-negative); §6.3 (the Kitchen worked example — allergy-status-unknown is not all-clear); W0 Law 8; ADR-0019; ADR-0020 (unknown handling).
- **Kitchen-specific because:** allergy is Kitchen's live safety-relevant E6 read, and meal planning against an unproven allergy status is the corpus's named deepest trap.
- **Relation to section 5 / harm guard:** **complementary to section 5, not duplicative** — section 5 shows the unknown honestly; this bait forbids the inference that overwrites the unknown with a manufactured negative or all-clear.
- **Classification:** review-only for aptness; fixture and runtime deferred to evaluation.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### KITCH-B3 — Meal-pattern-to-health-state inference
- **Forbidden system move:** inferring a disorder, motive, diagnosis, or other health state from meal timing, frequency, quantity, or omission recorded in Kitchen data.
- **Lawful response boundary:** keep meal patterns as organisational C1 records; retain a neutral meal-planning posture; refuse the health-state conclusion; provide only neutral, user-requested information within scope; route a genuine health concern to the governed process.
- **Doctrine anchor:** W0 Law 8 (which names disordered-eating patterns as a prohibited inference target); W0 §5.2; ADR-0019.
- **Kitchen-specific because:** meal-pattern data is uniquely Kitchen's; the disordered-eating inference target is named in Law 8 for this room's data shape.
- **Relation to section 5 / harm guard:** an inference, distinct from the §5.2 harm-guard mechanic (deficit/restriction/scoring, routed to sections 7–8); no staleness state is involved, so it is not section-5 behaviour.
- **Classification:** review-only for aptness and restriction/disordered-eating risk; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### KITCH-B4 — Nutrition-information-to-treatment reframing
- **Forbidden system move:** converting neutral, user-requested nutrition information into treatment, prevention, recovery, or therapeutic direction for the user.
- **Lawful response boundary:** keep nutrition information neutral and user-requested within scope; organise the user's own records; refuse treatment, prevention, or therapeutic direction; keep the room a preparation surface, never a clinical one.
- **Doctrine anchor:** W0 Law 6 (clinical line); W0 §5.2 (neutral nutrition information only); ADR-0002; ADR-0019.
- **Kitchen-specific because:** neutral nutrition information is Kitchen's to display; the reframing-into-treatment move is the room's specific clinical-line-creep risk.
- **Relation to section 5 / harm guard:** a specific behavioural reframing a fixture can later exercise, retained in section 4 while the general Law 6 boundary is also carried in section 7; not section-5 state behaviour and not the restriction-mechanic harm guard.
- **Classification:** review-only for whether the boundary stays organisational rather than advisory; fixture and runtime deferred.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### KITCH-B5 — Preference-to-medical-requirement elevation
- **Forbidden system move:** treating an ordinary user preference or exclusion as though it were a confirmed medical or safety requirement — including inflating a non-safety confirmed dietary requirement into safety-relevant status without an accepted source classifying it so.
- **Lawful response boundary:** preserve a preference as a preference; keep confirmed dietary requirements at their non-safety-by-default tier unless a separate accepted source classifies a particular item as safety-relevant; infer no medical significance merely because an item is confirmed; keep allergy verification distinct from preference handling.
- **Doctrine anchor:** W0 §5.2 (preferences stay preferences); W1-D3 §6.3 (safety set is allergy/medication/condition/injury — confirmed dietary requirements not automatically included); ADR-0019.
- **Kitchen-specific because:** the preference / confirmed-dietary-requirement / allergy distinctions are exactly Kitchen's E6-adjacent surface; the tier-inflation move is unique to this room.
- **Relation to section 5 / harm guard:** kept separate from KITCH-B1 (B1 manufactures a health fact; B5 mis-assigns authority tier); a mis-classification of tier, not a section-5 staleness state, and not a harm-guard mechanic.
- **Classification:** review-only for ordinary-preference medicalisation risk; fixture and runtime deferred.
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

**Kitchen room-register wording (review of record — proposed, not final).** These are the Kitchen voice for the states quoted above; each is bracketed with generic placeholders (never real health content) and instantiates the shared rule without altering it. Kitchen's **live safety-relevant read is allergy** (E6); **confirmed dietary requirements are non-safety by default** unless a separate accepted source classifies a particular item as safety-relevant. Because allergy context can be relied on when Kitchen plans a meal, the always-show and acknowledge-before-continuing rules are live for the allergy-safety states. **Coverage ledger** — every inherited W1-D3 state and contradicted context is visibly mapped to a proposed string:

| W1-D3 state / context | Source semantics (verbatim quotation above) | Proposed string |
|---|---|---|
| **Current** | "Within its review interval" · "Normal use, age surfaced" | RR-Current |
| **Review due** (non-safety) | "Interval passed…" · "Usable, with a visible review-due flag" | RR-ReviewDue-NonSafety |
| **Review due** (allergy-safety, relied-on) | row 3 — review interval passed; inline uncertainty **Always** | RR-ReviewDue-Safety |
| **Stale** (non-safety) | "Past the renewal grace period" · "Usable only with explicit uncertainty surfacing…" | RR-Stale-NonSafety |
| **Stale** (allergy-safety, relied-on) | row 3 — renewal grace period passed; inline uncertainty **Always** | RR-Stale-Safety |
| **Expired** | "Past the hard limit…" · "Not usable as truth. Treated as **unknown** until re-reviewed" | RR-Expired |
| **Superseded** | "Replaced; permanent terminal state" · "History only" | RR-Superseded |
| **Unknown freshness** | "No reliable review date…" · "Treated as stale until reviewed" | RR-UnknownFreshness |
| **Contradicted** | §5 — both accounts visible; "Newer is not truer until the user says so" | RR-Contradicted |
| **Expired / contradicted / unknown + allergy-safety use** | row 5 — acknowledged inline before continuing; most-protective | RR-Unknown-Safety |
| **Expired / contradicted / unknown + non-safety use** | row 6 — treated as unknown; uncertainty named | RR-Unknown-NonSafety |

- **RR-Current** — *Current, within its review interval; label and age carried.* — *"This meal plan uses [profile item] — [authority label], last reviewed [age] — and it is Current, within its review interval."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-NonSafety** — *Review due (non-safety); usable with a visible review-due flag; label and age carried.* — *"This meal plan uses [profile item] — [authority label], last reviewed [age] — whose review is due because its review interval has passed; usable, with this review-due flag shown."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-Safety** — *Review due, allergy-safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This meal plan relies on an allergy record — [authority label], last reviewed [age] — whose review is due because its review interval has passed; because it is safety-relevant, this plan carries that uncertainty inline: please verify it before relying on the plan."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-NonSafety** — *Stale (non-safety); usable only with uncertainty named in the output; label and age carried.* — *"This meal plan uses [profile item] — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; this plan names that uncertainty wherever it relies on it."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-Safety** — *Stale, allergy-safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This meal plan relies on an allergy record — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; because it is safety-relevant, this plan carries that uncertainty inline: please verify it before relying on the plan."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Expired** — *Expired; not usable as truth, treated as unknown until re-reviewed; label and status surfaced; routes to the unknown handling.* — *"[profile item] — [authority label], last reviewed [age] — is expired: past its hard limit and not usable as truth, so it is treated as unknown until re-reviewed."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Superseded** — *Superseded; replaced, a permanent terminal state; history only, not used as current.* — *"[profile item] has been superseded — replaced, a permanent terminal state; the earlier version is kept as history only and is not used as current."*
  `Review of record pending W6 governed string catalogue.`
- **RR-UnknownFreshness** — *Unknown freshness; no reliable review date; treated as stale until reviewed; label visible, uncertainty named.* — *"[profile item] — [authority label] — has no reliable review date; it is treated as stale until reviewed, and any plan relying on it names that uncertainty."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Contradicted** — *Contradicted; both accounts shown with their labels and dates; older-item staleness surfaced; neither settled; the room resolves nothing.* — *"Two accounts of [profile item] disagree — [source A: authority label A, date A] and [source B: authority label B, date B]; both are shown with their labels and dates, the older account's staleness is surfaced alongside where applicable, and neither is treated as settled — newer is not truer until you decide through review."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-Safety** — *Expired / contradicted / unknown, allergy-safety use; state, reason, label, and age/status carried; acknowledged inline before continuing, most-protective verbal.* — *"The allergy record this plan would rely on — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; the state and the reason are acknowledged here before continuing, this plan carries that uncertainty, and you should verify before relying on it — it is not all-clear; you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-NonSafety** — *Expired / contradicted / unknown, non-safety use; state, reason, label, and status carried; treated as unknown, uncertainty named.* — *"The [profile item] here — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; this plan names that uncertainty, does not treat it as settled, and you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`

Each string names its state and its source-grounded reason, visibly carries the authority label and age/status where the shared table requires it, and carries uncertainty inline where required. **Kitchen-specific rule:** **allergy-status-unknown means verify before relying on the meal plan; it never means all-clear.** This is a **verbal / surfacing posture only** — no unsupported warning, restriction, recommendation, or functional block is minted, and W1-D3 §10.6 (block-versus-warn) remains **inherited and open** under the §6.4 floor. Confirmed dietary requirements remain **non-safety by default** unless separately classified by an accepted source. None of these strings warns, restricts, recommends, reassures in a way that obscures uncertainty, or gives medical advice.

## 6. Processing boundary

Carried under ADR-0018's paired form for the processing edge, with the ADR-0017 architectural-isolation requirement.

**Reference:** W1-D1 §5 · E11-K; ADR-0017 (Room Isolation Model).

**Verbatim quotation (W1-D1 §5 · E11-K):**

> - **E11-K. Kitchen → Z3.** AI assistance on C1 Kitchen records only. Approved Profile sections enter Kitchen processing exclusively through E6 — never as direct Z3 payload.

*Declaration.* Kitchen AI assistance is a **user-initiated processing disclosure event** (Law 1; ADR 0001) on **C1 Kitchen records only**; its grant is single-task by default, session at maximum (W1-D2). **E6 is the exclusive Profile-context entry** — no direct Profile payload enters Kitchen processing outside E6. Under **ADR-0017**: Kitchen processing occurs in a context that has never contained another room's content; **one grant binds one room; the session derives from the grant**; cross-room content is **unreachable, not merely forbidden**; **operational enforcement belongs to W5** and this contract claims no runtime isolation exists. Three things are distinguished and must not be conflated: **E11-K** — governed Kitchen AI processing; **category-#11 embedded E6 content** — C3 handling *within* the C1 meal-plan record (section 3); and **E10** — the outbound **non-AI** transfer boundary (section 3). **E10 does not become an AI-processing grant.** This contract **establishes no VendorAdapter, connector, network, endpoint, credential, runtime filter, or payload-enforcement implementation, claims none has been implemented or verified, and authorises none** — E10 is a declared boundary only, and operational enforcement belongs to W5. The E6 display-versus-processing split is a declared **W5 dependency**, not a Kitchen-owned open question.

## 7. Speech rules

Kitchen applies the safety-surfacing doctrine (ADR-0002) with the clinical line (W0 Law 6) and the Kitchen purpose and harm-pattern guard (W0 §5.2) in room terms. The room **must**: distinguish organisational meal planning from medical or therapeutic advice; provide **only neutral, user-requested nutrition information** within scope; **refuse** diagnosis, treatment, prevention, recovery, or therapeutic direction (the general Law 6 boundary, carried here in addition to KITCH-B4); **never** create calorie-deficit or weight-loss optimisation; **never** create restriction loops or adherence-to-target mechanics; **never** moralise food as good or bad; **never** make unsupported "safer" or "healthier" claims (most-protective framing mints nothing); keep **allergy-status-unknown distinct from all-clear**; and describe an E10 transmission honestly without claiming ordering or connector capability. Surfacing reads governance labels only (ADR-0002 Doctrine 1); the only thing ever withheld is the room's own overclaiming, never the user's own action (Doctrine 3). If the user requests a restriction, deficit, weight-loss, or moralised-scoring mechanic, Kitchen declines that mechanic specifically and remains otherwise available (§5.2). The room gives **no medical or therapeutic recommendations, no personalised nutrition or dietary advice, and no diagnosis, treatment, prevention, recovery, or health optimisation**; its lawful outputs remain **organisational meal planning, organising the user's own Kitchen records, and neutral, user-requested nutrition information within accepted scope**. It does **not** provide therapeutic meal planning, weight-loss or deficit advice, restriction mechanics, unsupported "safer" or "healthier" claims, or personalised medical nutrition — consistent with KITCH-B4 and the general Law 6 boundary — and it does **not** adopt companion, therapeutic, or clinical framing.

## 8. Forbidden list

The Kitchen anti-map, named for emphasis though default-deny already excludes each item. Kitchen must not:

- read any Approved Profile content beyond the E6 closed list (allergies, confirmed dietary requirements only);
- read the Health Vault, or perform any cross-room read or cross-room inference;
- embed Profile content beyond the E6 closed list into any record, including a meal plan;
- transfer anything to a vendor beyond E10;
- place quantity or amount in the current E10 payload;
- place free text, notes, annotations, substitutions, or explanations in the payload;
- place preference or rationale in the payload;
- place E6, Profile, dietary, allergy, or health context in the payload;
- place authority labels, age, freshness, uncertainty, or contradiction status in the payload;
- treat any identifier (user, account, household, room, list, item, vendor, device, session, or grant) as vendor-payload authority;
- place metadata or hidden fields in the payload;
- use meaning-bearing ordering or grouping in the payload;
- perform or encode vendor selection, address, payment, ordering, substitutions, pricing, availability, fulfilment, auto-purchase, or preferred-vendor steering;
- treat the internal governance log as part of the payload;
- read, embed, or transmit conditions, medications, injuries, or supplements;
- read, embed, or transmit Wellness, Gym, or Meditation content;
- infer dietary conditions, restriction patterns, or health states from food data;
- operate as a restriction engine or apply moralised-food mechanics;
- make unsupported safety or health claims;
- claim that W5, a VendorAdapter, or a connector exists.

Incidental serial order in a list carries **no priority and no semantic meaning**. Every prohibition here restates existing law; none mints a new authority.

## 9. Validator hooks

Per ADR-0021's decidability line, every governed term is **mechanically checkable** or **review-only**, with runtime/enforcement matters separately **deferred to evaluation**. No term floats in the ambiguous middle. A validator inspects deterministic repository artefacts only; **a validator must never judge nutritional, dietary, clinical, or vendor-operational adequacy** — that would be a judging validator (doctrine minting by machinery), which is prohibited.

**Mechanically checkable (document-decidable):**

- eleven-section structure, order, numbering, and non-blank bodies;
- Kitchen identity present (section 1);
- exact source references present for E6, the home row, categories #9/#10/#11, T3, User-reported, E10, E11-K, and ADR-0020;
- byte-level verbatim quotation fidelity for E6, the Kitchen home row, categories #9/#10/#11, W1-D3 T3, the User-reported row, E10, the W1-D2 vendor-disclosure grant row, E11-K, and the complete ADR-0020 shared-table quotation;
- C1 class fidelity for the Kitchen home and categories;
- preservation of the load-bearing E6 word `only`;
- the category-#11 C3-handling wording present and unchanged;
- the E10 load-bearing words `only`, `minimum payload`, `never`, `the list, full stop`, `per transmission`, and `actual payload` preserved;
- the five `KITCH-B` labels present and unique;
- exactly five future-fixture declarations, one per bait;
- no fixture identifiers; no catalogue identifiers; no placeholder token; no realistic clinical/food-health pair;
- ADR-0020 quotation fidelity; all six W1-D3 states present; eleven room-register strings each carrying the W6 review-of-record mark;
- the allowed E10 payload class (bare item identity only) stated; the prohibited direct and indirect payload classes stated;
- an explicit stated distinction between the transmitted payload and the internal governance log;
- no connector, schema, API, or existence claim;
- the section 11 open-questions body present.

**Review-only (human judgement):**

- identity fitness and that no unearned capability is advertised;
- scope-selection correctness and E6-widening risk;
- bait aptness and association-teaching risk;
- ordinary-preference medicalisation risk; restriction / disordered-eating risk;
- room-register wording quality; neutral item-name judgement;
- whether an item identity indirectly reveals E6, preference, or other context;
- whether any ordering carries semantic meaning;
- whether the proposed E10 surface is genuinely minimal;
- speech quality and indirect leakage; constitutional soundness; semantic authority minting.

**Evaluation / later enforcement (deferred, not a contract-validator target):**

- fixture existence and behaviour; runtime inference; model obedience;
- operational isolation; actual payload inspection; runtime field filtering;
- connector behaviour; network transmission; authentication; vendor response handling;
- ordering implementation; logging implementation; exfiltration testing;
- W5 enforcement; W6 catalogue binding.

## 10. Constitutional check

This contract implements existing law and mints nothing new. It **implements** W0 Law 6 (the clinical line), Law 8 (no cross-room or food-derived inference), and Law 9 (the Meditation wall); it **preserves** the W0 §5.2 harm-pattern guard, **E6 as a closed read** (allergies, confirmed dietary requirements only), **C1 Kitchen records**, category #11's **exact C3-handling rule**, and **E10 as the bare-list outward edge only**. It **creates no new edge, no new record class, and no new authority state**; it **creates no commerce capability and no connector**; and it **authorises no implementation or transmission**. Every scope clause is carried in ADR-0018 paired form from W1-D1, W1-D2, and W1-D3; the shared behaviour standard is carried verbatim from ADR-0020; the wording strings route to the future W6 governed string catalogue as review-of-record.

## 11. Open questions

None at acceptance.

*(Inherited matters, carried but not owned by this contract: W1-D3 §10.6 block-versus-warn remains inherited and open, carried only through the verbatim shared-table quotation in section 5 under the §6.4 floor; the E6 display-versus-processing isolation split is a declared W5 dependency; the W6 room-register catalogue binding is deferred. No inherited matter becomes a Kitchen-owned open decision. The E10 payload questions are settled by the accepted rulings and are not reopened here: quantity is excluded from payload authority; identifiers are excluded from payload authority; incidental serial order carries no semantic authority.)*

---

*A contract is the room's laws gathered into one place, in the exact accepted words. The Kitchen may hold a person's own food records honestly, plan a meal or a grocery list at their asking, and let only the bare list walk out to a vendor — and it may never turn a food choice into a health verdict, nor let "no allergy on record" mean "safe."*
