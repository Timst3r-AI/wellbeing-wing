# Synthetic Fixture Strategy

**Status:** Accepted by human reviewer, 2026-07-05 (Stage A — strategy only; Stage B fixture data pending W2-D6)
**Phase:** W2 — Governance Evaluation & Enforcement Foundations (deliverable 4, Stage A)
**Classification:** Docs-only in Stage A. This document defines the binding rules for all evaluation data, forever — not just W2's. It lands no fixture data, no code, no loaders, no tooling.
**Governed by:** W2 Alignment Report (§5 W2-D4); W2-D1; W1-D6 (§3.10 — no test may require private data); W1-D5 (hard cases); the accepted W1 corpus

---

**Bad fixtures test nothing. Real data tests the wrong thing at unacceptable cost.**

## 1. Purpose

The deterministic tests (W2-D5) need data to assert against: grants to validate, labels to check, edges to probe, contradictions to surface. This strategy makes that data a governed artifact — reviewable, mapped to the grammar IDs it exercises, and structurally incapable of containing real health information. These rules bind every fixture ever created for this project, in every phase.

## 2. The fixture rules (binding)

1. **Fully synthetic, by construction — never by scrubbing.** Fixtures are authored from nothing. Derivation from any real person's health information — including anonymised, aggregated, paraphrased, or "inspired by" — is prohibited. There is no de-identification pathway, because there is no identification to remove.
2. **Marked SYNTHETIC in name and content.** Every fixture file carries `SYNTHETIC` in its filename and a marker block at the top of its content (§4) stating: synthetic, authored for governance testing, corresponds to no real person.
3. **Non-realistic identifiers only.** Personas use structured artificial identifiers (`Persona-K1`, `Persona-M3`) — never human-plausible names. A realistic name anywhere in `fixtures/` is always a public-safety finding, with no judgment call required.
4. **Medically meaningless values, structurally valid forms.** Fixture health content uses placeholder tokens — `Allergen-X`, `Medication-A17`, `Condition-Q` — well-formed for the grammar being tested, meaningless as medicine. **Ontology rule:** these are grammar fixtures, not synthetic medical claims. `Allergen-X` is not a fake allergen; it is a token occupying the allergen *slot* in a grammar-shaped structure. Fixtures are not fake clinical data — fake clinical data invites clinical reasoning; grammar placeholders cannot. No fixture is clinically meaningful; **no fixture may require medical plausibility to pass**; a fixture that starts needing clinical realism has left this strategy's scope and is redesigned, not medically enriched.
5. **Every fixture maps to grammar IDs.** Each fixture declares, in its marker block, which IDs it exercises: D1 edges (`E2`, `M2`…), D3 labels and transitions (`D3-T6`…), D2 grant elements, D5 threats (`D5-T08`…). Unmapped fixtures are dead weight; the map is what makes the set reviewable for coverage.
6. **Fixtures are data, never code.** No loaders, generators, or helper scripts in `fixtures/` — those are verification code and live in `tests/` (W2-D5). A fixture is inert.

## 3. Format

Fixture files are JSON — same rationale as the registry: strict parsing, zero-dependency consumption, no implicit-typing surprises. Conventions:

- **Filename:** `SYNTHETIC-<persona>-<subject>.json` (e.g., `SYNTHETIC-persona-k1-grants.json`), lowercase, hyphenated.
- **Encoding:** UTF-8, no BOM, LF line endings — the registry's rules, uniformly applied.
- **Field conventions:** field names in lower_snake_case; IDs referencing governance namespaces use their canonical prefixed forms verbatim (`D3-T6`, `D5-T08`, `E11-K`).

## 4. The SYNTHETIC marker block (schema)

Every fixture file's top-level object begins with a `synthetic_marker` object:

```json
{
  "synthetic_marker": {
    "synthetic": true,
    "notice": "SYNTHETIC fixture authored for governance testing. Corresponds to no real person. Values are grammar placeholders, not medical content.",
    "exercises": ["D3-T6", "D5-T08"],
    "persona": "Persona-K1"
  }
}
```

- `synthetic` is literally `true`, always — a mechanically checkable assertion target.
- `notice` carries the fixed wording above, verbatim.
- `exercises` is the grammar-ID map (rule 5); empty is invalid.
- `persona` names the artificial identifier(s) the fixture uses.

A file in `fixtures/` without a valid marker block is a defect (W2-D5 Tier 1 asserts this once fixtures exist).

## 5. Hard-case coverage (the Stage B seed set)

The seed set must exercise, at minimum: expired safety-relevant items (allergies at every staleness state); contradicted medications (record-vs-record and user-vs-record); unknown-scoped absences vs confirmed negatives (the D3 §5.5 trap, both sides); the full staleness ladder walk (current → review due → stale → expired); consent grants missing each grammar element in turn (thirteen invalid grants, one per required element); blanket-scope and unbounded-duration grant attempts; cross-room bait (Kitchen data inviting a Gym inference); Meditation Room bridge attempts; consent revocation mid-task; a forbidden-edge attempt for every row of the D1 anti-map; agent-origin content attempting each prohibited authority transition.

The fixture set is itself reviewable: coverage review checks every hard case has at least one fixture, verified against the marker-block maps.

## 6. The two-stage rule (binding sequence)

W2-D4 lands in two explicitly separated stages. **The deliverable ID remains W2-D4 throughout — staging, not renumbering.**

- **Stage A — this document, alone.** No fixture data lands with it. *(This stage.)*
- **Stage B — the seed fixture set.** `fixtures/SYNTHETIC-*.json` files are committed **only after W2-D6 has landed and its public-safety scan has run over the fixture files in landing mode** (covering the not-yet-tracked files before their first commit). Fixtures are the highest-volume text/data surface this repo will have; they are never committed before the scan exists to pre-check them. Stage B's landing brief enumerates the fixture files individually, per the landing protocol. If W2-D6 is delayed, Stage B waits — no schedule pressure converts unscanned data into an acceptable commit.

## 7. Registration boundary

This strategy document is registered (`W2-D4`). **Fixture data files are not registry governance documents** — they are data governed *by* this document, marked and mapped per its rules, checked by scan and tests, but they carry no registry entries. The registry indexes authority; fixtures exercise it.

## 8. Non-scope

No real health data, ever, in any form or derivation. No loaders, parsers, or test code. No behavioural-evaluation transcripts or prompts (a later phase; they will need their own strategy extension, reviewed then). No fixture modelling a real clinical scenario in medically meaningful terms. No demographic realism (ages, locations, occupations) beyond what a grammar test structurally requires — and the default is: none.

## 9. Public-safety note

This document contains no private names, no private system references, no companion framing, no personal health details, no clinical examples, and no project lineage beyond this repository. All example values are grammar placeholders; the placeholder register (`Persona-K1`, `Allergen-X`, `Medication-A17`, `Condition-Q`) is itself the rule.
