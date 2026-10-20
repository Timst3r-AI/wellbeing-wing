# W8-D4 — Validation Session Record

**Status:** Accepted by human reviewer, 2026-10-21. **Effective only on publication and remote verification.**
**Date:** 2026-10-19
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D4 — Instrument validation (landing **D4-D**)
**Identity:** `W8-D4-VSR`, type `phase-record`; it carries the acceptance of governed register `W8-D4-DR-01`
**Position:** the session record of D4-D on the validation corpus `W8-V1`. **It reads no withheld byte, reproduces no commitment, reveals nothing, compares nothing and counts nothing.** D4-E stays closed until this record is published and independently remote-verified.
**Derived public baseline:** `a08ba584bea8e2576dd7450c6374a4ff4f0aa149`, the published and remotely verified correction `W8-CHC`; the session corpus stays bound to the corpus landing (section 2)
**Governed by:** ADR-0060, whole, its Parts G, H and J included; ADR-0057 Parts A to C as ADR-0060 carries them, ADR-0057 byte-untouched; `W8-D4-IVB`; `W8-D4-VCR`, `W8-V1-CM-01` and `W8-V1-CM-02`; `W8-CHC`; **ADR-0054, whole — carried, never reinterpreted**; ADR-0058, whole, its decision 5 operative; ADR-0055 as reconciled; the effective `W8-D2-CBC` committed-object reading rule; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**Eighteen individual human dispositions now stand in a register that publication will fix, each the reviewer's own, written down before any sealed construction hypothesis is read. Beside them stand the reviewer's account of how the review was done, in the reviewer's own words, and the record of what the reviewer had already seen.**

## 1. The human act

1. **On 2026-10-17 the human authority, acting as the sole human reviewer, returned exactly one lawful token for each of the eighteen cases of the validation corpus**, from the session packet rendered by the published renderer from the corpus's committed Git object bytes. The packet put the ADR-0054 decision 26 review question to every case unaltered, with all three lawful dispositions available and no default. The return passed the structural completeness check — one line per packet case, each a lawful token — reported as pass or fail with no tally, and the reviewer confirmed it by explicit act as their complete submitted return (section 4).
2. **Every token in the register is an individual human act.** Each was supplied by the human reviewer for its own case (ADR-0054 decision 18; ADR-0057 decision 6, carried by ADR-0060 decision 26). The implementer transcribed the returned tokens exactly, and inferred, defaulted, filled, bulk-selected, recommended or substituted none. Set in the packet's own response form, the register's rows reproduce byte for byte the confirmed return whose SHA-256 the architect records in item 15.
3. **Immutability (ADR-0057 decision 12, carried by ADR-0060 decision 29).** Before this record is published the reviewer alone may revise a token, by explicit act. After publication a disposition is fixed. After reveal, no disposition may be amended by any route. Accepting this record is also the reviewer confirming the transcription of their own tokens.

## 2. The register and the bindings

4. **The register is `governance/validation-review/W8-D4-validation-register.json`, governed register `W8-D4-DR-01`, whose acceptance this record carries:** one closed canonical-bytes object under ADR-0057 decision 9 as ADR-0060 decision 28 carries it, one row per case of the validation corpus sorted by case identity, each row exactly the case identity and the returned token. It carries no authored class, intended disposition, method, family, construction map, authoring check, rationale, inconclusive-condition selection, confidence, per-row timestamp or other withheld authoring metadata (ADR-0057 decision 10), and no row of any other corpus.
5. **The bindings this record carries (ADR-0057 decision 11; ADR-0060 decision 25):**

| Binding | Value |
|---|---|
| Act date | 2026-10-17 |
| Reviewer role | the human authority, as the sole human reviewer |
| Packet SHA-256 | `sha256:84f937fc6b2ae6ad0dda973bb2b336289ea80a4c031825380d0e7ffe222a290a` |
| Register | `governance/validation-review/W8-D4-validation-register.json` |
| Register LF SHA-256 | `sha256:89d55e2ac9de9531330faa9687385c0cedf2efcfff855d56b0b6e35ee01b25a0` |
| Corpus landing commit | `f638cca75ec4a192685bf5cd53f29451cfdbbdd9` |
| Case home tree at that commit | `77e9a5c8fa760753278e9df3b696bd4647ad5e9f` |
| Commitment manifest LF SHA-256 | `sha256:c9d35040a45140c0b5bdd7724f04f0922d213ee3cfff9de9f7f13d6b08f6576f` |
| Construction manifest LF SHA-256 | `sha256:9c4c3e9d24953fb08458afacc504066fa4b21ae76b0d75a2d7d7b901103a57b3` |

6. **The packet is transient and untracked.** Anyone can regenerate it from the published renderer and the published validation cases at the bound commit, and confirm its hash (ADR-0057 decision 5, carried by ADR-0060 decision 24). From the binding alone were derived the packet's case set, the register's membership and the existence check, each equal exactly to the bound commitment manifest's identities (ADR-0060 decision 25). Before the packet's hash was recorded, the renderer's input paths were proven to be exactly the bound commitment manifest's case paths; the hash was recomputed independently by the architect and by the implementer, each from the committed objects, each matching.

## 3. One session, and case independence

7. **This was the validation corpus's one session, held over the whole corpus, family members included, as ADR-0060 decision 15 requires.** Family members are recognisable to a reader even while their relation is withheld; this record does not say whether any family exists. Case independence carries whole: each case is dispositioned on its own two variants alone, and no case is decided because of another (ADR-0054 decision 30).

## 4. The reviewer's procedural account

8. **The reviewer's statement, given on 2026-10-17, verbatim:**

> i reviewed it independently.

9. **The reviewer's clarification, given on 2026-10-18, verbatim:**

> no to both

10. **The reviewer's account, drafted on 2026-10-18 and adopted by the reviewer on 2026-10-19, verbatim:**

> Dated 18 October 2026.
>
> I reviewed the W8-D4 validation cases independently and confirm that my submitted return is complete.
>
> I relayed W8-D3 documents between the architect and the implementer, but I did not read their contents. I did not read W8-D3 summaries in our messages or the method descriptions in the opening brief or ADR-0060.
>
> From my first access to the validation corpus through the date of this account, I received the procedural and drafting help described separately by the architect and implementer, and no other assistance.
>
> I will report any further assistance or relevant event before the session record is published so that the account can be updated.

11. **The reviewer's confirmation of the return, given on 2026-10-19, verbatim:**

> I confirm that the attached return is my complete submitted return.

12. **The reviewer's continuation of the account, dated 21 October 2026 and adopted by the reviewer on 2026-10-21, verbatim:**

> Since my account dated 18 October 2026, I have received only the procedural and drafting assistance described separately by the architect and the implementer, including the session-candidate reviews and repairs and help drafting this continuation.
>
> I have received no other assistance and have no other relevant events to report. Nothing changes my earlier account; this continuation carries it forward through 21 October 2026.
>
> I will report any further assistance or relevant event before the session record is published so that my account can be updated.

13. **The statement, the clarification, the adopted account, the confirmation and the continuation are the reviewer's procedural account under ADR-0060 decision 29: the account adopted on 2026-10-19 for the period it describes, carried forward by the continuation adopted on 2026-10-21.** Each keeps its own date. **The adopted account describes the conduct interval from the reviewer's first access to the validation corpus's case material, at the review of its authoring candidate, through 18 October 2026, and the continuation carries it forward through 21 October 2026.** Its adoption on 2026-10-19 preserves the earlier statements' dates and does not itself extend the account's factual coverage; the continuation carries its actual date and the reviewer's own adopted words, as any later continuation must. It is a human statement. No test proves the absence of influence, semantic independence or reviewer blinding, and none is claimed. **Publication of this record is conditional on that account remaining complete and accurate through publication: any further relevant event is reported before publication, and an event that requires an updated account or review pauses publication.** This condition is a continuing process duty, not a machine proof and not an advance assertion about future events.

## 5. Prior exposure

14. **The reviewer's prior exposure is recorded here and never attested away (ADR-0060 decision 29).** The published facts: the revealed supplementary constructions and the W8-D3 comparison were published by the W8-D3 reveal landing, whose record `W8-D3-CCR` the human authority accepted on 2026-10-13; the method descriptions are published in the opening brief `W8-D4-IVB` and in ADR-0060, each accepted by the human authority on 2026-10-14; and the validation corpus's authoring candidate, whose review was the reviewer's first access to its case material, was accepted as `W8-D4-VCR` on 2026-10-15; that record's item 7 records that access as the beginning of the conduct interval. Each acceptance shows a document's availability to the human authority; neither acceptance nor possession alone establishes which contents were read. The reviewer's own statements about those documents, including the relaying of W8-D3 documents, are carried verbatim in items 9, 10 and 12, beside these facts. **Neither the facts nor the statements determine what influence, if any, followed, and this record makes no such determination.**

## 6. Procedural context, separately attributed

15. **The architect's procedural account and drafting assistance, separately attributed, with roles only; it is not part of the reviewer's account.** The architect verified the preparation, the corpus bindings and the packet reproduction; delivered the cases verbatim, one at a time; transcribed the reviewer's chosen tokens; restored the temporary draft once from the reviewer's messages; and checked the complete return for structural completeness. The architect supplied no case-level judgement, recommended token or case rationale. At the reviewer's request, the architect assembled the account draft, sought clarification of missing factual disclosures, and incorporated the reviewer's answers: the clarification in item 9 answered the architect's two questions, whether the reviewer had read the W8-D3 summaries in their messages or the method descriptions, and whether the reviewer had received any other assistance beyond the described procedural and drafting help. A further clarification about relaying documents without reading them is kept in private working notes because it names the implementer, and the account's role language is drafted wording, not a silent alteration of a quotation. The architect records that the reviewer confirmed the complete submitted return on 2026-10-17, its bytes unchanged, with SHA-256 `sha256:3532f852bdad6285fcd9538dab49eeafc9e64f29249496bb3bd7ad9f94701235`. The architect also helped the reviewer put the continuation in item 12 into words, from the reviewer's own factual answer.
16. **The implementer's account, separately attributed.** The implementer ran the placeholder probe, checked the corpus binding, performed the existence check, rendered the packet and delivered it on 2026-10-17 with a case-free review procedure. The reviewer shared the packet with the architect, whose mechanical preparation check reproduced it, and on 2026-10-17 with the implementer, which confirmed only that its bytes equal the rendered packet; ADR-0057 decision 8, carried by ADR-0060 decision 27, provides that sharing material with the architect or implementer for the permitted purposes alone is not itself a breach. On 2026-10-19 the reviewer's confirmation referred to an attachment that had not arrived; the implementer asked for the exact files and built nothing until the reviewer supplied them, and the return then supplied is byte-identical to the return the architect records. On 2026-10-21 the reviewer supplied the continuation in item 12 in the reviewer's own message, and the implementer carried it verbatim into this candidate. The implementer's assistance was confined to rendering and delivery, the structural completeness check, exact transcription and binding, and the drafting of this candidate. Nothing case-level reached the reviewer from the implementer, and the implementer made no determination about the reviewer's process.
17. **This record does not classify any exchange under ADR-0047 decision 3 and does not state whether model contact occurred;** ADR-0058 Part F carries whole.
18. **The conduct interval continues until this record is published, and any further relevant event must be reported before publication.** No observation under ADR-0057 decision 11 was volunteered, so none is carried.

## 7. Custody

19. **The existence check found every expected authoring record and every expected construction record of the validation corpus present by exact name in that corpus's own custody sub-location (ADR-0060 decision 30):** exact-name presence checks only, at packet preparation on 2026-10-17 and again before this candidate on 2026-10-19, with nothing listed, opened, parsed or hashed and no retained record of any other corpus listed or touched. **The location is never named in any surface.**
20. **No withheld byte was read:** no commitment was reproduced, nothing was copied, revealed or compared, and no count exists. ADR-0060 decisions 31 and 32 carry whole, and the reveal landing begins only after this record is published and independently remote-verified.
21. **A proof over named custody records establishes binding mechanics only; the existence check is a governed process duty, honoured and recorded here, never proven by a test**, and no proof in this landing reads custody.

## 8. Proof successions at this landing

22. **Exactly the two successions that ADR-0060 decision 38 stages for this landing move, each an exact transformation of its fixed pre-image at the derived public baseline, proven by VS8:**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_calibration_law.py` | K12 | `sha256:2dca05bbd21544cdd3e524e59c2e431172e88e571441a22588f47a9f2141e36f` | `sha256:aa3870f66b9fc8b739e35261412f25243aedf29c50b41d4f7ac15a28152b757c` |
| `tests/test_w8_validation_law.py` | VL10 | `sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02` | `sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113` |

23. The disposition-law module's K12 register-schema limb admits exactly the validation register beside the published W8-D3 register, its former holders staying proven at the derived public baseline. The validation law's VL10 admits exactly the register home, the register, this record and the two W8-D4 entries they add, the corpus-stage state staying proven at the corpus landing commit. ADR-0058's R9 board sentence does not move; decision 38 reserves its movement to the completion landing, and only if that landing diagnoses a divergence. **No other existing proof moves at this landing.**

## 9. Proof obligations

24. **Twelve obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_validation_session.py`.** Every historical proof reads this landing's fixed snapshot and executes every helper it relies on from that snapshot's bytes; the live absence and admission gates stay in VL10. Two of those helpers still reach fixed-law values through live module aliases — the calibration register validator, through the envelope's identity pattern and the packet's token set, and the exposure check, through the packet's token set — and this record claims no more independence than that.

| # | Obligation | Decidability |
|---|---|---|
| **VS1** | The register is one closed canonical-bytes object under ADR-0057 decision 9, read as its raw bytes before its first commit: LF with one terminal LF, the fixed schema, one row per bound identity in order, each exactly an identity and a lawful token; set in the packet's response form, its rows reproduce the confirmed return's recorded SHA-256 | **Mechanical for the transcription; the return is the reviewer's own act** |
| **VS2** | The binding chain holds through the register: the recorded binding equals the published one at the corpus commit, never the session baseline; the bound manifests hold the same eighteen distinct identities, none of either earlier corpus; the packet inputs are exactly the manifest's case paths, and the register rows exactly its identities | **Mechanical** |
| **VS3** | The register's and this record's working copies correspond to their snapshot bytes, which once committed are the committed objects, a checkout's line-ending display apart | **Mechanical** |
| **VS4** | Section 2's binding table, read whole, is exactly the act date, the reviewer role, the packet hash, the register path and hash, and the four-value corpus binding | **Mechanical for carriage; the packet hash's recomputation is a process act recorded in section 2** |
| **VS5** | This record carries its individual-act, transcription, session, account, publication-condition, prior-exposure, non-classification, conduct, immutability, custody and succession statements, each once, the prior-exposure dates matching the registry, and the nine rules | **Mechanical** |
| **VS6** | The attribution boundary: each of the five human statements is verbatim in a dated block of its own, the quotation boundary closed, and the architect's and implementer's accounts appear only outside every quotation block, in their separately attributed items | **Mechanical for carriage; the account is the human statement itself** |
| **VS7** | No case identity, disposition token, reserved authoring label, schema literal, count statement or unpinned digest appears in this record, the two new registry roles or the board wording this landing adds | **Mechanical** |
| **VS8** | The two staged successions are the exact transformations pinned in section 8, whose table is read whole | **Mechanical** |
| **VS9** | Nothing of this landing existed at the derived public baseline, and at this landing's snapshot no reveal home, validation record, completion record or later entry exists | **Mechanical** |
| **VS10** | This record and `W8-D4-DR-01` are registered at W8-D4, their hashes and status matching this record's header | **Mechanical for binding; acceptance is the human act** |
| **VS11** | The registry and the board change exactly as authorised from their baseline pre-images, in draft or accepted form, the `W8-CHC` entry and row and R9's sentence preserved | **Mechanical** |
| **VS12** | This landing's census is exactly section 10's | **Mechanical** |

## 10. Census

25. **This landing's census is exactly seven paths:** NEW `governance/validation-review/W8-D4-validation-register.json` · NEW `docs/phases/W8-D4-validation-session-record.md` · NEW `tests/test_w8_validation_session.py` · MODIFY `tests/test_w8_calibration_law.py` · MODIFY `tests/test_w8_validation_law.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. No corpus home is touched.

## 11. Doctrine carriage

26. The nine anti-collapse rules carry whole:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

## What this record does not establish

27. This record establishes no commitment reproduction, no reveal, no comparison, no agreement or divergence and no count; no authored class, method, family, composition or intended token of any case; no correctness of any token; no absence of influence, semantic independence or reviewer blinding; no determination about the reviewer's process or prior exposure; no comparability between any two corpora; no claim about the corpus's retained bytes; no reviewer route of any kind; no classification of any exchange under ADR-0047 decision 3; no model behaviour of any kind; and no resolution of ADR-0047 precondition 3 or of any carried state. **No disposition in the register may be cited as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — session, packet, register, reviewer, custody, binding. Roles only, under ADR-0056. No case text is quoted, no case is named or characterised, no token is tallied, and no association or figure from the void attempt appears. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The reviewer wrote first, and in public; the seals are still unbroken; and beside the writing stand the reviewer's own words about how it was done and what had already been seen.*
