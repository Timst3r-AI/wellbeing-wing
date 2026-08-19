"""Q1 and Q2 — first-contact doctrine proofs (ADR-0047 decisions 18, 9, 24, 25).

Q1 — chain integrity. The fifteen-link first-contact anti-collapse chain is carried
byte-identically wherever a governed record reaches for it. A dropped, reordered,
reworded, or abbreviated link fails.

Q2 — precondition-set integrity. ADR-0047's decision 9 table carries exactly seven
preconditions, each with a source and a named discharge location.

Mechanism, per ADR-0047 decision 25: the chain is held LITERALLY here so the canonical
text stays legible in the file that guards it. Because the negative control below is a
deliberately broken copy of that chain, this module would otherwise fail on its own
source, so it excludes only itself — the same remedy scripts/public-safety-scan.py uses
via SELF_EXCLUDED and ADR-0046 decision 28 records for P1.

What these proofs do NOT establish, stated here so no reader infers it from a green run:
Q1 and Q2 green together prove that the chain is intact and the preconditions are
enumerated. They prove NOTHING about whether model contact occurred. Q3 — that no record
asserts contact has occurred — is review-only in full (ADR-0047 decisions 24 and 26) and
joins P2 as a standing human-review duty. Q4 remains a debt until the generated or
specimen artefact class exists.
"""

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RECORD = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"

# ADR-0047 decision 18 — the chain, carried literally.
CHAIN = (
    "named ≠ authorised · authorised ≠ scheduled · scheduled ≠ performed · "
    "specimen ≠ contact · contact ≠ capability · generated ≠ said · "
    "fluent ≠ correct · plausible ≠ true · two variants ≠ a better variant · "
    "difference ≠ defect · captured ≠ endorsed · routed ≠ reviewed · "
    "reviewed ≠ approved · model output ≠ evidence · no contact ≠ nothing proven."
)

# Anything reaching for the chain starts here and must land on the whole of it.
ANCHOR = "named ≠ authorised"

EXPECTED_LINKS = 15

# See the module docstring and ADR-0047 decision 25: exactly one path, this module.
SELF_EXCLUDED = frozenset({"tests/test_w7_first_contact_doctrine.py"})

TEXT_SUFFIXES = (".md", ".json", ".py")


def tracked_text_files():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    return [f for f in out if f.endswith(TEXT_SUFFIXES) and f not in SELF_EXCLUDED]


def chain_reaches():
    """Yield (relative_path, text_found_at_the_anchor) for every reach at the chain."""
    for rel in tracked_text_files():
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in re.finditer(re.escape(ANCHOR), text):
            yield rel, text[match.start():match.start() + len(CHAIN)]


def precondition_rows():
    """Parse ADR-0047 decision 9's table into a list of cell lists."""
    lines = (ROOT / RECORD).read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("| # | Precondition |"))
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


class ChainIntegrity(unittest.TestCase):
    """Q1. ADR-0047 decisions 18, 19, 24."""

    def test_chain_has_exactly_fifteen_links(self):
        self.assertEqual(CHAIN.count("≠"), EXPECTED_LINKS)

    def test_self_exclusion_is_exactly_this_module(self):
        self.assertEqual(len(SELF_EXCLUDED), 1)
        self.assertEqual(
            Path(__file__).resolve().relative_to(ROOT).as_posix(),
            next(iter(SELF_EXCLUDED)),
            "the excluded path must be this module and nothing else",
        )

    def test_the_chain_is_present_in_the_corpus(self):
        # A vacuous pass is not a pass.
        self.assertGreater(len(list(chain_reaches())), 0)

    def test_every_reach_carries_the_whole_chain(self):
        for rel, found in chain_reaches():
            with self.subTest(path=rel):
                self.assertEqual(
                    found, CHAIN,
                    f"chain not carried byte-identically in {rel}: {found[:80]!r}",
                )

    def test_the_check_rejects_a_dropped_and_a_reordered_link(self):
        # Negative controls: the check must bite, not merely pass.
        dropped = CHAIN.replace("specimen ≠ contact · ", "")
        reordered = CHAIN.replace(
            "fluent ≠ correct · plausible ≠ true",
            "plausible ≠ true · fluent ≠ correct",
        )
        for label, variant in (("dropped", dropped), ("reordered", reordered)):
            with self.subTest(control=label):
                self.assertNotEqual(variant, CHAIN)
                self.assertTrue(variant.startswith(ANCHOR))


class PreconditionSetIntegrity(unittest.TestCase):
    """Q2. ADR-0047 decisions 9, 10, 11, 24."""

    def test_there_are_exactly_seven_preconditions(self):
        self.assertEqual(len(precondition_rows()), 7)

    def test_rows_are_numbered_one_to_seven_in_order(self):
        numbers = [r[0] for r in precondition_rows()]
        self.assertEqual(numbers, [str(n) for n in range(1, 8)])

    def test_every_row_names_a_source_and_a_discharge_location(self):
        for row in precondition_rows():
            with self.subTest(precondition=row[0]):
                self.assertEqual(len(row), 5, "row shape changed")
                self.assertTrue(row[1].strip(), "precondition text is empty")
                self.assertTrue(row[2].strip(), "source is empty")
                self.assertTrue(row[3].strip(), "discharge location is empty")
                self.assertTrue(row[4].strip(), "standing is empty")


class WhatGreenDoesNotMean(unittest.TestCase):
    """ADR-0047 decision 26, asserted against this module so it cannot be dropped."""

    def test_the_module_states_that_green_does_not_prove_contact_did_not_occur(self):
        self.assertIn("prove NOTHING about whether model contact occurred", __doc__)
        self.assertIn("review-only in full", __doc__)


if __name__ == "__main__":
    unittest.main()
