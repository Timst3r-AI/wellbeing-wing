"""W8-D5-C — adequacy finding record proofs (W8-D5-AFR, EF1–EF9).

The finding record that ADR-0061 decision 17 fixes, landed at D5-C together
with W8-D5's completion: the human authority's own threshold answer, reasons
against the seven criteria by express adoption of the architect's separately
attributed assisted reading, the finding - exactly one of the law's three
forms - any named gap, the alternative evidence routes, the attribution of
assistance and the limits. This module proves the record's carriage: the
instruction verbatim; the closed criteria list and the finding form as the
law and the effective brief pin them - the form stated once, and no lawful
form name standing outside the human act, the adopted reading, the finding
line and the record's two pinned restatements, in any emphasis, case or
spacing; the routes and limits byte-identical to the brief; the adopted
reading whole, each part exactly once; the
non-authorisations as one block; the exposure limits over the record's
logical prose paragraphs; every evidential citation inside the law's index;
every fixed artefact unchanged; the exact EL7 succession and its table; the
exact registry, board and census; and W8-D5's completion - each with
planted-mutant or negative controls. Closed validators compare against
trusted expected values held here and refuse unrecognised material rather
than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the record
afterwards - and executes the helpers it relies on, the review-law module
and the opening module among them, from that snapshot's bytes, in a private
namespace. This module holds no present-state gate of its own, and the
succeeded EL7 holds none: W8-D6 and W8-D7 stay refused by ADR-0058's R9
alone (ADR-0061 decision 35). The residual live reach is disclosed
exactly: each snapshot-executed helper module imports, at its own top
level, the live modules it aliases for the fixed-law values it reads from
them, and no more independence than that is claimed.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity, token
name, schema literal or method label as a literal: the lists it checks are
the opening module's pins, executed from the snapshot. It performs no review
and makes no finding; the finding it binds is the human authority's.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that the finding is right, or that any other finding
would be wrong; the meaning of any prose beyond the explicit form names the
textual closure refuses; any answer to the reception threshold or to any
criterion
beyond the human authority's recorded words; that the instrument is mature,
valid or ready; that model contact would or would not add useful evidence;
anything about any case, disposition, divergence or reviewer; that any
model was contacted; or that W8-D6 or W8-D7 may open.
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

# The published, remotely verified W8-D5 review law: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "18d6230b5f7281577c18892dd7b95e9448f310c2"
# Landing provenance anchors a reference may name without citing evidence.
ANCHORS = (BASELINE, "c8e13d47f305e0378609ffec1d31f890f629239d",
           "6704649ed80c27112c00c14093c82645e8d090cf",
           "ce78a242df25898d90debee9513bdce7e511471b")

RECORD = "docs/phases/W8-D5-adequacy-finding-record.md"
SELF_REL = "tests/test_w8_evidence_adequacy_finding.py"
LAWMOD = "tests/test_w8_evidence_adequacy_law.py"
LAW = "docs/decisions/0061-w8-evidence-adequacy-review-law.md"
OPENING = "tests/test_w8_evidence_adequacy_opening.py"
BRIEF = "docs/phases/W8-D5-evidence-adequacy-brief.md"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, LAWMOD, REGISTRY, BOARD})
D5_ENTRIES = frozenset({"W8-D5-EAB", "ADR-0061", "W8-D5-AFR"})
LATER_THAN_D5 = ("W8-D6", "W8-D7")
# Paths a reference may name as governing law, human act or landing
# provenance without citing evidence (ADR-0061 decision 17).
GOVERNING_PATHS = frozenset({BRIEF, LAW, RECORD, SELF_REL, LAWMOD, OPENING,
                             RECOVERY, REGISTRY, BOARD})

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py",
           "ea": OPENING,
           "el": LAWMOD}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    LAWMOD: ("review-law module",
             "sha256:84cacb92c68a1fb77ab2a6adb79185c5cc9ae64fef15fe6a3ea894fa7c47be24",
             "569e019386da6ee5ccf71f2e0fdd9fbd3d5111b4"),
    REGISTRY: ("registry",
               "sha256:fcdd167ac0a10c1ca06bfc0802c5f037de1b6737bc0a80c6594f6844b6aced4b",
               "766e9cd8b9ca8277fae6d1bff4fa404afd4c68b1"),
    BOARD: ("board",
            "sha256:be3026895f0f0cc24a07889d6fb6a5f18254e6688df049f0ebb80c7b00278b26",
            "aed24c3d012b6f56fd2d7bfbb1acf7ad37df2619"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {LAWMOD: ("sha256:2104f9b5d3b1375698c7ec1b13e15817a31bdb9000bf194933dc0c8b3bda7a27", "330658b9c713cea91979aef98323307ba65964da")}

# ------------------------------------------ the one succession: EL7's gates
# The one proof succession the W8-D5-C landing proposes (ADR-0061 Part J,
# decisions 34 and 35): EL7's staged absences stay proven at the review law's
# landing snapshot, and the admission of exactly the finding record, its proof
# module and the one W8-D5 entry this landing adds - and still no W8-D6 or
# W8-D7 entry - is proven at this landing's own fixed snapshot. No
# present-state gate remains: W8-D6 and W8-D7 stay refused by ADR-0058's R9
# alone. Six sites, each an exact transformation of the law module's fixed
# pre-image at 18d6230b. LAWMOD is the module's path.
SITES = {LAWMOD: (
    ("EL7",
     "them, from that snapshot's bytes, in a private namespace. The present-state\n"
     "gates are EL7's staged absences alone, each succeeded only by the finding\n"
     "landing that ADR-0061 Part J names. The residual live reach is disclosed\n"
     "exactly: each snapshot-executed helper module imports, at its own top level,\n",
     "them, from that snapshot's bytes, in a private namespace. EL7's staged\n"
     "absences were the present-state gates until the finding landing (D5-C)\n"
     "succeeded them under ADR-0061 Part J: each former absence stays proven at\n"
     "this landing's own snapshot, and the admission of exactly the finding\n"
     "record, its proof module and the one W8-D5 entry that landing added - and\n"
     "still no W8-D6 or W8-D7 entry - is proven at that landing's own fixed\n"
     "snapshot. No present-state gate remains: W8-D6 and W8-D7 stay refused by\n"
     "ADR-0058's R9 alone. The residual live reach is disclosed exactly: each\n"
     "snapshot-executed helper module imports, at its own top level,\n"),
    ("EL7",
     'FINDING_RECORD = "docs/phases/W8-D5-adequacy-finding-record.md"\n'
     'FINDING_MODULE = "tests/test_w8_evidence_adequacy_finding.py"\n',
     'FINDING_RECORD = "docs/phases/W8-D5-adequacy-finding-record.md"\n'
     'FINDING_MODULE = "tests/test_w8_evidence_adequacy_finding.py"\n'
     "# The finding landing's one W8-D5 entry, admitted with the record and its\n"
     "# module once that landing succeeded EL7's staged absences (Part J).\n"
     'FINDING_ENTRY = "W8-D5-AFR"\n'
     "D5_ENTRIES_AT_FINDING = D5_ENTRIES | {FINDING_ENTRY}\n"),
    ("EL7",
     "def historical(read, rel):\n"
     '    """One helper module as it stands in this landing\'s snapshot, executed in\n',
     "def finding_snapshot(law_commit):\n"
     '    """(commit, violations) for the finding landing (D5-C), the one landing\n'
     "    ADR-0061 Part J lets succeed EL7's staged absences. Before its commit\n"
     "    exists the snapshot is the candidate over a HEAD that must be this\n"
     "    landing's commit; afterwards it is the one commit that added the finding\n"
     "    record, whose sole parent must be this landing's commit. Once that\n"
     '    commit exists the snapshot is fixed: no later entry or path moves it."""\n'
     "    if law_commit is None:\n"
     '        return None, ["this landing is not yet committed"]\n'
     '    adds = _git("log", "--diff-filter=A", "--format=%H", "--",\n'
     "                FINDING_RECORD).split()\n"
     "    if not adds:\n"
     '        head = _git("rev-parse", "HEAD").strip()\n'
     "        return None, ([] if head == law_commit else\n"
     '                      ["uncommitted finding candidate is not over this "\n'
     '                       "landing\'s commit"])\n'
     "    if len(adds) != 1:\n"
     '        return None, ["the finding record was added more than once"]\n'
     '    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]\n'
     "    if parents != [law_commit]:\n"
     '        return adds[0], ["the finding landing\'s sole parent is not this "\n'
     '                         "landing\'s commit"]\n'
     "    return adds[0], []\n"
     "\n"
     "\n"
     "def historical(read, rel):\n"
     '    """One helper module as it stands in this landing\'s snapshot, executed in\n'),
    ("EL7",
     "def staged_absence_violations(tracked, exists, entries):\n"
     '    """EL7: no finding record, no finding proof module, the W8-D5 entries\n'
     '    exactly the brief\'s and this record\'s, no W8-D6 or W8-D7 entry."""\n'
     "    v = []\n"
     "    for p in (FINDING_RECORD, FINDING_MODULE):\n"
     "        if p in tracked or exists(p):\n"
     '            v.append("a finding-landing path exists: %s" % p)\n'
     '    if {e["id"] for e in entries if e["deliverable"] == "W8-D5"} != D5_ENTRIES:\n'
     '        v.append("the W8-D5 entries are not exactly the brief\'s and this "\n'
     '                 "record\'s")\n',
     "def staged_absence_violations(tracked, exists, entries, landed=False):\n"
     '    """EL7: no finding record, no finding proof module, the W8-D5 entries\n'
     "    exactly the brief's and this record's, no W8-D6 or W8-D7 entry - or,\n"
     "    once the finding landing has succeeded these absences (`landed`),\n"
     "    exactly that landing's record, module and one W8-D5 entry admitted,\n"
     '    and still no W8-D6 or W8-D7 entry."""\n'
     "    v = []\n"
     "    for p in (FINDING_RECORD, FINDING_MODULE):\n"
     "        if landed and not (p in tracked and exists(p)):\n"
     '            v.append("a finding-landing path is missing: %s" % p)\n'
     "        if not landed and (p in tracked or exists(p)):\n"
     '            v.append("a finding-landing path exists: %s" % p)\n'
     "    expected = D5_ENTRIES_AT_FINDING if landed else D5_ENTRIES\n"
     '    if {e["id"] for e in entries if e["deliverable"] == "W8-D5"} != expected:\n'
     '        v.append("the W8-D5 entries are not exactly the brief\'s and this "\n'
     '                 "record\'s" + (" and the finding record\'s" if landed\n'
     '                               else ""))\n'),
    ("EL7",
     "        # The present-state gates, each succeeded only by the finding\n"
     "        # landing (ADR-0061 Part J): no finding record, no finding module,\n"
     "        # the W8-D5 entries exactly the brief's and this record's, and no\n"
     "        # W8-D6 or W8-D7 entry.\n"
     '        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n'
     '        with self.subTest(fact="present state: no finding-landing artefact "\n'
     '                               "and the W8-D5 entries exactly the two"):\n'
     "            self.assertEqual(staged_absence_violations(\n"
     '                _git("ls-files").split(), lambda p: (ROOT / p).exists(),\n'
     "                live), [])\n",
     "        # Succeeded at the finding landing (ADR-0061 Part J, decisions 34\n"
     "        # and 35): each former absence stays proven at this landing's\n"
     "        # snapshot above, and the admission of exactly the finding record,\n"
     "        # its proof module and the one W8-D5 entry that landing added - and\n"
     "        # still no W8-D6 or W8-D7 entry - is proven at that landing's own\n"
     "        # fixed snapshot. No present-state gate remains here: W8-D6 and\n"
     "        # W8-D7 stay refused by ADR-0058's R9 alone.\n"
     "        landing, problems = finding_snapshot(commit)\n"
     "        self.assertEqual(problems, [])\n"
     '        at_landing = json.loads(snapshot_bytes(landing, REGISTRY))["entries"]\n'
     "        landed_tracked = snapshot_tracked(landing)\n"
     '        with self.subTest(fact="at the finding landing\'s snapshot: exactly "\n'
     '                               "its record, module and W8-D5 entry admitted"):\n'
     "            self.assertEqual(staged_absence_violations(\n"
     "                landed_tracked, lambda p: p in landed_tracked, at_landing,\n"
     "                landed=True), [])\n"),
    ("EL7",
     '                "the brief\'s entry removed": (\n'
     "                    tracked, lambda p: False,\n"
     '                    [e for e in at_snapshot if e["id"] != "W8-D5-EAB"])}.items():\n'
     '            with self.subTest(control="%s is refused" % name):\n'
     "                self.assertTrue(staged_absence_violations(*args))\n",
     '                "the brief\'s entry removed": (\n'
     "                    tracked, lambda p: False,\n"
     '                    [e for e in at_snapshot if e["id"] != "W8-D5-EAB"])}.items():\n'
     '            with self.subTest(control="%s is refused" % name):\n'
     "                self.assertTrue(staged_absence_violations(*args))\n"
     "        # Historical controls over mutated copies of the finding landing's\n"
     "        # fixed snapshot: none reads the present registry or tree, and none\n"
     "        # demands the refusal of any genuinely later entry.\n"
     '        with self.subTest(control="the former absences at the finding "\n'
     '                                  "landing\'s snapshot are refused"):\n'
     "            self.assertTrue(staged_absence_violations(\n"
     "                landed_tracked, lambda p: p in landed_tracked, at_landing))\n"
     "        for name, args in {\n"
     '                "a fourth W8-D5 entry at the finding landing\'s snapshot": (\n'
     "                    landed_tracked, lambda p: p in landed_tracked,\n"
     '                    at_landing + [dict(base, id="W8-D5-SNT",\n'
     '                                       deliverable="W8-D5")]),\n'
     '                "a W8-D6 entry at the finding landing\'s snapshot": (\n'
     "                    landed_tracked, lambda p: p in landed_tracked,\n"
     '                    at_landing + [dict(base, id="W8-D6-SNT",\n'
     '                                       deliverable="W8-D6")]),\n'
     '                "the finding record missing at the finding landing\'s "\n'
     '                "snapshot": (\n'
     "                    [p for p in landed_tracked if p != FINDING_RECORD],\n"
     "                    lambda p: p != FINDING_RECORD and p in landed_tracked,\n"
     "                    at_landing),\n"
     '                "the finding entry missing at the finding landing\'s "\n'
     '                "snapshot": (\n'
     "                    landed_tracked, lambda p: p in landed_tracked,\n"
     '                    [e for e in at_landing if e["id"] != FINDING_ENTRY])}.items():\n'
     '            with self.subTest(control="%s is refused" % name):\n'
     "                self.assertTrue(staged_absence_violations(*args, landed=True))\n"),
)}

# ------------------------------------------------------ the human act, bound
# The human authority's instruction of 2026-10-26, recorded verbatim in the
# record's Part A: two personal names rendered by functional role under
# ADR-0056 and shown in square brackets, nothing else changed.
INSTRUCTION = "**26 October 2026**\n\nMy reception judgement is that the published handling route is sufficient as it stands.\n\nMy finding is **undetermined**: the published evidence does not settle whether actual model contact would add useful evidence of the permitted kind beyond what the synthetic record already supplies.\n\nI expressly adopt [the architect]’s attributed assisted reading dated 26 October 2026, supplied as [the architect's assisted-reading file of that date], as the basis for my reasoning against the seven criteria, with its stated sources and limitations. Preserve that assistance separately attributed, alongside my own judgements.\n\nI authorise **D5-C preparation only**, under ADR-0061 decision 28, over `18d6230b5f7281577c18892dd7b95e9448f310c2`, binding these judgements.\n\nRun the placeholder probe over every existing check before fixing the census. Apply only the authorised exact successions, preserve the historical proofs and R9 sentence and constant, and return one unaccepted finding-and-completion candidate. Report any unlisted refusal or missing human input; infer no additional judgement.\n\nThis authorises no acceptance, commit, publication, diagnosis, custody access, model contact, D6 or D7 work."
THRESHOLD = "the published handling route is sufficient as it stands"
FORM = "undetermined"
FINDING_LINE = ("8. **The finding, exactly one form of ADR-0061 decision 16:** "
                "undetermined — the published evidence does not settle the "
                "question.")
# The record's own two restatements of the chosen form outside the human
# act, the adopted reading and the finding line: pinned here, each carried
# exactly once, the only other places a lawful form name may stand.
POSITION_SENTENCE = ("It carries the human authority's own threshold answer, "
                     "reasons, finding and express adoption of separately "
                     "attributed assistance — the finding is undetermined — "
                     "and completes W8-D5.")
COMPLETE_SENTENCE = "An undetermined finding is complete, never a failure"
FORM_RESTATEMENTS = (POSITION_SENTENCE, COMPLETE_SENTENCE)
THRESHOLD_LINE = ("3. **The human authority's threshold answer, in its own "
                  "words: \"the published handling route is sufficient as it "
                  "stands.\"** It answers the question ADR-0061 decision 9 "
                  "asks")
CRITERION_FIVE_LINE = ("**The human authority's threshold answer (Part B):** "
                       "the published handling route is sufficient as it "
                       "stands.")
ADOPTION_LEAD = ("14. **The human authority's express adoption, 2026-10-26, "
                 "in the words of Part A:** \"")
CRITERION_HEADINGS = ("### Criterion one — discrimination",
                      "### Criterion two — uncertainty",
                      "### Criterion three — challenge",
                      "### Criterion four — limits",
                      "### Criterion five — reception",
                      "### Criterion six — marginal value",
                      "### Criterion seven — independence")
PART_D = "## Part D — The finding (ADR-0061 Part E)"
PART_G = ("## Part G — Separately attributed assistance and the human "
          "authority's express adoption (ADR-0061 Part G)")
# The adopted assisted reading, carried whole: each part's marker line in
# the record and the LF SHA-256 of the part's body as rendered - personal
# names by functional role, hyperlinks as published path and commit, one
# place name omitted, nothing else changed.
READING_PARTS = (
    ("**Adopted basis — the architect's assisted reading, section 1:**",
     'sha256:69d2dd88f752eec713b6fa34d9dd96b9bbf4925cabca4a293f95366170668a03'),
    ("**Adopted basis — the architect's assisted reading, section 2:**",
     'sha256:39657f6291cbb8146aef8d24bd083f5b2fe51f43468a6d529db8c357dc5b9804'),
    ("**Adopted basis — the architect's assisted reading, section 3:**",
     'sha256:1d26c4e7e1a11e127e1569d12a048d8327238fa623d4d01a1a8033f1a14eda0e'),
    ("**Adopted basis — the architect's assisted reading, section 4:**",
     'sha256:5024335b60ed8bbaefe8b42fe9a75e3cebdd8ea38dded733838a4e025e9da906'),
    ("**Adopted basis — the architect's assisted reading, section 5:**",
     'sha256:a8bcfb915a5b2a7cdb2876134a1f5d3a98045382f7b4a53d486bfd128de703a8'),
    ("**Adopted basis — the architect's assisted reading, section 6:**",
     'sha256:09cc755e7e7a8452199ef448a7b4f94650bd0c4b5e1db353363ed6b1ef2fe3ea'),
    ("**Adopted basis — the architect's assisted reading, section 7:**",
     'sha256:93a7595b96ca17456152defef316197a5abd01cc550e3bac8eac556e6cd458ff'),
    ("15. **The reading's statement of its standing, scope and provenance, verbatim:**",
     'sha256:e6fdd4cb10c84f9566abbecaf8e53cfeb2624d41028af1cee3a5ea5ce44b8fd3'),
    ("16. **The reading's preface on the reception question, verbatim:**",
     'sha256:fea1c3dfe0e0be825363a1743fa238d57c08f9aeb075885c1b6eb0cea275bddd'),
    ("17. **The reading's closing statement of what remains the human act, verbatim:**",
     'sha256:a6726eafee57162a6392af3a5ee4716731c826a761710dc163c889f3e8a65c3b'),
    ("18. **The index rows the reading cites, by published path and commit, verbatim from the reading's own table rendered without hyperlinks** (ADR-0061 Part F):",
     'sha256:c69693c8c55e78579f7c53a0054fdcff7cfd8db183ea7bebf6e3a729a83af294'),
)
READING_ROWS = (1, 3, 6, 7, 9, 12, 13, 14, 15, 16, 17, 18, 19, 27, 28, 29)
PREP_ROWS = (6, 12, 13, 14, 15, 18, 19, 27, 29)
# Load-bearing statements, each exactly once in the flattened record.
REQUIRED = (
    "These acts are the human authority's alone",
    "no mechanical result, count, scan or test establishes any part of the "
    "finding",
    "The threshold answer settles no finding form by itself",
    COMPLETE_SENTENCE,
    "No gap is named.",
    "none is authorised, scheduled, recommended or foreclosed by this record",
    "It is assistance, never the finding",
    "Adoption is the human authority's own act, recorded here before this "
    "record's acceptance",
    "no other assistance was adopted",
    "W8-D5 completes with the finding recorded",
    "Completion opens nothing.",
    "W8-D6 needs its own brief and authorisation, which neither this record "
    "nor the finding supplies",
    "does not state whether model contact occurred",
    "no W8-D5 finding discharges, waives or satisfies any of ADR-0047 Part "
    "D's preconditions",
    "No criterion is recorded here as unanswerable",
    "Every EF row proves mechanics and carriage only.",
    "Its finding is the human authority's bounded answer to one fixed "
    "question on one fixed index, and nothing more.",
    POSITION_SENTENCE,
)
WITHHELD = ("decides nothing about W8-D6", "amends no disposition",
            "diagnoses no divergence", "names no case", "reads no custody",
            "contacts no model",
            "W8-D6 and W8-D7 remain closed behind their own briefs",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "any contact decision (W8-D6) or closure (W8-D7)",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record",
            "any new grouped outcome count, rate or ranking by corpus, "
            "authored class or validation method",
            "any resolution of ADR-0047 precondition 3 or of any carried "
            "state")
NON_AUTH_SECTION = "## Part K — Explicit non-authorisations"
NON_AUTH_INTRO = "28. This record and W8-D5's completion do not authorise:"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - any contact decision (W8-D6) or closure (W8-D7), or the opening of "
    "either;",
    "    - any finding by anyone but the human authority, or any reading of "
    "this finding as a readiness, safety, correctness or approval claim;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition or reveal, or any "
    "change to an existing one, including any made from captured generated "
    "material;",
    "    - any new grouped outcome count, rate or ranking by corpus, authored "
    "class or validation method;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059, ADR-0060 or ADR-0061, or of `W8-D5-EAB`;",
    "    - any score, rate, ranking, threshold, readiness, safety, "
    "correctness, approval, `certif-` or `complian-` claim;",
    "    - any use, as evidence, of any path, commit or object outside the "
    "index of ADR-0061 Part F;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any resolution of ADR-0047 precondition 3 or of any carried state.",
)
NON_AUTH_CLOSE = ("    **Model contact, W8-D6 and W8-D7 remain outside this "
                  "record.**")
# Part K whole: heading, blank, introducing item, the twelve lines, blank,
# closing sentence, trailing blank - compared as one block, nothing skipped.
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))
SUCCESSION_SECTION = "## Part L — Proof successions (ADR-0061 Part J)"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
CENSUS_LEAD = "**This landing's census is exactly five paths:** "
COMPLETION = "**W8-D5 completes with the finding recorded**"
ROUTES_LEAD = ("11. **The alternative routes are carried byte-identically "
               "from the effective brief, so that the finding is not read "
               "against an empty comparison:**")
LIMITS_LEAD = ("20. **The limits of the effective brief's section 6 bound this "
               "finding and are carried byte-identically, each once:**")

# --------------------------------------- board and registry: authorised edits
AFR_LINK = ("([`W8-D5-adequacy-finding-record.md`]"
            "(W8-D5-adequacy-finding-record.md))")
AFR_STATUS_TAIL = (
    "W8-D5 with the human authority's finding recorded — undetermined: on the "
    "published evidence alone, the question whether actual model contact "
    "would add useful evidence is not settled — with the threshold answer "
    "that the published handling route is sufficient as it stands, the "
    "reasons against the seven criteria by express adoption of the "
    "architect's separately attributed assisted reading over the review "
    "law's evidence index alone, no gap named, and the alternative routes "
    "and the limits carried from the opening brief; the review law's EL7 "
    "staged absences succeed at this landing, R9's sentence and constant "
    "unchanged; the finding decides nothing about W8-D6, which needs its own "
    "brief and authorisation.")
AFR_STATUS = {
    "draft": ("**A draft W8-D5 adequacy finding record, `W8-D5-AFR`, is "
              "before the human reviewer** " + AFR_LINK + ": if accepted, it "
              "would complete " + AFR_STATUS_TAIL),
    "accepted": ("**The W8-D5 adequacy finding record, `W8-D5-AFR`, is "
                 "accepted** " + AFR_LINK + " — accepted %s: it completes "
                 + AFR_STATUS_TAIL),
}
AFR_ROW = ("| W8-D5 — Adequacy Finding Record (W8-D5-AFR) | "
           "[`W8-D5-adequacy-finding-record.md`]"
           "(W8-D5-adequacy-finding-record.md) | ")
AFR_ROW_BODY = (
    "Tier J: **the human authority's finding and W8-D5's completion** — the "
    "threshold answer that the published handling route is sufficient as it "
    "stands; the reasons against the seven criteria by express adoption of "
    "the architect's separately attributed assisted reading, carried "
    "verbatim and cited to the review law's evidence index alone; the "
    "finding, exactly one of the law's forms: undetermined — the published "
    "evidence does not settle the question; no gap named; the alternative "
    "routes and the limits carried from the opening brief; W8-D5 complete "
    "with the finding recorded. The review law's EL7 staged absences succeed "
    "at this landing; ADR-0058's R9 sentence and constant stay unchanged. "
    "**No contact decision, diagnosis, custody access or contact capability; "
    "every disposition and divergence stays as published; W8-D6 and W8-D7 "
    "stay closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
CLOSED_AFTER = ("**" + R9_SENTENCE + " W8-D6 and W8-D7 remain closed behind "
                "their own briefs.**")
# The review law's status sentence closes directly before the retained R9
# sentence, and its row is the table's last.
LAW_CLOSE = "human authority's own act at the finding landing. "
BOARD_STATUS_ANCHOR = LAW_CLOSE + CLOSED_AFTER
BOARD_ROW_ANCHOR = ("every W8-D3, W8-D4 and W8-D5 record stays fixed; W8-D6 "
                    "and W8-D7 stay closed; no model contact.** |\n")
AFR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
AFR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D5-AFR", "path": RECORD, "type": "phase-record",
    "title": "W8-D5 - Adequacy Finding Record",
    "role": (
        "The W8-D5 adequacy finding record of landing D5-C, the human "
        "authority's own act under ADR-0061: carries verbatim the human "
        "authority's threshold answer that the published handling route is "
        "sufficient as it stands; the reasons against the seven criteria by "
        "express adoption of the architect's separately attributed assisted "
        "reading of the published evidence, index rows only; and the "
        "finding, exactly one of the law's forms - undetermined, the "
        "published evidence does not settle the question. Names no gap; "
        "carries the alternative evidence routes and the limits of the "
        "opening brief byte-identically; completes W8-D5 with the finding "
        "recorded. The review law's EL7 staged absences succeed at this "
        "landing; ADR-0058's R9 sentence and constant stay unchanged. "
        "Decides nothing about W8-D6, amends no disposition, diagnoses no "
        "divergence, names no case, reads no custody, contacts no model and "
        "carries no score, rate, ranking or readiness claim; W8-D6 and W8-D7 "
        "stay closed."),
    "depends_on": ["ADR-0061", "W8-D5-EAB", "W8-AR", "ADR-0054", "ADR-0047",
                   "ADR-0046", "ADR-0055", "ADR-0057", "ADR-0058", "ADR-0059",
                   "ADR-0060", "W8-D2-DIB", "W8-D2-DIC", "W8-D3-SCB",
                   "W8-S1-SOB", "W8-S1-SCR", "W8-S1-CM-01", "W8-D3-HDR",
                   "W8-D3-DR-01", "W8-D3-CCR", "W8-D4-IVB", "W8-D4-VCR",
                   "W8-V1-CM-01", "W8-V1-CM-02", "W8-D4-VSR", "W8-D4-DR-01",
                   "W8-D4-VRC", "W8-D4-CPR", "W8-D2-CBC", "ADR-0056",
                   "W7-CR"],
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


# Marks a reader folds away or a writer may vary when naming a form:
# emphasis and code marks, the zero-width and soft-hyphen code points. The
# fold removes them, makes every whitespace run one space and folds case -
# a bounded textual fold, never a Markdown parser.
FOLDED_MARKS = re.compile("[*_`~\u200b\u200c\u200d\u2060\ufeff\u00ad]")


def folded(text):
    return " ".join(FOLDED_MARKS.sub("", text).split()).casefold()


def _blob(raw):
    return subprocess.run(["git", "hash-object", "--stdin"], input=raw,
                          cwd=ROOT, capture_output=True,
                          check=True).stdout.decode().strip()


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def d5c_snapshot():
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
    commit, problems = d5c_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_eaf_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def brief_item(n):
    """One numbered item of the effective brief at the baseline, its text
    after the number - the brief writes each as one line."""
    lines = [l for l in baseline_text(BRIEF).split("\n")
             if l.startswith("%d. " % n)]
    return lines[0][len("%d. " % n):] if len(lines) == 1 else None


def instruction_quote():
    return "\n>\n".join("> " + p for p in INSTRUCTION.split("\n\n"))


def block_after(text, marker, ea):
    """The record's lines after the one line equal to `marker`, up to the
    next heading or numbered item, outer blank lines stripped; None unless
    the marker occurs exactly once."""
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows) if l == marker]
    if len(heads) != 1:
        return None
    body = []
    for l in rows[heads[0] + 1:]:
        if l.startswith("#") or ea.ITEM.match(l):
            break
        body.append(l)
    return "\n".join(body).strip("\n")


def carriage_violations(text, h):
    """EF1: the instruction verbatim once; the threshold answer and the
    finding in its words; exactly one finding form in the law's wording,
    stated once, and no lawful form name outside the trusted regions, in
    any emphasis, case or spacing; the criteria list and headings;
    the routes and limits byte-identical to the brief; the nine rules and
    the chain once; the adopted reading whole, each part once; the
    load-bearing statements once; no preselecting wording."""
    ea = h.ea
    flat = _flat(text)
    v = []
    if text.count(instruction_quote()) != 1:
        v.append("the instruction is not quoted verbatim exactly once")
    if INSTRUCTION.count(THRESHOLD) != 1 or FORM not in INSTRUCTION:
        v.append("the bound instruction does not carry the threshold answer "
                 "and the finding")
    rows = text.split("\n")
    if sum(1 for l in rows if l.startswith(THRESHOLD_LINE)) != 1:
        v.append("the threshold answer is not stated once in Part B")
    if rows.count(CRITERION_FIVE_LINE) != 1:
        v.append("the threshold answer is not carried into criterion five")
    if rows.count(FINDING_LINE) != 1:
        v.append("the finding line is not present exactly once")
    law_form = [l for l in ea.FORM_LINES if l.strip().startswith("- **%s**" % FORM)]
    if len(law_form) != 1 or not FINDING_LINE.endswith(
            law_form[0].strip()[len("- **%s**" % FORM):]):
        v.append("the finding line is not the law's wording of its form")
    # Outside the trusted regions - the human act and the adopted reading,
    # which name the three forms as the law does, the finding line, and the
    # record's two pinned restatements of the chosen form - no lawful form
    # name stands at all, in any emphasis, case or spacing: the record
    # states the finding once, in the finding line, and declares no other.
    # A textual closure over the explicit form names; it proves no meaning
    # of any other prose.
    outside = text.replace(instruction_quote(), "", 1)
    for marker, _ in READING_PARTS:
        body = block_after(text, marker, ea)
        if body:
            outside = outside.replace(body, "", 1)
    for region in (FINDING_LINE,) + FORM_RESTATEMENTS:
        outside = outside.replace(region, "", 1)
    named = folded(outside)
    v += ["a lawful finding form is named outside the human act, the adopted "
          "reading, the finding line and the pinned restatements: %s" % form
          for form in ea.FORMS if form in named]
    adoption = [l for l in rows if l.startswith(ADOPTION_LEAD)]
    if len(adoption) != 1 or INSTRUCTION.split("\n\n")[3] not in adoption[0]:
        v.append("the express adoption is not quoted once in Part G")
    v += ea.closed_list_violations(text, ea.CRITERIA_LINES, ea.CRITERIA,
                                   "criterion")
    brief = baseline_text(BRIEF)
    if ea.closed_list_violations(brief, ea.CRITERIA_LINES, ea.CRITERIA,
                                 "criterion"):
        v.append("the effective brief does not carry the pinned criteria")
    heads = [l for l in rows if l.startswith("### ")]
    if heads != list(CRITERION_HEADINGS):
        v.append("the criterion headings are not exactly the seven, in order")
    for n in range(1, 8):
        marker = ("**Adopted basis — the architect's assisted reading, "
                  "section %d:**" % n)
        if text.count(marker) != 1:
            v.append("criterion %d has no single adopted-basis marker" % n)
    routes, limits = brief_item(26), [brief_item(n) for n in range(27, 33)]
    if routes is None or text.count("\n> " + routes + "\n") != 1:
        v.append("the alternative routes are not carried once from the brief")
    for n, item in zip(range(27, 33), limits):
        if item is None or text.count("> %d. %s\n" % (n, item)) != 1:
            v.append("brief item %d is not carried once" % n)
    for name, block in (("nine-rule", ea.nine_rules()),
                        ("contact-chain", ea.contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    for marker, pin in READING_PARTS:
        body = block_after(text, marker, ea)
        if body is None:
            v.append("reading part marker not present once: %s" % marker[:40])
        elif _sha(body.encode("utf-8")) != pin:
            v.append("reading part altered: %s" % marker[:40])
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    low = flat.lower().replace(ea.RUNWAY_QUESTION.lower(), "")
    v += ["preselecting wording: %s" % p for p in ea.PRESELECTION if p in low]
    return v


def withholding_violations(text, ea):
    """EF2: every withheld phrase present, and Part K exactly its authorised
    whole block."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = ea.section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["Part K is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("Part K is not exactly its authorised whole block")
    return v


def succession_rows(h):
    return [["`%s`" % LAWMOD, ", ".join(h.auth.labels(SITES[LAWMOD])),
             "`%s`" % PREIMAGE[LAWMOD][1], "`%s`" % POSTIMAGE[LAWMOD][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def exposure_violations(text, h):
    """EF3: the opening module's textual guard over the text's logical prose
    paragraphs, the succession row the one exempt exact line."""
    return h.ea.exposure_violations(h.el.prose_paragraphs(text), h,
                                    exempt=(succession_row_line(h),))


CITATION = re.compile(r"\[Rows? ([^\]]*)\]")
ROW_LIST = re.compile(r"index rows ((?:\d+(?:, | and ))*\d+)")
READING_TABLE_ROW = re.compile(
    r"^\| (\d+) \| ([^|]+?) \| `([^`]+)` \| `([0-9a-f]{40})` \|$", re.M)
PATHLIKE = re.compile(r"(?<![A-Za-z0-9_./-])(?:docs|governance|tests)/[A-Za-z0-9_./-]+")


def cited_rows(text):
    nums = set()
    for m in CITATION.finditer(text):
        for part in re.findall(r"\d+(?:[–-]\d+)?", m.group(1).split(";")[0]):
            if "–" in part or "-" in part:
                a, b = re.split("[–-]", part)
                nums |= set(range(int(a), int(b) + 1))
            else:
                nums.add(int(part))
    for m in ROW_LIST.finditer(text):
        nums |= {int(x) for x in re.findall(r"\d+", m.group(1))}
    return nums


def citation_violations(text, h):
    """EF4: every cited row is an index row; the reading's table is exactly
    those rows' identities, paths and commits as the index pins them; every
    commit named is an index commit or a landing anchor; no hyperlink, and
    no path outside the index and the governing records."""
    index = h.el.INDEX
    v = []
    table = {int(m[1]): (m[2].strip(), m[3], m[4])
             for m in READING_TABLE_ROW.finditer(text)}
    if set(table) != set(READING_ROWS):
        v.append("the reading's table rows are not the pinned rows")
    for n, (ident, path, commit) in table.items():
        if not 1 <= n <= len(index):
            v.append("a table row is outside the index: %d" % n)
            continue
        bullet, label, ipath, icommit, obj, sha, files = index[n - 1]
        if (ident, path, commit) != (label, ipath, icommit):
            v.append("table row %d differs from the index" % n)
    cited = cited_rows(text)
    if not cited or not cited <= set(range(1, len(index) + 1)):
        v.append("a cited row is outside the index")
    if not cited <= set(READING_ROWS) | set(PREP_ROWS):
        v.append("a cited row is outside the reading's table")
    commits = set(re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", text))
    allowed = {r[3] for r in index} | set(ANCHORS)
    if not commits <= allowed:
        v.append("a commit outside the index and the anchors is named")
    if "http" in text:
        v.append("a hyperlink is present")
    paths = set(PATHLIKE.findall(text))
    allowed_paths = {r[2] for r in index} | GOVERNING_PATHS
    stray = {p for p in paths if p.rstrip(".") not in allowed_paths}
    if stray:
        v.append("a path outside the index and the governing records: %s"
                 % sorted(stray)[0])
    return v


def fixed_paths():
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    return base_tracked, [p for p in base_tracked
                          if p not in (LAWMOD, REGISTRY, BOARD)]


def fixed_artefact_violations(changed, tracked, fixed, base_tracked, homes):
    v = []
    moved = sorted(set(changed) & set(fixed))
    if moved:
        v.append("a fixed path changed: %s" % moved[0])
    missing = sorted(set(base_tracked) - set(tracked))
    if missing:
        v.append("a baseline path is missing: %s" % missing[0])
    for home in homes:
        extra = sorted(p for p in tracked if p.startswith(home + "/")
                       and p not in base_tracked)
        if extra:
            v.append("an extra file in a fixed home: %s" % extra[0])
    return v


def succession_table_violations(text, h):
    rows, v = h.rev.closed_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                                 SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, record, h, sites=None):
    """EF6: the law module is the exact reviewed post-image of its fixed
    pre-image under the EL7 sites, reversible, and Part L's table is exactly
    its trusted row."""
    sites = SITES[LAWMOD] if sites is None else sites
    v = []
    pre = baseline_text(LAWMOD)
    if _sha(pre.encode("utf-8")) != PREIMAGE[LAWMOD][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[LAWMOD][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("EL7",):
        v.append("the sites are not EL7's alone")
    return v + succession_table_violations(record, h)


def record_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and AFR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (AFR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         LAW_CLOSE + fill(AFR_STATUS[state]) + " " + CLOSED_AFTER),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + AFR_ROW + fill(ROW_PREFIX[state]) + AFR_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D5",
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
    return " ".join([AFR_ROW, AFR_ROW_BODY, AFR_STATUS["draft"],
                     AFR_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, record_text, h):
    """EF7: this record's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D5 entries are exactly the brief's, the
    law's and this record's; no W8-D6 or W8-D7 entry."""
    v = []
    e = {x["id"]: x for x in entries}.get("W8-D5-AFR")
    state, date = h.rec.header_state(record_text)
    if e is None:
        return ["no W8-D5-AFR entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            RECORD, "phase-record", "W8", "W8-D5"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(record_text.encode("utf-8")):
        v.append("the entry's hash differs from the record")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D5"} != D5_ENTRIES:
        v.append("the W8-D5 entries are not exactly the three")
    if [x["id"] for x in entries if x["deliverable"] in LATER_THAN_D5]:
        v.append("a W8-D6 or W8-D7 entry exists")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted to
    call - the review-law module's among them - is replaced and the previous
    state restored on exit, tolerating a name a later landing has renamed or
    removed."""

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
        ("test_w8_evidence_adequacy_opening", "closed_list_violations",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_opening", "exposure_violations",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_opening", "CRITERIA_LINES", ()),
        ("test_w8_evidence_adequacy_law", "staged_absence_violations",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_law", "finding_snapshot",
         lambda *a, **k: (None, ["sabotaged"])),
        ("test_w8_evidence_adequacy_law", "prose_paragraphs", lambda t: t),
        ("test_w8_evidence_adequacy_law", "INDEX", ()),
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


ALL = ("env", "law", "pkt", "cal", "rec", "cor", "vr", "rev", "auth", "ea",
       "el")


# ------------------------------------------------------------------ proofs
class EF1_Carriage(unittest.TestCase):
    def test_ef1_record_carries_the_human_act_and_the_closed_forms(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ea", "el")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="instruction verbatim, threshold answer, one "
                               "finding form and no other form named, "
                               "criteria, routes, limits, blocks, the "
                               "reading whole, statements once"):
            self.assertEqual(carriage_violations(text, h), [])
        with self.subTest(fact="the fold: emphasis, code, zero-width and "
                               "soft-hyphen marks removed, case and "
                               "spacing folded"):
            self.assertEqual(folded("**Mature\u00a0 Enough**"), "mature enough")
            self.assertEqual(folded("_un\u200bdeter\u00admined_\n"),
                             "undetermined")
            self.assertEqual(folded("`not`\tmature  enough"),
                             "not mature enough")
            self.assertEqual(folded("not determined"), "not determined")
        quote = instruction_quote()
        crit = h.ea.CRITERIA_LINES[1]
        marker1 = READING_PARTS[0][0]
        body1 = block_after(text, marker1, h.ea)
        for name, mutated in (
                ("a word of the instruction changed", text.replace(
                    quote, quote.replace("sufficient", "adequate", 1), 1)),
                ("the instruction quoted twice", text.replace(
                    quote, quote + "\n\n" + quote, 1)),
                ("the finding form changed to another lawful form",
                 text.replace(FINDING_LINE, FINDING_LINE.replace(
                     "undetermined — the published evidence does not settle "
                     "the question.", "**mature enough** — sentinel.", 1), 1)),
                ("the finding line removed", text.replace(
                    FINDING_LINE + "\n", "", 1)),
                ("a second form named in bold before Part D", text.replace(
                    "\n" + PART_D, "\nThe finding is also **not mature "
                    "enough**.\n\n" + PART_D, 1)),
                ("a plain contradictory finding appended after the "
                 "record's end", text + "\nFinding: mature enough.\n"),
                ("a plain duplicate of the adopted form appended",
                 text + "\nFinding: undetermined.\n"),
                ("the finding line carried twice", text.replace(
                    FINDING_LINE + "\n", FINDING_LINE + "\n" + FINDING_LINE
                    + "\n", 1)),
                ("a plain declaration before Part D", text.replace(
                    "\n" + PART_D, "\nThe finding is not mature enough.\n\n"
                    + PART_D, 1)),
                ("a form in upper case", text.replace(
                    "\n" + PART_D, "\nTHE FINDING IS UNDETERMINED.\n\n"
                    + PART_D, 1)),
                ("a form parted by a line break and extra spaces",
                 text.replace("\n" + PART_D, "\nFinding:  mature\n   enough."
                              "\n\n" + PART_D, 1)),
                ("a form in italics", text.replace(
                    "\n" + PART_D, "\nThe finding is _mature enough_.\n\n"
                    + PART_D, 1)),
                ("a form in code marks", text.replace(
                    "\n" + PART_D, "\nFinding: `not mature enough`.\n\n"
                    + PART_D, 1)),
                ("a form parted by a no-break space", text.replace(
                    "\n" + PART_D, "\nFinding: mature\u00a0enough.\n\n"
                    + PART_D, 1)),
                ("a form split by a zero-width space", text.replace(
                    "\n" + PART_D, "\nFinding: undeter\u200bmined.\n\n"
                    + PART_D, 1)),
                ("a logically wrapped declaration", text.replace(
                    "\n" + PART_D, "\nThe finding is not undetermined.\n\n"
                    + PART_D, 1)),
                ("a form declared inside an adopted reading part",
                 text.replace(body1, body1 + "\nFinding: mature enough.", 1)),
                ("the pinned position sentence restated with another form",
                 text.replace(POSITION_SENTENCE, POSITION_SENTENCE.replace(
                     "undetermined", "mature enough"), 1)),
                ("a pinned restatement carried twice, the second in lower "
                 "case", text.replace(
                     COMPLETE_SENTENCE, COMPLETE_SENTENCE + "; "
                     + COMPLETE_SENTENCE[0].lower() + COMPLETE_SENTENCE[1:],
                     1)),
                ("the threshold answer altered in Part B", text.replace(
                    THRESHOLD_LINE, THRESHOLD_LINE.replace("sufficient",
                                                           "adequate"), 1)),
                ("the threshold answer dropped from criterion five",
                 text.replace(CRITERION_FIVE_LINE + "\n\n", "", 1)),
                ("an eighth criterion", text.replace(
                    crit + "\n", crit + "\n    - **coverage** — sentinel;\n",
                    1)),
                ("a criterion differing from the brief's by one word",
                 text.replace(crit, crit.replace("no detection", "no proof"),
                              1)),
                ("two criterion headings swapped", text.replace(
                    CRITERION_HEADINGS[0], "### swap", 1).replace(
                    CRITERION_HEADINGS[1], CRITERION_HEADINGS[0], 1).replace(
                    "### swap", CRITERION_HEADINGS[1], 1)),
                ("a word of the adopted reading changed", text.replace(
                    body1, body1.replace("the", "a", 1), 1)),
                ("a reading part carried twice", text.replace(
                    marker1 + "\n\n" + body1,
                    marker1 + "\n\n" + body1 + "\n\n" + body1, 1)),
                ("a reading part's marker removed", text.replace(
                    marker1 + "\n\n", "", 1)),
                ("an alternative route reworded", text.replace(
                    "by a diagnosis of the recorded divergences",
                    "by diagnosis of the divergences", 1)),
                ("a limit of section 6 dropped", text.replace(
                    "> 29. " + brief_item(29) + "\n", "", 1)),
                ("the express adoption dropped from Part G", text.replace(
                    ADOPTION_LEAD, "14. **Adoption:** \"", 1)),
                ("a removed statement", text.replace(REQUIRED[4], "", 1)),
                ("a readiness sentence", text.replace(
                    "\n" + PART_D, "\nThe instrument is mature.\n\n" + PART_D,
                    1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "ea", "el")
                self.assertEqual(carriage_violations(text, hh), [])


class EF2_Withholding(unittest.TestCase):
    def test_ef2_record_withholds_every_later_act(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ea")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="every withheld phrase carried, Part K whole"):
            self.assertEqual(withholding_violations(text, h.ea), [])
        for s in WITHHELD[:4]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, ""), h.ea))
        pair = NON_AUTH_LINES[3] + "\n" + NON_AUTH_LINES[4] + "\n"
        tail = NON_AUTH_LINES[-1] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this part.\n"
        for name, mutated in (
                ("a dropped non-authorisation", text.replace(
                    NON_AUTH_LINES[9] + "\n", "", 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[4] + "\n" + NON_AUTH_LINES[3] + "\n", 1)),
                ("a thirteenth non-authorisation", text.replace(
                    tail, NON_AUTH_LINES[-1] + "\n    - any sentinel line;\n\n"
                    + NON_AUTH_CLOSE + "\n", 1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n" + neutral + "\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n    This landing "
                              "authorises a contact decision.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a line between the heading and the introducing item",
                 text.replace(NON_AUTH_SECTION + "\n\n" + NON_AUTH_INTRO
                              + "\n", NON_AUTH_SECTION + "\n\n" + neutral
                              + NON_AUTH_INTRO + "\n", 1)),
                ("a line after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a non-breaking-space line as the blank separator",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated, h.ea))


class EF3_NoExposure(unittest.TestCase):
    def test_ef3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, *ALL)
        text = read(RECORD).decode("utf-8")
        for surface, body in (("record", text),
                              ("registry role", NEW_ENTRY["role"]),
                              ("board wording", added_board_wording())):
            with self.subTest(surface=surface):
                self.assertEqual(exposure_violations(body, h), [])
        token = sorted(h.pkt.TOKENS)[0]
        method = sorted(h.law.ADMITS)[0]
        row = succession_row_line(h)
        for name, planted in {
                "case identity": text + "\nW8-C-" + "0" * 64 + "\n",
                "unpinned digest": text + "\nsha256:" + "f" * 64 + "\n",
                "schema literal": text + "\n" + h.pkt.PACKET_SCHEMA + "\n",
                "method label": text + "\n" + method + "\n",
                "count beside a token": text + "\n3 " + token + "\n",
                "count beside a relation": text + "\nagreements: 7\n",
                "percentage": text + "\n50%\n",
                "decimal": text + "\n0.5\n",
                "succession row altered to another digest": text.replace(
                    row, row.replace(POSTIMAGE[LAWMOD][0],
                                     "sha256:" + "f" * 64, 1), 1),
                "score split by a soft line break": text + "\nscore\n5\n",
                "worded score split by a soft line break":
                    text + "\nscore is\n5\n",
                "continuation indentation under a figure word":
                    text + "\nscore\n    5\n",
                "no-break-space line between word and value":
                    text + "\nscore\n \n5\n"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertNotEqual(planted, text)
                self.assertTrue(exposure_violations(planted, h))
        with self.subTest(control="a figure word and a numbered item parted "
                                  "by a blank line stay apart"):
            self.assertEqual(exposure_violations(
                text + "\nthreshold\n\n9. A numbered item.\n", h), [])
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, *ALL)
                self.assertEqual(exposure_violations(text, hh), [])


class EF4_CitationsInsideTheIndex(unittest.TestCase):
    def test_ef4_every_evidential_citation_resolves_to_the_index(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "el")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="cited rows, the reading's table, commits and "
                               "paths all inside the index and the "
                               "governing records"):
            self.assertEqual(citation_violations(text, h), [])
            self.assertEqual(len(h.el.INDEX), 29)
            self.assertEqual(h.el.index_binding_violations(), [])
        rows = [m.group(0) for m in READING_TABLE_ROW.finditer(text)]
        first = rows[0]
        for name, mutated in {
                "a row cited outside the index": text + "\n[Row 30.]\n",
                "a table row's commit altered": text.replace(
                    first, first[:-43] + "0" * 40 + " |", 1),
                "a table row's path altered": text.replace(
                    first, first.replace("docs/", "docs/x/", 1), 1),
                "a table row dropped": text.replace(first + "\n", "", 1),
                "a foreign commit named": text + "\n`" + "a" * 40 + "`\n",
                "a hyperlink": text + "\nht" + "tps://example.invalid/\n",
                "a path outside the index": text
                + "\n`governance/validation-review/other.json`\n"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(citation_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "el")
                self.assertEqual(citation_violations(text, hh), [])


class EF5_FixedArtefactsUnchanged(unittest.TestCase):
    def test_ef5_every_home_record_law_brief_and_module_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "el")
        tracked = snapshot_tracked(commit)
        changed = landing_paths(commit)
        base_tracked, fixed = fixed_paths()
        homes = h.el.FIXED_HOMES
        with self.subTest(fact="every baseline path other than the three "
                               "modified census paths is unchanged, nothing "
                               "is missing, no fixed home gains a file"):
            self.assertEqual(fixed_artefact_violations(
                changed, tracked, fixed, base_tracked, homes), [])
            for rel in (LAW, BRIEF, OPENING, RECOVERY):
                self.assertIn(rel, fixed)
                self.assertEqual(_blob(read(rel)),
                                 _git("rev-parse", BASELINE + ":" + rel)
                                 .strip())
        reveal_file = next(p for p in base_tracked
                           if p.startswith("governance/validation-reveal/"))
        for name, (c, t) in {
                "a changed revealed record": (changed | {reveal_file},
                                              tracked),
                "a changed review law": (changed | {LAW}, tracked),
                "a changed opening module": (changed | {OPENING}, tracked),
                "a removed baseline path": (
                    changed, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    changed, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    c, t, fixed, base_tracked, homes))


class EF6_EL7Succession(unittest.TestCase):
    def test_ef6_el7_succession_is_exact_and_the_absences_stay_proven(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "el")
        record = read(RECORD).decode("utf-8")
        present = read(LAWMOD).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[LAWMOD][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + LAWMOD)
                             .strip(), PREIMAGE[LAWMOD][2])
        with self.subTest(exact_succession="review-law module"):
            self.assertEqual(succession_violations(present, record, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[LAWMOD][1])
        at_law = json.loads(committed(BASELINE, REGISTRY))["entries"]
        law_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
        with self.subTest(fact="the succeeded module keeps every former "
                               "absence proven at the law's landing and "
                               "proves exactly this landing's three admitted "
                               "at the one snapshot both modules identify"):
            self.assertEqual(h.el.D5_ENTRIES_AT_FINDING, D5_ENTRIES)
            self.assertEqual(h.el.staged_absence_violations(
                law_tracked, lambda p: False, at_law), [])
            now = json.loads(read(REGISTRY))["entries"]
            tracked = snapshot_tracked(commit)
            self.assertEqual(h.el.staged_absence_violations(
                tracked, lambda p: p in tracked, now, landed=True), [])
            self.assertEqual(h.el.finding_snapshot(BASELINE), (commit, []))
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[LAWMOD][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[LAWMOD] + (("EL7", first, first + "# planted\n"),)),
                "a site labelled for another proof": (
                    present, SITES[LAWMOD][:2] + (("EL6",)
                                                  + SITES[LAWMOD][2][1:],)
                    + SITES[LAWMOD][3:])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(text, record, h, table))
        row = succession_row_line(h)
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "an unknown source row": record.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a duplicate authorised row": record.replace(
                    row + "\n", row + "\n" + row + "\n", 1),
                "an extra field": record.replace(row, row + " extra |", 1),
                "a non-blank line under the table": record.replace(
                    row + "\n", row + "\nA stray line.\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, record)
                self.assertTrue(succession_table_violations(mutant, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "el")
                self.assertEqual(succession_violations(present, record, hh),
                                 [])


class EF7_RegistryAndBoard(unittest.TestCase):
    def test_ef7_registered_and_changed_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        record = read(RECORD).decode("utf-8")
        state, date, v = record_state(record, h)
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
                               "once", state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED_AFTER), 1)
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        at_snapshot = json.loads(reg)["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, record, h), [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        base = at_snapshot[-1]
        for name, entries in {
                "a fourth W8-D5 entry": at_snapshot + [dict(
                    base, id="W8-D5-SNT", deliverable="W8-D5")],
                "a W8-D6 entry": at_snapshot + [dict(
                    base, id="W8-D6-SNT", deliverable="W8-D6")],
                "a wrong record hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                        if e["id"] == "W8-D5-AFR" else e
                                        for e in at_snapshot],
                "a wrong type": [dict(e, type="adr")
                                 if e["id"] == "W8-D5-AFR" else e
                                 for e in at_snapshot],
                "the law's entry removed": [e for e in at_snapshot
                                            if e["id"] != "ADR-0061"]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, record, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))
                self.assertEqual(entry_violations(at_snapshot, record, hh), [])


class EF8_Census(unittest.TestCase):
    def test_ef8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the review-law module "
                               "change among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, LAWMOD})
        flat = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(re.escape(CENSUS_LEAD) + r"(.*?) 32\. ", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RUNWAY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


class EF9_CompletionWithoutALiveGate(unittest.TestCase):
    def test_ef9_completion_recorded_once_and_no_present_state_gate(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="completion stated once, opening nothing"):
            self.assertEqual(text.count(COMPLETION), 1)
            self.assertEqual(text.count("Completion opens nothing."), 1)
            self.assertIn("W8-D6 and W8-D7 remain closed behind their own "
                          "briefs", text)
        tracked = snapshot_tracked(commit)
        entries = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="at this landing's snapshot, nothing of W8-D6 "
                               "or W8-D7 exists"):
            self.assertEqual([e["id"] for e in entries
                              if e["deliverable"] in LATER_THAN_D5], [])
            self.assertEqual([p for p in tracked if Path(p).name.startswith(
                ("W8-D6", "W8-D7"))], [])
        src = read(SELF_REL).decode("utf-8")
        # The two live-read idioms, assembled so that this proof's own
        # source does not carry them as literals.
        live_reads = ("(ROOT / " + "REGISTRY).read_" + "bytes()",
                      '"ls-' + 'files"')
        with self.subTest(fact="this module holds no present-state gate of "
                               "its own: no live registry or working-tree "
                               "read outside the snapshot helpers"):
            body = src.split("# ------------------------------------------------------------------ proofs", 1)[1]
            for idiom in live_reads:
                self.assertNotIn(idiom, body)
        el7_of = lambda src: src.split("class EL7_StagedAbsences", 1)[1].split(
            "\nclass ", 1)[0]
        with self.subTest(fact="the succeeded EL7 holds no present-state gate: "
                               "neither live-read idiom in its proof"):
            for idiom in live_reads:
                self.assertNotIn(idiom, el7_of(read(LAWMOD).decode("utf-8")))
        with self.subTest(control="the pre-image's EL7 carried a present-state "
                                  "read, and is refused"):
            self.assertTrue(any(idiom in el7_of(baseline_text(LAWMOD))
                                for idiom in live_reads))
        for name, mutated in {
                "completion stated twice": text.replace(
                    COMPLETION, COMPLETION + " " + COMPLETION, 1),
                "completion dropped": text.replace(COMPLETION, "", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated.count(COMPLETION), 1)
        with self.subTest(control="a W8-D6 entry at the snapshot is refused"):
            planted = entries + [dict(entries[-1], id="W8-D6-SNT",
                                      deliverable="W8-D6")]
            self.assertTrue([e["id"] for e in planted
                             if e["deliverable"] in LATER_THAN_D5])


if __name__ == "__main__":
    unittest.main()
