# W8-D3 — Human Disposition Record

**Status:** Accepted by human reviewer, 2026-10-13. **Effective only on publication and remote verification.**
**Date:** 2026-10-12
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D3 — Synthetic calibration (landing **D3-C**)
**Identity:** `W8-D3-HDR`, type `phase-record`; it carries the acceptance of governed register `W8-D3-DR-01`
**Position:** the session record of D3-C on the session corpus that ADR-0059 binds. **It reads no withheld byte, reproduces no commitment, reveals nothing, compares nothing and counts nothing.** D3-D stays unopened until this record is published and independently remote-verified.
**Derived public baseline:** `9ded8c44abfd4c911d938814a7f551944998ec53`, the published and remotely verified proof correction `W8-HPC`; the session corpus stays bound to the supplementary authoring landing (section 2)
**Governed by:** ADR-0057 as reconciled by ADR-0059, whole; ADR-0059 and `W8-S1-SOB`, whole; `W8-HPC`, whose decision 8 makes it this landing's prerequisite; the effective `W8-D3-SCB` as reconciled; **ADR-0054, whole — carried, never reinterpreted**; ADR-0058, whole, its decision 5 operative; `W8-S1-SCR` and `W8-S1-CM-01`; ADR-0055 as reconciled; the effective `W8-D2-CBC` committed-object reading rule; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**Twelve individual human dispositions now stand in a register that publication will fix, each the reviewer's own, written down before any sealed construction hypothesis is read. Beside them stands the reviewer's account of how the review was done, in the reviewer's own words.**

## 1. The human act

1. **On 2026-10-12 the human authority, acting as the sole human reviewer, returned exactly one lawful token for each of the twelve cases of the session corpus**, from the session packet rendered by the published renderer from the corpus's committed Git object bytes. The packet put the ADR-0054 decision 26 review question to every case unaltered, with all three lawful dispositions available and no default. The return passed the structural completeness check — twelve lines, one per packet case, each a lawful token — reported as pass or fail with no tally, and the reviewer confirmed it by explicit act as their complete submitted return.
2. **Every token in the register is an individual human act.** Each was supplied by the human reviewer for its own case (ADR-0054 decision 18; ADR-0057 decision 6), as the reviewer's own words in section 3 state. The implementer transcribed the returned tokens exactly, and inferred, defaulted, filled, bulk-selected, recommended or substituted none.
3. **Immutability (ADR-0057 decision 12).** Before this record is published the reviewer alone may revise a token, by explicit act. After publication a disposition is fixed. After reveal, no disposition may be amended by any route. Accepting this record is also the reviewer confirming the transcription of their own tokens.

## 2. The register and the bindings

4. **The register is `governance/discriminating-review/W8-D3-disposition-register.json`, governed register `W8-D3-DR-01`, whose acceptance this record carries:** one closed canonical-bytes object under ADR-0057 decision 9, one row per case of the session corpus sorted by case identity, each row exactly the case identity and the returned token. It carries no authored class, intended disposition, construction map, authoring check, rationale, inconclusive-condition selection, confidence, per-row timestamp or other withheld authoring metadata (ADR-0057 decision 10), and no row of any other corpus.
5. **The bindings this record carries (ADR-0057 decision 11; ADR-0059 decision 9):**

| Binding | Value |
|---|---|
| Act date | 2026-10-12 |
| Reviewer role | the human authority, as the sole human reviewer |
| Packet SHA-256 | `sha256:c8f0b0a8152cca652e450bcdd08354d978596e9a206bfe540c0851e16eecfd11` |
| Register | `governance/discriminating-review/W8-D3-disposition-register.json` |
| Register LF SHA-256 | `sha256:3a1846c02434739c641c58f6428f6b7da4bab2e6a3b24e6b8bff4b4337df2b5a` |
| Session-corpus commit | `83253039ec274a2496b37b618949fd00d3cd7c8e` |
| Supplement home tree at that commit | `a00a0be832ba597ec2f2b68e19ca37d29af58f6d` |
| Manifest LF SHA-256 | `sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28` |

6. **The packet is transient and untracked.** Anyone can regenerate it from the published renderer and the published supplementary cases at the bound commit, and confirm its hash (ADR-0057 decision 5). Before its hash was recomputed and recorded, the renderer's input paths were proven to be exactly the bound manifest's case paths in the supplement home at the bound commit (ADR-0059 decision 11); the hash was later recomputed independently by the architect and by the implementer, each from the committed objects, each matching. The validation chain of ADR-0059 decision 10 holds through the register: the binding, the corpus, the packet inputs and the register rows, each equal to the bound manifest's identity set, none an original-corpus identity.

## 3. The reviewer's procedural account

7. **The reviewer's initial procedural attestation under ADR-0059 decision 15, given on 2026-10-12, is the reviewer's four quoted statements, reproduced verbatim and together, and nothing else.** The framing that introduced two of them was assembled with the architect's help and is carried separately in item 11. It covers the conduct interval from the reviewer's first access to the supplementary corpus's case material, including the review of that corpus's authoring landing, to the date it was given; the reviewer's dated continuation in item 8 carries the account forward. It is a human statement. No test proves the absence of influence, semantic independence or reviewer blinding, and none is claimed.

> “The cases were not reviewed in isolation from each other. They arrived in sequence in one conversation, with my earlier dispositions and reasoning visible to me throughout.”
>
> “My doctrine review preceded the cases. It included my own views on where the law pulls toward particular tokens, which I carried into the reading.”
>
> “individually verified.”
>
> “No, it was mine.”

8. **The reviewer's continuation of the procedural account, given on 2026-10-13, verbatim:**

> Since my account of 2026-10-12, I have received further mechanical review, clarification of the governing requirements, and drafting assistance from the architect and implementer concerning the candidate, the A3 correction and the rebuild. This has included their reports and reviews, and draft diffs containing my own submitted register rows.
>
> During this period, I have received no case-level judgements, preferred or predicted dispositions, case-level rationales, withheld authoring information or aggregate feedback about the cases from anyone else. Nothing has occurred that requires a correction to my earlier account.
>
> My earlier account, together with this continuation, is complete and accurate as at the date above. I will report any further relevant event before publication, and publication must pause if that event requires an updated account or review.

**The initial attestation and its continuation together are the reviewer's procedural account under ADR-0059 decision 15, which the reviewer states is complete and accurate as at 2026-10-13. Publication of this record is conditional on that account remaining complete and accurate through publication: any further relevant event is reported before publication, and an event that requires an updated account or review pauses publication.** This condition is a continuing process duty, not a machine proof and not an advance assertion about future events.

9. **The reviewer's clarification, given on 2026-10-12, verbatim:**

> My statement about the cases not being reviewed in isolation described their sequential presentation in one conversation, with earlier responses visible. Please read it together with my clarification, “individually verified”, and my statement that the judgements were mine.

10. **The human authority's determination.** The reviewer's account engages the review law: the packet law's statement that each case is reviewed independently, on its two variants alone (ADR-0057 decision 3), the reviewer's free reading order (ADR-0057 decision 7), and ADR-0054 decisions 20, 27 and 30. Before this record was built, the implementer stopped and put to the human authority and the architect the question how that account stands under those provisions; the implementer made no determination. The human authority's determination, given on 2026-10-12 after the architect's review, verbatim:

> I have considered the architect’s review and determine that my reported process fits the governing provisions.

11. **Procedural context, separately attributed.** The following was assembled with the architect's help from the reviewer's statements and is recorded with roles only; it is not part of the attestation. In the assembled message, the third quoted statement was introduced with the words “To clarify how I assessed the cases, my words were:” and the fourth with the words “When the architect asked whether anyone had supplied case-level judgements, preferred answers, rationales or withheld authoring information, covering my first access to the supplementary material including the L2 review, I answered:”, with the architect named by role. The human reviewer–architect conversation was used for rule clarification, case presentation and transcription. The assistance provided in it included mechanical checks, explanation of the governing rules, unchanged presentation of the cases and transcription of the reviewer's choices. The architect also helped assemble the reviewer's attestation message from the statements and clarifications the reviewer supplied. The architect also helped the reviewer put the continuation in item 8 into words.
12. **The implementer's account, separately attributed.** The implementer rendered the packet and delivered it with a case-free review procedure. The reviewer shared the packet with the architect, whose mechanical check verified it, and with the implementer, which recomputed its hash by an independent rendering; ADR-0059 decision 14 provides that sharing material with the architect or implementer for the permitted purposes alone is not itself a breach. The implementer's assistance was confined to rendering and delivery, the structural completeness check, and exact transcription and binding. Since the initial attestation, the implementer's assistance has been mechanical and drafting work only: the first build of this landing and its stop, the `W8-HPC` correction and its publication, and this rebuild; the reports the reviewer received from the implementer were case-free, and the draft diffs carried the reviewer's own register rows. Nothing case-level reached the reviewer from the implementer.
13. **This record does not classify any exchange under ADR-0047 decision 3 and does not state whether model contact occurred;** ADR-0058 Part F carries whole (ADR-0059 decision 16).
14. **The conduct interval continues until this record is published, and any further relevant event must be reported before publication.** No observation under ADR-0057 decision 11 was volunteered, so none is carried.

## 4. Custody

15. **The existence check found the session corpus's twelve expected records present by name in that corpus's own custody sub-location (ADR-0057 decision 13):** exact-name presence checks only, performed at packet preparation and before the first build of this landing, on 2026-10-12, and again before this rebuild, on 2026-10-13, with nothing listed, opened, parsed or hashed and no retained record of any other corpus listed or touched. **The location is never named in any surface.**
16. **No withheld byte was read:** no commitment was reproduced, nothing was copied, revealed or compared, and no count exists. ADR-0057 decision 14 carries whole.
17. **A proof over named custody records establishes binding mechanics only; the existence check is a governed process duty, honoured and recorded here, never proven by a test**, and no proof in this landing reads custody.

## 5. Proof successions at this landing

18. **Exactly the three successions that ADR-0059 Part G decision 26 stages for this landing move, each an exact transformation of its fixed pre-image at the derived public baseline, proven by H8:**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_calibration_law.py` | K12 | `sha256:d9e372ee85b37adc2b70ba8ff3d08de564debaaadf3b9e98f303b9ea69d4dcc8` | `sha256:448e1aa056a9ce176d7ae1b1856bb6eb459b8e1180fc0eae341419c5c19dc328` |
| `tests/test_w8_session_recovery_law.py` | R7, R9 | `sha256:a50c71a2074cf5f31660f1bda5434c6bf592a9ec9a44719ffb47c91fadfdedb9` | `sha256:8934a5248504228a0950f5afedc523a377e063746d3e18e37dced914855219ea` |

19. The disposition-law module's K12 register limb and register-schema homes admit exactly the published register; its former absence stays proven at ADR-0057's landing commit, and the reveal home stays empty. ADR-0058's R7 admits exactly the register, this record and the two W8-D3 registry entries they add, its former absence staying proven at ADR-0058's landing commit; R9's board sentence succeeds to this landing's wording — *No reveal, comparison, count or calibration exists yet.* — its earlier form staying proven at that same commit, the derived baseline of ADR-0059. **No other existing proof moves at this landing.**
20. **This landing was first prepared over the supplementary authoring landing and stopped before anything was staged**, because ADR-0059's proof A3 derived its permitted historical pins from the working copy and would have rejected the authorised R7 and R9 succession; the separately governed `W8-HPC` corrected A3, and this landing was rebuilt over it. The session-corpus binding, the packet binding, the reviewer's return and the act's date are unchanged by the rebuild.

## 6. Proof obligations

21. **Twelve obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_disposition_record.py`:**

| # | Obligation | Decidability |
|---|---|---|
| **H1** | The register is one closed canonical-bytes object under ADR-0057 decision 9: LF with one terminal LF, the fixed schema, twelve rows sorted by case identity, each exactly an identity and a lawful token, one-to-one with the session corpus | **Mechanical** |
| **H2** | The ADR-0059 validation chain holds through the register on the real corpus: the recorded binding equals the published one, and is the corpus commit, never the session baseline; the bound manifest holds twelve distinct identities none of them original, the packet inputs are exactly its case paths, and the register rows are exactly its identities | **Mechanical** |
| **H3** | The register's and this record's working copies equal their snapshot bytes, which once committed are the committed objects, up to line endings | **Mechanical** |
| **H4** | This record's binding table carries exactly the act date, the reviewer role, the packet hash, the register path and hash, and the published session-corpus binding | **Mechanical for carriage; the packet hash's recomputation is a process act recorded in section 2** |
| **H5** | This record carries its individual-act, transcription, attestation, combined-account, publication-condition, non-classification, conduct, immutability, custody and succession statements, each once, and the nine rules | **Mechanical** |
| **H6** | The attribution boundary: the attestation is exactly the reviewer's four quoted statements, verbatim and together in one block of their own; the clarification and the determination are each verbatim in a block of their own; the dated continuation is verbatim in a block of its own under its dated label; and the assisted framing and the continuation's drafting assistance each appear once, outside every quotation block, only in the separately attributed context | **Mechanical for carriage; the attestation is the human statement itself** |
| **H7** | No case identity, disposition token, reserved authoring label, schema literal, count statement or unpinned digest appears in this record, the two new registry roles or the board wording this landing adds | **Mechanical** |
| **H8** | The three staged successions are the exact transformations pinned in section 5 | **Mechanical** |
| **H9** | Nothing of this landing existed at the derived public baseline, the `W8-HPC` landing, and no reveal home, completion record or later entry exists now | **Mechanical** |
| **H10** | This record and `W8-D3-DR-01` are registered at W8-D3, their hashes and status matching this record's header | **Mechanical for binding; acceptance is the human act** |
| **H11** | The registry and the board change exactly as authorised from their baseline pre-images, in draft or accepted form, with the `W8-HPC` entry and row preserved | **Mechanical** |
| **H12** | This landing's census is exactly decision 22's | **Mechanical** |

## 7. Census

22. **This landing's census is exactly seven paths:** NEW `governance/discriminating-review/W8-D3-disposition-register.json` · NEW `docs/phases/W8-D3-human-disposition-record.md` · NEW `tests/test_w8_disposition_record.py` · MODIFY `tests/test_w8_calibration_law.py` · MODIFY `tests/test_w8_session_recovery_law.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. Neither the original corpus home nor the supplement home is touched.

## 8. Doctrine carriage

23. The nine anti-collapse rules carry whole:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

## What this record does not establish

24. This record establishes no commitment reproduction, no reveal, no comparison, no agreement or divergence and no count; no authored class, composition or intended token of any case; no correctness of any token; no absence of influence, semantic independence or reviewer blinding; no comparability between any two corpora; no claim about either corpus's retained bytes; no reviewer route of any kind; no classification of any exchange under ADR-0047 decision 3; no model behaviour of any kind; and no resolution of ADR-0047 precondition 3 or of any carried state. **No disposition in the register may be cited as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — session, packet, register, reviewer, custody, binding. Roles only, under ADR-0056. No case text is quoted, no case is named or characterised, no token is tallied, and no association or figure from the void attempt appears. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The reviewer wrote first, and in public; the seals are still unbroken; and the reviewer's own account of how the writing was done stands beside it, in the reviewer's own words.*
