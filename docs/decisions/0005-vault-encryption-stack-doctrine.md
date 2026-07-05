# 0005 — Vault Encryption Stack Doctrine

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (deliverable 1, doctrine pair — lands with ADR 0004) · **Blocks:** all W3 Vault code
**Decision mode:** doctrine now; implementation evidence required before final stack choice.

## Decision question

What cryptographic doctrine governs the Vault's implementation of ADR 0001's user-held-key custody — and which choices are decidable now versus after a library evaluation spike?

## Context

ADR 0001 fixed *who* holds keys and *what* the host may see (ciphertext). Nothing yet fixes the cryptography that makes those words true. This is the classic place where governance projects fail quietly: the doctrine is perfect and the implementation uses a broken mode. The record separates what architecture can decide (doctrine, prohibitions, structure) from what only evidence can decide (specific libraries, primitives, parameters).

## Decision

**Decided now (doctrine):**

1. **No custom cryptography, ever.** No home-rolled primitives, no novel compositions of primitives, no "simplified" constructions. The Wing uses an audited, actively maintained, widely deployed cryptographic library, through its highest-level safe interfaces.
2. **Authenticated encryption only.** Every encrypted object is integrity-protected; tampering is detectable, not just unreadable.
3. **Key derivation from user-held secrets uses a memory-hard KDF** of the current well-reviewed class. The user-facing custody form (passphrase, key file, or passphrase+keyfile) is part of this record's final form after the spike reports on platform key-handling realities.
4. **Versioned format with migration path, no escrow.** Every encrypted store carries a format version header. Algorithm agility means: a future migration re-encrypts under user control, inside Z1, with the user's keys — it never means a recovery mechanism, a side-channel, or an operator capability. "We'll migrate later" without this structure is escrow pressure in disguise; with it, migration is an ordinary user-side operation.
5. **Envelope structure decided at spike time, within a fixed constraint:** whether encryption is per-record or whole-store is an evidence question (performance, residue interaction, partial-sync futures) — but either way, key material never appears in any store, any log, any export, and no derived key is persisted beyond what the chosen library's audited patterns require.
6. **OS keychain integration is deferred to its own record.** Convenience unlock via platform keychains changes the custody story and gets its own review; the Vault key's custody is not delegated to any platform service by default.

**Deferred to spike evidence:** specific library selection; specific primitive suite as exposed by that library; KDF parameters; envelope structure; keyfile format.

## Rationale

Everything an architect can get wrong in cryptography is avoided by using audited high-level interfaces; everything an architect can get right is in the doctrine above. Naming a specific library from prose, without evaluating its platform bindings, maintenance state, and interaction with the (also undecided) runtime stack, would be premature certainty.

## Options considered

- **(a) Audited mainstream library, high-level interfaces** (libsodium-class libraries are the candidate family, named as candidates requiring later technical verification, not as a selection). **Accepted as doctrine.**
- **(b) OS-platform crypto services as primary.** Rejected as primary: custody becomes platform-mediated and platform-divergent; may return as a convenience layer via its own record (decision 6).
- **(c) Custom composition of lower-level primitives.** Rejected permanently (decision 1).

## Accepted recommendation

Doctrine as decided; the candidate library family is evaluated in a shared platform/crypto evaluation spike (the platform and crypto evaluations share one spike, since binding quality is platform-dependent); a short follow-up record ("Vault Encryption Stack — Final Selection") lands the specific choices with the spike's evidence attached.

## Consequences

Two-stage decision (doctrine + selection) adds one review cycle and prevents the worst outcome (a stack chosen by prose). The no-keychain-by-default posture makes first-run UX blunter — consistent with ADR 0001's named costs. The versioned-format requirement adds small up-front format work and buys every future migration.

## Non-goals

No hosted-mode sync design; no multi-device key distribution (ADR 0001 consequence, later phase); no backup mechanics (the future backup-guidance record); no recovery of any kind (ADR 0001 alternative 3 stands).

## Implementation gates

No Vault code until: this record accepted, the spike completed, and the final-selection record accepted. The spike itself is not repo code — spikes are disposable evaluation work outside the repository, never committed; their findings documents are their only lasting artifact, attached to the selection record.

## Testing / evaluation requirements

Round-trip and tamper-detection tests; wrong-key behaviour (clean failure, no partial plaintext); format-version handling (unknown version = clean refusal); KDF parameter verification against the selection record; interaction with residue tests (ADR 0004) — decryption paths leave nothing behind.

## Public-safety considerations

The record and spike findings discuss mechanisms generically and publicly (algorithm choices are public knowledge and gain nothing from secrecy); no user-specific configuration details in any public artifact.

## Dependencies

ADR 0001; W1-D5 (D5-T01/T14/T19); ADR 0004 (residue interaction); the future runtime/platform stack record (shared spike).

## What implementation work must not do until this record is accepted

No cryptographic code of any kind; no library installation; no key-handling prototypes; no format design in code. Drafting the final-selection record's *template* is permitted (docs only).

## Open questions

1. Custody form (passphrase / keyfile / both) — user-experience evidence from the spike informs this.
2. Envelope structure (per-record vs whole-store) — spike evidence.
3. Whether the future multi-device design constrains the format header now (flagged to the spike: cheap to reserve, costly to retrofit).
