# Wellbeing Wing

A modular, AI-assisted personal wellbeing environment built governance-first.

**Status:** Phase W2 — Governance Evaluation & Enforcement Foundations (runway accepted). W0 and W1 closed. No code exists yet, deliberately.

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
| **W2** | Governance evaluation & enforcement foundations — making the governance testable, nothing user-facing | Runway accepted; deliverables in progress |
| W3+ | Defined at the close of W2 | — |

## Repository structure

```
docs/
├── constitution/   # The W0 Constitution — the governing document for all phases
├── decisions/      # Design decision records (ADR-style), one decision per file
├── architecture/   # W1 governance-architecture deliverables (data boundary map, consent, authority, threat model, evaluation plan)
├── governance/     # Governance registry (human-readable index) and repo governance docs
└── phases/         # Phase index, phase runways, and closure records
governance/         # Machine-readable governance registry (registry.json — canonical)
```

## Reading order

1. [`docs/constitution/W0-wellbeing-wing-constitution.md`](docs/constitution/W0-wellbeing-wing-constitution.md) — start here; everything else is downstream of it
2. [`docs/phases/README.md`](docs/phases/README.md) — phase plan, runways, and closure records
3. [`docs/architecture/`](docs/architecture/) — the W1 governance corpus (data boundary map, consent, authority, threat model, evaluation plan)
4. [`docs/decisions/`](docs/decisions/) — decision records as they accumulate

## License

Not yet selected — to be decided before the repository accepts external contributions. (Tracked as a setup task, not a constitutional question.)
