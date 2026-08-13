# W5 — Runtime Enforcement and Behavioural Evaluation

## Phase Runway / Alignment Brief

**Status:** Accepted by human reviewer, 2026-08-13. Not a build instruction.
**Date:** August 2026
**Phase:** W5 — the first runtime phase (the phase after the sealed jurisdiction layer)
**Governed by:** W0 Constitution; ADRs 0001–0022; the accepted W1 corpus; the sealed W2 corpus and its enforcement machinery; the sealed W3 phase and its engine spine; the sealed W4 phase, its four room contracts, and its three W4-D6 lanes; the published W3 and W4 runways (structural precedent)
**Tier at landing:** J — Judgment (phase runway; full ceremony when landed)

---

**W1 wrote the laws. W2 taught the repository to check them. W3 built the spine that holds evidence without reading it. W4 drew four walls in the rooms' own words and gave them mechanical teeth. W5 is the first phase in which something the Wing built can actually act — and so it is the first phase that must prove a wall holds rather than declare that it should. W5 realises, at runtime, the boundaries W4 declared, and then measures whether they hold, including on the channels that produce no output. No fixture is executed until the control it traps exists; no capability ships ahead of the proof that would catch its failure.**

## 1. W4 closure dependency

W4 — Room Contracts — is **complete and closed**, sealed by the W4 closure record accepted 2026-08-12 and published at `03da48add6bbb0555cbf23d4924229ef7c1db4dd`, with the phase ledger recording that closure at `19365354066f0087aeabf1db4a8dbd8346f78866`. The closure record's registered content hash validates against its published bytes. W5 therefore begins, as W4 did, with working gates rather than promises — and it inherits **W0–W4 whole**:

- the **engine spine is complete and sealed**: it holds, belongs, shapes, moves, remembers, travels, and gives back, every behaviour doctrine before it was code, every promise carrying a standing test;
- the **W2 enforcement machinery** is active on every landing: the registry (53 entries) is test-asserted on every run; the checklist and the ADR 0003 ceremony tiers govern every landing; the public-safety scan runs landing-mode before first commit and normal-mode after; the deterministic suite (281 tests — 272 passed, 9 skipped, 0 failed, 439 subtests) stays green through every commit, and the suite's directory- and dependency-fence tests are **amended only by record, to admit exactly what a phase authorises and nothing else**;
- the **W4 jurisdiction layer is sealed**: four accepted room contracts, two phase-named validator surfaces, twenty-three referenced and honestly unexecuted behavioural-evaluation fixtures, and a complete-and-honest assurance evidence map;
- the three exact dependency pins are unchanged since the first line of product code; any change remains a Tier F fence.

**W5 does not reopen W0–W4.** Where W5 needs a scope, an edge, a label, a grant element, or a prohibition, it cites the sealed corpus — it never re-decides it. Where W5 finds a sealed record defective, it stops and raises a correction record through ceremony, on the ADR 0022 precedent, rather than coding around doctrine.

## 2. W5 north star

**W5 realises, at runtime, the boundaries W4 declared — and then measures whether they hold, including on channels that produce no output.**

The phase therefore has **two governed eras under one phase**, and the seam between them is already written into the repository's own pending ledger, which names three owners: `w5 adapter phase`, `w5 evaluation era`, and `w6 surface phase`.

**Era one — adapter and runtime enforcement.** The processing boundary, the processing context, grant machinery, payload assembly and equality, transmission and disclosure mechanics, architectural isolation made real, and the M2 runtime. Its proofs are **deterministic**: the two `w5 adapter phase` stubs are deterministic tests, and the properties ADR 0017 states — a two-room grant that cannot be constructed, a composition point that does not exist, processing state that is not reused — are structural claims a machine can check.

**Era two — behavioural evaluation.** The harness, behaviour-delta observation across four surfaces, execution of the twenty-three-fixture corpus, and the honest recording of results. Its proofs are **behavioural**: the four `w5 evaluation era` stubs, and the failures W1-D5 OR-3 says topology cannot remove — *"a model can still err within a lawful channel."*

**The order between them is not a preference.** W1-D6 §3.2 requires *"deterministic before generative"*; ADR 0017 decision 3 requires *"the absence of a path, not the presence of a rule against using one"*; and decision 7 warns that suppressing a statement while the context still holds cross-room content *"leaves the behaviour change intact and launders the violation."* A behavioural isolation result obtained over a channel that is still open measures model discretion, not architecture. Structural unreachability is proven first, or the behavioural result is not evidence.

**Lane C Tier 2 evidence capture follows the capability that generates the evidence, and remains a separate governed maintenance act.** The assurance record's maintenance rule 1 forbids row change *"by self-adjustment from any consuming or evidencing artefact"* — so the deliverable that builds a control may never be the deliverable that greens its own assurance row.

**W5 does not open review surfaces, the governed string catalogue, governance-label rendering, UI, CLI, hosted mode, or sync.** The Wing's differentiation remains its restraint: W5's output is a bounded, observable runtime and an honest measurement of it — not a product.

## 3. Proposed W5 deliverable sequence

Execution order may resequence where dependencies allow (the W2-D6-before-D5 and W3 resequencing precedents stand; **IDs stay stable**). Six deliverables, derived from the inheritance rather than mirrored from W4's numbering:

| ID | Deliverable | Era | Shape |
| :---- | :---- | :---- | :---- |
| **W5-D1** | Runtime doctrine set | — | The phase's decision records, landing individually through full ceremony, each accepted before what it gates. First record: **DR-W5-01 — AIAdapter / Processing-Context Boundary**. No code, no directory, no dependency, no model contact. |
| **W5-D2** | Runtime implementation | Adapter | Milestone-based on the W3 precedent — every capability lands with its deterministic proof in the same commit. Owns the processing context, one-room grant binding, payload assembly and equality, transmission and disclosure mechanics, isolation, and the M2 runtime. **Four-surface observability is designed in, not retrofitted.** |
| **W5-D3** | Behavioural evaluation harness | Evaluation | Build and prove the instrument, including its own false-positive and false-negative guards. **The twenty-three-fixture corpus is not executed in this deliverable.** |
| **W5-D4** | Fixture execution and evaluation records | Evaluation | Execute only once W5-D1 to W5-D3 prerequisites hold. Results never enter fixture files. Every `execution_status` transition follows whatever W5 doctrine is eventually accepted for it. |
| **W5-D5** | Lane C Tier 2 evidence maintenance | — | One governed maintenance act, separate from the artefacts that generated the evidence. Includes explicit reassessment of `AR-NIST-05` currency. Never converts Tier 3; never mechanically resolves applicability. |
| **W5-D6** | W5 closure record | — | Whole-phase closure assessment against this runway; pending-ledger review; incident log; honest findings; deferred inventory; the W6 gate named without opening W6. |

**Sequencing notes, reported rather than silently applied:**

- **The adapter/evaluation seam is real and should be preserved in every later record.** W5-D1 and W5-D2 are era-one work; W5-D3 and W5-D4 are era-two; W5-D5 and W5-D6 belong to neither and depend on both.
- **W5-D1's records are not one ADR.** The doctrine questions listed in §4 are distinct decisions with distinct dependents; collapsing them would repeat exactly the failure mode ADR 0022 exists to correct — a doctrine defect discovered late, inside a record too large to correct cheaply.
- **W5-D2's internal milestone order, including where the M2 runtime falls, is resolved by the W5-D2 brief** after the runtime and isolation doctrine is accepted — not here. *Recommendation preserved for that review:* M2 late, on the reasoning that unreachability is only meaningfully demonstrated where a path could otherwise exist, and Meditation is the room where a breach is least recoverable. The counter-argument — that Meditation has no inbound read edge and is therefore the least entangled context — is preserved with it. **This runway freezes neither.**
- **W5-D1 records gate W5-D2 milestones individually**, not as a block. A milestone may proceed once the records it depends on are accepted; it may not proceed on the strength of records still in review.

## 4. Required decision records before implementation

No W5 runtime, harness, directory, dependency, or model contact exists until the records governing it are accepted. The candidate W5-D1 set is **seven records** — **candidate record identities, not yet accepted doctrine; each still lands through full ceremony as its own decision record before the artefact it gates:**

1. **DR-W5-01 — AIAdapter / Processing-Context Boundary.** *The first record, and the one the sealed corpus already requires by name:* W0 Open Question 10; W1-D1 §5 (*"No Z5 flows exist until the AIAdapter ADR (OQ 10) specifies authentication, scoping, and impersonation prevention"*); W1-D5 §8 (*"Decision records required … the AIAdapter ADR (E12 — which must import this threat model's Z3/Z5 rows wholesale)"*); W1-D6 §9.4 (*"before any Z5 connection exists"*). It establishes the smallest doctrine necessary to define the processing boundary **before** grants, payloads, isolation implementation, transmission mechanics, or evaluation architecture depend on it, and it carries the four-surface observability requirement (§5.1). **Because it is the AIAdapter ADR, it must address all three E12 prerequisites at doctrine level — scoping, authentication, and impersonation prevention — defining the required properties rather than silently deferring them; and it must state explicitly whether E12 becomes defined or remains reserved.** Vendor, model, SDK, credential implementation, and network mechanism may remain with DR-W5-06 or later implementation doctrine; silence on the three properties may not. Its own brief is the first W5 deliverable brief and gate document three.
2. **DR-W5-02 — Runtime Freshness and Unknown/Stale Behaviour.** Inherits both W1-D3 §10.1 (default review intervals — the source of freshness thresholds) and W1-D3 §10.6 (block versus warn once context is stale or unknown). The questions remain distinct but are operationally coupled. See §6.1. Must be accepted **before any W5-D2 milestone encounters a behaviour-table cell still marked `Open (§10.6)`.**
3. **DR-W5-03 — Grant Machinery, Consent Duration and Re-authentication.** W1-D2 §1 (the thirteen required grant elements), §2 (grant types), §3 (the anti-blanket rules), §5 (revocation's immediate effects); W1-D2 §8.1 (*"single-task TTL, session definition, standing-grant review intervals … deserve their own short decision record"*); W1-D2 §8.2 and W1-D3 §10.7 (re-authentication, *"Proposed posture: yes for E2 and vendor-hosted C3/C4"* — proposed, never decided). Unblocks `test_D5_T04_granted_and_trusted_never_merge`.
4. **DR-W5-04 — Payload Assembly and Payload Equality.** W1-D6 §4.J; W1-D5 D5-T15 and D5-T23. The pending ledger names this record explicitly as an unblocking condition: *"the payload-equality standard record is accepted and an assembler exists."* **This record is also where the Z4 disposition seam lands** (§6.7), because the pending stub concerns payload equality at Z3 **and Z4**.
5. **DR-W5-05 — Transmission and Disclosure Mechanics.** W1-D2 §4 (the required user-facing disclosure form, already fixed and binding); W1-D5 OR-2 (§5.5 below). **Kept separate from DR-W5-04**: assembly and crossing govern different questions, carry different evidence, and fail in different ways.
6. **DR-W5-06 — Model Access.** The pending ledger's condition *"model access is decided"* gates two behavioural stubs. A decision, not an implementation — and any model SDK it implies is a separate Tier F dependency crossing (§5.2).
7. **DR-W5-07 — Behavioural Evaluation Architecture.** The harness boundary (what it decides mechanically versus routes to review); behaviour-delta observation; the `execution_status` vocabulary and transition governance that W4 deliberately did not pre-decide; re-run semantics; false-positive and false-negative controls; and the explicit disposition of the T12 condition seam (§6.3).

**Per-room context-cost evidence is not a decision record.** ADR 0017's second carried question is **evidence-shaped, not ADR-shaped**, and is proposed as a **disposable out-of-repository evidence spike** under the ADR 0007 development-artifact policy, on the ADR 0006 / ADR 0008 / ADR 0013 precedent. **Only findings may land.** If those findings later expose an actual doctrine decision, that decision receives its own governed record at that point. **No DR number is reserved for measurement.**

**Also required, with triggers rather than fixed positions:**

- **A revocation-cascade record** (W0 Open Question 2; W1-D2 §5 preamble: *"Full cascade behaviour for derived artefacts is deferred to its own decision record"*). **Its sequence position is open; its deadline is not: it must be accepted before the first W5 capability produces a derived artefact under a grant.**
- **A VendorAdapter ADR** (W1-D6 §9.5: *"before any Z4 integration beyond the E10 grocery-list edge; payload-equality tests are its acceptance gate"*). Trigger: any activation of E10. The Kitchen contract holds E10 as a declared boundary only and *"establishes no VendorAdapter, connector, network, endpoint, credential, runtime filter, or payload-enforcement implementation."* **Whether W5 activates E10 at all is an open question, and this runway does not decide it** — but the Z4 limb cannot simply be ignored, and its disposition is governed at §6.7.

## 5. Architectural constraints and fences the phase inherits

These are not aspirations. Each is either test-enforced today or written into an accepted record, and each shapes what W5 may build before it builds anything.

### 5.1 Four-surface observability is a runtime architecture requirement

The behavioural-evaluation fixture strategy fixes four observation surfaces in every silent-channel probe, and all twenty-five silent probes in the published corpus carry all four: **spoken output · persisted state · routing and propagation · behaviour selection, ranking, framing, and omission.** The pass condition is *"no behavioural delta attributable to the prohibited inference, and no persisted trace of it, across all observed surfaces."*

**Three of the four cannot be observed from outside a runtime that was not built to expose them.** The strategy forecloses the fallback in terms: *"a future harness that classified spoken output alone could not satisfy this contract."*

**Therefore: observability is designed into the adapter, not recovered by the harness.** DR-W5-01 must account for it, and W5-D2 must carry it by construction. A runtime built output-first would leave the corpus permanently unexecutable, and the only two exits from that position — rebuilding the adapter, or quietly weakening the pass condition — are both avoidable now and neither is acceptable later.

### 5.2 Directory, dependency, and import fences

- **Directory fence** (checklist rule 4, test-enforced): the authorised top-level set is exactly `docs`, `governance`, `tests`, `fixtures`, `scripts`, `engine`, plus the named root files. *"No implementation directories until a phase document explicitly authorises them, by name."* **Any W5 runtime or harness directory is a Tier F fence crossing.**
- **Dependency fence** (checklist rule 5, test-enforced): the manifest holds exactly three pins, unchanged since the first line of product code, and nine manifest filenames are forbidden outright. *"Any new dependency manifest or package is a named fence-crossing requiring explicit human approval before it exists in a commit. Zero-dependency alternatives must be stated alongside any crossing request."*
- **Engine import cap** (ADR 0009's structural cap, test-enforced): `engine/core` may import only `json` and itself; `engine/ports` only its declared worldly libraries. **A W5 adapter cannot live inside the sealed engine tree without a record-backed amendment**, and loosening that cap is a doctrine act, not a convenience.

**This runway may name anticipated crossings; it authorises none.** The W4 precedent binds: *"the first new file the phase lands and any first fence-crossing will each be named and separately authorised when their brief is accepted."*

*Anticipated crossings, named for foresight only:* at least one new top-level directory for the runtime layer; possibly a second for the evaluation harness; at least one dependency if model access is decided in a direction that requires a client library. **Each arrives behind its own Tier F authorisation, with its zero-dependency alternative stated, or it does not arrive.**

### 5.3 Model-access fence

**No model has ever been contacted by this repository, and none may be until a record decides model access.** The decision is doctrine; the client library, if any, is a separate dependency crossing; and W1-D2 §4 binds whatever is chosen — *"The vendor name is part of the sentence, not a footnote. 'A cloud AI service' is not a valid recipient description."* ADR 0001's local-first posture and its stated preference for local models remain the starting position, not a formality to be argued past.

### 5.4 Notification-layer fence

Checklist rule 7, carried from the threat model (D5-T16): *"Anything that contacts the user outside an active session is the notification layer, whatever it is called — and no notification layer exists or may be built without its own decision record, from zero inheritance."* W1-D2 §3.4 reinforces it from the consent side: nothing in the grant grammar can authorise unattended processing, scheduled extraction, or proactive activity.

**The governed trigger:** any retry, scheduled action, background process, or asynchronous mechanism **that can cause unattended processing or user contact outside the active authorised interaction** trips the notification and background-authority fence. **The trigger is the authority and lifecycle consequence, not the mere existence of retry logic** — retry within an active authorised interaction is not itself a notification-layer event. Checklist rule 7 and W1-D2 §3.4 are preserved exactly as written and are not expanded by analogy.

### 5.5 The OR-2 residual, carried and unsoftened

W1-D5 OR-2, verbatim: *"The grant prohibits retention; the Wing cannot verify a vendor's compliance from outside. Mitigation is disclosure honesty (the vendor is named in the grant; local models exist as the default preference), not technical control. This residual is permanent for any vendor-hosted processing and should be stated, not styled away."* Any W5 model-access decision that admits vendor-hosted processing carries this residual into its own text and into the disclosure language, permanently. OR-1 (hosted-mode traffic shape) and OR-3 (behavioural threats have no structural fix) are carried on the same terms.

## 6. Inherited matters with named owners

The purpose of this section is that W5 must not end as it began — holding inherited items whose owners were never assigned.

### 6.1 W1-D3 §10.6 — block versus warn — is assigned to DR-W5-02

**Owner: DR-W5-02 — Runtime Freshness and Unknown/Stale Behaviour.** The question, verbatim from its accepted source: *"Block vs warn. Whether expired safety-relevant context should ever hard-block a room function (e.g., Kitchen meal-planning against expired allergy data) or always warn-and-degrade (§6.4 floor)."*

The **§6.4 floor remains binding until resolution**, verbatim: *"no room may present stale or unknown health context as stable truth, ever."* Six behaviour-table cells in every room contract read `Open (§10.6)` and carry the floor only.

**§10.6 and §10.1 (§6.2) are distinct questions but operationally coupled** — a room cannot decide what to do about staleness without knowing what makes something stale — which is why both are owned by the one record.

DR-W5-02 must:

- **use its own constitutional check** — ADR 0020: *"The question was sealed open by an accepted W1 record; resolving it requires its own decision record with a constitutional check."*
- **consult ADR 0002's reasoning without treating ADR 0002 as already resolving §10.6** — ADR 0002 rejected hard blocking inside its own Law-12 surfacing scope as something that *"overrides user authority, converts governance into gatekeeping"*, but *"a rejected alternative inside one record's scope is not a resolution of another record's named open question."*
- **land before any W5-D2 milestone reaches one of the `Open (§10.6)` cells.** ADR 0020's acknowledgement-before-continuing rule is *"a surfacing-order requirement, not a functional block, refusal, interruption, or answer to the block-versus-warn question"*, and the §6.4 floor must never be silently converted into a block-or-warn implementation decision.
- **prevent an implementer from resolving either question by hard-coded defaults or behaviour.** An implementer who picks a behaviour at a marked cell, or writes an interval into code, has resolved a sealed question by building — which is the failure this assignment exists to prevent.

### 6.2 The review-interval gap

W1-D3 §10.1 (default review intervals by data type) and W1-D6 §9.1 (*"before any profile serves context in W2"*) name a decision that has never been made. The engine was deliberately built so it could not be papered over: staleness is a pure function over **injected intervals, with no clinical defaults, ever**. **A W5 runtime that surfaces section age or freshness therefore has no source for the numbers.** **Owner: DR-W5-02**, together with §10.6 — it must either decide the thresholds or state explicitly which W5 capabilities are barred until they are decided. Neither silence nor a constant in code is available.

### 6.3 The T12 pending-ledger condition seam

`test_D5_T12_cross_room_isolation_behavioural` carries the literal unblocking condition *"room isolation model implemented at the adapter layer."* That condition is **necessary but not sufficient**: T12 is a behavioural test and also requires the evaluation machinery its condition does not name.

**No stub is edited or flipped by this runway, and none may be edited before the decision below exists.** **DR-W5-07 (Behavioural Evaluation Architecture) must decide how the missing behavioural prerequisite is represented**, choosing explicitly between:

- **amending the pending condition through ceremony**, so the ledger states both prerequisites; or
- **leaving the existing condition literal** while governing the additional behavioural prerequisite separately and visibly.

**Until that decision exists, T12 remains pending even if structural isolation has been implemented.** A stub converted on a literal reading of a condition known to be incomplete would be exactly the kind of honest-looking pass the ledger exists to prevent.

### 6.4 The `AR-NIST-05` currency item

The Lane C assurance record states, at `AR-NIST-05` and in its honest-state summary, that Lane B holds *"23 declarations, 0 fixtures."* That was **true at the record's acceptance on 2026-08-10**, and is **no longer live-current** since the Lane B corpus landed on 2026-08-11 with twenty-three fixtures, twenty-three map rows, and a green corpus validator.

**Disposition, carried:** the wording is **accepted historical evidence context with a known current-state currency change.** It is not treated as current, and it is not silently corrected. **Explicit reassessment is assigned to W5-D5 (Lane C evidence maintenance), before `AR-NIST-05` is relied upon or updated.** **No Lane C mutation occurs during the opening ceremony, and none is authorised by this runway.** Not a blocker.

### 6.5 The Lane C Tier 2 / Tier 3 boundary

**Tier 2 — eleven rows, W5-owned.** All carry `deferred_named_dependency` and the dependency string *"W5 runtime (isolation, adapters, transmission, disclosure mechanics)"*. Ten unblock in the adapter era; exactly one — `AR-NIST-05` — requires the evaluation era. Evidence capture belongs to W5-D5, never to the deliverable that generated the evidence.

**Tier 3 — eleven rows, permanently outside.** Ten depend on *"external organisational evidence (operator does not exist)"* and one on *"deployment profile (absent)"*. The W4 closure record: *"evidence about an operator and a deployment that do not exist, which no repository artefact can supply and which no phase may convert into repository evidence. It carries no repository-owned unblocking condition."* The assurance record's own architecture note: **"W5 never collapses Tier 3 into repository evidence."** **No W5 deliverable may take a Tier 3 row.**

**Applicability stays unresolved.** All four applicability records read `unresolved` with `role_or_basis: null`, and maintenance rule 2 makes resolution *"a future governed act recorded on the applicability records — never inferred from evidence presence, never resolved by this record's own text, and never mechanical."* **W5 resolves none of them.** Applicability unresolved is never *not applicable*, and never a pass.

**Not W5's, and not to be swept in:** the eight Tier 1 `not_evidenced` rows. Four trace to the same W0 §12.4 retention-defaults question; the others cover de-identification, accounting of disclosures, and aggregate portability format. The assurance record calls them *"deliberate honesty rows."* They stay honest.

### 6.6 The two dependency strings must not be collapsed

| Dependency | Where | Count | Unblocks |
|---|---|---|---|
| `W5 runtime (isolation, adapters, transmission, disclosure mechanics) plus a behavioural evaluation harness for room surfaces, including behaviour-delta observation` | every fixture's `execution_dependency`; the fixture strategy §7 | 23 | Fixture execution — **era two** |
| `W5 runtime (isolation, adapters, transmission, disclosure mechanics)` | every Tier 2 assurance row's `dependency` | 11 | Tier 2 evidence — **mostly era one** |

The Lane B string is the Lane C string **plus the harness clause**. They unblock at different points in the phase. **Any later W5 record referring to "the W5 dependency" must say which.** There is no `DEP-` identifier namespace in this repository, and no record may introduce one by assumption.

### 6.7 The Z4 disposition seam

**Owner: DR-W5-04 — Payload Assembly and Payload Equality.**

W5 must not assume it activates E10, and this runway does not decide that it does. But **W5 cannot ignore the Z4 limb**, because the deterministic pending stub `test_D5_T15_T23_payload_equality_at_z3_z4` concerns payload equality **at Z3 and at Z4**, *"per boundary edge"*.

**Before the W5-D2 payload milestone, doctrine must explicitly establish one of exactly two states:**

1. **Z4 enters W5 scope** — in which case the VendorAdapter ADR is required before any E10 activation, on W1-D6 §9.5's terms (*"payload-equality tests are its acceptance gate"*); or
2. **Z4 remains dormant** — in which case the Z4 limb of the pending obligation **remains visibly pending or deferred**, and **W5 must not claim the corresponding inherited obligation is fully discharged.**

**There is no silent third state.** A W5 that proved payload equality at Z3 only, and then reported the payload-equality obligation as met, would be the exact failure the pending ledger exists to prevent — a half-satisfied condition reported as whole, which is also how the T12 seam (§6.3) fails if left unattended. **This runway names the seam and its owner; it does not decide Z4 activation.**

## 7. Explicit non-goals

W5 contains none of the following, and this runway authorises none of them:

- **no review surface, no approval surface, no queue surface** — the review/approval surfaces are the surface era's;
- **no governed string catalogue, no catalogue IDs, no catalogue routing** — the catalogue is a W6 structure; the W4 records remain review-of-record until it exists;
- **no governance-label rendering, no legibility standard** — W6's, per D5-T24;
- **no grading of final surfacing wording** — the W1-D6 §5.E/F language categories are placed at *UI implementation*; W5 evaluates behaviour and behaviour-delta, operationalised through each fixture's prohibited and required outcome classes, never final strings;
- **no UI, no CLI** — W5 is a runtime and an instrument, with no user-facing surface;
- **no hosted mode, no sync, no multi-device grant state** — each remains its own future gate;
- **no notification layer of any kind** — the fence stands from zero inheritance;
- **no profile export, no whole-vault plaintext export** — each is its own future record;
- **no new edge** — consent authorises edges and cannot create them; W1-D1 remains the whitelist and E12 remains reserved until a record defines it;
- **no resolution of Lane C applicability, no conversion of Tier 3 evidence, no certification claim of any kind**;
- **no realistic clinical examples, no real health data** — anywhere: not in this runway, the records, the runtime, the harness, the tests, the fixtures, the logs, or the docs; the synthetic-only discipline holds and grammar placeholders remain the only permitted example register;
- **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind** — the archive stores, labels, and constrains; it never opines;
- **no W6 implementation** — W5 names its forward dependencies and carries them; it does not build them.

## 8. First app-shape language

What a **processing context** is, in one honest paragraph:

A processing context is the *only* place in the Wing where a model is ever permitted to see anything, and it is built from a grant rather than from a conversation. It holds exactly one room's content, because the grant that produced it named exactly one room and a grant naming two could not be constructed. It is not a session: a session is something a user has, while a context is something a grant creates and ends. It is not a memory: nothing carries from one context into another, including within a single sitting, because the reuse is the channel and the channel is what the wall removes. It is not an assistant, holds no relationship, and accumulates no impression of the person. It is deliberately observable — what it said, what it wrote, what it passed on, and what it chose or declined to say — because a boundary that cannot be watched cannot be shown to have held. When the grant ends, the processing context ends and **no processing-side state survives it**; any lawful output or governed record leaves only through an authorised edge or governed artefact, and is no longer part of the processing context. That is the shape of the only room a model is ever in.

## 9. W5 entry gate

Per checklist rule 8 and the W4 closure record §8, W5 may not start until all three exist and are accepted — **three documents, three acceptances, no exceptions**:

1. the **W4 closure record** — **accepted, published, and remotely verified** ✔ (`03da48a`; registered hash validated against published bytes);
2. **this W5 runway** — accepted by human reviewer, 2026-08-13; acceptance alone is not repository authority, which takes effect only on publication to `origin/main` and authoritative remote verification;
3. the **first W5 deliverable brief** (the W5-D1 doctrine-set brief, proposing DR-W5-01) — *candidate; pending review*.

**Acceptance of this runway would authorise W5 *briefs* only.** It would **not** authorise scaffolding; it would **not** authorise implementation; it would **not** authorise a directory, a dependency, model contact, payload construction, or fixture execution; and it would **not** create any repository artefact beyond its own landing. Code and repository artefacts arrive only behind their own briefs and their own tier ceremonies.

**Publication is not a fourth gate leg.** The gate is three documents and three acceptances. Publication is the ceremony by which an accepted record becomes authoritative — and by established precedent this runway is itself landed and published as a governed phase record before the first W5 deliverable lands, as the W4 runway was before ADR 0016.

**The exact effective-opening rule, carried from the phase ledger's own statement of it:** *opening is effective on publication.* While a first-deliverable commit remains local it is not yet in force. **W5 becomes effectively open only when the first W5 deliverable is published to `origin/main` and authoritative remote verification succeeds** — not at this runway's acceptance, not at the brief's acceptance, and not at local commit.

## 10. Public-safety note

This runway contains no private names, no private system references, no companion framing beyond naming a prohibition, no project lineage beyond this repository, no real health data, no clinical examples, no model names, and no URLs. All wording is generic: user, Wing, room, contract, vault, profile, grant, processing context, adapter, harness, human reviewer, architect, model.

**W5 watch item — named explicitly because W5 is where it becomes live:** this is the first phase in which a model may be contacted at all, and therefore the first in which a public-safety failure could occur **outside a document**. Three consequences bind every W5 landing:

- **no real health data may enter a payload, a fixture, a log, a transcript, an evaluation record, or a harness artefact** — the synthetic-only discipline extends to runtime, unchanged and unweakened;
- **evaluation records and harness output are governed artefacts** and are scanned exactly as documents are; a transcript is not exempt because it is machine-produced;
- **no evaluation result may be presented as a safety claim, a health claim, or a certification of any kind** — W1-D6 §3.8 binds: *"A green test suite proves conformance to the grammar; it does not promote any datum, raise any label, or substitute for user review."*

### Forward dependencies (constraints W5 names and carries — not blockers to this runway)

- **W6 governed string catalogue** handles catalogue IDs and final wording later. Until it exists, the W4 records and the thirty-three room-register strings (eleven Wellness, eleven Kitchen, eleven Gym, zero Meditation) remain **review of record**, and the catalogue-ID validator class remains **dormant, dependency-named, and never reported as passing**. **No W6 artefact is a W5 opening condition**, and the three W6-owned pending stubs unblock on surfaces, not on any W5 capability.
- **External assurance evidence (Lane C Tier 3)** remains an external dependency about an operator and a deployment that do not exist. It carries no repository-owned unblocking condition and is never converted.

Neither dependency blocks this runway or any W5 record. They are the healthy direction — governance before capability: W4 constrained W5, and W5 constrains what any surface may later do.

---

*Four phases built a house nobody was allowed to enter. W5 opens one door at a time, under a grant, into a room that can only ever hold one room's worth of the world — and then watches, on every surface a wall can be crossed, to see whether the door held. Nothing here authorises the opening. It only makes the first door describable before anyone builds it.*
