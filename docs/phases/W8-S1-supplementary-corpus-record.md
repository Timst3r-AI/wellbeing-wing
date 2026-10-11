# W8-S1 — Supplementary Corpus: Record

**Status:** Accepted by human reviewer, 2026-10-11. **Effective only on publication and remote verification.**
**Date:** 2026-10-11
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** none — the phase-level supplementary corpus under ADR-0059 and `W8-S1-SOB`; W8-D2 stays complete as built
**Identity:** `W8-S1-SCR`, type `phase-record`; it carries the acceptance of governed register `W8-S1-CM-01`
**Position:** the record of the one supplementary authoring landing that `W8-S1-SOB` opens. **It renders no packet, holds no session, records no disposition, reveals nothing, compares nothing and counts nothing.** D3-C stays open and blocked until this record is effective, and this record authorises no session; D3-D stays unopened.
**Derived public baseline:** `2bb87a308d4cc1ce795869bb94370d3bdc75ae0e`, the published and remotely verified L1 landing of ADR-0059 and `W8-S1-SOB`
**Governed by:** ADR-0059 and `W8-S1-SOB`, whole; ADR-0055 as reconciled by `W8-D2-MSA` and by ADR-0059; **ADR-0054, whole — carried, never reinterpreted**; `W8-D2-DIB` sections 3 to 6; the effective `W8-D2-CBC` committed-object reading rule; ADR-0058, whole, its decision 5 operative; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**Twelve new cases now stand in public, each with a sealed construction hypothesis held apart in a drawer of its own, and nothing about what any of them was built to be has crossed into anything a reviewer can see. The first set stays sealed and untouched beside them.**

## 1. What landed

1. **This landing publishes exactly twelve reviewer-visible supplementary cases and one class-opaque commitment manifest in the supplement home `governance/discriminating-supplement/`.** The cases are `W8-C-<64-hex>.json` files in Part C canonical bytes, under evidence-derived identities and mechanical filenames. The manifest, `W8-S1-commitment-manifest.json`, follows the ADR-0055 decision 28 container law, and its acceptance is carried by this record as governed register `W8-S1-CM-01`.
2. **Every case passes the published envelope validator, and every identity is distinct and disjoint from every original-corpus identity.**
3. **The manifest's LF SHA-256 at this landing is `sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28`; it binds this corpus only, and no row of the original corpus appears in it.**
4. **Composition is withheld until the supplement's own reveal:** no authored class, intended token, construction map, rationale, class count or case-to-class mapping appears in this record, the manifest, the cases, the board, the registry or any review output.

## 2. Custody

5. **Before any case, nonce or retained record existed, the supplement's own custody sub-location passed its sentinel durability exercise:** a fresh sub-location inside the existing outside-repository review transport, outside the repository and outside transient storage; exclusive create refusing a second write; a separate-process raw-byte reopen equal to what was written; standard library only, with no provider, credential, secret store or dependency; and the labelled sentinel removed, so the records area began empty. **The location is never named in any surface.**
6. **Each withheld authoring record was frozen after its reviewer-visible bytes and every non-nonce field, its commitment nonce generated once and never rerolled, and then written once with exclusive create, never reopened for write.**
7. **Every commitment was reproduced by hashing the exact retained bytes directly, before any parse, twice before landing: at authoring, twelve of twelve, and at freeze through the manifest binding, pass.**
8. **No original retained record was listed, opened, parsed, hashed, copied or moved by any act of this landing**, and the original corpus's cases, manifest, commitments, completion record and register are byte-untouched.
9. **A proof over named custody records establishes binding mechanics only; the custody acts above are governed process duties, honoured and recorded here, never proven by a test**, and no proof in this landing reads custody.

## 3. Freshness and provenance

10. **The cases were authored in a separate authoring context grounded in the public doctrine and the approved construction law only.** That context did not read the original corpus home or its history, did not read any material of the void attempt, and used none of the void attempt's associations, derived distributions or purported answers (ADR-0058 decision 5); it adapted no original case and used none as a template. **The authoring account confirms, case-free, that it honoured the `W8-D2-DIB` section 3 duties this corpus carries:** the corpus materially exercises all three authoring classes and the breadth of the doctrine, and every case satisfies its class-specific authoring law, checked at authoring and recorded only in its withheld record. Mechanical validation checks shape and class constraints only; whether each case is semantically adequate stays a review-only question.
11. **The textual non-reuse guards pass in both directions:** the corpus module's C10 guard finds no ten-word sequence of any original variant in any supplementary file, and this landing's S10 sweep finds no ten-word sequence of any supplementary variant in any other tracked text. **These establish textual non-reuse and distinct identities only, never semantic independence, and the reviewer's broader prior exposure cannot be mechanically excluded.**
12. Twelve is fixed for workload and continuity of the session mechanics only; no statistical comparability with the void attempt or with the original corpus is claimed.

## 4. Conduct

13. **The reviewer's own review of the twelve visible cases at this landing is lawful access to visible evidence; it begins the conduct interval of ADR-0059 decision 13, and the session record's attestation later records it.**
14. **Review outputs that reach the reviewer at this landing carry no case-level content beyond the visible bytes themselves.** The architect's review is law and mechanics review only and gives no likely disposition, case-level judgment, ranking or preferred outcome to anyone, by any route (`W8-S1-SOB` item 16).

## 5. Proof successions at this landing

15. **Exactly the two successions that ADR-0059 Part G decision 25 stages for this landing move, each an exact transformation of its fixed pre-image at the L1 landing, proven by S12:**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_discriminating_instrument_envelope.py` | V12 | `sha256:cca0b83d0c50675b3ec1d32aa2b11f29a61633a47a0bf5d3434d9b1f6143d5b9` | `sha256:e7e80df8dbad8397574b9558a3892ac638e16e0d3549e2662e6181a55bb6944e` |
| `tests/test_w8_recovery_authority.py` | A9 | `sha256:2390dcaed53b5d9bffe3e1c53bcbaeac97290e2572162adaa3f78dc43cb45299` | `sha256:ed8b7bdd012d8164e76d5cebc47c4190e3f8adbc254e1da91addd45d56a2901e` |

16. The envelope module's case-home limb admits exactly the supplement home beside the original home, and its vacancy limb is unchanged. The authority module's pre-authoring absence limb stays proven at the L1 landing commit, and its present limb is the closure that S1 proves. **No other existing proof moves at this landing.**

## 6. Proof obligations

17. **Thirteen obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_supplementary_corpus.py`:**

| # | Obligation | Decidability |
|---|---|---|
| **S1** | The supplement home holds exactly the twelve cases and the manifest, tracked and on disk; once committed, the home has not moved and every home file's working copy equals its committed bytes up to line endings | **Mechanical** |
| **S2** | Every case passes the published envelope validator byte for byte, carries no packet-structure line, and its working copy matches its committed bytes | **Mechanical** |
| **S3** | The case identities are exactly the manifest's twelve, distinct and disjoint from every original-corpus identity, refused through the ADR-0059 validation chain otherwise | **Mechanical** |
| **S4** | The manifest is one closed two-field object under the container law, in canonical bytes and lexical order | **Mechanical** |
| **S5** | Every manifest row binds one-to-one to its case's exact published bytes | **Mechanical** |
| **S6** | Every commitment has the exact shape, is distinct, and is disjoint from every visible digest and every original commitment | **Mechanical** |
| **S7** | No reserved authoring label, withheld-record schema or disposition token appears on any visible surface of this landing | **Mechanical** |
| **S8** | This record and `W8-S1-CM-01` are registered at phase W8 with no deliverable, their hashes and status matching | **Mechanical for binding; acceptance is the human act** |
| **S9** | The manifest holds exactly twelve distinct identities, and this record and the board carry the fixed total sentence. On this record, the board wording this landing adds and the two new registry roles, every token recognised by the stated grammar is the literal word twelve. That grammar recognises only ASCII word tokens from the closed list one to twenty plus dozen, and decimal numerals, with at most two words between it and the word “case” or “cases”, list-item numbering excluded | **Mechanical within that grammar only; count wording it does not recognise, such as zero or hyphenated compounds, is outside this claim** |
| **S10** | No ten-word sequence of any supplementary variant occurs in any other tracked text | **Mechanical; semantic independence is never established** |
| **S11** | This record carries its custody, freshness, conduct and non-establishment statements and no case identity, digest other than its pins, or token | **Mechanical** |
| **S12** | The two staged successions are the exact transformations pinned in section 5, and this landing's census is exactly decision 18's | **Mechanical** |
| **S13** | The registry and the board change exactly as authorised, in draft or accepted form | **Mechanical** |

## 7. Census

18. **This landing's census is exactly nineteen paths:** NEW twelve `governance/discriminating-supplement/W8-C-<64-hex>.json` · NEW `governance/discriminating-supplement/W8-S1-commitment-manifest.json` · NEW `docs/phases/W8-S1-supplementary-corpus-record.md` · NEW `tests/test_w8_supplementary_corpus.py` · MODIFY `tests/test_w8_discriminating_instrument_envelope.py` · MODIFY `tests/test_w8_recovery_authority.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`.

## What this record does not establish

19. This record establishes no packet, no session, no disposition, no D3-C disposition-register instance, no commitment reproduction at review, no reveal, no comparison and no count; no authored class, composition or intended token of any case; no semantic independence of any case; no comparability between any two corpora; no claim about the original corpus's retained bytes; no reviewer route of any kind; no model behaviour of any kind; and no resolution of ADR-0047 precondition 3 or of any carried state. **No disposition ever made may cite this record as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — corpus, case, manifest, custody, commitment, reviewer. No case text is quoted and no case is characterised. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*New paper, a new drawer, and the seals checked twice before the paper was shown to anyone.*
