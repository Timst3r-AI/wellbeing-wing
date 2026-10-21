"""W8-D4-E — validation reveal proofs (W8-D4-VRC, VR1–VR12).

The reveal landing of W8-D4 on the validation corpus W8-V1: the exact
retained bytes of the corpus's eighteen authoring records and eighteen
construction records published at the two reveal homes of ADR-0060
decision 23, each hashing to its published commitment; the case-level
comparison of each human token to its authored intended token as agreement
or divergence; the two permitted count kinds; and the two proof
successions decision 38 stages for this landing. This module proves the
reveal homes' closure, the exact bytes, every record's validity and
binding, the four-value binding chain, the comparison and the counts read
whole, the fixed dispositions, the record's carriage and exposure limits,
the exact transformations and the census, each with planted-mutant or
negative controls.

Following ADR-0060 decision 39, every proof here reads this landing's fixed
snapshot - the candidate over the baseline before the commit exists, the
one commit that added this record afterwards - and executes every helper,
constant and reserved literal it relies on from that snapshot's bytes, in
a private namespace, never from a live module a later landing may lawfully
succeed. Before the commit exists the revealed files are read as their raw
bytes. This module imports no other proof module; it holds no live gate on
the absence or admission of any future artefact, and those gates stay in
VL10. The residual live reach is disclosed exactly: each snapshot-executed
helper module imports, at its own top level, the live modules it aliases
- the envelope, packet, calibration, corpus, authority, recovery,
supplement and opening modules - for the fixed-law values it reads from
them (the identity and digest patterns, canonical bytes, the token,
relation and class vocabularies, the reserved labels and the reveal gate's
names), and no more independence than that is claimed.

THIS MODULE READS NO CUSTODY. It reads the published reveal homes, the
corpus's committed cases and manifests, the published register and session
record, and, for identity disjointness only, the published manifests of
both earlier corpora. It names no case as a literal and holds no
disposition token, method label or schema literal as a literal.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any human token or authored intended token is
right; that any agreement means the instrument detected anything or that a
divergence is a reviewer error; any diagnosis; any rate, score or
readiness; the absence of influence or the reviewer's independence; that
any retained record was handled as the record states; or that any later
landing may now begin.
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

# The published, remotely verified corpus landing: the immutable corpus
# commit ADR-0060 decision 25 binds.
CORPUS = "f638cca75ec4a192685bf5cd53f29451cfdbbdd9"
# The published, remotely verified session landing: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "44947adf9b60f2ce462be97a2c0e628a3ecbdd89"

HOME = "governance/validation-cases"
MANIFEST = HOME + "/W8-V1-commitment-manifest.json"
CMANIFEST = HOME + "/W8-V1-construction-manifest.json"
FOREIGN_MANIFESTS = (
    "governance/discriminating-instrument/W8-D2-commitment-manifest.json",
    "governance/discriminating-supplement/W8-S1-commitment-manifest.json")
REGISTER = "governance/validation-review/W8-D4-validation-register.json"
SESSION_RECORD = "docs/phases/W8-D4-validation-session-record.md"
REVEAL_ROOT = "governance/validation-reveal"
AUTH_HOME = REVEAL_ROOT + "/authoring"
CONS_HOME = REVEAL_ROOT + "/construction"
RECORD = "docs/phases/W8-D4-validation-record.md"
SELF_REL = "tests/test_w8_validation_reveal.py"
ENVELOPE = "tests/test_w8_discriminating_instrument_envelope.py"
LAWMOD = "tests/test_w8_validation_law.py"
LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
ADR54 = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
COMPLETION_RECORD = "docs/phases/W8-D4-completion-record.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, ENVELOPE, LAWMOD, REGISTRY,
                          BOARD})
TOTAL = 18
LATER_DELIVERABLES = ("W8-D5", "W8-D6", "W8-D7")
EARLIER_D4 = frozenset({"W8-D4-IVB", "ADR-0060", "W8-D4-VCR", "W8-V1-CM-01",
                        "W8-V1-CM-02", "W8-D4-VSR", "W8-D4-DR-01"})

# The helper modules whose snapshot bytes the proofs execute.
HELPERS = {"env": ENVELOPE, "law": LAWMOD,
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": "tests/test_w8_session_recovery_law.py",
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py"}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    ENVELOPE: ("envelope module",
               "sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700", "3e1b4d4fedc2ab322a7d0cf9b090f78078b25ac3"),
    LAWMOD: ("validation-law module",
             "sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113", "609989bfe7004fddebe760cb92a7ff8d692ad0af"),
    REGISTRY: ("registry",
               "sha256:14aa003d4a578f7a22513e9f069df087b377667cf2b6aab64f3e9df7dbfbc015",
               "2e065b282213186873615e40e56d7a1cd950d1b4"),
    BOARD: ("board",
            "sha256:60eea89a6c06f5575cb413d199c831c14a934a6f092b10449d99b179f389c613",
            "5835fbec08d74631a08740a4d748adb025949824"),
}
# The reviewed post-images of the two successions: (LF SHA-256, blob).
POSTIMAGE = {ENVELOPE: ("sha256:d4685301e949b072510b38862dc59ebdcef9e383cc549d186712940c3d8fba4c", "ec932062722d07a7d109dc3a3a90d1dfc38f9895"),
             LAWMOD: ("sha256:66a16bf2fe7cd71ff0dd382dbe30ce9b1afc35da5d90060082c7a79960ad6c50", "71b33fd6d7415a691fc8e6d1a426e1fa7c4aa29e")}

# ----------------------------------------- the two staged successions (d38)
SITES = {
    ENVELOPE: (
        ('V12',
         '                if p.startswith("governance/discriminating-reveal/"):\n                    continue\n',
         '                if p.startswith("governance/discriminating-reveal/"):\n                    continue\n                # Succeeded at the W8-D4 reveal landing (ADR-0060 Part J\n                # decision 38): the validation authoring reveal home is\n                # admitted beside it.\n                if p.startswith("governance/validation-reveal/authoring/"):\n                    continue\n'),
    ),
    LAWMOD: (
        ('VL10',
         'SESSION_IDS = frozenset({"W8-D4-VSR", "W8-D4-DR-01"})\n',
         'SESSION_IDS = frozenset({"W8-D4-VSR", "W8-D4-DR-01"})\n# Admitted at the reveal landing (ADR-0060 Part J decision 38): the two\n# reveal homes for the validation corpus\'s identities, the construction\n# reveal home joining the holders of the construction schema literal, and\n# the validation record with its W8-D4 entry. The session-stage state stays\n# proven at the session landing commit.\nD4D_LANDING = "44947adf9b60f2ce462be97a2c0e628a3ecbdd89"\nREVEAL_HOMES = (VALIDATION_HOMES[2] + "/authoring",\n                VALIDATION_HOMES[2] + "/construction")\nVALIDATION_RECORD = LATER_RECORDS[2]\nREVEAL_IDS = frozenset({"W8-D4-VRC"})\n'),
        ('VL10',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None, session=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it. Succeeded at the session\n    landing: `session` is that landing\'s admitted path set - the\n    register and the session record - or None for the state before it."""\n    admitted = frozenset(corpus or ()) | frozenset(session or ())\n    landed = corpus is not None\n    held = session is not None\n    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n           | (SESSION_IDS if held else frozenset()))\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())\n                  | ({VALIDATION_HOMES[1]} if held else set()))\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None, session=None,\n                              reveal=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it. Succeeded at the session\n    landing: `session` is that landing\'s admitted path set - the\n    register and the session record - or None for the state before it.\n    Succeeded at the reveal landing: `reveal` is that landing\'s admitted\n    path set - both reveal homes\' records and the validation record - or\n    None for the state before it."""\n    admitted = (frozenset(corpus or ()) | frozenset(session or ())\n                | frozenset(reveal or ()))\n    landed = corpus is not None\n    held = session is not None\n    shown = reveal is not None\n    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n           | (SESSION_IDS if held else frozenset())\n           | (REVEAL_IDS if shown else frozenset()))\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    if shown:\n        holders_ok |= {p for p in reveal\n                       if p.startswith(REVEAL_HOMES[1] + "/")}\n    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())\n                  | ({VALIDATION_HOMES[1]} if held else set())\n                  | ({VALIDATION_HOMES[2]} if shown else set()))\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n\n\ndef reveal_admitted():\n    """The reveal landing\'s admitted paths: both reveal homes\' records for\n    the identities the corpus landing\'s committed commitment manifest\n    binds, and the validation record."""\n    rows = json.loads(committed(D4C_LANDING, CORPUS_MANIFEST))["rows"]\n    return ({VALIDATION_RECORD}\n            | {"%s/%s.json" % (home, r["case_id"])\n               for home in REVEAL_HOMES for r in rows})'),
        ('VL10',
         '    def test_vl10_no_later_artefact_before_its_own_landing(self):\n        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names. Succeeded at the corpus landing and again at\n        # the session landing: each former state stays proven at its own\n        # landing commit, and the present admits exactly the landed\n        # artefacts.\n        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()\n        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[\n            "entries"]\n        before_holders = schema_holders(\n            before, lambda p: committed(D4B_LANDING, p))\n        with self.subTest(fact="nothing later existed at the D4-B landing"):\n            self.assertEqual(staged_absence_violations(\n                before, lambda p: False, before_entries, before_holders), [])\n            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))\n        at_corpus = _git("ls-tree", "-r", "--name-only", D4C_LANDING).split()\n        corpus_entries = json.loads(committed(D4C_LANDING, REGISTRY))[\n            "entries"]\n        corpus_holders = schema_holders(\n            at_corpus, lambda p: committed(D4C_LANDING, p))\n        corpus = corpus_admitted(lambda rel: committed(D4C_LANDING, rel))\n        with self.subTest(fact="nothing of the session existed at the corpus "\n                               "landing"):\n            self.assertEqual(staged_absence_violations(\n                at_corpus, lambda p: False, corpus_entries, corpus_holders,\n                corpus), [])\n            self.assertEqual(sorted(corpus_holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        session = {SESSION_REGISTER, SESSION_RECORD}\n        with self.subTest(fact="exactly the corpus and session landings\' "\n                               "artefacts are admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus, session), [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module and the construction manifest"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        planted_entry = dict(entries[-1], id="W8-D4-VRC", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session),\n                "an extra file in the register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus, session),\n                "a reveal-home path": (\n                    tracked + [VALIDATION_HOMES[2] + "/authoring/x.json"],\n                    exists, entries, holders, corpus, session),\n                "a validation record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[2], entries,\n                    holders, corpus, session),\n                "a premature validation-record entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus, session),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus,\n                    session),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None, session),\n                "the session artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n',
         '    def test_vl10_no_later_artefact_before_its_own_landing(self):\n        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names. Succeeded at the corpus, session and reveal\n        # landings: each former state stays proven at its own landing\n        # commit, and the present admits exactly the landed artefacts.\n        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()\n        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[\n            "entries"]\n        before_holders = schema_holders(\n            before, lambda p: committed(D4B_LANDING, p))\n        with self.subTest(fact="nothing later existed at the D4-B landing"):\n            self.assertEqual(staged_absence_violations(\n                before, lambda p: False, before_entries, before_holders), [])\n            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))\n        at_corpus = _git("ls-tree", "-r", "--name-only", D4C_LANDING).split()\n        corpus_entries = json.loads(committed(D4C_LANDING, REGISTRY))[\n            "entries"]\n        corpus_holders = schema_holders(\n            at_corpus, lambda p: committed(D4C_LANDING, p))\n        corpus = corpus_admitted(lambda rel: committed(D4C_LANDING, rel))\n        with self.subTest(fact="nothing of the session existed at the corpus "\n                               "landing"):\n            self.assertEqual(staged_absence_violations(\n                at_corpus, lambda p: False, corpus_entries, corpus_holders,\n                corpus), [])\n            self.assertEqual(sorted(corpus_holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        session = {SESSION_REGISTER, SESSION_RECORD}\n        at_session = _git("ls-tree", "-r", "--name-only", D4D_LANDING).split()\n        session_entries = json.loads(committed(D4D_LANDING, REGISTRY))[\n            "entries"]\n        session_holders = schema_holders(\n            at_session, lambda p: committed(D4D_LANDING, p))\n        with self.subTest(fact="nothing of the reveal existed at the session "\n                               "landing"):\n            self.assertEqual(staged_absence_violations(\n                at_session, lambda p: False, session_entries,\n                session_holders, corpus, session), [])\n            self.assertEqual(sorted(session_holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        reveal = reveal_admitted()\n        construction_reveal = sorted(p for p in reveal\n                                     if p.startswith(REVEAL_HOMES[1] + "/"))\n        with self.subTest(fact="exactly the corpus, session and reveal "\n                               "landings\' artefacts are admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus, session, reveal),\n                [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module, the construction manifest and "\n                               "the construction reveal home"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST] + construction_reveal))\n            self.assertEqual(len(construction_reveal), 18)\n        planted_entry = dict(entries[-1], id="W8-D4-CPR", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "an extra file in the register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "an unbound reveal-home path": (\n                    tracked + [REVEAL_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "a path under the reveal root itself": (\n                    tracked + [VALIDATION_HOMES[2] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "a completion record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[3], entries,\n                    holders, corpus, session, reveal),\n                "a premature completion entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus, session, reveal),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus,\n                    session, reveal),\n                "a construction schema literal in the authoring home": (\n                    tracked, exists, entries,\n                    holders + [REVEAL_HOMES[0] + "/W8-C-x.json"], corpus,\n                    session, reveal),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None, session, reveal),\n                "the session artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, None, reveal),\n                "the reveal artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, session,\n                    None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n'),
    ),
}
D38_CLAUSE = ("the envelope module's authoring-schema limb admits exactly "
              "the validation authoring reveal home beside the W8-D3 reveal "
              "home; and VL10 admits exactly the two reveal homes for the "
              "validation corpus's identities, the construction reveal home "
              "joining the holders of the construction schema literal, and "
              "the validation record with its W8-D4 entry.")

# The record's three tables, each read whole.
COMPARISON_SECTION = "## 3. The case-level comparison"
COMPARISON_HEADER = ("| Case identity | Human token | Authored intended "
                     "token | Relation |")
COMPARISON_SEPARATOR = "|---|---|---|---|"
COUNTS_SECTION = "## 4. The permitted counts"
COUNTS_HEADER = "| Kind | Count | Statement |"
COUNTS_SEPARATOR = "|---|---|---|"
SUCCESSION_SECTION = "## 5. Proof successions at this landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
CELL_CODE = re.compile(r"`([^`\s]+)`")
CELL_COUNT = re.compile(r"(0|[1-9][0-9]*)")
# Derived figures (ADR-0060 decision 35), as textual mechanics over the
# record outside its two validated tables: a percent or proportion form, a
# fraction, a decimal, a value beside a figure word, or a count beside a
# kind or token. The record's own negations ("no rate, score ...") carry no
# value and pass; VR8 proves them present. No semantic reading is claimed.
PERCENT = re.compile(r"%|\bper cent\b|\bpercent\b|\baccuracy\b|"
                     r"\bproportion\b|\bprecision\b|\brecall\b")
FRACTION = re.compile(r"\b\d+\s*/\s*\d+\b|\b\d+\s+(?:in|of|out of)\s+\d+\b")
DECIMAL = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])")
FIGURE_WORDS = ("rate", "ratio", "score", "grade", "percentage", "proportion",
                "share", "mean", "average", "accuracy", "threshold", "ranking")
FIGURE_VALUE = re.compile(
    r"\b(?:%s)s?\b[^\w\n]{0,3}(?:(?:of|for|at|is|was|equals|to)\b[^\w\n]{0,3})?"
    r"[-+]?\d" % "|".join(FIGURE_WORDS), re.I)

# --------------------------------------- board and registry: authorised edits
VRC_LINK = ("([`W8-D4-validation-record.md`]"
            "(W8-D4-validation-record.md))")
VRC_STATUS_TAIL = (
    "the exact retained bytes of the validation corpus's eighteen authoring "
    "records and eighteen construction records, every commitment reproduced "
    "before any parse, with the case-level comparison of each human token "
    "to its authored intended token as agreement or divergence and the two "
    "permitted count kinds; it diagnoses nothing, amends no disposition and "
    "derives no rate, score or readiness interpretation.")
VRC_STATUS = {
    "draft": ("**A draft validation record, `W8-D4-VRC`, is before the "
              "human reviewer** " + VRC_LINK + ": if accepted, it would "
              "publish " + VRC_STATUS_TAIL),
    "accepted": ("**`W8-D4-VRC` — the validation record — is accepted** "
                 + VRC_LINK + " — accepted %s: it publishes "
                 + VRC_STATUS_TAIL),
}
VRC_ROW = ("| W8-D4 — Validation Record (W8-D4-VRC) | "
           "[`W8-D4-validation-record.md`](W8-D4-validation-record.md) | ")
VRC_ROW_BODY = (
    "Tier J: **the D4-E reveal, comparison and counts** — every published "
    "authoring and construction commitment of the validation corpus `W8-V1` "
    "reproduced from the exact retained bytes before any parse, the exact "
    "bytes copied to the two reveal homes and scanned there, never in "
    "custody, and parsed only after a clean scan; every revealed record "
    "passing its published validator and bound to its case, its filename, "
    "both manifest rows and the published visible digest, methods admitted "
    "for their classes and family seeds verified; the comparison of each "
    "human token to its authored intended token as agreement or divergence, "
    "and the two permitted count kinds, each carrying its statement; the "
    "envelope authoring-schema limb and the validation law's VL10 "
    "succeeding by exact transformation. **No disposition amended; no "
    "divergence diagnosed, explained away or corrected; no rate, score or "
    "readiness derived; D4-F is the human authority's decision; W8-D5 to "
    "W8-D7 stay closed.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = "remote-verified. **No divergence is diagnosed"
BOARD_ROW_HEAD = "| W8-D4 — Validation Session (record, W8-D4-VSR) | "
VRC_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
VRC_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D4-VRC", "path": RECORD, "type": "phase-record",
    "title": "W8-D4 - Validation Record",
    "role": (
        "The W8-D4 validation record of landing D4-E, the reveal of the "
        "validation corpus W8-V1: every published authoring and construction "
        "commitment reproduced by hashing the exact retained bytes before "
        "any parse, the exact bytes copied to the two reveal homes of "
        "ADR-0060 decision 23, scanned there and never in custody, and "
        "parsed only after a clean scan; every revealed authoring record "
        "bound to its identity, filename, manifest row and published "
        "visible digest, every revealed construction record bound to its "
        "case, authored class and authoring commitment with methods "
        "admitted for their classes and family seeds verified, and the "
        "construction manifest bound in every direction. Carries exactly "
        "the case-level comparison of each human token to its authored "
        "intended token as agreement or divergence, and exactly the two "
        "permitted count kinds, each carrying its statement; organises no "
        "outcome by method or family; amends no disposition; diagnoses, "
        "explains away and corrects nothing; derives no rate, score or "
        "readiness interpretation. Moves exactly the envelope "
        "authoring-schema limb and the validation law's VL10 by exact "
        "transformation, with proof obligations VR1 to VR12. Diagnosis, if "
        "the human authority so decides, belongs to D4-F."),
    "depends_on": ["ADR-0060", "W8-D4-VSR", "W8-D4-DR-01", "W8-D4-VCR",
                   "W8-V1-CM-01", "W8-V1-CM-02", "W8-D4-IVB", "W8-CHC",
                   "ADR-0057", "ADR-0058", "ADR-0054", "ADR-0055",
                   "W8-D2-CBC", "ADR-0056", "W8-AR", "W7-CR"]}
REQUIRED = (
    "refused exactly the successions ADR-0060 decision 38 stages for it.",
    "reproduced by hashing the exact retained bytes directly, read-only, "
    "before any parse",
    "No retained record of either earlier corpus was listed, opened, "
    "parsed, hashed, copied or moved by any act of this landing",
    "Only after every commitment reproduced were the exact retained bytes "
    "copied",
    "The landing scan ran over exactly the thirty-six candidate copies and "
    "found nothing; the scanner was never run against the custody "
    "location.",
    "The location is never named in any surface.",
    "Only after that clean scan were the copies parsed.",
    "A proof over named custody records establishes binding mechanics only;",
    "The reveal publishes the exact retained bytes",
    "are not individually registered.",
    "That is the whole of the comparison.",
    "An authored intended token is a construction hypothesis, never an "
    "answer key and never a certified correct answer.",
    "Revealed material never becomes retroactive disposition evidence.",
    "The dispositions were fixed at the session landing's publication, and "
    "none is amended by any route.",
    "this record organises no outcome by them",
    "No count by method, family or class is published",
    "Diagnosis is not this record's act.",
    "No other existing proof moves at this landing.",
    "This landing's census is exactly forty-two paths:",
    "No corpus home, register or session record is touched.",
    "W8-D5 through W8-D7 remain closed behind their own briefs.",
    "Neither this record nor any of its green proofs supplies any of those "
    "conclusions.",
    "this record neither performs that weighing nor authorises W8-D5 to open",
)
# Wording withdrawn at r2: an unqualified bar on later evidence use would
# repeat the restriction ADR-0060 decision 48 removed, which preserves the
# separately governed weighing W8-D4-IVB item 14 reserves to W8-D5.
WITHDRAWN = ("may be cited as evidence",
             "may not be cited as evidence",
             "cannot be cited as evidence")


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


def worktree(rel):
    """A candidate surface before this landing's commit exists: a revealed
    file is read as its raw, unconverted bytes; every other surface keeps
    its LF treatment."""
    raw = (ROOT / rel).read_bytes()
    return raw if rel.startswith(REVEAL_ROOT + "/") else _lf(raw)


def l10_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added this record, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the validation record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return worktree(rel) if commit is None else committed(commit, rel)


def snapshot():
    commit, problems = l10_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot: the bytes
    `read` yields for `rel`, executed in a fresh private namespace that is
    registered nowhere."""
    ns = {"__name__": "_w8_vrc_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def manifest_rows():
    return json.loads(committed(CORPUS, MANIFEST))["rows"]


def construction_rows():
    return json.loads(committed(CORPUS, CMANIFEST))["rows"]


def manifest_ids():
    return [r["case_id"] for r in manifest_rows()]


def foreign_ids():
    out = set()
    for rel in FOREIGN_MANIFESTS:
        out |= {r["case_id"] for r in json.loads(committed(CORPUS, rel))[
            "rows"]}
    return out


def visible_bytes():
    return {c: committed(CORPUS, "%s/%s.json" % (HOME, c))
            for c in manifest_ids()}


def reveal_paths(home):
    return sorted("%s/%s.json" % (home, c) for c in manifest_ids())


def revealed(read, home):
    return {c: read("%s/%s.json" % (home, c)) for c in manifest_ids()}


def published_commitments():
    return ({r["case_id"]: r["authoring_commitment_sha256"]
             for r in manifest_rows()},
            {r["case_id"]: r["construction_commitment_sha256"]
             for r in construction_rows()})


def register_rows():
    return json.loads(committed(BASELINE, REGISTER))["rows"]


def home_closure_violations(tracked, on_disk, home):
    expected = reveal_paths(home)
    v = []
    if sorted(p for p in tracked if p.startswith(home + "/")) != expected:
        v.append("the tracked reveal home differs from the bound set")
    if sorted(on_disk) != expected:
        v.append("the reveal home on disk differs from the bound set")
    return v


def authoring_binding_violations(rows, visible, revealed_auth, h):
    """Every revealed authoring record: the published withheld-record
    validator, its identity equal to its filename and manifest row, its
    visible digest equal to the row and to the published visible bytes,
    canonical bytes, and the manifest binding in both directions."""
    v = h.env.manifest_binding_violations(rows, visible, revealed_auth)
    for row in rows:
        cid = row["case_id"]
        if cid not in revealed_auth:
            continue
        try:
            rec = json.loads(revealed_auth[cid])
        except ValueError:
            v.append("a revealed authoring record is not JSON")
            continue
        v += h.env.authoring_record_violations(rec)
        v += h.env.cross_binding_violations(json.loads(visible[cid]),
                                            visible[cid], rec)
        if rec.get("case_id") != cid:
            v.append("a revealed identity differs from its filename")
        if rec.get("reviewer_visible_sha256") != row["reviewer_visible_sha256"]:
            v.append("a revealed visible digest differs from its row")
        if revealed_auth[cid] != h.env.canonical_bytes(rec):
            v.append("a revealed authoring record is not in canonical bytes")
    return v


def construction_binding_violations(rows, visible, revealed_auth,
                                    revealed_cons, cmanifest_raw, h):
    """Every revealed construction record: Part E's validator bound to its
    case, its authored class and its authoring commitment; identity and
    digest equal to its filename and row; the construction manifest bound
    in every direction; and the family rule over the corpus."""
    v = []
    parsed = {}
    for row in rows:
        cid = row["case_id"]
        if cid not in revealed_cons or cid not in revealed_auth:
            v.append("a construction record or its authoring record is "
                     "missing")
            continue
        try:
            auth = json.loads(revealed_auth[cid])
            vis = json.loads(visible[cid])
        except ValueError:
            v.append("an authoring record or case is not JSON")
            continue
        v += h.law.construction_record_violations(
            revealed_cons[cid], vis, auth.get("authored_class"),
            row["authoring_commitment_sha256"])
        try:
            rec = json.loads(revealed_cons[cid])
        except ValueError:
            continue
        if rec.get("case_id") != cid:
            v.append("a construction identity differs from its filename")
        if rec.get("reviewer_visible_sha256") != row["reviewer_visible_sha256"]:
            v.append("a construction visible digest differs from its row")
        parsed[cid] = rec
    v += h.law.construction_manifest_violations(cmanifest_raw, rows,
                                                revealed_cons)
    if len(parsed) == len(rows):
        v += h.law.family_violations({c: json.loads(visible[c])
                                      for c in parsed}, parsed)
    return v


def observed_binding():
    return {"commit": CORPUS,
            "home_tree": _git("rev-parse", CORPUS + ":" + HOME).strip(),
            "commitment": _sha(_lf(committed(CORPUS, MANIFEST))),
            "construction": _sha(_lf(committed(CORPUS, CMANIFEST)))}


def recorded_binding(h):
    """The four values the published session record carries, read whole
    from its binding table at the baseline."""
    text = _lf(committed(BASELINE, SESSION_RECORD)).decode("utf-8")
    rows, v = h.rev.closed_table(text, "## 2. The register and the bindings",
                                 "| Binding | Value |", "|---|---|", 2)
    d = {r[0]: r[1].strip("`") for r in rows if len(r) == 2}
    return {"commit": d.get("Corpus landing commit"),
            "home_tree": d.get("Case home tree at that commit"),
            "commitment": d.get("Commitment manifest LF SHA-256"),
            "construction": d.get("Construction manifest LF SHA-256")}, v


def chain_violations(c):
    """The binding chain of ADR-0060 decision 25 through the reveal: the
    recorded binding is the published one at the corpus commit; the
    manifests, the register and both reveal sets are each exactly the bound
    identities; the reveal follows the full gate."""
    v = []
    if c["recorded"] != c["observed"] or any(
            x in (None, "") for x in c["recorded"].values()):
        v.append("the recorded binding is not the published one")
    ids = c["manifest_ids"]
    if len(ids) != TOTAL or len(set(ids)) != TOTAL or ids != sorted(ids):
        v.append("the bound manifest is not eighteen distinct identities in "
                 "order")
    if c["construction_ids"] != ids:
        v.append("the construction manifest is not one-to-one")
    if set(ids) & set(c["foreign_ids"]):
        v.append("an identity of an earlier corpus is bound")
    if c["register_ids"] != ids:
        v.append("the register rows are not exactly the bound identities")
    for name in ("authoring_reveal_ids", "construction_reveal_ids"):
        if c[name] != ids:
            v.append("%s is not exactly the bound identities" % name)
    if not all(c["gate"].get(k) is True for k in
               ("session_record_verified", "commitments_reproduced",
                "copies_scanned_clean")):
        v.append("the reveal gate is not fully passed")
    return v


def mechanical_comparison(register, revealed_auth, h):
    human = {r["case_id"]: r["disposition"] for r in register}
    out = []
    for cid in sorted(revealed_auth):
        intended = json.loads(revealed_auth[cid])["intended_disposition"]
        out.append((cid, human[cid], intended,
                    h.cal.relation(human[cid], intended)))
    return out


def mechanical_counts(comparison, h):
    return h.cal.counts([{"disposition": hum} for _, hum, _, _ in comparison],
                        [rel for _, _, _, rel in comparison])


def count_order(h):
    return list(h.pkt.TOKENS) + list(h.cal.RELATIONS)


def comparison_violations(text, expected, h):
    """The comparison table, whole: exactly eighteen rows in ascending
    identity order, each exactly the four permitted fields with lawful
    tokens and a closed relation, and exactly the mechanical comparison."""
    rows, v = h.rev.closed_table(text, COMPARISON_SECTION, COMPARISON_HEADER,
                                 COMPARISON_SEPARATOR, 4)
    parsed = []
    for cells in rows:
        m = [CELL_CODE.fullmatch(c) for c in cells]
        if not all(m):
            v.append("a malformed comparison cell")
            continue
        cid, human, intended, rel = (x.group(1) for x in m)
        if not h.env.CASE_ID_RE.fullmatch(cid):
            v.append("a malformed identity cell")
        if human not in h.pkt.TOKENS or intended not in h.pkt.TOKENS:
            v.append("a token outside the closed set")
        if rel not in h.cal.RELATIONS:
            v.append("a relation outside the closed set")
        parsed.append((cid, human, intended, rel))
    if len(rows) != TOTAL:
        v.append("the table does not hold exactly eighteen rows")
    ids = [p[0] for p in parsed]
    if len(ids) != len(set(ids)):
        v.append("a duplicate row")
    if ids != sorted(ids):
        v.append("rows are not in ascending identity order")
    if parsed != list(expected):
        v.append("the rows are not exactly the mechanical comparison")
    return v


def counts_violations(text, expected, h):
    """The count table, whole: exactly the five permitted kinds in fixed
    order, each an integer count equal to the mechanical one and carrying
    exactly its statement."""
    rows, v = h.rev.closed_table(text, COUNTS_SECTION, COUNTS_HEADER,
                                 COUNTS_SEPARATOR, 3)
    kinds = []
    for cells in rows:
        kind = CELL_CODE.fullmatch(cells[0])
        if not kind:
            v.append("a malformed or unknown count kind")
            continue
        if not CELL_COUNT.fullmatch(cells[1]):
            v.append("an invalid count cell")
            continue
        if cells[2] != h.cal.COUNT_STATEMENT:
            v.append("a count without its exact statement")
        kinds.append(kind.group(1))
        exp = expected.get(kind.group(1))
        if exp is None or int(cells[1]) != exp["count"]:
            v.append("a count differs from the mechanical one")
    if kinds != count_order(h):
        v.append("the kinds are not exactly the five permitted, in fixed "
                 "order")
    return v


def succession_rows(h):
    return [["`%s`" % rel, ", ".join(h.auth.labels(SITES[rel])),
             "`%s`" % PREIMAGE[rel][1], "`%s`" % POSTIMAGE[rel][0]]
            for rel in (ENVELOPE, LAWMOD)]


def succession_table_violations(record, h):
    rows, v = h.rev.closed_table(record, SUCCESSION_SECTION,
                                 SUCCESSION_HEADER, SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted rows, in "
                 "order")
    return v


def succession_violations(rel, present, record, h, sites=None):
    sites = SITES[rel] if sites is None else sites
    v = []
    pre = _lf(committed(BASELINE, rel)).decode("utf-8")
    if _sha(pre.encode("utf-8")) != PREIMAGE[rel][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[rel][0]:
        v.append("the bytes are not the reviewed post-image")
    return v + succession_table_violations(record, h)


def carriage_violations(text):
    flat = _flat(text)
    v = ["missing or repeated: %s" % s[:48] for s in REQUIRED
         if flat.count(s) != 1]
    v += ["withdrawn wording present: %s" % w for w in WITHDRAWN if w in flat]
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def vrc_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and VRC_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (VRC_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_row_anchor(board_pre):
    rows = [l for l in board_pre.split("\n") if l.startswith(BOARD_ROW_HEAD)]
    return rows[0] + "\n" if len(rows) == 1 else None


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    anchor = board_row_anchor(board_pre)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "remote-verified. " + fill(VRC_STATUS[state])
         + " **No divergence is diagnosed"),
        ("row", anchor,
         anchor + VRC_ROW + fill(ROW_PREFIX[state]) + VRC_ROW_BODY + " |\n"),
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


def expected_registry(base_text, record_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, record_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    """The wording this landing adds to the board in both lawful states, the
    accepted forms dated with a sample so that no format sign remains."""
    sample = "2026-01-01"
    return " ".join([VRC_ROW, VRC_ROW_BODY, VRC_STATUS["draft"],
                     VRC_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def reserved_literals(h):
    return (tuple(sorted(h.pkt.TOKENS)),
            (h.pkt.PACKET_SCHEMA, h.cal.REGISTER_SCHEMA, h.env.AUTHORING_SCHEMA)
            + tuple(h.law.NEW_SCHEMAS),
            tuple(sorted(h.law.ADMITS)))


def withheld_texts(revealed_auth, revealed_cons):
    """The free-text fields the revealed records carry, which must leave the
    reveal homes through no other surface."""
    out = set()
    for raw in revealed_auth.values():
        rec = json.loads(raw)
        out.add(rec["authoring_rationale"])
        out.add(rec["commitment_nonce"])
    for raw in revealed_cons.values():
        rec = json.loads(raw)
        out.add(rec["method_note"])
        out.add(rec["construction_nonce"])
    return {t for t in out if isinstance(t, str) and len(t) >= 16}


def count_beside_kind(tokens):
    kinds = "|".join(["agreements?", "divergences?", "cases? agree"]
                     + [re.escape(t) for t in sorted(tokens)])
    return re.compile(r"\b\d+\s+(?:%s)\b|\b(?:%s)\b\s*[:=]?\s*\d+\b"
                      % (kinds, kinds))


def figure_hits(text, tokens):
    """Labelled derived-figure forms in a text that should carry none."""
    v = ["a percent or proportion form: %s" % x for x in PERCENT.findall(text)]
    v += ["a fraction: %s" % x for x in FRACTION.findall(text)]
    v += ["a decimal: %s" % x for x in DECIMAL.findall(text)]
    v += ["a value beside a figure word: %s" % x
          for x in FIGURE_VALUE.findall(text)]
    v += ["a count beside a kind: %s" % x
          for x in count_beside_kind(tokens).findall(text)]
    return v


def derived_figure_violations(record, counts, comparison, h):
    """The record outside its two validated tables - the exact mechanical
    count rows and comparison rows removed, digests and commit identities
    removed - carries no derived-figure form."""
    text = record
    for kind in count_order(h):
        row = "| `%s` | %d | %s |" % (kind, counts[kind]["count"],
                                      h.cal.COUNT_STATEMENT)
        text = text.replace(row, "", 1)
    for cid, hum, intended, rel in comparison:
        text = text.replace("| `%s` | `%s` | `%s` | `%s` |"
                            % (cid, hum, intended, rel), "", 1)
    text = h.rec.DIGEST.sub("", text)
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", "", text)
    return figure_hits(text, h.pkt.TOKENS)


def exposure_violations(text, h, withheld, allow_tokens=False):
    """No reserved authoring label, schema literal, method label, withheld
    text, count statement, derived figure or count beside a kind; tokens
    only where the record's own comparison lawfully carries them."""
    v = ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    tokens, schemas, methods = reserved_literals(h)
    v += ["a schema literal is present" for s in schemas if s in text]
    v += ["a method label: %s" % m for m in methods
          if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]
    v += ["withheld text is present" for w in withheld if w in text]
    if not allow_tokens:
        v += ["a token is present" for t in tokens if t in text]
        if h.cal.COUNT_STATEMENT in text:
            v.append("a count statement is present")
        v += figure_hits(text, tokens)
    return v


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted
    to call is replaced and the previous state restored on exit, tolerating
    a name a later landing has renamed or removed."""

    ABSENT = object()
    TARGETS = (
        ("test_w8_discriminating_instrument_envelope", "reveal_violations",
         lambda *a, **k: []),
        ("test_w8_discriminating_instrument_envelope",
         "authoring_record_violations", lambda *a, **k: []),
        ("test_w8_validation_law", "construction_record_violations",
         lambda *a, **k: []),
        ("test_w8_validation_law", "family_violations", lambda *a, **k: []),
        ("test_w8_calibration_law", "relation", lambda a, b: "agreement"),
        ("test_w8_calibration_law", "counts", lambda *a, **k: {}),
        ("test_w8_session_recovery_law", "R9_REVEAL", "mechanics sentinel"),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_recovery_authority", "apply_sites",
         lambda text, sites: (text, [])),
        ("test_w8_reveal_calibration", "closed_table",
         lambda *a, **k: ([], [])),
    )

    @classmethod
    def state(cls):
        return {(m, n): getattr(importlib.import_module(m), n, cls.ABSENT)
                for m, n, _ in cls.TARGETS}

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
class VR1_RevealHomesClosure(unittest.TestCase):
    def test_vr1_each_home_holds_exactly_the_corpus(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        ids = manifest_ids()
        with self.subTest(fact="eighteen, the validation corpus only"):
            self.assertEqual(len(ids), TOTAL)
            self.assertFalse(set(ids) & foreign_ids())
        with self.subTest(fact="no reveal home at the baseline"):
            self.assertEqual([p for p in _git(
                "ls-tree", "-r", "--name-only", BASELINE).split()
                if p.startswith(REVEAL_ROOT + "/")], [])
        tracked = snapshot_tracked(commit)
        for home in (AUTH_HOME, CONS_HOME):
            on_disk = ([home + "/" + p.name for p in (ROOT / home).iterdir()]
                       if (ROOT / home).is_dir() else [])
            with self.subTest(fact="exactly the eighteen, tracked and on "
                                   "disk", home=home.rsplit("/", 1)[1]):
                self.assertEqual(home_closure_violations(tracked, on_disk,
                                                         home), [])
            good = reveal_paths(home)
            for name, (t, d) in {
                    "an extra tracked path": (good + [home + "/x.json"], good),
                    "an extra file on disk": (good, good + [home + "/y"]),
                    "a missing record": (good[1:], good[1:]),
                    "a foreign identity": (good[1:] + [
                        "%s/%s.json" % (home, sorted(foreign_ids())[0])],
                        good)}.items():
                with self.subTest(control="%s is refused" % name,
                                  home=home.rsplit("/", 1)[1]):
                    self.assertTrue(home_closure_violations(t, d, home))
        with self.subTest(fact="nothing under the reveal root outside the "
                               "two homes"):
            self.assertEqual([p for p in tracked
                              if p.startswith(REVEAL_ROOT + "/")
                              and not p.startswith((AUTH_HOME + "/",
                                                    CONS_HOME + "/"))], [])


class VR2_ExactRetainedBytes(unittest.TestCase):
    def test_vr2_every_revealed_file_hashes_to_its_commitment(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env")
        pub_auth, pub_cons = published_commitments()
        rev_auth, rev_cons = revealed(read, AUTH_HOME), revealed(read,
                                                                 CONS_HOME)
        with self.subTest(fact="eighteen authoring commitments reproduce"):
            self.assertEqual(h.env.reveal_violations(pub_auth, rev_auth), [])
        with self.subTest(fact="eighteen construction commitments reproduce"):
            self.assertEqual(h.env.reveal_violations(pub_cons, rev_cons), [])
        with self.subTest(fact="no carriage return: the bytes are as "
                               "retained"):
            self.assertTrue(all(b"\r" not in b for b in
                                list(rev_auth.values())
                                + list(rev_cons.values())))
        if commit is not None:
            with self.subTest(fact="working copies correspond to the "
                                   "committed objects"):
                for home, revs in ((AUTH_HOME, rev_auth),
                                   (CONS_HOME, rev_cons)):
                    for cid in revs:
                        self.assertEqual(_lf((ROOT / home / (cid + ".json"))
                                             .read_bytes()), revs[cid])
        cid = sorted(rev_auth)[0]
        for name, mutated in (
                ("a one-byte change", rev_auth[cid][:-2] + b" \n"),
                ("a line-ending conversion",
                 rev_auth[cid].replace(b"\n", b"\r\n")),
                ("a reserialisation", (json.dumps(json.loads(rev_auth[cid]),
                                                  indent=1) + "\n").encode()),
                ("a construction record under an authoring name",
                 rev_cons[cid])):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(h.env.reveal_violations(
                    pub_auth, dict(rev_auth, **{cid: mutated})))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env")
                self.assertEqual(hh.env.reveal_violations(pub_auth, rev_auth),
                                 [])
                self.assertTrue(hh.env.reveal_violations(
                    pub_auth, dict(rev_auth, **{cid: rev_auth[cid] + b" "})))


class VR3_RecordValidityAndBinding(unittest.TestCase):
    def test_vr3_records_valid_and_bound(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law")
        rows = manifest_rows()
        visible = visible_bytes()
        rev_auth, rev_cons = revealed(read, AUTH_HOME), revealed(read,
                                                                 CONS_HOME)
        cmanifest_raw = _lf(committed(CORPUS, CMANIFEST))
        with self.subTest(fact="every authoring record valid and bound"):
            self.assertEqual(authoring_binding_violations(
                rows, visible, rev_auth, h), [])
        with self.subTest(fact="every construction record valid and bound, "
                               "the construction manifest bound in every "
                               "direction, the family rule held"):
            self.assertEqual(construction_binding_violations(
                rows, visible, rev_auth, rev_cons, cmanifest_raw, h), [])
        cid, other = sorted(rev_auth)[0], sorted(rev_auth)[1]
        rec = json.loads(rev_auth[cid])
        for name, mutated in (
                ("another case's record under this name", rev_auth[other]),
                ("a wrong visible digest", h.env.canonical_bytes(
                    dict(rec, reviewer_visible_sha256="sha256:" + "0" * 64))),
                ("an out-of-vocabulary token", h.env.canonical_bytes(
                    dict(rec, intended_disposition="pass")))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(authoring_binding_violations(
                    rows, visible, dict(rev_auth, **{cid: mutated}), h))
        crec = json.loads(rev_cons[cid])
        methods = sorted(h.law.ADMITS)
        a_class = rec["authored_class"]
        foreign_method = next((m for m in methods
                               if a_class not in h.law.ADMITS[m]), None)
        cmutants = {
            "another case's construction record": rev_cons[other],
            "a wrong authoring commitment": h.env.canonical_bytes(dict(
                crec, authoring_commitment_sha256="sha256:" + "0" * 64)),
            "a seed carried by neither variant": h.env.canonical_bytes(dict(
                crec, family_seed_sha256="sha256:" + "1" * 64)),
            "a reserialised record": (json.dumps(crec, indent=1)
                                      + "\n").encode()}
        if foreign_method is not None:
            cmutants["a method not admitted for the class"] = \
                h.env.canonical_bytes(dict(crec, method=foreign_method))
        for name, mutated in cmutants.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(construction_binding_violations(
                    rows, visible, rev_auth, dict(rev_cons, **{cid: mutated}),
                    cmanifest_raw, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law")
                self.assertEqual(authoring_binding_violations(
                    rows, visible, rev_auth, hh), [])
                self.assertEqual(construction_binding_violations(
                    rows, visible, rev_auth, rev_cons, cmanifest_raw, hh), [])


class VR4_BindingChain(unittest.TestCase):
    def test_vr4_chain_holds_through_the_reveal(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev", "auth")
        recorded, v = recorded_binding(h)
        self.assertEqual(v, [])
        ids = manifest_ids()
        # The published gate vocabulary, as the W8-D3 reveal proofs carry
        # it: mechanics over the gate's names only, never proof that the
        # process duties behind them were honoured.
        gate = dict.fromkeys(h.auth.REVEAL_GATE, True)
        self.assertEqual(sorted(gate), ["commitments_reproduced",
                                        "copies_scanned_clean",
                                        "session_record_verified"])
        c = {"recorded": recorded, "observed": observed_binding(),
             "manifest_ids": ids,
             "construction_ids": [r["case_id"] for r in construction_rows()],
             "foreign_ids": sorted(foreign_ids()),
             "register_ids": [r["case_id"] for r in register_rows()],
             "authoring_reveal_ids": sorted(revealed(read, AUTH_HOME)),
             "construction_reveal_ids": sorted(revealed(read, CONS_HOME)),
             "gate": gate}
        with self.subTest(fact="the chain holds through the reveal"):
            self.assertEqual(chain_violations(c), [])
        with self.subTest(fact="the bound commit is the corpus commit, never "
                               "the session baseline"):
            self.assertEqual(c["observed"]["commit"], CORPUS)
            self.assertNotEqual(CORPUS, BASELINE)
        for name, mutated in (
                ("a premature reveal", dict(c, gate=dict(
                    gate, copies_scanned_clean=False))),
                ("a partial reveal", dict(c, authoring_reveal_ids=ids[1:])),
                ("a construction reveal out of step", dict(
                    c, construction_reveal_ids=ids[1:] + ids[:1])),
                ("a foreign-corpus reveal", dict(
                    c, authoring_reveal_ids=ids[1:] + c["foreign_ids"][:1])),
                ("a wrong recorded commit", dict(c, recorded=dict(
                    recorded, commit=BASELINE))),
                ("a missing recorded value", dict(c, recorded=dict(
                    recorded, construction=None)))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(chain_violations(mutated))


class VR5_Comparison(unittest.TestCase):
    def test_vr5_the_recorded_comparison_is_exactly_the_mechanical_one(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "pkt", "cal", "rev")
        record = read(RECORD).decode("utf-8")
        mech = mechanical_comparison(register_rows(), revealed(read, AUTH_HOME),
                                     h)
        with self.subTest(fact="exactly the mechanical comparison, read "
                               "whole"):
            self.assertEqual(len(mech), TOTAL)
            self.assertEqual(comparison_violations(record, mech, h), [])
        with self.subTest(fact="agreement exactly on byte-identical tokens"):
            for _, hum, intended, rel in mech:
                self.assertEqual(rel, "agreement" if hum == intended
                                 else "divergence")
        row = next(l for l in record.split("\n")
                   if l.startswith("| `W8-C-"))
        last = [l for l in record.split("\n") if l.startswith("| `W8-C-")][-1]
        top = COMPARISON_HEADER + "\n" + COMPARISON_SEPARATOR + "\n"
        rel_cell = row[row.rindex("| `") + 2:]
        flipped = row[:row.rindex("| `") + 2] + (
            "`divergence` |" if rel_cell.startswith("`agreement`")
            else "`agreement` |")
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
                self.assertTrue(comparison_violations(mutated, mech, h))
        for name, mutated in h.rev.boundary_mutants(
                record, COMPARISON_SECTION,
                last[:-1] + " mechanics sentinel |").items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(comparison_violations(mutated, mech, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "pkt", "cal", "rev")
                self.assertEqual(comparison_violations(
                    record, mechanical_comparison(
                        register_rows(), revealed(read, AUTH_HOME), hh), hh),
                    [])


class VR6_Counts(unittest.TestCase):
    def test_vr6_only_the_two_count_kinds_each_with_its_statement(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "pkt", "cal", "rev", "rec")
        record = read(RECORD).decode("utf-8")
        comparison = mechanical_comparison(register_rows(),
                                           revealed(read, AUTH_HOME), h)
        mech = mechanical_counts(comparison, h)
        self.assertEqual(h.cal.count_violations(mech), [])
        with self.subTest(fact="exactly the mechanical counts, read whole"):
            self.assertEqual(counts_violations(record, mech, h), [])
        with self.subTest(fact="the fixed order, zeros included, is the "
                               "permitted set"):
            self.assertEqual(sorted(mech), sorted(count_order(h)))
        with self.subTest(fact="no derived figure outside the two validated "
                               "tables"):
            self.assertEqual(derived_figure_violations(record, mech,
                                                       comparison, h), [])
        line = next(l for l in record.split("\n")
                    if l.startswith("| `agreement` |"))
        last = next(l for l in record.split("\n")
                    if l.startswith("| `divergence` |"))
        statement = h.cal.COUNT_STATEMENT

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
                self.assertTrue(counts_violations(mutated, mech, h))
        for name, mutated in h.rev.boundary_mutants(
                record, COUNTS_SECTION, "| `mechanics-sentinel` | 999 | "
                + statement + " |").items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(counts_violations(mutated, mech, h))
        anchor = "14. **Diagnosis is not this record's act.**"
        self.assertEqual(record.count(anchor), 1)

        def planted(sentence):
            return record.replace(anchor, sentence + "\n\n" + anchor, 1)
        for name, sentence in (
                ("a lawful negation", "No rate, score, grade, percentage or "
                                      "ranking is derived here."),
                ("a decision citation", "ADR-0060 decision 35 and item 14 "
                                        "of the brief bind this record."),
                ("a date", "The act is dated 2026-10-21."),
                ("a worded count", "Eighteen cases stand in the table.")):
            with self.subTest(positive_control="%s is accepted" % name):
                self.assertEqual(derived_figure_violations(
                    planted(sentence), mech, comparison, h), [])
        tok = sorted(h.pkt.TOKENS)[0]
        for name, sentence in (
                ("the decimal rate of the review's reproducer",
                 "Agreement rate: 0.5"),
                ("a rate with an equals sign", "rate = 0.5"),
                ("a rate with no punctuation", "rate 0.5"),
                ("a rate of an integer", "a rate of 3"),
                ("a score with a colon", "score: 3"),
                ("a percentage", "Agreement rate: 50%"),
                ("a slash fraction", "1/2 of the cases agree"),
                ("an in-fraction", "1 in 2 cases"),
                ("an of-fraction", "9 of 18 cases"),
                ("a bare decimal", "0.5"),
                ("a count beside a kind", "11 agreements"),
                ("a kind beside a count", "agreements: 11"),
                ("a count beside a token", "5 " + tok),
                ("a token beside a count", tok + ": 5"),
                ("a mean", "mean 2.0"),
                ("an accuracy", "accuracy 95"),
                ("a ranking value", "ranking: 1")):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(derived_figure_violations(
                    planted(sentence), mech, comparison, h))
        with self.subTest(control="a figure inside the count table's "
                                  "section, after the table, is refused"):
            self.assertTrue(derived_figure_violations(
                record.replace(last + "\n", last + "\n\nAgreement rate: "
                               "0.5\n", 1), mech, comparison, h))


class VR7_DispositionsFixed(unittest.TestCase):
    def test_vr7_register_and_session_record_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        for rel in (REGISTER, SESSION_RECORD):
            with self.subTest(path=rel):
                self.assertEqual(read(rel), committed(BASELINE, rel))
                self.assertEqual(_lf((ROOT / rel).read_bytes()),
                                 committed(BASELINE, rel))
        with self.subTest(control="a one-byte change is detected"):
            raw = committed(BASELINE, REGISTER)
            self.assertNotEqual(raw.replace(b"[", b"[ ", 1), raw)


class VR8_RecordCarriage(unittest.TestCase):
    def test_vr8_record_carries_its_statements(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        flat = _flat(text)
        for s in REQUIRED:
            with self.subTest(carried=s[:44]):
                self.assertEqual(flat.count(s), 1)
        with self.subTest(fact="no withdrawn evidence-bar wording"):
            self.assertEqual(carriage_violations(text), [])
        with self.subTest(control="a removed statement is detected"):
            self.assertTrue(carriage_violations(
                text.replace(REQUIRED[0], "", 1)))
        with self.subTest(control="a repeated statement is detected"):
            self.assertTrue(carriage_violations(
                text + "\n" + REQUIRED[-1] + "\n"))
        for bar in ("No disposition or count in this record may be cited as "
                    "evidence for any of those propositions.",
                    "Nothing here may not be cited as evidence.",
                    "This cannot be cited as evidence of adequacy."):
            with self.subTest(control="a planted evidence bar is detected"):
                self.assertTrue(carriage_violations(text + "\n" + bar + "\n"))
        with self.subTest(fact="the nine-rule block is byte-identical"):
            adr = _lf(committed(BASELINE, ADR54)).decode("utf-8")
            m = re.search(r"^> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                          r"failure\.\*\*)$", adr, re.M)
            self.assertIsNotNone(m)
            self.assertEqual(text.count("> %s\n" % m.group(1)), 1)
        with self.subTest(fact="the four-value binding is stated in the "
                               "header"):
            o = observed_binding()
            for value in o.values():
                self.assertIn("`%s`" % value, text)


class VR9_NoExposureBeyondTheComparison(unittest.TestCase):
    def test_vr9_only_the_authorised_fields_leave_the_reveal_homes(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor")
        record = read(RECORD).decode("utf-8")
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D4-VRC"]["role"] + " " + by_id["W8-D4-VRC"]["title"]
        withheld = withheld_texts(revealed(read, AUTH_HOME),
                                  revealed(read, CONS_HOME))
        self.assertTrue(withheld)
        with self.subTest(surface="record"):
            self.assertEqual(exposure_violations(record, h, withheld,
                                                 allow_tokens=True), [])
            pins = [p.split(":", 1)[1] for p in
                    [PREIMAGE[r][1] for r in (ENVELOPE, LAWMOD)]
                    + [POSTIMAGE[r][0] for r in (ENVELOPE, LAWMOD)]
                    + list(observed_binding().values())[2:]]
            no_ids = h.rec.CASE_ID_ANYWHERE.sub("", record)
            self.assertEqual([v for v in h.rec.exposure_violations(no_ids,
                                                                    pins)
                              if "digest" in v], [])
        for name, text in (("registry role and title", role),
                           ("board wording this landing adds",
                            added_board_wording())):
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(exposure_violations(text, h, withheld), [])
        tokens, schemas, methods = reserved_literals(h)
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([t for t in tokens if t in src], [])
            self.assertEqual([s for s in schemas if s in src], [])
            self.assertEqual([m for m in methods if re.search(
                r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), src)], [])
            self.assertIsNone(h.rec.CASE_ID_ANYWHERE.search(src))
        for name, plant in {
                "a reserved label": sorted(h.cor.RESERVED_FIELDS)[0],
                "a schema literal": schemas[0],
                "a method label": methods[0],
                "withheld text": sorted(withheld)[0],
                "a token": tokens[0],
                "a count statement": h.cal.COUNT_STATEMENT,
                "a count beside a kind": "with 11 agreements recorded",
                "a decimal rate": "an agreement rate of 0.5"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(
                    added_board_wording() + " " + plant, h, withheld))


class VR10_Successions(unittest.TestCase):
    def test_vr10_staged_successions_are_exact(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "law", "env")
        record = read(RECORD).decode("utf-8")
        for rel in (ENVELOPE, LAWMOD):
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(), PREIMAGE[rel][2])
            present = read(rel).decode("utf-8")
            with self.subTest(exact_succession=PREIMAGE[rel][0]):
                self.assertEqual(succession_violations(rel, present, record,
                                                       h), [])
                self.assertEqual(_blob(present.encode("utf-8")),
                                 POSTIMAGE[rel][1])
        with self.subTest(fact="ADR-0060 decision 38 stages exactly these"):
            self.assertIn(D38_CLAUSE, _flat(_lf(committed(BASELINE, LAW))
                                            .decode("utf-8")))
        with self.subTest(fact="the succeeded modules carry this landing's "
                               "constants"):
            self.assertEqual(tuple(h.law.REVEAL_HOMES), (AUTH_HOME, CONS_HOME))
            self.assertEqual(h.law.VALIDATION_RECORD, RECORD)
            self.assertEqual(h.law.REVEAL_IDS, frozenset({"W8-D4-VRC"}))
            self.assertEqual(h.law.D4D_LANDING, BASELINE)
            self.assertEqual(sorted(h.law.reveal_admitted()),
                             sorted([RECORD] + reveal_paths(AUTH_HOME)
                                    + reveal_paths(CONS_HOME)))
        present = read(LAWMOD).decode("utf-8")
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[LAWMOD][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[LAWMOD] + (("planted", first,
                                      first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(LAWMOD, text, record, h,
                                                      table))
        rows = succession_rows(h)
        last = "| " + " | ".join(rows[-1]) + " |"
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        for name, mutated in (
                ("a space-prefixed duplicate row", record.replace(
                    last + "\n", last + "\n " + last + "\n", 1)),
                ("a row with no opening pipe", record.replace(
                    last, last[2:], 1)),
                ("reversed rows", record.replace(
                    "| " + " | ".join(rows[0]) + " |\n" + last + "\n",
                    last + "\n| " + " | ".join(rows[0]) + " |\n", 1)),
                ("an altered separator", record.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom",
                 record.replace(last + "\n", last + "\nmechanics sentinel\n",
                                1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, h))
        for name, mutated in h.rev.boundary_mutants(
                record, SUCCESSION_SECTION, last).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(succession_table_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev")
                for rel in (ENVELOPE, LAWMOD):
                    self.assertEqual(succession_violations(
                        rel, read(rel).decode("utf-8"), record, hh), [])


class VR11_RegistryAndBoard(unittest.TestCase):
    def test_vr11_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = vrc_state(read(RECORD).decode("utf-8"), h)
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
            self.assertTrue(board_ok(h.auth.apply_sites, h.rec.R9_REVEAL))
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        entries = json.loads(reg)["entries"]
        e = {x["id"]: x for x in entries}.get("W8-D4-VRC")
        with self.subTest(entry="W8-D4-VRC"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]),
                             (RECORD, "phase-record", "W8", "W8-D4"))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            self.assertEqual(e["content_hash"], record_hash)
        with self.subTest(fact="no revealed record is individually "
                               "registered, and the W8-D4 entries are the "
                               "earlier seven and this one"):
            self.assertEqual([x["id"] for x in entries
                              if x["path"].startswith(REVEAL_ROOT + "/")], [])
            self.assertEqual({x["id"] for x in entries
                              if x["deliverable"] == "W8-D4"},
                             EARLIER_D4 | {"W8-D4-VRC"})
            self.assertEqual([x["id"] for x in entries
                              if x["deliverable"] in LATER_DELIVERABLES], [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(fact="the session row and the correction row are "
                               "preserved"):
            self.assertEqual(board.count(BOARD_ROW_HEAD), 1)
            self.assertEqual(board.count(
                "| W8 — Case-Home Scope Correction (W8-CHC) |"), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites,
                                         hh.rec.R9_REVEAL))


class VR12_Census(unittest.TestCase):
    def test_vr12_census_is_exactly_forty_two_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        expected = set(FIXED_CENSUS) | set(reveal_paths(AUTH_HOME)) \
            | set(reveal_paths(CONS_HOME))
        with self.subTest(fact="the census is exactly forty-two paths"):
            self.assertEqual(len(FIXED_CENSUS), 6)
            self.assertEqual(len(expected), 42)
            self.assertEqual(paths, expected)
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {ENVELOPE, LAWMOD, SELF_REL})
        with self.subTest(fact="no corpus home, register or session record "
                               "is touched"):
            self.assertEqual([p for p in paths if p.startswith(
                (HOME + "/", "governance/discriminating-",
                 "governance/validation-review/"))
                or p == SESSION_RECORD], [])
        record = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly forty-two "
                          r"paths:\*\* (.*?) No corpus home", record)
            self.assertIsNotNone(m)
            named = set(re.findall(r"`([^`]+)`", m.group(1)))
            self.assertEqual(named - {AUTH_HOME + "/W8-C-<64-hex>.json",
                                      CONS_HOME + "/W8-C-<64-hex>.json"},
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {LAW},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, expected)


if __name__ == "__main__":
    unittest.main()
