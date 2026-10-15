"""W8-CHC — case-home scope correction proofs (CH1–CH8).

A bounded phase-level correction, outside W8-D4, separately governed by the
human authority's acceptance of its record: the envelope module's V12
case-home tuple admits exactly the two validation reveal homes that ADR-0060
decision 23 fixes, beside its four existing homes, by one exact
transformation of its effective corpus-landing post-image. ADR-0060 decision
38 stages the reveal landing's authoring-schema succession of that module
but not its case-home limb; this record expressly settles that scope and
claims no more. It amends no law and adds no succession to any W8-D4
landing, and it opens no home in effect: the validation law's VL10 keeps
refusing every reveal-home path until the reveal landing's own succession.

Following ADR-0060 decision 39's pattern, every proof here reads this
landing's fixed snapshot - the working copy over the baseline before the
commit exists, the one commit that added this record afterwards - and
every helper implementation, constant and reserved literal a proof relies
on is executed from that same snapshot's bytes, in a private namespace,
never taken from a live module that a later landing may lawfully succeed.
This module imports no other proof module; it holds no live gate on the
absence or admission of any future artefact, and the live VL10 gates stay
in VL10.

THIS MODULE READS NO CUSTODY. It names no case, holds no case identity,
disposition token or schema literal as a literal, renders no packet and
opens no withheld record. Its planted paths are built at run time and exist
only inside the controls.

WHAT GREEN DOES NOT MEAN. A green run proves the exact transformation, its
scope and its carriage only. It NEVER establishes: that any reveal may now
begin; anything about any case, its class, method, family or composition;
that any retained record exists or is intact; anything about the reviewer;
or that the instrument is valid, mature or ready.
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

# The published, remotely verified corpus landing: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "f638cca75ec4a192685bf5cd53f29451cfdbbdd9"
CORPUS_PARENT = "054f1270b8206a059636e18e012223ddfe52d5ea"

RECORD = "docs/phases/W8-case-home-scope-correction.md"
SELF_REL = "tests/test_w8_case_home_scope_correction.py"
ENVELOPE = "tests/test_w8_discriminating_instrument_envelope.py"
LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
CENSUS = frozenset({RECORD, SELF_REL, ENVELOPE, REGISTRY, BOARD})

# The helper modules whose snapshot bytes the proofs execute.
LAWMOD = "tests/test_w8_validation_law.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
AUTHORITY = "tests/test_w8_recovery_authority.py"
REVEAL = "tests/test_w8_reveal_calibration.py"
PACKET = "tests/w8_review_packet.py"
CALIBRATION = "tests/test_w8_calibration_law.py"
VCORPUS = "tests/test_w8_validation_corpus.py"
# The validation-law module at this landing is the corpus landing's reviewed
# post-image, unmoved: (LF SHA-256, blob).
LAWMOD_PIN = ("sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02",
              "ce39f6c0812cae5c36d646f3db211547544560ce")

# The four homes the case-home tuple admits at the baseline, and the two
# validation reveal homes of ADR-0060 decision 23 this correction adds.
EXISTING_HOMES = ("governance/discriminating-instrument/",
                  "governance/discriminating-supplement/",
                  "governance/discriminating-reveal/",
                  "governance/validation-cases/")
REVEAL_HOMES = ("governance/validation-reveal/authoring/",
                "governance/validation-reveal/construction/")
DECISION_23 = ("reveal homes `governance/validation-reveal/authoring/` and "
               "`governance/validation-reveal/construction/`, each holding "
               "`<case_id>.json`")
LAW_PIN = ("sha256:f4440effdab671b49572d14cf8ef14c7d2b1b711e33361cf4ddd59c7c855aae8",
           "f6955c079ec323a9dd5e6d20854c9b226e59b79a")

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    ENVELOPE: ("envelope module",
               "sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80",
               "f579b93fc107fad5c55455ff65353081fd456795"),
    REGISTRY: ("registry",
               "sha256:975873235fb3268338f116ec0773cc1b82fa201abbcefd3d31fad573e2f4d709",
               "30db2676577f525e9ba8f3b2f3f5214d421d69c3"),
    BOARD: ("board",
            "sha256:2b35a961621b0265d8e52f1778fd1bbc0997ed67b4d395930870f709c9ff758f",
            "95b3ade324fd8f398aa6f334982787fe54d070a8"),
}
# The reviewed post-image of the one change: (LF SHA-256, blob).
POSTIMAGE = {ENVELOPE: ("sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700", "3e1b4d4fedc2ab322a7d0cf9b090f78078b25ac3")}

# ------------------------------------------------- the one exact change
TUPLE_TAIL_OLD = ('                      "governance/validation-cases/"))], '
                  '[])\n')
TUPLE_TAIL_NEW = ('                      "governance/validation-cases/",\n'
                  '                      # Admitted by the separate case-home '
                  'scope\n'
                  '                      # correction W8-CHC, outside '
                  'ADR-0060 Part J\n'
                  '                      # decision 38.\n'
                  '                      "governance/validation-reveal/'
                  'authoring/",\n'
                  '                      "governance/validation-reveal/'
                  'construction/"))], [])\n')
SITES = {ENVELOPE: (("V12", TUPLE_TAIL_OLD, TUPLE_TAIL_NEW),)}
TUPLE_HEAD = '                 if "W8-C-" in p and not p.startswith(\n'
TUPLE_END = '))], [])\n'

# The record's section 3 succession table, read whole: exactly this header,
# this separator and the one row built from the trusted pins.
SUCCESSION_SECTION = "## 3. The exact change"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"

# --------------------------------------- board and registry: authorised edits
CHC_LINK = ("([`W8-case-home-scope-correction.md`]"
            "(W8-case-home-scope-correction.md))")
CHC_STATUS_TAIL = (
    "exactly the two validation reveal homes of ADR-0060 decision 23 to the "
    "envelope's case-home check, as a separate phase-level act outside "
    "W8-D4; it amends no law and opens no home in effect, the validation "
    "law's VL10 still refusing every reveal path until the reveal landing.")
CHC_STATUS = {
    "draft": ("**A draft case-home scope correction, `W8-CHC`, is before the "
              "human reviewer** " + CHC_LINK + ": if accepted, it would "
              "admit " + CHC_STATUS_TAIL),
    "accepted": ("**`W8-CHC` — the case-home scope correction — is "
                 "accepted** " + CHC_LINK + " — accepted %s: it admits "
                 + CHC_STATUS_TAIL),
}
CHC_ROW = ("| W8 — Case-Home Scope Correction (W8-CHC) | "
           "[`W8-case-home-scope-correction.md`]"
           "(W8-case-home-scope-correction.md) | ")
CHC_ROW_BODY = (
    "Tier J: **a bounded phase-level proof-scope correction, outside "
    "W8-D4** — ADR-0060 decision 38 stages the reveal landing's envelope "
    "authoring-schema succession but not its case-home limb, so the "
    "validation reveal homes of decision 23 would have met a refusal outside "
    "that closed list; found by the corpus-landing preparation's forward "
    "probes and confirmed independently. The envelope V12 case-home tuple "
    "now admits exactly those two homes beside its four existing homes, by "
    "one exact transformation proven with negative controls, its vacancy "
    "limb unchanged; the validation law's VL10 keeps refusing every reveal "
    "path until the reveal landing. The record expressly settles its "
    "authority against decisions 38 and 39, as adopted by the human "
    "authority's acceptance; it amends no law and adds no succession to any "
    "W8-D4 landing. **No case, manifest, register, custody, session, reveal "
    "or diagnosis; D4-D preparation stays closed until separately "
    "authorised; W8-D5 to W8-D7 stay closed.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = ("composition stays withheld until the corpus's own "
                       "reveal. **No divergence is diagnosed")
BOARD_ROW_HEAD = "| W8-D4 — Validation Corpus (record, W8-D4-VCR) | "
CHC_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CHC_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-CHC", "path": RECORD, "type": "phase-record",
    "title": "W8 - Case-Home Scope Correction",
    "role": (
        "A bounded phase-level proof-scope correction, outside W8-D4, of the "
        "envelope module's V12 case-home limb: its admitted-home tuple "
        "admits exactly the two validation reveal homes of ADR-0060 decision "
        "23 beside its four existing homes, by one exact transformation of "
        "the effective corpus-landing post-image, its vacancy limb and every "
        "other line unchanged, so that the reveal landing meets only the "
        "successions decision 38 stages for it. Expressly settles its "
        "authority and scope against ADR-0060 decisions 38 and 39: a "
        "separate governing act of the human authority, effective only on "
        "its own acceptance, publication and remote verification, "
        "authorising exactly this one change at its own landing, adding no "
        "succession to any W8-D4 landing and amending no law; the validation "
        "law's VL10 keeps refusing every reveal path until the reveal "
        "landing. Proof obligations CH1 to CH8. A prerequisite of the reveal "
        "landing; D4-D preparation stays closed until separately authorised. "
        "No case, manifest, register, custody, session, reveal or "
        "diagnosis."),
    "depends_on": ["ADR-0060", "W8-D4-VCR", "W8-D4-IVB", "ADR-0059",
                   "W8-HPC", "W8-HAC", "ADR-0054", "ADR-0056", "W8-AR",
                   "W7-CR"]}
REQUIRED = (
    "This record is a separate governing act of the human authority",
    "It authorises exactly one bounded change, at its own landing:",
    "This scope settlement is express, and it takes effect only through the "
    "human authority's acceptance of this record, which adopts it.",
    "It amends no law and adds no succession to any W8-D4 landing.",
    "keeps refusing every tracked path in either reveal home until the "
    "reveal landing's own VL10 succession",
    "D4-D preparation stays closed until separately authorised",
    "This landing's census is exactly five paths:",
    "Any need for a sixth path is a further stop.",
    "No other existing proof moves at this landing.",
    "is executed from this landing's snapshot bytes, never taken from the "
    "live module",
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


def l8_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added this record, whose sole
    parent must be BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the correction record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot():
    commit, problems = l8_snapshot()
    if commit is None:
        return commit, problems, (lambda rel: _lf((ROOT / rel).read_bytes()))
    return commit, problems, (lambda rel: committed(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot: the bytes
    `read` yields for `rel`, executed in a fresh private namespace that is
    registered nowhere. A historical proof calls only these helpers and
    constants, never the live module, which a later landing may lawfully
    succeed (ADR-0060 decision 38)."""
    ns = {"__name__": "_w8_chc_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(read(rel), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def case_home_tuple(text):
    """The V12 case-home tuple, as the string literals between its one
    opening line and its closing; None unless that opening occurs exactly
    once and closes."""
    if text.count(TUPLE_HEAD) != 1:
        return None
    start = text.index(TUPLE_HEAD) + len(TUPLE_HEAD)
    end = text.find(TUPLE_END, start)
    if end < 0:
        return None
    block = "\n".join(l for l in text[start:end].split("\n")
                      if not l.strip().startswith("#"))
    return tuple(re.findall(r'"([^"\n]+)"', block))


def v12_refusals(paths, homes):
    """The V12 case-home limb's predicate over `paths` for the admitted
    `homes`: every path carrying the case prefix outside them."""
    return [p for p in paths if "W8-C-" in p and not p.startswith(homes)]


def scope_violations(homes):
    v = []
    if homes is None:
        return ["the case-home tuple is missing or not unique"]
    if len(set(homes)) != len(homes):
        v.append("a home is repeated")
    if homes != EXISTING_HOMES + REVEAL_HOMES:
        v.append("the case-home tuple is not exactly the four existing "
                 "homes followed by decision 23's two reveal homes")
    return v


def succession_rows(authority):
    """The section 3 row, built from the trusted site table and pins."""
    return [["`%s`" % ENVELOPE, ", ".join(authority.labels(SITES[ENVELOPE])),
             "`%s`" % PREIMAGE[ENVELOPE][1], "`%s`" % POSTIMAGE[ENVELOPE][0]]]


def succession_table_violations(record, reveal, authority):
    """Section 3's table, read whole by the reviewed closed-table reader
    before its row is used: exactly the header, the separator and the one
    trusted row; no row is selected by pattern."""
    rows, v = reveal.closed_table(record, SUCCESSION_SECTION,
                                  SUCCESSION_HEADER, SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(authority):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, record, reveal, authority, sites=None):
    """The exact transformation: the fixed pre-image under the site table
    yields exactly the present bytes, the site occurs once, the table
    reverses, the result is the reviewed post-image, and the record's closed
    table pins it."""
    sites = SITES[ENVELOPE] if sites is None else sites
    v = []
    pre = _lf(committed(BASELINE, ENVELOPE)).decode("utf-8")
    if _sha(pre.encode("utf-8")) != PREIMAGE[ENVELOPE][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[ENVELOPE][0]:
        v.append("the bytes are not the reviewed post-image")
    return v + succession_table_violations(record, reveal, authority)


def planted(home, n):
    """A labelled mechanics path under `home`, built at run time."""
    return "%sW8-C-%s.json" % (home, ("%x" % n) * 64)


REVEAL_PATHS = [planted(h, i + 1) for i, h in enumerate(REVEAL_HOMES)]
ELSEWHERE_PATHS = [planted(h, 7) for h in (
    "governance/validation-reveal/", "governance/validation-reveal/other/",
    "governance/validation-review/", "docs/phases/")]


def two_gate_violations(read, commit):
    """CH3's verdict at this landing's snapshot, from the snapshot's own V12
    tuple and the snapshot's own VL10 helper and context: the corrected
    limb admits a planted path in each reveal home and nowhere else new,
    the baseline limb refused them, and VL10 holds at the snapshot while
    refusing each planted reveal-home path with exactly its refusal."""
    pre = case_home_tuple(_lf(committed(BASELINE, ENVELOPE)).decode("utf-8"))
    post = case_home_tuple(read(ENVELOPE).decode("utf-8"))
    v = []
    if v12_refusals(REVEAL_PATHS, pre) != REVEAL_PATHS:
        v.append("the baseline limb did not refuse both reveal homes")
    if v12_refusals(REVEAL_PATHS, post or ()) != []:
        v.append("the corrected limb does not admit both reveal homes")
    if v12_refusals(ELSEWHERE_PATHS, post or ()) != ELSEWHERE_PATHS:
        v.append("the corrected limb admits a place outside the two homes")
    law = historical(read, LAWMOD)
    tracked = snapshot_tracked(commit)
    entries = json.loads(read(REGISTRY))["entries"]
    holders = [law.LAW, law.SELF_REL, law.CONSTRUCTION_MANIFEST]
    corpus = law.corpus_admitted(read)

    def vl10(paths):
        return law.staged_absence_violations(paths, lambda p: False, entries,
                                             holders, corpus)
    if vl10(tracked) != []:
        v.append("VL10 does not hold at this landing's snapshot")
    for path in REVEAL_PATHS:
        if vl10(tracked + [path]) != ["a later home is tracked: %s" % path]:
            v.append("VL10 does not refuse a reveal-home path exactly")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def record_state(text, recovery):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CHC_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CHC_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_row_anchor(board_pre):
    """The corpus landing's board row, read from the pinned pre-image."""
    rows = [l for l in board_pre.split("\n") if l.startswith(BOARD_ROW_HEAD)]
    return rows[0] + "\n" if len(rows) == 1 else None


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    anchor = board_row_anchor(board_pre)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "composition stays withheld until the corpus's own reveal. "
         + fill(CHC_STATUS[state]) + " **No divergence is diagnosed"),
        ("row", anchor,
         anchor + CHC_ROW + fill(ROW_PREFIX[state]) + CHC_ROW_BODY + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": None,
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


def reserved_literals(read):
    """The reserved token and schema literals, as this landing's snapshot
    defines them."""
    env = historical(read, ENVELOPE)
    return (tuple(sorted(env.TOKENS)),
            (historical(read, PACKET).PACKET_SCHEMA, env.AUTHORING_SCHEMA,
             historical(read, CALIBRATION).REGISTER_SCHEMA)
            + tuple(historical(read, LAWMOD).NEW_SCHEMAS))


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted
    to call is replaced - a later diagnostic rewording, and gates that
    refuse nothing - and the previous state is restored on exit. It
    requires no live name to exist: a helper a later landing has renamed
    or removed is installed temporarily and removed again on exit, and
    every value that existed before is restored by identity."""

    ABSENT = object()
    TARGETS = (("test_w8_validation_law", "staged_absence_violations"),
               ("test_w8_validation_law", "corpus_admitted"),
               ("test_w8_session_recovery_law", "R9_REVEAL"),
               ("test_w8_session_recovery_law", "header_state"),
               ("test_w8_session_recovery_law", "exposure_violations"),
               ("test_w8_recovery_authority", "apply_sites"),
               ("test_w8_reveal_calibration", "closed_table"))

    @classmethod
    def state(cls):
        """Each target's present live value, or ABSENT."""
        return {(m, n): getattr(importlib.import_module(m), n, cls.ABSENT)
                for m, n in cls.TARGETS}

    def __enter__(self):
        live = importlib.import_module("test_w8_validation_law")
        original = getattr(live, "staged_absence_violations", None)
        if original is None:
            original = lambda *a, **k: []

        def reworded(*a, **k):
            return [m.replace("a later home is tracked",
                              "an unadmitted later-home path is tracked")
                    for m in original(*a, **k)]
        replacements = {
            "staged_absence_violations": reworded,
            "corpus_admitted": lambda read: set(),
            "R9_REVEAL": "mechanics sentinel",
            "header_state": lambda text: (None, None),
            "exposure_violations": lambda text, pins=(): [],
            "apply_sites": lambda text, sites: (text, []),
            "closed_table": lambda *a, **k: ([], [])}
        self.saved = []
        for module, name in self.TARGETS:
            mod = importlib.import_module(module)
            self.saved.append((mod, name, getattr(mod, name, self.ABSENT)))
            setattr(mod, name, replacements[name])
        return self

    def __exit__(self, *exc):
        for mod, name, value in reversed(self.saved):
            if value is self.ABSENT:
                mod.__dict__.pop(name, None)
            else:
                setattr(mod, name, value)
        return False


# ------------------------------------------------------------------ proofs
class CH1_ExactTransformation(unittest.TestCase):
    def test_ch1_the_envelope_change_is_exactly_the_reviewed_one(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        authority = historical(read, AUTHORITY)
        reveal = historical(read, REVEAL)
        record = read(RECORD).decode("utf-8")
        present = read(ENVELOPE).decode("utf-8")
        with self.subTest(fact="the baseline object is the corpus landing's "
                               "reviewed post-image"):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + ENVELOPE)
                             .strip(), PREIMAGE[ENVELOPE][2])
            self.assertIn(PREIMAGE[ENVELOPE][1],
                          committed(BASELINE, VCORPUS).decode("utf-8"))
        with self.subTest(fact="one exact, reversible transformation, pinned "
                               "by hash and blob"):
            self.assertEqual(succession_violations(present, record, reveal,
                                                   authority), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[ENVELOPE][1])
        with self.subTest(fact="the record's table is exactly its trusted "
                               "lines, read whole"):
            self.assertEqual(succession_table_violations(record, reveal,
                                                         authority), [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, ()),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[ENVELOPE] + (("V12", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(text, record, reveal,
                                                      authority, table))
        with self.subTest(control="a wrong record pin is refused"):
            self.assertTrue(succession_violations(present, record.replace(
                POSTIMAGE[ENVELOPE][0], "sha256:" + "0" * 64, 1), reveal,
                authority))
        row = "| " + " | ".join(succession_rows(authority)[0]) + " |"
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        for name, mutated in (
                ("a space-prefixed duplicate row", record.replace(
                    row + "\n", row + "\n " + row + "\n", 1)),
                ("a tab-prefixed duplicate row", record.replace(
                    row + "\n", row + "\n\t" + row + "\n", 1)),
                ("an exact duplicate row", record.replace(
                    row + "\n", row + "\n" + row + "\n", 1)),
                ("a row with no opening pipe", record.replace(
                    row, row[2:], 1)),
                ("a row with a fifth cell", record.replace(
                    row, row[:-2] + " | mechanics sentinel |", 1)),
                ("a dropped row", record.replace(row + "\n", "", 1)),
                ("an altered header", record.replace(
                    top, SUCCESSION_HEADER + " Note |\n"
                    + SUCCESSION_SEPARATOR + "\n", 1)),
                ("an altered separator", record.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the top", record.replace(
                    top, "mechanics sentinel\n" + top, 1)),
                ("delimiter-free material touching the bottom",
                 record.replace(row + "\n", row + "\nmechanics sentinel\n",
                                1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, reveal,
                                                            authority))
                self.assertTrue(succession_violations(present, mutated,
                                                      reveal, authority))
        for name, mutated in reveal.boundary_mutants(
                record, SUCCESSION_SECTION, row).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, reveal,
                                                            authority))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                self.assertEqual(succession_violations(
                    present, record, historical(read, REVEAL),
                    historical(read, AUTHORITY)), [])


class CH2_Scope(unittest.TestCase):
    def test_ch2_exactly_decision_23s_two_reveal_homes_are_added(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        pre = _lf(committed(BASELINE, ENVELOPE)).decode("utf-8")
        present = read(ENVELOPE).decode("utf-8")
        with self.subTest(fact="the baseline tuple is the four existing "
                               "homes"):
            self.assertEqual(case_home_tuple(pre), EXISTING_HOMES)
        with self.subTest(fact="the tuple is the four existing homes followed "
                               "by decision 23's two reveal homes"):
            self.assertEqual(scope_violations(case_home_tuple(present)), [])
        law = _lf(committed(BASELINE, LAW)).decode("utf-8")
        with self.subTest(fact="decision 23 names exactly these reveal "
                               "homes"):
            self.assertIn(DECISION_23, _flat(law))
            self.assertEqual(sorted(set(re.findall(
                r"governance/validation-reveal/[a-z]+/", _flat(law)))),
                sorted(REVEAL_HOMES))
        with self.subTest(fact="the law is byte-untouched at this landing"):
            here = read(LAW)
            self.assertEqual((_sha(here), _blob(here)), LAW_PIN)
            self.assertEqual(_sha(_lf(committed(BASELINE, LAW))), LAW_PIN[0])
        homes = EXISTING_HOMES + REVEAL_HOMES
        for name, mutant in {
                "a broadened reveal root": homes + ("governance/"
                                                    "validation-reveal/",),
                "a third reveal home": homes + ("governance/validation-reveal/"
                                                "other/",),
                "a missing reveal home": homes[:-1],
                "a repeated home": homes + homes[-1:],
                "reordered homes": homes[:-2] + homes[-1:] + homes[-2:-1],
                "a broadened governance prefix": EXISTING_HOMES
                + ("governance/",),
                "a missing tuple": None}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(scope_violations(mutant))


class CH3_TwoGates(unittest.TestCase):
    """The correction removes only the V12 barrier: V12 now admits paths in
    the two reveal homes and nowhere else new, while VL10 - its helper and
    context executed from this landing's snapshot - still refuses every
    reveal-home path until the reveal landing's own succession."""

    def test_ch3_v12_admits_only_the_reveal_homes_and_vl10_still_bars(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        with self.subTest(fact="the historical VL10 context is the corpus "
                               "landing's reviewed module, unmoved"):
            here = read(LAWMOD)
            self.assertEqual((_sha(here), _blob(here)), LAWMOD_PIN)
        with self.subTest(fact="both gates hold as stated, at this landing's "
                               "snapshot"):
            self.assertEqual(two_gate_violations(read, commit), [])
        with self.subTest(control="a later live-helper change leaves the "
                                  "historical verdict unchanged"):
            with LiveHelpersSabotaged():
                self.assertEqual(two_gate_violations(read, commit), [])
        with self.subTest(control="a renamed live helper: the control "
                                  "completes, the verdict stands, and every "
                                  "live name is restored exactly"):
            absent = LiveHelpersSabotaged.ABSENT
            live = importlib.import_module("test_w8_validation_law")
            old = "staged_absence_violations"
            new = "staged_membership_violations"
            kept = {n: live.__dict__.get(n, absent) for n in (old, new)}
            helper = kept[old] if kept[old] is not absent else kept[new]
            try:
                live.__dict__.pop(old, None)
                if helper is not absent:
                    setattr(live, new, helper)
                before = LiveHelpersSabotaged.state()
                with LiveHelpersSabotaged():
                    verdict = two_gate_violations(read, commit)
                after = LiveHelpersSabotaged.state()
                self.assertIs(before[("test_w8_validation_law", old)], absent)
                self.assertEqual(verdict, [])
                self.assertNotIn(old, live.__dict__)
                self.assertTrue(all(after[k] is before[k] for k in before))
            finally:
                for n, value in kept.items():
                    if value is absent:
                        live.__dict__.pop(n, None)
                    else:
                        setattr(live, n, value)
            self.assertTrue(all(live.__dict__.get(n, absent) is value
                                for n, value in kept.items()))
        source = read(LAWMOD)
        gate = b"if p.startswith(homes) and p not in admitted]"
        weakenings = {
            "a historical gate that admits both reveal homes":
                gate.replace(b"homes)", b"homes[:2])"),
            "a historical gate that admits one reveal home":
                gate.replace(b"admitted]", b'admitted and "/authoring/" not '
                                           b'in p]'),
            "an inverted historical gate":
                gate.replace(b"if p.", b"if not p.")}
        for name, weak in weakenings.items():
            bad = source.replace(gate, weak)
            with self.subTest(control="%s is refused" % name):
                self.assertEqual(source.count(gate), 1)
                self.assertNotEqual(bad, source)
                self.assertTrue(two_gate_violations(
                    lambda rel, bad=bad: bad if rel == LAWMOD else read(rel),
                    commit))


class CH4_HistoryPreserved(unittest.TestCase):
    def test_ch4_every_earlier_claim_stays_proven_at_its_own_commit(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        reveal = historical(read, REVEAL)
        authority = historical(read, AUTHORITY)
        pre = _lf(committed(BASELINE, ENVELOPE)).decode("utf-8")
        present = read(ENVELOPE).decode("utf-8")
        head, tail = pre.split(TUPLE_TAIL_OLD)
        with self.subTest(fact="every envelope line outside the one site is "
                               "unchanged, the vacancy limb included"):
            self.assertTrue(present.startswith(head))
            self.assertTrue(present.endswith(tail))
            self.assertEqual(len(present), len(head) + len(TUPLE_TAIL_NEW)
                             + len(tail))
            self.assertIn('self.assertEqual([p for p in held if "W8-C-" in p]'
                          ', [])', head)
        with self.subTest(fact="the corpus landing's proofs read their own "
                               "commit, unmoved"):
            self.assertIn('BASELINE = "%s"' % CORPUS_PARENT,
                          committed(BASELINE, VCORPUS).decode("utf-8"))
            self.assertEqual(_git("rev-list", "--parents", "-n", "1",
                                  BASELINE).split()[1:], [CORPUS_PARENT])
        edited = pre.replace('held if "W8-C-" in p]',
                             'held if "W8-C-" in p and 0]', 1)
        edited, _ = authority.apply_sites(edited, SITES[ENVELOPE])
        with self.subTest(control="a vacancy-limb edit breaks the exact "
                                  "transformation"):
            self.assertNotEqual(edited, present)
            self.assertTrue(succession_violations(
                edited, read(RECORD).decode("utf-8"), reveal, authority))


class CH5_Census(unittest.TestCase):
    def test_ch5_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(len(CENSUS), 5)
            self.assertEqual(paths, set(CENSUS))
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {ENVELOPE, SELF_REL})
        for name, p in {"an extra path": paths | {LAW},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(CENSUS))


class CH6_RegistryAndBoard(unittest.TestCase):
    def test_ch6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        recovery = historical(read, RECOVERY)
        authority = historical(read, AUTHORITY)
        state, date, v = record_state(read(RECORD).decode("utf-8"), recovery)
        self.assertEqual(v, [])
        board_pre = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(BASELINE, REGISTRY)).decode("utf-8")
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")

        def board_ok(apply_sites, r9):
            expected, problems = apply_sites(
                board_pre, board_sites(state, date, board_pre))
            return problems == [] and board == expected and r9 in board
        with self.subTest(fact="exact authorised board, R9's sentence "
                               "retained", state=state):
            self.assertIsNotNone(board_row_anchor(board_pre))
            self.assertTrue(board_ok(authority.apply_sites,
                                     recovery.R9_REVEAL))
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        e = {x["id"]: x for x in json.loads(reg)["entries"]}.get("W8-CHC")
        with self.subTest(entry="W8-CHC"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]),
                             (RECORD, "phase-record", "W8", None))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            if commit is None:
                self.assertEqual(e["content_hash"],
                                 _sha(_lf((ROOT / RECORD).read_bytes())))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = authority.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                rec = historical(read, RECOVERY)
                self.assertEqual(record_state(read(RECORD).decode("utf-8"),
                                              rec)[2], [])
                self.assertTrue(board_ok(historical(read, AUTHORITY)
                                         .apply_sites, rec.R9_REVEAL))


class CH7_RecordCarriage(unittest.TestCase):
    def test_ch7_record_carries_its_settlement_and_no_exposure(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        recovery = historical(read, RECOVERY)
        text = read(RECORD).decode("utf-8")
        flat = _flat(text)
        missing = [s[:44] for s in REQUIRED if flat.count(s) < 1]
        with self.subTest(fact="every required statement is carried"):
            self.assertEqual(missing, [])
        pins = [PREIMAGE[ENVELOPE][1].split(":", 1)[1],
                POSTIMAGE[ENVELOPE][0].split(":", 1)[1]]
        with self.subTest(fact="no identity, unpinned digest or token"):
            self.assertEqual(recovery.exposure_violations(text, pins), [])
        for name, plant in {"a case identity": planted("", 10)[:-5],
                            "an unpinned digest": "d" * 64}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(recovery.exposure_violations(
                    text + "\n" + plant, pins))
        with self.subTest(control="a removed statement is detected"):
            self.assertNotIn(REQUIRED[0], _flat(text.replace(REQUIRED[0], "")))


class CH8_ModuleHygiene(unittest.TestCase):
    def test_ch8_no_token_schema_or_identity_in_this_module(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tokens, schemas = reserved_literals(read)
        case_id = historical(read, RECOVERY).CASE_ID_ANYWHERE
        src = SELF.read_text(encoding="utf-8")
        with self.subTest(fact="the module is this landing's committed "
                               "object, once committed"):
            if commit is not None:
                self.assertEqual(_lf(SELF.read_bytes()),
                                 committed(commit, SELF_REL))
        with self.subTest(fact="no token, schema literal or case identity"):
            self.assertTrue(tokens and schemas)
            self.assertEqual([t for t in tokens if t in src], [])
            self.assertEqual([s for s in schemas if s in src], [])
            self.assertIsNone(case_id.search(src))
        for name, plant in {"a token": tokens[0],
                            "a schema literal": schemas[0]}.items():
            with self.subTest(control="a planted %s is detected" % name):
                planted_src = src + "\n# " + plant
                self.assertTrue([t for t in tokens if t in planted_src]
                                or [s for s in schemas if s in planted_src])


if __name__ == "__main__":
    unittest.main()
