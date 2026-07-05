# W3 — Health Vault and Health Profile Foundations

## Phase Runway / Alignment Report

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026
**Phase:** W3 — the first product-spine phase
**Governed by:** W0 Constitution; ADR 0001; ADR 0002; ADR 0003; the accepted W1 corpus; the sealed W2 corpus and its enforcement machinery
**Tier at landing:** J — Judgment (phase runway; full ceremony when landed)

---

**W1 wrote the laws. W2 taught the repo to check them. W3 builds the first thing the laws were written for — the spine that holds evidence, derives context, and lets the user decide what becomes true. No model touches any of it yet.**

## 1. W2 closure dependency

W2 is sealed and published (closure record accepted 2026-07-05). W3 therefore begins with working gates, not promises:

- the **registry** indexes every governance document and is test-asserted on every run;
- the **checklist** and **ADR 0003 ceremony tiers** govern every landing;
- the **public-safety scan** runs in landing mode over every enumerated file before first commit, and in normal mode after;
- the **synthetic fixtures** and **deterministic suite** must stay green through every W3 commit — the suite's directory-fence tests will be *amended, by record, to admit exactly what W3 authorises*, and nothing else.

Every W3 landing inherits this machinery whole. W3 adds product-spine code under it — the first phase where "the only code checks rules" gives way, deliberately and gate-by-gate, to code that does something, still under rules that check it.

## 2. W3 north star

**The first useful product direction is an honest health archive.** A governed filing cabinet with unusual integrity: the user can keep their health evidence encrypted under keys only they hold, record where each document came from, see honestly what is known, unknown, stale, contradicted, or pending review — and decide, section by section, what becomes active working context.

It is **not** an AI health assistant. **Not** a medical adviser. **Not** a recommendation engine. The Wing's differentiation is its restraint, and the first impression it makes should be of an archive that refuses to lie, not an assistant with opinions. Anything a model might later do arrives through the adapter phase's own gates — none of which W3 opens.

**The structural insight that shapes the phase:** the corpus's authority grammar contains a complete no-AI path — user entry → *user-reported* → user review → *confirmed by user* (D3-T3/T4), plus correction and supersession. W3 builds the entire spine on that path. The extraction pipeline (E2→E3) exists in the data model as a labelled possibility and is exercised only by synthetic-fixture simulation in tests; no model, local or hosted, touches anything in W3.

## 3. Proposed W3 deliverable sequence

| ID | Deliverable | Shape |
| :---- | :---- | :---- |
| **W3-D1** | Encryption / platform decision cluster | The stack decisions, evidence-gated: doctrine records accepted first, a disposable evaluation spike (never committed) reports against fixed criteria, then final-selection records land the choices |
| **W3-D2** | Vault data boundary and import boundary | E1 implemented as doctrine demands: bytes plus user-supplied provenance, zero content interpretation at import; the Vault as evidence layer, encrypted at the user boundary, single lawful outbound edge reserved |
| **W3-D3** | Health Profile object model | Draft and Approved layers as data structures: inseparable authority and staleness label pairs, provenance references, bounded-unknown records, contradiction flags — the D3 grammar as a working data model, no UI |
| **W3-D4** | Draft → Approved review flow | The transition engine with user-act gating (D3-T2/T4/T7/T8); per the accepted minimal-review posture: tests simulate review acts against synthetic fixtures only; nothing real becomes Approved until real review surfaces exist in a later phase |
| **W3-D5** | Local storage / residue rules | The plaintext residue policy implemented and residue-tested: nothing decrypted persists past task end; logs plaintext-free in every build configuration; platform-uncontrollable residue documented honestly |
| **W3-D6** | Export / backup / key-loss wording | Export as a right at the data layer; encrypted backup export with restore symmetry; the key-loss and backup sentences vetted and catalogued — consequence and remedy in the same breath, plain, not frightening |
| **W3-D7** | W3 closure readiness | Closure record: criteria assessment, suite extended and green, pending-ledger updates (W3-owned stubs unblocked or honestly carried), incident log, and the W4/W5 gate drafted |

Execution order may resequence where dependencies allow (the W2-D6-before-D5 precedent stands; IDs stay stable). The likely critical path: D1's doctrine records → D1 spike → D1 selections → D2/D3 in parallel → D4/D5 → D6 → D7.

## 4. Required decision records before implementation

No W3 implementation code lands until these are accepted — and **reviewed v-drafts already exist for all eight** in the planning corpus, awaiting the relay's review loop:

1. **Encryption stack** (doctrine now: no custom crypto, audited library, authenticated encryption, versioned format, escrow-free migration; final selection after spike evidence)
2. **Runtime / platform stack** (doctrine now: verifiably telemetry-silent, no background processes, user-initiated updates; selection after the scored spike)
3. **Plaintext residue policy** (default-deny persistence; logs plaintext-free always; the first gate on the critical path)
4. **Dev log / screenshot policy** (synthetic-only development artifacts from the first W3 commit)
5. **Import file boundary** (bytes + user provenance; no OCR, no classification, no content-derived anything)
6. **Minimal review question** (tests simulate; real review waits for surfaces — reversal only by new record)
7. **Local backup guidance** (ciphertext backup anywhere, key custody nowhere but the user; offered once, never nagged)
8. **Key-loss onboarding wording** (the plain sentence, vetted; firm, not theatrical)

Each lands through full ceremony as its own decision record before the code it gates.

## 5. Explicit non-goals

W3 contains: **no AI adapters, no prompts, no model payloads, no agent behaviour** (the adapter phase's gates are untouched; prompt-eligibility remains false everywhere); **no UI polish** (W3 is a data layer with the minimum surface its own testing requires — the review-surface phase owns everything a user will actually look at); **no reminders or notifications** (the definition fence stands: anything contacting the user outside an active session is the notification layer, which does not exist); **no hosted service, no cloud sync** (local-first, local-only; hosted remains its own future gate with its own disclosures); **no clinical logic** (no diagnosis, treatment advice, recommendations, interactions, or clinical decision support of any kind — the archive stores and labels; it never opines); **no real health records anywhere** — not in the repo, tests, fixtures, logs, screenshots, or docs; the synthetic-only discipline extends into the runnable era via the dev-artifact policy, and a real user's real data exists only in that user's local runtime, never in any project artifact.

## 6. First app-shape language

What the spine does, in plain words — the first honest sentence of product this project has produced:

- the user can **add or import a document** into an encrypted Vault only they can open;
- the user can **record where it came from** — source, date, a note in their own words;
- the system can **label what is known, unknown, stale, contradicted, or pending review** — and never pretends otherwise;
- the user **decides what becomes the Approved Health Profile**, section by section;
- **everything else remains evidence or draft** — visible, labelled, and without authority until a user act says otherwise.

Nothing in that list requires a model, and nothing in it makes a claim about the user's health. That is the point.

## 7. W3 entry gate

Per checklist rule 8 and the W2 closure record §8, W3 may not start until all three exist and are accepted:

1. the W2 closure record — **accepted and published** ✔;
2. this W3 runway — pending review;
3. the first W3 deliverable brief — pending.

Three documents, three acceptances, no exceptions. This runway, when accepted, authorises W3 *briefs* — not immediate scaffolding, not implementation. Code arrives only behind its decision records, its briefs, and its tier ceremonies; the first new directory and the first cryptographic dependency will be the phase's first Tier F crossings, each named and separately authorised.

## 8. Public-safety note

This runway contains no private names, no private system references, no companion framing, no project lineage beyond this repository, no real health data, no clinical examples, and no model names. All wording is generic: user, Wing, vault, draft profile, approved profile, human reviewer, architect, model.

---

*Two phases proved the Wing can govern itself. W3 builds the first thing worth governing: a place where a person's evidence is safe, their record is honest, and nothing becomes true about them without their own hands making it so.*
