"""W8-D1 — evaluation doctrine structural proofs (the mechanical rows of
ADR-0054 Part K: V1–V7 and V10–V12).

The doctrine is real: ADR-0054 fixes the W8 case-level vocabulary, the
recognised governed-property law with its prior-authority growth rule, the
four-category evidence architecture, the blinding law, the nine anti-collapse
rules, the human-review law and the case-independence law, before any case
exists. This module binds those load-bearing sentences to the landed bytes
mechanically, and proves the closed sets are EXACT: a fabricated fourth W8
disposition, tenth recognised property or fifth evidence category makes the
relevant proof red, demonstrated by planted-mutant negative controls. It is
derived proof, never doctrine: every canonical string and every extractor is
checked against the published ADR-0054 bytes, and nothing here re-expresses
authority. No proof here is, or may become, a semantic classifier.

WHAT GREEN DOES NOT MEAN. A green run of this module proves carriage,
byte-stability and closed-set exactness of the doctrine's structural
invariants only. It NEVER establishes: whether any difference is
governance-relevant, governance-neutral or indeterminate — that is V8, a
human semantic judgment in full; which disposition any case deserves; that
any case, fixture, corpus, calibration or execution record exists or is
lawful; that any model was contacted or behaved in any way; anything about
model safety, correctness or quality; that ADR-0047 precondition 3 moved
from its lawful resting state; that Part Q or the local-wordlist seam was
resolved; that any W7 record, disposition or unknown changed; that W8-D2 is
open; or that any disposition is a score, grade or aggregate verdict.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCTRINE = ROOT / "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"


def _lf(b):
    return b.replace(b"\r\n", b"\n")


def _text(p):
    return _lf(Path(p).read_bytes()).decode("utf-8")


W8_TOKENS = ("governance_delta_present", "no_governance_delta",
             "review_inconclusive")
ADR0053_TOKEN = "governance_delta_not_established"

_SNAKE_TOKEN_RE = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")


def disposition_like_tokens(text):
    """Every backticked snake_case token in the doctrine's bytes."""
    return _SNAKE_TOKEN_RE.findall(text)


def vocabulary_violations(text):
    """Non-empty exactly when a disposition-like token outside the authorised
    set appears anywhere in the doctrine."""
    allowed = set(W8_TOKENS) | {ADR0053_TOKEN}
    return sorted(set(disposition_like_tokens(text)) - allowed)


def recognised_properties(text):
    """The bold property names of decision 1, extracted from its own span."""
    start = text.index("presently recognised governed properties are exactly nine:")
    end = text.index("\n\n2.", start)
    return re.findall(r"\*\*([a-z][a-z ]+)\*\*", text[start:end])


def evidence_categories(text):
    """The bold category names of decision 19's four bullets."""
    start = text.index("Four evidence categories, kept distinct by law:**")
    end = text.index("\n\n20.", start)
    return re.findall(r"- +\*\*([A-Z][^*]+)\*\*", text[start:end])


NON_CONTACT_BINDINGS = (
    "**It authors no case, builds no corpus, performs no calibration, "
    "performs no review, contacts no model, and opens no later "
    "deliverable.**",
    "no model behaviour, quality, or comparison — no model was contacted "
    "and none may be under it",
    "no model prompt, contact harness, provider configuration, credential, "
    "transport, or W8-D2 brief",
)


def missing_non_contact_bindings(text):
    return [s for s in NON_CONTACT_BINDINGS if s not in text]


DEFINITIONAL = (
    "**`governance_delta_present` is lawful exactly when admissible source "
    "evidence establishes that a recognised governed property differs between "
    "the paired variants and that the difference changes a downstream "
    "obligation, permission, authority, treatment or state under the Part A "
    "test.**",
    "**`no_governance_delta` is a positive finding, defined in its own right, "
    "and never the residue left when a delta cannot be proven: admissible "
    "source evidence must affirmatively support governed equivalence "
    "— that every recognised governed property engaged by either variant has "
    "the same state in both under the downstream-obligation test.**",
    "**`review_inconclusive` is a completed, lawful disposition — not "
    "hesitation, not failure, not a pending state, and not a weaker form of "
    "either other result.**",
)

CLOSURE_SENTENCE = ("The set is **closed by this record**; any extension "
                    "requires its own governed amendment.")

NINE_RULES = ("**confidence ≠ authority · verbosity ≠ governance "
              "significance · warmth ≠ permission · explanation ≠ "
              "evidence · textual difference ≠ governance difference · "
              "textual similarity ≠ governance equivalence · absence of "
              "explicit wording ≠ absence of governed effect · mechanical "
              "agreement ≠ human acceptance · uncertainty ≠ failure.**")

EXPECTED_PROPERTIES = ["authority", "provenance", "permission", "persistence",
                       "memory treatment", "decision status",
                       "boundary crossing", "attribution", "review state"]

EXPECTED_CATEGORIES = ["Admissible source evidence",
                       "Structural and provenance support material",
                       "Withheld authoring material",
                       "Post-disposition calibration material"]

GROWTH_LAW = ("**The list is growable only, never casually extensible, and "
              "growth requires prior authority.**")
REVEAL_NEVER_EXTEND = "**it may not itself extend the law.**"
PRIOR_AUTHORITY = "lands before any evaluation case relies on that property"

SOLE_GROUNDING = ("**Reviewer disposition is grounded only in admissible "
                  "source evidence.**")
NO_CONVERSION = "**Conversion between categories does not exist in this doctrine.**"

RELATION_SENTENCES = (
    "ADR-0053 remains the undisturbed law of the published W7 "
    "generated-evaluation class",
    "**no W7 record is ever re-dispositioned under the W8 vocabulary**",
    "**`governance_delta_not_established` is not a member of the W8 vocabulary "
    "and may not be written into any W8 case; `no_governance_delta` may never "
    "be applied to the published W7 records.**",
    "**W7 remains historically true**",
)

METADATA_NON_DISCLOSURE = ("**nothing in filenames, identifiers, metadata, "
                           "ordering or other reviewer-visible material may "
                           "disclose whether a case was authored as a true "
                           "governance delta, a negative control, or a "
                           "genuinely inconclusive case.**")
POST_DISPOSITION_ONLY = ("Authoring class and intent may be revealed **only "
                         "after the disposition is recorded**")
LABEL_NEVER_EVIDENCE = ("**The authoring label is never evidence for the "
                        "answer it was designed to test**")
NO_AGGREGATE_BEFORE = ("**no aggregate output of any kind — counts, "
                       "distributions, streaks, or comparisons — before the "
                       "reviewer's dispositions for the session are complete "
                       "and recorded.**")

NEVER_DEFAULT = ("**failure to prove a delta never defaults to "
                 "`no_governance_delta`.**")
REVIEW_QUESTION = ("*on the admissible source evidence alone, does a "
                   "recognised governed property differ between the paired "
                   "variants in a way that changes a downstream obligation, "
                   "permission, authority, treatment or state?*")

CASE_ORDERING = "**Case ordering must not become hidden evidence.**"
AGGREGATE_SEQUENCING = ("**Aggregation may occur only after the session's "
                        "required individual dispositions exist, and may "
                        "never rewrite them.**")

NON_CLAIMS = (
    "This record establishes no evaluation case, no fixture, no corpus, no "
    "calibration result, no execution record, and no disposition",
    "no resolution of ADR-0047 precondition 3, which remains outstanding in "
    "its lawful resting state",
    "**No disposition ever made under this doctrine may be cited as evidence "
    "for any of those propositions.**",
)


class V1toV2_Vocabulary(unittest.TestCase):
    def test_v1_tokens_and_definitions_byte_identical(self):
        src = _text(DOCTRINE)
        for tok in W8_TOKENS:
            with self.subTest(token=tok):
                self.assertIn("`%s`" % tok, src)
        for sentence in DEFINITIONAL:
            with self.subTest(definition=sentence[:48]):
                self.assertIn(sentence, src)

    def test_v2_vocabulary_is_exactly_the_authorised_set(self):
        src = _text(DOCTRINE)
        with self.subTest(fact="closure sentence present"):
            self.assertIn(CLOSURE_SENTENCE, src)
        with self.subTest(fact="no disposition-like token beyond the "
                               "authorised set exists anywhere in the record"):
            self.assertEqual(vocabulary_violations(src), [])
        with self.subTest(fact="every authorised W8 token actually occurs"):
            found = set(disposition_like_tokens(src))
            for tok in W8_TOKENS:
                self.assertIn(tok, found)
        with self.subTest(fact="the ADR-0053 middle token appears only inside "
                               "Part E's relation law"):
            part_e = src[src.index("## Part E"):src.index("## Part F")]
            total = src.count("`%s`" % ADR0053_TOKEN)
            self.assertEqual(total, part_e.count("`%s`" % ADR0053_TOKEN))
            self.assertGreater(total, 0)
        with self.subTest(control="a fabricated fourth W8 disposition is "
                                  "detected"):
            mutated = src.replace(
                CLOSURE_SENTENCE,
                "A fourth working value `model_pass_detected` is available. "
                + CLOSURE_SENTENCE)
            self.assertEqual(vocabulary_violations(mutated),
                             ["model_pass_detected"])

    def test_v6_w7_relation_sentences(self):
        src = _text(DOCTRINE)
        for sentence in RELATION_SENTENCES:
            with self.subTest(relation=sentence[:48]):
                self.assertIn(sentence, src)


class V3_AntiCollapse(unittest.TestCase):
    def test_v3_nine_rule_block_byte_identical(self):
        src = _text(DOCTRINE)
        self.assertIn(NINE_RULES, src)
        with self.subTest(control="a block with a dropped rule is detected"):
            broken = NINE_RULES.replace(" · uncertainty ≠ failure", "")
            self.assertNotIn(broken, src.replace(NINE_RULES, ""))
        with self.subTest(control="a reworded rule is not present"):
            self.assertNotIn("uncertainty ≠ weakness", src)
        with self.subTest(fact="abbreviation-is-collapse law present"):
            self.assertIn("abbreviation is collapse by other means", src)


class V4toV5_PropertiesAndEvidence(unittest.TestCase):
    def test_v4_recognised_property_set_is_exactly_nine(self):
        src = _text(DOCTRINE)
        with self.subTest(fact="the recognised set is exactly the nine, in "
                               "order"):
            self.assertEqual(recognised_properties(src), EXPECTED_PROPERTIES)
        with self.subTest(fact="growth-requires-prior-authority law present"):
            part_a = src[src.index("## Part A"):src.index("## Part B")]
            self.assertIn(GROWTH_LAW, part_a)
            self.assertIn(PRIOR_AUTHORITY, part_a)
            self.assertIn(REVEAL_NEVER_EXTEND, part_a)
        with self.subTest(control="a fabricated tenth recognised property is "
                                  "detected"):
            mutated = src.replace(
                "**review state** (what is routed, disposed, pending, or "
                "superseded)",
                "**review state** (what is routed, disposed, pending, or "
                "superseded) · **continuity** (what carries across sessions)")
            self.assertEqual(len(recognised_properties(mutated)), 10)
            self.assertNotEqual(recognised_properties(mutated),
                                EXPECTED_PROPERTIES)

    def test_v5_evidence_architecture_is_exactly_four_categories(self):
        src = _text(DOCTRINE)
        with self.subTest(fact="the categories are exactly the four, in "
                               "order"):
            self.assertEqual(evidence_categories(src), EXPECTED_CATEGORIES)
        with self.subTest(fact="sole-grounding and no-conversion laws "
                               "present"):
            part_f = src[src.index("## Part F"):src.index("## Part G")]
            self.assertIn(SOLE_GROUNDING, part_f)
            self.assertIn(NO_CONVERSION, part_f)
        with self.subTest(control="a fabricated fifth evidence category is "
                                  "detected"):
            mutated = src.replace(
                "    - **Post-disposition calibration material**",
                "    - **Ambient context material** — whatever surrounds the "
                "case.\n    - **Post-disposition calibration material**")
            self.assertEqual(len(evidence_categories(mutated)), 5)
            self.assertNotEqual(evidence_categories(mutated),
                                EXPECTED_CATEGORIES)


class V7_BlindingAndReviewProtections(unittest.TestCase):
    def test_v7_blinding_and_no_aggregate_before_completion(self):
        src = _text(DOCTRINE)
        part_h = src[src.index("## Part H"):src.index("## Part I")]
        with self.subTest(fact="metadata non-disclosure law present"):
            self.assertIn(METADATA_NON_DISCLOSURE, part_h)
        with self.subTest(fact="post-disposition-only reveal present"):
            self.assertIn(POST_DISPOSITION_ONLY, part_h)
        with self.subTest(fact="authoring-label-never-evidence law present"):
            self.assertIn(LABEL_NEVER_EVIDENCE, part_h)
        with self.subTest(fact="no-aggregate-before-completion law present"):
            self.assertIn(NO_AGGREGATE_BEFORE, part_h)


class V11_QuestionAndNeverDefault(unittest.TestCase):
    def test_v11_exact_review_question_and_never_default(self):
        src = _text(DOCTRINE)
        with self.subTest(fact="the exact human review question is present"):
            self.assertIn(REVIEW_QUESTION, src)
        with self.subTest(fact="the never-default law is present"):
            self.assertIn(NEVER_DEFAULT, src)
        with self.subTest(fact="elimination is barred"):
            self.assertIn("**Neither substantive disposition may be reached "
                          "by elimination.**", src)


class V12_CaseIndependence(unittest.TestCase):
    def test_v12_case_independence_and_aggregate_sequencing(self):
        src = _text(DOCTRINE)
        part_i = src[src.index("## Part I"):src.index("## Part J")]
        with self.subTest(fact="case-ordering law present"):
            self.assertIn(CASE_ORDERING, part_i)
        with self.subTest(fact="aggregate-sequencing law present"):
            self.assertIn(AGGREGATE_SEQUENCING, part_i)


class V10_NonClaimsAndCorrections(unittest.TestCase):
    def test_v10_non_claims_carried(self):
        src = _text(DOCTRINE)
        for sentence in NON_CLAIMS:
            with self.subTest(non_claim=sentence[:48]):
                self.assertIn(sentence, src)
        with self.subTest(fact="V8 honesty: the human judgment is declared "
                               "review-only in the proof table"):
            self.assertIn("**Review-only, in full.** This is the human "
                          "semantic judgment itself", src)

    def test_v10_no_contact_and_no_later_deliverable_bindings_bite(self):
        src = _text(DOCTRINE)
        with self.subTest(fact="all no-contact / no-contact-authority / "
                               "no-W8-D2 bindings present"):
            self.assertEqual(missing_non_contact_bindings(src), [])
        for sentence in NON_CONTACT_BINDINGS:
            with self.subTest(control="removal is detected: "
                                      + sentence[:40]):
                mutated = src.replace(sentence, "")
                self.assertEqual(missing_non_contact_bindings(mutated),
                                 [sentence])

    def test_four_bound_corrections_present(self):
        src = _text(DOCTRINE)
        with self.subTest(correction="1: prior authority before property growth"):
            self.assertIn(PRIOR_AUTHORITY, src)
            self.assertIn(REVEAL_NEVER_EXTEND, src)
        with self.subTest(correction="2: surface features not themselves "
                                     "governed properties; property change "
                                     "controls"):
            self.assertIn("**Surface features are not governed properties in "
                          "themselves.**", src)
            self.assertIn("the governed-property change controls", src)
        with self.subTest(correction="3: conflict means unresolved conflict "
                                     "within admissible source evidence"):
            self.assertIn("**unresolved conflict within admissible source "
                          "evidence**", src)
            self.assertNotIn("conflict between evidence classes", src)
        with self.subTest(correction="4: pre-disposition blinding with "
                                     "post-disposition reveal"):
            self.assertIn("is withheld from the reviewer before disposition",
                          src)
            self.assertIn(POST_DISPOSITION_ONLY, src)
        flat = " ".join(__doc__.split())
        for clause in ("whether any difference is governance-relevant",
                       "which disposition any case deserves",
                       "that any model was contacted",
                       "that ADR-0047 precondition 3 moved",
                       "that W8-D2 is open",
                       "score, grade or aggregate verdict"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)


if __name__ == "__main__":
    unittest.main()
