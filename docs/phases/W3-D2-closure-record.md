# W3-D2 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations · **Deliverable:** D2 — Engine Spine (store and import foundation)
**Type:** Closure record / audit seal. Docs-only. Authorises nothing to be built.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway; the W3-D1 doctrine cluster (ADRs 0004–0012); ADR 0013; the W2 closure-record precedent

---

**W3-D2 built the first thing the doctrine was written for: an encrypted store that forgets nothing it holds and remembers nothing it shouldn't, an import path that refuses to understand what it carries, and a custody layer that makes the vault belong to exactly one person. Every behaviour was decided in a reviewed record before it was code, and every promise now has a standing test.**

## 1. Closure statement

**W3-D2 — the engine spine — is complete and closed.** The store exists. The import path exists. Key custody and the sealed key envelope exist. The residue-at-scale proof exists. The format-seam confirmation exists. The engine's own documentation exists, carrying its honest residuals in ink. Nothing in the deliverable is half-built, paused, or silently deferred: what was built is listed below with its publication commit, and what was not built is named in §5 with the decision venue it waits for.

## 2. The published chain

| Landing | Commit | What it published |
|---|---|---|
| ADR 0013 — KDF, custody, and envelope selection | `d9aa22400745d498962435c10391bf2bdd32485f` | The v1 key architecture: moderate KDF profile (evidence-based, review-dated provisional), passphrase-alone custody, two-layer wrap, per-record envelopes, envelope-travels-with-backups reasoning |
| M1 — store skeleton | `d44095392ff2b3423d3553cb6126281406826217` | The engine package and ports architecture; seal/unseal under a caller-supplied key; the 16-byte versioned header; the residue and posture test classes; the exact-pinned dependency set and the self-testing fence |
| M2 — import path | `ddcd3a2ffb0ee8d3d0ba0e7c8c68e65cf8d0ce23` | Bytes plus verbatim user provenance in, one sealed record out; type verification capped at magic-number/shape depth; refusal writes nothing; the structural no-interpretation cap |
| M3 — key custody | `d646e1b6e2605f03e2472aa70f62c4c53ce82f7c` | The versioned key envelope; create/unlock/change-passphrase; records proven byte-identical across custody events; derivation through the single crypto port |
| M4 (Landing 1) — residue at scale and format seam | `d6c51134b178b79c635f33f663a6e8bbb5b3bf9f` | The 30-record synthetic vault with the all-ciphertext property proven at every checkpoint, including after a killed process; the cross-format refusal matrices; the engine's in-ink documentation |

This record is the deliverable's final landing (Landing 2), sealing the chain above.

## 3. Verification at closure

- **Deterministic suite: 105 tests — 94 passed, 11 standing skips (the named Tier 3 ledger), 0 failures** at the time of closure.
- **Public-safety scan: pass, zero findings**, normal mode over all tracked files, at the time of closure.
- **Registry: 29 entries before this closure; this record's entry advances it to 30.** No product landing in the chain above touched the registry — the governance/product boundary held through five consecutive landings.
- **Dependency manifest: unchanged through the entire deliverable** — the three pins authorised at M1 remain the engine's whole third-party surface.
- The directory fence, posture assertions, structural no-interpretation cap, and no-emission checks stand as permanent suite members; every future landing inherits them.

## 4. Honest findings carried forward

Named here so closure cannot bury them:

1. **Language-level key-copy residual** — the runtime cannot guarantee key zeroing; copies persist until collection and may be paged. Acknowledged in the runtime-selection record, mitigated by narrowest-scope handling, documented in the engine's own documentation. Tests cannot prove memory absence, and no claim otherwise exists anywhere in this repository.
2. **Per-record cardinality and approximate-size leakage** — record count and rough sizes are observable on disk without any key. Accepted with reasons in ADR 0013, carried in the threat-register entries of the engine documentation, never euphemised.
3. **Weak-passphrase honesty** — the memory-hard KDF raises attacker cost but cannot make a weak passphrase strong. Strength posture (floor, wording) is deferred to the future first-run/surface decisions, bound by the key-loss wording record.
4. **Non-atomic write behaviour** — a process killed mid-write can leave one truncated record, which refuses cleanly with a one-record blast radius and no plaintext residue (proven by test). An atomic-write change would alter file-write and residue behaviour and remains **a future decision, not a silent fix**.

## 5. Deferred at closure

Nothing below exists, and nothing below is authorised by this record. Each waits for its own reviewed decision or milestone: the W3-D3 profile model; UI of any kind; CLI; first-run flow; passphrase strength floor or meter; user-selected KDF profile; keyfile custody; "both" custody; recovery service, escrow, secret questions, cloud recovery, or any hidden recovery path (these are foreclosed permanently, not deferred — listed here so the closure restates it); backup/export mechanics; sync; hosted mode; review surface; profile layer; room behaviour; model contact; vault layout; record naming; listing; indexing; search; the atomic-write decision; the licence decision; the concept-overview landing.

## 6. Gate

W3-D3 (profile model) has **not** started. Its entry gate is this closure plus its own runway-governed brief and reviewed decisions; nothing in this record pre-authorises any part of it. The engine spine stands ready as the foundation the profile work will consume — through the same ceremony that built it.
