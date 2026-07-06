# Engine

The local headless engine spine: an encrypted store that forgets nothing it holds and remembers nothing it shouldn't, an import path that refuses to understand what it carries, and a custody layer that makes the vault belong to exactly one person. No UI, no CLI, no network, no model contact — one API, its tests, and nothing else. Every behaviour here was decided in a reviewed record before it was code; this document summarises and cites, it decides nothing.

## The spine

- **Store** (`core/header.py`, `core/store.py`) — seal/unseal of one blob under a caller-supplied key, authenticated encryption via the audited library (ADR 0005, ADR 0008). Keys are per-operation arguments in the narrowest scope; no module retains a key; nothing here logs or prints, by structural test.
- **Import** (`core/intake.py`, `core/record.py`) — bytes plus user-supplied provenance in, one sealed record out (ADR 0009). Zero content interpretation: inspection is capped at magic-number / file-shape depth, enforced structurally (the core can import only `json` and itself — it cannot parse what it cannot import). A refused import writes nothing. Provenance is stored verbatim; absent source and date are labelled *unprovenanced by user* inside the sealed record.
- **Custody** (`core/envelope.py`, `core/custody.py`) — the two-layer wrap (ADR 0013): records are sealed under a random master key; the passphrase-derived key seals only the master, inside the key envelope. Passphrase change re-seals the one small envelope; no record is ever re-encrypted by a custody event. Creating an envelope where one exists is refused — destruction of access is never a silent side effect.
- **Profile model** (`core/profile.py`, `core/profile_records.py`) — the authority/staleness grammar (W1-D3) as data shapes, and their sealed persistence. See the profile-layer section below.
- **Ports** (`ports/`) — crypto, storage, clock, and ledger behind interfaces; the doctrine core stays pure and every worldly behaviour is swappable and testable. The crypto port is the single worldly crypto door.

## The versioned formats

Every format is versioned from its first byte and refuses unknown versions, malformed layouts, and (where the format owns its length) truncation and trailing bytes. No format silently accepts ambiguity.

| Format | Module | Magic | Shape |
|---|---|---|---|
| Store header | `core/header.py` | `WBWG` | 16 bytes: magic 4 + version 2 + reserved 10; prefixes every sealed blob |
| Record | `core/record.py` | — (see note) | version 2 + length-prefixed provenance JSON + length-prefixed payload; exact-length enforced |
| Key envelope | `core/envelope.py` | `WBWK` | magic 4 + version 2 + profile name + parameters + salt + sealed master; exact-length enforced |
| Ledger | `core/ledger_store.py` | `WBWL` | 16-byte header (magic 4 + version 2 + reserved 10), then length-prefixed frames, each frame its own small ciphertext decrypting to one event; torn tail refused with intact history preserved |
| Backup | `core/backup.py` | `WBWB` | 16-byte public header + length-prefixed reachable key envelope (WBWK ciphertext) + sealed payload authenticated under the restored master, holding manifest, sealed records, and ledger — no names, cardinality, or structure outside the sealed payload |

**Honest note on the record format:** the inner record carries no magic of its own. This is accepted and documented, not hidden: record bytes exist only inside sealed store plaintext, so context disambiguates, and the leading version field refuses foreign bytes — the cross-decoder tests prove each format's bytes are refused by every other format's decoder. The store header is a prefix format by design (the bytes after it are ciphertext), so a trailing-bytes refusal does not apply to it.

## The custody model (ADR 0013)

Passphrase-only in v1. The key-derivation function is the library's memory-hard KDF at the **moderate named profile** — a review-dated provisional selected on machine-level evidence; named profiles only, never hand-tuned numbers. The envelope records the profile name, its resolved parameters, and the per-vault salt (not a secret, stored in the clear per standard practice), and opening honours the *recorded* parameters — so future profile changes are versioned migrations, never breaks. Fresh salt on every create and every passphrase change.

The sealed key envelope lives in its own small file beside the records, at a caller-chosen path (vault layout, naming, listing, indexing, and search are deferred to their own reviewed decisions). It travels with backups: it is ciphertext, not the user-held secret, and a restored backup opens only with the passphrase (ADR 0013 decision 5, reasoning recorded there in full).

**There is no recovery path and none may ever be added.** No keyfile in v1, no escrow, no recovery service, no secret questions, no cloud recovery, no hidden path of any kind. Losing the passphrase makes the master unreachable and the vault unrecoverable — not by the user, not by the Wing, not by anyone — exactly as the published key-loss wording (ADR 0012) promises.

## The profile layer (W3-D3)

The profile object model exists (`core/profile.py`): the W1-D3 grammar as pure shapes — inseparable authority/staleness label pairs, bounded unknowns, contradiction and supersession structures, ledger event shapes, and staleness as a pure function over **injected** intervals (no clinical judgment is encoded as a constant anywhere; intervals arrive by their own future reviewed decision). Sealed profile persistence exists (`core/profile_records.py`) for profile items and bounded unknowns, through the store path unchanged.

- **In-payload typing, no format change.** A profile record declares its class and payload version inside the inner record's provenance JSON; the byte-level encoding is untouched and there is **no record format v2**. Imported evidence records remain exactly as published and carry no record class — **evidence-by-absence** is the accepted v1 distinguishability rule, stated here honestly; a future record class would force the format-evolution decision this design deliberately defers.
- **Truth labels do not persist.** The only profile write path refuses confirmed items, because no review path exists and none may be improvised (the minimal-review-posture record). Confirmed shapes exist in memory for grammar completeness and tests only. Loading reconstructs through the object-model constructors, so an illegal persisted state refuses on the way out too.
- **Still absent, by decision:** no review or approval path, no extraction, no model contact. (The transition engine and the durable ledger have since arrived through their own gates — see the transition-layer section below.)

## The transition layer (W3-D4)

The transition catalogue, runnable matrix, and pure validator exist (`core/transitions.py`, M1): all eight W1-D3 transitions are catalogued — understanding, never permission — and a whitelist matrix permits only this era's executable rows, refusing everything else by absence. **T1 (agent extraction under grant) is catalogued but dormant**: any T1-shaped request is refused as unavailable — a distinct status, not illegal — until grant machinery exists by its own future authority. The applier exists (M2): per-transition functions that validate through the classifier first, mutate nothing, build every successor through the object-model constructors, and take no storage, crypto, port, or file arguments.

- **User acts are data, and — within this repository's enforcement — test-tree only.** Gated transitions (T2/T4/T7/T8, the truth-minting and history-writing ones) require a `UserAct`; the suite walks the application tree's syntax and fails on any construction site, no production factory exists, and the shape is not re-exported. T3 (user entry), T5 (staleness decay, one adjacent step per application, authority untouched, injected intervals only — still no defaults), and T6 (contradiction flagging, both sides visibly retained) run without acts because they only enter or lower.
- **Events are emitted by the appliers and kept by the caller-side ledger store** (`core/ledger_store.py`, per the durable-ledger doctrine record): independently sealed append frames under the master key, append-only (prior bytes byte-identical after every append), torn tail refused with intact history preserved (one-event blast radius on this platform's non-atomic appends), whole-ledger erasure as the user's explicit act only. The appliers remain pure and never see the store. v1 keeps the events that exist today; import/custody emission is a named future extension.
- **Truth labels remain unpersistable.** The applier can compute confirmed states in memory during gated synthetic tests; the profile write path refuses them regardless, and no non-test store receives a truth label. No review surface, no approval surface, no extraction, no model contact.
- **T8 performs supersession only** — the old item is retained and relabelled, the successor linked; there is no reactivation, no undo, and no removal of history, per the grammar's terminal-state rule.

## Backup (W3-D6, in progress)

Backup export and restore symmetry exist (`core/backup.py`, M1): one portable ciphertext file in the WBWB shape above — the key envelope rides *reachable* (restore must derive the master from it before anything else can open; it is never trapped inside the payload it unlocks). Restore is file-plus-passphrase into an **empty target only** — no merge, no overwrite — with the five-step validation order (magic/version, envelope unwrap via the published custody path, payload authentication, structural manifest validation, and only then writes). **No health-record plaintext is decrypted in the restore path**; sealed members move verbatim. Member sets are caller-supplied, always — the engine never crawls, guesses, or discovers files. Single-record export-as-right exists (`core/export.py`, M2): the user's own bytes leave byte-identical to how they entered, under no gate but the owner's act — a right, not a transition. Provenance always returns as structured data and is written as a legible sidecar **only when explicitly requested, never silently**; every destination is validated before any write, existing destinations refuse, and profile-class records refuse (their export is a future governed path). The D6 closure (M3) remains ahead under its own gate; whole-vault plaintext export is deferred to its own future record.

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
