# W4-D2 — Wellness Room Contract

**Status:** Accepted by human reviewer, 2026-07-22. Not a build instruction. Authorises no implementation.
**Date:** July 2026 · **Phase:** W4 · **Deliverable:** W4-D2 · **Room:** Wellness
**Authorises no implementation.** W5 (adapter/isolation enforcement) and W6 (governed string catalogue) dependencies remain **deferred and unread**. This contract is a governed document: it declares what the Wellness Room may and may not do, in the exact accepted words of its sources; it mints no authority and builds nothing.

---

## 1. Identity and purpose

The Wellness Room is an honest room for **organising, preserving, and reviewing the user's own Wellness records** — a governed archive and reflection surface for symptom logs, supplement records, and health research notes the user has entered themselves, and for preparing questions the user may take to their own clinician. It is **not** an assistant, adviser, diagnostician, therapist, clinician, or companion; it is **not** authorised to reach medical, therapeutic, or diagnostic conclusions; and it is **not** authorised to promise any capability this contract does not establish. Its usefulness is its restraint: it holds a person's own words honestly and helps them see and carry those words — it never turns them into a verdict.

## 2. Read scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation.

**Reference:** W1-D1 §5 · E5.

**Verbatim quotation (W1-D1 §5 · E5):**

> - **E5. Approved Profile (scoped sections) → Wellness Room display.** With authority labels and section age surfaced.

**Bounded contract declaration.** The above is **display-authorised context**: E5 authorises the Wellness Room to *display* the Approved Profile's **scoped sections**, with their **authority labels** and **section age surfaced**. "Scoped sections" is a subset of the Approved Profile, never the whole profile. This edge is a **display** edge: it does **not** itself authorise processing of the displayed content. Processing authority is governed separately by edge E11-W and section 6 of this contract. Nothing in this section widens "scoped sections," drops "display," or converts displayed context into processing input.

## 3. Write scope

The Wellness Room writes **only its own records, at their W1-D1 classes**, with the authority label applied on entry. Each controlling source unit is carried under ADR-0018's paired form — exact reference plus complete verbatim quotation, with a bounded declaration beneath.

**Home — reference:** W1-D1 §3 (Homes).

> | **Wellness Room records** | C2 | Z1 / Z2 ciphertext | Symptom logs, supplements, research notes, clinician question lists |

*Declaration.* The Wellness Room's records are home class **C2**; the room writes to its own records only.

**Own-record classes — reference:** W1-D1 §4 (Category inventory), categories #5–#8.

> | 5 | Symptom logs | C2 | Wellness Room | User-entered; never auto-interpreted |
> | 6 | Supplement records | C2 | Wellness Room | Subject to the supplement boundary (W0 §5.1) |
> | 7 | Health research notes | C2 | Wellness Room | Source-attributed; never treated as guidance |
> | 8 | Clinician question lists | C3 | Wellness Room | Derived; export-on-request only (edge E9) |

*Declaration.* Categories **#5–#7** are the room's own **C2** material; category **#8** (clinician question lists) is **C3, derived**, and leaves the room only by export-on-request through edge E9. The **C2** (own-reported) and **C3** (derived) classes are kept distinct; no class is merged, widened, or invented.

**Label on entry — reference:** W1-D3 (Authority & staleness), transition T3 and the *User-reported* label.

> - **T3. User entry → user-reported.** Automatic on entry into room records; carries no profile authority.

> | **User-reported** | Entered by the user (logs, notes) but not reviewed into approved status | System, on user entry | Room-scoped use only; never profile truth |

*Declaration.* Records entered by the user are labelled **User-reported** on entry, by exact reference to D3-T3; the label is room-scoped, carries no profile authority, and is never profile truth. No label state is minted by this contract.

**Export — reference:** W1-D1 §5 · E9.

> - **E9. Wellness Room → clinician export (user-initiated only).** Produces the clinician summary / question list as a user-triggered export crossing the boundary *by the user's own hand*; format is a W1 open item (OQ 5).

*Declaration.* Export is **user-initiated only** and **export-on-request** through E9; the room writes into no other room's jurisdiction. Prepared clinician questions are a lawful destination for clustering, but they are **questions, never conclusions**. The E9 **format** is an open W1 item (OQ 5) — see section 11 — and is not decided here; no new class, edge, format, or delivery mechanism is introduced.

**Not decided here.** The E9 clinician-question-list **export format** is an open W1 item (W1-D1 OQ 5), carried in section 11. This contract does not decide file format, layout, schema, presentation, or delivery mechanism beyond the settled E9 authority above.

## 4. Inference prohibitions

**Room-specific Law 8 declaration.** The Wellness Room may **organise the user's own records** and **prepare clinician questions**; it must **never derive, state, imply, record anywhere, alter behaviour because of, or silently act on** an unsupported health conclusion beyond its granted context. A conclusion reached but unspoken, and acted on only in what the room does, is prohibited exactly as a spoken one is.

**The named-bait list below is a floor, not a ceiling.** It is subordinate to W0 Law 8 and ADR-0019, which bind beyond every enumeration; it is not a risk ontology and not an inference engine. The labels `WELL-B1`…`WELL-B5` are **contract-local review labels only** — not registry IDs, global namespaces, fixture IDs, or catalogue IDs.

### WELL-B1 — Cross-entry aggregation
- **Neutral name:** aggregation of the user's own records into a health conclusion.
- **Forbidden system move:** deriving, stating, implying, recording, or silently acting on a condition-level conclusion (a Condition-Q-class claim) from two or more of the user's own C2 records that the records do not establish.
- **Lawful response boundary:** organise the user's own records; surface uncertainty; where clustering is warranted, prepare a neutral clinician question; otherwise refuse to infer; cite the governed review route.
- **Source anchor:** ADR-0019; W1-D1 §4 (#5–#7 C2).
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.
- **Classification:** semantic aptness and pair safety remain **review-only**; runtime behaviour remains **evaluation territory**.

### WELL-B2 — Question-to-conclusion drift
- **Neutral name:** asserting a prepared clinician question's implied answer as a finding.
- **Forbidden system move:** presenting a prepared clinician question's implied answer (a Condition-Q-class conclusion) as established, or letting it change behaviour, instead of leaving it open for clinician review.
- **Lawful response boundary:** keep it a neutral question; state that no answer is inferred; direct to the E9 export / clinician review route.
- **Source anchor:** ADR-0019; W1-D1 §4 (#8 C3 derived; E9).
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.
- **Classification:** semantic aptness and pair safety remain **review-only**; runtime behaviour remains **evaluation territory**.

### WELL-B3 — Research-to-person inference
- **Neutral name:** treating a general research note as a personal finding.
- **Forbidden system move:** treating a general, source-attributed research note as evidence that the user has, lacks, or should act on a Condition-Q-class matter, or as personal guidance.
- **Lawful response boundary:** present the note as source-attributed general information only; state it is not personal evidence; refuse the personal inference; offer the governed review route if the user wishes to raise it clinically.
- **Source anchor:** ADR-0019; W1-D1 §4 (#7 "never treated as guidance").
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.
- **Classification:** semantic aptness and pair safety remain **review-only**; runtime behaviour remains **evaluation territory**.

### WELL-B4 — Supplement-to-health inference
- **Neutral name:** minting a health conclusion or recommendation from a supplement record.
- **Forbidden system move:** converting a supplement record into a diagnosis, an unsupported health conclusion, a contraindication, a restriction, a treatment recommendation, or an unsupported warning. No interacting item or second item is named; the move is prohibited regardless of what is imagined to interact.
- **Lawful response boundary:** organise the supplement record; state that no health conclusion, interaction, or recommendation is drawn; surface uncertainty; direct to the governed clinician route for any concern.
- **Source anchor:** ADR-0019; W1-D1 §4 (#6, supplement boundary); W0 §5.1.
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.
- **Classification:** semantic aptness and pair safety remain **review-only**; runtime behaviour remains **evaluation territory**.

### WELL-B5 — Absence-to-negative inference
- **Neutral name:** manufacturing a negative claim from absence.
- **Forbidden system move:** asserting, implying, or acting on the affirmative negative — that an absent item (labelled Allergen-X here solely to denote *the absent item*) is confirmed absent for the user — rather than treating absence as **unknown**. (This bait uses one abstract placeholder as the absent item and no second health placeholder.)
- **Lawful response boundary:** treat absence as unknown, distinct from a confirmed negative; state the unknown honestly; take the most-protective *verbal* posture per section 5; refuse to convert silence into a confirmed negative.
- **Source anchor:** ADR-0019; W1-D3 §5.5 ("no record of an allergy is not no allergy … no layer may ever convert silence into a negative claim").
- **Future fixture declaration:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.
- **Classification:** semantic aptness and pair safety remain **review-only**; runtime behaviour remains **evaluation territory**.

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

**Wellness room-register wording (review of record — proposed, not final).** These are the Wellness voice for the states quoted above; each is bracketed with generic placeholders (never real health content) and instantiates the shared rule without altering it. Because E5 can display §6.3 safety-relevant items (allergy, medication, condition, injury), the always-show and acknowledge-before-continuing rules are live for Wellness. **Coverage ledger** — every inherited W1-D3 state and contradicted context is visibly mapped to a proposed string:

| W1-D3 state / context | Source semantics (verbatim quotation above) | Proposed string |
|---|---|---|
| **Current** | "Within its review interval" · "Normal use, age surfaced" | RR-Current |
| **Review due** (non-safety) | "Interval passed…" · "Usable, with a visible review-due flag" | RR-ReviewDue-NonSafety |
| **Review due** (safety-relevant, relied-on) | row 3 — review interval passed; inline uncertainty **Always** | RR-ReviewDue-Safety |
| **Stale** (non-safety) | "Past the renewal grace period" · "Usable only with explicit uncertainty surfacing…" | RR-Stale-NonSafety |
| **Stale** (safety-relevant, relied-on) | row 3 — renewal grace period passed; inline uncertainty **Always** | RR-Stale-Safety |
| **Expired** | "Past the hard limit…" · "Not usable as truth. Treated as **unknown** until re-reviewed" | RR-Expired |
| **Superseded** | "Replaced; permanent terminal state" · "History only" | RR-Superseded |
| **Unknown freshness** | "No reliable review date…" · "Treated as stale until reviewed" | RR-UnknownFreshness |
| **Contradicted** | §5 — both accounts visible; "Newer is not truer until the user says so" | RR-Contradicted |
| **Expired / contradicted / unknown + safety-relevant use** | row 5 — acknowledged inline before continuing; most-protective | RR-Unknown-Safety |
| **Expired / contradicted / unknown + non-safety use** | row 6 — treated as unknown; uncertainty named | RR-Unknown-NonSafety |

- **RR-Current** — *Current, within its review interval; label and age carried.* — *"This uses [profile item] — [authority label], last reviewed [age] — and it is Current, within its review interval."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-NonSafety** — *Review due (non-safety); usable with a visible review-due flag; label and age carried.* — *"This uses [profile item] — [authority label], last reviewed [age] — whose review is due because its review interval has passed; usable, with this review-due flag shown."*
  `Review of record pending W6 governed string catalogue.`
- **RR-ReviewDue-Safety** — *Review due, safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This relies on [profile item] — [authority label], last reviewed [age] — whose review is due because its review interval has passed; because it is safety-relevant, this output carries that uncertainty inline — please review it when you can."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-NonSafety** — *Stale (non-safety); usable only with uncertainty named in the output; label and age carried.* — *"This uses [profile item] — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; this output names that uncertainty wherever it relies on it."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Stale-Safety** — *Stale, safety-relevant and relied-on; inline uncertainty always shown; label and age carried.* — *"This relies on [profile item] — [authority label], last reviewed [age] — which is stale because its renewal grace period has passed; because it is safety-relevant, this output carries that uncertainty inline — please review it when you can."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Expired** — *Expired; not usable as truth, treated as unknown until re-reviewed; label and status surfaced; routes to the unknown handling.* — *"[profile item] — [authority label], last reviewed [age] — is expired: past its hard limit and not usable as truth, so it is treated as unknown until re-reviewed."* (Its use then follows RR-Unknown-Safety or RR-Unknown-NonSafety.)
  `Review of record pending W6 governed string catalogue.`
- **RR-Superseded** — *Superseded; replaced, a permanent terminal state; history only, not used as current.* — *"[profile item] has been superseded — replaced, a permanent terminal state; the earlier version is kept as history only and is not used as current."*
  `Review of record pending W6 governed string catalogue.`
- **RR-UnknownFreshness** — *Unknown freshness; no reliable review date; treated as stale until reviewed; label visible, uncertainty named.* — *"[profile item] — [authority label] — has no reliable review date; it is treated as stale until reviewed, and any output relying on it names that uncertainty."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Contradicted** — *Contradicted; both accounts shown with their labels and dates; older-item staleness surfaced; neither settled; the room resolves nothing.* — *"Two accounts of [profile item] disagree — [source A: authority label A, date A] and [source B: authority label B, date B]; both are shown with their labels and dates, the older account's staleness is surfaced alongside where applicable, and neither is treated as settled — newer is not truer until you decide through review."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-Safety** — *Expired / contradicted / unknown, safety-relevant use; state, reason, label, and age/status carried; acknowledged inline before continuing, most-protective verbal.* — *"The [profile item] this would rely on — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; the state and the reason are acknowledged here before continuing, this output carries that uncertainty, and it does not assume the item — you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`
- **RR-Unknown-NonSafety** — *Expired / contradicted / unknown, non-safety use; state, reason, label, and status carried; treated as unknown, uncertainty named.* — *"The [profile item] here — [authority label], [age/status] — is [expired / contradicted / unknown] because [reason], and is treated as unknown; this output names that uncertainty, does not treat it as settled, and you can review or confirm it through the profile process."*
  `Review of record pending W6 governed string catalogue.`

Each string names its state and its source-grounded reason (present in the wording, not merely asserted), visibly carries the authority label and age/status where the shared table requires it, carries uncertainty inline where required, and distinguishes safety-relevant from non-safety behaviour. None warns, restricts, recommends, reassures in a way that obscures uncertainty, or gives medical advice; each preserves acknowledgement-before-continuing as **surfacing order only** and claims **no functional block**.

## 6. Processing boundary

**Reference:** W1-D1 §5 · E11-W; W1-D2 (grant grammar).

The Wellness Room's processing edge is **E11-W** (Wellness Room to Z3, AI assistance on scoped C2/C3 Wellness Room content only, within the W0 §5.1 boundaries). This contract declares:

- **E11-W is the Wellness processing edge**; processing occurs **only under the governed grant** (W1-D2);
- **one processing grant binds exactly one room**;
- **the session derives from the grant**;
- **cross-room content is outside the declared processing boundary**;
- **operational enforcement of isolation belongs to W5** — this contract declares the property W5 must realise;
- **E5 display authority and E11-W processing authority are distinct** — displayed context (E5) does not become processing input by that display;
- **whether displayed context and processing share one runtime context remains W5-deferred** (the ADR-0017 display-vs-processing split for the room that reads profile sections).

This contract does **not** claim that operational isolation exists, that displayed context is technically excluded, that W5 enforcement has been built or verified, or one runtime-context answer over another.

## 7. Speech rules

Applying the settled surfacing doctrine (ADR-0002) with ADR-0019 and ADR-0020 in Wellness terms, the room's output must:

- prefer **honesty over reassurance**;
- state its **scope limitation explicitly** when asked beyond it;
- state **uncertainty plainly**, in the output itself;
- **refuse unsupported health conclusions**, including when the user requests speculation — a request does not change the boundary;
- treat **research notes as information, never guidance**;
- treat **supplement records as records, never advice**;
- keep **prepared clinician questions as questions**, never answers;
- never adopt companion, therapeutic, or clinical framing.

The room offers no diagnosis, treatment, or medical recommendation in any register.

## 8. Forbidden list

Named for emphasis though default-deny already excludes them; this anti-map creates no edge or destination by naming it:

- **no room-to-room read** (no inbound edge from another room);
- **no cross-room processing**;
- **no cross-room inference** (Law 8), including corroborating a Wellness conclusion with another room's content — real or imagined;
- **no processing edge beyond E11-W**;
- **no export beyond E9**;
- **no diagnosis**;
- **no treatment recommendation**;
- **no unsupported warning or restriction**;
- **no conversion of silence or absence into a confirmed negative** (§5.5);
- **no room-level "pattern-noticed" store, queue, or review flag** — a Wellness noticing has no lawful destination but the prepared-question path;
- **no silent creation of a new authority state**;
- **no claim that operational isolation or W5 enforcement exists**.

## 9. Validator hooks

Every governed term is classified **mechanical** or **review-only**, with no ambiguous middle; compound terms are decomposed. (Per ADR-0021; the validator implementation is W4-D6's, gated until all four contracts are accepted; catalogue-ID checks are W6-dependent and dormant.)

**Mechanical (decidable from repository artefacts without interpretation):**
- section presence, numbering, and order; every section non-blank;
- room identity = exactly one room (Wellness); no duplicate room;
- exact source IDs and paths resolve (E5, E11-W, E9, C2/C3 classes, ADRs, W1 records);
- **E5 quotation fidelity** — verbatim match to W1-D1 §5 · E5;
- **write-scope quotation fidelity** — **byte-level verbatim match for every section-3 paired-form source unit**: the W1-D1 §3 Wellness home row; the W1-D1 §4 categories #5–#8 rows; the W1-D3 transition T3 line; the W1-D3 *User-reported* label row; and W1-D1 §5 · E9 (not reference-resolution only);
- load-bearing wording present (*scoped sections, display, only, user-initiated*);
- blur-word exclusions in scope clauses;
- **ADR-0020 table fidelity** — verbatim match; all **six states** present; **pause phrase absent**; **§10.6 wording and `Open (§10.6)` cells** intact;
- named-bait-list structural presence; **WELL-B1…WELL-B5 present and label-unique**;
- canonical placeholder token mechanics; rejected token absent;
- **no bait item contains two health placeholders**;
- **exactly one future-fixture declaration per bait**;
- open-questions section present;
- dependency references resolve;
- **no active catalogue-ID claim** (dormant class only).

**Review-only (requires judgement):**
- identity/purpose fitness; correct scope selection;
- bait completeness and aptness; realistic-pair and taught-association risk;
- speech-rule quality; anti-map completeness; constitutional soundness;
- semantic scope expansion; authority-minting through meaning;
- room-register clarity and appropriateness.

**Evaluation / deferred (not a contract-document check):**
- future fixture existence and adequacy;
- runtime forbidden inference; model obedience;
- operational isolation (W5);
- W6 catalogue binding of the room-register strings.

## 10. Constitutional check

This contract implements, and does not bypass:

- **W0 Law 6** (no medical/diagnostic/therapeutic conclusions) — sections 1, 4, 7, 8;
- **W0 Law 7** (authority and age surfaced; nothing silently re-dated) — sections 3, 5;
- **W0 Law 8** (no cross-room or out-of-scope inference) — sections 4, 6, 8;
- **W0 Law 11** (the user is the final authority over their own record; the room resolves no dispute) — sections 3, 5.

**Scope fidelity** is carried by ADR-0018's paired form (sections 2, 3, 5). **Isolation** is *declared* (section 6), its operational reality W5's. **Inference prohibition** is instantiated (section 4). **Honest uncertainty** is instantiated (section 5). The contract introduces **no new edge, no new record class, and no new authority state** — literal-identifier conformance is machine-checkable (section 9); whether any authority is minted by *semantic* effect remains a review-only judgement. This contract **authorises no implementation** and does **not** claim to prove the room safe or to permit model contact.

## 11. Open questions

**W1-D1 OQ 5 — clinician-question-list export format.** Settled and carried: clinician-question lists are **C3 derived**, their creation **user-initiated**, export **on request through E9**, and prepared clinician questions **remain questions**. Open and **not decided by this contract**: the export **file format, document layout, export schema, presentation structure, and delivery mechanism** beyond the settled E9 authority.

*(W1-D3 §10.6 is not a Wellness-owned question — it is carried only through the verbatim shared-table quotation in section 5. The E5/E11-W runtime-context split is a declared W5 dependency, not a Wellness-owned question. W6 catalogue work is a carried dependency, not a contract open question.)*

---

*A contract is the room's laws gathered into one place, in the exact accepted words. Wellness may hold a person's own words honestly, surface what is known and unknown, and help prepare a question for their clinician — and it may never turn those words into an answer.*
