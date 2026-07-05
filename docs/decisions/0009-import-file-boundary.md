# 0009 — Import File Boundary

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster, Landing B — lands with ADR 0010) · **Blocks:** the W3-D2 engine milestone (vault store + import)

## Decision question

What does import (D1 edge E1: User → Vault) accept, what does it record, and — decisively — what is it forbidden to understand?

## Context

E1 is one line in the boundary map: "Upload of records. Encryption at the user boundary before any storage." Implementation needs the line expanded: which file forms, what metadata, and where ingestion stops and interpretation would begin. The danger is not in the accepting — it is in the helpful extras: auto-detected dates, auto-classified document types, auto-extracted titles. Each is a small unlicensed read of C4 content, and together they are extraction without a grant — E2's work done without E2's governance.

## Decision

1. **Import stores bytes plus user-supplied provenance. Nothing else.** The vault record is: the file as provided (encrypted at the boundary per ADR 0005), plus provenance the *user* supplies — source description, document date as the user states it, an optional user note — plus system facts requiring no content reading (import timestamp, file size, file-type identification per decision 3).
2. **Zero content interpretation at import.** No OCR. No text extraction. No classification. No auto-dating from content. No auto-titling from content. No thumbnail generation (also an ADR 0004 forbidden artifact class). No language detection. The import path never parses past what integrity requires.
3. **File-type identification is integrity work, not content reading:** verifying that a file's header matches its claimed type (a well-formedness check, capped at magic-number/structure depth) is permitted and required — corrupt or mistyped files are refused with an honest message. This is the full extent of permitted inspection.
4. **Accepted forms, v1 — provisional at this landing, per the reviewers' cluster decision:** PDF; PNG/JPEG; plain text and Markdown. The list hardens with the platform evidence already recorded (ADR 0008 selected the runtime; format-handling confirmation belongs to the W3-D2 engine brief). Additions later are ordinary follow-up decisions, not new doctrine, provided decisions 1–3 bind unchanged.
5. **Anything beyond this boundary is processing under grant.** Future OCR, summarisation, or auto-organisation is Z3 work on C4 content: an E2-family grant, a processing disclosure event, its own review. The import boundary is where that machinery is kept honest.
6. **Import is not validation of truth.** An imported file carries no authority — evidence is maximally sensitive and carries zero working authority until extraction and review (D3). Import surfaces must not imply the Wing "accepted" the document's contents; it accepted the bytes.
7. **Provenance posture:** source and date encouraged, note optional; an import with empty provenance is permitted but visibly labelled *unprovenanced by user*.

## Rationale

The entire authority grammar depends on evidence entering the vault *uninterpreted*: E2→E3→E4 is where interpretation is governed, labelled, and reviewed. Interpretation at import would create content-derived data with no authority label, no provenance chain, and no grant — unlabelled truth, the exact thing D3 exists to prevent. Strictness also keeps import boring, and boring is correct at the evidence layer.

## Options considered

- **(a) Bytes + user provenance only.** Accepted.
- **(b) Light metadata extraction** ("for organisation"). Rejected: unlicensed C4 reads; organisational value belongs to the user's own provenance entries or to future granted processing.
- **(c) Full ingestion pipeline at import.** Rejected: extraction without a grant; maximises residue surface at the point of maximal sensitivity.

## Accepted recommendation

Option (a), with decision 3's narrow integrity carve-out and decision 4's provisional format list.

## Consequences

Users type their own provenance — honest friction with a clean authority story. Vault browsing pre-extraction is by provenance and date, not content search (consistent with ADR 0004; the future index record inherits both constraints). Import surfaces must make provenance entry fast, because the policy makes it near-mandatory.

## Non-goals

Does not design extraction (adapter era); does not decide the future search index; does not cover room-record entry (not E1); does not define export formats.

## Implementation gates

Accepted before any E1 code. Refusal-message wording joins the governed string catalogue when that structure exists; this record is its review of record until then.

## Testing / evaluation requirements

Round-trip byte identity (bytes out == bytes in, under user key); type-verification refusal cases; a **no-interpretation structural assertion** (the import path contains no parser deeper than type verification); residue tests on the import path per ADR 0004; provenance persistence tests.

## Public-safety considerations

All import tests use synthetic files per the fixture strategy — grammar placeholders, never realistic clinical content. Refusal messages never echo file content.

## Dependencies

D1 (E1); W0 §6; D3 (evidence carries no authority); ADR 0004 (residue on the import path); ADR 0005 (encryption at the boundary); ADR 0008 (selected runtime, format confirmation venue); W2-D4 (fixtures).

## What implementation work must not do until this record is accepted

No import code; no file-parsing utilities for governed content; no format libraries; no vault write path (import is the vault write path).

## Open questions

1. Maximum file size and the refusal message (implementation detail with a surface face — decided at the engine brief, within this doctrine).
2. Whether camera capture is in v1 scope — if yes, still decision-1-bound: the photo is the bytes; no enhancement, no OCR.
