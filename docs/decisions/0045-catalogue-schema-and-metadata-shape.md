# 0045 — Catalogue Schema and Metadata Shape (W6-D2-B)

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation by itself.
**Date:** August 2026 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D2** (landing **W6-D2-B**)
**Position:** the second landing of the W6-D2 five-landing plan: the schema-shape decision record, defining the future catalogue's JSON top-level structure, entry record shape, metadata fields, canonical key order, null/empty semantics, lifecycle posture, and validation-facing constraints — **inside the fixed W6-D2-A inputs, which are not reopened.** The blueprint is decided in doctrine; **no file, no standalone schema artefact, no entry, and no identifier — final or illustrative — is created.** The default of decision-record-only holds: no source-derived need for a separate schema file was found, and none exists.
**Constitutional references:** W0 Laws 3, 13; W0 Non-Goal 7. **No law is amended.**
**North star carried:** governed truth must survive display without becoming authority.
**Resolves:** none.

---

**The ground is firm; this record draws the blueprint. Every entry the register will ever hold gets its shape today: eleven fields, one canonical order, no hidden defaults, and a ceiling written into every record as its last field — so that a future reader opening the file finds each string already wearing, in its own metadata, the sentence that keeps it honest. Nothing is poured. The drawings are signed, the validator knows exactly what to measure, and the thirty-three candidates now know exactly what admission would require of them.**

## Decision question

**What JSON shape will the future catalogue artefact take — top level, entry record, fields, key order, null semantics, lifecycle — such that W6-D2-C can validate it deterministically, W6-D2-D can populate it one string at a time, and no field, grouping, or ordering can ever encode authority, priority, or display permission?**

## Controlling law

- **The W6-D2 opening brief (`W6-D2-GSC`)** — landing B's assignment: the record shape carrying ADR-0042 decision 2's fields as data, no final IDs absent separate explicit grant.
- **ADR-0044, fixed inputs not reopened:** home `governance/string-catalogue.json` · format JSON under the standing conventions · registered-with-hash at first creation · ADR-0039 rule 12 owed by the artefact about itself · and the identity/authority ceiling: registration, presence, hash correctness, and membership are necessary where later law requires them, **never sufficient for display**.
- **ADR-0042** — the eleven-field metadata law (decision 2), ID law (decisions 6–7), namespace law (decisions 8–9), seed posture, the thirteen validator obligations this schema must be checkable against, and the exclusion law (nothing in the schema may smuggle in layout, glyphs, colours, affordances, or behaviour).
- **ADR-0038** — the seven vocabulary classes as the only lawful class values; class-as-data; the barred display list and stem bans the validator will enforce over `string` fields; derived-never-stored (the schema stores derivation *references*, never derived presentation states).
- **ADR-0039** — the authority-non-increasing derivation law behind `derivation_reference`; **ADR-0040/0041** — the accompaniment tables behind `accompaniment_linkage`; **ADR-0043** — the register may never become a surface, store, or channel, which bounds what fields may exist at all.
- **Repository precedent** — `registry.json`'s top-level pattern (version, note, entries), followed as the option E source-derived refinement.

## Decisions

### Part A — The door

1. **This record decides the schema in doctrine and creates nothing.** The catalogue file remains uncreated; no standalone schema file exists or is needed (the schema's single authoritative statement is this record, and the validator implements it directly — a second schema artefact would be a second source of truth); no entry exists; no `CAT-####` identifier exists in any form, including illustrative.

### Part B — The top-level shape

2. **The future artefact is a single JSON object with four top-level keys, in this canonical order:** `catalogue_version` (a version string for the artefact's own format, advanced only by governed record) · `status` (the artefact's own lifecycle posture — birth value `governed_register_active`, changed only by governed record) · `governance_note` (a fixed, brief statement of what the artefact is and is not, byte-stable, its wording set at W6-D2-D's first population within ADR-0042's identity law) · `entries` (the array of catalogue records, **born empty at file creation and populated only by W6-D2-D's per-string decisions**).

3. **Why this shape:** it is the registry's own proven pattern — version, note, entries — the closest structural kin in the tree; it gives the validator a fixed four-key surface to assert exactly; and it holds no field in which grouping, ranking, or display semantics could ever live. **Defining these keys creates no file**: the values above are doctrine for a future artefact, and the first byte of that artefact arrives only at a later authorised landing.

### Part C — The entry record shape

4. **Option A is chosen: a flat `entries` array, each entry a complete record carrying all eleven fields.** No grouping by class (option B rejected: grouping becomes semantic hierarchy — a reviewer shortcut today is a class-priority claim tomorrow, V6's exact drift). No grouping by room or source (option C rejected: room grouping encodes domain ownership and pre-decides surface information architecture that is DR-W6-06-era law, not storage). No normalised multi-table shape (option D rejected: premature normalisation creates hidden joins, validation fragility across referential seams, and a second system to keep honest — the register is small, and explicit repetition is cheaper than implicit joins). **Deterministic order within the array: sorted by `id`, ascending, allocation order — which by ADR-0042 encodes nothing.**

5. **Every entry carries every field, always — no omitted keys, no hidden defaults.** Nullability is explicit and closed: exactly two fields are nullable (`derivation_reference`, `prohibition_register`), with defined meanings below; every other field is mandatory and non-null. An entry missing a key, carrying an extra key, or ordering keys non-canonically is invalid — shape errors are validator failures, never style choices.

6. **The canonical key order, fixed:** `id` · `string` · `vocabulary_class` · `source_authority` · `derivation_reference` · `accompaniment_linkage` · `prohibition_register` · `source_citation_requirement` · `supersession_retirement_posture` · `proof_obligations` · `display_authorisation_statement`. Identity first, the governed wording second, its law after, and **the ceiling last — every record ends with the sentence that bounds it.**

### Part D — Field semantics, one by one

7. **`id`** — a lawfully allocated `CAT-####` value (ADR-0042 grammar), required for every real entry, **allocated only by W6-D2-D or later authorised landings — never by this record, which contains no such identifier in any form.** The ID identifies one governed string record only, and encodes nothing: no class, room, priority, quality, confidence, ranking, order, approval, source authority, display permission, or any property from the barred families.

8. **`string`** — the exact governed display wording, verbatim: the governed text itself, never a paraphrase. No string exists in this landing. Barred words and stems remain governed by ADR-0038 over this field absolutely, with the single lawful exception routed through `prohibition_register` below.

9. **`vocabulary_class`** — one machine value from a closed set of exactly seven, each tied one-to-one to ADR-0038 decision 3: `source_state_label` · `derived_presentation_label` · `routing_label` · `non_authority_label` · `review_label` · `prohibition_label` · `future_owned_label`. Class is data, not prose; it authorises nothing and implies no quality, rank, or readiness.

10. **`source_authority`** — a non-empty array of citations, each a registered-record identifier with a section or decision pointer (`"ADR-0040 decision 10"` form): the governed sources that authorise the string's existence and wording, supporting source-bound exactness rather than vague provenance. **No source authority, no entry — and source authority is not display authority.**

11. **`derivation_reference`** — `null` where the string is verbatim from its source; where derived, a citation to the accepted record carrying the registered deterministic derivation rule, which must be authority-non-increasing under ADR-0039 decision 5. No unregistered derivation can be expressed in the schema at all — the field admits citations, not formulas — so softening-by-derivation has no place to live.

12. **`accompaniment_linkage`** — an array of citations to the governed accompaniments ADR-0040/0041 require for the string's state or role, referenced **before allocation by their record-and-decision citations** (never by unallocated catalogue IDs; after W6-D2-D allocates, linkage may cite `CAT-####` values of admitted accompaniment entries). An empty array is lawful **only** where no accompaniment law applies, and the validator cross-checks emptiness against the class and the ADR-0040/0041 tables — an accompaniment can never be omitted by choice, only absent by law.

13. **`prohibition_register`** — `null` for every ordinary entry, meaning barred wording is unlawful anywhere in its `string`; for prohibition-class entries and any entry whose wording lawfully contains barred terms in negation form, an object `{ "basis": "<record citation>" }` citing the law that permits it. This is the schema's single gate for barred content: **the validator enforces that `certif-`, `complian-`, and every barred word or stem appear in a `string` only where `prohibition_register` is non-null** — distinguishing a prohibited example lawfully displayed as prohibition from an unlawful display string, exactly as ADR-0038 decision 11 requires.

14. **`source_citation_requirement`** — exactly `"required"` or `"not_required"`: whether later display of this string must carry its source citation or source-bounded explanation. **Never optional where ADR-0038 decision 9, ADR-0040, or ADR-0041 require source-bound language** — the validator cross-checks the value against class and law, so "not_required" is a checked legal fact, never a convenience.

15. **`supersession_retirement_posture`** — a structured object, birth value `{ "state": "active" }`; supersession `{ "state": "superseded", "by": "<CAT-#### once allocated>", "record": "<citation>" }`; retirement `{ "state": "retired", "record": "<citation>" }`. Entries are stable and immutable in `id` and `string`; posture changes only by future governed record; **no silent edit, no deletion-as-cleanup, no ID reuse, ever** — a superseded or retired entry remains in the file as history with its posture visible.

16. **`proof_obligations`** — a non-empty array of machine-readable obligation tokens from a closed set defined here and extendable only by record: `barred_word_check` · `class_check` · `derivation_check` · `accompaniment_check` · `source_check` · `lifecycle_check` · `no_display_authorisation_check`. The tokens name what the validator and any future surface must satisfy for this entry; **listing an obligation claims no proof has occurred** — obligations are debts, not receipts.

17. **`display_authorisation_statement`** — a single fixed sentence, byte-identical in every entry, verbatim: **"catalogue membership is necessary where later law requires it, never sufficient for display; entry presence, id presence, registry hash, and validator results do not authorise display."** The ceiling as data, in every record, checked verbatim by the validator — so no entry can ever be read, exported, or excerpted without its own boundary travelling with it.

### Part E — Handoffs

18. **W6-D2-C receives, as its complete validation specification:** the four-key top-level shape and canonical order · the eleven-field entry list and canonical key order · the closed seven-value class set · the two-field nullability law and every null/empty meaning · the id-sorted deterministic array order · the lifecycle object grammar · the closed proof-obligation token set · the fixed verbatim ceiling sentence · the prohibition-register gate over barred wording · and the cross-checks (accompaniment emptiness against law; citation requirement against class; barred terms against register) — together with ADR-0042 Part F's thirteen obligations, which this schema is shaped to make checkable without exception.

19. **W6-D2-D receives:** a schema into which each of the thirty-three seed candidates may later be admitted — one at a time, on the record, with class, sources, and metadata complete — or rejected with the reason written down. **Nothing is admitted or rejected here; no bulk admission, no silent admission; rejection remains lawful.**

### Part F — Boundaries

20. **This record does not decide:** any actual entry or wording · any allocation · the `governance_note`'s final wording (W6-D2-D's first population, inside ADR-0042's identity law) · the validator implementation (W6-D2-C) · any admission or rejection (W6-D2-D) · completion (W6-D2-E) · grading (W6-D3) · surfaces (W6-D4). **W6-D2 remains open under its brief; W6-D2-A remains in force unweakened; W6-D3 through W6-D6 remain unopened; W7 remains unopened.** No fixture, evaluation record, pending-ledger entry, Lane C row, Tier 3 row, or applicability record changes; no validator wakes; no model is contacted; no dependency is added.

## Alternatives considered

- **Grouped-by-class entries (option B, rejected).** A grouping is a claim about kinship and rank that the flat array refuses to make; the class lives in each record as data, where the validator checks it and no eye can read hierarchy into it.
- **Grouped-by-room entries (option C, rejected).** Room grouping is surface information architecture smuggled into storage — and the Meditation zero would become a visible empty section, converting a source-derived finding into a permanent visual statement no record authorised.
- **Normalised multi-table shape (option D, rejected).** Four small tables joined by references would make every validator check a join and every diff a puzzle; the register's honesty budget is better spent on explicit, repeated, checkable fields.
- **A standalone schema file (considered, not created).** The brief's default holds: this record is the schema's single authoritative statement and the validator implements it directly. A second artefact would be a second source of truth with its own drift risk, and no source-derived need for one was found.
- **Optional keys with implied defaults (rejected firmly).** An implied default is an invisible decision; every field is present, every null is defined, and absence is always an error rather than a meaning.

## Consequences

- W6-D2-C can be written against a complete, closed specification — every check enumerated, no judgement calls in the validator.
- W6-D2-D's admissions become fill-in-the-record acts: each candidate either satisfies eleven explicit fields or is rejected with the gap named.
- Every future reader of the catalogue file meets the ceiling sentence inside every entry — the register carries its own boundary at record granularity, forever.

## Constitutional check

- **Law 3** — no field, grouping, order, or default can encode authority: the ID law, flat array, id-sort, and per-entry ceiling close every channel this schema could have offered.
- **Law 13** — the schema is auditable doctrine now and auditable data later; every posture change requires a governed record.
- **W0 Non-Goal 7** — the ceiling sentence in every entry makes certification-style misreading structurally impossible at the record level.
- **No new authority, no new namespace, no allocation** — the `CAT-####` grammar stays grammar-only; this record contains no such identifier in any form.

## Non-goals

This record authorises no catalogue file, no standalone schema file, no entry, no final or illustrative catalogue ID, no seed admission or rejection, no string grading, no D5-T24 execution, no validator wake or edit, no rendered label, no UI, no CLI, no review surface, no cache, no annotation store, no state store, no workflow, no approval, conversion, or retirement path, no human review, no human decision record, no runtime, fixture, evaluation-record, pending-ledger, Lane C, Tier 3 or applicability change, no model contact, no generative evaluation, no dependency, no E10/vendor, Z4, E12/Z5 or hosted movement, no W6-D3 through W6-D6 opening, and no W7 opening. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording — schema, field, entry, record, class, citation, validator. Barred vocabulary appears only inside prohibitions; the two scan-sensitive families appear only as the stems the validator will police. No real user data, no vendor or model names, no URLs, and no claim of any kind about any person, string, or readiness.

## Dependencies

`W6-D2-GSC` (direct and required — landing B's assignment) · `ADR-0044` (direct and required — the fixed inputs this schema lives inside) · `ADR-0042` (direct and required — the eleven-field law, ID law, and validator obligations) · `ADR-0038` (direct — the seven classes, barred list, stems, derived-never-stored) · `ADR-0039` (direct — rule 12 and authority-non-increasing derivations) · `ADR-0040` (direct — accompaniment law behind `accompaniment_linkage`) · `ADR-0041` (direct — its accompaniments and human-act boundary) · `ADR-0043` (direct — the no-surface/no-store bound on what fields may exist) · `ADR-0003` (operative ceremony authority).

## Open boundaries and later ownership

1. **Validator implementation of this specification** — W6-D2-C, waking the dormant class with same-commit proofs.
2. **First file creation, `governance_note` wording, allocation, and every admission or rejection** — W6-D2-D, per string, on the record.
3. **Proof-obligation token-set extension** — future governed records only.
4. **Any posture change to any future entry** — its own governed record, visible forever.

---

*The blueprint is signed: eleven fields, one order, two lawful nulls, seven class values, and a ceiling sentence that will live inside every record like a keel inside a hull. The register now exists everywhere except on disk — which is exactly where it should exist, one landing before the watcher wakes to measure it.*
