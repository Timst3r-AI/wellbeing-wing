# 0012 — Key-Loss Onboarding Wording

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing C — lands with ADR 0011) · **Blocks:** any first-run experience; real-data use

## Decision question

What exact sentence tells a new user that a lost key means a lost vault — and what tone, placement, and follow-through keep that honesty from becoming either fine print or fear theatre?

## Context

ADR 0001 requires the key-loss cost be presented plainly at setup — never buried in technical notes or fine print. A sentence that plain will be under permanent pressure from two directions: softening (to reduce setup abandonment — consent-shaping) and dramatisation (warning styling that reads as danger rather than fact). Both fail the user. This record fixes the sentence, its moment, and its manner.

## Decision

1. **The vetted sentence (decided at review; the Wing's own inability named explicitly):**
   > *"Your vault is locked with a key only you hold. If this key is lost, your vault cannot be opened — not by you, not by the Wing, not by anyone — and there is no reset. Keeping a backup of your key is up to you; we'll show you how."*
2. **Placement: before vault creation, on its own moment, in the same visual register as the rest of first-run.** Not buried in a flow, not a linked document. The user acknowledges it once (a single deliberate action, recorded as a content-free governance event) and is taken directly to the backup offer — consequence and remedy in one motion.
3. **Tone doctrine — plain, not frightening; firm, not theatrical:** ordinary presentation (no alarm styling, no warning icons, no confirmation rituals); active plain-language sentences at an accessible reading level; states fact and agency, never dread. The sentence must pass both failure-direction reviews: no softening, no dramatisation.
4. **Said once, honestly, then trusted.** After the onboarding acknowledgment and the single restatement on backup-skip, the Wing does not re-raise key loss unprompted. The fact is discoverable on demand (vault settings state it verbatim), never pushed.
5. **The wording is a governed string** — it enters the string catalogue when that structure exists; until then this record is its review of record. Changes follow the two-tier rule; any change motivated by setup-completion concerns is definitionally consent-shaping and refused (there are no such metrics anyway — the no-telemetry posture stands).
6. **Localisation carries the doctrine, not just the words** — reading level and tone requirements apply per language; flagged as future scope, first-language-only stated honestly.

## Rationale

The sentence is the architecture's honesty made personal: the entire user-held-key doctrine is real to a user only at this moment. Pairing consequence with agency is what keeps plain from becoming hostile — the user leaves the moment knowing the stakes *and* holding the remedy. The said-once rule respects the capable-adult posture: repetition of warnings is how systems say they don't believe the user heard them.

## Options considered

- **(a) Plain dedicated moment + single acknowledgment + immediate backup offer.** Accepted.
- **(b) Warning-styled confirmation ritual** (type-to-confirm class). Rejected: theatrical; teaches users the Wing performs danger rather than states fact.
- **(c) Inline note within a setup flow.** Rejected: buried-in-flow is fine print with better margins.

## Accepted recommendation

Option (a); the sentence per decision 1 as vetted at review (the doctrine in decisions 2–6 is the record's substance; the sentence is its instance, and its wording is governed because its meaning is its wording).

## Consequences

Some first-run abandonment may occur at the honesty moment — accepted; a user who leaves because the Wing told the truth was saved a worse conversation later. The acknowledgment event anchors the future support posture: the Wing can honestly say the user was told, once, clearly.

## Non-goals

No recovery mechanisms (the no-escrow doctrine stands); no backup mechanics (the paired record); no general first-run design (release-phase scope); no persuasion optimisation of any kind.

## Implementation gates

Accepted before any first-run flow exists; the vetted sentence exists before anything renders it.

## Testing / evaluation requirements

String-source assertion (the moment renders the catalogued string verbatim, once the catalogue exists); acknowledgment-event test (content-free governance entry written); said-once assertion (no other code path raises key-loss messaging unprompted); a stranger-comprehension check at the release phase: does a cold reader correctly answer "who can recover your vault if you lose your key?" — measured with synthetic-persona testing, never analytics.

## Public-safety considerations

The sentence and its moment are public artifacts; no clinical examples anywhere in first-run; capture rules for any illustration follow the standing synthetic-only disciplines.

## Dependencies

ADR 0001 (the named cost, plain-statement requirement); ADR 0011 (paired landing; the remedy the sentence hands off to); ADR 0002 (the language-law posture — honest sentences never softened for acceptance); the no-telemetry posture (no completion metrics exist to optimise against).

## What implementation work must not do until this record is accepted

No first-run flows; no key-loss wording in any tree; no acknowledgment-flow code.

## Open questions

1. Whether the settings restatement uses the identical string or a registered shorter variant — a catalogue decision, flagged.
