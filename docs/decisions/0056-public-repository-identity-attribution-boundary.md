# 0056 — Public Repository Identity and Attribution Boundary

**Status:** Accepted by human reviewer, 2026-10-05. **Effective only on publication and remote verification.**
**Date:** October 2026 · **Phase:** W8 — Generative Evaluation Maturity, cross-cutting repository governance · **Deliverable:** none
**Position:** This record governs public repository identity and attribution only. **It opens no W8 deliverable, changes no W8 evaluation doctrine, changes no case or commitment byte, performs no disposition, reveal or calibration, contacts no model, and authorises no Git-history rewrite. W8-D3 through W8-D7 remain closed behind their own gates.**
**Derived public baseline:** `756d3d3512202a905a5d3b689d75bf06ae31ccf5`, the published and remotely verified W8-D2 corpus landing
**Governed by:** W0, whole, as applicable; the W2-D3 Phase Entry Checklist, especially rules 1, 2, 3, 6 and 9; ADR-0003; the published W7 closure state; the effective W8 runway; ADR-0054 and ADR-0055 only insofar as their existing W8 boundaries remain untouched
**Tier:** J — cross-cutting repository governance with downstream dependents.

---

**A public repository can be honest about its past without wearing it as a name tag. This record separates three things that were previously one: who may be named in the current public tree (functional governance roles), who signs future published commits (the public project identity), and what the already-published history is (a named, preserved, honestly described residue). Nothing in it touches what any record decided — only how the people behind the acts are referred to in public.**

## Decision question

**How does the public Wellbeing Wing preserve a person-neutral and private-lineage-neutral current public identity while retaining auditable governance history, distinguishing functional roles from private identities, preserving legitimate public AI collaboration attribution, and ensuring that future Git publication does not silently reintroduce personal or private-project attribution?**

## Decisions

1. **Current-tree public identity.** Tracked public content uses functional governance roles rather than private human, persona, relationship or private-house identities. Where an historical act must be described, **the role that actually performed the act is named.**

2. **Role-faithful substitution.** A historical review or disposition act is described as performed by **the human reviewer**; an authority or authorisation act by **the human authority**; architecture work by **the architect**; implementation work by **the implementer**, **the builder**, or **the executor** according to the source act. **A generic label must not erase an authority distinction carried by the original source.**

3. **Meaning preservation.** Public-identity remediation may alter attribution wording and only the grammar necessary to make that substitution read correctly. **It must not alter decisions, dispositions, requirements, chronology, counts, permissions, prohibitions, evidence status, authority relationships, acceptance meaning, historical acts or governed outcomes.**

4. **Semantic identity, not lexical coincidence.** A text match is not automatically an identity reference. **URLs, legal or standards identifiers, acronyms, ordinary words and other lexical collisions remain byte-untouched** unless their own governing source independently changes. The accepted Stage-0 census established exactly three such collisions, all preserved — and the external assurance source register (`docs/governance/external-assurance-source-register.md`) itself already explains why one such apparent match is a legitimate EUR-Lex European Legislation Identifier path segment rather than a person reference.

5. **Generated artefacts follow their source.** Where a private attribution originates in deterministic source code, **the source is remediated and the artefact is regenerated.** A generated artefact is not hand-edited independently of its generator.

6. **Registry atomicity.** Source documents remain authoritative over registry summaries. **Any Landing B source-document byte change and its canonical registry hash and role update must move atomically.** Registry prose must itself use public functional roles.

7. **Future Git author and committer identity.** Beginning with this record's own publication commit, repository commits use **`Timst3r-AI` as author and committer, with that account's verified privacy-safe GitHub noreply address.** A personal human name or personal email is not a lawful future repository publication identity.

8. **AI collaboration attribution.** Legitimate AI collaboration may remain publicly attributable using public provider or tool identities — including Claude/Anthropic and OpenAI/Codex — **where the attribution is factually true. Such attribution is acknowledgement of contribution only: it creates no authority, review status, acceptance or decision right**, and it must not import private personas, relationship naming, private-house lineage or private transcript context into the Wing. Existing historical Claude/Anthropic attribution remains lawful historical public collaboration attribution and is not a remediation target. An OpenAI/Codex co-author identity may be used **only if its exact GitHub identity and address mapping is independently verified and the contribution is genuine** — no account mapping may be invented merely to create a contributor avatar.

9. **Historical Git preservation.** This record does not rewrite already published Git objects. At the accepted Stage-0 baseline there are **157 commits reachable from `main`; all 157 carry the legacy personal author identity and all 157 carry the legacy personal committer identity; 12 historical commit messages contain one or more private-project identity terms; and 33 historical Claude/Anthropic attribution trailers exist.** These are **named historical residues, not the future publication posture. No rebase, filter-repo operation, force-push, object replacement or equivalent history rewrite is authorised by this record.**

10. **Truthful public claims.** Once Landing B is effective, the project may claim that the current tracked public tree contains no genuine private-identity references **only if the final semantic review and census establish that fact.** It must not claim that the entire public Git repository or its historical lineage contains no private identity **while pre-ADR-0056 Git objects remain publicly reachable.**

11. **Bounded succession.** This decision governs an accepted three-landing remediation: **Landing A** — this law and its registry and board binding; **Landing B** — current-tree semantic identity remediation; **Landing C** — front-door documentation refresh. **Acceptance of the architecture does not collapse these into one landing.** Each landing has its own fixed path scope, candidate verification and human public-safety review.

12. **No W8 capability movement.** This record is cross-cutting repository governance. **It does not reopen W8-D1 or W8-D2 and does not open W8-D3. D2 remains complete as built. D3 remains a separately gated future act.**

## Alternatives considered

- **Rewrite all historical Git objects** — rejected: it would replace the published commit identities on which later governance and proof succession rely, turning a public-identity correction into an evidence-chain migration.
- **Leave current-tree private attribution untouched because it is historical** — rejected: the current public tree remains an active adoption surface, and the standing public-safety law already prohibits private names and private lineage.
- **Blind global search-and-replace** — rejected: lexical equality is not semantic identity, and Stage 0 demonstrated real collisions that must remain untouched.
- **Remove all AI attribution** — rejected: public AI collaboration attribution is not private identity, and it is legitimate when factually accurate.

## Consequences

- Future commits become public-project attributed rather than personally attributed.
- The current tree can be repaired without rewriting the evidence chain.
- Historical Git metadata remains inspectable and must be described honestly.
- Landing B requires semantic human review, not merely mechanical zero counts.
- Claude attribution may remain.
- OpenAI/Codex attribution may be added on genuine contribution with a verified identity mapping.
- W8-D3 remains closed.

## Public-safety note

Generic and structural wording throughout — role, identity, attribution, residue, register. Public AI provider and tool names appear only as attribution law, never as a model-behaviour claim; no model is contacted or evaluated by this record. No private human, persona, relationship or private-house name appears; no personal address appears; no real health data, no clinical examples, no identified person, no URLs, no credential and no machine path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*The acts were real and the history is kept. What changes is only the name on the public door: from here forward the project signs as the project, the people appear as the roles they held, and the past is allowed to remain the past — visible, described, and never quietly rewritten.*
