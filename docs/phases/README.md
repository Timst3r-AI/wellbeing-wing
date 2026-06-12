# Phases

**Build philosophy: capability follows governance, not the other way around.**

A phase is closed when its deliverables are complete, reviewed, and checked against the Constitution. No phase begins before the prior phase closes.

## W0 — Constitution

**Scope:** The governing document — purpose, non-goals, core laws, room boundaries, the Health Vault pattern, privacy-by-design principles, agent boundaries, risks and failure modes, open questions.

**Deliverable:** [`../constitution/W0-wellbeing-wing-constitution.md`](../constitution/W0-wellbeing-wing-constitution.md)

**Status:** Drafted (v0.1.1, W0.1 cleanup pass applied) — under review.

**Closes when:** the Constitution is approved as the binding governance document for all subsequent phases.

## W1 — Governance Architecture and Data Boundary Design

**Scope:** Still no UI and no production code. Per Constitution §13, W1 delivers:

1. **Data boundary map** — every data category, its sensitivity class, its home (Vault / Profile / room records / audit), and every permitted flow, with Laws 4, 8, and 9 expressed as explicit edges that do or do not exist.
2. **Consent and scope model** — the grant object (who, what, why, how long), revocation behaviour, and resolution of Open Question 2 (revocation cascade).
3. **Authority and staleness model** — authority labels, last-reviewed timestamps, re-review triggers, and supersession (Laws 3 and 7), defined before any schema exists.
4. **Safety surfacing decision document** — resolution of Open Question 1 (Law 12 mechanics) as its own reviewed decision record.
5. **Threat model** — Vault-centred security analysis and the local-first vs hosted decision (Open Question 6), which should be decided **first**, since every other W1 deliverable inherits from it. *Keystone resolved: [ADR 0001](../decisions/0001-local-first-user-held-keys.md) (Accepted) settles the local-first vs hosted decision via user-held keys; remaining W1 deliverables inherit from it.*
6. **Evaluation plan skeleton** — which constitutional laws map to deterministic tests vs behavioural evaluation (Open Question 12).

**Status:** Planned. Begins when W0 closes.

## W2 and beyond

Defined at the close of W1. Schema, agents, and UI are designed only after the governance architecture they must obey exists in writing.
