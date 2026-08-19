# 0049 — Field Law for Generated-Output / Authored-Specimen Evaluation Records (W7-D2-C)

**Status:** Accepted by human reviewer, 2026-08-19. Not a build instruction. Authorises no implementation by itself.
**Date:** August 2026 · **Phase:** W7 — First-Contact Governance and Synthetic Model Evaluation · **Deliverable:** **W7-D2** (landing **W7-D2-C**, the third of five)
**Position:** the third W7-D2 landing. ADR-0048 chose the ground and the material; **this record draws the blueprint** — every field, its nesting, its order, its nullability, and the vocabularies it may carry. **It pours no concrete:** no directory, no schema file, no manifest, no record, no proof module, and no generated-output, authored-specimen, capture-payload or example-payload text.
**Constitutional references:** W0 Laws 1, 3, 6, 8, 9, 10, 11, 13; W0 §10; W0 Non-Goal 7. **No law is amended.**
**North star carried:** **generated text may enter the public Wing only as synthetic, governed evaluation evidence** — never authority, advice, truth, safety evidence, approval, or a decision about any person.
**Resolves:** none.

---

**A blueprint for a container that has never held anything is really an argument about what could go wrong, written in field names. So this one is mostly about what is missing. There is no field for a winner, because a nullable winner is a winner waiting. There is no field on a capture that could make it an input again, because recirculation you cannot express is recirculation you cannot do. There is no field for the text a scan objected to, because the report of a problem must not repeat it. And there is no way for a machine to write a review disposition, because the only lawful values belong to a record that has not been written yet. Everything present is here to be declared. Everything absent is here to be impossible.**

## Decision question

**What exactly does a future generated-output or authored-specimen evaluation record contain — which fields, at which level, in what order, required or nullable, drawn from which vocabularies and owned by whom — such that provenance cannot be laundered, a pair cannot be half-recorded, a winner cannot be named, captured text cannot be recirculated, a machine cannot write a human's disposition, and **the non-authority ceiling cannot be absent from a complete governed record, while a partial excerpt cannot lawfully be represented as the complete governed record or as carrying its full governance context** — decided now, without creating the schema file, a manifest, or a single record?**

## Controlling law

- **ADR-0048 (W7-D2-B), whole and consumed rather than re-decided** — the class is an extension of the existing evaluation-record class (3–6); the home `governance/generated-evaluation/`, reserved and not created (7–10); **JSON as material and format class only, with this record owning every future key name, order, nesting, nullability, value set and field** (11–13); one record per evaluation unit with both captures whole and omission expressible as a schema violation (14–16); **registered manifest per run, content hash per record, one registry entry per run** (17–21); **captured text never edited once landed, human-review fields written afterwards as subsequent governed acts** (22–25); the shape is not permission (26–29).
- **ADR-0046, whole** — the three lawful origins closed with a fourth unlawful (7–8, 10); **no-recirculation, capture terminal (9)**; the closed exclusion list (11–12); **provenance declarability as the admission condition and the five minimum declarable facts (19–22)**; **the non-authority ceiling carried byte-identically inside every record, with specimen parity (23–26)**.
- **ADR-0047, whole** — the three provenance definitions (3); **provenance does not launder in either direction (4)**; handling binds identically on both classes (6–8); the seven preconditions (9–11); **contact is complete at transmission-and-return whether or not anything is kept (3a, 12)**.
- **`W7-AR`** — §3 north star; **§6's nine binding properties**, of which this record makes six structural; **§7's reservation of the model boundary to W7-D3**; §8.1, §9, §10.
- **`W7-D2-RSB`** — the six standing statements and the five-component sequence; **all W7-D2 proofs land in W7-D2-E.**
- **ADR-0034 B6 decisions 32–35** · **W2-D4** rules 1–6, §3 conventions, **§4 the marker-block precedent** · **ADR-0007** decisions 1, 2, 4, 6 · **`W7-D1-FCB`**, whole.
- **Live repository artefacts, read as precedent rather than doctrine** — the W5-D4 records under `governance/evaluation/`, whose probes already carry `paired_variant_captures` **as an object keyed by variant label**, a `delta_finding` of `{outcome, differing_surfaces, missing_surfaces}` with **no winner field**, and a declared `routed_to_human_review`; the harness's closed outcome set `no-delta-observed` / `routed-to-review` / `unknown-not-absent`; the four `OBSERVED_SURFACES`; and the scan machinery's own category names.

## Decisions

### Part A — The door

1. **This record decides the blueprint and pours no concrete.** After its landing the repository contains exactly one new governed artefact: this record. **`governance/generated-evaluation/` still does not exist. No schema file exists. No proof module exists. No manifest exists. No generated or specimen record exists.** No run, probe, fixture or harness. **No generated-output text, authored-specimen text, capture payload text, or example payload text is authored, generated, or imported by this landing** — this record is itself authored governance prose, which is not payload text and is not of the class it governs.

2. **C does not discharge W7-D2 by itself.** W7-D2-D and W7-D2-E remain unlanded. **W7-D3 remains unbegun and the model boundary remains unchosen. No model may be contacted after this record lands.**

3. **ADR-0048 is consumed, not reopened.** Home, format class, granularity, integrity posture and immutability are fixed inputs. This record adds nothing to them and narrows nothing in them.

### Part B — The canonical record shape

4. **One top-level wrapper key, `generated_evaluation_record`**, mirroring the existing `evaluation_record` idiom of the class this one extends.

5. **Fifteen record-level fields, every one always present, in this canonical order.** No omitted keys, no hidden defaults; **absence of a required key is an error, never a default.**

| # | Field | Holds | Nullable |
|---|---|---|---|
| 1 | `record_id` | `GER-####`, flat and meaning-free; allocation order encodes nothing — **the namespace this record mints, Part S** | no |
| 2 | `run_id` | the run this record belongs to; the manifest's join key | no |
| 3 | `authorising_record` | citation to the governed record that authorised the run | no |
| 4 | `as_of` | the run date | no |
| 5 | `synthetic_marker` | `{synthetic: true, notice}` — `synthetic` literally `true` as an assertion target; **`notice` byte-fixed at the value in Part T** | no |
| 6 | `model_contact` | `{occurred, contact_class, authorising_record}` — Part F | one inner |
| 7 | `inputs` | non-empty array; each `{origin, citation, reference}` — Part E | no |
| 8 | `pairing` | `{probe_id, variant_labels}` — exactly two distinct labels — Part G | no |
| 9 | `captures` | **object keyed by variant label**, key set identical to `pairing.variant_labels` — Part H | no |
| 10 | `delta` | `{outcome, differing_surfaces, missing_surfaces}` — Part I | no |
| 11 | `findings` | array of finding events; empty is lawful and meaningful — Part K | no |
| 12 | `exclusion_check` | `{list_reference, checked: true, result}` | no |
| 13 | `no_recirculation` | `{capture_terminal: true}` — a literal-true assertion target | no |
| 14 | `human_review` | `{routed, disposition, disposition_record}` — Part J | two inner |
| 15 | `non_authority` | **the ADR-0046 decision 23 ceiling sentence, byte-identical** — Part L | no |

6. **Five capture-level fields**, inside each value of `captures`, in this canonical order:

| # | Field | Holds | Nullable |
|---|---|---|---|
| 1 | `text_class` | closed two-value set — Part D | no |
| 2 | `authoring_record` | citation to the act that authored a specimen | yes — Part D |
| 3 | `text` | the capture payload | no |
| 4 | `text_digest` | `sha256:` of the `text` value only — Part M | no |
| 5 | `scan_status` | closed two-value set — Part K | no |

7. **Which facts live where, decided rather than inherited by habit.** **Record level** holds what is true of the evaluation unit: identity, provenance posture, contact posture, inputs, the pair's declaration, the delta, findings, the standing checks, the review slot, and the ceiling. **Capture level** holds only what is true of one side of the pair: its class, its authoring citation, its text, that text's digest, and its scan status. **Review level** holds the routing fact and the later human act, and the two are not the same: **`human_review.routed` is a creation-time fact** the record carries when it is written, while **`human_review.disposition` and `human_review.disposition_record` are the later human act** — **the only two positions in the whole shape a later act may fill.** **Nothing appears at two levels**, and no capture-level field describes the unit.

   **The counting convention, fixed so "field count" has one meaning.** A *schema-property position* is a named key in a declared object shape. **Repeated instances are counted once per distinct shape, never per instance** — one `inputs` item shape, one capture-object shape, one finding-event shape, however many the record holds. Under that convention:

| Level | Positions |
|---|---|
| Wrapper key (`generated_evaluation_record`) | 1 |
| Top-level record fields | 15 |
| Nested record-object and item fields (`synthetic_marker` 2 · `model_contact` 3 · `inputs[]` item 3 · `pairing` 2 · `delta` 3 · `exclusion_check` 3 · `no_recirculation` 1 · `human_review` 3) | 20 |
| Capture-object fields | 5 |
| Finding-event fields | 5 |
| **Total schema-property positions** | **46** |

   **`locus`'s inner positions are not counted here**, because its inner shape is W7-D2-D's and does not exist yet.

### Part C — Canonical order and its rationale

8. **The order is governed, not cosmetic. A reader meets the record in the direction the governance runs:** *identity → what it is made of → whether anything was contacted → what went in → what was expected → what came back → what differed → what was found → what was checked → what a human owes → what none of it may be taken to mean.*

9. **Three orderings decided against the obvious.** **`pairing` precedes `captures`** — the declaration of what must be present comes before the thing that must be present, mirroring `synthetic_marker` preceding `inputs`; a reader learns the pair's shape before meeting either half, so a missing half is legible on the way past rather than on reflection. **`findings` precedes the standing checks**, because a finding is a fact about this run while the checks are obligations discharged for every run. **`non_authority` is last, always** — not because it follows the captured text, which it does not: `delta`, `findings`, the two standing checks and `human_review` sit between them. **It is last because a reader finishes the complete governed record on the ceiling, and no field may be appended after it.** The ceiling is the record's closing statement, not its caption on the text.

### Part D — Provenance, and why it cannot be laundered

10. **`text_class` is a closed two-value set on each capture:** **`generated_output`** — text produced by a model — and **`authored_synthetic_specimen`** — text written by a human inside this repository, from nothing, deliberately carrying the properties of generated prose. ADR-0047 decision 3(b) and 3(c), verbatim in meaning.

11. **The distinction is provenance, never appearance, and the schema never asks how the text looks.** A specimen indistinguishable from generated output is a specimen. A generated sentence rewritten by a human is generated output. **There is no field describing style, fluency, plausibility, or model-likeness**, because any such field invites classification by resemblance and resemblance is exactly what ADR-0047 decision 4 forbids.

12. **Two structural constraints make a laundered claim invalid rather than merely untrue.** A schema cannot stop a lie, but it can stop a lie from being *well-formed*:
   - **A capture may declare `generated_output` only if `model_contact.occurred` is true.** No contact, no generated output — the class cannot appear in a record that declares nothing was contacted.
   - **A capture declaring `authored_synthetic_specimen` must carry a non-null `authoring_record`**, citing the governed act that authorised the authoring. **A specimen with no named author-act is invalid**, so relabelling generated text as a specimen requires manufacturing a citation to a record that must exist.

13. **`authoring_record` is null if and only if `text_class` is `generated_output`.** Both directions bind: generated output carries no authoring citation, and a specimen without one is not a specimen.

14. **A record may hold captures of both classes.** ADR-0047 decision 6 binds the handling identically, so a mixed unit is lawful and **visible** rather than impossible-to-express. `text_class` never changes what is required of a capture; it changes only what the record honestly says about where the text came from.

### Part E — Inputs and the closed origin set

15. **`inputs` is a non-empty array. Each input declares `origin` from the closed three-value set** — **`authored_synthetic`**, **`repository_fixture`**, **`governed_public_record`** — carried from ADR-0046 decision 7, with a `citation` locating it and a `reference` naming what was used. **A fourth value is invalid**, per ADR-0046 decision 8, and an empty `inputs` array is invalid because an evaluation unit with no declared input has no declared provenance at all.

### Part F — Model-contact declaration, and contact ≠ authorised

16. **`model_contact` is `{occurred, contact_class, authorising_record}`.** `occurred` is a boolean. `authorising_record` is a citation or null.

17. **The nullability law is conditional on `occurred`, and it is the only rule this record states.** **`occurred: false`** requires `contact_class: "none"` and `authorising_record: null`. **`occurred: true`** requires a `contact_class` member W7-D3 has authorised and a **non-null** `authorising_record`. There is no valid record in which contact occurred and nothing is cited.

   **Contact ≠ authorised survives this, and is not weakened by it.** `occurred: true` states only the fact that contact happened; **the cited record is not thereby proven to have lawfully authorised it**, and whether the citation resolves under the later contact gate is **a separate validation obligation** belonging to that gate. A citation is a claim, not a clearance.

   **This class does not need to make an invalid contact record landable in order for an incident to be reported honestly.** ADR-0047 decisions 12–15 govern an ungated contact through **stop-and-report**. **The stop-and-report obligation exists under ADR-0047; a generated-evaluation record is not that incident report**, and this record neither designs nor names the form such a report takes.

18. **`contact_class` has exactly one value owned by this record: `none`.** It is the lawful value when `occurred` is false, and it is the only lawful value today. **Every other member of the set is W7-D3's**, and this record does not enumerate, hint at, rank, or reserve one. It fixes the field's existence and its type, and nothing else. **Nothing here prefers or forecloses a repository-managed local dependency, an adapter to an externally running local model, a manual governed import, or no public model contact with authored specimens** — the field is identical in shape under all four.

19. **Today, only the no-contact `model_contact` posture is expressible under this field law**, because every contact-bearing `contact_class` member belongs to **W7-D3** and none exists. **That is a statement about this field, not about records:** no record of this class may be materialised at all yet, since `pairing.variant_labels` is still W7-D4's. A consequence of the gates, not a preference of this record.

### Part G — Pair completeness

20. **`pairing` is `{probe_id, variant_labels}`, where `variant_labels` is an array of exactly two distinct labels.**

21. **`captures` is an object whose key set is identical to `pairing.variant_labels`** — same members, same count, no extras, no absences. **This is where pair completeness becomes structural.** A missing variant is not a shorter array, not a null, not an empty convenience value, and not an editorial choice: **it is a key that the record declared and did not provide**, which is a schema violation on its face.

22. **There is deliberately no `paired` boolean and no `expected_capture_count`.** A boolean creates a `false` branch in which one capture is lawful, and a count creates a number that can be set to one. **The pair is not a property the record asserts; it is the shape the record has.**

23. **The label vocabulary itself is not this record's to close.** Paired-variant construction is **W7-D4's** — the live W5 precedent uses `with_bait` / `without_bait`, which is that era's trap idiom and not a general law. **This record fixes cardinality, distinctness, and the key-set identity; W7-D4 fixes the names.** Reported as a dependency rather than pre-decided.

24. **Capture identity is `(record_id, variant_label)`.** There is no separate `capture_id`, because an identifier beside the key it duplicates can drift from it, and a reference that cannot drift is worth more than one that reads prettily.

### Part H — Capture structure

25. **Each capture is whole and individually attributable:** its class, its authoring citation where the class requires one, its text payload, that text's digest, and its scan status — and **nothing about the other half of the pair.** Attribution is the key it hangs under; relation to the evaluation unit is the record that contains it.

26. **`text` holds the future capture payload and is required.** **This record authors, generates and imports no capture payload and contains no example payload, structural placeholder or otherwise**: where a value must be referred to it is referred to by field name and constraint. **There is no field for a truncated, summarised, cleaned, or normalised form of the text**, because a second rendering of a capture is a second capture that no one declared.

### Part I — Delta and routing

27. **`delta` is `{outcome, differing_surfaces, missing_surfaces}` — the live `delta_finding` spine inherited exactly, with nothing added.** The live records also carry a sibling `basis` on some probes and not others; **this record does not lift it into the W7 delta.** An unowned free-text justification beside a delta is the most natural place for a verdict to appear, and the record already states why an outcome may be unknown through `model_contact`. **`outcome` is the closed three-value set already in use** — **`no-delta-observed`**, **`routed-to-review`**, **`unknown-not-absent`** — none of which means passed, safe, true, or fit for anything.

28. **`differing_surfaces` and `missing_surfaces` are arrays drawn from the four observed surfaces**, and both may be empty. **A delta states what differed. It never states which side was better.** **One cross-field rule binds the outcome to the routing fact — Part T, decision 59.**

29. **Routing is declared, never inferred.** `human_review.routed` is a boolean the record carries; no reader may compute routing from an outcome, and no outcome implies a disposition.

### Part J — Human review as a later governed act

30. **`human_review` is `{routed, disposition, disposition_record}`, a top-level object structurally separate from `captures` and `delta`.** `routed` is required and present at record creation. **`disposition` and `disposition_record` are null until a later human act writes them.**

31. **The machine-writable path is closed by ownership, not by convention.** **The disposition value set belongs to W7-D6**, not to this record. Until W7-D6 lands there is no lawful non-null value, so **any non-null disposition is invalid on its face** — and after W7-D6, a disposition is invalid unless `disposition_record` cites a governed record. **A machine cannot write a valid disposition today, and cannot write one later without a human landing the record it must cite.**

32. **This is what keeps captured text frozen while review stays live.** ADR-0048 decisions 22–25 bind: the capture is terminal in time, and the two nullable review fields are the only positions in the shape that a later act may fill. **Whether a disposition may itself later change is W7-D6's, and is not decided here.**

### Part K — Findings, and the handoff to W7-D2-D

33. **`findings` is an array; empty is lawful and meaningful.** Each finding event carries exactly the five fields **`{finding_id, capture_ref, category, locus, disposition}`** and no sixth. **This record fixes the finding event's field set; it does not fix every inner shape** — `locus`'s internal structure is **W7-D2-D's**, and this record deliberately stops claiming otherwise rather than inventing a line-or-offset union against no real artefact.

34. **There is no field for the matched text, and `locus` may not become one.** `locus` identifies **a position within the named capture** and is bound by two constraints this record fixes and D may not relax: **it may not contain, quote, excerpt, or paraphrase any part of the captured text**, and it must be resolvable against a capture that is present in the same record. **W7-D2-D's rule that a finding must not reproduce what it found is made unbreakable here by never providing anywhere to put it** — the five-field set has no text-bearing member, and `locus`'s inner shape inherits that bar whatever form D gives it.

35. **`capture_ref` is a variant label present in `captures`, **and it is bound to that capture's `scan_status` by Part T, decision 60.**** `category` is a scan-machinery category name, constrained to the names the scan actually emits and cross-checkable against it — **not free text, and not this record's to invent.**

36. **`disposition`'s value set is W7-D2-D's, wholly.** This record fixes that the field exists, that it is required on every finding, and that it may hold no value D has not defined. **It does not enumerate D's vocabulary, and nothing here may be read as pre-deciding it.** A finding is never a verdict, never a winner, and never a conclusion about a capture.

### Part L — The non-authority ceiling

37. **`non_authority` carries the ADR-0046 decision 23 sentence, byte-identical, as the record's last field:**

> **Generated output is evaluation evidence only. It is not truth, advice, diagnosis, therapy, safety evidence, correctness evidence, clinical validity, legal conformance, production readiness, approval, or a decision about any person.**

38. **Inside the record, and nowhere else instead.** Not in documentation alone, not in the manifest alone, not in a validator, not in a surrounding surface. **The record that carries the text carries its own ceiling. Byte fidelity is required** because ADR-0046 decision 23 fixes the sentence; a paraphrased ceiling is a different ceiling.

   **What that does and does not guarantee, stated plainly.** **Every complete governed record carries the ceiling as its final field.** **A partial excerpt can omit it** — no field placement prevents someone quoting three lines out of the middle. **What the placement does guarantee is that an excerpt which omits the ceiling is visibly not the whole record**, and the binding rule follows: **an excerpt that omits the ceiling must never be represented as the complete governed record, or as carrying the record's full governance context.**

39. **Specimen parity.** The ceiling is required identically on records holding authored specimens. ADR-0046 decision 25.

### Part M — Integrity, and the manifest boundary

40. **The record never contains its own content hash.** A record carrying a digest of itself cannot be written — computing it changes the bytes it digests. **The record's content hash lives only in the manifest**, which ADR-0048 decision 17 registers.

41. **`text_digest` is not circular and is not the record hash.** It digests **the `text` value alone**, so the dependency runs `text → text_digest → record bytes → manifest hash` and never returns.

   **The exact bytes hashed, fixed so the digest has one deterministic meaning.** `sha256` over the **UTF-8 encoding of the decoded `text` string value** — that is, the string after JSON unescaping, never the escaped JSON source. **JSON escaping does not participate**, so a re-serialisation that changes escaping changes no digest. **No newline normalisation occurs**: the repository's LF rule governs *files*, and a capture's line endings are part of what was captured, so normalising would digest something other than the capture. **No Unicode normalisation occurs**, for the same reason — a capture is preserved as received, not as tidied. The recorded value is the lowercase hexadecimal digest prefixed `sha256:`, matching the repository's existing hash notation. **What it proves, stated precisely so it is not oversold:** that a capture's payload matches the digest recorded beside it — **internal consistency, not immutability over time.** It is not a substitute for the manifest hash and **it does not discharge ADR-0048's S3**, which remains candidate-mechanical there.

42. **The record/manifest boundary, drawn explicitly.** **In the record:** `record_id`, `run_id`, `authorising_record`, `as_of` — identity and provenance. **In the manifest only:** the per-record path, the per-record content hash, the record inventory, and any run-level totals. **In neither:** a count of records inside a record, or a summary of the run inside a record. **A record that indexes its siblings has become a manifest**, and ADR-0048 decision 21 keeps the manifest an index rather than a summary.

### Part N — Structural absences

43. **Four absences, each a field that does not exist at any level — not a null, not a false, not an empty value.** ADR-0048's three are preserved and one is added by this record's own design.

| Absence | What is barred | Why the hole would be shaped like the thing |
|---|---|---|
| **No winner** | any field, at any level, whose value identifies one capture as selected, preferred, best, chosen, primary, recommended, or superior — under **any** name | `W7-AR` §6 forbids a machine-selected winner; **a nullable winner is a winner waiting for a convenience to fill it** |
| **No capture-level recirculation field** | any capture-level **input-origin, downstream-use, reuse, feed, destination, or recirculation-authority** field | ADR-0046 decision 9: **input** origins belong to `inputs`, and capture is terminal. **An addressable recirculation path that cannot be expressed cannot be taken** — and decision 61 closes the input side of the same path. **What remains is re-authoring, which no field set can catch and T6 keeps review-only.** **This bars reuse, not provenance:** `text_class` is provenance *classification* and `authoring_record` is provenance *accountability*, and **neither makes a capture an input or a reusable source** |
| **No machine-writable review path** | any field permitting a disposition to be valid without a W7-D6 value and a cited governed record | ADR-0046's and ADR-0039's refusal of machine verdicts; **a review-shaped hole a machine can fill is machine authority** |
| **No matched-text field on a finding** | any field holding, quoting, excerpting, or paraphrasing the text a scan objected to | ADR-0007 decision 2: **a report that repeats the problem republishes it** |

44. **The absences are semantic, not lexical.** A future field that performs one of these functions under a different name is barred by this record whether or not its name appears above. **A winner-shaped hole is still winner-shaped.**

   **How that is enforced, split honestly between machine and human.** **Mechanically (T2):** **every one of the twelve object shapes this record fixes** is closed to its exact declared field set, so **no field can be added anywhere C governs** — which catches a renamed winner, a capture origin, or a matched-text holder not by understanding it but by refusing anything unlisted. **By review (T6):** whether a *permitted* field is being used to perform a barred function. **A machine cannot infer semantic function from a name, and this record does not pretend it can.**

### Part O — Vocabularies and their owners

45. **Closed and owned by this record, with every value stated — a cardinality is not a vocabulary:**

| Vocabulary | Values | Source |
|---|---|---|
| `text_class` | `generated_output` · `authored_synthetic_specimen` | ADR-0047 decision 3(b), 3(c) |
| `inputs[].origin` | `authored_synthetic` · `repository_fixture` · `governed_public_record` | ADR-0046 decision 7 |
| `delta.outcome` | `no-delta-observed` · `routed-to-review` · `unknown-not-absent` | inherited verbatim from live use |
| `delta.differing_surfaces[]`, `delta.missing_surfaces[]` | `spoken_output` · `persisted_state` · `routing_propagation` · `behaviour_selection_ranking_framing_omission` | the four observed surfaces, **carried explicitly here and bound to their source** so a validator resolves them without interpretation |
| `scan_status` | `no_findings` · `findings_present` | **C-owned.** The scan reports, per file, whether findings were emitted; these two tokens name exactly that and nothing more. **Neither is a disposition** — dispositions are W7-D2-D's |
| `exclusion_check.result` | `no_listed_item_present` · `listed_item_present` | **C-owned.** The ADR-0046 decision 11 list is a presence test; these two tokens name its only two outcomes, and **neither authorises landing** |

46. **Bounded by this record, enumerated elsewhere:** `findings[].category` — constrained to the scan machinery's own category names and cross-checkable against them, never free text.

47. **Not closed by this record, with the owner named. `contact_class` is not a C-owned closed vocabulary:** this record fixes **one currently lawful token, `none`**, and closes nothing. **W7-D3 owns every contact-bearing member**, and **`none` is not an implicit preference for the no-contact option** — it is the token a record needs when nothing was contacted, which is the only state that exists before W7-D3 lands. Also not closed here: `contact_class` beyond `none` → **W7-D3** · `human_review.disposition` → **W7-D6** · `findings[].disposition` → **W7-D2-D** · `pairing.variant_labels` → **W7-D4**. **No `other`, no `custom`, no free-text state, and no implicit extension point exists in any vocabulary this record closes.** Where a set is not this record's to close, the field's **boundary** is fixed and its **members** are left to their owner, reported as a dependency rather than pre-decided.

### Part P — Nullability

48. **Four nullable positions, re-derived against the corrected field design rather than assumed.** The combined design packet reasoned to three; this record's anti-laundering design adds `authoring_record`. **The model-contact rule was then tightened at decision 17, and the count was recomputed rather than carried: it remains four, because that correction changed *when* `authorising_record` is null but not *whether* it can be.** Every position names a lifecycle reason:

| Position | Null when | Lifecycle reason |
|---|---|---|
| `model_contact.authorising_record` | `occurred` is false | there was no contact, so there is nothing to have authorised |
| `human_review.disposition` | before a later human act | the value set is W7-D6's and does not yet exist |
| `human_review.disposition_record` | before a later human act | the citation cannot precede the record it cites |
| `captures.<label>.authoring_record` | `text_class` is `generated_output` | a model's output has no human author to name |

49. **Nullability is exceptional and never a convenience.** **No field is nullable because an implementer might not have the value handy**; each of the four is null only in a state the governance itself creates. **Every other field, at every level, is required.**

### Part Q — Proof obligations

50. **Nine obligations are specified. Three are demonstrated against this record's own tables, five are debts, one is review-only — and the mechanical/semantic line is drawn where a machine can actually stand.** T2 checks that the field set is exactly this record's; **whether a permitted field is abused is T6's, and is review-only.** **None is implemented here** — all W7-D2 proofs land in **W7-D2-E**, after their subjects, per `W7-D2-RSB`.

| # | Obligation | Fails when | Decidability and timing |
|---|---|---|---|
| **T1** | **Schema-statement integrity.** The field tables, the canonical-order claim, the vocabulary table and the nullability table agree with one another and with the stated counts. | A count diverges from its table; an order claim contradicts the table; a vocabulary is enumerated twice differently. | **Mechanical — demonstrated against this candidate.** Implementable in W7-D2-E |
| **T2** | **Canonical field-set integrity.** **Every object shape fixed by this record equals its declared canonical field set** — the wrapper, the top-level record, `synthetic_marker`, `model_contact`, the `inputs` item, `pairing`, `delta`, `exclusion_check`, `no_recirculation`, `human_review`, the capture object, and the finding-event object: **twelve fixed shapes.** No fixed shape accepts an added, missing or renamed field, and **canonical order is preserved wherever this record governs order.** **`locus`'s inner shape is excluded, because W7-D2-D owns it and it does not yet exist.** | Any added, missing, or renamed field **in any of the twelve shapes** — including a known prohibited addition such as a winner-, capture-origin-, or matched-text-shaped key, and including a nested rename such as `synthetic_marker.notice` to `note`. | **Mechanical — demonstrated against this candidate.** Implementable in W7-D2-E. **This is a closed-set check over field membership and order, not a semantic judgement, and it closes no later-owned vocabulary** |
| **T3** | **Acyclic integrity graph.** No field's value is defined in terms of a digest that includes it. | A record-level self-hash, or a digest whose input contains the digest. | **Mechanical — demonstrated against this candidate.** Implementable in W7-D2-E |
| **T4** | **Pair bijection.** In every record, `captures`' key set equals `pairing.variant_labels` exactly. | A declared label with no capture, or a capture under an undeclared label. | Mechanical, **debt** — no record exists |
| **T5** | **Ceiling verbatim and last.** The decision 37 sentence appears byte-identically as the final field of every record. | Absent, reworded, abbreviated, or followed by another field. | Mechanical, **debt** — no record exists |
| **T6** | **Semantic-absence and laundering review.** Whether an allowed field is being *used* to perform a winner, reuse, verdict, or recirculation function under a lawful name; **whether captured text was copied, paraphrased, summarised or re-authored into a new `authored_synthetic` input — the limb of non-recirculation T9 cannot reach**; whether the design prevents laundering in practice; whether a mixed-class record stayed honest. | — | **Review-only, in full.** **A machine cannot infer semantic function from a name**, so this duty cannot be mechanised and is not claimed to be. Joins **P2**, **Q3**, **R7** and **S4** |
| **T7** | **Delta-routing coherence.** Decision 59 holds in every record. | `delta.outcome` is `routed-to-review` while `human_review.routed` is false. | Mechanical, **debt** — no record exists |
| **T8** | **Capture scan-status coherence.** Decision 60 holds for every capture. | A capture marked `no_findings` that a finding references, or one marked `findings_present` that none references. | Mechanical, **debt** — no record exists |
| **T9** | **Input-source non-recirculation.** No `inputs[].citation` or `inputs[].reference` resolves into the generated-evaluation class. | A citation or reference resolving to a `GER-####` identifier, to a path under `governance/generated-evaluation/`, or to a capture or finding address inside that class. | Mechanical, **debt** — no record exists. **The re-authoring limb is not mechanical and stays in T6** |

51. **Self-reference, checked before claiming.** T1, T2 and T3 all read **the field, vocabulary and nullability tables**, never the prose. This record names the barred functions in Part N's prose in order to forbid them; **a prohibition in prose is not a table row**, so T2 — a closed-set comparison over table rows — does not fire on this record's own bans. **All three were run against this candidate: none self-failed, no self-exclusion is needed, and none is proposed.** Should implementation prove otherwise, **the remedy is a disclosed self-exclusion in the owning record before landing** — one path, asserted to resolve to the module — as ADR-0046 decision 28 and ADR-0047 decision 25 record.

### Part R — Inheritance and boundaries

52. **What this record hands W7-D2-D:** a finding-event shape with a required disposition slot whose vocabulary is D's alone, a `capture_ref` that resolves inside the record, a `category` bounded by the live scan, and **no field anywhere to put the matched text in**.

53. **What this record hands W7-D2-E:** T1, T2 and T3 demonstrated; **T4, T5, T7, T8 and T9 as debts**; T6 as review-only, **now carrying the re-authoring limb of non-recirculation that T9 cannot reach**. **ADR-0048's S3 is not discharged by `text_digest`** and remains exactly as B left it.

54. **What this record hands W7-D4 and W7-D6:** a field boundary each, with the members left to them — `pairing.variant_labels` and `human_review.disposition` respectively.

55. **What this record does not touch.** ADR-0046's fence, ADR-0047's crossing, ADR-0048's ground, in any provision. **The model boundary and its four options.** The pending ledger, the carried W6 findings, the applicability records, the Tier 3 rows, the T12 obligation, the carried questions. E10, Z4, E12/Z5, the hosted class, the local class. **W7-D3 through W7-D7 remain unopened, and W8 is named only as unopened.**

### Part S — The identifier namespace this record mints

56. **This record mints one identifier namespace: `GER-####`, for generated-evaluation records.** Stating it plainly matters, because the alternative — creating a namespace while a constitutional check claims none was created — is exactly the kind of quiet contradiction this deliverable exists to refuse.

57. **What the namespace is and is not.** **Numeric allocation order carries identity only.** A higher `GER` number is **not more authoritative, important, severe, complete, correct, reviewed, or successful** than a lower one; allocation order encodes no outcome and no quality. **The identifier mints no authority** — it is record identity and nothing else, and a record existing under a well-formed identifier is not thereby valid, landed, reviewed, or true. **No identifier is allocated by this record**; the grammar is defined and the namespace stands empty, on the **ADR-0042 `CAT-####` precedent**, whose registry entry reads *grammar defined only — no identifier allocated*. **The landing registry entry declares the namespace in `id_namespaces`** in the same form.

### Part T — Fixed field values and cross-field coherence

58. **`synthetic_marker.notice` is byte-fixed at this value, authored here because no live source fixes one suitable for this class:**

> **SYNTHETIC generated-evaluation record authored for governance testing. Corresponds to no real person. Captured text is synthetic by construction and is not about any real person.**

   **The alternative was assessed and rejected on its bytes.** W2-D4 §4's marker notice — carried identically by `tests/evaluation_harness.py`'s `REQUIRED_NOTICE` and by every live fixture — reads *"SYNTHETIC fixture authored for governance testing. Corresponds to no real person. Values are grammar placeholders, not medical content."* **That notice is fixture-specific in two places:** a generated-evaluation record is **not a fixture**, and its captures are **not grammar placeholders**. Binding this class to it would make every record assert two things that are false of it. **Paraphrasing it was not an option either**, since a paraphrased byte-fixed value is not byte-fixed.

   **Authoring it here follows the ADR-0045 precedent**, where the schema-law record fixed a single sentence byte-identical in every entry. **The notice states synthetic provenance and nothing else** — authority is the ceiling's job at decision 37, and the two do not overlap.

59. **Delta-routing coherence, one-way.** **`delta.outcome == "routed-to-review"` requires `human_review.routed == true`**, because the outcome literally says routing occurred and a record may not assert an event it then denies. **The reverse does not follow:** `human_review.routed == true` is lawful under any outcome, since a record may be routed for another governed reason — including a finding. **And routing implies nothing about disposition:** no outcome, and no routing flag, permits a disposition to be inferred, written, or presumed.

60. **Capture scan-status coherence.** For each variant label, **`scan_status == "no_findings"` if and only if no `findings[].capture_ref` references that capture**, and **`scan_status == "findings_present"` if and only if at least one does.** This forecloses the one contradiction the field set would otherwise permit: a record saying *this capture had no findings* while carrying a finding against it. **The rule binds the two facts to each other and decides nothing about what happens next** — the disposition mechanism remains W7-D2-D's entirely.

61. **Input-source non-recirculation: the input door is not a reuse socket.** Part N closes the capture side by giving a capture no field in which to declare an origin or a downstream use. **This closes the other side.** **A future generated-evaluation record, any `GER-####` identifier, anything under `governance/generated-evaluation/`, and any capture or capture-derived representation from that class may not resolve as scenario material through `inputs[].citation` or `inputs[].reference`.**

   **In particular:** generated output may not become a later input · an authored-specimen capture may not become a later input · **a capture is not made reusable merely by citing the record that contains it** · and **copying, paraphrasing, summarising or re-authoring captured text into a new `authored_synthetic` input cleanses nothing** — provenance does not launder in either direction (ADR-0047 decision 4), and a new name is not a new origin.

   **One distinction is preserved and is not narrowed by this rule.** A later governance, review or closure record **citing a `GER-####` as evidence that an evaluation occurred** is a different act from **the `inputs` field of another evaluation unit using that record or its captures as scenario material.** The former may be lawful under its own later authority; **the latter is barred here.** The bar is on *feeding this class back into itself*, not on *referring to it*.

   **This narrows none of ADR-0046's three lawful input-origin categories in general.** They remain exactly as decision 15 states them. **What is barred is recirculating this artefact class through those categories** — an input is still lawfully authored-synthetic, fixture, or governed public record, and simply may not be this class wearing one of those labels.

   **What this rule reaches, and what it does not.** **Mechanically (T9):** any citation or reference that *resolves* into the class — an identifier, a path, a capture or finding address. **By review (T6):** whether captured prose was re-authored into something that no longer points anywhere. **No field law can close the second, and this record does not claim to.**

## Consequences

**Made easier:** W7-D2-D designs a disposition mechanism against a finding shape that already refuses to hold the offending text. W7-D2-E writes proofs against tables rather than intentions. And a future reader can answer *where did this text come from* and *what may it not be taken to mean* without leaving the file.

**Made harder, deliberately:** a record cannot be landed half-paired, cannot name a better answer, cannot re-use its own captures, cannot carry a machine's disposition, and cannot quote what a scan objected to. Every one of those is a thing someone will eventually want to do.

**Accepted cost.** **Four nullable positions**, re-derived against the corrected field design rather than carried: the count is unchanged from the previous draft, but it is now unchanged *because it was recomputed*, not because it was preserved. `authoring_record` is what makes a specimen claim accountable rather than merely asserted. **Five proof obligations are debts rather than two** — T4 and T5 on record shape, **T7 and T8 on Part T's coherence rules**, and **T9 on input-source non-recirculation**, which together are exactly the contradictions and the reuse path the field set would otherwise have permitted. **One residue stays with a human forever:** T9 closes every *addressable* route back in, and **no check can prove that captured prose was not copied, paraphrased or re-authored into a newly named input** — T6 holds that, and this record says so rather than implying the door is fully bolted. **Four vocabularies stay open**, each waiting on an owner — and the gates they impose are conditional, not uniform. **Every record needs W7-D4's paired-variant labels before it can be materialised at all.** **A record containing a finding needs W7-D2-D's disposition vocabulary**; a record with an empty `findings` array does not. **A record in which contact actually occurred needs W7-D3's contact-class members and authorisation posture**; a **no-contact specimen record needs no contact-bearing D3 value.** And **an initial record is valid with `human_review.disposition` and `disposition_record` null** — **W7-D6 is required only before a non-null human disposition is written.** That ordering is load-bearing: **W7-D6 reviews W7-D5's records, so W7-D5's records cannot require W7-D6 to exist before they are valid.** **And a field-level fact is not a phase-level shortcut:** that a no-contact specimen record needs no contact-bearing W7-D3 token **does not skip the phase sequence** — **W7-D3 remains the governed boundary decision before any W7-D4 or W7-D5 work**, whatever a given record's contact posture turns out to be. And **`text_digest` proves consistency, not immutability**; this record says so rather than letting the field imply more than it does.

## Constitutional check

- **Law 1** — nothing contacts anyone, nothing runs in the background, no notification surface exists or is implied.
- **Law 3** — nothing self-promotes: no field ranks, selects, or prefers; a delta states difference and never merit.
- **Law 6** — the clinical line holds: the ceiling sits inside every record as its last field, byte-identical.
- **Law 8** — inference stays closed: **no capture may be addressed as an input**, on either side — a capture cannot declare an origin (Part N) and an input cannot resolve to this class (decision 61) — so **no addressable accumulation path exists.** Re-authoring captured prose into a newly named input is the residue no field set can catch, and it is held by review under T6.
- **Law 9** — the Meditation wall is untouched; no material crosses it and no field bridges anything.
- **Law 10** — consent is untouched: evaluation has no user, and no field here functions as a grant.
- **Law 11** — no person is gated; nothing here conditions anyone's access to anything.
- **Law 13** — every field is declared, ordered, and checkable, and the review slot keeps a human act a human act.
- **W0 §10** — the agent-to-agent rule is carried whole: text arriving from a model is unverified input everywhere, including inside a record that preserves it faithfully.
- **W0 Non-Goal 7** — no `complian-`, safety, or `certif-` claim arises from this record or anything it governs.
- **No new authority, with one named exception that is identity and not authority.** No edge, zone, class, grant type, or authority state is minted; **no fence is crossed and no allowlist is amended.** **This record does mint one identifier namespace, `GER-####`** (Part S) — meaning-free record identity that confers nothing, on the ADR-0042 `CAT-####` precedent. **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide, or design: **the creation of `governance/generated-evaluation/`, a schema file, a manifest, a proof module, or any record of the class** · any run, probe, fixture, or harness · **any generated-output, authored-specimen, capture-payload or example-payload text, whether generated, imported, or authored** · the finding-disposition vocabulary · the human-review disposition vocabulary · the variant-label vocabulary · the model boundary or any narrowing of its four options · any provider, adapter, client, credential, key, token, secret, private configuration, or model binary · retention, archival, or withdrawal-from-view · whether a disposition may later change · any dependency · W7-D2-D or W7-D2-E · W7-D3 through W7-D7 · W8 · private adoption in any form · the repair of the carried W6 findings · the optional audit proof module · any stub conversion · any applicability resolution · any Tier 3 conversion · **E10, Z4, E12/Z5, the hosted class, or the local class** · or **medical, therapeutic, diagnostic, or crisis behaviour of any kind.** It amends no record, and it contains no real health data and no clinical examples.

**The six standing statements bind this record in full:** W7-D2 creates a shape, not content · authorises no model contact · authorises no specimen · authorises no generated-output import · authorises no harness · **narrows none of W7-D3's four options.**

## Public-safety considerations

Generic and structural wording throughout — field, capture, variant, delta, locus, digest, manifest. **No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no machine-identifying detail, no private lineage, and **no generated-output, authored-specimen, capture-payload or example-payload text**.** Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. **Decision 34 is itself a public-safety decision** and the most easily missed one in the design: the finding shape has nowhere to put what it found. **Nothing here is, or may be presented as, a safety, health, clinical, legal, or regulatory claim of any kind.**

## Dependencies

`ADR-0048` (direct and required — fixed inputs, not reopened) · `W7-D2-RSB` · `ADR-0046` · `ADR-0047` · `W7-AR` · `W7-D1-FCB` · `ADR-0034` (B6) · `ADR-0033` (B1) · `W2-D4` (rules, §3, §4) · `ADR-0007` · `ADR-0045` (the schema-law precedent this record follows) · `ADR-0003` · `W6-CR` (carried context).

## Open boundaries and later ownership

- **`findings[].disposition` values, and the disposition mechanism** — W7-D2-D.
- **All nine proof obligations** — W7-D2-E; **T1, T2, T3 demonstrated here and implemented there**; **T4, T5, T7, T8 and T9 debts** against a class that does not exist; **T6 review-only in full**.
- **`pairing.variant_labels` members** — W7-D4.
- **`contact_class` members beyond `none`** — W7-D3, wholly, through a Tier F crossing record.
- **`human_review.disposition` members, and whether a disposition may later change** — W7-D6.
- **Retention, archival, and withdrawal-from-view** — W7-D5, per ADR-0034 B6 decision 35 as ADR-0048 assigned it.
- **T6, and ADR-0048's S4** — standing human-review duties alongside P2, Q3 and R7, owned by no machinery and never closed.

---

*Four vocabularies in this blueprint are deliberately unfinished, and each stops at a different owner's door rather than at one shared deadline. W7-D4 supplies the paired-variant labels without which nothing can be materialised at all. W7-D2-D is needed only when a finding exists. W7-D3 supplies contact-bearing values when contact actually occurs — and remains the governed boundary decision before any later execution work, whatever a given record's contact posture. W7-D6 is needed only before a non-null human disposition is written, which is why a W7-D5 record is valid with those two fields still null: the reviewer's law cannot be a precondition of the records it reviews. A schema that could be filled in completely today would be a schema that had quietly decided things belonging to someone else. This one is drawn to the edge of its own authority and stops there, with every gap labelled and addressed.*
