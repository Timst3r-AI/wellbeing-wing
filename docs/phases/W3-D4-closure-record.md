# W3-D4 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations · **Deliverable:** D4 — Transition Engine
**Type:** Closure record / audit seal. Docs-only. Authorises nothing to be built.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway; W1-D3 (the transition grammar this deliverable enforces); ADR 0010 (the minimal review posture this deliverable was built inside); ADRs 0004, 0005, 0009, 0013; the accepted W3-D4 planning brief and its reviewer rulings; the closure-record precedent

---

**D4 built the engine that moves items between states — and built it unable to move anything toward truth without a lawful user act. Three transitions run alone and only ever lower; four wait for acts that nothing in the application tree can construct; one sleeps until a grant exists by its own future authority. The deliverable's own pending proofs were converted to running tests before this seal.**

## 1. Closure statement

**W3-D4 — the transition engine — is complete and closed as a deliverable.** The transition catalogue, runnable matrix, and pure validator exist. The per-transition applier with user-act gating exists. Every successful application emits exactly one data-only ledger event. The structural guards exist and landed in the same commit as the instrument they guard. Nothing in the deliverable is half-built or silently deferred: what was built is cited below by commit, and what was not built is named in §5 with the decision venue it waits for.

## 2. The published chain and its decision anchor

| Landing | Commit | What it published |
|---|---|---|
| M1 — catalogue, matrix, validator | `0118742c07782985c5e71edcbb97e19f286d8273` | All eight W1-D3 transitions catalogued (understanding, never permission); the runnable matrix as a whitelist with refusal by absence, proven by exhaustive enumeration; a pure content-free validator classifying runnable/gated/dormant/illegal |
| M2 — applier with user-act gating | `5a3b7e811a6c8349a65aa817b296ee1eaaba12c4` | Per-transition appliers validating through the classifier, in-memory only, mutating nothing, emitting exactly one ledger event per application; user acts as data, constructible only in the test tree within repository enforcement; the AST guards landed in the same commit |
| Pending-ledger cleanup | `8465c538a76f628c86f097eea3942b993147a548` | Both W3-owned pending stubs converted in place to live proofs — the paper-to-engine bridging test and the create/use/terminate residue proof — names preserved, before this closure |

D4 ran on its accepted planning brief plus reviewer rulings rather than a separate decision record; the rulings are restated compactly so this seal is self-anchoring: **milestones M1/M2/M3 as landed, durable ledger never folded in; `UserAct` owned by the transition module, not re-exported, application-tree construction mechanically forbidden, all claims repository-scoped; durable ledger deferred to a separate decision record; skip-ledger cleanup by its own separately-authorised pass (executed as such); contradiction/supersession persistence deferred; D4 closes standalone.** In-flight rulings, equally binding: **the T7 relabelling-row split** (M1 matrix carried the relabelling row only; M2 implemented the composite's correction-entry side); **the data-only validator** (classification never raises; the applier's bridge does); **T5 as one adjacent step per application** with multi-step decay by repetition; **the T5 clockless elapsed-marker convention** (time-automatic events record the elapsed measure they were computed from — the core has no clock and invented none); **T8 as supersession only**.

## 3. Verification at closure

- **Deterministic suite: 180 tests — 171 passed, 9 pending-ledger skips (all owned by future phases), 0 failures** at the time of closure — including the exhaustive matrix sweep, the six named anti-grammar tests, the `UserAct` structural guards, and the converted live proofs.
- **Public-safety scan: pass, zero findings**, normal mode over all tracked files, at the time of closure.
- **Registry: 32 entries before this closure; this record's entry advances it to 33.** No D4 landing touched the registry — the governance/product boundary held through the whole deliverable.
- **Dependency manifest: unchanged.** The three pins remain the engine's whole third-party surface.
- **The truth-label persistence refusal was cross-checked live:** an applier-produced confirmed item, handed to the profile write path, refuses — write-free and content-free.

## 4. Honest findings carried forward

1. **The `UserAct` guarantees are repository-scoped.** The suite walks the application tree's syntax and fails on any construction site; no production factory exists; the shape is not re-exported. The project guards its own tree and claims nothing beyond what its suite can enforce.
2. **Ledger events are emitted, not durably stored.** Every application's event is produced and provable; durable ledger storage waits for its own decision record, and until then the record of governance is honest about being in-memory.
3. **Truth labels are computable in memory and not persistable.** The applier can produce confirmed states during gated synthetic tests; the profile write path refuses them regardless; no non-test store receives a truth label.
4. **T5 uses the clockless elapsed-marker convention** — a deterministic elapsed measure, not a wall-clock timestamp, because the pure core has no clock and the applier must not invent one.
5. **T1 remains dormant** — catalogued, refused as unavailable (never illegal, never runnable) until grant machinery exists by its own future authority.
6. **T8 has no reactivation** — supersession is terminal; the old item is retained and relabelled, never revived, never removed.
7. *Observation, no action taken:* the pending ledger's module docstring ("nothing can yet run") now describes only the nine remaining future-phase stubs — harmless, noted here rather than edited.

## 5. Deferred at closure

Nothing below exists, and nothing below is authorised by this record; each waits for its own reviewed decision or era: **durable ledger storage; Approved persistence; contradiction and supersession persistence; the T1 production path** (extraction under grant — adapter era); **the review-surface era** (real review and approval surfaces, with the string catalogue, fatigue standard, and legibility work they require); and the standing never-items, restated so closure cannot soften them — no escrow or recovery path in any form, no model contact without its own governed decision, no real health data ever. W3-D5 and later W3 deliverables remain unstarted; the D5 runway-mapping question is a separate later discussion and is not decided by this closure.

## 6. Gate

W3-D5 and everything after it sit behind their own runway discussion, briefs, and reviewed decisions. The transition engine stands ready as the layer future review surfaces will drive — through acts those surfaces must earn the right to construct, under the same ceremony that built everything beneath them. Nothing in this record pre-authorises any part of it.
