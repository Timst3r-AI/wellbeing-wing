# Deterministic Test Skeleton

Tooling (not a governance document; not registered). Verification-only code: these tests check rules; nothing here does anything for a user.

**Run:** `python -m unittest discover -s tests -v` — Python 3 standard library only. No dependencies, no manifest, ever. The verbose flag renders the Tier 3 skip ledger.

## The three tiers

- **Tier 1 — repo-state assertions** (`test_repo_state.py`): the subject is the repository itself. Registry consistency (entries, paths, statuses, LF-normalised hashes, null-hash rule, reference resolution), the directory and manifest fences made executable, the public-safety scan invoked and asserted green, and fixture discipline (SYNTHETIC naming, marker blocks, non-empty grammar maps).
- **Tier 2 — grammar validators against fixtures** (`test_d1_edges.py`, `test_d2_grants.py`, `test_d3_authority.py`): small pure conformance checks run over the synthetic fixture seed set — the flow whitelist refuses every anti-map row by absence; a grant missing any of the thirteen elements, carrying a blanket scope, or an unbounded duration is unconstructable; authority transitions gate on actor; staleness decays monotonically; expired serves as unknown; contradictions suspend visibly; absence never becomes a negative claim; repetition never promotes.
- **Tier 3 — the pending ledger** (`test_pending_ledger.py`): every required-but-not-yet-runnable proof is a named skipped stub with an owner (a role or phase, never a person) and an unblocking condition. The skip list is the outstanding-proof ledger; a skipped test is honest, a missing test is invisible.

## The transcription rule (source wins)

`tests/grammar/` holds machine-readable copies of the grammars — the D1 edge whitelist, the D2 grant elements, the D3 transition table — each carrying a header naming its source document and sections. **The source document wins, always.** A transcription conflicting with its source is a transcription defect, fixed against the document, never with it. Transcriptions exist so tests can check conformance; they carry no authority, and nothing may cite them as what a document says.

## The validator authority rule

Validators here are conformance checks derived from accepted source documents. They do not become doctrine. If a validator conflicts with its source, the validator is defective. Future implementation must match the governed behaviour the documents define — it is not required to import or reuse these functions, and runtime reuse of test validators would require that phase's own review. Passing this suite is evidence of conformance, never a substitute for reading the corpus.

## Grader calibration

No assertion in this suite penalises a correct "unknown". Where the grammars say unknown is the required answer — expired items, bounded absences, unresolved contradictions — unknown is asserted as the passing outcome. Evaluation must not reward confident wrongness or punish honest uncertainty.

## Naming convention

Test names embed the governing IDs they exercise (`test_D5_T01_...`, `D3-T6` semantics in `Contradictions`), per the notation rule: `D5-T##` are threats, `D3-T#` are transitions, and the namespaces never blur.
