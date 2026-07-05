#!/usr/bin/env python3
"""Public-safety scan for this repository.

Report-only. Python 3 standard library only. No dependencies, ever.

Modes:
  normal   (default)        scan all git-tracked files
  landing  --landing P...   scan exactly the given paths (tracked or not),
                            as enumerated by a landing brief, before commit

The scan supplements human review; it never replaces it. Findings are
review flags, not verdicts. Exit codes: 0 clean, 1 findings, 2 error.

Optional local wordlist: <repo-root>/.public-safety.local.txt
  - one term per line; never committed (gitignored); absence is normal
  - wordlist matches are always masked and can never be allowlisted

Allowlist: scripts/scan-allowlist.txt (committed, public-safe)
  - format: path | category | fingerprint | justification
  - path-scoped (one file, no globs), category-scoped, phrase-scoped
  - an entry with any empty field is invalid and ignored with a warning

Output masking: every reported match is masked (first character plus
asterisks). No output mode prints a matched term in full; category,
path, and line number are sufficient for human triage at the file.

Self-scan note: the scan's own source and README are scanned like any
tracked file (their category-name mentions are allowlisted, narrowly).
scripts/scan-allowlist.txt itself is excluded from scanning by design:
its entries quote fingerprints, so scanning it would demand recursive
self-entries; it is human-reviewed content under the same public-safety
rules, enforced at review rather than by self-reference.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWLIST_PATH = REPO_ROOT / "scripts" / "scan-allowlist.txt"
WORDLIST_PATH = REPO_ROOT / ".public-safety.local.txt"
SELF_EXCLUDED = {"scripts/scan-allowlist.txt"}

# Public, generic pattern categories. Never add a private term here:
# the public repo must not preserve the very terms it prevents.
PATTERNS = [
    ("external-link", re.compile(r"https?://|docs\.google", re.IGNORECASE)),
    ("compliance-claim", re.compile(r"\bcomplian(?:t|ce)\b", re.IGNORECASE)),
    ("claim-strength", re.compile(
        r"\b(?:HIPAA|GDPR|APP)\b.{0,60}?(?i:\bcompliant\b|\bcompliance\b|\bcertified\b)")),
    ("companion-framing", re.compile(r"\bcompanion\b", re.IGNORECASE)),
    ("real-data", re.compile(
        r"\bDOB\b|\bMRN\b|\bdate of birth\b|\bmedical record number\b|\b\d{3}-\d{2}-\d{4}\b",
        re.IGNORECASE)),
]
# Applied only under fixtures/: human-plausible name pairs are always findings there.
FIXTURES_NAME_PATTERN = ("real-data", re.compile(r"\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b"))


def mask(text):
    text = text.strip()
    if not text:
        return "(empty)"
    return text[0] + "*" * min(len(text) - 1, 11)


def load_allowlist():
    entries, warnings = [], []
    if not ALLOWLIST_PATH.exists():
        return entries, warnings
    for n, raw in enumerate(ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4 or not all(parts):
            warnings.append(f"allowlist line {n}: invalid entry ignored (needs 4 non-empty fields)")
            continue
        path, category, fingerprint, _justification = parts
        if "*" in path or "?" in path:
            warnings.append(f"allowlist line {n}: glob paths are not permitted; entry ignored")
            continue
        entries.append((path.replace("\\", "/"), category, fingerprint))
    return entries, warnings


def load_wordlist():
    if not WORDLIST_PATH.exists():
        return []  # absence is normal and passes
    terms = []
    for raw in WORDLIST_PATH.read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if t and not t.startswith("#"):
            terms.append(t)
    return terms


def tracked_files():
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files"],
        capture_output=True, text=True, check=True)
    return [REPO_ROOT / p for p in out.stdout.splitlines() if p]


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None  # binary or unreadable: skipped, reported in summary


def scan_file(path, rel, wordlist, allowlist):
    findings, suppressed = [], 0
    text = read_text(path)
    if text is None:
        return None, 0
    is_fixture = rel.startswith("fixtures/")
    for lineno, line in enumerate(text.splitlines(), 1):
        checks = list(PATTERNS)
        if is_fixture:
            checks.append(FIXTURES_NAME_PATTERN)
        for category, pattern in checks:
            for m in pattern.finditer(line):
                if any(p == rel and c == category and f in line
                       for p, c, f in allowlist):
                    suppressed += 1
                    continue
                findings.append((rel, lineno, category, mask(m.group(0))))
        for term in wordlist:
            if term.lower() in line.lower():
                # never allowlistable, always masked
                findings.append((rel, lineno, "local-wordlist", mask(term)))
    return findings, suppressed


def main():
    ap = argparse.ArgumentParser(description="Public-safety scan (report-only).")
    ap.add_argument("--landing", nargs="+", metavar="PATH",
                    help="landing mode: scan exactly these files (tracked or not)")
    args = ap.parse_args()

    if args.landing:
        paths = []
        for p in args.landing:
            fp = Path(p)
            if not fp.is_absolute():
                fp = REPO_ROOT / p
            if not fp.exists():
                print(f"error: landing path does not exist: {p}", file=sys.stderr)
                return 2
            paths.append(fp)
        mode = "landing"
    else:
        paths = tracked_files()
        mode = "normal"

    allowlist, warnings = load_allowlist()
    wordlist = load_wordlist()

    all_findings, total_suppressed, skipped = [], 0, []
    for fp in paths:
        try:
            rel = fp.resolve().relative_to(REPO_ROOT).as_posix()
        except ValueError:
            rel = fp.resolve().as_posix()  # outside repo (landing mode): scanned, shown absolute
        if rel in SELF_EXCLUDED:
            continue
        result, suppressed = scan_file(fp, rel, wordlist, allowlist)
        if result is None:
            skipped.append(rel)
            continue
        all_findings.extend(result)
        total_suppressed += suppressed

    for w in warnings:
        print(f"warning: {w}")
    for rel, lineno, category, masked in all_findings:
        print(f"{rel}:{lineno}: [{category}] {masked}")
    print(f"-- scan mode: {mode}; files scanned: {len(paths)}; "
          f"findings: {len(all_findings)}; allowlist-suppressed: {total_suppressed}; "
          f"binary/skipped: {len(skipped)}; local wordlist: "
          f"{'present' if wordlist else 'absent (normal)'}")
    if all_findings:
        print("-- findings are review flags, not verdicts; the human decides.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
