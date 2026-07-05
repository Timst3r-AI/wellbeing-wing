# 0007 — Development-Artifact Policy

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing A — lands with ADR 0006) · **Blocks:** the evaluation spike's outputs; all runnable-era development

## Decision question

Once anything in this project runs — beginning with the evaluation spike — what rules govern the artifacts development produces: logs, findings, terminal output, notes, messages, and every text that work creates about the work?

## Context

Through the doctrine era, the project's publication surface was documents the scan could read before commit. The moment anything executes, a new artifact class appears: things *about* the running system that carry fragments *of* it — a pasted log line, a findings note, an observation with a path in it. Each is a publication event the doctrine era never had to price. The first runnable artifact of this project is the evaluation spike itself, so this policy must be law before the spike draws breath — which is why it lands atomically with the spike's own record.

## Decision

1. **Synthetic-only, everywhere, always.** Every development artifact — local debugging included — uses synthetic fixture data only. There is no "just my own data for a quick test" exception: real data used in development manufactures exactly the artifacts this policy exists to prevent, and scrubbing-after is a rejected pathway (there is no identification to remove if none was present).
2. **Paste is publication.** *Headline law:* any log excerpt, output fragment, or artifact content entering an issue, note, message, review, or document is a **new publication event, re-checked at paste time by the person pasting.** The original artifact's cleanliness never transfers to the paste; the paste earns its own.
3. **Effective from the first runnable artifact** — the evaluation spike. This policy governs the spike's outputs from its first minute; nothing runnable predates it.
4. **Spike output hygiene** (shared law with the spike's own record): synthetic data only; **no machine-identifying detail beyond OS class — no hostnames, no usernames, no device names, no serial numbers, no local folder paths, no screenshot metadata**; raw logs never leave the throwaway workspace.
5. **Spike artifacts never become product artifacts — not by copy, not by paste.** The only public trace of spike work is the public-safe evidence summary inside the future final-selection record. Copying spike output into any repo file, draft record, or landed document is a policy violation regardless of how clean the fragment looks.
6. **Commit, review, and issue text** contain no content strings from any store — synthetic included (synthetic content in messages trains reviewers to stop checking). Categories, identifiers, and behaviours only.
7. **Crash and debug artifacts are local files** — plaintext-free with respect to governed content per ADR 0004, inspected before any sharing, shared only by deliberate human action. Never automatic transmission.
8. **Scan-scope extension:** the public-safety scan's documentation gains a scope note covering development surfaces (issue/review templates, captions, filenames) — a tooling-doc touch with no registry impact, per the established tooling boundary.

## Rationale

The realistic leak vector for a governed project is rarely the database; it is the artifact about the database — the paste made at speed, the findings note with a home directory in it. Making the rules effective at the *development* boundary, before habits form, is cheaper than retrofitting after the first awkward paste. The synthetic-only rule is deliberately judgment-free: it is the only version that needs no decision at paste time, and paste time is exactly when judgment fails.

## Options considered

- **(a) Synthetic-only + paste-is-publication + spike hygiene.** Accepted.
- **(b) Trust-based artifact review** (developers judge each artifact at sharing time). Rejected: judgment under deadline is the failure mode, not the control.
- **(c) Real-data debugging locally, scrubbed at sharing.** Rejected: scrubbing is a de-identification pathway, already rejected twice in this corpus for fixtures and captures; the same logic binds here.

## Accepted recommendation

Option (a), decisions 1–8.

## Consequences

Debugging anything real (post-release, far future) requires a reproduce-with-synthetic-fixtures discipline — harder, and correct; that discipline gets designed with support processes in a later era, not improvised. Spike findings take slightly longer to write (generic wording, no paths) — that cost is the control working.

## Non-goals

No demo-mode or watermark design (review-package era); no release-material rules (release era); no screenshot mechanics beyond the synthetic-only rule (no surfaces exist yet); no runtime logging design (ADR 0004 owns runtime behaviour; this policy owns what development *does with* artifacts).

## Implementation gates

Accepted before the spike runs — enforced by the atomic pairing. The scan's dev-surface scope note lands with or promptly after this record, as a tooling-doc change.

## Testing / evaluation requirements

Review-enforced in this era (the checklist gains the paste-time re-check as a standing review item); the scan's extended patterns cover committed development surfaces once the scope note lands; no suite changes now — future engine-era additions arrive with their own records.

## Public-safety considerations

This record is itself a public-safety control; its examples are deliberately abstract, naming artifact classes rather than incidents. Everything it governs inherits the repo's standing wording rules.

## Dependencies

ADR 0004 (plaintext-free log rule, extended here to artifact handling); ADR 0006 (paired landing; shared spike-hygiene law); W2-D4 (synthetic fixture ontology); W2-D6 (scan, scope-note mechanics).

## What implementation work must not do until this record is accepted

No spike execution (jointly gated with the paired record); no development artifact sharing of any kind from any runnable work; no issue/review template creation for the runnable era.

## Open questions

1. Whether the scan's dev-surface patterns land with this record's landing or at the first moment a dev-surface template actually exists — reviewers' call; the scope note itself costs one tooling-doc paragraph either way.
