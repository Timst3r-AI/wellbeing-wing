# External Assurance Source Register

**Status:** Accepted by human reviewer, 2026-08-10. Not a build instruction. Authorises no implementation.
**Date:** 2026-08-10 · **Phase:** W4 — Room Contracts (deliverable W4-D6, Lane C)
**Scope:** Documentation only. This register records the provenance and currency of external
authoritative sources consulted by the Wing's privacy and health-data assurance work. It creates
no data category, edge, class, authority state, permission, or implementation.

---

## 1. Governing boundary

**Source registration records provenance and currency. It does not certify compliance. It does
not determine applicability. The presence of a source in this register does not mean a legal
requirement applies to the Wing. A source register is evidence provenance — never legal authority
delegated to the Wing.** The Wing's constitutional posture governs every use of this register: it
is designed to privacy-by-design principles *aligned with* the named frameworks and makes no
certified-compliance claim (W0 §2 non-goal 7, §9).

## 2. Schema and identifier semantics

Each entry carries exactly twelve fields: `source_id`, `authority_publisher`, `title`,
`canonical_locator`, `jurisdiction_framework`, `source_kind`, `currency_status`,
`publication_version_date`, `retrieval_date`, `reverification_date`, `supersession`,
`dependent_rows`.

- `source_kind` distinguishes what a source **is**: `law_or_rule`, `regulator_guidance`,
  `engineering_standard`, `proposed_rule`. A proposed rule is a kind, never a successor to
  current law.
- `currency_status` is the separate axis of whether a source **currently stands**: `current`
  or `superseded`.
- Absence is explicit, never silent: `supersession = null` where no successor has taken effect;
  `dependent_rows = []` where no accepted assurance row yet depends on the source. An empty
  dependent-row set is not evidence a source is unnecessary.
- **Identifier rule:** `SRC-<FAMILY>-<NN>`, family in the fixed taxonomy order
  {HIPAA, HBNR, APP, GDPR, NIST}; `<NN>` is the stable allocation sequence within its family —
  an allocation identifier, never a ranking. Identifiers are immutable once accepted; a new
  source receives the next unused number in its family; existing sources are never renumbered;
  the numeric suffix carries no authority, priority, chronology, or legal significance.

## 3. Registered sources

```json
[
  {"source_id": "SRC-HIPAA-01", "authority_publisher": "HHS/OCR via eCFR",
   "title": "45 CFR Part 160 — General Administrative Requirements",
   "canonical_locator": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "eCFR current codification as at 2026-08-09",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-02", "authority_publisher": "HHS/OCR via eCFR",
   "title": "45 CFR Part 164 — Security and Privacy (Subparts C, D, E)",
   "canonical_locator": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "eCFR current codification as at 2026-08-09",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-03", "authority_publisher": "HHS/OCR",
   "title": "Summary of the HIPAA Privacy Rule",
   "canonical_locator": "https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "guidance page; underlying rule published 2000-12-28, modified 2002-08-14",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-04", "authority_publisher": "HHS/OCR",
   "title": "Minimum Necessary Requirement guidance (45 CFR 164.502(b), 164.514(d))",
   "canonical_locator": "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "guidance page (undated)",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-05", "authority_publisher": "HHS/OCR",
   "title": "Guidance Regarding Methods for De-identification of PHI (45 CFR 164.514(a)-(c))",
   "canonical_locator": "https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "guidance issued 2012-11-26",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-06", "authority_publisher": "HHS/OCR",
   "title": "Breach Notification Rule guidance",
   "canonical_locator": "https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "guidance page; underlying rule 2009 (HITECH), as codified",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HIPAA-07", "authority_publisher": "HHS/OCR via Federal Register",
   "title": "HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information (NPRM)",
   "canonical_locator": "https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information",
   "jurisdiction_framework": "US-federal / HIPAA-aligned", "source_kind": "proposed_rule",
   "currency_status": "current", "publication_version_date": "issued 2024-12-27; published 2025-01-06; comments closed 2025-03-07",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HBNR-01", "authority_publisher": "FTC via eCFR",
   "title": "16 CFR Part 318 — Health Breach Notification Rule",
   "canonical_locator": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-318",
   "jurisdiction_framework": "US-federal / FTC-HBNR", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "2024 amendments effective 2024-07-29 (final rule published 2024-05-30)",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-HBNR-02", "authority_publisher": "FTC",
   "title": "Complying with FTC's Health Breach Notification Rule",
   "canonical_locator": "https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0",
   "jurisdiction_framework": "US-federal / FTC-HBNR", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "post-2024-amendment guidance",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-APP-01", "authority_publisher": "Federal Register of Legislation (AU)",
   "title": "Privacy Act 1988 (Cth), Schedule 1 — Australian Privacy Principles",
   "canonical_locator": "https://www.legislation.gov.au/C2004A03712/latest",
   "jurisdiction_framework": "AU-Commonwealth / APP-aligned", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "Compilation No. 104 (C2026C00227), in force 2026-06-04, registered 2026-06-17",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-APP-02", "authority_publisher": "OAIC",
   "title": "Australian Privacy Principles Guidelines",
   "canonical_locator": "https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines",
   "jurisdiction_framework": "AU-Commonwealth / APP-aligned", "source_kind": "regulator_guidance",
   "currency_status": "current", "publication_version_date": "progressively updated; Chapter 3 updated 2026-05-13",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-APP-03", "authority_publisher": "Federal Register of Legislation (AU)",
   "title": "Privacy and Other Legislation Amendment Act 2024 (Cth)",
   "canonical_locator": "https://www.legislation.gov.au/C2024A00128/asmade",
   "jurisdiction_framework": "AU-Commonwealth / APP-aligned", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "2024 (as made)",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-GDPR-01", "authority_publisher": "EUR-Lex (EU)",
   "title": "Regulation (EU) 2016/679 (General Data Protection Regulation)",
   "canonical_locator": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng",
   "jurisdiction_framework": "EU / GDPR-style", "source_kind": "law_or_rule",
   "currency_status": "current", "publication_version_date": "2016-04-27; consolidated text CELEX 02016R0679-20160504",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []},

  {"source_id": "SRC-NIST-01", "authority_publisher": "NIST CSRC",
   "title": "NIST SP 800-122 — Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)",
   "canonical_locator": "https://csrc.nist.gov/pubs/sp/800/122/final",
   "jurisdiction_framework": "US-NIST / engineering baseline", "source_kind": "engineering_standard",
   "currency_status": "current", "publication_version_date": "Final, 2010-04",
   "retrieval_date": "2026-08-09", "reverification_date": "2026-08-09",
   "supersession": null, "dependent_rows": []}
]
```

Research-label mapping (annotation only): SRC-HIPAA-01↔S1 · 02↔S2 · 03↔S3 · 04↔S4 · 05↔S5 · 06↔S6 · 07↔S7 · SRC-HBNR-01↔S8 · 02↔S9 · SRC-APP-01↔S10 · 02↔S11 · 03↔S12 · SRC-GDPR-01↔S13 · SRC-NIST-01↔S14.

## 4. Maintenance rules

1. Entries change only through governed register updates landed by ceremony — never by silent
   edit and never by self-adjustment from any consuming artefact.
2. A superseded or materially changed source routes every dependent assurance row back to
   review; supersession is recorded visibly via the `supersession` pointer and
   `currency_status`, never by silent replacement.
3. Re-verification against the primary source is required before any acceptance-grade use of an
   entry; `reverification_date` records the most recent verification. No expiry interval is
   invented: no accepted source authorises one.
4. Only primary authoritative sources are registrable. Secondary commentary may aid discovery
   but never becomes register authority.

## 5. Horizon and re-verification evidence

Recorded as supporting governance evidence — never as additional register fields:

1. **HIPAA Security Rule NPRM (SRC-HIPAA-07):** a proposed rule, still pending as verified
   2026-08-09; the current Security Rule remains operative. Re-verify before any later
   acceptance-grade reliance if materially delayed.
2. **NIST SP 800-122 (SRC-NIST-01):** NIST has stated an intention to consolidate its guidance
   into a future SP 800-60 revision and withdraw SP 800-122. No actual supersession has
   occurred; a real currency event flows through a governed register update.
3. **APP 1.7–1.9:** automated-decision transparency obligations commence 2026-12-10. Outside
   the active assurance mapping set (APP 3/6/11/12/13); carried for later doctrinal review only;
   not a finding that the Wing is an APP entity.
4. **OAIC APP guidance (SRC-APP-02):** actively updated through 2026; re-verify relevant
   chapters wherever a mapping relies on them.

## 6. Public-safety note

This register contains no private names, no private system references, no companion framing, no
personal health details, and no project lineage beyond this repository. Canonical locators are
official primary-source addresses recorded as provenance; the path segment `eli` appearing in
the EUR-Lex locator is the EU's European Legislation Identifier scheme. Entries describe
documents about law and guidance, never people.
