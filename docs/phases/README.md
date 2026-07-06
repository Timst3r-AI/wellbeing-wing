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

**Status:** **W3 — Health Vault and Health Profile Foundations — is complete and closed** (W3-D1 through W3-D6 sealed, W3-D7 phase closure published, 2026-07-06; see [`W3-closure-record.md`](W3-closure-record.md)). **W4 has not started and must open through its own runway/gate.**

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
| W3-D3 — Profile Object Model, Milestone 2: sealed profile persistence | [`../../engine/core/profile_records.py`](../../engine/core/profile_records.py) | Accepted by human reviewer, 2026-07-06 — Tier J: profile items and bounded unknowns sealed through the store path unchanged; in-payload typing with evidence-by-absence (no record format v2); truth-label persistence refused at the only write path per the minimal-review-posture record; loading reconstructs through the object-model constructors; contradiction/supersession/ledger-event persistence and the transition engine remain deferred to W3-D4 under its own gates |
| W3-D3 — Closure Record | [`W3-D3-closure-record.md`](W3-D3-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals the Health Profile object model — published chain and the seven planning rulings cited, verification state at closure, honest findings carried forward (including the completeness nuance: transition-era shapes exist but do not persist), deferred list preserved; authorises nothing to be built; W3-D4 not started |
| W3-D4 — Transition Engine, Milestone 1: catalogue, matrix, and validator | [`../../engine/core/transitions.py`](../../engine/core/transitions.py) | Accepted by human reviewer, 2026-07-06 — Tier J: all eight W1-D3 transitions catalogued (understanding, never permission); the runnable matrix as a whitelist with refusal by absence; a pure content-free validator classifying runnable/gated/dormant/illegal; T1 catalogued but dormant until grant machinery exists by its own authority; T2/T4/T7/T8 recognised as gated — no application, no user acts, no events, no persistence change; the applier and its structural guards remain W3-D4 M2 under its own gates |
| W3-D4 — Transition Engine, Milestone 2: applier with user-act gating | [`../../engine/core/transitions.py`](../../engine/core/transitions.py) | Accepted by human reviewer, 2026-07-06 — Tier J: per-transition appliers validating through the classifier, in-memory only, emitting exactly one data-only ledger event per application (emitted, never stored — durable ledger deferred to its own decision); user acts as data, constructible only in the test tree within repository enforcement (AST guard landed in the same commit); truth labels computable in memory during gated synthetic tests and still unpersistable; T7 composite implemented (supersede + mint correction, retained history); T8 supersession only, no reactivation; contradiction/supersession persistence remains deferred |
| W3-D4 — Closure Record | [`W3-D4-closure-record.md`](W3-D4-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals the transition engine — published chain (M1, M2, and the pending-ledger cleanup) cited by commit, the planning-brief and in-flight rulings restated, verification state at closure, honest findings carried forward, deferred list preserved; authorises nothing to be built; W3-D5 and later deliverables not started |
| W3-D5 — Closure Record (mapping-based) | [`W3-D5-closure-record.md`](W3-D5-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals residue rules as a deliverable satisfied by absorption — no separate D5 milestones existed; the expected work landed inside the published D2/D3/D4 evidence discipline, and the record carries the full ADR 0004 clause-by-clause mapping with proof names and commit anchors, two honest notes, and the forward gates; authorises nothing to be built |
| W3 — Durable-Ledger Doctrine (D6 gate) | [`0015-durable-ledger.md`](../decisions/0015-durable-ledger.md) | Accepted by human reviewer, 2026-07-06 — Tier J: the durable ledger exists as doctrine — sealed under the master-key custody boundary, independently sealed append frames, doctrine-wide event scope with v1 limited to existing transition events, backup-unit membership as sealed ciphertext, erasure as the user's knowing act only; the implementation milestone remains unstarted, and D6 remains gated until its sequencing is authorised; authorises no implementation |
| W3 — Durable-Ledger Store (implementation milestone) | [`../../engine/core/ledger_store.py`](../../engine/core/ledger_store.py) | Accepted by human reviewer, 2026-07-06 — Tier J: ADR 0015 as code — the WBWL versioned ledger file of independently sealed append frames under the master key; append order preserved and proven bytewise append-only; torn tail refused with intact history preserved (one-event blast radius); whole-ledger erasure as an explicit act; the appliers untouched (the writer is caller-side); import/custody emission remains a named future extension; backup/export mechanics remain D6 |
| W3-D6 — Milestone 1: backup export and restore symmetry | [`../../engine/core/backup.py`](../../engine/core/backup.py) | Accepted by human reviewer, 2026-07-06 — Tier J: the WBWB portable ciphertext file — public header, reachable key envelope, sealed payload holding manifest, records, and ledger with no structure visible outside it; restore is file-plus-passphrase into an empty target only, five-step validation before any write, no record plaintext decrypted to restore; member sets caller-supplied (the engine never discovers files); single-record export (M2) and the D6 closure (M3) remain under their own gates |
| W3-D6 — Milestone 2: export as a right | [`../../engine/core/export.py`](../../engine/core/export.py) | Accepted by human reviewer, 2026-07-06 — Tier J: single-record plaintext export at the data layer — the imported bytes leave byte-identical under no gate but the owner's act; provenance always returned as structured data, written as a sidecar only when explicitly requested; destinations validated before any write, existing destinations refuse, profile-class records refuse (their export deferred to its own governed path); no batch, no whole-vault plaintext export (own future record), no UserAct or review machinery; the D6 closure (M3) remains under its own gate |
| W3-D6 — Closure Record | [`W3-D6-closure-record.md`](W3-D6-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals export/backup/restore — published chain cited by commit; the seven planning rulings (headlined by the WBWB circularity correction) and two M2 rulings restated; consumed ADR 0015 inputs named; the WBWB container shape, five-step restore validation order, and export-right contract carried in ink; honest findings and deferred list preserved; authorises nothing to be built; W3-D7 not started |
| W3-D7 — W3 Closure Record | [`W3-closure-record.md`](W3-closure-record.md) | Accepted by human reviewer, 2026-07-06 — Tier J: seals the phase — the six deliverable seals cited by commit, criteria assessed against the runway, verification state, the nine future-owned pending stubs named, the incident log (five entries with lessons), the honest-findings roll-up, the W4/W5 gate naming next-era draft material without pre-deciding it, and the deferred list; authorises nothing to be built; W4 not started |

## W4 and beyond

Defined as W3 progresses. Rooms, adapters, and surfaces are designed only after the spine they must obey exists — and only through their own gates.
