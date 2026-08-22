# 0051 — W7 Model-Boundary Decision: No Public Model Contact

**Status:** Accepted by human reviewer, 2026-08-22. Not a build instruction. Authorises no implementation by itself. **Effective only on publication and remote verification.**
**Date:** August 2026 · **Phase:** W7 — First-Contact Governance and Synthetic Model Evaluation · **Deliverable:** **W7-D3** (the Tier F model-boundary decision)
**Position:** the model-boundary decision the W7-D3 opening brief was written to produce. The brief framed four options and ranked none; this record ranks them and selects one. **It performs no contact, creates no artefact of the generated-evaluation class, and opens no later deliverable.**
**Baseline assessed:** `5ce8a923e8a52bf17e9b4c1bd81d1e714c79b135`
**Resolves:** none registered. **This record discharges ADR-0047 precondition 2 on publication and remote verification**, but that precondition carries no registry identifier, so `resolves` stays empty.
**Governed by:** the published **W7-D3 opening brief** (`W7-D3-MBB`), whole; the W7 runway (`W7-AR`) §7 option space and §8.1 gate discipline; **ADR-0046** and **ADR-0047**, consumed whole; **ADR-0033** Part A and decisions 12–14; **ADR-0034** A6 decision 17; **ADR-0048**, **ADR-0049**, **ADR-0050** as the landed W7-D2 law; the **W7-D2-E** proof completion record; **ADR-0003**'s tier ladder.
**Tier:** **F** — ADR-0003: *fence-crossings … anything irreversible or outward-facing … full ceremony plus explicit human reviewer authorisation.* **The architect advised; the human reviewer accepted, 2026-08-22.**

---

**The question is not whether a model would be interesting. It is which model posture this repository can lawfully hold today, under the law as it actually stands, with every dependency the choice creates already owned. Four options were framed neutrally and none was ranked. This record ranks them, and it is written so that the ranking can be checked rather than trusted — the weights are stated before the scores, the scores are argued from sources, and the sensitivity analysis is run hard enough to find the weighting under which the recommendation loses.**

---

## 1. Status and authority

**This is the accepted W7-D3 Tier F model-boundary decision.** It authorises no implementation, no crossing, no dependency, no contact, no specimen, no harness, and no artefact of the generated-evaluation class. **It was accepted by the human reviewer on 2026-08-22, and it takes effect only on publication and remote verification.**

**W7-D3 is open** for brief-governed model-boundary decision work only, its opening brief published and verified at the baseline above. **[law]** This record is the decision that work exists to produce.

### 1.1 Source discipline

Carried from the opening brief unchanged. **[law]** — a landed governing statement, cited. **[mechanism]** — observable behaviour of live repository code or data. **[precedent]** — prior corpus handling; persuasive, not binding. **[inference]** — this record's own reasoning. **No [inference] is law.**

**The analysis is reasoning; the selection is a decision.** Everything in §§5–7 — the weights, the scores, the sensitivity readings — remains **[inference]**, and may be disputed on its merits. **The selected option in §8 is not an inference. It is the accepted Tier F decision of the human reviewer**, taken on 2026-08-22 under ADR-0003's rule that *the architect advises, classifies, and recommends; the human reviewer accepts.* **[law]**

**What acceptance has and has not yet done.** Human acceptance settles *what was decided*. It does **not** by itself move the public governance state: **until this record is landed, published and remotely verified, ADR-0047 precondition 2 remains OUTSTANDING in public authority.** **[law: the standing effective-on-publication rule this corpus applies to every governed record]**

## 2. The decision question

> **What public W7 model or contact posture, if any, may lawfully cross the existing boundary — under what Tier F authority, what `contact_class` posture, what credential, configuration and binary posture, what failure and timeout law, what reproducibility posture, and with what first-contact consequences — while preserving the synthetic-only public boundary and leaving no pre-execution dependency ownerless?** **[law: the published opening brief §3]**

**"None" is a lawful answer** and a complete one, not an abstention. **[law: the opening brief §3, carried]**

## 3. Baseline and controlling law

**Public baseline `5ce8a923e8a52bf17e9b4c1bd81d1e714c79b135`**, four-way verified, registry 108 entries, `governance/generated-evaluation/` absent, no `GER-####` identifier allocated, no ADR-0051, `requirements.txt` at exactly three pinned lines. **[mechanism]**

**Precondition standing at this date:** 1 satisfied · 2 **OUTSTANDING** · 3 **OUTSTANDING** · 4 law in force · 5 closed · 6 **DISCHARGED** · 7 **OUTSTANDING**. **[law: ADR-0047 decision 9, updated by the sealed W7-D2 and the published D3 opening]**

**Part Q as it stands today: no finding-bearing GER is landable.** **[law: ADR-0050 decisions 53–54]** **The `local-wordlist` coordinate seam is unresolved.** **[law: ADR-0050 decision 16]**

**Nine controlling constraints this record may not reopen**, carried from the opening brief §4 and not re-argued here: the model boundary is W7-D3's alone · gate discipline binds · the hosted class is not opened and its future conditions may not be narrowed · the local class is doctrinally constructable only · synthetic-only is constructional · capture is terminal · machine production buys no scan exemption · the seven preconditions are conjunctive and unwaivable · no credential, token, key, secret, private configuration, machine path or model binary may enter the repository. **[law]**

## 4. Stage one — legal eligibility of each option

**No option is eliminated here for being inconvenient.** This stage asks only one question: **could this posture be adopted lawfully today, under the law as it actually stands?**

### 4.1 What counts as contact, decided by the source rather than by intuition

ADR-0047 decision 3(a) defines model contact as **"the act of transmitting any probe, prompt, fixture, or governed material to a model and receiving text back"**, and closes the modality question explicitly: **"Local or hosted, direct or adapted, interactive or batched, one exchange or many, by script or by hand."** **[law]**

**This has a consequence for Option C that materially changes its standing, and it is the most important finding of this stage.** **A manual governed model-output import is model contact.** Performing it by hand does not make it something else, because the definition is keyed to the act, not to the automation. **C is not a low-surface route around the contact gate; it is the contact gate walked through slowly.** **[inference, following directly from the quoted law]**

**This corrects an intuition the architect and the implementer both entertained during pre-decision discussion** — that C's minimal machinery made it materially lighter than A or B. **On the law it is not.** C inherits **every** precondition A and B inherit. **[inference]**

**And C carries one hazard the others do not.** `W7-AR` §7 records that A, B and C **"each require actual generated text to come from somewhere, and the two lawful sources — a local model and a hosted model — are respectively a Tier F crossing and a dormant door."** **[law]** A and B are explicitly local. **C's source is unspecified**, and if it were hosted, the posture is **barred outright** by precondition 5 and ADR-0033 decision 12. **[law]** **C is therefore eligible only in a local-sourced form, and choosing C would require fixing that in the decision itself.** **[inference]**

### 4.2 Eligibility findings

| Option | Eligible today? | On what condition |
|---|---|---|
| **A** — repository-managed local dependency | **Yes, in principle** | Local class only. Requires a recorded Tier F crossing (p2), a named first-contact gate in the performing deliverable's brief (p3), and an accepted harness binding (p7). Requires a `requirements.txt` change, which the deterministic suite treats as **a named fence-crossing** **[mechanism]** |
| **B** — adapter to an externally running local model | **Yes, in principle** | Same three preconditions. No in-repository dependency, but the adapter contract must carry its environment assumptions honestly **[law: `W7-AR` §7]** |
| **C** — manual governed model-output import | **Yes, but only local-sourced** | Same three preconditions, because it **is** contact. **Barred outright if the source is a hosted model** — precondition 5 and ADR-0033 d12 **[law]** |
| **D** — no public model contact, authored synthetic specimens | **Yes — as a selectable no-contact posture under current law** | A specimen is **not** contact — ADR-0047 decision 4 — and decision 5 states plainly that specimens are **"a *lawful* case"**, with the choice reserved to W7-D3. **[law]** **Selecting D performs no contact, but it does not bypass ADR-0047.** The Tier F decision **still accounts for precondition 2**, which is discharged **only** through the proved-empty applicable crossing set of §9; **preconditions 3 and 7 remain OUTSTANDING** in their governed roles. **No precondition is waived, deemed inapplicable, or made not to exist.** |

**No option is eliminated at stage one.** **A, B and C are lawful contact-bearing postures whose contact cannot be performed until the applicable outstanding preconditions are discharged. D is a lawful no-contact posture whose selection still requires W7-D3's Tier F accounting: this decision discharges precondition 2 by proving the applicable crossing set empty, while preconditions 3 and 7 remain outstanding in their governed roles.** **Being un-met is not being unlawful**, and this record does not conflate them — but **no precondition of ADR-0047 “does not arise”**, and decision 11's conjunctive, unwaivable set is not narrowed by any posture selected here. **[law; inference]**

**One thing stage one does establish firmly: A, B and C are legally closer to one another than the option space suggests.** All three are contact. All three trip the same three outstanding preconditions. **The genuine spread between them is engineering surface and evidence quality, not lawfulness.** **[inference]**

## 5. Weighting method

**Weights are fixed before scores are assigned**, so that no score can be tuned to a desired total. **[inference]**

| Weight | Criterion | What it measures |
|---|---|---|
| **30%** | Current-law conformance and Part-Q no-reliance | Fit with the law as it stands, **and** whether the option's value depends on Part Q later relaxing |
| **20%** | Evidence value for W7 | How much the posture lets W7 actually demonstrate |
| **20%** | Public auditability and reproducibility | Can an outside reader re-derive what happened from public bytes |
| **15%** | Boundary expansion / public-private exposure | How much new surface the repository takes on |
| **10%** | Operational and control complexity | How much machinery and procedure must be trusted |
| **5%** | Reversibility and stopping cost | What remains if the phase stops |

Scores are **1–5**, higher is better. **The architect supplied a baseline score set to be tested rather than copied**, and every departure below is argued.

## 6. Scored comparison

| Option | Law 30% | Evidence 20% | Audit 20% | Boundary 15% | Ops 10% | Rev 5% | **Weighted** |
|---|---|---|---|---|---|---|---|
| **A** | 3 | **5** | 4 | 2 | 2 | 2 | **3.30** |
| **B** | 2 | **5** | 2 | 2 | 2 | 2 | **2.60** |
| **C** | 2 | 4 | **2** | 3 | 3 | 2 | **2.65** |
| **D** | **5** | 3 | **5** | **5** | **5** | **5** | **4.60** |

### 6.1 Departures from the architect baseline, and why

**One score changed: C's auditability, 1 → 2.** The architect's 1 scored process reproducibility, which for C is genuinely nil. But C's **artefact** is byte-inspectable once landed and carries its citation, so a reader can audit *what was imported* even though they cannot re-derive *the importing*. **1 understated that. C rises 2.45 → 2.65** and overtakes B. **[inference]**

**Two scores were deliberately left alone in directions that do not favour the recommendation**, and both deserve stating because leaving them alone was a choice:

**A's evidence stays at 5, though there is a real argument for 4.** Under current Part Q, a capture that trips the scanner produces **no published GER** — and A's exposure to that is uncontrolled, because A does not choose what the model says. So A's *realisable* evidence under current law is lower than its *potential* evidence. **The no-reliance rule makes this sharp: if A is scored at 5 on the assumption that the interesting captures will eventually be publishable, that is exactly the reliance on a future Part-Q relaxation that the opening brief forbids.** **[law: the opening brief §11.2]** Scoring A at 4 would drop it to **3.10** and widen D's margin. **A is left at 5 anyway**, giving the strongest contact option maximum credit, with the concern surfaced here and tested in §7. **[inference]**

**D's evidence stays at 3, though there is a real argument for 4.** `W7-AR` states the phase's north star as **"The model is not the milestone. The governed handling of model output is the milestone."** **[law]** Measured against W7's own stated purpose rather than against model-knowledge in the abstract, D's evidence value is higher than 3. **D is left at 3** — the conservative figure, scored against the harsher reading. **[inference]**

**Both departures-not-taken push in the same direction: they make D's win narrower than a partial reading would.** That is deliberate.

### 6.2 What the scores mean, option by option

**A — 3.30, the strongest contact option.** Full credit where it is due: **the best model-behaviour evidence of any practical path**, machinery-attested provenance, and the **highest reproducibility among the contact options**, because a pinned dependency is a thing another party can install. Against it: the **first dependency addition since W3** **[law: `W7-AR` §2]**, direct movement of a three-line manifest the suite fence-tests on every run **[mechanism]**, a local binary and runtime surface, a one-way first-contact act once performed, uncontrolled Part-Q exposure, and a live failure/timeout law to write. **A loses on the weighted total, not on "contact is risky"** — it scores highest of all four on evidence and second on auditability, and still finishes 1.30 behind.

**B — 2.60.** Credit: **no in-repository dependency movement at all**, and real model-behaviour evidence equal to A's. Against it: the repository inherits **environment assumptions it cannot verify or reproduce** — which cuts directly against the reproducibility posture D3 is required to settle — a binary and runtime outside the governed surface, proximity to private configuration, one-way contact, and the same Part-Q exposure. **B's central problem is that it buys A's evidence by paying with the thing D3 must guarantee.**

**C — 2.65.** Credit: **no repository dependency**, a small implementation surface, and **genuinely model-authored text**. Against it: provenance rests on **human attestation** — and ADR-0049 states plainly that **a citation is a claim, not a clearance** **[law]** — the **highest anti-laundering burden** of the four, execution not publicly reproducible, operator procedure inside the trust chain, one-way contact, Part-Q exposure, **and the §4.1 finding that it is contact in full with a hosted-source hazard on top.**

**D — 4.60.** Credit: no dependency, no runtime, no credential, no private configuration, no binary, no contact-bearing path; **full byte inspectability** and the highest public reproducibility; the lowest public/private boundary expansion; **no irreversible first-contact act**; and the ability to **construct difficult specimens deliberately** rather than waiting for a model to produce the awkward case. Against it: §19 below, at length.

## 7. Sensitivity analysis

**A single weight table is not an argument.** Four re-weightings, each chosen to attack the recommendation.

| # | Re-weighting | A | D | Winner |
|---|---|---|---|---|
| 0 | Primary table | 3.30 | **4.60** | D by 1.30 |
| 1 | Evidence 40%, law 15%, audit 20, boundary 10, ops 10, rev 5 | 3.75 | **4.20** | D by 0.45 |
| 2 | Evidence 50%, law 10%, audit 15, boundary 10, ops 10, rev 5 | 3.90 | **4.00** | **D by 0.10** |
| 3 | **Law 0%**, evidence 50%, audit 20, boundary 15, ops 10, rev 5 | 3.90 | **4.00** | **D by 0.10** |
| 4 | Law 20%, evidence 50%, audit 30%, **boundary / ops / reversibility all 0%** | **4.30** | 4.00 | **A by 0.30** |

**Reading 3 is the strongest single result.** Shifting weight from law to evidence, **D still wins even when current-law conformance is weighted at zero and evidence at fifty percent.** Algebraically, transferring weight *x* from law to evidence gives A = (330 + 2x)/100 and D = (460 − 2x)/100; they cross at *x* = 32.5, which is beyond the 30 points available. **On that axis alone, A never overtakes D.** **[inference, arithmetic shown so it can be checked]**

**Reading 4 is where the recommendation loses, and it is reported rather than buried.** A overtakes D when **boundary expansion, operational complexity and reversibility are given zero weight** and evidence is at 50%. That is the honest crossover, and it names precisely what one would have to believe: **that adding the repository's first dependency since W3, taking on a binary and runtime surface, and performing an irreversible first-contact act are all worth nothing.** For a corpus whose fence is asserted by a test on every run **[mechanism]** and whose entire architecture is built to make irreversible acts deliberate, that position is not defensible — **but it is a position, and a reader is entitled to see the weighting that produces it.** **[inference]**

**Two further probes, both survived:** scoring A's auditability at 5 gives A **3.50** against D's 4.60; scoring D's law conformance at 4 rather than 5 gives D **4.30**, still ahead of A's 3.30. **The result is not an artefact of one arbitrary table.**

## 8. Decision — Option D

**Accepted by the human reviewer, 2026-08-22:**

> ### **PUBLIC W7 WILL NOT CONTACT A MODEL.**
>
> **The selected W7 model boundary is Option D: no public model contact, with authored synthetic generated-text specimens under the identical governed-handling regime.**

**This is a real W7-D3 decision, not a deferral.** §19 confronts that directly. **It takes effect on publication and remote verification of this record.**

**A, B and C are not "still open".** Each remains **possible only through a future governed amendment or crossing of its own**, with its own record and its own ceremony. **Nothing in this decision schedules, prefers, or pre-authorises such an amendment.** **[inference, applying `W7-AR` §7's no-decision-by-momentum rule in both directions]**

## 9. Tier F crossing — the applicable set is proved empty

**The Tier F instrument is retained, as the opening brief requires under every option.** **[law]** Under the selected posture, the crossing record's content is a **proof of emptiness**, and it is set out item by item so that the claim can be checked rather than accepted.

| Crossing kind | Required by Option D? | Why not |
|---|---|---|
| **Dependency crossing** | **No** | Nothing enters `requirements.txt`; the three pinned lines are untouched **[mechanism]** |
| **Adapter / environment crossing** | **No** | No external runtime is assumed, contracted or depended upon |
| **Manual-import crossing** | **No** | No model output is imported by any means, including by hand |
| **Binary crossing** | **No** | No model binary is installed, vendored, referenced or required |
| **Credential / configuration crossing** | **No** | No credential, token, key, secret or private runtime configuration is required |
| **Contact-bearing execution path** | **No** | No transmission-and-return to a model occurs under ADR-0047 decision 3(a) |
| **New top-level directory or root file** | **No** | The selected posture creates none |

**The applicable Tier F crossing set for the selected W7 posture is therefore EMPTY.**

**Precondition 2 is not waived, not deemed inapplicable, and not satisfied by analogy.** The precondition requires that **every applicable Tier F crossing is recorded**. Under Option D **every applicable crossing has been accounted for, and the applicable set is proved empty** — which discharges the requirement exactly as a recorded crossing would. **[law: ADR-0047 decision 9 precondition 2, read against `W7-AR` §7]**

> **This record is accepted. On publication and remote verification it DISCHARGES ADR-0047 precondition 2.**
>
> **Until then precondition 2 remains OUTSTANDING in public authority.**
>
> **It discharges no other precondition, at any stage.**

## 10. `contact_class`

**Under Option D, `contact_class` remains exactly `none`, and no contact-bearing member is minted.** **[law: ADR-0049 decisions 18–19, which reserve every other member to W7-D3 and record that `none` is the only lawful value today]**

**No future token is reserved.** **No hypothetical contact-class value for A, B or C is named, hinted at, ranked or sketched.** A future amendment opening a contact-bearing posture would have to govern that vocabulary **then**, from its own authority. **[inference, applying ADR-0033 decision 14's rule that stating a standard is not opening a path]**

## 11. Credential, configuration and binary posture

**Under Option D, concretely and not as a restatement of the general prohibition:**

no credential is required · no token or secret is required · no private runtime configuration is required · no model binary is required · no model installation is required · **no model provider is selected** · no SDK or client library is selected · **nothing enters `requirements.txt`**, which remains exactly `PyNaCl==1.6.2`, `cffi==2.0.0`, `pycparser==3.0`. **[mechanism]**

**The standing repository prohibition is preserved whole and unweakened.** **[law: `W7-AR` §7]** **The selected posture does not merely comply with it — it removes the occasion for it to be tested.**

## 12. Failure and timeout law

**The opening brief requires this to be stated even where the selected posture has no runtime failures, and it is stated rather than skipped.** **[law]**

> **There is no model runtime in W7. There is therefore no model non-response, no partial response, no truncation, no provider error and no model timeout to govern.**

**No timeout machinery is invented for a path that does not exist.** Writing failure law for an absent runtime would create the appearance of a capability the phase does not have — the precise confusion the anti-collapse chain exists to prevent. **[inference]**

**What is not a model failure mode, stated so it cannot be smuggled in later:** specimen-authoring errors, harness defects, scanner behaviour, and record-assembly faults are **not** model failures. They belong to their actual owners — **W7-D4 for the harness, W7-D5 for execution** — and a later record may not describe any of them as evidence about a model. **[inference]**

## 13. Reproducibility

**The evaluation material under Option D is authored and byte-inspectable, and the selected posture introduces no unverifiable external runtime assumption.** **[inference]**

**The one-bit scan-environment rule is carried whole from the opening brief §10** **[law]**:

> **capture-time local-wordlist effective branch state: `active` or `inactive`**, determined from the **effective filtered list the scanner actually used**, and classified as **public run provenance rather than private machine configuration**.

**Nothing more may be recorded**: no term counts · no terms · no fingerprints · no wordlist hash · no backing-file presence · no machine identity · no private configuration. **Representation in the run manifest remains W7-D4's.** **[law: the opening brief §10]**

**Dormancy is not resolution.** A run whose branch was `inactive` establishes only that the path was dormant **for that run**, and repeated inactivity never accumulates into a resolved seam. **[law: the opening brief §10]**

## 14. The six-seam register survives Option D intact

**Selecting D discharges none of these, and D is not permitted to become the reason any of them relaxes.** **[inference]** All six are carried from the published opening brief §11 unchanged. **[law]**

**Four HARD prerequisites — each must be discharged before its own named moment:**

| # | Seam | Must exist before | Owner |
|---|---|---|---|
| 1 | **Manifest artefact shape** | any run manifest or GER landing | **W7-D4** |
| 2 | **`active`/`inactive` scan-environment representation** | any governed run being represented | **W7-D4** |
| 3 | **W7-D2-E proof succession** | the first GER | **W7-D4 designs, W7-D5 performs** |
| 4 | **GER lifecycle and identity law, including reuse semantics** | the first `GER-####` identifier allocation | **W7-D5** |

**Two LAWFULLY CARRYABLE limitations — on their stated conditions only:**

| # | Seam | May be carried only if |
|---|---|---|
| 5 | **Part Q** | its current narrowing is **explicitly accepted** by the authority that owns it **and** the proposed execution is **proved lawful** under that narrowing |
| 6 | **`local-wordlist` locus production** | the **complete per-run posture** holds — naturally inactive means dormant for that run only; active with no finding may continue; **active with a finding and no lawful locus is stop-and-report**; and **inactivity is never manufactured** |

**Routing is not the gate; timing is.** **No run manifest, generated-evaluation home artefact, GER or identifier allocation may be materialised until every hard prerequisite is discharged at or before its named moment and each carryable limitation is resolved or explicitly accepted on its stated terms.** **[law: the opening brief §11.0]**

## 15. Part Q — decided under current law, with no reliance on change

**This decision was taken against Part Q exactly as it stands: no finding-bearing GER is landable.** **[law: ADR-0050 decisions 53–54]**

> **Option D was not selected on any assumption that W7-D4 will later relax Part Q.**

**D remains the recommended posture even if Part Q never changes**, and the scoring shows why: D's advantages — no dependency, no runtime, full inspectability, no irreversible act — are entirely independent of Part Q's disposition. **Part Q's narrowing costs D the same thing it costs every option: a capture that trips the scanner cannot be published as a GER.** **[inference]**

**Under D that cost is smaller in one specific and honest way, and larger in none:** the specimen author controls what the specimen contains, so exposure to the narrowing is **chosen rather than encountered**. **That is control over the failure path, not immunity from it** — an authored specimen that trips a committed pattern produces exactly the same finding, the same non-landability and the same stop-and-report as generated output would, because ADR-0047 decision 6 binds the handling identically. **[law]**

**W7-D4 retains the later choice**, through its own ceremony, to resolve Part Q or to explicitly accept the narrowing. **This record pre-judges neither and takes nothing from either outcome.** **[inference]**

## 16. Working-state invariant

Carried whole from the opening brief §12. **[law]**

> **UNLANDED AND UNDISPOSITIONED CAPTURE WORKING STATE MUST REMAIN OUTSIDE THE REPOSITORY.**

**No raw specimen or capture working state, no record under assembly, no finding-bearing payload, no withheld capture text, and no transient evaluation output may use the repository as scratch space.** This binds identically under Option D: **a specimen in progress is working state exactly as a capture is.** **[inference]**

**The protection is presently enforced by S1's filesystem assertion** and must be **carried forward deliberately** through the W7-D4 proof succession rather than silently dropped when S1 reaches its lawful endpoint. **[mechanism; law: the opening brief §12]**

## 17. Precondition posture after this decision

**The column below states the standing this record produces *once it is effective*.** **Human acceptance alone does not move it.** At the time of writing, the public baseline is `5ce8a923e8a52bf17e9b4c1bd81d1e714c79b135` and **precondition 2 is still OUTSTANDING in public authority**; it becomes DISCHARGED when this record is published and independently verified, and not before. **[law; inference]**

| # | Precondition | Standing after publication and remote verification of this accepted decision |
|---|---|---|
| 1 | W5-D2 runtime authority | Satisfied |
| **2** | **Every applicable Tier F crossing recorded** | **DISCHARGED by this record** — applicable set proved empty, §9 |
| **3** | **Named first-contact gate in the performing deliverable's brief** | **OUTSTANDING** |
| 4 | Synthetic-only artefacts throughout | Law in force; per-artefact conformance still proven at each landing |
| 5 | No hosted access absent a future governed record | Closed, and not opened here or by implication |
| 6 | Generated-output record shape exists and is accepted | **DISCHARGED** by the sealed W7-D2 |
| **7** | **Harness binding exists and is accepted** | **OUTSTANDING** — W7-D4 unopened |

**Precondition 3 under Option D.** It is **not waived, not discharged, not inapplicable, and not failed.** **There is simply no contact act in W7 to exercise it.** **[law: ADR-0047 decisions 9–11]**

**That is a lawful resting state, and the corpus says so in its own words.** The fifteenth and final link of the anti-collapse chain is **`no contact ≠ nothing proven`**, and ADR-0047 decision 20 makes it load-bearing in both directions: *"Choosing not to contact a model proves nothing about a model — and it does not mean W7 proved nothing. The governed handling is the claim, and the handling can be proven whole without a model ever being contacted. A closure record that treats a no-contact outcome as a failure to deliver would have collapsed this link."* Decision 33 hands that warning forward to W7-D5 through W7-D7. **[law]**

**W7-D7 must nonetheless report precondition 3 honestly as outstanding** if D remains the phase posture through closure. **A lawful resting state is not a discharged one**, and blurring the two would fail in the opposite direction — implying a gate had been passed that was never approached. **[inference]**

**Precondition 7 remains OUTSTANDING and W7-D4 remains unopened.** **This record smuggles no harness binding into itself**: it names no probe, no trap, no variant label, no capture-count rule and no exam material. **[inference]**

## 18. What Option D still allows W7 to demonstrate

**Stated as what later governed execution *may test*, never as what is already proven.** **Selecting D proves none of the following; it leaves them available to be proved.** **[inference]**

Governed-handling parity between authored specimens and generated output — **the strongest item on this list, because ADR-0047 decision 6 binds the handling identically, so these are not weaker governance tests merely because the prose was authored** **[law]** · record-shape conformance against ADR-0049's forty-six positions · pairing and capture completeness · finding creation and the finding/non-landability mechanics · Part-Q behaviour under current law · the stop-and-report posture · manifest integrity mechanics once W7-D4 defines the manifest · proof succession · lifecycle mechanics once W7-D5 settles them · review routing · **the deliberate construction of difficult and failure-path specimens** rather than waiting for one to occur · working-state discipline · public/private boundary preservation.

## 19. What Option D does not prove — the cost of the recommendation

**This section is the price of the decision and is stated at full strength, not as a footnote.** **[inference]**

**Option D establishes nothing whatever about:**

- **model quality** · **model correctness** · **model safety**
- **model behaviour** of any kind, in general or in particular
- **local-model behaviour** — how a model actually runs on a given machine
- **provider behaviour**
- **runtime reliability** · **adapter reliability**
- **timeout, non-response, truncation or error behaviour** of a real model
- **inference behaviour unique to a real model** — the things a specimen author cannot imagine because they have never seen them

**These are genuine evidence losses, and they are the losses the twenty-six recorded unknowns most want answered.** A specimen answers a question about models **exactly as well as its author's understanding of models allows, and no better** — and an author who knows the scan rules does not write adversarial samples by accident. **[inference]**

**The honest summary of the trade:** D buys lawfulness, reproducibility, zero surface and reversibility, and it pays with **every claim that could only be made by meeting a model.** **The recommendation rests on the judgement that W7's stated milestone is the governed handling rather than the model** — `W7-AR`: *"The model is not the milestone. The governed handling of model output is the milestone."* **[law]** **If that premise is rejected, the recommendation should be rejected with it.**

> **No later W7 record, summary, board row or closure statement may silently generalise specimen evidence into model evidence.** Doing so would collapse ADR-0047 decision 3's provenance distinction, which forbids laundering **in either direction**. **[law]**

## 20. Rejected alternatives, and the ground of rejection

**A — rejected on the weighted total, not on risk aversion.** A scores **highest of all four on evidence** and second on auditability. It loses because it takes the repository's **first dependency since W3**, moves a fence the suite tests on every run, adds a binary and runtime surface, performs an irreversible act, and inherits uncontrolled Part-Q exposure — and because those costs are weighted, not waved. **A is the option this record would revisit first** if the evidence premise changed. **[inference]**

**B — rejected because it pays for A's evidence with D3's own deliverable.** B's environment assumptions are unverifiable by the repository, and **reproducibility posture is something W7-D3 is required to settle**, not trade away. **[law: `W7-AR` §8 table]** B also places a runtime outside the governed surface and nearest the private boundary.

**C — rejected, and its apparent lightness is the reason to look at it hardest.** §4.1 establishes that C **is** contact, by the source's own words. Its provenance rests on human attestation where **a citation is a claim, not a clearance** **[law: ADR-0049]**, its execution is not publicly reproducible, its operator procedure sits inside the trust chain, and it carries a hosted-source hazard that would bar it outright. **C offers A's legal exposure with less than A's evidence and far less than A's reproducibility.**

## 21. Reversibility and the law of future amendment

**Selecting D is a decision, and it does not make A, B or C available later by default.** Each would require **its own governed amendment or crossing**, with its own record, its own Tier F ceremony and its own human authorisation. **[inference]**

**What D preserves is not optionality but cleanliness of the ground:** no dependency to remove, no binary to uninstall, no credential ever created, no irreversible contact act to be undone — because **contact is one-way and cannot be undone once performed** **[law: ADR-0047 decisions 12–15]**. **A later record that opens a contact-bearing posture starts from an unmarked boundary rather than a crossed one.**

**"Remains possible" is not "remains open."** An option that needs a new governed act to reach is not an option already available, and no later record may cite this decision as having kept one warm. **[inference]**

## 22. Proof obligations — classified against demonstrated evidence

**Every obligation below was prototyped against the exact final decision bytes and, where a repository-state fact is involved, the live baseline — with planted negative controls. Nothing here is called mechanical because a regex could be written for it.** **[precedent: W7-D2-E, where S3 was demoted from candidate-mechanical to review-only precisely because feasibility was demonstrated rather than assumed]**

| # | Obligation | Classification | Where it lives |
|---|---|---|---|
| **M1** | Exactly one posture is selected, and it is the no-contact posture | **MECHANICAL — LIVE** | `tests/test_w7_model_boundary_decision.py` |
| **M2a** | The bounded `contact_class` declaration for Option D is exactly `none` | **MECHANICAL — LIVE** | same module |
| **M2b** | No contact-bearing vocabulary member is minted | **REVIEW-ONLY IN FULL** | a human duty. **Not implemented as a token scan** |
| **M3** | The six-seam register carries exactly **four HARD** and **two CARRYABLE** seams, each with its timing gate | **MECHANICAL — LIVE** | same module |
| **M4** | The precondition posture is effective-on-publication: p2 discharged on effect, p3 outstanding, p6 discharged, p7 outstanding | **MECHANICAL — LIVE** | same module |
| **M5** | `requirements.txt` unchanged at its approved pins | **MECHANICAL — LIVE ELSEWHERE, NOT DUPLICATED** | `tests/test_repo_state.py::DirectoryFence::test_approved_manifest_contains_exactly_the_authorised_lines` |
| **M6** | The reserved home is absent and no `GER-####` identifier is allocated | **MECHANICAL — LIVE** | same module |
| **M7** | **The ADR-0046 fixed public/private invariant clause is carried exactly** | **MECHANICAL — LIVE** | same module |
| **M8** | `ADR-0051` is the single decision identity; no alias; no identifier namespace | **MECHANICAL — LIVE** | same module |

**M2b, stated precisely so the demotion is legible.** This record lawfully discusses contact-bearing alternatives in ordinary prose — it must, in order to reject them on the merits. **Deciding whether such prose has *minted* a vocabulary member, as opposed to *describing* a posture, is a semantic judgement**, and a whole-document token scan would either ban lawful discussion or pass vacuously. **[inference; precedent: ADR-0046 decision 29(b) and ADR-0047 Q3, where the same distinction defeated mechanisation]**

**M7, stated precisely so it is not oversold.** The proof establishes that **the ADR-0046 decision 14 fixed clause — *a separate governed authority outside this repository* — is carried exactly, neither truncated nor extended, wherever it appears.** **It does not, and must not, claim that a full sentence is globally byte-fixed**: ADR-0046 fixes **the clause**, and decision 15 permits sentence-position grammar around it. **[law]** The full sentence in §24 is carried whole, and acceptance criterion 13 continues to require that of this record — but that is a requirement on this record, not a claim about every record. **The proof reads the clause from ADR-0046 at run time and never transcribes it**, so the module contains no copy and needs no self-exclusion. **[inference]**

**Demonstrated evidence.** The proof module runs **8 test functions and 53 subtests** green against the proposed landing state, and **14 of 14 planted mutants are detected** — posture flipped, second selection marker, marker deleted, `contact_class` made contact-bearing, a HARD row de-structured, a CARRYABLE condition emptied, **p3 flipped to discharged**, **the effective-on-publication qualifier weakened to acceptance**, **one carriage of the invariant clause truncated**, **one carriage word-continued into an extended clause**, the H1 number altered, **an alias minted**, **an identifier namespace minted**, and **a GER identifier allocated**. **[mechanism]**

**M7 rejects extension as well as truncation, without banning lawful grammar.** A truncated carriage is caught by comparing the clause against its own leading prefix; an **extended** one is caught by a **bounded continuation check** — after the exact fixed clause, Markdown closers, then at most one space, then sentence punctuation or a dash are all accepted, because **ADR-0046 decision 15 permits sentence-position grammar** **[law]**, while a **direct word continuation is rejected**. **The negative control runs the same predicate**, and a further control proves that the predicate still accepts the lawful forms — a full stop, a bold close, a close-then-dash, a comma linkage, and a line end. **[inference]**

> **No ownerless mechanical debt remains.** Seven obligations are live in this landing's own proof module, one is already discharged by an existing deterministic test and is deliberately not duplicated, and one limb is review-only in full.

### 22.1 Review-only duties and their disposition

| # | Duty | Disposition |
|---|---|---|
| **R1** | Was the A/B/C/D comparison **fair**, or advocacy arranged as analysis? | **DISPOSITIONED FOR THIS RECORD** by Tier F human acceptance, 2026-08-22 |
| **R2** | Are the **weights reasonable** for this repository at this moment? | **DISPOSITIONED FOR THIS RECORD** by Tier F human acceptance |
| **R3** | Was the decision made **from the sources rather than from momentum**? | **DISPOSITIONED FOR THIS RECORD** by Tier F human acceptance |
| **R4** | Is Option D's **evidence limitation stated strongly enough** to survive later quotation? | **DISPOSITIONED FOR THIS RECORD** by Tier F human acceptance |
| **R5** | Could a later reader mistake **specimen evidence for model evidence**? | **STANDING REVIEW-ONLY DUTY**, through every later W7 artefact and summary |

**R1–R4 were disposed of by the act of acceptance, and only for this record.** They were live questions about *this* analysis; the reviewer answered them by accepting it. **They do not carry forward as debts, and acceptance of a later record would have to dispose of its own.** **[inference]**

**R5 is different and does not close.** It carries forward the **already-existing provenance and anti-laundering law** — ADR-0047 decision 3's provenance definitions and decision 4's rule that **provenance does not launder in either direction** **[law]** — and **human acceptance of this decision does not extinguish it.** It binds every later W7 record, board row, packet, summary and closure statement.

> **R5 is a standing duty, not a W7-D3-owned debt.** It does not prevent W7-D3 closing, and **no mechanical test discharges it** — not the module landed here, and not any future one. Whether a sentence generalises specimen evidence into model evidence is exactly the semantic judgement no scan can make.

**R1 and R3 deserved particular scrutiny from a reviewer who did not write this record**, because the implementer knew the architect's recommendation before performing the analysis. **The sensitivity table in §7 exists so that R1 and R3 could be tested rather than trusted** — including reading 4, which shows the recommendation losing. **[inference]**

## 23. Handoffs

**To W7-D4:** the manifest artefact shape and its proof binding · the Part Q pre-execution ceremony — resolve or explicitly accept the narrowing with lawfulness proved · `local-wordlist` locus production or a pre-capture stop posture · manifest representation of the one-bit scan-environment fact · proof-succession design and the new post-materialisation invariant · the working-state-outside-repository harness law · `pairing.variant_labels` · the exam paper, its probes and its lawful traps · capture-count rules · **the proof that every input is synthetic, which under Option D is the whole provenance story.**

**To W7-D5:** execution of the W7-D4 proof transition **before** the first GER · retention, archival and withdrawal-from-view · identifier persistence and reuse semantics · first materialisation of the manifest and records · execution enforcement of the working-state invariant. **Under the selected posture, no deliverable performs contact, and precondition 3 is never reached.**

## 24. Public / private boundary

**The full public sentence, carried whole:**

> **Any real-person adoption is a separate governed authority outside this repository.**

**The fixed invariant is the clause** — *a separate governed authority outside this repository* — and the sentence above is a **permitted sentence-position form** under ADR-0046 decision 15. **[law]**

**No W7-D3 artefact may name, describe, locate, date, specify, implement, schedule or depend upon that external authority.** This record contains no real-person content, no private lineage, no private implementation, no machine paths, no credentials, no vendor secrets, and **no model or vendor branding of any kind** — none being needed, since **no provider is selected.** **[law: ADR-0046 Part E]**

## 25. Non-goals, and what does not exist

**This record does not:** open the hosted class or narrow ADR-0033 decision 13's conditions · perform, schedule or require contact · create any artefact of the generated-evaluation class · design the exam · author a specimen · resolve Part Q · resolve the locus seam · settle lifecycle or identity · open W7-D4 through W7-D7 · open W8 · make any claim about model behaviour, safety, clinical validity or fitness for any purpose.

**Does not exist at this record's landing:** no `governance/generated-evaluation/` directory · no schema · no manifest · no generated-evaluation record · no `GER-####` identifier allocated · no authored specimen · no generated output produced or imported · no harness built or bound · no dependency added or changed · **no model contacted** · no W7-D4 or W7-D5 opening.

**This landing mints exactly one governed identity, `ADR-0051`.** It creates no alias, no second decision identifier, and **no identifier namespace of any kind** — no `GER-####` allocation and no contact-class vocabulary. **[inference]**

## 26. Acceptance criteria — the standard this record was held to

**Stated as the test the reviewer applied, and retained so a later reader can re-apply it.** An accepted W7-D3 Tier F decision record is acceptable only if it:

1. **selects exactly one posture**, on grounds traceable to sources rather than to convenience or momentum;
2. **carries the sensitivity analysis including the weighting under which the recommendation loses**, so the choice can be checked rather than trusted;
3. **proves the applicable Tier F crossing set** — recorded crossings, or emptiness demonstrated item by item — and discharges **precondition 2 and nothing else**;
4. **fixes `contact_class`** and mints, reserves and hints at no contact-bearing token;
5. **states the credential, configuration and binary posture concretely** for the selected option;
6. **states the failure and timeout law**, or records with reasons that the posture has no runtime failure modes, without inventing machinery for an absent runtime;
7. **states the reproducibility posture**, including the one-bit scan-environment rule and its classification as public run provenance;
8. **carries the six-seam register binding**, with four hard prerequisites, two carryable limitations, each timing gate, and the exact conditions for carrying a limitation;
9. **carries the working-state-outside-repository invariant**;
10. **preserves precondition 3 undischarged**, names no first-contact gate, and states the no-contact resting state as lawful while requiring W7-D7 to report it outstanding;
11. **opens no dormant door** and narrows no ADR-0033 condition;
12. **states D's evidence limitations at least as prominently as its advantages**;
13. **carries the public/private invariant sentence whole**;
14. **states what it does not decide**, at the same length as what it does.

## 27. Accepted human rulings, and issues carried downstream

**The two questions this record put to the human reviewer were resolved in the act of acceptance. Neither remains open.** **[law: the reviewer's Tier F acceptance, 2026-08-22]**

### 27.A Accepted rulings

**A1 — The evidence premise: ACCEPTED.** `W7-AR`'s premise that **the governed handling, not contact with a model, is W7's milestone** — *“The model is not the milestone. The governed handling of model output is the milestone.”* — **is accepted for W7.** The Option D decision rests on it, and **accepting this Tier F decision accepted that premise.** **This is no longer an open question.**

**A2 — The precondition 3 resting state: ACCEPTED.** **ADR-0047 precondition 3 may lawfully remain OUTSTANDING through a no-contact W7 closure**, provided **W7-D7 reports that state honestly as outstanding.** The proviso is a standing obligation on W7-D7, not a condition on this decision. **This is no longer an open question.**

**What acceptance did not do.** It did not discharge precondition 3, did not make it inapplicable, and did not make the no-contact outcome a discharge of anything beyond precondition 2 on publication. **A lawful resting state is not a discharged one.** **[inference]**

### 27.B Carried downstream issues

1. **What the twenty-six unknowns can honestly be said to test** under a specimen-only regime. **Owned by W7-D4** when it builds the exam, and by **W7-D7** when it reports on what was tested.
2. **Whether Part Q is resolved, or its narrowing explicitly accepted with execution proved lawful under it.** Scheduled to **W7-D4**'s own ceremony. **Not pre-judged here**, and §15's no-reliance rule holds whichever way it goes.

### 27.C Future amendment observation — non-operative

**If a later governed authority changes the evidence premise, Option A is the first contact-bearing posture this analysis indicates should be reconsidered.** **This creates no schedule, no opening, no reservation and no authority**, and no later record may cite it as any of those. **[inference]**

---

*Four options were framed without ranking, and this record ranks them. It gives the strongest contact option maximum credit on evidence, scores the recommendation conservatively on the same axis, and then attacks its own conclusion until it finds the weighting that breaks it — which requires believing that fence expansion, control complexity and irreversibility are worth nothing at all. The recommendation is that public W7 will not contact a model: not because contact is frightening, but because the phase's milestone is the handling, and the handling can be proven whole without one.*
