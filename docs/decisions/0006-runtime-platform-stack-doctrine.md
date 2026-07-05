# 0006 — Runtime / Platform Stack Doctrine

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing A — lands with ADR 0007) · **Blocks:** the evaluation spike; all future repo code; the conditional early command-line caller
**Decision mode:** doctrine and spike plan now; the stack selection itself is deferred to a final-selection record with spike evidence attached.

## Decision question

What doctrine constrains the Wing's runtime/platform choice, what evaluation spike produces the evidence, and what rules govern the spike itself — with the selection explicitly deferred until the evidence exists?

## Context

The platform is the most inherited decision after the constitution: it determines residue behaviour, telemetry exposure, crypto-binding quality, packaging, and the texture of every future surface. It is also the decision most likely to be made by familiarity rather than fit. ADR 0005 requires a final-selection record grounded in spike evidence; nothing yet makes the spike lawful or defines what it must measure. Per the accepted implementation-shape input, the decision's scope has deliberately narrowed: the engine-first architecture means no app-shell selection is needed now — the shell question is deferred to the review-package phase, decided with a working engine as evidence.

## Decision

**Platform doctrine — binding on any candidate:**

1. **Local-first native execution.** The Wing runs on the user's machine; no server component exists in the first release.
2. **Verifiably telemetry-silent — proven by observation, never by documentation trust.** The spike proves silence by network capture at install, first run, idle, and exit. A stack whose telemetry, crash reporting, or phone-home cannot be provably and completely silenced is disqualified regardless of other merits. Vendor documentation claiming silence is an input to *where to look*, never evidence of silence itself.
3. **No background processes.** The Wing runs when the user runs it: no daemons, no launch agents, no schedulers.
4. **User-initiated updates only.** No auto-update machinery may be inherited from the stack by default.
5. **Accessibility is a first-class scored criterion**, not a later patch — future surfaces inherit whatever the stack makes possible.
6. **Scope of this decision:** runtime + crypto-binding quality + residue behaviour + packaging path. **No app-shell selection** is made by this record or its selection record.

**The spike plan:**

7. **Candidates** are drawn from three classes — a lightweight native-shell class, a local-process class, and a bundled-runtime class — with the concrete candidate list confirmed at spike kickoff by the reviewers (kept out of this record so the landed doctrine names categories, not products).
8. **One identical thin slice per candidate:** create an encrypted store with a candidate crypto binding, import one synthetic file, read it back, terminate — then measure.
9. **Scored criteria, fixed here:** telemetry silence (network capture, per decision 2); residue behaviour (what the stack writes where — ADR 0004 compatibility); crypto-binding quality and memory-handling honesty; footprint and startup; packaging/signing path; accessibility behaviour of the slice; update posture (shippable with all auto-update machinery absent); transitive dependency surface.

**The spike rules:**

10. **Disposable, outside the repo, never committed.** The spike runs in throwaway local workspaces; no spike code, configuration, or output enters version control.
11. **Output hygiene:** spike outputs contain synthetic data only and **no machine-identifying detail beyond OS class — including no hostnames, no usernames, no device names, no serial numbers, no local folder paths, and no screenshot metadata.** Raw logs never leave the workspace.
12. **Spike artifacts never become product artifacts — not by copy, not by paste.** The only lasting public trace of the spike is the **public-safe evidence summary inside the future final-selection record**, written for review, sufficient to justify the choice, and nothing more. No evidence directory, no findings files in the repo, unless a later brief explicitly authorises them.
13. **Governed from minute one:** ADR 0007 (landed with this record) applies to everything the spike produces.

**Deferred to the selection record:** the stack choice; specific crypto library selection and parameters (per ADR 0005); packaging specifics.

## Rationale

Doctrine is decidable from the corpus; the stack is not — binding quality, residue behaviour, and packaging realities are observable facts. Fixing the criteria before the evidence prevents the classic failure (scoring rigged post-hoc around a favourite), and fixing the spike's hygiene rules before it runs prevents the runnable era's first artifacts from being its first leaks. Deferring the shell question shrinks the decision to what the engine actually needs now.

## Options considered

- **(a) Doctrine + criteria + governed spike now; selection later with evidence.** Accepted.
- **(b) Select a stack from architectural prose.** Rejected: premature certainty about observable facts; the exact failure mode this record exists to prevent.
- **(c) Decide the full application shell now.** Rejected: the engine-first shape makes it unnecessary, and a shell chosen without a working engine is chosen on aesthetics.

## Accepted recommendation

Option (a), decisions 1–13; a short final-selection record lands the choice with the evidence summary attached.

## Consequences

One spike cycle before any repo code — deliberate slowness at the highest-leverage decision. The doctrine disqualifies some popular defaults in advance, which is the point. The selection record inherits a fixed scoring table it cannot quietly amend.

## Non-goals

No stack selection; no library installation (a future Tier F event with the engine); no app-shell decision; no CI platform choice; no mobile posture; no hosted anything.

## Implementation gates

The spike may run only after this record and its paired policy are published. No repo code until the final-selection record is accepted. The first dependency installation remains a separately authorised fence-crossing.

## Testing / evaluation requirements

The spike *is* the evaluation; its criteria are fixed above. The selection record must show, item by item, how the chosen stack satisfies doctrine decisions 1–5, with the network-capture result for decision 2 summarised explicitly. Post-selection, telemetry silence becomes a permanent test-class expectation for the engine era.

## Public-safety considerations

The landed record names candidate *classes*, not products; concrete candidates are confirmed at kickoff in review. The evidence summary in the selection record is public-safe by construction: generic wording, synthetic data references only, no environment detail beyond OS class.

## Dependencies

ADR 0004 (residue criteria); ADR 0005 (shared spike, selection-record requirement); the W3 runway; ADR 0007 (paired landing; shared spike-hygiene law).

## What implementation work must not do until this record is accepted

No spike execution; no candidate installation anywhere, including outside the repo; no benchmark scaffolding; no stack decisions embedded in any draft engine design.

## Open questions

1. How many OS targets the spike covers (cost scales with the answer — decided at kickoff).
2. The concrete candidate list (confirmed at kickoff by the reviewers).
3. Whether the encrypted-store format header reserves multi-device fields now (flagged from ADR 0005's open questions; cheap to reserve, costly to retrofit — the spike should report on it).
