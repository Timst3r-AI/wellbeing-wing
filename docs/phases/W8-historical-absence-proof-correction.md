# W8 — Historical-Absence Proof Correction

**Status:** Accepted by human reviewer, 2026-10-13. **Effective only on publication and remote verification.**
**Date:** 2026-10-13
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** none — a phase-level proof-implementation correction, outside W8-D3
**Identity:** `W8-HAC`, type `phase-record`
**Position:** a bounded correction of how the D3-C proof H9 checks absence. **It amends no law, moves no case, manifest, register, session record, procedural account or custody, renders no packet, records no disposition and opens no gate.** D3-C stays effective and its dispositions stay fixed. The reveal landing stays paused before custody access until this record is effective.
**Derived public baseline:** `66b6e6ca7e33e5e0fd326d61653a0c13d1679878`, the published and remotely verified D3-C session landing
**Governed by:** ADR-0059, whole and unchanged, its decisions 27 and 28 included; the effective `W8-D3-SCB` as reconciled, its sections 3.4, 8 and 11 included; ADR-0057 as reconciled; ADR-0058; `W8-D3-HDR` and `W8-D3-DR-01`; **ADR-0054, whole — carried, never reinterpreted**; `W8-HPC` as precedent only; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**An absence proven at a landing is history, and history should be read from the commit that made it. This record lets one proof keep its history and stop vetoing the future, and claims no more authority than that.**

## 1. The defect

1. **The D3-C proof H9, in `tests/test_w8_disposition_record.py`, proves that nothing of the reveal landing existed at the session landing.** Its tracked-path and registry checks read the D3-C snapshot, and stay true at that commit for good. Two of its assertions, however, read the **present filesystem**: that no reveal home and no completion record exist on disk.
2. **The reveal landing must create exactly those two things.** H9 would therefore refuse the reveal landing's authorised artefacts whatever their bytes. H9 is not in ADR-0059 Part G decision 27's closed list of reveal-landing successions, nor in the D3 brief's section 3.4 census. Decision 28 adds "No other proof moves".
3. **The defect was found by the reveal-landing preparation, which stopped before any custody access**, and the stop was upheld on independent architectural review. A placeholder probe showed that H9 was the only refusal outside the authorised successions. The defect passed the session landing's review and tests because nothing then existed on disk. **It lies in H9's implementation; no law, doctrine, disposition or human act is at fault**, and the session landing's published bytes are as accepted.

## 2. Authority and scope

4. **ADR-0059 decision 28, and the D3 brief's closed succession list as ADR-0059 reconciles it, bind the reveal landing. That landing cannot change H9, or add a twenty-second path, on its own authority, and this record does not claim that it could.**
5. **This record is a separate governing act of the human authority, held at phase level and outside W8-D3, Tier J, effective only on its own acceptance, publication and independent remote verification.** It is not a landing that ADR-0059 permits, and it adds nothing to ADR-0059's Part G list. **It authorises exactly one bounded implementation change, at its own landing: H9's two present-filesystem assertions run only while the D3-C snapshot is uncommitted.** Nothing else is authorised.
6. **This scope settlement is express, and it takes effect only through the human authority's acceptance of this record, which adopts it.** No proof edit, registry classification, architectural review or green test adopts it. `W8-HPC` informs the route as precedent only, and supplies no permission for this change.
7. **What stays unchanged:**
   - ADR-0059's text, its decisions 27 and 28 and its Part G staging; every succession of the reveal landing, exactly as decision 27 stages it; ADR-0054, ADR-0055, ADR-0057, ADR-0058 and the D3 brief, all byte-untouched;
   - H9's snapshot selection, its fatal validation and every historical absence assertion. The former absence stays proven at the D3-C commit, and the existing current-state guards, K12 and R8, keep their duties until their authorised reveal-landing successions;
   - D3-C's effective status, its register and its procedural account, and the session corpus's binding to the supplementary authoring landing;
   - the behaviour of every other proof.
8. **This correction is a prerequisite of the reveal landing.**
   - The reveal landing's preparation stays paused before custody access until this record is effective. Whether it then resumes is the human authority's act.
   - On resumption, its baseline becomes this correction's commit, and its session corpus stays bound to the supplementary authoring landing under ADR-0059 decision 9.
   - Its strict sequence restarts from the beginning: re-grounding, reproduction from the exact retained bytes, the byte copy, the scan of the copies and only then any parse.

## 3. The exact change

9. **The change is two sites, both inside H9, in `tests/test_w8_disposition_record.py`:**

```diff
         with self.subTest(fact="no reveal home, tracked or on disk"):
             self.assertEqual([p for p in tracked
                               if p.startswith(REVEAL_HOME + "/")], [])
-            self.assertFalse((ROOT / REVEAL_HOME).exists())
+            if commit is None:
+                self.assertFalse((ROOT / REVEAL_HOME).exists())
         with self.subTest(fact="no completion record and no later entry"):
             self.assertNotIn(COMPLETION_RECORD, tracked)
-            self.assertFalse((ROOT / COMPLETION_RECORD).exists())
+            if commit is None:
+                self.assertFalse((ROOT / COMPLETION_RECORD).exists())
```

10. **The snapshot is the existing `l3_snapshot()`.** It identifies the one commit that added the register and requires its sole parent to be the `W8-HPC` landing; before that commit exists, it admits the working candidate only over that fixed baseline. **H9's assertion that the snapshot reports no problems stays ahead of both conditional checks, so a failed snapshot remains fatal.** No movable branch reference is substituted.
11. **Nothing is broadened.** The tracked-path and registry assertions are unchanged and still read the D3-C snapshot, refusing any reveal path, completion record, completion entry or later-deliverable entry in that history. Before the D3-C commit, both present-disk assertions run exactly as before.

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_disposition_record.py` | H9 | `sha256:14e1c88341a387335df6c87ea04546fbfc1714ed987b94b1335b4d5e3429c77d` | `sha256:cbbc829168ee0077b926655557c6bc761c3284ec4b725a3f28b755a74ae3fb9d` |

## 4. Census and human acts

12. **This landing's census is exactly four paths:** MODIFY `tests/test_w8_disposition_record.py` · NEW `docs/phases/W8-historical-absence-proof-correction.md` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. Any need for a fifth path is a further stop.
13. **Standing duties at this landing:** P2 and Q3; P4a reported separately; **a fresh P4b human act**; acceptance; publication only as the ADR-0056 public project identity; and independent remote verification. Mechanical evidence never substitutes for a human act. That evidence is the exact edit, the full suite, the scans, and the historical, pre-commit and future-state controls, reported with the candidate.

## What this record does not establish

14. This record establishes none of the following:
    - no case, corpus, manifest, register, session record, packet, disposition, custody access, commitment reproduction, reveal, comparison or count;
    - no amendment of any law, and no succession for any D3 landing;
    - no reviewer route of any kind;
    - no classification of any exchange under ADR-0047 decision 3;
    - no model behaviour of any kind;
    - no resolution of ADR-0047 precondition 3 or of any carried state.

    **No disposition ever made may cite this record as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — proof, snapshot, absence, landing, record. Roles only, under ADR-0056. No case text is quoted and no case is named, and no association or figure from the void attempt appears. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*What was absent then stays proven absent then; what comes next is left to the proofs that were written to admit it.*
