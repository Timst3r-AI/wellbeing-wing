# W8-D4-C — Validation Corpus Record

**Status:** Accepted by human reviewer, 2026-10-15. **Effective only on publication and remote verification.**
**Date:** 2026-10-14
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D4 — Instrument validation (landing **D4-C**)
**Identity:** `W8-D4-VCR`, type `phase-record`; it carries the acceptance of the governed registers `W8-V1-CM-01` and `W8-V1-CM-02`
**Position:** the corpus landing of W8-D4 under the effective ADR-0060. **It renders no packet, holds no session, records no disposition, reveals nothing, compares nothing, counts nothing, diagnoses nothing and contacts no model.** D4-D, D4-E and D4-F remain separately authorised.
**Derived public baseline:** `054f1270b8206a059636e18e012223ddfe52d5ea`, the published and remotely verified ADR-0060 landing
**Governed by:** ADR-0060, whole; the effective `W8-D4-IVB`; **ADR-0054, whole — carried, never reinterpreted**; ADR-0055 Parts A to I as ADR-0060 carries them; ADR-0058, its decision 5 operative; ADR-0059 decision 19; the effective `W8-D2-CBC`; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**The harder exam is written and sealed. Its cases are published as their visible evidence alone; how each was built is sealed in two records of its own, outside the repository, until the reveal — and nothing about which is which leaves the seal before then.**

## 1. What this landing publishes

1. **This landing publishes exactly eighteen reviewer-visible validation cases and two class-opaque manifests in the validation case home** `governance/validation-cases/`: the commitment manifest, governed register `W8-V1-CM-01`, LF SHA-256 `sha256:c9d35040a45140c0b5bdd7724f04f0922d213ee3cfff9de9f7f13d6b08f6576f`; and the construction manifest, governed register `W8-V1-CM-02`, LF SHA-256 `sha256:9c4c3e9d24953fb08458afacc504066fa4b21ae76b0d75a2d7d7b901103a57b3`. The corpus is `W8-V1`, of exactly eighteen reviewer-visible validation cases.
2. **Every case passes the published envelope validator, and every identity is distinct and disjoint from every published identity of either earlier corpus.** Identities, filenames and order are mechanical consequences of the visible evidence (ADR-0055 Parts B to D), and every manifest row binds its case's exact bytes.
3. **Composition is withheld until the corpus's own reveal:** no class, method, family or count beyond the corpus size appears in any surface of this landing. Shared variant text, if any, is visible in the published cases; which cases form a declared family, and by which methods, stays sealed in the construction records.

## 2. Authoring and freshness

4. **The corpus was authored by the authoring implementer in a separate, blinded authoring context, from the public doctrine, the accepted brief and ADR-0060 alone.** That context did not read either earlier corpus's home, the reveal home, their history or the W8-D3 completion record; used nothing from the void attempt (ADR-0058 decision 5); and adapted no published case. Its account to this record is case-free, and every construction working file stayed in the corpus's own custody.
5. **Each case is built by exactly one of ADR-0060's methods admitted for its authored class, and any variant text shared between cases is the declared seed of one family, of two or three members** — checked mechanically at authoring with ADR-0060's own validators, and proven over the revealed records only at reveal.
6. **Freshness:** the published C10 and S10 guards passed over the new cases before anything entered custody and again at the end; this landing's own proof finds no ten-word sequence shared, in either direction, with any published case of either earlier corpus, and no validation sequence in any other tracked text at this landing. **These establish textual non-reuse and distinct identities only, never semantic independence or the absence of influence** (ADR-0059 decision 18).
7. **The reviewer's access to the visible cases at this landing is lawful access to visible evidence: it begins the conduct interval of ADR-0060 decision 27**, and the session record later records it. No class, method, family, construction or case-level judgment reaches the reviewer from anyone else.

## 3. Custody

8. **Before any case, nonce or retained record existed, the corpus's own custody sub-location passed its sentinel durability exercise** (ADR-0060 decision 22): created fresh inside the existing outside-repository review transport, outside the repository and outside transient storage; write-once refusal and a separate-process raw-byte re-read proven in both record areas; the sentinel removed and both areas left empty; standard library only, with no provider, credential, secret store or dependency. **The location is never named in any surface.**
9. **Each authoring record and each validation-construction record was frozen in that sub-location once:** each authoring nonce generated once after the authoring fields and the visible bytes were frozen; each construction nonce generated once after every other field of both records was frozen; none rerolled; every record written once with exclusive create and never reopened for write.
10. **Every commitment of both kinds was reproduced by hashing the exact retained bytes directly, before any parse, twice before landing:** at authoring, in a separate process; and at freeze, against the written manifests.
11. **No retained record of either earlier corpus was listed, opened, parsed, hashed, copied or moved by any act of this landing.**
12. **A proof over named custody records establishes binding mechanics only;** the custody acts are governed process duties, honoured and recorded here, never proven by a test, and no test of this landing reads custody.

## 4. Proof successions (ADR-0060 Part J decision 38)

13. **Exactly the two successions that decision 38 stages for this landing move, each an exact transformation of its fixed pre-image at the baseline.** The placeholder probe found exactly these to refuse this landing. **No other existing proof moves at this landing.**

| Proof module | Site | Pre-image LF SHA-256 | Post-image LF SHA-256 |
|---|---|---|---|
| `tests/test_w8_discriminating_instrument_envelope.py` | V12 | `sha256:99047ceb3f58f5209598d9eb84cd6972cc2786ca4e7a43ce1dfbfe8f592d7323` | `sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80` |
| `tests/test_w8_validation_law.py` | VL10 | `sha256:b07e367761654ad3856f64598e513bea8b81badadab1fb2dd66b6a30082a88d9` | `sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02` |

14. The envelope's case-home limb admits the validation case home beside its three existing homes, its vacancy limb unchanged. VL10 keeps its former absences proven at the ADR-0060 landing commit and admits exactly this landing's case files, both manifests, this record and its three W8-D4 entries, the construction manifest joining the holders of its own schema literal; every later home, record and entry stays refused until its own landing.

## 5. Proof obligations

15. **Thirteen obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_validation_corpus.py`.** Each reads this landing's fixed snapshot, apart from the committed-object correspondence these immutable artefacts require (ADR-0060 decision 39). Before the landing commit exists, the twenty immutable corpus files are read as their raw, unconverted bytes, so their canonical form and every binding over them are proven on the bytes as written; once committed, the proofs read the committed objects, and a checkout's line-ending display is permitted only as correspondence to them:

| # | Obligation |
|---|---|
| **VC1** | The case home holds exactly the corpus at this landing, and once committed every corpus file corresponds to its committed object |
| **VC2** | Every case is lawful, canonical, mechanically named and free of packet structure |
| **VC3** | The identities are exactly the commitment manifest's, distinct, and disjoint from both earlier corpora |
| **VC4** | The commitment manifest's closed container, ordering and exact-byte binding; its commitments whole-string, distinct and disjoint |
| **VC5** | The construction manifest's closed shape, one-to-one with the commitment manifest; its commitments distinct and disjoint |
| **VC6** | No variant text is shared beyond one family's limit of three members |
| **VC7** | Textual non-reuse in both directions with both earlier corpora, and no validation sequence elsewhere at this landing |
| **VC8** | No reserved label, token, published schema literal, method label or construction schema literal on any visible surface of this landing |
| **VC9** | The stated total is eighteen wherever a total is stated |
| **VC10** | This record carries its statements and exposes no identity, unpinned digest or token |
| **VC11** | The two successions are the exact transformations pinned in section 4, whose table is read whole as exactly its header, separator and two trusted rows, as decision 38 stages them |
| **VC12** | The registry and the board change exactly as authorised, in draft or accepted form |
| **VC13** | This landing's census is exactly decision 16's |

16. **This landing's census is exactly twenty-six paths:** NEW `governance/validation-cases/W8-C-<64-hex>.json` (eighteen, named by identity) · NEW `governance/validation-cases/W8-V1-commitment-manifest.json` · NEW `governance/validation-cases/W8-V1-construction-manifest.json` · NEW `docs/phases/W8-D4-validation-corpus-record.md` · NEW `tests/test_w8_validation_corpus.py` · MODIFY `tests/test_w8_discriminating_instrument_envelope.py` · MODIFY `tests/test_w8_validation_law.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`.

## What this record does not establish

17. This record establishes no packet, session, disposition, register instance, reproduction at reveal, reveal, comparison, count or diagnosis; no class, method, family or composition of any case; no freshness beyond textual non-reuse and distinct identities; no semantic independence; no claim about the reviewer's prior exposure beyond what the session record will record; no verdict on the instrument, its validity, maturity, adequacy or readiness; no model behaviour of any kind; and no resolution of ADR-0047 precondition 3 or of any carried state. **Neither this record nor any of its green proofs supplies any of those acts or conclusions.**

## Public-safety note

Generic and structural wording throughout — corpus, case, manifest, custody, record, reviewer. No case text is quoted and no case is named. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The cases are on the table and the seals are in the drawer. What the reviewer sees is evidence; what the author intended waits, unread, for the reveal.*
