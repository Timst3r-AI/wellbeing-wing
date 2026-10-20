"""W8-D4-D — validation session record proofs (W8-D4-VSR, VS1–VS12).

The session landing of W8-D4 on the validation corpus W8-V1 that ADR-0060
binds: the human authority's eighteen returned tokens bound into governed
register W8-D4-DR-01, and the session record W8-D4-VSR carrying the act's
date, the reviewer role, the packet hash, the register binding, the
four-value corpus binding of ADR-0060 decision 25, the one-session rule, the
statement that every token is an individual human act, the reviewer's
procedural account verbatim with each statement's own date, its dated
continuation included, and the record
of the reviewer's prior exposure, with the two proof successions ADR-0060
decision 38 stages for this landing, prepared over the effective correction
W8-CHC. This module proves the register's shape and exact membership
through the binding chain, the record's bindings, carriage and attribution
boundary, and the exact transformations of everything this landing changes,
each with planted-mutant or negative controls.

Following ADR-0060 decision 39, every proof here reads this landing's fixed
snapshot - the candidate over the baseline before the commit exists, the
one commit that added this record afterwards - and executes every helper,
constant and reserved literal it relies on from that snapshot's bytes, in a
private namespace, never from a live module a later landing may lawfully
succeed. Before the commit exists the register is read as its raw bytes.
This module imports no other proof module; it holds no live gate on the
absence or admission of any future artefact, and those gates stay in VL10.
Two snapshot-executed helpers still reach fixed-law values through live
module aliases - the calibration register validator, through the
envelope's identity pattern and the packet's token set, and the exposure
check, through the packet's token set - and no more independence than that
is claimed.

THIS MODULE READS NO CUSTODY. It renders no packet, opens no withheld
authoring or construction record, names no case as a literal and holds no
disposition token or schema literal as a literal. It reads the published
register and record, the validation corpus's committed tree and manifests
at the corpus landing, and, for identity disjointness only, the published
manifests of both earlier corpora.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any token is right, or any authored intent, method,
family, agreement or divergence; that the confirmed return whose hash the
register reproduces is the reviewer's own act, which the reviewer confirms
by accepting this record;
the absence of influence, semantic independence or reviewer blinding;
anything about the reviewer's process or prior exposure beyond what the
record carries; that any custody record exists or is intact; whether any
exchange falls within ADR-0047 decision 3 or whether any model was
contacted; or that any reproduction, reveal, comparison or count may now
begin.
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
# The published, remotely verified correction W8-CHC: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "a08ba584bea8e2576dd7450c6374a4ff4f0aa149"

HOME = "governance/validation-cases"
MANIFEST = HOME + "/W8-V1-commitment-manifest.json"
CMANIFEST = HOME + "/W8-V1-construction-manifest.json"
FOREIGN_MANIFESTS = (
    "governance/discriminating-instrument/W8-D2-commitment-manifest.json",
    "governance/discriminating-supplement/W8-S1-commitment-manifest.json")
REGISTER_HOME = "governance/validation-review"
REGISTER = REGISTER_HOME + "/W8-D4-validation-register.json"
RECORD = "docs/phases/W8-D4-validation-session-record.md"
SELF_REL = "tests/test_w8_validation_session.py"
CALIBRATION = "tests/test_w8_calibration_law.py"
LAWMOD = "tests/test_w8_validation_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
ADR54 = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
REVEAL_ROOT = "governance/validation-reveal/"
LATER_RECORDS = ("docs/phases/W8-D4-validation-record.md",
                 "docs/phases/W8-D4-completion-record.md")
FIXED_CENSUS = frozenset({REGISTER, RECORD, SELF_REL, CALIBRATION, LAWMOD,
                          REGISTRY, BOARD})
TOTAL = 18
SESSION_ENTRIES = frozenset({"W8-D4-VSR", "W8-D4-DR-01"})
EARLIER_D4 = frozenset({"W8-D4-IVB", "ADR-0060", "W8-D4-VCR", "W8-V1-CM-01",
                        "W8-V1-CM-02"})
LATER_DELIVERABLES = ("W8-D5", "W8-D6", "W8-D7")

# The helper modules whose snapshot bytes the proofs execute.
HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": CALIBRATION,
           "rec": "tests/test_w8_session_recovery_law.py",
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "law": LAWMOD}

# The session's fixed values, carried by the record (VS4).
ACT_DATE = "2026-10-17"
REVIEWER_ROLE = "the human authority, as the sole human reviewer"
PACKET_SHA256 = ("sha256:84f937fc6b2ae6ad0dda973bb2b336289ea80a4c031825380d0e"
                 "7ffe222a290a")
RETURN_SHA256 = ("sha256:3532f852bdad6285fcd9538dab49eeafc9e64f29249496bb3bd7"
                 "ad9f94701235")

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    CALIBRATION: ("disposition-law module",
                  "sha256:2dca05bbd21544cdd3e524e59c2e431172e88e571441a22588f47a9f2141e36f",
                  "9163e63f24b501b480a8b4679f983da85ed5aa2f"),
    LAWMOD: ("validation-law module",
             "sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02",
             "ce39f6c0812cae5c36d646f3db211547544560ce"),
    REGISTRY: ("registry",
               "sha256:08cd28c96ab3f691a87b73c591b1eb595cb33e11117b414e07f166074dcf8aca",
               "374c45c0372055bfc49da790c271ccb70c94e5ca"),
    BOARD: ("board",
            "sha256:7293390b70d8198cabccd6d0b33a7445b900e9fd183c98afac94e973c6b9c6e8",
            "a60b4abd6880480ad9142bc15ec821777715ee84"),
}
# The reviewed post-images of the two successions: (LF SHA-256, blob).
POSTIMAGE = {CALIBRATION: ("sha256:aa3870f66b9fc8b739e35261412f25243aedf29c50b41d4f7ac15a28152b757c", "aaba3ce6dd15dfc194d7b8e0f5e2960099df6bc7"),
             LAWMOD: ("sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113", "609989bfe7004fddebe760cb92a7ff8d692ad0af")}

# ----------------------------------------- the two staged successions (d38)
SITES = {
    CALIBRATION: (
        ('K12',
         'SESSION_MANIFEST = ("governance/discriminating-supplement/"\n                    "W8-S1-commitment-manifest.json")\n',
         'SESSION_MANIFEST = ("governance/discriminating-supplement/"\n                    "W8-S1-commitment-manifest.json")\n# K12\'s register-schema limb as succeeded at the validation session\n# landing (ADR-0060 Part J decision 38): the validation register joins\n# the register schema\'s admitted instances beside the published register;\n# the former holders stay proven at that landing\'s baseline.\nVALIDATION_BASELINE = "a08ba584bea8e2576dd7450c6374a4ff4f0aa149"\nVALIDATION_REGISTER = ("governance/validation-review/"\n                       "W8-D4-validation-register.json")\n'),
        ('K12',
         '        for marker in (packet.PACKET_SCHEMA, REGISTER_SCHEMA):\n            allowed = homes | ({REGISTER_PATH} if marker == REGISTER_SCHEMA\n                               else set())\n',
         '        with self.subTest(fact="the register schema lived only in the law, "\n                               "its code and the published register at the "\n                               "validation session landing\'s baseline"):\n            held = {p.split(":", 1)[1] for p in subprocess.run(\n                ["git", "grep", "-l", "-F", REGISTER_SCHEMA,\n                 VALIDATION_BASELINE], cwd=ROOT, capture_output=True,\n                text=True).stdout.split()}\n            self.assertIn(REGISTER_PATH, held)\n            self.assertNotIn(VALIDATION_REGISTER, held)\n            self.assertTrue(held <= homes | {REGISTER_PATH},\n                            sorted(held))\n        for marker in (packet.PACKET_SCHEMA, REGISTER_SCHEMA):\n            allowed = homes | ({REGISTER_PATH, VALIDATION_REGISTER}\n                               if marker == REGISTER_SCHEMA else set())\n'),
    ),
    LAWMOD: (
        ('VL10',
         'CORPUS_IDS = frozenset({"W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02"})\n',
         'CORPUS_IDS = frozenset({"W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02"})\n# Admitted at the session landing (ADR-0060 Part J decision 38): the\n# register home, the register, the session record and the two W8-D4\n# entries they add. The corpus-stage state stays proven at the corpus\n# landing commit.\nD4C_LANDING = "f638cca75ec4a192685bf5cd53f29451cfdbbdd9"\nSESSION_REGISTER = VALIDATION_HOMES[1] + "/W8-D4-validation-register.json"\nSESSION_RECORD = LATER_RECORDS[1]\nSESSION_IDS = frozenset({"W8-D4-VSR", "W8-D4-DR-01"})\n'),
        ('VL10',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it."""\n    admitted = frozenset(corpus or ())\n    landed = corpus is not None\n    ids = D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    on_disk_ok = admitted | ({VALIDATION_HOMES[0]} if landed else set())\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None, session=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it. Succeeded at the session\n    landing: `session` is that landing\'s admitted path set - the\n    register and the session record - or None for the state before it."""\n    admitted = frozenset(corpus or ()) | frozenset(session or ())\n    landed = corpus is not None\n    held = session is not None\n    ids = (D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n           | (SESSION_IDS if held else frozenset()))\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    on_disk_ok = (admitted | ({VALIDATION_HOMES[0]} if landed else set())\n                  | ({VALIDATION_HOMES[1]} if held else set()))\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n'),
        ('VL10',
         '    def test_vl10_no_later_artefact_before_its_own_landing(self):\n        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names. Succeeded at the corpus landing: the former\n        # absence stays proven at the D4-B landing commit, and the present\n        # admits exactly that landing\'s artefacts.\n        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()\n        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[\n            "entries"]\n        before_holders = schema_holders(\n            before, lambda p: committed(D4B_LANDING, p))\n        with self.subTest(fact="nothing later existed at the D4-B landing"):\n            self.assertEqual(staged_absence_violations(\n                before, lambda p: False, before_entries, before_holders), [])\n            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        adds = _git("log", "--diff-filter=A", "--format=%H", "--",\n                    CORPUS_RECORD).split()\n        corpus = corpus_admitted(\n            (lambda rel: committed(adds[-1], rel)) if adds\n            else (lambda rel: _lf(read(rel))))\n        with self.subTest(fact="exactly the corpus landing\'s artefacts are "\n                               "admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus), [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module and the construction manifest"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        planted_entry = dict(entries[-1], id="W8-D4-VSR", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus),\n                "a tracked register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus),\n                "a session record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[1], entries,\n                    holders, corpus),\n                "a premature session entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n',
         '    def test_vl10_no_later_artefact_before_its_own_landing(self):\n        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names. Succeeded at the corpus landing and again at\n        # the session landing: each former state stays proven at its own\n        # landing commit, and the present admits exactly the landed\n        # artefacts.\n        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()\n        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[\n            "entries"]\n        before_holders = schema_holders(\n            before, lambda p: committed(D4B_LANDING, p))\n        with self.subTest(fact="nothing later existed at the D4-B landing"):\n            self.assertEqual(staged_absence_violations(\n                before, lambda p: False, before_entries, before_holders), [])\n            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))\n        at_corpus = _git("ls-tree", "-r", "--name-only", D4C_LANDING).split()\n        corpus_entries = json.loads(committed(D4C_LANDING, REGISTRY))[\n            "entries"]\n        corpus_holders = schema_holders(\n            at_corpus, lambda p: committed(D4C_LANDING, p))\n        corpus = corpus_admitted(lambda rel: committed(D4C_LANDING, rel))\n        with self.subTest(fact="nothing of the session existed at the corpus "\n                               "landing"):\n            self.assertEqual(staged_absence_violations(\n                at_corpus, lambda p: False, corpus_entries, corpus_holders,\n                corpus), [])\n            self.assertEqual(sorted(corpus_holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        session = {SESSION_REGISTER, SESSION_RECORD}\n        with self.subTest(fact="exactly the corpus and session landings\' "\n                               "artefacts are admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus, session), [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module and the construction manifest"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        planted_entry = dict(entries[-1], id="W8-D4-VRC", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus, session),\n                "an extra file in the register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus, session),\n                "a reveal-home path": (\n                    tracked + [VALIDATION_HOMES[2] + "/authoring/x.json"],\n                    exists, entries, holders, corpus, session),\n                "a validation record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[2], entries,\n                    holders, corpus, session),\n                "a premature validation-record entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus, session),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus,\n                    session),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None, session),\n                "the session artefacts without their landing": (\n                    tracked, exists, entries, holders, corpus, None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n'),
    ),
}
D38_CLAUSE = ("the disposition-law module's K12 register-schema limb admits "
              "exactly the validation register beside the published W8-D3 "
              "register; and VL10 admits exactly the register home, the "
              "register, the session record and the two W8-D4 entries they "
              "add.")

# The record's two tables, each read whole.
BINDING_SECTION = "## 2. The register and the bindings"
BINDING_HEADER = "| Binding | Value |"
BINDING_SEPARATOR = "|---|---|"
SUCCESSION_SECTION = "## 8. Proof successions at this landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"

# --------------------------------------- board and registry: authorised edits
VSR_LINK = ("([`W8-D4-validation-session-record.md`]"
            "(W8-D4-validation-session-record.md))")
VSR_STATUS_TAIL = (
    "the human authority's eighteen individual dispositions on the "
    "validation corpus, one lawful token per case, in governed register "
    "`W8-D4-DR-01`, with the packet hash, the corpus binding, the reviewer's "
    "own procedural account and the record of prior exposure; nothing "
    "withheld was read, the dispositions are fixed on publication, and D4-E "
    "stays closed until this record is published and independently "
    "remote-verified.")
VSR_STATUS = {
    "draft": ("**A draft validation session record, `W8-D4-VSR`, is before "
              "the human reviewer** " + VSR_LINK + ": if accepted, it would "
              "record " + VSR_STATUS_TAIL),
    "accepted": ("**`W8-D4-VSR` — the validation session record — is "
                 "accepted** " + VSR_LINK + " — accepted %s: it records "
                 + VSR_STATUS_TAIL),
}
VSR_ROW = ("| W8-D4 — Validation Session (record, W8-D4-VSR) | "
           "[`W8-D4-validation-session-record.md`]"
           "(W8-D4-validation-session-record.md) | ")
VSR_ROW_BODY = (
    "Tier J: **the D4-D session record** — the human authority's eighteen "
    "individual dispositions on the validation corpus `W8-V1`, one lawful "
    "token per case, returned complete from the session packet rendered by "
    "the published renderer from committed Git objects and transcribed "
    "exactly into governed register `W8-D4-DR-01`, whose acceptance this "
    "record carries; it binds the act's date, the reviewer role, the packet "
    "hash, the register and the corpus's four-value binding, states that "
    "every token is an individual human act and that the corpus had one "
    "session, and carries the reviewer's procedural account verbatim with "
    "the record of prior exposure, publication conditional on that account "
    "remaining complete and accurate and no test claimed to prove the "
    "absence of influence. Custody checked for existence only; the "
    "disposition-law K12 register-schema limb and the validation law's VL10 "
    "succeed by exact transformation. **No withheld byte read; no "
    "reproduction, reveal, comparison or count; D4-E stays closed until "
    "this record is published and remotely verified.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = ("until the reveal landing. **No divergence is "
                       "diagnosed")
BOARD_ROW_HEAD = "| W8 — Case-Home Scope Correction (W8-CHC) | "
VSR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
VSR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRIES = (
    {"id": "W8-D4-VSR", "path": RECORD, "type": "phase-record",
     "title": "W8-D4 - Validation Session Record",
     "role": (
         "The W8-D4 session record of landing D4-D on the validation corpus "
         "W8-V1: the human authority's eighteen individual dispositions, one "
         "lawful token per case, returned complete from the session packet "
         "rendered by the published renderer from committed Git objects, and "
         "bound exactly into the disposition register whose acceptance this "
         "record carries as governed register W8-D4-DR-01. Carries the act's "
         "date, the reviewer role, the packet SHA-256, the register binding "
         "and the corpus's four-value binding (corpus landing commit, case "
         "home tree and both manifests' SHA-256), the statement that every "
         "token is an individual human act, the one-session rule, the "
         "reviewer's procedural account verbatim with each statement's own "
         "date, the record of the reviewer's prior exposure, and the "
         "architect's and implementer's accounts separately attributed, with "
         "publication conditional on the account remaining complete and "
         "accurate; no test proves the absence of influence, and none is "
         "claimed. Records the existence-only custody check, and moves "
         "exactly the disposition-law K12 register-schema limb and the "
         "validation law's VL10 by exact transformation, with proof "
         "obligations VS1 to VS12. No withheld byte read; no reproduction, "
         "reveal, comparison or count; D4-E stays closed."),
     "depends_on": ["ADR-0060", "W8-D4-IVB", "W8-D4-VCR", "W8-V1-CM-01",
                    "W8-V1-CM-02", "W8-CHC", "ADR-0057", "ADR-0058",
                    "ADR-0054", "ADR-0055", "W8-D2-CBC", "ADR-0056", "W8-AR",
                    "W7-CR"]},
    {"id": "W8-D4-DR-01", "path": REGISTER, "type": "governed-register",
     "title": "W8-D4 - Validation Disposition Register",
     "role": (
         "The disposition register of W8-D4 landing D4-D: one closed "
         "canonical-bytes object under ADR-0057 decision 9 as ADR-0060 "
         "decision 28 carries it, one row per case of the validation corpus "
         "W8-V1, sorted by case identity, each row exactly the case identity "
         "and the human reviewer's returned token; it carries no authored "
         "class, intended disposition, method, family, construction map, "
         "rationale, confidence, timestamp or other withheld authoring "
         "metadata, and binds this corpus only. Its acceptance is carried by "
         "the record W8-D4-VSR; after publication every disposition is "
         "fixed."),
     "depends_on": ["W8-D4-VSR", "ADR-0060", "ADR-0057", "W8-V1-CM-01",
                    "ADR-0054"]},
)

# -------------------------------------------- the reviewer's own words
STATEMENT_LABEL = ("8. **The reviewer's statement, given on 2026-10-17, "
                   "verbatim:**")
STATEMENT = "> i reviewed it independently.\n"
CLARIFICATION_LABEL = ("9. **The reviewer's clarification, given on "
                       "2026-10-18, verbatim:**")
CLARIFICATION = "> no to both\n"
ACCOUNT_LABEL = ("10. **The reviewer's account, drafted on 2026-10-18 and "
                 "adopted by the reviewer on 2026-10-19, verbatim:**")
ACCOUNT_PARAGRAPHS = (
    "Dated 18 October 2026.",
    "I reviewed the W8-D4 validation cases independently and confirm that "
    "my submitted return is complete.",
    "I relayed W8-D3 documents between the architect and the implementer, "
    "but I did not read their contents. I did not read W8-D3 summaries in "
    "our messages or the method descriptions in the opening brief or "
    "ADR-0060.",
    "From my first access to the validation corpus through the date of this "
    "account, I received the procedural and drafting help described "
    "separately by the architect and implementer, and no other assistance.",
    "I will report any further assistance or relevant event before the "
    "session record is published so that the account can be updated.",
)
ACCOUNT = ">\n".join("> %s\n" % p for p in ACCOUNT_PARAGRAPHS)
CONFIRMATION_LABEL = ("11. **The reviewer's confirmation of the return, "
                      "given on 2026-10-19, verbatim:**")
CONFIRMATION = ("> I confirm that the attached return is my complete "
                "submitted return.\n")
CONTINUATION_LABEL = ("12. **The reviewer's continuation of the account, "
                      "dated 21 October 2026 and adopted by the reviewer on "
                      "2026-10-21, verbatim:**")
CONTINUATION_PARAGRAPHS = (
    "Since my account dated 18 October 2026, I have received only the "
    "procedural and drafting assistance described separately by the "
    "architect and the implementer, including the session-candidate reviews "
    "and repairs and help drafting this continuation.",
    "I have received no other assistance and have no other relevant events "
    "to report. Nothing changes my earlier account; this continuation "
    "carries it forward through 21 October 2026.",
    "I will report any further assistance or relevant event before the "
    "session record is published so that my account can be updated.",
)
CONTINUATION = ">\n".join("> %s\n" % p for p in CONTINUATION_PARAGRAPHS)
HUMAN_BLOCKS = ((STATEMENT_LABEL, STATEMENT),
                (CLARIFICATION_LABEL, CLARIFICATION),
                (ACCOUNT_LABEL, ACCOUNT),
                (CONFIRMATION_LABEL, CONFIRMATION),
                (CONTINUATION_LABEL, CONTINUATION))
# The procedural framing: the architect's and the implementer's, each only
# in its own separately attributed item, outside every quotation block.
ARCHITECT_ITEM = ("15. **The architect's procedural account and drafting "
                  "assistance, separately attributed")
ARCHITECT_FRAMING = (
    "delivered the cases verbatim, one at a time",
    "the architect assembled the account draft",
    "the clarification in item 9 answered the architect's two questions",
    "the account's role language is drafted wording, not a silent "
    "alteration of a quotation",
    "The architect also helped the reviewer put the continuation in item 12 "
    "into words, from the reviewer's own factual answer.",
)
IMPLEMENTER_ITEM = "16. **The implementer's account, separately attributed.**"
IMPLEMENTER_FRAMING = (
    "rendered the packet and delivered it on 2026-10-17 with a case-free "
    "review procedure",
    "Nothing case-level reached the reviewer from the implementer",
    "On 2026-10-21 the reviewer supplied the continuation in item 12 in the "
    "reviewer's own message, and the implementer carried it verbatim into "
    "this candidate.",
)
# The published acceptance dates of the documents decision 29's prior
# exposure concerns, each stated by the record as in the registry.
EXPOSURE_FACTS = (
    ("W8-D3-CCR", "2026-10-13",
     "whose record `W8-D3-CCR` the human authority accepted on 2026-10-13"),
    ("W8-D4-IVB", "2026-10-14",
     "the opening brief `W8-D4-IVB` and in ADR-0060, each accepted by the "
     "human authority on 2026-10-14"),
    ("ADR-0060", "2026-10-14",
     "the opening brief `W8-D4-IVB` and in ADR-0060, each accepted by the "
     "human authority on 2026-10-14"),
    ("W8-D4-VCR", "2026-10-15",
     "was accepted as `W8-D4-VCR` on 2026-10-15"),
)
REQUIRED = (
    "Every token in the register is an individual human act.",
    "The implementer transcribed the returned tokens exactly, and inferred, "
    "defaulted, filled, bulk-selected, recommended or substituted none.",
    "Set in the packet's own response form, the register's rows reproduce "
    "byte for byte the confirmed return whose SHA-256 the architect records "
    "in item 15.",
    "this record does not say whether any family exists.",
    "Case independence carries whole: each case is dispositioned on its own "
    "two variants alone, and no case is decided because of another "
    "(ADR-0054 decision 30).",
    "The adopted account describes the conduct interval from the reviewer's "
    "first access to the validation corpus's case material, at the review of "
    "its authoring candidate, through 18 October 2026, and the continuation "
    "carries it forward through 21 October 2026.",
    "Its adoption on 2026-10-19 preserves the earlier statements' dates and "
    "does not itself extend the account's factual coverage; the continuation "
    "carries its actual date and the reviewer's own adopted words, as any "
    "later continuation must.",
    "the account adopted on 2026-10-19 for the period it describes, carried "
    "forward by the continuation adopted on 2026-10-21.",
    "It is a human statement. No test proves the absence of influence, "
    "semantic independence or reviewer blinding, and none is claimed.",
    "Publication of this record is conditional on that account remaining "
    "complete and accurate through publication: any further relevant event "
    "is reported before publication, and an event that requires an updated "
    "account or review pauses publication.",
    "This condition is a continuing process duty, not a machine proof and "
    "not an advance assertion about future events.",
    "The reviewer's prior exposure is recorded here and never attested away "
    "(ADR-0060 decision 29).",
    "that record's item 7 records that access as the beginning of the "
    "conduct interval.",
    "neither acceptance nor possession alone establishes which contents were "
    "read.",
    "Neither the facts nor the statements determine what influence, if any, "
    "followed, and this record makes no such determination.",
    "and this record claims no more independence than that.",
    "it is not part of the reviewer's account.",
    "the implementer made no determination about the reviewer's process.",
    "This record does not classify any exchange under ADR-0047 decision 3 "
    "and does not state whether model contact occurred;",
    "The conduct interval continues until this record is published, and any "
    "further relevant event must be reported before publication.",
    "No observation under ADR-0057 decision 11 was volunteered, so none is "
    "carried.",
    "Before this record is published the reviewer alone may revise a token, "
    "by explicit act. After publication a disposition is fixed. After "
    "reveal, no disposition may be amended by any route.",
    "The location is never named in any surface.",
    "No withheld byte was read:",
    "A proof over named custody records establishes binding mechanics only;",
    "No other existing proof moves at this landing.",
    "D4-E stays closed until this record is published and independently "
    "remote-verified.",
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


def worktree(rel):
    """A candidate surface before this landing's commit exists: the register
    is read as its raw, unconverted bytes; every other surface keeps its LF
    treatment."""
    raw = (ROOT / rel).read_bytes()
    return raw if rel == REGISTER else _lf(raw)


def l9_snapshot():
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
        return None, ["the session record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return worktree(rel) if commit is None else committed(commit, rel)


def snapshot():
    commit, problems = l9_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


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
    ns = {"__name__": "_w8_vsr_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def manifest_rows(rel):
    return json.loads(committed(CORPUS, rel))["rows"]


def manifest_ids():
    return [r["case_id"] for r in manifest_rows(MANIFEST)]


def foreign_ids():
    out = set()
    for rel in FOREIGN_MANIFESTS:
        out |= {r["case_id"] for r in json.loads(committed(CORPUS, rel))[
            "rows"]}
    return out


def home_case_paths():
    names = _git("ls-tree", "--name-only", CORPUS + ":" + HOME).split()
    return sorted("%s/%s" % (HOME, n) for n in names if n.startswith("W8-C-"))


def observed_binding():
    return {"commit": CORPUS,
            "home_tree": _git("rev-parse", CORPUS + ":" + HOME).strip(),
            "commitment": _sha(_lf(committed(CORPUS, MANIFEST))),
            "construction": _sha(_lf(committed(CORPUS, CMANIFEST)))}


def register_violations(raw, ids, h):
    """The register's exact bytes: one closed canonical object under the
    law, LF only with exactly one terminal LF, one row per bound identity in
    order, each a lawful token."""
    v = []
    if b"\r" in raw or not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        v.append("the register is not LF with exactly one terminal LF")
    try:
        obj = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return v + ["the register is not JSON"]
    if h.env.canonical_bytes(obj) != raw:
        v.append("the register is not in canonical bytes")
    v += h.cal.register_violations(obj, ids)
    rows = obj.get("rows") if isinstance(obj, dict) else None
    got = ([r.get("case_id") if isinstance(r, dict) else None for r in rows]
           if isinstance(rows, list) else None)
    if got != list(ids):
        v.append("the rows are not exactly the bound identities, in order")
    return v


def transcription_violations(raw, h):
    """The register is the exact transcription of the confirmed return: its
    rows, set in the packet's own response form, reproduce the return's
    recorded SHA-256 byte for byte."""
    try:
        rows = json.loads(raw.decode("utf-8"))["rows"]
        text = "".join("%s %s\n" % (h.pkt.response_line(r["case_id"]),
                                    r["disposition"]) for r in rows)
    except (UnicodeDecodeError, ValueError, KeyError, TypeError):
        return ["the register cannot be set in the response form"]
    if _sha(text.encode("utf-8")) != RETURN_SHA256:
        return ["the register is not the exact transcription of the "
                "confirmed return"]
    return []


def register_ids(raw):
    return [r["case_id"] for r in json.loads(raw)["rows"]]


def binding_rows(record, h):
    """Section 2's binding table, read whole: (rows, violations)."""
    return h.rev.closed_table(record, BINDING_SECTION, BINDING_HEADER,
                              BINDING_SEPARATOR, 2)


def expected_binding_rows(register_raw):
    o = observed_binding()
    return [["Act date", ACT_DATE], ["Reviewer role", REVIEWER_ROLE],
            ["Packet SHA-256", "`%s`" % PACKET_SHA256],
            ["Register", "`%s`" % REGISTER],
            ["Register LF SHA-256", "`%s`" % _sha(_lf(register_raw))],
            ["Corpus landing commit", "`%s`" % o["commit"]],
            ["Case home tree at that commit", "`%s`" % o["home_tree"]],
            ["Commitment manifest LF SHA-256", "`%s`" % o["commitment"]],
            ["Construction manifest LF SHA-256", "`%s`" % o["construction"]]]


def binding_table_violations(record, register_raw, h):
    rows, v = binding_rows(record, h)
    if rows != expected_binding_rows(register_raw):
        v.append("the binding table is not exactly its trusted rows")
    return v


def recorded_binding(rows):
    d = {r[0]: r[1].strip("`") for r in rows if len(r) == 2}
    return {"commit": d.get("Corpus landing commit"),
            "home_tree": d.get("Case home tree at that commit"),
            "commitment": d.get("Commitment manifest LF SHA-256"),
            "construction": d.get("Construction manifest LF SHA-256")}


def chain_input(record, register_raw, h):
    rows, _ = binding_rows(record, h)
    ids = manifest_ids()
    return {"recorded": recorded_binding(rows),
            "observed": observed_binding(),
            "manifest_ids": ids,
            "construction_ids": [r["case_id"] for r in manifest_rows(
                CMANIFEST)],
            "foreign_ids": foreign_ids(),
            "packet_paths": ["%s/%s.json" % (HOME, i) for i in ids],
            "home_case_paths": home_case_paths(),
            "register_ids": register_ids(register_raw)}


def chain_violations(c):
    """The binding chain of ADR-0060 decision 25 through the register: the
    recorded binding is the published one at the corpus commit; the case
    set, the packet inputs and the register rows are each exactly the bound
    commitment manifest's identities."""
    v = []
    rec, obs = c["recorded"], c["observed"]
    if any(rec.get(k) in (None, "") for k in obs) or rec != obs:
        v.append("the recorded binding is not the published one")
    ids = c["manifest_ids"]
    if len(ids) != TOTAL or len(set(ids)) != TOTAL or ids != sorted(ids):
        v.append("the bound manifest is not eighteen distinct identities in "
                 "order")
    if c["construction_ids"] != ids:
        v.append("the construction manifest is not one-to-one with the "
                 "commitment manifest")
    if set(ids) & set(c["foreign_ids"]):
        v.append("an identity of an earlier corpus is bound")
    paths = ["%s/%s.json" % (HOME, i) for i in ids]
    if c["packet_paths"] != paths or c["home_case_paths"] != paths:
        v.append("the packet inputs are not exactly the manifest's case "
                 "paths")
    if c["register_ids"] != ids:
        v.append("the register rows are not exactly the bound identities")
    return v


def quotation_blocks(text):
    """Every block of contiguous quotation lines, each with its LFs."""
    blocks, current = [], []
    for line in text.split("\n"):
        if line.startswith(">"):
            current.append(line + "\n")
        elif current:
            blocks.append("".join(current))
            current = []
    if current:
        blocks.append("".join(current))
    return blocks


INDENTED_QUOTE = re.compile(r"^[ \t]+>")
VCR_RECORD = "docs/phases/W8-D4-validation-corpus-record.md"
VCR_ITEM_7 = ("7. **The reviewer's access to the visible cases at this landing "
              "is lawful access to visible evidence: it begins the conduct "
              "interval of ADR-0060 decision 27**")


def markdown_blank(line):
    """A blank line as Markdown defines it: empty, or SPACE and TAB only.
    Any other character - a no-break space, an em space, a form feed -
    makes the line text, which may lazily continue a quotation."""
    return line.strip(" \t") == ""


def quote_boundary_violations(text):
    """The quotation boundary, closed for this record's fixed layout: no
    quotation marker is indented (CommonMark admits up to three spaces), and
    every run of quotation lines is set apart by a Markdown blank line, or
    the record's start or end, on each side, so that no lazily continued or
    adjoining line can join a quotation unseen."""
    v = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if INDENTED_QUOTE.match(line):
            v.append("an indented quotation marker")
        if not line.startswith(">"):
            continue
        prev = lines[i - 1] if i > 0 else ""
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if not markdown_blank(prev) and not prev.startswith(">"):
            v.append("a quotation is not set apart above")
        if not markdown_blank(nxt) and not nxt.startswith(">"):
            v.append("a quotation is not set apart below")
    return v


def nine_rules_block():
    adr = _lf(committed(BASELINE, ADR54)).decode("utf-8")
    m = re.search(r"^> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                  r"failure\.\*\*)$", adr, re.M)
    return "> %s\n" % m.group(1) if m else None


def attribution_violations(text):
    """The attribution boundary: every quotation block is exactly one of the
    four human statements or the nine rules, each once; each human statement
    sits directly under its own dated label; and the architect's and the
    implementer's framing each appear once, outside every block, only in
    their separately attributed items."""
    v = quote_boundary_violations(text)
    blocks = quotation_blocks(text)
    expected = [b for _, b in HUMAN_BLOCKS] + [nine_rules_block()]
    if sorted(blocks) != sorted(expected):
        v.append("the quotation blocks are not exactly the four human "
                 "statements and the nine rules, each once")
    for label, block in HUMAN_BLOCKS:
        if text.count(label) != 1:
            v.append("a dated label is missing or repeated")
        if text.count(label + "\n\n" + block) != 1:
            v.append("a human statement is not verbatim directly under its "
                     "dated label")
    for item, framing in ((ARCHITECT_ITEM, ARCHITECT_FRAMING),
                          (IMPLEMENTER_ITEM, IMPLEMENTER_FRAMING)):
        lines = [l for l in text.split("\n") if l.startswith(item)]
        for f in framing:
            if text.count(f) != 1:
                v.append("attributed framing occurs %d times" % text.count(f))
            if any(f in b for b in blocks):
                v.append("attributed framing sits inside a quotation block")
            if len(lines) != 1 or f not in lines[0]:
                v.append("attributed framing is outside its attributed item")
    return v


def exposure_fact_violations(record, registry_at_baseline):
    v = []
    by_id = {e["id"]: e for e in registry_at_baseline["entries"]}
    flat = _flat(record)
    for eid, date, fragment in EXPOSURE_FACTS:
        e = by_id.get(eid)
        if e is None or (e["status"], e["accepted_date"]) != ("accepted",
                                                              date):
            v.append("%s is not accepted on %s in the registry" % (eid, date))
        if fragment not in flat:
            v.append("the record does not state %s's acceptance date" % eid)
    return v


def succession_rows(h):
    return [["`%s`" % rel, ", ".join(h.auth.labels(SITES[rel])),
             "`%s`" % PREIMAGE[rel][1], "`%s`" % POSTIMAGE[rel][0]]
            for rel in (CALIBRATION, LAWMOD)]


def succession_table_violations(record, h):
    rows, v = h.rev.closed_table(record, SUCCESSION_SECTION,
                                 SUCCESSION_HEADER, SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted rows, in "
                 "order")
    return v


def succession_violations(rel, present, record, h, sites=None):
    """The exact staged transformation of a proof module: its fixed baseline
    pre-image under the site table yields exactly the present bytes, each
    site occurs once, the table reverses, the result is the reviewed
    post-image, and the record's closed succession table pins it."""
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


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def vsr_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and VSR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (VSR_ACCEPTED % date) not in head:
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
         "until the reveal landing. " + fill(VSR_STATUS[state])
         + " **No divergence is diagnosed"),
        ("row", anchor,
         anchor + VSR_ROW + fill(ROW_PREFIX[state]) + VSR_ROW_BODY + " |\n"),
    )


def new_entry(spec, state, date, content_hash):
    return {
        "id": spec["id"], "aliases": [], "title": spec["title"],
        "type": spec["type"], "phase": "W8", "deliverable": "W8-D4",
        "path": spec["path"], "status": state,
        "accepted_date": date if state == "accepted" else None,
        "role": spec["role"], "governs": [],
        "depends_on": list(spec["depends_on"]), "resolves": [],
        "id_namespaces": [], "implementation_permission": "none",
        "open_decisions": [], "content_hash": content_hash,
        "hash_exclusion_reason": None, "errata": [],
    }


def expected_registry(base_text, hashes, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    added = [new_entry(spec, state, date, hashes[spec["path"]])
             for spec in NEW_ENTRIES]
    return (base_text[:-len(tail)] + "\n    },\n"
            + ",\n".join(_indent(json.dumps(e, indent=2, ensure_ascii=False),
                                 4) for e in added)
            + "\n  ]\n}\n")


def added_board_wording():
    return " ".join([VSR_ROW, VSR_ROW_BODY] + list(VSR_STATUS.values()))


def reserved_literals(h):
    """The reserved token and schema literals, as the snapshot defines
    them."""
    return (tuple(sorted(h.pkt.TOKENS)),
            (h.pkt.PACKET_SCHEMA, h.cal.REGISTER_SCHEMA, h.env.AUTHORING_SCHEMA)
            + tuple(h.law.NEW_SCHEMAS))


def exposure_violations(text, pins, h):
    """No case identity, no digest-shaped string apart from the exact pins,
    no disposition token, no reserved authoring label, no schema literal and
    no count statement."""
    v = h.rec.exposure_violations(text, pins)
    v += ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    _, schemas = reserved_literals(h)
    v += ["a schema literal is present" for s in schemas if s in text]
    if h.cal.COUNT_STATEMENT in text:
        v.append("a count statement is present")
    return v


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted
    to call is replaced - gates that refuse nothing and helpers that return
    nothing - and the previous state is restored on exit. It requires no
    live name to exist: a helper a later landing has renamed or removed is
    installed temporarily and removed again on exit, and every value that
    existed before is restored by identity."""

    ABSENT = object()
    TARGETS = (
        ("test_w8_calibration_law", "register_violations",
         lambda *a, **k: []),
        ("test_w8_discriminating_instrument_envelope", "canonical_bytes",
         lambda *a, **k: b""),
        ("test_w8_session_recovery_law", "exposure_violations",
         lambda *a, **k: []),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_session_recovery_law", "R9_REVEAL", "mechanics sentinel"),
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
class VS1_RegisterShape(unittest.TestCase):
    def test_vs1_register_is_closed_canonical_and_complete(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "cal", "pkt")
        raw = read(REGISTER)
        ids = manifest_ids()
        with self.subTest(fact="the register's exact bytes are lawful and "
                               "complete"):
            self.assertEqual(register_violations(raw, ids, h), [])
        with self.subTest(fact="the register is the exact transcription of "
                               "the confirmed return"):
            self.assertEqual(transcription_violations(raw, h), [])
        obj = json.loads(raw)
        good = h.env.canonical_bytes(obj)
        rows = obj["rows"]
        other = next(t for t in sorted(h.pkt.TOKENS)
                     if t != rows[0]["disposition"])
        swapped = h.env.canonical_bytes(
            dict(obj, rows=[dict(rows[0], disposition=other)] + rows[1:]))
        with self.subTest(control="another lawful token on one row keeps the "
                                  "shape lawful but breaks the transcription"):
            self.assertEqual(register_violations(swapped, ids, h), [])
            self.assertTrue(transcription_violations(swapped, h))
        mutants = {
            "pretty-printed bytes": (json.dumps(obj, indent=2) + "\n")
            .encode("utf-8"),
            "a carriage return": good.replace(b"\n", b"\r\n"),
            "a second terminal LF": good + b"\n",
            "an unlawful token": h.env.canonical_bytes(
                dict(obj, rows=[dict(rows[0], disposition="pass")]
                     + rows[1:])),
            "a withheld field on a row": h.env.canonical_bytes(
                dict(obj, rows=[dict(rows[0], authored_class="A")]
                     + rows[1:])),
            "a missing row": h.env.canonical_bytes(dict(obj, rows=rows[1:])),
            "an identity followed by a newline": h.env.canonical_bytes(
                dict(obj, rows=[dict(rows[0], case_id=rows[0]["case_id"]
                                     + "\n")] + rows[1:])),
            "rows out of order": h.env.canonical_bytes(
                dict(obj, rows=rows[1:] + rows[:1])),
            "an extra outer field": h.env.canonical_bytes(
                dict(obj, note="x")),
            "a wrong schema": h.env.canonical_bytes(
                dict(obj, schema=obj["schema"] + "x")),
        }
        for name, mutated in mutants.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(register_violations(mutated, ids, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                self.assertEqual(register_violations(
                    raw, ids, helpers(read, "env", "cal")), [])


class VS2_BindingChain(unittest.TestCase):
    def test_vs2_membership_through_the_register(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        c = chain_input(read(RECORD).decode("utf-8"), read(REGISTER), h)
        with self.subTest(fact="the chain holds through the register"):
            self.assertEqual(chain_violations(c), [])
        with self.subTest(fact="the bound commit is the corpus commit, never "
                               "the session baseline"):
            self.assertEqual(c["observed"]["commit"], CORPUS)
            self.assertNotEqual(CORPUS, BASELINE)
        ids, foreign = c["manifest_ids"], sorted(c["foreign_ids"])
        planted = {
            "an earlier corpus's row": dict(
                c, register_ids=c["register_ids"][1:] + foreign[:1]),
            "a missing row": dict(c, register_ids=c["register_ids"][1:]),
            "a duplicate row": dict(
                c, register_ids=c["register_ids"][:-1]
                + c["register_ids"][:1]),
            "a wrong recorded commit": dict(c, recorded=dict(
                c["recorded"], commit=BASELINE)),
            "a missing recorded value": dict(c, recorded=dict(
                c["recorded"], home_tree=None)),
            "a wrong recorded manifest": dict(c, recorded=dict(
                c["recorded"], construction=c["recorded"]["commitment"])),
            "the manifest among the packet inputs": dict(
                c, packet_paths=c["packet_paths"] + [MANIFEST]),
            "a construction manifest out of step": dict(
                c, construction_ids=ids[1:] + ids[:1]),
        }
        for name, mutated in planted.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(chain_violations(mutated))


class VS3_CommittedObjectReading(unittest.TestCase):
    def test_vs3_working_copies_correspond_to_snapshot_bytes(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        for rel in (REGISTER, RECORD):
            with self.subTest(path=rel):
                self.assertEqual(_lf((ROOT / rel).read_bytes()),
                                 _lf(read(rel)))
                if commit is not None:
                    self.assertEqual(read(rel), committed(commit, rel))
        raw = read(REGISTER)
        with self.subTest(control="a one-byte content change is detected"):
            self.assertNotEqual(_lf(raw.replace(b"[", b"[ ", 1)), raw)
        with self.subTest(fact="a checkout's line-ending display is display "
                               "only"):
            self.assertEqual(_lf(raw.replace(b"\n", b"\r\n")), raw)


class VS4_RecordBindings(unittest.TestCase):
    def test_vs4_binding_table_is_exact(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        record = read(RECORD).decode("utf-8")
        raw = read(REGISTER)
        with self.subTest(fact="the binding table, read whole, is exactly "
                               "its trusted rows"):
            self.assertEqual(binding_table_violations(record, raw, h), [])
        rows = expected_binding_rows(raw)
        act = "| %s | %s |" % tuple(rows[0])
        for key, value in rows:
            with self.subTest(control="an altered %s is refused" % key):
                line = "| %s | %s |" % (key, value)
                self.assertTrue(binding_table_violations(
                    record.replace(line, "| %s | x%s |" % (key, value), 1),
                    raw, h))
        for name, mutated in {
                "a repeated row": record.replace(act, act + "\n" + act, 1),
                "an indented duplicate row": record.replace(
                    act, act + "\n " + act, 1),
                "a dropped row": record.replace(act + "\n", "", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(binding_table_violations(mutated, raw, h))
        for name, mutated in h.rev.boundary_mutants(
                record, BINDING_SECTION, act).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(binding_table_violations(mutated, raw, h))


class VS5_RecordCarriage(unittest.TestCase):
    def test_vs5_record_carries_its_statements(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        flat = _flat(text)
        for s in REQUIRED:
            with self.subTest(carried=s[:44]):
                self.assertEqual(flat.count(s), 1)
        with self.subTest(control="a removed statement is detected"):
            self.assertNotIn(REQUIRED[0], flat.replace(REQUIRED[0], ""))
        with self.subTest(fact="the nine-rule block is byte-identical"):
            block = nine_rules_block()
            self.assertIsNotNone(block)
            self.assertEqual(text.count(block), 1)
        reg = json.loads(committed(BASELINE, REGISTRY))
        with self.subTest(fact="the prior-exposure dates are the registry's"):
            self.assertEqual(exposure_fact_violations(text, reg), [])
        with self.subTest(control="a wrong prior-exposure date is detected"):
            self.assertTrue(exposure_fact_violations(text.replace(
                "accepted on 2026-10-13", "accepted on 2026-10-12", 1), reg))
        with self.subTest(fact="the corpus record's item 7 is the published "
                               "source of the first-access statement"):
            self.assertEqual(_lf(committed(BASELINE, VCR_RECORD)).decode(
                "utf-8").count(VCR_ITEM_7), 1)


class VS6_Attribution(unittest.TestCase):
    def test_vs6_human_statements_verbatim_and_framing_apart(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="the attribution boundary holds, the "
                               "quotation boundary closed"):
            self.assertEqual(attribution_violations(text), [])
        first, rest = ACCOUNT.split("\n>\n", 1)
        line = "Mechanics sentinel inserted into the quotation.\n"
        item_14 = next(l for l in text.split("\n")
                       if l.startswith(ARCHITECT_ITEM)) + "\n"
        boundary = {
            "a one-space quotation line after the statement": text.replace(
                STATEMENT, STATEMENT + " > " + line, 1),
            "a two-space quotation line after the statement": text.replace(
                STATEMENT, STATEMENT + "  > " + line, 1),
            "a three-space quotation line after the statement": text.replace(
                STATEMENT, STATEMENT + "   > " + line, 1),
            "an unmarked continuation after the statement": text.replace(
                STATEMENT, STATEMENT + line, 1),
            "an unmarked continuation after the account": text.replace(
                ACCOUNT, ACCOUNT + line, 1),
            "an unmarked continuation after the confirmation": text.replace(
                CONFIRMATION, CONFIRMATION + line, 1),
            "adjoining material before the account": text.replace(
                ACCOUNT_LABEL + "\n\n" + ACCOUNT,
                ACCOUNT_LABEL + "\n\n" + line + ACCOUNT, 1),
            "a one-space quotation line before the confirmation": text
            .replace(CONFIRMATION_LABEL + "\n\n" + CONFIRMATION,
                     CONFIRMATION_LABEL + "\n\n > " + line + CONFIRMATION, 1),
            "an indented quotation in the attributed context": text.replace(
                item_14, item_14 + "   > " + line, 1),
            "an unmarked continuation after the continuation": text.replace(
                CONTINUATION, CONTINUATION + line, 1),
            "a one-space quotation line before the continuation": text
            .replace(CONTINUATION_LABEL + "\n\n" + CONTINUATION,
                     CONTINUATION_LABEL + "\n\n > " + line + CONTINUATION, 1),
            "a dropped continuation": text.replace(
                CONTINUATION_LABEL + "\n\n" + CONTINUATION, "", 1),
            "a reworded continuation": text.replace(
                CONTINUATION_PARAGRAPHS[1], CONTINUATION_PARAGRAPHS[1].replace(
                    "through 21 October 2026", "through 22 October 2026"), 1),
            "the continuation merged into the account": text.replace(
                CONTINUATION_LABEL + "\n\n" + CONTINUATION, "", 1)
            .replace(ACCOUNT, ACCOUNT + ">\n" + CONTINUATION, 1),
            "the continuation's drafting help moved into its block": text
            .replace(CONTINUATION, CONTINUATION + ">\n> "
                     + ARCHITECT_FRAMING[-1] + "\n", 1),
        }
        for name, mutated in boundary.items():
            with self.subTest(boundary_control="%s is detected" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(attribution_violations(mutated))
        tested = (("statement", STATEMENT_LABEL, STATEMENT),
                  ("account", ACCOUNT_LABEL, ACCOUNT),
                  ("confirmation", CONFIRMATION_LABEL, CONFIRMATION),
                  ("continuation", CONTINUATION_LABEL, CONTINUATION))
        separators = (("a no-break space", " "), ("an em space", " "),
                      ("a form feed", "\u000c"))
        for which, label, block in tested:
            for sep_name, sep in separators:
                after = text.replace(block, block + sep + "\n" + line, 1)
                before = text.replace(label + "\n\n" + block,
                                      label + "\n\n" + sep + "\n" + block, 1)
                for place, mutated in (("after", after), ("before", before)):
                    with self.subTest(separator_control="%s line %s the %s "
                                      "is not a blank separator"
                                      % (sep_name, place, which)):
                        self.assertNotEqual(mutated, text)
                        self.assertTrue(quote_boundary_violations(mutated))
                        self.assertTrue(attribution_violations(mutated))
            for blank_name, blank in (("a space", " "), ("a tab", "\t"),
                                      ("spaces and tabs", " \t \t"),
                                      ("tabs and spaces", "\t  ")):
                accepted = text.replace(block + "\n", block + blank + "\n", 1)
                with self.subTest(blank_control="a line of %s after the %s "
                                  "is a blank separator" % (blank_name, which)):
                    self.assertNotEqual(accepted, text)
                    self.assertEqual(quote_boundary_violations(accepted), [])
                    self.assertEqual(attribution_violations(accepted), [])
        with self.subTest(fact="the record's own separators are blank lines "
                               "as Markdown defines them"):
            self.assertTrue(markdown_blank("") and markdown_blank(" \t"))
            self.assertFalse(markdown_blank(" ") or markdown_blank("\u000c"))
        mutants = {
            "a one-character change to the account": text.replace(
                ACCOUNT_PARAGRAPHS[1], ACCOUNT_PARAGRAPHS[1][:-1], 1),
            "reordered account paragraphs": text.replace(
                ACCOUNT, rest.rstrip("\n") + "\n>\n" + first + "\n", 1),
            "inserted material in the account": text.replace(
                ACCOUNT, ACCOUNT.replace("\n>\n", "\n>\n> (summary)\n>\n", 1),
                1),
            "the statement merged into the account": text.replace(
                STATEMENT_LABEL + "\n\n" + STATEMENT, STATEMENT_LABEL + "\n",
                1).replace(ACCOUNT, ACCOUNT + ">\n" + STATEMENT, 1),
            "a dropped confirmation": text.replace(CONFIRMATION, "", 1),
            "a reworded clarification": text.replace(
                CLARIFICATION, "> no to either\n", 1),
            "an altered account date": text.replace(
                ACCOUNT_LABEL, ACCOUNT_LABEL.replace("2026-10-19",
                                                     "2026-10-18"), 1),
            "architect framing moved into a block": text.replace(
                ACCOUNT, ACCOUNT + ">\n> " + ARCHITECT_FRAMING[0] + "\n", 1),
            "architect framing removed from its item": text.replace(
                ARCHITECT_FRAMING[0], "presented the cases", 1),
            "implementer framing moved into a block": text.replace(
                CONFIRMATION, CONFIRMATION + ">\n> " + IMPLEMENTER_FRAMING[1]
                + "\n", 1),
            "a planted quotation block": text.replace(
                CONTINUATION, CONTINUATION + "\n> (another statement)\n", 1),
        }
        for name, mutated in mutants.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(attribution_violations(mutated))


class VS7_NoExposure(unittest.TestCase):
    def test_vs7_no_case_token_label_schema_or_count_exposed(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "cor", "pkt", "cal", "env", "law")
        record = read(RECORD).decode("utf-8")
        raw = read(REGISTER)
        o = observed_binding()
        pins = [PACKET_SHA256, RETURN_SHA256, _sha(_lf(raw)), o["commitment"],
                o["construction"]]
        pins += [PREIMAGE[r][1] for r in (CALIBRATION, LAWMOD)]
        pins += [POSTIMAGE[r][0] for r in (CALIBRATION, LAWMOD)]
        pins = [p.split(":", 1)[1] for p in pins]
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        surfaces = {
            "record": (record, pins),
            "new registry roles and titles": (" ".join(
                by_id[s["id"]]["role"] + " " + by_id[s["id"]]["title"]
                for s in NEW_ENTRIES), []),
            "board wording this landing adds": (added_board_wording(), []),
        }
        for name, (text, excused) in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(exposure_violations(text, excused, h), [])
        tokens, schemas = reserved_literals(h)
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertTrue(tokens and schemas)
            self.assertEqual([t for t in tokens if t in src], [])
            self.assertEqual([s for s in schemas if s in src], [])
            self.assertIsNone(h.rec.CASE_ID_ANYWHERE.search(src))
        planted = {
            "a case identity": manifest_ids()[0],
            "a disposition token": tokens[0],
            "a bare digest": "e" * 64,
            "a reserved label": sorted(h.env.ALL_CHECKS)[0],
            "the register schema": h.cal.REGISTER_SCHEMA,
            "a count statement": h.cal.COUNT_STATEMENT,
        }
        for name, plant in planted.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(record + "\n" + plant,
                                                    pins, h))


class VS8_Successions(unittest.TestCase):
    def test_vs8_staged_successions_are_exact(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "cal", "law")
        record = read(RECORD).decode("utf-8")
        for rel in (CALIBRATION, LAWMOD):
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
            self.assertEqual(h.cal.VALIDATION_REGISTER, REGISTER)
            self.assertEqual(h.cal.VALIDATION_BASELINE, BASELINE)
            self.assertEqual(h.law.SESSION_REGISTER, REGISTER)
            self.assertEqual(h.law.SESSION_RECORD, RECORD)
            self.assertEqual(h.law.SESSION_IDS, SESSION_ENTRIES)
            self.assertEqual(h.law.D4C_LANDING, CORPUS)
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
                ("a tab-prefixed duplicate row", record.replace(
                    last + "\n", last + "\n\t" + last + "\n", 1)),
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
                for rel in (CALIBRATION, LAWMOD):
                    self.assertEqual(succession_violations(
                        rel, read(rel).decode("utf-8"), record, hh), [])


class VS9_AbsenceAtTheBaseline(unittest.TestCase):
    def test_vs9_nothing_before_and_nothing_later_at_this_snapshot(self):
        before = _git("ls-tree", "-r", "--name-only", BASELINE).split()
        base_entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
        with self.subTest(fact="at the baseline: no register home, register "
                               "or session record"):
            self.assertEqual([p for p in before if p.startswith(
                REGISTER_HOME + "/") or p == RECORD], [])
            self.assertEqual([e["id"] for e in base_entries
                              if e["id"] in SESSION_ENTRIES], [])
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tracked = snapshot_tracked(commit)
        entries = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="at this snapshot: no reveal home and no "
                               "later record"):
            self.assertEqual([p for p in tracked if p.startswith(REVEAL_ROOT)
                              or p in LATER_RECORDS], [])
        d4 = {e["id"] for e in entries if e["deliverable"] == "W8-D4"}
        with self.subTest(fact="at this snapshot: the W8-D4 entries are the "
                               "earlier ones and this landing's two"):
            self.assertEqual(d4, EARLIER_D4 | SESSION_ENTRIES)
            self.assertEqual([e["id"] for e in entries
                              if e["deliverable"] in LATER_DELIVERABLES], [])
        with self.subTest(control="a planted validation-record entry is "
                                  "refused"):
            planted = d4 | {"W8-D4-VRC"}
            self.assertNotEqual(planted, EARLIER_D4 | SESSION_ENTRIES)


class VS10_Registration(unittest.TestCase):
    def test_vs10_record_and_register_are_bound(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        state, date, v = vsr_state(read(RECORD).decode("utf-8"), h)
        self.assertEqual(v, [])
        for spec in NEW_ENTRIES:
            e = by_id.get(spec["id"])
            with self.subTest(entry=spec["id"]):
                self.assertIsNotNone(e)
                self.assertEqual((e["path"], e["type"], e["phase"],
                                  e["deliverable"]),
                                 (spec["path"], spec["type"], "W8", "W8-D4"))
                self.assertEqual(e["content_hash"],
                                 _sha(_lf(read(e["path"]))))
                self.assertEqual((e["status"], e["accepted_date"]),
                                 (state, date))
                self.assertTrue({"ADR-0060", "ADR-0057", "ADR-0054"}
                                <= set(e["depends_on"]))
        with self.subTest(fact="the register's acceptance is carried by the "
                               "record"):
            self.assertIn("W8-D4-VSR", by_id["W8-D4-DR-01"]["depends_on"])
        with self.subTest(control="a register status apart from the record "
                                  "is refused"):
            e = by_id["W8-D4-DR-01"]
            flipped = ("accepted", "2000-01-01") if state == "draft" \
                else ("draft", None)
            self.assertNotEqual((e["status"], e["accepted_date"]), flipped)


class VS11_RegistryAndBoard(unittest.TestCase):
    def test_vs11_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = vsr_state(read(RECORD).decode("utf-8"), h)
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
        hashes = {rel: _sha(_lf(read(rel))) for rel in (RECORD, REGISTER)}
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, hashes, state,
                                                    date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, hashes, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(fact="the W8-CHC entry and board row are "
                               "preserved"):
            chc = {e["id"]: e for e in json.loads(reg)["entries"]}["W8-CHC"]
            self.assertEqual((chc["status"], chc["accepted_date"]),
                             ("accepted", "2026-10-15"))
            self.assertEqual(board.count(BOARD_ROW_HEAD), 1)
        with self.subTest(control="an unauthorised registry edit is "
                                  "refused"):
            self.assertNotEqual(reg.replace('"W8-D4-VSR"', '"W8-D4-VSRx"'),
                                expected_registry(reg_pre, hashes, state,
                                                  date))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites,
                                         hh.rec.R9_REVEAL))


class VS12_Census(unittest.TestCase):
    def test_vs12_census_is_exactly_seven_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly seven paths"):
            self.assertEqual(len(FIXED_CENSUS), 7)
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {CALIBRATION, LAWMOD, SELF_REL})
        with self.subTest(fact="no corpus home is touched"):
            self.assertEqual([p for p in paths if p.startswith(
                (HOME + "/", "governance/discriminating-"))], [])
        record = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly seven "
                          r"paths:\*\* (.*?) ## ", record)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {LAW},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
