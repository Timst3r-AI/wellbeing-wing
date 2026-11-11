"""W9 runway — phase-entry proofs (W9-AR, AR1–AR5).

The landing of the W9 phase runway, gate document two of the standing
three-document entry gate, over the effective W8 closure commit. This module
proves mechanics and carriage only: that the runway at its landing is
byte-for-byte the reviewed text, in its draft or its accepted status form
(AR1); that the one proof succession this landing makes - CC7 of the W8
closure record's module - is the exact reviewed transformation of a fixed
pre-image, reversible, leaving in the succeeded module no executable
expression of the withdrawn live registry read, with the succeeded claim
holding at the W8 closure commit (AR2); that the registry and the board change exactly, by one appended entry
and one appended section (AR3); the one present-state gate this landing
leaves (AR4); and the census (AR5) - each with planted-mutant or negative
controls. Closed validators compare against trusted expected values held
here and refuse unrecognised material rather than skip it.

Every proof but one limb reads this landing's fixed snapshot - the candidate
over the baseline before the commit exists, the one commit that added the
runway afterwards - so that no later lawful landing moves it. AR4's
present-state limb is the exception, and it is this module's only executable
live registry read: every registry entry's phase is one of W0 to W9. It
succeeds CC7's no-later-phase limb at this landing and stands until a later
accepted act lawfully succeeds it. It refuses an entry of any later phase,
it does not refuse an entry of W9, and it decides nothing else about any
entry. CC7's W8-D7 entry-set limb is left historical, with no present-state
successor. The residual live reach is disclosed exactly: the code that runs
is this file as the working tree holds it; it reads history through the
local repository; and before the landing commit exists it reads the
candidate from the working tree. It imports no other test module.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity, schema
literal, method label or disposition token.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that the runway is accepted, or that W9 is open; any
application boundary, release scope or release criterion; that any human
review duty was performed - P2, Q3 and P4b remain human acts;
anything about any model, case, disposition or divergence; that any model
was or was not contacted; that any ADR-0047 precondition moved; that any W8
standing changed; or that any later phase may open.
"""
import ast
import datetime
import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The effective W8 closure commit: this landing's baseline, and the commit at
# which the succeeded CC7 claim stays proven.
BASELINE = "c6de8a99f09d60164def9f330f72437b2812c370"

RUNWAY = "docs/phases/W9-runway-application-release-scope-and-contract.md"
SELF_REL = "tests/test_w9_runway.py"
CLOSURE = "tests/test_w8_closure_record.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
FIXED_CENSUS = frozenset({RUNWAY, SELF_REL, CLOSURE, REGISTRY, BOARD})
NEW_PATHS = frozenset({RUNWAY, SELF_REL})
# The phases an entry may carry: AR4's whole rule.
KNOWN_PHASES = frozenset("W%d" % n for n in range(10))
# The phases that existed at the baseline, and the W8-D7 entry set CC7 held.
EARLIER_PHASES = frozenset("W%d" % n for n in range(9))
D7_ENTRIES = frozenset({"W8-D7-CAB", "W8-D7-CAR", "W8-CR"})

# Fixed pre-images at the baseline: (LF SHA-256, blob).
PREIMAGE = {
    CLOSURE: ("sha256:df13a66df9ee2f8f42e07092cfebf471211ce9901223feda0247d7e1a92c7c22",
              "a7558ca6c742c5605d8860ae8c8e898d19d5d4f7"),
    REGISTRY: ("sha256:8ea1b1f2082726ca24d546112777dec36767c9b33bb230bc34791545e8136c3e",
               "183cf91c6dc3372db39db51286ddc24440cad6d8"),
    BOARD: ("sha256:d2db3dc091c3d1ddff5e9a8d45bf0f2d9b2f7a082a14585d723c3e25ca7c68ab",
            "3e8cb6f0c74c459cf2f6d98e5360c2f5675b46fd"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {
    CLOSURE: ("sha256:ba81ab6a84fee2dee8b96b2ce8559e9184f33518c1cbd6bf5a397ec33d3ab135",
              "dd2112aed9176218c2ef42e334fa8823418c2a56"),
}
# The reviewed runway in its draft status form: LF SHA-256. The accepted form
# differs from it in the one status line and in nothing else.
RUNWAY_DRAFT = "sha256:0f982c2718d6885a8267d6c37a00b75e35ed084dd187b69aca67d4b1dc24e429"

# ------------------------------------------------ the runway's status line
STATUS_INDEX = 4
STATUS_DRAFT = ("**Status:** Draft for human review. Not accepted. Not a build "
                "instruction.")
STATUS_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. Not a build "
                   "instruction.")
ACCEPTED_LINE = re.compile(r"\*\*Status:\*\* Accepted by human reviewer, "
                           r"(\d{4}-\d{2}-\d{2})\. Not a build instruction\.")

# ----------------------- the one succession: the closure record module's CC7
SITES = (
    ("CC7",
     "bytes, in a private namespace. CC7's W8-D7 entry set and its no-later-phase\n"
     "limb are this module's present-state gates, moved here from the assessment\n"
     "module's CB7 at this landing, until a later accepted act lawfully succeeds\n"
     "them. The residual live reach is disclosed exactly: each snapshot-executed\n",
     "bytes, in a private namespace. CC7's W8-D7 entry set and its no-later-phase\n"
     "limb were this module's present-state gates, moved here from the assessment\n"
     "module's CB7 at this landing, until the W9 runway's landing (W9-AR)\n"
     "succeeded them to a historical proof at this landing's own published\n"
     "commit. The residual live reach is disclosed exactly: each snapshot-executed\n"),
    ("CC7",
     "BASELINE = \"6ee0127e91f755d39b7fdc5af08bb1bcf1b16437\"\n"
     "D7B_LANDING = \"6ee0127e91f755d39b7fdc5af08bb1bcf1b16437\"\n",
     "BASELINE = \"6ee0127e91f755d39b7fdc5af08bb1bcf1b16437\"\n"
     "# Succeeded at the W9 runway's landing (W9-AR; W8-CR section 12, item 35,\n"
     "# and section 14, items 40 and 41): CC7's W8-D7 entry set and its\n"
     "# no-later-phase limb stay proven at this landing's own published commit;\n"
     "# this module holds no executable live registry read.\n"
     "D7C_LANDING = \"c6de8a99f09d60164def9f330f72437b2812c370\"\n"
     "D7B_LANDING = \"6ee0127e91f755d39b7fdc5af08bb1bcf1b16437\"\n"),
    ("CC7",
     "        # The present-state gates of this module, moved here from the\n"
     "        # assessment module's CB7 at this landing, until a later accepted act\n"
     "        # lawfully succeeds them under the gate pattern this record carries.\n"
     "        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))[\"entries\"]\n"
     "        with self.subTest(fact=\"the W8-D7 entries are the brief's, the \"\n"
     "                               \"assessment's and this record's, and no later \"\n"
     "                               \"phase's entry exists\"):\n"
     "            self.assertEqual(entry_violations(live, record, h), [])\n",
     "        # Succeeded at the W9 runway's landing (W9-AR): the W8-D7 entry set\n"
     "        # and the no-later-phase limb stay proven at this landing's own\n"
     "        # published commit, D7C_LANDING.\n"
     "        at_landing = json.loads(committed(D7C_LANDING, REGISTRY))[\"entries\"]\n"
     "        with self.subTest(fact=\"the W8-D7 entries were the brief's, the \"\n"
     "                               \"assessment's and this record's, and no later \"\n"
     "                               \"phase's entry existed, at this landing's \"\n"
     "                               \"published commit\"):\n"
     "            self.assertEqual(commit, D7C_LANDING)\n"
     "            self.assertEqual(entry_violations(at_landing, record, h), [])\n"),
)
D7C_LINE = 'D7C_LANDING = "%s"\n' % BASELINE
HISTORICAL_READ = 'json.loads(committed(D7C_LANDING, REGISTRY))["entries"]'
LIVE_READ_LINE = ('        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))'
                  '["entries"]\n')

# --------------------------------------------- the one registry entry, W9-AR
TITLE = "W9 - Application Release Scope and Contract (Phase Runway)"
DEPENDS_ON = (
    "W0", "W1-D1", "W1-D2", "W2-D3", "ADR-0003", "ADR-0004", "ADR-0006",
    "ADR-0008", "ADR-0010", "ADR-0043", "ADR-0046", "ADR-0047", "ADR-0051",
    "W4-D2", "W4-D3", "W4-D4", "W4-D5", "W8-CR",
)
ROLE = (
    "The W9 phase runway and gate document two of the standing "
    "three-document entry gate, authorising W9 briefs only and never "
    "implementation, a directory or dependency crossing, model contact "
    "or a release, effective on publication and remote verification. "
    "W9 is the scope-and-contract phase for a public reference "
    "release: it settles, on paper and from source, what such a "
    "release would be, what authority each capability needs and what "
    "evidence each claim would require. Seven deliverables behind "
    "their own briefs - application boundary doctrine, capability and "
    "authority baseline, release scope, workflow scope, integration "
    "posture, release contract, and closure. The W7 public/private "
    "boundary and synthetic-only law are inherited whole; the W8-D5 "
    "finding stays undetermined and the W8-D6 decision authorises "
    "nothing; ADR-0047 precondition 3 remains outstanding in its "
    "lawful resting state; the W8-CR section 9 inventory is inherited "
    "whole, each row at its published standing, the completed closure "
    "programme distinguished from the matters carried forward, and "
    "none of it reopened, solved or reclassified by this runway; the "
    "proposed release criteria and the proposed later labels are "
    "drafts accepted by nothing here; and nothing is built and no "
    "model is contacted by anything this runway authorises."
)

# ------------------------------------------- the one appended board section
BOARD_HEAD = (
    "\n"
    "## W9 — Application Release Scope and Contract\n"
    "\n"
    "**Scope:** The phase that decides, before any application code "
    "exists, what a supported public reference release of the Wing "
    "would be, what authority each part of it needs, and what evidence "
    "each of its claims would require. **W9 is a scope-and-contract "
    "phase, not an implementation phase:** every W9 deliverable is a "
    "governed document, and no directory, dependency, interface, model "
    "contact or release belongs to it.\n"
    "\n"
    "**Runway:** "
    "[`W9-runway-application-release-scope-and-contract.md`](W9-runway-application-release-scope-and-contract.md)\n"
    "\n"
)
BOARD_STATUS = {
    "draft": (
        "**Status:** **A draft W9 runway, `W9-AR`, is before the human "
        "reviewer — not accepted, and opening nothing.** The W8 closure "
        "record is gate document one. This runway would become gate "
        "document two only on its acceptance, publication and remote "
        "verification, authorising W9 briefs only. **Gate document three — "
        "the first W9 deliverable brief — does not exist, the entry gate "
        "is not complete, and W9-D1 is not open.** "
    ),
    "accepted": (
        "**Status:** **The W9 entry gate is two documents complete of "
        "three:** the W8 closure record is gate document one, and this "
        "runway — accepted {DATE} — is gate document two, **effective on "
        "publication and remote verification, authorising W9 briefs only** "
        "— never implementation, never a directory or dependency crossing, "
        "never model contact, never a release. **Gate document three — the "
        "first W9 deliverable brief — does not exist, the entry gate is "
        "not yet complete, and W9-D1 is not open.** "
    ),
}
BOARD_TAIL = (
    "No application exists and no release contract is accepted; no "
    "directory, dependency, credential, provider or transport was "
    "introduced; the W8-D5 finding stays undetermined and the W8-D6 "
    "decision authorises nothing; ADR-0047 precondition 3 remains "
    "outstanding in its lawful resting state; and the whole inventory "
    "of `W8-CR` §9 stands exactly as that record carries it, each row "
    "at its published standing — row thirty the completed closure "
    "programme, rows one to twenty-nine the matters carried forward — "
    "with none of it reopened, solved or reclassified by this phase's "
    "existence. Any real-person adoption is "
    "a separate governed authority outside this repository. Every W9 "
    "deliverable opens only through its own accepted brief, and any "
    "later phase opens only through its own runway and gate.\n"
)
CENSUS_SENTENCE = re.compile(r"\*\*This landing's census is exactly five "
                             r"paths:\*\* (.*?)\. A green run")


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


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def existed(commit, rel):
    return subprocess.run(["git", "cat-file", "-e", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True).returncode == 0


def landing_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the runway, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", RUNWAY).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the runway was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot():
    commit, problems = landing_snapshot()

    def read(rel):
        return (_lf((ROOT / rel).read_bytes()) if commit is None
                else committed(commit, rel))
    return commit, problems, read


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def apply_sites(text, sites):
    v = []
    for label, old, new in sites:
        n = text.count(old)
        if n != 1:
            v.append("%s: pre-image site occurs %d times" % (label, n))
            continue
        text = text.replace(old, new)
    return text, v


def reverse_sites(text, sites):
    v = []
    for label, old, new in reversed(sites):
        n = text.count(new)
        if n != 1:
            v.append("%s: post-image site occurs %d times" % (label, n))
            continue
        text = text.replace(new, old)
    return text, v


def live_registry_reads(source):
    """How many executable expressions of the withdrawn idiom - the working
    tree's registry read as `(ROOT / REGISTRY).read_bytes()` - a module's
    source holds. A bounded count of one idiom, read from the syntax tree so
    that a string literal quoting it is not counted; never a claim that the
    source reads no other working-tree byte."""
    n = 0
    for node in ast.walk(ast.parse(source)):
        if not (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "read_bytes"):
            continue
        base = node.func.value
        if (isinstance(base, ast.BinOp) and isinstance(base.op, ast.Div)
                and isinstance(base.left, ast.Name) and base.left.id == "ROOT"
                and isinstance(base.right, ast.Name)
                and base.right.id == "REGISTRY"):
            n += 1
    return n


# -------------------------------------------------------------- validators
def runway_state(text):
    """AR1: (state, date, violations). The runway is the reviewed text with
    its one status line in the draft form, or in the accepted form carrying
    a real calendar date."""
    lines = text.split("\n")
    marks = [i for i, line in enumerate(lines) if line.startswith("**Status:**")]
    if marks != [STATUS_INDEX]:
        return None, None, ["the status line is not the fifth line alone"]
    v, state, date = [], None, None
    line = lines[STATUS_INDEX]
    if line == STATUS_DRAFT:
        state = "draft"
    else:
        m = ACCEPTED_LINE.fullmatch(line)
        if m is None:
            v.append("the status line is neither the draft nor the accepted "
                     "form")
        else:
            try:
                datetime.date.fromisoformat(m.group(1))
                state, date = "accepted", m.group(1)
            except ValueError:
                v.append("the acceptance date is not a calendar date")
    lines[STATUS_INDEX] = STATUS_DRAFT
    if _sha("\n".join(lines).encode("utf-8")) != RUNWAY_DRAFT:
        v.append("outside its status line the runway is not the reviewed text")
    return state, date, v


def succession_violations(present, sites=None):
    """AR2's first limb: the CC7 succession is the exact reviewed
    transformation of the closure module's fixed pre-image, reversible, its
    sites CC7's alone, the pinned anchor this landing's baseline, the
    succeeded module holding no executable live registry read."""
    sites = SITES if sites is None else sites
    v = []
    pre = baseline_text(CLOSURE)
    if _sha(pre.encode("utf-8")) != PREIMAGE[CLOSURE][0]:
        v.append("the baseline pre-image differs from its pin")
    expected, problems = apply_sites(pre, sites)
    v += problems
    if expected != present:
        v.append("the bytes are not the exact authorised post-image")
    for label, _, new in sites:
        if present.count(new) != 1:
            v.append("%s: post-image site occurs %d times"
                     % (label, present.count(new)))
    restored, problems = reverse_sites(present, sites)
    v += problems
    if restored != pre:
        v.append("reversing the table does not restore the pre-image")
    if _sha(present.encode("utf-8")) != POSTIMAGE[CLOSURE][0]:
        v.append("the bytes are not the reviewed post-image")
    if tuple(dict.fromkeys(label for label, _, _ in sites)) != ("CC7",):
        v.append("the sites are not CC7's alone")
    if present.count(D7C_LINE) != 1:
        v.append("the succession's anchor is not this landing's baseline")
    if present.count(HISTORICAL_READ) != 1 or LIVE_READ_LINE in present:
        v.append("the succeeded CC7 does not read the W8 closure commit alone")
    if pre.count(LIVE_READ_LINE) != 1 or HISTORICAL_READ in pre:
        v.append("the pre-image is not the live-gated module")
    try:
        reads = (live_registry_reads(pre), live_registry_reads(present))
    except SyntaxError:
        reads = None
    if reads != (1, 0):
        v.append("the one executable live registry read is not exactly what "
                 "this succession withdraws")
    return v


def closure_claim_violations(entries):
    """AR2's second limb: the claim CC7 held as a present-state gate until
    this landing, read as a fact about one committed registry."""
    v = []
    if {e["id"] for e in entries if e["deliverable"] == "W8-D7"} != D7_ENTRIES:
        v.append("the W8-D7 entries are not exactly the brief's, the "
                 "assessment's and the closure record's")
    if phase_violations(entries, EARLIER_PHASES):
        v.append("an entry of a phase later than W8 exists")
    return v


def new_entry(state, date, runway_hash):
    return {"id": "W9-AR", "aliases": [], "title": TITLE,
            "type": "phase-record", "phase": "W9", "deliverable": None,
            "path": RUNWAY, "status": state, "accepted_date": date,
            "role": ROLE, "governs": [], "depends_on": list(DEPENDS_ON),
            "resolves": [], "id_namespaces": [],
            "implementation_permission": "none", "open_decisions": [],
            "content_hash": runway_hash, "hash_exclusion_reason": None,
            "errata": []}


def expected_registry(base_text, state, date, runway_hash):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, runway_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def board_section(state, date):
    status = BOARD_STATUS[state]
    if state == "accepted":
        status = status.replace("{DATE}", date)
    return BOARD_HEAD + status + BOARD_TAIL


def registry_violations(reg, state, date, runway_hash):
    """AR3: the registry is the baseline text with exactly this runway's one
    entry appended, in the state and with the date the runway's own status
    line carries, bound to the runway's bytes."""
    v = []
    base = baseline_text(REGISTRY)
    if _sha(base.encode("utf-8")) != PREIMAGE[REGISTRY][0]:
        v.append("the baseline registry differs from its pin")
    if state not in BOARD_STATUS:
        return v + ["the runway carries no recognised state"]
    if reg != expected_registry(base, state, date, runway_hash):
        v.append("the registry is not the baseline text with exactly this "
                 "runway's one entry appended")
    return v


def board_violations(board, state, date):
    """AR3: the board is the baseline text with exactly this runway's one
    section appended, in the state the runway's own status line carries."""
    v = []
    base = baseline_text(BOARD)
    if _sha(base.encode("utf-8")) != PREIMAGE[BOARD][0]:
        v.append("the baseline board differs from its pin")
    if state not in BOARD_STATUS:
        return v + ["the runway carries no recognised state"]
    if board != base + board_section(state, date):
        v.append("the board is not the baseline text with exactly this "
                 "runway's one section appended")
    return v


def phase_violations(entries, known=KNOWN_PHASES):
    """AR4's whole rule: every entry's phase is one of the known phases - by
    default W0 to W9. It reads the phase field and nothing else."""
    stray = sorted({"%s (%r)" % (e.get("id"), e.get("phase"))
                    for e in entries
                    if not isinstance(e.get("phase"), str)
                    or e.get("phase") not in known})
    return (["an entry of a later phase, or of no known phase, exists: "
             + ", ".join(stray)] if stray else [])


# ------------------------------------------------------------------ proofs
class AR1_Runway(unittest.TestCase):
    def test_ar1_runway_is_the_reviewed_text_in_one_status_form(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RUNWAY).decode("utf-8")
        state, date, v = runway_state(text)
        with self.subTest(fact="the runway is the reviewed text in its draft "
                               "or its accepted status form", state=state):
            self.assertEqual(v, [])
            self.assertIn(state, ("draft", "accepted"))
            self.assertEqual(date is None, state == "draft")
        line = text.split("\n")[STATUS_INDEX]
        other = (STATUS_ACCEPTED % "2000-01-01" if state == "draft"
                 else STATUS_DRAFT)
        with self.subTest(control="the other status form is read as the other "
                                  "state, over the same reviewed text"):
            got = runway_state(text.replace(line, other, 1))
            self.assertEqual(got[2], [])
            self.assertNotEqual(got[0], state)
            self.assertIn(got[0], ("draft", "accepted"))
        for name, mutated in {
                "a byte changed outside the status line": text + " ",
                "a field label removed outside the status line":
                    text.replace("\n**Date:** ", "\n", 1),
                "an impossible acceptance date": text.replace(
                    line, STATUS_ACCEPTED % "2026-02-30", 1),
                "an acceptance date in another notation": text.replace(
                    line, STATUS_ACCEPTED % "1 January 2000", 1),
                "a status line of neither form": text.replace(
                    line, "**Status:** Accepted.", 1),
                "a second status line": text.replace(
                    line + "\n", line + "\n" + line + "\n", 1),
                "the status line moved": text.replace(
                    line + "\n", "\n" + line + "\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(runway_state(mutated)[2])


class AR2_Succession(unittest.TestCase):
    def test_ar2_cc7_succession_exact_and_the_succeeded_claim_holds(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        present = read(CLOSURE).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[CLOSURE][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + CLOSURE)
                             .strip(), PREIMAGE[CLOSURE][1])
        with self.subTest(exact_succession=POSTIMAGE[CLOSURE][0]):
            self.assertEqual(succession_violations(present), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[CLOSURE][1])
        at_closure = json.loads(committed(BASELINE, REGISTRY))["entries"]
        with self.subTest(fact="the W8-D7 entries were the brief's, the "
                               "assessment's and the closure record's, and "
                               "no later phase's entry existed, at the W8 "
                               "closure commit"):
            self.assertEqual(closure_claim_violations(at_closure), [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[1:]),
                "the live read restored beside the historical one": (
                    present.replace(SITES[2][2],
                                    SITES[2][2] + LIVE_READ_LINE, 1), None),
                "the anchor moved off the W8 closure commit": (
                    present.replace(D7C_LINE, 'D7C_LANDING = "%s"\n'
                                    % ("0" * 40), 1), None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES + (("CC7", first, first + "# planted\n"),)),
                "a site of another label": (
                    present, (("CC8",) + SITES[0][1:],) + SITES[1:])}.items():
            with self.subTest(control="%s is refused" % name):
                if table is None:
                    self.assertNotEqual(text, present)
                self.assertTrue(succession_violations(text, table))
        model = at_closure[-1]
        for name, entries in {
                "a fourth W8-D7 entry": at_closure + [dict(
                    model, id="W8-D7-SNT", deliverable="W8-D7")],
                "a missing W8-D7 entry": [e for e in at_closure
                                          if e["id"] != "W8-D7-CAB"],
                "a later phase's entry": at_closure + [dict(
                    model, id="W9-SNT", phase="W9",
                    deliverable=None)]}.items():
            with self.subTest(claim_control="%s is refused" % name):
                self.assertTrue(closure_claim_violations(entries))


class AR3_RegistryAndBoard(unittest.TestCase):
    def test_ar3_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        # The state and date are read from the runway's status line; whether
        # the runway is the reviewed text is AR1's verdict and is not
        # repeated here.
        state, date, _ = runway_state(read(RUNWAY).decode("utf-8"))
        self.assertIn(state, ("draft", "accepted"))
        runway_hash = _sha(read(RUNWAY))
        for rel in (REGISTRY, BOARD):
            with self.subTest(pre_image=rel):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(), PREIMAGE[rel][1])
        reg = read(REGISTRY).decode("utf-8")
        board = read(BOARD).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(
                registry_violations(reg, state, date, runway_hash), [])
        base_entries = json.loads(baseline_text(REGISTRY))["entries"]
        entries = json.loads(reg)["entries"]
        with self.subTest(fact="every baseline entry is unchanged and in "
                               "place, and the one new entry binds the "
                               "runway's path, state, date and bytes and "
                               "depends only on entries registered at the "
                               "baseline"):
            self.assertEqual(entries[:-1], base_entries)
            self.assertEqual(entries[-1],
                             new_entry(state, date, runway_hash))
            self.assertEqual([e["id"] for e in entries].count("W9-AR"), 1)
            self.assertLessEqual(set(DEPENDS_ON),
                                 {e["id"] for e in base_entries})
        with self.subTest(fact="exact authorised board", state=state):
            self.assertEqual(board_violations(board, state, date), [])
        other = "accepted" if state == "draft" else "draft"
        other_date = "2000-01-01" if other == "accepted" else None
        section = board_section(state, date)
        end = "\n  ]\n}\n"
        for name, mutated in {
                "the other acceptance form": expected_registry(
                    baseline_text(REGISTRY), other, other_date, runway_hash),
                "a hash that is not the runway's": expected_registry(
                    baseline_text(REGISTRY), state, date,
                    "sha256:" + "0" * 64),
                "an earlier entry altered": reg.replace(
                    '"id": "W8-CR"', '"id": "W8-CR-SNT"', 1),
                "a second new entry": reg[:-len(end)] + ",\n" + _indent(
                    json.dumps(dict(new_entry(state, date, runway_hash),
                                    id="W9-AR-SNT"), indent=2,
                               ensure_ascii=False), 4) + end,
                "an extra byte": reg + " "}.items():
            with self.subTest(registry_control="%s is refused" % name):
                self.assertNotEqual(mutated, reg)
                self.assertTrue(registry_violations(
                    mutated, state, date, runway_hash))
        for name, mutated in {
                "the other acceptance form": baseline_text(BOARD)
                + board_section(other, other_date),
                "the section appended twice": board + section,
                "an earlier section altered": board.replace(
                    "\n## W8 ", "\n## W8  ", 1),
                "the section's closing sentence removed": board.replace(
                    BOARD_TAIL, "", 1),
                "an extra byte": board + " "}.items():
            with self.subTest(board_control="%s is refused" % name):
                self.assertNotEqual(mutated, board)
                self.assertTrue(board_violations(mutated, state, date))


class AR4_PhaseGate(unittest.TestCase):
    def test_ar4_no_registry_entry_of_a_phase_later_than_w9(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="at this landing's snapshot every entry's "
                               "phase is one of W0 to W9, and the one W9 "
                               "entry is the runway's"):
            self.assertEqual(phase_violations(at_snapshot), [])
            self.assertEqual([e["id"] for e in at_snapshot
                              if e["phase"] == "W9"], ["W9-AR"])
        with self.subTest(fact="at the baseline no W9 entry existed"):
            self.assertEqual(phase_violations(json.loads(committed(
                BASELINE, REGISTRY))["entries"], EARLIER_PHASES), [])
        # The present-state gate of this module, succeeding CC7's
        # no-later-phase limb at this landing, until a later accepted act
        # lawfully succeeds it under the three-document pattern.
        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]
        with self.subTest(fact="no registry entry of a phase later than W9 "
                               "exists"):
            self.assertEqual(phase_violations(live), [])
        with self.subTest(fact="this gate's read is this module's one "
                               "executable live registry read"):
            self.assertEqual(live_registry_reads(
                _lf(SELF.read_bytes()).decode("utf-8")), 1)
        model = at_snapshot[-1]
        with self.subTest(control="a further W9 entry is not refused"):
            self.assertEqual(phase_violations(at_snapshot + [dict(
                model, id="W9-D1-SNT", type="phase-brief",
                deliverable="W9-D1")]), [])
        for name, phase in {"a W10 entry": "W10", "a W14 entry": "W14",
                            "a phase of another form": "w10",
                            "a padded W9": "W9 ", "no phase": None,
                            "a phase that is not text": 10}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(phase_violations(at_snapshot + [dict(
                    model, id="W10-SNT", phase=phase)]))


class AR5_Census(unittest.TestCase):
    def test_ar5_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the closure record's "
                               "module change among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, CLOSURE})
        with self.subTest(fact="the runway and this module are new, and the "
                               "other three paths existed at the baseline"):
            self.assertEqual({p for p in FIXED_CENSUS
                              if not existed(BASELINE, p)}, set(NEW_PATHS))
        flat = _flat(read(RUNWAY).decode("utf-8"))
        with self.subTest(fact="the runway names the fixed census"):
            m = CENSUS_SENTENCE.search(flat)
            self.assertIsNotNone(m)
            self.assertEqual(sorted(re.findall(r"`([^`]+)`", m.group(1))),
                             sorted(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {"README.md"},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
