# W4 — Room Contracts

## Phase Runway / Alignment Brief

**Status:** Accepted by human reviewer, 2026-07-10. Not a build instruction.
**Date:** July 2026
**Phase:** W4 — the first jurisdiction phase (the phase after the sealed product spine)
**Governed by:** W0 Constitution; ADRs 0001–0015; the accepted W1 corpus; the sealed W2 corpus and its enforcement machinery; the sealed W3 phase and its six deliverable closure records; the published W3 runway (structural precedent)
**Tier at landing:** J — Judgment (phase runway; full ceremony when landed)

---

**W1 wrote the laws. W2 taught the repo to check them. W3 built the spine that holds evidence, shapes context, and lets the user decide what becomes true. W4 draws the walls: four rooms, each a jurisdiction with a written contract — what it may read, what it may write, what it must never infer, and how it stays honest when the ground is unknown. No adapter is opened, no model is contacted, no surface is shipped. W4 writes the law the rooms will later be held to.**

## 1. W3 closure dependency

W3 — Health Vault and Health Profile Foundations — is **complete and closed**, sealed at published head `ee65f4399a35410dd6cdc4aaa1774022c4c8e50d` (W3 closure record accepted 2026-07-06). W4 therefore begins, as W3 did, with working gates rather than promises — and it inherits **W0–W3 whole**:

- the **engine spine is complete and sealed**: it holds without reading, belongs without escrow, shapes without inventing, moves without self-promoting, remembers without leaking, travels without telling, and gives back without gatekeeping — every behaviour doctrine before it was code, every promise carrying a standing test;
- the **W2 enforcement machinery** is active on every landing: the registry (37 entries) indexes every governance document and is test-asserted on every run; the checklist and ADR 0003 ceremony tiers govern every landing; the public-safety scan runs in landing mode over every enumerated file before first commit and in normal mode after; the synthetic fixtures and deterministic suite (218 tests — 209 passed, 9 skipped, 0 failures) stay green through every commit, and the suite's directory- and dependency-fence tests are **amended, by record, to admit exactly what W4 authorises, and nothing else**;
- the three exact dependency pins are unchanged since the first line of product code; any change remains a Tier F fence.

**W4 does not reopen W0–W3.** The laws, the map, the enforcement layer, and the spine are settled history; W4 stands on them and adds the jurisdiction layer above them. Where W4 needs a scope, it cites the sealed map — it never re-decides it.

## 2. W4 north star

**W4 is the room-contract phase.** Its purpose is to make four rooms into **enforceable jurisdictions** — each governed by a written contract that a future adapter or surface must obey before the room can lawfully act:

- **Wellness Room**
- **Kitchen**
- **Gym**
- **Meditation Room**

A room contract states, for exactly one room: **what it may read** (its granted D1 edge, restated verbatim or by reference); **what it may write** (its own records only, at their D1 classes, labelled on entry per D3-T3); **what it must never infer** (the general Law 8 rule plus the room's named-bait list, each bait bound to a future eval fixture); **how it behaves when relied-on context is unknown, stale, expired, or contradicted** (one shared behaviour standard, instantiated in room wording); and **what validators can later check** mechanically versus what stays review-only. Rooms are separate jurisdictions; there are four contracts written against one skeleton, never one combined rooms document.

**W4 does not open adapters, prompts, model payloads, review surfaces, UI, CLI, hosted sync, profile export, whole-vault plaintext export, medical/therapeutic/diagnostic/crisis behaviour, or companion behaviour.** The Wing's differentiation remains its restraint: W4's output is contracts that constrain what any later capability is permitted to do — not a capability. Anything a model might one day do arrives through the adapter phase's own gates, none of which W4 opens.

## 3. Proposed W4 deliverable sequence

Execution order may resequence where dependencies allow (the W2-D6-before-D5 and W3 resequencing precedents stand; **IDs stay stable**). The proposed sequence:

| ID | Deliverable | Shape |
| :---- | :---- | :---- |
| **W4-D1** | Room-contract doctrine decision records | The six accepted doctrine candidates (DR-W4-01 … DR-W4-06) land as individual briefs through full ADR ceremony — the template, isolation model, scope confirmation, cross-room inference standard, unknown/stale/contradicted standard, and validator requirements — each accepted before the contracts or validators it gates |
| **W4-D2** | Wellness Room contract | The ten-section contract (eleven with open-questions) written against the accepted template; reads E5 (scoped display, labels and ages), writes own records; named-bait list = aggregation of self-reported records toward diagnosis |
| **W4-D3** | Kitchen contract | Same skeleton; reads E6 (*allergies, confirmed dietary requirements only*, standing consent with review date); named-bait list = conditions inferred from food patterns |
| **W4-D4** | Gym contract | Same skeleton; reads E7 (*confirmed injury/physical notes only*, same conditions as E6); named-bait list = injury inferred from activity data |
| **W4-D5** | Meditation Room contract | Same skeleton, structurally different instantiation; reads **nothing from any other home** (M1–M2 are its complete edge list); named-bait list = any outward-facing signal whatsoever, in any direction |
| **W4-D6** | Contract validator requirements / validator plan | DR-W4-06 operationalised: the decidability-drawn line made concrete as a validator plan; the mechanically-checkable validators specified and (per the DR-W4-06 gate) **built only after all four contracts are accepted** |
| **W4-D7** | W4 closure record | Closure: criteria assessment against this runway, suite extended and green, pending-ledger review, incident log, and the W5 gate named without pre-deciding it |

**Sequencing option (reported, not silently substituted):** DR-W4-06 (the *doctrine record*, landing in W4-D1) and W4-D6 (the *validator plan/build deliverable*) share a number but are two different things — the record decides the decidability line; the deliverable specifies and later builds the validators. Because DR-W4-06's own gate holds that validators "land only after all four contracts are accepted," W4-D6's *requirements/plan* can be written any time after DR-W4-06 lands, but its *build* necessarily follows W4-D2…D5. A cleaner framing some may prefer: keep W4-D6 as the validator **plan** (buildable early) and treat the validator **implementation** as a bounded milestone inside W4-D6 gated on the four contracts — same IDs, the gate made explicit. Flagged to avoid the W1-D3-vs-W3-D3 naming trap: *DR-W4-0n* (doctrine record) and *W4-Dn* (deliverable) are distinct namespaces; spell them out.

## 4. Required decision records before implementation

No W4 contract or validator code lands until these are accepted; **reviewed drafts already exist for all six** in the planning corpus (the W4 room-contracts doctrine pack), and the architect and human reviewer have ruled each acceptable as a runway candidate with the sub-rulings folded below. Each still lands through full ceremony as its own decision record before the artifact it gates.

1. **DR-W4-01 — Room Contract Template.** The fixed ten-section skeleton, every section filled ("not applicable" written with its reason, never blank). *Ruling folded:* **yes** to the optional eleventh "open questions" section per contract.
2. **DR-W4-02 — Room Isolation Model.** *Ruling folded:* room separation is **architectural, not policy** — each room's model interactions occur in a context that has never contained another room's content, unreachable rather than merely forbidden. The two open questions — the display-vs-processing context split, and per-room context-cost evidence — are **carried to W5** (the adapter era), not resolved in W4.
3. **DR-W4-03 — Read/Write Scope Confirmation.** *Ruling folded:* the **D1 room scopes remain source of truth**; contracts restate scope **verbatim or by reference, never by paraphrase** (the plausible paraphrase is precisely the failure mode). Load-bearing words (*confirmed*, *only*, *scoped sections*, *user-initiated*) are named as load-bearing; blur-words are banned within scope sections; scope changes are D1 amendments first.
4. **DR-W4-04 — Cross-Room Inference Prohibition Standard.** Violation is defined by observable consequence — deriving a health-relevant conclusion beyond granted context **and then doing anything with it**, silent action the primary target. *Rulings folded:* user-requested speculation **inherits the surfacing-doctrine refusal shape**; the record **includes one contract example** showing the correct refusal / safe-response pattern; the **named-bait lists are the highest public-safety surface in W4 drafting**; **canonical placeholder vocabulary only** (Persona-K9, Condition-Q, Allergen-X, Medication-A17) — `Ingredient-X` is normalised out unless it becomes a formally accepted placeholder.
5. **DR-W4-05 — Unknown/Stale/Contradicted Behaviour Standard.** One shared behaviour table, quoted per contract, never re-derived. *Rulings folded:* **hard-block-vs-warn stays open** — W4 must **not** resolve the inherited D3 open question; rule **"always"** for the safety-relevant grace-fraction (the inline uncertainty sentence is not conditioned on a grace threshold for the safety-relevant set); **most-protective framing is surfacing/verbal only and must never manufacture a new claim, restriction, or recommendation**.
6. **DR-W4-06 — Contract Validator Requirements.** *Rulings folded:* accept the **decidability-drawn line** (a term is validated iff its correctness is decidable from repo artifacts without interpretation — a judging validator is doctrine minting by machinery, and is not built); accept the **one-suite recommendation** (validators extend the existing deterministic suite, phase-named tests); the **catalogue-ID validator class is W6-dependent** — until the W6 governed string catalogue exists, the W4 records serve as **review of record** under the established "joins the governed string catalogue when that structure exists" precedent (ADRs 0009 / 0011 / 0012).

## 5. Explicit non-goals

W4 contains none of the following, and this runway authorises none of them:

- **no adapter implementation** — the adapter layer is W5's, untouched;
- **no model contact, no prompts, no model payloads** — prompt-eligibility remains false everywhere;
- **no review surface** — the review/approval surfaces are the surface era's;
- **no governed string catalogue implementation** — the catalogue is a W6 structure; W4 cites it as review-of-record only;
- **no UI, no CLI** — W4 is a doctrine-and-contract layer with no user-facing surface;
- **no hosted mode, no sync** — local-first, local-only; hosted remains its own future gate;
- **no profile export, no whole-vault plaintext export** — each is its own future record;
- **no medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind** — the archive stores, labels, and constrains; it never opines;
- **no realistic clinical examples, no real health data** — anywhere: not in the runway, the records, the contracts, the tests, the fixtures, the logs, or the docs; the synthetic-only discipline holds, grammar placeholders only;
- **no W5 or W6 implementation** — W4 names its forward dependencies (§8) and carries them; it does not build them.

## 6. First app-shape language

What a room contract *is*, in one honest paragraph:

A **room contract is a governed jurisdiction** — a written, testable statement of what one room of the Wing is permitted to read, permitted to write, forbidden to infer, and required to say when the ground is uncertain. It is **not an assistant**: it holds no conversation and makes no recommendation. It is **not a room UI**: nothing in it is a screen a user looks at. It is **not a prompt**: it contacts no model and carries no payload. It is a **contract that future adapters and surfaces must obey before a room can lawfully act at all** — the wall drawn in words and given executable teeth, so that when capability finally arrives, it arrives already bound. Nothing in a room contract makes a claim about the user's health; it defines the shape of restraint each room will be held to. That is the point.

## 7. W4 entry gate

Per checklist rule 8 and the W3 closure record §8, W4 may not start until all three exist and are accepted — the same three-documents-three-acceptances gate that opened and closed the phases before it:

1. the **W3 closure record** — **accepted and published** ✔ (`ee65f43`);
2. **this W4 runway** — *pending review*;
3. the **first W4 deliverable brief** (the first of the six doctrine records, DR-W4-01) — *pending*.

Three documents, three acceptances, no exceptions. **Acceptance of this runway would authorise W4 *briefs* only.** It would **not** authorise scaffolding; it would **not** authorise implementation; it would **not** create any repository artifact. Code and repo artifacts arrive only behind their own briefs and their own tier ceremonies; the first new file the phase lands and any first fence-crossing will each be named and separately authorised when their brief is accepted.

## 8. Public-safety note

This runway contains no private names, no private system references, no companion framing beyond naming a prohibition, no project lineage beyond this repository, no real health data, no clinical examples, and no model names. All wording is generic: user, Wing, room, contract, vault, draft profile, approved profile, human reviewer, architect, model.

**W4 watch item — named explicitly because W4 is where it becomes live:** the **named-bait lists are the highest public-safety surface in W4 drafting**. A bait list written with realistic clinical pairs would itself be a small inference engine in documentation form. Therefore, when the four contracts are drafted (W4-D2 … W4-D5):

- **grammar placeholders only** (Persona-K9, Condition-Q, Allergen-X, Medication-A17);
- **no realistic clinical pairs** — e.g. a food-avoidance pattern is illustrated only as "must never become a Condition-Q inference," never with a real ingredient-to-diagnosis mapping;
- **no private, person, or project lineage**;
- **no companion framing** except where the sentence names the prohibition itself (the prohibition-statement allowlist class, per corpus precedent — each such line authorised individually at landing).

### Forward dependencies (constraints W4 names and carries — not blockers to this runway)

- **W5 adapter layer** enforces DR-W4-02's architectural isolation *later* — each processing grant binds to one room, the session derives from the grant, and no adapter interface accepts content from two rooms. W4 sets the doctrine the W5 adapter must implement; the enforcement mechanism (and the two carried open questions) belong to the adapter era.
- **W6 governed string catalogue** handles catalogue IDs and wording routing *later* — DR-W4-05's room-register wording and DR-W4-06's catalogue-ID validator resolve against it. Until W6 lands, the W4 records are **review of record** for their wording, on the ADR 0009 / 0011 / 0012 precedent.

Neither dependency blocks the W4 runway or the W4 doctrine records. They are the healthy direction — governance before capability: W4 constrains W5 and W6; it does not wait on them.

---

*Three phases proved the Wing can govern itself and built the spine worth governing. W4 draws the first walls — four rooms, four contracts, one skeleton — so that when a model is finally allowed near any of them, the room already knows exactly what it may not do.*
