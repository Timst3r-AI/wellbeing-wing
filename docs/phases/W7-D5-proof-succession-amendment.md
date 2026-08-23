# W7-D5 - Proof Succession Scope Amendment

**Status:** Accepted by human reviewer, 2026-08-23. **Effective on publication and remote verification.** It authorises the two bounded H12 and M6 succession edits for the successful Landing B candidate only; at its own landing it edits neither proof module, creates no home, allocates no GER identifier and begins no run.

**Date prepared:** 2026-08-23  
**Phase:** W7 - First-Contact Governance and Synthetic Model Evaluation  
**Deliverable:** W7-D5 - Synthetic execution records and first generated-evaluation materialisation  
**Identity:** `W7-D5-PSA`, type `phase-record`  
**Amends:** `W7-D5-SEB` (`docs/phases/W7-D5-synthetic-execution-materialisation-brief.md`), revision v1.1 to v1.2  
**Architect:** Ari  
**Builder/executor after acceptance:** Eli  
**Human authority:** Tara  
**Baseline for this candidate:** `77e388dd3af57ec0dbc445ecf02fa7ca4e434dbc` - `W7-D5: Govern first synthetic execution materialisation`  
**Baseline registry state:** 113 entries, last `W7-D5-SEB`

---

## 1. Why this amendment exists

W7-D5 implementation preparation stopped **before preflight and before any capture**. `W7-D5-RUN-01` was not consumed: no disposable run clone was created, no preflight check ran, and no specimen was admitted. The authoritative repository was untouched at the published Landing A state.

The stop was triggered by a pre-implementation sweep of the whole proof corpus for present-state assertions that a successful materialisation would break. The accepted brief's section 24 designs proof succession for exactly three assertions in `tests/test_w7_generated_evaluation_shape.py`. The sweep found two more assertions of the same class in modules the brief does not permit to change:

1. **`tests/test_w7_synthetic_harness.py`** - the frozen D4 proof module, hash-pinned by brief section 6, any edit a section 34 hard stop. Its `H12_ProofSuccession.test_h12_vacancy_holds_now_and_the_successor_bites_on_fakes` carries an unconditional limb asserting that `governance/generated-evaluation/` does not exist on disk and has no tracked file.
2. **`tests/test_w7_model_boundary_decision.py`** - the D3 model-boundary proof module, absent from the brief's 33-path successful landing scope. Its `RepositoryStateAtThisLanding.test_m6_home_absent_and_no_ger_identifier_allocated` carries unconditional limbs asserting the same absence, alongside a registry limb (no `GER-####` registry identifier) that remains true after D5.

A successful Landing B necessarily makes both vacancy assertions false, while brief section 37 items 2 and 5 require both modules green over the exact proposed tracked state. The successful candidate was therefore impossible without either exceeding the brief's scope or landing red proofs. Implementation stopped and reported rather than improvising, and Ari independently confirmed both contradictions against the published `77e388dd` state.

## 2. Character of the correction

**The correction is architectural, not doctrinal.** No decision of ADR-0046 through ADR-0052 changes. ADR-0051 Option D stands. `W7-D4-SHR` and every historical completion record are unchanged and require no erratum: each was true when it landed, and the two assertions were true of the repository at their own landings. What failed was forward scope - the v1.1 brief succeeded three present-state assertions and did not scope the other two. This amendment corrects the scope by the doctrine-first pattern: the amending record lands first, and implementation consumes the corrected law second.

## 3. The ten settlements

1. **The D4 exam and harness remain permanently byte-frozen** at their existing published hashes: `fixtures/SYNTHETIC-w7-d4-exam.json` at `9755cca1e8f9e41d7c89d532abb2f674a0189ec58935e3a5763fd641c90406a7` and `tests/w7_synthetic_evaluation_harness.py` at `e50172f5393a8753c9f4a93e29ef52e50cd366c0539a7c483787c085ea31f1fb`. Nothing in this amendment loosens either.
2. **`tests/test_w7_synthetic_harness.py` hash `6da85d5b2b745e6156d7317f8859fde393489fee8b6df963310a9ebac747d860` becomes the D5 pre-succession baseline pin.** Only H12 may receive the bounded successful-materialisation succession edit; every other byte of the module must remain identical to the pin.
3. **`tests/test_w7_model_boundary_decision.py` is pinned pre-succession at `3748a16b219404fcd8d3686431adecc3713850aa3d2983f52d38a2970a45e722`.** Only M6 may receive the bounded successful-materialisation succession edit; every other byte of the module must remain identical to the pin.
4. **H12 succession design.** The vacancy limb becomes a from-published-history proof: the reserved home had no tracked artefact at every commit up to and including the parent of the first authorised materialisation commit. H12 retains its disposable-home successor checks unchanged. **Current real-home conformance is owned by D5's materialised-state proof module, not by H12** - H12 makes no claim about the real home's present contents after materialisation.
5. **M6 succession design.** The home limbs become a from-published-history proof of the ADR-0051 landing-era condition: no generated-evaluation home and no GER allocation existed at the ADR-0051 landing, and none existed at any commit up to and including the parent of the first authorised materialisation commit. M6 no longer asserts current vacancy after D5. M6's registry limb - no registry entry id beginning `GER-` - remains a current-state assertion and remains true after D5.
6. **Neither succession edit occurs on a stopped `RUN-01`.** Both edits may enter only the successful Landing B candidate. A stop landing under brief section 21.4 remains exactly three paths and touches neither module.
7. **Successful Landing B changes from exactly 33 paths to exactly 35 paths**, adding `tests/test_w7_synthetic_harness.py` (H12 succession only) and `tests/test_w7_model_boundary_decision.py` (M6 succession only) to the implementation/proof group.
8. **Brief section 37 still requires both complete modules green** against the exact successful proposed tracked state, after their authorised succession edits. Greenness of the edited modules is measured over the whole module, not over the edited test alone.
9. **No other D3 or D4 proof, decision, exam, harness, engineering or doctrine byte is authorised to change.** The succession edits are bounded to the two named tests. Any wider diff in either module against its pre-succession pin is a hard stop.
10. **The inherited-present-state-assertion sweep joins the standing architecture review discipline.** Before any future materialisation-class brief is accepted, the whole proof corpus is swept for present-state assertions the landing would break, and every hit is either explicitly succeeded by the brief or explicitly declared unaffected. The v1.1 omission survived two independent read-only reviews; the sweep is the check that found it, and it is now a named review step rather than an accident.

## 4. Brief reconciliation to v1.2

The accepted `W7-D5-SEB` brief is reconciled to revision v1.2 in the same landing as this record, per the live amendment precedent: content changed at enumerated sites, registry content hash recomputed in the same commit, and a dated note appended to the `W7-D5-SEB` registry entry pointing here.

The v1.2 reconciliation touches exactly these sites and nothing else:

1. header revision line: v1.1 to v1.2, naming this amendment;
2. section 6: the closing byte-drift paragraph distinguishes the permanently frozen exam and harness from the pre-succession D4 proof pin and its bounded H12 authorisation;
3. section 24: a new subsection 24.4 carries the H12 and M6 succession designs of settlements 4-6;
4. section 34 hard-stop 8: reworded so a D4 harness or exam edit remains an unconditional hard stop while the bounded H12 succession edit authorised here is not one, and any D4 proof edit beyond it is;
5. section 35: the successful landing scope becomes exactly 35 paths, the implementation/proof group grows to five paths (items 31 and 32 naming the two bounded module successions), the governance group renumbers to 33-35, and the exclusion line for the D4 proof module carries the bounded-H12 exception;
6. section 37: items 2 and 5 state that the two modules are measured complete and green after their authorised succession edits; item 12's landing-scan count becomes 35;
7. section 38.1: the P4b review target becomes the 35-path final candidate;
8. section 39: ceremony steps 4, 8 and 12 count 35 paths;
9. section 45: the instruction freezes the exam and harness permanently, holds the two proof modules at their pre-succession pins, and applies only the bounded H12 and M6 succession edits in the successful Landing B candidate.

No other line of the brief changes. The acceptance status, Landing A scope, run identity and retry law, GER lifecycle, retention, authority split, namespace transition, stop-and-report form, registry mechanics, and every other section of v1.1 are carried byte-identically.

## 5. What this amendment does not do

At its own landing this record:

- creates no `governance/generated-evaluation/` home and no artefact of the class;
- allocates no `GER-####` identifier and leaves the registry namespace declaration untouched and true;
- begins no run: `W7-D5-RUN-01` remains unconsumed;
- edits neither proof module: both remain byte-identical to their pre-succession pins until the successful Landing B candidate;
- changes no D4 exam or harness byte;
- contacts no model and produces no generated output;
- adds no dependency and touches no scanner or allowlist line;
- resolves neither Part Q nor the `local-wordlist` coordinate seam;
- discharges no ADR-0047 precondition: precondition 3 remains outstanding;
- opens neither W7-D6 nor W7-D7 nor W8.

## 6. Landing scope of this amendment

Exactly four paths:

1. new `docs/phases/W7-D5-proof-succession-amendment.md` (this record);
2. modify `docs/phases/W7-D5-synthetic-execution-materialisation-brief.md` to revision v1.2 at the section 4 sites;
3. modify `governance/registry.json`: one new `W7-D5-PSA` entry, and the `W7-D5-SEB` entry's content hash recomputed with a dated amendment note appended;
4. modify `docs/phases/README.md`: one `W7-D5-PSA` row and the W7-D5 status sentence reconciled.

**Proposed landing subject:** `W7-D5: Amend proof succession scope`

## 7. Acceptance criteria

Tara and Ari should be satisfied, before this amendment lands, that:

- both pre-succession pins equal the published blobs at `77e388dd`;
- the v1.2 diff touches exactly the section 4 sites;
- the succession designs prove history, not present vacancy, and claim nothing about post-materialisation real-home contents that belongs to the materialised-state module;
- the stop path still touches neither module;
- nothing here weakens Part Q, the wordlist seam, Option D, P4a/P4b, or any ADR-0046 through ADR-0052 decision;
- after this amendment, the successful Landing B candidate can satisfy brief section 37 without any act outside its authorised scope.

## 8. Constitutional and boundary check

This amendment introduces no real-person data, no identified person's wellbeing material, no credential or private configuration, no machine-identifying detail, no model binary, and no private adoption implementation detail.

**Any real-person adoption is a separate governed authority outside this repository.**
