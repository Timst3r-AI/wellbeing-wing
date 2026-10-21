"""W8-D4-F — completion proofs (W8-D4-CPR, CP1–CP10).

The completion landing of W8-D4, without diagnosis by the human
authority's decision: every recorded divergence stays recorded and
undiagnosed, nothing is corrected, and W8-D4 completes. This module proves
the decision's verbatim carriage, the record's completion-without-diagnosis
statements and its inability to express a case-level diagnosis, the
preservation of ADR-0058's R9 sentence and constant, the byte-stability of
every fixed artefact, the programme table read whole, the one staged
succession, the registry and board forms, the record's carriage and
exposure limits and the census, each with planted-mutant or negative
controls.

Following ADR-0060 decision 39, every proof here reads this landing's fixed
snapshot - the candidate over the baseline before the commit exists, the
one commit that added this record afterwards - and executes every helper,
constant and reserved literal it relies on from that snapshot's bytes, in
a private namespace, never from a live module a later landing may lawfully
succeed. This module imports no other proof module; it holds no live gate
on the absence or admission of any future artefact, and those gates stay
in VL10. The residual live reach is disclosed exactly: each
snapshot-executed helper module imports, at its own top level, the live
modules it aliases - the envelope, packet, calibration, corpus, authority,
recovery, supplement, opening, validation-law and reveal modules - for the
fixed-law values it reads from them, and no more independence than that is
claimed.

THIS MODULE READS NO CUSTODY AND NO CASE. It reads the published record,
registry, board and proof modules, the git history of the W8-D4 landings,
and, for byte-stability only, the published homes and records. It names no
case and holds no disposition token, method label or schema literal.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any diagnosis, or that none is warranted; that any token
is right; any rate, score or readiness; any verdict on the instrument; the
absence of influence or the reviewer's independence; or that any later
deliverable may now begin.
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

# The published, remotely verified reveal landing: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "67ed076503f1087cefed31dd163a706a87d3b8a6"

RECORD = "docs/phases/W8-D4-completion-record.md"
SELF_REL = "tests/test_w8_validation_completion.py"
LAWMOD = "tests/test_w8_validation_law.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
ADR54 = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, LAWMOD, REGISTRY, BOARD})
LATER_DELIVERABLES = ("W8-D5", "W8-D6", "W8-D7")
EARLIER_D4 = frozenset({"W8-D4-IVB", "ADR-0060", "W8-D4-VCR", "W8-V1-CM-01",
                        "W8-V1-CM-02", "W8-D4-VSR", "W8-D4-DR-01",
                        "W8-D4-VRC"})
# The fixed homes and records every proof below holds byte-stable.
FIXED_HOMES = ("governance/validation-cases", "governance/validation-review",
               "governance/validation-reveal",
               "governance/discriminating-instrument",
               "governance/discriminating-supplement",
               "governance/discriminating-reveal")
FIXED_RECORD_IDS = ("W8-D4-IVB", "ADR-0060", "W8-D4-VCR", "W8-D4-VSR",
                    "W8-D4-VRC", "W8-CHC", "W8-D3-CCR")

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": LAWMOD,
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "ses": "tests/test_w8_validation_session.py",
           "vr": "tests/test_w8_validation_reveal.py"}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    LAWMOD: ("validation-law module",
             "sha256:66a16bf2fe7cd71ff0dd382dbe30ce9b1afc35da5d90060082c7a79960ad6c50",
             "71b33fd6d7415a691fc8e6d1a426e1fa7c4aa29e"),
    REGISTRY: ("registry",
               "sha256:c8a013cebfd852750062ea99df9cbe477d5420095ce2136018c63a798aabb7ca",
               "857c983260f4581593cad6738fb1a000f9b846eb"),
    BOARD: ("board",
            "sha256:222e05d16186a2bbf46c2088e0dcedef5e8dd057d728dba51bdf4272ae93e043",
            "29a2159458860282c306bdc3d2726f4c8b0f2199"),
    RECOVERY: ("session-recovery module",
               "sha256:6873de43760267cb51366078818cbc33ac5e50bbfd8cabe9eb840dd05d910b97", "d0bafd22b15f949d980ab3dc0884250ed325c4aa"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {LAWMOD: ("sha256:a3bbdad77f375cd91cb5646ea234f01a44fe66e1cbc5aab8de54206e7580c762", "7c3d7e4fb1a5f82a8a38bd09d03f1be5059b491e")}

# ------------------------------------------ the one staged succession (d38)
SITES = {
    LAWMOD: (
        ('VL10',
         'REVEAL_IDS = frozenset({"W8-D4-VRC"})\n',
         'REVEAL_IDS = frozenset({"W8-D4-VRC"})\n# Admitted at the completion landing (ADR-0060 Part J decision 38): the\n# completion record and its W8-D4 entry. The reveal-stage state stays\n# proven at the reveal landing commit.\nD4E_LANDING = "67ed076503f1087cefed31dd163a706a87d3b8a6"\nCOMPLETION_RECORD = LATER_RECORDS[3]\nCOMPLETION_IDS = frozenset({"W8-D4-CPR"})\n'),
        ('VL10',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None, session=None,\n                              reveal=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it. Succeeded at the session\n    landing: `session` is that landing\'s admitted path set - the\n    register and the session record - or None for the state before it.\n    Succeeded at the reveal landing: `reveal` is that landing\'s admitted\n    path set - both reveal homes\' records and the validation record - or\n    None for the state before it."""\n    admitted = (frozenset(corpus or ()) | frozenset(session or ())\n                | frozenset(reveal or ()))\n    landed = corpus is not None\n    held = session is not None\n    shown = reveal is not None\n    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n           | (SESSION_IDS if held else frozenset())\n           | (REVEAL_IDS if shown else frozenset()))\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    if shown:\n        holders_ok |= {p for p in reveal\n                       if p.startswith(REVEAL_HOMES[1] + "/")}\n    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())\n                  | ({VALIDATION_HOMES[1]} if held else set())\n                  | ({VALIDATION_HOMES[2]} if shown else set()))\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None, session=None,\n                              reveal=None, completion=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it. Succeeded at the session\n    landing: `session` is that landing\'s admitted path set - the\n    register and the session record - or None for the state before it.\n    Succeeded at the reveal landing: `reveal` is that landing\'s admitted\n    path set - both reveal homes\' records and the validation record - or\n    None for the state before it. Succeeded at the completion landing:\n    `completion` is that landing\'s admitted path set - the completion\n    record - or None for the state before it."""\n    admitted = (frozenset(corpus or ()) | frozenset(session or ())\n                | frozenset(reveal or ()) | frozenset(completion or ()))\n    landed = corpus is not None\n    held = session is not None\n    shown = reveal is not None\n    closed = completion is not None\n    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n           | (SESSION_IDS if held else frozenset())\n           | (REVEAL_IDS if shown else frozenset())\n           | (COMPLETION_IDS if closed else frozenset()))\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    if shown:\n        holders_ok |= {p for p in reveal\n                       if p.startswith(REVEAL_HOMES[1] + "/")}\n    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())\n                  | ({VALIDATION_HOMES[1]} if held else set())\n                  | ({VALIDATION_HOMES[2]} if shown else set()))\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n'),
        ('VL10',
         '        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        reveal = reveal_admitted()\n        construction_reveal = sorted(p for p in reveal\n                                     if p.startswith(REVEAL_HOMES[1] + "/"))\n        with self.subTest(fact="exactly the corpus, session and reveal "\n                               "landings\' artefacts are admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus, session, reveal),\n                [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module, the construction manifest and "\n                               "the construction reveal home"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST] + construction_reveal))\n            self.assertEqual(len(construction_reveal), 18)\n        planted_entry = dict(entries[-1], id="W8-D4-CPR", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "an extra file in the register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "an unbound reveal-home path": (\n                    tracked + [REVEAL_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "a path under the reveal root itself": (\n                    tracked + [VALIDATION_HOMES[2] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal),\n                "a completion record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[3], entries,\n                    holders, corpus, session, reveal),\n                "a premature completion entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus, session, reveal),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus,\n                    session, reveal),\n                "a construction schema literal in the authoring home": (\n                    tracked, exists, entries,\n                    holders + [REVEAL_HOMES[0] + "/W8-C-x.json"], corpus,\n                    session, reveal),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None, session, reveal),\n                "the session artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, None, reveal),\n                "the reveal artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, session,\n                    None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n',
         '        at_reveal = _git("ls-tree", "-r", "--name-only", D4E_LANDING).split()\n        reveal_entries = json.loads(committed(D4E_LANDING, REGISTRY))[\n            "entries"]\n        reveal_holders = schema_holders(\n            at_reveal, lambda p: committed(D4E_LANDING, p))\n        reveal = reveal_admitted()\n        construction_reveal = sorted(p for p in reveal\n                                     if p.startswith(REVEAL_HOMES[1] + "/"))\n        with self.subTest(fact="nothing of the completion existed at the "\n                               "reveal landing"):\n            self.assertEqual(staged_absence_violations(\n                at_reveal, lambda p: False, reveal_entries, reveal_holders,\n                corpus, session, reveal), [])\n            self.assertEqual(sorted(reveal_holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST] + construction_reveal))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        completion = {COMPLETION_RECORD}\n        with self.subTest(fact="exactly the corpus, session, reveal and "\n                               "completion landings\' artefacts are admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus, session, reveal,\n                completion), [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module, the construction manifest and "\n                               "the construction reveal home"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST] + construction_reveal))\n            self.assertEqual(len(construction_reveal), 18)\n        planted_entry = dict(entries[-1], id="W8-D4-XYZ", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal, completion),\n                "an extra file in the register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus, session, reveal, completion),\n                "an unbound reveal-home path": (\n                    tracked + [REVEAL_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal, completion),\n                "a path under the reveal root itself": (\n                    tracked + [VALIDATION_HOMES[2] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session, reveal, completion),\n                "an unlisted W8-D4 entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus, session, reveal, completion),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus,\n                    session, reveal, completion),\n                "a construction schema literal in the authoring home": (\n                    tracked, exists, entries,\n                    holders + [REVEAL_HOMES[0] + "/W8-C-x.json"], corpus,\n                    session, reveal, completion),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None, session, reveal,\n                    completion),\n                "the session artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, None, reveal,\n                    completion),\n                "the reveal artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, session, None,\n                    completion),\n                "the completion artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, session,\n                    reveal, None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n'),
    ),
}
D38_CLAUSES = (
    "At the completion landing (D4-F): VL10 admits exactly the completion "
    "record and its W8-D4 entry;",
    "ADR-0058's R9 board limb moves only if that landing's board wording "
    "diagnoses a divergence")

# ADR-0058's R9 sentence, which this landing preserves.
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_BOLD = ("**No divergence is diagnosed, explained away or corrected. W8-D5 "
           "through W8-D7 remain closed behind their own briefs.**")

# The human authority's decision, carried verbatim under its dated label.
DECISION_LABEL = ("1. **The human authority's decision on diagnosis, "
                  "received on 2026-10-21:**")
DECISION = ("> I choose D4-F completion without diagnosis. Leave all "
            "recorded divergences undiagnosed.\n")
FRAMING = (
    "The decision is the human authority's alone, under the first decision "
    "point of `W8-D4-IVB` item 29 and ADR-0060 decision 36.",
    "It is recorded verbatim above; this record adds nothing to it, "
    "interprets nothing in it and narrows nothing.")

# The programme table, read whole: (landing, act, identities, commit).
PROGRAMME = (
    ("D4-A", "the opening brief", ("W8-D4-IVB",),
     "ad59925813f8b0c39789dac3b29383a5f6e25cea"),
    ("D4-B", "the validation law", ("ADR-0060",),
     "054f1270b8206a059636e18e012223ddfe52d5ea"),
    ("D4-C", "the validation corpus",
     ("W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02"),
     "f638cca75ec4a192685bf5cd53f29451cfdbbdd9"),
    ("D4-D", "the validation session", ("W8-D4-VSR", "W8-D4-DR-01"),
     "44947adf9b60f2ce462be97a2c0e628a3ecbdd89"),
    ("D4-E", "the reveal and comparison", ("W8-D4-VRC",),
     "67ed076503f1087cefed31dd163a706a87d3b8a6"),
)
W8_D3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"
CHC_COMMIT = "a08ba584bea8e2576dd7450c6374a4ff4f0aa149"
PROGRAMME_SECTION = "## 2. The W8-D4 programme as completed"
PROGRAMME_HEADER = "| Landing | Act | Identities | Landing commit |"
PROGRAMME_SEPARATOR = "|---|---|---|---|"
SUCCESSION_SECTION = "## 5. Proof successions at this landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"

# --------------------------------------- board and registry: authorised edits
CPR_LINK = "([`W8-D4-completion-record.md`](W8-D4-completion-record.md))"
CPR_STATUS_BODY = (
    "by the human authority's decision: every divergence recorded in W8-D3 "
    "and W8-D4 stays recorded and undiagnosed, nothing is corrected, no "
    "finding is taken to separate authority, and the dispositions, cases "
    "and revealed records stay exactly as published.")
DRAFT_OPEN = ("**A draft completion record, `W8-D4-CPR`, is before the human "
              "reviewer**")
ACCEPTED_OPEN = "**`W8-D4-CPR` — the completion record — is accepted**"
CPR_STATUS = {
    "draft": (DRAFT_OPEN + " " + CPR_LINK + ": if accepted, it would "
              "complete W8-D4 without diagnosis, " + CPR_STATUS_BODY),
    "accepted": (ACCEPTED_OPEN + " " + CPR_LINK + " — accepted %s: **W8-D4 "
                 "is complete, without diagnosis**, " + CPR_STATUS_BODY),
}
CPR_ROW = ("| W8-D4 — Completion Record (W8-D4-CPR) | "
           "[`W8-D4-completion-record.md`](W8-D4-completion-record.md) | ")
CPR_ROW_BODY = (
    "Tier J: **the D4-F completion of W8-D4, without diagnosis**, by the "
    "human authority's decision, recorded verbatim: every recorded "
    "divergence stays recorded and undiagnosed; nothing is corrected; no "
    "finding is taken to separate authority; the dispositions, cases, "
    "manifests, revealed records and earlier records stay unchanged; the "
    "validation law's VL10 succeeds by exact transformation and ADR-0058's "
    "R9 does not move. **W8-D5 to W8-D7 stay closed.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = "readiness interpretation. **No divergence is diagnosed"
BOARD_ROW_HEAD = "| W8-D4 — Validation Record (W8-D4-VRC) | "
CPR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CPR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D4-CPR", "path": RECORD, "type": "phase-record",
    "title": "W8-D4 - Completion Record",
    "role": (
        "The W8-D4 completion record of landing D4-F, without diagnosis by "
        "the human authority's decision, recorded verbatim under its dated "
        "label: every divergence recorded in W8-D3 and W8-D4 stays recorded "
        "and undiagnosed, no outcome of the closed diagnosis set is "
        "assigned to any case, nothing is corrected and no finding is taken "
        "to separate authority. Binds the W8-D4 programme as completed, "
        "each landing to the commit that added its record; keeps the "
        "dispositions, cases, manifests, revealed records and every earlier "
        "record byte-unchanged; names and characterises no case; derives no "
        "rate, score or readiness interpretation. Moves exactly the "
        "validation law's VL10 by exact transformation, ADR-0058's R9 "
        "sentence and constant preserved, with proof obligations CP1 to "
        "CP10. Opens none of W8-D5 to W8-D7."),
    "depends_on": ["ADR-0060", "W8-D4-VRC", "W8-D4-VSR", "W8-D4-DR-01",
                   "W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02", "W8-D4-IVB",
                   "W8-D3-CCR", "W8-CHC", "ADR-0057", "ADR-0058", "ADR-0054",
                   "ADR-0055", "W8-D2-CBC", "ADR-0056", "W8-AR", "W7-CR"]}

# Completion-without-diagnosis statements (CP2).
NO_DIAGNOSIS = (
    "By the human authority's decision, diagnosis does not enter W8-D4: "
    "every recorded divergence stays recorded and undiagnosed, nothing is "
    "corrected, and W8-D4 completes.",
    "Because diagnosis does not enter W8-D4, the remaining decision points "
    "of item 29 do not arise at this landing:",
    "No divergence is diagnosed.",
    "Every divergence that the validation record `W8-D4-VRC` records stays "
    "recorded exactly as published there, and undiagnosed.",
    "Every divergence that the W8-D3 completion record `W8-D3-CCR` leaves "
    "undiagnosed also stays undiagnosed:",
    "No outcome from the closed set of `W8-D4-IVB` item 27 is assigned to "
    "any case, and no case is named or characterised in this record.",
    "No outcome attributes error to the reviewer, and nothing declares "
    "either token correct.",
    "Nothing is corrected",
    "This record creates no route to a diagnosis.",
    "The board wording this landing adds diagnoses nothing, so ADR-0058's "
    "R9 board limb does not move",
)
# Fixed-state, succession and closure statements (CP8).
REQUIRED = (
    "The dispositions were fixed at the session record's publication",
    "and none is amended by any route.",
    "The eighteen validation cases, both manifests, the register, the "
    "session record, the thirty-six revealed records and the validation "
    "record are byte-unchanged by this landing, and so is every W8-D3 "
    "artefact.",
    "This record makes no custody decision.",
    "Exactly the one succession that ADR-0060 decision 38 stages for this "
    "landing moves,",
    "No other existing proof moves at this landing.",
    "This landing's census is exactly five paths:",
    "No case, manifest, register, revealed record or earlier record is "
    "touched.",
    "On this record's acceptance, publication and independent remote "
    "verification, W8-D4 is complete,",
    "W8-D5 through W8-D7 remain closed behind their own briefs; this record "
    "opens none of them.",
    "this record neither performs that weighing nor authorises W8-D5 to open.",
    "Neither this record nor any of its green proofs supplies any of those "
    "conclusions.",
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


def l12_snapshot():
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
        return None, ["the completion record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = l12_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot: the bytes
    `read` yields for `rel`, executed in a fresh private namespace that is
    registered nowhere."""
    ns = {"__name__": "_w8_cpr_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def nine_rules_block():
    adr = _lf(committed(BASELINE, ADR54)).decode("utf-8")
    m = re.search(r"^> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                  r"failure\.\*\*)$", adr, re.M)
    return "> %s\n" % m.group(1) if m else None


def decision_violations(text, h):
    """CP1: the decision verbatim directly under its dated label, once; the
    only quotation blocks are the decision and the nine rules; every
    quotation set apart; no framing inside a quotation."""
    v = h.ses.quote_boundary_violations(text)
    blocks = h.ses.quotation_blocks(text)
    if sorted(blocks) != sorted([DECISION, nine_rules_block()]):
        v.append("the quotation blocks are not exactly the decision and the "
                 "nine rules, each once")
    if text.count(DECISION_LABEL) != 1:
        v.append("the dated label is missing or repeated")
    if text.count(DECISION_LABEL + "\n\n" + DECISION) != 1:
        v.append("the decision is not verbatim directly under its label")
    for f in FRAMING:
        if text.count(f) != 1:
            v.append("framing occurs %d times" % text.count(f))
        if any(f in b for b in blocks):
            v.append("framing sits inside a quotation block")
    return v


def strip_pins(text):
    """The text with 64-hex digests and 40-hex commit identities removed."""
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", "", text)
    return re.sub(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", "", text)


def no_diagnosis_violations(text, h):
    """CP2: the completion-without-diagnosis statements each once, and no
    case identity, token, count statement or derived-figure form anywhere,
    so that no case-level diagnosis can be expressed."""
    flat = _flat(text)
    v = ["missing or repeated: %s" % s[:48] for s in NO_DIAGNOSIS
         if flat.count(s) != 1]
    if h.rec.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    v += ["a token is present" for t in h.pkt.TOKENS if t in text]
    if h.cal.COUNT_STATEMENT in text:
        v.append("a count statement is present")
    v += h.vr.figure_hits(strip_pins(text), h.pkt.TOKENS)
    return v


def r9_violations(board, recovery_bytes, h):
    """CP3: the session-recovery module byte-unchanged, its R9 constant the
    exact sentence, and the board carrying the sentence once, in its bold
    closing form, after the wording this landing adds."""
    v = []
    if recovery_bytes != _lf(committed(BASELINE, RECOVERY)):
        v.append("the session-recovery module changed")
    if _sha(recovery_bytes) != PREIMAGE[RECOVERY][1]:
        v.append("the session-recovery module is not its pinned bytes")
    if h.rec.R9_REVEAL != R9_SENTENCE:
        v.append("the R9 constant is not the exact sentence")
    if board.count(R9_SENTENCE) != 1 or board.count(R9_BOLD) != 1:
        v.append("the board does not carry the R9 sentence exactly once")
    counts = [board.count(o) for o in (DRAFT_OPEN, ACCEPTED_OPEN)]
    opens = [board.find(o) for o in (DRAFT_OPEN, ACCEPTED_OPEN)
             if board.count(o) == 1]
    if (sum(counts) != 1 or len(opens) != 1
            or not opens[0] < board.find(R9_BOLD)):
        v.append("the added status wording does not stand once, before the "
                 "R9 sentence")
    return v


def moved_after_r9(board):
    """Mechanics only: the board with this landing's status sentence moved
    from before the R9 sentence to after it."""
    start = min(board.find(o) for o in (DRAFT_OPEN, ACCEPTED_OPEN)
                if board.find(o) >= 0)
    end = board.find(" **No divergence is diagnosed", start)
    sentence = board[start:end]
    out = board[:start] + board[end + 1:]
    return out.replace(R9_BOLD, R9_BOLD + " " + sentence, 1)


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
    """The fixed homes' files and the fixed records, as at the baseline."""
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
    paths = {e["id"]: e["path"] for e in reg}
    homes = {h: sorted(p for p in base_tracked if p.startswith(h + "/"))
             for h in FIXED_HOMES}
    return homes, [paths[r] for r in FIXED_RECORD_IDS]


def fixed_artefact_violations(now, tracked, homes, records, base):
    """CP4: every fixed home's file set and bytes, and every fixed record's
    bytes, identical to the baseline."""
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


def programme_rows():
    return [[landing, act, " · ".join("`%s`" % i for i in ids),
             "`%s`" % commit] for landing, act, ids, commit in PROGRAMME]


def programme_violations(record, h):
    """CP5, the record: the table read whole is exactly its trusted rows,
    and the correction's commit is named once."""
    rows, v = h.rev.closed_table(record, PROGRAMME_SECTION, PROGRAMME_HEADER,
                                 PROGRAMME_SEPARATOR, 4)
    if rows != programme_rows():
        v.append("the programme table is not exactly its trusted rows")
    if record.count("`%s`" % CHC_COMMIT) != 1:
        v.append("the record does not name the correction's commit once")
    return v


def history_violations(programme=PROGRAMME):
    """CP5, the history: each commit added each listed record, on the
    first-parent line from the W8-D3 completion to the baseline, in order;
    each record is an accepted W8-D4 entry; the correction is the separate
    act named."""
    v = []
    entries = {e["id"]: e for e in
               json.loads(committed(BASELINE, REGISTRY))["entries"]}
    line = _git("rev-list", "--first-parent", "--reverse",
                W8_D3_COMPLETION + ".." + BASELINE).split()
    order = []
    for _, _, ids, commit in programme:
        if commit not in line:
            v.append("a landing commit is off the first-parent line")
            continue
        order.append(line.index(commit))
        for rid in ids:
            e = entries.get(rid)
            if e is None or (e["status"], e["deliverable"]) != ("accepted",
                                                               "W8-D4"):
                v.append("%s is not an accepted W8-D4 entry" % rid)
                continue
            adds = _git("log", "--diff-filter=A", "--format=%H", BASELINE,
                        "--", e["path"]).split()
            if adds != [commit]:
                v.append("%s was not added by its listed commit" % rid)
    if order != sorted(order):
        v.append("the landings are not in first-parent order")
    if not line or line[0] != programme[0][3]:
        v.append("the opening brief does not follow the W8-D3 completion")
    chc = entries.get("W8-CHC")
    if (chc is None or chc["deliverable"] is not None or
            _git("log", "--diff-filter=A", "--format=%H", BASELINE, "--",
                 chc["path"]).split() != [CHC_COMMIT]):
        v.append("the case-home correction is not the separate act named")
    return v


def succession_rows(h):
    return [["`%s`" % LAWMOD, ", ".join(h.auth.labels(SITES[LAWMOD])),
             "`%s`" % PREIMAGE[LAWMOD][1], "`%s`" % POSTIMAGE[LAWMOD][0]]]


def succession_table_violations(record, h):
    rows, v = h.rev.closed_table(record, SUCCESSION_SECTION,
                                 SUCCESSION_HEADER, SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, record, h, sites=None):
    sites = SITES[LAWMOD] if sites is None else sites
    v = []
    pre = _lf(committed(BASELINE, LAWMOD)).decode("utf-8")
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
    return v + succession_table_violations(record, h)


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def cpr_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CPR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CPR_ACCEPTED % date) not in head:
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
         "readiness interpretation. " + fill(CPR_STATUS[state])
         + " **No divergence is diagnosed"),
        ("row", anchor,
         anchor + CPR_ROW + fill(ROW_PREFIX[state]) + CPR_ROW_BODY + " |\n"),
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
    return " ".join([CPR_ROW, CPR_ROW_BODY, CPR_STATUS["draft"],
                     CPR_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def exposure_violations(text, h):
    """No case identity, token, count statement, schema literal, method
    label, reserved authoring label or derived-figure form."""
    v = ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    tokens, schemas, methods = h.vr.reserved_literals(h)
    v += ["a schema literal is present" for s in schemas if s in text]
    v += ["a method label: %s" % m for m in methods
          if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]
    v += ["a token is present" for t in tokens if t in text]
    if h.rec.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    if h.cal.COUNT_STATEMENT in text:
        v.append("a count statement is present")
    v += h.vr.figure_hits(strip_pins(text), tokens)
    return v


def carriage_violations(text, h):
    flat = _flat(text)
    v = ["missing or repeated: %s" % s[:48] for s in REQUIRED
         if flat.count(s) != 1]
    v += ["withdrawn wording present: %s" % w for w in h.vr.WITHDRAWN
          if w in flat]
    block = nine_rules_block()
    if block is None or text.count(block) != 1:
        v.append("the nine-rule block is not carried once, byte-identical")
    return v


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted
    to call is replaced and the previous state restored on exit, tolerating
    a name a later landing has renamed or removed."""

    ABSENT = object()
    TARGETS = (
        ("test_w8_validation_session", "quote_boundary_violations",
         lambda *a, **k: []),
        ("test_w8_validation_session", "quotation_blocks",
         lambda *a, **k: []),
        ("test_w8_validation_reveal", "figure_hits", lambda *a, **k: []),
        ("test_w8_validation_reveal", "reserved_literals",
         lambda *a, **k: ((), (), ())),
        ("test_w8_session_recovery_law", "R9_REVEAL", "mechanics sentinel"),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_recovery_authority", "apply_sites",
         lambda text, sites: (text, [])),
        ("test_w8_reveal_calibration", "closed_table",
         lambda *a, **k: ([], [])),
        ("test_w8_validation_law", "staged_absence_violations",
         lambda *a, **k: []),
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
class CP1_DecisionVerbatim(unittest.TestCase):
    def test_cp1_the_decision_stands_verbatim_under_its_label(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ses")
        record = read(RECORD).decode("utf-8")
        with self.subTest(fact="the decision verbatim under its dated label; "
                               "only the decision and the nine rules are "
                               "quoted; framing outside"):
            self.assertEqual(decision_violations(record, h), [])
        block = DECISION_LABEL + "\n\n" + DECISION
        for name, mutated in (
                ("a reworded decision", record.replace(
                    "Leave all recorded divergences undiagnosed.",
                    "Leave the recorded divergences undiagnosed.", 1)),
                ("a decision moved off its label", record.replace(
                    block, DECISION_LABEL + "\n\nThe decision follows.\n\n"
                    + DECISION, 1)),
                ("framing inside the quotation", record.replace(
                    DECISION, DECISION + "> " + FRAMING[0] + "\n", 1)),
                ("an indented quotation marker", record.replace(
                    "\n" + DECISION, "\n " + DECISION, 1)),
                ("a lazily continued line", record.replace(
                    DECISION + "\n", DECISION + "mechanics sentinel\n", 1)),
                ("a second quotation", record.replace(
                    "\n## 2.", "\n> mechanics sentinel\n\n## 2.", 1)),
                ("a repeated label", record.replace(
                    "\n## 2.", "\n" + DECISION_LABEL + "\n\n## 2.", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(decision_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "ses")
                self.assertEqual(decision_violations(record, hh), [])
                self.assertTrue(decision_violations(record.replace(
                    "\n" + DECISION, "\n " + DECISION, 1), hh))


class CP2_CompletionWithoutDiagnosis(unittest.TestCase):
    def test_cp2_no_case_level_diagnosis_can_be_expressed(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "pkt", "cal", "vr")
        record = read(RECORD).decode("utf-8")
        with self.subTest(fact="the statements each once; no identity, "
                               "token, count statement or figure"):
            self.assertEqual(no_diagnosis_violations(record, h), [])
        tok = sorted(h.pkt.TOKENS)[0]
        anchor = "## 4. What stays fixed"
        self.assertEqual(record.count(anchor), 1)

        def planted(line):
            return record.replace(anchor, line + "\n\n" + anchor, 1)
        for name, mutated in (
                ("a planted case identity", planted(
                    "W8-C-" + "a" * 64 + " — construction")),
                ("a planted token", planted("The token " + tok + " stands.")),
                ("a planted count statement", planted(
                    h.cal.COUNT_STATEMENT)),
                ("a planted count beside a kind", planted("2 divergences")),
                ("a planted decimal", planted("0.5")),
                ("a removed statement", record.replace(
                    "No divergence is diagnosed.", "", 1)),
                ("a repeated statement", planted(
                    "This record creates no route to a diagnosis."))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(no_diagnosis_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "pkt", "cal", "vr")
                self.assertEqual(no_diagnosis_violations(record, hh), [])
                self.assertTrue(no_diagnosis_violations(planted("0.5"), hh))


class CP3_R9Preserved(unittest.TestCase):
    def test_cp3_r9_sentence_and_constant_preserved(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        board = read(BOARD).decode("utf-8")
        recovery = _lf(read(RECOVERY))
        with self.subTest(fact="R9 module, constant and board sentence "
                               "preserved"):
            self.assertEqual(r9_violations(board, recovery, h), [])
            self.assertEqual(_git("rev-parse", BASELINE + ":" + RECOVERY)
                             .strip(), PREIMAGE[RECOVERY][2])
        for name, (b, r) in {
                "a removed R9 sentence": (board.replace(R9_SENTENCE, "", 1),
                                          recovery),
                "a doubled R9 sentence": (board + "\n" + R9_SENTENCE + "\n",
                                          recovery),
                "an altered R9 sentence": (board.replace(
                    R9_SENTENCE, "No divergence is diagnosed.", 1), recovery),
                "the added wording after the R9 sentence": (
                    moved_after_r9(board), recovery),
                "a changed recovery module": (board, recovery + b"# x\n")}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(r9_violations(b, r, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec")
                self.assertEqual(r9_violations(board, recovery, hh), [])


class CP4_FixedArtefactsUnchanged(unittest.TestCase):
    def test_cp4_every_fixed_artefact_is_byte_unchanged(self):
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
        register = homes["governance/validation-review"][0]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed register": (
                    dict(now, **{register: now[register] + b" "}), tracked),
                "a changed earlier record": (
                    dict(now, **{records[0]: now[records[0]] + b" "}),
                    tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-cases/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))


class CP5_ProgrammeTable(unittest.TestCase):
    def test_cp5_the_programme_table_binds_each_landing(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        record = read(RECORD).decode("utf-8")
        with self.subTest(fact="the table read whole is its trusted rows"):
            self.assertEqual(programme_violations(record, h), [])
        with self.subTest(fact="each landing commit added its records, in "
                               "first-parent order"):
            self.assertEqual(history_violations(), [])
        p = list(PROGRAMME)
        for name, prog in (
                ("a commit that did not add the record",
                 p[:1] + [p[1][:3] + (p[2][3],)] + p[2:]),
                ("landings out of order", [p[1], p[0]] + p[2:]),
                ("an identity under the wrong landing",
                 [p[0][:2] + (("ADR-0060",),) + p[0][3:]] + p[1:])):
            with self.subTest(history_control="%s is refused" % name):
                self.assertTrue(history_violations(tuple(prog)))
        rows = ["| " + " | ".join(r) + " |" for r in programme_rows()]
        top = PROGRAMME_HEADER + "\n" + PROGRAMME_SEPARATOR + "\n"
        for name, mutated in (
                ("swapped rows", record.replace(
                    rows[0] + "\n" + rows[1], rows[1] + "\n" + rows[0], 1)),
                ("a wrong commit", record.replace(
                    rows[1], rows[1].replace(PROGRAMME[1][3],
                                             PROGRAMME[0][3]), 1)),
                ("a dropped row", record.replace(rows[2] + "\n", "", 1)),
                ("a duplicated row", record.replace(
                    rows[2] + "\n", rows[2] + "\n" + rows[2] + "\n", 1)),
                ("a malformed separator", record.replace(
                    top, PROGRAMME_HEADER + "\n|---|---|---|\n", 1)),
                ("an extra column", record.replace(
                    PROGRAMME_HEADER, PROGRAMME_HEADER + " Note |", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(programme_violations(mutated, h))
        for name, mutated in h.rev.boundary_mutants(
                record, PROGRAMME_SECTION, rows[-1]).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(programme_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(programme_violations(record, hh), [])


class CP6_Succession(unittest.TestCase):
    def test_cp6_the_staged_succession_is_exact(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "law")
        record = read(RECORD).decode("utf-8")
        present = read(LAWMOD).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[LAWMOD][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + LAWMOD)
                             .strip(), PREIMAGE[LAWMOD][2])
        with self.subTest(exact_succession=PREIMAGE[LAWMOD][0]):
            self.assertEqual(succession_violations(present, record, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[LAWMOD][1])
        with self.subTest(fact="ADR-0060 decision 38 stages exactly this"):
            law = _flat(_lf(committed(BASELINE, LAW)).decode("utf-8")
                        .replace("**", ""))
            for clause in D38_CLAUSES:
                self.assertIn(clause, law)
        with self.subTest(fact="the succeeded module carries this landing's "
                               "constants"):
            self.assertEqual(h.law.D4E_LANDING, BASELINE)
            self.assertEqual(h.law.COMPLETION_RECORD, RECORD)
            self.assertEqual(h.law.COMPLETION_IDS, frozenset({"W8-D4-CPR"}))
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[LAWMOD][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[LAWMOD] + (("planted", first,
                                      first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(text, record, h, table))
        row = "| " + " | ".join(succession_rows(h)[0]) + " |"
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        for name, mutated in (
                ("a space-prefixed duplicate row", record.replace(
                    row + "\n", row + "\n " + row + "\n", 1)),
                ("a row with no opening pipe", record.replace(row, row[2:], 1)),
                ("an altered separator", record.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom",
                 record.replace(row + "\n", row + "\nmechanics sentinel\n",
                                1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, h))
        for name, mutated in h.rev.boundary_mutants(
                record, SUCCESSION_SECTION, row).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(succession_table_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev")
                self.assertEqual(succession_violations(present, record, hh),
                                 [])


class CP7_RegistryAndBoard(unittest.TestCase):
    def test_cp7_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = cpr_state(read(RECORD).decode("utf-8"), h)
        self.assertEqual(v, [])
        board_pre = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(BASELINE, REGISTRY)).decode("utf-8")
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")

        def board_ok(apply_sites):
            expected, problems = apply_sites(
                board_pre, board_sites(state, date, board_pre))
            return problems == [] and board == expected
        with self.subTest(fact="exact authorised board", state=state):
            self.assertIsNotNone(board_row_anchor(board_pre))
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        entries = json.loads(reg)["entries"]
        e = {x["id"]: x for x in entries}.get("W8-D4-CPR")
        with self.subTest(entry="W8-D4-CPR"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]),
                             (RECORD, "phase-record", "W8", "W8-D4"))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            self.assertEqual(e["content_hash"], record_hash)
        with self.subTest(fact="the W8-D4 entries are the earlier eight and "
                               "this one; no later deliverable"):
            self.assertEqual({x["id"] for x in entries
                              if x["deliverable"] == "W8-D4"},
                             EARLIER_D4 | {"W8-D4-CPR"})
            self.assertEqual([x["id"] for x in entries
                              if x["deliverable"] in LATER_DELIVERABLES], [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(fact="the earlier W8-D4 rows are preserved"):
            for head in (BOARD_ROW_HEAD,
                         "| W8-D4 — Validation Session (record, W8-D4-VSR) |",
                         "| W8 — Case-Home Scope Correction (W8-CHC) |"):
                self.assertEqual(board.count(head), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))


class CP8_RecordCarriage(unittest.TestCase):
    def test_cp8_record_carries_its_statements(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "vr")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="statements each once; nine rules; no "
                               "withdrawn evidence-bar wording"):
            self.assertEqual(carriage_violations(text, h), [])
        with self.subTest(control="a removed statement is detected"):
            self.assertTrue(carriage_violations(
                text.replace(REQUIRED[0], "", 1), h))
        with self.subTest(control="a repeated statement is detected"):
            self.assertTrue(carriage_violations(
                text + "\n" + REQUIRED[-1] + "\n", h))
        with self.subTest(control="a planted evidence bar is detected"):
            self.assertTrue(carriage_violations(
                text + "\nNo outcome here may be cited as evidence.\n", h))
        with self.subTest(control="an altered nine-rule block is detected"):
            self.assertTrue(carriage_violations(
                text.replace("uncertainty ≠ failure", "uncertainty = failure",
                             1), h))


class CP9_NoExposure(unittest.TestCase):
    def test_cp9_no_case_level_material_enters_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr")
        record = read(RECORD).decode("utf-8")
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D4-CPR"]["role"] + " " + by_id["W8-D4-CPR"]["title"]
        for name, text in (("record", record),
                           ("registry role and title", role),
                           ("board wording this landing adds",
                            added_board_wording())):
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(exposure_violations(text, h), [])
        with self.subTest(surface="record digests are only its pins"):
            pins = [p.split(":", 1)[1] for p in
                    (PREIMAGE[LAWMOD][1], POSTIMAGE[LAWMOD][0])]
            self.assertEqual([v for v in h.rec.exposure_violations(record,
                                                                    pins)
                              if "digest" in v], [])
        tokens, schemas, methods = h.vr.reserved_literals(h)
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
                "a token": tokens[0],
                "a case identity": "W8-C-" + "b" * 64,
                "a count statement": h.cal.COUNT_STATEMENT,
                "a count beside a kind": "with 11 agreements recorded",
                "a decimal rate": "an agreement rate of 0.5"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(
                    added_board_wording() + " " + plant, h))


class CP10_Census(unittest.TestCase):
    def test_cp10_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {LAWMOD, SELF_REL})
        record = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?) No case, manifest", record)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {LAW},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
