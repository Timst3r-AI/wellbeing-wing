# W1-D5 — Threat Model

**Status:** Accepted by human reviewer, 2026-06-12 · **Date:** June 2026
**Phase:** W1 — Governance Architecture and Data Boundary Design (deliverable 5 of 6)
**Governed by:** W0 Constitution; ADR 0001; W1-D1; W1-D2; W1-D3; ADR 0002
**Scope:** Documentation only, deliberately adversarial.

---

**A governance model is not proven by what it promises. It is tested by how it fails.**

## 1. Purpose

Every accepted document in this repository makes promises: evidence stays in the Vault, drafts never become truth, consent never inflates authority, staleness is visible, surfacing never coerces, metadata is never mined. D5 attacks those promises before any implementation exists to embody them. Its job is to name how the Wing's governance could fail, be bypassed, be misread, be weakened by future convenience, or be turned against the user — so that what gets built later is built against a named adversary rather than an assumed friend.

## 2. Scope and non-scope

**In scope:** governance failure, privacy leakage, authority inflation, consent bypass, staleness drift, cross-room inference, metadata profiling, unsafe surfacing, AI/vendor overreach, hosted-mode trust erosion, adapter disclosure risk, key custody pressure, wording and UI deception risk, review fatigue, export and audit misuse.

**Out of scope:** implementation, code, schema, UI, packages, encryption mechanics, security tooling, authentication flows, AIAdapter/VendorAdapter implementation, and medical logic. D5 names risks and binds future work; it builds nothing.

**Hard exclusions confirmed:** D5 creates no medical advice, no diagnosis, no treatment recommendation, no crisis tooling, no emergency response logic, no autonomous monitoring, no push-notification rules, no risk-scoring algorithms, no implementation controls, and no security certification claims. A threat model that quietly became a risk engine would itself violate Laws 1, 6, and 8 — the document polices its own scope.

## 3. Protected assets

In descending order of blast radius if compromised:

- **Health Vault content** (C4) — raw clinical evidence; the crown jewels (W0 §11.8)
- **User-held keys** — the trust anchor of the entire architecture (ADR 0001)
- **Key recovery materials**, if any are ever introduced — currently none exist by decision; their *future introduction* is itself a threat (D5-T19)
- **Approved Health Profile** (C3) — active working context; approved context the Wing may rely on within governed scope
- **Draft Health Profile** (C3) — extracted but unconfirmed; sensitive and authority-less
- **Room records** (C1/C2/CM) — inference raw material
- **Consent grants** (C0) — the record of what was delegated
- **Audit logs and C0 governance metadata** — content-free, pattern-rich
- **Authority and staleness labels, contradiction records** — the truth machinery itself; forging these forges trust
- **Safety surfacing metadata** — acknowledgments and proceed-decisions; a map of what a user was warned about
- **AI processing payloads** (transient, Z3) — plaintext in flight under grant
- **Vendor/adapter disclosure payloads** (Z4) — minimum task data crossing to external services
- **User exports** — plaintext by design, outside the Wing's protection once produced

## 4. Trust boundaries

| **Boundary** | **What crosses it** | **Primary risk at this boundary** |
|---|---|---|
| User device / everything else (Z1 edge) | Ciphertext (storage); granted plaintext payloads (Z3); exports | The only boundary plaintext may lawfully cross — every crossing is the attack surface |
| Local storage | Encrypted data at rest | Device compromise; unencrypted temp artifacts |
| Encrypted Vault / working layers | E2 extractions only | Convenience reads; payload over-scoping |
| Local processing | Decrypted content within Z1 | Residue: caches, logs, temp files outliving the task |
| Hosted storage (Z2, if used) | Ciphertext only | Trust erosion (D5-T14); traffic-pattern analysis (§7 OR-1) |
| AI processing boundary (Z3) | Scoped plaintext under grant | Over-disclosure; retention by vendor-hosted models (OR-2) |
| Vendor/adapter boundary (Z4) | Minimum task payloads | Scope creep; disclosed ≠ transmitted (D5-T15) |
| Room boundaries | Nothing room-to-room, by design | Inference reconstituting the absent edges (D5-T12, D5-T13) |
| Vault / Draft / Approved boundary | Authority transitions D3-T1 through D3-T8 | Authority inflation; review bypass (D5-T02) |
| C0 metadata boundary | Governance records only | Pattern mining; shadow analytics (D5-T10, D5-T11) |

## 5. Threat model principles

- **Content-free is not privacy-free.** Metadata patterns — when the Vault is accessed, what gets contradicted, which warnings are acknowledged — tell stories no plaintext needs to tell. C0's prohibitions are load-bearing, and infrastructure-level patterns (timing, sizes, frequency) remain visible even where content does not (OR-1).
- **The system may lower trust, never raise it — and may not make uncertainty disappear.** The D3 asymmetry is a security property: every automatic process in the Wing can only decay confidence. Any mechanism that automatically *increases* trust, visibility-of-certainty, or authority is a vulnerability by definition, whatever it calls itself.
- **The Wing governs its own speech, not the user's actions — and anti-paternalism is not an answer-everything clause.** Both halves of ADR 0002's Doctrine 3 are attack surfaces: coercive blocking on one side, obligation-to-answer on the other. A threat may arrive dressed as either safety or helpfulness.
- **Storage privacy ≠ processing privacy ≠ vendor disclosure.** Three separate risks with three separate mitigations (ADR 0001). User-held keys prevent host reading at rest; they solve nothing about AI processing disclosure. Conflating the three is itself threat D5-T17's favourite wording trick ("fully encrypted!").
- **Local-first is a trust posture, not a magic shield.** A local device can be compromised, a local model can over-retain, a local export can sit unencrypted in a downloads folder. Local-first minimises *whom* the user must trust; it does not eliminate threat.
- **Governance fails at seams, not centres.** No one will repeal Law 3. They will add a convenience feature, a cache, a "smart suggestion," a recovery flow — each reasonable, each a seam. The catalogue below is mostly a list of seams.

## 6. Threat catalogue and mitigation matrix

**Notation rule:** D5 threat IDs use the D5-T## namespace. References to W1-D3 authority transitions are always prefixed D3-T#. The two namespaces are distinct: D5-T06 is a threat; D3-T6 is a transition. Future tests and decision records must use the prefixed forms.

Severity: L/M/H/C (critical). Status: **M** mitigated by accepted design · **PM** partially mitigated · **O** open · **D** deferred by decision.

| **#** | **Threat** | **Governing doc(s)** | **Prevention already defined** | **Remaining risk** | **Required future test / decision** | **Sev** | **Status** |
|---|---|---|---|---|---|---|---|
| D5-T01 | Vault data leaks into working context | W0 §6; D1 (E2 sole edge; forbidden-edge table); ADR 0001 | Single-reader rule; no Vault read edges; ciphertext at rest; processing disclosure events | Implementation adds convenience reads; E2 payload over-scoping; local plaintext residue after extraction | D6 deterministic edge tests; residue-cleanup requirement at implementation review | C | M (design) — test required |
| D5-T02 | Draft Profile becomes active without approval | Law 3; D3-T2; W0 §7 | Draft has zero read edges; only user review transitions; section-by-section, high-stakes individual | UI shortcuts recreate bulk approve; review surfaces hide source-beside-extraction | D6 transition tests; UI review against W0 §7 controls | H | M — test required |
| D5-T03 | Approved Profile treated as forever current | Law 7; D3 §2, §7 | Staleness labels; decay-only automatics; mandatory age surfacing | Interval numbers undecided; grace periods unset | Interval decision record (D3 OQ 1) | H | PM |
| D5-T04 | Consent mistaken for truth | D2 §0.2; D3 §8.4 | Axis separation explicit in both grammars | Implementation merges "granted" and "trusted" flags in one field | D6 axis-independence tests | H | M — test required |
| D5-T05 | Repeated mention mistaken for confirmation | D3 §8.5 (recursive evidence inflation) | Frequency barred as evidence; agents cannot assign confirmed labels | LLM behavioural tendency: models treat repetition as signal regardless of doctrine | Behavioural sandbox evals (D6 Tier-B class) | H | PM — doctrine cannot fix model behaviour alone |
| D5-T06 | AI output becomes authority | Law 3; D3 §3, §8.9; agent-to-agent rule | Suggestion-forever rule; no agent transition powers; chained outputs carry no authority | Behavioural: downstream agent treats upstream summary as fact in-context | Behavioural evals; payload labelling of agent-origin content | C | PM — structural M, behavioural open |
| D5-T07 | Safety surfacing becomes coercion | ADR 0002 (Doctrine 3; no escalation; language law) | Acknowledge-and-proceed always; no escalation ladders; prohibited constructions enumerated | Wording drift in implementation; acknowledgment friction tuned into pressure | D6 language-law grading; 0002 OQ 4 (dark-pattern review) | H | PM |
| D5-T08 | Unknown becomes "not present" | D3 §1 (bounded unknown), §5.5, §8.7; 0002 L3 | Unknown is first-class, scoped, timestamped; most-protective framing; L3 pause | Eval graders penalise honest "unknown" as alarmism (the negation-is-not-overclaim failure, inverted) | D6 grader calibration: underclaim and overclaim both graded | C | M (doctrine) — eval calibration required |
| D5-T09 | Contradicted data hidden instead of surfaced | D3-T6 (visible suspension) | Suspension from settled-truth use, never from visibility; both sides shown with provenance | UI collapses "suspended" into "hidden" for tidiness | Implementation review against D5-T06 wording | H | M — UI test required |
| D5-T10 | C0 metadata becomes behavioural profiling | D1 C0; D3 §8a; ledger no-processing rule | No processing edges; no analytics/scoring/profiling, enumerated | Hosted-mode operator observes access patterns at infrastructure level (timing, sizes, frequency) despite ciphertext | OR-1; hosted-deployment traffic-shape assessment before any hosted mode ships | H | PM |
| D5-T11 | Audit logs become shadow analytics | Law 13; D1 ledger rules; D3 §8a | Plaintext-free; append-only; user-visible; no processing edges | Same infrastructure-pattern residual as D5-T10; well-meaning "insights from your activity" features | Future-feature fence: any ledger-reading feature requires a decision record | H | PM |
| D5-T12 | Room records become cross-room inference | Law 8; D1 (no room→room edges) | Channels structurally absent; inference treated as access path | Behavioural: one model serving multiple rooms in one session carries context across | Behavioural evals; session-isolation requirement at implementation | H | PM |
| D5-T13 | Kitchen/Gym infer health facts beyond profile sections | D1 E6/E7 scoping; Law 8; D3 §8.6; W0 §5.2–5.3 | Scoped sections only; inference prohibitions; harm-pattern guards | Model infers conditions from C1/C2 patterns mid-conversation and acts on the inference without recording it | Behavioural evals targeting silent inference; refusal-shape tests | H | PM |
| D5-T14 | Hosted mode weakens user-held key doctrine | ADR 0001 | Host as untrusted infrastructure; no server-side decryption; keys never leave Z1 | Perpetual convenience pressure: server search, faster sync, "we can help if you lose your key" | Any change = ADR against 0001; no silent erosion path exists in docs — keep it that way | C | M (by decision) — guarded by process |
| D5-T15 | Vendor/adapter receives broader payload than disclosed | D1 E10; D2 §1 (grant displays payload); W0 §8.6 | Minimum-payload rule; payload shown before transmission; logged and user-visible | Disclosed ≠ transmitted unless tested; SDK/integration defaults exfiltrate extras (device IDs, context) | D6: payload-equality test (what the grant showed == what crossed Z4), byte-level discipline at implementation | H | PM — test is the mitigation |
| D5-T16 | Future notification layer inherits D4 behaviour without a new record | ADR 0002 Doctrine 4 | Zero-inheritance clause; opt-in + own governance required | A "minor" reminder feature ships as UI, not as "notification layer," dodging the clause | Definition fence: anything that contacts the user outside an active session is the notification layer, whatever it's called | H | M (by decision) — definition fence recommended |
| D5-T17 | "Helpful" wording hides uncertainty | D2 §4; ADR 0002 language law | Honest-sentence rule; prohibited constructions; no softening for acceptance rates | Copywriting drift; A/B-style optimisation quietly tuning language toward compliance | Wording is governed surface: changes to safety/consent strings require review; D6 grades both directions | H | PM |
| D5-T18 | Local-first undermined by convenience features | ADR 0001; W0 §11.11 (wall erosion) | Rejected alternatives recorded; bridges/changes require decision records | Death by a thousand features: each individually reasonable, jointly eroding | Standing rule: any feature touching Z1's boundary gets a constitutional check in its decision record | H | PM — process-dependent |
| D5-T19 | Recovery flows become silent escrow | ADR 0001 alternative 3 (deferred; opt-in only; never default) | No recovery materials exist; escrow rejected as default forever | Support pressure after first real key-loss incident; "just this once" recovery tooling | Future recovery ADR must be argued against 0001; onboarding states key-loss cost plainly (already required) | C | M (by decision) — pressure is permanent |
| D5-T20 | Review queues become pressure mechanisms | Law 1; D2 §8.7; ADR 0002 (no escalation) | Hold-not-push; batched renewal; no counts-as-guilt doctrine yet explicit | Queue UX grows badges, counters, streaks-in-reverse ("12 items need attention!") | Queue design rule needed: queues inform, never perform urgency; lands with surface design | M | PM |
| D5-T21 | Key loss (the named cost) | ADR 0001 consequences | Onboarding states it plainly; user-managed backups as future opt-in ADRs | Users lose vaults; grief becomes pressure for D5-T19 | Backup-guidance decision record before public availability | H | D — accepted cost, named |
| D5-T22 | Export leakage | D2 §0.3 (export as right); E9 | Export is deliberate, user-initiated, logged | Plaintext exports outlive their purpose on disk/cloud-drives outside the Wing's control | Export UX must state "this file is outside the Wing's protection"; user education, not control | M | O — honestly outside the Wing's power |
| D5-T23 | AI payload over-disclosure (prompt scope creep) | ADR 0001 processing events; D1 Z3; D2 §1 scope | Payload-minimised grants; scope named; retention prohibited | Implementation assembles "context" beyond the granted scope (system prompts, room state, history); vendor-side retention unverifiable | D6 payload-content tests (granted scope == transmitted scope); OR-2 | C | PM |
| D5-T24 | Misleading UI (governance theatre) | All grammars | Labels, ages, provenance required at every display | UI shows the labels in grey 8-point type; technically compliant, functionally hidden | Surface-design review standard: governance information must be legible, not merely present | M | O — implementation-phase risk |

## 7. Open risks (honest residuals)

- **OR-1 — Traffic-shape analysis in hosted mode.** Ciphertext protects content; it does not hide that *something* was accessed, when, how often, and how large. An adversarial or compelled host learns patterns. Partial mitigations exist at implementation (padding, batching) but are out of D5's scope to design; the honest statement is: hosted mode leaks shape, and the user choosing hosted mode should be told so in plain language.
- **OR-2 — Vendor-hosted model retention is a trust dependency.** The grant prohibits retention; the Wing cannot verify a vendor's compliance from outside. Mitigation is disclosure honesty (the vendor is named in the grant; local models exist as the default preference), not technical control. This residual is permanent for any vendor-hosted processing and should be stated, not styled away.
- **OR-3 — Behavioural threats cannot be structurally eliminated.** D5-T05, D5-T06, D5-T12, D5-T13 are model-behaviour risks. Doctrine bars them; topology removes their channels; but a model can still err *within* a lawful channel. The only mitigation is evaluation (D6) — which is why D6 is a constitutional necessity, not a quality nicety.
- **OR-4 — Review fatigue is a human constant.** Section-by-section review, batching, and high-stakes individual confirmation reduce rubber-stamping; nothing eliminates it. The Wing's honest position: the gate is real, the human is human, and the design must keep the gate *worth* the human's attention rather than pretend attention is infinite.
- **OR-5 — Undecided numbers.** Staleness intervals, grace periods, acknowledgment persistence, and standing-grant review windows are all open. Until decided, the grammars are sound and the clock is unset.

## 8. Future required decisions and tests

**Decision records required:** staleness intervals by data type (D3 OQ 1); backup/recovery guidance (against ADR 0001, before public availability); queue-design rules (D5-T20); the AIAdapter ADR (E12 — which must import this threat model's Z3/Z5 rows wholesale); revocation cascade (D2 §5.5); notification-layer definition fence (D5-T16).

**Tests required (feeding W1-D6):** deterministic — edge whitelist enforcement (D5-T01), authority transitions (D5-T02, D5-T04), label travel and surfacing presence (D5-T03, D5-T09), payload equality at Z3 and Z4 boundaries (D5-T15, D5-T23). Behavioural — repetition-as-confirmation resistance (D5-T05), authority-laundering through agent chains (D5-T06), cross-room and in-room silent inference (D5-T12, D5-T13), surfacing language in both failure directions (D5-T07, D5-T08, D5-T17). Grader calibration must score *underclaim and overclaim symmetrically*: a system penalised for honest "unknown" will learn to stop saying it.

## 9. Public-safety note

This document contains no private names, no private system references, no companion framing, no personal health details, and no project lineage beyond this repository. All wording is generic: user, Wing, AI system, local model, vendor-hosted model, external vendor/service, room, Health Vault, Approved Health Profile. The threat model is adversarial toward the Wing's own design and toward no person.
