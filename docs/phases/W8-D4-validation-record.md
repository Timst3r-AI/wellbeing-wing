# W8-D4 — Validation Record

**Status:** Accepted by human reviewer, 2026-10-21. **Effective only on publication and remote verification.**
**Date:** 2026-10-21
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D4 — Instrument validation (landing **D4-E**, reveal and comparison)
**Identity:** `W8-D4-VRC`, type `phase-record`
**Position:** the reveal landing and validation record of W8-D4 on the validation corpus `W8-V1`. **It amends no disposition, diagnoses no divergence and derives no rate, score or readiness interpretation.** Diagnosis, if the human authority so decides, belongs to D4-F.
**Derived public baseline:** `44947adf9b60f2ce462be97a2c0e628a3ecbdd89`, the published and remotely verified session landing; the corpus stays bound to the corpus landing: commit `f638cca75ec4a192685bf5cd53f29451cfdbbdd9`, case home tree `77e9a5c8fa760753278e9df3b696bd4647ad5e9f`, commitment manifest `sha256:c9d35040a45140c0b5bdd7724f04f0922d213ee3cfff9de9f7f13d6b08f6576f`, construction manifest `sha256:9c4c3e9d24953fb08458afacc504066fa4b21ae76b0d75a2d7d7b901103a57b3`
**Governed by:** ADR-0060, whole, its Parts E, F, H, I and J especially; ADR-0057 Parts A to C as ADR-0060 decision 24 carries them and Parts D to G as its decisions 31 to 35 carry them, ADR-0057 byte-untouched; ADR-0055's nonce, commitment, manifest and custody decisions as ADR-0060 decision 20 carries them; `W8-D4-IVB`; `W8-D4-VCR`, `W8-V1-CM-01` and `W8-V1-CM-02`; `W8-D4-VSR` and governed register `W8-D4-DR-01`; `W8-CHC`; ADR-0058, whole, its decision 5 operative; **ADR-0054, whole — carried, never reinterpreted**; ADR-0055 as reconciled; the effective `W8-D2-CBC`; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**The reviewer wrote first, in public, and the writing was fixed. Then the seals were checked byte for byte, the sealed construction hypotheses were read, and the two were set side by side — case by case, as agreement or divergence, and as nothing more.**

## 1. The ordered sequence

1. **The session landing was published and independently remote-verified before anything here began**, and its dispositions were fixed at that publication (ADR-0057 decision 12, carried by ADR-0060 decision 29). The reveal landing's placeholder probe ran over every existing check before this landing's census was fixed and before any custody access, and refused exactly the successions ADR-0060 decision 38 stages for it.
2. **Every published authoring commitment and every published construction commitment of the validation corpus — and of no other corpus — reproduced by hashing the exact retained bytes directly, read-only, before any parse** (ADR-0060 decision 31): all eighteen authoring records and all eighteen construction records present by exact name in the corpus's own custody sub-location, each hashing to its published commitment in `W8-V1-CM-01` or `W8-V1-CM-02`. **No retained record of either earlier corpus was listed, opened, parsed, hashed, copied or moved by any act of this landing**, and no retained record was deleted, rewritten or moved.
3. **Only after every commitment reproduced were the exact retained bytes copied**, unparsed, unnormalised and unrewritten, to the reveal-candidate paths `governance/validation-reveal/authoring/<case_id>.json` and `governance/validation-reveal/construction/<case_id>.json`, for the corpus's identities only; each copy hashed to its published commitment (ADR-0060 decision 32).
4. **The landing scan ran over exactly the thirty-six candidate copies and found nothing; the scanner was never run against the custody location.** No suppression, redaction or byte repair was made or needed. **The location is never named in any surface.**
5. **Only after that clean scan were the copies parsed.** Every revealed authoring record passes the published withheld-record validator and binds to its identity, its filename, its row in `W8-V1-CM-01` and the published digest of its reviewer-visible case; every revealed construction record passes Part E's validator and binds to its case, its filename, its row in `W8-V1-CM-02`, the published visible digest and its authoring commitment, with every method admitted for its authored class and every declared family seed verified against the published variants; and the construction manifest binds one-to-one, in every direction, to the commitment manifest and to the exact construction bytes.
6. A proof over named custody records establishes binding mechanics only; the reproduction, the copy and the non-access above are governed process duties, honoured and recorded here, never proven by a test, and no proof in this landing reads custody.

## 2. The reveal

7. **The reveal publishes the exact retained bytes** of the corpus's eighteen authoring records and eighteen construction records at the two reveal homes of ADR-0060 decision 23, never a reserialised, normalised or redacted form. They are bound by `W8-V1-CM-01` and `W8-V1-CM-02` and are not individually registered. Before the first commit the proofs read the candidate copies exactly as written, unconverted; once committed, they read the committed objects with the working-copy correspondence check `W8-D2-CBC` carries.

## 3. The case-level comparison

8. **For each case of the corpus the comparison records exactly the case identity, the human token from the published register, the authored intended token from the revealed authoring record, and one relation from the closed set `agreement` · `divergence` — `agreement` exactly when the two tokens are byte-identical (ADR-0060 decision 33).** That is the whole of the comparison.

| Case identity | Human token | Authored intended token | Relation |
|---|---|---|---|
| `W8-C-224dc4ac410fd32c344ca1d39d948a2dcc146e97e9f89ff761aa461f59613d0a` | `no_governance_delta` | `review_inconclusive` | `divergence` |
| `W8-C-23de3b55b873e026be7fccd5199e0d74989401d7ce97685a23ba2af7ad5adf5f` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-2fad5559b07e0d24e30f21e8743e9860c8fe778ad76a9e846d0efc7c1dbad104` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-30e24e458c7137ad0fbd2e21d0d6f8b4496bca803d29c80cbc1a763ed9cde3dc` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-32bedf2c9cfe147a0da29daf890bb0dd50b28f5c5d282a415d6ec6643f991295` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-35f7acd3efaf804f81d8aee586a8edc1b07bee9fac7db38398e6d1c50c64b479` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-390abb964797144986a7d71c8c6e1ab50ee0d276f9a0396a6604fe614dad6f83` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-4b5933e69e8271917035ada3434f771ef8440b9940773a0ab33ca2cd487d62aa` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-84e5452f1313bbac2006525ab9d33a8abd2ef1dc90e552e5cee661b87d2bad3c` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-942db1c26a1da0bd8f23d2010638c4deee88aed73089cd065bd850b4dc8a78d1` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-afba55854b8def22bb5332127d5a2f49e08c95926175cb36a35c862be61e7368` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-c83be3cf51fe4caa24cabbe709fc9cf82423f3b3f307f82c4a6fa7547ff45e6b` | `review_inconclusive` | `no_governance_delta` | `divergence` |
| `W8-C-c8d4216b86a7c35fca5a9dea5c7eb896e728766e024e6bb3dc0fa3775123dc05` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-d1eb9814a2057382450cc49e447ed6798831497390f1002c1838d8e61d9455cb` | `review_inconclusive` | `review_inconclusive` | `agreement` |
| `W8-C-d8844873aaeb6711e82b2f1c2a5a60f2aef789b78ada7497c172aae1d667e624` | `governance_delta_present` | `governance_delta_present` | `agreement` |
| `W8-C-ec7fcc90cf6d6c60098841cd82563fbe845d575adf84b27b9ebbd9af514a3c45` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-f41374b06364670400be9a80dc5d02c1e112604cd5535d27ac98cc19c763f074` | `no_governance_delta` | `no_governance_delta` | `agreement` |
| `W8-C-fca0cbf0e3035758f793269166e981c5a58e7de2848507f5b013c7ba52c670a4` | `no_governance_delta` | `no_governance_delta` | `agreement` |

9. **An authored intended token is a construction hypothesis, never an answer key and never a certified correct answer.** **An agreement does not establish that the instrument detected anything, that either token is correct or that any case passed; a divergence is lawful signal about the case, the construction, the doctrine or the procedure — never a reviewer error** (ADR-0060 decision 34). **Revealed material never becomes retroactive disposition evidence.**
10. **The dispositions were fixed at the session landing's publication, and none is amended by any route.** The register and the session record are byte-unchanged by this landing.
11. **Method and family stay in the revealed construction records, published as their exact bytes; this record organises no outcome by them** (ADR-0060 decision 33).

## 4. The permitted counts

12. **Exactly two kinds of count are published: per-token counts of the corpus's human dispositions, all three tokens with zero counts included, and per-relation counts of `agreement` and `divergence`. Each count carries, in the same place, its statement (ADR-0054 decision 31; ADR-0060 decision 35).**

| Kind | Count | Statement |
|---|---|---|
| `governance_delta_present` | 5 | a count of individual human acts and nothing more |
| `no_governance_delta` | 7 | a count of individual human acts and nothing more |
| `review_inconclusive` | 6 | a count of individual human acts and nothing more |
| `agreement` | 16 | a count of individual human acts and nothing more |
| `divergence` | 2 | a count of individual human acts and nothing more |

13. **No count by method, family or class is published, and no percentage, rate, score, grade, ranking, threshold, pass/fail result, model-performance claim or readiness interpretation is derived, published or implied.** A column of identical marks would itself be a finding, never a success.
14. **Diagnosis is not this record's act.** This record diagnoses, explains away and corrects nothing; any diagnosis belongs to D4-F, only if the human authority so decides, and W8-D4 completes in either case (ADR-0060 decision 36).

## 5. Proof successions at this landing

15. **Exactly the two successions that ADR-0060 decision 38 stages for this landing move, each an exact transformation of its fixed pre-image at the derived public baseline, proven by VR10:**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_discriminating_instrument_envelope.py` | V12 | `sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700` | `sha256:d4685301e949b072510b38862dc59ebdcef9e383cc549d186712940c3d8fba4c` |
| `tests/test_w8_validation_law.py` | VL10 | `sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113` | `sha256:66a16bf2fe7cd71ff0dd382dbe30ce9b1afc35da5d90060082c7a79960ad6c50` |

16. The envelope module's authoring-schema limb admits exactly the validation authoring reveal home beside the W8-D3 reveal home; its case-home limb was already succeeded by the separately governed `W8-CHC`. VL10 admits exactly the two reveal homes for the corpus's identities, the construction reveal home joining the holders of the construction schema literal, and this record with its W8-D4 entry, the session-stage state staying proven at the session landing commit. ADR-0058's R9 board sentence does not move. **No other existing proof moves at this landing.**

## 6. Proof obligations

17. **Twelve obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_validation_reveal.py`.** Every proof reads this landing's fixed snapshot — the revealed files as their raw bytes before the first commit, and as committed objects with working-copy correspondence afterwards — and executes every helper it relies on from that snapshot's bytes, never from a live module a later landing may lawfully succeed; the live absence and admission gates stay in VL10.

| # | Obligation | Decidability |
|---|---|---|
| **VR1** | Each reveal home holds exactly the corpus's eighteen identities, tracked and on disk, and held nothing at the derived public baseline | **Mechanical** |
| **VR2** | Every revealed file hashes to its published commitment, authoring to `W8-V1-CM-01` and construction to `W8-V1-CM-02`; before the first commit read exactly as written, afterwards as the committed object with its working copy corresponding | **Mechanical** |
| **VR3** | Every revealed authoring record passes the published withheld-record validator and binds to its identity, filename, manifest row and published visible digest; every revealed construction record passes Part E's validator and binds to its case, class and authoring commitment; the construction manifest binds in every direction; and the family rule holds over the corpus | **Mechanical** |
| **VR4** | The four-value binding the session record carries is the published one at the corpus commit, and the reveal sets, the register's identities and the manifests' identities are each exactly the bound set, refusing a partial, premature or foreign reveal | **Mechanical** |
| **VR5** | The comparison table, read whole within its section, is exactly the mechanical one: its exact header and separator, then exactly eighteen rows of exactly the four permitted fields in ascending identity order, the published human token, the revealed authored intended token, and agreement exactly on byte-identical tokens; any malformed, surplus, duplicate or stray row is refused, never skipped | **Mechanical; neither side is a certified correct answer** |
| **VR6** | The count table, read whole within its section, holds exactly the five permitted rows in fixed order, zeros included, each an integer count equal to the mechanical one and carrying its exact statement; any unknown, malformed, duplicate or surplus row is refused, never skipped; and outside its two validated tables the record carries no percentage sign or ratio word, fraction, decimal, value beside a figure word, or count beside a kind or token | **Mechanical; textual forms only** |
| **VR7** | The register and the session record are byte-unchanged: no disposition is amended | **Mechanical** |
| **VR8** | This record carries its sequence, reveal, comparison, count, non-diagnosis, non-amendment, inference-limit and closure statements, each once, and the nine rules, and carries no bar on the later evidence use that `W8-D4-IVB` item 14 and ADR-0060 decision 48 reserve | **Mechanical** |
| **VR9** | No authored class, rationale, construction map, check, label, nonce, method note, method label or schema literal leaves the reveal homes through this record, the new registry role or the board wording this landing adds; the role and board carry no token or count | **Mechanical** |
| **VR10** | The two staged successions are the exact transformations pinned in section 5, whose table is read whole | **Mechanical** |
| **VR11** | The registry and the board change exactly as authorised, in draft or accepted form, with no revealed record individually registered and R9's sentence retained | **Mechanical for binding; acceptance is the human act** |
| **VR12** | This landing's census is exactly section 7's | **Mechanical** |

## 7. Census and position

18. **This landing's census is exactly forty-two paths:** NEW eighteen `governance/validation-reveal/authoring/W8-C-<64-hex>.json` · NEW eighteen `governance/validation-reveal/construction/W8-C-<64-hex>.json` · NEW `docs/phases/W8-D4-validation-record.md` · NEW `tests/test_w8_validation_reveal.py` · MODIFY `tests/test_w8_discriminating_instrument_envelope.py` · MODIFY `tests/test_w8_validation_law.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. No corpus home, register or session record is touched.
19. **On this record's acceptance, publication and independent remote verification, the reveal is effective.** W8-D4 then completes at D4-F, whose record diagnoses only if the human authority so decides. W8-D5 through W8-D7 remain closed behind their own briefs. Both earlier corpora's retained records stay in their existing custody under their own authority, which this record does not choose.

## 8. Doctrine carriage

20. The nine anti-collapse rules carry whole:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

## What this record does not establish

21. This record establishes no correctness of any human token or authored intended token; no answer key; no diagnosis, explanation or correction of any divergence; no rate, score, grade, ranking or readiness of anything; no validity, maturity or adequacy of the instrument; no finding about the reviewer, the reviewer's independence or the absence of influence; no comparability between any two corpora; no claim about either earlier corpus's retained bytes; no model behaviour of any kind; no classification of any exchange under ADR-0047 decision 3; and no resolution of ADR-0047 precondition 3 or of any carried state. **Neither this record nor any of its green proofs supplies any of those conclusions.** Any diagnosis belongs to D4-F only if the human authority so decides (ADR-0060 decision 36), and any later weighing of the case-level outcomes recorded here belongs solely to the separately governed evidence-adequacy review that `W8-D4-IVB` item 14 reserves to W8-D5, under its own brief and authority; **this record neither performs that weighing nor authorises W8-D5 to open**, and every prohibition of ADR-0060 decision 35 binds it whole.

## Public-safety note

Generic and structural wording throughout — reveal, commitment, comparison, count, reviewer, custody. Roles only, under ADR-0056. No case text is quoted and no case is characterised; the comparison carries identities and tokens only. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*Written first, sealed apart, opened last: what the reviewer judged and what the author built now stand side by side, agreeing where they agree, diverging where they diverge, and claiming nothing more.*
