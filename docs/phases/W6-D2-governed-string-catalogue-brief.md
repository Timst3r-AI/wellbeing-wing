# W6-D2 — Governed String Catalogue Opening Brief

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation by itself.
**Date:** 2026-08-17 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D2**
**Position:** the W6-D2 opening brief, landing after the W6-D1 doctrine set completed at ADR-0043's publication. **Its acceptance and publication opens W6-D2 for brief-governed work only**: it defines the deliverable's landing plan, acceptance gates, proof obligations, and safe sequence — and every landing in that sequence still requires its own authorisation through its own ceremony. **This brief creates no catalogue, no file, no schema; allocates no final catalogue ID; admits, rejects, and grades no string; wakes no validator; renders nothing.**
**Governed by:** ADR-0042 (catalogue identity and namespace law — the gate this brief opens behind) and ADR-0043 (the surface contract); ADR-0038 through ADR-0041 whole; the W6-D1 brief's completion posture; the W6 runway's catalogue-scope-creep risk binding.
**Tier at landing:** J — full ceremony.

---

**The law of the register is written; this brief is the plan for building it without breaking a single sentence of that law. Five landings, each small enough to prove: decide the artefact's home, decide its shape, wake the watcher, admit the candidates one at a time on the record, and close with everything exact. The thirty-three strings that waited five phases will not be rushed through the door in a batch — because a register whose first entries arrived unexamined would be born owing exactly the debt this phase exists to refuse.**

## 1. Opening statement and gate posture

**W6-D2 is open at this brief's acceptance, publication, and remote verification — for planning and brief-governed landings only, and nothing else is.** The ADR-0042 Part G gate is satisfied on its first condition (DR-W6-05 accepted and published) and this brief supplies its second (W6-D2's own accepted brief). W6-D3 through W6-D6 remain unopened behind their own briefs; W7 remains unopened. *Opening is effective on publication:* while this brief's commit remains local it is not in force. **No catalogue artefact exists at this brief's landing, and none is created by it.**

## 2. W6-D2 identity and non-identity

**W6-D2 is the governed string catalogue deliverable**: its purpose is to create — later, and only through authorised landings — the governed register of approved display strings and their required metadata that ADR-0042 defined, validated by the woken catalogue-ID validator, seeded by per-string admission decisions over the review-of-record corpus.

**W6-D2 is not:** string grading · review-of-record evaluation · D5-T24 execution (all W6-D3's, behind its own brief) · rendered labels · UI · CLI · a review surface (W6-D4's, behind ADR-0043 and its own brief) · runtime work · model contact · human review · catalogue-free copy work · product glossary work · or design-system work. The catalogue holds governed words about states; everything else the surface era does happens elsewhere, behind other gates.

## 3. The doctrine consumed, whole

All six W6-D1 records bind every W6-D2 landing, unweakened: **ADR-0038** (the seven classes, class-as-data, verbatim-or-registered-derived, derived-never-stored, the barred list with the `certif-` and `complian-` stem bans) · **ADR-0039** (display may preserve source authority; display may not create authority — applied to registration itself; rule 12's declarability) · **ADR-0040** (the accompaniment table as catalogue content) · **ADR-0041** (its accompaniments and the human-act display boundary) · **ADR-0042** (identity, membership, exclusions, ID law, namespace law, seed posture, the thirteen validator obligations, and the Part G gate this brief operates) · **ADR-0043** (the surface contract, so nothing in W6-D2 quietly becomes a surface: **membership in the catalogue is necessary, never sufficient, for later display**). Conflicts resolve toward the consumed records, and this brief is the defect wherever it appears to disagree.

## 4. The W6-D2 sequence — five landings, each behind its own authorisation

Conservative by design: the catalogue is not collapsed into one landing, because per-string admission, validator waking, and artefact creation are three different kinds of act with three different failure modes, and each deserves its own measured set and its own gate.

| Landing | Name | Shape |
| :---- | :---- | :---- |
| **W6-D2-A** | Catalogue artefact shape and home decision | Decides, by record: the artefact's repository home, format, registry posture (registered-with-hash or deliberately excluded, stated either way), and its declarability statement per ADR-0039 rule 12. **No entries. No IDs. No schema fields beyond what the decision itself requires to be stated.** |
| **W6-D2-B** | Catalogue schema and metadata shape | Decides the record shape carrying ADR-0042 decision 2's fields as data: ID · string · vocabulary class · source authority · derivation reference where derived · accompaniment linkage where required · prohibition register where applicable · source-citation requirement where applicable · supersession/retirement posture · proof obligations · **and the standing no-display-authorisation statement.** No final IDs unless the landing's own authorisation separately and explicitly grants allocation. |
| **W6-D2-C** | Validator wake landing | Wakes the dormant catalogue-ID validator **only** under its own measured landing: implements the thirteen ADR-0042 Part F obligations exactly, amends the dormancy assertion by record, and proves green **in the same commit as the artefact state it validates**. The validator is never woken ahead of something real to check. |
| **W6-D2-D** | Seed corpus admission pass | Admits or rejects the thirty-three review-of-record strings **one by one, on the record** — each with its admission-or-rejection decision, its class, source, and metadata where admitted, and its stated reason where rejected. **Rejection is lawful. No bulk admission. No silent admission.** The validator runs green over the result in the same commit. |
| **W6-D2-E** | W6-D2 completion record | Closes the deliverable only after artefact, validator, seed decisions, registry, and proofs are all exact — a completion record in the standing closure style, naming what W6-D3 inherits and opening nothing. |

Resequencing within this set follows the standing precedent (IDs stable, dependencies honoured); a landing may be merged with its neighbour **only** if its own authorisation explicitly justifies why the merged landing is safer than the split — the default is five.

## 5. The thirty-three strings — seed corpus posture

The source-derived count, carried exactly: **eleven Wellness · eleven Kitchen · eleven Gym · zero Meditation** — and **the Meditation zero remains a source-derived finding, not an error to fill.** At this brief's landing and until W6-D2-D: the thirty-three are **seed corpus candidates, not catalogue entries**; they are **not graded, not admitted, not renderable**; and W6-D2 must admit or reject each through its own governed admission process, where **rejection is a lawful outcome** and every decision is on the record. Grading — the D5-T24 language-law pass — is W6-D3's and happens to admitted strings later, behind its own brief; admission here is governance fitness under ADR-0042, never quality judgement.

## 6. Validator posture

The current posture, stated exactly: **the validator is dormant** — `check_m13_catalogue_dormancy` asserts dormancy only, and **the current dormancy assertion is not catalogue-ID validation**. **This brief does not wake, edit, or activate it.** Waking is W6-D2-C's own governed landing, which must implement the thirteen ADR-0042 Part F obligations exactly — grammar, uniqueness, no-pre-authority IDs, class-as-data, lawful classes, barred-word and stem absence outside the prohibition register, accompaniment linkage, derivation references, source-bounded citations, supersession semantics, no ranking in IDs, no record without accepted source authority, no display-authorisation from ID presence — **with validator proof same-commit with the catalogue artefact it validates.**

## 7. The catalogue-ID gate

Carried from ADR-0042 in full: the **`CAT-####` namespace is grammar-only until a W6-D2 landing lawfully allocates**; IDs, once allocated, are **stable · immutable except through visible supersession or retirement · never reused**; an ID encodes **no room, class, priority, ranking, or confidence**; an ID is **never a verdict, never a source citation, never a display authorisation** — necessary, never sufficient. No ID exists at this brief's landing, and any identifier appearing in W6-D2 planning material before allocation is marked non-final.

## 8. Acceptance criteria — when W6-D2 is complete

W6-D2 is complete only when, and only through its authorised landings: the catalogue artefact exists with its shape and home governed by record · the validator is awake and green under same-commit proofs · **every admitted string carries its class, source, and required derivation/accompaniment/prohibition metadata as data** · **every seed string is either admitted or rejected on the record** · no barred word or stem appears outside the lawful prohibition register · no catalogue ID encodes or confers authority · **no label is rendered and no surface exists** · and W6-D3 remains unopened until its own brief. Completion is recorded by W6-D2-E and claims exactly this — a governed register exists and is validated — and nothing more: **a complete catalogue is doctrine-conformant storage, not display, not grading, not approval of a single word's wording.**

## 9. Boundaries with the other deliverables

**W6-D2** builds the register. **W6-D3** grades admitted strings per D5-T24 and reviews the historical register items, behind its own brief. **W6-D4** builds surfaces under ADR-0043's twenty proof obligations, behind its own brief. **W6-D5** audits presentation against sources. **W6-D6** closes the phase. Nothing in W6-D2 renders, grades, surfaces, audits, or closes — and nothing in this brief opens W6-D3, W6-D4, W6-D5, or W6-D6.

## 10. What remains unopened and untouched after this brief lands

W6-D3 through W6-D6 and W7: unopened. The catalogue artefact, schema, entries, and IDs: nonexistent. The validator: dormant. The thirty-three strings: candidates, untouched. The nine pending stubs: visible and unconverted. The evaluation records, fixtures, runtime, Lane C, Tier 3 rows, and applicability records: byte-untouched. The generative era: assigned to no phase, behind ADR-0034's first-contact gate. No model contact, no dependency, no E10/vendor, Z4, E12/Z5, or hosted movement. **And no wording in this brief — or in any W6-D2 landing it plans — may imply that the catalogue, a catalogue ID, or the brief itself authorises display, proof, safety, approval, review, conversion, retirement, correctness, or readiness of any kind.**

## 11. Public-safety considerations

Generic and structural wording — catalogue, register, string, record, class, validator, landing. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. No real user data, no vendor or model names, no URLs, and no claim of any kind about any person, string, or readiness.

## 12. Boundary

**This brief opens W6-D2 and nothing else.** The next lawful step is the W6-D2-A landing — the catalogue artefact shape and home decision — through its own authorisation, only if Tara asks.

---

*The plan for the register, in the register's own spirit: five small doors instead of one large one, a watcher woken only when there is something true to watch, and thirty-three candidates who will each hear their name read out — admitted with their papers in order, or declined with the reason written down. Nothing about the catalogue will ever need to be taken on faith, including how it was built.*
