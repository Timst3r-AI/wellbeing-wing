# 0015 — Durable Ledger Doctrine

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (post-D5 doctrine gate; precedes the D6 brief by sequencing ruling)
**Decision mode:** doctrine-derived; no evidence spike required — nothing here turns on measurement.
**Blocks:** the durable-ledger implementation milestone; the D6 brief (which consumes this record's backup-unit answer); the honest retirement of the W3-D4 closure's emitted-never-stored finding.

## Decision question

The transition engine emits exactly one governance event per successful application — and nothing holds those events past process exit. When a governance event is emitted, **what may hold it durably: in what form, under whose key, with what append semantics, erasable by whom, and travelling where?** This record answers all five, as doctrine, before any implementation exists.

## Context

W3-D4 published the appliers with events emitted and returned to the caller, never stored — recorded in its closure as an honest carried finding, with durable storage explicitly deferred to this record. W3-D5 is closed; the residue accounting is sealed. W3-D6 (export/backup/restore) waits on one question only this record can settle: whether the ledger joins the backup unit. The ledger port's stand-in has carried the promise since the first engine milestone: durable ledger storage arrives with the milestone that needs it. This record decides what that milestone must build.

## Controlling law

- **W0 Law 13:** every transition, flag, suspension, and resolution is a ledger event — the record of governance must exist.
- **W1-D3 §8a — the load-bearing clause:** ledger records are C0 governance metadata: content-free with respect to health, personal, and contemplative content, but **privacy-sensitive by pattern**. The pattern of what gets reviewed, contradicted, or superseded — and when — is itself a sensitive signal. Governance metadata has no processing edges: never analytics, never behavioural profiling, never inference input; governance, audit, and user-visible export only.
- **W1-D1:** the ledger rule binds — no processing edges, in the boundary map's own terms.
- **Law 11 and W1-D2 §0.3:** the user is the final authority over their own record; removal of history is exclusively the user's erasure right, exercised knowingly.
- **ADR 0004 decision 4:** any persistent derived artifact requires its own record with its own encryption story and its own residue tests. This is that record for the ledger.
- **ADR 0005 / ADR 0013:** the sealed-store machinery, the per-record envelope philosophy (small blast radius, minimal plaintext windows), and the backup-unit reasoning this record extends.
- **ADR 0010:** nothing about durable events creates a review or approval path; the posture assertions bind unchanged.
- **The W3-D4 and W3-D5 closure records:** the carried finding this record retires, and the sealed residue accounting the implementation must not disturb.

## Decision

1. **A durable ledger exists.** The record of governance is not optional and does not evaporate on process exit; Law 13's expectation becomes a persisted reality through the implementation milestone this record sequences.
2. **The ledger stores sealed, under the master-key custody boundary.** Per §8a, an unsealed activity history would leak meaning by pattern — undoing per-record envelope discretion one metadata line at a time. The honest trade-off is accepted and stated: the ledger is writable only while the vault is unlocked (acceptable, because governance events only occur during unlocked operations), and reading one's own ledger requires one's own passphrase — the design working, not failing.
3. **Doctrine direction for form: independently sealed append frames.** Appending to a single sealed blob would re-encrypt the whole history per event — the whole-store shape already rejected for records. The direction is one ledger file of length-prefixed frames, **each frame its own small ciphertext**, versioned with the same discipline as every format before it. Frame-level detail belongs to the implementing milestone, within this direction.
4. **Event scope: doctrine-wide, implementation-narrow.** The doctrine covers **all governance events** — every transition, flag, suspension, and resolution, and in time the import and custody operations' events. **v1 implementation scope is the events that exist today: the emitted transition events.** Import/custody event emission is named as an **explicit future extension — not retrofitted now, not mandated by this record.**
5. **The ledger joins the backup unit as sealed ciphertext.** The user's governance history is theirs; ciphertext travels, keys never — exactly as the key envelope travels under the key-architecture record's reasoning. A backup that restored a vault without its history would be a quiet amnesia nobody chose. The D6 brief consumes this as settled doctrine.
6. **Erasure is the user's explicit, knowing act — only.** Never automatic, never a side effect: **erasing a profile item does not silently erase its governance history** (that would be history-rewriting by side door). **v1 erasure may be whole-ledger only; scoped erasure is deferred to future mechanics.** No retention rule may resist the user's explicit erasure. Honest limit, stated: erasure reaches the local ledger; copies the user has taken (backups, exports) are the user's own to manage — the engine never pretends to reach them.

## Allowed and forbidden metadata classes

**Allowed:** event kind (transition identifiers, and operation-class identifiers when the extension arrives); references drawn from identifiers and grammar vocabulary (section identities, label names); timestamps and the clockless elapsed markers the engine already emits; counts. **Forbidden:** content of any governed class; content-derived values; free text beyond fixed vocabulary; aggregations or analytics of any kind; anything enabling behavioural profiling or cross-room inference. The event shape already refuses a content field by construction; this record makes the storage half doctrine: **what may not be emitted may never be stored, and what is stored may never grow processing edges.**

## Append-only doctrine and platform honesty

The ledger is **append-only**: history is never rewritten, reordered, or compacted; the erasure right is the sole exception, and it removes, never edits. Platform honesty, in ink from the start: **appends are not atomic on this filesystem** (the non-atomic-write finding's sibling). A crash mid-append may tear the final frame. The doctrine's answer is the per-record philosophy applied to events: **a torn tail frame is detected and refused cleanly; every prior frame remains intact and readable; the blast radius is one event** — and no claim of perfect durability is ever made anywhere.

## Relationship to D6 (backup / export / restore)

Three answers handed to the D6 brief as settled inputs: the ledger **is in the backup unit** (decision 5); restore behaviour for a backup carrying a torn ledger tail follows the same clean-refusal-of-the-tail, keep-the-rest doctrine; and ledger export to the user is a **rights-category operation** (user-visible export is among the ledger's only permitted uses) whose mechanics belong to D6 or later — this record grants the doctrine, not the feature.

## Implementation sequencing

**Decision record first — this record.** Then a **small dedicated implementation milestone, before D6's build arc**, so D6 consumes a finished ledger rather than co-building one. **This record authorises no implementation**: it sets doctrine and the sequencing expectation only; the milestone arrives through its own scope pass, landing prep, and authorisations, like every milestone before it. The implementation must preserve, unchanged: applier purity (appliers take no ports — the ledger writer is caller-side), the event shape, the test stand-in, and every standing posture, residue, and structural assertion.

## Non-goals

Does not build storage; does not retrofit import/custody emissions; does not design scoped erasure; does not design ledger export surfaces or any surface; does not create review/approval machinery or touch ADR 0010's ground; does not decide D6's backup format beyond the membership answer; does not add dependencies, directories, or formats beyond naming the frame direction.

## Testing / evaluation requirements (for the later implementation)

Frame roundtrip under the master key; torn-tail refusal with prior frames intact (the one-event blast radius, proven not asserted); append-only semantics (no rewrite path exists); no plaintext event data on disk (residue class extended to the ledger file); wrong-key clean refusal; whole-ledger erasure as an explicit act that removes the file and nothing else; the forbidden-metadata classes unconstructable or refused at the writer; every standing assertion green throughout.

## Public-safety considerations

Ledger content is identifiers, vocabulary, timestamps, and counts — never health content; all test events synthetic, grammar placeholders only. The pattern-sensitivity that motivates sealing is itself the public-safety story: this record exists so that activity history never becomes a readable signal at rest. No real data, no machine identity, no surfaces, no wording for surfaces.

## Dependencies

W0 Law 13; Law 11; W1-D1; W1-D2 §0.3; W1-D3 §8a; ADR 0004; ADR 0005; ADR 0010; ADR 0013; the W3-D4 closure record; the W3-D5 closure record; the accepted remaining-runway mapping rulings (sequencing).

## Open questions

1. **Ledger file custody detail** — the frames seal under the master key directly, or under a ledger-purpose subkey derived from it (a wrap-pattern nicety with key-hygiene appeal); implementation-milestone question within decision 2, flagged for its scope pass.
2. **Event ordering guarantees** — append order versus emitted order under concurrent future callers; trivially identical today (no concurrency exists), named so the milestone states it rather than assumes it.
3. Whether the ledger file's **path stays caller-chosen** like every store file so far (the presumption, keeping layout deferred) — confirm at the milestone.
