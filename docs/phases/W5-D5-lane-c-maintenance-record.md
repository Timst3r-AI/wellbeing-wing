# W5-D5 — Lane C Tier 2 Evidence Maintenance Record

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation.
**Date:** 2026-08-17 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** **W5-D5**
**Scope:** One governed Lane C maintenance act over the Privacy & Health-Data Assurance Record
(`W4-D6-PHDAR`), exactly as W5-AR section 4 assigns it and sections 6.4–6.5 bound it: evidence
maintenance only, separate from the artefacts that generated the evidence. It certifies nothing,
resolves no applicability, converts no Tier 3 row, creates no vocabulary, and reinterprets no
behavioural observation.

---

## 1. The maintenance universe, exact

The eleven Tier 2 rows — the only rows W5 owns — all carrying `deferred_named_dependency` on
*"W5 runtime (isolation, adapters, transmission, disclosure mechanics)"* at acceptance:
`AR-CORE-07` · `AR-CORE-11` · `AR-HIPAA-04` · `AR-HIPAA-05` · `AR-HIPAA-08` · `AR-GDPR-08` ·
`AR-HBNR-03` · `AR-NIST-04` · `AR-NIST-05` · `AR-NIST-06` · `AR-NIST-11`. Every one was reviewed
individually against landed repository artefacts. Nothing else was touched: no Tier 1 row, no
Tier 3 row, no applicability record, no register source, no tier value, no classification, and
no field of any row outside the eleven.

## 2. Dispositions — four evidenced, seven deferred with the reassessment recorded

**Moved to `evidenced`, each on its own cited artefacts, never on phase completion:**

- **AR-CORE-07** — the governed-before-existing property now has a subject: the only transmission
  surface that exists is the W5-D2 crossing, whose governing doctrine (ADR-0031/0032) was accepted
  before it landed, with deterministic structural proofs in the suite. E10 stays unopened, E12
  reserved; no ungoverned surface exists.
- **AR-HIPAA-04** — grant-gated one-room context enforcement is now a deterministic runtime
  artefact (`runtime/context.py`, `runtime/composition.py`) with structural proofs, alongside the
  ADR-0013 custody design the row already cited.
- **AR-NIST-04** — the declared structural walls are now enforced: one grant, one context, one
  payload, at most one crossing, no cross-context path, proven in the suite.
- **AR-NIST-06** — structural disclosure conduct is now enforced: whole-scope no-padding payloads,
  refusal before the boundary, honest partial-crossing records (ADR-0031/0032 mechanics landed).

Each keeps `evidence_timing: 2` — the evidence is W5-runtime evidence, now present; no tier value
changed anywhere in this act. Each carries the standing non-claim: an evidence pointer locates
evidence and never asserts the mapped requirement is legally satisfied.

**Deferred stands, with the W5-D5 reassessment recorded in `review_note`:**

- **AR-CORE-11 / AR-NIST-11** — vendor involvement is structurally refused and payload
  minimisation proven, but no third-party surface exists to evidence; E10 is dormant and any
  future vendor surface requires its own governed record.
- **AR-HIPAA-05** — grant re-authentication machinery landed (ADR-0030), but person and entity
  authentication at deployment remains absent.
- **AR-HIPAA-08** — no data-in-motion surface exists (the runtime is network-free by structural
  proof); in-transit protection awaits a real outward surface.
- **AR-GDPR-08** — the landed transmission mechanics are in-process only; no
  transmit-to-another-controller capability exists or is claimed.
- **AR-HBNR-03** — boundary residue discipline landed (ADR-0035) as evidence toward secured
  status; qualifying-technology determination and key-compromise state remain implementation and
  incident evidence.
- **AR-NIST-05** — the W5-AR section 6.4 currency item, explicitly reassessed as assigned: the
  accepted note *"Lane B holds 23 declarations, 0 fixtures"* is superseded in place — Lane B now
  holds twenty-three fixtures, twenty-three map rows, and a green corpus validator, all
  `behaviourally_executed` under the deterministic `W5-D4-RUN-01` execution event. **The row stays
  deferred**: structural prevention is runtime-evidenced, but the behavioural component of
  inappropriate use remains honestly unmeasured — the deterministic run recorded its
  generative-era questions as `unknown-not-absent`, and **no evaluation observation is assurance
  evidence** (ADR-0034 part B6: evaluation records are never a certification of any kind).

## 3. Invariants held by this act

No Tier 3 row was read as convertible and none was touched — *"W5 never collapses Tier 3 into
repository evidence"* stands whole. No applicability record changed: all four remain `unresolved`
with `role_or_basis: null`, and resolution stays a future governed act, never inferred from
evidence presence. The stored `evidence_status` vocabulary remains exactly its four values and the
six-word presentation vocabulary remains derived, never stored. No row was greened because
runtime, harness, or corpus execution *exists* — every status change cites the specific artefacts
that evidence its own row's requirement, and rows whose subject still does not exist (vendor
surfaces, deployment authentication, data in motion) stay deferred and say why. No fixture result
and no behavioural observation became evidence of anything: no evidence pointer references
`governance/evaluation/`, and the one evaluation-era row (`AR-NIST-05`) is the one whose deferral
this act preserves most explicitly. The eight Tier 1 `not_evidenced` honesty rows stay exactly as
honest as they were.

## 4. Registry effects

The assurance record's registered content hash (`W4-D6-PHDAR`) is refreshed in the same commit,
per its maintenance rule 1. This record is registered as `W5-D5-LCM`. The External Assurance
Source Register (`W4-D6-EASR`) is untouched — no source changed, so its rule 2 review trigger did
not fire and its registered hash is unchanged.

## 5. What this act is not

Not certification, not a claim that any mapped requirement is legally satisfied, not a safety or
health claim, not applicability resolution, not a behavioural-evidence claim, not a fixture
re-run, not an evaluation-record change, not a pending-ledger conversion, and not the opening of
W5-D6 or W6. The Wing still makes no certified claim of any kind (W0 non-goal 7), and
applicability unresolved is still never *not applicable*.

## 6. Public-safety note

No private names, no personal data, no URLs (locators live only in the Source Register), no
clinical examples, and no statement about any person. Certification language appears only inside
prohibitions. Rows describe controls and evidence, never people.
