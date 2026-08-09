# W4-D5 — Meditation Room Contract

**Status:** Accepted by human reviewer, 2026-08-09. Not a build instruction. Authorises no implementation.
**Date:** 2026-08-09 · **Phase:** W4 · **Deliverable:** W4-D5 · **Room:** Meditation
**Authorises no implementation.** W5 (adapter/isolation enforcement) and W6 (governed string catalogue) dependencies remain **deferred and unread**. This contract is a governed document: it declares what the Meditation Room may and may not do, in the exact accepted words of its sources; it mints no authority, builds nothing, and signals nothing outward.

---

## 1. Identity and purpose

The Meditation Room is the Wing's **contemplative jurisdiction**: a room for meditation practice, reflection, contemplative and spiritual practice, and — where the user chooses to keep one — the user's own teaching or scripture library. Its records are **CM**, a sensitivity peer of the health evidence class but a separate category behind a structural wall, never a rung of the health ladder. The room holds what a person does in practice, what they write in their own words, and what they have chosen to bring into their own library; it may support practice timers and study at the user's initiation. It is **not** mental-health treatment, therapy, counselling, diagnosis, sleep treatment, productivity optimisation, a spiritual authority, a doctrinal arbiter, a crisis service, or a companion surface, and it reaches no conclusion about the person from anything it holds. Its usefulness is its restraint: it keeps a person's practice and their own words, in their own hands, and it does not turn either into a verdict. Its exact read, write, processing, and outward authority is fixed in sections 2, 3, 6, and 8, not in this paragraph.

---

## 2. Read scope

Carried under ADR-0018's paired form — exact reference plus complete verbatim quotation. Meditation's scope is stated **from its complete edge list and the "no other edges" clause**, never from a summary formulation.

### 2.1 Inbound read from other rooms — not applicable

**Not applicable — this room has no authorised inbound read edge from other rooms.**

No Approved Profile read edge exists for this room; no health, food, or fitness context reaches it through any inbound edge; no such edge is created here. This is the standard N/A-with-a-reason form required of every room contract, not a bespoke exception.

### 2.2 Own-room read and write — M1

**Reference:** W1-D1 §5, *Meditation Room (complete edge list)*, edge **M1**.

**Verbatim quotation (W1-D1 §5):**

> - **M1. User ↔ Meditation Room records.** Read, write, practice, reflect.

**Read declaration.** M1 is the user's own access to their own Meditation records — **read, write, practice, reflect** — exercised inside the user trust boundary. It is a **right, not a grant**: the user's access to their own records is never consent-gated, and no grant object stands between a person and their own practice, reflections, or library. M1 is an own-room edge; it is not an inbound read from another room, and the inapplicability recorded at §2.1 does not touch it.

### 2.3 The complete edge list

**Reference:** W1-D1 §5, *Meditation Room (complete edge list)*, closing clause.

**Verbatim quotation (W1-D1 §5):**

> **There are no other Meditation Room edges.** No M→health, no health→M, no M→Profile, no M→adapters, no M-derived metadata in any other home. Any future bridge is a user-created, named, separately consented, revocable construct requiring its own decision record (W0 §5.4) — and until such a record exists, bridge requests are declined by design, not by discretion.

**Reference:** W1-D1 §5, forbidden-edge table.

**Verbatim quotation (W1-D1 §5):**

> | Meditation Room ↔ anything beyond M1–M2 | Law 9 |

**Edge-set declaration.** The Meditation Room's complete edge set is exactly **M1 and M2**. There is **no inbound Profile read edge and no inbound cross-room read edge**; there is no health→Meditation edge; there is no adapter or vendor edge. Absence of an edge is absence of authority, and no consent, request, or instruction can create one. The complete edge set as asserted in this section is identical to the set asserted in section 8.

---

## 3. Write scope

Own records only, at their D1 class, with the authority label assigned on entry.

**Reference:** W1-D1 §2, sensitivity classes, class **CM**.

**Verbatim quotation (W1-D1 §2):**

> | **CM** | Contemplative | Meditation, reflection, spiritual, and contemplative data; sensitivity **peer of C4** but a separate category with a structural wall, not a tier on the health ladder (Law 9) | Practice records, reflections, contemplative notes, library annotations |

**Reference:** W1-D1 §3, homes.

**Verbatim quotation (W1-D1 §3):**

> | **Meditation Room records** | CM | Z1 / Z2 ciphertext | Structurally isolated; see §5, edges M1–M2 (the only two that exist) |

**Reference:** W1-D1 §4, category inventory, categories 14–16.

**Verbatim quotation (W1-D1 §4):**

> | 14 | Meditation practice records | CM | Meditation Room | |
> | 15 | Reflections & contemplative notes | CM | Meditation Room | |
> | 16 | Contemplative library & annotations | CM | Meditation Room | User-curated |

**Write declaration.** Meditation writes its **own CM records only** — **Meditation practice records (#14)**, **Reflections & contemplative notes (#15)**, and **Contemplative library & annotations (#16, User-curated)** — at their D1 class. It writes to no other home, no other room, no Profile, and no adapter.

**Entry semantics.**

**Reference:** W1-D3 §4, transition **T3**; W1-D3 §1, *User-reported* label.

**Verbatim quotation (W1-D3 §4):**

> - **T3. User entry → user-reported.** Automatic on entry into room records; carries no profile authority.

**Verbatim quotation (W1-D3 §1):**

> | **User-reported** | Entered by the user (logs, notes) but not reviewed into approved status | System, on user entry | Room-scoped use only; never profile truth |

User-entered Meditation records receive the **User-reported** label on entry: **room-scoped use only, never profile truth**, carrying **no profile authority**. This contract mints **no new authority label and no new authority state**.

### 3.1 What the room holds

**Practice records (#14).** A record of a practice the user undertook — including a sit, a walk, or a period of practice the user chooses to record. W0 §5.4 authorises the room to *"support practice timers and study at the user's initiation"*.

**Silent and no-guidance practice.** A silent or no-guidance practice — a timer, a bell, or an unaccompanied sit — **writes nothing by default**. No record is created, and none is required. Where the user **explicitly chooses** to record a completed silent sit, that record is a **#14 Meditation practice record**, User-reported on entry, like any other practice the user records.

**Breath practice.** **Breath awareness and natural-breath attention** may be recorded as a contemplative practice under **#14**. This contract claims **no wider breath authority** — no paced-breathing protocol, retention protocol, breath challenge, specialised or intensive breathwork, physiological manipulation, or medical breathing treatment is within the room's scope, and none is defined, taxonomised, or minted here.

**Reflections and contemplative notes (#15).** The user's own writing, in their own words. Within M1 and M2 authority the room may **hold, retrieve, and organise** a reflection, and — **at the user's initiation** — **discuss** it with them. What a reflection does **not** do is gain authority by being written: **it remains the user's User-reported CM record, and it does not become a system-confirmed person-state, a Profile fact, confirmed health context, or an authority-bearing claim merely because the user wrote it.** The room does not convert it into a conclusion about the person (section 4, MED-B2).

**Contemplative library and annotations (#16).** The **user-curated** teaching or scripture library the user chooses to keep, together with the user's own annotations on it. W0 §5.4 authorises the room to *"hold a user-curated library"*. The user brings and curates the material; the room holds it; the user annotates it; and, under M2 at the user's initiation, the room may **help the user engage with a text** on the terms M2 already sets. **The room does not independently source, fetch, curate, or supply external canonical material or translations into the library under its own authority, and no room-supplied translation or externally sourced content becomes #16 material through this contract** — see section 8.

### 3.2 Current-session choices are not persistent records

A user's choices for the practice in front of them — its length, whether it is guided or unguided, whether it is silent, which of their own texts is open — are **current instructions, not persistent preference records**. This contract establishes **no preference category**, stores no persistent setting, and does not reinterpret #14 to hold settings. No W1-D1 amendment is proposed, implied, or required.

### 3.3 Category boundary

Every data category lives in exactly one home. Meditation's categories are **#14, #15, and #16**, and they are **CM**. **Movement, rest, recovery, and sleep logs are not among them**: this room does not own, write, or acquire that category, and a practice recorded here — including an evening or wind-down sit — is a **#14 CM contemplative practice record in the Meditation Room**, never a rest, recovery, or sleep record. The room frames no practice in sleep-outcome or recovery-outcome terms, which would be a health conclusion this room has no authority to reach.

---

## 4. Inference prohibitions

**The general rule.** A room must not derive a health-relevant or room-jurisdiction conclusion outside its granted context. The prohibition binds **even when the user requests it**: a user request cannot create an absent edge, widen a grant, or authorise a forbidden inference. It binds whether the conclusion is volunteered or requested, stated or unstated, hedged, questioned, or attributed to the user — and **silent behavioural change is the primary target**. Hedging, uncertainty phrasing, and user attribution do not launder a forbidden inference. This room carries the uniform standard, and W0 §5.4 applies **Law 8 with full force** to it: Meditation data may not be mined for mood, mental-health, or behavioural inference.

**Named-bait list — a floor, not a ceiling.** The seven baits below are this room's named minimum. **Law 8 and Law 9 bind beyond the enumeration**, and a forbidden inference outside this list is no less forbidden. Labels are **contract-local review labels** — not registry identifiers, global namespace entries, fixture identifiers, or catalogue identifiers. Each bait declares exactly one future evaluation-fixture reference; **no fixture identifier is created and no fixture exists.**

**A structural note that governs every entry below.** This room has no edge to a governed profile route, and converting an out-of-authority noticing into a prompt, flag, or suggestion aimed at another room would itself be the outward signal Law 9 forbids. Where a forbidden conclusion is declined, the room states its own limit, continues within authorised context, and **places the noticing nowhere**. The user's own movement between rooms is the user's action and is never gated; the room does not carry an observation there on their behalf.

### MED-B1 — Practice-pattern → mental or behavioural state inference

- **Forbidden system move:** using the frequency, duration, timing, interruption, abandonment, trend, or any other pattern across the user's own #14 practice records to manufacture a mental, emotional, psychological, or behavioural state about the user.
- **Lawful response boundary:** keep a practice record a neutral record of a practice that occurred; surface only what the user recorded; assert no state, mood, or disposition; decline the characterisation if asked, state the room's limit, and continue within authorised context. Do not convert the forbidden characterisation into a **system-generated** derived flag, note, prompt, suggestion, or other artefact that carries the inference. **The user's own records are untouched by this boundary:** it constrains what the system may generate, never what the user may write or keep.
- **Doctrine anchor:** W0 Law 8; W0 §5.4 (*"be mined for mood, mental-health, or behavioural inference (Law 8 applies with full force)"*); W0 §2 non-goal 3; ADR-0002; ADR-0019; W1-D3 §8.6.
- **Meditation-specific because:** practice patterns are the most continuously generated signal this room holds, and mood is the first mining target W0 §5.4 names.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B2 — Reflection-content → manufactured person-state

- **Forbidden system move:** converting the user's own #15 reflection or contemplative note into a system claim about who the person is or how the person is — restating their record as a property of them, summarising it into a characterisation, or carrying such a conclusion into later behaviour, whether the resulting claim is favourable, unfavourable, or neutral.
- **Lawful response boundary:** the user's words remain a CM record belonging to the user. Within authorised context the room may hold, organise, retrieve, and — under M2, user-initiated — discuss the record with the user. Keep the grammatical subject the record, never the person: what the record says, when it was written, that it is the user's own. Where a characterisation is requested, decline it, state the limit, and remain available for the practice or the record itself.
- **Doctrine anchor:** ADR-0002 (the Wing speaks about its records, never about the user's body, condition, or risk); W0 Law 8; W0 §5.4; W1-D3 T3; ADR-0019.
- **Meditation-specific because:** category #15 expressly makes *Reflections & contemplative notes* a primary Meditation-owned record type, and because those records may contain first-person language about inner experience, the collapse from *what the record says* to *what the person is* is especially direct here.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B3 — Meditation-derived outward signal in any direction

- **Forbidden system move:** any Meditation-derived content, metadata, conclusion, flag, score, pattern indication, behavioural trace, or other signal appearing in another home, or influencing the behaviour of another room, in any direction and by any mechanism — including writing outward, persisting anything from an M2 processing event outside the room, allowing an M2 payload or its output to reach another room's context, and changing another room's behaviour, selection, ranking, framing, or omission because of something known only here.
- **Lawful response boundary:** the complete edge list is M1–M2 and nothing else. M2 persists nothing outside the room and no output may be written to any other room. Where a request would require a crossing, decline it, state that the boundary is structural, and continue within authorised context. Mint no bridge, no summary destined elsewhere, and no derived artefact whose purpose is to be read outside. A bridge, if the user ever wants one, is a separate, explicit, user-created, revocable construct requiring its own decision record.
- **No channel is implied by its prohibition.** No outward mechanism, field, payload, bridge, or interface exists, and nothing in this entry describes one. The bait addresses the **attempted crossing** — including a simulated, proposed, or offered crossing — against a boundary that is absolute.
- **Doctrine anchor:** W0 Law 9; W1-D1 §5 (*"There are no other Meditation Room edges…"*) and the forbidden-edge table; M2's no-output-elsewhere clause; W1-D2 §2; ADR-0018; ADR-0019.
- **Meditation-specific because:** this room's outward boundary is constitutional rather than unprovisioned — Law 9 is implemented structurally, so the failure mode is the construction of a channel doctrine says does not exist.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B4 — Absence or frequency → motivation, progress, or wellbeing verdict

- **Forbidden system move:** converting missed, shortened, abandoned, irregular, frequent, prolonged, or otherwise patterned practice — or the absence of any practice record at all — into a conclusion about the user's motivation, discipline, commitment, progress, improvement, decline, wellbeing, or equivalent person-level meaning; treating a gap in records as evidence that something did or did not happen; treating repetition as confirmation.
- **Lawful response boundary:** frequency is not evidence and absence is not negative evidence. A gap in records means only that the room holds no record. Surface what is recorded, as recorded; assert no trajectory; convert no absence into a claim, warning, recommendation, restriction, or prompt. Silence is not converted into a negative claim at any layer.
- **Doctrine anchor:** W1-D3 §5.5 (*"No layer may ever convert silence into a negative claim"*); W1-D3 §8.5 and §8.7; W0 Law 8; W0 §1 and §2 non-goal 5; W0 Law 1; ADR-0019.
- **Meditation-specific because:** W0 §5.4's own Bridges paragraph names *meditation streaks* as its worked example of what the Wing does not do — the constitution anticipated this room's temptation inside this room's own section. No reviewed source authorises Meditation to assess motivation, discipline, or progress.
- **Note:** a gap between records is **not** a freshness state; section 5 governs.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B5 — Library or text choice → religion, belief, or identity inference

- **Forbidden system move:** deriving a religion, religious identity, belief, faith, affiliation, adherence, worldview, or comparable identity attribute about the user from what they choose to read, open, store, curate, or annotate in their #16 library, or from the pattern of those choices — including recording such an attribute, acting on it, carrying it into later interactions, or letting it change what the room offers.
- **Lawful response boundary:** **content choice is not identity.** A user opening, holding, or annotating material establishes that they chose to engage with that material and nothing further. The library is the user's own curation; their annotations are their own records. The room may hold the material and, under M2 at the user's initiation, help them engage with it; it may not conclude anything about the person from the presence of the material. Where an identity characterisation is requested, decline it and state the limit. No persistent tradition attribute exists to record, and none is created.
- **Doctrine anchor:** W0 §5.4 (*"if the user chooses"*; *"hold a user-curated library"*); W1-D1 #16 (*User-curated*); W0 §9 and W0 §5.4 (contemplative and religious data as a maximally sensitive category in its own right); W0 Law 8; ADR-0019.
- **Meditation-specific because:** this is the only room holding material whose subject matter is a tradition, and therefore the only room in which a content choice could be mistaken for a declaration about the person — in a domain where the user has said nothing.
- **Preservation note:** this bait constrains **inference from** the library. It does not narrow the library: the user-curated teaching or scripture library remains authorised under W0 §5.4 and #16.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B6 — Practice → spiritual-attainment or moral verdict

- **Forbidden system move:** converting the user's practice — its occurrence, duration, consistency, modality, reported experience, or the content of their reflections — into a claim of spiritual attainment, advancement, depth, stability, purity, virtue, moral quality, worthiness, or equivalent status about the person; ranking, grading, or comparing practice; describing a practice or a person as advanced, deepening, regressing, or insufficient; or carrying such an assessment silently into how the room responds.
- **Lawful response boundary:** the room holds practices and the user's own words, and reaches no verdict about the person in any register — psychological, spiritual, or moral. Where an assessment is requested, decline it, state that the room does not assess practice or practitioner, and remain available for the practice itself. Assert no scale, no direction of travel, and no standard against which the person is measured.
- **The self-description distinction:** **no reviewed source authorises Meditation, or the system, to mint, promote, or treat as authoritative a spiritual-attainment or moral-status conclusion about the user.** A **user's own self-description may remain their #15 User-reported reflection** — a person may write in their own words about their practice, their sense of progress, or their moral or spiritual life, and nothing forbids them doing so. What is forbidden is the system converting such a record, or any practice data, into **its own verdict, authority state, or system-confirmed status**.
- **Doctrine anchor:** ADR-0019; W0 Law 3; W0 Law 8; W0 §1 and §2 non-goal 5; ADR-0002; W1-D3 §8.6.
- **Meditation-specific because:** the risk arises from #14 and #15 together and exists in no other room's jurisdiction.
- **Note:** **no spiritual-progress ontology is established, even in order to prohibit it** — no stage, level, attainment, milestone, criterion, or practice-to-state mapping is named here.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

### MED-B7 — Absent-edge or cross-room-context reliance

- **Forbidden system move:** the room obtaining, importing, retrieving, requesting, inferring, reconstructing, relying on, or behaviourally acting on Profile, health, food, fitness, or any other room's context through an edge that does not exist — including treating a user's request, instruction, or consent as permission to create such an edge, widen a grant, or reach otherwise unreachable context. The silent case is included: behaviour that changes because such context was reached or reconstructed is a breach whether or not anything is said.
- **Lawful response boundary:** the complete edge list is M1–M2; **no inbound Profile or cross-room read edge exists**, and no grant type exists that could authorise one. Where a request would require unreachable context, decline the crossing, state that this room has **no authorised Profile or cross-room health, food, fitness, or other-room context and no route by which to retrieve any**, and continue within authorised context. Reconstruct nothing from what the room does hold; assume nothing in place of what it cannot reach.
- **User-authored free text remains lawful.** This bait does **not** prohibit, restrict, discourage, flag, or degrade the user's own #15 reflection because their words mention their body, health, medication, food, movement, sleep, or any other subject. The user writes what they wish; **their words remain their own CM record, User-reported**, and they do **not** become Profile context, do **not** become confirmed health context, do **not** create an inbound edge, and do **not** authorise retrieval of or reliance on another room's data. The room neither censors the record nor treats its subject matter as a governance event, and it must not treat a topic mentioned in a reflection as though it were confirmed context it may act on. **The writing is lawful; the reaching is not.**
- **Doctrine anchor:** W1-D1 §5 and the forbidden-edge table; W0 §5.4 (*"receive health, food, or fitness data by default"*); W0 Law 9; W0 Law 4; W1-D2 §2; ADR-0018; ADR-0019.
- **Meditation-specific because:** this room's complete edge list contains **no inbound Profile or cross-room read edge of any kind**, so there is no granted cross-room or Profile edge that could be over-read; the only available failure mode is **manufacturing access** to context that has no authorised channel.
- **Classification:** review-only for bait aptness; fixture and runtime deferred.
- **Future fixture:** Exactly one future evaluation-fixture reference is required for this bait. Identifier syntax and fixture format are deferred to W4-D6. No fixture currently exists or is implied.

---

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

### 5.1 Meditation's structural instantiation

**This room's instantiation is structurally different, and says so.** Meditation relies on **no health context** — M1–M2 is its complete edge list — and **the shared table above applies only to its own records' freshness.**

**No live safety-relevant Profile context exists as a governed Meditation input.** The safety-relevant set is W1-D3 §6.3's, verbatim: *"a safety-relevant item (allergy, medication, condition, injury)"*. Each is a Profile item reachable only through an inbound Profile read edge, and this room has none. Rows 3 and 5 of the shared table therefore have **no live instance here**. That a user's own reflection may mention any subject does not alter this: a #15 record is the user's own CM record at User-reported authority, and it is neither Profile context nor confirmed health context.

**Absence of a safety-relevant staleness case is not absence of risk.** This room's primary risk surface is **Law 8 inference and Law 9 structural isolation and outward signalling** — addressed in sections 4 and 8, not here.

### 5.2 No CM review schedule exists

Verified against live sources at drafting:

- **No source-authorised CM review interval exists.**
- **No CM renewal grace period exists.**
- **No CM hard limit exists.**

Therefore:

- **A date is not a freshness state.** A record carrying the date it was made is not thereby *Current*.
- **#14, #15, and #16 do not become *Current*, *Review due*, *Stale*, or *Expired* through age alone.** No such transition is authorised, and none is created here.
- **Bibliographic or source age is not W1-D3 freshness.** The era, edition, or origin of material a user keeps in their library is a property of that material, never a staleness state of the record.
- **This contract mints no CM interval, grace period, or hard limit.**

**Zero current Meditation-specific room-register strings are derived.** Room-register wording may realise the shared rule only where the source permits wording; where no state has an authorised trigger, there is nothing to realise, and manufacturing wording would mint the very transitions no source authorises. **This zero is a current, source-derived finding — not a permanent claim about all future Meditation doctrine.** If a later accepted source explicitly creates a CM freshness transition, this section is revisited then, through that record's own ceremony.

The future governed string catalogue dependency stands, with **zero Meditation strings currently routed to it**.

### 5.3 Inherited, not owned

Two W1-D3 open questions are carried here in their **inherited, upstream status**. Neither is a Meditation-owned open decision, and **no W1-D3 amendment is required to land this room.**

**Verbatim quotation (W1-D3 §10.1):**

> 1. **Default review intervals by data type.** Medications, allergies, conditions, injuries, preferences — each needs a number and a grace period. Deserves a short, focused decision record with clinical-adjacent input.

**Verbatim quotation (W1-D3 §10.6):**

> 6. **Block vs warn.** Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor).

**Verbatim quotation (W1-D3 §6.4), the paired floor clause:**

> 4. **Whether staleness ever hard-blocks room functionality** (rather than warns and degrades) is left open (§10.6) — but the floor is fixed here: no room may present stale or unknown health context as stable truth, ever.

This contract resolves neither question and recommends no answer to either.

---

## 6. Processing boundary

**Reference:** W1-D1 §5, *Meditation Room (complete edge list)*, edge **M2**; W1-D1 §5, E11 rule.

**Verbatim quotation (W1-D1 §5):**

> - **M2. Meditation Room (scoped content) → Z3, user-initiated only.** E.g., the user asks for help engaging with a text or reviewing their own reflections. Processing disclosure event; CM payload; nothing persists outside the room; no output may be written to any other room.

**Verbatim quotation (W1-D1 §5, E11 rule):**

>   - **M2** remains the only Meditation Room processing edge; **E12** remains reserved.

**Reference:** W1-D2 §2, grant types.

**Verbatim quotation (W1-D2 §2):**

> | **AI processing disclosure** | E11-W, E11-K, E11-G, M2 | Single-task default; session maximum | Per ADR 0001. Always user-initiated. M2 grants additionally bind to the Meditation Room's no-output-elsewhere rule |

**Processing declaration.** Meditation's only processing edge is **M2**. It is **user-initiated only**; it carries **scoped CM content**; it is a **processing disclosure event**; its grant is **single-task by default with a session maximum**; **nothing persists outside the room**; **no output may be written to any other room**; and **no M-derived metadata appears in any other home**. Meditation is not an E11-family room, and no E11-family edge substitutes for M2. **E12 remains reserved.** No grant type exists for a Meditation Room bridge, because no such edge exists.

**Architectural isolation.** This room instantiates the **uniform architectural-isolation standard** of ADR-0017, on the same terms as every other room: each room's processing interaction occurs in a context that has never contained another room's content; cross-room content is **unreachable, not merely forbidden**; **one processing grant binds exactly one room**, and the processing context derives from the grant; no interface accepts content from two rooms; processing state is not reused across rooms; and filtering or output controls alone are insufficient. **This is a declaration of the required property, not a claim that operational enforcement exists** — realisation belongs to a later phase, and no mechanism, adapter, session, or payload machinery is specified or implied here. No Meditation exception to the isolation standard is created. The room's additional outward-signal prohibition is instantiated in **section 4**, not here.

**M2 output is assistance, not source material.** Discussion generated under M2 from a user's #16 material **remains AI assistance**. It **must not be represented as part of the user's source material, or as authoritative source text, merely because it discusses that material**. Nothing produced under M2 becomes active, authoritative, or persistent working context without the user's own review. This contract mints **no canonical-authority state, no bibliographic-provenance state, no translation-authority state, and no scripture-authority state**; the source-and-authenticity distinction is carried as a **review-only risk** at section 9.

---

## 7. Speech rules

**The room speaks about its records, not about the person.** It may speak of what a record says, when it was made, that it is the user's own, and what the room does and does not hold. It does not describe the user's body, condition, state, character, or standing. A sentence whose subject is the record cannot overclaim about the human, and that grammatical discipline is this room's principal speech rule.

**The user's language stays theirs.** A reflection is the user's account of their own experience. The room may hold it, retrieve it, and — at the user's initiation under M2 — discuss it with them. It does not paraphrase a reflection back as a finding, summarise it into a characterisation, or treat its subject matter as a fact the room may act on.

**When a forbidden characterisation is requested**, the room: declines to infer or confirm the conclusion; avoids repeating or strengthening the suspected pattern; states the room's lawful boundary; continues within authorised context; and **mints no claim, restriction, recommendation, warning, authority state, or status**. It offers no substitute conclusion, and it places no noticing anywhere.

**Silent practice.** Where the user has **deliberately chosen a silent or no-guidance practice**, the room **does not add unsolicited narration** — that is the user's current instruction, and the Wing does not push. This is a consequence of that instruction and of Law 1; it is not a general rule that the room stays silent, and it neither creates nor implies a universal silence doctrine.

**No outreach.** The room never initiates contact and **does not send unsolicited prompts, reminders, nudges, re-engagement messages, or other outreach**. It remains available when the user initiates the interaction. This clause governs unsolicited outreach only: guidance the user has asked for — including instruction offered within a guided practice they chose — is lawful inside an authorised session and is not restricted here.

**Governed strings are not authored here.** Final user-facing wording and any catalogue identifiers belong to the later governed string catalogue; this section fixes the semantic requirements only, and this room currently routes no strings to it.

---

## 8. Forbidden list

Named for emphasis, though default-deny already excludes every item. The edge set asserted here is identical to the set asserted in section 2.

**Edges and flows.** The Meditation Room may not:

- hold or use any edge beyond **M1 and M2**;
- obtain, import, retrieve, request, reconstruct, or rely on Profile, health, food, fitness, or any other room's context through an absent edge, or treat a user request as creating or widening one;
- write, send, or signal outward to any room, home, agent, or adapter;
- place M-derived metadata in any other home;
- influence another room's behaviour, selection, ranking, framing, or omission on the strength of anything known only here;
- hold a vendor, adapter, connector, publisher, or external-service edge of any kind;
- construct or operate a bridge to another room absent its own separate, explicit, user-created, revocable decision record;
- read the Health Vault, the Draft Profile, or the Approved Profile.

**Noticings and records.** The room may not:

- create a pattern-flag, "for review" queue, or any other pathway for an out-of-authority noticing — **the absence of such a pathway is deliberate architecture, not a missing feature**;
- store a persistent preference, setting, or profile of the user's practice choices;
- mint an authority label, authority state, freshness state, review interval, grace period, or hard limit;
- write a movement, rest, recovery, or sleep record, or acquire that category by any route.

**Content supply.** The room holds a **user-curated** library under #16 and may help the user engage with their own material under M2. The following remain **deferred and are not authorised by this contract**:

- room-initiated external fetching;
- third-party canonical-content ingestion;
- room-supplied translations;
- room-curated tradition collections;
- external publisher or source feeds;
- a formal bibliographic or source-provenance regime.

**This exclusion is about content supply, not about the library.** It does not narrow, condition, or defer the user-curated teaching or scripture library that W0 §5.4 and category #16 already authorise. Deferred items are future surfaces of this room, awaiting their own authority; none is created, promised, or designed here. **This contract makes no copyright or licensing determination**, and none of the above should be read as one.

**Conclusions about the person.** The room may not manufacture a mental, emotional, behavioural, psychological, spiritual, moral, or health conclusion about the user from practice, reflection, library content, frequency, or absence — see section 4, whose seven baits are a floor and not a ceiling.

**Engagement mechanics.** The room may not operate streaks, streak pressure, guilt mechanics, leaderboards, competitive comparison, escalating practice targets, calmness scores, spiritual-progress scores, practice-performance scores, "more minutes is better or healthier" framing, productivity-optimisation claims, adherence tracking against targets, or any re-engagement or behavioural-nudging mechanic. Every item here restates existing law; none is new doctrine, and if the user asks for such a mechanic the room declines that mechanic specifically and remains otherwise available.

---

## 9. Validator hooks

Every governed term below carries exactly one classification. No term is left in the ambiguous middle; compound terms are decomposed so that a mechanical part and a judgement part are never bundled.

### 9.1 Mechanically checkable

- **Contract identity and section structure** — one room identity; eleven sections present, in fixed order, under fixed numbering, each non-blank.
- **"Not applicable" carries a reason** — presence of non-empty reason text at §2.1 (adequacy of that reason is review-only, below).
- **Open-questions section** — present; where empty, body matches the exact accepted wording.
- **Validator-hooks completeness** — every governed term in this section carries exactly one classification.
- **Scope integrity** — every exact reference in sections 2, 3, 5, and 6 resolves, and every verbatim quotation matches its cited source text.
- **Load-bearing words present; source-backed blur-words absent** in every scope clause.
- **Shared-table fidelity** — the ADR-0020 quotation at section 5 is intact; all six states present; the rejected pause phrase absent; inherited §10.6 wording unaltered.
- **Named-bait mapping — declaration only** — seven baits present, each with exactly one declared future evaluation-fixture reference, none with zero and none with multiple.
- **Placeholder mechanics** — placeholder tokens, where any are used, drawn from the canonical set; rejected tokens absent.
- **Cross-reference coherence** — dependency identifiers and source paths resolve; the isolation clause at section 6 cites its record.
- **Anti-map consistency, and the exact Meditation edge set** — the forbidden list at section 8 intersects no granted edge, and **this contract asserts its complete edge list exactly: M1 and M2, in section 2 and section 8 alike, with no divergence between them.**
- **Catalogue-identifier dormancy** — no catalogue-identifier check is claimed active; this room routes zero strings and the class stands dormant with its named dependency.

### 9.2 Review-only

- **Named-bait substantive completeness and aptness** — no artefact enumerates the full risk space; Law 8 and Law 9 bind beyond the enumeration.
- **Whether each bait captures its intended risk without becoming an inference engine**, and the realistic-pairing risk.
- **Spiritual-association realism risk** — whether any bait wording could teach a practice-to-spiritual-state association. This risk is specific to this room and has no precedent in the accepted corpus.
- **Doctrinal adequacy of the §2.1 "Not applicable" reason.**
- **Identity and purpose fitness** (§1).
- **Speech-rule application quality** (§7), including whether the silent-practice rule stays bounded to the user's own instruction rather than generalising.
- **The transient-choice versus persistent-preference line** (§3.2) — whether the boundary holds in practice as written.
- **Content-supply boundary wording** (§8) — in particular, whether the exclusion can be read as narrowing the authorised user-curated library.
- **Source-and-authenticity risk** (§6) — whether generated M2 discussion could be taken for the user's source material, canonical text, translation, or authoritative teaching.
- **The zero-string derivation** (§5.2) — whether the derivation is sound and whether zero remains correct.
- **Constitutional-explanation soundness** (§10).
- **Semantic scope expansion or authority minting beyond literal identifiers.**
- **Completeness of behavioural prohibitions.**
- **Runtime obedience, operational isolation, and runtime forbidden inference** — not repository artefacts; later-phase evaluation territory.
- **Any clinical, diagnostic, medical, or therapeutic judgement** — never machine-decided, and never decided by this project's validators at all.

**No validator and no fixture exists.** Every mechanical class above is a *definition* of what would be checkable; its per-contract execution is gated to a later authorised unit, and human review after any mechanical pass is always required. This contract declares no fixture identifier, no fixture format, and no catalogue identifier.

---

## 10. Constitutional check

- **Law 1 — Initiation.** The room waits. It does not initiate unsolicited prompts, reminders, nudges, re-engagement messages, or other outreach; guidance inside a user-initiated practice remains governed by the user's chosen session. The silent-practice rule at §7 is an application of the user's own instruction, not an exception.
- **Law 3 — Nothing self-promotes.** M2 output is assistance at birth and assistance thereafter (§6); nothing the room generates becomes authority without the user's review.
- **Law 4 — Minimum necessary access.** The room's access is its own records under M1 and a scoped, user-initiated CM payload under M2; there is nothing else to receive.
- **Law 6 — The clinical line.** No diagnosis, treatment, or clinical framing arises anywhere in this contract, including around breath (§3.1) and around rest (§3.3).
- **Law 8 — No inferred conditions.** Implemented in §4's general rule and seven named baits, and in §8's conclusions clause; W0 §5.4 applies Law 8 to this room *with full force*.
- **Law 9 — The Meditation Room stands apart.** Implemented as the shortest edge list in the map — M1 and M2, nothing else (§2, §8) — and as the absolute outward boundary at MED-B3.
- **Law 11 — The user owns the data.** M1 is a right, not a grant (§2.2); the user's access to their own records is never consent-gated.
- **Law 13 — Auditability.** M2 grants and their disclosure events are ledger entries; the ledger records activity and is never input to processing.

**This contract introduces no new authority.** It creates: **no new edge**; **no new category**; **no new sensitivity class**; **no new authority state or label**; **no new freshness state**; **no CM review interval, grace period, or hard limit**; **no new grant type**; **no source-provenance or canonical-authority regime**; **no external content edge**; **no preference category**; **no fixture, validator, or catalogue identifier**; and **no implementation authority**. It proposes and requires **no W1-D1 amendment** and **no W1-D3 amendment**. No law required reinterpretation, and no amendment to the Constitution is proposed or required.

---

## 11. Open questions

None at acceptance.

---

*A contract is the room's laws gathered into one place, in the exact accepted words. The Meditation Room may hold a person's practice, the words they write about it, and the books they chose to bring — and it may never turn a quiet week into a verdict, a reflection into a diagnosis, a chosen text into a declared belief, or a practice into a measure of the person.*
