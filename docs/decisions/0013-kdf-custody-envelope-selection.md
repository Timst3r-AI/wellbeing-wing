# 0013 — Key Derivation, Custody, and Envelope Selection

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D2 — between published engine milestones and any key-handling milestone)
**Decision mode:** doctrine-derived for custody, wrap architecture, and envelope; evidence-based (disposable micro-spike, per the platform-doctrine rules) for the KDF profile, which enters as a review-dated provisional.
**Blocks:** every milestone that touches real key handling — key derivation, first-run, passphrase change, profile layer, backup/export.

## Decision question

The published engine can seal and unseal records under a key, and can import bytes with provenance — but every key it has ever held was a test-supplied random, by decision. Four questions were deliberately left open by the encryption doctrine and the runtime selection: **where does the key come from (KDF), what does the user hold (custody), how are keys arranged (wrap architecture), and what is one sealed unit (envelope)?** This record closes all four for v1.

## Controlling law

- **ADR 0004 (plaintext residue):** minimal plaintext windows; default-deny persistence past task end. Bears directly on the envelope choice and on what custody material may rest on disk.
- **ADR 0005 (encryption doctrine):** no custom cryptography; authenticated encryption; memory-hard KDF class; versioned format; no escrow, ever. The custody and envelope questions are ADR 0005's own named opens; this record answers them within its lines.
- **ADR 0008 (runtime selection):** the selected stack and its binding key-handling caveat — language-level key copies persist until collection; short-lived key objects in narrowest scope are the standing mitigations. All selections below must not widen that honest residual.
- **ADR 0011 (backup guidance):** ciphertext travels, keys never. Decision 5 below records the deliberate reading of that line for the sealed key envelope.
- **ADR 0012 (key-loss wording):** the vetted sentence — a key only the user holds, no reset, no one else able to open the vault — is the test every custody design must pass literally.
- **W3-D2 engine brief:** named these questions as its open items and required them to be settled by reviewed decision before deeper milestones.

## Micro-spike evidence summary (public-safe)

A disposable micro-spike, outside the repo under the platform-doctrine and artifact-policy rules, measured the selected library's three named memory-hard KDF profiles (Argon2id family) on one Windows-class consumer machine — existing pinned dependencies only, synthetic throwaway passphrase, numbers retained and nothing else:

| Profile | Parameters | Derivation wall-clock | Transient memory | Result |
|---|---|---|---|---|
| interactive | ops 2 / 64 MB | ~0.10 s | ~64 MB | pass |
| moderate | ops 3 / 256 MB | ~0.58–0.60 s, stable across runs | ~256 MB | pass |
| sensitive | ops 4 / 1024 MB | ~3.1–5.9 s, unstable (near-2× variance) | ~1 GB | pass with concern |

A full wrap/unwrap cycle (derive → seal a 32-byte stand-in master key → open → verify) **passed on all three profiles**; the sealed key envelope is approximately 72 bytes; the KDF dominates the entire open cost — the wrap layer adds no meaningful runtime cost. The sensitive profile's timing instability at a ~1 GB transient allocation is the signature of memory pressure, implying allocation-failure risk — a refusal-to-open failure mode — on lower-memory machines of the same class.

## Decision

1. **KDF profile: the selected library's *moderate* named profile, as the v1 review-dated provisional.** Named profiles only, never hand-tuned numbers — the no-custom-cryptography doctrine extended to parameters. The profile name, its resolved parameters, and the per-vault random salt are recorded inside the versioned key envelope (the salt is not a secret and stores in the clear, per standard practice), so any future profile change is a versioned migration — re-derive at next open, re-seal the envelope — never a break. The *interactive* profile is **not needed as a v1 fallback** on the evidence. The *sensitive* profile is **rejected as the v1 default** for its memory-pressure and refusal-to-open risk, without prejudice to a future user-selected strength option by separate record.
2. **Custody: passphrase, alone, for v1.** Nothing key-shaped ever rests on disk — the strongest residue posture available — and the key-loss sentence is most literally true: the key-producing secret lives in the user's head or on the user's own paper, outside every threat the software carries. **No keyfile in v1. No "both" option in v1. No escrow, no recovery service, no secret questions, no cloud recovery, no hidden recovery path — in any form, ever.** A keyfile may arrive later only through its own reviewed decision, as a second way to produce the key-encryption key.
3. **Architecture: the two-layer wrap pattern.** Records are sealed under a random master key; the passphrase-derived key seals only the master, inside the small versioned key envelope. Built entirely from the already-selected library's authenticated encryption — no new primitive, no custom construction. Passphrase change re-seals the one small envelope; no record is ever re-encrypted for a custody event. The published milestone-1/2 store and import code is confirmed unchanged as the permanent core — its per-operation random key becomes the master key. **Stated plainly: the wrap layer creates no recovery path. Losing the passphrase makes the master unreachable and the vault unrecoverable — not by the user, not by the Wing, not by anyone — exactly as the published key-loss wording promises.**
4. **Envelope: per-record sealed blobs.** Each record is one sealed unit, as the published milestones already shape it. Opening one record decrypts one record — the minimal plaintext window; corruption's blast radius is one record; import cost is constant in vault size; backup is the natural copying of ciphertext files. **Honest cost, named for the threat register in ink: record cardinality and approximate record sizes are observable on disk without any key.** This leakage is accepted, documented, and never euphemised.
5. **The sealed key envelope travels with backups.** Reasoning, recorded to foreclose future convenient ambiguity: the envelope is *ciphertext* — the master key sealed under the passphrase-derived key by authenticated encryption — not the user-held secret. The user-held secret is the passphrase, which never travels anywhere. A backup containing records plus the sealed envelope restores on any machine *only* with the passphrase, which is the honest meaning of "a key only you hold." This preserves "ciphertext travels, keys never" by its intent and its letter: what travels is ciphertext; what never travels is the key-producing secret. Implementation must never treat this paragraph as negotiable in either direction — the envelope always travels with a backup, and nothing plaintext-key-shaped ever does.
6. **Key-envelope residence: its own small versioned file beside the records.** Same versioned-format discipline as everything sealed — magic, version, refusal of unknown versions — and not hidden inside or appended to any record's header: key custody and record content are different subjects and stay structurally separate. Vault layout, record naming, listing, indexing, and search remain **deferred to their own reviewed decisions**; this record places one file and decides nothing else about arrangement.

## Options considered

- **KDF — interactive / moderate / sensitive:** interactive viable everywhere but the weakest brute-force posture for a high-value, rarely-opened target; **moderate accepted** — sub-second stable open, transient spike within ordinary machines' reach; sensitive rejected as default — unstable on the measured machine, failure-prone below it.
- **Custody — passphrase / keyfile / both:** **passphrase accepted**; keyfile rejected for v1 — plaintext key material resting beside the vault (disk theft takes both), silent loss modes, and contradictory backup instructions (the vault backup must exclude it while the user must separately preserve it); "both" rejected for v1 — two custody paths double the testing and wording surface for no v1 need.
- **Architecture — direct passphrase-derived record keys / two-layer wrap:** direct derivation rejected — it makes passphrase change a full-vault re-encryption and couples every record to the custody form; **wrap accepted** — custody events touch ~72 bytes, custody forms become interchangeable producers of the key-encryption key, and the published core is preserved unchanged.
- **Envelope — per-record / whole-store / hybrid:** **per-record accepted**; whole-store rejected — every import rewrites everything (total blast radius mid-failure), every open decrypts everything (maximal plaintext window, against the residue doctrine's grain), backup degenerates to full-copy churn; hybrid (per-record plus sealed manifest) rejected for v1 — the manifest *is* the deferred vault-layout/index decision arriving through a side door, and deferred doctrine stays deferred.

## Rationale

Every selection is the one that keeps an already-published promise. Moderate is the strongest profile the evidence shows the actual machine class sustaining without a refusal-to-open failure mode — and a vault that cannot open is a worse betrayal than a slower brute force. Passphrase custody is the only form where the residue doctrine's "nothing key-shaped rests" holds absolutely and the key-loss sentence needs no footnote. The wrap pattern is what makes the other choices cheap to hold and cheap to revisit: profiles migrate, passphrases change, custody forms could multiply — and no record is ever re-encrypted for any of it. Per-record envelopes put the residue doctrine's minimal-window principle into the format itself. Where a choice has a real cost — cardinality leakage, weak-passphrase honesty — the cost is written down, not traded away silently.

## Consequences

- The engine's next milestone can implement derivation, the key envelope, and passphrase change against settled doctrine.
- The key envelope becomes the second versioned format in the system (after the store header), with the same refusal discipline.
- Backup guidance (W3-D6 era) inherits decision 5 verbatim: the backup unit is "records plus sealed envelope"; restore requires the passphrase; no other path exists.
- The threat register must carry, in ink: per-record cardinality/size observability; the weak-passphrase honest weakness (the memory-hard KDF raises attacker cost but cannot make a weak passphrase strong, and no surface may imply otherwise); and the standing language-level key-copy residual from the runtime selection.
- First-run and passphrase-entry surfaces, when they exist, are bound by the published key-loss wording and by decision 2's no-recovery absolutes.

## Non-goals

Does not design first-run, passphrase entry, or any wording surface (the key-loss record's venue, needing a surface to exist); does not decide vault layout, naming, listing, indexing, or search; does not design backup/export mechanics; does not add a keyfile or any second custody form; does not create a user-selected strength option; does not revisit the runtime or library selection.

## Implementation gates

Accepted before any key-derivation, custody, or envelope code exists. The implementing milestone lands through its own authorisation (Tier J expected — no new dependency or directory is required by any selection above; any deviation discovered is a pause). The KDF profile enters code as this record's review-dated provisional, recorded in the key envelope from the first vault.

## What implementation work must not do until this record is accepted

No KDF call, custody structure, key envelope, wrap/unwrap path, or passphrase-handling code; no alteration of the published store or import modules toward any selection here; no installation or request of any dependency.

## Testing / evaluation requirements

Wrap/unwrap roundtrip under a synthetic throwaway passphrase; wrong-passphrase failure that is clean, content-free, and indistinguishable in wording posture from the store's existing integrity refusal; unknown envelope version refused cleanly; KDF profile, parameters, and salt recorded in the envelope and honoured on re-open; passphrase change re-seals the envelope while every record file remains byte-identical; no passphrase, derived key, or master key bytes in any store, output, log, or test artifact — dedicated assertions, not hopes; residue class extended to the derivation path as far as the platform allows; the structural no-interpretation and posture assertions remain green throughout.

## Public-safety considerations

All tests use synthetic throwaway passphrases and grammar-placeholder content only — never real passphrases, never real data. Refusal messages never echo passphrases, keys, or content. The evidence summary above is the micro-spike's entire public surface: timings, memory figures, and pass/fail on a Windows-class machine, with no machine identity, no paths, no retained secrets. No evidence artifact enters the repo except this record's summary.

## Dependencies

ADR 0004 (residue); ADR 0005 (encryption doctrine — closes its two named opens); ADR 0008 (runtime selection and key-handling caveat); ADR 0009 (import path unchanged by these selections); ADR 0011 (backup guidance — decision 5 records its deliberate reading); ADR 0012 (key-loss wording — custody tested against it); the W3-D2 engine brief and its review corpus (decision brief and micro-spike findings note).

## Open questions

1. **Minimum passphrase posture** — whether v1 sets a minimum length or similar floor, and how the surface stays honest about what a floor does and does not buy (wording-era question; belongs with the first-run surface decision, bound by the key-loss record).
2. **User-selected strength option** — whether a later record offers the sensitive profile to users who choose it knowingly (explicitly not v1).
3. **Rekey ceremony surface** — passphrase change is architecturally cheap by decision 3; when and how it is offered is a surface decision for its own time.
4. **Key-envelope file naming** — an implementation detail for the implementing milestone's landing, within decision 6's residence rule.
