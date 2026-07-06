# W3-D3 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations · **Deliverable:** D3 — Health Profile Object Model
**Type:** Closure record / audit seal. Docs-only. Authorises nothing to be built.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway; W1-D3 (the authority and staleness model this deliverable implements); ADRs 0004, 0005, 0009, 0010, 0013; the accepted W3-D3 planning brief and its reviewer rulings; the closure-record precedent

---

**D3 gave the authority grammar hands that can hold everything and sign nothing. The shapes exist, the shapes persist, and every illegal state — an unlabelled item, an unbounded unknown, an agent-minted truth — refuses to be built at all, in memory and on the way back off disk alike.**

## 1. Closure statement

**W3-D3 — the Health Profile object model — is complete and closed, as the object-model deliverable it was scoped to be.** The grammar's shapes exist: profile items with their inseparable authority and staleness label pairs; provenance references; bounded unknowns; contradiction structures; supersession structures; the Approved layer as shape only; staleness as a pure computation over injected intervals. Sealed persistence exists for `ProfileItem` and `BoundedUnknown`, through the store path unchanged, with in-payload typing — no record-format v2, no new store class.

**The completeness nuance, stated so this seal cannot blur it:** contradiction, supersession, and ledger-event structures exist as shapes and are exercised in memory under test, but **they do not persist in D3** — their persistence is deferred to W3-D4 or later, arriving when transitions create them. D3 is complete as the object model; it is not, and never claimed to be, a transition engine.

## 2. The published chain and its decision anchor

| Landing | Commit | What it published |
|---|---|---|
| M1 — the grammar as shapes | `58eacd861c3ec1e29300ad37191f4779522a2432` | `engine/core/profile.py`: label vocabulary verbatim from the accepted grammar (transcription-alignment tested); illegal states unconstructable; Approved layer as shape; ledger event shapes; pure staleness computation |
| M2 — sealed profile persistence | `6e14deb239d27d641e2727b2f7155f3b901e1385` | `engine/core/profile_records.py`: profile items and bounded unknowns sealed through the unchanged store path; in-payload typing; truth-label persistence refused at the only write path; loading reconstructed through the object-model constructors |

D3 ran on its accepted planning brief plus reviewer rulings rather than a separate decision record; the rulings are therefore cited here so this seal is self-anchoring:

1. **In-payload typing** for record-class discrimination; no record-format v2; no change to the inner record encoding; no separate store-file class.
2. **Staleness is a pure function in D3**; transition events that act on it belong to D4.
3. **Intervals are injected parameters with no defaults** — clinical judgment is never encoded as a constant.
4. **The Approved-layer shape is defined** (the grammar is incomplete without it); no Approved instance may exist in any non-test store, per the minimal-review-posture record.
5. **Ledger event shapes are data-only in D3**; durable ledger storage is deferred to D4.
6. **The skip ledger remains unchanged** unless separately authorised.
7. **D4 gets its own brief** after D3's milestones land; the deliverables are never combined.

## 3. Verification at closure

- **Deterministic suite: 139 tests — 128 passed, 11 standing skips (the named pending ledger, unchanged), 0 failures** at the time of closure.
- **Public-safety scan: pass, zero findings**, normal mode over all tracked files, at the time of closure.
- **Registry: unchanged through both milestones — 31 entries before this closure; this record's entry advances it to 32.** The governance/product boundary held again.
- **Dependency manifest: unchanged.** The three pins remain the engine's whole third-party surface.
- **No truth-label item persists anywhere:** the only profile write path refuses confirmed items, tested against both truth labels, write-free and content-free.
- **The `Approved` literal is confined to `engine/core/profile.py`**, its designated shape home, and **`ApprovedProfile` is not re-exported** — both mechanically verified.

## 4. Honest findings carried forward

1. **Evidence-by-absence** is the accepted v1 distinguishability rule: profile records self-declare their class inside the record's provenance JSON; imported evidence records remain exactly as published and declare nothing. Documented in the engine's own documentation; a future record class would force the deliberately-deferred format-evolution decision.
2. **Truth-label persistence is refused until a real review path exists** — confirmed shapes live in memory and tests only, and the refusal is enforced at the only write path, not merely asserted.
3. **The Approved shape exists only in `engine/core/profile.py`** and is not re-exported — the posture refinement ratified at M1.
4. **Profile persistence uses in-payload typing, not record-format evolution.**
5. **Staleness interval defaults remain absent by design** — the clinical question stays genuinely open for its own future reviewed decision.
6. **Contradiction, supersession, and ledger-event persistence is deferred** to the deliverable whose transitions create them.

## 5. Deferred at closure

Nothing below exists, and nothing below is authorised by this record; each waits for its own reviewed decision or deliverable: the W3-D4 transition engine; durable ledger storage; any review path; any approval path; extraction; model contact; UI; CLI; search, index, or layout; room behaviour; backup/export mechanics; staleness interval defaults; any key/custody change; contradiction persistence; supersession persistence; ledger-event persistence; Approved persistence; record-format v2; any new store class; skip-ledger cleanup (evidence noted at M1 stands; the pass remains separately authorisable); clinical examples and real data (prohibited always, listed so the closure restates it).

## 6. Gate

W3-D4 (the transition engine) has **not** started, and no transition-engine work of any kind has begun. Its entry gate is this closure plus its own planning brief and reviewed decisions — walked with full ceremony, because D4 is where the minimal-review-posture record's fences are the ground itself. Nothing in this record pre-authorises any part of it.
