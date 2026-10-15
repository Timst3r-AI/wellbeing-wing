# W8 — Case-Home Scope Correction

**Status:** Accepted by human reviewer, 2026-10-15. **Effective only on publication and remote verification.**
**Date:** 2026-10-15
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** none — a phase-level proof-scope correction, outside W8-D4
**Identity:** `W8-CHC`, type `phase-record`
**Position:** a bounded correction of which homes the envelope module's V12 case-home limb admits. **It amends no law, moves no case, manifest, register, record or custody, renders no packet, records no disposition and opens no home in effect.** D4-C stays effective and its corpus stays fixed. D4-D preparation stays closed until separately authorised after this record is effective.
**Derived public baseline:** `f638cca75ec4a192685bf5cd53f29451cfdbbdd9`, the published and remotely verified W8-D4 corpus landing
**Governed by:** ADR-0060, whole and unchanged, its decisions 23, 38 and 39 included; the effective `W8-D4-IVB` and `W8-D4-VCR`; ADR-0059 decision 27 as precedent; `W8-HPC` and `W8-HAC` as precedent only; **ADR-0054, whole — carried, never reinterpreted**; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**A closed list should stay closed, and the way to settle what it left out is a separate act that says so. This record admits two named homes to one check, proves exactly that, and claims no more authority than that.**

## 1. The gap

1. **ADR-0060 decision 23 places the validation reveal records in two homes, `governance/validation-reveal/authoring/` and `governance/validation-reveal/construction/`, each holding `<case_id>.json`.** Their mechanical names carry the case prefix.
2. **The envelope module's V12 case-home limb refuses every tracked path carrying that prefix outside its admitted homes.** After the corpus landing those are the two W8-D2 and W8-S1 homes, the W8-D3 reveal home and the validation case home.
3. **Decision 38 stages the reveal landing's envelope authoring-schema succession and its VL10 succession, but not this limb, and its list is closed:** each staged succession is authorised only in its own landing and only as an exact transformation, and decision 39 makes any refusal outside the list a stop. The reveal records would therefore meet a refusal that no landing may lawfully move. ADR-0059 decision 27, the precedent, named both envelope limbs for its reveal home.
4. **The gap was found by the corpus landing's preparation, in its forward placeholder probes, and was confirmed by independent architectural review in two rounds.** Earlier cumulative probes had masked it, because the limb was already refusing the corpus landing's own stage. **It lies in the scope of decision 38's closed list; no doctrine, case, manifest, custody, human act or published byte of the corpus landing is at fault.**

## 2. Authority and scope

5. **Decision 38 and decision 39 bind every W8-D4 landing. Neither the session landing nor the reveal landing can change this limb, or add a path for it, on its own authority, and this record does not claim that either could.**
6. **This record is a separate governing act of the human authority, held at phase level and outside W8-D4, Tier J, effective only on its own acceptance, publication and independent remote verification.** It is not a landing that decision 38 permits, and it adds nothing to decision 38's list. **It authorises exactly one bounded change, at its own landing: the V12 case-home tuple admits exactly decision 23's two validation reveal homes, beside its four existing homes.** Nothing else is authorised. It amends no law and adds no succession to any W8-D4 landing.
7. **This scope settlement is express, and it takes effect only through the human authority's acceptance of this record, which adopts it.** No proof edit, registry classification, architectural review or green test adopts it. `W8-HPC` and `W8-HAC` inform the route as precedent only, and supply no permission for this change.
8. **What stays unchanged:**
   - ADR-0060's text, its decisions 23, 38 and 39 and its Part J staging, byte-untouched; every staged succession of the session, reveal and completion landings, exactly as decision 38 stages it, the reveal landing's envelope authoring-schema succession and VL10 succession included;
   - V12's vacancy limb and every other line of the envelope module;
   - the validation law's VL10, which **keeps refusing every tracked path in either reveal home until the reveal landing's own VL10 succession**, so that no home opens in effect before that landing;
   - the corpus landing's effective status, its eighteen cases, both manifests, its custody, its record and its proofs, which read the corpus landing's own commit and stay proven there;
   - the behaviour of every other proof.
9. **This correction is a prerequisite of the reveal landing.** With it effective, the reveal landing meets only the successions decision 38 stages for it, as the incremental placeholder probes reported with this candidate show. **D4-D preparation stays closed until separately authorised** after this record is effective; the session landing's listed successions are unaffected.

## 3. The exact change

10. **The change is one site, the closing line of the V12 case-home tuple in `tests/test_w8_discriminating_instrument_envelope.py`:**

```diff
                       "governance/discriminating-reveal/",
                       # Succeeded at the W8-D4 corpus landing (ADR-0060
                       # Part J decision 38).
-                      "governance/validation-cases/"))], [])
+                      "governance/validation-cases/",
+                      # Admitted by the separate case-home scope
+                      # correction W8-CHC, outside ADR-0060 Part J
+                      # decision 38.
+                      "governance/validation-reveal/authoring/",
+                      "governance/validation-reveal/construction/"))], [])
```

11. **Its pre-image is the corpus landing's reviewed post-image of the module, read from the baseline commit; its post-image is pinned here and in the proof module by hash and blob.** The proof module reads this landing's own snapshot: the working copy over the baseline before the commit exists, and the one commit that added this record afterwards, whose sole parent must be the baseline. No movable branch reference is substituted. **Every helper a historical proof relies on — the validation law's VL10 gate and its context, R9's sentence and the record helpers, the site and closed-table helpers, and the reserved literal sets — is executed from this landing's snapshot bytes, never taken from the live module**, which a later landing may lawfully succeed under decision 38; the live VL10 gates stay in VL10.

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_discriminating_instrument_envelope.py` | V12 | `sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80` | `sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700` |

12. **Nothing is broadened.** The limb still refuses the case prefix everywhere outside its six admitted homes, including directly under the reveal root and in any other directory beneath it. No other existing proof moves at this landing.

## 4. Proof obligations

13. **Eight obligations, mechanics only, each with negative controls, landed in `tests/test_w8_case_home_scope_correction.py`:**

| # | Obligation |
|---|---|
| **CH1** | The envelope module is exactly the pinned post-image of one exact, reversible transformation of its baseline pre-image, and section 3's table is read whole as exactly its header, separator and one trusted row |
| **CH2** | The case-home tuple is exactly the four existing homes followed by decision 23's two reveal homes, decision 23 names exactly those, and the law is byte-untouched |
| **CH3** | The corrected limb admits the two reveal homes and nowhere else new, while VL10, its helper and context executed from this landing's snapshot, still refuses every reveal-home path; a later change to the live helper leaves that verdict unchanged, and a genuine weakening of the historical gate is refused |
| **CH4** | Every envelope line outside the one site is unchanged, the vacancy limb included, and the corpus landing's proofs stay on their own commit |
| **CH5** | This landing's census is exactly section 5's |
| **CH6** | The registry and the board change exactly as authorised, in draft or accepted form |
| **CH7** | This record carries its settlement and exposes no identity, unpinned digest or token |
| **CH8** | The proof module carries no token, schema literal or case identity |

## 5. Census and human acts

14. **This landing's census is exactly five paths:** MODIFY `tests/test_w8_discriminating_instrument_envelope.py` · NEW `tests/test_w8_case_home_scope_correction.py` · NEW `docs/phases/W8-case-home-scope-correction.md` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. Any need for a sixth path is a further stop.
15. **Standing duties at this landing:** P2 and Q3; P4a reported separately; **a fresh P4b human act**; acceptance, which adopts section 2's settlement; publication only as the ADR-0056 public project identity; and independent remote verification. Mechanical evidence never substitutes for a human act. That evidence is the exact edit, the full suite, the scans, the placeholder probe before the census and the incremental forward probes, reported with the candidate.

## What this record does not establish

16. This record establishes none of the following:
    - no case, corpus, manifest, register, session record, packet, disposition, custody access, commitment reproduction, reveal, comparison or count;
    - no amendment of any law, and no succession for any W8-D4 landing;
    - no authority for the session, reveal or completion landing to begin;
    - no classification of any exchange under ADR-0047 decision 3;
    - no model behaviour of any kind;
    - no resolution of ADR-0047 precondition 3 or of any carried state.

    **No disposition ever made may cite this record as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — proof, home, limb, landing, record. Roles only, under ADR-0056. No case text is quoted and no case is named. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*Two named homes are admitted to one check; the law that names them stays as it was written.*
