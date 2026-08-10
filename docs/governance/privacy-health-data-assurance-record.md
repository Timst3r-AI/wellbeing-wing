# Privacy & Health-Data Assurance Record

**Status:** Accepted by human reviewer, 2026-08-10. Not a build instruction. Authorises no implementation.
**Date:** 2026-08-10 · **Phase:** W4 — Room Contracts (deliverable W4-D6, Lane C)
**Scope:** Documentation only. This record maps the Wing's privacy and health-data assurance
controls to repository evidence, consuming the External Assurance Source Register (`W4-D6-EASR`)
as its sole external-source authority. It certifies nothing, resolves no applicability, and
creates no data category, edge, class, authority state, permission, or implementation.

---

## 1. Governing boundary

**This record maps controls to evidence. It is not compliance certification, and nothing in it may be
presented as one.** The Wing makes no certified-compliance claim (W0 §2 non-goal 7); absence of
evidence is never evidence of compliance; **applicability unresolved is never not applicable**; and
interpretation remains review-only, never mechanical. The published Source Register governs the
provenance and currency of every external source cited here — it does not decide applicability or
legal status, and neither does this record.

## 2. Architecture carried

Thirteen stable primitives (P1–P13). Four regulatory/alignment overlays — HIPAA-aligned, APP-aligned
(active set APP 3/6/11/12/13), GDPR-style, FTC HBNR — each with an applicability record; one
voluntary engineering baseline (NIST SP 800-122) with **no statutory applicability axis**. Stored
`evidence_status` has exactly four values; stored `applicability_status` exactly three, on overlay
records only; the six-word assurance vocabulary is **derived at presentation, never stored**.
Timing tiers: 1 = repository/doctrine evidence now; 2 = W5-dependent runtime evidence; 3 = external
organisational/deployment evidence. **W5 never collapses Tier 3 into repository evidence.**
Row identifiers `AR-<FAMILY|CORE>-<NN>` follow the register's allocation-identifier semantics:
stable allocation order, immutable once accepted, never a ranking.

## 3. Applicability records

```json
[
 {
  "applicability_id": "APR-HIPAA",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "current_applicability_status": "unresolved",
  "role_or_basis": null,
  "deciding_facts": "operator identity; covered-entity or business-associate relationship; electronic covered transactions",
  "decided_by": "review-only",
  "profile_dependency": "deployment profile (absent)"
 },
 {
  "applicability_id": "APR-APP",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "current_applicability_status": "unresolved",
  "role_or_basis": null,
  "deciding_facts": "whether a deployed operator is an APP entity; annual-turnover and activity tests; jurisdictional nexus",
  "decided_by": "review-only",
  "profile_dependency": "deployment profile (absent)"
 },
 {
  "applicability_id": "APR-GDPR",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "current_applicability_status": "unresolved",
  "role_or_basis": null,
  "deciding_facts": "controller or processor role; establishment or targeting within territorial scope",
  "decided_by": "review-only",
  "profile_dependency": "deployment profile (absent)"
 },
 {
  "applicability_id": "APR-HBNR",
  "framework": "FTC-HBNR",
  "framework_kind": "alignment_overlay",
  "current_applicability_status": "unresolved",
  "role_or_basis": null,
  "deciding_facts": "vendor-of-personal-health-records status; technical capacity to draw identifiable health information from multiple sources; non-coverage by HIPAA",
  "decided_by": "review-only",
  "profile_dependency": "deployment profile (absent)"
 }
]
```

**All four overlays: `current_applicability_status = unresolved`, `role_or_basis = null`.** Nothing
in this record narrows that; deciding facts await a deployment profile that does not exist.

## 4. Assurance rows

```json
[
 {
  "row_id": "AR-CORE-01",
  "primitive": "P1",
  "framework": "none",
  "framework_kind": null,
  "requirement": "every held data category is inventoried with class and sensitivity",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "W1-D1 category table is a deterministic artefact; coverage checkable",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "docs/architecture/W1-data-boundary-map.md sections 2 and 4",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "twenty categories, six classes; adequacy of classing stays review-only"
 },
 {
  "row_id": "AR-CORE-02",
  "primitive": "P2",
  "framework": "none",
  "framework_kind": null,
  "requirement": "every category lives in exactly one governed home",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "home table plus Lane A conformance checks are deterministic",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "docs/architecture/W1-data-boundary-map.md section 3; tests/test_w4_contract_conformance.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-CORE-03",
  "primitive": "P3",
  "framework": "none",
  "framework_kind": null,
  "requirement": "access is minimum-necessary, consent-gated, default-deny",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "doctrine artefacts exist; real-world minimality is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 4; docs/architecture/W1-D2-consent-scope-model.md",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "doctrine-evidenced; operational access control awaits a runtime"
 },
 {
  "row_id": "AR-CORE-04",
  "primitive": "P4",
  "framework": "none",
  "framework_kind": null,
  "requirement": "processing is per-purpose and consent-scoped; special-category data takes explicit consent",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "grant grammar exists; purpose fidelity in operation is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 10; W1-D2 grant elements; ADR-0001 disclosure events",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-CORE-05",
  "primitive": "P5",
  "framework": "none",
  "framework_kind": null,
  "requirement": "use and disclosure are whitelist-only with a named anti-map; no secondary use",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "edge whitelist and anti-map are enumerable; Lane A M12a validates anti-map fidelity",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 section 5; tests/test_w4_contract_conformance.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-CORE-06",
  "primitive": "P6",
  "framework": "none",
  "framework_kind": null,
  "requirement": "data at rest is ciphertext outside the user trust boundary, with residue proofs",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "residue and seal tests are deterministic and run in the suite",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0004; ADR-0005; ADR-0013; engine/core/store.py; tests residue classes",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "design-and-test evidenced; deployed-instance storage posture is a deployment fact"
 },
 {
  "row_id": "AR-CORE-07",
  "primitive": "P7",
  "framework": "none",
  "framework_kind": null,
  "requirement": "any transmission surface is governed before it exists",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "no transmission surface exists; nothing runtime to inspect",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": null,
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "E10 unimplemented; E12 reserved; in-transit protection is W5 evidence"
 },
 {
  "row_id": "AR-CORE-08",
  "primitive": "P8",
  "framework": "none",
  "framework_kind": null,
  "requirement": "governed events are auditable, append-only, user-visible, plaintext-free",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "ledger store and its tests are deterministic artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 13; ADR-0015; engine/core/ledger_store.py; tests/test_engine_ledger.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-CORE-09",
  "primitive": "P9",
  "framework": "none",
  "framework_kind": null,
  "requirement": "retention is limited and user-controlled with defined defaults",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "storage-limitation posture exists; retention defaults remain an open question",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "W0 section 12 names retention defaults as open; honesty requires not_evidenced"
 },
 {
  "row_id": "AR-CORE-10",
  "primitive": "P10",
  "framework": "none",
  "framework_kind": null,
  "requirement": "export and erasure are first-class user rights, never consent-gated",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "export path and erasure act are implemented and tested",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 11; engine/core/export.py; ADR-0015 erasure; backup/restore tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "amendment/correction flows exist as user edit rights (E8, T7)"
 },
 {
  "row_id": "AR-CORE-11",
  "primitive": "P11",
  "framework": "none",
  "framework_kind": null,
  "requirement": "third-party surfaces carry minimum payloads and named adapters only",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "doctrine exists; no adapter exists to inspect",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": null,
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "E10 payload doctrine accepted; vendor conduct is runtime-plus-organisational"
 },
 {
  "row_id": "AR-CORE-12",
  "primitive": "P12",
  "framework": "none",
  "framework_kind": null,
  "requirement": "incidents can be detected, handled, and notified",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "no incident process or operator exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-CORE-13",
  "primitive": "P13",
  "framework": "none",
  "framework_kind": null,
  "requirement": "evidence pointers are deterministic: registry hashes, suite proofs, conformance checks",
  "source_ref": [],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "registry hash recomputation and the suite are deterministic",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "governance/registry.json; tests/test_repo_state.py; Lane A validator",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-01",
  "primitive": "P1",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "health-information inventory and system boundary are defined",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "inventory artefact presence is decidable",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 sections 2-4",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-02",
  "primitive": "P5",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "permitted use and disclosure boundaries are enumerated, default-deny",
  "source_ref": [
   "SRC-HIPAA-02",
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "whitelist enumeration is decidable",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 section 5",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-03",
  "primitive": "P3",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "minimum-necessary limitation on access and use",
  "source_ref": [
   "SRC-HIPAA-04"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "structural rule exists; operational minimality is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 4; W1-D2 scoped grants",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-04",
  "primitive": "P3",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "access controls restrict who may reach held health context",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "custody design exists; enforcement is runtime",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "ADR-0013 custody",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-05",
  "primitive": "P3",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "person or entity authentication where applicable",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "passphrase custody designed; deployment authentication absent",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "ADR-0013",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-06",
  "primitive": "P8",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "audit controls record access and activity",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "ledger artefact and tests exist",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0015; engine/core/ledger_store.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "coverage across a deployed system remains review-only"
 },
 {
  "row_id": "AR-HIPAA-07",
  "primitive": "P6",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "integrity safeguards against undetected alteration",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "authenticated encryption is designed and tested; adequacy is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0005; engine seal/unseal tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-08",
  "primitive": "P7",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "transmission security for data in motion",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "no transmission surface exists",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": null,
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-09",
  "primitive": "P6",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "storage protection for data at rest",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "residue proofs are deterministic",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0004 tests; ADR-0013 envelope",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-10",
  "primitive": "P13",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "risk analysis and risk management are documented and maintained",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "organisational process; W1-D5 threat model is input, not the process",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": "docs/architecture/W1-D5-threat-model.md",
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-11",
  "primitive": "P11",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "business-associate and subcontractor obligations where applicable",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "no vendor relationship exists; legal necessity and adequacy are judgement",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "artefact-at-governed-location could later be mechanical; requirement and adequacy never"
 },
 {
  "row_id": "AR-HIPAA-12",
  "primitive": "P10",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "individual access to their own held health information",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "read and export paths are implemented, tested artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "engine/core/export.py; E8 own-record access",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed from a former compound access/amendment/accounting row per the settled decomposition rule"
 },
 {
  "row_id": "AR-HIPAA-13",
  "primitive": "P9",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "organisational retention, return, and destruction obligations (obligation component)",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "retention schedules, return duties, and destruction attestations are operator evidence; none defined",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed: the repository destruction/erasure capability is AR-HIPAA-19 and does not green this obligation"
 },
 {
  "row_id": "AR-HIPAA-19",
  "primitive": "P9",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "destruction/erasure capability for held records (capability component)",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "mechanical",
  "decidability_basis": "erasure paths are implemented, tested artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0015 erasure; engine erasure tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed from AR-HIPAA-13: capability only; the organisational obligation remains Tier 3 external evidence in AR-HIPAA-13"
 },
 {
  "row_id": "AR-HIPAA-14",
  "primitive": "P12",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "breach detection and notification readiness",
  "source_ref": [
   "SRC-HIPAA-06"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "no detection or notification capability exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-15",
  "primitive": "P1",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "de-identification method and determination, if any de-identified claim is ever made",
  "source_ref": [
   "SRC-HIPAA-05"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "no de-identification claim or capability exists",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "no de-identification claim is made",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "requirement attaches only if a claim is made; synthetic fixtures are not de-identified data"
 },
 {
  "row_id": "AR-HIPAA-16",
  "primitive": "P13",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "workforce, physical, and policy safeguards",
  "source_ref": [
   "SRC-HIPAA-02"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "no organisation is modelled in-repo",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HIPAA-17",
  "primitive": "P10",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "individual amendment/correction capability over their own held information",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "direct user correction is an implemented immediate-override right; formal request/denial workflow is organisational",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D3 T7 user correction; E8; W0 Law 11",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "evidences the direct-correction capability only; a formal amendment-request process would be organisational evidence"
 },
 {
  "row_id": "AR-HIPAA-18",
  "primitive": "P10",
  "framework": "HIPAA-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "accounting of disclosures deliverable to the individual",
  "source_ref": [
   "SRC-HIPAA-03"
  ],
  "applicability_ref": "APR-HIPAA",
  "classification": "review-only",
  "decidability_basis": "the mapped accounting obligation is unassessed; the ledger is a foundation, not the deliverable",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "the user-visible append-only ledger (L1/L2, ADR-0015) records disclosure events and is partial foundation; no accounting deliverable exists or is assessed"
 },
 {
  "row_id": "AR-APP-01",
  "primitive": "P4",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "collection of sensitive health information only with consent and where reasonably necessary (APP 3 alignment)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "consent-first architecture exists; necessity is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 section 8 consent model; W1-D2",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-APP-02",
  "primitive": "P5",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "use and disclosure limited to the primary consented purpose (APP 6 alignment)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "purpose-bound grants exist; operational fidelity is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D2 grant purpose element; W1-D1 whitelist",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-APP-03",
  "primitive": "P6",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "technical protection measures against misuse, interference, loss, and unauthorised access (APP 11 alignment, technical component)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "technical protection is designed and residue/seal-tested; reasonable-steps sufficiency is judgement against C104 text",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0004/0005/0013; residue and custody tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "technical component only, decomposed per the settled rule; map against current compilation C104 wording, not pre-amendment summaries"
 },
 {
  "row_id": "AR-APP-04",
  "primitive": "P10",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "user access to their own information (APP 12 alignment)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "mechanical",
  "decidability_basis": "export/read paths are implemented artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "E8; engine/core/export.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-APP-05",
  "primitive": "P10",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "user correction of their own information (APP 13 alignment)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "user correction exists as T7 immediate override; formal correction-request handling is organisational",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D3 T7; W0 Law 11",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-APP-06",
  "primitive": "P6",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "organisational measures required within reasonable steps (APP 11.3, C104)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "C104 APP 11.3 expressly includes technical and organisational measures; no operator or organisational evidence exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed so technical repository evidence cannot green the organisational component; Tier 3 never collapses into repository evidence"
 },
 {
  "row_id": "AR-APP-07",
  "primitive": "P10",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "destruction/erasure capability for information no longer needed (APP 11.2 alignment, capability component)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "mechanical",
  "decidability_basis": "erasure paths are implemented, tested artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0015 erasure; engine erasure tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-APP-08",
  "primitive": "P9",
  "framework": "APP-aligned",
  "framework_kind": "alignment_overlay",
  "requirement": "the no-longer-needed determination that triggers destruction (APP 11.2 alignment, retention-trigger component)",
  "source_ref": [
   "SRC-APP-01",
   "SRC-APP-02"
  ],
  "applicability_ref": "APR-APP",
  "classification": "review-only",
  "decidability_basis": "retention defaults remain an open question; no trigger determination exists to evidence",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "same open question as AR-CORE-09; capability (AR-APP-07) must not green the trigger"
 },
 {
  "row_id": "AR-GDPR-01",
  "primitive": "P4",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "purpose limitation and data minimisation as architecture",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "structural rule exists; minimisation adequacy is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 4/10; W1-D1 minimum edges",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-GDPR-02",
  "primitive": "P4",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "explicit consent as the basis for special categories of personal data (Article 9 alignment)",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "consent doctrine exists; lawful-basis analysis is legal judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 section 9; W1-D2 explicit-consent grants",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "the Wing additionally treats contemplative (CM) data as special-category by its own stricter doctrine; that is a Wing rule layered on the Article 9 mapping, not a statutory category defined by the Regulation"
 },
 {
  "row_id": "AR-GDPR-03",
  "primitive": "P10",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "erasure as a first-class operation",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "mechanical",
  "decidability_basis": "erasure paths implemented and tested",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0015; engine erasure tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-GDPR-04",
  "primitive": "P10",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "export of held records in a usable form: original bytes returned byte-identical with structured machine-readable provenance",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "mechanical",
  "decidability_basis": "deterministic tests prove byte symmetry and structured JSON provenance on export",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "engine/core/export.py (E1-to-E8 byte symmetry; provenance as structured JSON, indent-2); tests/test_engine_export.py",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "narrowed to what the artefacts actually prove; the wider portability properties are AR-GDPR-07"
 },
 {
  "row_id": "AR-GDPR-07",
  "primitive": "P10",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "aggregate portability in a structured, commonly used, machine-readable form",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "no aggregate-export format assessment exists; repository-evidenceable when made",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "single-record byte-exact export (AR-GDPR-04) does not evidence the aggregate format property; whole-vault plaintext export is itself a deferred future record; transmit-to-another-controller is AR-GDPR-08"
 },
 {
  "row_id": "AR-GDPR-08",
  "primitive": "P10",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "transmit-to-another-controller capability",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "transmission is a runtime surface; no transmission capability presently exists and none is claimed",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": null,
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed from AR-GDPR-07: format property is Tier 1 repository evidence, transmission is W5 runtime evidence and must not share its row"
 },
 {
  "row_id": "AR-GDPR-05",
  "primitive": "P9",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "storage limitation with retention defaults",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "retention defaults remain an open question",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "same open question as AR-CORE-09"
 },
 {
  "row_id": "AR-GDPR-06",
  "primitive": "P13",
  "framework": "GDPR-style",
  "framework_kind": "alignment_overlay",
  "requirement": "data protection by design and by default, most-protective defaults",
  "source_ref": [
   "SRC-GDPR-01"
  ],
  "applicability_ref": "APR-GDPR",
  "classification": "review-only",
  "decidability_basis": "design posture pervades doctrine; sufficiency is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 section 9; default-deny whitelist; ADR-0001",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HBNR-01",
  "primitive": "P12",
  "framework": "FTC-HBNR",
  "framework_kind": "alignment_overlay",
  "requirement": "breach-of-security notification duties to individuals, the FTC, and media where applicable",
  "source_ref": [
   "SRC-HBNR-01",
   "SRC-HBNR-02"
  ],
  "applicability_ref": "APR-HBNR",
  "classification": "review-only",
  "decidability_basis": "no notification capability or operator exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HBNR-02",
  "primitive": "P1",
  "framework": "FTC-HBNR",
  "framework_kind": "alignment_overlay",
  "requirement": "personal-health-record scope: technical capacity to draw identifiable health information from multiple sources",
  "source_ref": [
   "SRC-HBNR-01"
  ],
  "applicability_ref": "APR-HBNR",
  "classification": "review-only",
  "decidability_basis": "capacity is a deployed-product fact; no deployment exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "deployment profile (absent)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "local-first doctrine is not proof a future deployed product lacks multi-source capacity"
 },
 {
  "row_id": "AR-HBNR-03",
  "primitive": "P6",
  "framework": "FTC-HBNR",
  "framework_kind": "alignment_overlay",
  "requirement": "secured status of PHR identifiable health information",
  "source_ref": [
   "SRC-HBNR-01"
  ],
  "applicability_ref": "APR-HBNR",
  "classification": "review-only",
  "decidability_basis": "encrypted-at-rest design requirement exists; qualifying technology and key-compromise state are implementation and incident evidence",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "ADR-0005/0013 design",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-HBNR-04",
  "primitive": "P12",
  "framework": "FTC-HBNR",
  "framework_kind": "alignment_overlay",
  "requirement": "breach detection sufficient to start the notification clock",
  "source_ref": [
   "SRC-HBNR-01"
  ],
  "applicability_ref": "APR-HBNR",
  "classification": "review-only",
  "decidability_basis": "no detection capability exists",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-01",
  "primitive": "P1",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "PII inventory and identification",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "category inventory is a deterministic artefact",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 section 4",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-02",
  "primitive": "P2",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "data location and home mapping",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "one-home rule is enumerable and Lane-A-checked",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 section 3",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-03",
  "primitive": "P1",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "confidentiality impact levels",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "class ladder exists; level appropriateness is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W1-D1 section 2 classes",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-04",
  "primitive": "P3",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "prevention of inappropriate access",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "structural walls declared; enforcement is runtime",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "ADR-0017 isolation declarations",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-05",
  "primitive": "P5",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "prevention of inappropriate use",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "inference prohibition declared and bait-tested at document level; behaviour is runtime",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "ADR-0019; 23 bait declarations",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "Lane B holds 23 declarations, 0 fixtures"
 },
 {
  "row_id": "AR-NIST-06",
  "primitive": "P5",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "prevention of inappropriate disclosure",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "anti-map and payload minimisation declared; conduct is runtime",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": "W1-D1 anti-map; E10 doctrine",
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-07",
  "primitive": "P3",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "least and minimum access",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "minimum-necessary is structural; operational minimality is judgement",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "W0 Law 4; W1-D2",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-08",
  "primitive": "P9",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "retention defaults (retention component)",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "retention defaults remain an open question",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "same open question as AR-CORE-09; decomposed: disposal/erasure capability is AR-NIST-13"
 },
 {
  "row_id": "AR-NIST-09",
  "primitive": "P12",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "incident response for PII",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "organisational process absent",
  "evidence_status": "external_evidence_required",
  "evidence_timing": 3,
  "evidence_pointer": null,
  "dependency": "external organisational evidence (operator does not exist)",
  "safe_wording": "external organisational evidence required",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-10",
  "primitive": "P1",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "de-identification and re-identification risk",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "no de-identification claim or capability",
  "evidence_status": "not_evidenced",
  "evidence_timing": 1,
  "evidence_pointer": null,
  "dependency": null,
  "safe_wording": "control evidence absent",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "synthetic fixtures are synthetic, not de-identified"
 },
 {
  "row_id": "AR-NIST-11",
  "primitive": "P11",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "third-party PII exposure",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "review-only",
  "decidability_basis": "no third-party surface exists",
  "evidence_status": "deferred_named_dependency",
  "evidence_timing": 2,
  "evidence_pointer": null,
  "dependency": "W5 runtime (isolation, adapters, transmission, disclosure mechanics)",
  "safe_wording": "deferred to W5",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-12",
  "primitive": "P8",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "logging without sensitive over-disclosure",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "plaintext-free ledger constraint is tested; scan is deterministic",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "C0 constraint; ADR-0004 log rules; public-safety scan",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": null
 },
 {
  "row_id": "AR-NIST-13",
  "primitive": "P9",
  "framework": "NIST SP 800-122",
  "framework_kind": "engineering_baseline",
  "requirement": "disposal/erasure capability (capability component)",
  "source_ref": [
   "SRC-NIST-01"
  ],
  "applicability_ref": null,
  "classification": "mechanical",
  "decidability_basis": "erasure paths are implemented, tested artefacts",
  "evidence_status": "evidenced",
  "evidence_timing": 1,
  "evidence_pointer": "ADR-0015 erasure; engine erasure tests",
  "dependency": null,
  "safe_wording": "control evidence present in accepted doctrine artefacts",
  "prohibited_overclaim": "asserting the mapped requirement is legally satisfied",
  "review_note": "decomposed from AR-NIST-08: capability only; the retention-defaults determination stays open in AR-NIST-08"
 }
]
```

## 5. Derived assurance-state presentation

Derivation rule: overlay row + applicability `unresolved` → **applicability unresolved** (never a
pass); overlay row + `does_not_apply` → **not applicable**; overlay row + `applies`, or any
core/baseline row → the underlying evidence status.

| row | primitive | framework | stored evidence_status | tier | derived assurance state |
|---|---|---|---|---|---|
| AR-CORE-01 | P1 | none | evidenced | 1 | **evidenced** |
| AR-CORE-02 | P2 | none | evidenced | 1 | **evidenced** |
| AR-CORE-03 | P3 | none | evidenced | 1 | **evidenced** |
| AR-CORE-04 | P4 | none | evidenced | 1 | **evidenced** |
| AR-CORE-05 | P5 | none | evidenced | 1 | **evidenced** |
| AR-CORE-06 | P6 | none | evidenced | 1 | **evidenced** |
| AR-CORE-07 | P7 | none | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-CORE-08 | P8 | none | evidenced | 1 | **evidenced** |
| AR-CORE-09 | P9 | none | not_evidenced | 1 | **not evidenced** |
| AR-CORE-10 | P10 | none | evidenced | 1 | **evidenced** |
| AR-CORE-11 | P11 | none | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-CORE-12 | P12 | none | external_evidence_required | 3 | **external evidence required** |
| AR-CORE-13 | P13 | none | evidenced | 1 | **evidenced** |
| AR-HIPAA-01 | P1 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-02 | P5 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-03 | P3 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-04 | P3 | HIPAA-aligned | deferred_named_dependency | 2 | **applicability unresolved** |
| AR-HIPAA-05 | P3 | HIPAA-aligned | deferred_named_dependency | 2 | **applicability unresolved** |
| AR-HIPAA-06 | P8 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-07 | P6 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-08 | P7 | HIPAA-aligned | deferred_named_dependency | 2 | **applicability unresolved** |
| AR-HIPAA-09 | P6 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-10 | P13 | HIPAA-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-HIPAA-11 | P11 | HIPAA-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-HIPAA-12 | P10 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-13 | P9 | HIPAA-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-HIPAA-19 | P9 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-14 | P12 | HIPAA-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-HIPAA-15 | P1 | HIPAA-aligned | not_evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-16 | P13 | HIPAA-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-HIPAA-17 | P10 | HIPAA-aligned | evidenced | 1 | **applicability unresolved** |
| AR-HIPAA-18 | P10 | HIPAA-aligned | not_evidenced | 1 | **applicability unresolved** |
| AR-APP-01 | P4 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-02 | P5 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-03 | P6 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-04 | P10 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-05 | P10 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-06 | P6 | APP-aligned | external_evidence_required | 3 | **applicability unresolved** |
| AR-APP-07 | P10 | APP-aligned | evidenced | 1 | **applicability unresolved** |
| AR-APP-08 | P9 | APP-aligned | not_evidenced | 1 | **applicability unresolved** |
| AR-GDPR-01 | P4 | GDPR-style | evidenced | 1 | **applicability unresolved** |
| AR-GDPR-02 | P4 | GDPR-style | evidenced | 1 | **applicability unresolved** |
| AR-GDPR-03 | P10 | GDPR-style | evidenced | 1 | **applicability unresolved** |
| AR-GDPR-04 | P10 | GDPR-style | evidenced | 1 | **applicability unresolved** |
| AR-GDPR-07 | P10 | GDPR-style | not_evidenced | 1 | **applicability unresolved** |
| AR-GDPR-08 | P10 | GDPR-style | deferred_named_dependency | 2 | **applicability unresolved** |
| AR-GDPR-05 | P9 | GDPR-style | not_evidenced | 1 | **applicability unresolved** |
| AR-GDPR-06 | P13 | GDPR-style | evidenced | 1 | **applicability unresolved** |
| AR-HBNR-01 | P12 | FTC-HBNR | external_evidence_required | 3 | **applicability unresolved** |
| AR-HBNR-02 | P1 | FTC-HBNR | external_evidence_required | 3 | **applicability unresolved** |
| AR-HBNR-03 | P6 | FTC-HBNR | deferred_named_dependency | 2 | **applicability unresolved** |
| AR-HBNR-04 | P12 | FTC-HBNR | external_evidence_required | 3 | **applicability unresolved** |
| AR-NIST-01 | P1 | NIST SP 800-122 | evidenced | 1 | **evidenced** |
| AR-NIST-02 | P2 | NIST SP 800-122 | evidenced | 1 | **evidenced** |
| AR-NIST-03 | P1 | NIST SP 800-122 | evidenced | 1 | **evidenced** |
| AR-NIST-04 | P3 | NIST SP 800-122 | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-NIST-05 | P5 | NIST SP 800-122 | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-NIST-06 | P5 | NIST SP 800-122 | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-NIST-07 | P3 | NIST SP 800-122 | evidenced | 1 | **evidenced** |
| AR-NIST-08 | P9 | NIST SP 800-122 | not_evidenced | 1 | **not evidenced** |
| AR-NIST-09 | P12 | NIST SP 800-122 | external_evidence_required | 3 | **external evidence required** |
| AR-NIST-10 | P1 | NIST SP 800-122 | not_evidenced | 1 | **not evidenced** |
| AR-NIST-11 | P11 | NIST SP 800-122 | deferred_named_dependency | 2 | **deferred — named dependency** |
| AR-NIST-12 | P8 | NIST SP 800-122 | evidenced | 1 | **evidenced** |
| AR-NIST-13 | P9 | NIST SP 800-122 | evidenced | 1 | **evidenced** |

## 6. Honest-state summary

- **Rows: 65** — CORE 13 · HIPAA-aligned 19 · APP-aligned 8 · GDPR-style 8 · FTC-HBNR 4 · NIST SP 800-122 13
- **Stored evidence_status:** {'deferred_named_dependency': 11, 'evidenced': 35, 'external_evidence_required': 11, 'not_evidenced': 8}
- **Timing tiers:** {1: 43, 2: 11, 3: 11}
- **Derived presentation:** {'applicability unresolved': 39, 'deferred — named dependency': 6, 'evidenced': 15, 'external evidence required': 2, 'not evidenced': 3} — every one of the 39 overlay rows presents as *applicability
  unresolved* today, exactly as the architecture requires; the underlying evidence work is neither
  hidden nor overclaimed.
- **Deliberate honesty rows:** retention defaults and the destruction trigger are `not_evidenced`
  (W0 §12 open question — AR-CORE-09/AR-GDPR-05/AR-NIST-08/AR-APP-08); the accounting-of-disclosures
  deliverable is `not_evidenced` with the ledger named as foundation only (AR-HIPAA-18); aggregate
  portability's format property is `not_evidenced` (AR-GDPR-07) while its transmission capability
  is `deferred_named_dependency` to W5 with no present-capability claim (AR-GDPR-08); APP 11.3 organisational
  measures are `external_evidence_required` and never greened by technical evidence (AR-APP-06);
  de-identification is `not_evidenced` with no claim made (AR-HIPAA-15/AR-NIST-10); Lane B's 23/0/0
  state is cited as declaration-only evidence (AR-NIST-05).

## 7. Register consumption

Source references used: SRC-HIPAA-02/03/04/05/06 · SRC-APP-01/02 · SRC-GDPR-01 · SRC-HBNR-01/02 ·
SRC-NIST-01 — eleven of the fourteen register entries. SRC-HIPAA-01, SRC-HIPAA-07 and SRC-APP-03
remain registered without dependent rows — the NPRM by design as horizon-only — and an empty
dependent-row set is not evidence a source is unnecessary. The register's `dependent_rows` fields
for the eleven cited entries were populated through governed source-register maintenance in the
same atomic landing that made this record governed, under the register's maintenance rule 1; its
rule 2 routes every row here back to review if a cited source is superseded or materially changed.

## 8. Maintenance rules

1. Rows change only through governed updates landed by ceremony — never by silent edit and never
   by self-adjustment from any consuming or evidencing artefact.
2. Applicability resolution is a future governed act recorded on the applicability records —
   never inferred from evidence presence, never resolved by this record's own text, and never
   mechanical.
3. A superseded or materially changed register source routes every row citing it back to review.
4. An evidence pointer locates evidence; it is never a claim that the mapped requirement is
   legally satisfied, and it never resolves applicability.
5. The six-word assurance vocabulary remains derived at presentation and is never stored.

## 9. Validation at acceptance

Mechanical checks run against the JSON blocks above at acceptance: row count and family counts;
sixteen stored fields per row; unique row IDs; enum validity for `evidence_status`,
`classification`, `evidence_timing`; cardinality rules — core rows `framework none / kind null /
applicability null`, baseline rows `kind engineering_baseline / applicability null`, overlay rows
`applicability_ref` resolving to one of four applicability records; every `source_ref` resolving
to a register `source_id`; every `deferred_named_dependency` naming its dependency; every
`external_evidence_required` row at Tier 3 naming its external dependency; derived-state
computation; **no URLs anywhere in this record** (locators live only in the register); no
affirmative certification claim — prohibited formulations occur only where named as forbidden.

## 10. Public-safety note

This record contains no private names, no private system references, no personal health details,
no real personal data, and no project lineage beyond this repository. It contains no URLs —
canonical locators live only in the Source Register. Statements naming certification occur only
as prohibitions, never as claims. Rows describe controls and evidence, never people.
