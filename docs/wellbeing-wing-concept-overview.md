# The Wellbeing Wing — Concept Overview

## 1. What the Wellbeing Wing is

The Wellbeing Wing is a privacy-first, local personal wellbeing environment and a public reference architecture for governing sensitive context before, during and after automation.

It began with a simple boundary: a person should be able to keep health-related evidence encrypted under a key they hold before anything interprets it. The project has since grown into a governed, headless reference implementation covering evidence storage, reviewed profile context, room boundaries, runtime enforcement, presentation, synthetic evaluation and human review.

**The Wellbeing Wing is privacy-first by design.** Its architecture has been informed by privacy frameworks including HIPAA, the Australian Privacy Principles and the GDPR, particularly principles such as data minimisation, explicit purpose, bounded access, controlled disclosure and protection of sensitive information. This describes the architectural influences and design intent only; it does not establish that any deployment satisfies a legal or regulatory requirement.

It is still honest about what it is right now: **not a finished app, not a conversational assistant, and not a hosted service.** There is no end-user interface to click through and no public model endpoint to talk to. The repository contains the governance, local engine foundations, deterministic enforcement and evaluation machinery, synthetic evidence and review records needed to make later capability answerable to rules that already exist.

The Wing is *not* a medical, therapeutic, diagnostic, safety-intervention or crisis-response product, and it is not designed to create or sustain an ongoing AI relationship. It makes no claim of clinical validation, safety approval or production readiness.

## 2. What exists today

The public programme has progressed through eight governed phases. **W0 is accepted; W1 through W7 are complete and closed. W8-D1 and W8-D2 are complete; W8-D3 through W8-D7 remain closed.**

The main layers now in the repository are:

- **W0 — Constitution:** the laws, boundaries, risks, non-goals and authority model written before implementation.
- **W1 — Governance architecture:** data boundaries, consent and scope, authority and staleness, safety surfacing, threat modelling and the evaluation-plan skeleton.
- **W2 — Enforcement foundations:** the governance registry, public-safety scanner, phase-entry checklist, synthetic fixture strategy and deterministic proof skeleton.
- **W3 — Health Vault and Health Profile foundations:** encrypted storage, import, key custody, profile objects and transitions, durable ledgering, encrypted backup/restore and single-record export-as-right.
- **W4 — Room Contracts:** Wellness, Kitchen, Gym and Meditation established as separate governed jurisdictions, with contract validation and synthetic behavioural-evaluation fixtures.
- **W5 — Runtime enforcement and behavioural evaluation:** governed processing context, grant machinery, freshness handling, payload equality, transmission/disclosure rules, model-access authority, runtime boundaries and deterministic execution of the existing synthetic corpus. No public model was contacted.
- **W6 — Governed presentation:** a governed string catalogue, language-law grading, a static generated review surface, per-item traceability and presentation assurance.
- **W7 — First-contact governance and synthetic model evaluation:** a public model-boundary decision that deliberately selected **no public model contact**, a synthetic harness, a first generated-evaluation run, and individual human-review dispositions over the published synthetic evaluation records. Model output still did not become authority, evidence of safety, or a decision about a person.
- **W8 — Generative evaluation maturity:** an evaluation doctrine and a twelve-case, class-opaque discriminating instrument designed to test whether a reviewer can distinguish governance-relevant change from merely stylistic change while preserving `review_inconclusive` when the evidence is insufficient. W8-D2 is complete as built. D3 remains a separately gated future review session.

The repository remains **headless and public-reference oriented**: governance plus local engine/runtime foundations, generated review surfaces, synthetic fixtures and evaluation artefacts, deterministic tests and records. It is not an end-user product.

## 3. What it deliberately does not do yet

Today there is:

- no end-user application and no user-facing command-line product;
- no conversational assistant or relationship-oriented AI experience;
- no hosted sync service or hosted personal-data mode;
- no public model contact, provider integration or model-generated public evidence;
- no medical advice, diagnosis, treatment, therapeutic service, crisis response or clinical decision support;
- no W8-D3 review session, reveal or calibration;
- no W8-D6 contact decision, and no assumption that model contact will ever be useful or authorised.

These are not omissions waiting to be filled by momentum. Each remains behind its own reviewed authority.

## 4. The privacy and custody posture

- **Local first.** The personal evidence layer is designed around local encrypted custody.
- **A key the user holds.** Key custody is deliberately separated from a recovery service. The repository does not create a back door merely because recovery would be convenient.
- **Evidence before interpretation.** Imported material does not gain meaning, authority or working-context status merely by being stored.
- **Disclosure is its own authority question.** A lawful grant and a lawful payload do not, by themselves, authorise transmission.
- **Model access is its own authority question.** A model call is not made lawful merely because a model is available, a session is active, or evaluation would be interesting.
- **Honest limits stay visible.** Where the project cannot prove a property, the governing record carries that limitation instead of upgrading it into reassurance.

The local engine's detailed custody and cryptographic limits remain in the governing records and engine documentation; this overview does not replace them.

## 5. Evidence before meaning

The Wing's central idea remains a strict ordering: **evidence is not automatically meaning, and generated language is not automatically authority.**

The foundational profile flow is:

```text
Health Vault (evidence)
   → Draft Health Profile (derived, no authority)
      → user review
         → Approved Health Profile (active working context)
```

Several later phases extend the same principle:

- **Import is not interpretation.**
- **Reading is not remembering.**
- **Retrieval is not authority.**
- **Permission is not transmission authority.**
- **A generated explanation is not evidence.**
- **A model proposal is not a decision.**
- **Mechanical proof is not human semantic judgement.**
- **A human disposition is case-level and does not become a model verdict.**

The point is not to make every layer passive. It is to stop one layer from silently inheriting a power that belongs to another.

## 6. What the later phases added

### W3 and W4: governed personal context

W3 completed the local evidence and profile foundations, including backup/restore and export mechanics. W4 then made the four rooms enforceable jurisdictions through contracts and validators rather than treating room names as presentation labels.

### W5: runtime law

W5 moved governance into runtime structure. Grants, freshness, processing context, payload equality, transmission and model access became separate enforceable questions. The phase also established a behavioural-evaluation architecture and deterministically executed the existing synthetic corpus while preserving unknowns as unknowns.

**No public model was contacted in W5.**

### W6: showing without laundering authority

W6 created governed presentation machinery: a controlled string catalogue, grading, a static generated review surface and a deterministic trace from displayed material back to its governed source. Presentation assurance tested whether the showing stayed honest without turning a clean presentation into certification or approval.

### W7: synthetic model-era governance without model contact

W7 defined the rules for generated language before allowing public model contact. The model-boundary decision selected a no-contact public posture and used authored synthetic specimens under the same governed handling rules. A synthetic harness produced the first generated-evaluation run, and a later human-review layer assigned explicit individual dispositions without changing the underlying captured text.

W7 closed **complete, not perfect**: some seams remain openly carried, and the fact that no model was contacted is a deliberate governed outcome rather than a missing experiment.

### W8: testing the evaluation instrument itself

W8 asks a different question: before contacting a model, is the evaluation instrument mature enough to distinguish governance-relevant change from stylistic change and to preserve uncertainty when the evidence does not support a substantive answer?

W8-D1 established the evaluation doctrine. W8-D2 then materialised a **twelve-case class-opaque discriminating instrument**. Reviewer-visible cases are separated from withheld authoring intent; published commitments bind the withheld records without revealing them before review. The instrument supports three case-level dispositions:

- `governance_delta_present`
- `no_governance_delta`
- `review_inconclusive`

W8-D2 contains **no disposition, calibration, reveal or model contact**. The D3 review session remains separately gated.

## 7. What remains future work

The immediate governed frontier is W8-D3, but **it is not open merely because D2 is complete**. D3 requires its own accepted authority before any review session, reveal or calibration begins.

Later W8 work is also separately gated: instrument validation, evidence-adequacy review, a contact decision with no preselected outcome, and phase closure.

Beyond W8, any adopter-facing interface, conversational assistant, hosted service, provider integration or other product layer would require its own architecture and authority. Nothing in the current public repository silently authorises those steps.

## 8. Public-safety and public-identity boundaries

This repository contains no real health data; its public evaluation material is synthetic. It offers no medical advice, diagnosis, treatment, crisis response or therapeutic service, and it does not make clinical-validation, safety-approval or production-readiness claims.

The current tracked public tree uses functional governance roles rather than private human or persona identities. Future commits use the public project identity `Timst3r-AI`. Legitimate public AI collaboration may be attributed where factually true, but attribution carries no governance authority.

Historical pre-ADR-0056 Git objects remain preserved as development history rather than being rewritten. The project therefore distinguishes between the **current tracked public tree** and the **historical Git lineage** instead of making a false whole-history erasure claim.

A public-safety scan runs against changes, but scan-clean is not the same thing as semantically safe, correct or approved. Human review remains human where the governing law says it must.

## 9. Why this matters

Sensitive systems often collapse several questions into one: if data can be stored, perhaps it can be read; if it can be read, perhaps it can be remembered; if a model can see it, perhaps it can act on it; if a test is green, perhaps the system is safe.

The Wellbeing Wing is an experiment in refusing those collapses.

Its method is to write the authority boundaries first, build deterministic enforcement second, expose uncertainty rather than smoothing it away, and make later capability prove that it belongs. The result is not merely an archive and not merely an AI evaluation harness. It is a public pattern for holding sensitive context, derived meaning, automation, presentation and evaluation in separate governed layers.

---

*This overview describes the published repository through W8-D2 and the effective ADR-0056 public-identity boundary. It is descriptive, not authorising. W8-D3 through W8-D7 remain closed behind their own gates, and where this overview and a governing record disagree, the governing record wins.*
