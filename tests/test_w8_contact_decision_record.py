"""W8-D6-B — contact decision record proofs (W8-D6-CDR, DR1–DR9).

The decision landing of W8-D6 and its completion: the record that carries
the human authority's stated choice in the runway's closed outcome form,
the human authority's reasons and its disposition of the separate
instruments by its express adoption of separately attributed assistance,
with that assistance carried whole and the record of its adoption, the
standing of every
ADR-0047 precondition unchanged, and the separate instruments a contact
outcome leaves to their own authority, named and not supplied; and the
one proof succession the
placeholder probe found the decision landing to need - the opening
module's CD7, its W8-D6 entry set and its W8-D7 limb, succeeded to a
historical proof at the D6-A landing commit. This module proves the
record's carriage - Part A exactly its two acts, their labels and
framing - and its textual outcome closure; its non-authorisations;
its exposure limits over logical prose paragraphs; that every citation
resolves to the effective brief's basis; that every case home, register,
revealed record, earlier record and earlier proof module other than the
opening module is byte-unchanged; the exact, reversible CD7 succession and
its closed table; the exact registry, board and census; and completion
without any present-state gate - each with planted-mutant or negative
controls.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the record
afterwards - and executes the helpers it relies on, the opening module
among them, from that snapshot's bytes, in a private namespace. This
module holds no present-state gate, and the succeeded CD7 holds none:
W8-D7 stays refused by ADR-0058's R9 alone. The residual live reach is
disclosed exactly: each snapshot-executed helper module imports, at its
own top level, the live modules it aliases for the fixed-law values it
reads from them, and no more independence than that is claimed.

DR1's outcome closure reads the record outside its trusted regions - the
verbatim instruction, the outcome line and the contact outcome line pinned
from the effective brief - through a bounded fold (emphasis and code marks
and invisible code points removed, whitespace runs made one space, case
folded) and refuses the two outcome names not carried, any outcome named
behind a decision, outcome or choice label, and any recommendation stem
outside the one pinned negation. It is a textual closure over explicit
forms; it proves nothing about the meaning of other prose.

DR4's row-reference check reads each logical paragraph of the record - the
CommonMark blank-line form the effective brief's module gives - with
line-leading quote markers dropped, character references decoded and the
same bounded fold, so that emphasis and code marks, invisible code points,
a soft line break, a no-break space and case cannot hide an explicit
numeric reference to a basis row; every member of the list or range that
follows is read, so a valid first row cannot carry an invalid later one,
and no list runs across a paragraph break. Commits and paths are read
exactly as written. It is a bounded textual check over explicit numeric
references; it proves nothing about what a citation means.

DR1 pins the human authority's act of 2026-10-31, carried verbatim in
Part A, and the text that act adopts - the architect's proposed reasoning,
preserved with its stated limits and the fixed sources it cites, and the
architect's proposed disposition of the separate instruments, carried with
its stated basis and standing - each block the record's quote lines after
its one marker line, pinned by the LF SHA-256 of those lines as carried.
Outside those blocks it pins, line by line, the stretch of each part the
blocks stand in, so that no block moves, doubles or loses its attribution
and no prose is added beside it; Part G's record of assistance and
adoption is pinned whole. No pending slot remains and none is admitted.
The draft and the accepted form are both admitted, the status line,
registry and board binding as DR7 proves.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity,
schema literal or method label as a literal, and no disposition token. It
takes no decision and supplies no reason.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that the decision is right; any reason for it; that any
contact is authorised, scheduled, lawful or possible; anything about any
model, case, disposition, divergence or reviewer; that any model was
contacted; that any ADR-0047 precondition moved; or that W8-D7 may open.
"""

import hashlib
import html
import importlib
import json
import re
import subprocess
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified W8-D6 opening brief: this landing's sole
# parent, the commit every pre-image below is read from, and the D6-A
# landing commit at which CD7's claim stays proven after its succession.
BASELINE = "753e6abea8d67a16332799af615fdcfa4aefa7b9"
D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"
D5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
ANCHORS = frozenset({BASELINE, D5_COMPLETION,
                     "18d6230b5f7281577c18892dd7b95e9448f310c2",
                     "c8e13d47f305e0378609ffec1d31f890f629239d",
                     "6704649ed80c27112c00c14093c82645e8d090cf",
                     "ce78a242df25898d90debee9513bdce7e511471b"})

RECORD = "docs/phases/W8-D6-contact-decision-record.md"
SELF_REL = "tests/test_w8_contact_decision_record.py"
OPENING = "tests/test_w8_contact_decision_opening.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
BRIEF = "docs/phases/W8-D6-contact-decision-brief.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, OPENING, REGISTRY, BOARD})
D6_ENTRIES = frozenset({"W8-D6-CDB", "W8-D6-CDR"})
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
                    "W8-D5-EAB", "W8-D5-AFR", "W8-D6-CDB", "W8-D2-CBC",
                    "ADR-0056", "W7-CR", "W7-D3-MBB")
FIXED_MODULES = (RECOVERY, "tests/test_w8_evidence_adequacy_opening.py",
                 "tests/test_w8_evidence_adequacy_law.py",
                 "tests/test_w8_evidence_adequacy_finding.py")

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py",
           "cdb": OPENING}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    OPENING: ("opening module",
              "sha256:30c5826a9514c6c069dcd408e85823e25b51144d6f57af83b04803817623e7fb",
              "1a40b02a8c4620c2b30862a87b87b94ded8e0453"),
    REGISTRY: ("registry",
               "sha256:0dc11b2c198312e020b1d12d21bb35db7f72085688062d6303f14687e098461c",
               "080046cec585dbfa8c965f48cafb771d48c8be91"),
    BOARD: ("board",
            "sha256:197d6a574cdc22aad968c05e58f16bd07e3edc1ec1638d8a1a1b74e3ffcade38",
            "0251fc71dcad1b2e2bd66f215e35e03f0368bb3b"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {OPENING: ("sha256:94572c3ee65f7895b0630c8fe41c736321ae8db030197db79406009947bd0322", "645758e1f53f7ec60c1cac42ff938d5fd1dd41f5")}

# ------------------------------------- the one succession: the opening's CD7
SITES = {
    OPENING: (
        ('CD7',
         "bytes, in a private namespace. CD7's W8-D6 entry set is the one\npresent-state gate, as the W8-D4 and W8-D5 openings' were, until the\ndecision landing moves it. The residual live reach is disclosed exactly:\n",
         "bytes, in a private namespace. CD7's W8-D6 entry set was the one\npresent-state gate, as the W8-D4 and W8-D5 openings' were, until the\ndecision landing (W8-D6-CDR) succeeded it, its W8-D7 limb included, to\na historical proof at the D6-A landing commit; no present-state gate\nremains in this module, and W8-D7 stays refused by ADR-0058's R9\nalone. The residual live reach is disclosed exactly:\n"),
        ('CD7',
         'D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"\n',
         'D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"\n# The D6-A landing commit, at which CD7\'s W8-D6 entry set and its\n# W8-D7 limb stay proven after their succession at the decision\n# landing (W8-D6-CDR).\nD6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"\n'),
        ('CD7',
         '        # The one present-state gate of this landing, as the W8-D4 and\n        # W8-D5 openings\' were: the W8-D6 entries are exactly this brief\'s\n        # and no W8-D7 entry exists, until the decision landing moves it.\n        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n        with self.subTest(fact="present state: the W8-D6 entries are this "\n                               "brief\'s alone and no W8-D7 entry exists"):\n            self.assertEqual(entry_violations(live, brief, h), [])\n',
         '        # Succeeded at the decision landing (W8-D6-CDR): the W8-D6 entry\n        # set and the absence of any W8-D7 entry stay proven at the D6-A\n        # landing commit. No present-state gate remains here; W8-D7 stays\n        # refused by ADR-0058\'s R9 alone.\n        at_landing = json.loads(committed(D6A_LANDING, REGISTRY))["entries"]\n        with self.subTest(fact="at the D6-A landing: the W8-D6 entries were "\n                               "this brief\'s alone and no W8-D7 entry "\n                               "existed"):\n            self.assertEqual(entry_violations(at_landing, brief, h), [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
CLOSED = "**" + R9_SENTENCE + " W8-D7 remains closed behind its own brief.**"
LIVE_READS = ("(ROOT / " + "REGISTRY).read_" + "bytes()", '"ls-' + 'files"')
PROOFS_MARK = "# ------------------------------------------------------------------ proofs"

# --------------------------------------------------------------- carriage
INSTRUCTION_ITEM = ("1. **The human authority's instruction of 2026-10-30 is "
                    "recorded verbatim below.** One personal name within it is "
                    "rendered by functional role under ADR-0056 and shown in "
                    "square brackets; nothing else is changed, added or omitted.")
INSTRUCTION_BLOCK = (
    "> Dated 30 October 2026.",
    ">",
    "> I authorise D6-B preparation only over the effective baseline "
    "753e6abea8d67a16332799af615fdcfa4aefa7b9. My stated choice is contact.",
    ">",
    "> Prepare a separately attributed assisted reading of the published basis "
    "to support my consideration of that choice, alongside one unaccepted "
    "decision-record and completion candidate. Proposed reasons must remain "
    "identified as assistance pending my express adoption. Do not present them "
    "as words or reasoning I have already supplied.",
    ">",
    "> Follow the effective brief, including probing before fixing the census "
    "and completing CD7’s historical succession, including its W8-D7 limb. "
    "Preserve the D5 finding and every standing contact precondition.",
    ">",
    "> Return the candidate, bound diff and bindings for [the architect]’s "
    "review. Identify any missing human input plainly and together.",
    ">",
    "> This authorises no acceptance, commit, publication, model call, "
    "implementation, provider or route selection, custody access, diagnosis or "
    "D7 work.",
)
DECISION_LINE = ("3. **The outcome this record carries, exactly one of "
                 "`W8-D6-CDB` item 23, as the human authority's stated "
                 "choice:** contact.")
CONTACT_ITEM = "4. **That outcome is carried byte-identically from item 23:**"
INSTRUMENT_ITEM = ("11. **The separate instruments a contact outcome leaves to "
                   "their own authority, named and not supplied** "
                   "(`W8-D6-CDB` item 26):")
INSTRUMENT_LINES = (
    "    - a separately accepted implementation brief, naming ADR-0047 "
    "precondition 3's first-contact gate for the deliverable that would "
    "perform contact;",
    "    - a Tier F crossing record of its own, recording every applicable "
    "crossing for the selected posture;",
    "    - all seven conjunctive preconditions of ADR-0047 Part D holding "
    "together at the moment of contact;",
    "    - the governed handling of ADR-0047 decision 6 for anything captured.",
)
PRECONDITION_SECTION = ("## Part D — The standing of every ADR-0047 Part D "
                        "precondition, unchanged")
PRECONDITION_HEADER = "| # | Precondition | Standing, unchanged by this record |"
PRECONDITION_SEPARATOR = "|---|---|---|"
PRECONDITION_ROWS = [
    ["1", "W5-D2 runtime authority exists", "Satisfied before W7"],
    ["2", "Every applicable Tier F crossing is recorded",
     "Discharged for the W7 no-contact posture, its applicable crossing set "
     "proved empty; a contact-bearing posture needs its own governed crossing"],
    ["3", "A named first-contact gate appears in the brief of the deliverable "
          "that would perform it",
     "Outstanding in its lawful resting state; no gate is named here or "
     "anywhere"],
    ["4", "Synthetic-only artefacts throughout",
     "Law in force; conformance proven at each landing, never presumed"],
    ["5", "No hosted access absent a future governed record opening that class",
     "Closed; not opened here or by implication"],
    ["6", "The generated-output record shape exists and is accepted",
     "Discharged by a published W7 deliverable"],
    ["7", "The harness binding exists and is accepted",
     "Discharged by a published W7 deliverable"],
]
PART_A = "## Part A — The human authority's acts, recorded verbatim"
ITEM_2 = ("2. **These acts are the human authority's alone** (`W8-D6-CDB` items "
          "12, 36 and 37). This record carries them, adds no judgement to them "
          "and interprets nothing in them. The stated choice becomes this "
          "record's decision only by the human authority's acceptance of this "
          "record, with the human authority's reasons stated in Part C before "
          "that acceptance. No mechanical result, count, scan or test "
          "establishes any part of the decision (ADR-0054 decision 22). The "
          "text the act of 2026-10-31 adopts is the architect's, carried "
          "verbatim with its attribution in Parts C and E, and the whole "
          "reading it is taken from is carried as assistance in Part G; its "
          "adoption is the human authority's own act, recorded in the act's "
          "own words above and accounted for in Part G.")
# The human authority's act of 2026-10-31, recorded verbatim in Part A: one
# personal name rendered by functional role under ADR-0056 at each of its
# three occurrences, and the one file name carrying it rendered by its role,
# each in square brackets; nothing else changed.
ACT_ITEM = ("**The human authority's act of 2026-10-31 is recorded verbatim "
            "below.** One personal name within it is rendered by functional "
            "role under ADR-0056 at each of its three occurrences, and the one "
            "file name carrying that name is rendered by its role, each shown "
            "in square brackets; nothing else is changed, added or omitted.")
ACT = (
    "Dated 31 October 2026." "\n\n"
    "I have considered [the architect]’s architect-attributed reading, "
    "[the architect's assisted-reading file], dated 30 October 2026." "\n\n"
    "I expressly adopt the proposed reasoning in section 4 as my "
    "reasons for my stated choice of contact, preserving its sources "
    "and limits. I also adopt section 5’s proposed disposition: all "
    "separate instruments remain unopened, and whether and where to "
    "seek authority for them remains unresolved for a separate governed "
    "act." "\n\n"
    "Record my adoption separately from [the architect]’s attributed "
    "assistance. I adopt no part of the implementer-prepared reading. "
    "Infer no consideration or adoption beyond what I state." "\n\n"
    "Prepare the complete D6-B revision within the existing five paths, "
    "carrying and pinning this act and the adopted text. Revalidate it "
    "and return it for [the architect]’s review." "\n\n"
    "This is preparation only. It authorises no acceptance, commit, "
    "publication, model contact, implementation, route or provider "
    "selection, custody access, diagnosis or D7 work."
)
# The text the act adopts and what is preserved with it: the architect's
# assisted reading of 2026-10-30, carried verbatim. Each block is the
# record's quote lines after its one marker line, pinned by the LF SHA-256
# of those lines as carried. The reading itself is carried whole, as
# assistance, under its own marker in Part G and pinned the same way.
PART_C = "## Part C — Reasons on the published basis (`W8-D6-CDB` item 24)"
PART_E = ("## Part E — What this outcome does not do, and the separate "
          "instruments it leaves")
PART_G = ("## Part G — Separately attributed assistance and the human "
          "authority's express adoption (`W8-D6-CDB` items 12, 33 and 35)")
MARK_REASONS = ("**Adopted reasons — the architect's assisted reading of "
                "2026-10-30, section 4, its proposed reasoning, verbatim:**")
MARK_LIMITS = ("**Preserved with them as assistance, not itself adopted — "
               "that section's closing statement of their limits, verbatim:**")
MARK_SOURCES = ("**Preserved with them as assistance, not itself adopted — "
                "that reading's section 2, the fixed sources the reasoning "
                "cites, verbatim:**")
MARK_DISPOSITION = ("**Adopted disposition — the architect's assisted reading "
                    "of 2026-10-30, section 5, its proposed disposition, "
                    "verbatim:**")
MARK_BASIS = ("**Carried with it as assistance, not itself adopted — that "
              "section's opening statement of its basis and limits, "
              "verbatim:**")
MARK_STANDING = ("**Carried with it as assistance, not itself adopted — that "
                 "section's closing statement of its standing, verbatim:**")
# The reading itself, carried whole as assistance in Part G: every line of
# the file as one quote line (a line the reading quotes becomes a nested
# quote line), so that the file is recoverable exactly; and the statement
# that closes it, keeping the two adopted proposals apart from the rest.
MARK_READING = ("**The assistance considered, carried whole — the architect's "
                "assisted reading of 2026-10-30, every line verbatim as "
                "assistance, none of it the human authority's words "
                "(`W8-D6-CDB` items 33 and 35):**")
READING_CLOSE = ("**Of the reading above, the human authority's act of "
                 "2026-10-31 adopts exactly its section 4 proposed reasoning "
                 "and its section 5 proposed disposition, each carried again "
                 "under its own marker in Parts C and E; every other line of "
                 "it — its provenance, its fixed sources, its account of what "
                 "the basis supplies and where judgement remains, its "
                 "statements of limits and standing, its standing gates and "
                 "its note on use — is the architect's assistance, considered "
                 "by the human authority and not adopted, and no line of it "
                 "becomes the human authority's judgement, a reason of this "
                 "record or an instruction received by its carriage here.**")
CARRIED = {
    MARK_REASONS: "sha256:8d8bcf80b7edbf167e4dbc09f72ee1af1da707aacb5465a4c494e3b84416d8f3",
    MARK_LIMITS: "sha256:9ba6f0bf94faa55940373cccdb10a4f6b54300e44cad307cfca95e374846cfd1",
    MARK_SOURCES: "sha256:cba15d81044d8d41d7e2a4b20f94d4726f0918ac0df291c04c03dc468380f20c",
    MARK_DISPOSITION: "sha256:5552f4b48154e141d8bd6352efef71bd4ba02bcce7cc19b4a8c8d23284b9e870",
    MARK_BASIS: "sha256:23dcd93faec9e052e9322f557ed5129e43b931c2b4f84b5ac4869aa90208c6be",
    MARK_STANDING: "sha256:b5fd95454b13ce92ba96aed66d8cee6689008ac6642e1d0244e72959d1cd372b",
    MARK_READING: "sha256:2b8c83aa4c3bf6513cc170a2a55198a1b5c449ffa1c29760512e99cfcfeb4945",
}
ITEM_6 = ("6. **The human authority's reasons are stated here before this "
          "record's acceptance, in its own words or by its express adoption of "
          "separately attributed assistance; each cites only basis rows of "
          "`W8-D6-CDB` section 3 by identity, path and commit, and a reason the "
          "basis cannot support is not given.**")
ITEM_7 = ("7. **No reason in this record is anyone's but the human "
          "authority's.** It records no recommendation by any assistance, and "
          "no assistance supplies, recommends, infers, defaults or fills the "
          "decision (`W8-D6-CDB` item 37). The adopted reasons are the human "
          "authority's by its own express act; their words are the "
          "architect's, carried with their attribution.")
ITEM_14 = ("14. **Whether and where the separate instruments are taken to their "
           "own authority is the human authority's decision point** "
           "(`W8-D6-CDB` item 36), and none is opened by this record:")
ITEM_17 = ("17. **Any separately attributed assistance the human authority "
           "considers is recorded here as assistance — its role, its date and "
           "the basis rows it read — with the human authority's express "
           "adoption of it, if any, recorded as the human authority's own act, "
           "before this record's acceptance.** Assistance is never the "
           "decision, and silence is never a decision.")
ACCOUNT_LEAD = ("**The record of assistance and adoption, as the human "
                "authority's act of 2026-10-31 states it (Part A):**")
ACCOUNT_LINES = (
    "- **Considered:** the architect's assisted reading of 2026-10-30, "
    "architect-attributed assistance prepared in the architect's role under "
    "`W8-D6-CDB` items 12, 33, 35 and 37, as its section 1 states, citing "
    "basis rows 1, 2, 3, 4, 5, 6, 7, 9, 10, 14 and 15 (its section 2).",
    "- **Adopted, as the human authority's own act:** that reading's section "
    "4 proposed reasoning, as the human authority's reasons for its stated "
    "choice (Part C); and its section 5 proposed disposition of the separate "
    "instruments (Part E).",
    "- **Preserved with the adopted text, carried and not itself adopted:** "
    "the reading's section 2, the fixed sources the reasoning cites, and "
    "section 4's closing statement of its limits (Part C), as the act "
    "directs; and section 5's opening statement of its basis and limits and "
    "its closing statement of its standing (Part E), carried as the "
    "reading's section 7 asks of any adoption.",
    "- **Carried whole as assistance, not adopted:** the reading itself, "
    "every line, below in this part, so that the decision's basis can be "
    "read beside the assistance the human authority considered "
    "(`W8-D6-CDB` items 33 and 35). Of it, the human authority adopts "
    "exactly the two proposals named above and nothing else.",
    "- **Not adopted:** any part of the implementer-prepared reading of "
    "2026-10-30. This record carries none of it.",
    "- **Nothing further is inferred:** the act states no other consideration "
    "or adoption, and this record records none.",
    "- **The adoption stands apart from the assistance:** the adopting act is "
    "the human authority's own words in Part A; the adopted text is the "
    "architect's, verbatim under its attribution in Parts C and E; neither "
    "stands in for the other.",
)
# Each human-input part, from its first pinned line to the part's end:
# exactly these lines, in order, with the pinned blocks' quote lines after
# their markers and no other line of any kind. Part A is pinned whole by
# part_a_lines().
SPANS = (
    (PART_C, (ITEM_6, "", MARK_REASONS, "", "", MARK_LIMITS, "", "",
              MARK_SOURCES, "", "", ITEM_7, "")),
    (PART_E, (ITEM_14, "", MARK_DISPOSITION, "", "", MARK_BASIS, "", "",
              MARK_STANDING, "", "")),
    (PART_G, (ITEM_17, "", ACCOUNT_LEAD, "") + ACCOUNT_LINES
     + ("", MARK_READING, "", "", READING_CLOSE, "")),
)
PENDING_MARK = "PENDING HUMAN INPUT"
RECOMMEND_STATEMENT = ("It records no recommendation by any assistance, and no "
                       "assistance supplies, recommends, infers, defaults or "
                       "fills the decision")
REQUIRED = (
    "These acts are the human authority's alone",
    "The stated choice becomes this record's decision only by the human "
    "authority's acceptance of this record, with the human authority's "
    "reasons stated in Part C before that acceptance.",
    "No mechanical result, count, scan or test establishes any part of the "
    "decision",
    "A contact decision is not contact.",
    "No W8-D6 act transmits anything to a model or receives anything from one",
    "No reason in this record is anyone's but the human authority's.",
    RECOMMEND_STATEMENT,
    "No precondition moves at this landing",
    "The table establishes nothing about whether any discharged precondition "
    "would hold for a contact-bearing posture.",
    "Precondition 3 stays outstanding:",
    "This outcome authorises nothing",
    "No performing deliverable exists in the published law.",
    "this record is not a runway amendment, an added deliverable, an "
    "implementation brief or a Tier F crossing.",
    "The route is not this record's",
    "manual import is contact in full",
    "Assistance is never the decision, and silence is never a decision.",
    "Completion opens nothing.",
    "this record classifies no exchange under ADR-0047 decision 3 and does not "
    "state whether model contact occurred",
    "Model contact and W8-D7 remain outside this record.",
)
COMPLETION = "**W8-D6 completes with the decision recorded**"
LIMITS_ITEM = ("15. **The limits of the effective brief's section 6 bound this "
               "decision and are carried byte-identically, each once:**")
SUCCESSION_SECTION = "## Part K — Proof successions (`W8-D6-CDB` section 9)"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
PROGRAMME_SECTION = "## Part H — W8-D6's completion"
PROGRAMME_HEADER = "| Landing | Act | Identity | Landing commit |"
PROGRAMME_SEPARATOR = "|---|---|---|---|"
PROGRAMME_ROWS = [
    ["D6-A", "the opening brief", "`W8-D6-CDB`",
     "`753e6abea8d67a16332799af615fdcfa4aefa7b9`"],
    ["D6-B", "this record: the decision and the completion", "`W8-D6-CDR`",
     "the one commit that adds this record"],
]

# A bounded fold: marks a reader folds away or a writer may vary, the
# zero-width and soft-hyphen code points removed; whitespace runs made one
# space; case folded. Never a Markdown parser.
FOLDED_MARKS = re.compile("[*_`~​‌‍⁠﻿­]")
NOT_CARRIED = re.compile(r"\bdefer\w*|\binsufficient\s+value\b")
LABELLED = re.compile(r"\b(?:decision|outcome|choice)\b\s*(?:is|:|=|—|-)\s*"
                      r"(?:the\s+)?(?:contact|deferral|presently\s+insufficient"
                      r"\s+value)\b")
RECOMMEND = re.compile(r"recommend")

NON_AUTH_SECTION = "## Part J — Explicit non-authorisations"
NON_AUTH_INTRO = "24. This record and W8-D6's completion do not authorise:"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, harness, "
    "implementation or contact surface;",
    "    - any selection of a route, provider or model class, or any opening or "
    "narrowing of the hosted class;",
    "    - any Tier F crossing, any amendment of ADR-0051, any implementation "
    "brief, any performing deliverable or any first-contact gate;",
    "    - any closure (W8-D7), or the opening of W8-D7;",
    "    - any reopening, re-weighing or amendment of the W8-D5 finding, or any "
    "second adequacy finding;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition or reveal, or any change "
    "to an existing one, including any made from captured generated material;",
    "    - any new grouped outcome count of any kind;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059, ADR-0060 or ADR-0061, or of `W8-D5-EAB`, "
    "`W8-D5-AFR` or `W8-D6-CDB`;",
    "    - any score, rate, ranking, threshold, readiness, safety, correctness, "
    "approval, `certif-` or `complian-` claim;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any discharge, waiver or satisfaction of any ADR-0047 Part D "
    "precondition, any resolution of precondition 3, or any movement of any "
    "carried state.",
)
NON_AUTH_CLOSE = "    **Model contact and W8-D7 remain outside this record.**"
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))

# DR4's row-reference view: each logical paragraph of the record (the
# effective brief's CommonMark blank-line form), line-leading quote markers
# dropped, character references decoded, then the bounded fold above - so
# emphasis and code marks, invisible code points, a soft line break, a
# no-break space or any other whitespace, and case cannot hide an explicit
# numeric reference. Every numeric member of the list or range that follows
# is read, so a valid first row cannot carry an invalid later one, and no
# list runs across a paragraph break. Never a proof of what a citation means.
QUOTE_MARKS = re.compile(r"^[ \t]*(?:>[ \t]?)+", re.M)
ROW_REF = re.compile(r"basis[\s\-‐-―]*rows?")
ROW_NUM = r"[(\[]*\d+(?:\.\d+)*[)\]]*"
ROW_SEP = (r"(?:\s*(?:,|;|/|&|\+|-|[‐-―]|\band\b|\bor\b|\bto\b|"
           r"\bthrough\b)\s*)+|\s+")
ROW_LIST = re.compile(r"[\s:#(\[]*(%s(?:(?:%s)%s)*)" % (ROW_NUM, ROW_SEP,
                                                        ROW_NUM))
# DR4's direct routes, the first eight those the architect's review showed.
ROW_ROUTES_REFUSED = {
    "a plain row outside the table": "basis row 16",
    "the row in bold": "basis row **16**",
    "the row in a code mark": "basis row `16`",
    "the row after a soft line break": "basis row\n16",
    "the row after a no-break space": "basis row 16",
    "the reference capitalised": "Basis row 16",
    "an outside row after a valid one, in bold": "basis rows 1, **16**",
    "an outside row after a valid one, wrapped": "basis rows 1,\n16",
    "a range running outside the table": "basis rows 14–16",
    "an outside row after an alternative": "basis rows 1 or 16",
    "an outside row in brackets": "basis rows (1, 16)",
    "a zero-width space inside the reference": "basis​ row 16",
    "a no-break space as a character reference": "basis row&nbsp;16",
    "a quoted reference wrapped inside the quote": "> basis row\n> 16",
    "a decimal row": "basis row 1.6",
    "row zero": "basis row 0",
}
ROW_ROUTES_ADMITTED = {
    "the last row in bold": "basis row **15**",
    "a row in a code mark": "basis row `3`",
    "a row after a soft line break": "basis row\n4",
    "a row after a no-break space": "basis row 5",
    "the reference capitalised": "Basis row 2",
    "a list ending in the last row, in bold": "basis rows 1, **15**",
    "a list ending in the last row, wrapped": "basis rows 1,\n15",
    "a range ending in the last row": "basis rows 14–15",
    "a quoted reference wrapped inside the quote": "> basis row\n> 15",
    "a list stopped by a paragraph break": "basis row 5\n\n16 numbered",
}
FULL_COMMIT = re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")
PATHLIKE = re.compile(r"(?<![A-Za-z0-9_./-])(?:docs|governance|tests|scripts)/"
                      r"[A-Za-z0-9_./-]+[A-Za-z0-9_]")
SCHEME = "://"

# --------------------------------------- board and registry: authorised edits
CDR_LINK = ("([`W8-D6-contact-decision-record.md`]"
            "(W8-D6-contact-decision-record.md))")
CDR_STATUS_TAIL = (
    "the human authority's decision on the runway's separately governed "
    "question, the outcome contact as the human authority's stated choice, "
    "a decision that authorises nothing, with the human authority's reasons "
    "on the published basis and its disposition of the separate instruments, "
    "both by its express adoption of the architect's separately attributed "
    "assistance, that assistance carried whole beside the adoption, the "
    "standing of every ADR-0047 precondition unchanged, and "
    "the separate instruments any contact would still need named and not "
    "supplied and left unopened, no performing deliverable existing in the "
    "published law; and W8-D6's completion. The opening module's CD7 "
    "succeeds, its W8-D6 entry set and W8-D7 limb, to a historical proof at "
    "the D6-A landing, R9's sentence and constant unchanged and W8-D7 refused "
    "by R9 alone; no model is contacted, no provider, route or model class "
    "is selected and no precondition moves.")
CDR_STATUS = {
    "draft": ("**A draft W8-D6 contact decision record, `W8-D6-CDR`, is before "
              "the human reviewer** " + CDR_LINK + ": if accepted, it would "
              "record " + CDR_STATUS_TAIL),
    "accepted": ("**The W8-D6 contact decision record, `W8-D6-CDR`, is "
                 "accepted** " + CDR_LINK + " — accepted %s: it records "
                 + CDR_STATUS_TAIL),
}
CDR_ROW = ("| W8-D6 — Contact Decision Record (W8-D6-CDR) | "
           "[`W8-D6-contact-decision-record.md`]"
           "(W8-D6-contact-decision-record.md) | ")
CDR_ROW_BODY = (
    "Tier J: **the human authority's contact decision and W8-D6's "
    "completion** — the outcome contact as the human authority's stated "
    "choice, a decision that authorises no contact, credential, provider, "
    "transport, prompt, harness, implementation or contact surface and "
    "selects no route or model class; the reasons on the published basis "
    "the human authority's, by its express adoption of the architect's "
    "separately attributed assistance, carried whole; every ADR-0047 "
    "precondition "
    "unchanged, precondition 3 outstanding; the implementation brief, the "
    "Tier F crossing and the performing deliverable named and not supplied, "
    "every separate instrument left unopened. The "
    "opening module's CD7 succeeds to a historical proof; ADR-0058's R9 "
    "sentence and constant unchanged. **No contact, provider, route, "
    "diagnosis or custody access; the W8-D5 finding stays as recorded; "
    "W8-D7 stays closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
STATUS_LEAD = "contacts no model and preselects no outcome. "
BOARD_STATUS_ANCHOR = STATUS_LEAD + CLOSED
BOARD_ROW_ANCHOR = ("every W8-D3, W8-D4 and W8-D5 record stays fixed; W8-D7 "
                    "stays closed; no model contact.** |\n")
CDR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CDR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D6-CDR", "path": RECORD, "type": "phase-record",
    "title": "W8-D6 - Contact Decision Record",
    "role": (
        "The contact decision record of W8-D6, landing D6-B, the human "
        "authority's own act under the effective opening brief W8-D6-CDB: "
        "carries verbatim the human authority's stated choice in the "
        "runway's closed outcome form - the outcome contact, a decision that "
        "actual model contact is to be pursued which authorises no contact, "
        "credential, provider, transport, prompt, harness, implementation or "
        "contact surface and selects no route or model class; the human "
        "authority's reasons on the published basis and its disposition of "
        "the separate instruments, both by its express adoption of the "
        "architect's separately attributed assistance, with that assistance "
        "carried whole and the record of its adoption; the standing of every "
        "ADR-0047 "
        "precondition, "
        "unchanged, precondition 3 outstanding in its lawful resting state; "
        "and the separate instruments any contact would still need - a "
        "separately accepted implementation brief naming the first-contact "
        "gate, a Tier F crossing record of its own, every precondition "
        "holding together - named and not supplied and left unopened, no "
        "performing "
        "deliverable existing in the published law. Completes W8-D6 with the "
        "decision recorded; completion opens nothing. The opening module's "
        "CD7, its W8-D6 entry set and W8-D7 limb, succeeds to a historical "
        "proof at the D6-A landing, with proof obligations DR1 to DR9; "
        "ADR-0058's R9 sentence and constant stay unchanged and W8-D7 stays "
        "refused by R9 alone. Reopens no finding, diagnoses nothing, reads no "
        "custody and contacts no model; W8-D7 stays closed."),
    "depends_on": ["W8-D6-CDB", "W8-AR", "W8-D5-AFR", "ADR-0061", "W8-D5-EAB",
                   "ADR-0047", "ADR-0046", "ADR-0033", "ADR-0034", "ADR-0049",
                   "ADR-0051", "ADR-0054", "ADR-0058", "W8-D4-CPR", "W7-CR",
                   "W7-D3-MBB", "ADR-0056"],
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
    return " ".join(FOLDED_MARKS.sub("", text).split()).casefold()


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def d6b_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the record, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = d6b_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_cdr_historical_" + Path(rel).stem,
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
    chain's opening link is never written here."""
    ends = [line[2:] for line in baseline_text(CONTACT_LAW).split("\n")
            if line.startswith("> **")
            and line.endswith("no contact ≠ nothing proven.**")]
    return ends[0] if len(ends) == 1 else None


def limit_lines():
    """The effective brief's section-6 items 31 to 35, read from the
    committed brief at the baseline."""
    rows = baseline_text(BRIEF).split("\n")
    out = [l for l in rows if re.match(r"^3[1-5]\. ", l)]
    return out if len(out) == 5 else None


def contact_line(h):
    """The contact outcome line of the effective brief's item 23, read from
    the snapshot-executed opening module and confirmed in the committed
    brief."""
    line = h.cdb.OUTCOME_LINES[1]
    return line if baseline_text(BRIEF).count(line + "\n") == 1 else None


def outside_trusted(text, h):
    out = text
    for block in ("\n".join(INSTRUCTION_BLOCK), DECISION_LINE, contact_line(h)
                  or "\x00", RECOMMEND_STATEMENT):
        out = out.replace(block, "", 1)
    return out


def act_quote():
    return "\n>\n".join("> " + p for p in ACT.split("\n\n"))


def quote_after(rows, i):
    """The quote lines after the marker at rows[i] - one blank line, then
    every line beginning '>' up to a blank line or the end; None unless that
    shape holds."""
    if i + 2 >= len(rows) or rows[i + 1] != "" or not rows[i + 2].startswith(">"):
        return None
    j = i + 2
    while j < len(rows) and rows[j].startswith(">"):
        j += 1
    if j < len(rows) and rows[j] != "":
        return None
    return "\n".join(rows[i + 2:j])


def part_a_lines():
    """Part A exactly: its heading, the instruction's label and quotation,
    the act's label and quotation, and item 2, each line in order, with no
    other line - quoted or not, plain or indented - anywhere in the part."""
    return ((PART_A, "", INSTRUCTION_ITEM, "") + INSTRUCTION_BLOCK
            + ("", ACT_ITEM, "") + tuple(act_quote().split("\n"))
            + ("", ITEM_2, ""))


def span_remainder(span):
    """The span's lines with each carried block's quote lines removed at
    their positions after its marker - exactly those lines and no others -
    so that every other line, quoted or not, stays to be compared."""
    rest, i = [], 0
    while i < len(span):
        rest.append(span[i])
        body = quote_after(span, i) if span[i] in CARRIED else None
        if body is not None:
            rest.append(span[i + 1])
            i += 2 + len(body.split("\n"))
            continue
        i += 1
    return tuple(rest)


def completion_violations(text):
    """Part A exactly its pinned lines; the human act of 2026-10-31 under
    its label, once; each carried block once, after its marker, unaltered;
    each human-input part's stretch exactly its pinned lines around those
    blocks, no other line admitted; no pending slot or marker in any form.
    The draft and the accepted form alike."""
    v = []
    if PENDING_MARK in text:
        v.append("a pending slot or marker remains")
    if section_lines(text, PART_A) != list(part_a_lines()):
        v.append("Part A is not exactly its pinned lines: the two acts, "
                 "their labels and framing, and no other line")
    if text.count(ACT_ITEM + "\n\n" + act_quote() + "\n\n") != 1:
        v.append("the act of 2026-10-31 is not carried once under its label")
    rows = text.split("\n")
    for marker, digest in CARRIED.items():
        at = [i for i, l in enumerate(rows) if l == marker]
        body = quote_after(rows, at[0]) if len(at) == 1 else None
        if body is None:
            v.append("a carried block is not present once: %s" % marker[:52])
        elif _sha(body.encode("utf-8")) != digest:
            v.append("a carried block is altered: %s" % marker[:52])
    for heading, skeleton in SPANS:
        sec = section_lines(text, heading)
        starts = [i for i, l in enumerate(sec or []) if l == skeleton[0]]
        if len(starts) != 1:
            v.append("a human-input part does not open as pinned: %s"
                     % heading[:32])
            continue
        if span_remainder(sec[starts[0]:]) != skeleton:
            v.append("a human-input part is not exactly its pinned lines "
                     "around its blocks: %s" % heading[:32])
    return v


def section_lines(text, heading):
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows) if l == heading]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(rows))
                if rows[j].startswith("## ")), len(rows))
    return rows[heads[0]:end]


def carriage_violations(text, state, h):
    """DR1: the verbatim instruction, the outcome line and the contact
    outcome line, each once and in place; the textual outcome closure; the
    separate instruments, the precondition table and the section-6 limits
    exactly; the nine rules and the chain once; the load-bearing statements
    each once; the human act and the text it adopts carried and pinned,
    and no pending slot, in either form."""
    flat = _flat(text)
    v = []
    block = "\n".join(INSTRUCTION_BLOCK)
    if text.count(INSTRUCTION_ITEM + "\n\n" + block + "\n\n") != 1:
        v.append("the verbatim instruction is not carried once under its label")
    if text.count("\n" + DECISION_LINE + "\n") != 1:
        v.append("the outcome line is not carried exactly once")
    line = contact_line(h)
    if line is None or text.count(CONTACT_ITEM + "\n" + line + "\n") != 1:
        v.append("the contact outcome is not carried byte-identically, once")
    if line is not None and text.count(line) != 1:
        v.append("the contact outcome line occurs more than once")
    out = folded(outside_trusted(text, h))
    v += ["an outcome not carried is named: %s" % m.group(0)
          for m in NOT_CARRIED.finditer(out)]
    v += ["a labelled outcome form: %s" % m.group(0)
          for m in LABELLED.finditer(out)]
    if RECOMMEND.search(out):
        v.append("a recommendation stem outside the pinned negation")
    if text.count(INSTRUMENT_ITEM + "\n" + "\n".join(INSTRUMENT_LINES)
                  + "\n") != 1:
        v.append("the separate instruments are not exactly their four lines")
    rows, problems = h.rev.closed_table(text, PRECONDITION_SECTION,
                                        PRECONDITION_HEADER,
                                        PRECONDITION_SEPARATOR, 3)
    v += problems
    if rows != PRECONDITION_ROWS:
        v.append("the precondition table is not exactly its trusted rows")
    limits = limit_lines()
    if limits is None:
        v.append("the section-6 limits are not in the brief")
    else:
        quoted = "\n\n".join("> " + l for l in limits)
        if text.count(LIMITS_ITEM + "\n\n" + quoted + "\n\n") != 1:
            v.append("the section-6 limits are not carried byte-identically")
    for name, b in (("nine-rule", nine_rules()), ("contact-chain",
                                                  contact_chain())):
        if b is None or text.count("> %s\n" % b) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    if flat.count(_flat(COMPLETION)) != 1:
        v.append("the completion is not stated once")
    v += completion_violations(text)
    return v


def withholding_violations(text):
    """DR2: section J exactly its authorised whole block."""
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return ["section J is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        return ["section J is not exactly its authorised whole block"]
    return []


def basis_commits(h):
    return {r[3] for r in h.cdb.BASIS_ROWS}


def basis_paths(h):
    return {r[2] for r in h.cdb.BASIS_ROWS}


def cited_rows(text, h):
    """Every numeric member of every explicit basis-row reference, as
    written, read through DR4's row-reference view. Paragraphs are parted
    on the source before any character reference is decoded."""
    out = []
    paras = h.cdb.prose_paragraphs(QUOTE_MARKS.sub("", text)).split("\n\n")
    for para in (folded(html.unescape(p)) for p in paras):
        for m in ROW_REF.finditer(para):
            listed = ROW_LIST.match(para, m.end())
            if listed:
                out += re.findall(r"\d+(?:\.\d+)*", listed.group(1))
    return out


def citation_violations(text, h):
    """DR4: every explicit numeric basis-row reference names a row of the
    effective brief's table; every full commit is a basis commit or a
    landing anchor; no hyperlink; no path outside the basis and the
    governing records. Commits and paths are read exactly as written."""
    v = []
    n = len(h.cdb.BASIS_ROWS)
    for x in cited_rows(text, h):
        if not (re.fullmatch(r"\d+", x) and 1 <= int(x) <= n):
            v.append("a cited basis row is outside the basis: %s" % x)
    commits = set(FULL_COMMIT.findall(text))
    if not commits <= basis_commits(h) | ANCHORS:
        v.append("a commit outside the basis and the anchors is named")
    if SCHEME in text:
        v.append("a hyperlink is present")
    allowed = basis_paths(h) | {RECORD, SELF_REL, OPENING, RECOVERY, REGISTRY,
                                BOARD, BRIEF}
    v += ["a path outside the basis and the governing records: %s" % p
          for p in sorted(set(PATHLIKE.findall(text)) - allowed)]
    return v


def batch(commit, paths):
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
    return homes, [paths[r] for r in FIXED_RECORD_IDS] + list(FIXED_MODULES)


def fixed_artefact_violations(now, tracked, homes, records, base):
    v = []
    for home, files in homes.items():
        if not files:
            v.append("a fixed home is empty at the baseline: %s" % home)
        if sorted(p for p in tracked if p.startswith(home + "/")) != files:
            v.append("a fixed home's file set changed: %s" % home)
    for p in [f for files in homes.values() for f in files] + records:
        if p not in now or now[p] != base[p]:
            v.append("a fixed file changed or is missing")
    return v


def succession_rows(h):
    return [["`%s`" % OPENING, ", ".join(h.auth.labels(SITES[OPENING])),
             "`%s`" % PREIMAGE[OPENING][1], "`%s`" % POSTIMAGE[OPENING][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def succession_table_violations(text, h):
    rows, v = h.rev.closed_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                                 SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def cd7_of(src):
    return src.split("class CD7_EntrySet", 1)[1].split("\nclass ", 1)[0]


def succession_violations(present, record, h, sites=None):
    sites = SITES[OPENING] if sites is None else sites
    v = []
    pre = baseline_text(OPENING)
    if _sha(pre.encode("utf-8")) != PREIMAGE[OPENING][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[OPENING][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("CD7",):
        v.append("the sites are not CD7's alone")
    body = cd7_of(present)
    if any(idiom in body for idiom in LIVE_READS):
        v.append("the succeeded CD7 still holds a live read")
    if "committed(D6A_LANDING, REGISTRY)" not in body:
        v.append("the succeeded CD7 does not read the D6-A landing commit")
    if ('D6A_LANDING = "%s"\n' % D6A_LANDING) not in present:
        v.append("the succeeded module does not pin the D6-A landing")
    return v + succession_table_violations(record, h)


def cdr_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CDR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CDR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         STATUS_LEAD + fill(CDR_STATUS[state]) + " " + CLOSED),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + CDR_ROW + fill(ROW_PREFIX[state]) + CDR_ROW_BODY
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


def expected_registry(base_text, record_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, record_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    sample = "2026-01-01"
    return " ".join([CDR_ROW, CDR_ROW_BODY, CDR_STATUS["draft"],
                     CDR_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, record_text, h):
    """DR7: this record's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D6 entries are exactly the brief's and
    this record's; no W8-D7 entry."""
    v = []
    e = {x["id"]: x for x in entries}.get("W8-D6-CDR")
    state, date = h.rec.header_state(record_text)
    if e is None:
        return ["no W8-D6-CDR entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            RECORD, "phase-record", "W8", "W8-D6"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(record_text.encode("utf-8")):
        v.append("the entry's hash differs from the record")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D6"} != D6_ENTRIES:
        v.append("the W8-D6 entries are not exactly the brief's and this "
                 "record's")
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
    call is replaced and the previous state restored on exit."""

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
        ("test_w8_contact_decision_opening", "exposure_violations",
         lambda *a, **k: []),
        ("test_w8_contact_decision_opening", "prose_paragraphs",
         lambda t: t),
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
class DR1_Carriage(unittest.TestCase):
    def test_dr1_record_carries_the_human_act_and_the_closed_outcome(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev", "rec", "cdb")
        text = read(RECORD).decode("utf-8")
        state, date, sv = cdr_state(text, h)
        self.assertEqual(sv, [])
        with self.subTest(fact="carriage, closure and pending slots", state=state):
            self.assertEqual(carriage_violations(text, state, h), [])
        line = contact_line(h)
        for name, mutated in (
                ("a non-carried outcome named plainly", text + "\nDeferral.\n"),
                ("a labelled non-carried outcome in bold",
                 text + "\n**Decision:** deferral.\n"),
                ("the third outcome named", text
                 + "\nThe presently insufficient value outcome.\n"),
                ("a labelled carried outcome in code marks",
                 text + "\n`Outcome: contact`.\n"),
                ("a labelled outcome wrapped over a soft break",
                 text + "\nThe choice is\ncontact.\n"),
                ("a labelled outcome with a zero-width space",
                 text + "\nDecision​: contact.\n"),
                ("a recommendation by assistance",
                 text + "\nThe architect recommends this outcome.\n"),
                ("a recommendation in capitals",
                 text + "\nRECOMMENDED.\n"),
                ("a second outcome line", text.replace(
                    DECISION_LINE, DECISION_LINE + "\n" + DECISION_LINE, 1)),
                ("the outcome line removed", text.replace(
                    DECISION_LINE + "\n", "", 1)),
                ("the contact outcome rewritten", text.replace(
                    line, line.replace("is a decision and not",
                                       "is an authorisation and", 1), 1)),
                ("the verbatim instruction altered", text.replace(
                    "My stated choice is contact.", "My choice is contact.", 1)),
                ("an instrument dropped", text.replace(
                    INSTRUMENT_LINES[1] + "\n", "", 1)),
                ("a precondition row altered", text.replace(
                    "Outstanding in its lawful resting state; no gate",
                    "Discharged; no gate", 1)),
                ("a limit dropped", text.replace(
                    "> " + limit_lines()[2] + "\n\n", "", 1)),
                ("a removed statement", text.replace(
                    REQUIRED[3], "", 1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, state, h))
        for name, mutated in {
                "a pending slot restored": text.replace(
                    MARK_REASONS + "\n", "> **" + PENDING_MARK + " [R]:** "
                    "sentinel.\n\n" + MARK_REASONS + "\n", 1),
                "a pending marker outside its form": (
                    text + "\n" + PENDING_MARK + "\n"),
                "the act altered": text.replace(
                    "> I expressly adopt the proposed reasoning",
                    "> I adopt the proposed reasoning", 1),
                "the act's non-adoption reversed": text.replace(
                    "I adopt no part of the implementer-prepared reading.",
                    "I adopt part of the implementer-prepared reading.", 1),
                "the act's rendering undone": text.replace(
                    "[the architect]’s attributed assistance",
                    "the architect’s attributed assistance", 1),
                "an adopted reason altered": text.replace(
                    "I consider that narrow opportunity worth pursuing",
                    "I consider that opportunity worth pursuing", 1),
                "the reasons' limits dropped": text.replace(
                    MARK_LIMITS + "\n\n" + quote_after(
                        text.split("\n"), text.split("\n").index(MARK_LIMITS))
                    + "\n\n", "", 1),
                "a source row altered": text.replace(
                    "> | 7 | ADR-0033 |", "> | 8 | ADR-0033 |", 1),
                "the adopted disposition altered": text.replace(
                    "> I leave all the separate instruments unopened.",
                    "> I leave the separate instruments unopened.", 1),
                "the adopted reasons re-attributed": text.replace(
                    MARK_REASONS, MARK_REASONS.replace(
                        "the architect's assisted reading of 2026-10-30",
                        "the human authority's own words", 1), 1),
                "a carried block doubled": text.replace(
                    MARK_STANDING + "\n", MARK_STANDING + "\n\n> sentinel\n\n"
                    + MARK_STANDING + "\n", 1),
                "prose added beside an adopted block": text.replace(
                    "\n" + MARK_LIMITS + "\n", "\nThese reasons are the "
                    "implementer's.\n\n" + MARK_LIMITS + "\n", 1),
                "a consideration inferred": text.replace(
                    ACCOUNT_LINES[4] + "\n", ACCOUNT_LINES[4] + "\n- **Considered:** "
                    "the implementer-prepared reading of 2026-10-30.\n", 1),
                "the record of adoption reworded": text.replace(
                    "neither stands in for the other.",
                    "each stands in for the other.", 1),
                # Part A, closed whole (the architect's r3 review, F-1): the
                # two exact review recipes first, then the boundary controls.
                "an extra quotation after the act": text.replace(
                    ACT_ITEM + "\n\n" + act_quote() + "\n\n",
                    ACT_ITEM + "\n\n" + act_quote() + "\n\n"
                    + "> I also authorise an additional crossing.\n\n", 1),
                "an extra quotation after the act, indented": text.replace(
                    ACT_ITEM + "\n\n" + act_quote() + "\n\n",
                    ACT_ITEM + "\n\n" + act_quote() + "\n\n"
                    + " > I also authorise an additional crossing.\n\n", 1),
                "an extra quotation before the act": text.replace(
                    ACT_ITEM + "\n\n", ACT_ITEM + "\n\n> sentinel.\n\n", 1),
                "an extra quotation before the instruction": text.replace(
                    INSTRUCTION_ITEM + "\n\n",
                    INSTRUCTION_ITEM + "\n\n> sentinel.\n\n", 1),
                "an extra quotation after the instruction, indented":
                    text.replace(
                        "\n".join(INSTRUCTION_BLOCK) + "\n\n",
                        "\n".join(INSTRUCTION_BLOCK) + "\n\n > sentinel.\n\n",
                        1),
                "a quotation line joined to the act": text.replace(
                    "> Dated 31 October 2026.",
                    "> Dated 31 October 2026.\n> I also authorise an additional "
                    "crossing.", 1),
                "the act duplicated": text.replace(
                    act_quote() + "\n\n",
                    act_quote() + "\n\n" + act_quote() + "\n\n", 1),
                "the instruction duplicated": text.replace(
                    "\n".join(INSTRUCTION_BLOCK) + "\n\n",
                    "\n".join(INSTRUCTION_BLOCK) + "\n\n"
                    + "\n".join(INSTRUCTION_BLOCK) + "\n\n", 1),
                "an unmarked line added before item 2": text.replace(
                    "\n\n" + ITEM_2,
                    "\n\nThe human authority also said more.\n\n" + ITEM_2, 1),
                "an unmarked line added after item 2": text.replace(
                    ITEM_2 + "\n\n", ITEM_2 + "\n\nA further sentence.\n\n", 1),
                # The reading carried whole (the architect's r3 review, F-2).
                "the carried reading altered": text.replace(
                    "It makes no new adequacy finding",
                    "It makes a new adequacy finding", 1),
                "a section of the carried reading dropped": text.replace(
                    "> ## 7. Use in the decision record\n>\n", "", 1),
                "the carried reading's own quotation flattened": text.replace(
                    "> > The purpose of my stated choice",
                    "> The purpose of my stated choice", 1),
                "the carried reading re-attributed": text.replace(
                    MARK_READING, MARK_READING.replace(
                        "the architect's assisted reading",
                        "the human authority's own reading", 1), 1),
                "the adoption statement widened": text.replace(
                    "adopts exactly its section 4 proposed reasoning and its "
                    "section 5 proposed disposition",
                    "adopts the whole of it", 1),
                "an extra quotation after the carried reading": text.replace(
                    "\n\n" + READING_CLOSE,
                    "\n\n> sentinel.\n\n" + READING_CLOSE, 1)}.items():
            with self.subTest(completion_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(completion_violations(mutated))
                self.assertTrue(carriage_violations(mutated, state, h))
        with self.subTest(positive="Part A admits its two multi-paragraph "
                                   "quotations exactly as they stand"):
            self.assertEqual(section_lines(text, PART_A), list(part_a_lines()))
            self.assertEqual(act_quote().count("\n>\n"), 5)
            self.assertEqual("\n".join(INSTRUCTION_BLOCK).count("\n>\n"), 5)
        h_state = {"draft": ("accepted", CDR_DRAFT, CDR_ACCEPTED % "2000-01-01"),
                   "accepted": ("draft", CDR_ACCEPTED % date, CDR_DRAFT)}
        other, old, new = h_state[state]
        with self.subTest(positive="the %s form of this record is admitted" % other):
            flipped = text.replace(old, new, 1)
            self.assertNotEqual(flipped, text)
            self.assertEqual(carriage_violations(flipped, other, h), [])
        with self.subTest(positive="the fold is the bounded fold"):
            self.assertEqual(folded("Out​come **is**\n  _contact_."),
                             "outcome is contact.")
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev", "rec", "cdb")
                self.assertEqual(carriage_violations(text, state, hh), [])


class DR2_NonAuthorisations(unittest.TestCase):
    def test_dr2_record_carries_its_non_authorisations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="section J is its whole block"):
            self.assertEqual(withholding_violations(text), [])
        tail = NON_AUTH_LINES[-1] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this section.\n"
        for name, mutated in (
                ("a line dropped", text.replace(NON_AUTH_LINES[5] + "\n", "", 1)),
                ("two lines swapped", text.replace(
                    NON_AUTH_LINES[5] + "\n" + NON_AUTH_LINES[6] + "\n",
                    NON_AUTH_LINES[6] + "\n" + NON_AUTH_LINES[5] + "\n", 1)),
                ("an extra line", text.replace(
                    NON_AUTH_LINES[0] + "\n",
                    NON_AUTH_LINES[0] + "\n    - any sentinel line;\n", 1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("a permission sentence after the last line", text.replace(
                    tail, NON_AUTH_LINES[-1] + "\n    This landing authorises "
                    "an additional crossing.\n\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("unmarked prose after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a no-break-space separator", text.replace(
                    tail, NON_AUTH_LINES[-1] + "\n \n" + NON_AUTH_CLOSE
                    + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated))


class DR3_NoExposure(unittest.TestCase):
    def test_dr3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr",
                    "auth", "cdb")
        text = read(RECORD).decode("utf-8")
        exempt = (succession_row_line(h),)
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D6-CDR"]["role"] + " " + by_id["W8-D6-CDR"]["title"]
        for name, surface, ex in (("record", text, exempt),
                                  ("registry role and title", role, ()),
                                  ("board wording this landing adds",
                                   added_board_wording(), ())):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(h.cdb.exposure_violations(surface, h, ex), [])
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
                "a figure split over a soft line break": "score\n5",
                "a figure behind a worded connector and indentation":
                    "score is\n    5",
                "a decimal rate": "an agreement rate of 0.5",
                "a percentage": "50%"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(h.cdb.exposure_violations(
                    text + "\n" + plant + "\n", h, exempt))
        with self.subTest(positive="a genuine blank line keeps two "
                                   "paragraphs apart"):
            self.assertEqual(h.cdb.exposure_violations(
                text + "\nscore\n\n5\n", h, exempt), [])
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr", "auth", "cdb")
                self.assertEqual(hh.cdb.exposure_violations(text, hh, exempt),
                                 [])
                self.assertTrue(hh.cdb.exposure_violations(
                    text + "\nscore\n5\n", hh, exempt))


class DR4_Citations(unittest.TestCase):
    def test_dr4_every_citation_resolves_to_the_basis(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "cdb")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="every citation resolves"):
            self.assertEqual(citation_violations(text, h), [])
        with self.subTest(fact="the record cites the basis"):
            self.assertTrue(cited_rows(text, h))
        for name, plant in {
                "a basis row outside the table": "basis row 16",
                "a commit outside the basis and the anchors": "0" * 40,
                "a hyperlink": "see ht" + "tps" + SCHEME + "example.invalid",
                "a path outside the basis":
                    "docs/phases/W8-D3-human-disposition-record.md"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(citation_violations(
                    text + "\n" + plant + "\n", h))
        for name, plant in ROW_ROUTES_REFUSED.items():
            with self.subTest(row_control="%s is refused" % name):
                self.assertTrue(citation_violations(
                    text + "\n" + plant + "\n", h))
        for name, plant in ROW_ROUTES_ADMITTED.items():
            with self.subTest(row_positive="%s is admitted" % name):
                self.assertEqual(citation_violations(
                    text + "\n" + plant + "\n", h), [])
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "cdb")
                self.assertEqual(citation_violations(text, hh), [])
                self.assertTrue(citation_violations(
                    text + "\nbasis rows 1,\n16\n", hh))


class DR5_FixedArtefacts(unittest.TestCase):
    def test_dr5_every_fixed_home_record_and_module_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tracked = snapshot_tracked(commit)
        homes, records = fixed_paths()
        every = [f for files in homes.values() for f in files] + records
        base = batch(BASELINE, every)
        now = batch(commit, every)
        with self.subTest(fact="fixed homes, records and modules "
                               "byte-identical to the baseline"):
            self.assertEqual(len(base), len(every))
            self.assertEqual(fixed_artefact_violations(
                now, tracked, homes, records, base), [])
        reveal_file = homes["governance/validation-reveal"][0]
        brief = records[FIXED_RECORD_IDS.index("W8-D6-CDB")]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}), tracked),
                "a changed opening brief": (
                    dict(now, **{brief: now[brief] + b" "}), tracked),
                "a changed session-recovery module": (
                    dict(now, **{RECOVERY: now[RECOVERY] + b" "}), tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))


class DR6_CD7Succession(unittest.TestCase):
    def test_dr6_cd7_succession_is_exact_and_historical(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "cdb")
        record = read(RECORD).decode("utf-8")
        present = read(OPENING).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[OPENING][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + OPENING)
                             .strip(), PREIMAGE[OPENING][2])
        with self.subTest(exact_succession=PREIMAGE[OPENING][0]):
            self.assertEqual(succession_violations(present, record, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[OPENING][1])
        with self.subTest(fact="the succeeded CD7's claim holds at the D6-A "
                               "landing commit"):
            self.assertEqual(h.cdb.D6A_LANDING, D6A_LANDING)
            at = json.loads(committed(D6A_LANDING, REGISTRY))["entries"]
            self.assertEqual({e["id"] for e in at
                              if e["deliverable"] == "W8-D6"}, {"W8-D6-CDB"})
            self.assertEqual([e["id"] for e in at
                              if e["deliverable"] in LATER_THAN_D6], [])
        with self.subTest(control="the pre-image's CD7 carried a live read"):
            self.assertTrue(any(idiom in cd7_of(baseline_text(OPENING))
                                for idiom in LIVE_READS))
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[OPENING][1:]),
                "a live read restored": (present.replace(
                    'at_landing = json.loads(committed(D6A_LANDING, REGISTRY))',
                    'at_landing = json.loads(_lf((ROOT / ' + 'REGISTRY).read_'
                    + 'bytes()))', 1), None),
                "the anchor moved to the W8-D5 completion": (present.replace(
                    'D6A_LANDING = "%s"' % D6A_LANDING,
                    'D6A_LANDING = "%s"' % D5_COMPLETION, 1), None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[OPENING] + (("CD7", first, first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                if table is None:
                    self.assertNotEqual(text, present)
                self.assertTrue(succession_violations(text, record, h, table))
        row = succession_row_line(h)
        for name, mutated in (
                ("a duplicated row", record.replace(row + "\n", row + "\n"
                                                    + row + "\n", 1)),
                ("an altered separator", record.replace(
                    SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR,
                    SUCCESSION_HEADER + "\n|---|---|---|", 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "cdb")
                self.assertEqual(succession_violations(present, record, hh), [])


class DR7_RegistryBoardAndEntries(unittest.TestCase):
    def test_dr7_registry_board_and_w8_d6_entries(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        record = read(RECORD).decode("utf-8")
        state, date, v = cdr_state(record, h)
        self.assertEqual(v, [])
        board_pre = baseline_text(BOARD)
        reg_pre = baseline_text(REGISTRY)
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")
        with self.subTest(fact="exact authorised board, R9's sentence once",
                          state=state):
            expected, probs = h.auth.apply_sites(board_pre,
                                                 board_sites(state, date))
            self.assertEqual(probs, [])
            self.assertEqual(board, expected)
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED), 1)
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(
                reg_pre, _sha(read(RECORD)), state, date))
        entries = json.loads(reg)["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(entries, record, h), [])
        with self.subTest(fact="no W8-D7 entry at the baseline"):
            self.assertEqual([e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] in LATER_THAN_D6], [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, _sha(read(RECORD)), other, "2000-01-01"))
        base = entries[-1]
        for name, ents in {
                "a third W8-D6 entry": entries + [dict(
                    base, id="W8-D6-SNT", deliverable="W8-D6")],
                "a W8-D7 entry": entries + [dict(
                    base, id="W8-D7-SNT", deliverable="W8-D7")],
                "a wrong record hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                        if e["id"] == "W8-D6-CDR" else e
                                        for e in entries]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(ents, record, h))


class DR8_Census(unittest.TestCase):
    def test_dr8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the opening module "
                               "change among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, OPENING})
        flat = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?) ## ", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RECOVERY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


class DR9_CompletionWithoutALiveGate(unittest.TestCase):
    def test_dr9_completion_recorded_once_and_no_present_state_gate(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        flat = _flat(text)
        with self.subTest(fact="completion stated once, opening nothing"):
            self.assertEqual(flat.count(_flat(COMPLETION)), 1)
            self.assertEqual(flat.count("Completion opens nothing."), 1)
            self.assertIn("W8-D7 remains closed behind its own brief", flat)
        with self.subTest(fact="the programme table is exactly its rows"):
            h = helpers(read, "rev")
            rows, v = h.rev.closed_table(text, PROGRAMME_SECTION,
                                         PROGRAMME_HEADER,
                                         PROGRAMME_SEPARATOR, 4)
            self.assertEqual(v, [])
            self.assertEqual(rows, PROGRAMME_ROWS)
        tracked = snapshot_tracked(commit)
        entries = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="at this landing's snapshot nothing of W8-D7 "
                               "exists"):
            self.assertEqual([e["id"] for e in entries
                              if e["deliverable"] in LATER_THAN_D6], [])
            self.assertEqual([p for p in tracked if Path(p).name.startswith(
                "W8-D7")], [])
        src = read(SELF_REL).decode("utf-8")
        with self.subTest(fact="this module holds no present-state gate of "
                               "its own"):
            # Split at the marker line itself, never at this constant's own
            # definition, which carries the same text inside quotes.
            self.assertEqual(src.count("\n" + PROOFS_MARK + "\n"), 1)
            body = src.split("\n" + PROOFS_MARK + "\n", 1)[1]
            for idiom in LIVE_READS:
                self.assertNotIn(idiom, body)
        with self.subTest(fact="the succeeded CD7 holds no present-state "
                               "gate"):
            for idiom in LIVE_READS:
                self.assertNotIn(idiom, cd7_of(read(OPENING).decode("utf-8")))
        for name, mutated in {
                "completion stated twice": text.replace(
                    COMPLETION, COMPLETION + " " + COMPLETION, 1),
                "completion dropped": text.replace(COMPLETION, "", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(_flat(mutated).count(_flat(COMPLETION)), 1)


if __name__ == "__main__":
    unittest.main()
