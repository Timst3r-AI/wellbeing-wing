# 0044 — Catalogue Artefact Shape and Home (W6-D2-A)

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation by itself.
**Date:** August 2026 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D2** (landing **W6-D2-A**)
**Position:** the first landing of the W6-D2 five-landing plan: the decision record for the future governed string catalogue artefact's repository home, file format, registry posture, and declarability posture. **It decides where and in what shape the catalogue will one day live — and creates none of it.** No catalogue file, no schema, no entry, no `CAT-####` identifier (final or illustrative), no seed admission, no validator wake, no rendering.
**Constitutional references:** W0 Laws 3, 13; W0 Non-Goal 7. **No law is amended.**
**North star carried:** governed truth must survive display without becoming authority.
**Resolves:** none.

---

**Before the register can be built, someone has to say where it stands and what it is made of — and say it in ink, so the file's own existence is never an accident of convenience. This record picks the ground: one machine-readable artefact, in the governance tree beside the registry it mirrors, hash-tracked like every governed document, and shaped so that a validator can read every claim it will ever carry. Nothing is built today. The plot is surveyed, the material is chosen, and the deed is recorded — so that when W6-D2-B pours the foundation, not one decision has to be made under load.**

## Decision question

**Where will the governed string catalogue artefact live, in what format, under what registry posture, and with what declarability guarantee — decided now, as fixed input to W6-D2-B, without creating the artefact, its schema, its entries, or its identifiers?**

## Controlling law

- **The W6-D2 opening brief (`W6-D2-GSC`)** — landing W6-D2-A's assigned scope, verbatim: home, format, registry posture, declarability statement; *no entries, no IDs, no schema fields beyond what the decision itself requires to be stated.*
- **ADR-0042, whole** — catalogue identity (a governed register, never a surface or a source of authority), the membership and exclusion laws the artefact must be able to carry, the ID and namespace law the artefact must be able to host without encoding meaning in identity, the seed posture, the thirteen validator obligations the artefact must be checkable against, and the Part G gate.
- **ADR-0043** — declarability, no-surface, no-cache/no-store, no-fifth-channel: the artefact this record sites must be a register a bounded reader consumes — it can never itself become a surface, a store of display state, or a channel.
- **ADR-0039 rule 12** — declarability as the admission condition, owed by the catalogue artefact about itself; **ADR-0038** — class-as-data and mechanical checkability, which the format must serve.
- **Repository precedent, consulted as required by the brief's option D:** the registry (`governance/registry.json` — a single governed JSON register, self-reference-excluded from hashing); the evaluation records (`governance/evaluation/` — a governed JSON artefact class, deliberately unregistered under ADR-0034 B6); the Lane C pattern (JSON blocks inside registered Markdown doctrine documents); and the fixture rule (data files carry no registry entries).

## Decisions

### Part A — The door

1. **This record decides shape and home and creates nothing.** After this landing the repository contains exactly one new governed artefact: this record. The catalogue itself remains uncreated, and every statement below about "the artefact" describes a future thing that only W6-D2-B and later authorised landings may bring into existence.

### Part B — The home

2. **The future catalogue artefact's home is `governance/string-catalogue.json`** — a single artefact in the governance tree, beside the registry it structurally mirrors.

3. **Why this home:** the catalogue is governance-visible by nature — an index of what may be shown, not documentation about it — and the brief requires it visibly within governance boundaries, never hidden in runtime or tests. `governance/` is the repository's established home for exactly this kind of thing: the registry (the index of authority) and the evaluation records (the governed observation class) already live there, and the catalogue (the index of permitted words) is their sibling in kind. A single file, rather than a directory of fragments, keeps the register atomic: one artefact, one hash, one diff per change, one thing for the validator to hold whole — the `registry.json` precedent, followed deliberately.

### Part C — The format

4. **The future catalogue artefact's format is JSON** — UTF-8, no BOM, LF line endings, lower_snake_case keys, indented for line-oriented diffs — the repository's standing data conventions (W2-D4 §3), carried unchanged.

5. **Why this format:** the brief's constraints are deterministic, diffable, mechanically checkable, stable under review, and fit for validator consumption — and JSON under the standing conventions satisfies all five with the least machinery: deterministic parse with no prose ambiguity; line-oriented diffs at record granularity; direct consumption by the future W6-D2-C validator with no extraction step; and structural room for every ADR-0042 decision 2 field as data. **Key order, record layout, and every schema field remain W6-D2-B's** — this record fixes the material, not the blueprint.

### Part D — The registry posture

6. **The future catalogue artefact will be registered in `governance/registry.json` with a content hash**, under its own entry, created by the same authorised landing that first creates the file — hash and bytes born together, moving only together in atomic commits, under the standing same-commit hash discipline.

7. **Registration provides integrity tracking only.** It is not display authority, not acceptance of any entry, not proof of any wording's quality, and not a claim of any kind — exactly as a registered doctrine document's hash proves its bytes and nothing about the world. The identity-versus-authority separation is preserved at every layer: **a catalogue file existing, being registered, and hashing correctly cannot authorise the display of one word.** Display authorisation continues to require everything the six W6-D1 records require, of which catalogue membership is one necessary condition among several, never a sufficient one.

8. **Why registered rather than excluded:** the two exclusion precedents do not apply. The registry excludes *itself* only to avoid recursive self-reference; the evaluation records are excluded because they are an append-only *observation* class whose integrity is proven by deterministic reproduction. The catalogue is neither: it is a small, live, authority-adjacent register — like the fixture strategy's map, whose registered hash moves with every governed change — and hash-tracking is precisely how this repository keeps such registers honest. Deliberate exclusion was considered and rejected: it would make the one artefact listing every displayable word the least integrity-tracked governed file in the tree, which is backwards.

### Part E — The declarability posture

9. **The future artefact must satisfy ADR-0039 rule 12 about itself before anything it holds can:** it must be able to declare, as data, every catalogue-record field ADR-0042 decision 2 requires and W6-D2-B will shape — ID, string, vocabulary class, source authority, derivation reference, accompaniment linkage, prohibition register, source-citation requirement, supersession/retirement posture, proof obligations, and the standing no-display-authorisation statement — and it must remain mechanically checkable, whole, by the future W6-D2-C validator implementing the thirteen Part F obligations. **This names the required capability; the fields themselves are not created here.** An artefact shape that cannot carry these declarations would fail this record before failing any later one.

### Part F — Alternatives, assessed as the brief required

10. **Option B — Markdown under `docs/`, registered (rejected).** Human-readable, but the register's meaning would live in prose-adjacent structure: weaker machine validation, an extraction step in front of every validator check, and the named risk the runway bound — copy-deck drift, where a readable file quietly becomes an editable voice. The catalogue's readers are validators and future surfaces; humans read it through governance, not through typography.

11. **Option C — split model, machine catalogue plus generated documentation (deferred, not adopted).** Premature for W6-D2-A: no surface exists, no reader exists, and generated read-only documentation is at earliest a W6-D5-era presentation-assurance question. Splitting now would create a second artefact with no consumer and a synchronisation obligation with no proof machinery. The single machine artefact is decided; any future generated view is someone else's record, derived read-only, never a second source.

12. **Option D — repository-pattern alternatives (consulted; one pattern followed, one rejected).** The Lane C pattern (JSON inside registered Markdown) was assessed and rejected for the catalogue: it suits doctrine-with-data documents where prose rulings and rows belong together, but the catalogue's doctrine already lives in six ADRs, and a pure register gains nothing from a prose wrapper except extraction fragility. The `registry.json` pattern — single governed JSON register in `governance/` — was followed instead, as the closest kin in function and the strongest precedent in place.

### Part G — Inheritance and boundaries

13. **W6-D2-B receives as fixed input:** the home (`governance/string-catalogue.json`), the format (JSON under the standing conventions), the registry posture (registered-with-hash at first creation), and the declarability capability requirement of decision 9. B shapes the schema and record layout inside these; it does not reopen them.

14. **Still owned elsewhere, untouched here:** the schema and metadata shape (W6-D2-B) · the validator wake and the thirteen obligations' implementation (W6-D2-C) · every seed admission or rejection decision (W6-D2-D) · completion (W6-D2-E) · grading (W6-D3) · surfaces (W6-D4) · presentation assurance (W6-D5) · phase closure (W6-D6).

15. **W6-D2 remains open under its brief; W6-D3 through W6-D6 remain unopened; W7 remains unopened.** No seed string is admitted, rejected, or graded; no validator is woken or edited; no label renders; no fixture, evaluation record, pending-ledger entry, Lane C row, Tier 3 row, or applicability record changes; no model is contacted; no dependency is added.

## Consequences

- W6-D2-B can begin at the blueprint, with ground, material, and deed already in ink — no schema decision will smuggle in a home decision under load.
- The catalogue will be born registered, hash-tracked from its first byte, and structurally checkable — the same governance posture as every document it will serve.
- The two drift risks the runway named — copy-deck drift and catalogue scope creep — are both cut off at the shape: a machine register in the governance tree has no prose to drift and no room to grow sideways.

## Constitutional check

- **Law 3** — nothing about home, format, or registration confers authority: decision 7 states the ceiling in terms, and the identity-versus-authority separation survives the artefact's whole lifecycle.
- **Law 13** — the artefact will be auditable data under a registered hash, in the tree built for exactly that.
- **W0 Non-Goal 7** — no posture decided here can be presented as any certification-style property of the catalogue or its contents.
- **No new authority, no new namespace, no allocation** — the `CAT-####` grammar stays grammar-only; this record contains no identifier of that shape at all.

## Non-goals

This record authorises no catalogue file, no schema, no entry, no final or illustrative catalogue ID, no seed admission or rejection, no string grading, no D5-T24 execution, no validator wake or edit, no rendered label, no UI, no CLI, no review surface, no cache, no annotation store, no state store, no workflow, no approval, conversion, or retirement path, no human review, no human decision record, no runtime, fixture, evaluation-record, pending-ledger, Lane C, Tier 3 or applicability change, no model contact, no generative evaluation, no dependency, no E10/vendor, Z4, E12/Z5 or hosted movement, no W6-D3 through W6-D6 opening, and no W7 opening. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording — artefact, register, home, format, hash, validator. Barred vocabulary appears only inside prohibitions; the two scan-sensitive families are untouched entirely. No real user data, no vendor or model names, no URLs, and no claim of any kind about any person, string, or readiness.

## Dependencies

`W6-D2-GSC` (direct and required — landing A's assigned scope) · `ADR-0042` (direct and required — everything the artefact must be able to carry and be checked against) · `ADR-0043` (direct — the register may never become a surface, store, or channel) · `ADR-0039` (direct — rule 12 owed by the artefact about itself) · `ADR-0038` (direct — class-as-data and mechanical checkability served by the format) · `ADR-0003` (operative ceremony authority).

## Open boundaries and later ownership

1. **Schema, record layout, and key order** — W6-D2-B, inside this record's fixed inputs.
2. **The registry entry for the artefact** — created by the first authorised landing that creates the file, hash and bytes together.
3. **Validator implementation against this shape** — W6-D2-C, per ADR-0042 Part F.
4. **Any generated read-only view** — a future record, at earliest W6-D5-era, derived and never a second source.

---

*The ground is chosen: one file, in the governance tree, made of the same honest material as the registry beside it, hash-tracked from its first byte to its last. Nothing stands there yet — and that is the discipline holding, not the work lagging. When the schema comes, it will find the ground already firm.*
