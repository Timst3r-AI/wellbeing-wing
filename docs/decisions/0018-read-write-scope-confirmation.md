# 0018 — Read/Write Scope Confirmation

**Status:** Accepted by human reviewer, 2026-07-10. Not a build instruction.
**Date:** July 2026 · **Phase:** W4 — Room Contracts (third doctrine record; deliverable W4-D1)
**Decision mode:** doctrine-derived; no evidence spike required — this record confirms and transmits the sealed map, deciding a fidelity mechanism, not a scope.
**Constitutional references:** W1-D1 (the authoritative data-boundary map — sole source of truth for scope; §0 Rule 1 whitelist); W1-D2 (consent authorises edges, cannot create them); W1-D3 (the D3-T3 label-on-entry rule); the W0 no-new-authority discipline.
**Blocks:** the Read Scope and Write Scope sections of every room contract (W4-D2 … W4-D5), which carry their scope under this record's fidelity rule.

## Decision question

ADR 0016 fixed a Read Scope section and a Write Scope section in every room contract; W1-D1 already decided *which* scope each room has. The question this record answers is narrow: **how must the four contracts carry those authoritative read and write scopes without semantic drift?** It does not reopen which scope any room should have — the map decided that — only how scope text moves from the map into a contract without a plausible paraphrase quietly moving a boundary.

## Context

W4 is open for governed doctrine and brief work only; ADR 0016 (the template) and ADR 0017 (isolation) are the first two landed W4 doctrine records, and this is the proposed third. Scope terms are governance boundaries — the operative text of a permission, where one altered word changes what is allowed — not explanatory prose. Direct reading of the live W1-D1 during this record's preparation exposed that even the W4 planning pack and the runway restate D1's scope in slightly drifted words: the friendliest paraphrase is exactly where a boundary silently shifts. This record makes fidelity mechanical, so no contract can carry a drifted scope.

## Controlling law

- **W1-D1 §0 Rule 1 — the map is a whitelist.** A flow that does not appear in §5 does not exist; absence of an edge is a prohibition, not an oversight; new edges arrive only via a decision record with a constitutional check.
- **W1-D1 §§3–5** — the homes, category inventory, and flow edges are the authoritative statement of every room's read and write scope. Sole source of truth.
- **W1-D2 §0.1** — consent authorises edges; it cannot create them. A grant references a permitted W1-D1 edge by ID; a "yes" to an unlisted flow is a request for a new edge, not a grant. Consent cannot conjure an absent edge.
- **W1-D3 (authority/staleness), transition T3** — the label applied to room records on entry.
- **W0 no-new-authority discipline** — this record introduces no edge, class, consent form, or authority state; it constrains how existing scope is transcribed.

## Decision

1. **W1-D1 is the sole source of truth for every room's read and write scope.** No other document — including this record, the W4 pack, the runway, or a summary — is scope authority.
2. **Scope is carried into a contract only through the required paired form:**
   - **(a) Exact authority reference** — the registered W1-D1 record, the exact section, and the exact edge or scope identifier (e.g. `W1-D1 §5 · E6`). This is the **controlling authority**.
   - **(b) Complete verbatim quotation** — copied from the cited W1-D1 source, punctuation and load-bearing qualifiers preserved, visibly marked as a quotation. This provides **human legibility**.
   Both are required for every authoritative read/write scope. **Reference-only is not the normal accepted form; quotation-only is not the normal accepted form.**
3. **If the quotation and the cited D1 source differ, the contract fails review.** D1 governs — but the contract must be corrected to match D1 before acceptance; a mismatch is never resolved by altering D1.
4. **Contracts never paraphrase scope.** Friendlier, shorter, broader, narrower, modernised, "clarified," or "equivalent" wording is **not equivalent governance.** A contract cannot independently widen, narrow, reinterpret, simplify, modernise, or clarify a D1 scope.
5. **Blur-words are prohibited within a scope clause.** The named, source-backed prohibited terms are: **"generally", "such as", "including", "including but not limited to".** These are accepted **examples** of the broader rule, not an exhaustive vocabulary list. **The broader anti-drift rule:** *any wording that opens, softens, generalises, exemplifies, or makes discretionary an exact W1-D1 boundary is prohibited within a scope clause.* Blur-words may appear in clearly non-authoritative explanatory prose (room-side procedure) **only where they cannot be mistaken for scope authority.**
6. **Scope amendments occur in W1-D1 first**, through their own accepted decision-and-constitutional-check ceremony. **Contracts update only after the D1 amendment lands**; contracts may not lead a scope change. **Stale or mismatched contract quotations fail review** — never tolerated as "close enough." No silent widening or narrowing, in either direction.
7. **Absence of a D1 edge means absence of authority** — not an undocumented discretionary permission. **Consent or grants cannot create an absent edge** (W1-D2 §0.1).
8. **Rooms write only their own authorised record classes** (W1-D1 §§3–4), with the authority label applied on entry by exact reference to the sealed **D3-T3** rule. **No room writes into another room's jurisdiction** (no room→room write edge exists).
9. **This record confirms and transmits scope; it mints none.** ADR 0016 created the Read Scope and Write Scope slots; ADR 0017 supplies the complementary architectural-isolation wall; DR-W4-03 supplies the fidelity rule and names D1 as the content source. No room contract is drafted here.

## Constitutional check

- **W1-D1 Rule 1 upheld:** the record adds no edge and asserts the whitelist; absence stays a prohibition.
- **No new authority:** no edge, class, consent form, or authority state is minted; the record constrains transcription of existing scope only.
- **Authority axes respected (W1-D1 Rule 2; W1-D2 §2):** confirming scope raises no authority and lowers no sensitivity; the D3-T3 label carries no profile authority.
- **No law required reinterpretation**, and **no amendment to the Constitution or to W1-D1 is proposed or authorised** by this record.

## Authoritative read scopes

Reproduced from the live W1-D1 §5, punctuation and qualifiers preserved. Contracts carry each in the paired form (exact reference + complete verbatim quotation).

- **Wellness Room — edge E5.** Verbatim: *"E5. Approved Profile (scoped sections) → Wellness Room display. With authority labels and section age surfaced."* Load-bearing: *scoped sections* (a subset, not the whole Profile); read is **to display**; *authority labels and section age surfaced*.
- **Kitchen — edge E6.** Verbatim: *"E6. Approved Profile (allergies, confirmed dietary requirements only) → Kitchen. Scoped read under standing consent; section age surfaced on every use."* Load-bearing: *only* (closed list); *confirmed*; *standing consent*; *section age surfaced on every use*.
- **Gym — edge E7.** Verbatim: *"E7. Approved Profile (confirmed injury/physical notes only) → Gym. Same conditions as E6."* Load-bearing: *confirmed*; *only*; conditions stated **by reference** — *"Same conditions as E6"* — which the contract preserves **as a reference**, never expanded into a restated list.
- **Meditation Room — complete edge list M1–M2.** Verbatim: *"M1. User ↔ Meditation Room records. Read, write, practice, reflect."* and *"M2. Meditation Room (scoped content) → Z3, user-initiated only."* with *"nothing persists outside the room; no output may be written to any other room."* and *"There are no other Meditation Room edges."* The Meditation Room has **no Approved-Profile read edge** — no health→Meditation edge exists. Its contract states scope from its **complete edge list and the "no other edges" clause**, **not** from an intuitive "reads nothing" summary.

## Authoritative write scopes

From the live W1-D1 §§3–4 (homes and category inventory). Every room writes only its own records, at their D1 classes; no record class is invented or derived from a room's name.

- **Wellness Room — home C2.** Own record classes: *"Symptom logs"* (C2), *"Supplement records"* (C2), *"Health research notes"* (C2); *"Clinician question lists"* (**C3** — *"Derived; export-on-request only (edge E9)"*). Not authorised to write: the Approved Profile (that is the user's own act via E4, not a room write); any other room's records.
- **Kitchen — home C1.** Own record classes: *"Recipes, food preferences"* (C1), *"Grocery & staples lists"* (C1), *"Meal plans"* (C1 — *"May embed scoped Profile reads (E6); inherits C3 handling when it does"*). Not authorised to write: the Approved Profile; any other room's records.
- **Gym — home C1 + C2.** Own record classes: *"Workout plans"* (C1), *"Movement / rest / recovery logs"* (C2). Not authorised to write: the Approved Profile; any other room's records.
- **Meditation Room — home CM.** Own record classes: *"Meditation practice records"* (CM), *"Reflections & contemplative notes"* (CM), *"Contemplative library & annotations"* (CM — *"User-curated"*). Writes nothing outward (M2: *"no output may be written to any other room"*); nothing beyond M1–M2.

**Label on entry (D3-T3), by exact reference and, where quoted, verbatim:** *"T3. User entry → user-reported. Automatic on entry into room records; carries no profile authority."* The applied label is **User-reported** — *"Entered by the user (logs, notes) but not reviewed into approved status,"* applied by *"System, on user entry,"* *"Room-scoped use only; never profile truth."* Contracts state this by citing D3-T3, not by re-describing it.

## Load-bearing language

Named from the live D1 text; not redefined beyond the accepted corpus.

- **confirmed** (E6, E7) — only reviewed-and-confirmed items enter; dropping it admits unconfirmed data.
- **only** (E6, E7, M2) — a closed list / exclusive condition; replacing it with discretionary wording opens the category.
- **scoped sections** (E5) — a subset of the Approved Profile; broadening to "the Profile" leaks every section.
- **user-initiated** (M2, E9) — the user starts it; no background or automatic processing (Law 1).
- **standing consent** (E6) — a specific W1-D2 consent form, not open-ended permission.
- **section age surfaced / on every use** (E5, E6) — staleness shown at point of use; an honesty requirement.
- **display** (E5) — a read to display, not a processing payload (Profile enters processing only via E6/E7, never as direct Z3 payload).
- **nothing persists outside the room / no output … to any other room** (M2) — the Meditation outward boundary is absolute (Law 9).
- **Same conditions as E6** (E7) — a **reference**, preserved as such, never expanded.

## Alternatives considered

- **Paired form — exact reference (authority) + complete verbatim quotation (legibility) (chosen).** The reference makes staleness and drift detectable (it points at the live map); the quotation puts the exact words in front of implementers. Chosen because it satisfies both the anti-drift requirement and the pack's insistence that implementers need the words present.
- **Reviewed paraphrase (rejected).** Allowing a "carefully reviewed" restatement. Rejected: the failure mode is precisely the plausible paraphrase — a reviewer approves friendly wording that has quietly moved a boundary.
- **Reference-only as the rule (rejected).** Contracts cite D1 by ID with no quotation. Rejected: implementers under delivery pressure need the words in front of them; a bare citation invites reconstruction from memory — reintroducing paraphrase.
- **Quotation-only (rejected as the normal form).** Verbatim text with no controlling reference. Rejected: a quotation with no citation cannot be checked for staleness after a D1 amendment; it can silently go out of date.

## Consequences

- **Easier:** every contract's Read/Write Scope section has one mechanical form to follow; a reviewer compares the quotation against the cited D1 clause and passes or fails on an exact match.
- **Easier (drift detection):** because the authority is a live reference, a D1 amendment makes every stale contract quotation detectably wrong at its next review.
- **Harder (deliberately):** no contract may "improve," shorten, or modernise a scope; an inapplicable-looking qualifier must still be carried; a friendlier wording fails review.
- **Constrains future work:** scope changes must be W1-D1 amendments first; contracts follow, never lead; the planning pack and runway are never scope authority.
- **Preserved honesty:** the record documents that even the project's own planning summaries drifted from D1 (see Source-fidelity finding), and fixes the class of error rather than the instances.

### Source-fidelity finding

Direct reading of the live W1-D1 during this record's preparation exposed **wording drift in the W4 pack and runway summaries.** For the record:

- **W1-D1 wins.** It is the sole scope authority.
- **The pack and the runway are planning materials, not scope authority.** Their summaries must **not** be copied into room contracts.
- **D1 must not be altered to match the summaries.**
- **No pack or runway amendment is authorised by this record.**
- **Future contracts cite and quote D1 directly.**

Three concrete discrepancies, preserved as evidence for the fidelity doctrine (not open questions):

1. **Kitchen scope** — summary used *"allergies and confirmed dietary requirements only"*; **D1 uses** *"allergies, confirmed dietary requirements only"* (a comma, not "and").
2. **Kitchen conditions** — summary used *"standing consent with review date"*; **D1 uses** *"Scoped read under standing consent; section age surfaced on every use."*
3. **Wellness scope** — summary used *"scoped display, labels and ages surfaced"*; **D1 uses** *"Approved Profile (scoped sections) → Wellness Room display. With authority labels and section age surfaced."*

## Non-goals

This record does not decide: new edges; new record classes; new consent forms; new grants; adapter mechanics; context assembly; prompt wording; payload schemas; UI presentation; session behaviour; validators; contract implementations; or any W5 or W6 implementation. It builds no adapter, session, prompt, payload, validator, surface, or engine code, and it authorises no medical, therapeutic, diagnostic, crisis, or companion behaviour, contains no real health data, and gives no clinical examples.

## Public-safety considerations

Role-generic, structural wording throughout. No private names, no model names, no private or project lineage. The verbatim D1 scope labels quoted here (e.g. *"allergies, confirmed dietary requirements only"*, *"confirmed injury/physical notes only"*) are **authorised structural source quotations from the sealed map** — reproduced for fidelity, not examples about a real person; no clinical example, diagnosis example, or medical pair is constructed. Where any illustrative example is unavoidable it uses edge IDs, section IDs, or canonical grammar placeholders (Persona-K9, Condition-Q, Allergen-X, Medication-A17). No companion framing except where a sentence names a prohibition. No implementation claims — this record confirms doctrine, it builds nothing.

## Dependencies

W0 (no-new-authority discipline); W1-D1 (the authoritative map — read and write scope source); W1-D2 (consent authorises edges, cannot create them); W1-D3 (D3-T3 label-on-entry); ADR 0003 (ceremony); ADR 0016 (the Read/Write Scope slots this record's rule fills); ADR 0017 (the complementary architectural-isolation wall); and the W4 runway (W4-AR). All landed and resolvable. This record does **not** depend on W5 or W6.

## Open questions

None at acceptance.

---

*The map already wrote the words. A contract's only lawful move is to carry them unchanged — cited for authority, quoted for legibility, never re-said — because the friendliest paraphrase is exactly where a boundary quietly moves.*
