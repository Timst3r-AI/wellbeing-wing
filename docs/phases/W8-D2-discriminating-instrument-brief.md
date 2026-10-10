# W8-D2 — Discriminating Instrument: Opening Brief

**Status:** Accepted by human reviewer, 2026-10-02. **Effective on publication and remote verification**, at which point it opens W8-D2 for discriminating-instrument work only, and nothing beyond W8-D2.
**Date:** 2026-10-02
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D2 — Discriminating instrument
**Identity:** `W8-D2-DIB`, type `phase-brief`
**Position:** the opening brief of W8-D2. On its acceptance, publication and independent remote verification — and only then — **W8-D2 opens for discriminating-instrument work only. W8-D3 through W8-D7 remain closed.** This brief authorises no case, no corpus artefact, no authoring record, no commitment, no calibration, no disposition, and no contact surface.
**Derived public baseline:** `6e9e0f155944bea3117b82a5b4216ce6c50abaa4`, the published and remotely verified ADR-0054 landing
**Governed by:** the published W8 runway (`W8-AR`) and the effective `W8-D1-EDB`, whole; **ADR-0054, whole — the evaluation doctrine this instrument must be built under and may not reinterpret**; ADR-0046 through ADR-0053 as consumed by ADR-0054; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**W8-D2 builds the exam that can fail: a fresh authored synthetic corpus in which true governance deltas, negative controls and genuinely inconclusive cases are indistinguishable from the reviewer's side until the reviewer has answered. The whole deliverable is an exercise in withholding: the law that separates what a reviewer may see from what an author knew lands first, the cases land second, and the answers the authors intended stay sealed — committed by hash, revealed only after judgment, and never evidence for the judgment they were designed to test.**

## 1. What this brief opens, and what it does not

1. On acceptance, publication and independent remote verification, this record opens **W8-D2 only**, for the two-landing programme of section 2. **W8-D3 through W8-D7 remain closed behind their own briefs.**
2. Effective W8-D2 does **not** mean: that any case exists · that the case-shape law exists · that any disposition or calibration is authorised · that any class count or case-to-class mapping is disclosed · that any model contact is authorised · or that any later deliverable is open.
3. No case may be authored before the D2-B law of section 2 is accepted, published and remotely verified. **Case authoring before effective D2-B law is a stop condition, not a head start.**

## 2. The W8-D2 programme — two landings, each behind its own acceptance

### D2-B — Case-shape, evidence-separation and blinding law (proposed identity ADR-0055)

The law that lands **before the first case**. It must:
- define a **new W8 case class — never a reuse, extension or adaptation of the W7 GER class**, whose records, schema and law remain historically true and untouched;
- settle the **exact reviewer-visible case shape**: what fields exist, which are admissible source evidence under ADR-0054 Part F, and which are structural/provenance support material;
- settle the **neutral identity and ordering rules**: a deterministic, class-independent rule for case identifiers and presentation order that **cannot be chosen, gamed or read to signal authored class**;
- settle the **withheld-authoring-record shape** (section 5);
- settle the **commitment and reveal mechanism** (section 6), including the byte-exact reveal obligation and its stop-and-report rule;
- land with **structural proofs** in the established V-pattern: carriage, byte-stability and closed-set exactness only, with planted-mutant controls, and an explicit declaration that no proof decides or hints at any case's class or disposition.

### D2-C — Corpus materialisation and W8-D2 completion

Only after D2-B is effective: the landing of the **fixed reviewer-visible synthetic instrument** — the neutral case records — together with **one published SHA-256 commitment per withheld authoring record, bound one-to-one to the final neutral case identity**, and the W8-D2 completion record. **No human disposition and no calibration occur anywhere in D2.** The exact landing scopes of D2-B and D2-C are proposed in their own candidates against their own baselines; this brief fixes their architecture, not their path lists.

## 3. Corpus law

4. **The W8 corpus is fresh authored synthetic material, constructed from the public governance law under ADR-0054's authoring laws (Parts B, C and D).** It is **not copied, rewritten or adapted from the twenty-six W7 GERs, the W7 exam prose, or the twenty-six historical unknowns** — those remain historically true and carried exactly as the W7 closure record leaves them, and **they are not W8 case material**.
5. The corpus must **materially exercise all three ADR-0054 authoring classes** and the breadth of the doctrine: cases engaging a range of the nine recognised governed properties, negative controls varying a range of surface features, and inconclusive cases exercising the Part D conditions. **How many of each, and which case is which, is withheld authoring material** (section 6).
6. Every case must satisfy its ADR-0054 class-specific authoring law, checked at authoring and recorded in the withheld authoring record — never in any reviewer-visible surface.

## 4. Blinding and neutrality law

7. **Every W8 case has a neutral, class-opaque reviewer-visible representation.** Before disposition, **no reviewer-visible filename, identifier, metadata field, order, title, source label or other surface may disclose or encode** whether the case was authored as class A, class B or class C.
8. The reviewer-visible case shape contains **only** material the D2-B law expressly permits. At minimum it carries: **the paired variants, whole and symmetric**; synthetic provenance and integrity material that does not disclose authoring intent; and **a neutral case identity**. It contains **no pre-filled disposition, no intended answer, no authoring class, no governed-property answer key, no authoring rationale and no class-coded label** — nothing from which the authored class can be read or inferred short of performing the human review itself.
9. **Case ordering is class-independent by construction:** D2-B establishes a deterministic neutral ordering and identity rule, fixed before any case is authored, that cannot be selected to signal class. Ordering is never hidden evidence (ADR-0054 decision 30).

## 5. The withheld authoring record

10. **Each case's authoring record is a distinct withheld artefact**, never part of the reviewer-visible surface. It may contain: the authored class; the intended W8 disposition; the governed property or properties used in construction; the class-specific ADR-0054 authoring checks as performed; any deliberately varied surface features or deliberately underdetermined evidence; the locatable authoring rationale; the reviewer-visible case hash it corresponds to; and **a high-entropy commitment nonce whose only purpose is to make the published commitment non-enumerable**.
11. **The nonce is not a credential, provider secret, transport key, or repository authority. It carries no capability.** It exists solely inside the withheld synthetic authoring record until reveal, and is published with that record after disposition. Nothing about it touches ADR-0046's credential and secret prohibitions, which bind unweakened.
12. **Custody:** from D2-C's landing until the D2-C corpus's custody ends by its own separately governed act — which no session, reproduction or reveal of another corpus supplies — the exact withheld authoring records remain **byte-fixed outside the reviewer-visible repository surface, in an outside-repository review transport governed for this purpose by D2-B**. `W7-D6-HDR` §3 is precedent only for preserving review material outside the repository for a later governed handoff; **it is not prior authority for D2's byte-stable custody or commitment/reveal mechanics — those mechanics are established by this W8-D2 architecture and must be fixed completely by D2-B before any case is authored.** The withheld records' integrity must be enforceable at any time against the published commitments. **They must not be pasted into a relay packet, commit message, README, registry role, chat response, or any other surface the human reviewer could see before disposition.** If exact byte-stable custody across the D2-to-D3 handoff cannot be guaranteed **without introducing a provider, credential, secret store, private-data lineage or new dependency — STOP before any case is authored.**

## 6. Commitments, reveal, and non-disclosure of composition

13. **D2-C publishes one SHA-256 commitment per withheld authoring record, bound one-to-one to the final neutral case identity.** The commitment set is reviewer-visible; the preimages are not.
14. **Reveal belongs to D3, not D2.** Only after the required individual dispositions on a corpus exist may that corpus be revealed, and only under governed authority: the D2-C corpus's reveal, retirement or other custody end requires its own separately governed act, and a D3 reveal of the supplementary corpus authored under ADR-0059 reveals that corpus only — and **reveal must reproduce every previously published commitment of the corpus revealed byte-exactly before any calibration comparison is made. A mismatch is a stop-and-report event**, never a reconciliation exercise.
15. **D2 must not publicly disclose a class distribution, an expected token distribution, or any case-to-class mapping before review.** Composition belongs to withheld authoring material until post-disposition reveal, and **no balancing assumption, expected distribution or corpus-composition fact may become evidence for any case** (ADR-0054 decision 30's barred reasons bind).
16. After reveal, the authoring records become **post-disposition calibration material under ADR-0054 Part F** — never retroactive evidence for any disposition already made.

## 7. Doctrine carriage

17. **ADR-0054 binds this deliverable whole and is not reinterpreted by it:** the evidence architecture intact — case variants admissible source evidence, structural/provenance material support only, authoring material withheld, reveal post-disposition calibration material, **no category conversion**; the human review question **byte-identical to ADR-0054 decision 26**; all three W8 tokens available on every future case; **D2 authors no human answer**.
18. **An authored intended disposition is a construction hypothesis, not a certified correct answer.** Future disagreement between a human disposition and an authored intent is **calibration signal about the case or the instrument — not reviewer error, and not permission to rewrite either side silently**; any resolution is its own governed act.
19. **The nine ADR-0054 anti-collapse rules are carried whole wherever they are carried** — abbreviation is collapse by other means — and **no aggregate score, success rate, winner, grade, model verdict, readiness claim or equivalent may be introduced anywhere in D2.**

## 8. Boundaries

20. **Model contact:** D2 authorises no model contact, no prompt for actual contact, no provider, credential, SDK, transport, model binary or contact harness. **ADR-0047 precondition 3 remains untouched in its lawful resting state**, and W8-D6 remains the later, separately governed contact decision with no outcome preselected.
21. **Public/private:** the boundary carries whole — no real-person data of any kind, no identified-person material, no real device or wearable data, no private relationship or lived-interaction material, no private model transcripts, no credentials or secrets, no machine-identifying detail beyond permitted class-level information, no model binary, no real-person evaluation channel, no private-adoption implementation detail, nothing that would turn the public Wing into a live personal instrument. **Synthetic-first remains by construction, never by scrubbing.**
22. **Standing per-landing duties:** P2 and Q3 at every D2 landing; P4a reported separately; **a fresh P4b human act at every D2 landing**, never inferred from P4a or from any machine result.
23. **Carried states, untouched — no cleanup by proximity:** ADR-0047 precondition 3 · Part Q and the `local-wordlist` seam · the twenty-six historical unknowns · the nine pending stubs · the inherited W6 inventory · the named stale `docs/governance/registry.md` derivative · all other W7 closure carriage.

## 9. Stop conditions

Stop and report — never absorb — if any of the following occurs: authoring intent cannot be kept blinded through the reviewer-visible surface · the exact withheld package cannot be retained byte-stable through D3 under section 5.12's terms · any class leakage through identifiers, filenames, metadata or ordering · any need to reuse the W7 GER class · any need to expose class counts or composition before review · any case authoring before the D2-B law is effective · any calibration or disposition during D2 · any model-contact surface · any public/private boundary risk · any need for a governed property not already recognised by ADR-0054 (a revealed need is reported for its own amendment; it never extends the law) · any conflict with a governing source · or any landing that cannot stay within its accepted path scope.

## 10. Builder autonomy

Within these boundaries the builder owns the route: prose organisation, exact file naming where a mechanically superior convention exists, registry and board wording, proof organisation, deterministic ordering-rule design, and mechanically equivalent implementation choices — with no routine relay. **The architecture boundaries of sections 2 through 9 are not builder-variable.**

## 11. Acceptance criteria for this brief

This brief is acceptable only if the human reviewer agrees that: W8-D2 is a two-landing programme — law before cases, cases before nothing else · the corpus is fresh synthetic material and the W7 corpus is not case material · the reviewer-visible surface is class-opaque with blinding enforced down to filenames, identifiers, metadata and ordering · authoring records are withheld, committed by per-case SHA-256 with a non-enumerability nonce, and revealed only post-disposition by D3 with byte-exact reproduction required · composition and class counts stay withheld until reveal · ADR-0054's evidence architecture, review question, tokens, anti-collapse rules and case-independence law carry unweakened · authored intent is a construction hypothesis and never a certified answer · no contact surface, no aggregate vocabulary, no boundary weakening, and no carried state moves · and every stop condition of section 9 escalates rather than absorbs.

## Reconciliation note (ADR-0059)

Sections 12 and 14 are reconciled in place by ADR-0059, so that custody and reveal bind each corpus separately: no session, reproduction or reveal of the one supplementary corpus that record opens ends, opens or reveals the D2-C corpus's custody. The reconciliation is effective only on ADR-0059's acceptance, publication and remote verification. Every other provision is unchanged, and the D2-C completion record stays as built.

## Public-safety note

Generic and structural wording throughout — case, variant, class, commitment, reveal, reviewer, instrument. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*An exam is only as honest as its envelope. D2 spends one landing on the envelope and one on the paper inside it, and publishes nothing but sealed wax where the answers would be — because the first time anyone learns what the authors intended must be after a human has already said what the evidence shows.*
