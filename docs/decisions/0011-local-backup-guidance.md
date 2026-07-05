# 0011 — Local Backup Guidance

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing C — lands with ADR 0012) · **Blocks:** real-data use; the W3-D6 engine milestone (export/backup operations)

## Decision question

What backup story does the Wing offer for the vault and its keys, such that key loss has a real mitigation without any form of escrow?

## Context

ADR 0001 named the cost: user-held keys are user-losable keys. The threat model named the permanent pressure: recovery flows become silent escrow, and grief becomes the argument for them. A backup story must exist before real data does — but every convenient version of "we can help" reintroduces the trusted party the architecture exists to remove. This record defines what help looks like when the answer to "can you unlock it?" must stay *no*.

## Decision

1. **Two things need backing up, and they are treated differently.** The **store** (ciphertext) can be backed up anywhere, safely, because it is unreadable without keys — the Wing provides a one-action *encrypted backup export* producing a portable ciphertext file (well-defined by ADR 0005's versioned format). The **key/passphrase** is the user's alone; the Wing provides guidance for keeping it safe (written copy in a secure place, a password manager of the user's choosing) and never stores, transmits, or receives it.
2. **Backup is offered, never required.** Offered once at onboarding, immediately after the key-loss statement (ADR 0012) — consequence and remedy in the same breath. Skippable; the consequence of skipping is restated once, plainly; **it is never mentioned again unprompted.** Backup remains available on demand from the vault's own surfaces.
3. **Ciphertext may go where the user pleases.** Guidance may honestly say the exported backup file is safe on user-chosen external media or the user's own cloud storage — with the equally honest note that the *key must never travel with it*. This is user action over their own data, not hosted mode, and creates no operator involvement.
4. **No Wing-operated backup destination exists** — no "backup to our service," free or paid, ever, without a future record argued against ADR 0001.
5. **Restore is symmetric and user-performed:** point the Wing at a backup file, supply the key, done. A backup file plus no key is nothing, and the restore surface says so without drama.
6. **Printed recovery codes are deferred** to their own record (key material in physical form deserves its own custody analysis), noted as the likely next mitigation if passphrase loss proves common.
7. **Tone doctrine (shared with the paired record):** plain, not frightening; firm, not theatrical. Backup guidance describes what to do, not what to fear.

## Rationale

Separating store-backup (easy, safe, encourageable) from key-custody (irreducibly the user's) keeps the honest promise intact while removing most practical loss scenarios: disk failure, device loss, and accidental deletion are all survivable with a ciphertext backup plus a key kept anywhere sensible. The remaining scenario — losing the key itself — is the one the architecture priced in, and no backup design can remove it without becoming escrow.

## Options considered

- **(a) Encrypted export + key guidance, offered once.** Accepted.
- **(b) Wing-operated encrypted cloud backup.** Rejected: operator-held ciphertext plus operator-adjacent recovery pressure; also drags hosted-mode disclosure obligations in early.
- **(c) No backup story in W3.** Rejected: the first disk failure converts into avoidable total loss and maximal escrow pressure.

## Accepted recommendation

Option (a), decisions 1–7.

## Consequences

Backup completeness depends on user follow-through — accepted; the design maximises the chance the one offer lands. Restore testing becomes a standing engine test class. The export file format inherits the versioned-format requirement.

## Non-goals

No multi-device sync (key-distribution problem, later phase); no recovery codes (deferred, decision 6); no scheduled/automatic backups (background-behaviour question, flagged not smuggled).

## Implementation gates

Accepted before real data enters any real vault; wording lands via the governed string catalogue when it exists (this record is its review of record until then); backup/export code is engine code and inherits every engine gate.

## Testing / evaluation requirements

Round-trip restore tests (backup → wipe → restore → verify, synthetic fixtures); backup-file-is-ciphertext byte assertion (no plaintext, no key material in the export); no-nag assertion (after the onboarding offer and one restatement, no code path re-raises backup unprompted); restore-without-key behaves as honest refusal.

## Public-safety considerations

Guidance text is public and generic; examples never describe a specific user's storage habits; all test artifacts synthetic.

## Dependencies

ADR 0001 (alternative 3; named costs); ADR 0005 (versioned format); the threat model's recovery-pressure and key-loss entries; ADR 0012 (paired landing; the consequence this record remedies); ADR 0004 and ADR 0007 (residue and artifact law over implementation and testing).

## What implementation work must not do until this record is accepted

No backup or export-format code; no onboarding flow design; no restore mechanics; no scheduled-backup machinery of any kind.

## Open questions

1. Whether v1 offers an *optional user-initiated* backup reminder setting (a user-requested standing prompt vs the no-push law's purity) — recommend deferring to the review-package phase.
2. Recovery-code record timing — before or with the release phase's non-household gate.
