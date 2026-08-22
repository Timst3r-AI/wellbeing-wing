# 0052 — Exclusion-List Conformance (P4) Decomposition and Decidability Correction

**Status:** **Accepted by human reviewer, 2026-08-22.** Not a build instruction. Authorises no implementation.
**Date:** 2026-08-22 · **Phase:** W7 — First-Contact Governance and Synthetic Model Evaluation (doctrine correction arising in deliverable W7-D4)
**Amends:** ADR-0046 (Synthetic-Only Public Law and the Adoption Boundary) — the **P4 row of decision 27**, the **lead sentence of decision 27**, and by addition a new **decision 29A**. By correction, not bypass.
**Decision mode:** **implementation-derived, then review-corrected.** The defect was found by faithfully attempting the accepted doctrine against the first artefact of the class; the first proposed correction was itself an overclaim and was corrected under architect review before landing. Both steps are recorded in section 4 decision 9 rather than tidied away.
**Controlling law:** the W0 no-new-authority discipline; W2-D3 checklist rule 2 (two-tier change rule); ADR-0003 (ceremony); ADR-0018 (scope fidelity); **ADR-0021 decision 1 (decidability draws the line) and decision 3 with §57 (compound terms are decomposed; nothing is "partly automated")**; ADR-0022 (the M10/M12 precedent for an implementation-discovered decidability correction and for clause decomposition); ADR-0046 (the record corrected); ADR-0047 and ADR-0049 (the doctrine that consumes it).
**Blocks:** the final W7-D4 implementation landing, which is suspended until this correction is published and remotely verified. The six W7-D4 candidate artefacts are preserved byte-unchanged in the meantime and are reconciled to this record in their own later governed act, never in this commit.

---

## 1. Decision question

ADR-0046 decision 27 specifies six proof obligations and, following ADR-0021 decision 1, declares for each whether a machine can decide it. It classifies **P4 — exclusion-list conformance — as Mechanical**, and states that **P2 alone is review-only**.

W7-D4 is the landing that first creates artefacts of the class, so P4 reached the implementation point decision 28 assigns it. Implementation found that **decision 11 is a prohibition over kinds, and no kind in it is decidable as a kind from repository bytes.** Predicates can detect bounded surface forms that a violation *often* takes. They cannot decide whether an artefact belongs to a prohibited family, because family membership turns on provenance, character, context and effect.

The question: **how is P4 stated so that the mechanical part claims only what it decides, the semantic part is owned rather than implied, and decision 11 is narrowed in no respect whatever?**

## 2. Context

W7-D4 implemented P4 by parsing decision 11's families from ADR-0046 at run time and checking them over the class artefact's bytes. Eight families yielded useful surface guards, with negative controls, and are clean. Three yielded no useful guard at all.

The W7-D4 packet reported that as **P4: 8 of 11 mechanical + 3 of 11 review-only**. That report was unfaithful to the landed record, which says Mechanical without qualification. **A packet is not an amending instrument.**

A first correction candidate then proposed restating P4's decidability as *"mechanical in part, review-only in part"* with an 8 + 3 = 11 partition. **Architect review rejected that too, and correctly.** It contained the same class of overclaim one level down: it implied the eight families were mechanically decided and only three were not, when the record's own evidence section already showed semantic residues sitting inside families 1, 2 and 4. The general truth is stronger — **the implemented predicates decide bounded surface forms, never complete families** — and a partition of the list into "mechanical families" and "review-only families" cannot be drawn at all. ADR-0021 §57 names the formulation that was reached for: *"No term may be 'partly automated' without a precise decomposition."*

**This record corrects the doctrine by decomposition. It amends no prohibition.**

## 3. Controlling sources and accepted rulings

- **ADR-0046 decision 11** — the exclusion list. **Consumed here, not touched.**
- **ADR-0046 decision 12** — the list is growable only, never narrowable. Binding on this record, which narrows nothing.
- **ADR-0046 decision 27** — the obligations table whose P4 row and lead sentence are corrected. Its Part H carries a one-line pointer to this record, added in the same commit per the ADR-0021 precedent; no corrected rule is restated there.
- **ADR-0046 decision 29** — why P2 cannot be mechanical: **(a)** no lawful needle exists for a name that may not be written; **(b)** rule-explaining prose and the barred thing itself cannot be told apart without semantic judgement. Both structural. **This record finds (a) and (b) reach into decision 11 as well.**
- **ADR-0046 decision 30** — mechanical and review-only are kept apart; no review judgement is smuggled into a green check. **Extended by this record, never relaxed.**
- **ADR-0021 decision 1** — mechanically checkable **iff** decidable from deterministic repository artefacts **without interpretation**; cost is irrelevant.
- **ADR-0021 decision 3 and §57** — every governed term is classified as exactly mechanical or review-only, and **a compound term is decomposed**; the worked example is that section *presence* is mechanical while section *adequacy* is review-only. **This is the discipline P4 must satisfy, and the reason a "partly mechanical" row is not available.**
- **ADR-0022** — the precedent in both respects: an accepted decidability classification corrected after implementation showed it could not hold, and a conflated row decomposed into named clauses with explicit non-claims, under the ruling that **mechanical fidelity never becomes semantic adequacy**.
- **ADR-0049 T6** — the re-authoring residue no field set can catch, already held by review.
- **`scripts/public-safety-scan.py`** — the live scanner, measured rather than assumed.
- **The W7-D4 candidate artefacts** — the bytes against which every measurement below was taken.

## 4. Decision

**1. P4 is decomposed into two named clauses, P4a and P4b**, as ADR-0021 decision 3 requires. The prior single row conflated a bounded decidable check with an unbounded semantic prohibition. **The prior "Mechanical" classification is withdrawn, and so is the "mechanical in part, review-only in part" formulation proposed before this revision.**

**2. Decision 27's P4 row is replaced by two rows:**

| # | Obligation | Fails when | Decidability |
|---|---|---|---|
| **P4a** | **Mechanical exclusion surface guards.** Over the bytes of every artefact of the class, detect the bounded, writable and enumerable surface forms named by a **governed guard inventory**, with the barred forms carried as stems and the instrument holding them excluding precisely itself. **The live family inventory is read from decision 11; the guard inventory and its family mapping are explicitly governed and mechanically reconciled to that live inventory.** No guard, and no guard-to-family assignment, is inferred from decision 11's prose. Each guard carries governed **positive** controls that must trigger and governed **clean** controls that must not. | Any of: a guarded surface form is detected in the bytes of an artefact of the class; **or** a required guard or control is absent or disabled; **or** a governed positive control fails to trigger; **or** a governed clean control begins triggering; **or** the live family inventory fails reconciliation against the governed guard inventory. | **Mechanical.** Every listed condition is decidable from deterministic repository artefacts without interpretation |
| **P4b** | **Complete exclusion-list conformance.** No artefact of the class falls inside any of decision 11's eleven families, on any ground. | An artefact's **provenance, character, context or effect** places it inside a prohibited family — **whether or not any enumerable surface form is present**, and including material whose bytes are indistinguishable from lawful material. | **Review-only, in full.** Decision 29A records why, and the reasons are structural rather than gaps in tooling |

**3. P4 conforms only when P4a is green AND P4b has received human review at that landing.** **P4a is necessary and not sufficient.** **A green P4a is no evidence for P4b in any degree** — not partial evidence, not presumptive evidence, not evidence for the families it guards.

**4. P4a makes four explicit non-claims.** It makes **no claim** that a guarded family is clear of violations; **no claim** that an unguarded family is clear of anything; **no claim** that the guard inventory is complete or ever will be; and **no claim to detect every possible semantic narrowing of a guard beyond its governed controls** — a guard may be weakened in ways its controls do not reach, and **whether a guard remains adequate is P4b's question, not P4a's.** Its green result means one thing only: **none of the enumerated surface forms is present in the bytes examined, and every governed control behaved as its inventory says it must.**

**5. The truthful arithmetic replaces the withdrawn partition.** No partition of decision 11 into mechanical and review-only families exists or may be stated. What may be stated is:

- **eleven families remain wholly prohibited;**
- **eight currently have one or more mechanical surface guards;**
- **three currently have no useful mechanical surface guard;**
- **all eleven remain inside complete human conformance review under P4b.**

"Currently" is load-bearing. A guard may be added to a family later **by amending the governed guard inventory**, which changes P4a's inventory and nothing about P4b.

**6. The ordinary public-safety scan is not P4a's instrument, and a clean scan is evidence for neither clause.** Measured in section 5.2: the scan's committed categories touch three of the eleven families, one of those only for paths under `fixtures/`, and even there they match particular surface forms rather than deciding a family. P4a requires its own governed instrument, and any future packet offering a clean scan in place of one is non-conforming.

**7. The stem device of the prior wording is preserved and generalised.** The prior row's instinct — that scan-sensitive families must be carried as stems so the prohibition stays clean — was correct and is kept. It is extended with the self-exclusion discipline decision 28 already applies to P1: **the module holding the barred surface forms excludes precisely itself, asserted to be exactly one path resolving to that module**, and any governed artefact carrying a declared statement of what it refuses names that statement as an exact literal, asserted to be the only such line, with the remainder proved clean.

**8. Reporting discipline, extending decision 30.** **P4a and P4b are reported separately, always.** A P4a report carries its guard inventory, its family coverage, and its negative-control results. A P4b report carries a named human review act at that landing, or records P4 as not conforming. **"P4 green" is non-conforming language and may not appear** in any packet, closure record, board row, registry role or summary; **"P4a green" may never be shortened to "P4 green"**; and no artefact may state or imply that a mechanical run established complete exclusion-list conformance.

**9. The discovery history is preserved, not tidied.** The sequence was: `P4 accepted as Mechanical → W7-D4 implementation attempts it against the first artefact of the class → eight useful guards, three families with none → packet proposes an 8/3 partition → architect review rejects the partition as a second overclaim → decomposition into P4a and P4b`. **The prior wording was legitimately derived and honestly attempted**; the first correction was directionally right and still overclaimed; **no earlier record is rewritten to imply the decomposition was always known.**

**10. Decision 11 is untouched, and no prohibition is weakened.** All eleven families remain fully prohibited in every artefact, path, field, filename and commentary. The list remains growable only. **What changes is the instrument and the honesty of the claim, never the prohibition.**

**11. Order of consumption.** Doctrine first, implementation second. The W7-D4 artefacts are preserved unchanged until this correction is accepted and published; then only source references, classification wording and reporting language are reconciled, and the complete W7-D4 ceremony is re-run before the final packet is returned. **This record authorises no implementation and no landing of its own.**

**12. Decision 27's lead sentence is corrected** to read:

> Six proof obligations are specified; each names what fails it, and each declares honestly whether a machine can decide it. **Four are mechanical in full.** **One — P2 — is review-only in full and admits no mechanical clause at all**, for the reasons decision 29 records. **One — P4 — is compound and is decomposed at decision 29A** into **P4a**, a mechanical surface guard, and **P4b**, complete conformance, which is review-only in full. **P2 remains the only obligation for which no mechanical clause exists**; **P4b is a review-only clause whose greenness no mechanical result can supply.**

## 5. Why the prior P4 wording could not hold

### 5.1 What the prior row assumed

The prior row assumed the whole of decision 11 could be **"expressed in scannable terms, with the two scan-sensitive families carried as stems"**. That assumption holds for *tokens*. **Decision 11 is not a list of tokens; it is a list of kinds**, and kind membership is not a property of bytes. A credential-shaped string is evidence of a credential; its absence is not evidence that no credential is present, and no rewriting of the guard changes that direction of inference.

### 5.2 The ordinary scanner, measured rather than assumed

The live scanner carries five committed categories — `external-link`, `claim-strength`, `real-data`, and two further categories, one concerning a form of claim strength and one concerning a relational framing word — plus one name-pair rule scoped to paths under `fixtures/`. Each guarded family was given a violating probe assembled at run time and passed through the **live** `scan_file`:

| decision 11 family | live scan, outside `fixtures/` | live scan, under `fixtures/` |
| --- | --- | --- |
| real-person data of any kind | `real-data` | `real-data` |
| identified person's room, health, movement, food, device, contemplative or journal material | **nothing** | `real-data` |
| real wearable or device data | **nothing** | **nothing** |
| private model transcripts | **nothing** | **nothing** |
| credentials, tokens, keys, secrets, private configuration | **nothing** | **nothing** |
| machine-identifying detail beyond OS class | **nothing** | **nothing** |
| a model binary | **nothing** | **nothing** |
| a real-person evaluation channel | `external-link` | `external-link` |

**Five of the eight guarded families receive nothing from the scan in either scope.** One receives a report only inside `fixtures/`. The two that do report do so incidentally — a marker or a link form that happens to sit inside a much larger family — and neither decides its family. A clean scan therefore carries no information at all about most of decision 11.

### 5.3 The bounded surface guards — decision 29A(a)

Eight families currently have one or more guards. Each guard is decided over a writable, enumerable surface form, from deterministic repository artefacts, without interpretation, and each has a governed positive control that plants a violating string assembled at run time so that no tracked line carries one. **The guard-to-family assignment below is a governed declaration, not an inference from decision 11's wording**; the live family inventory is read from the record and reconciled against it:

1. **real-person data of any kind** — the identifier and record-number markers the `real-data` category carries, plus the fixtures name-pair rule;
2. **identified person's material** — human-plausible name pairs, and the requirement that every persona token is in the artificial `Persona-` form;
3. **real wearable or device data** — serial-shaped tokens and device-identifier forms;
4. **private model transcripts** — declared class and origin, and the absence of any generated-output token;
5. **credentials, tokens, keys, secrets, private configuration** — key-shaped assignments, bearer forms, and private-key block headers, carried as stems;
6. **machine-identifying detail beyond OS class** — drive-rooted, user-home and network-share path forms, carried as stems; repository-relative paths explicitly unaffected, per decision 11's own parenthesis;
7. **a model binary** — model-weight file extensions, carried as stems;
8. **a real-person evaluation channel** — declared channel values against their source, and the absence of any live endpoint form.

**Every one of these decides a surface form, and none decides its family.** That is a general property, not a defect in three of them. Three illustrations make the shape of it concrete rather than abstract: guards 1 and 2 decide whether a name-shaped or marker-shaped token is present, **not whether a plausible-looking identity is a real person's**; guard 4 decides declaration and token absence, **not whether lawful-looking prose was re-authored from a transcript** — ADR-0049 T6 holds that and it stays human; guard 6 decides path form, **not whether an innocuous-looking repository-relative reference discloses a machine's arrangement.** The same gap exists behind all eight.

**Mechanical fidelity never becomes semantic adequacy**, in ADR-0022's words, and P4a never becomes P4b.

### 5.4 The three families with no useful guard — decision 29A(b)

These families are not "the review-only ones" — **all eleven are inside P4b.** They are the families where not even a partial guard exists, so P4b is the only instrument that touches them at all. Each reason is structural, in the form decision 29 uses for P2, and none will be closed by a better instrument.

**(i) Private relationship or lived-interaction material.** The bar is on **provenance and character**, not on any token. Authored synthetic prose describing an interaction is lawful; recorded lived material describing the same interaction is barred; **the two can be byte-identical in form.** A pattern permissive enough to admit the fifty-two lawful specimens is permissive enough to admit a transcribed one, and a pattern strict enough to exclude the transcribed one would fail the lawful corpus. This is decision 29(b)'s structure applied to a different subject: **form does not separate the classes.**

**(ii) Private adoption implementation detail.** This family inherits decision 29(a) **directly and without modification**. The material is precisely what decision 16 bars from appearing anywhere in this repository. A mechanical check needs a search term; writing the term would put the barred material into the repository and breach the very law the check enforces. **There is no lawful needle, so there is no lawful check** — the identical reasoning that makes P2 review-only in full.

**(iii) Anything that would turn the public Wing into a live personal instrument.** This family is **not an enumerable set at all.** It is a consequence clause: its subject is what an artefact would *do* if run or adopted, not what any artefact contains. Deciding it requires reasoning about effect. Any pattern would be a proxy for that reasoning, and **a green proxy is worse than an honest human duty**, because it would report as decided the one item on the list that most needs a person to have looked.

### 5.5 The arithmetic, stated so nothing is lost and nothing is implied

**No partition is claimed.** The four statements of decision 5 are the whole of what the counts support: eleven wholly prohibited; eight currently guarded; three currently unguarded; **all eleven inside P4b.** The guard count is an inventory of instruments, **not a measure of how much of decision 11 has been decided** — the answer to that question is none of it, mechanically.

The **live family inventory** is read from decision 11 at run time rather than assumed, and the **governed guard inventory** is reconciled against it. If the list grows under decision 12, reconciliation fails and P4a fails with it, until the new family is entered in the governed inventory with its guard position recorded — which is the correct behaviour for a growable-only list, and which is why **reconciliation failure**, rather than a bare count comparison, is written into P4a's failure predicate.

## 6. What this record does not do

It does not touch decision 11's list, decision 12's growable-only rule, decision 14's invariant clause, decision 16's non-naming law, decisions 23–25's ceiling and specimen parity, or any prohibition anywhere in the corpus. It creates no exception, allowlist, suppression or exemption. It authorises no implementation, landing, identifier, model contact or generated output. It does not resolve ADR-0050 Part Q or the `local-wordlist` seam. It opens no deliverable.

**The same test was applied to the other five obligations, and none needs decomposition.** P1, P3, P5 and P6 each state a **bounded structural condition** — a clause matching byte-for-byte, a declared origin drawn from a closed set, a sentence present byte-identically, a declared input origin that is not a capture — and each is decidable as stated, with its semantic residue already owned elsewhere and named there. **P2 states a semantic prohibition and is already review-only in full.** P4 was unique in stating a semantic prohibition while claiming to be mechanical, which is what made it the only row requiring decomposition.

## 7. Constitutional check

- **No new authority.** The record narrows a decidability claim and decomposes a compound obligation. It grants nothing.
- **Two-tier change rule (W2-D3 rule 2).** A material change to an accepted record requires a decision record, never an edit. This is that record.
- **Decidability draws the line (ADR-0021 d.1).** The correction is made on decidability grounds alone. Cost played no part; P4b would remain review-only with unlimited effort available.
- **No ambiguous middle (ADR-0021 d.3, §57).** Each clause is classified as exactly one of mechanical or review-only. **Nothing is "partly automated"**, and the formulation proposed before this revision is withdrawn precisely because it was.
- **Honest classification (ADR-0046 d.30).** The correction moves the whole of decision 11 inside a review-only clause. **It makes the doctrine substantially weaker as a claim and stronger as a description**, which is the direction a correction of this kind must run.
- **Growable-only (ADR-0046 d.12).** Nothing is shortened, softened or read down; the growth case is written into P4a's failure predicate as a **reconciliation** between the live family inventory and the governed guard inventory, so a family added under decision 12 fails the check until it is governed rather than passing unnoticed.
- **Scope fidelity (ADR-0018).** The correction touches one row, one sentence, and adds one decision. It reaches no further.

## 8. Alternatives considered

1. **Leave the doctrine and report P4 as mechanical.** Rejected: it would require either faking semantic families into predicates or reporting a green P4 that silently excluded most of the prohibition. Both are the failure decision 30 forbids.
2. **Leave the doctrine and report the split only in the packet.** Rejected: that is what the W7-D4 packet did, and it amends an accepted record by narration.
3. **Restate P4 as "mechanical in part, review-only in part" with an 8 + 3 partition.** **Proposed, reviewed and rejected.** It implied the eight families were decided, when the guards decide only surface forms, and ADR-0021 §57 forbids a partly-automated classification without a precise decomposition. Recorded here because it was a real step in the correction, not because it survived.
4. **Substitute the ordinary public-safety scan for P4.** Rejected on measurement: section 5.2 shows the scan reports nothing for five of the eight guarded families.
5. **Move all of P4 to review-only with no mechanical clause.** Rejected: eight families have working, negatively controlled guards, and discarding real protection to buy a tidier classification would trade safety for neatness. The guards are kept, and confined to what they prove.
6. **Add an allowlist of permitted continuations for the unguardable families.** Rejected on ADR-0046's own grounds — the silent allowlisting decision 13 forbids elsewhere in the same record, which decision 29(b) already refuses at this record's own boundary.

## 9. Consequences

**Accepted cost, and it is larger than the first correction admitted.** **The whole of decision 11 now sits inside a review-only clause.** P4 cannot be discharged by any test at any landing, now or ever, and every landing that creates an artefact of the class needs a human to have read it against eleven families and said so. The corpus can no longer claim to have mechanically enforced any part of its exclusion list — only to have guarded some surface forms of it. That is a genuine reduction in what the repository can prove about itself, stated plainly rather than presented as an improvement.

**A second cost.** P4 can never be reported as one result. Every packet, closure record and board row must carry both clauses, with P4b naming a human act, permanently. **The phrase "P4 green" leaves the vocabulary.**

**A third cost, and the sharpest.** Because P4b is review-only in full, **a landing can be fully green and still be in breach of decision 11** — and nothing mechanical will say so. That was already true before this record; the difference is that the corpus now admits it instead of implying otherwise.

**A fourth cost, smaller and worth naming.** P4a's own strength is bounded by its governed controls: it detects the surface forms and control regressions its inventory names, and a guard weakened in some way those controls do not reach will not be caught by P4a. **Guard adequacy is P4b's question**, which means the review clause covers the instrument as well as the artefact.

**What improves.** Eight families gain a real instrument with governed controls and a measured demonstration that the ordinary scan does not cover them, where the prior wording's assumption of scannability had produced nothing at all. The guards catch the careless case, which is the common case. And the corpus regains the property that matters most: **its decidability claims describe what it can actually decide.**

## 10. Public-safety considerations

This record names the barred families in order to classify them, exactly as decision 11 names them in order to forbid them, and carries every barred surface form as a stem or a placeholder rather than as a literal. It contains no real-person data, no credential, no machine-identifying path, no model binary reference, no private adoption detail, and no health or clinical content. It names no external authority. **Any real-person adoption is a separate governed authority outside this repository.**

## 11. Dependencies

- **Consumes:** ADR-0046 (corrected here), ADR-0021 d.1 and d.3/§57, ADR-0022 (precedent), ADR-0049 T6, ADR-0018, ADR-0003, W2-D3 rule 2, W0.
- **Consumed by:** the W7-D4 final landing, which reconciles its source references, classification wording and reporting language to this record, **declares its guard inventory and family mapping explicitly rather than deriving them from decision 11's prose, and proves that inventory reconciled against the live family inventory**, then re-runs its complete ceremony.
- **Blocks:** the W7-D4 final landing until accepted and published.
- **Opens:** nothing. W7-D5 through W7-D7 remain unopened.

## 12. Open questions

1. **Whether a later phase finds a guard for one of the three unguarded families.** Possible. It would be added by amending the governed guard inventory, would change P4a's inventory, and would change nothing about P4b. Not predicted here.
2. **Whether P4b warrants a standing named review duty in the W7 closure record**, alongside R5 and the ADR-0046 P2 / ADR-0047 Q3 duties. Named here as a question for W7-D7; not decided.
3. **Whether the same conflation exists in obligations owned by earlier phases.** Section 6 audited the other five W7-D1 obligations and found none. Records outside ADR-0046 were not audited, and this record makes no claim about them.

---

**This record decomposes a compound obligation and corrects a decidability claim. It permits nothing that decision 11 prohibits, and it makes nothing easier to land.**
