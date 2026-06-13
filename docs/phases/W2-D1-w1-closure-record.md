# W2-D1 — W1 Closure Record

**Status:** Accepted by human reviewer, 2026-06-13 **Date:** June 2026 **Phase:** W2 — Governance Evaluation & Enforcement Foundations (deliverable 1) **Type:** Closure record / audit seal. Docs-only. Authorises nothing to be built.

---

**W1 is not closed because the documents exist. W1 is closed because the accepted corpus now binds what later phases may build.**

## 1. Closure statement

**W1 — Governance Architecture and Data Boundary Design — is closed.** Its accepted corpus is the binding governance baseline for the Wellbeing Wing. No later phase may contradict it; changes to it follow the two-tier rule (material → decision record; non-semantic → logged errata) established in the W2 runway.

## 2. Accepted W1 corpus

The following are accepted, committed, and binding as of W1 closure:

| Document | Role |
| :---- | :---- |
| W0 Constitution | Foundational laws, non-goals, room boundaries |
| ADR 0001 | Local-first by default; hosted-compatible via user-held keys; processing disclosure events |
| W1-D1 — Data Boundary Map | Categories, zones, sensitivity classes, default-deny flow whitelist |
| W1-D2 — Consent & Scope Model | Permission grammar; rights-not-grants distinction |
| W1-D3 — Authority & Staleness Model | Truth and freshness grammar |
| ADR 0002 — Safety Surfacing Doctrine | Speech-integrity surfacing; intensity ladder; language law |
| W1-D5 — Threat Model | Adversarial governance threat catalogue and mitigation matrix |
| W1-D6 — Evaluation Plan Skeleton | What must be proven, and how, before features exist |

## 3. What W1 established

The binding baseline, in one line each:

- **User-held key doctrine** — the user holds the keys; hosted infrastructure is untrusted; storage, processing, and vendor disclosure are separate privacy questions (ADR 0001).
- **Health Vault → Draft Profile → Approved Profile** — evidence becomes derived context becomes working context only through user review (W0 §6–7; D3).
- **Default-deny flow whitelist** — a data flow not listed does not exist; absence of an edge is prohibition (D1).
- **Consent grammar** — edge-bound, scoped, time-bounded, revocable; no blanket or generic authority (D2).
- **Rights-not-grants distinction** — the user's own access, export, and erasure are rights, never consent-gated (D2 §0.3).
- **Authority & staleness grammar** — only the user mints truth; automated processes may lower trust, never raise it, and may never make uncertainty disappear (D3).
- **Safety surfacing doctrine** — the Wing governs its own speech, never the user's actions; surfacing reads labels, never bodies; no coercion, no escalation (ADR 0002).
- **Threat model** — the architecture is named adversarially, with honest residuals; governance fails at seams, not centres (D5).
- **Evaluation skeleton** — overclaim and underclaim graded symmetrically; behavioural risks require evaluation, not just doctrine (D6).
- **Public-safety requirements** — generic wording only; no private references; alignment, never compliance claims.

## 4. What W1 explicitly did not create

W1 produced governance and nothing else. It created **no** schema, app code, UI, test code, evaluation harness, prompts, scoring algorithms, agents, adapters, medical logic, security tooling, production workflows, real health data, or implementation dependencies. The Wing remains, at W1 closure, exactly as useful to an end user as it was at the project's start: not at all. This is by design.

## 5. Open decisions carried forward

Unresolved by intention, owned by future phases:

| Carried item | Lands in |
| :---- | :---- |
| Staleness intervals by data type | Decision record (D3 OQ 1) |
| Backup / recovery guidance | Decision record, before public availability (against ADR 0001) |
| Queue-design rules | Surface-design phase (D5-T20) |
| AIAdapter ADR | Defines D1 edge E12 (D5-T16; resolves W0 OQ 10) |
| VendorAdapter ADR | Governs E10 vendor disclosure mechanics |
| Revocation cascade | Decision record (resolves W0 OQ 2; D2 §5) |
| Notification-layer definition fence | Decision record (D5-T16) |
| UI surface-design standard | Surface-design phase (D5-T24 governance theatre; legibility rule) |
| Export warning language | Surface-design phase (D5-T22) |
| Hosted-mode disclosure language | Decision record (D5 OR-1, OR-2) |
| Evaluation harness implementation | Later phase, after W2 establishes testability (D6) |

This list is the carried-forward ledger; W2 closes none of it except where a W2 deliverable explicitly says so.

## 6. W2 authority boundary

**W2 may only make W1 testable and enforceable.** W2 may not treat W1 closure as permission to build user-facing health features. No room, Vault, agent, adapter, UI, or health workflow is authorised by this closure or by W2. The only code W2 may contain is code that checks rules; no code that does things for users.

## 7. Public-safety note

This record contains no private names, no private system references, no companion framing, no personal health details, and no project lineage beyond this repository. All wording is generic.

---

*W1 is sealed. The corpus binds. W2 begins the work of proving the Wing keeps its own laws — and builds nothing else.*
