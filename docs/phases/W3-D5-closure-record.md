# W3-D5 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations · **Deliverable:** D5 — Local Storage / Residue Rules
**Type:** Closure record / audit seal — mapping-based. Docs-only. Authorises nothing to be built.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway (including its resequencing clause); ADR 0004 (the policy this record accounts for); ADRs 0008, 0009, 0010, 0013; W1-D3; W1-D5 (where the residue risk was first named); the accepted remaining-runway mapping brief as review anchor; the closure-record precedent

---

**D5 was not skipped. Its expected work — the plaintext residue policy implemented and residue-tested — was absorbed into the published D2, D3, and D4 evidence discipline, operation by operation, as each landed. This closure is the accounting record proving that absorption: every clause of ADR 0004 mapped to its published proof, with nothing owed.**

## 1. Closure statement

**W3-D5 — Local storage / residue rules — is complete and closed, as a deliverable satisfied by absorption.** The runway expected the residue policy "implemented and residue-tested: nothing decrypted persists past task end; logs plaintext-free in every build configuration; platform-uncontrollable residue documented honestly." Every element of that expectation exists in the published repository and is proven by standing tests or standing documentation, as the table below accounts clause by clause. This resequencing — the work landing inside D2/D3/D4 rather than as a separate D5 arc — is exercised under the runway's own clause that *"execution order may resequence where dependencies allow; IDs stay stable."* The ID stayed stable; this is its seal.

## 2. The mapping: ADR 0004, clause by clause

| ADR 0004 clause | Published evidence | Proof names | Commits / records | Verdict |
|---|---|---|---|---|
| **1. Default-deny persistence** — no decrypted governed content persists past task end, in any form, anywhere | Residue test classes on every operation that seals or decrypts, covering normal termination, kill termination, refusal paths, and a populated vault at scale | `ResidueDiscipline` (store), `ImportResidue` + `RefusalResidue` (import), `CustodyResidue` (key envelope), `test_profile_plaintext_never_on_disk` (profile path), `VaultAtScale` + `KillAtScale` (30-record vault, all-ciphertext at every checkpoint), and the converted ledger proof `test_D5_T01_plaintext_residue_none_after_task` — carrying D5's own test-id namespace | `d440953` (store), `ddcd3a2` (import), `d646e1b` (custody), `d6c5113` (at scale), `6e14deb` (profile), `8465c53` (converted proof) | **Satisfied and tested** |
| **2. Logs plaintext-free** — all levels, all build configurations, debug included | Satisfied more strongly than written: no logging exists in the engine tree at all — no `print`, no logging import — proven structurally, so the clause cannot be violated by code that cannot exist | `test_engine_emits_nothing_and_logs_nothing` | `d440953`; standing in the suite since the first engine commit | **Satisfied by structure** (honest note 1 below) |
| **3. Forbidden artifact classes** — no content caches, search indexes, thumbnails, surviving temp files, crash-dump content, serialized UI state, analytics | Thumbnails and extraction structurally impossible (the import path cannot parse what it cannot import); temp files excluded by exact-file-set residue sweeps; indexes and search refused by standing deferral; UI state and crash-dump surfaces non-existent by phase; analytics barred by doctrine and by the governance-metadata no-processing-edges rule | `test_core_imports_only_json_and_itself` (structural import cap); the exact-file-set assertions throughout the residue classes; ADR 0009 §5 and the D3 closure's deferred list (index/search); W1-D3 §8a (no processing edges) | `ddcd3a2` (structural cap), `e0019ea` (deferral restated at D3 seal) | **Satisfied — partly by structure, partly by absence** (honest note 2 below) |
| **4. Exceptions are decision records** — no policy-level exceptions | No exception has been taken: the decisions corpus (0000–0014) contains no record granting a persistent derived artifact; no such artifact exists in the repository | The decisions corpus itself; the directory-fence and residue suites that would surface an undeclared artifact | ADRs 0000–0014 as published | **Satisfied — vacuously, stated honestly** |
| **5. Platform-uncontrollable residue documented, not denied** — mitigations where offered, honest residual in ink, no claim of totality | The engine documentation's honest-residuals section (language-level key copies, OS paging, *"tests cannot prove memory absence"*), the runtime-selection record's binding key-handling caveat with its narrowest-scope mitigations, the key-architecture record's threat-register entries, and the non-atomic-write finding | `engine/README.md` §Honest residuals and §Known finding; ADR 0008; ADR 0013 consequences | `d6c5113` (the in-ink documentation), `a6d0e57` (ADR 0008), `d9aa224` (ADR 0013) | **Satisfied — documented in ink** |
| **6. User-initiated copies are rights, not residue** — the policy governs what the Wing leaves behind, never what the user takes | No copy or export surface exists yet, so nothing violates the boundary; export and backup are already named as permitted rights categories, and the clause hands directly to the D6 arc that will build them | ADR 0010 decision 3 (rights categories); ADR 0004 decision 6 itself | `efab8df` (ADR 0009/0010) | **Satisfied by absence; hands off to D6** |

**Contradiction check at closure: none found.** The structural tests named above were verified present in the live tree at the time of this record; the decisions corpus contains no exception; the suite stood at 180 tests, 171 passed, 9 future-phase skips, 0 failures, with the public-safety scan passing over all tracked files.

## 3. Honest notes carried forward

1. **Clause 2's "every build configuration" is currently satisfied by structure in a single-configuration runtime.** There is one build class and no logging machinery; the day logging or build configurations are introduced, the clause becomes a live obligation — and the structural test makes that day a visible diff, not a silent drift.
2. **Clause 3's by-absence protections become live obligations in the surface era.** Serialized UI state, crash-dump content handling, and every render-layer artifact class are currently impossible because no surfaces exist; when the surface era arrives, these protections are **inherited, not forgotten** — this record is their forwarding address.

## 4. Review anchor

This closure's mapping was reviewed and accepted through the W3 remaining-runway mapping pass before drafting. The record above is deliberately self-sufficient: the full clause-by-clause accounting, proof names, and commit anchors are carried here so no reader requires any document outside the repository to understand why D5 closed.

## 5. Forward

The durable-ledger decision remains the next doctrine gate before the D6 brief; this closure does not decide ledger form, persistence, or backup-unit membership. W3-D6 remains the next real build arc for export, backup, restore symmetry, and key-loss wording usage; this closure does not authorise D6 work.

## 6. Gate

W3-D6 and W3-D7 have not started. Nothing in this record pre-authorises any part of either; each arrives through its own brief, rulings, and ceremony, as everything before them did.
