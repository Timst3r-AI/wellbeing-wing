# Wellbeing Wing

A governance-first, privacy-first architecture for personal wellbeing systems.

**Status:** The current published state is a governed, headless reference implementation and evaluation environment. **W0 is accepted; W1 through W7 are complete and closed. W8-D1 and W8-D2 are complete; W8-D3 through W8-D7 remain closed behind their own gates.**

The repository now contains the local Health Vault and Health Profile foundations, enforceable room contracts, runtime governance machinery, a static review surface, synthetic generated-evaluation records with individual human dispositions, and a class-opaque W8 discriminating instrument. **No public model has been contacted at any point.**

There is not yet an end-user application, conversational assistant or hosted sync service, and the Wing does not provide medical, therapeutic, diagnostic or crisis-response functions.

---

> **The user initiates. The wing holds. Nothing is pushed.**

---

## What this is

The Wellbeing Wing is a design and reference implementation for a personal wellbeing environment composed of four governed rooms: the **Wellness Room**, **The Kitchen**, **The Gym**, and the **Meditation Room**.

It is built around one governing idea:

**Personal health context is sensitive evidence that must be governed, not raw material to be mined.**

The project separates evidence, derived context, authority, presentation, runtime processing and evaluation so that one layer cannot silently inherit the powers of another. Where automation exists, it prepares, organises, compares, renders or evaluates under explicit constraints; it does not create authority by itself.

**The Wellbeing Wing is privacy-first by design.** Its architecture has been informed by privacy frameworks including HIPAA, the Australian Privacy Principles and the GDPR, particularly principles such as data minimisation, explicit purpose, bounded access, controlled disclosure and protection of sensitive information. This describes the architectural influences and design intent only; it does not establish that any deployment satisfies a legal or regulatory requirement.

The central data pattern remains:

```text
Health Vault (evidence)
   → Draft Health Profile (derived, no authority)
      → user review, section by section
         → Approved Health Profile (active working context)
```

*The Health Vault is evidence. The Health Profile is derived context. The user decides what becomes active.*

## What this is not

Not a medical device. Not a treatment platform. Not an AI therapist. Not designed to create or sustain an ongoing AI relationship. Not an engagement product built around push notifications, streaks, scores or nudging. Not a health-data marketplace.

The Wing does not diagnose, prescribe treatment, provide crisis response or make clinical decisions. Its privacy, governance and public-safety controls are architectural and technical safeguards, not claims of clinical validation, safety approval or production readiness.

## Build philosophy

**Capability follows governance, not the other way around.** Each phase is designed, reviewed and checked against its governing records before the next capability is allowed to exist.

| Phase | Scope | Status |
|---|---|---|
| **W0** | Constitution — laws, boundaries, risks, open questions | ✅ Accepted (2026-06-12) |
| **W1** | Governance architecture and data-boundary design | ✅ Closed (2026-06-12) |
| **W2** | Governance evaluation and enforcement foundations | ✅ Closed (2026-07-05) |
| **W3** | Health Vault and Health Profile foundations | ✅ Closed (2026-07-06) |
| **W4** | Room Contracts — four rooms as enforceable jurisdictions | ✅ Closed (2026-08-12) |
| **W5** | Runtime enforcement and behavioural evaluation | ✅ Closed (2026-08-17) |
| **W6** | Governed presentation and review surfaces | ✅ Closed (2026-08-17) |
| **W7** | First-contact governance and synthetic model evaluation | ✅ Closed (2026-10-01), with no public model contact |
| **W8** | Generative evaluation maturity | 🟡 In progress — D1 doctrine and D2 discriminating instrument complete; D3–D7 closed |

### What exists now

- A local encrypted Health Vault, import path and key-custody model.
- Draft and approved Health Profile foundations, transition rules, durable ledgering, encrypted backup/restore, and single-record export-as-right.
- Four governed room contracts and their validators and synthetic fixture corpus.
- Runtime enforcement for grants, processing context, freshness, payload equality, transmission/disclosure boundaries and model-access authority.
- A static generated review surface with deterministic traceability.
- A governed synthetic-evaluation architecture and published synthetic evaluation records.
- A human-review disposition layer in which individual generated-evaluation records receive explicit human dispositions without turning model output into authority.
- A W8 evaluation doctrine and a twelve-case, class-opaque discriminating instrument with published integrity commitments and withheld authoring records held outside the repository until a separately gated reveal.
- Deterministic proofs, mutation controls, public-safety scanning and a machine-readable governance registry binding governed records by content hash.

### What does not exist

- No end-user UI or user-facing command-line product.
- No conversational assistant or relationship-oriented AI experience.
- No hosted sync or hosted personal-data service.
- No public model contact, model runtime, provider integration or model-generated public evidence.
- No medical, diagnostic, therapeutic, clinical, crisis-response or safety-intervention capability.
- No W8-D3 review session, calibration, reveal or later contact decision. Those remain separately gated.

## Repository structure

```text
docs/
├── constitution/   # W0 governing constitution
├── decisions/      # ADR-style governing decisions
├── architecture/   # W1 governance architecture
├── governance/     # Human-readable governance material
├── phases/         # Phase runways, briefs, records and closure evidence
├── surface/        # Generated review-surface artefacts
└── wellbeing-wing-concept-overview.md
engine/             # Headless local engine foundations
runtime/            # Governed runtime enforcement machinery
tests/              # Deterministic proof and regression suite
fixtures/           # Synthetic fixtures only
scripts/            # Public-safety and deterministic generation tooling
governance/         # Canonical machine-readable registry and governed artefacts
requirements.txt    # Exact-pinned third-party surface
```

## Reading order

1. [`docs/wellbeing-wing-concept-overview.md`](docs/wellbeing-wing-concept-overview.md) — plain-language overview of what exists and what remains gated
2. [`docs/constitution/W0-wellbeing-wing-constitution.md`](docs/constitution/W0-wellbeing-wing-constitution.md) — governing laws
3. [`docs/phases/README.md`](docs/phases/README.md) — authoritative phase state, runways and closure records
4. [`governance/registry.json`](governance/registry.json) — canonical machine-readable governance registry
5. [`docs/architecture/`](docs/architecture/) — W1 architecture corpus
6. [`docs/decisions/`](docs/decisions/) — decision records

Where this README and a governing record disagree, the governing record wins.

## Public identity and attribution

The current tracked public tree uses functional governance roles rather than private human or persona identities. Future repository commits use the public project identity `Timst3r-AI`. Legitimate public AI collaboration may be attributed where factually true, but attribution never creates governance authority.

Pre-ADR-0056 Git objects remain preserved historical development history rather than being rewritten; the public-identity rule governs the current tree and future publication, not a retroactive erasure claim.

## License and adopters

Licensed under the [Apache License 2.0](LICENSE), with an accompanying [NOTICE](NOTICE). Broad reuse — including commercial and closed-source — is intentional: the pattern is meant to travel. See [ADR 0014](docs/decisions/0014-licence-selection.md) for the reasoning.

Forks and adaptations must not imply endorsement by, or equivalence to, this repository. The governance records here certify only this repository's own process, never a derivative. No medical, therapeutic, diagnostic, safety-intervention, crisis-response, clinical-validity or production-readiness claim is made.
