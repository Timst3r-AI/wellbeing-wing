# W8 — Documentation Erratum

**Status:** Accepted by human reviewer, 2026-10-24. **Effective only on publication and remote verification.**
**Date:** 2026-10-24
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** none — a phase-level documentation erratum, outside every W8 deliverable
**Identity:** `W8-DER`, type `phase-record`
**Position:** corrects six W8 statements in the root README and the tests README's dependency statement and family note so that each says what the published record says, and nothing more — deciding no question the record reserves. **It changes no governing record, no proof module other than its own, no case, manifest, register, revealed record or custody, and no registry entry other than its own.**
**Derived public baseline:** `ce78a242df25898d90debee9513bdce7e511471b`, the published and remotely verified W8-D4 completion
**Governed by:** the phase entry checklist (`docs/governance/checklist.md`), rules 2, 4 and 10; ADR-0056, whose Landing C was the front-door documentation refresh; ADR-0046 and the W8 runway's public/private boundary; ADR-0058 Part F, the reservation the corrected wording preserves; the effective records cited in section 3; the W7 closure record as the carried-state authority
**Tier at landing:** J — Judgment. Full ceremony.

---

**The front door said less than the record in five places and more than it in two. This erratum makes it say exactly as much, and no more.**

## 1. What this erratum corrects, and why

1. The root `README.md` was last changed on 2026-10-07, by the ADR-0056 Landing C front-door documentation refresh, when W8-D2 was the newest complete deliverable. Since then W8-D3 (`W8-D3-CCR`, accepted 2026-10-13) and W8-D4 (`W8-D4-CPR`, accepted 2026-10-22) have completed, each published and independently remote-verified. **Five statements in the README contradict the published record** — the status line, the contents sentence, the W8 row of the phase table, the "what exists now" bullet on the W8 instrument and the "what does not exist" bullet on W8-D3 — **and two assert more than the record establishes:** the contents sentence's closing claim that no public model has been contacted at any point, and the "what does not exist" bullet on model contact. The published authority for the whole history is narrower than either. W7 closed without model contact; W8-D6 is unopened and no W8 contact implementation is authorised before it; and ADR-0058 decision 15, carried whole by the W8-D3 and W8-D4 records, classifies no exchange under ADR-0047 decision 3 and does not state whether model contact occurred. The README now says exactly that, deciding the reservation in neither direction.
2. `tests/README.md` has not changed since it landed with W2-D5 on 2026-07-05, and still states that the suite is "Python 3 standard library only. No dependencies, no manifest, ever." The same day, W3-D2 milestone 1 landed the engine store skeleton with `requirements.txt`, under ADR-0008's selection of the local-process engine with its PyNaCl binding and the dependency-fence crossing that `tests/test_repo_state.py` records. Since then the manifest has pinned the engine's entire third-party runtime surface, the engine's crypto port has imported one of its packages, and the engine tests have needed it. The statement is true of the governance proofs and false of the suite as a whole. The same file describes only the W2 three-tier skeleton; the proof modules later phases added beside it go unmentioned.
3. **What this record is, and is not.** It is the named, separately accepted documentation-refresh act and audit record for two unregistered surfaces — a narrative front door and a tooling note. It is not a second errata ledger, and it amends no registered accepted record. Checklist rule 10 keeps errata to registered records in those records' own registry entries, and remains whole; the checklist supplies no unregistered-file exception, and this record claims none. Under rule 4 it supplies the exact root file and its purpose for the human reviewer to accept; its own registry entry binds the act in the ordinary way, as `W8-CHC`'s did. **Whether the corrections are non-semantic is the human reviewer's judgment under rule 2;** this record proposes them so — README statements lagging sealed acceptances, a reserved question restated as reserved, and a tooling note lagging an accepted fence crossing — and flips nothing.
4. **Root-file fence.** Checklist rule 4 admits an edit to `README.md` only when an accepted landing record names the exact root file and its purpose. This record names `README.md` for the purpose of section 2 and nothing else; `tests/README.md` lies inside the authorised `tests/` directory and is named here for the same reason.

## 2. The corrections, as exact sites

5. **Each correction is an exact transformation of a fixed pre-image at the derived public baseline, proven by DE1:** six sites in `README.md` (R1 to R6) and two in `tests/README.md` (T1 and T2), each occurring exactly once before and once after, with nothing else in either file changed. The proof module pins every old and new string. The new wording of each site is:

**R1** (`README.md`):

```text
**W0 is accepted; W1 through W7 are complete and closed. W8-D1 through W8-D4 are complete; W8-D5 through W8-D7 remain closed behind their own gates.**
```

**R2** (`README.md`):

```text
synthetic generated-evaluation records with individual human dispositions, a class-opaque W8 discriminating instrument, and two further W8 corpora — a twelve-case supplementary corpus for synthetic calibration and an eighteen-case validation corpus — each dispositioned by the human authority in one session with the authoring records withheld, then revealed as exact retained bytes and compared case by case, with every recorded divergence left undiagnosed by the human authority's decision. **W7 closed without model contact; W8-D6, the contact decision, remains unopened and no W8 contact implementation is authorised before it; and the published W8 records, under ADR-0058's standing reservation, classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred.**
```

**R3** (`README.md`):

```text
| **W8** | Generative evaluation maturity | 🟡 In progress — D1 doctrine, D2 discriminating instrument, D3 synthetic calibration and D4 instrument validation complete; D5–D7 closed |
```

**R4** (`README.md`):

```text
- A W8 evaluation doctrine; a twelve-case, class-opaque discriminating instrument whose withheld authoring records stay sealed outside the repository under their own authority; and two further corpora — twelve supplementary cases and eighteen validation cases — each with published integrity commitments, one human disposition session with the authoring records withheld, a byte-exact reveal of every withheld record, and a published case-level comparison carrying only the two permitted count kinds.
```

**R5** (`README.md`):

```text
- No diagnosis of any recorded divergence, no W8-D5 evidence-adequacy finding, no W8-D6 contact decision and no W8-D7 closure. Those remain separately gated.
```

**R6** (`README.md`):

```text
- No public model runtime, provider integration, transport, credentials or model-generated public evidence, and no W8 contact implementation before a lawful W8-D6 decision; ADR-0058's reservation on classifying any exchange stands.
```

**T1** (`tests/README.md`):

```text
**Run:** `python -m unittest discover -s tests -v` — Python 3 standard library plus the engine's entire third-party runtime surface, exact-pinned in `requirements.txt` (`PyNaCl==1.6.2`, `cffi==2.0.0`, `pycparser==3.0`), which the engine's crypto port imports and the engine tests need; no other dependency manifest is admitted. The verbose flag renders the Tier 3 skip ledger.
```

**T2** (`tests/README.md`):

```text
The skip list is the outstanding-proof ledger; a skipped test is honest, a missing test is invisible.

Later phases added their own proof modules beside these three tiers: `test_w4_*`, `test_w6_*`, `test_w7_*`, `test_w8_*`, `test_engine_*`, `test_runtime_*` and `test_evaluation_*`. The three tiers remain the W2 skeleton they stand on.
```

## 3. Grounding

6. **Every corrected statement is mapped to its sources at the baseline, and DE2 proves the mapping's mechanics:** each statement fragment occurs exactly once in its corrected file; for a `record` or `file` row the cited fragment occurs verbatim in the cited tracked source at `ce78a242`, a `record` row's identity is an accepted registry entry at that path, and a `file` row's path is named by no registry entry; a `registry` row's fact holds over the baseline registry; a `tree` row's fact holds over the baseline tracked tree; and this table, read whole, is exactly the module's trusted rows. **DE2 proves presence and structure, never entailment: that a fragment supports the whole of the statement beside it is the reviewer's reading, laid out here row by row so that it can be checked.** A statement that rests on more than one source has one row per source. Where a source limits what a statement may be taken to mean, the limit is cited as its own row.

| Statement (fragment in the corrected file) | Kind | Source | Evidence |
|---|---|---|---|
| `W8-D1 through W8-D4 are complete` | file | `README.md` | `W8-D1 and W8-D2 are complete` |
| `W8-D1 through W8-D4 are complete` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `W8-D3 is complete in the accepted sense` |
| `W8-D1 through W8-D4 are complete` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `W8-D4 is complete` |
| `W8-D1 through W8-D4 are complete` | registry | `governance/registry.json` | `every entry of deliverables W8-D1 to W8-D4 is accepted` |
| `W8-D5 through W8-D7 remain closed behind their own gates` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `W8-D5 through W8-D7 remain closed behind their own briefs` |
| `W8-D5 through W8-D7 remain closed behind their own gates` | registry | `governance/registry.json` | `no entry of deliverable W8-D5, W8-D6 or W8-D7` |
| `a twelve-case supplementary corpus for synthetic calibration` | record | `W8-S1-SCR` · `docs/phases/W8-S1-supplementary-corpus-record.md` | `exactly twelve reviewer-visible supplementary cases` |
| `an eighteen-case validation corpus` | record | `W8-D4-VCR` · `docs/phases/W8-D4-validation-corpus-record.md` | `exactly eighteen reviewer-visible validation cases` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D3-HDR` · `docs/phases/W8-D3-human-disposition-record.md` | `acting as the sole human reviewer, returned exactly one lawful token for each of the twelve cases` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `returned exactly one lawful token for each of the eighteen cases` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `This was the validation corpus's one session` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `twelve withheld authoring records` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D3-HDR` · `docs/phases/W8-D3-human-disposition-record.md` | `No test proves the absence of influence, semantic independence or reviewer blinding, and none is claimed.` |
| `each dispositioned by the human authority in one session with the authoring records withheld` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `No test proves the absence of influence, semantic independence or reviewer blinding, and none is claimed.` |
| `then revealed as exact retained bytes` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `The reveal publishes the exact retained bytes` |
| `then revealed as exact retained bytes` | record | `W8-D4-VRC` · `docs/phases/W8-D4-validation-record.md` | `The reveal publishes the exact retained bytes` |
| `compared case by case` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `the comparison records exactly the case identity` |
| `compared case by case` | record | `W8-D4-VRC` · `docs/phases/W8-D4-validation-record.md` | `the comparison records exactly the case identity` |
| `with every recorded divergence left undiagnosed by the human authority's decision` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `every recorded divergence stays recorded and undiagnosed` |
| `W7 closed without model contact` | record | `W7-CR` · `docs/phases/W7-closure-record.md` | `No model contact occurred anywhere in W7` |
| `W8-D6, the contact decision, remains unopened` | record | `W8-AR` · `docs/phases/W8-runway-generative-evaluation-maturity.md` | `Contact decision` |
| `W8-D6, the contact decision, remains unopened` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `W8-D5 through W8-D7 remain closed behind their own briefs` |
| `W8-D6, the contact decision, remains unopened` | registry | `governance/registry.json` | `no entry of deliverable W8-D5, W8-D6 or W8-D7` |
| `no W8 contact implementation is authorised before it` | record | `W8-AR` · `docs/phases/W8-runway-generative-evaluation-maturity.md` | `No W8 deliverable before W8-D6 may contact a model, prepare credentials, providers, transport or implementation for contact` |
| `classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred` | record | `ADR-0058` · `docs/decisions/0058-w8-d3-session-recovery-law.md` | `does not classify any exchange associated with the void attempt under ADR-0047 decision 3, and does not state whether model contact occurred` |
| `classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred` | record | `W8-D3-HDR` · `docs/phases/W8-D3-human-disposition-record.md` | `does not classify any exchange under ADR-0047 decision 3 and does not state whether model contact occurred` |
| `classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `does not classify any exchange under ADR-0047 decision 3 and does not state whether model contact occurred` |
| `classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `no classification of any exchange under ADR-0047 decision 3` |
| `D3 synthetic calibration and D4 instrument validation complete` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `W8-D3 is complete in the accepted sense` |
| `D3 synthetic calibration and D4 instrument validation complete` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `W8-D4 is complete` |
| `whose withheld authoring records stay sealed outside the repository under their own authority` | record | `ADR-0059` · `docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md` | `its retained records stay sealed in their existing custody` |
| `each with published integrity commitments` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | They are bound by `W8-S1-CM-01` |
| `each with published integrity commitments` | record | `W8-D4-VRC` · `docs/phases/W8-D4-validation-record.md` | They are bound by `W8-V1-CM-01` and `W8-V1-CM-02` |
| `one human disposition session with the authoring records withheld` | record | `W8-D3-HDR` · `docs/phases/W8-D3-human-disposition-record.md` | `acting as the sole human reviewer, returned exactly one lawful token for each of the twelve cases` |
| `one human disposition session with the authoring records withheld` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `This was the validation corpus's one session` |
| `one human disposition session with the authoring records withheld` | record | `W8-D4-VSR` · `docs/phases/W8-D4-validation-session-record.md` | `No test proves the absence of influence, semantic independence or reviewer blinding, and none is claimed.` |
| `a byte-exact reveal of every withheld record` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `The reveal publishes the exact retained bytes` |
| `a byte-exact reveal of every withheld record` | record | `W8-D4-VRC` · `docs/phases/W8-D4-validation-record.md` | `The reveal publishes the exact retained bytes` |
| `a published case-level comparison carrying only the two permitted count kinds` | record | `W8-D3-CCR` · `docs/phases/W8-D3-calibration-completion-record.md` | `Exactly two kinds of count are published` |
| `a published case-level comparison carrying only the two permitted count kinds` | record | `W8-D4-VRC` · `docs/phases/W8-D4-validation-record.md` | `Exactly two kinds of count are published` |
| `No diagnosis of any recorded divergence` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `No divergence is diagnosed.` |
| `no W8-D5 evidence-adequacy finding, no W8-D6 contact decision and no W8-D7 closure` | record | `W8-D4-CPR` · `docs/phases/W8-D4-completion-record.md` | `W8-D5 through W8-D7 remain closed behind their own briefs; this record opens none of them` |
| `no W8-D5 evidence-adequacy finding, no W8-D6 contact decision and no W8-D7 closure` | registry | `governance/registry.json` | `no entry of deliverable W8-D5, W8-D6 or W8-D7` |
| `No public model runtime, provider integration, transport, credentials or model-generated public evidence` | record | `W8-AR` · `docs/phases/W8-runway-generative-evaluation-maturity.md` | `choose a provider · build a model transport · create credentials` |
| `No public model runtime, provider integration, transport, credentials or model-generated public evidence` | file | `README.md` | `model-generated public evidence` |
| `no W8 contact implementation before a lawful W8-D6 decision` | record | `W8-AR` · `docs/phases/W8-runway-generative-evaluation-maturity.md` | `contact a model before a lawful W8-D6 decision and a separately accepted implementation brief` |
| `ADR-0058's reservation on classifying any exchange stands` | record | `ADR-0058` · `docs/decisions/0058-w8-d3-session-recovery-law.md` | `does not classify any exchange associated with the void attempt under ADR-0047 decision 3, and does not state whether model contact occurred` |
| `ADR-0058's reservation on classifying any exchange stands` | record | `W8-D3-HDR` · `docs/phases/W8-D3-human-disposition-record.md` | `ADR-0058 Part F carries whole` |
| the engine's entire third-party runtime surface, exact-pinned in `requirements.txt` | file | `requirements.txt` | `The engine's entire third-party runtime surface, exact-pinned.` |
| `which the engine's crypto port imports` | file | `engine/ports/crypto.py` | `import nacl.secret` |
| `and the engine tests need` | file | `tests/test_engine_custody.py` | `import nacl.pwhash` |
| `no other dependency manifest is admitted` | file | `tests/test_repo_state.py` | `exactly the engine directory and the single pinned manifest, nothing` |
| `Later phases added their own proof modules beside these three tiers` | tree | `tests/` | `seven proof families, each matching a tracked tests/test_*.py module` |
| `The three tiers remain the W2 skeleton they stand on` | record | `W2-D3` · `docs/governance/checklist.md` | `tests/` (W2-D5) |
| `The three tiers remain the W2 skeleton they stand on` | file | `tests/README.md` | `## The three tiers` |

Kinds: `record` — a verbatim fragment of a registered, accepted record or decision, cited by identity and path; `file` — a verbatim fragment of a tracked file at the baseline that no registry entry names (a README pre-image, carrying an earlier statement unchanged, or a tooling file), cited by path alone and refused by DE2 if the path turns out to be registered; `registry` — a fact over the baseline registry, checked directly; `tree` — a fact over the baseline tracked tree, checked directly. Nothing is paraphrased. The tests README's pinned lines are proven equal to `requirements.txt` at the baseline, and its named module families present in the tracked tree, by DE3.

## 4. What this erratum does not do

7. **It changes no governing record, no proof module other than its own, no case, manifest, register, revealed record, custody or registry entry other than its own.** It flips no status of any registered record. It adds no capability, readiness, safety, correctness or approval claim, and it removes none of the README's disclaimers, which DE4 proves retained. **It does not classify any exchange under ADR-0047 decision 3, does not state whether model contact occurred, and does not open, reproduce or seek a retrospective classification of anything ADR-0058 reserves.**
8. `docs/wellbeing-wing-concept-overview.md`, the README's first reading-order item, was refreshed together with the README under ADR-0056 Landing C and still describes the repository through W8-D2. **It is outside this erratum's authorised scope and is named here as a recorded observation for a separate decision**, not corrected.
9. The two corrected files remain narrative surfaces. Where either disagrees with a governing record, the governing record wins, as the README itself states; this erratum restates the record, it does not interpret it.

## 5. Proof obligations

10. **Six obligations, mechanics only, each with planted-mutant or negative controls, landed in `tests/test_w8_documentation_erratum.py`.** Every proof reads this landing's fixed snapshot and executes the helpers it relies on from that snapshot's bytes; the module holds no live gate.

| # | Obligation | Decidability |
|---|---|---|
| **DE1** | Both files are the exact pinned transformations of their baseline pre-images under the site tables — each site once, the tables reversible — with nothing else in either file changed; this record carries each site's new wording once | **Mechanical** |
| **DE2** | Every grounded statement occurs once in its corrected file; each `record` or `file` row's fragment occurs verbatim in its tracked source at the baseline, a `record` row's identity accepted at that path, a `file` row's path named by no registry entry; each `registry` and `tree` row's fact holds at the baseline; section 3's table, read whole, is exactly the trusted rows. Presence and structure only — never entailment | **Mechanical** |
| **DE3** | The tests README's pinned lines are exactly `requirements.txt`'s non-comment lines at the baseline; each named module family matches a tracked module and no other family is named; the README's W8 statements agree with the registry at the baseline — every W8-D1 to W8-D4 entry accepted, the two completion records present, no W8-D5 to W8-D7 entry | **Mechanical** |
| **DE4** | The two corrected files, this record and the board wording this landing adds carry no case identity, token, count beside a kind or token, reserved authoring label, schema literal or derived-figure form — the only strings set aside before the figure scan being the manifest's own pins, read from `requirements.txt` at the baseline, and the licence name, each matched whole between token boundaries and never as a prefix of a longer string; the wording this landing adds carries no method label; the README's three disclaimers are retained | **Mechanical; textual forms only** |
| **DE5** | The registry and the board change exactly as authorised, in draft or accepted form; R9's sentence is carried once; neither README gains a registry entry; this record's entry has no deliverable | **Mechanical for binding; acceptance is the human act** |
| **DE6** | This landing's census is exactly item 11's | **Mechanical** |

## 6. Census

11. **This landing's census is exactly six paths:** MODIFY `README.md` · MODIFY `tests/README.md` · NEW `docs/phases/W8-documentation-erratum.md` · NEW `tests/test_w8_documentation_erratum.py` · MODIFY `governance/registry.json` · MODIFY `docs/phases/README.md`. No governing record, case home, register, revealed record or other proof module is touched.

## Public-safety note

Generic and structural wording throughout. Roles only, under ADR-0056. No case is named, quoted or characterised; no token or count appears. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential and no custody location. **Any real-person adoption is a separate governed authority outside this repository.**

---

*A front door is a promise about what lies behind it. This one now keeps the promise the record already made — and no promise the record withholds.*
