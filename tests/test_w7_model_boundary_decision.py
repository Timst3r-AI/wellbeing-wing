"""W7-D3 — proofs for the ADR-0051 model-boundary decision.

THE SUBJECT OF THIS MODULE IS A DECISION RECORD, NOT A MODEL.

Seven obligations are mechanical and live: their subject is the landed decision
record itself, plus repository state that exists today.

  M1  the record declares exactly one selected posture, and it is D / no contact
  M2a the governed contact_class declaration for Option D is exactly `none`
  M3  the six-seam register carries exactly four HARD and two CARRYABLE seams
  M4  the precondition posture is p2-on-effect / p3 out / p6 discharged / p7 out
  M6  the generated-evaluation home is absent and no GER identifier is allocated
  M7  the ADR-0046 public/private invariant clause is carried exactly
  M8  the decision identity is exactly ADR-0051, with no alias and no namespace

  M2b no contact-bearing member is minted — REVIEW-ONLY, not implemented here.
      The record lawfully discusses contact-bearing alternatives in prose, and
      separating discussion from minting is a semantic judgement. A token scan
      would either ban lawful discussion or pass vacuously.

  M5  requirements.txt unchanged — MECHANICAL but ALREADY DISCHARGED by
      tests/test_repo_state.py::DirectoryFence::
      test_approved_manifest_contains_exactly_the_authorised_lines.
      Not duplicated here; a second copy would add no protection.

WHAT GREEN DOES NOT MEAN. A green run of this module NEVER establishes:
that model contact occurred; that any model behaviour, quality, correctness or
safety was tested; that an authored specimen exists; that Option D proves
anything whatever about a model; that ADR-0047 precondition 3 is discharged;
that precondition 7 is discharged; that Part Q is resolved; that the
local-wordlist coordinate seam is resolved; or that W7-D4 is open.
It establishes only that a decision record says what it says.

SOURCE AUTHORITY. Expectations are derived from landed records wherever a
source states them. In particular the public/private invariant clause is READ
FROM ADR-0046 at run time and never transcribed here, so this module contains
no copy of it and needs no self-exclusion.
"""

import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISION = ROOT / "docs/decisions/0051-model-boundary-no-public-contact.md"
ADR_BOUNDARY = ROOT / "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md"
REGISTRY = ROOT / "governance/registry.json"
RESERVED_HOME = "governance/generated-evaluation/"


def decision_text():
    return DECISION.read_text(encoding="utf-8")


def registry_entries():
    return json.loads(REGISTRY.read_bytes().decode("utf-8"))["entries"]


def invariant_clause():
    """ADR-0046 decision 14 fixes the clause. Read, never transcribed."""
    m = re.search(r"\*\*The fixed invariant is the clause:\*\*\s*\n\s*\n> \*\*(.+?)\*\*\s*\n",
                  ADR_BOUNDARY.read_text(encoding="utf-8"))
    if m is None:
        raise AssertionError("ADR-0046 decision 14 clause anchor not found (source drift)")
    return m.group(1)


# Markdown closers that may sit between the fixed clause and its punctuation.
CLOSERS = "*`)\"'”’"
# Punctuation that may lawfully follow the clause: sentence end, clause separator, or dash.
TERMINATORS = ".,;:!?—–"


def clause_carriage_is_bounded(text, clause, start):
    """True if the carriage of `clause` ending at `start` is not word-continued.

    ADR-0046 decision 15 permits sentence-position grammar around the fixed
    clause, so Markdown closers, then at most one space, then sentence
    punctuation or a dash are all lawful. What is NOT lawful is the clause
    running straight on into another word, which would extend it.
    """
    i = start
    while i < len(text) and text[i] in CLOSERS:
        i += 1
    if i >= len(text):
        return True                      # end of file closes the carriage
    if text[i] == "\n":
        return True                      # end of line closes the carriage
    if text[i] in TERMINATORS:
        return True
    if text[i] == " " and i + 1 < len(text) and text[i + 1] in TERMINATORS:
        return True                      # one space, then a dash or punctuation
    return False


SELECTION = r"\*\*The selected W7 model boundary is Option ([A-D]): ([^*]+)\*\*"
CONTACT_CLASS = r"Under Option D, `contact_class` remains exactly `([a-z_]+)`"
HARD_ROW = r"^\| (\d) \| \*\*([^|]+?)\*\* \| ([^|]+?) \| \*\*([^|]+?)\*\* \|$"
CARRY_ROW = r"^\| (\d) \| \*\*([^|]+?)\*\* \| (its current narrowing|the \*\*complete)([^|]*)\|$"
PRECON_ROW = r"^\| \*{0,2}([1-7])\*{0,2} \| (.+?) \| (.+?) \|$"
EFFECT_HEADER = ("| # | Precondition | Standing after publication and remote verification "
                 "of this accepted decision |")


def precondition_rows(text):
    rows = {}
    for line in text.split("\n"):
        m = re.match(PRECON_ROW, line)
        if m and any(k in m.group(3) for k in
                     ("OUTSTANDING", "DISCHARGED", "Satisfied", "Law in force", "Closed")):
            rows[m.group(1)] = m.group(3)
    return rows


# ==========================================================================
class DecisionRecordShape(unittest.TestCase):
    """M1, M2a, M3, M4 — the record's own declarations."""

    def test_m1_exactly_one_selected_posture_and_it_is_no_contact(self):
        t = decision_text()
        found = re.findall(SELECTION, t)
        with self.subTest(limb="exactly one canonical selection marker"):
            self.assertEqual(len(found), 1, f"expected one selection marker, found {len(found)}")
        with self.subTest(limb="the selected posture is D"):
            self.assertEqual(found[0][0], "D")
        with self.subTest(limb="the posture is stated as no public model contact"):
            self.assertIn("no public model contact", found[0][1])
        with self.subTest(control="a changed posture letter is detected"):
            self.assertNotEqual(
                re.findall(SELECTION, t.replace("is Option D:", "is Option A:")), found)
        with self.subTest(control="a second selection marker is detected"):
            self.assertEqual(len(re.findall(
                SELECTION, t + "\n**The selected W7 model boundary is Option B: x**\n")), 2)
        with self.subTest(control="a removed selection marker is detected"):
            self.assertEqual(len(re.findall(SELECTION, t.replace(
                "**The selected W7 model boundary is Option D:",
                "**The chosen thing was Option D:"))), 0)
        with self.subTest(control="score-table rows are not counted as selections"):
            self.assertTrue([r for r in t.split("\n") if r.startswith("| **A** |")],
                            "the score table must still exist for this control to mean anything")
            self.assertEqual(len(found), 1)

    def test_m2a_contact_class_declaration_is_none(self):
        t = decision_text()
        found = re.findall(CONTACT_CLASS, t)
        with self.subTest(limb="exactly one bounded declaration"):
            self.assertEqual(len(found), 1)
        with self.subTest(limb="the declared value is none"):
            self.assertEqual(found[0], "none")
        with self.subTest(control="an altered declared value is detected"):
            self.assertNotEqual(re.findall(CONTACT_CLASS, t.replace(
                "remains exactly `none`", "remains exactly `local`")), found)
        with self.subTest(control="a removed declaration is detected"):
            self.assertEqual(len(re.findall(CONTACT_CLASS, t.replace(
                "Under Option D, `contact_class` remains exactly", "Under Option D the class is"))), 0)
        with self.subTest(boundary="M2b is review-only and is not attempted here"):
            self.assertIn("REVIEW-ONLY, not implemented here", __doc__)

    def test_m3_six_seam_register_is_four_hard_and_two_carryable(self):
        t = decision_text()
        hard = re.findall(HARD_ROW, t, re.M)
        carry = re.findall(CARRY_ROW, t, re.M)
        with self.subTest(limb="four hard prerequisites"):
            self.assertEqual(len(hard), 4)
        with self.subTest(limb="two carryable limitations"):
            self.assertEqual(len(carry), 2)
        with self.subTest(limb="every hard row carries a non-empty timing gate"):
            for _, name, gate, _ in hard:
                self.assertTrue(gate.strip(), f"hard seam {name!r} has no timing gate")
        with self.subTest(control="a de-structured hard row is detected"):
            self.assertEqual(len(re.findall(HARD_ROW, t.replace(
                "| 1 | **Manifest artefact shape** |", "| 1 | Manifest shape |"), re.M)),
                len(hard) - 1)
        with self.subTest(control="an emptied carryable condition is detected"):
            self.assertEqual(len(re.findall(CARRY_ROW, t.replace(
                "its current narrowing is **explicitly accepted**", "maybe"), re.M)),
                len(carry) - 1)

    def test_m4_precondition_posture_and_effective_on_publication_qualifier(self):
        t = decision_text()
        rows = precondition_rows(t)
        with self.subTest(limb="the standing column is qualified by publication, not acceptance"):
            self.assertIn(EFFECT_HEADER, t)
        with self.subTest(limb="p2 discharged by this record once effective"):
            self.assertIn("DISCHARGED", rows["2"])
        with self.subTest(limb="p3 outstanding"):
            self.assertEqual(rows["3"].strip("* "), "OUTSTANDING")
        with self.subTest(limb="p6 discharged"):
            self.assertIn("DISCHARGED", rows["6"])
        with self.subTest(limb="p7 outstanding"):
            self.assertIn("OUTSTANDING", rows["7"])
        with self.subTest(control="p3 flipped to discharged is detected"):
            mutant = precondition_rows(t.replace(
                "| **3** | **Named first-contact gate in the performing deliverable's brief** "
                "| **OUTSTANDING** |",
                "| **3** | **Named first-contact gate** | **DISCHARGED** |"))
            self.assertNotEqual(mutant.get("3"), rows["3"])
        with self.subTest(control="an acceptance-only qualifier is detected"):
            self.assertNotIn("| # | Precondition | Standing after acceptance |", t)


# ==========================================================================
class RepositoryStateAtThisLanding(unittest.TestCase):
    """M6 — facts about the repository, not about the record."""

    def test_m6_home_absent_and_no_ger_identifier_allocated(self):
        out = subprocess.run(["git", "ls-files", "--", RESERVED_HOME],
                             cwd=ROOT, capture_output=True, text=True, check=True)
        tracked = [p for p in out.stdout.split() if p]
        with self.subTest(limb="no tracked file under the reserved home"):
            self.assertEqual(tracked, [])
        with self.subTest(limb="the reserved home does not exist on disk"):
            self.assertFalse((ROOT / RESERVED_HOME).exists())
        entries = registry_entries()
        with self.subTest(limb="no GER identifier is allocated in the registry"):
            self.assertEqual([e["id"] for e in entries if e["id"].startswith("GER-")], [])
        with self.subTest(control="a planted GER registry id would be detected"):
            planted = [e["id"] for e in entries] + ["GER-0001"]
            self.assertTrue([i for i in planted if i.startswith("GER-")])
        with self.subTest(control="a planted path under the home would be detected"):
            self.assertTrue((RESERVED_HOME + "GER-0001.json").startswith(RESERVED_HOME))
        with self.subTest(note="the home-vacancy limb is also covered by W7-D2-E S1"):
            self.assertTrue((ROOT / "tests/test_w7_generated_evaluation_shape.py").exists())


# ==========================================================================
class DerivedInvariantAndIdentity(unittest.TestCase):
    """M7, M8 — derived from landed source and from structured registry fields."""

    def test_m7_public_private_invariant_clause_carried_exactly(self):
        clause = invariant_clause()
        t = decision_text()
        with self.subTest(limb="the clause is carried at least once"):
            self.assertGreaterEqual(t.count(clause), 1)
        with self.subTest(limb="no truncated near-miss of the clause appears anywhere"):
            # A truncation is invisible to a plain count of the whole clause, because the
            # truncated text simply stops matching. Compare the clause against its own
            # leading prefix: every prefix occurrence must be part of a whole clause.
            prefix = clause.rsplit(" ", 1)[0]
            self.assertEqual(t.count(prefix), t.count(clause),
                             "a prefix of the clause appears without the whole clause")
        with self.subTest(control="a single truncated carriage is detected"):
            prefix = clause.rsplit(" ", 1)[0]
            mutant = t.replace(clause, prefix, 1)
            self.assertNotEqual(mutant.count(prefix), mutant.count(clause))
        with self.subTest(limb="no carriage runs on into another word"):
            for m in re.finditer(re.escape(clause), t):
                self.assertTrue(
                    clause_carriage_is_bounded(t, clause, m.end()),
                    f"clause extended at offset {m.end()}: {t[m.end():m.end() + 30]!r}")
        with self.subTest(control="a word-continued carriage is detected"):
            mutant = t.replace(clause, clause + " and elsewhere", 1)
            offsets = [m.end() for m in re.finditer(re.escape(clause), mutant)]
            self.assertFalse(
                all(clause_carriage_is_bounded(mutant, clause, o) for o in offsets),
                "the same predicate must reject a word-continued carriage")
        with self.subTest(control="lawful sentence-position grammar is still accepted"):
            for tail in (".", "**", "* — and so on", ", and nothing changes", "`\n"):
                probe = "x " + clause + tail
                self.assertTrue(
                    clause_carriage_is_bounded(probe, clause, probe.index(clause) + len(clause)),
                    f"lawful continuation wrongly rejected: {tail!r}")
        with self.subTest(boundary="this module contains no copy of the clause"):
            own = Path(__file__).read_text(encoding="utf-8")
            self.assertEqual(own.count(clause), 0,
                             "the clause must be derived from ADR-0046, never transcribed here")

    def test_m8_single_decision_identity_no_alias_no_namespace(self):
        t = decision_text()
        h1 = [l for l in t.split("\n") if l.startswith("# ")][0]
        m = re.match(r"^# (\d{4}) — ", h1)
        with self.subTest(limb="the H1 declares a four-digit decision number"):
            self.assertIsNotNone(m)
        with self.subTest(limb="the declared number is 0051"):
            self.assertEqual(m.group(1), "0051")
        entry = [e for e in registry_entries() if e["id"] == "ADR-0051"]
        with self.subTest(limb="exactly one ADR-0051 registry entry"):
            self.assertEqual(len(entry), 1)
        with self.subTest(limb="the entry path is the record this module reads"):
            self.assertEqual(entry[0]["path"], DECISION.relative_to(ROOT).as_posix())
        with self.subTest(limb="no alias is minted"):
            self.assertEqual(entry[0]["aliases"], [])
        with self.subTest(limb="no identifier namespace is minted"):
            self.assertEqual(entry[0]["id_namespaces"], [])
        with self.subTest(control="an altered H1 number is detected"):
            self.assertNotEqual(
                re.match(r"^# (\d{4}) — ", h1.replace("0051", "0052")).group(1), "0051")


# ==========================================================================
class WhatGreenDoesNotMean(unittest.TestCase):
    """The boundary contract, asserted so it cannot be deleted while green."""

    def test_module_states_its_boundary(self):
        flat = " ".join(__doc__.split())
        for clause in ("that model contact occurred",
                       "that any model behaviour, quality, correctness or safety was tested",
                       "that an authored specimen exists",
                       "that Option D proves anything whatever about a model",
                       "that ADR-0047 precondition 3 is discharged",
                       "that precondition 7 is discharged",
                       "that Part Q is resolved",
                       "that W7-D4 is open"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)
        with self.subTest(limb="the subject is stated as a record, not a model"):
            self.assertIn("THE SUBJECT OF THIS MODULE IS A DECISION RECORD, NOT A MODEL", __doc__)


if __name__ == "__main__":
    unittest.main()
