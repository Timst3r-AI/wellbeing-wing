# W9-D1 — Application Boundary Doctrine: Opening Brief

**Status:** Accepted by human reviewer, 2026-11-12. **Effective only on publication and remote verification.**
**Date:** November 2026
**Phase:** W9 — Application Release Scope and Contract
**Deliverable:** W9-D1 — Application boundary doctrine
**Identity:** `W9-D1-BDB`, type `phase-brief`
**Position:** gate document three of the standing W9 entry gate. On its acceptance, publication and independent remote verification — and only then — the entry gate is complete at three documents and three acceptances, and **W9-D1 opens for doctrine work only, and nothing beyond W9-D1**. This brief assigns the boundary question. It answers no part of it.
**Derived public baseline:** `1fcd893b3b0261d6d452fbf160d60e89455d6245`, the published and remotely verified W9 runway landing
**Governed by:** the W9 runway (`W9-AR`), whole — its §1, §5 question 1, §6 and §6.1, §7 to §9, §11 to §14 and §17 especially; the W8 closure record (`W8-CR`) as the carried-state authority, its §9 inventory whole; **ADR-0046, whole — carried, never reinterpreted by this brief**; W2-D4 and ADR-0007, the laws ADR-0046 carries; ADR-0034 decisions 10 to 12, 34 and 37; ADR-0047 decisions 3, 9 and 24; ADR-0051; ADR-0052; the W3 runway (`W3-AR`) §5; ADR-0004, ADR-0006, ADR-0009, ADR-0010, ADR-0011 and ADR-0012; W1-D1 and W1-D2; the checklist (`W2-D3`) rules 2, 4, 5, 7 and 8; ADR-0003
**Tier at landing:** J — Judgment. Full ceremony.

---

**The runway put one question ahead of every other: what may a public reference application be, and what may this repository hold once runnable application code exists? This brief assigns that question to a decision record. It says what the record must read, what it must answer, the forms an answer may take, and what the record may not do in order to reach one. It does not answer. It selects no reading of any accepted law, authorises no doctrine record, no application, no directory, no dependency and no model contact, and changes the standing of nothing carried from W8.**

## 1. What this brief opens, and what it does not

1. On acceptance, publication and independent remote verification, the W9 entry gate moves from two documents of three to **complete — three documents, three acceptances** (checklist rule 8) — and **W9-D1 opens for doctrine work only**.

2. Effective does **not** mean: that the doctrine record exists or is accepted · that any boundary question is answered · that any reading of ADR-0046 or of any other accepted law is selected · that W9-D2 to W9-D7 are open · that any scope, workflow, integration posture or release criterion is accepted · that any implementation, directory or dependency crossing is authorised · that model contact is authorised · or that any later phase is opened, scheduled or assigned work. The doctrine record lands only as its own separately authorised candidate behind this brief.

3. The eventual doctrine record carries the proposed identity **ADR-0062** — the next free decision-record number at this baseline, allocated at its own landing and not reserved here. It does not exist at this landing. No earlier analysis, planning summary or preparation note is repository authority for it or a source to be landed: the doctrine candidate is derived from the published corpus and this brief, after this brief is effective.

4. **Until the doctrine record is accepted, published and remotely verified, no boundary answer exists for any later deliverable to rely on** (`W9-AR` §6.1). A doctrine record still in review gates nothing and supports nothing, and no wording of this brief stands in for it.

## 2. The question, as the runway assigns it

5. The question is `W9-AR` §5 question 1, carried here unchanged: ***"What may a public reference application be, and what may this repository hold once runnable application code exists?"*** The runway calls it *"a doctrine question"* that is *"W9-D1's — decided by its own record before any other deliverable relies on an answer, and not decided by this runway."* It is not decided by this brief either.

6. The runway's row for W9-D1 (`W9-AR` §6) fixes the shape of the answer: **a decision record**, answering the question **from the sources**, that settles four things — **(a)** what a public reference application may be; **(b)** how the constructional test and the closed exclusion list bind application code, demonstrations, examples and release evidence; **(c)** the standing invariant by which anything beyond the public reference build is referred to, carried unchanged; and **(d)** whether any part of the proposed release needs a governing amendment or a different home. **It lands before any later deliverable relies on the boundary, and it is docs only.**

7. The question comes first because of where a release can go wrong before anything is built: *"A release contract is the phase's principal public-safety surface: it is where a capability can be claimed in words before anything supports it, and W9-D1 fixes the boundary before any criterion is accepted"* (`W9-AR` §17).

## 3. The accepted positions the record must read together

8. Every position in this section is accepted and in force. They are set beside each other because the runway sets them so (`W9-AR` §5 question 1). **This brief quotes them. It ranks none above another, reconciles none with another and selects no reading of any of them.**

| Source | What it holds |
| :---- | :---- |
| ADR-0046 decision 3 | *"Public W7 is synthetic-only by construction, never by scrubbing."* Derivation from any real person's content is prohibited, and *"There is no de-identification pathway in W7, because there is no identification to remove."* |
| ADR-0046 decision 4 | *"The test is constructional, not custodial. A W7 artefact, path, field, or process that could carry real-person content is unlawful regardless of whether it currently does."* *"A field that would accept a real transcript is a defect on the day it is defined, not on the day it is filled."* |
| ADR-0046 decisions 11 and 12 | The closed exclusion list of eleven families, ending *"or anything that would turn the public Wing into a live personal instrument"*, and *"The list is growable only, never narrowable."* |
| ADR-0046 decision 2 | *"A later record may extend the lists here through its own ceremony; none may narrow them by convenience."* |
| `W9-AR` §5 and §8 | That law was fixed for public W7, carried forward by the W8 runway and carried again by the W9 runway, *"under ADR-0046 carried unweakened"*; and *"No W9 deliverable widens a public field, source, processing class or permission to make a proposed release fit"*. |
| `W3-AR` §5 | *"no real health records anywhere — not in the repo, tests, fixtures, logs, screenshots, or docs; the synthetic-only discipline extends into the runnable era via the dev-artifact policy, and a real user's real data exists only in that user's local runtime, never in any project artifact."* |
| ADR-0007 decisions 1 and 2 | *"Synthetic-only, everywhere, always"* for every development artefact, local debugging included; and *"Paste is publication."* |
| ADR-0009 decisions 1 and 2, with the engine's own account | *"Import stores bytes plus user-supplied provenance. Nothing else."* *"Zero content interpretation at import."* The store seals one blob under a key its caller supplies. The sealed engine therefore accepts whatever bytes its caller supplies (`W9-AR` §5). |
| ADR-0010 decisions 1 and 4 | *"Tests simulate; nothing real becomes Approved until real review surfaces exist"*, with a standing assertion that no Approved-status item exists in any non-test store. |
| ADR-0011 and ADR-0012 | Each lists real-data use among what it blocks, and ADR-0011 is to be *"Accepted before real data enters any real vault"*. |
| ADR-0034 decisions 10 and 12 | Every evaluation artefact is synthetic-only, *"and no evaluation channel to a person exists or may be created"*; any future evaluation involving a real person's content would need its own governed authority, *"which nothing here creates or anticipates."* |
| ADR-0046 decisions 14 to 17 | The fixed invariant clause, the sentence-position grammar that alone may vary, the non-naming law, and *"Stating the clause creates nothing."* |

9. **The corpus has already held some of these together in practice, and the record must establish how, from the published record and not from assumption:** the sealed engine and the runtime were published under the synthetic-only discipline, and ADR-0046 was accepted while both stood in the tree. What that history shows about the reach of the constructional test, and what it does not show, is for the doctrine record to establish with citations. This brief draws no conclusion from it.

## 4. Required doctrine assignments

The doctrine record must settle all of the following. **Each is an assignment, not yet law, and none is answered here.**

### 4.1 The terms of the boundary

10. Define, by what each thing is and never by what it is called, the terms the boundary turns on: **the repository** and **a project artefact** (`W3-AR` §5; ADR-0007); **the public reference application** and **a reference build** made from it; **an installation**, and the **local runtime** of the person who runs one (`W3-AR` §5); **a demonstration**, **an example** and **a walkthrough**; **release evidence**; and **a channel** — any path by which bytes could travel from an installation to the project or to anything the project controls. Each definition is drawn from the sources. Where the sources do not close a term, the record says so and does not close it by preference.

### 4.2 The reach of the constructional test

11. Settle, from the sources, what ADR-0046 decision 4 binds once its subject is an application: the tracked bytes and the fields they define; the same fields as they stand in a build made from the repository; and the same fields as they stand in an installation's local runtime. The record must read decision 4 **whole**, beside the growable-only exclusion list and the non-naming law, and beside the older distinction between a project artefact and a person's local runtime (`W3-AR` §5; ADR-0007 decision 1; ADR-0009; item 9). **It may not read the test down for the convenience of the proposed release, and it may not read it up to make the proposed release impossible by assertion.**

12. **At least two readings are open on the published text, and neither is presumed.** On one, the law binds what the repository, and any channel the project controls, may hold. On the other, the constructional test reaches an application's own fields wherever they run. The record tests each against every source of section 3 and adopts neither by preference; it may find that one holds, that each holds in part, that a further reading is the right one, or that the published sources do not decide. **Whichever it finds, it shows the finding from the sources.**

### 4.3 The exclusion list, read against an application

13. Read each of the eleven families of ADR-0046 decision 11 against each class of thing an application release would add to the repository or publish from it — code · configuration and default values · packaging · logs and diagnostic output · demonstrations, examples and walkthroughs · documentation · release evidence · and the repository's own commentary — and state what each family forbids there, so that the record answers, class by class, what this repository may hold once runnable application code exists. **No family is read down, shortened or softened** (decision 12). A gap the record finds is a candidate **extension** under the record's own ceremony (decisions 2 and 12), never a candidate exception.

14. Give the last family — *"anything that would turn the public Wing into a live personal instrument"* — a reading drawn from the sources and not from the proposed release, including **what "the public Wing" denotes once a build can be made from the repository**. If the sources do not fix that meaning, the record says so (item 23).

### 4.4 Demonstrations, examples and captures

15. Settle whether, and how, the following bind demonstrations, examples, walkthroughs, default content and any capture of a running build: the closed three-origin set and its bar on a fourth origin (ADR-0046 decisions 7 and 8); **no-recirculation** (decision 9); **capture is publication**, checked at capture time (decision 5; ADR-0007 decision 2); the bar on content strings in the repository's own commentary (decision 6; ADR-0007 decision 6); the bar on machine-identifying detail (decision 11; ADR-0007 decision 4); and **declarability as the admission condition** (decisions 19 to 22), with the synthetic marker of W2-D4 §4 as its precedent. The record states what such an artefact must be able to declare about itself in order to land. **It authors none, and it defines no file, field or schema** (ADR-0046 decision 21 is the precedent for deciding a capability without deciding its shape).

### 4.5 Release evidence

16. Settle which accepted laws bind evidence about a build that would be retained in the repository or published from it — ADR-0034 decisions 10 to 12, 34 and 37 and ADR-0007 above all — and state what follows for the forms such evidence may take. **The record fixes the boundary inside which W9-D6 later settles form; it does not settle form.** In particular the lawful form of any evidence that depends on a person's comprehension stays assigned to W9-D6 exactly as `W9-AR` §15 leaves it, and no draft criterion is accepted, amended or ranked by the doctrine record.

### 4.6 The invariant, carried unchanged

17. Carry ADR-0046 decisions 14 to 17 **unchanged**: the clause, the permitted sentence-position grammar and nothing else, the non-naming law, and the rule that stating the clause creates nothing, opens nothing and establishes no dependency. Settle how public records, and any text an application or its published materials would carry, refer to anything beyond the public reference build: **in the fixed form and in no other.**

18. The record decides the boundary **from the public side only**. It does not name, describe, locate, date, specify, implement, schedule or depend upon the external side the fixed invariant refers to (ADR-0046 decision 16), and it does not design, describe or prepare any real-person use (`W9-AR` §11). Where an answer reaches the edge of the public side, the record says so in the fixed form and stops.

### 4.7 Where the public side ends

19. State, from the sources, where the public side ends: what the standing records permit a public reference application and its published materials to **be, hold and claim**, and what they refer elsewhere. The record reads together `W3-AR` §5; ADR-0010 decisions 1, 3 and 4; the blocks that ADR-0011 and ADR-0012 place on real-data use; the rule that a person's access to, export of and erasure of their own records are never consent-gated (`W9-AR` §7; W1-D1; W1-D2); and the fixed invariant. `W9-AR` §3 speaks of tasks completed *"with synthetic material"*, and the record may not treat that phrase, or any other wording of the runway's proposals, as having settled the point. **If the sources leave it open, the record says that they do** (item 23).

### 4.8 Channels

20. State what the standing law holds about any channel from an installation to the project: telemetry, crash and diagnostic reports, update checks, support and issue text, contributed examples and submitted evidence are the classes to be read, against ADR-0006's telemetry silence proven by observation, ADR-0004, ADR-0007 decisions 2, 6 and 7, and the exclusion list. **The record states law. It designs, selects and authorises no mechanism**, and it makes no statement that any channel exists.

### 4.9 Boundaries the record carries and does not redecide

21. Carry as part of the boundary, each exactly as published and none redecided: the model-contact and device boundary of `W9-AR` §9 — no model contact, no provider or model class, no transport, no credential, no model binary, no device-originated data — and the fences of `W9-AR` §7. **Integration posture is W9-D5's, the application shell is W9-D3's, workflows are W9-D4's and the release contract is W9-D6's**; the doctrine record supplies each of them a boundary and takes none of their decisions.

### 4.10 The fit of the proposed release

22. For each element of the proposed release that presupposes a boundary answer — the north star of `W9-AR` §3, the common journey and the four room tasks of §10, and the draft criteria of §15 so far as each presupposes one — state **exactly one** of the findings of item 23, with its sources. The record assesses boundary fit only. It accepts, rejects and amends no scope, workflow or criterion, and the proposed labels of `W9-AR` §16 are assessed for nothing.

23. **The findings are closed at five, and none is presumed:**
    - **within the standing law**, as the record reads it from the sources;
    - **within the standing law only under a stated prohibition or condition** that the record itself adds as an extension, by its own ceremony (ADR-0046 decisions 2 and 12);
    - **not within the standing law without a governing amendment** — the record reports the exact issue, the law concerned and the route for deciding it, and **does not take that decision** (`W9-AR` §8);
    - **not within this repository on any reading** — reported as needing a different home, in those words and no more (item 18);
    - **not decidable from the published sources** — stated as such, with what a decision would need.

24. **A finding that the published sources do not decide is complete and lawful**: it is not a failure and not a pending state. No finding is reached by elimination, by momentum, by the convenience of the proposed release, or because a proposed later label would otherwise have nothing to build on.

### 4.11 Decidability and proof obligations

25. For every rule the record states, declare honestly whether a machine can decide it, under the decidability discipline ADR-0046 decisions 27 to 30 and ADR-0047 decision 24 carry: *"an obligation is not called mechanical until a working check has been demonstrated against real bytes."* Specify each mechanical obligation with what fails it and the landing that would implement it. An obligation over artefacts that do not yet exist is specified and assigned to the landing that first creates such an artefact, and is *"a debt, not a receipt"* (ADR-0046 decision 28). **Review-only duties are named review-only and are never reported as mechanical results.**

26. P1 — the exact form of the invariant clause — continues to hold over every tracked text. **P2 remains review-only in full**, and no green result is evidence for it in any degree (ADR-0046 decisions 29 and 30). The record weakens neither and mechanises nothing that those decisions hold cannot be mechanised.

### 4.12 Inheritance

27. State what the record hands W9-D2 to W9-D7 as fixed input, consumed and not re-decided by them, and what it does not touch. **A later deliverable may extend the record's prohibitions through its own ceremony; none may narrow them by convenience.**

## 5. How the record may not reach an answer

28. The doctrine record may not: narrow, shorten, soften or read down any accepted law, list or fence — *"A W7 landing that would be easier if an item were absent is the exact circumstance the list exists for"* (ADR-0046 decision 12) · widen a public field, source, processing class or permission (`W9-AR` §8) · answer from a planning summary, from phase closure, from a count of proofs or from the wording of this brief (`W9-AR` §5) · describe a capability as existing where the source shows design only, or state what exists without a source citation (`W9-AR` §13 and §14) · amend, correct or reinterpret any accepted record — a needed change is reported with its route and decided, if at all, by its own record under the two-tier rule (checklist rule 2) · name, describe, elaborate or depend upon the external side the fixed invariant refers to, or design, describe or prepare any real-person use · decide scope, the application shell, any workflow, the integration posture or any release criterion · decide the E9 export format, vault layout, profile export, whole-vault export or recovery codes (`W9-AR` §11 and §12) · create any fixture, example, demonstration, application artefact, directory, dependency or manifest · turn the W8-D5 finding into a readiness finding or the W8-D6 decision into a permission · state whether model contact occurred · or make any diagnostic, therapeutic, crisis, legal, `certif-`, `complian-`, production-readiness, safety, correctness or approval claim.

29. **A boundary that is convenient is not thereby wrong, and a boundary that is inconvenient is not thereby right.** The record is judged on whether each finding follows from the sources it cites, and on nothing else.

## 6. The governing sources, pinned

30. **These are pinned entry points, not a choice of which law governs.** Every effective governing record binds the doctrine record whether or not it is listed here. Each source is read at the bytes its registry entry binds at the baseline the doctrine candidate is derived from, and a mismatch is a stop (item 34).

| Entry point | Read for |
| :---- | :---- |
| `W9-AR`, whole | The question, the row, the gate discipline, the fences, the boundaries, the non-goals, the tripwires and the quality gates |
| `W8-CR` §9 and §11 | The carried inventory, each row at its published standing, and what closure does not mean |
| ADR-0046, whole | The constructional test, the origins, the exclusion list, the invariant and the non-naming law, declarability, the proof obligations and their decidability |
| ADR-0052 | The decomposition of exclusion-list conformance into the mechanical P4a and the human P4b |
| W2-D4 and ADR-0007 | Synthetic by construction; the marker precedent; paste is publication; machine-identifying detail; commentary |
| ADR-0034 decisions 10 to 12, 34 and 37 | Evaluation artefacts, the bar on any evaluation channel to a person, and the bar on presenting results as claims |
| ADR-0047 decisions 3, 9 and 24; ADR-0051 | Contact defined by provenance; the seven conjunctive preconditions; the standing public posture |
| `W3-AR` §5; ADR-0004; ADR-0009; ADR-0010; ADR-0011; ADR-0012 | The project-artefact and local-runtime distinction; residue; the import boundary; the review posture; the blocks on real-data use |
| ADR-0006 | Platform doctrine, telemetry silence proven by observation |
| W1-D1 and W1-D2 | The flow whitelist; rights are not grants |
| `W2-D3` rules 2, 4, 5, 7 and 8; ADR-0003 | The two-tier rule, the fences, the entry gate and the ceremony tiers |
| The engine's own account, and the repository as it stands at the baseline | What is implemented, as distinct from what is designed |

## 7. Carried states and boundaries

31. **Carried states, named and untouched — no cleanup by proximity.** The whole inventory of `W8-CR` §9 stands exactly as that record carries it, each row at its published standing, and W9-D1 reopens, solves and reclassifies none of it. The four positions `W9-AR` §2 binds on every W9 deliverable bind here unchanged: the W8-D5 finding is undetermined; the W8-D6 decision is a decision that authorises nothing, its separate instruments unopened and its authority question unanswered; ADR-0047 precondition 3 is outstanding in its lawful resting state; and ADR-0058's reservation stands — the published records classify no exchange and state neither way whether model contact occurred. The three named stale derivatives stay named and unrepaired.

32. **Model-contact and device boundary, carried whole** (`W9-AR` §9): this deliverable authorises no model contact and must not call a model, select a provider or model class, build a transport, prepare a credential, author a prompt for contact, introduce a model binary, or treat future contact as inevitable; and it admits no device-originated data and designs no device source. The hosted class stays closed; E12 stays reserved; E10, Z4 and Z5 stay dormant.

33. **Public/private boundary, carried whole** (`W9-AR` §8). No record of this deliverable may contain: real-person data of any kind · any identified person's room, health, movement, food, device, contemplative, or journal material · real wearable or device data · private relationship or lived-interaction material · private model transcripts · credentials, tokens, keys, secrets, or private configuration · machine-identifying detail beyond permitted class-level information · a model binary · a real-person evaluation channel · private adoption implementation detail · or anything that would turn the public Wing into a live personal instrument. **Synthetic-first remains by construction, never by scrubbing**, and the external side is named in exactly one way:

> **Any real-person adoption is a separate governed authority outside this repository.**

## 8. Builder autonomy and stop conditions

34. Within this brief the builder owns the route: document structure, section order, exact prose, the order of work and mechanically equivalent choices, with no routine relay. **Mandatory stops:** the public head differs from the expected baseline · a consumed source does not match the bytes its registry entry binds · scope must change · a governing source conflicts with this brief · an assignment cannot be met without narrowing an accepted law or widening a public permission · a finding would require amending an accepted record · any wording would say more about the external side than the fixed invariant says · a fixture, example, demonstration, implementation artefact, directory, dependency or manifest becomes necessary · a model, provider, credential, transport or device surface becomes necessary · a capability would be described as existing where the source shows design only · published history would require alteration · a fact, judgment, date or authority exists that only the human reviewer can supply · or a proposed solution would convert a human judgment into a mechanical result. Everything else is a builder decision.

35. A stop is reported, never absorbed. **The record does not resolve by drafting what it was required to stop on.**

## 9. The doctrine landing, proposed

36. The doctrine landing, authorised only after this brief is effective and only by the human reviewer's separate instruction, is proposed as **docs only, as the runway's row states**: the doctrine record (proposed identity ADR-0062) · `governance/registry.json` · `docs/phases/README.md`. The W9 gates of `W9-AR` §14 bind it: the placeholder probe over every existing check before its census is fixed, every refusal reported and none absorbed; any proof succession an exact transformation of a fixed pre-image; no capability claim without a source citation; and no implementation artefact.

37. **This brief authorises no proof module for the doctrine landing and presumes none.** Proof obligations the record specifies are assigned by the record to the landings that will bear them (item 25). Whether any proof should accompany the doctrine record itself is a census question for that candidate's own review and the human reviewer's own instruction, and a proof, if one is ever authorised, covers structure and carriage only: **no mechanical proof may claim to establish a boundary judgment.**

## 10. Acceptance criteria for the doctrine record

38. The doctrine candidate is ready for review when: the terms of item 10 are defined from the sources, or stated as not closed by them · the reach of the constructional test is settled with citations, or stated as not decidable, with each open reading tested and none adopted by preference · each of the eleven families is read against each class of item 13 with none read down · the last family and "the public Wing" have a sourced reading, or a stated absence of one · demonstrations, examples, captures and release evidence each have their binding law stated, with no artefact authored and no shape defined · the invariant and the non-naming law are carried unchanged · the edge of the public side is stated from the public side only · the law on channels is stated and no mechanism designed · every element of item 22 carries exactly one finding of item 23 with its sources · every needed amendment is reported with its route and none is taken · every rule declares its decidability, with review-only duties named as such · the inheritance of item 27 is stated · no accepted law, list or fence is narrowed and no public permission widened · no carried state is touched · and no statement describes as existing anything the source shows as design only.

39. **A complete W9-D1 is doctrine complete, not capability begun.** It builds nothing, selects nothing and accepts no part of any release. W9-D2 still requires its own brief.

## 11. Human acts, and the judgments no record supplies

40. **Owed by the human reviewer at each W9-D1 landing, and performed by no machine result:** **P2**, the non-naming review over the exact candidate (ADR-0046 decision 27, review-only in full); **Q3**, the no-contact-asserted review over the exact candidate (ADR-0047 decision 24, review-only in full); and **a fresh P4b act** over the exact candidate across all eleven families of ADR-0046 decision 11 (ADR-0052), reported separately from the mechanical P4a and never inferred from it. Acceptance is the human reviewer's dated act, and publication is only as the ADR-0056 public project identity.

41. **Judgments the doctrine record may identify and may not supply:** whether a reported amendment is pursued, and by what record · whether a different home is sought for anything reported as needing one · whether an extension the record proposes is accepted · and whether the proposed release is changed to fit a boundary, or left as it is. **Silence is never a decision, and a green suite is never an acceptance.**

## 12. Positions this brief proposes for the human reviewer's acceptance

42. Accepting this brief accepts these positions and no others: **(a)** the identity `W9-D1-BDB` and this file name; **(b)** one decision record for W9-D1, proposed identity ADR-0062, allocated at its own landing and not reserved; **(c)** the twelve assignments of section 4 as the whole of what the doctrine record must settle; **(d)** the two readings of item 12 named as open, with neither presumed and others admitted; **(e)** the five findings of item 23 as the closed set, with "not decidable from the published sources" a complete and lawful finding; **(f)** that the doctrine record reports a needed amendment with its route and takes no amendment itself; **(g)** that the runway's "docs only" is read as written for the doctrine landing — record, registry and board, with no proof module authorised or presumed by this brief; and **(h)** the landing scope of section 13. **No position here is a boundary answer, and accepting them selects no reading of any accepted law.**

## 13. This landing

43. **This landing's census is exactly three paths:** NEW `docs/phases/W9-D1-application-boundary-doctrine-brief.md` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. It adds no proof module and no other file.

44. **No proof succession occurs at this landing and no present-state gate is added.** The one present-state gate the runway's landing left — every registry entry's phase is one of W0 to W9, held by `tests/test_w9_runway.py` — stands unchanged and is satisfied by this brief's entry, which is of W9. The runway's other proofs read the runway's own landing and are untouched. The standing registry-consistency proofs, the exact-form proof of the invariant clause and the public-safety scan bind this landing as they bind every landing. **A green run of any of them establishes mechanics and carriage only: it decides no boundary, performs no human review duty, and accepts nothing.**

## Public-safety note

Generic and structural wording throughout — repository, artefact, application, build, installation, demonstration, evidence, channel, boundary, finding. No real health data, no clinical examples, no identified person, no vendor, product or model named, no URLs, no private lineage. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. The external side is referred to only in the fixed form and is never elaborated. **Nothing here is, or may be presented as, a safety, health, clinical, legal or regulatory claim of any kind.**

---

*The gate closes with this document, and what it opens is small on purpose: permission to write down, before any application exists, where the public side ends. The runway promised a contract written while there was still nothing to defend. This is the first clause of it, and it is a question.*
