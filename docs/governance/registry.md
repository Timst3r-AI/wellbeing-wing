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
| ADR-0008 | adr | accepted | 2026-07-05 | `docs/decisions/0008-runtime-stack-final-selection.md` |
| ADR-0009 | adr | accepted | 2026-07-05 | `docs/decisions/0009-import-file-boundary.md` |
| ADR-0010 | adr | accepted | 2026-07-05 | `docs/decisions/0010-minimal-review-posture.md` |
| ADR-0011 | adr | accepted | 2026-07-05 | `docs/decisions/0011-local-backup-guidance.md` |
| ADR-0012 | adr | accepted | 2026-07-05 | `docs/decisions/0012-key-loss-onboarding-wording.md` |
| ADR-0013 | adr | accepted | 2026-07-05 | `docs/decisions/0013-kdf-custody-envelope-selection.md` |
| ADR-0014 | adr | accepted | 2026-07-06 | `docs/decisions/0014-licence-selection.md` |
| ADR-0015 | adr | accepted | 2026-07-06 | `docs/decisions/0015-durable-ledger.md` |
| ADR-0016 | adr | accepted | 2026-07-10 | `docs/decisions/0016-room-contract-template.md` |
| ADR-0017 | adr | accepted | 2026-07-10 | `docs/decisions/0017-room-isolation-model.md` |
| ADR-0018 | adr | accepted | 2026-07-10 | `docs/decisions/0018-read-write-scope-confirmation.md` |
| ADR-0019 | adr | accepted | 2026-07-11 | `docs/decisions/0019-cross-room-inference-prohibition-standard.md` |
| ADR-0020 | adr | accepted | 2026-07-11 | `docs/decisions/0020-unknown-stale-contradicted-behaviour-standard.md` |
| ADR-0021 | adr | accepted | 2026-07-15 | `docs/decisions/0021-contract-validator-requirements.md` |
| ADR-0022 | adr | accepted | 2026-08-09 | `docs/decisions/0022-contract-validator-m10-m12-correction.md` |
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
| W3-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-closure-record.md` |
| W3-D2-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-D2-closure-record.md` |
| W3-D3-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-D3-closure-record.md` |
| W3-D4-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-D4-closure-record.md` |
| W3-D5-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-D5-closure-record.md` |
| W3-D6-CR | phase-record | accepted | 2026-07-06 | `docs/phases/W3-D6-closure-record.md` |
| W4-AR | phase-record | accepted | 2026-07-10 | `docs/phases/W4-runway-room-contracts.md` |
| W4-D2 | room-contract | accepted | 2026-07-22 | `docs/rooms/wellness-room-contract.md` |
| W4-D3 | room-contract | accepted | 2026-08-04 | `docs/rooms/kitchen-room-contract.md` |
| W4-D4 | room-contract | accepted | 2026-08-09 | `docs/rooms/gym-room-contract.md` |
| W4-D5 | room-contract | accepted | 2026-08-09 | `docs/rooms/meditation-room-contract.md` |
| W4-D6-EASR | assurance-register | accepted | 2026-08-10 | `docs/governance/external-assurance-source-register.md` |
| W4-D6-PHDAR | assurance-record | accepted | 2026-08-10 | `docs/governance/privacy-health-data-assurance-record.md` |
| W4-D6-BEF | phase-record | accepted | 2026-08-11 | `docs/governance/behavioural-evaluation-fixtures.md` |
| W4-CR | phase-record | accepted | 2026-08-12 | `docs/phases/W4-closure-record.md` |
| W5-AR | phase-record | accepted | 2026-08-13 | `docs/phases/W5-runway-runtime-enforcement-evaluation.md` |
| ADR-0023 | adr | accepted | 2026-08-13 | `docs/decisions/0023-aiadapter-import-citation-correction.md` |
| ADR-0024 | adr | accepted | 2026-08-13 | `docs/decisions/0024-aiadapter-processing-context-boundary.md` |
| ADR-0025 | adr | accepted | 2026-08-13 | `docs/decisions/0025-provisional-freshness-governance-qualification.md` |
| ADR-0026 | adr | accepted | 2026-08-14 | `docs/decisions/0026-safety-relevant-set-citation-correction.md` |

Full field detail (aliases, roles, dependencies, namespaces, hashes, errata) lives in the canonical manifest. Type enum: `constitution` / `adr` / `architecture` / `phase-record` / `phase-brief` / `template` / `room-contract`. Implementation-permission enum: `none` / `verification-only` / `future-governed`.

## 6. Known errata

- **W0** (logged 2026-07-05): non-semantic header correction during W2-D2 landing, authorised by the human reviewer — the constitution's status line was updated from *"Draft for review"* to *"Accepted by human reviewer, 2026-06-12"*, aligning the source header with the acceptance sealed in W2-D1 §2 and `docs/phases/README.md`. No other W0 content changed; the W0 content hash was recomputed in the same commit.
- **W2-D3** (logged 2026-07-05): checklist rule 9 gained a one-line pointer to [ADR 0003](../decisions/0003-relay-landing-ceremony-tiers.md) (Relay Landing Ceremony Tiers), which extends the landing protocol. Amendment made via decision record per rule 2; the W2-D3 content hash was recomputed in the same commit.
- **W2-D3** (logged 2026-07-05): checklist rule 6 gained an erratum-level note citing the W2-D6 scripted scan layer (`scripts/public-safety-scan.py`); script plus human review applies from 2026-07-05. Non-semantic — the rule already provided for this transition. Hash recomputed in the same commit.

- **ADR-0021** (logged 2026-08-09): the section 11 mechanical validator requirements matrix gained a one-line pointer to [ADR 0022](../decisions/0022-contract-validator-m10-m12-correction.md) (Contract Validator M10/M12 Decidability Correction), which corrects the M10 and M12 requirements. Non-semantic: no corrected rule is restated in ADR-0021. Amendment made via decision record per checklist rule 2; hash recomputed in the same commit.

- **W4-D2** (logged 2026-08-09): the Wellness contract's section 2 E5 verbatim quotation regained the source-owned leading list marker ("- ") dropped in transcription, restoring byte-for-byte agreement with [W1-D1 §5](../architecture/W1-data-boundary-map.md). Non-semantic: two characters added, no clause content changed. Hash recomputed in the same commit.

- **W1-D5** (logged 2026-08-13): the section 8 required-decision-records list gained a corrected pointer for the AIAdapter ADR's import obligation, authorised by [ADR 0023](../decisions/0023-aiadapter-import-citation-correction.md). The citation instructed importing this threat model's "Z3/Z5 rows" wholesale; the document contains a Z3 boundary row and no Z5 row. Non-semantic: subjects and strength unchanged, no threat row or residual altered. Hash recomputed in the same commit.

- **W1-D6** (logged 2026-08-13): the section 9 item 4 AIAdapter ADR entry gained the same corrected pointer, authorised by [ADR 0023](../decisions/0023-aiadapter-import-citation-correction.md). Non-semantic: subjects and strength unchanged. Hash recomputed in the same commit.

- **ADR-0002** (logged 2026-08-14): the intensity-ladder safety-relevant definition had its provenance clause corrected, authorised by [ADR 0026](../decisions/0026-safety-relevant-set-citation-correction.md). The clause called ADR-0002's six-member safety-relevant set *"the same high-stakes set W0 §7 requires individual confirmation for"*; W0 §7's list has five members and excludes injuries. The corrected clause names W0 §7's five high-stakes fields together with injuries. The six-member set is not adjudicated and is unchanged; the ladder, per-case table, doctrines and language law are untouched. Amendment made via decision record per checklist rule 2; hash recomputed in the same commit.

## 7. Public-safety note

This registry contains no private names, no private system references, no companion framing, no personal health details, and no project lineage beyond this repository. Entries describe documents about governance, never people.
