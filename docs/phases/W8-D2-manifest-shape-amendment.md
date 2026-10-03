# W8-D2 — Manifest Shape Amendment

**Status:** Accepted by human reviewer, 2026-10-03. **Effective on publication and remote verification.**
**Date:** 2026-10-03
**Phase:** W8 — Generative Evaluation Maturity
**Deliverable:** W8-D2 — Discriminating instrument
**Identity:** `W8-D2-MSA`, type `phase-record`
**Position:** a bounded structural reconciliation of ADR-0055 Part J, landed before any case exists. On its acceptance, publication and independent remote verification it fixes the manifest file container that decision 28 omitted — and until that moment, **first-case authoring remains prohibited.**
**Derived public baseline:** `500d11a36f166d7cff2739e4bb583401aaa31a3c`, the published and remotely verified D2-B landing
**Governed by:** ADR-0055, whole, whose own decision question this amendment completes; the effective `W8-D2-DIB`; ADR-0054; the W8 runway; the W7-D5-PSA/MRA amendment precedent
**Tier at landing:** J — Judgment. Full ceremony.

---

**The envelope law promised that the manifest shape was fixed completely before any case is authored, and it almost was: rows, fields, ordering, opacity and binding are all law. The file that holds the rows was not. Implementation stopped at that gap before touching a single case, and this record closes it — one container, fixed in the one decision that already owned it, disturbing nothing else.**

## 1. Why implementation stopped

1. The D2-C architecture pass asked whether the exact outer JSON shape of `governance/discriminating-instrument/W8-D2-commitment-manifest.json` was already fixed by published authority. Re-grounding against every source gave the answer **no**: ADR-0055 decision 28 fixes each row (`case_id` · `reviewer_visible_sha256` · `authoring_commitment_sha256`), the sort order, class opacity and the one-to-one cross-artefact binding; Part C fixes canonical serialisation of every reviewer-visible object; the envelope module's V10 mechanics operate over row sequences — **and no published text states whether the manifest file is a bare array or a closed outer object.**

2. Because ADR-0055's decision question claims the manifest shape is **fixed completely before any case is authored**, the omission is a bounded defect in ADR-0055 itself, not a D2-C implementation choice — and choosing a container silently in D2-C was therefore barred. **Implementation stopped before the first case.** At the moment the defect was found, **no case, no nonce, no hidden authoring record, no commitment and no manifest instance existed** — the `W8-C-` namespace was and remains empty.

## 2. The reconciliation — structural and bounded, not doctrinal

3. **ADR-0055 decision 28 is expanded in place, at one site**, so that the decision which owns the manifest's rows also owns its container. The reconciled law, verbatim as inserted:

> **The manifest instance itself is one closed two-field JSON object — exactly `schema` and `rows`, with no undeclared outer or row field: `schema` byte-fixed as `w8-commitment-manifest-v1`, and `rows` the array containing exactly the rows this decision governs — serialised under Part C canonical bytes, with exactly one manifest instance for the D2-C corpus at `governance/discriminating-instrument/W8-D2-commitment-manifest.json`.**

4. **Nothing else moves.** This correction changes no class-opacity law, no commitment semantics, no custody or reveal law, no case identity or ordering law, and no other ADR-0055 decision. No decision is added and none is renumbered. **The existing V10 row law and the published envelope proof module remain historically valid and byte-untouched** — they governed rows and bindings correctly, and they still do.

5. **The D2-C corpus proof C4 will additionally enforce the newly fixed outer closed-object shape** when the corpus module lands with the corpus: exact two-field container, byte-fixed schema value, no undeclared field, canonical bytes, one instance at the fixed path. C7 is carried in its corrected form: *reviewer-surface leakage closure — no authored-class field, intended-disposition field, governed-property construction field, authoring rationale field, authoring schema, class-coded metadata or other reserved authoring material is exposed through the reviewer-visible structure or its non-evidence channels; filenames, IDs, ordering, manifest, registry and board carry no authored-class channel. Reserved authoring labels/tokens may additionally be mechanically rejected where decidable. Whether the natural-language paired evidence itself semantically discloses or over-signals the construction remains review-only; mechanical proof does not establish semantic case quality.*

## 3. Custody readiness, recorded at the architectural level

6. The existing outside-repository review transport passed its mechanics-only sentinel durability exercise before any case was authored: location **outside the repository tree** and **outside transient or session-cleanup storage**, on the existing local filesystem class at a durable per-user location; raw-byte write–close–independent-reopen–hash equality **PASS**, with the digest taken over exact retained bytes and no parse; **standard-library file I/O only — no provider, credential, secret store or new dependency**; and the procedural rule carried exactly: **written once at freeze and never reopened for write** — a discipline, since the filesystem does not itself enforce write-once semantics. The exact machine location is recorded nowhere in repository content or relay, by law.

## 4. What this amendment does not do

7. It authors no case, generates no nonce, creates no hidden authoring record, computes no commitment, materialises no manifest instance and opens no landing. **First-case authoring remains prohibited until this amendment is accepted, published and remotely verified**, and D2-C's corpus landing remains separately gated behind its own ceremony. ADR-0047 precondition 3 remains outstanding in its lawful resting state, and every carried W7 state remains exactly as the W7 closure record leaves it.

## Public-safety note

Generic and structural wording throughout — manifest, container, row, schema, transport. Barred vocabulary appears only inside prohibitions, with the two scan-sensitive families carried as stems. No real health data, no clinical examples, no identified person, no vendor or model named, no URLs, no private lineage, no credential, no machine path and no real-person content path. **Any real-person adoption is a separate governed authority outside this repository.**

---

*A law that forgets to name the envelope's envelope has not failed — it has been caught, by a builder who stopped at a missing noun with the drawer still provably empty. That is the correction path working at its cheapest: one sentence, one decision, zero cases, and nothing to unwind.*
