# W8-D2 — Committed-Blob Proof Correction

**Status:** Accepted by human reviewer, 2026-10-08. **Effective on publication and remote verification.**
**Date:** 2026-10-08
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D2 — Discriminating instrument
**Identity:** `W8-D2-CBC`, type `phase-record`
**Position:** a bounded correction of the W8-D2 corpus proof implementation. It changes which bytes three proof limbs read for the immutable published D2 artefacts, and nothing else. **It opens no deliverable: W8-D3 through W8-D7 remain closed behind their own briefs.**
**Derived public baseline:** `571ac0076590c6b3346f53ef828bc0c1ad2f9cad`, the published state after the ADR-0056 public-identity remediation
**Governed by:** ADR-0055 whole, especially decision 10; the W8-D2 completion record `W8-D2-DIC` and governed register `W8-D2-CM-01`; the effective `W8-D2-DIB`; ADR-0054; the W8 runway; the `W7-D5-PSA` and `W8-D2-MSA` bounded-correction precedent
**Tier at landing:** J — Judgment. Full ceremony.

---

**The cases were never wrong. The proofs were reading the wrong copy of them. A fresh checkout may rewrite the last byte of every line for the convenience of the machine it lands on; the published artefact is the committed object, and that is now what the byte-exact proofs read.**

## 1. The defect

1. On a fresh clone under the default configuration of a widely used Git distribution — line-ending conversion enabled at system level, and no attributes file in the repository — checkout rewrites the final line ending of each published case file and of the commitment manifest from LF to CR LF. **The published corpus proofs C2, C4 and C5 read those working-tree bytes and fail: 25 failures** — twelve in C2, one in C4 and twelve in C5. Under an LF checkout the same proofs pass.
2. **The committed artefacts were never wrong.** Every committed case and manifest object is byte-for-byte the canonical bytes the proofs require. The defect is that three byte-exact proofs depended on how a checkout chose to display those bytes. ADR-0055 decision 10 had already settled which bytes are the artefact: the canonical bytes are the artefact, and everything else is display.

## 2. The correction

3. **C2, C4 and C5 now read the committed object bytes** of the twelve published cases and the commitment manifest, at the current commit, from the Git object store. Their assertions are unchanged: the same validator, the same exact-canonical-bytes check, the same single-terminal-LF check, the same mechanical-filename check, the same container law and the same one-to-one digest binding, with the same planted-mutant controls.
4. **Pre-commit detection is preserved, not traded away.** Reading committed bytes alone would let a working-tree change to an immutable artefact pass until it was committed. Each byte-exact limb therefore also requires that **the working copy, with checkout line endings undone, is exactly the committed bytes** — so any content change to a case or the manifest, staged or not, still fails before commit, while a line-ending rewrite alone does not.
5. **The scope is held.** Only the immutable published D2 artefacts are read from committed objects. Every other read is unchanged: the registry, the phase board and the completion record are still read from the proposed working tree, and the parse-only and line-ending-normalised reads were never environment-dependent.
6. **Nothing else moves:** no case byte, no manifest byte, no commitment, no ADR, no D2 completion state, no registry binding of any D2 artefact, no other proof limb, no attributes file and no repository configuration.

## 3. Evidence, measured in disposable fresh clones of the baseline

7. **Under default line-ending conversion:** the published module failed with 25 failures and 315 passing subtests; the corrected module passed, 10 tests and 357 subtests.
8. **Under an LF checkout:** the published module passed, 10 tests and 344 subtests; the corrected module passed, 10 tests and 357 subtests. The thirteen added subtests are the working-copy correspondence checks — twelve in C2 and one in C4.
9. **Detection matrix** (LF clone, each mutation restored before the next): a line-ending-only rewrite of a case working copy — flagged by the published module, correctly passed by the corrected one; a one-byte content change to a case working copy, a one-digit change to the manifest working copy, and a staged content change to a case — each detected by both modules.

## 4. What this correction does not do

10. It performs no disposition, no review session, no custody act, no commitment reproduction, no reveal and no calibration; it contacts no model; and it opens nothing. **D2 remains complete as built, W8-D3 remains closed, and ADR-0047 precondition 3 remains outstanding in its lawful resting state.** Every carried state stays exactly where it was — no cleanup by proximity.

## Public-safety note

Generic and structural wording throughout — proof, object, checkout, line ending, artefact. No case text is quoted. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*A proof that passes on one machine and fails on another is not proving the artefact; it is proving the machine. This correction points the proofs back at the thing that was published, and leaves the thing itself exactly as it was.*
