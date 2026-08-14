# 0029 — Runtime Freshness and Unknown/Stale Behaviour (DR-W5-02)

**Status:** Accepted by human reviewer, 2026-08-14. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D1**
**Position:** the **second of the seven original W5-D1 decision records**. It creates no additional deliverable, no additional planning slot, and no eighth record identity.
**Decision mode:** one governed record in two parts — **Part A: Freshness semantics** · **Part B: Runtime consequence**. The parts are internal organisation, not two records.
**Constitutional references:** W0 Laws 1, 6, 7, 11, 12, 13; W0 §7 (review-fatigue controls, and the clinician-advice prohibition). **No law is amended.**
**Follows:** ADR 0025, which made this record writable and constrains it by ten safeguards; **ADR 0027**, whose publication lifted the block on this record and which assigned it the composition question, freshness coverage, and the definition of a freshness data type.
**Resolves:** **W1-D3 §10.1** (default review intervals by data type) and **W1-D3 §10.6** (block versus warn) — the two questions W5-AR §6.1 and §6.2 assign to this record. **Registry `resolves` identifiers to be confirmed at landing-scope time; W1-D3's open questions may carry no registered ids.**

---

**Time is the only thing in this Wing that changes a label by itself, and until now it had no numbers to change them by. This record supplies the numbers, says plainly that they are placeholders, and fixes what a room may and may not do when the ground under an answer has gone soft. It blocks no person and closes no room. It withholds exactly one thing: the Wing's own claim that something uncertain is settled.**

## Decision question

**What makes profile context stale, and what may a runtime do about it?**

Concretely, the two questions W1-D3 sealed open and W5-AR assigned here: **§10.1** — what review intervals apply, per data type, and what a *data type* even is; and **§10.6** — whether expired safety-relevant context may ever hard-block a room function, or must always warn and degrade.

## Controlling law

- **W0 Law 7** — *approved is not current*. This record is that law's arithmetic.
- **W0 Law 1** — the Wing holds; it does not push. No freshness work reaches outward.
- **W0 Law 11** — the user is never queued behind their own system.
- **W0 Law 6 and W0 §7** — no clinical judgement, and no overriding, reinterpreting or editorialising on clinician advice found in records.
- **W1-D3 §2** — the label semantics, and the two structural rules: staleness transitions are **the only automatic transitions**, downward only; and **"renewal is a review act, not a refresh."**
- **W1-D3 §5.5** — absence is never negative evidence; consumers receive a confirmed negative **or** unknown.
- **W1-D3 §6** — room consumption, scoped by its own preamble to *"their D1 edges (E6, E7)"*; **§6.3**'s four-member set and most-protective as *"a display and framing rule"*; **§6.4**'s floor: *"no room may present stale or unknown health context as stable truth, ever."*
- **W1-D3 §7** — intervals **per data type, not globally**; the five re-review triggers; renewal prompts as **internal flags surfaced at next relevant use**, batched for review fatigue.
- **W1-D3 §8.2** — no silent refresh, re-date or re-confirm. **§8a** — D3 records are C0 governance metadata with no processing edges.
- **ADR 0002** — the L0–L3 ladder over its six-member set; **Doctrine 3's single permitted block**: *"Nothing in this doctrine blocks the user… What can be 'blocked' is exactly one thing: the Wing presenting unsound data as settled truth"*; Doctrine 4's user-initiated fence; the language law; no escalation-on-noncompliance.
- **ADR 0020** — the shared behaviour table; always-shown inline uncertainty for §6.3's four; *"no new category list is invented"*; §10.6 left open.
- **ADR 0024** — structural, content-free refusal that *"echoes no refused content and writes no user, room, profile, or vault state"*; four-surface observability by construction; *"absence must be demonstrated, not presumed."*
- **ADR 0025** — thresholds only as **provisional governance defaults — not clinically validated**; the ten safeguards; **safeguard 14** as a partial disposition of §10.6; provisional status never lapsing by silence.
- **ADR 0027** — sets scoped by governance function and non-transferable; no canonical set; **no membership adjudicated**; ADR 0002 and ADR 0020 both valid with **no precedence**.
- **W5-AR §6.1, §6.2** — the assignment and its four obligations, including *"neither silence nor a constant in code is available."*

---

# Part A — Freshness semantics

## A1. A freshness data type is a governance policy key

1. **A *freshness data type* is a governance policy key.** Its entire content is a freshness policy. It exists to govern freshness behaviour and nothing else.

2. **What it is not**, stated because the term would otherwise drift: **not a clinical or medical taxonomy** · **not a confidentiality or sensitivity class** (D1's classes remain the sensitivity axis, and W1-D3 §10.2's question of whether expiry should also vary by class is **not** answered here — the axis is data type alone) · **not a substitute for W1-D1's category inventory**, which it indexes rather than replaces · **and it implies nothing whatever about membership of any safety-relevant or high-stakes set.** Per ADR 0027 those sets are scoped by governance function and non-transferable; **a policy key is not a set and confers no membership.**

3. **A field receives a freshness policy without reclassifying the information itself.** Attaching a key to an accepted field states how that field ages. It states nothing about what the field means, how sensitive it is, or who may read it.

4. **There is exactly one key shape.** Every key carries **`R`, `G` and `H`**. There is no second kind of key, no threshold-free key, and no key that opts out of ageing.

5. **No per-field override exists.** A field's freshness behaviour comes from its policy key and **from nowhere else** — not from a per-field exception, not from a room, not from a call site, not from configuration outside the key.

6. **A key without a complete `R`/`G`/`H` triple is unconstructable, not merely discouraged.** This keeps every key evaluable by the accepted decay function and leaves no policy that a runtime could hold but not apply.

## A2. The ladder, and what is governed

7. **The normative governed values are `R`, `G` and `H`** — review interval, renewal grace, hard limit. **`S`, the stale boundary, is derived and only derived: `S = R + G`.** It is never governed independently and never stated as a fourth free value.

8. **The ladder, from W1-D3 §2's own semantics:**

   | Label | Condition | §2's words |
   |---|---|---|
   | **current** | `0 ≤ elapsed < R` | *"Within its review interval"* |
   | **review due** | `R ≤ elapsed < S` | *"Interval passed; renewal surfaces at next relevant use"* |
   | **stale** | `S ≤ elapsed < H` | *"Past the renewal grace period"* |
   | **expired** | `H ≤ elapsed` | *"Past the hard limit for its type"* |

   **`S = R + G` follows from §2 rather than from choice:** stale begins where the renewal grace period ends, and that period begins at review-due.

9. **A change to `G` moves `S` automatically.** No record, table, configuration or implementation may govern `S` directly, because a directly governed `S` could silently desynchronise from `R + G`. **`H` is independent of both `R` and `G`.**

10. **The engine's three absolute thresholds are implementation representation, not a competing grammar.** Where a runtime supplies `review due`, `stale` and `expired` as absolute values, `stale` there **is** the computed `S`. **This record governs semantics; representation is W5-D2's, within these semantics.**

## A3. Unit

11. **The unit is the fixed-duration day: one day is exactly 24 elapsed hours.** Not a local-calendar day, and not a calendar month.

12. **The unit is a property of the policy and of the elapsed measure — never of the decay function.** The accepted engine's decay is unit-free by construction and must stay so. **W5-D2 may choose where elapsed duration is computed and how a timestamp becomes an elapsed measure; it may not redefine what the unit means.**

## A4. The seven keys and their values

13. **The key set is complete at seven, and closed by this record:** **medication · allergy · condition · injury · pregnancy status · clinician instructions · preference.** Extending the set is a future decision record, never a runtime or implementation judgment.

14. **The values.** **Every number in this table is a `provisional governance default — not clinically validated`.**

    | Freshness policy key | `R` | `G` | *`S` = `R`+`G`* | `H` |
    |---|---|---|---|---|
    | medication | 365 | 91 | *456* | 730 |
    | allergy | 365 | 91 | *456* | 730 |
    | condition | 365 | 91 | *456* | 730 |
    | injury | 365 | 91 | *456* | 730 |
    | pregnancy status | 365 | 91 | *456* | 730 |
    | clinician instructions | 365 | 91 | *456* | 730 |
    | preference | 730 | 182 | *912* | 1460 |

    Unit: fixed-duration days. `R`, `G` and `H` are governed; the italicised `S` column is **derived and shown for reading only**.

15. **The non-equivalence rule, binding wherever these values are reproduced or summarised.** Six of the seven keys carry identical values. **Their equality is a uniform provisional governance simplification and is not evidence of clinical equivalence.** It does not assert that pregnancy status ages like a medication, that an injury ages like an allergy, or that any two of the six behave alike in any clinical or physiological sense. It asserts only that the Wing, **lacking clinical-adjacent input**, applies one placeholder interval across every key it has not been given grounds to distinguish — with `preference` the sole distinguished key, distinguished on non-clinical grounds.

16. **Every reproduction or summary of a numeric `R`, `G`, derived `S`, or `H` value must carry the exact label `provisional governance default — not clinically validated`.** A representation that reproduces or summarises values from the six equal-key policies **must also carry the non-equivalence semantic rule of decision 15**: their equality is a uniform provisional governance simplification and is not evidence of clinical equivalence. **These are semantic carriage requirements, not a prescription of user-facing copy, layout or catalogue form; W6 may govern presentation, but neither meaning may be omitted.**

17. **The published chain permits provisional threshold-setting; it validates no specific number.** ADR 0025 authorises numbers **only** as provisional governance defaults, on the express footing that clinical-adjacent input **could not be obtained**. **That is permission, not support.** No accepted record and no input gathered in this phase endorses `365`, `91`, `730`, `182` or `1460` — each a **`provisional governance default — not clinically validated`** — as correct for anything. **No downstream record may cite this record, ADR 0025, or the chain as evidence for a value.**

18. **Pregnancy status and clinician instructions are each their own key.** Neither is mapped into `condition`, into `preference`, or into any other key, and neither acquires a clinical subtype. Per ADR 0027 this changes no safety-set membership, and it adjudicates no membership.

## A5. The provisional review horizon

19. **The provisional defaults are reviewed at W5 closure, or six months after this record's acceptance, whichever comes first.**

20. **That horizon is a governance review of the defaults. It is never a clinical review cadence**, and it is never the user's review interval. One asks *"are these governance placeholders still the right placeholders?"*; the other asks *"has this person's information been reviewed?"* **Wording that could be read as the second is prohibited.**

21. **Provisional status ends only by supersession or explicit re-affirmation, never by silence** (ADR 0025). The horizon is the trigger for that act, not an expiry of the defaults: reaching it without a decision leaves the defaults provisional and overdue, never validated by default.

## A6. Evaluation points and triggers

22. **Freshness must be valid at every governed reliance on the affected item.** At minimum, it is evaluated **before the first governed reliance in each relevant user-initiated interaction**; **if an authorised re-review trigger affecting that item has arisen before a later reliance, that trigger must be consumed before the later reliance.** This record does not require evaluation once per output, does not authorise continuous evaluation, and **does not prescribe whether or how a valid result is cached or memoised** — those mechanics belong to W5-D2.

23. **There is no background polling, fetching or refreshing, and no evaluation outside a user-initiated interaction.** Law 1 and ADR 0002 Doctrine 4 both bind; this record adds no outward-reaching behaviour of any kind.

24. **All five W1-D3 §7 re-review triggers are retained, unaltered**, and apply to every one of the seven keys without exception: **interval lapse · a new Vault upload touching the section · a contradiction flag · a supersession proposal · a user request.**

25. **An event trigger may raise its flag at its own authorised event, but the flag surfaces before reliance at next relevant use.** Raising is internal; surfacing is user-initiated. This is W1-D3 §7's own shape — *"internal flags surfaced at next relevant use (Law 1 — the Wing holds; it does not push)"* — and renewal prompts remain batched to respect review fatigue.

26. **Exact code placement, storage shape, and configuration form are W5-D2's**, within these semantics.

## A7. Acknowledgement is surfacing only

27. **An acknowledgement is surfacing only and never renewal.** It **writes no review timestamp** and changes **no freshness state, no authority label, no provenance, no contradiction flag, no supersession link, and no pending-review state.** The list is exhaustive by intent: a narrower statement would leave the remaining states arguable.

28. **The acknowledgement is still recorded** — ADR 0002 requires that — and **the record is a governance event under W1-D3 §8a, not a state change.** It may support governance, audit and review **within already-authorised C0 uses**. **This record creates no new export, disclosure, processing or propagation right.**

29. **Renewal requires a review act.** W1-D3 §2 — *"renewal is a review act, not a refresh"* — and §8.2's bar on silent refresh, re-dating and re-confirmation both bind. **No sequence of acknowledgements constitutes a review**, and no code path re-dates an item without a user review act in the chain.

30. **These two mechanisms meet at the same runtime moment and must never be conflated.** An L3 acknowledgement permits the user to proceed with a degraded claim; it does not make the claim less degraded, and the clock does not move.

---

# Part B — Runtime consequence

## B1. The consequence table

31. **The governed consequence of each state.**

    | State | Assertion | Provenance | Age | Framing | Acknowledgement | Dependent operation | Safeguard 14 predicate |
    |---|---|---|---|---|---|---|---|
    | **current** | assertable | retained | surfaced always | normal, age visible | not required | proceeds | not reachable |
    | **review due** | assertable | retained | surfaced | visible review-due flag; L1, or L2 where relied on | not required | proceeds | not reachable |
    | **stale** | assertable **only with explicit uncertainty in the output that relies on it** | retained | surfaced | never a footnote; L2 | not required | proceeds, carrying its uncertainty | **reachable** |
    | **expired** | **retained but not assertable as stable truth** | **retained** | **retained** | consumed as unknown; most-protective framing where safety-relevant; L3 | **required before an output resting on it** | proceeds unless the predicate is met | **reachable** |
    | **contradicted** | **suspended from settled-truth use, not hidden** | **both sides, with dates** | retained | both sides visible; prepared clinician question; L3 | **required** | proceeds unless the predicate is met | **reachable** |
    | **unknown** | none to assert | scope, source set and as-of time | as-of time | bounded unknown; L3 | **required** | proceeds unless the predicate is met | **reachable** |

32. **Expired remains the label; unknown is the treatment.** Time moves an item to `expired` and no further — the label does not become `unknown`. W1-D3 §6.2's *"treat as unknown"* is a **consumption rule**. **The last-known assertion, its provenance and its age are all retained**, and remain available for honest display; what is withdrawn is the item's usability as settled truth.

33. **Unknown never means absence, resolution or reassurance.** An unknown is always bounded by **scope, source set and as-of time** (W1-D3 §5.5). *No record found in the reviewed documents* may never become *not present*, *resolved*, *fine*, or *no longer a concern*. **Silence is never converted into a negative claim**, by any layer, ever.

34. **Two origins, one treatment.** Unknown-by-expiry carries a last-known assertion; unknown-at-source has none to carry. Both are consumed as unknown; only one has something to retain. **Neither is presented as the other.**

35. **The §6.4 floor is restated and remains absolute:** *"no room may present stale or unknown health context as stable truth, ever."*

## B2. Safeguard 14 is predicate-based

36. **Safeguard 14 is predicate-based, not label-based.** It fires **whenever safe completion of a dependent operation would require assuming that an uncertain safety-relevant fact is absent or resolved** — and it fires on that predicate alone, never on a state name.

37. **A stale item can satisfy the predicate.** W1-D3 §2 makes stale *"usable only with explicit uncertainty surfacing in any output that relies on it"* — stale is explicitly uncertain. Where an operation could carry that uncertainty honestly, the predicate is not met and the operation proceeds. Where the operation would have to round the uncertainty off to *absent* or *resolved* in order to complete, **the predicate is met and the operation fails closed.**

38. **The predicate is about what completion would require, not about which label the item carries.** Reading the table in B1 as a state-keyed permission list would be a misreading; the last column records only whether the predicate is **reachable** in that state.

39. **Safeguard 14's condition is not broadened by this record**, and no other safeguard of ADR 0025 is relaxed, narrowed or reinterpreted here.

## B3. Fail-closed scope

40. **The unit that may fail closed is the specific dependent operation or output — and nothing larger.**

41. **This disposition does not turn freshness review into a precondition** on the user's access to the room, their ability to correct or acknowledge information, or their ability to continue using room operations that do not depend on the uncertain fact. **A specific dependent Wing operation or output may fail closed when the exact safeguard-14 predicate is met; that is the Wing declining to produce that governed result, not a restriction on the person's agency.** ADR 0002 Doctrine 3 binds: *"Nothing in this doctrine blocks the user… What can be 'blocked' is exactly one thing: the Wing presenting unsound data as settled truth."*

42. **The room is never closed, gated or made unavailable as a whole.** A room whose one dependent output fails closed **remains open and usable**, and every operation in it that does not depend on the uncertain fact **remains available**.

43. **A fail-closed withholds only the dependent Wing-produced operation or output that cannot be completed without the forbidden assumption.** It does not close the room, withhold the user's own data, prevent correction or acknowledgement, or prevent the user from acting independently of the Wing's withheld result.

44. **The refusal is structural and content-free**, on ADR 0024's discipline: it echoes no refused content, writes no user, room, profile or vault state, and carries a fixed reason. **A content-free governance event may still be recorded** where doctrine requires one.

## B4. Assertion posture

45. **Assertion posture is derived at evaluation from exactly three inputs:** **(i) claim polarity** — including whether the claim is a positive assertion or an explicit absence assertion; **(ii) the item's current authority and freshness treatment** — treatment, not merely label, so an expired item's unknown treatment governs; and **(iii) applicable scoped-set membership** — naming *which* accepted set is consulted and for what governance purpose, per ADR 0027.

46. **Where assertion-posture evaluation is required, the derived runtime result is exactly one of three:** `positive safety constraint` · `ordinary positive fact` · `explicit absence assertion`. **These are runtime consequences of the inputs in decision 45**; they are **not** new authority states, freshness states, profile categories or safety-set memberships.

47. **The three posture results are derived and never persisted.** They are not stored as a profile field, taxonomy, authority label, staleness label, user attribute, governance-metadata attribute or persisted evaluation result. Where the distinction is needed it is **recomputed from decision 45's inputs**; **no layer may mint a durable posture vocabulary from these three results.**

## B5. Composition of the ADR 0002 and ADR 0020 mechanisms

48. **The two mechanisms apply independently, each within its own membership.** ADR 0002's L2/L3 surfacing ladder applies over ADR 0002's six-member set. ADR 0020's always-shown inline uncertainty applies over W1-D3 §6.3's four-member set, which ADR 0020 adopts verbatim.

49. **No precedence, no supersession, and no winning set is created.** Both records remain accepted, in force and unamended. This record adjudicates no membership of either set (ADR 0027).

50. **No fallback ADR 0020 inline rule may be inferred for a non-member of §6.3's four.** ADR 0020 states its rule for its own set and says nothing about non-members. **That silence is not a weaker rule, and it is not this record's to fill.** Any implementation, room contract or later record that supplies a non-member inline rule by inference is acting outside accepted authority.

---

## The §10.6 disposition, and its own constitutional check

**W5-AR §6.1 requires this record to give the block-versus-warn question its own constitutional check.** The question, verbatim from its accepted source:

> **Block vs warn.** Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor).

51. **The disposition.** §10.6 resolves **at the dependent-operation / output boundary**. Neither pure answer is adopted: it is **not** always-warn, because an operation that could only complete by assuming an uncertain safety-relevant fact absent or resolved must not complete; and it is **not** hard-blocking a room function, because the unit of failure is the dependent operation, never the room and never the user.

### Constitutional check on this disposition specifically

- **Law 11 holds.** Freshness review is not made a precondition on the user's access to the room or on correction. A dependent Wing operation or output may still fail closed under the exact safeguard-14 predicate, while independent room operations remain available. The user remains free to act independently of the Wing's withheld output; **acknowledgement does not compel the Wing to produce an output that fails the governed predicate.**
- **Law 6 (no clinical judgement) holds.** A fail-closed asserts nothing clinical. It is a refusal to assert — the opposite of an opinion — and it produces no diagnosis, inference, prediction or recommendation.
- **Law 7 (approved is not current) is served.** This disposition is what Law 7 costs at runtime: an item that has aged past its hard limit stops functioning as truth, visibly.
- **Law 12 and ADR 0002 hold, and the boundary is exact.** ADR 0002 rejected hard blocking **within its own Law-12 surfacing scope** as something that *"overrides user authority, converts governance into gatekeeping."* **This disposition does not reintroduce it:** it blocks no user and no room, and it operates inside Doctrine 3's single permitted block — *the Wing presenting unsound data as settled truth*. Per W5-AR §6.1 this record consults ADR 0002's reasoning **without treating ADR 0002 as having resolved §10.6**; the resolution is made here, with this check.
- **W1-D3 §6.4's floor is honoured, not converted.** The floor said no room may present stale or unknown context as stable truth. This disposition never presents it as stable truth, and it never silently converts the floor into an implementation choice about blocking — the choice is made in ink, at doctrine level, with its scope bounded.
- **ADR 0020's acknowledgement-before-continuing rule is untouched.** It remains *"a surfacing-order requirement, not a functional block"*, and this record does not convert it into one.
- **ADR 0025 safeguard 14 supplies the trigger; this disposition supplies the scope.** Neither is widened by the other. Safeguard 14 was a **partial** disposition of §10.6; this completes it without relaxing it.
- **No new authority.** No label, class, authority state, freshness state, edge, grant type or namespace is minted. **No safety-relevant or high-stakes set changes membership.**
- **No law required reinterpretation, and no amendment is proposed or required.**

52. **Acceptance of this record makes W1-D3 §10.6 doctrinally resolved for governed W5 runtime work.** The room-contract cells that literally retain `Open (§10.6)` are **not edited, superseded or textually amended by this record**; they remain historical source text unless a separately governed documentation update changes them. **W5-D2 must use this record as the authoritative §10.6 disposition when it reaches those cells** and may not treat their retained `Open` wording as permission to choose behaviour locally.

---

## Deterministic proof obligations for W5-D2

53. **These are structural obligations, provable without a model. Stating them here claims no behavioural result whatsoever.**

    - freshness-label derivation from an injected elapsed measure and a governed policy key, in the fixed-duration-day unit;
    - **refusal on a missing or non-increasing threshold configuration**, and on a key lacking a complete `R`/`G`/`H` triple;
    - **`S` computed as `R + G`, never read from an independent source**;
    - label monotonicity: a larger elapsed measure never yields an earlier label;
    - **freshness valid at every governed reliance**: where an authorised re-review trigger affecting an item has arisen before a later reliance, **that trigger is consumed before the later reliance** (decision 22);
    - **acknowledgement writes no review timestamp** and changes none of the six states listed in decision 27;
    - **renewal requires a review act**; no path re-dates an item without one;
    - last-known assertion, provenance and age **retained** across decay and into unknown treatment;
    - an expired item **never rendered as stable truth**;
    - **the fail-closed predicate fires mechanically when exactly its condition is met**, refusing content-free per ADR 0024;
    - the four observation surfaces expose freshness evaluation **by construction**, per ADR 0024 — *"absence must be demonstrated, not presumed."*

54. **Several of these already hold in the accepted engine** — threshold refusal, monotonicity, one-step downward decay, and provenance and age retention across decay. **W5-D2 verifies them at the runtime boundary; it does not re-legislate them.**

## Behavioural obligations, deferred and not claimed

55. **This record proves nothing behavioural and claims nothing behavioural.** Specifically deferred to **DR-W5-07** for architecture and to **W5-D3 and W5-D4** for the instrument and its execution:

    **whether a model given degraded, expired or unknown context nevertheless behaves as though the uncertain fact were absent or resolved.**

56. **No deterministic obligation above may be phrased, cited or summarised so as to imply that behavioural question is answered.** Structural correctness of the context a model receives is **not** evidence about what the model then does. **The twenty-three fixtures remain `behaviourally_unexecuted` and the nine pending stubs remain untouched by this record.**

---

## Alternatives considered

- **One record in two parts, semantics then consequence (chosen).** §10.1 and §10.6 are distinct questions but operationally coupled — *"a room cannot decide what to do about staleness without knowing what makes something stale"* — and splitting them would let one land without the other.
- **Two records, freshness and behaviour (rejected).** It would create an eighth W5-D1 identity, and it would let a behaviour record cite thresholds that had not landed, or a threshold record land with no consequence.
- **Decline to set numbers, and bar the dependent capabilities (rejected).** W5-AR §6.2 expressly offers this. Rejected because the bar would hold indefinitely — clinical-adjacent input was sought and could not be obtained (ADR 0025) — and an indefinite bar with no route out is a worse governance position than labelled placeholders with a review horizon.
- **Per-type differentiated numbers now (rejected as unfounded).** Nothing gathered in this phase supports distinguishing medication from allergy from pregnancy status. **Inventing a differentiation would dress a guess as a finding.** Uniformity with an explicit non-equivalence rule is the honest shape.
- **A non-ageing policy for pregnancy status and clinician instructions (considered and rejected).** It would have given two W0 high-stakes fields **no automatic transition at all**, since W1-D3 §2 makes staleness transitions the only automatic ones — leaving both able to read as permanently `current`, against the very law that says approved is not current. **Ordinary ageing keys avoid the problem instead of surfacing around it.**
- **Governing `S` directly as a fourth value (rejected).** A directly governed `S` can silently desynchronise from `R + G` when `G` changes.
- **A precedence rule between the ADR 0002 and ADR 0020 mechanisms (rejected).** Naming a winner in either direction would supersede an accepted mechanism from inside a different record's scope, which ADR 0027 forbids.
- **Always-warn, or hard-blocking a room function (both rejected).** The first would let an operation complete by treating uncertainty as resolved; the second would gate a room and, in practice, a person.
- **Answering §10.2's sensitivity-class axis here (rejected).** Not assigned, not required, and it would widen the freshness axis without a mandate.

## Consequences

- **W1-D3 §10.6 is doctrinally resolved for governed W5 runtime work**, and W5-D2 may reach the room-contract cells without resolving a sealed question by building. **The cells' retained `Open (§10.6)` text is not changed by this record** and remains historical source text until a separately governed documentation update alters it.
- **A runtime that surfaces section age or freshness now has a source for its numbers** — the gap W5-AR §6.2 named.
- **For as long as these defaults remain governed by this record, every reproduction or summary of a threshold value carries the exact provisional label.** Representations drawn from the six equal-key policies additionally carry the non-equivalence rule. **Supersession or explicit re-affirmation follows decision 21; silence never converts a provisional default into a validated one.** That deliberate carriage is **governance friction, not permanence.**
- **A review horizon now exists that someone must act on.** Reaching it without a decision leaves the defaults overdue, not validated.
- **Harder, deliberately:** a room may now decline to produce a specific output, and users will sometimes meet that. The alternative was a room that answered confidently from data it should not have trusted.
- **Six identical keys will look like imprecision, because they are.** The non-equivalence rule exists so that the imprecision is legible rather than mistaken for a finding.
- **No capability is authorised.** Nothing here builds, implements, transmits, or contacts a model.

## Constitutional check

- **Law 1** — no background polling, no outward reach, no push; every evaluation sits inside a user-initiated interaction and every flag surfaces at next relevant use.
- **Law 6 and W0 §7** — no clinical judgement anywhere; no threshold asserts anything about a body; no clinician advice is overridden, reinterpreted or editorialised; a fail-closed is a refusal to assert.
- **Law 7** — expanded from a principle into governed numbers and runtime consequence.
- **Law 11** — freshness review is not a precondition on room access or correction; a dependent Wing operation or output may fail closed under the governed predicate, while independent room operations remain available.
- **Law 12 and ADR 0002** — the ladder is consumed, not altered; the single permitted block is respected exactly; no escalation-on-noncompliance is introduced.
- **Law 13** — every transition, flag, acknowledgement and refusal is a content-free governance event under W1-D3 §8a.
- **No new authority.** No authority label, staleness label, sensitivity class, edge, grant type, namespace or set membership is minted or altered.
- **ADR 0027 honoured** — no set membership adjudicated, no canonical set created, no precedence asserted, no non-member inline rule inferred.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not: amend W0, W1-D3, W1-D6, ADR 0002, ADR 0020, ADR 0024, ADR 0025, ADR 0027, or any room contract; alter the membership of any safety-relevant or high-stakes set; create a canonical set or assert precedence between mechanisms; supply an ADR 0020 inline rule for non-members of §6.3's four; resolve W1-D3 §10.2, §10.7 or §10.8; claim clinical validation, certification, endorsement or safety for any number; convert any input gathered in this phase into clinical evidence; decide code placement, storage shape, configuration form, or where elapsed duration is computed; decide surfacing wording, string catalogues, labels or any user-visible copy; claim any behavioural result; execute or alter a fixture; touch the pending ledger, Lane C, or the engine; open W6; or authorise any implementation, directory, dependency, model contact, payload construction, transmission, or harness work. It contains no real health data and no clinical examples, and it authorises **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**

## Public-safety considerations

Generic and structural wording throughout — user, Wing, room, item, key, label, policy, operation, output, human reviewer, architect. **The key names — medication, allergy, condition, injury, pregnancy status, clinician instructions, preference — are the accepted corpus's own governance vocabulary**, taken from W1-D3 §10.1, W0 §7 and ADR 0002. **No named drug, diagnosis, allergen or procedure appears; no clinical example is given; no statement is made about any person.** The numbers are governance intervals carrying an explicit non-validation label and an explicit non-equivalence rule, and they describe how a record ages, never what is true of a body. No private names, no model or vendor names, no URLs, no project lineage beyond this repository.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D3` · `W1-D6` · `ADR-0002` · `ADR-0003` · `ADR-0020` · `ADR-0024` · `ADR-0025` · `ADR-0027` · `W5-AR`

**`ADR-0026` is deliberately absent.** This record depends on ADR 0027, which itself depends on ADR 0026; adding a transitive edge would assert a direct dependency that does not exist. **To be confirmed at landing-scope time rather than treated as final here.**

## Open boundaries, preserved explicitly

1. **W1-D3 §10.7 — re-authentication for high-stakes confirmations.** **Owner: DR-W5-03.** Not touched here, and its four-member list is not a freshness key set.
2. **ADR 0020's inline behaviour for a non-member of §6.3's four.** **Unstated in the corpus, not inferable, and not answered here.** Unowned.
3. **W1-D3 §10.8 — pattern hygiene**, whether unreviewed *possible pattern* items should auto-expire. **Outside this record.**
4. **W1-D3 §10.2 — whether expiry should also vary by D1 sensitivity class.** Not answered; the axis here is data type alone.
5. **Exact code placement, storage shape, configuration form, and where elapsed duration is computed.** **W5-D2.**
6. **Surfacing wording, string catalogue, labels, layout and UI.** **W6.** **W6 governs presentation; it does not govern meaning** — the provisional label and, where the six equal-key policies are represented, the non-equivalence rule are semantic carriage requirements under decision 16 and **may not be omitted by any presentation choice.**
7. **Whether a model given degraded or unknown context behaves as though the fact were absent or resolved.** **DR-W5-07 / W5-D3–D4.**

---

*The numbers in this record are the least defensible thing in the corpus, and they are labelled as such in every place they appear. That is the trade: a Wing that cannot say when something went stale will quietly treat everything as current, which is the one failure the whole authority model exists to prevent. Better a placeholder that announces itself than a silence that passes for freshness.*
