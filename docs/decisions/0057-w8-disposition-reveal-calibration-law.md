# 0057 — W8 Disposition, Reveal and Calibration Law

**Status:** Accepted by human reviewer, 2026-10-08. **Effective only on publication and remote verification. No W8-D3 session may be held before that moment, and every session held after it is held under this law.**
**Date:** October 2026 · **Phase:** W8 — Generative Evaluation Maturity · **Deliverable:** **W8-D3** (synthetic calibration; landing **D3-B**)
**Position:** the law the effective `W8-D3-SCB` opening brief requires to exist before any review session. **It renders no published case, holds no session, records no disposition, touches no custody location, reproduces no commitment, reveals nothing, compares nothing, counts nothing and contacts no model.** D3-C and D3-D remain separately authorised behind this record.
**Derived public baseline:** `f5b8ce789dc637f0cba3e3ef1920b410b2d21bc6`, the published and remotely verified W8-D3 opening
**Governed by:** the effective `W8-D3-SCB`, whole — this record turns its sections 4 to 8 into law and neither weakens nor extends them; **ADR-0054, whole — carried, never reinterpreted**; ADR-0055 as reconciled by `W8-D2-MSA`, whole; the effective `W8-D2-CBC`; `W8-D2-DIB`, `W8-D2-DIC` and `W8-D2-CM-01`; ADR-0050 for the human finding act; ADR-0056; the W8 runway; the W7 closure record as the carried-state authority
**Tier:** J — a governed session, recording, reveal and calibration law with downstream dependents, landed before the acts it governs.

---

**This record is the order of opening. It fixes how a human sees twelve cases without seeing anything else, how that human's twelve acts are written down where they can no longer move, how the sealed construction hypotheses are proven unaltered before anyone reads them, and how the two are then set side by side — case by case, as agreement or divergence, and as nothing more.**

## Decision question

**What are the exact session-packet law, disposition-register law, immutability law, custody and reproduction order, reveal sequence, calibration relation, permitted counts and bounded proof successions of W8-D3 — fixed completely before any session is held?**

## Part A — The session packet

1. **The session packet is rendered only by the published renderer `tests/w8_review_packet.py`, only from the committed Git object bytes of the published W8 review cases, as the effective `W8-D2-CBC` requires** — never from working-tree copies, never by hand and never by an unpublished tool. The renderer is deterministic and has no third-party dependency: it uses only the Python standard library apart from the published ADR-0055 envelope validator. Identical committed input bytes always produce identical packet bytes.
2. **The renderer accepts only an exact, lawful reviewer-visible case:** one canonical-bytes object passing the ADR-0055 reviewer-visible validator. **It refuses withheld authoring material** — the ADR-0055 withheld-record schema or any withheld-record field — **and refuses** malformed input, non-canonical bytes, duplicate identities, an empty set, and any variant line that could be read as packet structure.
3. **The packet is UTF-8 with LF line endings and exactly one terminal LF, and its structure is exactly:**

```
W8 REVIEW PACKET (w8-review-packet-v1)

Review question:
on the admissible source evidence alone, does a recognised governed property differ between the paired variants in a way that changes a downstream obligation, permission, authority, treatment or state?

Each case is reviewed independently, on its two variants alone. All three lawful dispositions are available on every case.

==== CASE <case_id> ====
---- BEGIN variant_a ----
<variant_a, whole and verbatim>
---- END variant_a ----
---- BEGIN variant_b ----
<variant_b, whole and verbatim>
---- END variant_b ----
Options: governance_delta_present | no_governance_delta | review_inconclusive
Disposition for <case_id>:
```

— one case block per case, in **ascending lexical `case_id` order**, blocks separated by one blank line. The review question is the ADR-0054 decision 26 question byte-identically. **Both variants appear whole, verbatim and whitespace-preserving, framed identically**, differing only in their label. The options line is identical on every case, in the doctrine's fixed order, with **no default and no pre-marked choice**; the response line carries nothing after its colon.

4. **The packet omits `structural_provenance_support`** — which remains present in the governed case artefacts as support material, never semantic grounding — **and omits** any diff, highlight, summary, length or similarity figure, digest other than the case identity itself, manifest content, ordering rationale, timestamp, running tally, token count, progress-by-token, and anything derived from withheld material.
5. **The packet is transient:** it is never tracked in the repository. Its SHA-256 is recorded in the session record, so that anyone can regenerate it from the published renderer and the published cases and confirm it.

## Part B — The session

6. **Only the human authority, acting as the human reviewer, supplies a disposition** (ADR-0054 decision 18). The implementer may render, prove completeness, record returned tokens exactly and bind them mechanically, and may not recommend, infer, default, fill, bulk-select or substitute. The architect may clarify governing law only — never case content — and may not recommend, rank or prefer.
7. **The session is the reviewer's:** reading order is free and revision before return is free. **The set is returned complete — exactly one of the three lawful tokens for every case — or the session is incomplete;** an incomplete session records nothing and reveals nothing.
8. **No authored class, intended disposition, construction map, authoring check, rationale, inconclusive-condition selection, nonce, expected distribution, class count, aggregate, recommendation, default, ranking, highlight, summary, diff or mechanical inference reaches the reviewer before all twelve dispositions exist and are recorded.**

## Part C — The disposition register and record

9. **The register is one closed canonical-bytes JSON object with exactly two fields, `schema` and `rows`: `schema` is byte-fixed as `w8-disposition-register-v1`; `rows` holds exactly one row per published case, sorted solely by `case_id`, each row exactly `case_id` and `disposition`, the disposition one of the three lawful tokens.** Its home is `governance/discriminating-review/W8-D3-disposition-register.json`, registered as a governed register whose acceptance the session record carries.
10. **The register carries no authored class, intended disposition, construction map, authoring check, rationale, inconclusive-condition selection, confidence, per-row timestamp or other withheld authoring metadata.** Once published, the human tokens can be counted mechanically: that distribution is a distribution of human acts, published as counts only under Part G, and it discloses nothing withheld.
11. **The session record** carries the act's date, the reviewer role, the packet SHA-256, the register binding, and the statement that every token is an individual human act — and, only if the reviewer volunteers one, a verbatim, non-disposition, non-evidentiary observation, admitted only if it reproduces no long run of case text and discloses nothing withheld; otherwise it is preserved outside the repository, on the `W7-D6-HDR` precedent.
12. **Immutability:** before the session record is published, the reviewer alone may revise a token, by explicit act. **After publication a disposition is fixed. After reveal, no disposition may be amended by any route.**

## Part D — Custody and reproduction order

13. **The session landing (D3-C) checks custody for existence only** — the expected records present by name, nothing opened, parsed or hashed.
14. **As a deliberate W8-D3 safeguard, nothing in the reveal landing (D3-D) begins until the session record is published and independently remote-verified.**
15. **Every published authoring commitment is reproduced by hashing the exact retained bytes directly, read-only, before any parse or reserialisation** (ADR-0055 decision 29). One missing record, one altered byte or one mismatch is **STOP AND REPORT**, with no reconciliation path.

## Part E — The reveal sequence

16. **After every commitment reproduces, the exact retained bytes are copied — without parsing, normalising, rewriting or reserialising them — to the untracked repository-relative reveal-candidate paths `governance/discriminating-reveal/<case_id>.json`, and each copy must hash to its published commitment.**
17. **The landing public-safety scan runs over exactly those candidate copies. The scanner is never run against the custody location,** so no custody location can appear in scanner output. **A finding is a STOP for the human ADR-0050 act; no implementer-created suppression, redaction or byte repair is permitted,** and no outcome is preselected.
18. **Only after a clean scan may the candidate bytes be parsed** — for cross-binding of each record to its case identity, filename, manifest row and published visible digest, and for the comparison of Part F.
19. Reveal publishes **the exact retained bytes**, never a reserialised, normalised or redacted form. **Before their first commit, proofs read the candidate copies exactly as written, unconverted, and each must hash to its commitment; once committed, proofs read the committed objects under `W8-D2-CBC`**, with the working-copy correspondence check that rule carries.

## Part F — The calibration relation

20. **For each case the comparison records exactly: the case identity, the human token from the published register, the authored intended token from the revealed record, and one relation from the closed two-member set `agreement` · `divergence` — `agreement` exactly when the two tokens are byte-identical, `divergence` otherwise. That is the whole of the comparison.**
21. **An authored intended disposition is a construction hypothesis, never an answer key and never a certified correct answer.** A divergence is recorded, never explained away, never corrected and never attributed to the reviewer; its diagnosis belongs to a later governed act, not to W8-D3. Revealed material is post-disposition calibration material only and never becomes evidence for, replaces or amends a disposition.

## Part G — Permitted counts

22. **Exactly two kinds of count may be published, only in the reveal landing and only after all dispositions exist: per-token counts of the human dispositions — all three tokens, zero counts included — and per-relation counts of `agreement` and `divergence`. Each count carries, in the same place, the statement that it is a count of individual human acts and nothing more** (ADR-0054 decision 31).
23. **No percentage, rate, score, grade, ranking, threshold, pass/fail result, model-performance claim or readiness interpretation** may be derived, published or implied. A column of identical marks would itself be a finding, never a success.

## Part H — Bounded proof successions

24. **Authorised for the reveal landing only:** the envelope module's V12 schema-string limb succeeds to a scoped form admitting the reveal home; the corpus module's C10 guard succeeds to a scope excluding the reveal home; and the corpus C7 board limb moves only if post-reveal board wording cannot avoid a reserved field name. **No other proof moves.** The committed-object reading rule is not a succession here: it is already effective through `W8-D2-CBC`.

## Part I — Doctrine carriage and boundaries

25. The nine anti-collapse rules carry whole:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

26. The human review question carries byte-identically from ADR-0054 decision 26: *on the admissible source evidence alone, does a recognised governed property differ between the paired variants in a way that changes a downstream obligation, permission, authority, treatment or state?*
27. **Standing duties at every W8-D3 landing:** P2 and Q3; P4a reported separately; **a fresh P4b human act at every landing**; publication only as the ADR-0056 public project identity. No model contact, prompt for contact, provider, credential, SDK, transport, binary or contact harness exists or is authorised; **ADR-0047 precondition 3 remains outstanding in its lawful resting state.** Every carried state — Part Q, the `local-wordlist` seam, the historical unknowns, the pending stubs, the inherited W6 inventory, the stale registry derivative, the inert allowlist entries and the two carried LF-checkout proof findings — stays exactly where it is.

## Part J — Proof obligations

28. **Twelve obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_calibration_law.py` over a clearly labelled mechanics sentinel — never over a published case:**

| # | Obligation | Decidability |
|---|---|---|
| **K1** | This record carries the review question, the nine rules, the three tokens, the relation set, the count statement and the D3 ordering law; the renderer's template carries this record's skeleton exactly | **Mechanical** |
| **K2** | The renderer refuses withheld authoring material, malformed or non-canonical input, duplicates, an empty set and structural-collision variants | **Mechanical** |
| **K3** | No default and no preselection: options identical on every case, response lines empty, token occurrences exactly one per case | **Mechanical** |
| **K4** | Completeness and verbatim carriage: both variants present, whole and whitespace-preserving | **Mechanical** |
| **K5** | Symmetry: both variants framed identically, differing only in label | **Mechanical** |
| **K6** | Omission: no provenance support, digest, tally, timestamp, summary, diff or withheld-derived material in the packet | **Mechanical** |
| **K7** | Determinism and committed-object reading: identical committed bytes yield identical packets; order of input and working-copy changes do not move the packet | **Mechanical** |
| **K8** | Ascending `case_id` order | **Mechanical** |
| **K9** | The register's closed shape, token set, ordering, canonical bytes and one-to-one binding | **Mechanical** |
| **K10** | The relation and count mechanics: `agreement`/`divergence` exactly; the two count kinds only, each with its statement | **Mechanical** |
| **K11** | The renderer reads only committed objects — no file, environment or network access — and no proof renders a published case | **Mechanical** |
| **K12** | Absence: no tracked packet, register or reveal artefact exists | **Mechanical for absence; the semantic quality of any future disposition is the human act itself** |

29. **Every K-row proves mechanics and carriage only.** No proof decides, predicts or hints at any disposition, any authored intent or any relation; and no green result is evidence about any case or any reviewer.

## What this record does not establish

30. This record establishes no session, no packet of published cases, no disposition, no register instance, no custody access, no commitment reproduction, no reveal, no comparison and no count; no model behaviour of any kind; no resolution of ADR-0047 precondition 3 or of any carried state; and no change to any W8-D2 artefact or W7 record. **No disposition ever made under this law may be cited as evidence for any of those propositions.**

## Public-safety note

Generic and structural wording throughout — packet, register, reveal, relation, count, reviewer, instrument. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems where needed. No case text is quoted. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no custody location and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The human writes first and the writing is published; the seals are proven before they are broken; the hypotheses are read last; and what the two say side by side is recorded as exactly that — agreement or divergence, counted as human acts, and claimed as nothing more.*
