# W2-D2 — Governance Registry / Accepted Document Index

## Alignment Brief

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** June 2026
**Phase:** W2 — Governance Evaluation & Enforcement Foundations (deliverable 2)
**Governed by:** W2 Alignment Report (§5 W2-D2, §9.3); W2-D1 (W1 Closure Record); the accepted W1 corpus
**Scope:** Documentation and registry data only. This brief decides fences; it builds nothing.

---

**W2-D1 sealed W1. W2-D2 makes the sealed corpus findable, checkable, and hard to misread — without making the index more authoritative than the corpus it points to.**

## 0. Core doctrine

**The registry may index authority. It must not mint authority.**

Every rule in this brief is an application of that sentence. The registry records what has been accepted, where it lives, and what it binds — it never becomes the thing that decides. The accepted documents remain the sole source of truth; the registry is a map of them, and a map that disagrees with the territory is a defective map, never a competing territory.

## 1. Purpose

The accepted corpus currently lives in scattered README prose: three README indexes, status lines inside nine documents, and cross-references maintained by hand. That was adequate for a phase where a human read everything. W2's enforcement machinery (the consistency check in W2-D5, the public-safety scan in W2-D6, any future CI gate) needs a single, structured, checkable answer to: *what documents exist, what is their status, where are they, what do they govern, and what do they depend on?*

W2-D2 creates that answer: a human-readable registry index and a machine-readable manifest, indexing the corpus so that document identity, status, path, role, and governing authority can be verified mechanically — without the registry ever substituting for reading the documents themselves.

## 2. Recommended scope (decision question 1)

**Recommendation: registry data only — both artifacts, no validation code.**

- `docs/governance/registry.md` — the human-readable index (documentation, as ever)
- `governance/registry.json` — the machine-readable manifest

The consistency check that asserts registry-matches-repo is **explicitly deferred to W2-D5** (it is verification code, and the runway's execution order lands the test skeleton last, after fixtures and the scan exist). W2-D2 defines what the check must verify (§7, §10); it does not write the check. This keeps W2-D2 free of code, keeps the dependency fence untouched, and honours the runway's execution-order rationale.

Rejected alternatives: *docs-only* (a registry that exists only as prose re-creates the scattered-README problem it exists to solve); *data + validation script now* (crosses into W2-D5's territory out of order and would land a script before the public-safety scan exists to check it).

## 3. Non-scope

W2-D2 creates no user-facing features, no health workflows, no UI, no agents, no adapters, no real or synthetic health data (the registry describes governance documents, never people), no test code, no scripts, no dependencies, no CI configuration, and no schema for anything other than the registry's own document-index format — the one carve-out the W2 runway already justified (§5 W2-D2: metadata about governance documents, not about health data). The registry does not index, summarise, or restate doctrine content; it locates and identifies documents.

## 4. Recommended registry format (decision question 2)

**Recommendation: combination — Markdown table for humans, JSON for machines. JSON over YAML.**

Rationale for JSON:

- **Strict parsing, no implicit-typing surprises.** YAML's implicit conversions (unquoted dates, version numbers becoming floats, `no` becoming `false`) are exactly the class of silent misreading a governance registry must not risk. "Small choice, long shadow" (runway §9.3) favours the strictest parse.
- **Universal consumption.** Any future CI gate, scan, or check reads JSON without a dependency decision. YAML parsing in most stacks means a library — a fence-crossing the registry itself would force.
- **Comments belong in the Markdown index anyway.** YAML's main advantage (comments) duplicates what `registry.md` is for. One artifact for reading, one for parsing; neither does the other's job.

Formatting rules for `registry.json`: pretty-printed (one field per line, for reviewable diffs), keys in a fixed documented order, LF line endings, UTF-8, entries sorted by `id`. A top-level `registry_version` field (schema version, starting `"1.0"`) so future field changes are themselves visible and governed.

The Markdown index and the JSON manifest carry the same entries; the consistency check (W2-D5) verifies they agree. Where they disagree before that check exists, **the JSON is the registry and the Markdown is its rendering** — one canonical artifact, not two.

## 5. Required registry fields (decision questions 3, 6)

### 5.1 Per-entry fields

| Field | Type | Notes |
|---|---|---|
| `id` | string, required | Stable identifier: `W0`, `ADR-0001`, `W1-D1`, `W2-D1`. Never reused, never renamed. |
| `aliases` | list, optional | Alternate identities, e.g. ADR-0002 carries alias `W1-D4`. |
| `title` | string, required | The document's own title, verbatim. |
| `type` | enum, required | `constitution` / `adr` / `architecture` / `phase-record` / `phase-brief` / `template`. `phase-record` covers phase runways and closure records (the W2 Alignment Report; W2-D1). `phase-brief` covers deliverable alignment briefs (this document; future W2 briefs). The two are deliberately distinct so closure records and briefs are never blurred. |
| `phase` | string, required | `W0`, `W1`, `W2`. |
| `deliverable` | string, nullable | `D1`–`D6` where applicable; null for ADRs and the constitution. |
| `path` | string, required | Repo-relative path, forward slashes. |
| `status` | enum, required | `accepted` / `draft` / `superseded` / `template`. Mirrors — never replaces — the document's own status line. |
| `accepted_date` | date, nullable | ISO 8601; null unless status is `accepted`. |
| `role` | string, required | One locational sentence: what the document *is*, not what it says. ("Defines the default-deny flow whitelist" — not a restatement of the whitelist.) |
| `governs` | list of ids | What this document binds or constrains. |
| `depends_on` | list of ids | What this document is governed by. `required_by` is **derived, never stored** — storing both directions invites the two lists to disagree. |
| `resolves` | list, optional | Open questions this document resolved (e.g. `W0-OQ-6`). |
| `id_namespaces` | list, optional | ID families the document owns: D1 edges (`E#`, `M#`, `L#`), `D3-T#`, `D5-T##`, `OR-#`. The registry is where namespace ownership is looked up; the owning document is where meanings live. |
| `implementation_permission` | enum, required | `none` / `verification-only` / `future-governed`. What building, if any, the document authorises. |
| `open_decisions` | list, optional | Pointers into the W2-D1 §5 carried-forward ledger — **references, not copies**. The ledger stays in W2-D1; duplicating it here would create the second source of truth this brief prohibits. |
| `content_hash` | string or null, recommended | Form: `sha256:<hex>` (lowercase hex digest). Computed over file content normalised to LF line endings before hashing, UTF-8, no BOM. Null only for registry artifacts themselves, with `hash_exclusion_reason` (§5.3). |
| `hash_exclusion_reason` | string, conditional | Required when and only when `content_hash` is null. Fixed wording for registry artifacts: `"registry artifact — self-reference exclusion"`. |
| `errata` | list, default empty | Logged non-semantic corrections, per the two-tier rule: date + one-line description each. |

### 5.2 What is deliberately not a field

- **`public_safety_classification`** — rejected. Every document in this public repo must be public-safe; a per-entry classification implies some entries might lawfully not be. Public safety is a global invariant (§8), not a per-document property.
- **`source_of_truth_rule`** — rejected as a field. It is one rule, stated once, in the registry document itself (§7); repeating it per entry adds nothing but drift surface.
- **`last_reviewed_date`** — rejected. A hand-maintained review date that nobody updates becomes false precision — the exact "approved is not current" failure D3 exists to prevent, reproduced in miniature. Git history carries when entries changed; the W2-D5 consistency check verifies registry-vs-repo agreement on every run, which is stronger than a self-reported date.

### 5.3 Content hashing — form, normalisation, and the self-reference rule

Including `content_hash` gives the future consistency check the power to detect **any** change to an accepted document — which is precisely what the two-tier change rule needs teeth for: a material edit without a decision record, or an erratum without a log entry, becomes mechanically visible as a hash mismatch. Every legitimate erratum requires updating the registry in the same commit, which is a feature — atomicity (§9).

**Hash form:** `sha256:<hex>`, lowercase hex digest. **Normalisation:** content is normalised to LF line endings before hashing (Windows checkouts must not produce false alarms), UTF-8, no byte-order mark. The normalisation rule is part of the schema, stated in `registry.md`, so every future implementation of the check hashes identically.

**Self-reference rule:** the registry cannot cleanly contain its own full-file hash — writing the hash into the file changes the file. Rather than clever workarounds (hashing around the field, two-pass computation), registry artifacts — `governance/registry.json` and `docs/governance/registry.md` — carry `content_hash: null` with `hash_exclusion_reason: "registry artifact — self-reference exclusion"`. Simpler, more honest, less clever. All other governance documents are hashed without exception. The consistency check treats a null hash as valid **only** when the exclusion reason is present and the entry is a registry artifact; null anywhere else is a failure.

### 5.4 Coverage and registry scope (decision question 6)

**Registry scope is defined explicitly, by directory.** Governance-bearing documents under:

- `docs/constitution/`
- `docs/decisions/`
- `docs/architecture/`
- `docs/phases/`
- `docs/governance/`

**Every governance-bearing document within that scope gets an entry, whatever its status** — accepted documents, the ADR template, and any future drafts the moment they land. Rationale: a registry of only accepted documents cannot detect an unregistered draft acquiring de facto authority; the default-deny spirit applies — an in-scope governance file with no registry entry is a consistency-check failure, so absence from the registry is meaningful.

**README indexes are narrative/index surfaces, not governance entries**, unless explicitly listed as such by a future decision. The root `README.md` and per-directory `README.md` files guide readers; they carry no doctrine and are not registered. This boundary is stated so that no future landing task tries to register every README or support file merely because it mentions governance.

**Future or planned documents get no entry until a file exists.** The carried-forward ledger (W2-D1 §5) already tracks planned decisions; mirroring it here would duplicate a source of truth.

## 6. Creation timing (decision question 7)

**Recommendation: create the machine-readable file now (in the post-approval landing), not schema-only.** A registry that exists only as a schema indexes nothing, verifies nothing, and closes nothing — W2-D2's closure criteria (§10) are unmeetable without the artifact. The runway already authorises `governance/` for exactly this purpose. Schema-only would defer the entire deliverable's value to an unnamed later moment.

## 7. Authority and conflict rules (decision questions 4, 5)

1. **Source documents win. Always. No exceptions.** The status line inside a document, as accepted by the human reviewer, is the authoritative record. The registry mirrors it.
2. **A registry-vs-document conflict is a registry defect, by definition.** The fix is a correction to the registry (errata-level, logged), never an edit to the document to match the registry.
3. **If investigating a conflict reveals the *document* is wrong** — the conflict exposed a real error in an accepted record — the document follows the two-tier rule: material → decision record; non-semantic → logged erratum. The registry updates only after the document does, in the same commit as the resolution.
4. **The registry contains only metadata derivable from the source documents' own headers and the repo's own state.** No judgment calls, no interpretations, no summaries of doctrine. If a field cannot be filled by pointing at a line in the source document or a fact of the repo, it does not belong in the registry.
5. **Nothing may cite the registry as authority for what a document says** — only for where it is, whether it exists, and what status it carries. Any future check, gate, script, or agent that treats registry content as doctrine violates this deliverable's core rule.
6. **The registry never gates the human reviewer.** It is an instrument of the review process, not a gatekeeper over it (the D2 rights-not-grants spirit, applied to governance itself).

## 8. Public-safety rules for registry entries (decision question 8)

- Generic wording only: no private names, no private system references, no companion framing, no project lineage beyond this repository — in every field, including `role` sentences and errata descriptions.
- Paths, titles, and identifiers come only from the public repo's own files.
- No health data of any kind, real or synthetic — the registry describes documents, never people.
- `registry.json` is **in scope for the public-safety scan** (W2-D6 must scan structured files, not just Markdown — this brief creates that requirement).
- No compliance claims: registry fields state acceptance and alignment, never legal-compliance status.

## 9. Reflecting accepted-record changes (decision question 9)

The two-tier rule (W2 runway, W2-D3) drives the registry, never the reverse:

- **Material / semantic change** → decision record first → the affected entry updates (status, path, hash, supersession) citing the decision record, in the same commit as the change. Superseded documents keep their entries with `status: superseded` — history is never unwritten (Law 13 spirit).
- **Non-semantic correction** → erratum logged in the entry's `errata` list, hash refreshed, same commit.
- **Atomicity rule:** a commit that changes a governance document but not its registry entry (or vice versa) is a defective commit. Until the W2-D5 check enforces this mechanically, the W2-D3 checklist carries it as a review rule.

## 10. Closure criteria for W2-D2 (decision question 10)

W2-D2 closes when:

1. This brief is accepted by the human reviewer.
2. `docs/governance/registry.md` and `governance/registry.json` exist, with entries for **every** governance-bearing document within the §5.4 directory scope (W0, ADR 0001, ADR 0002, W1-D1/D2/D3/D5/D6, W2 alignment report, W2-D1, the ADR template, and this brief once landed) — and no entries for README indexes or files outside that scope.
3. Every entry's `status`, `accepted_date`, and `path` have been verified against the source document's own header by human review — the first and only manual pass; thereafter the W2-D5 check takes over.
4. The Markdown index and JSON manifest agree entry-for-entry.
5. The authority and conflict rules (§7) are stated in `registry.md` itself, so the registry carries its own limits.
6. The public-safety scan requirement for structured files (§8) is recorded for W2-D6.
7. No code, scripts, tests, or dependencies were created.
8. The phases README reflects W2-D2's status; no other README changes its role.

## 11. What Claude Code may touch after review (decision question and required item 10)

**Nothing until this brief is accepted.** Upon acceptance, a landing brief may authorise exactly:

1. `docs/governance/registry.md` — new file (also the first file in `docs/governance/`)
2. `governance/registry.json` — new file (also the first file in `governance/`, the runway-authorised directory)
3. `docs/phases/README.md` — add the W2-D2 row to the W2 deliverables table
4. Root `README.md` — one structure-tree line adding `governance/`, if reviewers want the map current immediately (optional; may wait)
5. `docs/phases/W2-D2-governance-registry-brief.md` — this brief, landed with its accepted status, if reviewers want briefs in-repo (recommended: yes, following the W2-D1 precedent)

Explicitly not authorised, even after acceptance: scripts, tests, fixtures, dependencies, CI configuration, hooks, or any file outside the five above. If landing reveals the need for anything else, that is a new review question, not an improvisation.

## 12. Public-safety note

This brief contains no private names, no private system references, no companion framing, no personal health details, and no project lineage beyond this repository. All wording is generic.

---

*The corpus is sealed; the registry is its catalogue. A catalogue that cannot disagree with its library is useful; one that can overrule it is dangerous. W2-D2 builds the first kind.*
