"""W8-D6-A — contact-decision opening brief proofs (W8-D6-CDB, CD1–CD8).

The opening landing of W8-D6: the brief that fixes the contact decision's
question, its closed three-outcome form, the published basis the decision
may rest on, what each outcome would and would not do, the limits, the
human decision points and the stop conditions; and the one proof
succession the placeholder probe found a W8-D6 opening to need - ADR-0058's
R9 later-deliverable limb, its sentence and constant unchanged. This module
proves the brief's carriage, its closed outcome list and the absence of
preselecting wording; its non-authorisations; its exposure limits, with the
one trusted succession row and the trusted basis rows as the only digest
exemptions; that every case home, register, revealed record and earlier
W8-D3, W8-D4, W8-D5 and erratum record is byte-unchanged and that the basis
table is exactly its trusted rows resolving to their pinned objects; the
exact R9 succession and its closed table; and the exact registry, board and
census - each with planted-mutant or negative controls. Closed validators
compare against trusted expected values held here and refuse unrecognised
material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the brief
afterwards - and executes the helpers it relies on from that snapshot's
bytes, in a private namespace. CD7's W8-D6 entry set is the one
present-state gate, as the W8-D4 and W8-D5 openings' were, until the
decision landing moves it. The residual live reach is disclosed exactly:
each snapshot-executed helper module imports, at its own top level, the
live modules it aliases for the fixed-law values it reads from them, and no
more independence than that is claimed.

CD1's numbered-item pattern admits exactly CommonMark's ordered marker in
this brief's form - one to nine ASCII digits, a full stop and a space - so
that a line a Markdown reader folds into a protected item is never taken
for the next item's boundary. CD1's preselection scan sets aside the pinned
outcome lines, whose exact text the closed list already proves, and the
runway's own quoted sentence, and reads everything else through a bounded
fold - emphasis and code marks and the invisible code points removed, every
whitespace run one space, case folded - so that ordinary formatting hides
no inventoried phrase (the r1 review's F-2). Conformance to that bounded
inventory is never proof that arbitrary prose contains no recommendation.

CD3 reads every surface as logical prose paragraphs - blocks parted by
blank lines, empty or SPACE/TAB-only as CommonMark defines them, with every
whitespace run inside a block made one space - so that a soft line break,
continuation indentation or a separator line of no-break spaces, em spaces
or form feeds hides no figure or count from it (the r1 review's F-1). The
paragraph helper is locally owned and mirrors the published review-law
helper; the exempt exact rows survive the paragraph form unchanged.

This landing's derived public baseline is the published W8-D5 completion,
which is also the R9 succession's historical anchor, D5_COMPLETION, as the
W8-D3 completion was the W8-D4 opening's; CD5 proves the two equal and
proves that no W8-D6 or W8-D7 entry existed at it.

CD2 reads section 12 as one whole block - heading, blank separator,
introducing item, the thirteen non-authorisations, blank separator, closing
sentence and trailing separator, in that order and nothing else - so that
unmarked prose, a permission sentence, a differently indented bullet or a
line at either edge of the block is refused rather than skipped.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity,
schema literal or method label as a literal, and no disposition token. It
takes no decision and selects no outcome.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any contact decision, or which outcome is right; that
contact is warranted, unwarranted, ready or foreclosed; anything about any
model, case, disposition, divergence or reviewer; that any model was
contacted; that any ADR-0047 precondition moved; or that W8-D7 may open.
"""

import hashlib
import importlib
import json
import re
import subprocess
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified W8-D5 completion: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
# The R9 succession's historical anchor: the W8-D5 completion, which is this
# landing's baseline (as the W8-D3 completion was the W8-D4 opening's).
D5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"

BRIEF = "docs/phases/W8-D6-contact-decision-brief.md"
SELF_REL = "tests/test_w8_contact_decision_opening.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({BRIEF, SELF_REL, RECOVERY, REGISTRY, BOARD})
D6_ENTRIES = frozenset({"W8-D6-CDB"})
LATER_THAN_D6 = ("W8-D7",)
FIXED_HOMES = ("governance/validation-cases", "governance/validation-review",
               "governance/validation-reveal",
               "governance/discriminating-instrument",
               "governance/discriminating-supplement",
               "governance/discriminating-reveal",
               "governance/discriminating-review")
FIXED_RECORD_IDS = ("W8-AR", "ADR-0047", "ADR-0046", "ADR-0033", "ADR-0034",
                    "ADR-0049", "ADR-0051", "ADR-0054", "ADR-0055", "ADR-0057",
                    "ADR-0058", "ADR-0059", "ADR-0060", "ADR-0061", "W8-D3-SCB",
                    "W8-D3-HDR", "W8-D3-CCR", "W8-D4-IVB", "W8-D4-VCR",
                    "W8-D4-VSR", "W8-D4-VRC", "W8-D4-CPR", "W8-CHC", "W8-DER",
                    "W8-D5-EAB", "W8-D5-AFR", "W8-D2-CBC", "ADR-0056", "W7-CR",
                    "W7-D3-MBB")

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py"}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    RECOVERY: ("session-recovery module",
               "sha256:a1efe9fb15e75868acfb763c37735e648baa7bea62fe1b1357d80f078c2e6537",
               "b8a20d4b97585b6ef51476ebbcf407a7b6d32246"),
    REGISTRY: ("registry",
               "sha256:3c59bd26747344314be767dfe4223feb11c3f939b5c658543c5a96454287a21b",
               "86c6660ea60d551ed9e724e6263a5cc4a082e597"),
    BOARD: ("board",
            "sha256:dc577374b2e5a222f2982fe5d2dcea8cdc4b64ae3660447eaa1ad48d7a105f28",
            "1ae23ad1984106414692c4cd5f23b4fc22f64e37"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {RECOVERY: ("sha256:25bc3f70d043c854471748bdf6a6c1fe6e7864ce047007df19348dbd66293261", "055f57d7e07311f6a6224fc7e173d2c8bbe4dd1f")}

# ------------------------------------------ the one succession: ADR-0058 R9
SITES = {
    RECOVERY: (
        ('R9',
         '# Succeeded again at the W8-D5 opening (W8-D5-EAB section 8): the\n# absence of every W8-D5 to W8-D7 entry stays proven at the W8-D4\n# completion.\nD4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"\n',
         '# Succeeded again at the W8-D5 opening (W8-D5-EAB section 8): the\n# absence of every W8-D5 to W8-D7 entry stays proven at the W8-D4\n# completion.\nD4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"\n# Succeeded again at the W8-D6 opening (W8-D6-CDB section 9): the\n# absence of every W8-D6 and W8-D7 entry stays proven at the W8-D5\n# completion.\nD5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"\n'),
        ('R9',
         '        with self.subTest(fact="no registry entry opens W8-D6 or "\n                               "W8-D7"):\n            self.assertEqual([e["id"] for e in entries\n                              if e["deliverable"] in LATER[2:]], [])\n',
         '        # Succeeded again at the W8-D6 opening landing: the absence of\n        # every W8-D6 and W8-D7 entry stays proven at the W8-D5\n        # completion commit; W8-D6\'s entry set moves to that landing\'s\n        # own proof module, and W8-D7 stays unopened.\n        with self.subTest(fact="no registry entry opened W8-D6 or "\n                               "W8-D7 at the W8-D5 completion"):\n            at_d5 = json.loads(packet.committed_object_bytes(\n                ROOT, D5_COMPLETION, "governance/registry.json"))[\n                "entries"]\n            self.assertEqual([e["id"] for e in at_d5\n                              if e["deliverable"] in LATER[2:]], [])\n        with self.subTest(fact="no registry entry opens W8-D7"):\n            self.assertEqual([e["id"] for e in entries\n                              if e["deliverable"] in LATER[3:]], [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_LINE = 'R9_REVEAL = "%s"\n' % R9_SENTENCE

# ---------------------------------------------------------- the basis rows
# Trusted rows of the brief's section 3 table: (number, identity, path,
# commit at which the path's published bytes last changed, blob, raw
# SHA-256 of the committed bytes). Every object is byte-identical at
# BASELINE.
BASIS_SECTION = "## 3. The published basis"
BASIS_HEADER = "| # | Identity | Published path | Commit | Object | Raw SHA-256 |"
BASIS_SEPARATOR = "|---|---|---|---|---|---|"
BASIS_ROWS = (
    (1, "W8-D5-AFR", "docs/phases/W8-D5-adequacy-finding-record.md",
     "2aa2c75d20363ca7e54095f49b328bdd4db1350a", "9fbd1016bb58ae06d9e557ebd281f707f54b8fc5",
     "sha256:197254b69161aacef79dbb93c86939c4cc1b82e9cc39ac2fa0584207ea6cc558"),
    (2, "ADR-0061", "docs/decisions/0061-w8-evidence-adequacy-review-law.md",
     "18d6230b5f7281577c18892dd7b95e9448f310c2", "aec015d014c098b183deeb119a6c6293f4e4b6bb",
     "sha256:b81af71545cfc21d3311275110e66dc0768d87d24f1954138e95783773cf95d9"),
    (3, "W8-D5-EAB", "docs/phases/W8-D5-evidence-adequacy-brief.md",
     "c8e13d47f305e0378609ffec1d31f890f629239d", "78a78b2179740e769ef42bd2ed5944cb04fd71b8",
     "sha256:339c93d624f56f07165aa81696fb2f464cfec1fef2148ceace2b4222b8efe60a"),
    (4, "W8-AR", "docs/phases/W8-runway-generative-evaluation-maturity.md",
     "117a192091bfafa80cb3f6ae567b63204b6c7676", "da34be5dee7db4a94b4276f4024dd48e3076883a",
     "sha256:fda68f9d1e69c166587cfb746d7d1830b39ea99d9c4c6a9129a0b75d34eba24e"),
    (5, "ADR-0047", "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md",
     "02b58ccc9f37f46a72b79b9e61e6028057d313b7", "5f1fb5581a98ea8d9f03d97ad39a4bc39158c079",
     "sha256:63f8c84fe2a3235d69340e4bcbcb4cd1d2497ff46b89876ac128b097f6c72a35"),
    (6, "ADR-0046", "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md",
     "953efc928867f9a05321065b7ef4cc6515a09b3d", "14c1208e81fb59763a1f78ee3676276149b75b08",
     "sha256:b2bac9e3bbf3fd3cd3991c174671f2dbbbde3832363ef3df93cb67cde3de5270"),
    (7, "ADR-0033", "docs/decisions/0033-model-access.md",
     "1d4b19c45c4e12e777de654358d2c4a7562cd60a", "aefac956a771819d9116c22fc2dd49084efb97e8",
     "sha256:1ce7c980b3e45342e5fe485d053d9f4ef3ab887015914158a5146345a076ceba"),
    (8, "ADR-0034", "docs/decisions/0034-behavioural-evaluation-architecture.md",
     "6230d42649c0bc5d55250952c7b49d26412a8bb0", "92ad83d996e64f7671fb108fae0efe4766fc63a5",
     "sha256:650d51c916a74618a9967b9238d5acd727ba7d5b2c1362d94ed92255d906e982"),
    (9, "ADR-0049", "docs/decisions/0049-generated-evaluation-field-law.md",
     "a6de4c6e84d6691e0ddce6a9a30b5adada1d27bd", "abdfc33fab988e80dd0012a6dd23fbc38d73e28a",
     "sha256:bca3d94732bc95737ef77a5a0ae74561b91ddf3d62b0862d76cdfef9618af1d9"),
    (10, "ADR-0051", "docs/decisions/0051-model-boundary-no-public-contact.md",
     "e1dd86d561e458babdcfa56e6923aba9fb6f63b2", "2800a8260fc4379133fce418ea3e20fe5929e607",
     "sha256:a1af46b27a52fed4a1bb0f30c9b449148ba8178ddffddbcc76a1acbb634efda6"),
    (11, "ADR-0054", "docs/decisions/0054-generative-evaluation-maturity-doctrine.md",
     "6e9e0f155944bea3117b82a5b4216ce6c50abaa4", "77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43",
     "sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd"),
    (12, "ADR-0058", "docs/decisions/0058-w8-d3-session-recovery-law.md",
     "897f0b14a66ee956bd9fe36e63975b04d5dc9663", "5f8f0786b1bd8091696fe45cb05a388bb776b8b6",
     "sha256:6291da0206c576be10c6c5eea8a1e71490f836e20430663a8eb5038f49877cd3"),
    (13, "W8-D4-CPR", "docs/phases/W8-D4-completion-record.md",
     "ce78a242df25898d90debee9513bdce7e511471b", "14e49308ed63a4411400f769f25fda8095d74efb",
     "sha256:dd8a577de367946f5a7f5331a06a6a8df49fbe1b899dd6e6db2d527e62618471"),
    (14, "W7-CR", "docs/phases/W7-closure-record.md",
     "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3", "f57ea174237205f2d4e0783f48469ab84abe5c97",
     "sha256:8086966f2355c59d2c8ea34593d177446cac0ec9707977b27d186b7e0d96200a"),
    (15, "W7-D3-MBB", "docs/phases/W7-D3-model-boundary-opening-brief.md",
     "5ce8a923e8a52bf17e9b4c1bd81d1e714c79b135", "dd05f5732bdbaf50971b2fd898c162ca5eeb0524",
     "sha256:593a4b49605672301c1f15bfe5affe8f60cbc0ab737a3e2c6ac4192616487e30"),
)

# --------------------------------------------------------------- carriage
RUNWAY_SENTENCE = ("A separately governed decision — contact, defer, or determine "
                   "that contact would presently add insufficient value.")
REQUIRED = (
    "W8-D6 opens for contact-decision work only, through the landing programme "
    "of section 10. W8-D7 remains closed.",
    "This brief itself takes no contact decision, selects no outcome, authorises "
    "no contact, selects no provider, route or model class, prepares no "
    "credential, transport, prompt or harness, reads no custody, changes no "
    "case, disposition, finding or record, diagnoses no divergence and contacts "
    "no model.",
    "The three outcomes of item 23 answer it directly, in the runway's own "
    "terms; this brief adds no fourth and removes none.",
    "A contact decision is not contact.",
    "No W8-D6 act transmits anything to a model or receives anything from one.",
    "No W8-D6 act contacts a model, prepares credentials, providers, transport, "
    "prompts, a harness or implementation for contact, selects a provider, route "
    "or model class, or treats future contact as inevitable",
    "No W8-D6 outcome discharges, waives or satisfies any precondition",
    "A W8-D6 decision is not that amendment or crossing, and this brief ranks, "
    "prefers and pre-positions no contact-bearing posture;",
    "`contact_class` remains exactly `none`",
    "Synthetic-only is constructional and capture is terminal",
    "a decision not to pursue contact, now or by deferral, is not a failure of "
    "W8, and a decision to pursue contact proves nothing and authorises no step "
    "towards it.",
    "The decision is the human authority's own act.",
    "No mechanical result, count, scan or test establishes a decision",
    "The W8-D5 finding is complete and fixed.",
    "No W8-D6 act reopens, re-weighs, amends or supplements the finding, makes a "
    "second adequacy finding, or reads the case-level evidence afresh as if to "
    "make one;",
    "no W8-D6 act amends, re-dispositions, re-reveals or diagnoses any case.",
    "No W8-D6 act accesses custody or lists, opens, parses, hashes, copies or "
    "reveals any retained record",
    "The decision rests only on published bytes at fixed commits",
    "The published W7 record class is not the W8 instrument",
    "The rows are the basis's whole.",
    "The outcome form is closed.",
    "Each outcome is equally lawful, and none is preselected, expected or "
    "recommended by this brief. A deferral or a presently-insufficient-value "
    "outcome is complete, never a failure; a contact outcome authorises nothing.",
    "A reason the basis cannot support is not given.",
    "Under a contact outcome, contact would still be lawful only behind "
    "instruments this brief names and does not supply:",
    "The runway's deliverable table names no implementing deliverable, and this "
    "brief adds none:",
    "The route is not W8-D6's.",
    "manual import is contact in full",
    "The decision cannot exceed its basis.",
    "An undetermined finding points nowhere by itself.",
    "The sole decision-maker assessed the record the decision rests on.",
    "AI assistance is attributed, never substituted.",
    "Silence is never a decision.",
    "Each later landing runs a placeholder probe over every existing check "
    "before its census is fixed, and a refusal outside its authorised "
    "successions is a stop.",
    "Two landings are proposed, because the runway has already fixed the outcome "
    "set and the decision mints no vocabulary, record class or evidence index of "
    "its own;",
    "The decision record is a governed record at Tier J; it is not a Tier F "
    "crossing, and no outcome makes it one.",
    "Model contact and W8-D7 remain outside this brief.",
    "Acceptance of this brief adopts these positions.",
)
OUTCOMES = ("contact", "deferral", "presently insufficient value")
OUTCOME_LINES = (
    "**The outcome form is closed.** The human authority's decision answers the "
    "runway's question with exactly one of:",
    "    - **contact** — the human authority decides that actual model contact "
    "is to be pursued; this is a decision and not an authorisation, a schedule "
    "or a performance of contact: it authorises no contact, credential, "
    "provider, transport, prompt, harness, implementation or contact surface, "
    "selects no route or model class, and contact could occur only behind the "
    "separate instruments item 26 names, each needing its own authority, with "
    "all seven conjunctive preconditions of ADR-0047 Part D holding together;",
    "    - **deferral** — the human authority decides that the contact decision "
    "is not taken now; no contact is pursued and nothing is prepared, the "
    "decision stays open for a separately governed act that reopens it under "
    "its own authority, and the deferral is complete as W8-D6's outcome, not a "
    "failure of W8 and not a decision against contact;",
    "    - **presently insufficient value** — the human authority decides that "
    "actual model contact would presently add insufficient value; no contact is "
    "pursued and nothing is prepared, the decision is complete as W8-D6's "
    "outcome, it is not a finding about any model and not a failure of W8, and "
    "any later reconsideration would need its own governed act.",
    "",
    "    **Each outcome is equally lawful, and none is preselected, expected or "
    "recommended by this brief. A deferral or a presently-insufficient-value "
    "outcome is complete, never a failure; a contact outcome authorises "
    "nothing.**",
)
# A numbered item as this brief writes it and CommonMark admits it: one to
# nine ASCII digits, a full stop and a space. Unicode digits and longer
# runs are text, which a Markdown reader folds into the item above.
ITEM = re.compile(r"^[0-9]{1,9}\. ")
BOLD_BULLET = re.compile(r"^\s*[-*+]\s+\*\*")
# A CommonMark blank line: empty or SPACE/TAB only. A line of no-break
# spaces, em spaces or form feeds is not blank and parts no paragraph.
BLANK_LINE = re.compile(r"^[ \t]*$")
# Marks a reader folds away or a writer may vary when naming a phrase:
# emphasis and code marks, the zero-width and soft-hyphen code points. The
# fold removes them, makes every whitespace run one space and folds case -
# a bounded textual fold, never a Markdown parser.
FOLDED_MARKS = re.compile("[*_`~​‌‍⁠﻿­]")
# Wording that would preselect an outcome or the contact decision; none may
# appear anywhere in the brief outside the pinned outcome lines and the
# runway's quoted sentence.
PRESELECTION = ("contact is warranted", "contact is not warranted",
                "should be contacted", "should contact", "should not contact",
                "recommend contact", "recommends contact", "recommend deferral",
                "recommends deferral", "should defer", "should be deferred",
                "is ready for contact", "the instrument is mature",
                "the instrument is not mature", "the decision will be",
                "is expected to decide", "will decide", "likely outcome",
                "preferred outcome", "contact is inevitable",
                "contact is foreclosed", "will add useful evidence",
                "will not add useful evidence")
WITHHELD = ("takes no contact decision", "selects no outcome",
            "authorises no contact", "contacts no model",
            "W8-D7 remains closed",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "the contact decision itself, at this landing, or any closure (W8-D7)",
            "any selection of a provider, route or model class, or any opening "
            "or narrowing of the hosted class",
            "any Tier F crossing, any amendment of ADR-0051, or any "
            "implementation brief",
            "any reopening, re-weighing or amendment of the W8-D5 finding, or "
            "any second adequacy finding",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record")
SECTION_4 = "## 4. The decision question and the three outcomes"
SUCCESSION_SECTION = "## 9. Proof successions, each authorised only in its own landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
SECTION_REF = re.compile(r"§\d+(?:\.\d+)*")

# --------------------------------------- board and registry: authorised edits
CDB_LINK = ("([`W8-D6-contact-decision-brief.md`]"
            "(W8-D6-contact-decision-brief.md))")
CDB_STATUS_TAIL = (
    "W8-D6 for contact-decision work only, as two landings behind their own "
    "acceptances: this brief, and the human authority's contact decision "
    "record and completion. It carries the runway's decision in its own terms "
    "— contact, deferral, or presently insufficient value — with no outcome "
    "preselected; fixes the published basis the decision may rest on, with the "
    "W8-D5 finding weighed as recorded and never reopened; states what each "
    "outcome would and would not do, a contact outcome authorising nothing and "
    "naming the separate instruments any contact would still need without "
    "supplying them; states the limits and the human decision points; and "
    "takes no decision, selects no provider, route or model class, contacts no "
    "model and preselects no outcome.")
CDB_STATUS = {
    "draft": ("**A draft W8-D6 opening brief, `W8-D6-CDB`, is before the "
              "human reviewer** " + CDB_LINK + ": if accepted, it would open "
              + CDB_STATUS_TAIL),
    "accepted": ("**The W8-D6 opening brief, `W8-D6-CDB`, is accepted** "
                 + CDB_LINK + " — accepted %s: it opens " + CDB_STATUS_TAIL),
}
CDB_ROW = ("| W8-D6 — Contact Decision (opening brief, W8-D6-CDB) | "
           "[`W8-D6-contact-decision-brief.md`]"
           "(W8-D6-contact-decision-brief.md) | ")
CDB_ROW_BODY = (
    "Tier J: **opens W8-D6 for contact-decision work only** — the runway's "
    "separately governed decision, contact, deferral or presently insufficient "
    "value, taken by the human authority alone on the published basis, with no "
    "outcome preselected; what each outcome would and would not do is stated, "
    "a contact outcome authorising nothing and naming the separate instruments "
    "any contact would still need; the W8-D5 finding is weighed as recorded "
    "and never reopened; no provider, route or model class is selected and the "
    "hosted class stays closed. Two landings behind their own acceptances; any "
    "assistance is separately attributed and adopted only by the human "
    "authority's express act. ADR-0058's R9 later-deliverable limb succeeds at "
    "this landing, its sentence and constant unchanged, the W8-D5 completion "
    "kept as its historical anchor. **No decision, contact capability, "
    "diagnosis or custody access yet; every W8-D3, W8-D4 and W8-D5 record "
    "stays fixed; W8-D7 stays closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**" + R9_SENTENCE + " W8-D6 and W8-D7 remain closed behind "
                 "their own briefs.**")
CLOSED_AFTER = ("**" + R9_SENTENCE + " W8-D7 remains closed behind its own "
                "brief.**")
# The finding record's status sentence closes directly before the retained
# R9 sentence, and its row is the table's last.
AFR_CLOSE = "which needs its own brief and authorisation. "
BOARD_STATUS_ANCHOR = AFR_CLOSE + CLOSED_BEFORE
BOARD_ROW_ANCHOR = ("every disposition and divergence stays as published; "
                    "W8-D6 and W8-D7 stay closed; no model contact.** |\n")
CDB_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CDB_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D6-CDB", "path": BRIEF, "type": "phase-brief",
    "title": "W8-D6 - Contact Decision: Opening Brief",
    "role": (
        "The opening brief of W8-D6, the contact decision, under the W8 "
        "runway: opens W8-D6 for contact-decision work only through a "
        "two-landing programme - this brief, and the human authority's "
        "contact decision record and completion. Carries the runway's "
        "separately governed decision in its own terms - contact, deferral, "
        "or presently insufficient value - with no outcome preselected, a "
        "deferral or presently-insufficient-value outcome complete and never "
        "a failure, and a contact outcome a decision that authorises no "
        "contact, credential, provider, transport, prompt, harness, "
        "implementation or contact surface and selects no route or model "
        "class; fixes the published basis the decision may rest on, the "
        "W8-D5 finding weighed as recorded and never reopened; states what "
        "each outcome would and would not do and the separate instruments any "
        "contact would still need - a separately accepted implementation "
        "brief naming the first-contact gate, a Tier F crossing record of its "
        "own, and every ADR-0047 precondition holding together - named and "
        "not supplied, with the runway's deliverable table naming no "
        "implementing deliverable; states the limits, the human decision "
        "points and the stop conditions. Carries ADR-0058's R9 "
        "later-deliverable succession at its own landing, R9's sentence and "
        "constant unchanged and the W8-D5 completion kept as its historical "
        "anchor, with proof obligations CD1 to CD8. Takes no decision, "
        "diagnoses nothing, reads no custody and contacts no model; ADR-0047 "
        "precondition 3 stays outstanding in its lawful resting state; W8-D7 "
        "stays closed."),
    "depends_on": ["W8-AR", "ADR-0054", "ADR-0047", "ADR-0046", "ADR-0051",
                   "ADR-0033", "ADR-0034", "ADR-0049", "ADR-0055", "ADR-0057",
                   "ADR-0058", "ADR-0059", "ADR-0060", "ADR-0061", "W8-D5-EAB",
                   "W8-D5-AFR", "W8-D3-SCB", "W8-D3-HDR", "W8-D3-DR-01",
                   "W8-D3-CCR", "W8-D4-IVB", "W8-D4-VSR", "W8-D4-DR-01",
                   "W8-D4-VRC", "W8-D4-CPR", "W8-D2-CBC", "ADR-0056", "W7-CR",
                   "W7-D3-MBB", "W8-DER"],
}


# ----------------------------------------------------------------- helpers
def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def _lf(raw):
    return raw.replace(b"\r\n", b"\n")


def _sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _flat(text):
    return " ".join(text.split())


def _blob(raw):
    return subprocess.run(["git", "hash-object", "--stdin"], input=raw,
                          cwd=ROOT, capture_output=True,
                          check=True).stdout.decode().strip()


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def folded(text):
    """The bounded fold of the preselection scan: marks removed, whitespace
    runs made one space, case folded."""
    return " ".join(FOLDED_MARKS.sub("", text).split()).casefold()


def prose_paragraphs(text):
    """Markdown's logical paragraphs: blocks parted by blank lines - empty or
    SPACE/TAB-only, as CommonMark defines a blank line - with every run of
    whitespace inside a block made one space: a soft line break,
    continuation indentation, a tab, a no-break space, an em space or a
    form feed among them. Nothing is joined across a blank line, so a
    heading stays apart from the item below it. Locally owned; the same
    form the published review-law module gives its EL3."""
    blocks, cur = [], []
    for line in text.split("\n"):
        if BLANK_LINE.match(line):
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return "\n\n".join(re.sub(r"\s+", " ", " ".join(b)).strip()
                       for b in blocks)


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def d6a_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the brief, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", BRIEF).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the brief was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = d6a_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_cdb_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def nine_rules():
    m = re.search(r"^> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                  r"failure\.\*\*)$", baseline_text(DOCTRINE), re.M)
    return m.group(1) if m else None


def contact_chain():
    """ADR-0047 decision 18's chain block, found by its closing link. The
    chain's opening link is never written here: the W7 chain-integrity
    proof treats every occurrence of it as a reach that must carry the
    whole chain, and this module carries none."""
    ends = [line[2:] for line in baseline_text(CONTACT_LAW).split("\n")
            if line.startswith("> **")
            and line.endswith("no contact ≠ nothing proven.**")]
    return ends[0] if len(ends) == 1 else None


def closed_list_violations(text, lines, names, label, above=()):
    """A closed bold-bullet list carried as one numbered item: from the
    item's number up to the next numbered item, exactly `lines`, with
    numbered items directly either side, and each bold name once in the
    whole brief. `above` names the exact lines, besides a numbered item,
    that may lawfully sit directly above the item."""
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows)
             if ITEM.match(l) and l[ITEM.match(l).end():] == lines[0]]
    if len(heads) != 1:
        return ["the %s item is not present exactly once" % label]
    i = heads[0]
    end = next((j for j in range(i + 1, len(rows))
                if ITEM.match(rows[j]) or rows[j].startswith("#")), len(rows))
    v = []
    if tuple([lines[0]] + rows[i + 1:end]) != lines:
        v.append("the %s item is not exactly its members, each once" % label)
    if i == 0 or not (ITEM.match(rows[i - 1]) or rows[i - 1] in above):
        v.append("a line other than a numbered item abuts the %s item's top"
                 % label)
    if end >= len(rows) or not ITEM.match(rows[end]):
        v.append("the %s item is not followed directly by the next numbered "
                 "item" % label)
    v += ["%s %s is named %d times" % (label, n, text.count("**%s**" % n))
          for n in names if text.count("**%s**" % n) != 1]
    return v


def section_lines(text, heading):
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows) if l == heading]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(rows))
                if rows[j].startswith("## ")), len(rows))
    return rows[heads[0]:end]


def carriage_violations(text):
    """CD1: the runway's sentence, the nine rules, the contact chain and the
    load-bearing statements, each once; the closed outcome list; section 4's
    bold-led bullets exactly the outcomes; no preselecting wording."""
    flat = _flat(text)
    v = []
    runway = _flat(baseline_text(RUNWAY))
    if RUNWAY_SENTENCE not in runway:
        v.append("the runway's sentence is not in the runway")
    if flat.count('"%s"' % RUNWAY_SENTENCE) != 1:
        v.append("the runway's sentence is not carried exactly once")
    for name, block in (("nine-rule", nine_rules()),
                        ("contact-chain", contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    v += closed_list_violations(text, OUTCOME_LINES, OUTCOMES, "outcome")
    sec = section_lines(text, SECTION_4)
    if sec is None:
        v.append("section 4 is not present exactly once")
    else:
        bold = [l for l in sec if BOLD_BULLET.match(l)]
        if bold != list(OUTCOME_LINES[1:4]):
            v.append("section 4's bold-led bullets are not exactly the "
                     "outcomes")
    # The runway's own sentence is carried verbatim and is not the brief's
    # wording, and the pinned outcome lines define the lawful outcomes
    # whose exact text the closed list proves; every other occurrence is
    # checked through the bounded fold, so that emphasis, code marks,
    # invisible code points, wrapping and case hide no inventoried phrase.
    # A bounded textual inventory: it proves nothing about other prose.
    outside = text
    for line in OUTCOME_LINES:
        outside = outside.replace(line, "", 1)
    low = folded(outside).replace(folded(RUNWAY_SENTENCE), "")
    v += ["preselecting wording: %s" % p for p in PRESELECTION if p in low]
    return v


def boundary_mutants(text):
    """The numbered-item boundary regressions for the protected item: a line
    that is not a CommonMark ordered marker - Unicode digits, ten ASCII
    digits, a closing parenthesis, or a hash with no space - placed at the
    outcome item's top and after it; and the item's own number replaced by
    a non-marker prefix."""
    rows = text.split("\n")
    out_i = next(i for i, l in enumerate(rows)
                 if ITEM.match(l) and l[ITEM.match(l).end():] == OUTCOME_LINES[0])
    after = out_i + len(OUTCOME_LINES)
    lines = {"unicode digits": "١. mechanics sentinel",
             "ten ASCII digits": "1234567890. mechanics sentinel",
             "a closing parenthesis": "1) mechanics sentinel",
             "a hash with no space": "#1 mechanics sentinel"}
    out = {}
    for form_name, line in lines.items():
        for place, at in (("above the outcome item", out_i),
                          ("after the outcome item", after)):
            out["%s, %s" % (form_name, place)] = "\n".join(
                rows[:at] + [line] + rows[at:])
    body = rows[out_i][ITEM.match(rows[out_i]).end():]
    for prefix in ("١٩. ", "1234567890. "):
        out["the outcome item numbered %r" % prefix.strip()] = "\n".join(
            rows[:out_i] + [prefix + body] + rows[out_i + 1:])
    return out


NON_AUTH_SECTION = "## 12. Explicit non-authorisations"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - the contact decision itself, at this landing, or any closure "
    "(W8-D7);",
    "    - any selection of a provider, route or model class, or any opening "
    "or narrowing of the hosted class;",
    "    - any Tier F crossing, any amendment of ADR-0051, or any "
    "implementation brief;",
    "    - any reopening, re-weighing or amendment of the W8-D5 finding, or "
    "any second adequacy finding;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition or reveal, or any "
    "change to an existing one, including any made from captured generated "
    "material;",
    "    - any new grouped outcome count, rate or ranking by corpus, authored "
    "class or validation method;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059, ADR-0060 or ADR-0061, or of `W8-D5-EAB` or "
    "`W8-D5-AFR`;",
    "    - any score, rate, ranking, threshold, readiness, safety, "
    "correctness, approval, `certif-` or `complian-` claim;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any discharge, waiver or satisfaction of any ADR-0047 Part D "
    "precondition, any resolution of precondition 3, or any movement of any "
    "carried state.",
)
NON_AUTH_CLOSE = "    **Model contact and W8-D7 remain outside this brief.**"
NON_AUTH_INTRO = "45. This brief and W8-D6 do not authorise:"
# Section 12 whole: heading, blank, introducing item, the thirteen lines,
# blank, closing sentence, trailing blank - compared as one block, nothing
# skipped.
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))


def withholding_violations(text):
    """CD2: every non-authorisation phrase present anywhere, and section 12
    exactly its authorised whole block - heading, blank, introducing item,
    the thirteen lines in order, blank, closing sentence, trailing blank -
    with no other line anywhere in it."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["section 12 is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("section 12 is not exactly its authorised whole block")
    return v


def count_beside(tokens):
    """A number written beside a token or relation name, in either order,
    across up to eight non-alphanumeric characters. A textual guard only."""
    name = (r"(?<![A-Za-z0-9])(?:%s|agreements?|divergences?)(?![A-Za-z0-9])"
            % "|".join(re.escape(t) for t in sorted(tokens)))
    number = (r"(?<![A-Za-z0-9])(?:\d+|one|two|three|four|five|six|seven|"
              r"eight|nine|ten|eleven|twelve)(?![A-Za-z0-9])")
    gap = r"[^A-Za-z0-9\n]{0,8}"
    return re.compile("(?i)" + name + gap + number + "|" + number + gap + name)


def strip_refs(text):
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", "", text)
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", "", text)
    return SECTION_REF.sub("", text)


def exposure_violations(text, h, exempt=()):
    """CD3: over the text's logical prose paragraphs - so that a soft line
    break, continuation indentation or a non-blank separator hides nothing -
    no case identity, no digest outside the exempt exact lines (each
    surviving the paragraph form unchanged), no reserved authoring label,
    schema literal or method label, no number beside a token or relation
    name, and no derived-figure form. A textual guard only."""
    text = prose_paragraphs(text)
    v = []
    if h.rec.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    stripped = text
    for line in exempt:
        stripped = stripped.replace(line, "", 1)
    if re.search(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", stripped):
        v.append("an unpinned digest is present")
    v += ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    schemas = ((h.pkt.PACKET_SCHEMA, h.cal.REGISTER_SCHEMA,
                h.env.AUTHORING_SCHEMA) + tuple(h.law.NEW_SCHEMAS))
    v += ["a schema literal is present" for s in schemas if s in text]
    v += ["a method label: %s" % m for m in sorted(h.law.ADMITS)
          if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]
    if count_beside(h.pkt.TOKENS).search(text):
        v.append("a count beside a token or relation")
    v += h.vr.figure_hits(strip_refs(text), h.pkt.TOKENS)
    return v


def batch(commit, paths):
    """{path: LF bytes} for many paths in one process: the working copy
    before this landing's commit exists, committed objects otherwise."""
    if commit is None:
        return {p: _lf((ROOT / p).read_bytes()) for p in paths
                if (ROOT / p).is_file()}
    out = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT,
                         input="".join("%s:%s\n" % (commit, p)
                                       for p in paths).encode(),
                         capture_output=True, check=True).stdout
    got, i = {}, 0
    for p in paths:
        head_end = out.index(b"\n", i)
        head = out[i:head_end].split()
        if head[-1] == b"missing":
            i = head_end + 1
            continue
        size = int(head[2])
        got[p] = _lf(out[head_end + 1:head_end + 1 + size])
        i = head_end + 1 + size + 1
    return got


def fixed_paths():
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
    paths = {e["id"]: e["path"] for e in reg}
    homes = {h: sorted(p for p in base_tracked if p.startswith(h + "/"))
             for h in FIXED_HOMES}
    return homes, [paths[r] for r in FIXED_RECORD_IDS]


def fixed_artefact_violations(now, tracked, homes, records, base):
    """CD4: every fixed home's file set and bytes, and every fixed record's
    bytes - the three W8-D5 records among them - identical to the baseline."""
    v = []
    for home, files in homes.items():
        if not files:
            v.append("a fixed home is empty at the baseline: %s" % home)
        if sorted(p for p in tracked if p.startswith(home + "/")) != files:
            v.append("a fixed home's file set changed: %s" % home)
    for p in [f for files in homes.values() for f in files] + records:
        if p in now and now[p] != base[p]:
            v.append("a fixed file changed")
    return v


def basis_rows():
    return [["%d" % n, "`%s`" % i, "`%s`" % p, "`%s`" % c, "`%s`" % b, "`%s`" % s]
            for n, i, p, c, b, s in BASIS_ROWS]


def basis_row_lines():
    return ["| " + " | ".join(r) + " |" for r in basis_rows()]


def basis_table_violations(text, h):
    rows, v = h.rev.closed_table(text, BASIS_SECTION, BASIS_HEADER,
                                 BASIS_SEPARATOR, 6)
    if rows != basis_rows():
        v.append("the basis table is not exactly its trusted rows")
    return v


def basis_object_violations(rows=None, resolve=None, registered=None):
    """Each trusted row's path names its pinned object at its cited commit
    and at the baseline, the committed bytes carry the pinned raw SHA-256,
    and the identity is registered at that path at the baseline. `resolve`
    and `registered` are injectable for the controls."""
    rows = BASIS_ROWS if rows is None else rows
    if resolve is None:
        def resolve(commit, path):
            try:
                return (_git("rev-parse", "%s:%s" % (commit, path)).strip(),
                        _sha(committed(commit, path)))
            except subprocess.CalledProcessError:
                return (None, None)
    if registered is None:
        reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
        registered = {e["id"]: e["path"] for e in reg}
    v = []
    if [r[0] for r in rows] != list(range(1, len(rows) + 1)):
        v.append("the rows are not numbered consecutively from one")
    for n, ident, path, commit, blob, sha in rows:
        got_blob, got_sha = resolve(commit, path)
        if got_blob != blob:
            v.append("row %d: the object at the cited commit differs" % n)
        if got_sha != sha:
            v.append("row %d: the committed bytes differ from the pin" % n)
        if resolve(BASELINE, path)[0] != blob:
            v.append("row %d: the object at the baseline differs" % n)
        if registered.get(ident) != path:
            v.append("row %d: the identity is not registered at that path" % n)
    return v


def succession_rows(h):
    return [["`%s`" % RECOVERY, ", ".join(h.auth.labels(SITES[RECOVERY])),
             "`%s`" % PREIMAGE[RECOVERY][1], "`%s`" % POSTIMAGE[RECOVERY][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def succession_table_violations(text, h):
    rows, v = h.rev.closed_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                                 SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, brief, h, sites=None):
    sites = SITES[RECOVERY] if sites is None else sites
    v = []
    pre = baseline_text(RECOVERY)
    if _sha(pre.encode("utf-8")) != PREIMAGE[RECOVERY][1]:
        v.append("the baseline pre-image differs from its pin")
    expected, problems = h.auth.apply_sites(pre, sites)
    v += problems
    if expected != present:
        v.append("the bytes are not the exact authorised post-image")
    for label, _, new in sites:
        if present.count(new) != 1:
            v.append("%s: post-image site occurs %d times"
                     % (label, present.count(new)))
    restored, problems = h.auth.reverse_sites(present, sites)
    v += problems
    if restored != pre:
        v.append("reversing the table does not restore the pre-image")
    if _sha(present.encode("utf-8")) != POSTIMAGE[RECOVERY][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("R9",):
        v.append("the sites are not R9's alone")
    if present.count(R9_LINE) != 1 or pre.count(R9_LINE) != 1:
        v.append("R9's constant is not carried unchanged")
    return v + succession_table_violations(brief, h)


def cdb_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CDB_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CDB_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         AFR_CLOSE + fill(CDB_STATUS[state]) + " " + CLOSED_AFTER),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + CDB_ROW + fill(ROW_PREFIX[state]) + CDB_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D6",
        "path": NEW_ENTRY["path"], "status": state,
        "accepted_date": date if state == "accepted" else None,
        "role": NEW_ENTRY["role"], "governs": [],
        "depends_on": list(NEW_ENTRY["depends_on"]), "resolves": [],
        "id_namespaces": [], "implementation_permission": "none",
        "open_decisions": [], "content_hash": content_hash,
        "hash_exclusion_reason": None, "errata": [],
    }


def expected_registry(base_text, brief_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, brief_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    """The wording this landing adds to the board in both lawful states, the
    accepted forms dated with a sample so that no format sign remains."""
    sample = "2026-01-01"
    return " ".join([CDB_ROW, CDB_ROW_BODY, CLOSED_AFTER, CDB_STATUS["draft"],
                     CDB_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, brief_text, h):
    """CD7: this brief's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D6 entries are exactly this brief's; no
    W8-D7 entry."""
    v = []
    e = {x["id"]: x for x in entries}.get("W8-D6-CDB")
    state, date = h.rec.header_state(brief_text)
    if e is None:
        return ["no W8-D6-CDB entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            BRIEF, "phase-brief", "W8", "W8-D6"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(brief_text.encode("utf-8")):
        v.append("the entry's hash differs from the brief")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D6"} != D6_ENTRIES:
        v.append("the W8-D6 entries are not exactly this brief's")
    if [x["id"] for x in entries if x["deliverable"] in LATER_THAN_D6]:
        v.append("a W8-D7 entry exists")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted to
    call is replaced and the previous state restored on exit, tolerating a
    name a later landing has renamed or removed."""

    ABSENT = object()
    TARGETS = (
        ("test_w8_session_recovery_law", "R9_REVEAL", "mechanics sentinel"),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_recovery_authority", "apply_sites",
         lambda text, sites: (text, [])),
        ("test_w8_reveal_calibration", "closed_table",
         lambda *a, **k: ([], [])),
        ("test_w8_validation_reveal", "figure_hits", lambda *a, **k: []),
        ("test_w8_discriminating_instrument_corpus", "reserved_channel_hits",
         lambda *a, **k: []),
    )

    def __enter__(self):
        self.saved = []
        for module, name, value in self.TARGETS:
            mod = importlib.import_module(module)
            self.saved.append((mod, name, getattr(mod, name, self.ABSENT)))
            setattr(mod, name, value)
        return self

    def __exit__(self, *exc):
        for mod, name, value in reversed(self.saved):
            if value is self.ABSENT:
                mod.__dict__.pop(name, None)
            else:
                setattr(mod, name, value)
        return False


# ------------------------------------------------------------------ proofs
class CD1_Carriage(unittest.TestCase):
    def test_cd1_brief_carries_question_outcomes_and_statements(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="sentence, blocks, statements, closed list "
                               "and no preselection"):
            self.assertEqual(carriage_violations(text), [])
        for name, mutated in boundary_mutants(text).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated))
        first = OUTCOME_LINES[1]
        for name, mutated in (
                ("a fourth outcome", text.replace(
                    first + "\n", first + "\n    - **withdrawal** — sentinel;\n", 1)),
                ("a dropped outcome", text.replace(first + "\n", "", 1)),
                ("a stray line inside the outcome list", text.replace(
                    OUTCOME_LINES[3] + "\n", OUTCOME_LINES[3] + "\nsentinel\n", 1)),
                ("a preselecting sentence", text.replace(
                    "\n## 4.", "\nContact is warranted.\n\n## 4.", 1)),
                ("a preselecting sentence inside section 4, outside the "
                 "pinned lines", text.replace(
                    "\n24. **Every decision states",
                    "\nContact should be deferred.\n\n24. **Every decision "
                    "states", 1)),
                ("an outcome rewritten as an assertion", text.replace(
                    first, first.replace(
                        "the human authority decides that ", "", 1), 1)),
                ("a recommendation of contact", text.replace(
                    "\n## 4.", "\nThis brief would recommend contact.\n\n## 4.",
                    1)),
                ("an inventoried phrase in bold", text
                 + "\nContact **is warranted**.\n"),
                ("an inventoried phrase in italics", text
                 + "\nContact *is warranted*.\n"),
                ("an inventoried phrase in underscore emphasis", text
                 + "\nContact _is warranted_.\n"),
                ("an inventoried phrase in code marks", text
                 + "\nContact `is warranted`.\n"),
                ("an inventoried phrase with a zero-width space", text
                 + "\nContact is​ warranted.\n"),
                ("an inventoried phrase wrapped over a soft break", text
                 + "\nContact is\nwarranted.\n"),
                ("an inventoried phrase in capitals", text
                 + "\nCONTACT IS WARRANTED.\n"),
                ("a second inventoried phrase in bold", text
                 + "\nContact should **be deferred**.\n"),
                ("a removed statement", text.replace(REQUIRED[5], "", 1)),
                ("an altered runway sentence", text.replace(
                    RUNWAY_SENTENCE, RUNWAY_SENTENCE.replace("presently", "now"),
                    1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated))
        for name, added in (("a phrase outside the inventory",
                             "\nContact is pursued.\n"),
                            ("the quoted runway sentence in bold",
                             '\n**"%s"**\n' % RUNWAY_SENTENCE)):
            with self.subTest(positive="%s is not what the inventory refuses"
                                       % name):
                self.assertEqual(
                    [x for x in carriage_violations(text + added)
                     if x.startswith("preselecting wording")], [])
        with self.subTest(fact="the fold is the bounded fold: marks, "
                               "whitespace and case"):
            self.assertEqual(folded("Con​tact **is**\n  _warranted_."),
                             "contact is warranted.")


class CD2_NonAuthorisations(unittest.TestCase):
    def test_cd2_brief_carries_its_non_authorisations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="every non-authorisation carried"):
            self.assertEqual(withholding_violations(text), [])
        for s in WITHHELD[:3]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, "")))
        grouped = NON_AUTH_LINES[8] + "\n"
        pair = NON_AUTH_LINES[5] + "\n" + NON_AUTH_LINES[6] + "\n"
        tail = NON_AUTH_LINES[12] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this section.\n"
        for name, mutated in (
                ("the grouped-count non-authorisation dropped", text.replace(
                    grouped + NON_AUTH_LINES[9], NON_AUTH_LINES[9], 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[6] + "\n" + NON_AUTH_LINES[5] + "\n", 1)),
                ("a fourteenth non-authorisation", text.replace(
                    grouped + NON_AUTH_LINES[9],
                    grouped + "    - any sentinel line;\n" + NON_AUTH_LINES[9],
                    1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[12] + "\n" + neutral
                              + "\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[12] + "\n    This landing "
                              "authorises an additional session.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a differently indented extra bullet",
                 text.replace(tail, NON_AUTH_LINES[12] + "\n  - any sentinel "
                              "line;\n\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a line between the heading and the introducing item",
                 text.replace(NON_AUTH_SECTION + "\n\n" + NON_AUTH_INTRO
                              + "\n", NON_AUTH_SECTION + "\n\n" + neutral
                              + NON_AUTH_INTRO + "\n", 1)),
                ("a line between the introducing item and the first "
                 "non-authorisation",
                 text.replace(NON_AUTH_INTRO + "\n" + NON_AUTH_LINES[0]
                              + "\n", NON_AUTH_INTRO + "\n" + neutral
                              + NON_AUTH_LINES[0] + "\n", 1)),
                ("a line after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a non-breaking-space line as the blank separator",
                 text.replace(tail, NON_AUTH_LINES[12] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated))


class CD3_NoExposure(unittest.TestCase):
    def test_cd3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr")
        text = read(BRIEF).decode("utf-8")
        exempt = (succession_row_line(helpers(read, "auth")),) + tuple(
            basis_row_lines())
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D6-CDB"]["role"] + " " + by_id["W8-D6-CDB"]["title"]
        for name, surface, ex in (("brief", text, exempt),
                                  ("registry role and title", role, ()),
                                  ("board wording this landing adds",
                                   added_board_wording(), ())):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(exposure_violations(surface, h, ex), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertIsNone(h.rec.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([m for m in sorted(h.law.ADMITS) if re.search(
                r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), src)], [])
            for token in h.pkt.TOKENS:
                self.assertNotIn(token, src)
        tok = sorted(h.pkt.TOKENS)[0]
        for name, plant in {
                "a case identity": "W8-C-" + "d" * 64,
                "an unpinned digest": "e" * 64,
                "a reserved label": sorted(h.cor.RESERVED_FIELDS)[0],
                "a schema literal": h.env.AUTHORING_SCHEMA,
                "a method label": sorted(h.law.ADMITS)[0],
                "a count beside a token": "5 " + tok,
                "a count beside a relation": "agreement: 11",
                "a decimal rate": "an agreement rate of 0.5",
                "a percentage": "50%"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(text + "\n" + plant + "\n",
                                                    h, exempt))
        with self.subTest(control="a basis row with an altered digest is not "
                                  "exempt"):
            altered = basis_row_lines()[0].replace("sha256:1", "sha256:0", 1)
            self.assertNotEqual(altered, basis_row_lines()[0])
            self.assertTrue(exposure_violations(
                text.replace(basis_row_lines()[0], altered, 1), h, exempt))
        # The paragraph form: a figure or count split over a soft line
        # break, a worded connector, continuation indentation or a
        # non-blank separator line is refused as its same-line form is; a
        # genuine blank line - empty or SPACE/TAB-only - parts paragraphs.
        for name, route in {
                "a figure word and its value on one line": "\nscore: 5\n",
                "a figure word, a soft line break, its value": "\nscore\n5\n",
                "a figure word, a worded connector, a soft break, its value":
                    "\nscore is\n5\n",
                "a figure word, a soft break, a space-indented value":
                    "\nscore\n    5\n",
                "a figure word, a soft break, a tab-indented value":
                    "\nscore\n\t5\n",
                "a no-break-space separator line between them":
                    "\nscore\n \n5\n",
                "an em-space separator line between them":
                    "\nscore\n \n5\n",
                "a form-feed separator line between them":
                    "\nscore\n\u000c\n5\n",
                "a token, a soft line break, a count": "\n%s\n5\n" % tok,
                "a relation name, a soft line break, a count":
                    "\nagreements\n11\n"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(exposure_violations(text + route, h, exempt))
        for name, route in {
                "a figure word, a genuine blank line, a value":
                    "\nscore\n\n5\n",
                "a figure word, a space-only line, a value":
                    "\nscore\n   \n5\n",
                "a figure word, a tab-only line, a value":
                    "\nscore\n\t\n5\n"}.items():
            with self.subTest(positive="%s keeps two paragraphs apart" % name):
                self.assertEqual(exposure_violations(text + route, h, exempt),
                                 [])
        with self.subTest(fact="the paragraph form parts blocks only at "
                               "blank lines and makes each whitespace run "
                               "one space"):
            self.assertEqual(prose_paragraphs("a\n  b\tc\n \nd\n\ne\n \nf"),
                             "a b c d\n\ne\n\nf")
        with self.subTest(fact="every exempt row survives the paragraph form"):
            folded_text = prose_paragraphs(text)
            for line in exempt:
                self.assertEqual(folded_text.count(line), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr")
                self.assertEqual(exposure_violations(text, hh, exempt), [])
                self.assertTrue(exposure_violations(text + "\n0.5\n", hh,
                                                    exempt))


class CD4_FixedArtefactsAndBasis(unittest.TestCase):
    def test_cd4_every_case_home_register_and_record_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tracked = snapshot_tracked(commit)
        homes, records = fixed_paths()
        every = [f for files in homes.values() for f in files] + records
        base = batch(BASELINE, every)
        now = batch(commit, every)
        with self.subTest(fact="fixed homes and records byte-identical to "
                               "the baseline"):
            self.assertEqual(len(base), len(every))
            self.assertEqual(set(now), set(every))
            self.assertEqual(fixed_artefact_violations(
                now, tracked, homes, records, base), [])
        reveal_file = homes["governance/validation-reveal"][0]
        finding = records[FIXED_RECORD_IDS.index("W8-D5-AFR")]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed finding record": (
                    dict(now, **{finding: now[finding] + b" "}), tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))

    def test_cd4_basis_table_is_exactly_its_trusted_rows_resolving(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="the table read whole is the trusted rows"):
            self.assertEqual(basis_table_violations(text, h), [])
        with self.subTest(fact="every row resolves at its commit and at the "
                               "baseline, and is registered"):
            self.assertEqual(basis_object_violations(), [])
        with self.subTest(fact="the rows cover the finding, the law, the "
                               "brief and the runway"):
            idents = [r[1] for r in BASIS_ROWS]
            for i in ("W8-D5-AFR", "ADR-0061", "W8-D5-EAB", "W8-AR",
                      "ADR-0047", "ADR-0051"):
                self.assertIn(i, idents)
            self.assertEqual(len(set(idents)), len(idents))
        line = basis_row_lines()[0]
        top = BASIS_HEADER + "\n" + BASIS_SEPARATOR + "\n"
        for name, mutated in (
                ("a dropped row", text.replace(line + "\n", "", 1)),
                ("a duplicated row", text.replace(line + "\n", line + "\n"
                                                  + line + "\n", 1)),
                ("an altered commit", text.replace(
                    line, line.replace(BASIS_ROWS[0][3], "0" * 40, 1), 1)),
                ("an altered separator", text.replace(
                    top, BASIS_HEADER + "\n|---|---|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom", text.replace(
                    basis_row_lines()[-1] + "\n",
                    basis_row_lines()[-1] + "\nmechanics sentinel\n", 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(basis_table_violations(mutated, h))
        good = BASIS_ROWS[0]
        wrong_blob = (good[0], good[1], good[2], good[3], "0" * 40, good[5])
        wrong_sha = (good[0], good[1], good[2], good[3], good[4],
                     "sha256:" + "0" * 64)
        wrong_commit = (good[0], good[1], good[2], D4_COMPLETION, good[4],
                        good[5])
        unregistered = (good[0], "W8-D6-SNT") + good[2:]
        for name, rows in (("a wrong object", (wrong_blob,)),
                           ("a wrong digest", (wrong_sha,)),
                           ("a commit at which the object differs",
                            (wrong_commit,)),
                           ("an identity not registered at the path",
                            (unregistered,)),
                           ("a gap in the numbering", (good, BASIS_ROWS[2]))):
            with self.subTest(object_control="%s is refused" % name):
                self.assertTrue(basis_object_violations(rows))
        with self.subTest(control="a resolver returning the pins verbatim "
                                  "is not what is trusted"):
            self.assertEqual(basis_object_violations(
                resolve=lambda c, p: (good[4], good[5]),
                registered={good[1]: good[2]}, rows=(good,)), [])
            self.assertTrue(basis_object_violations(
                resolve=lambda c, p: (good[4], good[5]),
                registered={}, rows=(good,)))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(basis_table_violations(text, hh), [])


class CD5_R9Succession(unittest.TestCase):
    def test_cd5_r9_succession_is_exact_and_its_sentence_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "rec")
        brief = read(BRIEF).decode("utf-8")
        present = read(RECOVERY).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[RECOVERY][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + RECOVERY)
                             .strip(), PREIMAGE[RECOVERY][2])
        with self.subTest(exact_succession=PREIMAGE[RECOVERY][0]):
            self.assertEqual(succession_violations(present, brief, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[RECOVERY][1])
        with self.subTest(fact="R9's sentence and constants unchanged, the "
                               "new anchor the W8-D5 completion"):
            self.assertEqual(h.rec.R9_REVEAL, R9_SENTENCE)
            self.assertEqual(h.rec.D4_COMPLETION, D4_COMPLETION)
            self.assertEqual(h.rec.D5_COMPLETION, D5_COMPLETION)
            self.assertEqual(h.rec.LATER, ("W8-D4", "W8-D5", "W8-D6", "W8-D7"))
        with self.subTest(fact="the W8-D5 completion anchor is this "
                               "landing's baseline, at which no W8-D6 or "
                               "W8-D7 entry existed"):
            self.assertEqual(D5_COMPLETION, BASELINE)
            self.assertEqual(_git("rev-list", "--parents", "-n", "1",
                                  D5_COMPLETION).split()[1:],
                             ["18d6230b5f7281577c18892dd7b95e9448f310c2"])
            self.assertEqual([e["id"] for e in json.loads(
                committed(D5_COMPLETION, REGISTRY))["entries"]
                if e["deliverable"] in ("W8-D6",) + LATER_THAN_D6], [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[RECOVERY][1:]),
                "an altered R9 constant": (present.replace(
                    R9_LINE, R9_LINE.replace("corrected", "repaired"), 1),
                    None),
                "the anchor collapsed onto the W8-D4 completion": (
                    present.replace('D5_COMPLETION = "%s"' % D5_COMPLETION,
                                    'D5_COMPLETION = "%s"' % D4_COMPLETION, 1),
                    None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[RECOVERY] + (("R9", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                if table is None:
                    self.assertNotEqual(text, present)
                self.assertTrue(succession_violations(text, brief, h, table))
        row = succession_row_line(h)
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        for name, mutated in (
                ("a space-prefixed duplicate row", brief.replace(
                    row + "\n", row + "\n " + row + "\n", 1)),
                ("a row with no opening pipe", brief.replace(row, row[2:], 1)),
                ("an altered separator", brief.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom",
                 brief.replace(row + "\n", row + "\nmechanics sentinel\n",
                               1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, brief)
                self.assertTrue(succession_table_violations(mutated, h))
        for name, mutated in h.rev.boundary_mutants(
                brief, SUCCESSION_SECTION, row).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(succession_table_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "rec")
                self.assertEqual(succession_violations(present, brief, hh), [])
                self.assertEqual(hh.rec.R9_REVEAL, R9_SENTENCE)


class CD6_RegistryAndBoard(unittest.TestCase):
    def test_cd6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = cdb_state(read(BRIEF).decode("utf-8"), h)
        self.assertEqual(v, [])
        board_pre = baseline_text(BOARD)
        reg_pre = baseline_text(REGISTRY)
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")

        def board_ok(apply_sites):
            expected, problems = apply_sites(
                board_pre, board_sites(state, date, board_pre))
            return problems == [] and board == expected
        with self.subTest(fact="exact authorised board, R9's sentence kept "
                               "once, the closing range moved", state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED_AFTER), 1)
            self.assertNotIn(CLOSED_BEFORE, board)
        brief_hash = _sha(read(BRIEF))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, brief_hash,
                                                    state, date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, brief_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(control="the R9 sentence removed from the board is "
                                  "refused"):
            self.assertNotEqual(board.replace(R9_SENTENCE + " ", "", 1)
                                .count(R9_SENTENCE), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))


class CD7_EntrySet(unittest.TestCase):
    def test_cd7_registered_and_the_w8_d6_entry_set_is_this_briefs(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        brief = read(BRIEF).decode("utf-8")
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, brief, h), [])
        with self.subTest(fact="no W8-D6 or W8-D7 entry at the baseline"):
            self.assertEqual([e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] in ("W8-D6",) + LATER_THAN_D6], [])
        # The one present-state gate of this landing, as the W8-D4 and
        # W8-D5 openings' were: the W8-D6 entries are exactly this brief's
        # and no W8-D7 entry exists, until the decision landing moves it.
        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]
        with self.subTest(fact="present state: the W8-D6 entries are this "
                               "brief's alone and no W8-D7 entry exists"):
            self.assertEqual(entry_violations(live, brief, h), [])
        base = at_snapshot[-1]
        for name, entries in {
                "a premature second W8-D6 entry": at_snapshot + [dict(
                    base, id="W8-D6-SNT", deliverable="W8-D6")],
                "a W8-D7 entry": at_snapshot + [dict(
                    base, id="W8-D7-SNT", deliverable="W8-D7")],
                "a wrong brief hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                       if e["id"] == "W8-D6-CDB" else e
                                       for e in at_snapshot]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, brief, h))


class CD8_Census(unittest.TestCase):
    def test_cd8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and R9's change among the "
                               "proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, RECOVERY})
        flat = _flat(read(BRIEF).decode("utf-8"))
        with self.subTest(fact="the brief names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?) ## ", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RUNWAY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
