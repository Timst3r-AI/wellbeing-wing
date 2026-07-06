# Wellbeing Wing

A modular, AI-assisted personal wellbeing environment built governance-first.

**Status:** The current published state is a governed, headless engine foundation. W3 — Health Vault and Health Profile Foundations — is complete and closed as of 2026-07-06: the vault store, import path, key custody, health profile object model, transition engine, residue evidence accounting, durable ledger store, encrypted backup/restore, and single-record export-as-right are all published and sealed. There is still no user interface, command-line tool, hosted sync, assistant, medical/therapeutic/diagnostic/crisis function, or companion product. W4 has not started and must open through its own runway/gate.

---

> **The user initiates. The wing holds. Nothing is pushed.**

---

## What this is

The Wellbeing Wing is a design and reference implementation project for a personal wellbeing environment composed of four rooms — the **Wellness Room**, **The Kitchen**, **The Gym**, and the **Meditation Room** — built on one governing idea:

**Personal health context is sensitive evidence that must be governed, not raw material to be mined.**

AI agents in the Wing prepare, organise, summarise, compare, and surface. They do not decide, diagnose, advise treatment, or act on the user's behalf without explicit confirmation. The central data pattern:

```
Health Vault (evidence)
   → Draft Health Profile (agent-extracted, no authority)
      → user review, section by section
         → Approved Health Profile (active working context)
```

*The Health Vault is evidence. The Health Profile is derived context. The user decides what becomes active.*

## What this is not

Not a medical device. Not a treatment platform. Not an AI therapist. Not an engagement product — no push notifications, streaks, scores, or nudging. Not a health-data marketplace. It does not claim HIPAA, APP, GDPR, or any other legal compliance; it is designed to privacy-by-design principles **aligned with** those frameworks, adopting the strictest common denominator. See the Constitution, §2 and §9.

## Build philosophy

**Capability follows governance, not the other way around.** Each phase is designed, reviewed, and constitutionally checked before the next begins. No schema, agent, or UI is built before the governance layer it must obey exists in writing.

| Phase | Scope | Status |
|---|---|---|
| **W0** | Constitution — laws, boundaries, risks, open questions | ✅ Accepted (2026-06-12) |
| **W1** | Governance architecture and data boundary design | ✅ Closed — all deliverables accepted (2026-06-12) |
| **W2** | Governance evaluation & enforcement foundations — making the governance testable, nothing user-facing | ✅ Closed (2026-07-05) |
| **W3** | Health Vault and Health Profile foundations | ✅ Closed (2026-07-06) — Health Vault and Health Profile Foundations complete and sealed. |
| W4+ | Rooms, adapters, and surfaces — each through its own gate | Next phase — gated; not started. |

## Repository structure

```
docs/
├── constitution/   # The W0 Constitution — the governing document for all phases
├── decisions/      # Design decision records (ADR-style), one decision per file
├── architecture/   # W1 governance-architecture deliverables (data boundary map, consent, authority, threat model, evaluation plan)
├── governance/     # Governance registry (human-readable index) and repo governance docs
├── phases/         # Phase index, phase runways, and closure records
└── wellbeing-wing-concept-overview.md   # Plain-language overview: what exists, what deliberately doesn't yet
engine/             # The engine spine (headless): encrypted store, import path, key custody — see engine/README.md
tests/              # Deterministic test suite: repo-state checks and engine tests
fixtures/           # Synthetic fixtures only — no real data, ever
scripts/            # Public-safety scan and its allowlist
governance/         # Machine-readable governance registry (registry.json — canonical)
requirements.txt    # The engine's entire third-party surface, exact-pinned
```

## Reading order

1. [`docs/wellbeing-wing-concept-overview.md`](docs/wellbeing-wing-concept-overview.md) — a plain-language overview: what exists, what deliberately doesn't yet
2. [`docs/constitution/W0-wellbeing-wing-constitution.md`](docs/constitution/W0-wellbeing-wing-constitution.md) — the governing laws; everything else is downstream of it
3. [`docs/phases/README.md`](docs/phases/README.md) — phase plan, runways, and closure records
4. [`docs/architecture/`](docs/architecture/) — the W1 governance corpus (data boundary map, consent, authority, threat model, evaluation plan)
5. [`docs/decisions/`](docs/decisions/) — decision records as they accumulate

## License and adopters

Licensed under the [Apache License 2.0](LICENSE), with an accompanying [NOTICE](NOTICE). Broad reuse — including commercial and closed-source — is intentional: the pattern is meant to travel. See [ADR 0014](docs/decisions/0014-licence-selection.md) for the reasoning.

Forks and adaptations must not imply endorsement by, or equivalence to, this repository. The governance records here certify only this repository's own process, never a derivative. No medical, therapeutic, diagnostic, safety-intervention, or crisis-response claim is made.
