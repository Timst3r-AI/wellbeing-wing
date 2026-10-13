"""W8-D4-A — instrument-validation opening brief proofs (W8-D4-IVB, VB1–VB8).

The opening landing of W8-D4: the brief that fixes the validation
programme, its six methods, the evidence limits and human decision points
of divergence diagnosis, and its stop conditions; and the one proof
succession the placeholder probe found a W8-D4 opening to need - ADR-0058's
R9 later-deliverable limb. This module proves the brief's carriage, its
closed outcome list and its non-authorisations; its exposure limits, with
the one trusted succession row as the only digest exemption; that this
landing leaves the W8-D3 register and records, the revealed records and the
supplementary manifest byte-unchanged; the exact R9 succession and its
closed succession table; and the exact registry, board and census - each
with planted-mutant or negative controls. Closed validators compare against
trusted expected values held here, never against values read from the text
being checked, and refuse unrecognised material rather than skip it. Every
proof reads this landing's snapshot except one: the W8-D4 entry set of VB7,
a present-state gate succeeded at each later W8-D4 landing that adds an
entry.

THIS MODULE READS NO CUSTODY. It holds no case identity, schema literal or
count as a literal, authors no case and performs no validation.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any validation method is adequate or that the
instrument is valid, mature or ready; anything about any case, disposition,
divergence or reviewer; that any diagnosis is right; that any model was
contacted; or that W8-D5 through W8-D7 may open.
"""

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

import test_w8_calibration_law as calibration
import test_w8_discriminating_instrument_corpus as corpus
import test_w8_discriminating_instrument_envelope as envelope
import test_w8_recovery_authority as authority
import test_w8_session_recovery_law as recovery
import test_w8_supplementary_corpus as supplement
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified W8-D3 completion: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"
CORPUS = "83253039ec274a2496b37b618949fd00d3cd7c8e"

BRIEF = "docs/phases/W8-D4-instrument-validation-brief.md"
SELF_REL = "tests/test_w8_validation_opening.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
FIXED_CENSUS = frozenset({BRIEF, SELF_REL, RECOVERY, REGISTRY, BOARD})
D4_ENTRIES = {"W8-D4-IVB"}
LATER_THAN_D4 = ("W8-D5", "W8-D6", "W8-D7")

# Published artefacts this landing must leave byte-unchanged (LF SHA-256).
FIXED = {
    "governance/discriminating-review/W8-D3-disposition-register.json":
        "sha256:3a1846c02434739c641c58f6428f6b7da4bab2e6a3b24e6b8bff4b4337df2b5a",
    "docs/phases/W8-D3-human-disposition-record.md":
        "sha256:f438b825e18b6a0e625bfd8079b02d1350594f46e65aa307f4bddb12f2fddd3e",
    "docs/phases/W8-D3-calibration-completion-record.md":
        "sha256:b6e958ba42c59b5c45774eb5bbc66e5a1f8a8f19100f1b580c218e2509addf82",
    "governance/discriminating-supplement/W8-S1-commitment-manifest.json":
        "sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28",
}
REVEAL_HOME = "governance/discriminating-reveal"

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    RECOVERY: ("session-recovery module",
               "sha256:9c1c6dd6c534ce1fd8400442259e5da87c35821c19708695f513b4265a56bd2b",
               "318483c81f35a10f5a420dd5b4fc0bddda6ef171"),
    REGISTRY: ("registry",
               "sha256:8817f5c90d19f3c7db194f16277458c2b965d957de07cd8ee792ac6fde0bc4fe",
               "9d9095f7c3efdcbd07a632bba935eb3cd4646a66"),
    BOARD: ("board",
            "sha256:56b110908ee6e917aa364058c73c2b37466d9c854bde6bddcd8a9a5f562f7665",
            "b628ee1f1bde3b2354486f0adffd430f93d5dcae"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob). The only
# digests the brief may carry are this pin and its pre-image's.
POSTIMAGE = {
    RECOVERY: ("sha256:6873de43760267cb51366078818cbc33ac5e50bbfd8cabe9eb840dd05d910b97",
               "d0bafd22b15f949d980ab3dc0884250ed325c4aa"),
}

# ------------------------------------------ the one succession: ADR-0058 R9
SITES = {
    RECOVERY: (
        ("R9",
         'R9_REVEAL = "No divergence is diagnosed, explained away or corrected."\n',
         'R9_REVEAL = "No divergence is diagnosed, explained away or corrected."\n'
         "# R9's later-deliverable limb as succeeded at the W8-D4 opening\n"
         "# (W8-D4-IVB section 8).\n"
         'D3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"\n'),
        ("R9",
         '        with self.subTest(fact="no registry entry opens a later deliverable"):\n'
         '            self.assertEqual([e["id"] for e in entries\n'
         '                              if e["deliverable"] in LATER], [])\n',
         "        # Succeeded at the W8-D4 opening landing: the absence of every\n"
         "        # later-deliverable entry stays proven at the W8-D3 completion\n"
         "        # commit; W8-D4's entry set moves to that landing's own proof\n"
         "        # module, and W8-D5 to W8-D7 stay unopened.\n"
         '        with self.subTest(fact="no registry entry opened a later "\n'
         '                               "deliverable at the W8-D3 completion"):\n'
         "            at_completion = json.loads(packet.committed_object_bytes(\n"
         '                ROOT, D3_COMPLETION, "governance/registry.json"))[\n'
         '                "entries"]\n'
         '            self.assertEqual([e["id"] for e in at_completion\n'
         '                              if e["deliverable"] in LATER], [])\n'
         '        with self.subTest(fact="no registry entry opens W8-D5 to "\n'
         '                               "W8-D7"):\n'
         '            self.assertEqual([e["id"] for e in entries\n'
         '                              if e["deliverable"] in LATER[1:]], [])\n'),
    ),
}

# --------------------------------------------------------------- carriage
METHODS = ("mutations", "near-miss cases", "deceptive stylistic variation",
           "under-specified cases", "governance-preserving paraphrase",
           "boundary adversaries")
REQUIRED_IVB = (
    "W8-D4 opens for instrument-validation work only, through the landing "
    "programme of section 9. W8-D5 through W8-D7 remain closed.",
    "This brief itself authors no validation case, performs no validation, "
    "holds no session, records no disposition, reads no custody, reveals "
    "nothing, compares nothing, counts nothing, diagnoses no divergence and "
    "contacts no model.",
    "No model contact is assumed, performed or prepared",
    "Validation never yields a verdict on the instrument.",
    "Validation deliberately challenges the instrument and records "
    "case-level comparison outcomes.",
    "An agreement does not establish that the instrument detected anything, "
    "that either token is correct or that any case passed",
    "a divergence is lawful signal about the case, the construction, the "
    "doctrine or the procedure — never a reviewer error",
    "No W8-D4 act amends, re-dispositions or re-reveals any W8-D3 artefact.",
    "never rewrites that history",
    "Distinct homes do not remove the need for proof successions:",
    "distinct text and identities support freshness, never proven semantic "
    "independence or absence of influence",
    "W8-D4 still completes at that landing",
    "The original corpus's retained records stay sealed",
    "no case may rest on, or extend, an unrecognised property",
    "Fresh seeds only.",
    "The governing laws are written for their own corpora.",
    "leaving ADR-0055 and ADR-0057 byte-untouched.",
    "including review of the corpus's authoring candidate",
    "It never imports private conversation, unrecorded reasoning, model "
    "output or hidden context.",
    "No outcome attributes error to the reviewer (ADR-0054 decision 28), and "
    "no outcome declares either token correct.",
    "Nothing is corrected inside W8-D4.",
    "Each later landing runs a placeholder probe over every existing check "
    "before any custody access and before its census is fixed.",
    "Model contact and W8-D5 through W8-D7 remain outside this brief.",
    "Acceptance of this brief adopts these positions.",
)
OUTCOMES = ("construction", "doctrine", "procedure", "undetermined")
# Section 7's closed outcome item, exactly: its lead (after the item number),
# the four members in order, the blank line and the closing statement. The
# whole item, up to the next numbered item, must be exactly these lines.
OUTCOME_LINES = (
    "**The outcome set is closed.** Each diagnosed divergence is recorded "
    "with one or more of:",
    "    - **construction** — the case's visible evidence does not lawfully "
    "support its authored class under the class authoring law;",
    "    - **doctrine** — the doctrine admits more than one lawful reading of "
    "the case;",
    "    - **procedure** — the packet, the review procedure or the session "
    "conditions bear on the outcome;",
    "    - **undetermined** — the published evidence does not settle it.",
    "",
    "    **No outcome attributes error to the reviewer (ADR-0054 decision "
    "28), and no outcome declares either token correct.**",
)
ITEM = re.compile(r"^\d+\. ")
BOLD_BULLET = re.compile(r"^\s*[-*+]\s+\*\*")
# Wording withdrawn at r2 as conclusions the comparison cannot establish, or
# as boundaries wider than the permitted later acts; none may recur.
OVERCLAIMS = ("records whether it held", "whether the instrument noticed",
              "built to be clear", "would test recognition, not the instrument",
              "or reinterprets any W8-D3 artefact", "or its proofs is touched",
              "Nobody may see", "The failure it would expose",
              "reinterpretation of a W8-D3 artefact")
# Section 8's succession table: exactly this header, rule and one row built
# from the trusted pins (succession_row), with blank lines either side.
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_RULE = "|---|---|---|---|"
WITHHELD = ("authors no validation case", "performs no validation",
            "diagnoses no divergence", "contacts no model",
            "W8-D5 through W8-D7 remain closed",
            "The original corpus's retained records stay sealed",
            "no W8-D4 act lists, opens, parses, hashes, copies or reveals them",
            "any instrument verdict, adequacy judgement or readiness claim "
            "(W8-D5)",
            "any contact decision or contact surface (W8-D6)")
# A number written beside a token or relation name, in either order, across
# up to eight non-alphanumeric characters: whitespace, punctuation, table
# pipes and Markdown code or emphasis marks. A textual guard only; it is
# never semantic proof that no wording could express a count.
_COUNT_NAME = (r"(?<![A-Za-z0-9])(?:governance_delta_present|"
               r"no_governance_delta|review_inconclusive|agreements?|"
               r"divergences?)(?![A-Za-z0-9])")
_COUNT_NUMBER = (r"(?<![A-Za-z0-9])(?:\d+|one|two|three|four|five|six|seven|"
                 r"eight|nine|ten|eleven|twelve)(?![A-Za-z0-9])")
_COUNT_GAP = r"[^A-Za-z0-9\n]{0,8}"
COUNT_BESIDE = re.compile(
    "(?i)" + _COUNT_NAME + _COUNT_GAP + _COUNT_NUMBER + "|"
    + _COUNT_NUMBER + _COUNT_GAP + _COUNT_NAME)
DIGEST = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")

# --------------------------------------- board and registry: authorised edits
IVB_LINK = ("([`W8-D4-instrument-validation-brief.md`]"
            "(W8-D4-instrument-validation-brief.md))")
IVB_STATUS_TAIL = (
    "W8-D4 for instrument-validation work only, as six landings behind their "
    "own acceptances: this brief; the validation law; a fresh validation "
    "corpus; blind validation sessions; reveal and the case-level "
    "comparison; and, if the human authority so decides, divergence "
    "diagnosis and completion. It names six validation methods — mutations, "
    "near-miss cases, deceptive stylistic variation, under-specified cases, "
    "governance-preserving paraphrase and boundary adversaries — and authors "
    "no case, performs no validation and diagnoses nothing yet; the "
    "published W8-D3 record stays fixed and the original corpus's retained "
    "records stay sealed.")
IVB_STATUS = {
    "draft": ("**A draft W8-D4 opening brief, `W8-D4-IVB`, is before the "
              "human reviewer** " + IVB_LINK + ": if accepted, it would open "
              + IVB_STATUS_TAIL),
    "accepted": ("**The W8-D4 opening brief, `W8-D4-IVB`, is accepted** "
                 + IVB_LINK + " — accepted %s: it opens " + IVB_STATUS_TAIL),
}
IVB_ROW = ("| W8-D4 — Instrument Validation (opening brief, W8-D4-IVB) | "
           "[`W8-D4-instrument-validation-brief.md`]"
           "(W8-D4-instrument-validation-brief.md) | ")
IVB_ROW_BODY = (
    "Tier J: **opens W8-D4 for instrument-validation work only** — attempts "
    "to break the instrument with six methods, each a construction "
    "discipline for fresh synthetic cases whose method and family stay "
    "withheld until reveal. Six landings behind their own acceptances; "
    "divergence diagnosis, if the human authority so decides, comes last, "
    "rests on published evidence only, uses a closed outcome set, never "
    "attributes error to the reviewer and corrects nothing. ADR-0058's R9 "
    "later-deliverable limb succeeds at this landing. **No case, "
    "validation, session, reveal, diagnosis or count yet; the W8-D3 record "
    "stays fixed; the original corpus stays sealed; W8-D5 to W8-D7 stay "
    "closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**No divergence is diagnosed, explained away or "
                 "corrected. W8-D4 through W8-D7 remain closed behind their "
                 "own briefs.**")
CLOSED_AFTER = ("**No divergence is diagnosed, explained away or corrected. "
                "W8-D5 through W8-D7 remain closed behind their own briefs.**")
CCR_CLOSE = "effective on publication and remote verification. "
BOARD_STATUS_ANCHOR = CCR_CLOSE + CLOSED_BEFORE
BOARD_ROW_ANCHOR = "W8-D4 through W8-D7 stay closed.** |\n"
IVB_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
IVB_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D4-IVB", "path": BRIEF, "type": "phase-brief",
    "title": "W8-D4 - Instrument Validation: Opening Brief",
    "role": (
        "The opening brief of W8-D4, instrument validation, under the W8 "
        "runway: opens W8-D4 for instrument-validation work only through a "
        "six-landing programme - this brief, the validation law, a fresh "
        "validation corpus, blind validation sessions, reveal and the "
        "case-level comparison, and, if the human authority so decides, "
        "divergence diagnosis and completion. Defines six validation methods "
        "as construction disciplines for fresh synthetic cases, with method "
        "and family withheld until reveal; fixes the evidence limits, closed "
        "outcome set and human decision points of divergence diagnosis, "
        "which never attributes error to the reviewer and corrects nothing; "
        "carries ADR-0058's R9 later-deliverable succession at its own "
        "landing, with proof obligations VB1 to VB8. Authors no case, "
        "performs no validation and diagnoses nothing; the published W8-D3 "
        "record stays fixed, the original corpus stays sealed, W8-D5 to "
        "W8-D7 stay closed, and no model is contacted."),
    "depends_on": ["W8-AR", "ADR-0054", "ADR-0055", "ADR-0057", "ADR-0058",
                   "ADR-0059", "W8-D3-SCB", "W8-D3-HDR", "W8-D3-DR-01",
                   "W8-D3-CCR", "W8-S1-SCR", "W8-S1-CM-01", "W8-HPC",
                   "W8-HAC", "W8-D2-CBC", "ADR-0056", "W7-CR"],
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


def committed(commit, rel):
    return packet.committed_object_bytes(ROOT, commit, rel)


def l5_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added the brief, whose sole parent
    must be BASELINE."""
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
    return _lf((ROOT / rel).read_bytes() if commit is None
               else committed(commit, rel))


def snapshot_text(commit, rel):
    return snapshot_bytes(commit, rel).decode("utf-8")


def nine_rules():
    return re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                     r"failure\.\*\*)", _lf(committed(BASELINE, DOCTRINE))
                     .decode("utf-8")).group(1)


def carriage_violations(text, runway, nine):
    """What VB1 requires of the brief: each method as the runway names it,
    the review question, the tokens and the nine-rule block byte-identical,
    each load-bearing statement exactly once, and the closed outcome set."""
    flat = _flat(text)
    v = ["a method is not carried: %s" % m for m in METHODS
         if m not in runway or m not in flat.lower()]
    if "*" + packet.REVIEW_QUESTION + "*" not in text:
        v.append("the review question is not byte-identical")
    v += ["a token is not carried: %s" % t for t in packet.TOKENS
          if "`%s`" % t not in text]
    if nine not in text:
        v.append("the nine-rule block is not byte-identical")
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED_IVB if flat.count(s) != 1]
    return v


def section_lines(text, number):
    """The lines of section `number`, from its heading up to the next
    heading; None unless the heading occurs exactly once."""
    lines = text.split("\n")
    heads = [i for i, l in enumerate(lines)
             if l.startswith("## %d. " % number)]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(lines))
                if lines[j].startswith("## ")), len(lines))
    return lines[heads[0]:end]


def outcome_set_violations(text):
    """Section 7's outcome item must be exactly OUTCOME_LINES: every line from
    the item's number up to the next numbered item, with numbered items
    directly either side. Nothing inside it is skipped; no bold-led bullet
    appears elsewhere in section 7; each member's bold name occurs once in
    the whole brief. Structural carriage only, never a diagnosis's meaning."""
    lines = text.split("\n")
    heads = [i for i, l in enumerate(lines)
             if ITEM.match(l) and l[ITEM.match(l).end():] == OUTCOME_LINES[0]]
    if len(heads) != 1:
        return ["the outcome item is not present exactly once"]
    i = heads[0]
    end = next((j for j in range(i + 1, len(lines))
                if ITEM.match(lines[j]) or lines[j].startswith("#")),
               len(lines))
    v = []
    if tuple([OUTCOME_LINES[0]] + lines[i + 1:end]) != OUTCOME_LINES:
        v.append("the outcome item is not exactly its four members, each "
                 "once, and its closing statement")
    if i == 0 or not ITEM.match(lines[i - 1]):
        v.append("a line other than a numbered item abuts the outcome "
                 "item's top")
    if end >= len(lines) or not ITEM.match(lines[end]):
        v.append("the outcome item is not followed directly by the next "
                 "numbered item")
    sec = section_lines(text, 7)
    if sec is None:
        v.append("section 7 is not present exactly once")
    else:
        bold = [l for l in sec if BOLD_BULLET.match(l)]
        if bold != list(OUTCOME_LINES[1:5]):
            v.append("section 7's bold-led bullets are not exactly the four "
                     "outcome members")
    v += ["outcome %s is named %d times" % (o, text.count("**%s**" % o))
          for o in OUTCOMES if text.count("**%s**" % o) != 1]
    return v


def overclaim_violations(text):
    flat = _flat(text)
    return ["withdrawn wording recurs: %s" % s for s in OVERCLAIMS
            if s in flat]


def succession_row():
    """The one authorised succession row, built from the trusted pins - never
    read from the brief being checked."""
    return "| `%s` | R9 | `%s` | `%s` |" % (RECOVERY, PREIMAGE[RECOVERY][1],
                                          POSTIMAGE[RECOVERY][0])


def succession_table_violations(text):
    """Every '|'-bearing line of section 8, and the lines abutting them, must
    be exactly the header, the rule and the one authorised row, contiguous,
    with blank lines either side. Unknown, duplicate, malformed, indented or
    pipe-less rows are refused, never filtered out."""
    sec = section_lines(text, 8)
    if sec is None:
        return ["section 8 is not present exactly once"]
    piped = [i for i, l in enumerate(sec) if "|" in l]
    expected = [SUCCESSION_HEADER, SUCCESSION_RULE, succession_row()]
    if [sec[i] for i in piped] != expected:
        return ["section 8's table is not exactly its header, rule and one "
                "authorised row"]
    if piped != list(range(piped[0], piped[0] + len(expected))):
        return ["section 8's table is not contiguous"]
    v = []
    if sec[piped[0] - 1] != "":
        v.append("a non-blank line abuts the table's top")
    if piped[-1] + 1 >= len(sec) or sec[piped[-1] + 1] != "":
        v.append("a non-blank line abuts the table's bottom")
    return v


def withholding_violations(text):
    flat = _flat(text)
    return ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]


def fixed_record_violations(read):
    """read(rel) gives the LF bytes the snapshot holds. The pinned W8-D3
    register and records and the supplementary manifest, and every revealed
    record, must equal their baseline bytes; each revealed record must
    reproduce its published commitment."""
    v = []
    for rel, pin in FIXED.items():
        if _sha(_lf(committed(BASELINE, rel))) != pin:
            v.append("the baseline differs from its pin: %s" % rel)
        if _sha(read(rel)) != pin:
            v.append("changed at this landing: %s" % rel)
    rows = json.loads(committed(CORPUS, supplement.MANIFEST))["rows"]
    if not rows:
        v.append("the supplementary manifest has no rows")
    for i, r in enumerate(rows):
        rel = "%s/%s.json" % (REVEAL_HOME, r["case_id"])
        base = committed(BASELINE, rel)
        if envelope.sha256_bytes(base) != r["authoring_commitment_sha256"]:
            v.append("revealed record %d does not reproduce its commitment"
                     % i)
        if read(rel) != _lf(base):
            v.append("revealed record %d changed at this landing" % i)
    return v


def d4_entry_set(entries):
    return {e["id"] for e in entries if e["deliverable"] == "W8-D4"}


def later_entries(entries):
    return [e["id"] for e in entries if e["deliverable"] in LATER_THAN_D4]


def census_violations(paths, brief_flat):
    v = []
    if paths != set(FIXED_CENSUS):
        v.append("the landing's paths are not exactly the census")
    m = re.search(r"\*\*This landing's census is exactly five paths:\*\* "
                  r"(.*?) ## ", brief_flat)
    if m is None:
        v.append("the brief does not state the census")
    elif set(re.findall(r"`([^`]+)`", m.group(1))) != set(FIXED_CENSUS):
        v.append("the brief names a different census")
    return v


def exposure_violations(text, exempt=()):
    """No case identity, no digest outside the exempt exact lines (each
    removed once; the brief's only exemption is the trusted succession row),
    no reserved authoring label, no schema literal, and no number beside a
    token or relation name."""
    v = []
    if recovery.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    stripped = text
    for line in exempt:
        stripped = stripped.replace(line, "", 1)
    if DIGEST.search(stripped):
        v.append("an unpinned digest is present")
    v += ["a reserved label: %s" % s
          for s in corpus.reserved_channel_hits(text)]
    v += ["a schema literal" for s in (packet.PACKET_SCHEMA,
                                       calibration.REGISTER_SCHEMA,
                                       envelope.AUTHORING_SCHEMA)
          if s in text]
    if COUNT_BESIDE.search(text):
        v.append("a count beside a token or relation")
    return v


def succession_violations(rel, present, brief, sites=None):
    sites = SITES[rel] if sites is None else sites
    v = []
    pre = _lf(committed(BASELINE, rel)).decode("utf-8")
    if _sha(pre.encode("utf-8")) != PREIMAGE[rel][1]:
        v.append("the baseline pre-image differs from its pin")
    expected, problems = authority.apply_sites(pre, sites)
    v += problems
    if expected != present:
        v.append("the bytes are not the exact authorised post-image")
    for label, _, new in sites:
        if present.count(new) != 1:
            v.append("%s: post-image site occurs %d times"
                     % (label, present.count(new)))
    restored, problems = authority.reverse_sites(present, sites)
    v += problems
    if restored != pre:
        v.append("reversing the table does not restore the pre-image")
    if _sha(present.encode("utf-8")) != POSTIMAGE[rel][0]:
        v.append("the bytes are not the reviewed post-image")
    if authority.labels(sites) != ("R9",):
        v.append("the sites are not R9's alone")
    v += succession_table_violations(brief)
    return v


def ivb_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and IVB_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (IVB_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         CCR_CLOSE + fill(IVB_STATUS[state]) + " " + CLOSED_AFTER),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + IVB_ROW + fill(ROW_PREFIX[state]) + IVB_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D4",
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
            + authority._indent(json.dumps(new_entry(state, date, brief_hash),
                                           indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    return " ".join([IVB_ROW, IVB_ROW_BODY, CLOSED_AFTER]
                    + list(IVB_STATUS.values()))


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


# ------------------------------------------------------------------ proofs
class VB1_Carriage(unittest.TestCase):
    def test_vb1_methods_question_tokens_rules_and_statements(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, BRIEF)
        runway = _flat(_lf(committed(BASELINE, RUNWAY)).decode("utf-8"))
        nine = nine_rules()
        with self.subTest(fact="the brief carries everything VB1 requires"):
            self.assertEqual(carriage_violations(text, runway, nine), [])
        with self.subTest(fact="section 7's outcome list is closed"):
            self.assertEqual(outcome_set_violations(text), [])
        with self.subTest(fact="no withdrawn over-claim recurs"):
            self.assertEqual(overclaim_violations(text), [])
        for name, mutant in {
                "a removed statement": text.replace(REQUIRED_IVB[0], "", 1),
                "a duplicated statement": text + "\n" + REQUIRED_IVB[1] + "\n",
                "an altered nine-rule block": text.replace(
                    nine, nine.replace("≠", "=", 1), 1),
                "an altered review question": text.replace(
                    packet.REVIEW_QUESTION, packet.REVIEW_QUESTION.upper(), 1),
                "a dropped method": re.sub("(?i)near-miss cases", "near cases",
                                           text)}.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(carriage_violations(mutant, runway, nine))
        lines = text.split("\n")
        head = next(i for i, l in enumerate(lines) if ITEM.match(l)
                    and l[ITEM.match(l).end():] == OUTCOME_LINES[0])
        last_rule = next(i for i, l in enumerate(lines)
                         if l.startswith("## 8. "))

        def inserted(i, new):
            return "\n".join(lines[:i] + [new] + lines[i:])

        def replaced(i, new):
            return "\n".join(lines[:i] + [new] + lines[i + 1:])

        other = "- **other** — a category outside the declared outcome set."
        for name, mutant in {
                "an extra member (the r1 bypass)": inserted(head + 5,
                                                            "    " + other),
                "an extra member, unindented": inserted(head + 5, other),
                "an extra member at two spaces": inserted(head + 5,
                                                          "  " + other),
                "an extra member at six spaces": inserted(head + 5,
                                                          "      " + other),
                "an extra member after a tab": inserted(head + 5,
                                                        "\t" + other),
                "an extra member as an asterisk bullet": inserted(
                    head + 5, "    * **other** — outside the set."),
                "a duplicate member": inserted(head + 2, lines[head + 1]),
                "a missing member": "\n".join(lines[:head + 2]
                                              + lines[head + 3:]),
                "a malformed member": replaced(
                    head + 1, lines[head + 1].replace(" — ", " - ", 1)),
                "an unbolded member": replaced(
                    head + 4, lines[head + 4].replace("**undetermined**",
                                                      "undetermined", 1)),
                "a line between the lead and the first member": inserted(
                    head + 1, "    Further categories may apply."),
                "a non-blank line abutting the item's top": inserted(
                    head, "    " + other),
                "a line after the closing statement": inserted(
                    head + 7, "    " + other),
                "a bold-led member elsewhere in section 7": inserted(
                    last_rule - 1, "    " + other)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(outcome_set_violations(mutant))
        with self.subTest(control="every withdrawn over-claim is detected"):
            self.assertEqual([s for s in OVERCLAIMS if not
                              overclaim_violations(text + "\n" + s + "\n")],
                             [])


class VB2_NonAuthorisations(unittest.TestCase):
    def test_vb2_the_brief_withholds_every_later_act(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, BRIEF)
        with self.subTest(fact="every later act is withheld"):
            self.assertEqual(withholding_violations(text), [])
        for name, mutant in {
                "a removed withholding": text.replace("contacts no model", ""),
                "a weakened withholding": text.replace(
                    "W8-D5 through W8-D7 remain closed",
                    "W8-D5 through W8-D7 may open")}.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(withholding_violations(mutant))


class VB3_NoExposure(unittest.TestCase):
    def test_vb3_no_identity_digest_label_schema_or_count(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, BRIEF)
        reg = json.loads(snapshot_text(commit, REGISTRY))
        role = " ".join(e["role"] + " " + e["title"] for e in reg["entries"]
                        if e["id"] == "W8-D4-IVB")
        row = succession_row()
        for name, surface, exempt in (
                ("brief", text, (row,)),
                ("registry role and title", role, ()),
                ("board wording this landing adds", added_board_wording(),
                 ())):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(exposure_violations(surface, exempt), [])
        with self.subTest(fact="no token on the registry role or the board "
                               "wording"):
            for surface in (role, added_board_wording()):
                self.assertEqual([t for t in packet.TOKENS if t in surface],
                                 [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([s for s in (packet.PACKET_SCHEMA,
                                          calibration.REGISTER_SCHEMA,
                                          envelope.AUTHORING_SCHEMA)
                              if s in src], [])
        for name, plant in (("a case identity",
                             "W8-C-" + "a" * 64),
                            ("an unpinned digest", "b" * 64),
                            ("a reserved label",
                             sorted(corpus.RESERVED_FIELDS)[0]),
                            ("a count beside a relation",
                             "with 11 agreements")):
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(text + "\n" + plant,
                                                    (row,)))
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "an unknown succession row (the r1 bypass)": text.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a digest outside the table": text + "\nSee `sha256:%s`.\n"
                % ("f" * 64),
                "a trusted pin copied outside the table": text + "\n`%s`\n"
                % POSTIMAGE[RECOVERY][0],
                "the r1 count bypass": text
                + "\n`governance_delta_present`: 17\n"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(exposure_violations(mutant, (row,)))
        undetected = []
        for word in list(packet.TOKENS) + ["agreement", "agreements",
                                           "divergence", "divergences"]:
            for shape in ("{}", "`{}`", "**{}**", "**`{}`**", "*{}*"):
                name = shape.format(word)
                for n in ("1", "11", "17", "112", "eleven"):
                    for form in ("{n} {name}", "{n}\t{name}", "{n}: {name}",
                                 "{n} × {name}", "{name} {n}", "{name}: {n}",
                                 "{name} = {n}", "{name}, {n}",
                                 "{name} ({n})", "{name} — {n}",
                                 "| {name} | {n} |"):
                        plant = form.format(n=n, name=name)
                        if not exposure_violations(text + "\n" + plant
                                                   + "\n", (row,)):
                            undetected.append(plant)
        with self.subTest(control="every planted count form is detected: "
                                  "three tokens, both relations, either "
                                  "order, plain and code-formatted"):
            self.assertEqual(undetected, [])


class VB4_PublishedRecordsFixed(unittest.TestCase):
    def test_vb4_published_w8_d3_and_s1_artefacts_unchanged(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])

        def read(rel):
            return snapshot_bytes(commit, rel)

        with self.subTest(fact="this landing leaves the pinned and revealed "
                               "records unchanged"):
            self.assertEqual(fixed_record_violations(read), [])
        rows = json.loads(committed(CORPUS, supplement.MANIFEST))["rows"]
        for name, target in (
                ("a changed pinned record", sorted(FIXED)[0]),
                ("a changed revealed record",
                 "%s/%s.json" % (REVEAL_HOME, rows[0]["case_id"]))):
            with self.subTest(control="%s is refused" % name):
                def planted(rel, target=target):
                    return read(rel) + (b" " if rel == target else b"")
                self.assertTrue(fixed_record_violations(planted))


class VB5_R9Succession(unittest.TestCase):
    def test_vb5_the_r9_succession_is_exact(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        brief = snapshot_text(commit, BRIEF)
        with self.subTest(baseline_object=PREIMAGE[RECOVERY][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + RECOVERY)
                             .strip(), PREIMAGE[RECOVERY][2])
        self.assertEqual(succession_violations(
            RECOVERY, snapshot_text(commit, RECOVERY), brief), [])
        with self.subTest(fact="the succeeded module carries the "
                               "completion commit"):
            self.assertEqual(recovery.D3_COMPLETION, BASELINE)
            self.assertEqual(recovery.LATER[1:], LATER_THAN_D4)
        present = snapshot_text(commit, RECOVERY)
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[RECOVERY][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[RECOVERY] + (("planted", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(RECOVERY, text, brief,
                                                      table))
        with self.subTest(fact="the post-image is the reviewed object"):
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[RECOVERY][1])
        row = succession_row()
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "an unknown source row (the r1 bypass)": brief.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a duplicate authorised row": brief.replace(
                    row + "\n", row + "\n" + row + "\n", 1),
                "an extra field": brief.replace(row, row + " extra |", 1),
                "a missing field": brief.replace(
                    row, row.rsplit(" | ", 1)[0] + " |", 1),
                "another site label": brief.replace(
                    row, row.replace("| R9 |", "| R9, R10 |"), 1),
                "an indented row": brief.replace(row, "  " + row, 1),
                "a row without its opening pipe": brief.replace(row, row[2:],
                                                                1),
                "a row above the header": brief.replace(
                    SUCCESSION_HEADER, rogue + "\n" + SUCCESSION_HEADER, 1),
                "a non-blank line over the table": brief.replace(
                    "\n\n" + SUCCESSION_HEADER,
                    "\nA stray line.\n" + SUCCESSION_HEADER, 1),
                "a non-blank line under the table": brief.replace(
                    row + "\n", row + "\nA stray line.\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, brief)
                self.assertTrue(succession_table_violations(mutant))
                self.assertTrue(succession_violations(
                    RECOVERY, present, mutant))


class VB6_RegistryAndBoard(unittest.TestCase):
    def test_vb6_registry_and_board_change_exactly(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        brief = snapshot_text(commit, BRIEF)
        state, date, v = ivb_state(brief)
        self.assertEqual(v, [])
        board_pre = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(BASELINE, REGISTRY)).decode("utf-8")
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = snapshot_text(commit, BOARD)
        expected, problems = authority.apply_sites(board_pre,
                                                   board_sites(state, date))
        with self.subTest(fact="exact authorised board", state=state):
            self.assertEqual(problems, [])
            self.assertEqual(board, expected)
            self.assertEqual(recovery.board_surfaces(board)[2], [])
            self.assertIn(recovery.R9_REVEAL, board)
        reg = snapshot_text(commit, REGISTRY)
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(
                reg_pre, _sha(brief.encode("utf-8")), state, date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, _sha(brief.encode("utf-8")), other, "2000-01-01"))
            wrong, _ = authority.apply_sites(board_pre,
                                             board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)


class VB7_Registration(unittest.TestCase):
    def test_vb7_registered_and_w8_d4_entry_set(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        brief = snapshot_text(commit, BRIEF)
        state, date, _ = ivb_state(brief)
        by_id = {e["id"]: e for e in json.loads(
            snapshot_text(commit, REGISTRY))["entries"]}
        e = by_id.get("W8-D4-IVB")
        with self.subTest(fact="registered at W8-D4 with matching hash and "
                               "status"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]),
                             (BRIEF, "phase-brief", "W8", "W8-D4"))
            self.assertEqual(e["content_hash"], _sha(brief.encode("utf-8")))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            if commit is None:
                self.assertEqual(e["content_hash"], lf_hash(ROOT / BRIEF))
        # The W8-D4 entry set: a present-state gate, succeeded at each later
        # W8-D4 landing that adds an entry (W8-D4-IVB section 8).
        present = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]
        with self.subTest(fact="W8-D4 entries are exactly this brief's"):
            self.assertEqual(d4_entry_set(present), D4_ENTRIES)
        # W8-D5 to W8-D7 stay refused in the present state by ADR-0058's
        # succeeded R9; this proof binds their absence at this landing only.
        at_landing = json.loads(snapshot_text(commit, REGISTRY))["entries"]
        with self.subTest(fact="no W8-D5 to W8-D7 entry at this landing"):
            self.assertEqual(later_entries(at_landing), [])
        with self.subTest(control="a premature W8-D4 entry is refused"):
            planted = present + [dict(present[-1], id="W8-D4-PLANTED",
                                      deliverable="W8-D4")]
            self.assertNotEqual(d4_entry_set(planted), D4_ENTRIES)
        with self.subTest(control="a W8-D5 entry is refused"):
            planted = at_landing + [dict(at_landing[-1], id="W8-D5-PLANTED",
                                         deliverable="W8-D5")]
            self.assertTrue(later_entries(planted))


class VB8_Census(unittest.TestCase):
    def test_vb8_census_is_exactly_five_paths(self):
        commit, problems = l5_snapshot()
        self.assertEqual(problems, [])
        self.assertEqual(len(FIXED_CENSUS), 5)
        paths = landing_paths(commit)
        brief = _flat(snapshot_text(commit, BRIEF))
        with self.subTest(fact="the census is exactly five paths, as the "
                               "brief names it"):
            self.assertEqual(census_violations(paths, brief), [])
        for name, (p, b) in {
                "an extra path": (paths | {"docs/phases/placeholder.md"},
                                  brief),
                "a missing path": (paths - {REGISTRY}, brief),
                "a brief naming another path": (paths, brief.replace(
                    "`%s`" % REGISTRY, "`governance/placeholder.json`"))
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual((p, b), (paths, brief))
                self.assertTrue(census_violations(p, b))


if __name__ == "__main__":
    unittest.main()
