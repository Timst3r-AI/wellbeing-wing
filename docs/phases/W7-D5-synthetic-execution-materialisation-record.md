# W7-D5 - Synthetic Execution Records and First Materialisation: Development and Completion Record

**Status:** Accepted by human reviewer, 2026-08-23. **Effective on publication and remote verification**, at which point W7-D5 is complete. The landing-specific P4b review across all eleven families was performed and recorded CLEAR, and the exact final packet was separately accepted, before this status was written.

**Identity:** `W7-D5-SEC`, type `phase-record`  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D5 - Synthetic execution records and first generated-evaluation materialisation  
**Governing authority:** `W7-D5-SEB` revision v1.3, as amended by `W7-D5-PSA` and `W7-D5-MRA`  
**Baseline:** `a32bdf4e0aa0229f8e0d6386109cbd9c48e7fab5` - `W7-D5: Correct manifest registry classification` (run executed on the published PSA baseline `646a9dd9`, candidate reconciled onto the published MRA baseline)  
**Run identity:** `W7-D5-RUN-01` - executed once, wholly clean  
**Run `as_of` (UTC):** 2026-08-23

---

## 1. Authority and baseline (36.1)

The D5 brief governs at revision v1.3 (`docs/phases/W7-D5-synthetic-execution-materialisation-brief.md`, LF sha256 `804fcf07ed0137251c71ed37dd04192f177b09f5e4dc244404e2f6cc914233f1`), amended by the accepted `W7-D5-PSA` (`docs/phases/W7-D5-proof-succession-amendment.md`) and `W7-D5-MRA` (`docs/phases/W7-D5-manifest-registry-classification-amendment.md`). `W7-D5-RUN-01` was executed under the published PSA baseline `646a9dd9` and the candidate is reconciled onto the published MRA baseline `a32bdf4e` - the run was not rerun, per the MRA settlements. All four pre-succession source pins were re-proven against raw clone bytes before preflight:

| Artefact | SHA-256 (canonical LF) | Standing |
|---|---|---|
| `fixtures/SYNTHETIC-w7-d4-exam.json` | `9755cca1e8f9e41d7c89d532abb2f674a0189ec58935e3a5763fd641c90406a7` | permanently frozen, unchanged |
| `tests/w7_synthetic_evaluation_harness.py` | `e50172f5393a8753c9f4a93e29ef52e50cd366c0539a7c483787c085ea31f1fb` | permanently frozen, unchanged |
| `tests/test_w7_synthetic_harness.py` | `6da85d5b2b745e6156d7317f8859fde393489fee8b6df963310a9ebac747d860` | pre-succession pin; H12 bounded succession applied in this landing |
| `tests/test_w7_model_boundary_decision.py` | `3748a16b219404fcd8d3686431adecc3713850aa3d2983f52d38a2970a45e722` | pre-succession pin; M6 bounded succession applied in this landing |

The PSA-mandated corpus-wide temporal assertion sweep was repeated before run start: greps across the complete deterministic corpus for present-state absence, vacancy, unopened-state, zero-allocation and pre-capability assertions found **no hit outside the v1.2-authorised succession surface** (the three D2-E assertions, H12, and M6). Every other existence assertion in the corpus concerns engine/runtime workspace hygiene, W4 contract exports or W6 surface inventories, none of whose truth changes at D5 materialisation.

## 2. Run accounting (36.2)

`W7-D5-RUN-01` began at the section 7.1 boundary after a wholly green preflight (baseline descent, four pins, 26/23/52 exam arithmetic, home absent on disk and untracked and never introduced anywhere in history, no GER-prefixed registry id, no run entry, scanner and allowlist byte-identical to the published baseline) and was consumed at the first capture.

- **26 of 26 probes** executed in exam order, `D4-P01` through `D4-P26`;
- **52 of 52 captures**, each capture-scanned through the live scanner with no allowlist route;
- **0 findings**; no capture was edited, truncated, paraphrased or retried;
- **26 GERs** materialised in the disposable candidate clone only;
- no missing, extra or duplicate probe; 52 distinct capture texts;
- **one stable scan-environment bit for the whole run: `inactive`**, sampled at run start and re-asserted before every capture; the branch state never changed.

## 3. Provenance (36.3)

Every capture is an `authored_synthetic_specimen` admitted under its declared `authored_synthetic` origin. No generated output exists and no model was contacted; the harness has no contact path by construction, and ADR-0051 Option D governs throughout. The frozen D4 harness was invoked with `authorising_record = W7-D4-SHB`, the specimen-authoring authority the exam itself declares, and the pure D5 binding layer (`tests/w7_generated_evaluation_binding.py`) replaced **only the top-level run authority** with `W7-D5-SEB`, refusing any candidate whose captures do not carry `W7-D4-SHB`. Run authority and specimen authorship remain two facts in every record.

## 4. Identity and lifecycle (36.4)

The first contiguous block `GER-0001` through `GER-0026` was bound to probe order after the namespace preflight proved the `GER-####` namespace empty across the current tree and the entire authoritative history. The number carries identity only. The lifecycle law of brief sections 10-11 is now fixed and proven: published identity is stable; **no identifier is ever reused**, with authoritative history, not the current listing, as the source; the canonical path is `governance/generated-evaluation/<record_id>.json`; no rename, relocation or alias; **no deletion, no archive, no withdrawal-from-view mechanism exists**, and retention is **no automatic expiry**.

## 5. Manifest and S2 (36.5)

`governance/generated-evaluation/W7-D5-RUN-01-manifest.json` (LF sha256 recorded in its registry entry, which per `W7-D5-MRA` is type `governed-register` on the W6-CAT precedent, with its human acceptance carried by this record as its governing phase-record and no circular authority dependency) lists exactly the 26 records in GER/probe order with canonical repository-relative paths and per-record content hashes over the exact final bytes; `exam.content_hash` equals the frozen published exam hash; the scan-environment block is the closed one-bit shape carrying `inactive`. The home contains **exactly 27 files** and nothing else. **S2 is LIVE**: the frozen D4 manifest relation validates against the actual repository bytes (M8), and the registry carries the manifest hash (M12).

## 6. Proof succession (36.6)

- **S1 reached its lawful endpoint.** The succeeded S1 proves from published history that the reserved home had no tracked artefact through the parent of the first authorised materialisation commit, and that the materialising commit carries the accepted D5 brief. The original W7-D2-E record was true for every commit it governed; **no erratum is needed**.
- **The post-materialisation invariant is in force** (brief section 24.3), proven by M2/M3/M8: only authorised GERs and their registered manifest, each at its canonical identity path, each listed exactly once with a matching hash, no stray artefact.
- **H12 (D4 module) and M6 (D3 module) received exactly their W7-D5-PSA bounded successions**: each module differs from its pre-succession pin only inside the authorised span, proven mechanically by M1's bounded-diff proof; H12 now proves D4-era vacancy from history and keeps its disposable successor checks; M6 proves the ADR-0051 landing-era no-home/no-allocation condition from history, and its no-GER-registry-id limb remains current-state and true.
- **S3 is reclassified LIVE** after the required demonstration: the ID-scoped history proof (M10) runs against the real subjects, and its four required controls were demonstrated in disposable histories - rename-plus-capture-edit detected, delete-and-reuse detected, a review-metadata-only mutation accepted without capture change, duplicate-ID/different-capture detected.
- **The nineteen-obligation matrix after D5:** ENDPOINT/HISTORICAL 1 (S1) · LIVE 11 (S2 S3 T1 T2 T3 T4 T5 T7 T8 T9 U1) · READY-DEBT 4 (U2 U3 U4 U5) · REVIEW-ONLY 3 (S4 T6 U6). 1 + 11 + 4 + 3 = 19.

## 7. Part Q and the local-wordlist seam (36.7)

Part Q remains unresolved and its accepted W7 narrowing was binding throughout: any finding would have ended the successful-run path for the whole run. **No finding occurred.** No allowlist changed and no suppression was added; ADR-0050 Part I (no allowlist entry under the home) is proven live by M9. The `local-wordlist` coordinate seam remains unresolved: the run's branch was `inactive` as sampled from the effective scanner branch, **inactivity was not manufactured**, and an inactive run resolves nothing about the seam.

## 8. Human boundaries (36.8)

- **P4a**: the governed eleven-row D4 guard inventory was applied unchanged to the materialised class artefacts (26 GERs and the manifest) by M11 - live family reconciliation holds, eight guarded and three declared unguarded, all positive controls trigger, all clean controls stay clean, no guarded surface present, all five non-claims intact. **A green P4a is no evidence for P4b.**
- **P4b**: review-only in full across all eleven ADR-0046 decision 11 families. **Performed by Tara on 2026-08-23 against this exact final candidate, family by family across all eleven, disposition CLEAR, and separately followed by her final acceptance of the exact Landing B packet on 2026-08-23.** The act is landing-specific to these bytes, is not inferred from P4a in any degree, and establishes no model behaviour, safety, correctness, clinical validity, Part Q resolution, local-wordlist seam resolution, W7-D6 disposition or real-person adoption authority.
- **S4** (home signals its risk class; manifest stayed an index) and **T6** (no lawful field performing a barred semantic function; no re-authoring; no laundering) are standing human review duties at the final review and are not discharged by any test.
- **U6** has no subject in this landing: no finding occurred, and no U6 act is manufactured.
- `human_review.routed` is `true` and **`human_review.disposition` and `human_review.disposition_record` are null in every GER**. D5 acceptance is publication conformance; it is not a W7-D6 disposition, no disposition vocabulary exists yet, and W7-D6 remains unopened.

## 9. Verification (36.9)

All measured against the exact proposed 35-path tracked state in the disposable candidate clone:

- focused D5 materialised-state module: 16 tests / 154 subtests, green;
- D2-E shape module after succession: 18 tests / 115 subtests, green;
- whole D4 proof module after H12 succession: 14 tests / 156 subtests, green;
- whole D3 model-boundary module after M6 succession: 8 tests / 53 subtests, green;
- first-contact doctrine, boundary invariant, repo-state and pending-ledger proofs green; no ledger row touched;
- mutation and negative-control ceremony: 41 of 41 detected across the brief section 33 matrix, executed against in-memory mutants, disposable-copy state and throwaway git histories; the unmutated candidate proven green before and after;
- landing-mode scan over all 35 proposed paths: 35 files, 0 findings;
- normal scan over the complete proposed tracked state: 283 files, 0 findings, suppressions unchanged at 123;
- full deterministic suite: 565 passed, 9 skipped, 961 subtests, measured against the acceptance-transformed candidate; the standing pre-acceptance candidate measures 564 passed, 9 skipped, 961 subtests with exactly one deliberate failure - this record's candidate header against its accepted registry status - which resolves at the acceptance transformation and is the honest pre-acceptance state, not a defect;
- generated-evaluation home closed-set listing: exactly 27 files;
- registry consistency and content hashes: green; registry 115 to 117 entries, the manifest entry `governed-register` with its governing-record dependency and the completion record separately registered `phase-record`, per the M12 mechanical assertions;
- no model, dependency, credential, provider or binary path; `requirements.txt` untouched;
- no payload residue outside the accepted candidate files.

## 10. What completion does not establish (36.10)

No model behaviour claim. No behavioural pass or failure of any trap. No safety, correctness, clinical, legal, regulatory or production-readiness claim. No Part Q resolution. No local-wordlist seam resolution. No discharge of ADR-0047 precondition 3, which remains outstanding in its lawful resting state. No W7-D6 opening, no disposition vocabulary, no written disposition. No W7-D7 opening. No W8 opening. Specimen evidence is never model evidence (R5), and twenty-six executed probes are twenty-six exam questions about governed handling, not twenty-six findings about any model.

## 11. Constitutional and boundary check

This landing introduces no real-person data, no identified person's wellbeing material, no real device data, no private relationship material, no private model transcript, no credential or private configuration, no machine-identifying detail, no model binary, no real-person evaluation channel, no private adoption implementation detail, and no live personal instrument.

**Any real-person adoption is a separate governed authority outside this repository.**
