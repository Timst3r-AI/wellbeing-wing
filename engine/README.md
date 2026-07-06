# Engine

The local headless engine spine: an encrypted store that forgets nothing it holds and remembers nothing it shouldn't, an import path that refuses to understand what it carries, and a custody layer that makes the vault belong to exactly one person. No UI, no CLI, no network, no model contact — one API, its tests, and nothing else. Every behaviour here was decided in a reviewed record before it was code; this document summarises and cites, it decides nothing.

## The spine

- **Store** (`core/header.py`, `core/store.py`) — seal/unseal of one blob under a caller-supplied key, authenticated encryption via the audited library (ADR 0005, ADR 0008). Keys are per-operation arguments in the narrowest scope; no module retains a key; nothing here logs or prints, by structural test.
- **Import** (`core/intake.py`, `core/record.py`) — bytes plus user-supplied provenance in, one sealed record out (ADR 0009). Zero content interpretation: inspection is capped at magic-number / file-shape depth, enforced structurally (the core can import only `json` and itself — it cannot parse what it cannot import). A refused import writes nothing. Provenance is stored verbatim; absent source and date are labelled *unprovenanced by user* inside the sealed record.
- **Custody** (`core/envelope.py`, `core/custody.py`) — the two-layer wrap (ADR 0013): records are sealed under a random master key; the passphrase-derived key seals only the master, inside the key envelope. Passphrase change re-seals the one small envelope; no record is ever re-encrypted by a custody event. Creating an envelope where one exists is refused — destruction of access is never a silent side effect.
- **Ports** (`ports/`) — crypto, storage, clock, and ledger behind interfaces; the doctrine core stays pure and every worldly behaviour is swappable and testable. The crypto port is the single worldly crypto door.

## The three versioned formats

Every format is versioned from its first byte and refuses unknown versions, malformed layouts, and (where the format owns its length) truncation and trailing bytes. No format silently accepts ambiguity.

| Format | Module | Magic | Shape |
|---|---|---|---|
| Store header | `core/header.py` | `WBWG` | 16 bytes: magic 4 + version 2 + reserved 10; prefixes every sealed blob |
| Record | `core/record.py` | — (see note) | version 2 + length-prefixed provenance JSON + length-prefixed payload; exact-length enforced |
| Key envelope | `core/envelope.py` | `WBWK` | magic 4 + version 2 + profile name + parameters + salt + sealed master; exact-length enforced |

**Honest note on the record format:** the inner record carries no magic of its own. This is accepted and documented, not hidden: record bytes exist only inside sealed store plaintext, so context disambiguates, and the leading version field refuses foreign bytes — the cross-decoder tests prove each format's bytes are refused by every other format's decoder. The store header is a prefix format by design (the bytes after it are ciphertext), so a trailing-bytes refusal does not apply to it.

## The custody model (ADR 0013)

Passphrase-only in v1. The key-derivation function is the library's memory-hard KDF at the **moderate named profile** — a review-dated provisional selected on machine-level evidence; named profiles only, never hand-tuned numbers. The envelope records the profile name, its resolved parameters, and the per-vault salt (not a secret, stored in the clear per standard practice), and opening honours the *recorded* parameters — so future profile changes are versioned migrations, never breaks. Fresh salt on every create and every passphrase change.

The sealed key envelope lives in its own small file beside the records, at a caller-chosen path (vault layout, naming, listing, indexing, and search are deferred to their own reviewed decisions). It travels with backups: it is ciphertext, not the user-held secret, and a restored backup opens only with the passphrase (ADR 0013 decision 5, reasoning recorded there in full).

**There is no recovery path and none may ever be added.** No keyfile in v1, no escrow, no recovery service, no secret questions, no cloud recovery, no hidden path of any kind. Losing the passphrase makes the master unreachable and the vault unrecoverable — not by the user, not by the Wing, not by anyone — exactly as the published key-loss wording (ADR 0012) promises.

## Honest residuals (in ink, per ADR 0008)

- **Language-level key copies.** The runtime cannot guarantee zeroing: passphrases, derived keys, and the master transit memory as immutable byte objects that persist until collection, and the OS may page them. Narrowest-scope handling — derive, use, release within each operation — is the mitigation. **Tests cannot prove memory absence**, and nothing in this repository claims otherwise. This weakness was weighed and accepted, with mitigations, in the runtime-selection record.
- **What tests do prove** is the file-level story: exact file sets after every operation, no plaintext on disk at any checkpoint (including at scale and after a killed process), and refusal paths that write nothing.

## Threat-register entries (required by ADR 0013)

1. **Record cardinality and approximate sizes are observable on disk without any key.** A consequence of the per-record envelope choice; accepted for its residue, blast-radius, and backup properties, and never euphemised.
2. **A weak passphrase is the honest weakness of passphrase custody.** The memory-hard KDF raises attacker cost but cannot make a weak passphrase strong; no surface may ever imply otherwise. Strength posture (floor, wording) is a deferred first-run decision.
3. **The language-level key-copy residual** described above.

## Known finding: non-atomic writes

`FileStorage.write_blob` is not atomic. A process killed mid-write can leave one truncated file: a truncated *record* refuses cleanly at open (integrity failure, content-free message) and touches nothing beside itself — the one-record blast radius the per-record envelope was chosen for. No plaintext appears either way; the kill-at-scale test stands guard. An atomic write (temp-file-plus-rename) would change file-write and residue behaviour — it transiently creates a second path — and is therefore **a possible future decision, not implemented here**.

## Testing discipline

- Synthetic data only: grammar placeholders (Persona-K, Allergen-X classes), synthetic throwaway passphrases. No real content, ever, in any test, fixture, or output.
- **Residue tests must never print sensitive content.** Failure output identifies location and category — a file name, a phase, an error class — never bytes. A residue test that prints residue is a leak with a test badge.
- The structural emits-nothing test means the engine contains no print and no logging at all — the log-content assertion is satisfied by there being nothing that logs.
- The structural import-cap test means the core cannot acquire a parser without failing the suite.
- Posture assertions (ADR 0010) hold from the first merge: no review or approval machinery exists anywhere in this tree.
