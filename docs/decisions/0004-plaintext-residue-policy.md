# 0004 — Plaintext Residue Policy

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (deliverable 1, doctrine pair — lands with ADR 0005) · **Blocks:** all W3 code that decrypts anything

## Decision question

When decrypted content exists inside the user trust boundary (Z1) for a task, what may persist after the task ends — and what must be provably gone?

## Context

ADR 0001 and W1-D1 fix where plaintext may *exist* (Z1, and Z3 under grant). They do not say what happens to the working copies: caches, temp files, log lines, thumbnails, indexes, crash dumps, editor buffers. W1-D5 named residue as D5-T01's remaining risk — the Vault is honest and the swap file is not. This record is the first gate on the W3 critical path because the first line of code that decrypts anything either has this policy or starts accumulating debt against it.

## Decision

1. **Default-deny persistence.** No decrypted C2/C3/C4/CM content persists beyond the end of the task that decrypted it, in any form, in any location. "Task end" means the user-initiated operation completes or is cancelled — not session end, not app close.
2. **Logs are plaintext-free at all times** — not just after task end. No log line, at any level, in any build configuration, ever contains decrypted governed content. Log statements reference IDs, categories, and counts, never contents. This binds debug builds equally: a debug flag is not a grant.
3. **Enumerated forbidden artifact classes:** content caches, search indexes, thumbnails/previews, temp files surviving task end, crash dumps containing content, serialized UI state containing content, analytics of any kind (already barred, restated here because render layers write state).
4. **Exceptions are decision records.** Any future persistent derived artifact (e.g., a local search index) requires its own record with its own encryption story and its own residue tests. There are no policy-level exceptions.
5. **Platform-uncontrollable residue is documented, not denied.** OS-level swap, memory paging, and platform caches may be outside the Wing's control. The policy requires: mitigations applied where the platform offers them (memory locking where available — evidence-dependent); the honest residual documented in the threat model's terms; and no claim, anywhere, that residue control is total.
6. **User-initiated copies are rights, not residue.** The user copying their own content (clipboard, export) is E8/D2 §0.3 territory; the policy governs what the *Wing* leaves behind, never what the user takes.

## Rationale

Storage encryption is meaningless if working copies outlive tasks — the threat model's honeypot concern (§11.8) reconstitutes in the temp directory. Default-deny matches the corpus's structure everywhere else (D1 edges, D2 scopes): the safe state is the default state, and convenience earns its exceptions through review.

## Options considered

- **Bounded content caches with TTL.** Rejected: a TTL cache is residue with a schedule; every cache is an unencrypted-or-separately-keyed copy needing its own custody story.
- **Session-lifetime persistence** (cleared at app close). Rejected: sessions are long; a crash mid-session leaves everything; task-scoped is testable, session-scoped is hopeful.
- **Default-deny with per-record exceptions.** Accepted.

## Accepted recommendation

Default-deny (decision as stated). Doctrine now; the memory-locking and platform-mitigation specifics are **implementation evidence required** — the platform evaluation spike (future runtime/platform stack record, W3-D1 cluster) must report what the candidate platforms actually allow.

## Consequences

Search over Vault content is impossible until someone writes the index decision record — accepted cost, consistent with ADR 0001's "the Vault is evidence, not the working layer." Some UI conveniences (previews, recents) will need content-free forms. Every W3 feature pays a small residue-test tax; that tax is the feature.

## Non-goals

This record does not design encryption (ADR 0005), does not govern Z3 vendor-side retention (OR-2 territory), does not define the index exception it anticipates, and does not cover development artifacts (the future development-artifact policy record).

## Implementation gates

No code that decrypts governed content may be written until this record is accepted. The residue test class (below) must exist in the test tree before the first decrypting feature merges.

## Testing / evaluation requirements

- **Residue test class:** for every decrypting operation — create synthetic content, run the operation, terminate (normally and by kill), then verify no readable governed content exists outside the encrypted stores (filesystem sweep of app-writable locations; log content assertions).
- Log assertions run as standing checks on every build configuration, debug included.
- Crash-path test: induced crash mid-task leaves no content in dumps the Wing controls; platform dump behaviour documented.

## Public-safety considerations

All residue tests use synthetic fixtures (W2-D4 ontology). Test failure output must not print the content it found — it reports location and category only (a residue test that prints residue is a leak with a test badge).

## Dependencies

ADR 0001 (§6 plaintext zones); W1-D1 (Z1); W1-D5 (D5-T01); W2-D4 (fixtures); the W2 deterministic test machinery; the future runtime/platform stack record (platform mitigation evidence).

## What implementation work must not do until this record is accepted

No decryption code, no file-handling code for governed content, no logging framework configuration for the app, no temp-file conventions, no "prototype" that handles even synthetic content outside the test tree.

## Open questions

1. Memory-locking availability and cost per candidate platform (spike evidence).
2. Whether the residue sweep can be made platform-complete or must enumerate app-writable locations per OS (spike evidence).
3. The future index record's shape — anticipated, not designed here.
