"""W8-D4-B — instrument validation law proofs (ADR-0060, VL1–VL12).

The validation law that the accepted W8-D4 opening brief places at D4-B:
the method law and its admission table, the validation-construction record
and its manifest, the family and session rules, the carriage of the
commitment, custody, session, reveal and comparison law to the validation
corpus by the law's own decisions, the permitted counts, and the closed,
staged proof successions. This module proves the law's carriage and
withholding; its exposure limits, with the one trusted succession row as
the only digest exemption; the mechanics of every closed shape and rule
over clearly labelled sentinels; the exact VB7 succession; the staged
absences; and the exact registry, board and census - each with
planted-mutant or negative controls. Closed validators compare against
trusted expected values held here, never against values read from the text
being checked, and refuse unrecognised material rather than skip it; every
fixed-shape identity, digest and nonce is validated as a whole string of
explicit string type. Every proof reads this landing's snapshot except the
staged absences of VL10, which are present-state gates, each succeeded only
by the later landing that ADR-0060 Part J names. Proofs that later landings
add follow ADR-0060 decision 39: historical claims at their own landing's
fixed snapshot, new live absence or admission gates only in VL10, and the
candidate-byte and committed-object correspondence checks that immutable
artefacts require wherever ADR-0057 decision 19 and W8-D2-CBC apply.

THIS MODULE READS NO CUSTODY. It holds no case identity, no published
schema literal and no count as a literal, builds nothing but labelled
mechanics sentinels, authors no case and performs no validation.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any method is adequate or that the instrument is
valid, mature or ready; anything about any case, disposition, method,
family, divergence or reviewer; that any construction is semantically
sound; that any diagnosis is right; that any model was contacted; or that
W8-D5 through W8-D7 may open.
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
import test_w8_validation_opening as opening
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified W8-D4 opening: this landing's sole parent
# and the commit every pre-image below is read from.
BASELINE = "ad59925813f8b0c39789dac3b29383a5f6e25cea"

LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
SELF_REL = "tests/test_w8_validation_law.py"
OPENING = "tests/test_w8_validation_opening.py"
BRIEF = opening.BRIEF
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
DOCTRINE = opening.DOCTRINE
D2_MANIFEST = "governance/discriminating-instrument/W8-D2-commitment-manifest.json"
FIXED_CENSUS = frozenset({LAW, SELF_REL, OPENING, REGISTRY, BOARD})

# Decision 23's later homes, records and registry entries: each absent until
# its own landing (VL10, a staged present-state gate).
D4_ENTRIES = {"W8-D4-IVB", "ADR-0060"}
LATER_IDS = frozenset({"W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02", "W8-D4-VSR",
                       "W8-D4-DR-01", "W8-D4-VRC", "W8-D4-CPR"})
VALIDATION_HOMES = ("governance/validation-cases",
                    "governance/validation-review",
                    "governance/validation-reveal")
LATER_RECORDS = ("docs/phases/W8-D4-validation-corpus-record.md",
                 "docs/phases/W8-D4-validation-session-record.md",
                 "docs/phases/W8-D4-validation-record.md",
                 "docs/phases/W8-D4-completion-record.md")
# Admitted at the corpus landing (ADR-0060 Part J decision 38): the case
# home its commitment manifest binds, the two manifests, the corpus record
# and its three W8-D4 entries, the construction manifest joining the
# holders of its own schema literal. The former absence stays proven at
# the D4-B landing commit.
D4B_LANDING = "054f1270b8206a059636e18e012223ddfe52d5ea"
CORPUS_MANIFEST = VALIDATION_HOMES[0] + "/W8-V1-commitment-manifest.json"
CONSTRUCTION_MANIFEST = (VALIDATION_HOMES[0]
                         + "/W8-V1-construction-manifest.json")
CORPUS_RECORD = LATER_RECORDS[0]
CORPUS_IDS = frozenset({"W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02"})
# Admitted at the session landing (ADR-0060 Part J decision 38): the
# register home, the register, the session record and the two W8-D4
# entries they add. The corpus-stage state stays proven at the corpus
# landing commit.
D4C_LANDING = "f638cca75ec4a192685bf5cd53f29451cfdbbdd9"
SESSION_REGISTER = VALIDATION_HOMES[1] + "/W8-D4-validation-register.json"
SESSION_RECORD = LATER_RECORDS[1]
SESSION_IDS = frozenset({"W8-D4-VSR", "W8-D4-DR-01"})

# Part E: the validation-construction record and its manifest.
CONSTRUCTION_SCHEMA = "w8-validation-construction-v1"
CONSTRUCTION_MANIFEST_SCHEMA = "w8-construction-manifest-v1"
NEW_SCHEMAS = (CONSTRUCTION_SCHEMA, CONSTRUCTION_MANIFEST_SCHEMA)
CONSTRUCTION_FIELDS = frozenset(
    {"schema", "case_id", "method", "family_seed_sha256", "method_note",
     "reviewer_visible_sha256", "authoring_commitment_sha256",
     "construction_nonce"})
CONSTRUCTION_ROW_FIELDS = frozenset({"case_id",
                                     "construction_commitment_sha256"})
NONCE_RE = re.compile(r"[0-9a-f]{64}")
PUBLISHED_SCHEMAS = (packet.PACKET_SCHEMA, calibration.REGISTER_SCHEMA,
                     envelope.AUTHORING_SCHEMA, envelope.REVIEW_SCHEMA,
                     corpus.MANIFEST_SCHEMA)

# Decision 6: (label, method as the accepted brief names it, classes).
METHOD_TABLE = (
    ("mutation", "Mutations", "A, B, C"),
    ("near_miss", "Near-miss cases", "A, B"),
    ("deceptive_stylistic_variation", "Deceptive stylistic variation", "A, B"),
    ("under_specified", "Under-specified cases", "C"),
    ("governance_preserving_paraphrase", "Governance-preserving paraphrase",
     "B"),
    ("boundary_adversary", "Boundary adversaries", "A, B, C"),
)
ADMITS = {label: frozenset(classes.split(", "))
          for label, _, classes in METHOD_TABLE}
METHOD_HEADER = "| Method label | Method | Authored classes admitted |"
METHOD_RULE = "|---|---|---|"

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    OPENING: ("validation-opening module",
              "sha256:d83f21e8afb4965e32741a0bdefebb5dad7d68e6cd569dc0a6e3a2cd1b6b7f4c",
              "62cf3e41af86374c39928a07f7fa76bad87c90d6"),
    REGISTRY: ("registry",
               "sha256:9b48029a5690558e181a7c341b03beb37db1ed4e57f245d961549fcf7baf3608",
               "62e3d6e4c1bbed513dfb35f697ba0d33d22c90da"),
    BOARD: ("board",
            "sha256:2cd13223f01070bc813150c074483ba81d9954671f098786113dfd9898202340",
            "c7b4a859a8175059fb4adc2671f7cb71730e6c0a"),
}
# The reviewed post-image of this landing's one succession: (LF SHA-256,
# blob). The only digests the law may carry are this pin and its
# pre-image's.
POSTIMAGE = {
    OPENING: ("sha256:d0917547faca6e9ae09ad31dfb9a3516c3578c8a09d7403f678fc9cc10112d52", "71f5072562773b1784c07063fa1b5ea3ec51559e"),
}

# ------------------------------------- the one succession: the VB7 entry set
SITES = {
    OPENING: (
        ("VB7",
         "being checked, and refuse unrecognised material rather than skip "
         "it. Every\n"
         "proof reads this landing's snapshot except one: the W8-D4 entry set "
         "of VB7,\n"
         "a present-state gate succeeded at each later W8-D4 landing that "
         "adds an\n"
         "entry.\n",
         "being checked, and refuse unrecognised material rather than skip "
         "it. Every\n"
         "proof reads this landing's snapshot. VB7's W8-D4 entry set was a\n"
         "present-state gate until the D4-B landing moved it to the "
         "validation-law\n"
         "proof module (ADR-0060); it stays proven at the D4-A landing "
         "commit.\n"),
        ("VB7",
         'LATER_THAN_D4 = ("W8-D5", "W8-D6", "W8-D7")\n',
         'LATER_THAN_D4 = ("W8-D5", "W8-D6", "W8-D7")\n'
         "# The D4-A landing commit, at which VB7's W8-D4 entry set stays "
         "proven\n"
         "# after its succession at the D4-B landing (ADR-0060 Part J).\n"
         'D4A_LANDING = "ad59925813f8b0c39789dac3b29383a5f6e25cea"\n'),
        ("VB7",
         "        # The W8-D4 entry set: a present-state gate, succeeded at "
         "each later\n"
         "        # W8-D4 landing that adds an entry (W8-D4-IVB section 8).\n"
         "        present = json.loads(_lf((ROOT / REGISTRY).read_bytes()))"
         '["entries"]\n'
         '        with self.subTest(fact="W8-D4 entries are exactly this '
         "brief's\"):\n",
         "        # Succeeded at the D4-B landing (ADR-0060 Part J): the W8-D4 "
         "entry\n"
         "        # set stays proven at the D4-A landing commit, and its "
         "present-state\n"
         "        # gate moves to the validation-law proof module.\n"
         "        present = json.loads(committed(D4A_LANDING, REGISTRY))"
         '["entries"]\n'
         '        with self.subTest(fact="W8-D4 entries were exactly this '
         "brief's at \"\n"
         '                               "the D4-A landing"):\n'),
    ),
}

# --------------------------------------------------------------- carriage
REQUIRED_VL = (
    "It opens exactly one validation corpus, `W8-V1`, of exactly eighteen "
    "fresh cases, for the corpus landing D4-C only",
    "Eighteen is fixed for workload and continuity only.",
    "This record creates no substitute reviewer, no delegation mechanism, "
    "no new disposition source and no exception to either decision.",
    "A method is construction metadata, never evidence.",
    "no case may rest on, or extend, an unrecognised property",
    "No case field is added and the reviewer-visible envelope stays closed.",
    "An identity equal to any published identity is a collision and a STOP.",
    "These checks establish textual non-reuse and distinct identities only, "
    "never semantic independence or the absence of influence",
    "The architect's review of the corpus candidate is law and mechanics "
    "review only",
    "Any variant text that two or more validation cases share must be one "
    "declared family seed;",
    "Exactly one validation session is held, over the whole corpus, family "
    "members included.",
    "The session record states this co-presence rule plainly, without "
    "disclosing whether any family exists.",
    "separate from, and never a widening of, the ADR-0055 withheld "
    "authoring record",
    "The record never enters any reviewer-visible surface before "
    "disposition.",
    "It discloses no method, family, class or count beyond the corpus size.",
    "This record carries each, whole and unweakened, to the validation "
    "corpus by its own decisions, leaving ADR-0055 byte-untouched:",
    "if byte stability cannot be guaranteed there, STOP before the first "
    "case.",
    "This record carries its Parts A to C to the validation corpus, whole, "
    "by its own decisions, leaving ADR-0057 byte-untouched.",
    "the renderer's input paths are first proven to be exactly the bound "
    "commitment manifest's case paths, and only then is the packet hash "
    "recorded.",
    "including review of its authoring candidate",
    "the reviewer's prior exposure — to the revealed supplementary "
    "constructions, the W8-D3 comparison and the method descriptions of the "
    "brief and this law — recorded and never attested away",
    "No test proves the absence of influence, semantic independence or "
    "reviewer blinding, and none is claimed.",
    "Nothing in the reveal landing begins until the session record is "
    "published and independently remote-verified.",
    "Reveal publishes the exact retained bytes",
    "An agreement does not establish that the instrument detected anything, "
    "that either token is correct or that any case passed",
    "Diagnosis is not this record's act.",
    "Each later landing still runs its own placeholder probe over every "
    "existing check before any custody access and before its census is "
    "fixed;",
    "No green proof supplies a disposition, completes a landing or opens "
    "W8-D5.",
    "and nothing beside it.",
    "Method and family stay in the revealed construction records, published "
    "as their exact bytes at reveal",
    "holds no new live gate on the absence or admission of a future "
    "artefact: every such gate stays in VL10 and moves only by this list,",
    "This does not restrict the checks immutable artefacts require",
    "Neither this record nor any of its green proofs supplies any of those "
    "acts or conclusions.",
    "this record neither performs that weighing nor authorises W8-D5 to "
    "open",
)
# Wording withdrawn at r2 (the architect's r1 findings 2 to 4); none may
# recur.
WITHDRAWN = (
    "as case-level construction description, the revealed method label",
    "may be cited as evidence for any of those propositions",
    "reads its own landing's snapshot and holds no present-state gate",
)
WITHHELD = ("authors no case", "generates no nonce",
            "writes no retained record", "touches no custody location",
            "renders no packet", "holds no session", "records no disposition",
            "reproduces no commitment", "reveals nothing", "compares nothing",
            "counts nothing", "diagnoses nothing", "contacts no model",
            "No count by method, family or class is published",
            "leaving ADR-0055 byte-untouched",
            "leaving ADR-0057 byte-untouched",
            "W8-D5 through W8-D7 remain closed")

# --------------------------------------- board and registry: authorised edits
LAW_LINK = ("([`../decisions/0060-w8-instrument-validation-law.md`]"
            "(../decisions/0060-w8-instrument-validation-law.md))")
LAW_STATUS_TAIL = (
    "six method labels and the classes each admits, a separately committed "
    "validation-construction record, one corpus `W8-V1` of exactly eighteen "
    "fresh cases reviewed in one session, and the carriage of the "
    "commitment, custody, session, reveal and comparison law to that corpus "
    "by its own decisions; it authors no case, touches no custody and "
    "diagnoses nothing.")
LAW_STATUS = {
    "draft": ("**A draft W8-D4 validation law, ADR-0060, is before the human "
              "reviewer** " + LAW_LINK + ": if accepted, it would fix "
              + LAW_STATUS_TAIL),
    "accepted": ("**The W8-D4 validation law, ADR-0060, is accepted** "
                 + LAW_LINK + " — accepted %s: it fixes " + LAW_STATUS_TAIL),
}
LAW_ROW = ("| W8-D4 — Instrument Validation Law (ADR-0060) | "
           "[`../decisions/0060-w8-instrument-validation-law.md`]"
           "(../decisions/0060-w8-instrument-validation-law.md) | ")
LAW_ROW_BODY = (
    "Tier J: **fixes the validation law before any validation case** — six "
    "method labels and the classes each admits; a separately committed "
    "validation-construction record and manifest; one corpus, `W8-V1`, of "
    "exactly eighteen fresh cases reviewed in one session, family members "
    "included; the carriage of the commitment, custody, session, reveal and "
    "comparison law to that corpus by its own decisions, ADR-0055 and "
    "ADR-0057 byte-untouched; the two permitted count kinds only, with no "
    "count by method, family or class; and the closed, staged successions "
    "of the later landings. The opening brief's VB7 entry set succeeds at "
    "this landing. **No case, custody, session, reveal, count or diagnosis "
    "yet; the W8-D3 record stays fixed; the original corpus stays sealed; "
    "W8-D5 to W8-D7 stay closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = ("the original corpus's retained records stay sealed. "
                       "**No divergence is diagnosed")
BOARD_ROW_ANCHOR = opening.IVB_ROW_BODY + " |\n"
LAW_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification; no validation case may be authored before that "
             "moment, and every one authored after it is authored under this "
             "law.** No status is flipped by the implementer; acceptance is "
             "the human reviewer's dated act.")
LAW_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification; no validation "
                "case may be authored before that moment, and every one "
                "authored after it is authored under this law.**")
NEW_ENTRY = {
    "id": "ADR-0060", "path": LAW, "type": "adr",
    "title": "0060 - W8 Instrument Validation Law",
    "role": (
        "The W8-D4 instrument validation law, landed at D4-B before any "
        "validation case as the effective W8-D4-IVB requires: fixes six "
        "method labels and the authored classes each admits; a separately "
        "committed validation-construction record and its manifest; one "
        "validation corpus, W8-V1, of exactly eighteen fresh cases, with "
        "families of two or three permitted and every case reviewed in one "
        "session; the carriage of the commitment, custody, session, reveal "
        "and comparison law to that corpus by its own decisions, ADR-0055 "
        "and ADR-0057 byte-untouched; exactly the two permitted count kinds, "
        "with no count by method, family or class; and the closed, staged "
        "proof successions of the later landings, with proof obligations "
        "VL1 to VL12. The opening brief's VB7 W8-D4 entry set succeeds at "
        "this landing. Authors no case, touches no custody, holds no session "
        "and diagnoses nothing; W8-D5 to W8-D7 stay closed and no model is "
        "contacted."),
    "depends_on": ["W8-D4-IVB", "W8-AR", "ADR-0054", "ADR-0055", "ADR-0057",
                   "ADR-0058", "ADR-0059", "W8-D2-CBC", "W8-D3-SCB",
                   "W8-D3-CCR", "W8-S1-SCR", "W8-S1-CM-01", "ADR-0050",
                   "ADR-0056", "W7-CR"],
}

# Mechanics sentinels only — NOT cases, NOT authored, NOT governed content.
SENTINEL_TEXTS = tuple(
    "validation-law mechanics sentinel text %s — not a case, carries no "
    "governed meaning" % n for n in ("one", "two", "three", "four", "five"))
SENTINEL_NONCE = "0" * 64  # deterministic mechanics-only sentinel


# ----------------------------------------------------------------- helpers
_lf = opening._lf
_sha = opening._sha
_flat = opening._flat
_blob = opening._blob
committed = opening.committed


def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def l6_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added the law, whose sole parent
    must be BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", LAW).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the law was added more than once"]
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


def part_lines(text, letter):
    """The lines of Part `letter`, from its heading up to the next heading;
    None unless the heading occurs exactly once."""
    lines = text.split("\n")
    heads = [i for i, l in enumerate(lines)
             if l.startswith("## Part %s — " % letter)]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(lines))
                if lines[j].startswith("## ")), len(lines))
    return lines[heads[0]:end]


def closed_table_violations(sec, expected, what):
    """Every '|'-bearing line of the part, and the lines abutting them, must
    be exactly `expected`, contiguous, with blank lines either side."""
    if sec is None:
        return ["%s is not present exactly once" % what]
    piped = [i for i, l in enumerate(sec) if "|" in l]
    if [sec[i] for i in piped] != list(expected):
        return ["%s's table is not exactly its trusted lines" % what]
    if piped != list(range(piped[0], piped[0] + len(expected))):
        return ["%s's table is not contiguous" % what]
    v = []
    if sec[piped[0] - 1] != "":
        v.append("a non-blank line abuts %s's table top" % what)
    if piped[-1] + 1 >= len(sec) or sec[piped[-1] + 1] != "":
        v.append("a non-blank line abuts %s's table bottom" % what)
    return v


def method_rows():
    return ["| `%s` | %s | %s |" % row for row in METHOD_TABLE]


def brief_method_classes(brief):
    """The accepted brief's section 4 table, method name -> classes."""
    lines = opening.section_lines(brief, 4) or []
    out = {}
    for l in lines:
        m = re.fullmatch(r"\| \*\*(.+?)\*\* \|.*\| ([ABC](?:, [ABC])*) \|", l)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def nine_rules():
    return opening.nine_rules()


def carriage_violations(text, nine):
    flat = _flat(text)
    v = []
    if "*" + packet.REVIEW_QUESTION + "*" not in text:
        v.append("the review question is not byte-identical")
    v += ["a token is not carried: %s" % t for t in packet.TOKENS
          if "`%s`" % t not in text]
    if nine not in text:
        v.append("the nine-rule block is not byte-identical")
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED_VL if flat.count(s) != 1]
    v += ["withdrawn wording recurs: %s" % s[:44] for s in WITHDRAWN
          if s in flat]
    v += closed_table_violations(part_lines(text, "B"),
                                 [METHOD_HEADER, METHOD_RULE] + method_rows(),
                                 "Part B")
    return v


def withholding_violations(text):
    flat = _flat(text)
    return ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]


def succession_row():
    """The one authorised succession row, built from the trusted pins -
    never read from the law being checked."""
    return "| `%s` | VB7 | `%s` | `%s` |" % (OPENING, PREIMAGE[OPENING][1],
                                           POSTIMAGE[OPENING][0])


def succession_table_violations(text):
    return closed_table_violations(
        part_lines(text, "J"),
        [opening.SUCCESSION_HEADER, opening.SUCCESSION_RULE,
         succession_row()], "Part J")


def exposure_violations(text, exempt=(), new_schemas_allowed=False):
    """The opening's textual guard (no case identity, no digest outside the
    exempt exact lines, no reserved authoring label, no number beside a
    token or relation name), plus no published schema literal anywhere and,
    outside the law, neither new schema literal."""
    v = opening.exposure_violations(text, exempt)
    v += ["a published schema literal: %s" % s for s in PUBLISHED_SCHEMAS
          if s in text]
    if not new_schemas_allowed:
        v += ["a new schema literal: %s" % s for s in NEW_SCHEMAS if s in text]
    return v


def succession_violations(rel, present, law, sites=None):
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
    if authority.labels(sites) != ("VB7",):
        v.append("the sites are not VB7's alone")
    v += succession_table_violations(law)
    return v


def _is(pattern, value):
    """A whole-string match of an explicit string: never str(value), and
    never a match that stops before a terminal newline."""
    return isinstance(value, str) and pattern.fullmatch(value) is not None


def variants(visible):
    ase = visible["admissible_source_evidence"]
    return (ase["variant_a"], ase["variant_b"])


def text_digest(t):
    return "sha256:" + hashlib.sha256(t.encode("utf-8")).hexdigest()


def construction_record_violations(raw, visible, authored_class,
                                   authoring_commitment):
    """Part E's closed shape and field law over one construction record's
    exact bytes, bound to its visible case, the case's authored class and
    its authoring commitment."""
    try:
        rec = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return ["not a JSON object"]
    if not isinstance(rec, dict):
        return ["not a JSON object"]
    v = []
    if envelope.canonical_bytes(rec) != raw:
        v.append("not canonical bytes")
    if set(rec) != CONSTRUCTION_FIELDS:
        return v + ["field set: %s" % sorted(set(rec) ^ CONSTRUCTION_FIELDS)]
    if rec["schema"] != CONSTRUCTION_SCHEMA:
        v.append("schema")
    if not _is(envelope.CASE_ID_RE, rec["case_id"]):
        v.append("case_id shape")
    elif rec["case_id"] != visible["case_id"]:
        v.append("case_id does not bind the visible case")
    if not isinstance(rec["method"], str) or rec["method"] not in ADMITS:
        v.append("unknown method")
    elif authored_class not in ADMITS[rec["method"]]:
        v.append("method not admitted for the authored class")
    seed = rec["family_seed_sha256"]
    if seed is not None:
        if not _is(envelope.SHA_FIELD_RE, seed):
            v.append("family seed shape")
        elif seed not in {text_digest(t) for t in variants(visible)}:
            v.append("the family seed is carried by neither variant")
    if not (isinstance(rec["method_note"], str)
            and rec["method_note"].strip()):
        v.append("the method note is empty")
    rv = rec["reviewer_visible_sha256"]
    if not _is(envelope.SHA_FIELD_RE, rv):
        v.append("visible digest shape")
    elif rv != envelope.sha256_bytes(envelope.canonical_bytes(visible)):
        v.append("the visible digest does not bind")
    ac = rec["authoring_commitment_sha256"]
    if not _is(envelope.SHA_FIELD_RE, ac):
        v.append("authoring commitment shape")
    elif ac != authoring_commitment:
        v.append("the authoring commitment does not bind")
    if not _is(NONCE_RE, rec["construction_nonce"]):
        v.append("nonce shape")
    return v


def construction_manifest_violations(raw, commitment_rows,
                                     construction_bytes_by_id):
    """Part E decision 19: closed shape, canonical bytes, lexical order,
    uniqueness, and one-to-one binding to the commitment manifest's rows and
    to the exact construction-record bytes, in every direction."""
    try:
        obj = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return ["not a JSON object"]
    if not isinstance(obj, dict):
        return ["not a JSON object"]
    v = []
    if envelope.canonical_bytes(obj) != raw:
        v.append("not canonical bytes")
    if set(obj) != {"schema", "rows"}:
        return v + ["outer shape"]
    if obj["schema"] != CONSTRUCTION_MANIFEST_SCHEMA:
        v.append("schema")
    rows = obj["rows"] if isinstance(obj["rows"], list) else []
    if not rows:
        v.append("no rows")
    ids = []
    for r in rows:
        if not isinstance(r, dict) or set(r) != CONSTRUCTION_ROW_FIELDS:
            v.append("row shape")
            continue
        if not _is(envelope.CASE_ID_RE, r["case_id"]):
            v.append("row case_id shape")
            continue
        ids.append(r["case_id"])
        if not _is(envelope.SHA_FIELD_RE, r["construction_commitment_sha256"]):
            v.append("row commitment shape")
        elif r["case_id"] in construction_bytes_by_id and \
                r["construction_commitment_sha256"] != envelope.sha256_bytes(
                    construction_bytes_by_id[r["case_id"]]):
            v.append("row commitment does not reproduce")
    if len(ids) != len(set(ids)):
        v.append("duplicate case_id")
    if ids != sorted(ids):
        v.append("rows not in lexical case_id order")
    bound = [r.get("case_id") for r in commitment_rows]
    if sorted(set(ids)) != sorted(set(bound)) or len(ids) != len(bound):
        v.append("not one-to-one with the commitment manifest")
    if set(ids) != set(construction_bytes_by_id):
        v.append("not one-to-one with the construction records")
    return v


def family_violations(visible_by_id, records_by_id):
    """Part D decision 14: any variant text two or more cases share is one
    declared family seed of every case carrying it; a family has two or
    three members, each carrying the seed as one variant."""
    v = []
    if set(visible_by_id) != set(records_by_id):
        v.append("records do not match cases")
    carriers = {}
    for cid, vis in visible_by_id.items():
        for t in set(variants(vis)):
            carriers.setdefault(text_digest(t), set()).add(cid)
    declared = {}
    for cid, rec in records_by_id.items():
        seed = rec.get("family_seed_sha256")
        if seed is None:
            continue
        if not _is(envelope.SHA_FIELD_RE, seed):
            v.append("family seed shape")
            continue
        declared.setdefault(seed, set()).add(cid)
    for digest, cids in carriers.items():
        if len(cids) >= 2 and declared.get(digest) != cids:
            v.append("shared text is not one family seed declared by every "
                     "case carrying it")
    for seed, cids in declared.items():
        if not 2 <= len(cids) <= 3:
            v.append("a family of %d" % len(cids))
        if not cids <= carriers.get(seed, set()):
            v.append("a declared seed is carried by no variant of a member")
    return v


def membership_violations(bound, steps, foreign=frozenset()):
    """Decision 25's chain: the bound identity set is present, well formed,
    distinct and of this corpus only; then every derived step - in order,
    packet inputs, register rows, existence check, reproduction set and
    reveal set - equals it exactly, with no duplicate."""
    if not bound:
        return ["the bound set is empty"]
    if any(not _is(envelope.CASE_ID_RE, i) for i in bound):
        return ["the bound set has a malformed identity"]
    v = []
    if len(bound) != len(set(bound)):
        v.append("the bound set has a duplicate")
    if set(bound) & set(foreign):
        v.append("the bound set draws in another corpus")
    for name, ids in steps:
        if any(not _is(envelope.CASE_ID_RE, i) for i in ids):
            v.append("%s: malformed identity" % name)
            continue
        if len(ids) != len(set(ids)):
            v.append("%s: duplicate" % name)
        if set(ids) != set(bound):
            v.append("%s: not exactly the bound set" % name)
    return v


def staged_absence_violations(tracked, exists, entries, holders,
                              corpus=None, session=None):
    """VL10's present-state gates: no later home, record, registry entry or
    new schema literal before its own landing. Succeeded at the corpus
    landing: `corpus` is that landing's admitted path set - the two
    manifests, the corpus record and the case files its commitment manifest
    binds - or None for the state before it. Succeeded at the session
    landing: `session` is that landing's admitted path set - the
    register and the session record - or None for the state before it."""
    admitted = frozenset(corpus or ()) | frozenset(session or ())
    landed = corpus is not None
    held = session is not None
    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())
           | (SESSION_IDS if held else frozenset()))
    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed
                                    else set())
    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())
                  | ({VALIDATION_HOMES[1]} if held else set()))
    v = []
    homes = tuple(h + "/" for h in VALIDATION_HOMES)
    v += ["a later home is tracked: %s" % p for p in tracked
          if p.startswith(homes) and p not in admitted]
    v += ["a later record is tracked: %s" % p for p in tracked
          if p in LATER_RECORDS and p not in admitted]
    v += ["a later home or record exists on disk: %s" % p
          for p in VALIDATION_HOMES + LATER_RECORDS
          if exists(p) and p not in on_disk_ok]
    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:
        v.append("the W8-D4 entries are not exactly the admitted set")
    v += ["a later registry entry exists: %s" % e["id"] for e in entries
          if e["id"] in LATER_IDS - ids]
    v += ["a new schema literal is carried outside its admitted holders: "
          "%s" % p for p in holders if p not in holders_ok]
    return v


def corpus_admitted(read):
    """The corpus landing's admitted paths, from its commitment manifest as
    `read` gives it: the committed object once that landing exists."""
    rows = json.loads(read(CORPUS_MANIFEST))["rows"]
    return ({CORPUS_MANIFEST, CONSTRUCTION_MANIFEST, CORPUS_RECORD}
            | {"%s/%s.json" % (VALIDATION_HOMES[0], r["case_id"])
               for r in rows})

def schema_holders(tracked, read):
    out = []
    for p in tracked:
        try:
            data = read(p)
        except OSError:
            continue
        if any(s.encode("utf-8") in data for s in NEW_SCHEMAS):
            out.append(p)
    return out


def law_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and LAW_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (LAW_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "the original corpus's retained records stay sealed. "
         + fill(LAW_STATUS[state]) + " **No divergence is diagnosed"),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + LAW_ROW + fill(ROW_PREFIX[state]) + LAW_ROW_BODY
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


def expected_registry(base_text, law_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + authority._indent(json.dumps(new_entry(state, date, law_hash),
                                           indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    return " ".join([LAW_ROW, LAW_ROW_BODY] + list(LAW_STATUS.values()))


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def census_violations(paths, law):
    v = []
    if paths != set(FIXED_CENSUS):
        v.append("the landing's paths are not exactly the census")
    lines = [l for l in law.split("\n")
             if "**This landing's census is exactly five paths:**" in l]
    if len(lines) != 1:
        v.append("the law does not state the census exactly once")
    elif set(re.findall(r"`([^`]+)`", lines[0])) != set(FIXED_CENSUS):
        v.append("the law names a different census")
    return v


def sentinel_world():
    """Three labelled mechanics sentinels: two sharing one seed text as a
    declared family, one singleton. Each visible object passes the published
    visible validator; nothing here is a case."""
    t1, t2, t3, t4, t5 = SENTINEL_TEXTS
    visibles = [envelope.build_review_case(t1, t2),
                envelope.build_review_case(t1, t3),
                envelope.build_review_case(t4, t5)]
    seed = text_digest(t1)
    world = {}
    for vis, cls, method, fam in ((visibles[0], "A", "mutation", seed),
                                  (visibles[1], "B", "mutation", seed),
                                  (visibles[2], "C", "under_specified", None)):
        auth = envelope._sentinel_record(cls, vis["case_id"])
        auth["reviewer_visible_sha256"] = envelope.sha256_bytes(
            envelope.canonical_bytes(vis))
        auth_commitment = envelope.sha256_bytes(envelope.canonical_bytes(auth))
        rec = {"schema": CONSTRUCTION_SCHEMA, "case_id": vis["case_id"],
               "method": method, "family_seed_sha256": fam,
               "method_note": "mechanics sentinel - not a case",
               "reviewer_visible_sha256": auth["reviewer_visible_sha256"],
               "authoring_commitment_sha256": auth_commitment,
               "construction_nonce": SENTINEL_NONCE}
        world[vis["case_id"]] = (vis, cls, auth_commitment, rec)
    return world


def published_identities():
    ids = set()
    for rel in (D2_MANIFEST, supplement.MANIFEST):
        ids |= {r["case_id"] for r in
                json.loads(committed(BASELINE, rel))["rows"]}
    return frozenset(ids)


# ------------------------------------------------------------------ proofs
class VL1_Carriage(unittest.TestCase):
    def test_vl1_question_rules_tokens_method_table_and_statements(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, LAW)
        nine = nine_rules()
        with self.subTest(fact="the law carries everything VL1 requires"):
            self.assertEqual(carriage_violations(text, nine), [])
        for name, mutant in {
                "a removed statement": text.replace(REQUIRED_VL[3], "", 1),
                "a duplicated statement": text + "\n" + REQUIRED_VL[4] + "\n",
                "an altered nine-rule block": text.replace(
                    nine, nine.replace("≠", "=", 1), 1),
                "an altered review question": text.replace(
                    packet.REVIEW_QUESTION, packet.REVIEW_QUESTION.upper(),
                    1),
                "a dropped token": text.replace("`review_inconclusive`",
                                                "review_inconclusive")
                }.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(carriage_violations(mutant, nine))
        with self.subTest(control="every withdrawn wording is detected"):
            self.assertEqual([s for s in WITHDRAWN if not carriage_violations(
                text + "\n" + s + "\n", nine)], [])


class VL2_Withholding(unittest.TestCase):
    def test_vl2_the_law_withholds_every_later_act(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, LAW)
        with self.subTest(fact="every later act is withheld"):
            self.assertEqual(withholding_violations(text), [])
        for name, mutant in {
                "a removed withholding": text.replace("diagnoses nothing", ""),
                "a weakened withholding": text.replace(
                    "No count by method, family or class is published",
                    "A count by method may be published")}.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(withholding_violations(mutant))


class VL3_NoExposure(unittest.TestCase):
    def test_vl3_no_identity_digest_label_schema_or_count(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, LAW)
        reg = json.loads(snapshot_text(commit, REGISTRY))
        role = " ".join(e["role"] + " " + e["title"] for e in reg["entries"]
                        if e["id"] == "ADR-0060")
        row = succession_row()
        for name, surface, exempt, new_ok in (
                ("law", text, (row,), True),
                ("registry role and title", role, (), False),
                ("board wording this landing adds", added_board_wording(), (),
                 False)):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(exposure_violations(surface, exempt, new_ok),
                                 [])
        with self.subTest(fact="no token on the registry role or the board "
                               "wording"):
            for surface in (role, added_board_wording()):
                self.assertEqual([t for t in packet.TOKENS if t in surface],
                                 [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([s for s in PUBLISHED_SCHEMAS if s in src], [])
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "a planted case identity": text + "\nW8-C-" + "a" * 64 + "\n",
                "a planted digest": text + "\n" + "b" * 64 + "\n",
                "a planted reserved label": text + "\n"
                + sorted(corpus.RESERVED_FIELDS)[0] + "\n",
                "a planted count": text + "\n`no_governance_delta`: 17\n",
                "a planted published schema literal": text + "\n"
                + calibration.REGISTER_SCHEMA + "\n",
                "an unknown succession row": text.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a trusted pin copied outside the table": text + "\n`%s`\n"
                % POSTIMAGE[OPENING][0]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(exposure_violations(mutant, (row,), True))
        with self.subTest(control="a new schema literal outside the law is "
                                  "refused"):
            self.assertTrue(exposure_violations(
                LAW_ROW_BODY + " " + CONSTRUCTION_SCHEMA))


class VL4_MethodLaw(unittest.TestCase):
    def test_vl4_admission_table_is_exactly_decision_6(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_text(commit, LAW)
        brief = _lf(committed(BASELINE, BRIEF)).decode("utf-8")
        with self.subTest(fact="the law's table is exactly the trusted rows"):
            self.assertEqual(closed_table_violations(
                part_lines(text, "B"),
                [METHOD_HEADER, METHOD_RULE] + method_rows(), "Part B"), [])
        with self.subTest(fact="the classes equal the accepted brief's"):
            self.assertEqual(brief_method_classes(brief),
                             {name: classes
                              for _, name, classes in METHOD_TABLE})
        with self.subTest(fact="admission agrees with the accepted brief on "
                               "every pairing and refuses the rest"):
            brief_classes = brief_method_classes(brief)
            for label, name, _ in METHOD_TABLE:
                for c in "ABC":
                    self.assertEqual(c in ADMITS[label],
                                     c in brief_classes[name].split(", "))
            self.assertNotIn("A", ADMITS["under_specified"])
            self.assertNotIn("C", ADMITS["governance_preserving_paraphrase"])
        sec = part_lines(text, "B")
        rows = method_rows()
        for name, mutant in {
                "an extra class": [l.replace("| C |", "| A, C |")
                                   if l == rows[3] else l for l in sec],
                "a dropped row": [l for l in sec if l != rows[2]],
                "an extra row": [x for l in sec for x in
                                 ([l, "| `hybrid` | Hybrids | A |"]
                                  if l == rows[-1] else [l])],
                "an indented row": ["  " + l if l == rows[0] else l
                                    for l in sec],
                "a non-blank line under the table": [
                    x for l in sec for x in
                    ([l, "A stray line."] if l == rows[-1] else [l])]
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, sec)
                self.assertTrue(closed_table_violations(
                    mutant, [METHOD_HEADER, METHOD_RULE] + rows, "Part B"))


class VL5_ConstructionRecord(unittest.TestCase):
    def test_vl5_closed_shape_and_field_law_over_sentinels(self):
        world = sentinel_world()
        for cid, (vis, cls, ac, rec) in sorted(world.items()):
            with self.subTest(fact="a lawful sentinel record passes",
                              method=rec["method"]):
                self.assertEqual(envelope.review_case_violations(vis), [])
                self.assertEqual(construction_record_violations(
                    envelope.canonical_bytes(rec), vis, cls, ac), [])
        vis, cls, ac, rec = next(w for w in world.values()
                                 if w[3]["family_seed_sha256"])

        def mutated(**changes):
            r = dict(rec)
            for k, val in changes.items():
                if val is KeyError:
                    del r[k]
                else:
                    r[k] = val
            return envelope.canonical_bytes(r)
        canonical = envelope.canonical_bytes(rec)
        for name, (raw, klass) in {
                "an extra field": (mutated(extra="x"), cls),
                "a missing field": (mutated(method_note=KeyError), cls),
                "a wrong schema": (mutated(schema="w8-other-v1"), cls),
                "an unknown method": (mutated(method="hybrid"), cls),
                "a method not admitted for the class": (
                    mutated(method="under_specified"), cls),
                "a family seed carried by neither variant": (
                    mutated(family_seed_sha256=text_digest("unrelated")), cls),
                "a malformed family seed": (
                    mutated(family_seed_sha256="sha256:XYZ"), cls),
                "an empty method note": (mutated(method_note="  "), cls),
                "a malformed nonce": (
                    mutated(construction_nonce="A" * 64), cls),
                "an unbound case identity": (
                    mutated(case_id="W8-C-" + "f" * 64), cls),
                "an unbound visible digest": (
                    mutated(reviewer_visible_sha256="sha256:" + "1" * 64), cls),
                "an unbound authoring commitment": (
                    mutated(authoring_commitment_sha256="sha256:" + "2" * 64),
                    cls),
                "non-canonical bytes": (
                    json.dumps(rec, indent=2).encode("utf-8"), cls),
                "a class the method does not admit": (canonical, "Z"),
                "a nonce followed by a newline (the r1 finding)": (
                    mutated(construction_nonce=SENTINEL_NONCE + "\n"), cls),
                "a non-string nonce": (mutated(construction_nonce=7), cls),
                "a case identity followed by a newline": (
                    mutated(case_id=rec["case_id"] + "\n"), cls),
                "a non-string case identity": (mutated(case_id=17), cls),
                "a non-string method": (mutated(method=["mutation"]), cls),
                "a family seed followed by a newline": (
                    mutated(family_seed_sha256=rec["family_seed_sha256"]
                            + "\n"), cls),
                "a visible digest followed by a newline": (
                    mutated(reviewer_visible_sha256=rec[
                        "reviewer_visible_sha256"] + "\n"), cls),
                "an authoring commitment followed by a newline": (
                    mutated(authoring_commitment_sha256=ac + "\n"), cls)
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(construction_record_violations(
                    raw, vis, klass, ac))


class VL6_ConstructionManifest(unittest.TestCase):
    def test_vl6_closed_manifest_bound_one_to_one(self):
        world = sentinel_world()
        ids = sorted(world)
        record_bytes = {cid: envelope.canonical_bytes(world[cid][3])
                        for cid in ids}
        commitment_rows = [{"case_id": cid} for cid in ids]
        rows = [{"case_id": cid,
                 "construction_commitment_sha256":
                     envelope.sha256_bytes(record_bytes[cid])} for cid in ids]

        def manifest(rows_, schema=CONSTRUCTION_MANIFEST_SCHEMA, **extra):
            obj = {"schema": schema, "rows": rows_}
            obj.update(extra)
            return envelope.canonical_bytes(obj)
        with self.subTest(fact="a lawful sentinel manifest passes"):
            self.assertEqual(construction_manifest_violations(
                manifest(rows), commitment_rows, record_bytes), [])
        for name, (raw, crows, recs) in {
                "a duplicate row": (manifest(rows + rows[:1]),
                                    commitment_rows, record_bytes),
                "an orphan row": (manifest(rows), commitment_rows[1:],
                                  record_bytes),
                "a missing row": (manifest(rows[1:]), commitment_rows,
                                  record_bytes),
                "unsorted rows": (manifest(list(reversed(rows))),
                                  commitment_rows, record_bytes),
                "an extra row field": (manifest(
                    [dict(rows[0], note="x")] + rows[1:]), commitment_rows,
                    record_bytes),
                "an extra outer field": (manifest(rows, extra="x"),
                                         commitment_rows, record_bytes),
                "a wrong schema": (manifest(rows, schema="w8-other-v1"),
                                   commitment_rows, record_bytes),
                "a commitment that does not reproduce": (
                    manifest(rows), commitment_rows,
                    dict(record_bytes, **{ids[0]: b"altered\n"})),
                "a record with no row": (
                    manifest(rows[1:]), commitment_rows[1:], record_bytes),
                "non-canonical bytes": (
                    json.dumps({"schema": CONSTRUCTION_MANIFEST_SCHEMA,
                                "rows": rows}, indent=1).encode("utf-8"),
                    commitment_rows, record_bytes),
                "a row identity followed by a newline": (manifest(
                    [dict(rows[0], case_id=ids[0] + "\n")] + rows[1:]),
                    commitment_rows, record_bytes),
                "a row commitment followed by a newline": (manifest(
                    [dict(rows[0], construction_commitment_sha256=rows[0][
                        "construction_commitment_sha256"] + "\n")]
                    + rows[1:]), commitment_rows, record_bytes),
                "a non-string row identity": (manifest(
                    [dict(rows[0], case_id=17)] + rows[1:]), commitment_rows,
                    record_bytes)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(construction_manifest_violations(
                    raw, crows, recs))


class VL7_Families(unittest.TestCase):
    def test_vl7_family_rule_over_sentinels(self):
        world = sentinel_world()
        visible = {cid: w[0] for cid, w in world.items()}
        records = {cid: w[3] for cid, w in world.items()}
        with self.subTest(fact="a declared family of two and a singleton "
                               "pass"):
            self.assertEqual(family_violations(visible, records), [])
        fam = sorted(cid for cid, r in records.items()
                     if r["family_seed_sha256"])
        single = next(cid for cid, r in records.items()
                      if not r["family_seed_sha256"])
        t1 = SENTINEL_TEXTS[0]
        # Two more cases carrying the declared seed, each other text unique:
        # exactly four carriers of one seed.
        more = [envelope.build_review_case(t1, SENTINEL_TEXTS[i] + " x")
                for i in (1, 2)]
        for name, (vis, recs) in {
                "undeclared shared text": (visible, dict(
                    records, **{fam[0]: dict(records[fam[0]],
                                             family_seed_sha256=None)})),
                "a family of one": (visible, dict(
                    records, **{single: dict(
                        records[single],
                        family_seed_sha256=text_digest(SENTINEL_TEXTS[3]))})),
                "a family of four": (
                    dict(visible, **{c["case_id"]: c for c in more}),
                    dict(records, **{c["case_id"]: dict(
                        records[fam[0]], case_id=c["case_id"])
                        for c in more})),
                "a seed carried by no member's variant": (visible, dict(
                    records, **{fam[0]: dict(
                        records[fam[0]],
                        family_seed_sha256=text_digest("unrelated"))})),
                "records that do not match the cases": (
                    visible, {k: records[k] for k in fam}),
                "a non-string family seed": (visible, dict(
                    records, **{fam[0]: dict(records[fam[0]],
                                             family_seed_sha256=["x"])}))
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(family_violations(vis, recs))


class VL8_Membership(unittest.TestCase):
    def test_vl8_the_membership_chain_over_sentinel_identities(self):
        bound = sorted(sentinel_world())
        foreign = published_identities()
        names = ("packet inputs", "register rows", "existence check",
                 "reproduction set", "reveal set")
        lawful = [(n, list(bound)) for n in names]
        with self.subTest(fact="every step equal to the bound set passes"):
            self.assertTrue(foreign)
            self.assertEqual(membership_violations(bound, lawful, foreign),
                             [])
        some_foreign = sorted(foreign)[0]
        for name, (b, steps) in {
                "an empty bound set": ([], lawful),
                "a duplicate in the bound set": (bound + bound[:1], lawful),
                "a malformed bound identity": (bound + ["W8-C-short"], lawful),
                "a foreign identity in the bound set": (
                    bound + [some_foreign], lawful),
                "a mixed bound set": (bound[:1] + [some_foreign], lawful),
                "a malformed identity followed by a newline, propagated to "
                "every step (the r1 finding)": (
                    [i + "\n" for i in bound],
                    [(n, [i + "\n" for i in bound]) for n in names]),
                "a non-string bound identity": (bound + [17], lawful)
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(membership_violations(b, steps, foreign))
        for i, step in enumerate(names):
            for name, ids in {"missing": bound[1:],
                              "extra": bound + [some_foreign],
                              "duplicate": bound + bound[:1],
                              "malformed": [i + "\n" for i in bound]}.items():
                steps = list(lawful)
                steps[i] = (step, ids)
                with self.subTest(control="a %s %s is refused" % (name,
                                                                   step)):
                    self.assertTrue(membership_violations(bound, steps,
                                                          foreign))


class VL9_VB7Succession(unittest.TestCase):
    def test_vl9_the_vb7_succession_is_exact(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        law = snapshot_text(commit, LAW)
        present = snapshot_text(commit, OPENING)
        with self.subTest(baseline_object=PREIMAGE[OPENING][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + OPENING)
                             .strip(), PREIMAGE[OPENING][2])
        self.assertEqual(succession_violations(OPENING, present, law), [])
        with self.subTest(fact="the post-image is the reviewed object"):
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[OPENING][1])
        with self.subTest(fact="the succeeded module keeps the D4-A entry "
                               "set at its landing commit"):
            self.assertEqual(opening.D4A_LANDING, BASELINE)
            at_landing = json.loads(committed(BASELINE, REGISTRY))["entries"]
            self.assertEqual(opening.d4_entry_set(at_landing),
                             opening.D4_ENTRIES)
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[OPENING][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[OPENING] + (("VB7", first,
                                       first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(OPENING, text, law,
                                                      table))
        row = succession_row()
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "an unknown source row": law.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a duplicate authorised row": law.replace(
                    row + "\n", row + "\n" + row + "\n", 1),
                "an extra field": law.replace(row, row + " extra |", 1),
                "an indented row": law.replace(row, "  " + row, 1),
                "a row without its opening pipe": law.replace(row, row[2:],
                                                              1),
                "a non-blank line under the table": law.replace(
                    row + "\n", row + "\nA stray line.\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, law)
                self.assertTrue(succession_table_violations(mutant))


class VL10_StagedAbsences(unittest.TestCase):
    def test_vl10_no_later_artefact_before_its_own_landing(self):
        # Present-state gates, each succeeded only by the later landing
        # ADR-0060 Part J names. Succeeded at the corpus landing and again at
        # the session landing: each former state stays proven at its own
        # landing commit, and the present admits exactly the landed
        # artefacts.
        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()
        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[
            "entries"]
        before_holders = schema_holders(
            before, lambda p: committed(D4B_LANDING, p))
        with self.subTest(fact="nothing later existed at the D4-B landing"):
            self.assertEqual(staged_absence_violations(
                before, lambda p: False, before_entries, before_holders), [])
            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))
        at_corpus = _git("ls-tree", "-r", "--name-only", D4C_LANDING).split()
        corpus_entries = json.loads(committed(D4C_LANDING, REGISTRY))[
            "entries"]
        corpus_holders = schema_holders(
            at_corpus, lambda p: committed(D4C_LANDING, p))
        corpus = corpus_admitted(lambda rel: committed(D4C_LANDING, rel))
        with self.subTest(fact="nothing of the session existed at the corpus "
                               "landing"):
            self.assertEqual(staged_absence_violations(
                at_corpus, lambda p: False, corpus_entries, corpus_holders,
                corpus), [])
            self.assertEqual(sorted(corpus_holders), sorted(
                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))
        tracked = _git("ls-files").split()
        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]

        def exists(p):
            return (ROOT / p).exists()

        def read(p):
            return (ROOT / p).read_bytes()
        holders = schema_holders(tracked, read)
        session = {SESSION_REGISTER, SESSION_RECORD}
        with self.subTest(fact="exactly the corpus and session landings' "
                               "artefacts are admitted"):
            self.assertEqual(staged_absence_violations(
                tracked, exists, entries, holders, corpus, session), [])
        with self.subTest(fact="the new schema literals live in the law, "
                               "this module and the construction manifest"):
            self.assertEqual(sorted(holders), sorted(
                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))
        planted_entry = dict(entries[-1], id="W8-D4-VRC", deliverable="W8-D4")
        for name, args in {
                "an unbound case file": (
                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,
                    entries, holders, corpus, session),
                "an extra file in the register home": (
                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,
                    entries, holders, corpus, session),
                "a reveal-home path": (
                    tracked + [VALIDATION_HOMES[2] + "/authoring/x.json"],
                    exists, entries, holders, corpus, session),
                "a validation record on disk": (
                    tracked, lambda p: p == LATER_RECORDS[2], entries,
                    holders, corpus, session),
                "a premature validation-record entry": (
                    tracked, exists, entries + [planted_entry], holders,
                    corpus, session),
                "a schema literal elsewhere": (
                    tracked, exists, entries, holders + [BOARD], corpus,
                    session),
                "the corpus artefacts without their landing": (
                    tracked, exists, entries, holders, None, session),
                "the session artefacts without their landing": (
                    tracked, exists, entries, holders, corpus, None)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(staged_absence_violations(*args))

class VL11_RegistrationRegistryBoard(unittest.TestCase):
    def test_vl11_registered_and_changed_exactly(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        law = snapshot_text(commit, LAW)
        state, date, v = law_state(law)
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
            self.assertIn(recovery.R9_REVEAL, board)
        reg = snapshot_text(commit, REGISTRY)
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(
                reg_pre, _sha(law.encode("utf-8")), state, date))
        e = {x["id"]: x for x in json.loads(reg)["entries"]}.get("ADR-0060")
        with self.subTest(fact="registered at W8-D4 with matching hash and "
                               "status"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]),
                             (LAW, "adr", "W8", "W8-D4"))
            self.assertEqual(e["content_hash"], _sha(law.encode("utf-8")))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            if commit is None:
                self.assertEqual(e["content_hash"], lf_hash(ROOT / LAW))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, _sha(law.encode("utf-8")), other, "2000-01-01"))
            wrong, _ = authority.apply_sites(board_pre,
                                             board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)


class VL12_Census(unittest.TestCase):
    def test_vl12_census_is_exactly_five_paths(self):
        commit, problems = l6_snapshot()
        self.assertEqual(problems, [])
        self.assertEqual(len(FIXED_CENSUS), 5)
        paths = landing_paths(commit)
        law = snapshot_text(commit, LAW)
        with self.subTest(fact="the census is exactly five paths, as the "
                               "law names it"):
            self.assertEqual(census_violations(paths, law), [])
        for name, (p, t) in {
                "an extra path": (paths | {"docs/phases/placeholder.md"}, law),
                "a missing path": (paths - {REGISTRY}, law),
                "a law naming another path": (paths, law.replace(
                    "`%s`" % REGISTRY, "`governance/placeholder.json`"))
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual((p, t), (paths, law))
                self.assertTrue(census_violations(p, t))


if __name__ == "__main__":
    unittest.main()
