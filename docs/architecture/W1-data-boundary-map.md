# W1-D1 — Data Boundary Map

**Status:** Accepted by human reviewer, 2026-06-12 · **Date:** June 2026
**Phase:** W1 — Governance Architecture and Data Boundary Design (deliverable 1 of 6)
**Governed by:** W0 Constitution; ADR 0001 (local-first, user-held keys, processing disclosure events)
**Scope:** Documentation only. This map names every data category in the Wellbeing Wing, assigns it a sensitivity class and a home, and defines every permitted flow as an explicit edge. No schema, code, or UI is authorised by this document.

---

## 0. Reading rules

Three rules govern this entire document:

1. **The map is a whitelist.** A flow that does not appear in §5 does not exist. Absence of an edge is a prohibition, not an oversight. Future phases may propose new edges only via decision records with a constitutional check.
2. **Authority and sensitivity are different axes.** Sensitivity (this document) governs *who and what may touch data*. Authority (W0 §7 labels) governs *what data may be treated as true*. A datum can be low-authority and maximally sensitive (an unreviewed extraction from a pathology report) — both regimes apply independently.
3. **Trust boundaries come from ADR 0001.** Plaintext exists only inside the user trust boundary or inside an explicitly granted processing disclosure event. Everything else holds ciphertext or nothing.

## 1. Trust zones

| Zone | Definition | May hold plaintext? |
|---|---|---|
| **Z1 — User trust boundary** | The user's device(s) and key material; an unlocked, authenticated session | Yes |
| **Z2 — Untrusted host** | Any hosted storage/sync infrastructure (hosted mode) | Never — ciphertext only |
| **Z3 — Granted processing** | A live, consent-scoped processing disclosure event (ADR 0001): local model or named vendor model, for a named purpose and duration | Yes — scoped payload only, for the grant's duration |
| **Z4 — Vendor services** | Non-AI external services behind a `VendorAdapter` | Minimum task payload only (e.g., a grocery list); never health, profile, or contemplative content |
| **Z5 — Connected AI systems** | External AI systems behind an `AIAdapter` | Only via Z3 rules; connection model deferred to the AIAdapter ADR (resolves OQ 10) |

**Key material is its own category:** keys live in Z1 only, are never transmitted, never logged, never escrowed (ADR 0001, alternative 3). Key material has no outbound edges at all.

## 2. Sensitivity classes

| Class | Name | Definition | Examples |
|---|---|---|---|
| **C0** | Governance metadata | Plaintext-free with respect to health, personal, and contemplative content, but **privacy-sensitive by pattern**. No processing, no analytics, no behavioural profiling, no external disclosure except user-visible governance and user-initiated export | Consent grants, audit entries, review timestamps, authority labels, processing disclosure logs |
| **C1** | Personal, non-health | Personal preference and planning data with no health meaning on its own | Recipes, food preferences, grocery/staple lists, workout plans |
| **C2** | Health-adjacent, self-reported | User-entered records with health relevance but no clinical source | Symptom logs, supplement records, movement logs, rest/recovery records, health research notes |
| **C3** | Derived health context | Content extracted or summarised from evidence; the Profiles | Draft Health Profile, Approved Health Profile, clinician question lists |
| **C4** | Health evidence | Raw source records; maximal health sensitivity | Vault contents: clinical letters, pathology results, imaging reports, prescriptions, discharge summaries |
| **CM** | Contemplative | Meditation, reflection, spiritual, and contemplative data; sensitivity **peer of C4** but a separate category with a structural wall, not a tier on the health ladder (Law 9) | Practice records, reflections, contemplative notes, library annotations |

Two deliberate properties of this taxonomy: **CM is not "C5."** Making contemplative data a higher rung of the health ladder would imply it participates in health flows at sufficient privilege. It does not participate at any privilege; it is a separate jurisdiction. And **C1 is not "safe."** C1 data is the raw material of cross-room inference (W0 Law 8, failure mode 2); its protections come from edge restrictions, not from pretending food preferences reveal nothing.

A third property, added on architectural review: **C0 is content-free, not privacy-neutral.** The pattern of governance events — when the Vault was accessed, how often, clustering around which dates — can itself reveal sensitive circumstances without a word of plaintext. This is why the ledger has no processing edges (§5) and why C0 carries its own prohibition on analytics and profiling: the record of governance must never become a behavioural dataset.

## 3. Homes

Every category lives in exactly one home. Homes are storage-and-governance domains, not database tables.

| Home | Holds | Zone at rest | Notes |
|---|---|---|---|
| **Health Vault** | C4 | Z1 (local) / Z2 (hosted, ciphertext) | Evidence layer. Single reader: Health Profile Agent under grant (W0 §6–7) |
| **Profile Store** | C3 | Z1 / Z2 ciphertext | Draft and Approved Profiles, with authority labels and last-reviewed timestamps attached as inseparable metadata |
| **Wellness Room records** | C2 | Z1 / Z2 ciphertext | Symptom logs, supplements, research notes, clinician question lists |
| **Kitchen records** | C1 | Z1 / Z2 ciphertext | Recipes, preferences, grocery/staples, meal plans |
| **Gym records** | C1 + C2 | Z1 / Z2 ciphertext | Plans (C1); movement/rest logs (C2) |
| **Meditation Room records** | CM | Z1 / Z2 ciphertext | Structurally isolated; see §5, edges M1–M2 (the only two that exist) |
| **Consent & Audit Ledger** | C0 | Z1 / Z2 ciphertext | Append-only; user-visible; **plaintext-free with respect to C2/C3/C4/CM content** (ADR 0001) — entries reference categories and scopes, never contents |
| **Key material** | — | Z1 only | No edges. Not synced, not logged, not escrowed |
| **Transient processing payloads** | scoped C2/C3/C4 | Z3 only | Exist only for a grant's duration; never persisted by the processing side; retention prohibited |

## 4. Category inventory

| # | Data category | Class | Home | Notes |
|---|---|---|---|---|
| 1 | Vault records (clinical documents) | C4 | Health Vault | Provenance anchor for all C3 entries |
| 2 | Draft Health Profile | C3 | Profile Store | Authority: agent-extracted, pending review; never working context |
| 3 | Approved Health Profile | C3 | Profile Store | The only health context other rooms may read, by scoped section |
| 4 | Authority labels & review timestamps | C0 | Profile Store (attached) | Travel with every read; surfacing required (Law 7) |
| 5 | Symptom logs | C2 | Wellness Room | User-entered; never auto-interpreted |
| 6 | Supplement records | C2 | Wellness Room | Subject to the supplement boundary (W0 §5.1) |
| 7 | Health research notes | C2 | Wellness Room | Source-attributed; never treated as guidance |
| 8 | Clinician question lists | C3 | Wellness Room | Derived; export-on-request only (edge E9) |
| 9 | Recipes, food preferences | C1 | Kitchen | Inference source — protected by edge restrictions |
| 10 | Grocery & staples lists | C1 | Kitchen | Only category with a VendorAdapter edge (E10) |
| 11 | Meal plans | C1 | Kitchen | May embed scoped Profile reads (E6); inherits C3 handling when it does |
| 12 | Workout plans | C1 | Gym | |
| 13 | Movement / rest / recovery logs | C2 | Gym | |
| 14 | Meditation practice records | CM | Meditation Room | |
| 15 | Reflections & contemplative notes | CM | Meditation Room | |
| 16 | Contemplative library & annotations | CM | Meditation Room | User-curated |
| 17 | Consent grants | C0 | Ledger | Who, what, why, duration, revocation state |
| 18 | Audit entries / processing disclosure logs | C0 | Ledger | Actor, scope, recipient class, purpose, time — no content |
| 19 | Key material | — | Z1 only | No category edges; see §1 |
| 20 | Transient processing payloads | varies | Z3 | Scoped subsets of 1–8 under live grant |

## 5. Flow edges (the whitelist)

Notation: `source → destination` with conditions. Every edge involving C2/C3/C4 plaintext leaving Z1 is a **processing disclosure event** per ADR 0001 (grant naming recipient class, purpose, scope, duration; audited; payload-minimised).

### Health spine

- **E1. User → Vault.** Upload of records. Encryption at the user boundary before any storage; in hosted mode, only ciphertext reaches Z2.
- **E2. Vault → Health Profile Agent (Z3).** The *only* outbound Vault edge. Requires an explicit per-purpose grant; processing disclosure event; payload scoped to the permitted records.
- **E3. Health Profile Agent → Draft Profile.** Extractions land labelled *agent-extracted, pending review*, with provenance references to source records.
- **E4. Draft Profile → User review → Approved Profile.** Section-by-section; high-stakes fields individually confirmed (W0 §7). This is an **authority transition, not a data movement** — content changes status, not location. Review timestamp written (Law 7).
- **E5. Approved Profile (scoped sections) → Wellness Room display.** With authority labels and section age surfaced.
- **E6. Approved Profile (allergies, confirmed dietary requirements only) → Kitchen.** Scoped read under standing consent; section age surfaced on every use.
- **E7. Approved Profile (confirmed injury/physical notes only) → Gym.** Same conditions as E6.
- **E8. User ↔ any of their own records, any room.** The user reads and edits their own data freely within Z1; user action is never gated by the agent rules.
- **E9. Wellness Room → clinician export (user-initiated only).** Produces the clinician summary / question list as a user-triggered export crossing the boundary *by the user's own hand*; format is a W1 open item (OQ 5).

### Vendor and AI edges

- **E10. Kitchen (grocery/staples list only) → VendorAdapter (Z4).** Minimum payload: the list. Never preferences-as-rationale, never Profile content, never the dietary context that shaped the list. Logged; user-visible.
- **E11 (rule, not flow).** E11 is **not itself a permitted flow.** AI processing flows must be declared as concrete per-room, per-class, per-purpose edges. Every declared E11-family edge is user-initiated (Law 1; ADR 0001 — no background processing) and a full processing disclosure event. The declared edges:
  - **E11-W. Wellness Room → Z3.** AI assistance on scoped C2/C3 Wellness Room content only (e.g., summarising symptom logs on request, organising supplement records, preparing clinician questions), within the W0 §5.1 boundaries.
  - **E11-K. Kitchen → Z3.** AI assistance on C1 Kitchen records only. Approved Profile sections enter Kitchen processing exclusively through E6 — never as direct Z3 payload.
  - **E11-G. Gym → Z3.** AI assistance on C1/C2 Gym records only. Approved Profile sections enter exclusively through E7.
  - **M2** remains the only Meditation Room processing edge; **E12** remains reserved.

  Any future AI processing flow not on this list requires a new declared edge via decision record — the generic edge is deliberately absent so that it can never become the back door.
- **E12. AIAdapter (Z5) connections.** Edge *reserved, not yet defined*. No Z5 flows exist until the AIAdapter ADR (OQ 10) specifies authentication, scoping, and impersonation prevention. Reserving the edge explicitly prevents it from being improvised later.

### Meditation Room (complete edge list)

- **M1. User ↔ Meditation Room records.** Read, write, practice, reflect.
- **M2. Meditation Room (scoped content) → Z3, user-initiated only.** E.g., the user asks for help engaging with a text or reviewing their own reflections. Processing disclosure event; CM payload; nothing persists outside the room; no output may be written to any other room.

**There are no other Meditation Room edges.** No M→health, no health→M, no M→Profile, no M→adapters, no M-derived metadata in any other home. Any future bridge is a user-created, named, separately consented, revocable construct requiring its own decision record (W0 §5.4) — and until such a record exists, bridge requests are declined by design, not by discretion.

### Ledger edges

- **L1. All governed events → Consent & Audit Ledger.** Grants, revocations, disclosure events, authority transitions, Vault access, adapter payloads (by reference). Append-only.
- **L2. Ledger → User.** Full visibility (Law 13).
- **The ledger has no processing edges.** Audit data is never input to any agent, model, or inference process. The record of activity must not become a behavioral dataset — that would be cross-room inference through the back door (Law 8).

### Forbidden edges (the anti-map — named for emphasis, though Rule 1 already excludes them)

| Forbidden flow | Violates |
|---|---|
| Vault → any room, display, adapter, or export (other than E2) | W0 §6; ADR 0001 |
| Draft Profile → any room (it has no authority to be read as context) | Law 3 |
| Room → room, any direction, any payload | Law 4; failure mode 2 |
| Meditation Room ↔ anything beyond M1–M2 | Law 9 |
| Profile or preference content → VendorAdapter | W0 §8.6; failure mode 10 |
| Ledger → any processing | Law 8; L2 note |
| Agent-derived inference → any record without user confirmation | Laws 3, 8 |
| Key material → anywhere | ADR 0001 |

## 6. Plaintext zone summary (ADR 0001 applied)

Plaintext may exist in exactly two places: **Z1** (the user's unlocked session) and **Z3** (a live, granted, scoped processing payload). It may never exist in: hosted storage (Z2), ledger entries, adapter logs, vendor payloads beyond the minimum task data of E10, or any retained artifact of a Z3 event after the grant ends. W1's threat model (deliverable 5) inherits this summary as its starting state.

## 7. Constitutional check

- **Law 4** is implemented as the whitelist itself: minimum necessary access becomes *named edges with scoped payloads*, default-deny.
- **Law 8** is implemented as three structural absences: no room→room edges, no ledger→processing edge, no inference-write edge. The map removes the channels through which inference would travel, rather than asking agents to refrain.
- **Law 9** is implemented as the shortest edge list in the document: M1 and M2, nothing else.
- **Law 7** rides along every Profile edge (E5–E7): labels and ages are attached metadata, not optional context.
- **Law 13** is implemented as L1–L2 plus the plaintext-free constraint.
- **ADR 0001** is implemented in §1, §6, and the processing-disclosure conditions on E2, the E11 family, and M2.

No law required reinterpretation. Two design judgments, both reviewed: **E12 is reserved-but-undefined** — the alternative, omitting AIAdapter from the map entirely, was rejected because undocumented gaps get improvised under delivery pressure; a reserved edge with an explicit "nothing flows until the ADR exists" is safer than silence. And **E11 was converted from a generic edge to a rule with concrete per-room edges** on architectural review: the generic form was the loosest edge on the map, and loose edges become creep points. Default-deny now applies inside the AI-processing family, not just around it.

## 8. Feeds into

- **Consent & scope model (W1-D2):** every edge above that requires a grant defines what the grant object must express.
- **Safety surfacing decision (W1-D4 / OQ 1):** surfacing triggers may only reference categories and edges named here — the map bounds what surfacing is even allowed to see.
- **Threat model (W1-D5):** starts from §6.
- **AIAdapter ADR (OQ 10):** defines E12.
