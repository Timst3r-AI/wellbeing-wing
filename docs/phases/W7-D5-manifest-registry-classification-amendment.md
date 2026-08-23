# W7-D5 - Manifest Registry Classification Amendment

**Status:** Accepted by human reviewer, 2026-08-23. **Effective on publication and remote verification.** It corrects the run-manifest registry classification for the Landing B candidate; at its own landing it edits no implementation or test artefact, creates no home artefact, allocates no identifier, and does not rerun or alter the completed W7-D5-RUN-01.

**Date prepared:** 2026-08-23  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D5 - Synthetic execution records and first generated-evaluation materialisation  
**Identity:** `W7-D5-MRA`, type `phase-record`  
**Amends:** `W7-D5-SEB` (`docs/phases/W7-D5-synthetic-execution-materialisation-brief.md`), revision v1.2 to v1.3  
**Architect:** Ari  
**Builder/executor after acceptance:** Eli  
**Human authority:** Tara  
**Baseline for this candidate:** `646a9dd938c6bbab2c6a0fb11b7fe7523f65bcf4` - `W7-D5: Amend proof succession scope`  
**Baseline registry state:** 114 entries, last `W7-D5-PSA`

---

## 1. Why this amendment exists

`W7-D5-RUN-01` has been executed once under the accepted v1.2 brief and is **wholly clean**: 26 of 26 probes, 52 of 52 captures, zero findings, one stable `inactive` scan-environment bit. The run is complete, is held in the governed external candidate, and **is not rerun by anything in this amendment**.

During Landing B candidate assembly, the registry work surfaced an accepted-brief defect. Brief section 17.1 classifies the run-manifest registry entry as type `phase-record`, but the live registry law rejects that classification for this artefact: `tests/test_repo_state.py::RegistryConsistency::test_statuses_match_source_headers` requires every `accepted` entry's file to carry the prose header `Accepted by human reviewer` in its first eight lines, and a conformant JSON run manifest cannot carry a prose header - its shape is the closed D4 manifest shape, and section 16.2 forbids exactly the kind of annotation a header would be. The same test carries the lawful answer, governed at the W6-D2-C+D landing: entries of type `governed-register` are JSON data artefacts exempt from the header requirement, **with their human acceptance recorded in their governing phase-record**. The one live precedent is `W6-CAT`, the governed string catalogue at `governance/string-catalogue.json`, whose acceptance is recorded through its admission record and whose `depends_on` names that governing record.

Implementation did not choose by discretion. Assembly stopped, the evidence was reported, and Ari ruled the mismatch a genuine accepted-brief defect with the live repository law controlling. This amendment is the bounded governed correction, landing before candidate assembly resumes - the doctrine-first pattern, a third time.

## 2. Character of the correction

**Architectural and bounded.** One registry classification and its dependency direction change. No manifest shape, GER shape, run semantics, H12/M6 succession, S2/S3 law, Part Q posture, P4 decomposition, D6 boundary or any other element of the D5 architecture changes. No doctrine record is touched. The repo-state proof is not edited and no prose header is added to any JSON artefact.

## 3. Settlements

1. **The `W7-D5-RUN-01` registry entry is type `governed-register`** - the live registry type for JSON data artefacts, on the `W6-CAT` precedent.
2. **Its human acceptance is recorded in `W7-D5-SEC`**, the D5 completion record, which remains type `phase-record` and carries the acceptance prose the manifest cannot.
3. **`W7-D5-RUN-01.depends_on` includes `W7-D5-SEC`**, naming its governing record, mirroring `W6-CAT`'s dependency on its admission record.
4. **`W7-D5-SEC.depends_on` does not include `W7-D5-RUN-01`**, so the registry carries no circular authority dependency. The completion record still cites and verifies the manifest as evidence - citation is not authority dependency.
5. **M12 of the materialised-state proof module must mechanically assert**: the exact `governed-register` type of the manifest entry; its governing-record dependency on `W7-D5-SEC`; its canonical manifest path; its content hash matching the exact manifest bytes; `implementation_permission: "none"`; and that no `GER-####` identifier receives a registry row.
6. **Successful Landing B remains exactly 35 paths.** Every correction this amendment causes inside the Landing B candidate is metadata or content within already-counted paths (the registry entry's fields, and the M12 assertions inside the already-counted proof module).
7. **`W7-D5-RUN-01` remains the already completed, wholly clean governed run and must not be rerun.** This amendment does not touch the run, its captures, its GER bytes or its manifest bytes.
8. **The stop-report and completion-record classifications stand**: brief sections 17.2 and 21.4 correctly type `W7-D5-SEC` and `W7-D5-RUN-01-STOP` as `phase-record` - both are prose records - and are unchanged.

## 4. Brief reconciliation to v1.3

The accepted `W7-D5-SEB` brief is reconciled to revision v1.3 in the same landing as this record: content changed at enumerated sites, registry content hash recomputed in the same commit, and a dated note appended to the `W7-D5-SEB` registry entry pointing here.

The v1.3 reconciliation touches exactly these sites and nothing else:

1. header revision line: v1.2 to v1.3, naming this amendment;
2. section 17.1: the entry type becomes `governed-register`, with the acceptance-in-`W7-D5-SEC` mechanics, the governing-record dependency direction, and the no-circular-dependency rule stated;
3. section 32, M12: the proof-family description gains the settlement 5 assertions as its acceptance criterion.

No other line of the brief changes. Sections 16 (manifest shape), 17.2, 17.3, 21.4, 24, and every run, lifecycle, succession and boundary section of v1.2 are carried byte-identically.

## 5. What this amendment does not do

At its own landing this record:

- edits no implementation or test artefact - the H12/M6 successions, the D2-E succession, the binder and the materialised-state module are untouched here and remain Landing B candidate content;
- creates no generated-evaluation home artefact in the authoritative repository, no new GER and no new manifest;
- does not rerun, reopen or alter `W7-D5-RUN-01` or any of its captures;
- allocates no identifier and does not advance the namespace declaration, which advances only in successful Landing B;
- contacts no model and produces no generated output;
- adds no dependency and touches no scanner, allowlist or repo-state proof line;
- resolves neither Part Q nor the `local-wordlist` coordinate seam;
- discharges no ADR-0047 precondition: precondition 3 remains outstanding;
- opens neither W7-D6 nor W7-D7 nor W8.

## 6. Landing scope of this amendment

Exactly four paths:

1. new `docs/phases/W7-D5-manifest-registry-classification-amendment.md` (this record);
2. modify `docs/phases/W7-D5-synthetic-execution-materialisation-brief.md` to revision v1.3 at the section 4 sites;
3. modify `governance/registry.json`: one new `W7-D5-MRA` entry, and the `W7-D5-SEB` entry's content hash recomputed with a dated amendment note appended;
4. modify `docs/phases/README.md`: one `W7-D5-MRA` row and the W7-D5 status sentence reconciled.

**Proposed landing subject:** `W7-D5: Amend manifest registry classification`

## 7. Acceptance criteria

Tara and Ari should be satisfied, before this amendment lands, that:

- the cited test law and the `W6-CAT` precedent are exactly as the evidence report stated;
- the v1.3 diff touches exactly the section 4 sites;
- the dependency direction is acyclic: `W7-D5-RUN-01` depends on `W7-D5-SEC`, never the reverse;
- nothing here alters the manifest bytes, the GER bytes, the run accounting, or any succession or seam law;
- Landing B remains exactly 35 paths;
- after this amendment, the Landing B candidate can satisfy the registry law without editing any proof outside its authorised scope.

## 8. Constitutional and boundary check

This amendment introduces no real-person data, no identified person's wellbeing material, no credential or private configuration, no machine-identifying detail, no model binary, and no private adoption implementation detail.

**Any real-person adoption is a separate governed authority outside this repository.**
