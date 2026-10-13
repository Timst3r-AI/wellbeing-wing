# W8-D3 — Calibration Completion Record

**Status:** Accepted by human reviewer, 2026-10-13. **Effective only on publication and remote verification.**
**Date:** 2026-10-13
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D3 — Synthetic calibration (landing **D3-D**, reveal, comparison and completion)
**Identity:** `W8-D3-CCR`, type `phase-record`
**Position:** the reveal landing and completion record of W8-D3 on the session corpus that ADR-0059 binds. **It amends no disposition, diagnoses no divergence and derives no rate, score or readiness interpretation.** The original corpus's retained records stay sealed under their own authority.
**Derived public baseline:** `317c0ba9de76853d454774085cdf18f3a638c02f`, the published and remotely verified proof correction `W8-HAC`; the session corpus stays bound to the supplementary authoring landing: commit `83253039ec274a2496b37b618949fd00d3cd7c8e`, home tree `a00a0be832ba597ec2f2b68e19ca37d29af58f6d`, manifest `sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28`
**Governed by:** ADR-0057 as reconciled by ADR-0059, whole, its Parts D to H especially; ADR-0059, whole, its decisions 9 to 11 and 27 to 28 especially; the effective `W8-D3-SCB` as reconciled, its sections 3.4 and 6 to 8 especially; `W8-D3-HDR` and governed register `W8-D3-DR-01`; `W8-S1-SCR` and `W8-S1-CM-01`; `W8-HPC` and `W8-HAC`; ADR-0058, whole, its decision 5 operative; **ADR-0054, whole — carried, never reinterpreted**; ADR-0055 as reconciled; the effective `W8-D2-CBC`; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**The reviewer wrote first, in public, and the writing was fixed. Then the seals were checked byte for byte, the sealed construction hypotheses were read, and the two were set side by side — case by case, as agreement or divergence, and as nothing more.**

## 1. The ordered sequence

1. **The session landing was published and independently remote-verified before anything here began**, and its dispositions were fixed at that publication. The reveal landing's preparation then waited for the proof corrections `W8-HPC` and `W8-HAC`, each separately accepted, published and remote-verified, and restarted from re-grounding over `W8-HAC`.
2. **Every published commitment of the session corpus reproduced by hashing the exact retained bytes directly, read-only, before any parse** (ADR-0057 decision 15): all twelve expected records present by exact name in that corpus's own custody sub-location, and each hashing to its published commitment in `W8-S1-CM-01`. **No retained record of the original corpus was listed, opened, parsed, hashed, copied or moved by any act of this landing**, and no retained record was deleted, rewritten or moved.
3. **Only after every commitment reproduced were the exact retained bytes copied**, without parsing, normalising, rewriting or reserialising them, to the reveal-candidate paths `governance/discriminating-reveal/<case_id>.json`, for the session corpus's identities only; each copy hashed to its published commitment (ADR-0057 decision 16).
4. **The landing scan ran over exactly the twelve candidate copies and found nothing; the scanner was never run against the custody location.** No suppression, redaction or byte repair was made or needed (ADR-0057 decision 17). **The location is never named in any surface.**
5. **Only after that clean scan were the copies parsed.** Every revealed record passes the published withheld-record validator and binds to its identity, its filename, its row in `W8-S1-CM-01` and the published digest of its reviewer-visible case (ADR-0057 decision 18).
6. A proof over named custody records establishes binding mechanics only; the reproduction, the copy and the non-access above are governed process duties, honoured and recorded here, never proven by a test, and no proof in this landing reads custody.

## 2. The reveal

7. **The reveal publishes the exact retained bytes** of the session corpus's twelve withheld authoring records at `governance/discriminating-reveal/<case_id>.json`, never a reserialised, normalised or redacted form (ADR-0057 decision 19). They are bound by `W8-S1-CM-01` and are not individually registered. Before the first commit the proofs read the candidate copies exactly as written, unconverted; once committed, they read the committed objects with the working-copy correspondence check `W8-D2-CBC` carries.

## 3. The case-level comparison

8. **For each case of the session corpus the comparison records exactly the case identity, the human token from the published register, the authored intended token from the revealed record, and one relation from the closed set `agreement` · `divergence` — `agreement` exactly when the two tokens are byte-identical (ADR-0057 decision 20).** That is the whole of the comparison.

| Case identity | Human token | Authored intended token | Relation |
|---|---|---|---|
| `W8-C-14f93190ba019aa16ea961007abe23cd51f947125e834419f0b63872d0779149` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-1666151a089432a8937fcf8e61da58779171824a222761a1d918949730acf411` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-1ef4bd851e1bb8d0723e7aedf5307f046978946eb91211d8f9758d0710db4cfd` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-496af3eb9d5c89ebd67b62e8afc1ab777b438f7c67022f6a6904d6e48832a221` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-54f38b9cb5a756f97d3ed892347d3ae9b15b370a52ac90dfe84f85b5c8c50078` | `governance_delta_present` | `review_inconclusive` | `divergence` |
| `W8-C-562c474188435ba11ad566c98917bccbca835c1444f0de6f1ffdffa7132240a7` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-5ce90240d880f9284536f12d5479325714e8299911be730d32c30036c3aa481f` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-605199fd8984c2cee0820d47c3af8e142059dd898fc1b5c974f8c5597031d671` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-6be6f92228d2a556afd95e4a37f184ee63aa2d5be824cac6e011de5e3381ef9b` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-718e554e341126ea0e7dbd998a6bea9779ff27a1e33e0c410c798548e3626009` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-cda57fc7860eff6f9d02076e309c989ec1fd21e2fa7a268604a2e8dc7fff3eac` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-f4898f3869091d114602f2781446e5ff3004c663426004b1512712e6b5001ecb` | `governance_delta_present` | `governance_delta_present` | `agreement` |

9. **An authored intended token is a construction hypothesis, never an answer key and never a certified correct answer.** **A divergence is recorded, never explained away, never corrected and never attributed to the reviewer;** its diagnosis belongs to a later governed act, not to W8-D3 (ADR-0057 decision 21). **Revealed material is post-disposition calibration material only and never becomes evidence for, replaces or amends a disposition.**
10. **The dispositions were fixed at the session landing's publication, and none is amended by any route.** The register and the session record are byte-unchanged by this landing.

## 4. The permitted counts

11. **Exactly two kinds of count are published: per-token counts of the session corpus's human dispositions, all three tokens with zero counts included, and per-relation counts of `agreement` and `divergence`. Each count carries, in the same place, its statement (ADR-0054 decision 31; ADR-0057 decision 22).**

| Kind | Count | Statement |
|---|---|---|
| `governance_delta_present` | 6 | a count of individual human acts and nothing more |
| `no_governance_delta` | 3 | a count of individual human acts and nothing more |
| `review_inconclusive` | 3 | a count of individual human acts and nothing more |
| `agreement` | 11 | a count of individual human acts and nothing more |
| `divergence` | 1 | a count of individual human acts and nothing more |

12. **No percentage, rate, score, grade, ranking, threshold, pass/fail result, model-performance claim or readiness interpretation is derived, published or implied.** A column of identical marks would itself be a finding, never a success (ADR-0057 decision 23).

## 5. Proof successions at this landing

13. **Exactly the successions that ADR-0059 Part G decision 27 stages for the reveal landing move, each an exact transformation of its fixed pre-image at the derived public baseline, proven by RC10:**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_discriminating_instrument_envelope.py` | V12 | `sha256:e7e80df8dbad8397574b9558a3892ac638e16e0d3549e2662e6181a55bb6944e` | `sha256:99047ceb3f58f5209598d9eb84cd6972cc2786ca4e7a43ce1dfbfe8f592d7323` |
| `tests/test_w8_discriminating_instrument_corpus.py` | C10 | `sha256:7e9a5e7d7101c33fa3a79bf5979411b8c8a1da989731fcdbd0ca911766e22698` | `sha256:1d9ffef924e73d10d70e23e08b54ce5ea8e50051dfcc4f556f88b56321b20652` |
| `tests/test_w8_calibration_law.py` | K12 | `sha256:448e1aa056a9ce176d7ae1b1856bb6eb459b8e1180fc0eae341419c5c19dc328` | `sha256:2dca05bbd21544cdd3e524e59c2e431172e88e571441a22588f47a9f2141e36f` |
| `tests/test_w8_session_recovery_law.py` | R7, R8, R9 | `sha256:8934a5248504228a0950f5afedc523a377e063746d3e18e37dced914855219ea` | `sha256:9c1c6dd6c534ce1fd8400442259e5da87c35821c19708695f513b4265a56bd2b` |
| `tests/test_w8_supplementary_corpus.py` | S10 | `sha256:4a810d1be35c82f556362a9497624174351ce81d3e90b9241b3f88b116fc833e` | `sha256:b90ec8624d156579898094fb4996c73d1aad4c7d9e638f4d04ad26f3a72b6731` |

14. K12's reveal limb and R8 admit exactly the session corpus's identities in the reveal home, the former absence staying proven at their own landing commits and at the derived public baseline; R7's entry set admits this record; the envelope module's schema-string and case-home limbs admit the reveal home; the corpus module's C10 scope and the supplement module's freshness scope exclude it; and R9's board sentence succeeds again, to *No divergence is diagnosed, explained away or corrected.*, its earlier form staying proven at the derived public baseline. The corpus C7 board limb does not move, because the board wording of this landing names no reserved field. **No other existing proof moves at this landing.**

## 6. Proof obligations

15. **Twelve obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_reveal_calibration.py`:**

| # | Obligation | Decidability |
|---|---|---|
| **RC1** | The reveal home holds exactly the session corpus's twelve identities, tracked and on disk, and held nothing at the derived public baseline | **Mechanical** |
| **RC2** | Every revealed file hashes to its published commitment; before the first commit read exactly as written, afterwards as the committed object with its working copy corresponding | **Mechanical** |
| **RC3** | Every revealed record passes the published withheld-record validator, is in canonical bytes, and binds to its identity, filename, manifest row and published visible digest | **Mechanical** |
| **RC4** | The ADR-0059 validation chain holds through the reveal, refusing a premature, partial or original-corpus reveal | **Mechanical** |
| **RC5** | The comparison table, read whole within its section, is exactly the mechanical one: its exact header and separator, then exactly twelve rows of exactly the four permitted fields in ascending identity order, the published human token, the revealed authored intended token, and agreement exactly on byte-identical tokens; any malformed, surplus, duplicate or stray row is refused, never skipped | **Mechanical; neither side is a certified correct answer** |
| **RC6** | The count table, read whole within its section, holds exactly the five permitted rows in fixed order, zeros included, each an integer count equal to the mechanical one and carrying its exact statement; any unknown, malformed, duplicate or surplus row is refused, never skipped; and the record carries no ratio, percentage or rate | **Mechanical** |
| **RC7** | The register and the session record are byte-unchanged: no disposition is amended | **Mechanical** |
| **RC8** | This record carries its sequence, reveal, comparison, count, non-diagnosis, non-amendment and closure statements, each once, and the nine rules | **Mechanical** |
| **RC9** | No authored class, rationale, construction map, check, label, nonce or schema literal leaves the reveal home through this record, the new registry role or the board wording this landing adds; the role and board carry no token or count | **Mechanical** |
| **RC10** | The staged successions are the exact transformations pinned in section 5 | **Mechanical** |
| **RC11** | The registry and the board change exactly as authorised, in draft or accepted form, with no revealed record individually registered | **Mechanical for binding; acceptance is the human act** |
| **RC12** | This landing's census is exactly decision 16's | **Mechanical** |

## 7. Census and completion

16. **This landing's census is exactly twenty-one paths:** NEW twelve `governance/discriminating-reveal/<case_id>.json` · NEW `docs/phases/W8-D3-calibration-completion-record.md` · NEW `tests/test_w8_reveal_calibration.py` · MODIFY `tests/test_w8_discriminating_instrument_envelope.py` · MODIFY `tests/test_w8_discriminating_instrument_corpus.py` · MODIFY `tests/test_w8_calibration_law.py` · MODIFY `tests/test_w8_session_recovery_law.py` · MODIFY `tests/test_w8_supplementary_corpus.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`.
17. **On this record's acceptance, publication and independent remote verification, W8-D3 is complete in the accepted sense.** W8-D4 through W8-D7 remain closed behind their own briefs. The original corpus's retained records stay sealed in their existing custody; their custody, retirement or eventual reveal needs its own separately governed act, which this record does not choose (ADR-0059 decision 19).

## 8. Doctrine carriage

18. The nine anti-collapse rules carry whole:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

## What this record does not establish

19. This record establishes no correctness of any human token or authored intended token; no answer key; no diagnosis, explanation or correction of any divergence; no rate, score, grade, ranking or readiness of anything; no finding about the reviewer, the reviewer's independence or the absence of influence; no comparability between any two corpora; no claim about the original corpus's retained bytes; no model behaviour of any kind; no classification of any exchange under ADR-0047 decision 3; and no resolution of ADR-0047 precondition 3 or of any carried state. **No disposition or count in this record may be cited as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — reveal, commitment, comparison, count, reviewer, custody. Roles only, under ADR-0056. No case text is quoted and no case is characterised; the comparison carries identities and tokens only. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*Written first, sealed apart, opened last: what the reviewer judged and what the author built now stand side by side, agreeing where they agree, diverging where they diverge, and claiming nothing more.*
