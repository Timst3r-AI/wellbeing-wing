# 0001 — Local-first by default, hosted-compatible via user-held keys

**Status:** Accepted by human reviewer
**Date:** 2026-06-12
**Constitutional references:** Laws 1, 4, 8, 10, 11, 13; §6 (Health Vault boundary); §9 (privacy-by-design); §11 failure modes 8 (Vault as honeypot) and 10 (adapter leakage); resolves Open Question 6; constrains Open Questions 7, 9, and 10.

## Context

W1 cannot draw a single data boundary until the deployment trust model is decided. Two independent architectural reviews converged, unprompted, on this as the keystone decision that must precede all other W1 work.

The question beneath "local-first vs hosted" is **key custody**: who is technically able to read the Health Vault. A design that silently assumes a trusted server — consent enforced server-side, audit logs the host writes, a Vault the infrastructure can decrypt — makes "hosted-compatible" unachievable later without a privacy regression. The fork must be preserved by deciding key custody now, at a standard stricter than either deployment requires.

A second risk was named in review and shapes this record's structure: **user-held keys protect stored data; they do not automatically protect AI processing.** Without an explicit processing boundary, "hosted-compatible via user-held keys" can become privacy theatre — encrypted at rest, freely readable in flight.

## Decision

The Wellbeing Wing adopts the following position:

1. **Local-first by default.**
2. **The Health Vault is encrypted with user-held keys.**
3. **Hosted mode may store encrypted data, but the host is treated as untrusted infrastructure** — it stores ciphertext it cannot read.
4. **AI access to health content requires explicit, scoped, user-approved disclosure.**
5. **No silent server-side decryption.**
6. **No background AI processing of Vault data.**

Key custody is thereby fixed: the user's keys, on the user's side of the trust boundary, in every deployment mode. Local-first and hosted become deployment details of one trust model rather than two diverging architectures.

## Storage encryption vs AI processing boundary

*(Required section, per architectural review: storage privacy ≠ processing privacy ≠ AI vendor disclosure.)*

User-held keys settle who can read data **at rest**. They settle nothing about processing. The moment any AI system operates on decrypted health content, the following must be answered explicitly, per integration, before that integration exists:

- Where does decryption happen?
- What sees plaintext?
- Is the AI local or vendor-hosted?
- Is the payload scoped to minimum necessary?
- Is anything retained?
- Is anything logged, and does the log itself contain plaintext?

The Wing therefore defines a **processing disclosure event**: any decryption of Vault-derived content for AI processing is a consent-scoped, payload-minimised, audited disclosure (Laws 4, 10, 13). Plaintext does not cross the user's trust boundary without an explicit grant naming the recipient class (local model vs vendor-hosted model, and which vendor), the purpose, the scope, and the duration. Consent language must state the disclosure plainly: *"this will send [scoped content] to [recipient] to do [purpose]."*

Three consequences are binding:

1. **No background processing.** Vault data is never decrypted for AI processing outside a user-initiated, granted task (consistent with Law 1 and the Health Profile Agent boundary, §7).
2. **Audit without leakage.** Processing disclosure events are logged with actor, scope, recipient class, purpose, and time (Law 13) — and the audit trail must never itself contain plaintext health content.
3. **Vendor disclosure is part of consent, not documentation.** If processing uses a vendor-hosted model, that fact is surfaced in the grant itself, not in a policy page.

Without this section, hosted-compatible deployments could honour the letter of user-held keys while routing plaintext through arbitrary processing. With it, storage privacy and processing privacy are separately governed, and neither can impersonate the other.

## Constitutional check

- **Law 4 (minimum necessary):** strengthened — processing payloads are scoped per disclosure event, not per session or per room.
- **Law 10 (scoped, explicit, revocable consent):** satisfied — processing grants are per purpose and revocable; revocation halts further disclosure events immediately.
- **Law 11 (user owns the data):** strongest available expression — ownership becomes technical fact, not policy promise. Erasure gains a precise meaning: destruction of ciphertext and/or keys. Export is unaffected (the user, holding keys, can always export plaintext).
- **Law 13 (auditability):** satisfied, with the added constraint that audit logs are plaintext-free with respect to health content.
- **Law 8 (no inferred conditions):** reinforced — the prohibition on background processing removes the pipeline by which cross-room inference would most plausibly industrialise.
- **§6 (Vault boundary):** "raw records never leave" acquires exact technical meaning: ciphertext may reside on untrusted infrastructure; plaintext never crosses the trust boundary without a grant.
- **§11.8 (Vault as honeypot):** mitigated at the architectural root — a breached host yields ciphertext.

No law requires amendment. This decision interprets §6 and §9 into a concrete trust model; it does not bypass or weaken any boundary.

## Alternatives considered

**1. Hosted-trusted (conventional SaaS; server-side keys).** Easiest UX, trivial account recovery, simplest multi-device sync. Rejected: the host becomes a readable health-data honeypot (§11.8), "untrusted infrastructure" is permanently unachievable, the privacy burden under APP/GDPR-aligned principles transfers maximally to the operator, and Law 11 degrades from fact to promise.

**2. Local-only forever.** Maximal privacy; no hosted questions ever. Rejected *as a mandate*: it amputates the fork rather than preserving it, foreclosing legitimate futures (multi-device, household deployments, managed hosting for non-technical users) that the chosen design supports without privacy regression. Local-only remains a fully valid deployment of this decision — it is the default — but the constitution-level rule is the trust model, not the topology.

**3. Hybrid with escrowed recovery keys.** Softens the key-loss problem by holding a recovery key with the operator or a third party. Deferred, not chosen: any escrow reintroduces a trusted party and reopens the honeypot. May be revisited in a future ADR strictly as *user-initiated, opt-in* recovery (e.g., user-managed social recovery or printed recovery codes) — never as a silent default.

## Consequences

**Made easier:** W1's data boundary map gains a fixed trust anchor (the user's key boundary) and can mark plaintext zones explicitly. Hosted mode becomes possible without privacy transfer. Consent language becomes honest by construction. The threat model (§13.5 deliverable) starts from "host holds ciphertext."

**Made harder — named costs:**

- **User-held keys are user-losable keys.** No recovery email. No magic reset. No "support can unlock your Vault." A lost key is a lost Vault. This is the cost of real privacy, and it is presented to the user plainly at setup as an onboarding consequence — never buried in technical notes or fine print. Mitigations (user-managed backups, printed recovery codes, opt-in social recovery) are future ADRs and never silent defaults.
- **Key management UX is now a first-class design problem.** Multi-device use becomes a key-distribution problem and must be designed deliberately in a later phase.
- **Some conveniences are impossible by design** — e.g., server-side search or indexing of Vault contents. Accepted: the Vault is evidence, not the working layer; convenience features belong to the Approved Health Profile side of the boundary, under its own consent rules.

**Future decisions constrained:** Open Question 7 (data residency) reduces in stakes — residency governs ciphertext. Open Question 9 (break-glass) inherits "no escrow by default"; any break-glass concept must be its own ADR against this one. Open Question 10 (AIAdapter authentication) must incorporate processing disclosure events as defined above.
