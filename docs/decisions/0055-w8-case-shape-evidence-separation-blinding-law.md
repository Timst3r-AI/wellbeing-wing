# 0055 — W8 Case Shape, Evidence Separation and Blinding Law

**Status:** Accepted by human reviewer, 2026-10-03. **Effective only on publication and remote verification. No W8 case may be authored before that moment, and every case authored after it is authored under this law.**
**Date:** October 2026 · **Phase:** W8 — Generative Evaluation Maturity · **Deliverable:** **W8-D2** (discriminating instrument; landing **D2-B**)
**Position:** the envelope law the effective `W8-D2-DIB` opening brief requires to exist before the first case. **It authors no case, generates no authoring record, generates no nonce, computes no real commitment, materialises no corpus, performs no review, contacts no model, and opens no later landing.** D2-C is separately authorised behind this record.
**Derived public baseline:** `f8430ccc484e046ea950e96b33550ad3ee7df389`, the published and remotely verified W8-D2 opening
**Governed by:** the effective `W8-D2-DIB`, whole; **ADR-0054, whole — carried, never reinterpreted**; the W8 runway and `W8-D1-EDB`; ADR-0046 through ADR-0053 as consumed by ADR-0054; the W7 closure record as the carried-state authority
**Tier:** J — a governed record-shape and blinding law with downstream dependents, landed before the artefacts it governs.

---

**This record is the envelope. It fixes, before any paper exists: exactly what a reviewer may see, exactly what an author must seal away, how a case gets a name no author chose, how cases stand in an order no author arranged, and how the sealed record is committed so that opening it later can be proven honest to the byte. Nothing in this law knows any answer, and everything in it exists so that nothing else can whisper one.**

## Decision question

**What is the exact reviewer-visible case shape, the exact withheld authoring-record shape, the canonical-byte law, the neutral identity and ordering law, the nonce and commitment mechanics, the manifest shape, and the custody contract of the W8 discriminating instrument — fixed completely before any case is authored?**

## Part A — The reviewer-visible case shape

1. **The W8 case class is a new class.** It does not reuse, extend or adapt the W7 generated-evaluation (GER) class under `governance/generated-evaluation/`, whose records and law remain historically true and untouched.

2. **The reviewer-visible case is one closed JSON object with exactly four top-level fields and no undeclared field:** `schema` · `case_id` · `admissible_source_evidence` · `structural_provenance_support`.

3. **`schema` is byte-fixed as `w8-review-case-v1`.**

4. **`admissible_source_evidence` contains exactly two fields:** `variant_a` and `variant_b`, each a whole, non-empty string, and not byte-identical to each other. **They are the only semantic grounding available to the human reviewer** (ADR-0054 Part F carried).

5. **`structural_provenance_support` contains exactly three fields:** `synthetic` byte-fixed `true` · `source_evidence_sha256`, the 64-lowercase-hex SHA-256 of the exact canonical bytes of the `admissible_source_evidence` object as fixed in Part C — the same digest from which the case identity derives · `governed_by`, byte-fixed as the two-member list `["ADR-0054", "ADR-0055"]`. **This object is support material only and cannot become semantic grounds for a disposition.**

6. **Forbidden reviewer-visible material, closed by prohibition:** no title, authoring class, intended answer, governed-property key, rationale, expected token, surface-feature label, summary, diff, highlight, timestamp, authoring sequence, or descriptive filename — and nothing else beyond decision 2's four fields, so that the prohibition cannot be routed around by invention.

## Part B — Neutral variant orientation

7. **The author must not choose which text becomes `variant_a` and which becomes `variant_b`.** For the two final variant strings, compute SHA-256 over each exact UTF-8 byte sequence; **the variant whose digest sorts lexically first becomes `variant_a`**, the other `variant_b`. Identical byte sequences are invalid.

8. **No rewriting, nonce search or wording adjustment may be undertaken to obtain a preferred orientation.** If wording changes for a legitimate authoring reason, orientation is recomputed mechanically from the new bytes, and the change itself is recorded in the withheld authoring rationale.

## Part C — Canonical bytes

9. **One serializer governs every W8 reviewer-visible object and withheld authoring record:** UTF-8 · no BOM · JSON keys sorted · `ensure_ascii = false` · compact separators `","` and `":"` · NaN and Infinity forbidden · **exactly one terminal LF** · no Unicode normalisation after authorship. The governing operation is equivalent to:

```
json.dumps(value, ensure_ascii=False, sort_keys=True,
           separators=(",", ":"), allow_nan=False) + "\n"
```

10. **No later pretty-print, line-ending conversion or reserialisation may stand in for committed bytes.** The canonical bytes are the artefact; everything else is display.

## Part D — Neutral identity and ordering

11. **The case identity derives from the evidence and nothing else.** After deterministic orientation, canonicalise exactly the object `{"variant_a": …, "variant_b": …}` under Part C; let its SHA-256 digest be `H`. **The case identity is `W8-C-` followed by the full 64-lowercase-hex `H`, untruncated.** The reviewer-visible filename is derived mechanically from the identity alone: `<case_id>.json` — no descriptive suffix and no author-selected identifier anywhere.

12. **A collision is a stop.** If two proposed cases produce the same identity, **STOP** — no numbering, suffixing, renaming or collision repair.

13. **Presentation order is ascending lexical order of the full `case_id`, computed after the case bytes are frozen.** No authored class, intended disposition, governed property, creation time or author preference participates in identity or order.

14. **Hash grinding is prohibited.** A case may not be rewritten or regenerated because its computed identity would place it at an inconvenient or revealing position. **Identity and ordering are consequences of visible evidence, never another place for the author to whisper the answer.**

## Part E — The withheld authoring record

15. **The withheld authoring record is one closed canonical JSON object with exactly eleven fields and no undeclared field:** `schema` · `case_id` · `authored_class` · `intended_disposition` · `property_construction` · `surface_features_varied` · `inconclusive_conditions` · `authoring_checks` · `authoring_rationale` · `reviewer_visible_sha256` · `commitment_nonce`. **It never enters any reviewer-visible surface before disposition.**

16. **`schema` is byte-fixed as `w8-authoring-record-v1`.** `authored_class` has exactly three values — `A` · `B` · `C`. `intended_disposition` uses exactly ADR-0054's three tokens — `governance_delta_present` · `no_governance_delta` · `review_inconclusive`. **The binding is fixed: A → `governance_delta_present` · B → `no_governance_delta` · C → `review_inconclusive`.** The binding records the construction hypothesis only; **it is never a certified correct answer and never evidence available to the human reviewer before disposition.**

## Part F — The governed-property construction map

17. **`property_construction` contains exactly the nine ADR-0054 recognised governed properties — no tenth and no omission:** `authority` · `provenance` · `permission` · `persistence` · `memory treatment` · `decision status` · `boundary crossing` · `attribution` · `review state`. **Each maps to exactly one authoring-only state from the closed set:** `same` · `different` · `underdetermined` · `not_engaged`.

18. **Class constraints, structural and binding:** **Class A** requires at least one `different` and no `underdetermined`. **Class B** permits only `same` or `not_engaged`, with all nine affirmatively checked. **Class C** requires at least one `underdetermined`, with no established `different` on which a substantive answer could rest.

19. **Any need for a tenth governed property is an immediate STOP and a doctrine-amendment signal, never a schema extension** — ADR-0054 decision 2's prior-authority law carried: a case may reveal, it may never extend.

## Part G — Class-specific authoring requirements

20. **Class A:** the withheld record must identify the recognised property intended to differ, locate the visible evidence from which the difference is meant to be readable, and record that the author checked that `governance_delta_present` could lawfully be reached from visible source evidence alone.

21. **Class B:** the withheld record must carry the affirmative nine-property equivalence check, at least one materially varied surface feature in `surface_features_varied`, and the author's check that `no_governance_delta` could lawfully be reached from visible evidence alone.

22. **Class C:** the withheld record must name the engaged property, identify at least one exact ADR-0054 Part D condition being deliberately exercised, and record why a substantive answer would require evidence or authority the reviewer does not lawfully have.

23. **`authoring_checks` is a list of unique declarations from a closed nine-label vocabulary, with exactly the class-required labels present and no other class's labels:** class A requires `delta_property_identified` · `delta_evidence_located` · `delta_reachable_from_visible_evidence_checked`; class B requires `equivalence_all_nine_checked` · `surface_variation_recorded` · `non_delta_reachable_from_visible_evidence_checked`; class C requires `engaged_property_named` · `part_d_condition_identified` · `substantive_answer_unavailable_recorded`. Structural proofs prove the declarations exist, use this closed vocabulary, and match the authored class; **they may not prove that a semantic declaration is true** — that remains review-only, exactly as ADR-0054 Part K classifies it. **Structural shapes, closed:** `authoring_rationale` is a whole, non-empty string; `surface_features_varied` is a list of unique entries drawn from ADR-0054's eight surface features — `tone` · `warmth` · `confidence` · `verbosity` · `phrasing` · `formatting` · `politeness` · `explanatory depth` — with at least one entry for class B; `inconclusive_conditions` is a list of unique entries from Part H's four labels; `case_id` carries the exact `W8-C-<64-lowercase-hex>` shape and **must byte-equal the reviewer-visible case identity it seals**; and every hash-valued field carries the exact `sha256:<64-lowercase-hex>` shape.

## Part H — The inconclusive-condition vocabulary

24. **For the withheld record only, four closed labels correspond one-to-one with ADR-0054 decision 11:** `insufficient_source_evidence` · `multiple_material_governed_interpretations` · `unresolved_conflict_within_source_evidence` · `requires_unavailable_external_authority`. **Class C requires at least one; classes A and B require none.** These labels are withheld construction metadata, never reviewer evidence.

## Part I — Binding hash, nonce, and commitment

25. **`reviewer_visible_sha256`** is `sha256:` followed by the 64-lowercase-hex SHA-256 of the exact final canonical bytes of the complete reviewer-visible case object. It binds the hidden construction record to the exact visible case without disclosing the hidden record.

26. **The commitment nonce:** for future D2-C authoring, and for the one supplementary corpus authored under ADR-0059, each case receives **exactly 32 bytes of CSPRNG output, represented as 64 lowercase hexadecimal characters, generated once only, after the non-nonce authoring fields and the reviewer-visible bytes are frozen.** Standard-library cryptographic randomness is sufficient; **introducing a provider, credential, secret service or dependency is forbidden.** The nonce **carries no capability**, is not a credential or secret authority, exists only to prevent practical enumeration of a small hidden authoring vocabulary, **is never rerolled to obtain a preferred commitment**, and remains withheld until the reveal of its own corpus. **D2-B generates no nonce**; this record's proofs use a clearly labelled deterministic mechanics-only sentinel and create no W8 case specimen.

27. **The authoring commitment is `sha256:` followed by the SHA-256 of the exact canonical withheld-authoring-record bytes, including `commitment_nonce`.** It is an integrity commitment — not encryption, not confidentiality, not authority and not a credential. **Once published by D2-C — or, for the supplementary corpus, by its own authoring landing — neither the hidden record nor the nonce may move.**

## Part J — The D2-C manifest shape, defined and not materialised

28. **The future class-opaque manifest carries one row per case, sorted solely by `case_id`, each row exactly:** `case_id` · `reviewer_visible_sha256` · `authoring_commitment_sha256`. **The manifest instance itself is one closed two-field JSON object — exactly `schema` and `rows`, with no undeclared outer or row field: `schema` byte-fixed as `w8-commitment-manifest-v1`, and `rows` the array containing exactly the rows this decision governs — serialised under Part C canonical bytes, with exactly one manifest instance for the D2-C corpus at `governance/discriminating-instrument/W8-D2-commitment-manifest.json`.** *(Container fixed by the `W8-D2-MSA` reconciliation; effective only on that record's acceptance, publication and remote verification; nothing in it changes class opacity, commitment semantics, custody, reveal, case identity, ordering, or any other law of this record.)* **The one supplementary corpus authored under ADR-0059 has exactly one manifest instance of its own, under this same container law, at `governance/discriminating-supplement/W8-S1-commitment-manifest.json`; each manifest instance binds its own corpus only, and no row of one corpus appears in the other's.** **It contains no authored class, intended disposition, governed-property construction, rationale, expected distribution, class count or authoring sequence.** The total number of cases is visible once the corpus exists; **the composition is not.** **Each row corresponds one-to-one to exactly one reviewer-visible case and exactly one withheld record: its `case_id` names an existing case, its `reviewer_visible_sha256` equals the digest of that case's exact published bytes, and its `authoring_commitment_sha256` equals the SHA-256 of the exact retained hidden bytes for that same case — with no orphan row, no orphan case and no orphan record in either direction.**

## Part K — The custody contract

29. **For each corpus, from its authoring landing until its custody ends by a separately governed act — for the supplementary corpus authored under ADR-0059, its own reveal; for the D2-C corpus, only its own separately governed act, which no session, reproduction or reveal of another corpus supplies:** the exact withheld-record bytes remain outside the repository and outside every surface the human reviewer can see · no reserialisation, repair, scrubbing or normalisation is permitted · **each authoring landing — D2-C, and the supplementary authoring landing — must read its retained bytes back and reproduce every proposed commitment before landing** · **D3 must reproduce every published commitment of the corpus being revealed — and of no other corpus — from the same retained bytes before reveal and before any calibration comparison** — and **commitment reproduction hashes the exact retained bytes directly, before any parse or canonical reserialisation; a reproduction path that parses and reserialises retained material is itself unlawful, so altered bytes can never be repaired into agreement** · one missing record, one altered byte or one commitment mismatch is **STOP AND REPORT** · **there is no reconciliation path** · and no hidden record may appear in a relay message, chat response, commit message, README, registry role, log excerpt or proof output visible to the reviewer.

30. **No new external provider, credential, secret store or dependency may be named or introduced to solve custody.** If the existing outside-repository review transport cannot guarantee byte-stability across D2 to D3 — or, for the supplementary corpus, from its authoring to its reveal, in a custody sub-location of its own — **STOP before the first case of that corpus is authored.**

## Part L — Evidence separation and doctrine carriage

31. **ADR-0054's four evidence categories carry whole, with no category conversion:** admissible source evidence is the sole semantic grounding; structural and provenance support material is integrity and provenance only; withheld authoring material is invisible before disposition; post-disposition calibration material is revealed later and is never retroactive evidence.

32. **The human review question carries byte-identically from ADR-0054 decision 26:** *on the admissible source evidence alone, does a recognised governed property differ between the paired variants in a way that changes a downstream obligation, permission, authority, treatment or state?* **All three tokens remain available on every future case, with no default, recommendation, pressure or preselection**, and the nine evaluation anti-collapse rules carry whole wherever they are carried:

> **confidence ≠ authority · verbosity ≠ governance significance · warmth ≠ permission · explanation ≠ evidence · textual difference ≠ governance difference · textual similarity ≠ governance equivalence · absence of explicit wording ≠ absence of governed effect · mechanical agreement ≠ human acceptance · uncertainty ≠ failure.**

33. **Standing duties bind at every W8-D2 landing:** P2 and Q3; P4a reported separately; **a fresh P4b human act at every landing**; and no model contact, prompt for contact, provider, credential, SDK, transport, binary or contact harness anywhere in this deliverable. ADR-0047 precondition 3 remains outstanding in its lawful resting state.

## Part M — Proof obligations

34. **Twelve envelope obligations, mechanics only, each with planted-mutant controls, landed in `tests/test_w8_discriminating_instrument_envelope.py`:**

| # | Obligation | Decidability |
|---|---|---|
| **V1** | The closed reviewer-visible top-level shape — extra or missing field detected | **Mechanical** |
| **V2** | The exact `variant_a`/`variant_b` admissible-evidence shape: whole, non-empty, distinct, symmetric presence | **Mechanical** |
| **V3** | Forbidden pre-disposition fields absent — planted class, intended-answer, property-key and rationale leakage detected | **Mechanical** |
| **V4** | Deterministic orientation, identity derivation and class-independent lexical ordering — hidden-material changes cannot change identity or order | **Mechanical** |
| **V5** | The closed withheld-authoring-record schema and the exact `A`/`B`/`C` and three-token sets | **Mechanical** |
| **V6** | The exact nine-property construction map — tenth-property and missing-property mutants detected | **Mechanical** |
| **V7** | The exact class-to-token binding and the class-specific structural constraints | **Mechanical** |
| **V8** | Canonical-byte and SHA-256 reproducibility — one-byte mutation detected | **Mechanical** |
| **V9** | Nonce shape and no-capability carriage, using only a labelled mechanics sentinel | **Mechanical** |
| **V10** | The future manifest's one-to-one cross-artefact binding — row to exact visible bytes and exact retained bytes — with duplicate rejection, lexical ordering and class opacity | **Mechanical** |
| **V11** | Custody and reveal sequencing: commitment reproduction over exact retained bytes, before any parse, before reveal and before calibration; a semantics-preserving byte mutation is a stop; repair by reserialisation refused | **Mechanical over the mechanics; the custody of real bytes is a governed human process this proof cannot see** |
| **V12** | Doctrine carriage — the exact human question, the nine rules, the four categories, no conversion, no contact, the standing duties — and that **D2-B itself contains no W8 case, corpus, authoring record, nonce or real commitment** | **Mechanical for carriage and absence; the semantic meaning of any future case is review-only in full** |

35. **Every V-row proves mechanics and carriage only.** No proof in this record's module decides, predicts or hints at any case's authored class or human disposition; no proof establishes that an authoring declaration is semantically true; and no green result is evidence that any future case is well-constructed — V9 of ADR-0054 remains review-only at authoring, and V8 of ADR-0054 remains the human act.

## What this record does not establish

36. This record establishes no W8 case, no corpus, no authoring record, no nonce, no commitment, no manifest instance, no calibration, no disposition, no reveal, and no contact surface; no model behaviour of any kind; no resolution of ADR-0047 precondition 3, Part Q, the `local-wordlist` seam, any historical unknown or any inherited item; no change to the W7 GER class or any W7 record — **W7 remains historically true**; and no opening of D2-C, which lands only as its own separately authorised candidate under this law. **No disposition ever made under the instrument this law governs may be cited as evidence for any of those propositions.**

## Reconciliation note (ADR-0059)

Decisions 26 to 30 are reconciled in place by ADR-0059, the phase-level supplementary recovery authority, so that their nonce, commitment, manifest, custody and transport provisions bind each corpus separately: the D2-C corpus exactly as before, and the one supplementary corpus that record opens. The reconciliation is effective only on ADR-0059's acceptance, publication and remote verification. Every other decision of this record is unchanged; the published D2-C corpus, manifest and commitments are byte-untouched; and nothing in it changes the case shape, canonical bytes, identity, ordering, withheld-record shape or class opacity.

## Public-safety note

Generic and structural wording throughout — case, variant, class, record, commitment, nonce, reveal, reviewer, instrument. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The envelope is sealed before the letter is written, addressed by arithmetic instead of by hand, and filed in an order nobody picked. When the paper finally arrives, the only thing it will be able to say is what the evidence shows — because every other channel was closed by law while the drawer was still empty.*
