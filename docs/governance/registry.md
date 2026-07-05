# Governance Registry

**Status:** Accepted by human reviewer, 2026-07-05 (landed under W2-D2)
**Canonical form:** [`governance/registry.json`](../../governance/registry.json) — **the JSON is the registry; this document is its rendering.** Where they disagree, the JSON governs this file, and the source documents govern them both.
**Registered as:** `REGISTRY-MD` (this file) and `REGISTRY-JSON` (the manifest) — both are registry artifacts and carry `content_hash: null` with the self-reference exclusion.

---

**The registry may index authority. It must not mint authority.**

## 1. What this registry is — and is not

This registry records, for every governance-bearing document in scope: identity (`id`, `aliases`, `title`), status, path, role, dependencies, and governance metadata (namespaces, permissions, open-decision pointers, content hash, errata). It exists so that document identity, status, and location can be verified mechanically.

It does **not** summarise doctrine. Entry `role` fields are locational — what a document *is*, never a restatement of what it says. **Nothing may cite this registry as authority for what a document says** — only for where it is, whether it exists, and what status it carries. Any future check, gate, script, or agent that treats registry content as doctrine violates W2-D2's core rule.

## 2. Authority and conflict rules

1. **Source documents win. Always. No exceptions.** The status line inside a document, as accepted by the human reviewer, is the authoritative record. The registry mirrors it.
2. **A registry-vs-document conflict is a registry defect, by definition.** The fix is a correction to the registry (errata-level, logged in the entry), never an edit to the document to match the registry.
3. **If investigating a conflict reveals the *document* is wrong**, the document is fixed first through the two-tier rule (material → decision record; non-semantic → logged erratum), and the registry updates in the same commit as the resolution.
4. **Atomicity:** a commit that changes a governance document but not its registry entry (or vice versa) is a defective commit. Human-enforced until the W2-D5 consistency check mechanises it.
5. **The registry never gates the human reviewer.** It is an instrument of the review process, not a gatekeeper over it.

## 3. Scope

Governance-bearing documents under exactly these directories:

`docs/constitution/` · `docs/decisions/` · `docs/architecture/` · `docs/phases/` · `docs/governance/`

Every governance-bearing document within that scope gets an entry, whatever its status. **README indexes are narrative/index surfaces, not governance entries**, unless explicitly listed by a future decision. Future or planned documents get no entry until a file exists. An in-scope governance file with no entry is a consistency-check failure — absence from this registry is meaningful.

## 4. Hash rules

`content_hash` is `sha256:<hex>` (lowercase), computed over file content normalised to LF line endings, UTF-8, no BOM. **Self-reference exclusion:** the two registry artifacts (`governance/registry.json`, `docs/governance/registry.md`) carry `content_hash: null` with `hash_exclusion_reason: "registry artifact — self-reference exclusion"` — the registry cannot cleanly contain its own hash, and honest null beats clever workarounds. A null hash anywhere else is a defect. Any change to a registered document (including errata) refreshes its hash in the same commit.

## 5. Registered documents

| id | Type | Status | Accepted | Path |
|---|---|---|---|---|
| ADR-0000 | template | template | — | `docs/decisions/0000-template.md` |
| ADR-0001 | adr | accepted | 2026-06-12 | `docs/decisions/0001-local-first-user-held-keys.md` |
| ADR-0002 | adr | accepted | 2026-06-12 | `docs/decisions/0002-safety-surfacing.md` |
| ADR-0003 | adr | accepted | 2026-07-05 | `docs/decisions/0003-relay-landing-ceremony-tiers.md` |
| ADR-0004 | adr | accepted | 2026-07-05 | `docs/decisions/0004-plaintext-residue-policy.md` |
| ADR-0005 | adr | accepted | 2026-07-05 | `docs/decisions/0005-vault-encryption-stack-doctrine.md` |
| ADR-0006 | adr | accepted | 2026-07-05 | `docs/decisions/0006-runtime-platform-stack-doctrine.md` |
| ADR-0007 | adr | accepted | 2026-07-05 | `docs/decisions/0007-development-artifact-policy.md` |
| REGISTRY-JSON | phase-record | accepted | 2026-07-05 | `governance/registry.json` |
| REGISTRY-MD | phase-record | accepted | 2026-07-05 | `docs/governance/registry.md` |
| W0 | constitution | accepted | 2026-06-12 | `docs/constitution/W0-wellbeing-wing-constitution.md` |
| W1-D1 | architecture | accepted | 2026-06-12 | `docs/architecture/W1-data-boundary-map.md` |
| W1-D2 | architecture | accepted | 2026-06-12 | `docs/architecture/W1-D2-consent-scope-model.md` |
| W1-D3 | architecture | accepted | 2026-06-12 | `docs/architecture/W1-D3-authority-staleness-model.md` |
| W1-D5 | architecture | accepted | 2026-06-12 | `docs/architecture/W1-D5-threat-model.md` |
| W1-D6 | architecture | accepted | 2026-06-12 | `docs/architecture/W1-D6-evaluation-plan-skeleton.md` |
| W2-AR | phase-record | accepted | 2026-06-12 | `docs/phases/W2-alignment-report.md` |
| W2-CR | phase-record | accepted | 2026-07-05 | `docs/phases/W2-closure-record.md` |
| W2-D1 | phase-record | accepted | 2026-06-13 | `docs/phases/W2-D1-w1-closure-record.md` |
| W2-D2 | phase-brief | accepted | 2026-07-05 | `docs/phases/W2-D2-governance-registry-brief.md` |
| W2-D3 | phase-record | accepted | 2026-07-05 | `docs/governance/checklist.md` |
| W2-D4 | phase-record | accepted | 2026-07-05 | `docs/governance/fixtures.md` |
| W3-AR | phase-record | accepted | 2026-07-05 | `docs/phases/W3-runway-health-vault-profile-foundations.md` |

Full field detail (aliases, roles, dependencies, namespaces, hashes, errata) lives in the canonical manifest. Type enum: `constitution` / `adr` / `architecture` / `phase-record` / `phase-brief` / `template`. Implementation-permission enum: `none` / `verification-only` / `future-governed`.

## 6. Known errata

- **W0** (logged 2026-07-05): non-semantic header correction during W2-D2 landing, authorised by the human reviewer — the constitution's status line was updated from *"Draft for review"* to *"Accepted by human reviewer, 2026-06-12"*, aligning the source header with the acceptance sealed in W2-D1 §2 and `docs/phases/README.md`. No other W0 content changed; the W0 content hash was recomputed in the same commit.
- **W2-D3** (logged 2026-07-05): checklist rule 9 gained a one-line pointer to [ADR 0003](../decisions/0003-relay-landing-ceremony-tiers.md) (Relay Landing Ceremony Tiers), which extends the landing protocol. Amendment made via decision record per rule 2; the W2-D3 content hash was recomputed in the same commit.
- **W2-D3** (logged 2026-07-05): checklist rule 6 gained an erratum-level note citing the W2-D6 scripted scan layer (`scripts/public-safety-scan.py`); script plus human review applies from 2026-07-05. Non-semantic — the rule already provided for this transition. Hash recomputed in the same commit.

## 7. Public-safety note

This registry contains no private names, no private system references, no companion framing, no personal health details, and no project lineage beyond this repository. Entries describe documents about governance, never people.
