# W9 — Application Release Scope and Contract

## Phase Runway / Alignment Brief

**Status:** Accepted by human reviewer, 2026-11-11. Not a build instruction.
**Date:** November 2026
**Phase:** W9 — the phase that decides, before any application code exists, what a supported public reference release of the Wing would be, what authority each part of it needs, and what evidence each of its claims would require
**Governed by:** W0 Constitution; the accepted W1–W8 corpus whole; the W8 closure record and its carried inventory; W1-D1 and W1-D2 above all; ADR-0006, ADR-0010, ADR-0043, ADR-0046, ADR-0047 and ADR-0051 whole; the W3 through W8 runway precedent
**Tier at landing:** J — Judgment (phase runway; full ceremony when landed)

---

**Eight phases built a governed engine, four room contracts, a runtime that refuses, a surface that claims nothing, and an instrument for telling a governance change from a change of wording. None of that is an application, and W8's closure concludes nothing about readiness or usefulness. W9 is the phase that asks what a finite, supported, public reference release would be — and answers on paper, capability by capability, with the authority each one already has and the decision each one still needs. It builds nothing. The question it exists to settle is the one a release cannot survive leaving vague: what, exactly, is being claimed, and what would show it.**

## 1. Status and boundary

**This runway is gate document two** of the standing three-document entry gate, and it authorises **W9 briefs only** — never implementation, never a directory or dependency crossing, never model contact, never a release. *Opening is effective on publication:* the gate-document-two state takes effect only once this record is accepted, published on the default branch, and independently verified against the remote.

**W9 is public, synthetic-first, and bounded.** Any real-person adoption is a separate governed authority outside this repository, and no W9 record names, describes, implements, or depends on it.

**W9 is a scope-and-contract phase, not an implementation phase.** Every W9 deliverable is a governed document. The first line of application code, the first new directory and the first new dependency belong to no W9 deliverable, and each would arrive only behind its own later runway, brief and Tier F authorisation.

## 2. W8 closure baseline

W8 — Generative Evaluation Maturity — is **complete and closed** in the accepted sense, sealed under `W8-CR` at `c6de8a99f09d60164def9f330f72437b2812c370`, closing **complete, not perfect**. W9 inherits the whole inventory of `W8-CR` §9, thirty rows, **each at its exact published standing** (§12). Row thirty records the W8-D7 closure programme itself, which ended with that record and leaves no later landing; rows one to twenty-nine are the matters carried forward, and W9 reopens, solves and reclassifies none of them by existing.

W9 also inherits the standing state at that seal: **847 deterministic tests run, 838 passed and 9 skipped, with 4,943 subtests; 447 files scanning to zero findings with 118 suppressions and not one added across W8; the dependency manifest unchanged at its three pins since the first line of product code.** These are counts of proofs that ran and files that were read, and nothing more. **Closure is not capability:** `W8-CR` establishes no maturity, adequacy, readiness, safety or usefulness conclusion, and this runway draws none from it.

Four carried positions bind every W9 deliverable exactly as published and are not reinterpreted here: **the W8-D5 finding is undetermined** (`W8-D5-AFR`); **the W8-D6 decision is contact as a decision that authorises nothing**, its four separate instruments unopened and its authority question unanswered (`W8-D6-CDR`); **ADR-0047 precondition 3 is outstanding in its lawful resting state**; and **ADR-0058's reservation stands** — the published records classify no exchange and state neither way whether model contact occurred, and no W8 act prepared, authorised or performed model contact.

## 3. North star

**A person unfamiliar with this repository should be able to install a supported reference build, complete one bounded task in each room with synthetic material, see what information and what authority each task used, understand a refusal, exercise the rights the build supports, and recover the installation from the published instructions — and every claim the release makes should be one its retained evidence supports.**

The release must remain useful with no model and no device. An optional integration may add a bounded capability; it may never become a condition for a person's access to their own information or rights.

**W9 does not build toward that sentence. It decides what the sentence would have to mean, and what would have to be decided before any part of it could be built.**

## 4. Three completion states, kept distinct

| State | Meaning | Standing |
| :---- | :---- | :---- |
| **W8 closure** | The governed evaluation programme is complete, with its evidence limits stated and its carried matters at their published standings | Effective at the baseline of §2 |
| **A public reference release** | A specified build meets its own accepted contract for function, comprehension, security and maintenance, on the configurations actually tested | **Proposed.** No release contract is accepted; this runway accepts none |
| **Real-person adoption** | — | Any real-person adoption is a separate governed authority outside this repository |

**Completing one state opens none of the others by milestone effect.**

## 5. The questions W9 must settle

W9 answers these from published sources and the live repository, never from a planning summary and never from phase closure:

1. **Boundary.** What may a public reference application be, and what may this repository hold once runnable application code exists? ADR-0046 fixed public W7 as synthetic-only by construction — a law the W8 runway carried forward and §8 carries again — with a constructional test under which an artefact, path, field or process that *could* carry real-person content is unlawful regardless of whether it does. The sealed engine already accepts whatever bytes its caller supplies; the W3 runway already held that *"a real user's real data exists only in that user's local runtime, never in any project artifact"* (`W3-AR` §5); and the accepted backup and key-loss records already speak of real data entering a real vault behind their own gates (ADR-0011; ADR-0012). **How those accepted positions bind an installable application, its demonstrations, its examples and its release evidence is a doctrine question, and it is W9-D1's — decided by its own record before any other deliverable relies on an answer, and not decided by this runway.**
2. **Baseline.** For each component the release would reuse: is it implemented, tested, published design only, or a carried limitation — re-derived from source?
3. **Scope.** What is the intended use, who is the first intended reader, and what single environment is supported first? Which application shell, if any, satisfies the standing platform doctrine on observed evidence rather than on preference?
4. **Workflows.** For the common governed journey and for one bounded task in each room: exactly which declared edge, grant type, record class and room-contract clause permits each input, each processing step, each persistence and each output — and where none does, what decision would be needed?
5. **Integrations.** What must any optional integration contract require, and prove, before an integration could be admitted?
6. **Evidence.** What retained evidence would support each release claim, and in what lawful form?
7. **Responsibility.** Who is accountable for the reference build, its contracts, its assurance and its maintenance?

## 6. Proposed W9 deliverable sequence

Execution order may resequence where dependencies allow (**IDs stay stable**), but the gate discipline of §6.1 is not negotiable.

| ID | Deliverable | Shape |
| :---- | :---- | :---- |
| **W9-D1** | Application boundary doctrine | A decision record answering §5 question 1 from the sources: what a public reference application may be; how the constructional test and the closed exclusion list bind application code, demonstrations, examples and release evidence; the standing invariant by which anything beyond the public reference build is referred to, carried unchanged; and whether any part of the proposed release needs a governing amendment or a different home. **Lands before any later deliverable relies on the boundary.** Docs only |
| **W9-D2** | Capability and authority baseline | A governed record re-derived from source: every reusable component classified as implemented, tested, published design or carried limitation; every proposed release capability mapped to its declared edge, its governing record, and the exact brief or decision it still needs. **No capability is inferred from phase closure** |
| **W9-D3** | Release scope | Intended use, the first intended reader, one supported environment, and the application-shell decision route under ADR-0006's doctrine — evidence before selection. The directory and dependency crossings the scope would need are named and not authorised |
| **W9-D4** | Workflow scope | The common governed journey and one bounded task per room, each traced clause by clause to W1-D1's whitelist, W1-D2's grant types and the room contracts; the decision records the workflows would need, identified and sequenced. **No such record is taken by this deliverable unless its own brief assigns it** |
| **W9-D5** | Integration posture | Contract requirements and conformance proofs for optional integrations, stated as requirements. Deterministic non-model reference doubles only. **No live driver, provider, transport, credential or device connector** |
| **W9-D6** | Release contract | The proposed criteria of §15 converted into bounded acceptance scenarios, each with the evidence it requires and the lawful form of that evidence; responsibilities; the programme's human decision points |
| **W9-D7** | Closure | Whole-phase source re-derivation and closure under the discipline established through W2–W8 |

### 6.1 Gate discipline

The runway lands before any deliverable · **the boundary doctrine lands before any later deliverable relies on it** · the baseline lands before scope is fixed · scope lands before the release contract · the release contract is accepted, if at all, by its own record and its own human act, never by this runway · closure lands only after the evidence is published and independently reviewable. **Each deliverable requires its own accepted brief and its own authorisation, and no W9 deliverable implements anything.**

## 7. Fences the phase inherits

Each is carried exactly as published. **This runway may name anticipated crossings; it authorises none.**

- **Directory and root-file fence** (checklist rule 4; test-enforced): the authorised top-level set is exactly `docs`, `governance`, `tests`, `fixtures`, `scripts`, `engine`, `runtime` and the named root files. **Any application directory is a Tier F fence crossing**, and several conventional directory names are refused outright by the standing proof.
- **Dependency fence** (checklist rule 5; test-enforced): three pins, unchanged, and a closed list of forbidden manifest filenames. Any addition is a named crossing with its zero-dependency alternative stated.
- **Engine import cap** (ADR-0009; test-enforced) and the **runtime's separation from the sealed engine** in both directions (ADR-0024 decision 4).
- **Platform doctrine** (ADR-0006 decisions 1–5): local-first native execution with no server component in the first release; telemetry silence proven by observation, never by documentation trust; no background processes; user-initiated updates only; accessibility a scored criterion. **No application shell has been selected** (ADR-0006 decision 6; ADR-0008): selection needs its own record with observed evidence.
- **Plaintext residue** (ADR-0004): nothing decrypted persists past task end, logs are plaintext-free in every build configuration, and the enumerated artefact classes — content caches, previews, serialised interface state holding content — are forbidden without their own record.
- **Minimal review posture** (ADR-0010): nothing real becomes Approved until real review surfaces exist; a review command is a review surface in any medium; user acts are constructed only in the test tree; reversal needs a new decision record.
- **Surface contract** (ADR-0043): a surface writes nothing and persists nothing; recording a human act requires a future governed record creating a lawful store.
- **The flow whitelist** (W1-D1 §0 and §5): a flow without an edge does not exist, and consent authorises edges and cannot create them (W1-D2 §0). **Rights are not grants:** a person's access to, export of and erasure of their own records are never consent-gated.
- **The four room contracts** (`W4-D2` to `W4-D5`), each authorising no implementation, with the Meditation edge set exactly M1 and M2.
- **Notification fence** (checklist rule 7): anything that contacts a person outside an active session is the notification layer, which does not exist and may not be built without its own record.
- **The seven conjunctive first-contact preconditions** (ADR-0047 decision 9), and the standing public posture of ADR-0051.

*Anticipated crossings, named for foresight only:* at least one new top-level directory for an application layer; possibly a dependency if the shell evidence requires one; a decision record on the review path; a governed record creating any lawful store an application would need; decision records for room-record persistence, vault layout and the rights operations not yet built. **Each arrives behind its own authority, or it does not arrive.**

## 8. Public/private boundary

W9 inherits the W7 public/private boundary whole. In public records the external side is named exactly one way and never otherwise:

> **Any real-person adoption is a separate governed authority outside this repository.**

**No public W9 record may contain:** real-person data of any kind · any identified person's room, health, movement, food, device, contemplative, or journal material · real wearable or device data · private relationship or lived-interaction material · private model transcripts · credentials, tokens, keys, secrets, or private configuration · machine-identifying detail beyond permitted class-level information · a model binary · a real-person evaluation channel · private adoption implementation detail · or anything that would turn the public Wing into a live personal instrument.

**Synthetic-first remains structural: synthetic-only by construction, never by scrubbing** — under ADR-0046 carried unweakened. Every fixture, demonstration, example, walkthrough and evidence record a W9 deliverable proposes is authored from nothing. **No W9 deliverable widens a public field, source, processing class or permission to make a proposed release fit**; where the proposed release does not fit the standing law, W9-D1 reports the exact issue and the route for deciding it.

## 9. Model-contact and device boundary

**No W9 deliverable may contact a model, select a provider or model class, build a transport, prepare a credential, or treat future contact as inevitable.** The W8-D6 decision authorises nothing and is not converted into application processing permission by this phase. ADR-0047 decision 3 binds unchanged — contact is the act of transmission and return, *"Local or hosted, direct or adapted, interactive or batched, one exchange or many, by script or by hand"* — so neither a model running on the same machine nor an import of generated text by hand is a route around it. The hosted class stays closed; E12 stays reserved; E10, Z4 and Z5 stay dormant.

**No W9 deliverable admits device-originated data.** The Gym contract's device exclusion stands as written (`W4-D4` §3 and §8): no ingestion, synchronisation, device-file import, device adapter or device provenance label. A device source would be a new source and provenance decision by its own record, never an extension of anything decided here.

**A deterministic reference double is not a model, and its output is never represented as generated.** A task completed by a person from a template is that person's own record, and is never represented as model output either.

## 10. The common journey and the four room tasks — proposed, not accepted

Named so the briefs have a subject; **every permission below is W9-D4's to trace and none is settled here.**

The proposed journey: bring permitted information in · see its origin and authority · review what is pending · approve or decline through an authorised path · choose a room and a task · inspect the context used and its age · prepare an editable result · choose what to keep or take out. **Rights, grants and approval are distinct acts throughout.**

| Room | Proposed bounded task | Boundary the task must show in behaviour |
| :---- | :---- | :---- |
| Wellness | Assemble an editable clinician summary and question list, the export E9 names | Questions remain questions; provenance and uncertainty preserved; no diagnosis or treatment recommendation; export only by the person's own act through E9 |
| Kitchen | Prepare a requested meal and grocery plan | Profile content enters only through E6's closed list; no inferred condition, restriction mechanic or suitability ranking; nothing is ordered |
| Gym | Prepare or edit a requested movement and recovery plan | Profile content enters only through E7's closed list; no invented goals, compulsive mechanics or rehabilitation claim; no device-originated data; no outward edge |
| Meditation | Support a practice timer, study or reflection at the person's initiation | The edge set is M1 and M2 and nothing else; a silent practice writes nothing by default; nothing derived from the room appears in any other home |

## 11. Non-goals — what W9 must not do

W9 does not: implement any application, interface, service, caller or packaging · create any directory or add any dependency · select an application shell without observed evidence under ADR-0006 · contact a model, choose a provider, build a transport, or create credentials · admit device-originated data or design a device connector · design, describe or prepare any real-person use · create a review, approval or queue surface, or any store of human acts · reverse ADR-0010 by implication · create a new edge, grant type, record class, authority state or sensitivity class · decide the E9 export format, vault layout, profile export, whole-vault export or recovery codes except through a record its own brief assigns · give clinical advice or make diagnostic, therapeutic, crisis, legal, `certif-`, `complian-`, production-readiness, safety, correctness, or approval claims · resolve Part Q, the `local-wordlist` seam, or ADR-0047 precondition 3 merely because W9 begins · alter any W8 record, case home, register or revealed record · diagnose any recorded divergence or read any retained record · repair the three named stale derivatives incidentally · convert any pending stub by milestone effect · activate E10, Z4, E12/Z5, or the hosted class · open any later phase · or widen scope to help one.

## 12. Deferred and inherited items

Carried from W8, **each at the exact standing its own row of `W8-CR` §9 records, and none reopened, solved or reclassified by this runway or by W9's existence.** That inventory is the complete one and is not reproduced here; its standings differ, and they are not one status. Row thirty records the closure programme, which ended with `W8-CR`. Rows one to twenty-nine carry: ADR-0047 precondition 3, outstanding in its lawful resting state · Part Q and the `local-wordlist` seam, unresolved and bounded under named doctrine · the twenty-six historical generative-era unknowns, unanswered · the generative evaluation era beyond W7's synthetic scope, deferred under named doctrine, separately gated and assigned to no phase · the inherited W6 inventory, row by row — F-1 and F-2, carried, open and untaken; P-3, optional and untaken; the three ceremony-bound stubs, unconverted; the six generative-era stubs, unchanged behind the first-contact gate; the T12 amendment obligation, assigned and undischarged; the seven carried open questions, still alive; Lane C's eleven rows, external and never convertible; the four applicability records, unresolved by design, a state kept distinct from the external one; the dormant doors, untouched · the pending ledger, nine stubs, byte-untouched across W8 · the W8-D5 finding, undetermined, complete and fixed · the W8-D6 decision, a decision that authorises nothing · the four separate instruments it leaves, unopened, named and not supplied · the authority question, named and unanswered · the alternative evidence routes, named and untaken · the recorded divergences, undiagnosed · the void attempt, void and excluded, with ADR-0058's reservation standing · the retained records, sealed under their own authority · the two carried LF-checkout proof findings, recorded and not solved · the five inert allowlist entries, which suppress nothing · the three stale derivatives, named and unrepaired, their repair decisions unmade — the root `README.md`, `docs/governance/registry.md` and the concept overview · and the human reviewer's W7-D6 instrument-design observation, a future evaluation-design input and nothing more.

Carried from the engine and its governing records, **published limitations a release would have to dispose of honestly and W9 does not solve:** file writes are not atomic, with a one-record blast radius (the engine's own account) · key bytes cannot be zeroed at the language level (ADR-0008) · record cardinality and approximate sizes are observable on disk without any key, and a weak passphrase stays weak (the engine's threat-register entries under ADR-0013) · **a lost passphrase is a lost vault by decision, with no recovery path and none to be added** (ADR-0001; ADR-0012; ADR-0013) — a fixed property to be stated plainly, never a defect awaiting repair · restore is into an empty target only · single-OS evidence only (ADR-0008).

Open decisions the corpus already names and W9 inherits unanswered: the E9 export format (W1-D1 OQ 5) · vault layout, listing, indexing and search (ADR-0004; the engine's own account) · profile export and whole-vault plaintext export · printed recovery codes (ADR-0011 decision 6) · the application shell (ADR-0008) · cross-OS verification (ADR-0008) · retention defaults and the audit-trail surface (W0 §12 questions 4 and 8). **W9 addresses only what its own accepted deliverable briefs assign to it.**

## 13. Stop-and-report tripwires

Public head mismatch · consumed hash mismatch · any public wording that names the private external phase beyond the fixed invariant · any proposed fixture, example, demonstration or evidence form that is not synthetic by construction · any implementation artefact, directory, dependency or manifest · any model access path, credential, provider, transport or binary · any device source · any proposed flow without a declared edge presented as if consent could supply one · any proposed capability described as existing when the source shows design only · any release criterion satisfied by a test count, a phase closure or a mechanical result standing in for a human judgment · any wording that turns the W8-D5 finding into a readiness finding or the W8-D6 decision into a permission · any statement whether model contact occurred · any closure wording implying safety, readiness, correctness, `certif-` or `complian-` status, approval, or private adoption.

## 14. Quality gates for every W9 landing

The standing sixteen, carried from the W7 and W8 runways unchanged: re-ground live authority · verify expected public head · read the governing records · verify consumed hashes · confirm the synthetic-only boundary · confirm no person-specific content · confirm no credentials, keys, tokens, or private configuration · scan before staging · run the relevant proofs · materialise only the measured landing set · stage only intended files · run the full Commit Gate · commit only if exact · push by plain fast-forward only · remote-verify · return a publication packet. **Plus the W9-specific gates:** the placeholder probe over every existing check before any census is fixed, every refusal reported and none absorbed · any proof succession an exact transformation of a fixed pre-image, with the succeeded claim kept proven at its own commit · no capability claim without a source citation · no implementation artefact at any W9 landing · and the standing human-review duties P2 and Q3 at every landing, with P4a and P4b reported separately, always.

## 15. Proposed release criteria — drafts for W9-D6, accepted by nothing here

Each is a proposal. **None is a commitment until W9-D6 converts it into a bounded acceptance scenario and a human act accepts that record.** A criterion is never satisfied by a count of tests, and no numeric threshold is proposed without a reason tied to a supported journey.

| ID | Proposed requirement | Evidence the claim would need |
| :---- | :---- | :---- |
| RC-01 | A person unfamiliar with the repository can install, start and remove the supported build from the published instructions alone | A clean-environment exercise with prerequisites, package identity and a troubleshooting record |
| RC-02 | The synthetic demonstration and the supported manual workflows work with no model, device or external service | A repeatable offline journey with expected outputs and understandable unavailable states |
| RC-03 | Evidence, drafts and approved context stay distinct; provenance and age stay visible | Transition and provenance proofs, and comprehension evidence for the states shown |
| RC-04 | One bounded task in every included room works end to end | Four task walkthroughs with expected outcomes, refusal paths and known limitations |
| RC-05 | Room isolation, the Meditation wall and minimum necessary access hold at the application boundary | Positive and negative access proofs, including tampered requests |
| RC-06 | Delegated access can be inspected, expires and can be revoked; nothing new proceeds under invalid authority | Runtime proofs and understandable interface states, with in-flight limits stated honestly |
| RC-07 | The supported rights are usable and clearly scoped | Export, erasure and access walkthroughs; documented format, retention, backup and revocation limits |
| RC-08 | Incomplete, stale, malformed, conflicting or unavailable input never silently becomes authority | Failure cases and clear recovery choices; no invented observation |
| RC-09 | Backup, restore and a supported upgrade preserve the intended governed state | Clean restore, version migration, interrupted-write and damaged-backup exercises |
| RC-10 | An integration cannot expand authority, silently reroute, or have its output treated as approved context | Contract proofs, faulty-double controls and isolation evidence |
| RC-11 | The assembled build has a supported security and privacy account | Threat model, independent findings and dispositions, dependency inventory, a secret, log and telemetry review, and an open-risk statement |
| RC-12 | Essential flows are accessible and understandable | Keyboard and assistive-use checks in the supported environment; comprehension evidence for consequential choices |
| RC-13 | Release claims, configurations and maintenance are supportable | A versioned compatibility matrix, known limitations, changelog, a vulnerability route and a named maintenance responsibility |
| RC-14 | Public demonstration and evidence respect public construction and exclusion law | Synthetic provenance and the required mechanical and human reviews, kept distinct |

**Three limits on these drafts, stated so they are inherited rather than rediscovered.** RC-07 and RC-09 may never promise recovery from a lost passphrase or erasure of copies outside the build's control. **The lawful form of any evidence that depends on a person's comprehension is unsettled:** the standing law admits synthetic-persona testing and bars any evaluation channel to a person (ADR-0012; ADR-0034 decision 10), and W9-D6 must settle the form before RC-01, RC-03 or RC-12 can be accepted. And existing suite results remain evidence about their own subject: they establish nothing about an application that does not exist.

## 16. The proposed programme beyond W9 — named, not opened

Recorded so the release contract can be read against a whole. **These are planning labels, not phases.** No runway, brief, registry entry or authority exists for any of them; none is opened, scheduled, designed or assigned work by this runway; and each could open only through its own three-document gate.

| Proposed label | Proposed purpose |
| :---- | :---- |
| W10 | Runnable foundation — the permitted reference build, installation, storage configuration and a deterministic demonstration |
| W11 | Supported room workflows — one complete task per room within accepted scope |
| W12 | Governed integration kit — versioned contracts, deterministic reference doubles, conformance evidence |
| W13 | Integrated assurance — the assembled build assessed, with recovery, migration and adversarial exercises |
| W14 | Trial with synthetic material, and the release decision |

**No future phase is assigned an obligation merely because this runway wanted somewhere to put it.** Security, recovery, accessibility and maintenance are W9 scope questions from the first deliverable, not matters deferred to a later label.

## 17. Public-safety considerations

Generic and structural wording throughout — component, capability, edge, grant, room, task, criterion, evidence. No real health data, no clinical examples, no identified person, no vendor, product or model named, no URLs, no private lineage. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. **A release contract is the phase's principal public-safety surface: it is where a capability can be claimed in words before anything supports it, and W9-D1 fixes the boundary before any criterion is accepted.**

## 18. Next gates

**The W9 entry gate**, three documents and three acceptances: **(1)** the W8 closure record, published and remotely verified — **satisfied** · **(2)** this runway, reviewed and accepted — **satisfied by this record on its acceptance** · **(3)** the first W9 deliverable brief, reviewed and accepted — **lands behind this record**. Acceptance of this runway authorises **W9 briefs only**.

**The gate this landing succeeds.** `W8-CR` §14 left the live gates of the closure record's proof CC7 — the W8-D7 entry set, and the refusal of any registry entry of a later phase — in place *"until a later accepted act lawfully succeeds them"* under the three-document pattern. This runway's landing is that act and no more: CC7's W8-D7 entry set and its no-later-phase limb stay proven at the W8 closure commit, by an exact transformation of a fixed pre-image, and no other byte of any W8 proof moves.

**The gate this landing leaves, and its proofs.** One present-state gate succeeds CC7's no-later-phase limb, and this runway's own proof module, `tests/test_w9_runway.py`, holds it: every registry entry's phase is one of W0 to W9. It refuses an entry of any later phase, it does not refuse an entry of W9, and it decides nothing else about any entry; it stands until a later accepted act lawfully succeeds it under the same three-document pattern. CC7's W8-D7 entry-set limb is left historical, with no present-state successor. The module's obligations are five, each mechanical: **AR1** this runway's bytes are the reviewed text, in its draft or its accepted status form · **AR2** the CC7 succession is the exact reviewed transformation, and the succeeded claim holds at the W8 closure commit · **AR3** the registry and the board change exactly · **AR4** the present-state gate · **AR5** the census. **This landing's census is exactly five paths:** NEW `docs/phases/W9-runway-application-release-scope-and-contract.md` · NEW `tests/test_w9_runway.py` · MODIFY `tests/test_w8_closure_record.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. A green run of these proofs establishes mechanics and carriage only: it decides no boundary, scope or release criterion, performs no human review duty, and accepts nothing.

**Named and not opened:** model contact in any form · any real-person adoption, which remains a separate governed authority outside this repository · any device source · any implementation · the correction and conversion ceremonies carried from W6 · the three derivative repairs · the dormant doors · and every proposed label of §16. **Naming these opens none of them.**

---

*W8 taught the instrument to say "not enough evidence". W9 asks the same honesty of a release: to say what it is, what it is not yet, and what would have to be true before anyone was told otherwise. Nothing is built here. What is built later will be built against a contract that was written while there was still nothing to defend.*
