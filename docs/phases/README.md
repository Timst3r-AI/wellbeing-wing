# Phases

**Build philosophy: capability follows governance, not the other way around.**

A phase is closed when its deliverables are complete, reviewed, and checked against the Constitution. No phase begins before the prior phase closes.

## W0 — Constitution

**Scope:** The governing document — purpose, non-goals, core laws, room boundaries, the Health Vault pattern, privacy-by-design principles, agent boundaries, risks and failure modes, open questions.

**Deliverable:** [`../constitution/W0-wellbeing-wing-constitution.md`](../constitution/W0-wellbeing-wing-constitution.md)

**Status:** Accepted by human reviewer, 2026-06-12 (v0.1.1, W0.1 cleanup pass applied) — the binding governance document for all subsequent phases.

**Closes when:** the Constitution is approved as the binding governance document for all subsequent phases.

## W1 — Governance Architecture and Data Boundary Design

**Scope:** Still no UI and no production code. Per Constitution §13, W1 delivers:

1. **Data boundary map** — every data category, its sensitivity class, its home (Vault / Profile / room records / audit), and every permitted flow, with Laws 4, 8, and 9 expressed as explicit edges that do or do not exist.
2. **Consent and scope model** — the grant object (who, what, why, how long), revocation behaviour, and resolution of Open Question 2 (revocation cascade).
3. **Authority and staleness model** — authority labels, last-reviewed timestamps, re-review triggers, and supersession (Laws 3 and 7), defined before any schema exists.
4. **Safety surfacing decision document** — resolution of Open Question 1 (Law 12 mechanics) as its own reviewed decision record.
5. **Threat model** — Vault-centred security analysis and the local-first vs hosted decision (Open Question 6), which should be decided **first**, since every other W1 deliverable inherits from it. *Keystone resolved: [ADR 0001](../decisions/0001-local-first-user-held-keys.md) (Accepted) settles the local-first vs hosted decision via user-held keys; remaining W1 deliverables inherit from it.*
6. **Evaluation plan skeleton** — which constitutional laws map to deterministic tests vs behavioural evaluation (Open Question 12).

**Status:** Closed — all six deliverables accepted by human reviewer, 2026-06-12 (D1–D3, D5, D6 in [`../architecture/`](../architecture/); D4 landed as [ADR 0002](../decisions/0002-safety-surfacing.md); ADR 0001 resolved the keystone). Closure criteria per W1-D6 §8.

## W2 — Governance Evaluation & Enforcement Foundations

**Scope:** Translate the W1 corpus into enforceable scaffolding and evaluation readiness — verification only, nothing user-facing. The only code W2 may contain is code that checks rules.

**Runway:** [`W2-alignment-report.md`](W2-alignment-report.md)

**Status:** Closed — all deliverables landed and published; sealed by [`W2-closure-record.md`](W2-closure-record.md), accepted by human reviewer, 2026-07-05.

**Deliverables:**

| Deliverable | Document | Status |
|---|---|---|
| W2-D1 — W1 Closure Record | [`W2-D1-w1-closure-record.md`](W2-D1-w1-closure-record.md) | Accepted by human reviewer, 2026-06-13 |
| W2-D2 — Governance Registry | [`W2-D2-governance-registry-brief.md`](W2-D2-governance-registry-brief.md) · registry at [`../governance/registry.md`](../governance/registry.md) | Accepted by human reviewer, 2026-07-05 |
| W2-D3 — Phase Entry Checklist | [`../governance/checklist.md`](../governance/checklist.md) | Accepted by human reviewer, 2026-07-05 |
| W2-D4 — Synthetic Fixture Strategy | [`../governance/fixtures.md`](../governance/fixtures.md) · seed set in [`../../fixtures/`](../../fixtures/) | Stages A and B accepted by human reviewer, 2026-07-05 (Stage B landed after the W2-D6 landing-mode scan) |
| W2-D6 — Public-Safety Scan | [`../../scripts/README.md`](../../scripts/README.md) (tooling; executes before W2-D5, IDs stable) | Accepted by human reviewer, 2026-07-05 |
| W2-D5 — Deterministic Test Skeleton | [`../../tests/README.md`](../../tests/README.md) (tooling; three tiers + skip ledger) | Accepted by human reviewer, 2026-07-05 |
| W2 Closure Record | [`W2-closure-record.md`](W2-closure-record.md) | Accepted by human reviewer, 2026-07-05 |

## W3 — Health Vault and Health Profile Foundations

**Scope:** The first product-spine phase: the Health Vault as evidence layer, the Draft Health Profile as derived review layer, the Approved Health Profile as working context — built on the no-AI authority path, with user review before anything becomes active. No adapters, no models, no clinical logic, no notifications, no hosted anything.

**Runway:** [`W3-runway-health-vault-profile-foundations.md`](W3-runway-health-vault-profile-foundations.md)

**Status:** Entry gate complete — W2 closure accepted and published ✔, W3 runway accepted and published ✔, first W3 deliverable accepted ✔ (W3-D1, 2026-07-05). The W3-D1 cluster is complete (8/8 records, 2026-07-05). **W3-D2 — the engine spine — is complete and closed** (ADR 0013 plus four milestones, sealed by [`W3-D2-closure-record.md`](W3-D2-closure-record.md), 2026-07-06). W3-D3 has not started; later deliverables and any new fence-crossings remain separately authorised.

**Deliverables:**

| Deliverable | Documents | Status |
|---|---|---|
| W3-D1 — Plaintext Residue and Vault Encryption Doctrine (pair) | [`0004-plaintext-residue-policy.md`](../decisions/0004-plaintext-residue-policy.md) · [`0005-vault-encryption-stack-doctrine.md`](../decisions/0005-vault-encryption-stack-doctrine.md) | Accepted by human reviewer, 2026-07-05 — one atomic landing; neither record authorises implementation on its own |
| W3-D1 — Platform Stack Doctrine and Development-Artifact Policy (pair, Landing A) | [`0006-runtime-platform-stack-doctrine.md`](../decisions/0006-runtime-platform-stack-doctrine.md) · [`0007-development-artifact-policy.md`](../decisions/0007-development-artifact-policy.md) | Accepted by human reviewer, 2026-07-05 — one atomic landing; the evaluation spike becomes runnable only after publication, outside the repo, under the landed rules |
| W3-D1 — Runtime Stack Final Selection | [`0008-runtime-stack-final-selection.md`](../decisions/0008-runtime-stack-final-selection.md) | Accepted by human reviewer, 2026-07-05 — engine-spine selection on first-pass evidence (local-process class); the first binding installation remains a future, separately authorised fence-crossing |
| W3-D1 — Import Boundary and Minimal Review Posture (pair, Landing B) | [`0009-import-file-boundary.md`](../decisions/0009-import-file-boundary.md) · [`0010-minimal-review-posture.md`](../decisions/0010-minimal-review-posture.md) | Accepted by human reviewer, 2026-07-05 — one atomic landing; the engine brief consumes the pair together; neither record authorises implementation on its own |
| W3-D1 — Backup Guidance and Key-Loss Wording (trust-sentences pair, Landing C) | [`0011-local-backup-guidance.md`](../decisions/0011-local-backup-guidance.md) · [`0012-key-loss-onboarding-wording.md`](../decisions/0012-key-loss-onboarding-wording.md) | Accepted by human reviewer, 2026-07-05 — one atomic landing; consequence and remedy in one breath; completes the W3-D1 cluster (8/8); neither record authorises implementation on its own |
| W3-D2 — Engine Milestone 1: store skeleton (first product landing) | [`../../engine/`](../../engine/) · [`../../requirements.txt`](../../requirements.txt) | Accepted by human reviewer, 2026-07-05 — Tier F: one product directory, one exact-pinned dependency set, self-testing fence amendment; test-supplied keys only; import, derivation, custody, and export deferred to their milestones |
| W3-D2 — Engine Milestone 2: import path | [`../../engine/`](../../engine/) · [`0009-import-file-boundary.md`](../decisions/0009-import-file-boundary.md) | Accepted by human reviewer, 2026-07-05 — Tier J: intake operation per ADR 0009 (bytes plus user-supplied provenance in, one sealed record out; type verification capped at magic-number/shape depth; provisional 25 MB operational cap, not doctrine); interpretation of every kind, vault layout/naming/indexing, envelope finalisation, key custody, and export remain deferred to their own decisions |
| W3-D2 — KDF, Custody, and Envelope Selection | [`0013-kdf-custody-envelope-selection.md`](../decisions/0013-kdf-custody-envelope-selection.md) | Accepted by human reviewer, 2026-07-05 — closes ADR 0005's two named opens: moderate KDF profile (evidence-based, micro-spike, review-dated provisional), passphrase-alone custody with no recovery path in any form, two-layer wrap architecture, per-record envelopes; the implementing milestone remains separately authorised |
| W3-D2 — Engine Milestone 3: key custody | [`../../engine/`](../../engine/) · [`0013-kdf-custody-envelope-selection.md`](../decisions/0013-kdf-custody-envelope-selection.md) | Accepted by human reviewer, 2026-07-06 — Tier J: ADR 0013 as code — versioned key envelope (own file, caller-chosen path), two-layer wrap, moderate-profile derivation, passphrase change re-sealing the envelope only; no keyfile, no recovery path in any form; first-run wording, strength posture, vault layout, and backup/export mechanics remain deferred |
| W3-D2 — Engine Milestone 4 (Landing 1): residue at scale and format seam | [`../../tests/`](../../tests/) · [`../../engine/README.md`](../../engine/README.md) | Accepted by human reviewer, 2026-07-06 — Tier J: synthetic vault at scale (all-ciphertext property proven at every checkpoint, including after a killed process), cross-format refusal matrices, and the engine's in-ink documentation (honest residuals, threat-register entries, non-atomic-write finding); atomic write remains a possible future decision; D2 closure follows as its own landing |
| W3-D2 — Closure Record (Landing 2) | [`W3-D2-closure-record.md`](W3-D2-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals the engine spine — published chain cited by commit, verification state at closure, honest findings carried forward, deferred list preserved; authorises nothing to be built; W3-D3 not started |
| W3-D3 — Profile Object Model, Milestone 1: the grammar as shapes | [`../../engine/core/profile.py`](../../engine/core/profile.py) | Accepted by human reviewer, 2026-07-06 — Tier J: W1-D3's authority/staleness grammar as pure data structures — inseparable label pairs, bounded unknowns, contradiction and supersession shapes, the Approved layer as shape only (no instance path exists), ledger event shapes, staleness as a pure function over injected intervals (no clinical defaults); no persistence, no transitions, no review path — those remain W3-D3 M2 and W3-D4 matters under their own gates |

## W4 and beyond

Defined as W3 progresses. Rooms, adapters, and surfaces are designed only after the spine they must obey exists — and only through their own gates.
