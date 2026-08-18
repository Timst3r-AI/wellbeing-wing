"""P1 — the external-boundary invariant, exact form (ADR-0046 decisions 14, 15, 27, 28).

Scope is the invariant clause and only the clause. ADR-0046 decision 15 permits
sentence-position grammar and nothing else; this module proves that every occurrence
of the clause across tracked text is byte-exact, and fails if the permitted variation
set is ever widened.

What this module does NOT prove, stated here so no reader infers it from a green run:
P2 — the non-naming law — is review-only in full (ADR-0046 decisions 29 and 30). No
check here, and no check anywhere, discharges it. A green result means the clause is
intact. It says nothing about whether the external authority was named, described,
located, dated, or elaborated.
"""

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ADR-0046 decision 14 — the fixed invariant clause.
INVARIANT = "a separate governed authority outside this repository"

# The distinctive tail: anything reaching for the boundary must land on the full clause.
TAIL = "governed authority outside this repository"

# ADR-0046 decision 15 — the closed permitted-variation set: sentence-position grammar
# only, which for this clause means the leading article's case and nothing else.
PERMITTED_ARTICLES = ("a", "A")

TEXT_SUFFIXES = (".md", ".json", ".py")

# This module is the instrument, not the corpus. Its own source necessarily carries
# near-miss strings — the TAIL constant above, and the negative-control variants below
# that make the check bite — so scanning itself would fail on the machinery that proves
# the rule. This is the same structural situation scripts/public-safety-scan.py solves
# with its SELF_EXCLUDED set, and the same remedy, bounded identically: exactly one
# path, asserted below, so the exclusion cannot widen without this module going red.
SELF_EXCLUDED = frozenset({"tests/test_w7_boundary_invariant.py"})


def tracked_text_files():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    return [ROOT / f for f in out
            if f.endswith(TEXT_SUFFIXES) and f not in SELF_EXCLUDED]


def occurrences():
    """Yield (relative_path, matched_text) for every reach at the boundary clause."""
    for path in tracked_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(ROOT).as_posix()
        for match in re.finditer(re.escape(TAIL), text):
            start = match.start() - (len(INVARIANT) - len(TAIL))
            found = text[max(start, 0):match.end()]
            yield rel, found


class BoundaryInvariantExactForm(unittest.TestCase):
    """P1. ADR-0046 decisions 14, 15, 27, 28."""

    def test_permitted_variation_set_has_not_widened(self):
        # The guard ADR-0046 decision 27 requires: this proof fails if the set grows.
        self.assertEqual(PERMITTED_ARTICLES, ("a", "A"))
        self.assertEqual(
            INVARIANT, "a separate governed authority outside this repository"
        )

    def test_self_exclusion_is_exactly_this_module(self):
        # The scope boundary is declared, bounded, and unable to widen silently.
        self.assertEqual(len(SELF_EXCLUDED), 1)
        self.assertEqual(SELF_EXCLUDED, frozenset({"tests/test_w7_boundary_invariant.py"}))
        self.assertEqual(
            Path(__file__).resolve().relative_to(ROOT).as_posix(),
            next(iter(SELF_EXCLUDED)),
            "the excluded path must be this module and nothing else",
        )

    def test_the_clause_is_present_in_the_corpus(self):
        # A vacuous pass is not a pass: the corpus must actually carry the boundary.
        self.assertGreater(len(list(occurrences())), 0)

    def test_every_occurrence_matches_the_invariant_exactly(self):
        for rel, found in occurrences():
            with self.subTest(path=rel, found=found):
                self.assertEqual(
                    len(found), len(INVARIANT),
                    f"clause truncated or extended in {rel}: {found!r}",
                )
                self.assertIn(
                    found[0], PERMITTED_ARTICLES,
                    f"article outside the permitted set in {rel}: {found!r}",
                )
                self.assertEqual(
                    found[1:], INVARIANT[1:],
                    f"clause is not byte-exact in {rel}: {found!r}",
                )

    def test_the_check_rejects_a_synonym_and_an_expansion(self):
        # Negative control: the check must bite, not merely pass.
        for variant in (
            "a distinct governed authority outside this repository",
            "a separate and private governed authority outside this repository",
        ):
            with self.subTest(variant=variant):
                match = re.search(re.escape(TAIL), variant)
                start = match.start() - (len(INVARIANT) - len(TAIL))
                found = variant[max(start, 0):match.end()]
                self.assertNotEqual(found[1:], INVARIANT[1:])

    def test_green_here_does_not_discharge_the_non_naming_law(self):
        # ADR-0046 decisions 29 and 30, asserted against this module's own docstring so
        # the boundary between P1 and P2 cannot be quietly dropped from the file.
        self.assertIn("P2", __doc__)
        self.assertIn("review-only in full", __doc__)


if __name__ == "__main__":
    unittest.main()
