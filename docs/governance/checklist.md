# Phase Entry Checklist

**Status:** Accepted by human reviewer, 2026-07-05
**Phase:** W2 — Governance Evaluation & Enforcement Foundations (deliverable 3)
**Classification:** Docs-only / governance checklist. This document creates no code, automation, or tooling; its rules are human-enforced in W2 (approved decision: no automation yet).
**Governed by:** W2 Alignment Report (§5 W2-D3); W2-D1 (W1 Closure Record); W2-D2 (registry atomicity); the accepted W1 corpus

---

**The rules the repo already lives by, written down where they can be pointed at.**

Every landing so far has obeyed the same protocol: brief → review → human approval → enumerated landing → status flip by reviewer → scan → commit. This checklist makes that protocol explicit and bindable, so that future landings — by any model, any session, any contributor — are checked against a written standard instead of a remembered one.

## The ten rules

### 1. Status authority rule

Status flips (`Draft` → `Accepted`, and any other status change) are made only on the human reviewer's explicit instruction, dated. No model, script, or architect flips a status.

### 2. Two-tier change rule for accepted records

Material or semantic changes require a decision record — never an edit. Non-semantic corrections (typo, formatting, link, a header lagging a sealed acceptance) require a logged erratum in the affected document's registry entry, in the same commit as the correction. Whether a change is semantic is itself a reviewer judgment: **when in doubt, it is material** — and the doubt judgment belongs to the human reviewer.

### 3. Registry atomicity rule

A commit that changes a governance document but not its registry entry (or vice versa) is a defective commit. Document change, registry entry, and hash recomputation move together. Human-enforced until the W2-D5 consistency check mechanises it.

### 4. Directory and root-file fence

No implementation directories until a phase document explicitly authorises them, by name. The authorised set is exactly:

- **Now:** `docs/`, `governance/`
- **Upon their deliverables landing:** `fixtures/` (W2-D4 Stage B), `scripts/` (W2-D6), `tests/` (W2-D5)

Anything else appearing in the tree is a checklist violation regardless of content. **Root files are inside the fence too:** edits to root files (`README.md`, `.gitignore`, or any new root file) are allowed only when an accepted landing brief names the exact root file and its purpose; otherwise a new or modified root file is treated as a fence crossing, exactly as an unauthorised directory would be.

### 5. Dependency fence

Any new dependency manifest or package is a named fence-crossing requiring explicit human approval before it exists in a commit. Zero-dependency alternatives must be stated alongside any crossing request.

### 6. Public-safety rule

Every commit is checked against the public-safety scan — by human review until W2-D6 lands, by script **plus** review after. The script supplements human review; it never replaces it. No private names, no private system references, no companion framing, no personal health details, no project lineage beyond this repository, no real health data — in any file, any commit, ever.

*The scripted layer exists as of W2-D6 (2026-07-05): [`scripts/public-safety-scan.py`](../../scripts/public-safety-scan.py), documented in [`scripts/README.md`](../../scripts/README.md). Script plus human review applies from that date.*

### 7. Definition fences carried from the threat model

Anything that contacts the user outside an active session is the notification layer, whatever it is called (D5-T16) — and no notification layer exists or may be built without its own decision record, from zero inheritance. Any feature touching the Z1 trust boundary requires a constitutional check in its decision record (D5-T18).

### 8. Phase entry gate

A new phase's first deliverable may land only when all three exist and are accepted:

1. the prior phase's closure record;
2. the new phase's runway / alignment report;
3. the deliverable's own brief.

Three documents, three acceptances, no exceptions.

### 9. Landing protocol

Every landing task enumerates its files in advance. Files not on the list are not created or modified. **Discovering a needed file mid-landing is a review question, not an improvisation** — the landing pauses on that point, the reviewer decides, and the decision is recorded (the W0 header erratum during the W2-D2 landing is the founding precedent: discovered, surfaced, held for authorisation, then landed atomically).

*Landing ceremony tiers are defined in [ADR 0003](../decisions/0003-relay-landing-ceremony-tiers.md), which extends this rule (accepted 2026-07-05).*

### 10. Errata location

Errata live in the affected document's registry entry (`errata` field), summarised in the registry index's errata section. There is no separate errata ledger — one home, no drift.

## Closure criteria

W2-D3 closes when:

1. This checklist exists, is accepted by the human reviewer, and is registered (entry `W2-D3`).
2. **The checklist's own landing follows the checklist**, as far as the checklist is applicable at that moment: enumerated files, status by human approval, public-safety scan, registry atomicity. D3's closure depends on nothing that has not happened yet.
3. Public-safety scan clean; no code, automation, or dependencies created.

The W2 runway's "applied to at least one real commit cycle" criterion belongs to **W2 phase closure**, not to D3's own closure: the W2 closure record may cite a subsequent landing as additional evidence the checklist worked in practice, but D3's accepted status never depends on a future deliverable.

## Public-safety requirements

This checklist and every landing it governs obey rule 6 in full. The checklist itself describes repo process only — it contains no examples drawn from health data (real or synthetic) and no private context. Where landing reports quote file content for verification, grammar placeholders are the only permitted example register.

## Standing note

This checklist collects and operationalises rules that already exist in accepted documents; it creates no new doctrine. If a future landing seems to need a rule this checklist lacks, that is a signal a decision record is missing — the checklist is amended only downstream of one, per rule 2.
