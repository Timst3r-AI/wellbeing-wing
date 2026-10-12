# W8 — Historical-Pin Proof Correction

**Status:** Accepted by human reviewer, 2026-10-13. **Effective only on publication and remote verification.**
**Date:** 2026-10-12
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** none — a phase-level proof-implementation correction, outside W8-D3
**Identity:** `W8-HPC`, type `phase-record`
**Position:** a bounded correction of how ADR-0059's proof A3 derives the historical pins it permits. **It amends no law, moves no case, manifest, register, session record or custody, renders no packet, records no disposition and opens no gate.** It is a prerequisite of the rebuilt D3-C session landing; D3-D stays unopened.
**Derived public baseline:** `83253039ec274a2496b37b618949fd00d3cd7c8e`, the published and remotely verified supplementary authoring landing
**Governed by:** ADR-0059, whole and unchanged, its decision 28 included; `W8-S1-SOB` and `W8-S1-SCR`; the effective `W8-D3-SCB` as reconciled, its section 8 closed list and section 11 stop conditions included; ADR-0058; ADR-0057 as reconciled; **ADR-0054, whole — carried, never reinterpreted**; `W8-D2-CBC` and `W7-D5-PSA` as precedents only; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**A proof that checks history against the present will one day mistake a lawful change for a forgery. This record lets one proof read its history from the commit where that history was written, and claims no more authority than that.**

## 1. The defect

1. **ADR-0059's proof A3 checks that ADR-0059 carries no digest-shaped string other than its own pins.** For the Part F post-image pins it permits, it hashed the **present working-copy bytes** of the five Part F sources: ADR-0055, ADR-0057, the D3 brief, the D2 brief and the ADR-0058 proof module.
2. **Those post-image pins are historical: ADR-0059 decision 21 fixes them at its own landing.** ADR-0059 Part G decision 26 then requires the ADR-0058 proof module to change at the session landing, through R7 and R9. Once it changes, its present hash no longer equals its true historical post-image pin, and A3 would reject ADR-0059's unchanged history as an unpinned digest. The same mechanism would recur at the reveal landing.
3. **The defect was found by the D3-C session-landing candidate, which stopped before any session artefact was staged, committed or published**, as ADR-0059 decision 28 and the D3 brief's section 11 require, because no landing ADR-0059 permits may move A3. The stop was upheld on independent architectural review. **The defect lies in A3's implementation of its own obligation; no law, doctrine or human act is at fault.**

## 2. Authority and scope

4. **ADR-0059 decision 28, and the D3 brief's section 8 as ADR-0059 reconciles it, close the list of proof successions for the landings ADR-0059 permits. Neither the session landing nor the reveal landing holds authority to move A3, and this record does not claim that either did.**
5. **This record is a separate governing act of the human authority, held at phase level and outside W8-D3, Tier J, effective only on its own acceptance, publication and independent remote verification.** It is not a landing that ADR-0059 permits, and it adds nothing to ADR-0059's Part G list. **It authorises exactly one bounded implementation change, at its own landing: A3 derives the Part F post-image pins it permits from the validated, fixed L1 landing snapshot instead of the present working copy.** Nothing else is authorised.
6. **This scope settlement is express, and it takes effect only through the human authority's acceptance of this record, which names it.** No proof edit, registry classification or architectural review adopts it. `W8-D2-CBC` and `W7-D5-PSA` inform the route as precedents only, and neither supplies permission for this change.
7. **What stays unchanged:** ADR-0059's text, its decision 28 and its Part G staging; A3's obligation in ADR-0059 decision 33; every succession of the session and reveal landings, exactly as Part G stages it; ADR-0054, ADR-0055, ADR-0057, ADR-0058 and the D3 brief, byte-untouched; and the behaviour of every other proof.
8. **This correction is a prerequisite of the rebuilt D3-C session landing**, which may be prepared only after this record is effective and on the human authority's separate instruction. That landing's baseline becomes this correction's commit, and its session-corpus binding stays the supplementary authoring landing's, under ADR-0059 decision 9.

## 3. The exact change

9. **The change is one site, inside A3, in `tests/test_w8_recovery_authority.py`.** Before:

```python
    def test_a3_no_case_token_schema_or_unpinned_digest(self):
        pins = [p.split(":", 1)[1] for _, p, _ in PREIMAGE.values()]
        pins += [_sha(worktree_text(rel).encode("utf-8")).split(":", 1)[1]
                 for rel in (A55, A57, SCB, DIB, R58)]
```

After:

```python
    def test_a3_no_case_token_schema_or_unpinned_digest(self):
        # Corrected by W8-HPC: the Part F post-image pins A3 permits are
        # read from the validated L1 snapshot, never from the working
        # copy, so an authorised later succession of a Part F source
        # cannot unpin ADR-0059's history.
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        pins = [p.split(":", 1)[1] for _, p, _ in PREIMAGE.values()]
        pins += [_sha(snapshot_text(commit, rel).encode("utf-8"))
                 .split(":", 1)[1] for rel in (A55, A57, SCB, DIB, R58)]
```

10. **The historical snapshot is the existing `l1_snapshot()`, which identifies the one commit that added ADR-0059 and requires its sole parent to be the ADR-0058 landing. Its reported failures stay fatal.** At this baseline it selects the published L1 landing `2bb87a308d4cc1ce795869bb94370d3bdc75ae0e`. No movable branch reference is substituted.
11. **A3's current-surface checks are preserved.** It still scans the present ADR-0059 and `W8-S1-SOB` texts, and the wording L1 added, for case identities, disposition tokens, reserved schema literals and labels, and unpinned digests, and its negative controls are unchanged. **The permitted pins are not broadened:** they are the Part F pre-images and the post-images as landed at L1, and no present hash is admitted. Present-state conformance of the reconciled sources stays owned by A4, by ADR-0058's R5 and by the staged succession proofs.

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_recovery_authority.py` | A3 | `sha256:ed8b7bdd012d8164e76d5cebc47c4190e3f8adbc254e1da91addd45d56a2901e` | `sha256:c1371e53ea1c3828f1a7aa348da3be1f83b63024a362cfcc5aad0b6014e3731b` |

## 4. Census and human acts

12. **This landing's census is exactly four paths:** MODIFY `tests/test_w8_recovery_authority.py` · NEW `docs/phases/W8-historical-pin-proof-correction.md` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`.
13. **Standing duties at this landing:** P2 and Q3; P4a reported separately; **a fresh P4b human act**; acceptance; publication only as the ADR-0056 public project identity, and independent remote verification. Mechanical evidence — the exact edit, the full suite and the scans — is reported with the candidate and never substitutes for a human act.

## What this record does not establish

14. This record establishes no case, corpus, manifest, register, session record, packet, disposition, custody access, commitment reproduction, reveal, comparison or count; no amendment of any law; no succession for any D3 landing; no reviewer route of any kind; no classification of any exchange under ADR-0047 decision 3; no model behaviour of any kind; and no resolution of ADR-0047 precondition 3 or of any carried state. **No disposition ever made may cite this record as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — proof, pin, snapshot, landing, record. Roles only, under ADR-0056. No case text is quoted and no case is named, and no association or figure from the void attempt appears. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The pin was right all along; only the place it was checked against had moved.*
