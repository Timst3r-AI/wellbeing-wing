# W7 — First-Contact Governance and Synthetic Model Evaluation

## Phase Runway / Alignment Brief

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction.
**Date:** August 2026
**Phase:** W7 — the first phase in which generated language may be governed (the phase after the Surface Era)
**Governed by:** W0 Constitution; the accepted W1–W6 corpus whole; the W6 closure record and its carried inventory; ADR-0033 (model access) and ADR-0034 (behavioural evaluation architecture) above all; ADR-0038 through ADR-0045; the W3, W4, W5 and W6 runway precedent
**Tier at landing:** J — Judgment (phase runway; full ceremony when landed)

---

**Six phases built a Wing that holds without reading, refuses without arguing, watches without judging, and shows without claiming. Not one of them ever heard a sentence it had not written itself. W7 is the phase where generated language is finally allowed near the governed world — and the discipline is not enthusiasm but plumbing: what must already be true before a generated sentence may be written into a public record at all. The model is not the milestone. The governed handling of model output is the milestone.**

## 1. Status and boundary

**This runway is gate document two** of the standing three-document entry gate, and it authorises **W7 briefs only** — never capability, never contact, never execution. *Opening is effective on publication:* while this runway's commit remains local it is not in force; the gate-document-two state takes effect only once it is published on the default branch and that authority is independently verified against the remote.

**W7 is public, synthetic, and bounded.** It is the governed, demonstrable half of the model era. **Any real-person adoption is a separate governed authority outside this repository**, and no W7 record names, describes, implements, or depends on it.

## 2. W6 closure baseline

W6 — Surface Era — is **complete and closed**, sealed at `508ea5729d05ae838b15761d4d56ecc65bc61f91`, closing **complete, not perfect**: two correction-needed findings open, three W6-owned stubs ceremony-bound and unconverted, seven carried questions alive, eleven Lane C rows external, four applicability records unresolved. W7 inherits that inventory **named and unresolved** (§12) and resolves none of it by existing.

W7 also inherits the standing state: **494 deterministic proofs green, 229 files scanning to zero findings, zero dependencies since W3, and no model contacted in any phase to date.**

## 3. North star

**Generated text may enter the public Wing only as synthetic, governed evaluation evidence. It may be observed, preserved, compared, routed, and reviewed. It may not become authority, advice, truth, safety evidence, approval, or a decision about any person.**

The phase's honest boundary, stated once so no later record has to invent it: **W7 does not prove the Wing is safe with a model.** W7 asks only whether a model can enter a governed room, be observed honestly, fail without being laundered, and leave behind reviewable evidence.

## 4. Public/private boundary

**The public repository proves the pattern. Everything lived is elsewhere.** In public records the external side is named exactly one way and never otherwise:

> **Any real-person adoption is a separate governed authority outside this repository.**

**No public W7 record may contain:** real-person data of any kind · any identified person's room, health, movement, food, device, contemplative, or journal material · real wearable or device data · private relationship or lived-interaction material · private model transcripts · credentials, tokens, keys, secrets, private configuration, or machine paths · a real-person evaluation channel · private adoption implementation detail · or anything that would turn the public Wing into a live personal instrument.

**This boundary is the doctrine's own line, not a new constraint.** ADR-0034 A4 decision 10 already requires every evaluation artefact to be synthetic-only by construction and forbids any evaluation channel to a person; decision 12 already states that evaluation involving a real person's content "would require its own separate governed authority." W7 does not create that authority and does not anticipate it.

## 5. Synthetic-only law

**Public W7 is synthetic-only by construction, never by scrubbing** — the W2-D4 discipline, carried unweakened into a new artefact class. Every prompt, probe, fixture, scenario, capture, record, and review input in W7 is synthetic, fixture-derived, or governed public-record material. **A W7 artefact that could carry real-person content is unlawful regardless of whether it currently does.**

## 6. Generated-output artefact law

**Generated model prose is a new governed artefact class**, and it is the reason this phase exists. **W5 deltas were structural** — content-free references, event sequences, item ordering. **W7 deltas are textual**: a paired-variant evaluation may hold two generated answers side by side, and the difference between them may itself be the finding.

**Nine binding properties of the class**, to be made law by W7-D2 before any harness produces a record: synthetic-only by construction · never real-person content · both paired variants captured whole · no machine-selected winner · no omitted variant · no generated text promoted into a conclusion · every delta routed through human review unless a recorded human disposition exists · scan-clean or governed by an explicit bounded exception · public-safe enough that a stranger can inspect every byte.

**The non-authority ceiling, to be carried inside every generated-output record:**

> **Generated output is evaluation evidence only. It is not truth, advice, diagnosis, therapy, safety evidence, correctness evidence, clinical validity, legal conformance, production readiness, approval, or a decision about any person.**

**One consequence named now, because it is the hardest and W7-D2 must decide it rather than discover it:** every lawful scan exception this repository has granted was over text a *human wrote* — enumerable in advance, named in a record, proven bounded by a test that fails if it widens. **Generated prose cannot be enumerated in advance.** So the exception mechanism must invert: generated output is scanned like any artefact, and **a finding inside generated output is itself a governed event with a disposition path** — the record does not land, or it lands with the finding recorded and the text bounded or excluded. **It is never silently allowlisted.**

**A second consequence, this one favourable:** W6 already built the renderer for this shape. The review surface displays routed deltas with both captures whole, differing surfaces named, no machine conclusion, and no selected variant absent a human record. Those deltas were structural; the display law is identical for textual ones. **W7 inherits its display layer already governed.**

## 7. Model boundary and dependency crossing — decision space, not decision

**This runway does not decide the model path, and no later record may decide it by momentum.** W7-D3 decides it from source-grounded authority, through a **Tier F crossing record** — never a milestone footnote.

**Named constraints the decision inherits (runway inputs, not preferences):**
- **ADR-0033 keeps the hosted model class unopened**, and the local class **doctrinally constructable only**. Both remain listed among W6's dormant doors. **Nothing in W7 opens either by implication**; opening one would be its own governed record.
- **ADR-0034 A6 decision 17** requires, together, for any model-contacting proof: W5-D2 runtime authority · every applicable Tier F crossing · a named first-contact gate in the deliverable's brief · synthetic-only artefacts throughout · and no hosted access absent a future record.
- **Zero dependencies have been added since W3**, and the approved manifest is fence-tested on every run.
- **No credential, token, key, secret, private configuration, machine path, or model binary may enter the repository**, and the default posture is that none ever does.

**Four options for W7-D3 to assess, each on its own merits:**

| Option | Shape | Assessed against |
|---|---|---|
| **A** | Repository-managed local dependency | Reproducibility gained; first dependency crossing since W3; model-binary and installation boundary risk; heaviest fence movement |
| **B** | Adapter to a local model already running outside the repository | Repository stays governance and harness only; no binary; but lower reproducibility, and the adapter contract must carry its environment assumptions honestly |
| **C** | Manual model-output import under governed record shape | Lowest dependency surface; needs the strongest provenance and anti-laundering rules; execution not publicly reproducible |
| **D** | **No public model contact: synthetic generated-text specimens** | The whole governed-handling pattern proven with authored specimens carrying the properties of generated prose — the W2-D4 discipline applied to the new class. No dependency, no binary, no secret, no dormant door touched, fully reproducible, byte-inspectable. First contact is *governed* publicly and *performed* only under a separate authority |

**Observation offered for the decision, not as the decision:** options A, B and C each require actual generated text to come from somewhere, and the two lawful sources — a local model and a hosted model — are respectively a Tier F crossing and a dormant door. Option D reaches the phase's stated purpose without touching either. **W7-D3 must weigh this from the sources; this runway only ensures the constraint is inherited rather than discovered.**

## 8. Proposed W7 deliverable sequence

Execution order may resequence where dependencies allow (**IDs stay stable**), but the gate discipline of §8.1 is not negotiable.

| ID | Deliverable | Shape |
| :---- | :---- | :---- |
| **W7-D1** | First-contact doctrine and synthetic-only boundary | The doctrine records: first-contact governance, the synthetic-only public law, the external adoption boundary in its exact public wording, the non-goals, and the gate statement that W7 *names* model contact without performing it |
| **W7-D2** | Generated-output evaluation record shape | The schema for records that may contain generated text — paired-variant capture, textual-delta rules, machine-output and human-review fields kept structurally separate, scan and bounded-exception status, per-record public-safety note, and the non-authority ceiling inside every record. **Lands before any harness produces a record** |
| **W7-D3** | Model boundary, adapter, and dependency crossing | The Tier F crossing decision over §7's option space, with credential, configuration, binary, failure, timeout and reproducibility posture. **Lands before any model contact** |
| **W7-D4** | Synthetic harness binding: exam paper and traps | The 26 recorded unknowns as synthetic exam material and the 23 synthetic traps where lawful; probe pairing, paired-variant construction, capture-count rules, and the proof that every input is synthetic. **Lands after D2 and D3 are accepted** |
| **W7-D5** | Synthetic model execution records | Execution of the accepted harness only, producing records in the D2 schema with captures whole and no interpretation beyond event posture |
| **W7-D6** | Human review, honest deltas, and disposition records | The review law and vocabulary, then per-record dispositions. **The law lands before any disposition** |
| **W7-D7** | W7 closure and public/private boundary preservation | Whole-phase closure with the boundary audited, findings unhidden, and the next gates named without opening them |

### 8.1 Gate discipline

The runway lands before any deliverable · **the generated-output record shape lands before any harness produces generated records** · **the model boundary lands before any model contact** · the harness binding lands before execution · the human-review law lands before any disposition · closure lands only after the evidence is published and independently reviewable. **Each deliverable requires its own accepted brief and its own authorisation.**

## 9. Non-goals — what W7 must not do

W7 does not: evaluate any real person · contain any identified person's data, real wearable data, private relationship or lived-interaction material, private model transcripts, credentials, keys, tokens, secrets, private configuration, or a model binary · give clinical advice · make diagnostic, therapeutic, crisis, legal, `certif-`, `complian-`, production-readiness, safety, correctness, or approval claims · implement or open private adoption · build a website, demo product, meditation application, or any device or wearable bridge · perform whole-person-day work · open W8 · convert any pending stub by milestone effect · repair the carried W6 findings or implement the optional audit proof module absent separate authorisation · resolve applicability · convert Tier 3 evidence · or activate E10, Z4, E12/Z5, or the hosted class.

**W7 may use the 26 recorded unknowns and the synthetic traps as exam material. W7 may not convert stubs, repair carried findings, or resolve applicability simply because model contact occurred.**

## 10. Stop-and-report tripwires

Public head mismatch · consumed hash mismatch · any public wording that names the private external phase · any path that can carry real-person content · any model access path requiring secrets in the repository · any dependency added without a Tier F crossing · generated output appearing before the record shape exists · model contact before the model boundary exists · harness execution before the harness binding exists · a human-review disposition before the review law exists · generated output that cannot be made public-safe without distortion · scan rules that cannot distinguish generated prose from barred claims · a record shape that cannot carry both variants whole · model output bypassing the accepted record shape · **any result that is tempting to summarise as the model having passed** · any review disposition that would require clinical expertise or real-person context · any closure wording implying model safety, readiness, correctness, `certif-` or `complian-` status, approval, or private adoption.

## 11. Quality gates for every W7 landing

The standing sixteen: re-ground live authority · verify expected public head · read the governing records · verify consumed hashes · **confirm the synthetic-only boundary** · **confirm no person-specific content** · **confirm no credentials, keys, tokens, or private configuration** · scan before staging · run the relevant proofs · materialise only the measured landing set · stage only intended files · run the full Commit Gate · commit only if exact · push by plain fast-forward only · remote-verify · return a publication packet.

**Plus six W7-specific gates:** no generated output before the schema exists · no model contact before the boundary exists · no harness execution before the binding exists · no human-review disposition before the review law exists · no public record carrying real-person content · **no generated output summarised as proof of safety, correctness, or readiness.**

## 12. Deferred and inherited items

Carried from W6, **named and not solved by this runway or by W7's existence**: the two correction-needed findings and their named paths · the optional standing audit proof module · the three ceremony-bound W6-owned stubs · the six generative-era stubs and the 26 recorded unknowns · the undischarged T12 amendment obligation · the seven carried open questions · Lane C's eleven external rows and four unresolved applicability records · and the dormant doors — E10 and any vendor surface, Z4, E12/Z5, and the hosted class. **W7 addresses only what its own accepted deliverable briefs assign to it; correction and conversion ceremonies remain separate gates.**

## 13. Public-safety considerations

Generic and structural wording throughout — model, probe, capture, record, delta, reviewer, boundary. No real health data, no clinical examples, no identified person, no vendor or model named as endorsed, no URLs, no private lineage. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. **The generated-output class is the phase's principal public-safety surface, and §6 assigns its scan doctrine to W7-D2 before any generated byte exists.**

## 14. Next gates

**The W7 entry gate**, three documents and three acceptances: **(1)** the W6 closure record, published and remotely verified — **satisfied** · **(2)** this runway, reviewed and accepted — **satisfied by this record** · **(3)** the first W7 deliverable brief, reviewed and accepted — **does not exist**. Acceptance of this runway authorises **W7 briefs only**; capability arrives behind its own gates, as it has in every phase before.

**Named and not opened:** W8 · any real-person adoption, which remains a separate governed authority outside this repository · the correction and conversion ceremonies carried from W6 · and the dormant doors. **Naming these opens none of them.**

---

*Six phases of restraint bought the right to try this. A model may one day sit in one of these rooms and say something wrong, and the only thing that will matter is whether the Wing wrote down what was said, kept both answers whole, refused to pick a winner, and handed the whole thing to a human with its uncertainty intact. That is the milestone. The model is only the occasion.*
