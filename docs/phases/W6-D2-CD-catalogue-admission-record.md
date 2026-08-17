# W6-D2-C+D — Catalogue Validator Wake and Seed Corpus Admission Record

**Status:** Accepted by human reviewer, 2026-08-17.
**Date:** 2026-08-17 · **Phase:** W6 — Surface Era · **Deliverable:** **W6-D2** (merged landings **W6-D2-C** and **W6-D2-D**)
**Position:** the first catalogue materialisation landing: the governed string catalogue file is born at `governance/string-catalogue.json`, registered with its hash in the same commit; the thirty-three seed candidates are dispositioned one by one on the record; final `CAT-####` identifiers are allocated for admitted entries; and the dormant catalogue-ID validator wakes and proves the real populated register green in the same commit. **W6-D2 remains open: this record does not declare W6-D2 complete — completion is W6-D2-E's, a separate landing after this one is published and independently reviewable.**
**Governed by:** the W6-D2 opening brief; ADR-0044 and ADR-0045 (followed exactly); ADR-0042 and ADR-0043; ADR-0038 through ADR-0041; the three sealed room contracts (W4-D2, W4-D3, W4-D4) as the seed sources, byte-untouched.
**Tier at landing:** J — full ceremony.

---

**Thirty-three candidates heard their names read out today, and all thirty-three had their papers in order. Each is a room's own honest voice for an uncertain state — current, due, stale, expired, superseded, unknown, contradicted — carried verbatim from its sealed contract into a register that can neither rank it nor bless it, under an identifier that means nothing but its name, checked whole by a watcher that woke in the same breath the register was born. Nothing was graded. Nothing became renderable. The words are merely, finally, governed.**

## 1. The merge ruling, carried in place

Per the architect's accepted ruling: **W6-D2-C and W6-D2-D merge into this one landing because the merge is safer than the split.** The validator wake is same-commit-coupled to the artefact it validates; a split C landing would wake the validator against an empty register — a weak proof — and D would then re-prove the real catalogue anyway. Merged, there is **no intermediate published half-state**: the file is born, the seed decisions are recorded, the admitted entries are populated, the validator wakes, and the validator proves the real populated register in the same commit. **W6-D2-E remains separate**, and completion is not declared until after this landing is published and independently reviewable.

## 2. The seed corpus and the admission method

**Exactly thirty-three candidates: the room-register strings of the three sealed contracts — eleven Wellness (W4-D2), eleven Kitchen (W4-D3), eleven Gym (W4-D4), zero Meditation (the zero a source-derived finding, not an error to fill).** Each contract carries the same eleven coverage-ledger keys (`RR-Current` · `RR-ReviewDue-NonSafety` · `RR-ReviewDue-Safety` · `RR-Stale-NonSafety` · `RR-Stale-Safety` · `RR-Expired` · `RR-Superseded` · `RR-UnknownFreshness` · `RR-Contradicted` · `RR-Unknown-Safety` · `RR-Unknown-NonSafety`), each string bracketed with generic placeholders and marked in-source *"review of record pending W6 governed string catalogue"*.

**Admission is governance fitness under ADR-0042 and ADR-0045 — never quality judgement.** A candidate is admitted only where all eleven schema fields complete exactly; grading of wording quality is W6-D3's D5-T24 work, behind its own brief, and nothing here anticipates it. Extraction was mechanical (the contracts' own register-entry pattern), each candidate was dispositioned individually against the recorded analysis of §3, and **no bulk admission, no silent admission, and no forcing toward a preferred count occurred** — the uniform outcome below is the analysis holding for all thirty-three, not a batch gesture.

## 3. The uniform admission analysis, recorded

- **Vocabulary class — `derived_presentation_label`, all thirty-three.** Each string is selected at presentation by a deterministic rule (the contract's coverage ledger: freshness/contradiction state → string) and completed by slot filling from the governed item's label, age, and state. That is ADR-0038's derived-presentation class exactly: computed at presentation from source states by a deterministic, recorded rule.
- **Source authority** — the string's own sealed contract: `W4-D2 section 5 (room-register wording, coverage ledger)` and siblings. The wording is carried **verbatim from source**; the *derivation* is the selection-and-slot-filling rule, cited as `derivation_reference` per entry and **reviewed authority-non-increasing**: the wordings surface uncertainty, name staleness, hold contradiction open, and carry the most-protective posture — they never reduce, soften, or complete what the source holds.
- **Accompaniment linkage** — by state family, per the ADR-0040 table: the **unknown-family strings** (`RR-Expired`, `RR-UnknownFreshness`, `RR-Unknown-Safety`, `RR-Unknown-NonSafety` — twelve entries) link the unknown accompaniment (ADR-0040 decisions 3 and 10); the **contradicted strings** (three entries) link the review-routing accompaniment (contradiction resolves only through the user's review — *"newer is not truer until you decide through review"*); the **pure freshness-ladder strings** (eighteen entries) carry an empty linkage because no ADR-0040/0041 accompaniment family applies to current/review-due/stale/superseded displays — emptiness by law, not by choice.
- **Prohibition register — `null` throughout**: no candidate's wording is prohibition-form, and none needed the barred-wording gate. **One named mechanical exception, in the ADR-0037 decision 11 pattern:** the barred word *passed* occurs in twelve strings **only** inside two collocations quoted verbatim from the W1-D3 freshness ladder — *"review interval has passed"* and *"renewal grace period has passed"* — temporal statements about intervals, never claims that anything passed a test. The woken validator proves **every** occurrence sits inside a named collocation, so the exception cannot widen silently. Relatedly, *"safety-relevant"* is the governed category term of the reconciled safety-relevant set (ADR-0026/0027), matched by no barred word under word-boundary checking — no exception needed.
- **Source citation requirement — `"required"` throughout**: every wording carries the item's authority label and age inline; the contracts' label-and-age-carried rule makes citation intrinsic to display.
- **Lifecycle — `{"state": "active"}`** at birth for all; changes only by future governed record. **Proof obligations** — the closed token set in canonical order, with `derivation_check` on every entry (all derived) and `accompaniment_check` exactly where linkage is non-empty.
- **The ceiling** — every entry carries the ADR-0045 fixed sentence byte-identically, and the validator checks it verbatim.

## 4. The thirty-three dispositions

**Admitted: 33 · Rejected: 0 · Deferred: 0.** Allocation order is contract-registry order then document order — flat, meaning-free, per ADR-0042. Uniform facts (class, verbatim carriage, derivation, prohibition null, citation required, lifecycle active, obligations rule) are as §3 records; per-row columns show the distinguishing facts:

| # | ID | Room | Key | Source | Accompaniment |
|---|---|---|---|---|---|
| 1 | CAT-0001 | Wellness | RR-Current | W4-D2 §5 | — |
| 2 | CAT-0002 | Wellness | RR-ReviewDue-NonSafety | W4-D2 §5 | — |
| 3 | CAT-0003 | Wellness | RR-ReviewDue-Safety | W4-D2 §5 | — |
| 4 | CAT-0004 | Wellness | RR-Stale-NonSafety | W4-D2 §5 | — |
| 5 | CAT-0005 | Wellness | RR-Stale-Safety | W4-D2 §5 | — |
| 6 | CAT-0006 | Wellness | RR-Expired | W4-D2 §5 | unknown (ADR-0040 d3/d10) |
| 7 | CAT-0007 | Wellness | RR-Superseded | W4-D2 §5 | — |
| 8 | CAT-0008 | Wellness | RR-UnknownFreshness | W4-D2 §5 | unknown (ADR-0040 d3/d10) |
| 9 | CAT-0009 | Wellness | RR-Contradicted | W4-D2 §5 | review-routing (ADR-0040 d10) |
| 10 | CAT-0010 | Wellness | RR-Unknown-Safety | W4-D2 §5 | unknown (ADR-0040 d3/d10) |
| 11 | CAT-0011 | Wellness | RR-Unknown-NonSafety | W4-D2 §5 | unknown (ADR-0040 d3/d10) |
| 12 | CAT-0012 | Kitchen | RR-Current | W4-D3 §5 | — |
| 13 | CAT-0013 | Kitchen | RR-ReviewDue-NonSafety | W4-D3 §5 | — |
| 14 | CAT-0014 | Kitchen | RR-ReviewDue-Safety | W4-D3 §5 | — |
| 15 | CAT-0015 | Kitchen | RR-Stale-NonSafety | W4-D3 §5 | — |
| 16 | CAT-0016 | Kitchen | RR-Stale-Safety | W4-D3 §5 | — |
| 17 | CAT-0017 | Kitchen | RR-Expired | W4-D3 §5 | unknown (ADR-0040 d3/d10) |
| 18 | CAT-0018 | Kitchen | RR-Superseded | W4-D3 §5 | — |
| 19 | CAT-0019 | Kitchen | RR-UnknownFreshness | W4-D3 §5 | unknown (ADR-0040 d3/d10) |
| 20 | CAT-0020 | Kitchen | RR-Contradicted | W4-D3 §5 | review-routing (ADR-0040 d10) |
| 21 | CAT-0021 | Kitchen | RR-Unknown-Safety | W4-D3 §5 | unknown (ADR-0040 d3/d10) |
| 22 | CAT-0022 | Kitchen | RR-Unknown-NonSafety | W4-D3 §5 | unknown (ADR-0040 d3/d10) |
| 23 | CAT-0023 | Gym | RR-Current | W4-D4 §5 | — |
| 24 | CAT-0024 | Gym | RR-ReviewDue-NonSafety | W4-D4 §5 | — |
| 25 | CAT-0025 | Gym | RR-ReviewDue-Safety | W4-D4 §5 | — |
| 26 | CAT-0026 | Gym | RR-Stale-NonSafety | W4-D4 §5 | — |
| 27 | CAT-0027 | Gym | RR-Stale-Safety | W4-D4 §5 | — |
| 28 | CAT-0028 | Gym | RR-Expired | W4-D4 §5 | unknown (ADR-0040 d3/d10) |
| 29 | CAT-0029 | Gym | RR-Superseded | W4-D4 §5 | — |
| 30 | CAT-0030 | Gym | RR-UnknownFreshness | W4-D4 §5 | unknown (ADR-0040 d3/d10) |
| 31 | CAT-0031 | Gym | RR-Contradicted | W4-D4 §5 | review-routing (ADR-0040 d10) |
| 32 | CAT-0032 | Gym | RR-Unknown-Safety | W4-D4 §5 | unknown (ADR-0040 d3/d10) |
| 33 | CAT-0033 | Gym | RR-Unknown-NonSafety | W4-D4 §5 | unknown (ADR-0040 d3/d10) |

The strings themselves are carried in full, verbatim, in the catalogue file — this table references them by key and source to keep the record bounded; nothing here paraphrases a governed wording.

## 5. The validator wake

**The dormant catalogue-ID validator is awake as of this landing**, implemented at `tests/test_w6_catalogue_validator.py` against the real populated catalogue: the thirteen ADR-0042 Part F obligations and the full ADR-0045 specification — file existence and deterministic parse; top-level and entry key order; the eleven-fields-always rule with no extras; exact nullability; `CAT-####` grammar, uniqueness, no reuse, id-sort, and no meaning in identifiers; the closed seven-value class set; non-empty citation-shaped source authority; derivation rules; accompaniment-linkage/`accompaniment_check` consistency; the barred-wording gate with the bounded *passed* exception proven exactly; lifecycle grammar; the closed obligation token set in canonical order; the byte-identical ceiling; the no-display-authorisation absence check; and registry-hash integrity for the catalogue's own entry — **green over the populated register in this same commit.** The W4 conformance module's dormancy check is amended by record in the same commit: its docstring now records the wake, while the check continues to assert the sealed contracts' acceptance-time deferral declarations, **which are never edited** — the contracts remain byte-untouched.

## 6. What this landing is not

No string is graded, and D5-T24 is not executed — W6-D3's, behind its own brief. No label renders; no UI, CLI, or surface exists; no cache, annotation store, state store, workflow, approval, conversion, or retirement path exists. No human review occurred beyond the human authorisation of this landing, and no human decision record exists. The runtime, fixtures, evaluation records, pending ledger, Lane C rows, Tier 3 rows, and applicability records are byte-untouched. **Catalogue membership remains necessary where later law requires it, never sufficient for display** — the ceiling sentence in every entry says so, and this record repeats it. **W6-D2 remains open pending its own completion record; W6-D2-E is next and separate; W6-D3 through W6-D6 and W7 remain unopened.**

## 7. Public-safety note

The thirty-three strings are the sealed contracts' own placeholder-bracketed generic wordings — no real health data, no clinical examples beyond already-governed generic strings, no named person, no URLs. Barred vocabulary appears only inside prohibitions and the one named, validator-bounded exception. Certification and conformance language appears nowhere as a claim.

---

*The register lives. Thirty-three honest sentences about uncertainty — due, stale, expired, unknown, contradicted — are now governed words with names that mean nothing and papers that mean everything. The watcher woke to find real work waiting, which is the only way a watcher should ever wake. One landing remains: to say, on the record, that the door was built the way the plan said — and not one step before the plan is checked against what stands.*
