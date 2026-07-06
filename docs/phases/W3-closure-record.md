# W3 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations
**Type:** Phase closure record / audit seal. Docs-only. Authorises nothing to be built. This record satisfies W3-D7.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway; the six deliverable closure records; ADRs 0004–0015; the W2 closure-record precedent

---

**W3 set out to build the first thing worth governing: a place where a person's evidence is safe, their record is honest, and nothing becomes true about them without their own hands making it so. It closes with exactly that, published: a vault that holds without reading, belongs without escrow, shapes without inventing, moves without self-promoting, remembers without leaking, travels without telling, and gives back without gatekeeping. Every behaviour was doctrine before it was code, and every promise has a standing test.**

## 1. Closure statement

**W3 — Health Vault and Health Profile Foundations — is complete and closed.** W3-D1 through W3-D6 are sealed by their own registered closure records. **W3-D7 is satisfied by this closure record.** W4 has not started.

## 2. The deliverable chain

| Deliverable seal | Commit | What it sealed |
|---|---|---|
| W3-D1 cluster (ADRs 0004–0012) | `4848cb8` | The engine doctrine: residue, encryption, platform, artifacts, runtime selection, import boundary, review posture, backup guidance, key-loss wording |
| W3-D2 closure | `f899611` | The engine spine: store, import, key custody, residue at scale, format seam |
| W3-D3 closure | `e0019ea` | The Health Profile object model: the authority grammar as shapes, sealed profile persistence |
| W3-D4 closure | `1780e5b` | The transition engine: catalogue, runnable matrix, validator, applier with user-act gating |
| W3-D5 closure | `f623958` | Residue rules, closed by mapping-based evidence accounting |
| W3-D6 closure | `4997c3d` | Export, backup, and restore: the WBWB container, restore symmetry, export as a right |

Phase-level and project-level records landed within the phase: **ADR 0013** (key architecture, `d9aa224`); **ADR 0015** (durable-ledger doctrine, `f43255f`) and the **durable-ledger store** (`8b7cfea`); **ADR 0014** (licence selection, `afa913c` — project-level: Apache-2.0, LICENSE and NOTICE at root); the **public concept overview** (`1a0190b` — project-level: the front door).

## 3. Criteria assessment against the runway

| Deliverable | Runway expectation | Disposition |
|---|---|---|
| W3-D1 | Encryption/platform decision cluster, evidence-gated | **Met** — eight records, spike-evidenced runtime selection, sealed 8/8 |
| W3-D2 | Vault store and import foundation | **Met** — four milestones plus ADR 0013; the spine complete and sealed |
| W3-D3 | Health Profile object model: label pairs, provenance references, bounded unknowns, contradiction flags, no UI | **Met** — the grammar as shapes with illegal states unconstructable; sealed persistence; the transition-era structures honestly noted as unpersisted at its seal |
| W3-D4 | Draft → Approved review flow with user-act gating; tests simulate; nothing real becomes Approved | **Met** — catalogue/matrix/validator/applier; user acts constructible only in the test tree within repository enforcement; truth labels computable in memory and unpersistable |
| W3-D5 | Residue policy implemented and residue-tested | **Met by absorption** — the work landed inside D2/D3/D4's evidence discipline; closed by a mapping-based record carrying the clause-by-clause accounting, under the runway's own resequencing clause |
| W3-D6 | Export as a right; encrypted backup with restore symmetry; sentences vetted and catalogued | **Met** — the WBWB portable ciphertext file, empty-target five-step restore, single-record export-as-right; wording catalogued by citation to ADRs 0011/0012 |
| W3-D7 | Closure record: criteria assessment, suite green, pending-ledger updates, incident log, W4/W5 gate | **Met by this record** |

**The W3-owned pending stubs were converted to live proofs before the D4 seal** (`8465c53`) — the transition-enforcement bridge and the create/use/terminate residue proof, names preserved. Everything still pending is future-owned (§5).

## 4. Verification at phase closure

- **Deterministic suite: 218 tests — 209 passed, 9 skipped, 0 failures.**
- **Public-safety scan: PASS with unmasked exit code — zero findings** across all tracked files.
- **Registry: 36 entries before this closure; this record advances it to 37.**
- **Dependencies unchanged: the manifest's three exact pins have not moved since the first line of product code.**
- **The governance/product boundary held through every product landing of the phase** — no product commit ever touched a governance byte; the registry moved only when records moved it.

## 5. The pending ledger at closure

Nine stubs remain, every one future-owned — none is unsealed W3 work: **W5 adapter phase** — `test_D5_T15_T23_payload_equality_at_z3_z4`, `test_D5_T04_granted_and_trusted_never_merge`; **W5 evaluation era** — `test_D5_T05_repetition_resistance_behavioural`, `test_D5_T06_authority_laundering_resistance`, `test_D5_T12_cross_room_isolation_behavioural`, `test_D5_T13_in_room_silent_inference_resistance`; **W6 surface phase** — `test_language_law_grading_both_directions`, `test_D5_T02_no_bulk_approve_path_in_ui`, `test_D5_T24_label_legibility`. Each carries its owner and unblocking condition in the ledger itself; a skipped test is honest, a missing test is invisible.

## 6. Incident log

Recorded per the closure precedent, each with its lesson:

1. **The wrong-workspace scare** — an early session anchored to a non-canonical duplicate; resolved by absolute-path discipline and archiving the duplicate. *Lesson: the canonical path is stated in every landing instruction since.*
2. **The Downloads planning-corpus loss** — much of the review corpus vanished from the drafts folder mid-phase; re-materialised under architect rules (provenance notes removed, headings neutralised). *Lesson: drafts are conveniences; only landed records are real.*
3. **The concept-overview v2 draft loss** — the reviewed draft vanished before landing; rather than reconstruct from memory, a fresh v3 was drafted and re-reviewed. *Lesson: a lost reviewed draft is re-reviewed, never approximated.*
4. **The stale Landing A relay** — an already-consumed instruction was re-sent and refused correctly against live repository state. *Lesson: instructions are verified against the live state before execution; a relay can be stale, the repository cannot.*
5. **The exit-code-masking slip** — a piped exit-code check briefly masked a scan failure during the D6 closure landing; the suite's scan-invocation test failed honestly and forced the correction. *Lesson, as ruled: the verification suite caught what an operator shortcut masked. The battery outranked confidence.*

## 7. Honest findings — the phase roll-up

Carried forward in ink, none softened by closure: **the language-level key-copy residual** (the runtime cannot guarantee zeroing; tests cannot prove memory absence); **per-record cardinality and size leakage** at rest (accepted with reasons; notably *not* exported by the backup container); **weak-passphrase honesty** (the KDF raises attacker cost, it cannot make a weak passphrase strong; strength posture is a surface-era decision); **non-atomic writes** (one-file blast radius, torn-tail honesty, atomic write a possible future decision); **in-memory backup assembly** (fine at current scale, noted for the future); **repository-scoped guards** (the suite guards its own tree and claims nothing beyond what it can enforce).

## 8. The W4/W5 gate

The next era's entry material exists as draft/review material only: **the W4 room-contracts pack, the W5 adapter pack, and the W6 review-surface pack**. This record names them and does nothing more — they are not reviewed, not approved, and not pre-decided here. **W4 must open through its own runway and gate**, through the same ceremony that opened and closed this phase: reviewed records first, capability after.

## 9. Deferred out of W3

Nothing below exists, and nothing below is authorised by this record: the surfaces era (review surfaces, first-run, onboarding, wording cadence, the string catalogue); printed recovery codes; whole-vault plaintext export; profile export; atomic write; a ledger-purpose subkey; import/custody event emissions; scoped erasure; a user-selected KDF profile; contributor process (DCO/CLA); vault layout, record naming, listing, indexing, and search; the first caller; hosted or sync modes; UI and CLI; and — restated one final time so no closure ever softens it — **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind.**
