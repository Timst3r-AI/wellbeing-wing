# 0036 — Revocation Cascade for Derived Artefacts

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** none — the required-with-trigger record W5-AR §4 names, accepted **before the first W5 capability produces a derived artefact under a grant**, and the accepted W5-D2 milestone brief's explicit gate: **W5-D2-M05 does not materialise or land without this record.** It creates no planning slot and no milestone identity.
**Decision mode:** one governed record in three parts — **Part A: Invalidation events and the artefact taxonomy** · **Part B: The five dispositions and their assignment** · **Part C: Runtime consequence and boundaries.**
**Constitutional references:** W0 Laws 1, 3, 4, 5, 8, 10, 11, 13. **No law is amended.**
**Resolves:** **W0 Open Question 2** — *"Consent revocation cascade. When consent is revoked, what happens to derived context created under that consent? Options: flag for review, quarantine, or cascade-delete."* Registry `resolves: ["W0-OQ-2"]`, on the ADR-0001/0002/0024 precedent.

---

**Revocation has been terminal since W1: no future access, no new disclosure, no new derived outputs, the audit record remaining. What W1 deferred — deliberately, twice — was the fate of what already exists. This record answers it with the one rule the whole corpus has been converging on: the Wing may stop things, mark things, and hold things for the person to decide — but it never quietly deletes what a person may need, never quietly keeps using what a person withdrew, and never, under any pressure, edits history.**

## Decision question

**When a grant is revoked, expires, or is otherwise invalidated, what happens to derived artefacts, downstream references, cached views, boundary-held material, payload candidates, context products, logs, observations, and any later W5 runtime artefact that depended on that grant?**

## Controlling law

- **W0 Open Question 2**, verbatim above, with its three named options.
- **W1-D2 §5** — the five immediate effects, preserved in full and unaltered: no future access · no further processing disclosure events, in-flight events aborting where technically severable · no new derived outputs · **the audit record remains** · existing derived artefacts *"flagged for user review — visibly marked as derived under revoked consent"*, their final disposition *"governed by the later revocation cascade decision"*, acquiring **no new uses in the interim**. **This is that decision.**
- **W1-D2 §0.3 / W0 Law 11** — rights are not grants: the user's own records, exports, erasure and ledger view are never consent-gated and never revoked by the system.
- **ADR-0030 A6** — revocation is terminal and is a right, not a request; a revoked grant never reactivates; **the cascade was expressly not decided there.** ADR-0030 A4 — lawful succession is continued permission, not invalidation.
- **ADR-0004** — residue doctrine: default-deny persistence for Wing-held working material; **decision 6: user-initiated copies are rights, not residue.** **ADR-0035** — its applicability at the W5 runtime boundary, with the full residue tax on boundary operations.
- **ADR-0015** — the ledger is **append-only; history is never rewritten, reordered, or compacted; erasure is the user's explicit, knowing act — only**, and erasing an item never silently erases its governance history.
- **ADR-0024** — decisions 10–11: no processing-side state survives a context; revocation is expressible at the boundary, in-flight events aborting where severable, with non-severability recorded honestly, never described as an abort.
- **ADR-0032** — decisions 36–38: a crossing that occurred is recorded honestly and never claimed undone; **revocation stops future use; it does not reach backwards through a boundary the Wing does not control.** Decision 13's barred comfort claims. **ADR-0033 / W1-D5 OR-2** — no vendor path exists; nothing here claims vendor-side deletion, ever.
- **W5-AR §4** — the trigger: this record accepted before the first derived artefact under a grant; **the accepted W5-D2 brief fixes the deadline at before W5-D2-M05.**

---

# Part A — Invalidation events and the artefact taxonomy

## A1. What invalidates

1. **The invalidation events are exactly two: revocation and expiry of the authorising grant.** Ordinary completion is not invalidation — a grant that ran its course leaves its lawful outputs exactly where authorised edges put them. A declined grant produced nothing to cascade.

2. **Revocation and expiry are distinguished and never conflated.** Revocation is the person's terminal act — immediate, unconditional, requiring no justification. Expiry is time's act under the governed duration. **Their forward consequences are identical** — no new use, no new derivation, no new disclosure under that grant — **and their marks differ**: *derived under revoked consent* versus *derived under expired grant*. Neither mark is punitive, and neither event deletes anything by itself.

3. **Lawful succession is not invalidation.** A successor grant (ADR-0030 A4) is continued permission: artefacts derived under the predecessor are unaffected by the succession itself, keep their provenance to the predecessor's identity, and meet these rules only when their own governing grant lineage ends in revocation or expiry without succession.

## A2. The artefact taxonomy — every affected thing is exactly one of five kinds

4. **Source records are never cascade targets.** The grant governed *access* to a source, not the source's existence. A vault record outlives every grant ever issued over it, untouched.

5. **User-owned material is rights territory and the cascade never reaches it:** the user's own records, their exports and copies, and **any artefact whose chain includes the user's explicit review-and-adoption act** (the E4-class approval that made draft content the user's own working context). **Revocation is forward-looking and does not reach backwards through a completed user act** — un-approving is the user's own separate act, never the system's inference from a revocation.

6. **Wing-controlled derived artefacts** — extractions pending review, prepared summaries and question lists, cached or derived views, and any W5 runtime product that landed through an authorised edge **without** a subsequent user adoption act — **are the cascade's targets.**

7. **Boundary-held material is residue, not artefact:** in-context holdings, payload candidates, and any pre-output material that never left through an authorised edge **never became an artefact at all.** It is governed by the residue doctrine, not by this taxonomy.

8. **Content-free governance records** — ledger events, marks, fingerprints, lineage references — **are permanent** (Law 13; ADR-0015) and are the machinery by which everything above stays honest.

# Part B — The five dispositions and their assignment

## B1. The dispositions, defined and exhaustive

9. **Purge** — immediate destruction of Wing-held transient material, under the residue discipline's proofs. **Invalidate** — permanently barred from every future use: never again an input, a context payload, a derivation basis, or a disclosure candidate; the bar is machine-enforced and the mark is load-bearing. **Quarantine** — held visibly, unusable, surfaced to the user as an internal flag at next relevant use for the user's own decision. **Retain-by-reference** — content-free lineage and audit references remain so accountability survives the artefact. **Audit-only** — the C0 event trail, permanent and append-only.

## B2. The assignment, on any invalidation event

10. **Boundary-held material is purged immediately.** Any live context under the grant ends (ADR-0024 d11), in-flight events abort where technically severable with non-severability recorded honestly, and the residue sweep discipline applies on every termination path, including abort, crash, and kill.

11. **Wing-controlled derived artefacts are invalidated and quarantined, never silently deleted and never silently retained as usable.** Each carries its mark (decision 2) and **acquires no new uses** — W1-D2 §5.5's interim rule is hereby made the standing rule.

12. **The user decides the final disposition of each quarantined artefact** (Law 5: agents prepare, the user decides): **keep**, by an explicit adoption act that re-homes it as the user's own record (rights territory thereafter); or **delete**, by the user's erasure right. **The Wing never cascade-deletes on its own initiative** — automatic deletion would make the Wing the decider and could destroy material the person needs, including material whose absence is itself a safety hazard.

13. **User-owned material is untouched. Source records are untouched. Governance records are retained forever, content-free.** No disposition in this record deletes a user's record, edits history, or re-dates anything.

14. **Silent re-use is the named failure this record exists to prevent.** An invalidated artefact entering any context, payload, derivation, or crossing is **refused structurally** — the same unconstructable-shaped refusal every runtime door already uses — and the mark travels with every reference to the artefact so the refusal is reachable wherever the artefact is.

15. **No re-derivation laundering.** Deriving a new artefact *from* an invalidated one is a new use and is refused. The lawful path to equivalent content is a new grant over the source and a fresh derivation under it.

16. **Quarantine surfaces without pushing.** Flags are internal, surfaced at next relevant use, batched against review fatigue (Law 1; D5-T20's queue discipline) — never outreach, never urgency theatre, never a notification.

17. **Interrupted invalidation completes at next relevant use, never in the background.** Marking happens synchronously within the user-initiated revocation or the expiry-consuming operation; if a crash interrupts it, completion occurs within the next user-initiated operation that touches the grant's record — no background process, no scheduler, no unattended act (Law 1).

18. **Vendor-side material is beyond the cascade, and the record says so plainly.** Revocation halts future disclosures; past crossings remain honestly recorded; **no claim of vendor-side deletion, retrieval, or control is ever made** (OR-2; ADR-0032's barred claims). The cascade governs what the Wing holds, exactly as the residue policy governs what the Wing leaves.

## B3. The timing summary, in one place

19. **Immediate:** the no-new-use bar · in-flight abort where severable · boundary purge. **Swept:** every residue path, including abort, crash and kill, under the ADR-0035 tax. **Marked:** invalidation and quarantine marks on Wing-controlled derived artefacts, completing at next relevant use if interrupted. **Permanent:** the audit trail, lineage references, and disclosure history. **Never:** silent re-use · silent deletion of anything user-owned · any rewriting of history.

# Part C — Runtime consequence and boundaries

## C1. Obligations this record hands to the implementing milestones

20. **W5-D2-M05 and later milestones inherit, as deterministic proof obligations:** payload assembly refuses invalidated inputs · derived-artefact production records grant lineage at creation, so the cascade can always find its targets · the invalidation and quarantine marks are C0 governance metadata carrying no content · no code path deletes user-owned material · no code path re-uses an invalidated artefact · boundary purge on every termination path (already proven at W5-D2-M04 for context holdings, extended per milestone under the registered residue operations).

21. **This record authorises no implementation.** No assembler, no marker store, no quarantine surface, no code of any kind arises from it; W5-D2-M05 still requires its own pipeline authorisation and lands through its own gates.

## C2. What this record closes and what it leaves

22. **W0 Open Question 2 is resolved**, and W1-D2 §5.5's deferral is discharged — with W1-D2 itself unamended: its five immediate effects stand in full, and its interim no-new-uses rule is promoted, not replaced.

23. **Erasure remains the user's right on ADR-0015's terms** (whole-ledger in v1; scoped erasure a future mechanic), and nothing in this record adds any retention that resists the user's explicit erasure.

24. **Quarantine-surfacing wording, layout and any review surface are W6's.** The disposition machinery's schema, storage and marks' representation are W5-D2's, within these meanings. Multi-device and sync implications remain with the future records that own those capabilities.

---

## Alternatives considered

- **Automatic cascade-delete (rejected).** It makes the Wing the decider (Law 5 inverted), destroys material a person may need — including safety-relevant material whose silent absence is its own hazard — and converts a consent act into a data-loss event nobody chose.
- **Retain-as-usable (rejected firmly).** Permission would outlive the consent that created it — the precise failure the grant machinery exists to prevent.
- **Invalidate-and-quarantine with the user deciding (chosen).** It is W1-D2 §5.5's own trajectory made final: the Wing stops, marks, holds, and asks; the person decides.
- **Reaching back through completed user approvals (rejected).** Revocation is forward-looking; an approval was the user's own act, and only the user's own act un-does it.
- **Claiming vendor-side deletion (rejected).** OR-2 territory; every such claim is barred by name in accepted doctrine.
- **Deferring crash-path marking to a background completion job (rejected).** Law 1 admits no background act; next-relevant-use completion is the lawful shape.

## Consequences

- **W5-D2-M05 is unblocked at this record's publication and remote verification** — the payload milestone may now be authorised, inheriting decision 20's proof obligations.
- **Every future derived artefact is born findable** (lineage at creation) and **every invalidated one is born refusable** (the mark is load-bearing).
- **Harder, deliberately:** the Wing will sometimes hold a quarantined artefact the user never gets around to deciding about. It stays quarantined, visible, and unusable — honest limbo, not silent disposal.
- **No capability is authorised.** Nothing here builds, deletes, marks, surfaces, or contacts anything.

## Constitutional check

- **Law 1** — no push, no background completion; flags surface at next relevant use, batched.
- **Law 3** — nothing self-promotes: invalidation only lowers usability; no mark raises authority anywhere.
- **Law 4** — no new access arises; the cascade only narrows what may be touched.
- **Law 5** — agents prepare, the user decides: disposition of every quarantined artefact is the person's call.
- **Law 8** — cascade marks are C0 with no processing edges; the pattern of revocations never becomes an inference signal.
- **Law 10** — revocation is made meaningful to the end of the chain: scoped, explicit, revocable consent now has a governed afterlife.
- **Law 11** — rights untouched throughout: user records never deleted by the Wing, erasure supreme, export and self-access never gated.
- **Law 13** — the audit record remains, permanently, content-free, append-only.
- **No new authority.** No edge, zone, class, grant type, mark-as-authority, or namespace is minted; one registered open question is resolved and nothing else changes standing.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: any implementation · W5-D2-M05 or any milestone content · a payload assembler or payload-equality code · a processing-context extension · transmission or crossing · a marker store, schema, table or storage mechanism · deletion tooling · quarantine surfaces, wording or UI · scoped ledger erasure · any vendor-side claim · a notification or reminder path · model contact · harness work or fixture execution · a pending-ledger change or test conversion · behavioural proof · Lane C · W6 · E10 activation · Z4 discharge · a VendorAdapter ADR · E12/Z5 activation · or **medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind**. It amends no record. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording throughout — grant, artefact, mark, quarantine, ledger, boundary, user, Wing. No vendor or model is named and none is contacted. No real health data appears; no named drug, diagnosis or allergen; no clinical example; no statement about any person. The one safety-shaped argument made — that silent deletion of derived material can itself be hazardous — is stated about system design, never about any person. No private names, no URLs.

## Dependencies

**Proposed, and marked for landing-time verification — each resolved individually against the live registry, never assumed:**

`W0` · `W1-D2` · `W1-D5` · `ADR-0003` · `ADR-0004` · `ADR-0015` · `ADR-0024` · `ADR-0030` · `ADR-0031` · `ADR-0032` · `ADR-0033` · `ADR-0035` · `W5-AR`

**`W1-D2` is direct and required** — §5 and §5.5 are the deferral this record discharges, and §0.3 the rights boundary. **`ADR-0015` is direct** — append-only history and user-only erasure are relied on in terms. **`ADR-0004` and `ADR-0035` are direct** — the residue half of every termination path. **`ADR-0024`, `ADR-0030`, `ADR-0032`, `ADR-0033` are direct** — boundary end, terminal lifecycle, honest-crossing history, and the no-vendor-path posture, each in terms. **`ADR-0031` is direct** — decision 20's refusal obligation lands inside its payload doctrine. **`W1-D5` is direct** — OR-2. **`ADR-0003`** as operative Tier J ceremony authority. **Excluded:** everything else as transitive; `depends_on` is direct authority, never lineage.

## Open boundaries and later ownership

1. **Mark representation, lineage storage, and the refusal implementation** — **W5-D2-M05+**, under decision 20.
2. **Quarantine surfacing wording and any review surface** — **W6**.
3. **Scoped ledger erasure** — ADR-0015's future mechanic, unchanged.
4. **Multi-device propagation of invalidation** — lands with key distribution and sync, if ever.

---

*Three options sat in the constitution for two and a half months: flag, quarantine, or delete. The answer turned out to be the one the corpus had been practising all along — the Wing stops instantly, remembers permanently, holds visibly, and hands the only irreversible decision to the only person entitled to make it.*
