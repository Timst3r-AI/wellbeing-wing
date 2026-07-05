# Public-Safety Scan

Tooling documentation (not a governance document; not registered). The scan implements the scripted layer of checklist rule 6.

**The script supplements human review. It never replaces it.** Findings are review flags, not verdicts; the human decides.

## What it checks

Generic, public-safe pattern categories only — the public repo must not preserve the very private terms it is trying to prevent:

| Category | What it flags |
|---|---|
| `external-link` | `http(s)://` URLs and hosted-document links (the corpus uses relative links only) |
| `compliance-claim` | the words "compliant"/"compliance" — legitimate uses (anti-claims, behavioural senses, this tooling's own category names) are allowlisted narrowly |
| `claim-strength` | a named regulatory regime followed closely by claim language |
| `companion-framing` | the generic category term — legitimate self-referential uses (public-safety notes, rule text) are allowlisted narrowly |
| `real-data` | record-identifier keywords, identifier-shaped number formats, and — under `fixtures/` only — human-plausible name pairs (fixtures must use artificial identifiers like `Persona-K1`) |
| `local-wordlist` | matches from the optional local wordlist (see below); always masked; never allowlistable |

## Modes

- **Normal** (`python scripts/public-safety-scan.py`): scans all git-tracked files.
- **Landing** (`python scripts/public-safety-scan.py --landing PATH...`): scans exactly the files enumerated by a landing brief, **including untracked files, before their first commit**. No file may reach a commit merely because it was untracked and therefore invisible to the scan.

Exit codes: `0` clean, `1` findings, `2` error. Runs on Python 3 standard library only — no dependencies, no manifest, ever.

## Local wordlist contract

`<repo-root>/.public-safety.local.txt` — optional, one term per line, **never committed** (gitignored), **absence is normal and passes**. Wordlist matches are always masked in output (first character plus asterisks) and can never be allowlisted: a committed excuse for a private term would hint at the term. Even local scan logs never contain the terms in full.

## Output masking

Every reported match is masked — for example, a flagged word renders as `c*********`, an invented wordlist term `Examplename` would render as `E***********`. Category, path, and line number are sufficient for triage at the file itself. No output mode prints a matched term in full.

## Allowlist

`scripts/scan-allowlist.txt` — committed, public-safe. Format, one entry per line:

```
path | category | fingerprint | justification
```

Rules: path-scoped (one file, no globs); category-scoped; the fingerprint is a phrase the matched line contains, so the entry excuses that occurrence-class only; one-line public-safe justification required (an entry missing any field is invalid and ignored); no private term may appear anywhere in the allowlist; no directory or category-wide immunity — a new, different match in an allowlisted file is a new finding requiring its own entry. The allowlist exists to reduce false positives, never to teach the scan to look away.

`scan-allowlist.txt` itself is excluded from scanning by design: its fingerprints quote flagged phrases, so self-scanning would demand recursive entries. It is human-reviewed content under the same public-safety rules — enforced at review, stated here honestly.
