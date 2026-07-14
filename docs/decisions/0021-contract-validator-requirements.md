# 0021 — Contract Validator Requirements

**Status:** Accepted by human reviewer, 2026-07-15. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (sixth and final doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — the obligations are already sealed in ADR 0016–0020, and the suite conventions this record elevates were inspected read-only in the accepted brief.
**Controlling law:** the W0 no-new-authority discipline; ADR 0003 (ceremony); ADR 0016–0020 (the obligations classified); the W4 runway's accepted rulings (W4-AR §4.6).
**Blocks:** the Validator hooks section of every room contract (W4-D2 … W4-D5), which classifies its terms under this record's rule; the future W4-D6 validator plan/build deliverable, which operationalises this record.

## 1. Decision question

Five doctrine records created the obligations every room contract must satisfy; the deterministic suite that enforces governance has existed since W2. **Which contract terms get mechanical validators, which remain review-only, and how is that line drawn honestly** — so accepted grammar acquires executable teeth without a machine ever becoming the author of doctrine?

## 2. Context

W4 is open for governed doctrine and brief work only; this is the sixth and final W4-D1 doctrine record. Once it lands, the doctrine set is complete and the four room contracts (W4-D2 … W4-D5) may be drafted, each carrying a Validator hooks section that classifies its terms under this record. The classification is decided *before* the contracts exist so the machine's jurisdiction is fixed before there is anything to check — the wall-checking machine is never allowed to become the wall.

## 3. Controlling sources and accepted rulings

- **The accepted runway rulings (W4-AR §4.6):** the decidability-drawn line; the one-suite recommendation (phase-named tests); the catalogue-ID validator class as W6-dependent, with W4 records as review of record until the governed string catalogue exists (the established review-of-record precedent, cited as precedent only).
- **ADR 0016–0020** — the obligations inventory (§10).
- **The existing deterministic suite, inspected read-only:** one `unittest` discovery over the test tree, deterministic standard-library checks; phase-named tests; machine-readable source transcriptions backing exact-quotation checks; the validator authority rule already in ink (*a validator that conflicts with its source is defective*); and a bounded pending/deferred marker precedent (an explicitly skipped stub naming an owner and an unblocking condition). These are cited as **precedent**, not mandated as syntax (§16).

## 4. Decision

1. **Decidability draws the line.** A contract term receives a mechanical validator **if and only if** its correctness is decidable from deterministic repository artefacts without interpretation. **Implementation cost does not determine the classification.**
2. **No judging validator.** *"A judging validator is doctrine minting by machinery."* Where a check would require judgement, the term is review-only; the validator may route the matter to human review, never decide it.
3. **No ambiguous middle.** Every Validator hooks entry classifies its governed term as exactly **mechanical** or **review-only**; compound terms are decomposed.
4. **The common validator classes** are fixed at doctrine level (§11–§12); room-specific classifications belong to the contracts and the later W4-D6 plan.
5. **Contract validators are document checks, never behaviour checks** (§13). No runtime or model-behaviour validator is authorised.
6. **Failure behaviour is deterministic, evidence-bounded, and never self-repairing** (§14), with **minimum safe evidence** only.
7. **A mechanical pass is not acceptance** (§15); a failure is evidence, not authority.
8. **Validators extend the one existing deterministic suite** with phase-named tests (§16).
9. **DR-W4-06 and W4-D6 are distinct**, and **validator implementation is gated until all four contracts are accepted** (§17–§18).
10. **The catalogue-ID class is W6-dependent and dormant** until the governed string catalogue exists (§19).

## 5. Constitutional check

- **No new authority:** this record mints no edge, class, consent form, or authority state; it classifies how already-accepted rules may be checked, and adds no new room rule.
- **The no-judging rule serves the W0 discipline:** a validator that interpreted doctrine would mint doctrine by machinery — the rule forbids the machine the authority the ceremony reserves for reviewed records and the human reviewer.
- **The source-wins principle is preserved:** where a validator conflicts with its source, the validator is defective; a finding never amends a contract or a record.
- **No law required reinterpretation**, and **no sealed open question — including W1-D3 §10.6 — is touched.**

## 6. Decidability as the governing line

A term is mechanically checkable **iff** correctness is decidable from deterministic repository artefacts without interpretation. Cost is irrelevant to classification: a mechanically decidable but expensive check remains mechanical in doctrine; a cheap check that requires judgement remains review-only.

## 7. Mechanical versus review-only classification test

A validator is **mechanical** only when all of the following hold: (a) the complete required evidence is present in deterministic repository artefacts; (b) the expected result can be stated before execution; (c) the check has a stable pass/fail or exact-mismatch result; (d) the same artefacts yield the same result for any conforming implementation; (e) no intent, quality, adequacy, or policy judgement is needed; (f) the validator can explain the concrete artefact mismatch it found. Fail any one criterion and the term is **review-only.**

## 8. No judging validator

A validator must not decide: whether wording is wise; whether a prohibition is semantically exhaustive; whether a rationale is persuasive; whether a named-bait list captures every meaningful risk; whether room tone is sufficiently clear beyond an exact settled requirement; whether an uncertainty statement is protective enough; whether a contract has made the correct policy choice; whether an unresolved doctrine question should be answered; whether a source should be amended; whether two ambiguous passages mean the same thing. Where any such judgement would be required, the contract labels the term **review-only**; the validator identifies the relevant artefacts and routes the matter to human review.

## 9. No ambiguous middle

No term may be "partly automated" without a precise decomposition; "best effort"; "probably checkable"; silently unclassified; or represented as mechanical when a hidden human judgement is required. **A compound term is decomposed** — e.g. section *presence* is mechanical while the section's substantive doctrinal *adequacy* is review-only.

## 10. Common contract-term inventory

The obligations the five landed records create for every contract: **ADR 0016** — four separate contracts; eleven fixed sections in fixed order and numbering, present and non-blank; "Not applicable —" with a reason; the Open questions section with its exact empty wording; the Validator hooks section; the constitutional check. **ADR 0017** — the Processing Boundary section instantiates the isolation standard and cites its record (declaration only; operational isolation is W5's). **ADR 0018** — scope in the paired form (exact reference + complete verbatim quotation, mismatch fails); load-bearing words preserved; source-backed blur-words absent from scope clauses; the Meditation scope from its complete edge list. **ADR 0019** — the named-bait list (floor not ceiling); each bait mapped one-to-one to a declared future evaluation fixture; canonical placeholder vocabulary; the rejected tokens absent. **ADR 0020** — the shared behaviour table quoted intact; all six W1-D3 states; the acknowledgement-not-a-functional-block clause where required; inherited §10.6 wording unaltered where carried; room wording routed to the future catalogue (dormant until W6).

## 11. Mechanical validator requirements matrix

Doctrine-level classes, each source-verified as decidable. Common columns, stated once: **deterministic inputs** = the four accepted contract files, the cited source records and their transcriptions, and the registry; **implementation timing** = the class is defined now, but every per-contract check is **gated until W4-D2…D5 are all accepted**; **human review after a mechanical pass** = **always required** (§15).

| # | Term-class | Source | Artefact | Decidability proof | Pass condition | Bounded failure evidence |
|---|---|---|---|---|---|---|
| M1 | Four distinct contracts; exactly one room identity each; no duplicate room | ADR 0016 | Contract file set + room-identity fields | File count and identity fields are enumerable | Four contracts; one room each; no duplicates | The missing/extra/duplicated path or identity |
| M2 | Fixed sections, order, numbering; non-blank | ADR 0016 dd.2–3 | Section headers and bodies | Template fixes the exact list/order/numbers; presence and non-blankness are string-decidable | All eleven, in order, numbered, non-blank | Section number + mismatch class (missing/misplaced/blank) |
| M3 | "Not applicable" carries a reason — **presence only** (adequacy is R3) | ADR 0016 d.4 | N/A bodies | Non-empty text after the marker is string-decidable | Every N/A has non-empty reason text | File + section of the bare N/A |
| M4 | Open-questions section; exact accepted empty wording | ADR 0016 d.5 | Section 11 | The empty form is a fixed string | Present; empty form matches exactly | Expected vs observed body (bounded) |
| M5 | Validator-hooks completeness — every governed term classified mechanical or review-only | ADR 0016 §9 + this record | Section 9 | Classification tokens are enumerable against the section's own term list | Every term carries exactly one classification | The unclassified or double-classified term |
| M6 | Scope integrity — exact reference resolves; verbatim quotation matches cited source exactly | ADR 0018 dd.2–3 | Sections 2–3 | The transcription mechanism exists (source-wins); byte comparison against the cited clause | Reference resolves; quotation == source text | Mismatch class + expected/observed token or hash |
| M7 | Load-bearing words present; source-backed blur-words absent in scope clauses | ADR 0018 (word sets) | Scope clauses | Fixed word lists over template-delimited sections (M2 makes boundaries decidable) | Words present; banned phrases absent | The missing word or banned phrase, by clause |
| M8 | Shared-table fidelity — ADR 0020 quotation intact; six states present; pause phrase absent; not-a-block clause present where required; inherited §10.6 wording unaltered | ADR 0020 | Section 5 | Exact-string checks against the review of record | Quotation matches; labels found; counts as required | First divergence, as bounded expected/observed values |
| M9 | Named-bait mapping — **declaration only**: list present; every bait has exactly one declared future evaluation-fixture reference (none zero, none multiple; unique where the settled format requires; format per the later W4-D6-authorised deterministic format) | ADR 0019 d.5 | Section 4 entries and declared references | Counting declared references per bait is arithmetic over structured entries | Every bait ↔ exactly one declared reference | The bait with zero/multiple references, by identifier |
| M10 | Placeholder mechanics — placeholder tokens drawn from the canonical set; rejected tokens absent (realistic-pair risk is R2) | ADR 0019 dd.6–7 | Bait lists and examples | The canonical set is closed; membership and absence are string-decidable | All tokens canonical; rejected-token count 0 | The offending token, by line |
| M11 | Cross-reference coherence — dependency IDs and source paths resolve; the isolation clause cites its record | ADR 0017; ADR 0016 | Citations | The registry's reference-resolution machinery is the existing precedent | Every citation resolves | The dangling reference |
| M12 | Anti-map consistency — forbidden items intersect no granted edge; the Meditation contract asserts exactly its complete edge list | ADR 0018 | Section 8 vs section 2 | Set intersection over enumerated identifiers | Empty intersection; Meditation set exact | The intersecting or missing identifier |
| M13 | Catalogue-ID dormancy — no catalogue-ID check claimed active before W6 | W4-AR ruling; §19 | Declared validator classes | The deferral declaration is itself an artefact | Class declared dormant with its named dependency and activation condition | An active claim before W6 |

**Nothing above is mechanical merely because a regex is possible:** each row rests on a closed word list, a fixed template position, an exact source text, an enumerable identifier set, or a counted structural declaration.

**M9 boundary (ruled):** the mechanical check covers the **declaration only.** It must not determine whether the future fixture currently exists before fixtures are authorised; whether the fixture is behaviourally adequate; whether the bait is substantively complete; whether a model takes the bait; whether forbidden inference occurs at runtime; or whether a proposed scenario is clinically or semantically appropriate. Fixture existence, fixture-format activation, and behavioural adequacy belong to the future W4-D6 plan and evaluation work.

## 12. Review-only requirements matrix

| # | Term | Source | Failed criterion (§7) |
|---|---|---|---|
| R1 | Named-bait-list substantive completeness / aptness | ADR 0019 (floor-not-ceiling) | (a),(e) — no artefact enumerates the full risk space |
| R2 | Whether a bait description captures the intended inference risk without becoming a new inference engine; realistic-pair risk | ADR 0019 d.6 | (e) — semantic judgement over open vocabulary |
| R3 | Doctrinal adequacy of a "Not applicable" reason | ADR 0016 d.4 | (e) — soundness is interpretation |
| R4 | Identity/purpose fitness | ADR 0016 §1 | (e) — quality judgement |
| R5 | Speech-rule application quality | pack R6 d.2 (human-and-eval judgment, not string matching) | (e) — reserved by the source |
| R6 | Room-register wording preserving meaning beyond exact settled strings or identifiers | ADR 0020 §12 | (e) — semantic preservation is interpretation |
| R7 | Constitutional-explanation soundness | ADR 0016 §10 | (e) — argument quality |
| R8 | Semantic scope expansion or authority minting beyond literal identifiers | W0 discipline | (e) — semantic effect evades literal checks |
| R9 | Contextual clarity of uncertainty or contradiction wording beyond exact settled strings | ADR 0020 | (e) — context sufficiency |
| R10 | Completeness of behavioural prohibitions | ADR 0019 d.3 | (a),(e) — Law 8 binds beyond every enumeration |
| R11 | Runtime obedience; operational isolation; runtime forbidden inference | ADR 0017/0019 | (a) — not repository artefacts; W5/evaluation territory |
| R12 | Any clinical, diagnostic, medical, or therapeutic judgement | standing corpus prohibition | never machine-decided, and never decided by this project's validators at all |

## 13. Contract validators versus behavioural evaluations

A **contract validator** examines deterministic repository artefacts and asks whether a contract *document* conforms to accepted doctrine. A **future evaluation fixture** examines *implemented behaviour* under a controlled scenario. Sharply: document structure and exact quotation are validator territory; the *declaration* of bait-to-fixture mapping is validator territory; **fixture existence activates only under the later authorised plan; fixture adequacy and system behaviour are evaluation territory; operational isolation belongs to W5 enforcement/evaluation; model behaviour is never evaluated by a contract-document validator; DR-W4-06 authorises no runtime validator.**

## 14. Validator evidence and failure behaviour

Future validators must: fail deterministically; return non-zero on mechanical non-conformance; identify the exact file and the exact contract section or field; name the governing source; name the mismatch class; show **minimum safe expected-versus-observed evidence**; distinguish **missing, mismatched, duplicated, unresolved, deferred, and review-required** states; and must **never** auto-repair, silently normalise a quotation, fill a missing section, select one interpretation, or suppress a failure because the intent appears obvious.

**Minimum safe evidence (ruled):** expected-versus-observed reporting does **not** authorise dumping full room contracts into logs; dumping future fixture bodies; exposing real or sensitive profile material; copying unrelated contract sections; retaining sensitive mismatch content beyond the test run; or producing clinical or inferential explanations. Permitted evidence, as appropriate: repository-relative file path; contract section or field identifier; governing record and section; mismatch class; expected and observed **token, identifier, hash, count, or bounded structural value**; a short safe excerpt only when necessary and public-safe. **Prefer hashes, counts, identifiers, and bounded snippets over full-content logging.**

**Dormant and review-required marking (ruled semantics, not syntax):** a dormant or W6-dependent validator class must be **visibly deferred**; the deferral must **name its owner or governing future dependency** and **the condition that activates it**; and it must **never be reported as passing, implemented, or active.** The repository's existing bounded pending-marker pattern demonstrates that such honest deferral is practicable — it is cited as **precedent only**: no decorator, parameter names, file location, or implementation shape is mandated; the exact implementation belongs to the later W4-D6 plan. For review-only items, the suite reports a bounded review-required marker only where the accepted W4-D6 plan later defines one — review-required is never converted into a mechanical pass or failure by interpretation. No implementation syntax is mandated by this record.

## 15. Mechanical pass versus human acceptance

**A mechanical pass means only that the decidable document properties conform.** It does not mean: the contract is accepted; the room is safe; the room is complete; the doctrine is correct; implementation is authorised; model contact is authorised; or room operation is authorised. Human review and the full governance ceremony remain necessary. **A failure is evidence of non-conformance only** — it does not amend doctrine, choose the repair, or authorise edits; where a validator conflicts with its source, the validator is defective.

## 16. One-suite and phase-named-test direction

**Validators extend the existing deterministic suite** with phase-named tests consistent with repository convention. The inspected suite is cited as precedent: one unittest discovery suite; deterministic standard-library checks; phase-named tests; machine-readable source transcriptions; source-wins validator authority; and the bounded pending/deferred precedent. **Not mandated:** exact future test filenames; exact test function names; an exact decorator; and **not created:** a second harness, a standalone validator CLI, a parallel runner, a validator service, or any new dependency.

## 17. DR-W4-06 versus W4-D6 namespace

Two different things sharing a number, spelled out to avoid the naming trap: **DR-W4-06** is the sixth W4-D1 *doctrine record* — it decides the classification principles and contains no plan, test, or validator implementation. **W4-D6** is the later operational *plan/build deliverable* — it may specify exact checks after DR-W4-06 lands; its exact room-specific checks must be grounded in accepted contracts; and it requires its own bounded authorisation.

## 18. Four-contract acceptance and implementation gate

**Validators are built against accepted contracts, never drafts.** Validator implementation must not land until **W4-D2, W4-D3, W4-D4, and W4-D5 are all accepted** — their final paths and hashes known, their named-bait lists settled, their validator-hook classifications reviewable. After implementation: the validators run against all four accepted contracts; the extended suite must be green before W4 closure; future contract changes must keep the validators green; and **a validator finding does not itself authorise a contract amendment.**

## 19. W6 catalogue-ID dependency

Catalogue-ID existence, routing, and semantic-binding checks are **W6-dependent.** Until the governed string catalogue exists: the accepted W4 records are **review of record** for settled wording; exact settled quotations are mechanically checkable where the source artefact exists (M8); catalogue-ID validation is **dormant/deferred**, with the class **naming its activation dependency**; **no fake, provisional, or temporary IDs; no placeholder catalogue; no active-pass claim.** The dependency blocks nothing in W4 and authorises no reading or implementation of W6. Once W6 exists, the future W4-D6 plan may activate the class through its own authorised amendment or implementation milestone.

## 20. Relationship to ADR 0016 through ADR 0020

**ADR 0016** supplies the fixed contract shape and the Validator hooks section (M1–M5 and the classification home). **ADR 0017** supplies the isolation doctrine — this record may check contract *declarations* (M11), never adapter reality (W5's). **ADR 0018** supplies the exact-reference-plus-verbatim fidelity targets (M6–M7). **ADR 0019** supplies the named-bait and future-fixture-mapping targets (M9–M10); semantic bait adequacy stays review-only (R1–R2). **ADR 0020** supplies the shared table and exact uncertainty requirements (M8); W6 later supplies catalogue IDs. **This record adds no new room rule — it classifies how already-accepted rules may be checked.**

## 21. Alternatives considered

- **Decidability-drawn line (chosen).** Mechanical iff decidable from artefacts without interpretation. Chosen because it gives accepted grammar executable teeth while structurally denying the machine any doctrinal authority.
- **Validate everything with heuristics (rejected).** Heuristic judgement encoded in code is doctrine-by-code — the judging validator by another name.
- **Review-only contracts (rejected).** The machinery exists precisely so accepted grammar acquires executable teeth; leaving every term to review wastes the suite and invites drift.
- **A second validator harness / standalone CLI (rejected).** Closed by the accepted one-suite ruling; a parallel runner fragments the single deterministic battery that has enforced governance since W2.

## 22. Consequences

- **Easier:** the four contracts are written knowing exactly which of their promises a machine will hold them to, and reviewers focus judgement where only judgement works.
- **Easier (later):** the W4-D6 plan starts from fixed classes and principles rather than negotiating the machine's jurisdiction check by check.
- **Harder (deliberately):** no term may float unclassified; no check may quietly interpret; no pass may be waved through as acceptance; no dormant class may pretend to run.
- **Constrains future work:** validator implementation waits for four accepted contracts; the catalogue class waits for W6; every future contract change must keep the validators green through its own ceremony.
- **Preserved honesty:** the suite says exactly what it checked, what it deferred, and what it handed to humans — and never more than the minimum safe evidence.

## 23. Non-goals

This record does not decide or create: exact room-contract contents; room-specific validator hooks; room-specific named-bait lists; exact validator filenames; exact test names; validator implementation; the W4-D6 plan; fixture contents; evaluation harnesses; adapter enforcement; prompts; payloads; sessions; review surfaces; UI; CLI; new dependencies; a governed string catalogue; W5 implementation; W6 implementation; resolution of W1-D3 §10.6; or new doctrine through machine interpretation. It builds no validator, test, fixture, contract, adapter, session, prompt, payload, surface, or engine code, and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples.

## 24. Public-safety considerations

Role-generic and structural wording throughout — user, room, contract, validator, suite, artefact, human reviewer, architect, model. Canonical placeholders only where unavoidable (Persona-K9, Condition-Q, Allergen-X, Medication-A17) — none is needed in this record. No private names, no model names, no real health data, no realistic clinical pairs, no diagnosis or treatment examples, no medical recommendations, no private or project lineage. **Validator logs carry no sensitive contract content beyond the minimum safe mismatch evidence** (§14). **No claim, ever, that validator passage makes a room medically safe** — a mechanical pass is a conformance fact, not a safety judgement. **A validator must never become a small inference engine** by embedding realistic prohibited relationships into its matching logic or fixtures — the rule that governs the bait lists governs the machinery that checks them. No companion framing except where a sentence names a prohibition.

## 25. Dependencies

W0 (the no-new-authority discipline the no-judging rule serves); ADR 0003 (ceremony); ADR 0016, ADR 0017, ADR 0018, ADR 0019, ADR 0020 (the obligations classified); and the W4 runway (W4-AR — the accepted rulings). W1 and W2 source records are not direct dependencies: their rules reach this record through the landed W4 doctrine, and the suite conventions live in the test tree. ADR 0009, ADR 0011, and ADR 0012 are precedent-only for the review-of-record treatment and are not direct dependencies. This record does **not** depend on W5 or W6.

## 26. Open questions

None at acceptance.

---

*The wall-checking machine is never allowed to become the wall. It may hold a contract against the exact words the ceremony accepted — and where words alone can't decide, its whole duty is to say so and hand the question back to the humans who can.*
