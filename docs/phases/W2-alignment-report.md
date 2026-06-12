# W2 — Governance Evaluation & Enforcement Foundations

## Phase Alignment Report

**Status:** Accepted by human reviewer, 2026-06-12 — W2 runway. Authorises future W2 briefs, not immediate scaffolding. **Date:** June 2026 **Governed by:** W0 Constitution; ADR 0001; ADR 0002; W1-D1, D2, D3, D5, D6 (all accepted)

---

**W1 made the Wing governable. W2 makes the governance testable — before the Wing becomes useful.**

## 1. Purpose

W1 produced a complete governance corpus: laws, key custody, boundaries, consent grammar, authority grammar, surfacing doctrine, threat model, and evaluation plan. Every promise in that corpus is currently held up by review discipline alone. W2's purpose is to translate the corpus into **enforceable scaffolding and evaluation readiness**: a phase where the governance acquires executable teeth, synthetic test ground, and self-enforcement machinery — while deliberately building nothing a user would ever touch.

The risk W2 exists to prevent is specific: if implementation begins before the grammars are testable, the first working code becomes de facto authority ("but it works") and the documents quietly demote themselves to aspiration. D5 named this family of failure — governance theatre (D5-T24), seam erosion (Principle 6), authority inflation by existence. W2 is the structural answer: **prove the rules can be checked before building anything the rules must check.**

## 2. The A–D decision

**Recommendation: D — a combination, with strict fences.** Specifically: docs-only planning (A) **plus** limited repo scaffolding (B) **plus** the first deterministic test skeleton (C), under one governing rule that keeps the combination safe:

**The only code W2 may contain is code that checks rules. No code that does things for users.**

Rationale for rejecting the pure options: A alone cannot satisfy W2's own purpose — a phase about testability that ends with zero executable assertions has proven nothing and closes on faith. C alone, without the registry and closure scaffolding, builds tests against an un-indexed corpus and invites drift between what the documents say and what the tests check. B alone is scaffolding with nothing to scaffold. The combination is coherent because all three legs serve verification and none serves features.

## 3. What W2 may touch

- `docs/` — closure records, registry, guardrails, fixture strategy (documentation, as ever)
- `governance/` *(new)* — a machine-readable registry of accepted documents and statuses
- `tests/` *(new)* — deterministic test skeletons asserting the grammars
- `fixtures/` *(new)* — **fully synthetic** evaluation data, clearly marked as such
- `scripts/` *(new)* — the public-safety scan, runnable
- One test framework dependency, **if and only if** explicitly approved (see §8 — this is a named fence-crossing, not a default)

## 4. What W2 must not touch

No Wellness Room, Kitchen, Gym, or Meditation Room functionality. No Health Vault implementation or UI. No agents, no agent behaviour, no AIAdapter or VendorAdapter implementation. **No real health data — meaning: none committed to the repo, none in fixtures, none in docs, none in screenshots, none in logs, none in test artefacts.** (Future runtime handling of a user's own local health data is a separate implementation question and is not authorised by W2.) No schema for health content (the registry's document-index format is metadata *about governance documents*, not about health data — the one carve-out, justified in §5.2). No UI of any kind. No medical logic. No notification machinery. No private names, private system references, companion framing, or project lineage. No app feature build: W2's output is the list of what must be proven before features may exist, plus the first proofs.

## 5. Proposed W2 deliverables

**W2-D1 — W1 Phase Closure Record** (`docs/phases/W1-closure.md`). What was accepted, in what order, with commit references; the open-questions inventory from all W1 documents, each triaged as *decided / deferred-with-owner / blocking-for-which-phase*; and the incident log — including the D6 wrong-doorway event, recorded plainly as the process validation it was. A governance system that documents its own near-misses is one that stays honest about its seams.

**W2-D2 — Governance Registry.** Two artifacts: a human-readable index (`docs/governance/registry.md`) and a machine-readable manifest (`governance/registry.json` or `.yaml` — format choice for review, §9). Each entry: document, version, status, acceptance date, what it resolves, what it constrains, and its ID namespaces (D1 edges, D3 transitions, D5 threats). *Justification for the carve-out:* this is the one piece of structured data W2 creates, it describes documents rather than people, and it is the prerequisite for any future CI gate that refuses commits violating governance state. Metadata about governance is C0-adjacent in spirit: useful for enforcement, forbidden from becoming anything else.

**W2-D3 — Decision-Record Enforcement Rules & Repo Governance Checklist** (`docs/governance/checklist.md`). The written rules the repo already lives by, made explicit and bindable: status flips only by the human reviewer, dated; no implementation directories until a phase document authorises them; every PR/commit checked against the public-safety scan; the D5 definition fences carried in (anything contacting a user outside an active session is the notification layer, whatever it's called); new dependencies are fence-crossings requiring named approval; and a two-tier change rule for accepted records — **material or semantic changes require a decision record, never an edit; typo, formatting, link, or other non-semantic corrections require a logged errata note**, so that governance stays rigorous without tiny maintenance fixes becoming theatre. Whether a change is semantic is itself a reviewer judgment: when in doubt, it's material.

**W2-D4 — Synthetic Fixture Strategy** (`docs/governance/fixtures.md` + `fixtures/`). The rules for evaluation data: fully synthetic personas and records; no derivation from any real person's health information; every fixture file marked SYNTHETIC in name and content; fixtures designed to exercise the grammars' hard cases — expired allergies, contradicted medications, unknown-scoped absences, cross-room bait, consent-revocation mid-task. The fixture set is itself reviewable: bad fixtures test nothing.

**W2-D5 — Deterministic Test Skeleton** (`tests/`). Executable assertions, mapped by ID, for: the D1 edge whitelist (every forbidden edge has a test that it cannot be expressed); D2 grant validity (a grant missing any grammar element is rejected; blanket scopes are unconstructable); D3 transitions (no path from agent-extracted to confirmed without a user act; staleness decays, never refreshes); and the D5→D6 mappings (each D5-T## with a deterministic mitigation gets a named test stub, even if initially skipped/pending). Skeleton means: structure, naming, fixtures wired, assertions written where the grammars are already precise — not a complete harness, and nothing behavioural yet (behavioural evals are D6 territory and need decisions about model access that belong to a later phase).

**W2-D6 — Public-Safety Scan, Runnable** (`scripts/`). The scan that has so far been performed by review, scripted. The public repo contains **only generic, public-safe prohibited-pattern lists**: compliance-claim detection ("compliant" outside permitted contexts), real-data heuristics, companion-framing terms, and pattern categories — never actual private names or private lineage terms. The public repo must not preserve the very private terms it is trying to prevent. If a private wordlist is ever needed, it is optional, local, untracked, and `.gitignore`d (e.g., `.public-safety.local.txt`), with the scan treating its absence as normal. And the standing rule: the script *supplements* human review and never replaces it.

## 6. Risks of starting implementation too early (why W2 exists)

1. **Working code becomes authority.** The first running feature outranks the documents in every future argument, inverting the entire W1 order of precedence.
2. **Untested grammars harden into code assumptions.** If E11's per-room edges or D3's suspension semantics turn out to need refinement, finding that out in a test skeleton costs an afternoon; finding it out under a shipped feature costs a migration and a constitutional crisis.
3. **Seam multiplication** (D5 Principle 6). Every feature is a seam. Building features before enforcement machinery means every seam opens unguarded.
4. **Public-safety surface expands faster than scanning capability.** More files, more strings, more chances for a private reference or an overclaim to land — before the scan exists to catch it.
5. **Review fatigue transfers to code review.** The human gate that read every document carefully cannot read every diff carefully; enforcement machinery is what lets the gate scale without rubber-stamping (W0 failure mode 3, now in repo form).
6. **The demo gravity well.** Nothing erodes governance like something demoable. Once a Kitchen exists, "just one more feature" outcompetes "first one more test" in every prioritisation forever. W2 closes before that gravity exists.

## 7. What must be true before W2 can close

1. The W1 closure record is accepted, with every open question triaged and owned.
2. The registry exists in both forms, is accurate, and matches the repo's actual state (a test asserts this).
3. The governance checklist is accepted and has been applied to at least one real commit cycle.
4. Every accepted grammar has **at least one executable assertion** passing against synthetic fixtures — D1 edges, D2 grant validity, D3 transitions at minimum.
5. Every D5 threat with a deterministic mitigation has a named test (passing, or explicitly pending with an owner).
6. The public-safety scan runs clean against the full repo and is part of the checklist.
7. **No user-facing, product, room, agent, adapter, UI, or health-feature implementation directories exist.** Verification directories (`tests/`, `fixtures/`, `scripts/`, `governance/`) are allowed only where W2 explicitly authorises them (§3). W2 closes with the Wing exactly as useful to an end user as it was at W1's close: not at all. That is the success criterion, stated without irony.
8. A W3 scoping question is drafted — *what must be proven behaviourally (D6 Tier-B) before any room may be built, and what does that require?* — but not answered. Each phase ends by defining the next door, not opening it.

## 8. Should W2 include code at all?

**Yes — narrowly, and only of one kind: verification code.** Test assertions, fixture loaders, the registry-consistency check, the safety scan. Nothing that processes health data (there is none — fixtures are synthetic and the code that touches them is the test harness itself), nothing user-facing, nothing agentic.

This requires one honest fence-crossing to name: a test framework means a dependency manifest (the W1-era briefs prohibited `package.json` / dependencies, correctly, for a docs-only phase). W2 proposes to cross that fence **once, explicitly, with human approval, for test tooling only** — minimal framework, pinned versions, no transitive sprawl, choice of stack reviewed before installation (§9). If the reviewers prefer zero dependencies, the fallback is documented-but-stubbed tests in plain scripts — weaker, but the fence stays untouched. The decision is the reviewers', and the alignment report's job is to make it explicit rather than let it arrive inside a Claude Code commit.

## 9. What the human reviewer and architect should review before Claude Code touches the repo

1. **The A–D decision itself** — this report recommends D; that recommendation is reviewable like everything else.
2. **The dependency fence** (§8): test framework yes/no, and if yes, which stack and how pinned.
3. **Registry format**: JSON vs YAML, and the exact field set — small choice, long shadow, since future CI reads it.
4. **The fixture strategy** before any fixture exists: synthetic-only rules, marking conventions, and the hard-case list.
5. **The checklist contents** (W2-D3) — these become the repo's standing law; they deserve the same two-review-one-gate treatment as everything in W1.
6. **Deliverable order** — proposed execution order: D1 closure → D2 registry → D3 checklist → D4 fixtures → D6 scan → D5 tests last (tests assert against everything prior, so everything prior lands first). **Execution order may differ from deliverable numbering: W2-D6 may land before W2-D5 because the public-safety scan should exist before the deterministic test skeleton is committed. The deliverable IDs remain stable.**

---

*This is an alignment report. Nothing in it authorises repo changes. It exists so that when Claude Code receives W2 briefs, every fence in them was decided here, in review, by humans and architects — not improvised at the prompt.*
