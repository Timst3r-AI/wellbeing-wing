# 0048 — Record-Shape Doctrine for Generated-Output / Authored-Specimen Evaluation Records (W7-D2-B)

**Status:** Accepted by human reviewer, 2026-08-19. Not a build instruction. Authorises no implementation by itself.
**Date:** August 2026 · **Phase:** W7 — First-Contact Governance and Synthetic Model Evaluation · **Deliverable:** **W7-D2** (landing **W7-D2-B**, the second of five)
**Position:** the second W7-D2 landing. It decides **where a future generated-output or authored-specimen evaluation record will live, what it is made of, how coarse it is, how its integrity is proven, and that it may never be rewritten** — and it creates none of it. No directory, no schema, no field, no manifest, no record.
**Constitutional references:** W0 Laws 1, 3, 6, 8, 9, 10, 11, 13; W0 §10; W0 Non-Goal 7. **No law is amended.**
**North star carried:** **generated text may enter the public Wing only as synthetic, governed evaluation evidence** — observed, preserved, compared, routed, and reviewed, and **never authority, advice, truth, safety evidence, approval, or a decision about any person.**
**Resolves:** none.

---

**Before anything can hold a sentence nobody here wrote, someone has to say where such a thing would stand, what it would be made of, and what may never be done to it afterwards. This record picks that ground. It chooses a home whose path warns you what it may contain, a format the repository already trusts, a grain coarse enough that a missing half of a pair is a broken record rather than a tidy one, an integrity story that admits generated text cannot be reproduced, and a rule that captured text is never edited once it lands. Nothing is built today. The plot is surveyed and the deed recorded — so that when the field law is written, not one of these decisions has to be made under load.**

## Decision question

**Is the W7 generated-output / authored-specimen evaluation record an extension of the existing evaluation-record class or a new one; where will it live, in what format, at what granularity, under what integrity posture, and under what rule against later edits — decided now, as fixed input to W7-D2-C and W7-D2-D, without creating the directory, the schema, a manifest, or a single record?**

## Controlling law

- **The W7-D2-A opening brief (`W7-D2-RSB`), whole** — this record's assigned scope; the six standing statements; the five-component sequence with its merge discipline; the statement that a complete W7-D2 discharges exactly one of ADR-0047's seven preconditions and leaves three outstanding.
- **ADR-0046, whole and consumed rather than re-decided** — synthetic-only by construction and the constructional test (3–4); capture is publication (5); the three lawful origins with a fourth unlawful (7–8, 10); **no-recirculation, capture terminal (9)**; the closed, growable-only exclusion list (11–12); no exemption for machine production and finding-is-an-event (13); the boundary invariant and non-naming law (14–18); provenance declarability as the admission condition (19–22); the non-authority ceiling with specimen parity (23–26).
- **ADR-0047, whole and consumed rather than re-decided** — the three provenance definitions (3); a specimen is not model contact and provenance does not launder in either direction (4); **the governed handling binds on specimens and generated output identically (6–8)**; the seven conjunctive preconditions (9–11); one-way, non-retroactive, stop-and-report (12–15); no-recirculation and finding-is-an-event applied to contact (16–17); the fifteen-link chain (18–20).
- **ADR-0034 B6 decisions 32–35 and decision 37** — the evaluation artefact class and its permanent never-become rules; that such records **exist to be examined**; that they are **scanned exactly as documents are, synthetic-only, with no exemption for machine production**; that home, retention and lifecycle are governed at the landing that owns them; and that no evaluation result is presented as a safety, health, or `certif-` claim in any surface or derived artefact.
- **`W7-AR`** — §3 north star and honest boundary; **§6 the nine binding properties**; **§7's reservation of the model boundary to W7-D3**; §8.1 gate discipline; §9 non-goals; §10 tripwires.
- **`W7-D1-FCB`, whole** · **W2-D4** rules 1–6 and **§3 format conventions** · **ADR-0007** decisions 1, 2, 4, 6 · **the W6 closure record** as carried context only.
- **Live repository precedent, read as artefacts rather than doctrine:** the W5-D4 run manifest `W5-D4-RUN-01.json` and its twenty-three per-fixture records under `governance/evaluation/`, none of them individually registered; the registry's conventions for homes and hashes; and the top-level directory fence in `tests/test_repo_state.py`.

## Decisions

### Part A — The door

1. **This record decides shape and home and creates nothing.** After its landing the repository contains exactly one new governed artefact: this record. **No `governance/generated-evaluation/` directory exists. No schema, no field, no manifest, no record, no proof module, no run, no probe.** Every statement below about "a record of the class" describes a future thing that only later authorised landings may bring into existence.

2. **B does not discharge W7-D2 by itself.** W7-D2-C, W7-D2-D and W7-D2-E remain unlanded, each behind its own authorisation and its own ceremony. **W7-D3 remains unbegun and the model boundary unchosen.**

### Part B — Class relationship

3. **The W7 record is an extension of the existing evaluation-record class, not a parallel invention.** ADR-0034 B6 decision 32 created the evaluation-record class at doctrine level; W5-D4 materialised it. **W7 extends that class to carry text. It does not fork it.**

4. **What is inherited from the W5 content-free records, because it already works.** The live artefacts carry `record_id`, `run_id`, `authorising_record`, `as_of`, `instrument`, `model_contact`, a `probes` array whose `delta_finding` names **differing surfaces and no winner**, a per-probe `routed_to_human_review` flag, and `non_authority` as the closing field. **Several of `W7-AR` §6's nine properties are therefore already structural in this class** — the delta has never had a winner field, and routing has always been declared rather than assumed. **W7 inherits that spine, its idiom, and its habits of naming.**

5. **What changes, and it is exactly one thing: these records may carry text.** Everything that follows in this record — a separate home, a manifest-based integrity posture, an immutability rule — exists because of that single difference. **A content-free record and a text-bearing record are the same class with different risk**, and the shape decisions below are the places where that risk is handled rather than hoped about.

6. **Inheritance is not permission to blur.** ADR-0034 B6 decision 33's never-become rules bind the extended class in full and unchanged: never processing input · never a profiling source · never cross-room analytics · **never a behavioural dataset about a person** · never an authority source · **never clinical evidence** · **never safety `certif-`ation.**

### Part C — The home

7. **The home of the future class is `governance/generated-evaluation/`** — a **sibling** of `governance/evaluation/`, not a subdirectory of it, and never shared with it.

8. **Why a sibling and not the same tree, stated as the decision it is.** The W5 records are **content-free by construction**; the W7 records **may contain text a model produced**. Those are different risk classes wearing the same class name. **A reader, a scan rule, and a future contributor should be able to tell which tree may contain such text from the path alone, without opening a file** — and reusing `governance/evaluation/` would make the most sensitive artefact class in the repository indistinguishable by location from one of the least. Location is the cheapest signal a repository has, and this is the case that most deserves it.

9. **Why `governance/` and not a new top-level directory.** `governance/` is the established home for governed registers and the existing evaluation records, and the class is governance-visible by nature. **A new top-level entry would be a named fence crossing** requiring its own record-backed amendment to the top-level allowlist; a subdirectory of an already-authorised directory crosses no fence and moves nothing. **The home is chosen to cost no fence movement, and that is a feature of the choice rather than an accident of it.**

10. **The home is reserved, not created.** Naming it here creates no directory and no file. **An empty or absent home authorises nothing** — Part H.

### Part D — The format

11. **The format class is JSON**, under the repository's standing data conventions carried from W2-D4 §3: **UTF-8, no BOM, LF line endings, lower_snake_case keys, indented for line-oriented diffs.**

12. **Why JSON:** deterministic parse with no prose ambiguity; line-oriented diffs at record granularity so a review can see exactly what changed; direct consumption by a future validator with no extraction step; and consistency with every governed data artefact this repository already keeps — the registry, the catalogue, the fixtures, and the existing evaluation records. **A text-bearing record is the last place to introduce a second parsing story.**

13. **This record fixes the material, not the blueprint** — the ADR-0044 formula, deliberately reused. **Future W7 generated-evaluation key names, key order, nesting, nullability, closed value sets, and every field are W7-D2-C's, wholly.** This record may name existing W5 evaluation-record keys as live precedent for the inherited spine, but it fixes no future W7 schema key. Nothing in this record may be read as fixing a generated-evaluation field.

### Part E — Granularity

14. **One record per evaluation unit: one probe applied across a paired-variant pair, with both captures whole in the same record.** One unit, one file, one hash, one diff.

15. **Why not one record per capture.** Splitting a pair across two files would make **an omitted variant a missing file rather than a broken record** — and a missing file is the kind of absence that looks like tidiness. `W7-AR` §6 requires both variants captured whole and no omitted variant; **keeping the pair in one artefact makes an omission a defect in something that exists**, which is the only kind of omission a proof can catch.

16. **The consequence for W7-D2-C, stated so it is not discovered later:** an omitted variant must be expressible as a **schema violation**, never as an editorial choice, an empty field, or a permitted shorter record. **This record does not write that rule; it makes it writable.**

### Part F — Integrity posture

17. **A registered manifest per run, carrying a content hash for every record it lists. One registry entry per run, never one per record.** The records are integrity-tracked through the manifest; the manifest is integrity-tracked by the registry, exactly as every governed document is.

18. **Why not one registry entry per record.** The registry is an index of authority, not a file inventory. **A class that grows with every probe would grow the registry with every probe**, and an index that grows without bound stops being readable — which is the property that makes it useful. The manifest absorbs that growth and keeps one governed hash at the boundary.

19. **Why ADR-0034 B6's deliberate-exclusion precedent does not transfer, which is the load-bearing finding of this record.** The W5 evaluation records are unregistered because they are an append-only observation class **whose integrity is proven by deterministic reproduction** — run the instrument again, get the same bytes, and the absence of a hash costs nothing. **That argument is simply unavailable here.** Generated text **is not reproducible**: the same probe to the same model may return different text, and nothing in the repository can re-derive it. An authored synthetic specimen is **written, not derived**, so re-running nothing reproduces it either. **When reproduction proves nothing, the hash is the only thing left that proves anything** — so the class that most needs integrity tracking is precisely the one that cannot inherit the exclusion.

20. **Stated plainly so no later record repeats the mistake:** *unregistered-with-reproduction* was never a general posture for evaluation records. It was a posture for **reproducible** ones. **W7's records are not reproducible, and the posture does not follow the class name across.**

21. **What the manifest is for, and what it is not.** It is an integrity index and a run inventory. **It is not a summary, not a conclusion, not a scoreboard, and not a place where anything is ranked.** No manifest field may carry a verdict about a run, and `W7-AR` §6's *no generated text promoted into a conclusion* binds the manifest exactly as it binds a record.

### Part G — Immutability

22. **Captured text, once landed in a record, is never edited.** Not to fix a typo, not to normalise whitespace, not to shorten, not to tidy. **ADR-0046 decision 9 makes capture terminal in flow; this makes it terminal in time.**

23. **Correction happens by erratum or supersession under the standing ceremony**, with the original bytes preserved and the correction visible as a correction. A record that was wrong stays legible as a record that was wrong.

24. **Why, and it is not fastidiousness.** ADR-0047 decision 12 holds that first contact cannot be un-performed. **A record whose captured text could be edited would let the artefact drift away from the act it records** — and the whole value of the class is that it is an honest account of what was produced, including when what was produced was bad. **An editable capture is a capture you cannot trust, and an untrustworthy capture is worse than none**, because it looks like evidence.

25. **The one thing this does not freeze.** Fields recording **human review** may be written after landing, because a disposition is by construction a later human act. **This is not an exception to immutability: the captured text is frozen; the human's response to it is a subsequent governed event.** How that is expressed is W7-D2-C's, and whether a disposition may ever change is W7-D6's.

### Part H — Gate posture

26. **This shape is not permission, and nothing this record decides changes any gate.** A named home, a landed format decision, a defined schema, a green validator, a manifest, and an empty directory **authorise no model contact, no specimen, no generated-output import, and no harness.** **A container is not an invitation.**

27. **The six standing statements bind this record in full:** W7-D2 creates a shape, not content · authorises no model contact · authorises no specimen · authorises no generated-output import · authorises no harness · **narrows none of W7-D3's four options.**

28. **The preconditions are untouched.** A complete W7-D2 would discharge ADR-0047 decision 9's precondition 6 alone. **This record discharges nothing** — it is one of the five landings that together would. Preconditions 2, 3 and 7 stand outstanding, **no first-contact gate is named anywhere, and no model may be contacted after this record lands.**

29. **W7-D3's option space is untouched, deliberately and structurally.** Nothing here prefers, ranks, forecloses or pre-positions a repository-managed local dependency, an adapter to an externally running local model, a manual governed import, or no public model contact with authored synthetic specimens. **The home, format, granularity, integrity and immutability decisions are identical under all four** — which is the test this record applied to itself before proposing any of them.

### Part I — Proof obligations

30. **Four obligations are specified. One is demonstrated, one is a debt, one is candidate-mechanical with feasibility not yet demonstrated, and one is review-only.** Following ADR-0046 decision 27's discipline: **nothing is called mechanical here that has not been run**, and the decidability column is a claim this record is accountable for.

| # | Obligation | Fails when | Decidability and timing |
|---|---|---|---|
| **S1** | **Reserved-home vacancy.** No file exists under the reserved home until a landing authorised to create one has occurred. | Any file appears there before its authorising landing. | **Mechanical — demonstrated against current repository bytes.** Implementable in the **W7-D2-E** proof landing, per the W7-D2-A sequence |
| **S2** | **Manifest completeness.** Every record file in the home is listed by its run manifest with a content hash, and every hash matches. | An unlisted file, a listed file that is absent, a missing hash, or a hash that does not match. | Mechanical, **debt** — no manifest and no record exists |
| **S3** | **Capture immutability.** No landed record's captured text changes after its first landing. | A commit alters captured bytes in an existing record. | **Candidate-mechanical, feasibility not yet demonstrated.** A history-based check is plausible; **it is not called mechanical until it has been run.** W7-D2-E decides, and may return it as review-only |
| **S4** | **Whether the home genuinely signals its risk class**, and whether a manifest has stayed an index rather than becoming a summary. | — | **Review-only, in full.** Joins **P2**, **Q3** and **R7** as a standing human-review duty |

31. **Timing, stated so it cannot conflict with the sequence.** **No obligation in this record is implemented at this record's landing.** All proofs for W7-D2 land in **W7-D2-E**, after their subjects, as the W7-D2-A brief fixes. **S1 is demonstrated now and implemented then** — and it remains non-vacuous at that point, because C and D will have landed while the home must still be empty until a deliverable authorised to create records exists.

32. **Self-reference, checked before claiming.** S1's future module names the reserved home as a literal, but **S1 inspects the filesystem for files under that path and never inspects source text**, so a path string in a test file is not a file in the home. **Probed against current bytes: no self-failure, no exclusion needed, and none is proposed.** Should implementation prove otherwise, **the remedy is a disclosed self-exclusion in the owning record before landing** — one path, asserted to resolve to the module — as ADR-0046 decision 28 and ADR-0047 decision 25 record. **A scope boundary found after a green run is disclosed, never absorbed.**

### Part J — Alternatives, assessed

33. **Reusing `governance/evaluation/` (rejected).** One home for both classes. Rejected under decision 8: it would erase the only signal available at zero cost — the path — between a content-free record and one that may hold model-produced text.

34. **A new top-level directory (rejected).** Clearer still, at the price of a named fence crossing and an amendment to the top-level allowlist. Rejected as disproportionate: **a sibling inside an authorised directory buys the same legibility and moves no fence.**

35. **One registry entry per record (rejected).** Maximum integrity granularity. Rejected under decision 18: it converts the index of authority into a file inventory that grows without bound, and an unreadable index protects nothing.

36. **Inheriting the unregistered-with-reproduction posture (rejected, and the rejection is the record's centre).** Rejected under decisions 19–20: reproduction proves nothing about text that cannot be reproduced. **Adopting it would have looked like consistency and been the opposite.**

37. **Permitting minor edits to captured text — whitespace, obvious typos (rejected).** Rejected under decision 24: any edit permission is a judgement call at exactly the moment judgement is worst, and the value of the class is that it is an honest account including of bad output.

38. **Deciding retention and lifecycle here (deferred, not adopted).** ADR-0034 B6 decision 35 assigns home, retention and lifecycle to the landing that owns them. **Home is owned here; retention, archival and any withdrawal-from-view question are assigned to W7-D5**, the first deliverable with real records to reason about. **Stating the assignment is deliberate: silence would read as a decision, and it is not one.**

### Part K — Inheritance and boundaries

39. **What this record hands W7-D2-C:** a home, a format class with its conventions, a granularity that makes an omitted variant expressible as a violation, an integrity posture that requires a per-record hash the schema must accommodate, and an immutability rule that separates frozen captured text from later human-review fields. **Every key name, every field, and every value set remain C's.**

40. **What this record hands W7-D2-D:** a class whose records are scanned exactly as documents are with no exemption for machine production, and a home whose path makes the class identifiable to a scan rule.

41. **What this record hands W7-D2-E:** S1 demonstrated, S2 as a debt, **S3 as a candidate whose feasibility must be demonstrated before it is called mechanical**, and S4 as review-only.

42. **What this record does not touch.** ADR-0046's fence and ADR-0047's crossing, in any provision. The four model-boundary options. The pending ledger, the carried W6 findings, the applicability records, the Tier 3 rows, the T12 obligation, and the carried questions. E10, Z4, E12/Z5, the hosted class, and the local class. **W7-D3 through W7-D7 remain unopened, and W8 is named only as unopened.**

## Consequences

**Made easier:** W7-D2-C designs a schema against a settled home, format, grain and integrity story, in one pass rather than three. A reader meeting the repository for the first time can tell from a path which tree may hold model-produced text. And the manifest gives the class a single governed boundary that a future review surface can read without enumerating files.

**Made harder, deliberately:** every run costs a manifest and a registry entry, so there is no lightweight way to produce records quietly. Captured text can never be tidied, so a record with an ugly capture stays ugly. And a pair must be complete in one artefact, so a half-finished evaluation cannot be landed as a smaller whole one.

**Accepted cost.** **One obligation may turn out not to be mechanical** — S3's history-based immutability check is plausible and undemonstrated, and this record does not call it mechanical on the strength of plausibility. **One obligation is a debt** against a class that does not exist. **One is review-only forever**, joining the three that already are: whether a home still signals what it was chosen to signal is a judgement no check will ever make.

## Constitutional check

- **Law 1** — nothing contacts anyone, nothing runs in the background, no notification surface exists or is implied.
- **Law 3** — nothing self-promotes: a home mints no capability, a manifest confers no authority, and a hash proves bytes and nothing about the world.
- **Law 6** — the clinical line holds: no record of this class is a diagnosis or a clinical claim, and ADR-0046 decision 23's ceiling will sit inside every one of them.
- **Law 8** — inference stays closed: ADR-0034 B6 decision 33's never-become rules bind the extended class unchanged, and no-recirculation forecloses the accumulation path.
- **Law 9** — the Meditation wall is untouched; no material crosses it and no artefact bridges anything.
- **Law 10** — consent is untouched: evaluation has no user, no real grant exists in it, and no synthetic shape functions as one.
- **Law 11** — no person is gated; nothing here conditions anyone's access to anything.
- **Law 13** — every future record is a governed, auditable artefact by construction, and immutability keeps the audit trail an account rather than a draft.
- **W0 §10** — the agent-to-agent rule is carried whole: text arriving from a model is unverified input everywhere, including inside a record that preserves it faithfully.
- **W0 Non-Goal 7** — no `complian-`, safety, or `certif-` claim arises from this record or from anything it governs, in this era or any later one.
- **No new authority.** No edge, zone, class, grant type, authority state, or namespace is minted; **no top-level fence is crossed and no allowlist is amended.** **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide, or design: any key name, field, key order, value set, or nullability rule · the finding-disposition mechanism · any proof module · **the creation of `governance/generated-evaluation/` or any file in it** · any manifest · any record of the class · any run, probe, or fixture · retention, archival, or withdrawal-from-view · any model contact, provider, adapter, client, credential, key, token, secret, private configuration, or model binary · any prompt or probe wording · any specimen · any generated or imported text · the harness, its binding, or its execution · any human-review law or disposition vocabulary · any dependency · the model boundary or any narrowing of its four options · W7-D2-C, W7-D2-D, or W7-D2-E · W7-D3 through W7-D7 · W8 · private adoption in any form · the repair of the carried W6 findings · the optional audit proof module · any stub conversion · any applicability resolution · any Tier 3 conversion · **E10, Z4, E12/Z5, the hosted class, or the local class** · or **medical, therapeutic, diagnostic, or crisis behaviour of any kind.** It amends no record, and it contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording throughout — record, home, manifest, capture, run, grain, hash. **No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no machine-identifying detail, no private lineage.** Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. **The home's name is itself a public-safety decision** — decision 8 chooses a path that tells a scan rule and a human the same thing at the same time. **Nothing here is, or may be presented as, a safety, health, clinical, legal, or regulatory claim of any kind.**

## Dependencies

`W7-D2-RSB` (direct and required — this record's assigned scope) · `ADR-0046` and `ADR-0047` (direct and required — consumed whole) · `W7-AR` · `W7-D1-FCB` · `ADR-0034` (B6 decisions 32–35, decision 37) · `ADR-0033` (B1) · `W2-D4` (rules and §3) · `ADR-0007` · `ADR-0044` (the shape-and-home precedent this record follows) · `ADR-0003` · `W6-CR` (carried context).

## Open boundaries and later ownership

- **Every field, key name, order, and value set** — W7-D2-C, within decisions 13, 16 and 39.
- **The finding-disposition mechanism** — W7-D2-D, within ADR-0046 decision 13 and ADR-0047 decision 17.
- **All four proof obligations** — W7-D2-E, with **S3's feasibility to be demonstrated there and returned as review-only if it cannot be**.
- **Retention, archival, and any withdrawal-from-view question** — W7-D5, per ADR-0034 B6 decision 35.
- **Whether a human-review disposition may ever change once written** — W7-D6.
- **The model boundary and its four options** — W7-D3, wholly, through a Tier F crossing record.
- **S4** — a standing human-review duty, alongside P2, Q3 and R7, owned by no machinery and never closed.

---

*A home for something that does not exist is a strange thing to argue about, until you notice that every part of the argument is really about what happens on a bad day. The sibling directory is for the day someone greps the wrong tree. The manifest is for the day a file goes missing. The immutability rule is for the day a capture is embarrassing and a small edit would fix it. None of those days has arrived. That is exactly why this is the right moment to decide.*
