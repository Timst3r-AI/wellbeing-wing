# 0027 — Safety-Relevant Set Reconciliation and Freshness Coverage

**Status:** Accepted by human reviewer, 2026-08-14. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** none — this record reconciles inherited definitions rather than constituting deliverable content
**Decision mode:** reconciliation. Accepted sources use high-stakes / safety-relevant vocabulary with four different memberships. This record establishes what each governs, where the differences are lawful scope and where they are unresolved overlap, and how freshness coverage must be reconciled.
**Constitutional references:** W0 §7 (review-fatigue controls); W0 Laws 6, 7, 11, 12. No law is amended.
**Follows:** **ADR 0026**, which corrected ADR 0002's false identity claim on 2026-08-14 and deliberately left the layering question to this record.
**Blocks:** DR-W5-02, which cannot express runtime consequence for *expired safety-relevant* items until it knows which items those are. **The block lifts on this record's publication and independent remote verification; from that moment DR-W5-02 owns the composition question of decision 5 alongside its existing freshness decisions.**

---

**Four accepted records reach for the same idea and hold four different lists. Three of the differences are scope doing its job. One leaves a composition question: at room surfaces, two accepted mechanisms operate over different memberships, and no accepted record states how they interact for items covered only by one. Underneath all of it, two items the Constitution calls high-stakes have no way to become stale at all.**

## Decision question

**What does each accepted use of "safety-relevant" and "high-stakes" govern; where are the differences lawful scope and where are they unresolved overlap; and how must freshness coverage be reconciled so that no high-stakes item lacks a lawful decay-and-unknown path?**

## The source comparison, verbatim

| Source | Term used | Members | Count | Its own stated purpose |
|---|---|---|---|---|
| **W0 §7** | *"High-stakes fields"* | allergies · medications · diagnoses/conditions · pregnancy status · clinician instructions | **5** | A **review-fatigue control**: *"High-stakes fields require individual confirmation, one item at a time"* — governs **approval**, under "Review-fatigue controls (binding)" as item 2 |
| **W1-D3 §6.3** | *"a safety-relevant item"* | allergy · medication · condition · injury | **4** | **Room consumption**, inside a section whose preamble reads *"Rooms read approved sections only through their D1 edges (E6, E7)"* — i.e. **Kitchen and Gym** |
| **W1-D3 §10.7** | *"high-stakes confirmations"* | allergies · medications · pregnancy status · clinician instructions | **4** | **Re-authentication at review time** — an open question, not a decided set |
| **ADR 0002** | *"Safety-relevant"* | allergies · medications · diagnosed conditions · injuries · pregnancy status · clinician instructions | **6** | **The Wing's surfacing ladder** — which context escalates to L2 or L3 |
| **ADR 0020** | — | adopts **W1-D3 §6.3's, explicitly and verbatim** | 4 | The shared behaviour table carried by **every room contract (W4-D2 – W4-D5)** |

**No two of the four independently-authored lists are identical.** W0 §7 excludes injuries. W1-D3 §6.3 excludes pregnancy status and clinician instructions. W1-D3 §10.7 excludes conditions and injuries. ADR 0002 includes all six.

**Adoption is lopsided.** W1-D3 §6.3's four is quoted verbatim by ADR 0020, the Wellness room contract and the Meditation room contract, each stating that no new category list is invented. W0 §7's five and ADR 0002's six are each used only inside their own record. **The narrowest list carries the most downstream weight.**

**And the four-member list has already travelled beyond the scope it was written for.** W1-D3 §6 governs Kitchen and Gym by its own preamble; the Wellness contract nonetheless applies it, reasoning in terms: *"Because E5 can display §6.3 safety-relevant items (allergy, medication, condition, injury), the always-show and acknowledge-before-continuing rules are live for Wellness."* That extension is lawful — ADR 0020 and the contract are accepted and explicit — but it means **the list now governs a room its source section did not address.**

## Controlling law

- **W0 §7, review-fatigue control 2** — the high-stakes list, whose stated mechanism is individual confirmation during section-by-section approval. **W0 §7 has no numbered subsections; the corpus addresses this material as "W0 §7", and ADR 0026 forbids "sharpening" the pointer.**
- **W0 §7** — the Health Profile Agent *"may not … override, reinterpret, or editorialise on clinician advice found in records."*
- **W1-D3 §6** — *"Room consumption rules"*, scoped by its preamble to E6 and E7; **§6.3**'s four-member set and most-protective framing as *"a display and framing rule — it never becomes diagnosis, inference, or a new recorded claim."*
- **W1-D3 §6.4** — the floor: *"no room may present stale or unknown health context as stable truth, ever."*
- **W1-D3 §10.1** — *"Default review intervals by data type. Medications, allergies, conditions, injuries, preferences — each needs a number and a grace period."* The five types exist **only** here, inside an open question.
- **ADR 0002** — the L0–L3 ladder; its six-member definition; Doctrine 3's single permitted block; its per-case table including the Kitchen/Gym row; its statement that the set is *"fixed small to start"*; its rule that *"the safety-relevant set's L3 behaviour and the L0 honesty floor are not configurable"*; and **its open question 3: *"The safety-relevant set's governance — who proposes extensions, and does extension need clinical-adjacent input?"***
- **ADR 0020** — adopts §6.3's set verbatim, *"no new category list is invented"*; its always-shown rule for the safety-relevant set; **blocks the behaviour section of every room contract**; leaves §10.6 open.
- **ADR 0025** — safeguard 14's fail-closed condition fires on an *uncertain safety-relevant fact*; safeguards may not be silently relaxed.
- **ADR 0026** — corrected ADR 0002's identity claim; **explicitly did not adjudicate membership and did not decide which set governs which layer**, reserving both to this record.
- **W1-D1 §5** — *"E5. Approved Profile (scoped sections) → Wellness Room display"*; *"E6. Approved Profile (allergies, confirmed dietary requirements only) → Kitchen"*; *"E7. Approved Profile (confirmed injury/physical notes only) → Gym."*

## Decision

### What the sets are

1. **There is no canonical universal safety-relevant set, and none is created here.** Collapsing the lists into one would either over-trigger approval friction or under-protect surfacing, and would discard reasoning each source did deliberately.

2. **The sets are scoped by governance function, and each is non-transferable.** A record citing "the safety-relevant set" must say which one and for what purpose. **Membership of one set never implies membership of another**, in either direction.
   - **W0 §7 governs the individual-confirmation set at approval.** It answers *which fields the user must confirm one at a time*. It is a review-fatigue control and says so.
   - **W1-D3 §6.3 governs the room-consumption set**, within §6's own scope — *"Rooms read approved sections only through their D1 edges (E6, E7)"*, the Kitchen and the Gym. Its membership tracks what those edges deliver: allergies and confirmed dietary requirements via E6, confirmed injury and physical notes via E7.
   - **ADR 0002 governs the Wing's surfacing ladder** with its six-member set.
   - **W1-D3 §10.7 is an open question**, not a decided set, and is **not an accepted fourth authority.**

3. **ADR 0026 settles nothing about membership, and must not be read as if it did.** It corrected a false provenance claim and states in terms that ADR 0002's six-member set *"is not adjudicated by this correction and is not changed."* **Nothing in this record treats ADR 0026 as validating, endorsing or ratifying the six.**

### The composition question this record does not answer

4. **ADR 0002's Kitchen/Gym row is not a general room-layer delegation, and an earlier draft of this record was wrong to read it as one.** The claim is withdrawn, on two independent grounds read from the accepted text:
   - **It is textually bounded.** The row's state column reads *"Kitchen / Gym room-level uncertainty"* — two named rooms. It says nothing about Wellness or Meditation. And the section it points at, W1-D3 §6, is itself scoped to E6 and E7. The alignment is exact, and it is an alignment of **two bounded things**, not evidence of a general rule.
   - **It is a framing citation, not a membership delegation, and ADR 0002 proves this itself.** ADR 0002 cites §6.3 in exactly two places. The second is **L3's own Form column**: *"the output then carries most-protective framing (D3 §6.3)."* That citation governs L3 for **ADR 0002's own six-member set**. If citing §6.3 imported §6.3's membership, L3 would silently shrink from six members to four — contradicting the six-member definition printed two lines above it. **The citation therefore carries the framing rule, not the list.**
   **What the row therefore settles is narrow: at the Kitchen/Gym layer, most-protective framing is governed by §6.3. It settles nothing about how the two mechanisms compose.**

5. **A residual composition question survives, and is reported rather than smoothed away.** Two accepted mechanisms operate over different memberships, and both are live in a room:
   - **ADR 0002's L2/L3 surfacing mechanism**, over its **six-member** set, wherever the Wing surfaces — rooms included;
   - **ADR 0020's always-shown inline uncertainty mechanism**, over §6.3's **four-member** set, carried by **every room contract**.
   Four members are common to both. **Pregnancy status and clinician instructions are present only in ADR 0002's six**, so for those two items the always-shown room mechanism has no instance while the L2/L3 mechanism does.
   **The open question is how the two mechanisms compose for such items** — what a room does when the surfacing ladder is engaged over an item the room's own always-shown rule does not cover. **This record states neither precedence nor supersession, and names no winning set.** Both mechanisms remain accepted, in force, and unamended; what is undecided is their interaction, not their validity. **This record names the question and assigns it; it does not answer it.**

### The coverage gap

6. **Two high-stakes items have no lawful ageing-based freshness path.** The five freshness data types — medication, allergy, condition, injury, preference — exist only inside W1-D3 §10.1's open question. **Pregnancy status and clinician instructions are not in that list and appear in no other accepted freshness taxonomy.** Re-verified against current authority on 2026-08-14: **ADR 0026 changed neither fact.**
   The consequence is concrete: **they can never become review-due, stale, or expired.** ADR 0002 assigns *expired safety-relevant* items to L3 and treat-as-unknown — **and for these two the antecedent can never become true through ageing.** ADR 0025 safeguard 14 fires on an *uncertain safety-relevant fact* — **and for these two that uncertainty is unreachable by ageing.**
   **Pregnancy status makes the gap especially visible.** W0 §7 requires it to be individually confirmed; ADR 0002 places it at L3 when expired or unknown; and W1-D6's required failure example 7 is built on it. **Under current freshness coverage, however, ageing can never make it expire.**

7. **The gap is recorded as owned and is not closed here.** Closing it requires deciding whether pregnancy status and clinician instructions receive freshness coverage as data types, through another mechanism, or by an explicit governed decision that they do not decay. **This record does not extend the taxonomy, does not map either item into `condition`, `preference`, or any other existing category, and invents no mechanism.**

8. **A compounding finding, reported not resolved: "freshness data type" has no accepted definition.** The phrase returns **zero occurrences** across the corpus; the five types appear only as a list in §10.1's open-question prose and match no entry in W1-D1's category inventory. **Deciding whether pregnancy status is "a data type" is therefore currently undecidable against the corpus.**

### Preserved findings

9. **An ADR 0002 L3 acknowledgement is not a renewal and resets no freshness clock.** ADR 0002 records the acknowledgement and permits proceeding with degraded claims; W1-D3 §2 and §8.2 make renewal a review act that no acknowledgement can substitute for. **The two mechanisms meet at the same runtime moment and must never be conflated.** Carried forward for DR-W5-02 to state explicitly.

10. **ADR 0025 safeguard 14 is untouched and unweakened.** Nothing here narrows the fail-closed condition; decision 6 widens the territory over which it should one day be reachable.

11. **ADR 0002's open question 3 is partly answered and partly left open.** *Who proposes extensions* and *whether extension needs clinical-adjacent input* remain open; what is settled is that there is no single set to extend — extensions are proposed against a named, scoped set.

## Alternatives considered

- **Name the scoped sets, report the residual composition question, and record the coverage gap (chosen).** Changes no membership, resolves only what the accepted text supports, and hands both unresolved items to DR-W5-02 where they cannot be lost.
- **One canonical safety-relevant set (rejected).** Requires a membership either too wide for approval friction or too narrow for surfacing, and discards deliberate reasoning in three accepted sources.
- **Reading ADR 0002's Kitchen/Gym row as a general room-layer delegation (rejected — this was the earlier draft's error).** It would resolve the overlap by inference rather than by text, and ADR 0002's own L3 citation of §6.3 disproves the membership reading. **Architectural convenience is not evidence.**
- **Treating W1-D3 §6.3's four as the canonical set (rejected).** It is the narrowest with the widest adoption, which makes it tempting; adopting it as canonical would drop pregnancy status and clinician instructions out of the L2/L3 ladder — **weakening a safety mechanism by a bookkeeping choice.**
- **Answering the composition question here (rejected).** It would decide runtime interaction inside a definitions record. **It is also unnecessary as a separate act:** DR-W5-02 already owns the runtime consequence of expired and unknown safety-relevant items, and the composition question is the same question at the same layer. **No preliminary room-scoped record is created.**
- **Declaring a precedence rule between the two mechanisms (rejected).** Naming a winner — either set, either direction — would supersede an accepted mechanism by a reconciliation of definitions, which is exactly the substitution decision 2 forbids.
- **Closing the coverage gap by mapping pregnancy status into `condition` (rejected firmly).** A semantic mapping this record has no authority to make, not obviously correct, and doing it quietly would bury a safety gap inside a taxonomy convenience.
- **Amending W0 §7 (rejected).** Nothing here requires it, and ADR 0026 already established that the citation, not the Constitution, was the thing to fix.

## Consequences

- **The lifecycle is explicit.** This record **blocks DR-W5-02 until it is published and independently remote-verified**. On publication it becomes authority, the block lifts, and **DR-W5-02 inherits the composition question of decision 5 alongside its existing freshness decisions** — thresholds, the §10.6 remainder, assertion posture, evaluation points, renewal integrity. **No intermediate record stands between the two.**
- **DR-W5-02 becomes writable on this point**: it cites W1-D3 §6.3's consumption set by name and scope for Kitchen/Gym runtime consequence, without implying anything about the other sets.
- **The corpus gains a permanent, visible statement that two high-stakes items cannot currently expire.** That is uncomfortable and correct.
- **A second unresolved item is now visible rather than latent**: how the two mechanisms compose for items only one of them covers. It was always there; the earlier draft would have hidden it behind an inference.
- **Harder, deliberately:** every future record citing "the safety-relevant set" must name which one and why; no future record may substitute one set for another.
- **No behavioural or capability consequence.** No membership changes; no mechanism is built.

## Constitutional check

- **W0 §7 unamended**; its set keeps its approval scope.
- **Law 6 untouched** — no clinical judgement is made about any item.
- **Law 7 served** — decision 6 identifies where *approved is not current* cannot currently operate at all.
- **Law 11 untouched** — nothing here gates the user.
- **Law 12 and ADR 0002's ladder untouched** — the surfacing set's membership is unchanged and unadjudicated.
- **No new authority.** No label, class, authority state, freshness state, data type, edge or grant type is minted. **No set's membership is altered.**
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not: alter the membership of any accepted set; adjudicate ADR 0002's six; create a canonical set; amend W0, W1-D3, ADR 0002, ADR 0020, ADR 0025 or ADR 0026; answer how ADR 0002's and ADR 0020's mechanisms compose, or assert precedence, supersession or a winning set between them; create any preliminary room-scoped record; extend the freshness taxonomy; define what a freshness data type is; map pregnancy status or clinician instructions into any existing category; decide whether either receives freshness coverage; weaken ADR 0025 safeguard 14; resolve W1-D3 §10.6 or §10.7; open any wider citation audit; decide surfacing wording, catalogue IDs or UI; or authorise implementation, directory, dependency, model contact, payload, transmission, harness or fixture execution. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout. The item names used — allergies, medications, conditions, injuries, pregnancy status, clinician instructions — are **the accepted corpus's own governance vocabulary**, quoted from W0 §7, W1-D3 §6.3 and ADR 0002. **No named drug, diagnosis or allergen appears; no clinical example is given; no statement is made about any person.** No model or vendor names, no private names, no URLs, no project lineage beyond this repository.

## Dependencies

W0 (§7, its clinician-advice prohibition, Laws 6, 7, 11, 12); W1-D1 (§5's read edges; the category inventory); W1-D3 (§2, §6, §6.3, §6.4, §8.2, §10.1, §10.6, §10.7); ADR 0002 (the ladder, its set, its per-case table, Doctrine 3, open question 3); ADR 0003 (ceremony); ADR 0020 (the shared table, the adopted set, the always-shown rule); ADR 0025 (safeguard 14, the provisional discipline); **ADR 0026 (the published citation correction this record follows)**; and the W5 runway.

## Open questions

1. **How ADR 0002's six-member L2/L3 surfacing mechanism composes with ADR 0020's four-member always-shown room mechanism** for items present only in the former — pregnancy status and clinician instructions. **Owner: DR-W5-02.** No precedence, supersession or winning set is asserted here, and **no preliminary room-scoped record is created or required.**
2. **Do pregnancy status and clinician instructions receive freshness coverage, and how?** **Owner: DR-W5-02**, which must decide coverage, an alternative mechanism, or an explicit governed decision that they do not decay.
3. **What is a freshness data type?** No accepted source defines one. **Owner: DR-W5-02.** Question 2 cannot be answered rigorously before this one.
4. **ADR 0002's open question 3 remainder** — who proposes extensions to a scoped set, and whether extension needs clinical-adjacent input. **Owner: unassigned**; ADR 0025's finding that clinical-adjacent input is unavailable bears directly on it.
5. **Whether W1-D3 §10.7's re-authentication list should be reconciled** when that open question is taken up. **Owner: whichever record resolves §10.7.**

---

*Most of the disagreement turned out to be the corpus doing its job — different lists for different functions. One piece of it was not, and the earlier draft of this record had quietly resolved it by inference. Removing that inference put the real question back on the table, alongside the older one: why a field explicitly governed at approval, surfacing and failure-evaluation layers still has no lawful path by which ageing can make it stale.*
