# 0022 — Contract Validator M10/M12 Decidability Correction

**Status:** Accepted by human reviewer, 2026-08-09. Not a build instruction.
**Date:** 2026-08-09 · **Phase:** W4 — Room Contracts (validator correction; deliverable W4-D6, Lane A)
**Amends:** ADR 0021 (Contract Validator Requirements) — the M10 and M12 rows of its §11 mechanical validator requirements matrix, and the Lane A mechanical instance arithmetic derived from them. By correction, not bypass.
**Decision mode:** implementation-derived. The defect was found by faithfully attempting the accepted doctrine against the four accepted room contracts, and is reproduced in this record from live measurement.
**Controlling law:** the W0 no-new-authority discipline; W2-D3 checklist rule 2 (two-tier change rule); ADR 0003 (ceremony); ADR 0018 (scope fidelity); ADR 0019 (canonical placeholders); ADR 0021 (the record corrected).
**Blocks:** W4-D6 Lane A validator implementation, which is suspended until this correction is accepted.

---

## 1. Decision question

ADR 0021 classified every contract term as mechanically checkable or review-only, with decidability — not implementation cost — drawing the line. Implementation of Lane A then attempted two of those mechanical classes against the four accepted room contracts and found that **one cannot be satisfied by any conforming contract, and one asks for a list the corpus deliberately does not contain.**

The question: **how are M12 and M10 stated so that each is genuinely decidable from deterministic repository artefacts, without minting semantics, rewriting contracts, or writing a deliberately-excluded token into durable data?**

## 2. Context

Lane A derived 48 mechanical check instances from ADR 0021's thirteen classes against the four accepted contracts. Implementation began, froze provenance and structural expectations from the accepted baseline, and reached the validator itself — at which point M12's pass condition failed all four contracts, and M10's second clause proved unsourceable. Implementation stopped rather than coding around doctrine.

**This record corrects the doctrine. It does not reinterpret it in code, and it amends no contract.**

## 3. Controlling sources and accepted rulings

- **ADR 0021 §11** — the M10 and M12 rows corrected here; and its governing line: a term is mechanically checkable *if and only if* its correctness is decidable from deterministic repository artefacts **without interpretation**.
- **ADR 0021 §8, §9** — no judging validator; no ambiguous middle.
- **ADR 0019 d.6** — canonical placeholders only; the canonical vocabulary is closed.
- **ADR 0018** — scope fidelity; contracts carry accepted words, and a validator consumes doctrine rather than minting it.
- **W2-D3 checklist rule 2** — material or semantic changes require a decision record, never an edit.
- **The four accepted room contracts** — the artefacts against which both defects were measured.

## 4. Decision

1. **M12 is decomposed into two named clauses, M12a and M12b.** The record's prior single row conflated an undecidable claim with a decidable one.

2. **M12a — Anti-map identifier fidelity (corrected).** Structurally extract the edge identifiers appearing in a contract's section 8, **excluding quoted and source-transcribed regions**, and compare the observed set against the **frozen accepted anti-map identifier expectation** for that contract. **Pass:** observed set equals expected set. **Fail:** any missing or unexpected identifier — the two named mismatch classes. **Bounded evidence:** the missing or unexpected identifier.

3. **M12a makes two explicit non-claims.** It makes **no claim** about whether the prose surrounding an identifier is semantically adequate, and **no claim** that overlap between section 8 and section 2 identifiers is itself a defect. **The prior "empty intersection" pass condition is withdrawn.**

4. **The accepted anti-map identifier expectations are:** Wellness `{E11-W, E9}`; Kitchen `{E10, E6}`; Gym `{E7}`; Meditation `{M1, M2}`.

5. **M12b — Meditation exact edge set (unchanged).** `§2 asserted edge set = §8 asserted edge set = {M1, M2}`, over asserted identifiers only, quoted and source regions excluded, the expected set drawn from frozen expectation data. **This clause is preserved exactly as accepted.**

6. **Semantic adequacy remains R10's.** Whether an anti-map is complete, whether its boundary language actually prohibits what it should, whether a prohibition has been semantically weakened, and whether the anti-map is substantively sufficient are **review-only**. **Mechanical fidelity never becomes semantic adequacy.**

7. **M10 — Placeholder closed-set membership (corrected).** Extract every placeholder-shaped token in a contract, excluding quoted and source-transcribed regions, and verify that each belongs to the **accepted canonical placeholder set**. **Pass:** every observed placeholder-shaped token is canonical — vacuously true where none is used. **Fail:** any placeholder-shaped token outside the canonical set.

8. **No rejected-token list exists or may be created.** The canonical vocabulary is **closed**, so membership alone decides the check. **No excluded literal may be written into expectation data, code constants, test names, failure examples, fixtures, documentation, or this record.** The prior "rejected tokens absent" clause is satisfied by closure, not by enumeration.

9. **The canonical placeholder set for contracts is closed at:** `Allergen-X`, `Condition-Q`, `Medication-A17`, `Persona-K9`. **Scope note:** `docs/governance/fixtures.md` admits a broader persona family for *fixtures*; **M10 governs contracts and does not govern fixtures.**

10. **Token-recognition grammar (governed here because no accepted source defines one).** A **placeholder-shaped token** is: an initial-capitalised alphabetic word, a single hyphen, one uppercase letter, and zero or more digits, at word boundaries — `\b[A-Z][a-z]+-[A-Z][0-9]*\b`. **This is M10's contract-token recognition grammar. It is not a Wing-wide definition of placeholder syntax and does not govern fixtures.** The rule is **deterministic and lexical only.** It **must not** enumerate any excluded placeholder, infer semantics, classify prose by heuristic meaning, or broaden itself dynamically from the artefact under test. It is anchored on the observed form of the accepted vocabulary in the W4 runway and `docs/governance/fixtures.md` (W2-D4). **If a future contract introduces another legitimate identifier matching this lexical form, that is a governed vocabulary/syntax question rather than something implementation may silently exempt.**

11. **Bounded failure evidence for M10.** The offending observed token may be reported where public-safety rules permit its durable output; where they do not, the validator reports **file, line, and mismatch class only**, per existing scan doctrine.

12. **M10's decomposition collapses.** Under a closed set, "tokens drawn from the canonical set" and "rejected tokens absent" are the **same proposition**. M10 becomes **one instance per contract**.

13. **Corrected Lane A arithmetic:** M10 **4** (was 5); M12 **5** (M12a 4 + M12b 1, count unchanged, semantics corrected); **total mechanical instances 47** (was 48). By scope: **set-level 2 · Wellness 10 · Kitchen 11 · Gym 11 · Meditation 13.** Immediately implementable after this correction: **47 of 47.** The review surface is **unchanged at 37**.

14. **The discovery history is preserved, not tidied.** The sequence was: `46 provisional → 48 source-derived planning count → implementation discovery → 47 corrected count`. **48 was legitimately derived from the then-accepted wording**; implementation faithfully attempted that doctrine; the real contracts proved M12a's pass condition unsatisfiable; source inspection independently exposed the M10 duplication; implementation **stopped rather than coding around doctrine**; the doctrine was then corrected. **No earlier record is rewritten to imply 47 was always known.**

## 5. Why the prior M12a wording could not hold

Measured live against the four accepted contracts, with quoted regions excluded:

| Contract | §2 identifiers | §8 identifiers | Intersection | Prior pass condition |
|---|---|---|---|---|
| Wellness | `E11-W`, `E5` | `E11-W`, `E9` | `E11-W` | **FAIL** |
| Kitchen | `E6` | `E10`, `E6` | `E6` | **FAIL** |
| Gym | `E6`, `E7` | `E7` | `E7` | **FAIL** |
| Meditation | `M1`, `M2` | `M1`, `M2` | `M1`, `M2` | **FAIL** |

**Four of four conforming contracts fail, and the failure is by construction rather than by drafting error.** Every accepted §8 states prohibitions **relationally** — naming the granted boundary and forbidding what lies past it: *"no processing edge beyond E11-W"*; *"beyond the E6 closed list"*; *"beyond E7"*; *"any edge beyond M1 and M2"*. The identifier inside §8 is therefore the **granted** edge, so the intersection with §2 can never be empty.

To pass a contract under the prior wording, a validator would have to decide that `E7` in Gym §8 means *"nothing beyond E7 is permitted"* rather than *"E7 is forbidden"* — a judgement about negation scope and noun-phrase role. **That is interpretation, which ADR 0021's own decidability line excludes, and it is judging semantic adequacy, which R10 already owns.**

## 6. Constitutional check

- **No new authority.** This record creates no category, edge, class, authority state, freshness state, grant, provenance regime, or permission. It corrects two validator classes and the arithmetic they generate.
- **No contract is amended.** The four accepted room contracts are untouched; correcting the validator rather than the contracts preserves *a validator consumes accepted doctrine; it does not mint doctrine.*
- **ADR 0021 is not edited.** Per checklist rule 2, this material change travels as a decision record.
- **Public safety is improved, not merely preserved** — see §9.
- **No law required reinterpretation.** No constitutional amendment is proposed or required.

## 7. Alternatives considered

- **Corrected M12a as identifier fidelity (chosen).** Keeps the property that was always decidable — that an accepted anti-map has not silently drifted — and abandons the one that never was.
- **Reclassify M12a wholly as review-only (rejected).** Discards a genuinely decidable property; identifier drift is checkable without interpretation.
- **Restrict M12a to Meditation (rejected).** Arbitrary; three rooms would lose all mechanical anti-map protection.
- **Amend the four contracts to enumerate forbidden identifiers (rejected).** Rewrites accepted contracts to suit machinery — the exact inversion of the validator's role.
- **Teach the validator prohibition semantics (rejected).** Prohibited by ADR 0021 §8 and by the decidability line; would make machinery decide what a contract means.
- **Enumerate rejected tokens for M10 (rejected).** No source names one; enumeration would durably reintroduce a deliberately-excluded literal; and under a closed set it adds nothing.

## 8. Consequences

- **Easier:** Lane A becomes implementable — 47 of 47 instances, none dependency-blocked.
- **Easier:** M10 needs no exclusion list, so the excluded literal never enters committed data.
- **Harder (deliberately):** M12a now requires a **frozen per-contract expectation**, so a lawful contract amendment must be accompanied by a governed validator-data update. The expectation cannot self-adjust.
- **Preserved:** M12b, LA-R1, the review surface at 37, and every other mechanical class.
- **Constrains future work:** any future room contract must have its anti-map identifier expectation frozen at acceptance; and any future placeholder vocabulary change is a change to a **closed** set, requiring its own record.

## 9. Public-safety considerations

The M10 correction is a public-safety improvement. The prior wording, implemented literally, would have required writing a deliberately-excluded token into durable committed data — expectation file, code constants, test names, or failure examples. **Closed-set membership removes that requirement entirely while catching the same violations.** Failure evidence stays bounded, and where public-safety rules prohibit durable output of an offending token, file, line, and mismatch class are reported instead.

Role-generic, structural wording throughout. No private names, no model names, no private or project lineage. No realistic clinical, dietary, injury, or spiritual-attainment association. The canonical placeholder tokens appear only as the closed set this record governs.

## 10. Dependencies

W0; W2-D3 (checklist rule 2, rule 10); W2-D4 (the fixture vocabulary anchoring decisions 9 and 10); ADR 0003; ADR 0016; ADR 0018; ADR 0019; ADR 0021 (amended); W4-AR; and the four accepted room contracts (W4-D2, W4-D3, W4-D4, W4-D5), against whose accepted contents both defects were measured and from which decision 4's anti-map expectations are drawn.

## 11. Open questions

**None at acceptance.**

---

*Doctrine is corrected by the thing it governs meeting the world. The rule said an identifier inside a prohibition must be a forbidden identifier; every contract instead wrote "nothing beyond E7", and none wrote "E7 is forbidden". Asking a validator to tell those apart was asking it to read. What it can do — and now does — is notice when the accepted list of names in an anti-map has quietly changed.*
