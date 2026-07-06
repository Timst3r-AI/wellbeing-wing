# W3-D6 Closure Record

**Status:** Accepted by human reviewer, 2026-07-06. Not a build instruction.
**Phase:** W3 — Health Vault and Health Profile Foundations · **Deliverable:** D6 — Export / Backup / Restore
**Type:** Closure record / audit seal. Docs-only. Authorises nothing to be built.
**Date:** 2026-07-06
**Tier at landing:** J — full ceremony
**Governed by:** the W3 runway; ADRs 0004, 0009, 0010, 0011, 0012, 0013, 0015; W1-D2; the accepted W3-D6 planning brief v2 and its reviewer rulings; the closure-record precedent

---

**D6 taught the vault's promises to travel and gave the user's own bytes back. One portable file that tells nothing, carrying its own lock reachable and its contents silent; a restore that is exactly one sentence — file plus passphrase, into clean ground, done; and an export that returns what entered, byte-identical, under no gate but its owner's act. The shapes are carried in this record, in ink, so no reader needs a draft or a code comment to know what was built.**

## 1. Closure statement

**W3-D6 — Export / Backup / Restore — is complete and closed.** Backup export, restore symmetry, and export-as-right are all published. The runway's wording clause is satisfied by citation: the key-loss and backup sentences are vetted and catalogued in ADRs 0011 and 0012, the catalogue of record; the string-catalogue *structure* remains a surface-era matter. **W3-D7 has not started.**

## 2. The published chain

| Landing | Commit | What it published |
|---|---|---|
| M1 — backup export and restore symmetry | `0a7b9d4ae6f9025e40e8a4e9758cb265978babb2` | The WBWB portable ciphertext file; empty-target-only restore with five-step validation; the directory-target refusal guard; the four-magic seam |
| M2 — export as a right | `9381bc3f0ab22228487e00f7cd7cadf11853bb32` | Single-record plaintext export at the data layer; provenance as structured return always, sidecar only when explicit; destination validation before any write |

## 3. Decision anchor

D6 ran on its accepted planning brief v2 plus reviewer rulings, without a new decision record; the rulings are restated here so this seal is self-sufficient.

**The seven planning rulings:** (1) the WBWB container with the **circularity correction — the key envelope rides reachable, never trapped inside the payload it unlocks**, because restore must derive the master from it before anything else can open; (2) **empty-target-only restore** — no merge, no overwrite, refusal on existing vault material, writes only after validation, and no health-record plaintext decrypted merely to restore; (3) **single-record plaintext export as a data-layer right**, with the provenance sidecar as explicit optional output or structured return only — never a silent second disclosure artifact; (4) **whole-vault plaintext export deferred** to its own future decision record; (5) **`WBWB` as the fourth distinct magic**, with the seam matrix extended in both directions; (6) **caller-supplied source sets only** — the engine remains headless and never crawls, guesses, or discovers files, resolving the ledger-path question: a complete W3-era vault backup includes the durable ledger when the caller identifies the vault unit; (7) the **M1/M2/M3 milestone split**, with the container shape captured in this committed closure record.

**The two M2 rulings:** profile-class records **refuse** — this era's export is evidence-record export only, and profile export is deferred to its own future governed path; existing payload **and** provenance destinations **refuse before any write** — all destinations validate before either file is written.

**Consumed ADR 0015 inputs, named as consumed:** the ledger joins the backup unit as sealed ciphertext; the torn-tail restore doctrine travels (intact frames readable, the tail honestly reported at first read); the caller-supplied ledger/source-set question is resolved here.

## 4. The shapes, in ink (structural level)

**The WBWB backup container:**

1. a **minimal public WBWB header** carrying no vault information;
2. the **reachable encrypted WBWK key envelope / KDF metadata** — the same ciphertext that rests beside the vault, placed where restore can read it before holding the master;
3. the **sealed payload, authenticated under the restored master key**, holding the manifest, member structure, sealed records, and the durable ledger. **No record names, member names, cardinality, manifest, or ledger structure is exposed outside the sealed payload.** The travelling file tells nothing beyond "a backup of some vault, this format, this derivation cost."

**The restore validation order**, writes strictly last: (1) validate WBWB magic/version; (2) unwrap the reachable encrypted key envelope with the passphrase; (3) authenticate the sealed payload under the restored master; (4) validate the sealed manifest structurally; (5) only then write members to the empty target — as the sealed bytes they are.

**The export-right contract:** one evidence record's payload bytes out, **byte-identical** to what entered at import; provenance **always returned as structured data**; the provenance sidecar written **only when explicitly requested**; **all destinations validated before any write**, existing destinations refused; **profile-class records refused**; no batch export, no whole-vault plaintext export, no user-act machinery, no review or approve machinery — a right, not a transition.

## 5. Verification at closure

- **Deterministic suite: 218 tests — 209 passed, 9 pending-ledger skips (all future-phase owned), 0 failures** at the time of closure.
- **Public-safety scan: pass, zero findings**, normal mode over all tracked files.
- **Registry: unchanged through M1 and M2 — 35 entries before this closure; this record's entry advances it to 36.** The governance/product boundary held again.
- **Dependencies: unchanged.** The three pins remain the engine's whole third-party surface.
- **Four distinct magics** (`WBWG`, `WBWK`, `WBWL`, `WBWB`) with bidirectional seam discipline — every format refuses every other format's bytes.
- **Sources remain byte-identical** across export and backup operations, proven after successes and refusals alike; **every refusal is write-free**, proven refusal by refusal.
- **No D7 work exists.**

## 6. Honest findings carried forward

1. **Backup assembly holds the vault's ciphertext in memory** — fine at current scale, noted in ink for the future.
2. **A backup cannot be inventoried without the passphrase** — the design working, stated so nobody mistakes it for a defect.
3. **The provenance sidecar is never silent** — it exists only by the owner's explicit request.
4. **User-taken backups cannot be reached by later erasure** — copies the user has made are the user's own to manage; the engine never pretends otherwise.
5. **Torn-tail honesty travels** — a backup carrying a torn ledger tail restores with intact history readable and the tail reported, never hidden.

## 7. Deferred at closure

Nothing below exists, and nothing below is authorised by this record: whole-vault plaintext export (its own future decision record); profile export (its own future governed path); printed recovery codes (ADR 0011 decision 6's own future record); all surface-era wording, cadence, and onboarding (offered-once, never-nag, and the tone doctrine wait for real surfaces); batch export; merge or overwrite restore modes; sync, scheduling, search, adapter, UI, CLI; and — restated so closure cannot soften it — no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind. **W3-D7 — the phase closure, the final W3 act — arrives only through its own drafting instruction.**
