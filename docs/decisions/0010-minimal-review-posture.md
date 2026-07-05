# 0010 — Minimal Review Posture

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing B — lands with ADR 0009) · **Blocks:** the W3-D4 engine milestone (transition engine); fences the temporary-review-surface drift

## Decision question

Between the engine existing (W3) and real review surfaces existing (the review-package phase), how do the user-review transitions (D3-T2, D3-T4) occur — simulated in tests only, or via a minimal temporary review mechanism?

## Context

The transition engine is a W3 milestone, and its most important transitions require user review acts. The review-package phase owns real review surfaces, built against prerequisite records (string catalogue, fatigue standard, legibility). The gap between engine and surfaces must be filled by something — and what fills it determines whether the surface standards arrive intact or pre-empted. The accepted implementation-shape input sharpened the boundary: **a review command is a review surface** — terminals included.

## Decision

1. **Tests simulate; nothing real becomes Approved until real review surfaces exist.** The transition engine's user-act gate is exercised in tests via explicitly-marked test doubles operating only on synthetic fixtures. No mechanism exists in W3 by which any real person approves any real content into any real approved profile.
2. **Test doubles are structurally unreachable:** the simulated-review path exists only in the test tree, is unreachable from application code, and its use outside tests is a mechanically-detectable defect (a repo-state assertion lands with the engine: the application tree contains no caller of the simulation).
3. **The archive is useful without approvals.** Rights operations never wait for review machinery. Per the reviewers' cluster decision, the early caller may support **rights-operation categories** — evidence intake/import, status and provenance inspection, export, and backup — and **must explicitly exclude review/approve transitions.** Categories, not command names: the engine brief owns the verbs.
4. **A belt to the braces:** a standing assertion that no Approved-status item exists in any non-test store, from the engine's first milestone onward.
5. **Reversal requires a new decision record.** If mid-build pressure arises to add "just a simple approve step," that is a proposal to reverse this record — reviewed as such, never landed as a commit.

## Rationale

A "temporary" review mechanism would be built without the queue rules, the string catalogue, the fatigue standard, and the legibility treatment — that is, without everything that makes review *review* rather than a yes-button. Temporary mechanisms become permanent under delivery pressure precisely because they exist. The inconvenience of waiting is the fence. Meanwhile the grammar was designed so *user-reported* content is usable in room scope without profile authority — the archive's value does not depend on approvals existing.

## Options considered

- **(a) Tests simulate; real review waits for the review-package phase.** Accepted.
- **(b) Minimal governed command-line review mechanism now.** Rejected: every surface prerequisite would be violated or improvised; W0 §7's section-by-section, high-stakes-individual requirements cannot be shortcut, in any medium.
- **(c) Minimal mechanism restricted to synthetic personas.** Rejected: builds the code path and muscle memory of (b) while claiming the restraint of (a); the restriction would live one configuration flag from failure.

## Accepted recommendation

Option (a), with decision 2's structural enforcement and decision 3's rights-categories enumeration.

## Consequences

Approved-profile-dependent behaviour waits for the review-package phase — accepted; the first real review experience arrives inside the reviewed design. The early archive story (import, organise, export, back up) stands on rights alone, which matches the product's stated identity.

## Non-goals

Does not design review surfaces; does not modify the D3 grammar (this record chooses among implementation postures the grammar permits); does not enumerate CLI verbs (engine brief); does not decide the eventual review-surface medium.

## Implementation gates

The engine brief must reflect this scope (no review mechanism in any engine milestone). The no-caller assertion and the no-Approved-items assertion land with the engine's test extension, before the transition engine merges.

## Testing / evaluation requirements

Transition tests exercise every legal and illegal path via marked doubles against synthetic fixtures; the no-caller structural assertion (decision 2); the no-Approved-items standing assertion (decision 4).

## Public-safety considerations

Simulated review acts appear only in test fixtures and outputs governed by the synthetic-only rules; no other exposure.

## Dependencies

D3 §4 (T2/T4); W0 §7; the W3 runway (D4 framing); the implementation-shape input (review-command-is-a-surface boundary); ADR 0007 (artifact law over test outputs); the reviewers' cluster decisions (rights categories; explicit exclusion of review transitions).

## What implementation work must not do until this record is accepted

No engine milestone scoping that assumes a review path; no review-mechanism code in any tree; no transition-engine design that lacks the user-act gate.

## Open questions

None. This record is deliberately closed-form: one question, both alternatives fully argued, reversal path named.
