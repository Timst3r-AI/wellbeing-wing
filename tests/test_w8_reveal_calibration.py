"""W8-D3-D — reveal, calibration comparison and completion proofs
(W8-D3-CCR, RC1–RC12).

The reveal landing of W8-D3 on the session corpus that ADR-0059 binds: the
exact retained bytes of the supplementary corpus's twelve withheld authoring
records, published after every commitment reproduced and the candidate
copies scanned clean; the case-level comparison of each fixed human token
with its authored intended token as agreement or divergence; and the two
permitted count kinds, each with its statement. Prepared over the effective
W8-HAC correction, with the session corpus still bound to the supplementary
authoring landing. This module proves the reveal home's closure and exact
bytes, every record's validity and binding, the validation chain through the
reveal, the comparison and counts, and the exact transformations of
everything this landing changes, each with planted-mutant or negative
controls.

THIS MODULE READS NO CUSTODY. It reads the revealed records only at their
published reveal home - before the first commit exactly as written,
unconverted, and afterwards as committed objects - and never names, lists or
reaches a custody location. It holds no case identity, schema literal or
disposition token as a literal.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any human token or authored intended token is right;
that an authored intended token is an answer key - it is a construction
hypothesis; why any case diverged; anything about the reviewer; the absence
of influence or semantic independence; any rate, score, grade or readiness;
that any model was contacted; or that W8-D4 through W8-D7 may open.
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

# The immutable session-corpus commit (ADR-0059 decision 9) and this
# landing's sole parent, the effective W8-HAC correction, from which every
# pre-image below is read.
CORPUS = "83253039ec274a2496b37b618949fd00d3cd7c8e"
BASELINE = "317c0ba9de76853d454774085cdf18f3a638c02f"

HOME = supplement.HOME
MANIFEST = supplement.MANIFEST
ORIGINAL_MANIFEST = supplement.ORIGINAL_MANIFEST
REVEAL_HOME = "governance/discriminating-reveal"
REGISTER = "governance/discriminating-review/W8-D3-disposition-register.json"
SESSION_RECORD = "docs/phases/W8-D3-human-disposition-record.md"
RECORD = "docs/phases/W8-D3-calibration-completion-record.md"
SELF_REL = "tests/test_w8_reveal_calibration.py"
ENVELOPE = "tests/test_w8_discriminating_instrument_envelope.py"
CORPUS_MODULE = "tests/test_w8_discriminating_instrument_corpus.py"
CALIBRATION = "tests/test_w8_calibration_law.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
SUPPLEMENT = "tests/test_w8_supplementary_corpus.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
ADR59 = "docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md"
SUCCEEDED = (ENVELOPE, CORPUS_MODULE, CALIBRATION, RECOVERY, SUPPLEMENT)
FIXED_CENSUS = frozenset({RECORD, SELF_REL, REGISTRY, BOARD} | set(SUCCEEDED))
TOTAL = 12
# The D3-C session landing's fixed bytes: the dispositions are fixed.
REGISTER_PIN = ("sha256:3a1846c02434739c641c58f6428f6b7da4bab2e6a3b24e6b8bff4b"
                "4337df2b5a")
SESSION_RECORD_PIN = ("sha256:f438b825e18b6a0e625bfd8079b02d1350594f46e65aa30"
                      "7f4bddb12f2fddd3e")

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    ENVELOPE: ("envelope module",
               "sha256:e7e80df8dbad8397574b9558a3892ac638e16e0d3549e2662e6181a55bb6944e",
               "6803b82f840a41dc883875bd16c6a97eece3a22d"),
    CORPUS_MODULE: ("corpus module",
                    "sha256:7e9a5e7d7101c33fa3a79bf5979411b8c8a1da989731fcdbd0ca911766e22698",
                    "a4efee0a1d18f4c96869ebdec52e9fd03dbddac4"),
    CALIBRATION: ("disposition-law module",
                  "sha256:448e1aa056a9ce176d7ae1b1856bb6eb459b8e1180fc0eae341419c5c19dc328",
                  "e1ac9846f30318b0f991b434661cda7f955c1922"),
    RECOVERY: ("session-recovery module",
               "sha256:8934a5248504228a0950f5afedc523a377e063746d3e18e37dced914855219ea",
               "b8a6acabc7c43b8ef8985d1ab9e7669b404204a6"),
    SUPPLEMENT: ("supplement module",
                 "sha256:4a810d1be35c82f556362a9497624174351ce81d3e90b9241b3f88b116fc833e",
                 "ab962f36acb888a7779668034f102a26e921f756"),
    REGISTRY: ("registry",
               "sha256:47c5dba4ab392b8c5053aa11dfa7239c0c39aa997da647d211e898000072470f",
               "3266ebe526deccf6db9e1c8431a7f5708193730e"),
    BOARD: ("board",
            "sha256:21613d8748dd8803f95c297d6df5fd2d7baf7a8fd3a84692871def77b1e42d9f",
            "1e225f91e51ce869f1065d5df1b1f5c91e77a7a4"),
}
RECORD_SOURCES = {"`%s`" % rel: rel for rel in SUCCEEDED}

# ------------------------------- the staged successions of decision 27
R9_SENTENCE = "No reveal, comparison, count or calibration exists yet."
R9_REVEAL = "No divergence is diagnosed, explained away or corrected."

SITES = {
    ENVELOPE: (
        ("V12",
         '                 if "W8-C-" in p and not p.startswith(\n'
         '                     ("governance/discriminating-instrument/",\n'
         '                      "governance/discriminating-supplement/"))],'
         ' [])\n',
         '                 if "W8-C-" in p and not p.startswith(\n'
         '                     ("governance/discriminating-instrument/",\n'
         '                      "governance/discriminating-supplement/",\n'
         '                      "governance/discriminating-reveal/"))],'
         ' [])\n'),
        ("V12",
         '        with self.subTest(fact="no tracked file carries the authoring "\n'
         '                               "schema except this module and the law"):\n'
         '            offenders = []\n'
         '            for p in tracked:\n'
         '                if p in ("docs/decisions/0055-w8-case-shape-evidence-"\n'
         '                         "separation-blinding-law.md",\n'
         '                         "tests/test_w8_discriminating_instrument_"\n'
         '                         "envelope.py"):\n'
         '                    continue\n',
         '        with self.subTest(fact="no tracked file carries the authoring "\n'
         '                               "schema except this module, the law "\n'
         '                               "and the reveal home"):\n'
         '            offenders = []\n'
         '            for p in tracked:\n'
         '                if p in ("docs/decisions/0055-w8-case-shape-evidence-"\n'
         '                         "separation-blinding-law.md",\n'
         '                         "tests/test_w8_discriminating_instrument_"\n'
         '                         "envelope.py"):\n'
         '                    continue\n'
         '                # Succeeded at the reveal landing (ADR-0059 Part G\n'
         '                # decision 27): revealed records carry the schema by\n'
         '                # construction, so the reveal home is admitted.\n'
         '                if p.startswith("governance/discriminating-reveal/"):\n'
         '                    continue\n'),
    ),
    CORPUS_MODULE: (
        ("C10",
         '    home_rel = "governance/discriminating-instrument/"\n'
         '    return [p for p in out if p.endswith((".md", ".json"))\n'
         '            and not p.startswith(home_rel)]\n',
         '    home_rel = "governance/discriminating-instrument/"\n'
         '    # Succeeded at the reveal landing (ADR-0059 Part G decision 27):\n'
         '    # revealed records are authoring material about the cases, not\n'
         '    # reuse of them, so the reveal home is outside the guard\'s scope.\n'
         '    reveal_rel = "governance/discriminating-reveal/"\n'
         '    return [p for p in out if p.endswith((".md", ".json"))\n'
         '            and not p.startswith((home_rel, reveal_rel))]\n'),
    ),
    CALIBRATION: (
        ("K12",
         'REGISTER_PATH = REGISTER_HOME + "/W8-D3-disposition-register.json"\n',
         'REGISTER_PATH = REGISTER_HOME + "/W8-D3-disposition-register.json"\n'
         '# K12\'s reveal limb as succeeded at the reveal landing (ADR-0059\n'
         '# Part G decision 27): the reveal home admits exactly the session\n'
         '# corpus.\n'
         'REVEAL_BASELINE = "317c0ba9de76853d454774085cdf18f3a638c02f"\n'
         'SESSION_CORPUS = "83253039ec274a2496b37b618949fd00d3cd7c8e"\n'
         'SESSION_MANIFEST = ("governance/discriminating-supplement/"\n'
         '                    "W8-S1-commitment-manifest.json")\n'),
        ("K12",
         '        with self.subTest(fact="no reveal home is tracked"):\n'
         '            self.assertEqual(in_home(tracked, REVEAL_HOME), [])\n',
         '        with self.subTest(fact="no reveal home was tracked at the "\n'
         '                               "reveal landing\'s baseline"):\n'
         '            self.assertEqual(in_home(listed(REVEAL_BASELINE),\n'
         '                                     REVEAL_HOME), [])\n'
         '        with self.subTest(fact="the reveal home holds exactly the "\n'
         '                               "session corpus\'s identities"):\n'
         '            rows = json.loads(subprocess.run(\n'
         '                ["git", "cat-file", "-p", SESSION_CORPUS + ":"\n'
         '                 + SESSION_MANIFEST], cwd=ROOT, capture_output=True,\n'
         '                check=True).stdout)["rows"]\n'
         '            self.assertEqual(sorted(in_home(tracked, REVEAL_HOME)),\n'
         '                             sorted("%s/%s.json" % (REVEAL_HOME,\n'
         '                                                    r["case_id"])\n'
         '                                    for r in rows))\n'),
    ),
    RECOVERY: (
        ("R7",
         'SESSION_ENTRIES = {"W8-D3-HDR", "W8-D3-DR-01"}\n',
         'SESSION_ENTRIES = {"W8-D3-HDR", "W8-D3-DR-01"}\n'
         '# R7, R8 and R9 as succeeded at the reveal landing (ADR-0059 Part G\n'
         '# decision 27).\n'
         'SESSION_LANDING = "66b6e6ca7e33e5e0fd326d61653a0c13d1679878"\n'
         'REVEAL_BASELINE = "317c0ba9de76853d454774085cdf18f3a638c02f"\n'
         'REVEAL_ENTRIES = {"W8-D3-CCR"}\n'
         'SESSION_CORPUS = "83253039ec274a2496b37b618949fd00d3cd7c8e"\n'
         'SESSION_MANIFEST = ("governance/discriminating-supplement/"\n'
         '                    "W8-S1-commitment-manifest.json")\n'),
        ("R7",
         '        with self.subTest(fact="W8-D3 entries are the brief, the two laws "\n'
         '                               "and the two session entries only"):\n'
         '            self.assertEqual({e["id"] for e in entries\n'
         '                              if e["deliverable"] == "W8-D3"},\n'
         '                             D3_ENTRIES | SESSION_ENTRIES)\n',
         '        with self.subTest(fact="W8-D3 entries were the brief, the two "\n'
         '                               "laws and the two session entries at "\n'
         '                               "the session landing"):\n'
         '            at_session = json.loads(packet.committed_object_bytes(\n'
         '                ROOT, SESSION_LANDING, "governance/registry.json"))[\n'
         '                "entries"]\n'
         '            self.assertEqual({e["id"] for e in at_session\n'
         '                              if e["deliverable"] == "W8-D3"},\n'
         '                             D3_ENTRIES | SESSION_ENTRIES)\n'
         '        with self.subTest(fact="W8-D3 entries are those and the "\n'
         '                               "completion record only"):\n'
         '            self.assertEqual({e["id"] for e in entries\n'
         '                              if e["deliverable"] == "W8-D3"},\n'
         '                             D3_ENTRIES | SESSION_ENTRIES\n'
         '                             | REVEAL_ENTRIES)\n'),
        ("R8",
         '    def test_r8_no_reveal_home(self):\n'
         '        tracked = _git("ls-files").split()\n'
         '        self.assertEqual([p for p in tracked\n'
         '                          if p.startswith(REVEAL_HOME + "/")], [])\n'
         '        self.assertFalse((ROOT / REVEAL_HOME).exists())\n',
         '    def test_r8_reveal_home_holds_exactly_the_session_corpus(self):\n'
         '        # Succeeded at the reveal landing: the former absence stays\n'
         '        # proven at this record\'s own landing commit and at the reveal\n'
         '        # landing\'s baseline; the present admits exactly the session\n'
         '        # corpus\'s identities, tracked and on disk.\n'
         '        for at in (LANDING, REVEAL_BASELINE):\n'
         '            with self.subTest(fact="no reveal home at %s" % at[:12]):\n'
         '                self.assertEqual([p for p in _git(\n'
         '                    "ls-tree", "-r", "--name-only", at).split()\n'
         '                    if p.startswith(REVEAL_HOME + "/")], [])\n'
         '        rows = json.loads(packet.committed_object_bytes(\n'
         '            ROOT, SESSION_CORPUS, SESSION_MANIFEST))["rows"]\n'
         '        expected = sorted("%s/%s.json" % (REVEAL_HOME, r["case_id"])\n'
         '                          for r in rows)\n'
         '        with self.subTest(fact="tracked: exactly the session corpus"):\n'
         '            self.assertEqual(sorted(p for p in _git("ls-files").split()\n'
         '                                    if p.startswith(REVEAL_HOME + "/")),\n'
         '                             expected)\n'
         '        with self.subTest(fact="on disk: exactly the same files"):\n'
         '            self.assertEqual(sorted(REVEAL_HOME + "/" + p.name for p in\n'
         '                                    (ROOT / REVEAL_HOME).iterdir()),\n'
         '                             expected)\n'),
        ("R9",
         'R9_SENTENCE = "' + R9_SENTENCE + '"\n',
         'R9_SENTENCE = "' + R9_SENTENCE + '"\n'
         'R9_REVEAL = "' + R9_REVEAL + '"\n'),
        ("R9",
         '        with self.subTest(fact="the board now states no reveal exists, "\n'
         '                               "in the session landing\'s wording"):\n'
         '            board = _lf_text(BOARD)\n'
         '            self.assertIn(R9_SENTENCE, board)\n'
         '            self.assertNotIn(R9_EARLIER, board)\n',
         '        # Succeeded again at the reveal landing: the session landing\'s\n'
         '        # wording stays proven at the reveal landing\'s baseline.\n'
         '        with self.subTest(fact="the board stated no reveal existed at "\n'
         '                               "the reveal landing\'s baseline"):\n'
         '            self.assertIn(R9_SENTENCE, packet.committed_object_bytes(\n'
         '                ROOT, REVEAL_BASELINE, "docs/phases/README.md")\n'
         '                .decode("utf-8"))\n'
         '        with self.subTest(fact="the board now carries the reveal "\n'
         '                               "landing\'s wording"):\n'
         '            board = _lf_text(BOARD)\n'
         '            self.assertIn(R9_REVEAL, board)\n'
         '            self.assertNotIn(R9_SENTENCE, board)\n'
         '            self.assertNotIn(R9_EARLIER, board)\n'),
    ),
    SUPPLEMENT: (
        ("S10",
         'def other_tracked_texts():\n'
         '    return [p for p in _git("ls-files").split()\n'
         '            if p.endswith((".md", ".json")) and not p.startswith(HOME + "/")]\n',
         'def other_tracked_texts():\n'
         '    # Succeeded at the reveal landing (ADR-0059 Part G decision 27): the\n'
         '    # freshness scope excludes the reveal home, whose records are\n'
         '    # authoring material about these cases, not reuse of them.\n'
         '    return [p for p in _git("ls-files").split()\n'
         '            if p.endswith((".md", ".json"))\n'
         '            and not p.startswith((HOME + "/",\n'
         '                                  "governance/discriminating-reveal/"))]\n'),
    ),
}

# --------------------------------------- board and registry: authorised edits
CCR_LINK = ("([`W8-D3-calibration-completion-record.md`]"
            "(W8-D3-calibration-completion-record.md))")
CCR_STATUS_TAIL = (
    "the reveal of the session corpus's twelve sealed construction "
    "hypotheses as exact retained bytes, after every commitment reproduced "
    "and the candidate copies scanned clean, and the case-level comparison "
    "of each fixed human disposition with its authored intended token as "
    "agreement or divergence, with only the two permitted count kinds; "
    "authored intent stays a construction hypothesis, never an answer key, "
    "and W8-D3 is complete in the accepted sense, effective on publication "
    "and remote verification.")
CCR_STATUS = {
    "draft": ("**A draft calibration completion record, `W8-D3-CCR`, is "
              "before the human reviewer** " + CCR_LINK + ": if accepted, it "
              "would record " + CCR_STATUS_TAIL),
    "accepted": ("**The calibration completion record, `W8-D3-CCR`, is "
                 "accepted** " + CCR_LINK + " — accepted %s: it records "
                 + CCR_STATUS_TAIL),
}
CCR_ROW = ("| W8-D3 — Calibration Completion Record (W8-D3-CCR) | "
           "[`W8-D3-calibration-completion-record.md`]"
           "(W8-D3-calibration-completion-record.md) | ")
CCR_ROW_BODY = (
    "Tier J: **the reveal, the case-level comparison and W8-D3's "
    "completion** — every published commitment of the session corpus "
    "reproduced by hashing the exact retained bytes before any parse; the "
    "exact bytes copied to the reveal home and scanned clean, never the "
    "custody location; only then parsed, each record valid and bound to its "
    "identity, filename, manifest row and visible digest; each fixed human "
    "disposition set beside its authored intended token as agreement or "
    "divergence, with the two permitted count kinds each carrying its "
    "statement. Authored intent is a construction hypothesis, never an "
    "answer key; a divergence is recorded, never explained away, corrected "
    "or attributed to the reviewer. **No disposition amended; no rate, "
    "score or readiness interpretation; the original corpus's retained "
    "records stay sealed; W8-D4 through W8-D7 stay closed.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
HAC_STATUS_CLOSE = ("the reveal landing stays paused before custody access "
                    "until it is effective. ")
BOARD_STATUS_ANCHOR = HAC_STATUS_CLOSE + "**" + R9_SENTENCE
BOARD_ROW_ANCHOR = ("the reveal landing stays paused until this correction "
                    "is effective.** |\n")
CCR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CCR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D3-CCR", "path": RECORD, "type": "phase-record",
    "title": "W8-D3 - Calibration Completion Record",
    "role": (
        "The W8-D3 completion record of landing D3-D on the session corpus "
        "that ADR-0059 binds: every published authoring commitment "
        "reproduced by hashing the exact retained bytes, read-only, before "
        "any parse; the exact bytes copied to the reveal home and their "
        "landing scan clean, the custody location never scanned or named; "
        "only then parsed and bound to identity, filename, manifest row and "
        "visible digest; the twelve revealed records published as exact "
        "retained bytes, bound by W8-S1-CM-01 and not individually "
        "registered. Records the case-level comparison of each fixed human "
        "disposition with its authored intended token as agreement or "
        "divergence, and the two permitted count kinds, each a count of "
        "individual human acts and nothing more. Authored intent is a "
        "construction hypothesis, never an answer key; divergence is "
        "recorded, never diagnosed or corrected here. Moves exactly the "
        "reveal-landing successions of ADR-0059 Part G decision 27, with "
        "proof obligations RC1 to RC12, prepared over the effective proof "
        "correction W8-HAC. No disposition amended; no rate, score or "
        "readiness interpretation; W8-D4 to W8-D7 closed."),
    "depends_on": ["ADR-0057", "ADR-0059", "W8-D3-SCB", "W8-D3-HDR",
                   "W8-D3-DR-01", "W8-S1-SOB", "W8-S1-SCR", "W8-S1-CM-01",
                   "W8-HPC", "W8-HAC", "ADR-0058", "ADR-0054", "ADR-0055",
                   "W8-D2-CBC", "ADR-0056", "W8-AR", "W7-CR"],
}

COMPARISON_HEADER = ("| Case identity | Human token | Authored intended token "
                     "| Relation |")
COMPARISON_SECTION = "## 3. The case-level comparison"
COMPARISON_SEPARATOR = "|---|---|---|---|"
COUNTS_HEADER = "| Kind | Count | Statement |"
COUNTS_SECTION = "## 4. The permitted counts"
COUNTS_SEPARATOR = "|---|---|---|"
CELL_ID = re.compile(r"`(W8-C-[0-9a-f]{64})`")
CELL_WORD = re.compile(r"`([a-z_]+)`")
CELL_COUNT = re.compile(r"0|[1-9][0-9]*")
RATIO = re.compile(r"%|\b\d+\s*/\s*\d+\b|\bpercent\b|\baccuracy\b|"
                   r"\bproportion\b|\bprecision\b|\brecall\b")
REQUIRED_CCR = (
    "An authored intended token is a construction hypothesis, never an "
    "answer key and never a certified correct answer.",
    "A divergence is recorded, never explained away, never corrected and "
    "never attributed to the reviewer;",
    "Revealed material is post-disposition calibration material only and "
    "never becomes evidence for, replaces or amends a disposition.",
    "No percentage, rate, score, grade, ranking, threshold, pass/fail "
    "result, model-performance claim or readiness interpretation is derived, "
    "published or implied.",
    "Every published commitment of the session corpus reproduced by hashing "
    "the exact retained bytes directly, read-only, before any parse",
    "The landing scan ran over exactly the twelve candidate copies and found "
    "nothing; the scanner was never run against the custody location.",
    "Only after that clean scan were the copies parsed.",
    "No retained record of the original corpus was listed, opened, parsed, "
    "hashed, copied or moved by any act of this landing",
    "The location is never named in any surface.",
    "The dispositions were fixed at the session landing's publication, and "
    "none is amended by any route.",
    "No other existing proof moves at this landing.",
    "W8-D4 through W8-D7 remain closed behind their own briefs.",
)


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


def committed(commit, rel):
    return packet.committed_object_bytes(ROOT, commit, rel)


def l4_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added the completion record, whose
    sole parent must be BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the completion record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_text(commit, rel):
    raw = (ROOT / rel).read_bytes() if commit is None else committed(commit,
                                                                     rel)
    return _lf(raw).decode("utf-8")


def revealed_bytes(commit, case_id):
    """Before the first commit, the candidate copy exactly as written,
    unconverted; afterwards, the committed object (ADR-0057 decision 19)."""
    rel = "%s/%s.json" % (REVEAL_HOME, case_id)
    return (ROOT / rel).read_bytes() if commit is None else committed(commit,
                                                                      rel)


def manifest_rows():
    return json.loads(committed(CORPUS, MANIFEST))["rows"]


def manifest_ids():
    return [r["case_id"] for r in manifest_rows()]


def original_ids():
    return [r["case_id"]
            for r in json.loads(committed(CORPUS, ORIGINAL_MANIFEST))["rows"]]


def expected_reveal_paths():
    return sorted("%s/%s.json" % (REVEAL_HOME, c) for c in manifest_ids())


def binding_violations(rows, visible, revealed):
    """Every revealed record: the published withheld-record validator, its
    identity equal to its filename and manifest row, its visible digest equal
    to the row and to the published visible bytes, canonical bytes, and the
    manifest binding in both directions by exact bytes."""
    v = envelope.manifest_binding_violations(rows, visible, revealed)
    for row in rows:
        cid = row["case_id"]
        if cid not in revealed:
            continue
        try:
            rec = json.loads(revealed[cid])
        except ValueError:
            v.append("a revealed record is not JSON")
            continue
        v += envelope.authoring_record_violations(rec)
        v += envelope.cross_binding_violations(json.loads(visible[cid]),
                                               visible[cid], rec)
        if rec.get("case_id") != cid:
            v.append("a revealed identity differs from its filename")
        if rec.get("reviewer_visible_sha256") != row["reviewer_visible_sha256"]:
            v.append("a revealed visible digest differs from its row")
        if revealed[cid] != envelope.canonical_bytes(rec):
            v.append("a revealed record is not in canonical bytes")
    return v


def mechanical_comparison(register, revealed):
    human = {r["case_id"]: r["disposition"] for r in register["rows"]}
    out = []
    for cid in sorted(revealed):
        intended = json.loads(revealed[cid])["intended_disposition"]
        out.append((cid, human[cid], intended,
                    calibration.relation(human[cid], intended)))
    return out


def mechanical_counts(comparison):
    c = calibration.counts([{"disposition": h} for _, h, _, _ in comparison],
                           [rel for _, _, _, rel in comparison])
    return c


def section_lines(text, heading):
    """The lines of one labelled section, up to the next heading; None if
    the heading is missing or repeated."""
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l == heading]
    if len(starts) != 1:
        return None
    out = []
    for line in lines[starts[0] + 1:]:
        if line.startswith("## "):
            break
        out.append(line)
    return out


def closed_table(text, heading, header, separator, width):
    """(rows, violations) for the one table of a labelled section, read
    whole: every delimiter-bearing line of the section - including an
    indented row or one with no opening pipe - and every non-blank line
    adjacent to them must form one contiguous block of exactly the header,
    the separator and body rows of exactly `width` cells. Nothing is
    filtered out: any malformed, surplus, stray or boundary line is a
    violation."""
    section = section_lines(text, heading)
    if section is None:
        return [], ["the section %r is missing or repeated" % heading]
    at = [i for i, line in enumerate(section) if "|" in line]
    if not at:
        return [], ["the section holds no table"]
    start, end = at[0], at[-1] + 1
    while start > 0 and section[start - 1].strip():
        start -= 1
    while end < len(section) and section[end].strip():
        end += 1
    block = section[start:end]
    v = []
    if any(not line.strip() for line in block):
        v.append("the section's table lines are not one contiguous block")
    if block[0] != header:
        v.append("the header line is not exactly the law's")
    if len(block) < 2 or block[1] != separator:
        v.append("the separator line is malformed")
    rows = []
    for line in block[2:]:
        if not (line.startswith("| ") and line.endswith(" |")):
            v.append("a malformed row")
            continue
        cells = line[2:-2].split(" | ")
        if len(cells) != width:
            v.append("a row with %d cells" % len(cells))
            continue
        rows.append(cells)
    return rows, v


def comparison_violations(text, expected):
    """The comparison table, whole: exactly twelve rows in ascending
    identity order, each exactly the four permitted fields with lawful
    tokens and a closed relation, and exactly the mechanical comparison."""
    rows, v = closed_table(text, COMPARISON_SECTION, COMPARISON_HEADER,
                           COMPARISON_SEPARATOR, 4)
    parsed = []
    for cells in rows:
        m = [CELL_ID.fullmatch(cells[0])] + [CELL_WORD.fullmatch(c)
                                             for c in cells[1:]]
        if not all(m):
            v.append("a malformed comparison cell")
            continue
        cid, human, intended, rel = (x.group(1) for x in m)
        if human not in packet.TOKENS or intended not in packet.TOKENS:
            v.append("a token outside the closed set")
        if rel not in calibration.RELATIONS:
            v.append("a relation outside the closed set")
        parsed.append((cid, human, intended, rel))
    if len(rows) != TOTAL:
        v.append("the table does not hold exactly twelve rows")
    ids = [p[0] for p in parsed]
    if len(ids) != len(set(ids)):
        v.append("a duplicate row")
    if ids != sorted(ids):
        v.append("rows are not in ascending identity order")
    if parsed != list(expected):
        v.append("the rows are not exactly the mechanical comparison")
    return v


def counts_violations(text, expected):
    """The count table, whole: exactly the five permitted kinds in fixed
    order, each an integer count equal to the mechanical one and carrying
    exactly its statement. An unknown or malformed row fails; none is
    skipped."""
    rows, v = closed_table(text, COUNTS_SECTION, COUNTS_HEADER,
                           COUNTS_SEPARATOR, 3)
    kinds = []
    for cells in rows:
        kind = CELL_WORD.fullmatch(cells[0])
        if not kind:
            v.append("a malformed or unknown count kind")
            continue
        if not CELL_COUNT.fullmatch(cells[1]):
            v.append("an invalid count cell")
            continue
        if cells[2] != calibration.COUNT_STATEMENT:
            v.append("a count without its exact statement")
        kinds.append(kind.group(1))
        exp = expected.get(kind.group(1))
        if exp is None or int(cells[1]) != exp["count"]:
            v.append("a count differs from the mechanical one")
    if kinds != count_order():
        v.append("the kinds are not exactly the five permitted, in fixed "
                 "order")
    return v


def boundary_mutants(text, heading, surplus):
    """The boundary regression controls for one table: a surplus row
    prefixed by one space, three spaces or a tab, or with no opening pipe,
    placed immediately before the header, immediately after the last row,
    or later in the section; and a delimiter-free malformed line adjacent to
    either end of the table."""
    lines = text.split("\n")
    h = lines.index(heading)
    e = next((i for i in range(h + 1, len(lines))
              if lines[i].startswith("## ")), len(lines))
    table = [i for i in range(h + 1, e) if lines[i].startswith("|")]
    first, last = table[0], table[-1]
    later = next(i for i in range(last + 2, e) if lines[i].strip())
    out = {}
    for form, extra in (("one space", " " + surplus),
                        ("three spaces", "   " + surplus),
                        ("a tab", "\t" + surplus),
                        ("no opening pipe", surplus[2:])):
        for place, at in (("before the header", first),
                          ("after the last row", last + 1),
                          ("later in the section", later)):
            out["%s, %s" % (form, place)] = "\n".join(
                lines[:at] + [extra] + lines[at:])
    out["a delimiter-free line before the header"] = "\n".join(
        lines[:first] + ["mechanics sentinel"] + lines[first:])
    out["a delimiter-free line after the last row"] = "\n".join(
        lines[:last + 1] + ["mechanics sentinel"] + lines[last + 1:])
    return out


def count_order():
    return list(packet.TOKENS) + list(calibration.RELATIONS)


def succession_violations(rel, present, record, sites=None):
    """The exact staged transformation of a proof module: its fixed baseline
    pre-image under the site table yields exactly the present bytes, each
    site occurs once, the table reverses, and the record pins the result."""
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
    rows = {}
    for m in supplement.SUCCESSION_ROW.finditer(record):
        source = RECORD_SOURCES.get(m.group("source"))
        if source is not None:
            rows.setdefault(source, []).append(
                (tuple(s.strip() for s in m.group("labels").split(",")),
                 m.group("pre"), m.group("post")))
    found = rows.get(rel, [])
    if len(found) != 1:
        v.append("the record carries no single succession row for it")
    else:
        labels, pre_pin, post_pin = found[0]
        if labels != authority.labels(sites):
            v.append("the record names different sites")
        if pre_pin != PREIMAGE[rel][1]:
            v.append("the record's pre-image pin differs")
        if post_pin != _sha(present.encode("utf-8")):
            v.append("the record's post-image pin differs from the bytes")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def ccr_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CCR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CCR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         HAC_STATUS_CLOSE + fill(CCR_STATUS[state]) + " **" + R9_REVEAL),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + CCR_ROW + fill(ROW_PREFIX[state]) + CCR_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D3",
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
            + authority._indent(json.dumps(new_entry(state, date, record_hash),
                                           indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    return " ".join([CCR_ROW, CCR_ROW_BODY, R9_REVEAL]
                    + list(CCR_STATUS.values()))


def load_registry(commit):
    return json.loads(snapshot_text(commit, REGISTRY))


def snapshot():
    commit, problems = l4_snapshot()
    revealed = {c: revealed_bytes(commit, c) for c in manifest_ids()}
    register = json.loads(snapshot_text(commit, REGISTER))
    record = snapshot_text(commit, RECORD)
    return commit, problems, revealed, register, record


# ------------------------------------------------------------------ proofs
class RC1_RevealHomeClosure(unittest.TestCase):
    def test_rc1_reveal_home_holds_exactly_the_session_corpus(self):
        commit, problems = l4_snapshot()
        self.assertEqual(problems, [])
        expected = expected_reveal_paths()
        with self.subTest(fact="twelve, the session corpus only"):
            self.assertEqual(len(expected), TOTAL)
            self.assertFalse(set(manifest_ids()) & set(original_ids()))
        with self.subTest(fact="no reveal home at the baseline"):
            self.assertEqual([p for p in _git(
                "ls-tree", "-r", "--name-only", BASELINE).split()
                if p.startswith(REVEAL_HOME + "/")], [])
        tracked = (_git("ls-tree", "-r", "--name-only", commit).split()
                   if commit else _git("ls-files").split())
        with self.subTest(fact="tracked: exactly the twelve"):
            self.assertEqual(sorted(p for p in tracked
                                    if p.startswith(REVEAL_HOME + "/")),
                             expected)
        with self.subTest(fact="on disk: exactly the twelve"):
            self.assertEqual(sorted(REVEAL_HOME + "/" + p.name for p in
                                    (ROOT / REVEAL_HOME).iterdir()), expected)
        with self.subTest(control="an extra or an original identity is "
                                  "refused"):
            self.assertNotEqual(sorted(expected + [REVEAL_HOME + "/x.json"]),
                                expected)
            self.assertTrue(authority.reveal_violations(
                manifest_ids()[1:] + original_ids()[:1], manifest_ids(),
                original_ids(), dict.fromkeys(authority.REVEAL_GATE, True)))


class RC2_ExactRetainedBytes(unittest.TestCase):
    def test_rc2_every_revealed_file_hashes_to_its_commitment(self):
        commit, problems, revealed, _, _ = snapshot()
        self.assertEqual(problems, [])
        published = {r["case_id"]: r["authoring_commitment_sha256"]
                     for r in manifest_rows()}
        self.assertEqual(envelope.reveal_violations(published, revealed), [])
        with self.subTest(fact="no carriage return: the bytes are as "
                               "retained"):
            self.assertTrue(all(b"\r" not in b for b in revealed.values()))
        if commit is not None:
            with self.subTest(fact="working copies equal the committed "
                                   "objects"):
                for cid in revealed:
                    self.assertEqual(_lf(revealed_bytes(None, cid)),
                                     revealed[cid])
        cid = sorted(revealed)[0]
        for name, mutated in (
                ("a one-byte change", revealed[cid][:-2] + b" \n"),
                ("a line-ending conversion",
                 revealed[cid].replace(b"\n", b"\r\n")),
                ("a reserialisation", (json.dumps(json.loads(revealed[cid]),
                                                  indent=1) + "\n").encode())):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(envelope.reveal_violations(
                    published, dict(revealed, **{cid: mutated})))


class RC3_RecordValidityAndBinding(unittest.TestCase):
    def test_rc3_records_valid_and_bound(self):
        commit, problems, revealed, _, _ = snapshot()
        self.assertEqual(problems, [])
        rows = manifest_rows()
        visible = {c: committed(CORPUS, "%s/%s.json" % (HOME, c))
                   for c in manifest_ids()}
        self.assertEqual(binding_violations(rows, visible, revealed), [])
        cid = sorted(revealed)[0]
        rec = json.loads(revealed[cid])
        other = sorted(revealed)[1]
        for name, mutated in (
                ("another case's record under this name", revealed[other]),
                ("a wrong visible digest", envelope.canonical_bytes(
                    dict(rec, reviewer_visible_sha256="sha256:" + "0" * 64))),
                ("an out-of-vocabulary token", envelope.canonical_bytes(
                    dict(rec, intended_disposition="pass")))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(binding_violations(
                    rows, visible, dict(revealed, **{cid: mutated})))


class RC4_ValidationChain(unittest.TestCase):
    def test_rc4_chain_holds_through_the_reveal(self):
        commit, problems, revealed, register, record = snapshot()
        self.assertEqual(problems, [])
        ids, orig = manifest_ids(), original_ids()
        observed = {"commit": CORPUS,
                    "home_tree": _git("rev-parse", "%s:%s" % (CORPUS,
                                                             HOME)).strip(),
                    "manifest_sha256": _sha(_lf(committed(CORPUS, MANIFEST)))}
        gate = dict.fromkeys(authority.REVEAL_GATE, True)
        c = {"recorded_binding": dict(observed), "observed_binding": observed,
             "manifest_ids": ids, "original_ids": orig,
             "packet_paths": [p for p in _git("ls-tree", "--name-only",
                                              CORPUS, HOME + "/").split()
                              if p != MANIFEST],
             "register_ids": [r["case_id"] for r in register["rows"]],
             "existence_names": sorted(revealed),
             "reproduction_ids": sorted(revealed),
             "reveal_ids": sorted(revealed), "reveal_gate": gate}
        self.assertEqual(authority.session_chain_violations(c), [])
        for name, mutated in (
                ("a premature reveal", dict(c, reveal_gate=dict(
                    gate, copies_scanned_clean=False))),
                ("a partial reveal", dict(c, reveal_ids=sorted(revealed)[1:])),
                ("an original-corpus reveal", dict(
                    c, reveal_ids=sorted(revealed)[1:] + orig[:1]))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(authority.session_chain_violations(mutated))


class RC5_Comparison(unittest.TestCase):
    def test_rc5_the_recorded_comparison_is_exactly_the_mechanical_one(self):
        commit, problems, revealed, register, record = snapshot()
        self.assertEqual(problems, [])
        mech = mechanical_comparison(register, revealed)
        self.assertEqual(comparison_violations(record, mech), [])
        with self.subTest(fact="twelve rows, ascending, closed relation set"):
            self.assertEqual(len(mech), TOTAL)
            self.assertEqual([r[0] for r in mech], sorted(r[0] for r in mech))
            self.assertTrue({r[3] for r in mech} <= set(calibration.RELATIONS))
        with self.subTest(fact="agreement exactly on byte-identical tokens"):
            for _, h, a, rel in mech:
                self.assertEqual(rel == "agreement", h == a)
        row = next(l for l in record.split("\n") if l.startswith("| `W8-C-"))
        top = COMPARISON_HEADER + "\n" + COMPARISON_SEPARATOR + "\n"
        flipped = (row.replace("`agreement`", "`divergence`")
                   if "`agreement`" in row else
                   row.replace("`divergence`", "`agreement`"))
        for name, mutated in (
                ("a duplicate row with a fifth cell", record.replace(
                    row + "\n", row + "\n" + row[:-2]
                    + " | mechanics sentinel |\n", 1)),
                ("an exact duplicate row", record.replace(
                    row + "\n", row + "\n" + row + "\n", 1)),
                ("a flipped relation", record.replace(row, flipped, 1)),
                ("a relation outside the closed set", record.replace(
                    row, row[:row.rindex("`", 0, -3)] + "`agreed` |", 1)),
                ("a dropped row", record.replace(row + "\n", "", 1)),
                ("an extra header column", record.replace(
                    COMPARISON_HEADER, COMPARISON_HEADER + " Note |", 1)),
                ("a malformed separator", record.replace(
                    top, COMPARISON_HEADER + "\n|---|---|---|\n", 1)),
                ("a malformed row", record.replace(row, row[:-2], 1)),
                ("a stray table line later in the section", record.replace(
                    "\n9. **An authored", "\n| mechanics sentinel |\n\n9. "
                    "**An authored", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(comparison_violations(mutated, mech))
        for name, mutated in boundary_mutants(
                record, COMPARISON_SECTION,
                row[:-1] + " mechanics sentinel |").items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(comparison_violations(mutated, mech))


class RC6_Counts(unittest.TestCase):
    def test_rc6_only_the_two_count_kinds_each_with_its_statement(self):
        commit, problems, revealed, register, record = snapshot()
        self.assertEqual(problems, [])
        mech = mechanical_counts(mechanical_comparison(register, revealed))
        self.assertEqual(calibration.count_violations(mech), [])
        self.assertEqual(counts_violations(record, mech), [])
        with self.subTest(fact="the fixed order, zeros included, is the "
                               "permitted set"):
            self.assertEqual(sorted(mech), sorted(count_order()))
        with self.subTest(fact="no ratio, percentage or rate wording"):
            self.assertEqual(RATIO.findall(record), [])
        line = next(l for l in record.split("\n")
                    if l.startswith("| `agreement` |"))
        last = next(l for l in record.split("\n")
                    if l.startswith("| `divergence` |"))
        statement = calibration.COUNT_STATEMENT

        def with_count(cell):
            return record.replace(line, re.sub(r"^(\| `agreement` \| )[0-9]+",
                                               r"\g<1>" + cell, line), 1)
        for name, mutated in (
                ("an added hyphenated kind", record.replace(
                    last + "\n", last + "\n| `mechanics-sentinel` | 7 | "
                    + statement + " |\n", 1)),
                ("an added well-formed unknown kind", record.replace(
                    last + "\n", last + "\n| `score` | 1 | " + statement
                    + " |\n", 1)),
                ("a duplicate row", record.replace(
                    line + "\n", line + "\n" + line + "\n", 1)),
                ("a dropped row", record.replace(line + "\n", "", 1)),
                ("a changed count", with_count(str(mech["agreement"]["count"]
                                                   + 1))),
                ("a leading-zero count", with_count("0" + str(
                    mech["agreement"]["count"]))),
                ("a word count", with_count("eleven")),
                ("a negative count", with_count("-1")),
                ("a fractional count", with_count("1.5")),
                ("a dropped statement", record.replace(
                    line, line.replace(statement, "—"), 1)),
                ("an extra cell", record.replace(line, line[:-2]
                                                 + " | extra |", 1)),
                ("a malformed separator", record.replace(
                    COUNTS_HEADER + "\n" + COUNTS_SEPARATOR + "\n",
                    COUNTS_HEADER + "\n|---|---|\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(counts_violations(mutated, mech))
        for name, mutated in boundary_mutants(
                record, COUNTS_SECTION, "| `mechanics-sentinel` | 999 | "
                + statement + " |").items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(counts_violations(mutated, mech))
        with self.subTest(control="an added rate is detected"):
            self.assertTrue(RATIO.findall(record + "\nAgreement: 50%\n"))


class RC7_DispositionsFixed(unittest.TestCase):
    def test_rc7_register_and_session_record_untouched(self):
        commit, problems = l4_snapshot()
        self.assertEqual(problems, [])
        for rel, pin in ((REGISTER, REGISTER_PIN),
                         (SESSION_RECORD, SESSION_RECORD_PIN)):
            with self.subTest(fixed=rel):
                self.assertEqual(_sha(snapshot_text(commit, rel)
                                      .encode("utf-8")), pin)
                self.assertEqual(_sha(_lf(committed(BASELINE, rel))), pin)


class RC8_RecordCarriage(unittest.TestCase):
    def test_rc8_record_carries_its_statements(self):
        commit, problems, _, _, record = snapshot()
        self.assertEqual(problems, [])
        flat = _flat(record)
        for s in REQUIRED_CCR:
            with self.subTest(carried=s[:44]):
                self.assertEqual(flat.count(s), 1)
        with self.subTest(carried="nine-rule block byte-identical"):
            nine = re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                             r"failure\.\*\*)", _lf(committed(
                                 BASELINE, "docs/decisions/0054-generative-"
                                 "evaluation-maturity-doctrine.md"))
                             .decode("utf-8")).group(1)
            self.assertIn(nine, flat)
        with self.subTest(control="a removed statement is detected"):
            self.assertNotIn(REQUIRED_CCR[0], flat.replace(REQUIRED_CCR[0], ""))


class RC9_NoExposureBeyondTheComparison(unittest.TestCase):
    def test_rc9_only_the_authorised_fields_leave_the_reveal_home(self):
        commit, problems, revealed, _, record = snapshot()
        self.assertEqual(problems, [])
        by_id = {e["id"]: e for e in load_registry(commit)["entries"]}
        role = by_id["W8-D3-CCR"]["role"] + " " + by_id["W8-D3-CCR"]["title"]
        withheld = set()
        for raw in revealed.values():
            rec = json.loads(raw)
            withheld.add(rec["authoring_rationale"])
            withheld.add(rec["commitment_nonce"])
        surfaces = {"record": record, "registry role and title": role,
                    "board wording this landing adds": added_board_wording()}
        for name, text in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(corpus.reserved_channel_hits(text), [])
                self.assertEqual([s for s in (packet.PACKET_SCHEMA,
                                              calibration.REGISTER_SCHEMA,
                                              envelope.AUTHORING_SCHEMA)
                                  if s in text], [])
                self.assertEqual([w for w in withheld if w in text], [])
        count_beside_kind = re.compile(
            r"\b\d+\s+(?:agreements?|divergences?|cases? agree)\b|"
            r"\b(?:agreements?|divergences?)\s*[:=]?\s*\d+\b")
        for name in ("registry role and title",
                     "board wording this landing adds"):
            with self.subTest(no_token_or_count=name):
                text = surfaces[name]
                self.assertEqual([t for t in packet.TOKENS if t in text], [])
                self.assertIsNone(count_beside_kind.search(text))
        with self.subTest(control="a planted count beside a relation is "
                                  "detected"):
            self.assertIsNotNone(count_beside_kind.search(
                "with 11 agreements recorded"))
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([t for t in packet.TOKENS if t in src], [])
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([s for s in (packet.PACKET_SCHEMA,
                                          calibration.REGISTER_SCHEMA,
                                          envelope.AUTHORING_SCHEMA)
                              if s in src], [])
        with self.subTest(control="a planted reserved field is detected"):
            self.assertTrue(corpus.reserved_channel_hits(
                record + "\n" + sorted(corpus.RESERVED_FIELDS)[0]))


class RC10_Successions(unittest.TestCase):
    def test_rc10_staged_successions_are_exact(self):
        commit, problems, _, _, record = snapshot()
        self.assertEqual(problems, [])
        for rel in SUCCEEDED:
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(), PREIMAGE[rel][2])
            with self.subTest(exact_succession=PREIMAGE[rel][0]):
                self.assertEqual(succession_violations(
                    rel, snapshot_text(commit, rel), record), [])
        with self.subTest(fact="ADR-0059 Part G decision 27 stages exactly "
                               "these"):
            a59 = _flat(_lf(committed(BASELINE, ADR59)).decode("utf-8"))
            self.assertIn("K12's reveal limb and ADR-0058's R8 admit exactly "
                          "the session corpus's identities in the reveal home; "
                          "R7's entry set admits the completion record; the "
                          "envelope module's schema-string limb and case-home "
                          "limb admit the reveal home; the corpus module's C10 "
                          "scope and the supplement module's freshness scope "
                          "exclude the reveal home; R9's board sentence "
                          "succeeds again", a59)
        with self.subTest(fact="the succeeded modules carry this landing's "
                               "constants"):
            self.assertEqual(recovery.R9_REVEAL, R9_REVEAL)
            self.assertEqual(recovery.REVEAL_BASELINE, BASELINE)
            self.assertEqual(calibration.REVEAL_BASELINE, BASELINE)
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
                self.assertTrue(succession_violations(RECOVERY, text, record,
                                                      table))


class RC11_RegistryAndBoard(unittest.TestCase):
    def test_rc11_registry_and_board_change_exactly(self):
        commit, problems, _, _, record = snapshot()
        self.assertEqual(problems, [])
        state, date, v = ccr_state(record)
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
        reg = snapshot_text(commit, REGISTRY)
        rec_hash = _sha(record.encode("utf-8"))
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, rec_hash, state,
                                                    date))
        entry = {e["id"]: e for e in json.loads(reg)["entries"]}["W8-D3-CCR"]
        with self.subTest(fact="registered at W8-D3 with matching hash and "
                               "status"):
            self.assertEqual((entry["status"], entry["accepted_date"]),
                             (state, date))
            if commit is None:
                self.assertEqual(entry["content_hash"], lf_hash(ROOT / RECORD))
        with self.subTest(fact="no revealed record is individually "
                               "registered"):
            self.assertEqual([e["id"] for e in json.loads(reg)["entries"]
                              if e["path"].startswith(REVEAL_HOME)], [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, rec_hash, other, "2000-01-01"))
            wrong, _ = authority.apply_sites(board_pre,
                                             board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)


class RC12_Census(unittest.TestCase):
    def test_rc12_census_is_exactly_twenty_one_paths(self):
        commit, problems = l4_snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        expected = set(FIXED_CENSUS) | set(expected_reveal_paths())
        with self.subTest(fact="the census is exactly twenty-one paths"):
            self.assertEqual(len(expected), 21)
            self.assertEqual(paths, expected)
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             set(SUCCEEDED) | {SELF_REL})
        with self.subTest(fact="neither corpus home nor the register home "
                               "is touched"):
            self.assertEqual([p for p in paths if p.startswith(
                (HOME + "/", supplement.ORIGINAL_HOME + "/",
                 "governance/discriminating-review/"))], [])
        record = _flat(snapshot_text(commit, RECORD))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly twenty-one "
                          r"paths:\*\* (.*?) ## ", record)
            self.assertIsNotNone(m)
            named = set(re.findall(r"`([^`]+)`", m.group(1)))
            self.assertEqual(named - {REVEAL_HOME + "/<case_id>.json"},
                             set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
