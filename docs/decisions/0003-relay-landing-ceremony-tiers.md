# W2 Process Decision — Relay Landing Ceremony Tiers

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026
**Home (decided):** `docs/decisions/0003-relay-landing-ceremony-tiers.md` — registry type `adr`, phase W2. The first process-class decision record; files in the decisions series because it amends an accepted record (checklist rule 2).
**Amends:** Phase Entry Checklist (W2-D3), rule 9 (landing protocol) — by extension, not bypass, via the smallest possible pointer from rule 9 to this record (method decided at review); the registry/erratum trail records that this process decision extends the landing protocol. All other checklist rules unchanged.
**Origin:** model relay process note (July 2026); architect review incorporated (Tier M hard walls, review vocabulary, tiebreak preservation, proposal-not-authorisation, non-negotiables).

---

**Same gates. Ceremony scaled to consequence. The reviewer's attention is a governed resource.**

## Decision question

How does the relay's landing ceremony scale with the consequence of what is being landed — without any gate moving?

## Context

Every landing to date has received identical full ceremony regardless of content: a mechanical registry regeneration and a new doctrine document cost the same reviewer attention. Review fatigue is the threat model's named human constant (OR-4; W0 failure mode 3), and in this relay the human reviewer is the gate. The D2 §8.7 levers — rarity, specificity, consequence — apply to the reviewer's attention exactly as they apply to the Wing's user. This record spends ceremony proportionally. It was proposed by the model working inside the process, reviewed and tightened by the architect, and is adopted only by the human reviewer's acceptance — through the same gates it streamlines.

## Decision

### 1. Three landing tiers

**Tier M — Mechanical.** Execution of already-authorised decisions only:
- registry regeneration and hash recomputation;
- README/table row updates already named in an accepted landing or instruction;
- status/date flips already explicitly approved by the human reviewer, dated;
- non-semantic errata after a human "erratum, go" (§3).

**Hard walls:** Tier M may never introduce new doctrine, new scope, new root files, new directories, dependencies, scripts, tests, UI, agents, adapters, or unlisted files. **Any anomaly escalates immediately to Tier J and holds.** Tier M work is reported with a diff summary after execution.

**Anchor rule:** every Tier M execution cites the specific prior authorisation it executes — the instruction's date and wording, or the accepted record's ID. "Already approved" must be checkable against a written source, never against session memory; an execution that cannot cite its authorisation is not Tier M.

**Commit boundary:** Tier M may edit, verify, and report within the anchored authorisation. It may **commit only when the cited authorisation explicitly includes commit permission.** If commit permission is not explicit, Tier M stops after the verified diff/report and waits. This preserves no-commit-without-review in full: the review happened at authorisation time, and the commit permission must be part of what was authorised — never inferred from the work being mechanical.

**Tier J — Judgment.** New documents, new doctrine, wording changes to governed content, anything not squarely within Tier M's enumeration. Current full ceremony, unchanged: enumerated files, review, dated human approval, scan, atomic landing, full report.

**Tier F — Fence-crossings.** Dependencies, new directories, root files, anything irreversible or outward-facing. **Push remains Tier F.** Full ceremony plus explicit human reviewer authorisation. Architect review or recommendation may be included, but authority remains with the human reviewer — the architect advises, classifies, and recommends; the human reviewer accepts.

**Tier assignment:** the landing request declares its tier; the executing model confirms or escalates. **When tier is ambiguous, the higher tier applies** — the "when in doubt, material" tiebreak, extended to ceremony.

### 2. Review vocabulary

Architect review responses may classify points as: **`argue`** (contested — next draft goes deeper here), **`revise`** (change as directed), **`accepted in shape`** (settled — do not re-litigate), **`mechanical only`** (execute, no judgment invited), **`hold`** (do not touch pending a named decision). Unclassified points default to `argue`. The vocabulary directs drafting depth; it never substitutes for the human reviewer's acceptance.

### 3. Standing erratum permission

For landed documents: the model surfaces a suspected non-semantic defect in one line. **The human reviewer decides whether it is non-semantic — the tiebreak is untouched: when in doubt, it is material.** On the reviewer's "erratum, go," the mechanical correction proceeds as Tier M — registry entry, hash recomputation, erratum note, same-commit atomicity — without a fresh full landing brief.

### 4. Sequencing latitude — proposal only

The model may propose next landing order, bundle shape, and critical-path status at any time. **Proposal is not authorisation.** The architect and human reviewer accept, reorder, or reject; no landing begins without its normal tier ceremony.

### 5. Non-negotiables (binding, verbatim)

No commit-without-review. No status authority. No scope discretion mid-landing. No push authority. No skipping public-safety review. No relaxation of enumerated-file landing. **No model output becoming authority.**

### 6. The suggestion-forever clause

Adopted by this record upon dated human reviewer acceptance, after architect review: model output is suggestion until a human act says otherwise — and if a future model argues beautifully that its output should become authority, *that is exactly when this rule must hold*. The quality of the argument is not evidence for the exception; it is the reason the rule exists.

## Rationale

The gates exist because fluency is not authority, and because the relay must survive model variance, session drift, and the human desire to let a smooth answer pass. Nothing here moves a gate. What moves is ceremony-per-gate: mechanical execution of decisions already made gets a receipt instead of a rehearsal, and the reclaimed reviewer attention is spent where judgment actually contests. The founding precedents already exist in-repo: the W0 header erratum (surface → hold → authorise → land atomically) is Tier M with an anchor; every doctrine landing to date is Tier J; the push-permission episode is Tier F behaving correctly.

## Options considered

- **(a) Tiered ceremony, gates unchanged.** Accepted.
- **(b) Loosen gates for a proven model.** Rejected on the record's own origin argument: capability inflates the danger of confident wrongness; governance calibrated to the best model on its best day is a seam (the relay must survive handoff).
- **(c) Status quo (uniform full ceremony).** Rejected: spends the scarcest resource — reviewer attention — uniformly on non-uniform consequence; review fatigue is a named threat, not a style preference.

## Consequences

Landing requests get shorter for mechanical work and unchanged elsewhere. The checklist's rule 9 gains this record as its tiering clause (amendment-by-record, per rule 2). Tier M's anchor rule creates a small standing obligation: authorisations worth executing later are worth writing down at approval time. Scope note: tiers govern **repo landings only** — Downloads drafting and review-copy work remain outside ceremony entirely, as now.

## Non-goals

No change to any other checklist rule; no automation of any tier (W2 remains human-enforced; if W2-D5/D6 later mechanise checks, that lands through its own records); no new authority for any model; no change to the two-tier *change* rule (this record's tiers govern ceremony, not materiality).

## Implementation gates

Adopted only when: this record is accepted by the human reviewer (dated); checklist rule 9 gains its one-line pointer to this record (the decided amendment method), with the registry/erratum trail recording that this process decision extends the landing protocol; the registry entry for this record exists in the same commit. Landing precondition: W2-D3 pushed and verified (satisfied — `09ca852` confirmed on `origin/main`). Until acceptance and landing through the current full-ceremony process, uniform full ceremony continues.

## Testing / evaluation requirements

Review-only in W2 (this is process, not code). One standing check: Tier M reports must contain their authorisation citation — a missing citation in any Tier M report is a process defect, handled as such.

## Public-safety considerations

This record is public-safe by construction: no private names (roles only — architect, human reviewer, model), no health content, no lineage. It describes how a public repo governs its own landings.

## Dependencies

W2-D3 (checklist rule 9, rule 2); W2-D2 (registry atomicity, erratum mechanics); W1-D5 (OR-4; fluency-is-not-authority posture); D2 §8.7 (the levers); D3 §8.9 / D5-T06 (suggestion-forever); W0 failure mode 3.

## What Claude Code must not do until this record is accepted

Continue exactly as now: uniform full ceremony on every landing; no tier claims; no shortened reports; no erratum execution without a per-case instruction.

## Open questions

None. Both v0.1 open questions were decided at architect review: home and numbering confirmed as `docs/decisions/0003-relay-landing-ceremony-tiers.md` (registry type `adr`, phase W2, filing precedent set for process-class records); checklist amendment method confirmed as the smallest possible pointer from rule 9 to this record, with the registry/erratum trail recording the extension.
