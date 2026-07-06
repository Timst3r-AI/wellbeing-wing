# The Wellbeing Wing — Concept Overview

## 1. What the Wellbeing Wing is

The Wellbeing Wing is a privacy-first, local, personal wellbeing archive — and the governed engine that will one day serve it. It is a place where a person can keep their own health-related documents, encrypted under a key only they hold, before anyone or anything interprets them.

It is honest about what it is right now: **a governance corpus and an engine spine, not a finished app.** There is no interface to click, no assistant to talk to, and no service to sign up for. What exists is the foundation — built deliberately, reviewed before every step, and published so the work can be inspected, questioned, and adopted by others.

The Wing is *not* a medical, therapeutic, diagnostic, safety-intervention, or crisis-response product, and it is not an AI companion. It stores what you give it and gives it back. Everything beyond that — interpretation, review, sharing — is future work that must pass through its own governance before it may exist.

## 2. What exists today

The project has closed five chapters, each sealed by a reviewed record:

- **W0 — [a constitution](constitution/W0-wellbeing-wing-constitution.md)**: the laws the project must obey, written before any design.
- **W1 — the governance architecture**: data boundaries, consent and scope, authority and staleness, safety surfacing, a threat model — designed before any schema.
- **W2 — enforcement machinery**: [a registry](governance/registry.md) that indexes every governing document by content hash, a public-safety scan, synthetic test fixtures, and a deterministic test suite. The corpus checks itself.
- **W3-D1 — the engine doctrine**: nine reviewed decision records covering plaintext residue, encryption, platform selection, development artifacts, the import boundary, review posture, backup guidance, and the exact wording a person deserves about key loss.
- **W3-D2 — the engine spine**: the first product code, closed and sealed. In it:
  - **A store exists.** Content is sealed with authenticated encryption under a caller-supplied key, in a versioned format that refuses what it does not recognise.
  - **An import path exists.** Files enter as bytes plus the provenance the *user* writes — source, date, an optional note. The engine verifies only that a file has the shape it claims (a PDF looks like a PDF) and refuses to look deeper.
  - **Key custody exists.** A vault belongs to one person through a passphrase. The passphrase-derived key seals a random master key inside a small versioned envelope; changing the passphrase re-seals the envelope and touches no records. There is no reset, no recovery service, and no back door — by decision, permanently.
  - **A residue-at-scale proof exists.** Tests populate a realistic synthetic vault and verify that plaintext markers are not written to disk during the tested engine operations — at every step, and even when the process is killed mid-work.
  - **A format-seam confirmation exists.** The three versioned formats refuse each other's bytes and refuse ambiguity; nothing is silently accepted.
  - **[Engine documentation exists](../engine/README.md)**, carrying the honest limits in ink (see §4).

Everything above is held by a deterministic test suite and a public-safety scan that run on every change. The repository remains **headless**: an engine and its tests, nothing user-facing.

## 3. What it deliberately does not do yet

The next deliverable, W3-D3 — the profile model — **has not started.** Today there is:

- no profile model (no draft profiles, no approved profiles, no review of any kind)
- no user interface and no command-line tool
- no model contact of any kind — no AI reads, summarises, or organises anything
- no sync and no hosted mode — the published engine is local and headless
- no backup or export mechanics yet (the doctrine for them is written; the machinery is not)
- no recovery service — see custody, above
- no licence decision yet: the project intends broad adoptability, and the licence question is an open, deliberate decision rather than a default

None of these are missing by accident. Each waits behind its own reviewed decision, because in this project capability follows governance — never the other way around.

## 4. The privacy and custody posture

- **Local first.** The vault lives on the user's own machine, encrypted at the boundary before any storage.
- **A key only you hold.** Custody is a passphrase in v1. If the passphrase is lost, the vault cannot be opened — not by you, not by the Wing, not by anyone — and there is no reset. The project treats saying this plainly as a duty, not a disclaimer.
- **Ciphertext travels, keys never.** Backups, when the machinery exists, will be copies of encrypted records plus the sealed key envelope — restorable anywhere, but only with the passphrase.
- **Honest limits, in ink.** The engine's documentation names what cannot be promised: the runtime cannot guarantee that key material is zeroed from memory; the number and rough size of records is observable on disk even though their content is not; a strong derivation function cannot make a weak passphrase strong. These are documented and carried forward — never euphemised.

## 5. Evidence before meaning

The Wing's central idea is a strict ordering: **evidence is not automatically meaning.**

- **Import is not interpretation.** The engine never reads what it stores — no text extraction, no classification, no auto-dating, no thumbnails, no language detection. This is enforced structurally: the import path cannot parse what it cannot import, and a test fails if that changes.
- **Reading is not remembering, and retrieval is not memory.** Opening a record later does not make its contents part of anything's working knowledge. Nothing accumulates understanding behind the user's back.
- **A stored document carries no authority.** It is evidence, maximally protected and wholly uninterpreted, until a future, separately governed process — with the user's explicit review — turns any of it into working meaning. That process is the profile model, and it does not exist yet.

## 6. What W3-D2 completed

W3-D2 was the project's first product chapter: five landings, each preceded by its reviewed decision, closed by [a registered record](phases/W3-D2-closure-record.md) that cites every publication by commit so anyone can verify the chain. The store, the import path, key custody, the at-scale residue proof, and the format confirmations — all of it landed without touching a single governance document, which is itself the boundary working as designed.

## 7. What remains future work

In outline, and only through their own future gates: the profile model (W3-D3) — where evidence can become reviewed, user-approved working context; backup and export mechanics; first-run and passphrase surfaces, including the honest wording about passphrase strength; a first caller for the engine; and, further out, the room-contract, adapter, and review-surface layers that would let other systems interact with the Wing under explicit grants. No dates, no promises — each arrives when its governance does, or not at all.

## 8. Public-safety boundaries

This repository contains no real health data and never will: all test content is synthetic, built from grammar placeholders that correspond to no real person. It offers no medical advice, no diagnosis, no treatment, no crisis response, and no therapeutic service, and nothing in it should be read as any of those. It is not a companion and has no persona. A public-safety scan runs against every change to keep these boundaries mechanical, not aspirational.

## 9. Why this matters

Health records are among the most sensitive things a person owns, and the tools that hold them usually ask for trust upfront and prove it never. The Wing runs the experiment in the other order: write the laws first, build the enforcement second, and only then build the thing — in public, in small reviewed steps, with the limits stated as plainly as the features. If the experiment works, the result is not just an archive; it is a pattern any system, including AI systems, could adopt for holding what matters without quietly deciding what it means.

---

*Everything here describes the published state of the repository at the close of W3-D2. Nothing in this document authorises implementation, and where this overview and a governing record disagree, the record wins.*
