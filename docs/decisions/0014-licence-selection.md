# 0014 — Licence Selection

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (project-level decision; not a deliverable of the engine track)
**Decision mode:** values-derived, from the reviewed licence values pass; no evidence spike required.
**Blocks:** the LICENSE/NOTICE landing; the repository's readiness for external adoption and, eventually, external contribution.

## Decision question

The repository is public and now contains real product code, but no licence — which means default copyright: there is no general reuse permission. The concept overview states that broad adoptability is the goal and that the licence question is open and deliberate. This record closes it: **under what terms may the world read, reuse, and build on this work — and how is the project's governance intent preserved without bending a legal instrument to carry it?**

## Context

The Wing's stated identity is a pattern any system — including commercial and closed-source systems — could adopt for holding sensitive personal evidence without interpreting it. Real-world health tooling is overwhelmingly commercial and often closed-source; a licence that excludes those adopters would quietly convert "broad adoptability" into "adoptable by hobbyists." At the same time, the project has boundaries that must travel with the work: no implication of medical or therapeutic service, no implication that forks inherit the trust this repository's ceremony earned, and no confusion between the governed original and derivatives.

## Goals

Permit, deliberately and completely: reading, cloning, learning from the pattern, reuse, modification, redistribution, **commercial use, and closed-source use**. Preserve, by the right instrument in each case: attribution; warranty and liability disclaimers; the public-safety boundaries; the fork/endorsement distinction; and the principle that governance records certify this repository's process, never a derivative.

## Options considered

- **Apache License 2.0.** Permissive; adds an explicit patent grant, an explicit trademark non-grant, the NOTICE mechanism, and standard vetted terms with wide recognition. **Selected.**
- **MIT.** Acceptable in principle — shortest, universally trusted, covers attribution and disclaimer — but silent on patents, trademarks, and redistribution notices, which are exactly the three preserve-list items a licence *can* carry. **Not selected.**
- **BSD-3-Clause.** Carries a non-endorsement clause but lacks the patent grant and NOTICE mechanism. Dominated by Apache-2.0 for this intent. Not selected.
- **GPLv3 / AGPLv3.** **Rejected for v1 — a mission-fit rejection, not an anti-copyleft principle.** Copyleft protects software freedom by requiring derivatives to open; the Wing's mission is pattern propagation into systems that may be closed. The two are honourable and incompatible here. A future record could revisit if the mission changes.
- **Custom / moral-use licence.** **Rejected firmly.** The project's own doctrine-instinct applies: no custom cryptography, no custom legal instruments. Bespoke wording is unvetted, has no case law, chills adoption, and moral-use clauses are practically unenforceable. Governance intent belongs in documentation, not in bespoke licence clauses.
- **No licence (status quo).** **Rejected.** Default copyright leaves no general reuse permission and contradicts the published adoptability intent every day it persists.

## Decision

1. **The repository adopts the Apache License 2.0 for v1**, as published by the Apache Software Foundation, **standard and unmodified — byte-for-byte, never edited**.
2. **The copyright holder line uses the public GitHub repository owner/organisation name**, verified from the repository's public remote at landing. No private personal name appears unless the human reviewer explicitly directs it; had the owner string been ambiguous, the landing was to stop and report.
3. **A root NOTICE file accompanies the licence** — short, standard-compatible, carrying: the project name; the copyright notice; the non-endorsement/fork distinction; the pointer that this project is not medical, therapeutic, diagnostic, safety-intervention, crisis-response, or companion software; and the statement that governance records describe this repository's process, not certification of derivatives. **NOTICE is informational, not a custom moral-use licence — it grants nothing, restricts nothing, and adds no licence terms.** It provides a standard redistribution notice vehicle for attribution and boundary statements, nothing more.
4. **The README carries a short licence / forks-and-adopters section** — plain, not duplicating the concept overview — stating: the licence is Apache-2.0; forks and adaptations must not imply endorsement or equivalence; governance records certify only this repository's process; no medical, therapeutic, diagnostic, safety-intervention, or crisis-response claim is made.

## Rationale

Apache-2.0 is the only standard permissive licence that carries three of the preserve-list items natively: the patent grant removes the silent blocker that keeps cautious legal teams away from health-adjacent code; the trademark non-grant states in vetted text that forks get the code and not the name; and the NOTICE mechanism provides a standard redistribution notice vehicle for attribution and boundary statements, without adding licence terms. Everything else the project wants to preserve is documentation's job, and the documentation already exists. The licence stays a licence; the corpus stays the corpus.

## What the licence does

Grants everyone a perpetual, worldwide, royalty-free copyright and patent licence to use, reproduce, modify, and redistribute the work, commercially or not, open or closed, with attribution and the standard redistribution notice; disclaims all warranty and liability in standard terms; terminates the patent grant of anyone who litigates claiming the work infringes their patent.

## What the licence does not do

It does not grant the project's name or any trademark rights to derivatives. It does not certify, endorse, or extend this repository's governance ceremony to any fork. It does not prevent someone from building something contrary to the Wing's values with this code — no standard licence can, and this record chooses adoption over the illusion of control. It does not make any medical, safety, or fitness-for-purpose claim; it expressly disclaims them. And it does not prevent name confusion outright — trademark non-grant helps, but goodwill protection is a trademark-law matter outside any licence's power; the honest mitigation is the NOTICE text and the README section.

## Documentation / NOTICE division of labour

- **LICENSE:** the standard Apache-2.0 text, unmodified, ever.
- **NOTICE:** the short standard redistribution notice — project name and copyright line; forks and adaptations are not endorsed and must not claim endorsement or equivalence; this project is not medical, therapeutic, diagnostic, safety-intervention, crisis-response, or companion software; the governance records describe this repository's own process and do not certify derivatives.
- **README licence section:** the plain-language restatement, with a pointer to the concept overview and the registry for the full picture.
- **Governance corpus:** unchanged — it already carries the intent; this record simply refuses to duplicate it into legal text.

## Implications for forks and adopters

Anyone may take the engine, the pattern, or both — into products, services, research, or other archives — commercially or not, closed or open. What they may not take: the implication that this repository's reviewed ceremony vouches for their derivative, or the project's name as endorsement. Adopters inherit the code and the documented honest limits; trust they must earn the way this repository did — in the open, or not at all.

## Public-safety boundaries

This record and the LICENSE/NOTICE landing introduce no health content, no private names, no model names, and no machine identity. The not-medical statement in NOTICE is a boundary declaration, consistent with the concept overview and the corpus-wide prohibition texts already allowlisted by precedent. Scan findings on prohibition wording follow the established allowlist pattern with per-line justification.

## Non-goals

Does not open external contributions or select a contributor process (DCO/CLA is its own future decision); does not create any trademark registration or enforcement posture; does not decide licence treatment for future separately-published artifacts (each would get its own review); does not modify the concept overview; does not touch the engine, tests beyond the directory-fence amendment the two authorised root files require, registry conventions, or any governance doctrine.

## Landing requirements

One atomic landing: root `LICENSE` (standard Apache-2.0 text, byte-exact), root `NOTICE`, this record, the README section, and the registry entry and rendering row in the same commit (registry advances to 31). **Fence-crossings: `LICENSE` and `NOTICE` are two new root files, each explicitly authorised at Tier F by the human reviewer**; the self-testing directory fence admits exactly these two names under that authority and continues to reject any other root addition. No product code rides in the landing.

## Deferred questions

1. Contributor process (DCO/CLA and whether contributions open at all) — its own future decision.
2. Any trademark or name-protection posture beyond the licence's non-grant — future, if ever.
3. Licence treatment of future separately-published artifacts (specs, datasets, fixtures published standalone) — per-case future records.

## Risks

Apache-2.0's length can read as heavyweight for a small repository — cosmetic, and outweighed by the patent and NOTICE mechanics. Apache-2.0 code cannot be incorporated into GPLv2-only projects (GPLv3-or-later is compatible) — a minor, accepted edge. The trademark non-grant does not fully prevent name confusion (stated honestly above). The NOTICE file's boundary language must stay descriptive; any drift toward restrictive wording would recreate the rejected moral-use licence by the back door — decision 3's "informational, not a licence" rule is the guard, and review is the enforcement.
