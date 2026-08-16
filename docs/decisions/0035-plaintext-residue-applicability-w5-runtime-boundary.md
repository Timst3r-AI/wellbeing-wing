# 0035 — Plaintext Residue Applicability at the W5 Runtime Boundary

**Status:** Accepted by human reviewer, 2026-08-17. Not a build instruction. Authorises no implementation.
**Date:** August 2026 · **Phase:** W5 — Runtime Enforcement and Behavioural Evaluation · **Deliverable:** none — a governed applicability/finding record on the ADR-0025/ADR-0027 gate-record precedent. **It creates no planning slot, no W5-D2 milestone identity, and no runtime authority.**
**Decision mode:** a short finding record — the applicability check ADR-0024 open question 6 requires, completed and recorded after the W5-D1 doctrine set and before any W5-D2 implementation.
**Constitutional references:** W0 Laws 1, 4, 11, 13. **No law is amended.**
**Resolves:** none. ADR-0024 open question 6 is a body-level open question, not a registered identifier; this record **clears it in body** (decision 16) and claims nothing in the registry `resolves` field. **To be confirmed at landing-scope time.**

---

**ADR-0004 was written in July for a Wing that could decrypt and store. W5 is about to build the first thing that can decrypt and *speak*. This record asks the only question that gate allows — does the residue law reach the new room? — and writes the answer down where an implementer cannot lose it: it reaches, the one tenant it never met is dispositioned, and the recipient side stays exactly as honest as the corpus has always said it must be.**

## Decision question

**Does ADR-0004's plaintext-residue doctrine reach the Wing-controlled side of the transient Z3 processing boundary that W5-D2 will implement — and what, exactly, does W5-D2 inherit from it?**

## Controlling law

- **ADR-0004**, whole — the six decisions; the testing requirements (*"create synthetic content, run the operation, terminate (normally and by kill), then verify no readable governed content exists outside the encrypted stores"*); the non-goal that it *"does not govern Z3 vendor-side retention (OR-2 territory)"*; and its own tax rule: *"Every W3 feature pays a small residue-test tax; that tax is the feature."*
- **ADR-0024** — decision 8 (no processing-state continuity: *"caches, handles, summaries, embeddings, conversational or context state"*); decision 10 (*"no processing-side state survives a processing context"*, carrying W1-D1 §3); decision 13 (persisted-state absence *"demonstrated, not presumed"*); decision 20 (content-free ledger); **open question 6 — the assignment this record discharges**, in its own terms: *"a W5-D1 doctrine and applicability check, which must complete before any W5-D2 implementation. A brief is not doctrine and may not settle it."*
- **ADR-0033** — decision 11 (every physical model artefact behind its own Tier F crossing) and decision 47 (the check *"handled as its own pre-W5-D2 gate or separate governed record after the W5-D1 doctrine set is complete"*).
- **ADR-0034 B6** — the governed evaluation-record artefact class, created doctrinally, mechanics at W5-D4.
- **ADR-0030** — the *operation* vocabulary (single-task means *"the one declared operation for the one declared purpose, ending when that operation ends — whether it completes, fails, or is abandoned"*). **ADR-0031 decision 25 / ADR-0032 B3** — the last controllable point, beyond which the Wing makes no claim. **ADR-0032 B6** — telemetry and logging as governed disclosure surfaces.
- **W1-D1** — §1 (Z1/Z3), §3 (transient processing payloads *"exist only for a grant's duration; never persisted by the processing side; retention prohibited"*), §6 (plaintext in exactly two places). **W1-D2 §0.3** — rights are not grants. **W1-D5** — D5-T01 and the honest-residual register. **ADR-0001** — no background processing; audit never contains health content. **W5-AR §3, §5.2** — the W5-D2 assignment and the directory/dependency fences.

## Decision

### Applicability

1. **Finding: ADR-0004 substantially reaches the Wing-controlled side of the transient Z3 boundary, and W5-D2 implements under it.** This is the finding ADR-0024 open question 6 requires, recorded as such through ceremony. No extension record is needed; one new holder class is dispositioned at decision 8.

2. **ADR-0004 decision 1 — default-deny persistence — binds the boundary in full.** A local-class processing context runs on the user's own device, physically inside Z1; every Wing-written artefact of a Z3 operation — payload buffers, adapter working state, temporary copies — is *"any form, any location"* material, and none of it persists beyond the end of the task that decrypted it. This composes with, and is independently required by, ADR-0024 decision 10 and W1-D1 §3.

3. **ADR-0004 decision 2 — plaintext-free logs at all times — binds every W5-D2 component**: adapter, assembler, transmission path, refusal machinery, and all diagnostics, in every build configuration, debug included — *"a debug flag is not a grant."* It is congruent with, never weakened by, ADR-0032 B6's telemetry discipline and ADR-0024 decision 20's content-free ledger.

4. **ADR-0004 decision 3 — the forbidden artefact classes — binds at the boundary**, and its *content caches* item and ADR-0024 decision 8's forbidden continuity list prohibit the same object from two directions: what may not persist as residue may not survive as reuse. Neither rule narrows the other.

5. **ADR-0004 decision 6 is carried unchanged: user-initiated copies are rights, not residue** (W1-D2 §0.3). The policy governs what the Wing leaves behind, never what the user takes.

### The recipient-side boundary

6. **ADR-0004 does not govern Z3 vendor-side retention, by its own stated non-goal — and that is congruence, not a gap.** The recipient side of any crossing is governed by **disclosure honesty, not residue policy**: OR-2 is carried unsoftened, the Wing makes no claim past the last controllable point (ADR-0031 decision 25; ADR-0032 B3), and no hosted class exists to make claims about (ADR-0033).

7. **No softening, ever:** nothing in this record, and nothing W5-D2 builds under it, may claim residue control beyond the last controllable point, describe vendor-side behaviour as governed by this policy, or present the recipient-side exclusion as a defect to be engineered away.

### The new holder class — local model process memory

8. **A local model process's working memory is dispositioned as an ADR-0004 decision-5 class**: platform- and runtime-contingent residue the Wing does not fully control — **mitigated where the platform or runtime offers mitigation · honestly documented in the threat model's own terms · never denied · and never used to claim total residue control.** ADR-0004 predates any model concept; this disposition extends its decision-5 register to the one holder it never met, changing no other clause.

9. **Any model runtime remains behind its own Tier F dependency crossing under ADR-0033 decision 11**, and each such crossing carries its own residue story — the decision-8 disposition applied to the concrete runtime — at its own authorisation. Nothing here selects, installs, configures or contacts any model runtime.

### Task, context, and operation

10. **The three governing terms compose without conflict, and the mapping is recorded so no implementer maps them by intuition:** ADR-0004's **task** (a user-initiated operation, ending at completion or cancellation — *"not session end, not app close"*) · ADR-0024's **processing context** (grant-created, ending by completion, expiry, or revocation) · ADR-0030's **operation** (the one declared operation of one grant, ending when it completes, fails, or is abandoned). **A processing context is grant-bounded within a user-initiated task; whenever any governing end condition occurs — completion, cancellation, failure, abandonment, expiry, or revocation — the residue obligations attach at that moment.**

11. **No new vocabulary is minted.** Each record's term keeps its own meaning in its own scope; W5-D2 uses the governing records' vocabulary; **"session" remains deliberately non-controlling** (ADR-0024 decision 3), and runtime code that reintroduces session-scoped content lifetime is out of doctrine on its face.

### Evaluation artefacts — the recorded non-conflict

12. **ADR-0034 is the decision-4-shaped record for evaluation artefacts.** ADR-0004 decision 4 requires any persistent derived artefact to arrive by its own decision record with its own residue story; the evaluation-record class is exactly that — created doctrinally by ADR-0034 B6, synthetic-only, with encryption, home and retention mechanics assigned to W5-D4's own governed landing. **No unrecorded ADR-0004 exception exists, and none is created.** This record creates no evaluation record and does not open W5-D4.

### W5-D2 acceptance conditions

13. **W5-D2 inherits ADR-0004's residue-test obligations as acceptance conditions.** For **every boundary operation that transiently holds governed plaintext** — payload assembly, context creation and context end, crossing attempt, and abort — the residue test class applies in ADR-0004's own form: **create synthetic content · run the operation · terminate normally and by kill · sweep app-writable locations and assert no readable governed content outside the encrypted stores.**

14. **Abort and crash-path behaviour is documented, not assumed**: an induced failure mid-operation leaves no content in artefacts the Wing controls, platform dump behaviour is documented, and — per ADR-0004's public-safety rule — **residue test failure output reports location and category only, never the content it found.** Log assertions run on every build configuration.

15. **The residue-test tax binds every W5-D2 milestone: a boundary feature without its residue tests does not merge.** The tax is the feature, at the new boundary exactly as at the old. **No test is created or edited by this record.**

### Effect of this record

16. **This record clears ADR-0024 open question 6 for W5-D2.** The applicability check is complete and its finding is recorded through ceremony, as that question's own terms require.

17. **It authorises no implementation.** No runtime directory, no code, no dependency, no test, no model contact, and no runtime authority of any kind arises from it. **W5-D2 milestone-brief drafting may proceed after this record's acceptance; W5-D2 implementation still requires its own accepted brief, its own Tier F crossings, and its own ceremony — this record starts none of it.**

18. **Nothing unrelated is resolved.** W0 Open Question 2 (revocation cascade) remains open with its trigger-bound deadline; the pending ledger is untouched and no test is converted; no model contact is opened; W5-D3 and W5-D4 are not opened; and no fixture changes status.

## Alternatives considered

- **Recording the finding (chosen).** Both branches of ADR-0024 open question 6 end in a governed record; the analysis shows the reach is substantial, so the record is a finding, not an extension.
- **An ADR-0004 amendment or extension record (rejected as unnecessary).** Every ADR-0004 clause reaches unmodified; the one new holder class fits the decision-5 register ADR-0004 already built for exactly this shape of residual. Amending an accepted W3 record to say what it already says would be churn dressed as rigour.
- **Settling the check inside the W5-D2 brief (rejected, foreclosed).** ADR-0024's own words: *"a brief is not doctrine and may not settle it."*
- **Treating the vendor-side exclusion as a gap to close (rejected firmly).** It is the corpus's design: disclosure honesty, not technical control, past the last controllable point. Closing it would require claims the Wing cannot support — the exact failure ADR-0032 decision 13 bars.
- **Deferring the model-memory disposition to the first Tier F crossing (rejected).** The crossing carries the concrete story, but the class disposition is doctrine, and leaving it undecided would hand a governance question to a dependency authorisation.

## Consequences

- **The W5-D2 gate is discharged**: ADR-0024 open question 6 closes, and milestone-brief drafting may lawfully begin once this record is accepted.
- **Every W5-D2 milestone inherits a pre-written residue obligation** — the same tax W3 paid, at the new boundary, with the abort and crash paths named.
- **The honest residual grows by one named member**: local model process memory joins OS swap and platform caches in the documented-never-denied register, and no future artefact may describe residue control as total.
- **No capability is authorised.** Nothing here builds, decrypts, contacts, or runs anything.

## Constitutional check

- **Law 1** — nothing here creates background or unattended behaviour; residue obligations attach at task end inside user-initiated operations, and the record contacts no one.
- **Law 4** — minimum necessary is extended in time: content held for an operation ends with the operation, in every form and location the Wing controls.
- **Law 11** — the user's own copies remain rights, not residue; nothing here gates export, erasure, or self-access.
- **Law 13** — logs and ledger stay content-free in every configuration; the audit trail records activity without ever becoming the leak.
- **No new authority.** No edge, zone, class, grant type, vocabulary, planning slot or namespace is minted; no W5-D1 record is amended; ADR-0004 is applied, not changed.
- **No law required reinterpretation, and no amendment is proposed or required.**

## Non-goals

This record does not authorise, decide or design: any W5-D2 implementation or milestone brief content · a runtime directory · a software or package dependency · model implementation, contact, provider, binary, API, SDK or client · a credential · a prompt, system prompt or output parser · a schema, table, storage or event-store design · telemetry implementation · a test creation or edit · fixture execution · observation-record materialisation · a pending-ledger change or test conversion · behavioural proof · W5-D3 or W5-D4 execution · Lane C · W6 · E10 activation · Z4 discharge · a VendorAdapter ADR · E12/Z5 activation · or **medical, therapeutic, diagnostic, crisis, or companion behaviour of any kind**. It amends no record. It contains no real health data and no clinical examples.

## Public-safety considerations

Generic and structural wording throughout — task, operation, context, boundary, residue, artefact, store, log, sweep. No model or vendor is named and none is contacted. No real health data appears anywhere, and the record's own testing language preserves ADR-0004's rule that residue findings report location and category, never content. No named drug, diagnosis or allergen; no clinical example; no statement about any person; no private names, no URLs.

## Dependencies

**Proposed, and marked for landing-time verification — each to be resolved individually against the live registry, never assumed:**

`W0` · `W1-D1` · `W1-D2` · `W1-D5` · `ADR-0001` · `ADR-0003` · `ADR-0004` · `ADR-0024` · `ADR-0030` · `ADR-0031` · `ADR-0032` · `ADR-0033` · `ADR-0034` · `W5-AR`

**`ADR-0004` is direct and required** — the record's whole subject. **`ADR-0024` is direct and required** — open question 6 is the assignment, and decisions 8/10/13/20 are relied on in terms. **`ADR-0030` is direct** for the operation vocabulary of decision 10. **`ADR-0031` and `ADR-0032` are direct** — the last controllable point and the telemetry discipline are cited as controlling law in decisions 6–7 and 3. **`ADR-0033` is direct** — decision 9's Tier F boundary and decision 47's gate assignment. **`ADR-0034` is direct** — decision 12's non-conflict rests on its B6 class. **`ADR-0001` is direct** — the plaintext-zone root and no-background rule. **`W1-D1` is direct** (§1, §3, §6 quoted); **`W1-D2` is direct** (§0.3 rights-not-residue); **`W1-D5` is direct** (D5-T01 and the honest-residual register decision 8 writes into). **`ADR-0003` is direct** as operative Tier J ceremony authority. **Deliberately excluded:** ADR-0005 through ADR-0023, W1-D3, W1-D6, W2-D4, W4-D6-BEF, and the room contracts — each reaches this record, if at all, transitively, and `depends_on` is direct authority, never lineage.

## Open boundaries and later ownership

1. **The concrete residue story of any model runtime** — the Tier F crossing that proposes it, under decision 9.
2. **Memory-locking and platform-mitigation evidence** — ADR-0004's own open questions 1–2, unchanged; implementation evidence at W5-D2, documented honestly.
3. **Evaluation-record encryption, home and retention mechanics** — **W5-D4**, within ADR-0034 B6.
4. **The revocation-cascade record (W0 OQ 2)** — its own future record, trigger-bound before the first derived artefact under a grant.
5. **The anticipated search-index exception** — ADR-0004's decision 4, unbuilt and unowned, exactly as it was.

---

*The oldest kind of gate in this repository is a short record that says what an older record already meant, in a place the next builder cannot miss. ADR-0004 spent thirteen months being right about a boundary that did not exist yet. This record's only work is to say so in ink — and to hand W5-D2 the tax bill that comes with the compliment.*
