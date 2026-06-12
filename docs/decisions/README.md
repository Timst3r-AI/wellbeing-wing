# Design Decision Records

One file per decision, numbered sequentially: `NNNN-short-title.md`.

A decision record is required whenever a design choice:

- resolves an Open Question from the Constitution (§12), or
- interprets a constitutional law in a way future phases will rely on, or
- creates an exception mechanism (e.g., a Meditation Room bridge under Law 9), or
- would amend the Constitution itself (amendments are explicit, versioned, and reviewed — never silent).

Use `0000-template.md` as the starting point.

## Accepted decisions

| # | Decision | Status | Summary |
|---|----------|--------|---------|
| [0001](0001-local-first-user-held-keys.md) | Local-first by default, hosted-compatible via user-held keys | Accepted | Local-first by default; hosted-compatible via user-held keys; host treated as untrusted infrastructure; AI processing requires explicit scoped disclosure. |
| [0002](0002-safety-surfacing.md) | Safety Surfacing Doctrine | Accepted | Speech-integrity model: surfacing reads governance labels, never bodies; the subject of safety sentences is the data, not the person; intensity ladder L0–L3; acknowledgment, not permission; resolves W0 Open Question 1. |

## Known decisions required before W1 closes

| # | Decision | Resolves |
|---|---|---|
| ~~TBD~~ [0002](0002-safety-surfacing.md) | Safety surfacing mechanics — **resolved (Accepted)** | Constitution Open Question 1 / Law 12 |
| TBD | Consent revocation cascade | Constitution Open Question 2 / Law 10 |
| ~~TBD~~ [0001](0001-local-first-user-held-keys.md) | Local-first vs hosted storage — **resolved (Accepted)** | Constitution Open Question 6 |
| TBD | AIAdapter authentication and scoping | Constitution Open Question 10 |
