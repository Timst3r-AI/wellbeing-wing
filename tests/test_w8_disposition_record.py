"""W8-D3-C — human disposition record proofs (W8-D3-HDR, H1–H12).

The session landing of W8-D3 on the session corpus that ADR-0059 binds: the
human authority's twelve returned tokens bound into governed register
W8-D3-DR-01, and the session record W8-D3-HDR carrying the act's date, the
reviewer role, the packet hash, the register binding, the session-corpus
binding, the statement that every token is an individual human act and the
reviewer's procedural account verbatim (the initial attestation and its
dated continuation), with the three proof successions
ADR-0059 Part G decision 26 stages for this landing, prepared over the
effective proof correction W8-HPC. This module proves the
register's shape and exact membership through the ADR-0059 validation chain,
the record's bindings and carriage, and the exact transformations of
everything this landing changes, each with planted-mutant or negative
controls.

THIS MODULE READS NO CUSTODY. It renders no packet, opens no withheld
authoring record, names no case as a literal and holds no disposition token
as a literal. It reads the published register and record, the supplementary
corpus's committed tree and manifest, and, for identity disjointness only,
the published original manifest.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that any token is right, or any authored intent,
agreement or divergence; that the register transcribes the reviewer's
return, which the reviewer confirms by accepting this record; the absence of
influence, semantic independence or reviewer blinding; that any custody
record exists or is intact; whether any exchange falls within ADR-0047
decision 3 or whether any model was contacted; or that any reproduction,
reveal, comparison or count may now begin.
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

# The published, remotely verified supplementary authoring landing: the
# immutable session-corpus commit that ADR-0059 decision 9 binds.
CORPUS = "83253039ec274a2496b37b618949fd00d3cd7c8e"
# The published, remotely verified W8-HPC correction: this landing's sole
# parent and the commit every pre-image below is read from (W8-HPC
# decision 8).
BASELINE = "9ded8c44abfd4c911d938814a7f551944998ec53"

HOME = supplement.HOME
MANIFEST = supplement.MANIFEST
ORIGINAL_MANIFEST = supplement.ORIGINAL_MANIFEST
REGISTER_HOME = "governance/discriminating-review"
REVEAL_HOME = "governance/discriminating-reveal"
REGISTER = REGISTER_HOME + "/W8-D3-disposition-register.json"
RECORD = "docs/phases/W8-D3-human-disposition-record.md"
COMPLETION_RECORD = "docs/phases/W8-D3-calibration-completion-record.md"
SELF_REL = "tests/test_w8_disposition_record.py"
CALIBRATION = "tests/test_w8_calibration_law.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
ADR59 = "docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md"
FIXED_CENSUS = frozenset({REGISTER, RECORD, SELF_REL, CALIBRATION, RECOVERY,
                          REGISTRY, BOARD})
TOTAL = 12
SESSION_ENTRIES = {"W8-D3-HDR", "W8-D3-DR-01"}

# The session's fixed values, carried by the record (H4).
ACT_DATE = "2026-10-12"
REVIEWER_ROLE = "the human authority, as the sole human reviewer"
PACKET_SHA256 = ("sha256:c8f0b0a8152cca652e450bcdd08354d978596e9a206bfe540c0"
                 "851e16eecfd11")

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    CALIBRATION: ("disposition-law module",
                  "sha256:d9e372ee85b37adc2b70ba8ff3d08de564debaaadf3b9e98f303b9ea69d4dcc8",
                  "0764b9116b282d52460ac1e2aeacb5bb13bbbe58"),
    RECOVERY: ("session-recovery module",
               "sha256:a50c71a2074cf5f31660f1bda5434c6bf592a9ec9a44719ffb47c91fadfdedb9",
               "dd736313ee310e5b28a85a7bcfb5048b23a6fa23"),
    REGISTRY: ("registry",
               "sha256:5b345b709db84806262b4f95430b028544dbbff03192d801e54a85c6e039238a",
               "8ebf8497b4d841d43447b2f8ee1e770855de3c10"),
    BOARD: ("board",
            "sha256:ab43b535f22d24577266a5f65c07a83830e8dd931ea59c54745866abfee354aa",
            "1643762f4f0f4fb8bfff3410b95fd7db213b98b1"),
}
RECORD_SOURCES = {"`tests/test_w8_calibration_law.py`": CALIBRATION,
                  "`tests/test_w8_session_recovery_law.py`": RECOVERY}

# ----------------------------------------------- the three staged successions
R9_EARLIER = "No session, disposition, reveal or calibration exists yet."
R9_SENTENCE = "No reveal, comparison, count or calibration exists yet."

SITES = {
    CALIBRATION: (
        ("K12",
         'COUNT_STATEMENT = "a count of individual human acts and nothing more"\n',
         'COUNT_STATEMENT = "a count of individual human acts and nothing more"\n'
         "# K12 as succeeded at the session landing (ADR-0059 Part G decision\n"
         "# 26): the former absence stays proven at this record's own landing\n"
         "# commit.\n"
         'K12_LANDING = "372287baa4e71bce4353bbdf9ce5e0f2aec93fe1"\n'
         'REGISTER_HOME = "governance/discriminating-review"\n'
         'REVEAL_HOME = "governance/discriminating-reveal"\n'
         'REGISTER_PATH = REGISTER_HOME + "/W8-D3-disposition-register.json"\n'),
        ("K12",
         "    def test_k12_no_packet_register_or_reveal_artefact_exists(self):\n"
         "        tracked = subprocess.run([\"git\", \"ls-files\"], cwd=ROOT,\n"
         "                                 capture_output=True, text=True,\n"
         "                                 check=True).stdout.split()\n"
         "        with self.subTest(fact=\"no register or reveal home is tracked\"):\n"
         "            self.assertEqual(\n"
         "                [p for p in tracked if p.startswith(\n"
         "                    (\"governance/discriminating-review/\",\n"
         "                     \"governance/discriminating-reveal/\"))], [])\n"
         "        homes = {\"docs/decisions/0057-w8-disposition-reveal-calibration-law.md\",\n"
         "                 \"docs/phases/W8-D3-synthetic-calibration-brief.md\",\n"
         "                 \"tests/w8_review_packet.py\", \"tests/test_w8_calibration_law.py\"}\n"
         "        for marker in (packet.PACKET_SCHEMA, REGISTER_SCHEMA):\n"
         "            with self.subTest(fact=\"%s lives only in the law and its code\"\n"
         "                                   % marker):\n"
         "                found = []\n"
         "                for p in tracked:\n"
         "                    try:\n"
         "                        data = (ROOT / p).read_bytes()\n"
         "                    except OSError:\n"
         "                        continue\n"
         "                    if marker.encode(\"utf-8\") in data:\n"
         "                        found.append(p)\n"
         "                self.assertTrue(set(found) <= homes, sorted(found))\n",
         "    def test_k12_no_packet_and_only_the_published_register(self):\n"
         "        # Succeeded at the session landing: the register home admits\n"
         "        # exactly the published register, which alone joins the\n"
         "        # register schema's homes; the reveal home stays empty until its\n"
         "        # own landing.\n"
         "        def listed(*rev):\n"
         "            argv = ([\"ls-tree\", \"-r\", \"--name-only\"] + list(rev)\n"
         "                    if rev else [\"ls-files\"])\n"
         "            return subprocess.run([\"git\"] + argv, cwd=ROOT,\n"
         "                                  capture_output=True, text=True,\n"
         "                                  check=True).stdout.split()\n"
         "\n"
         "        def in_home(paths, home):\n"
         "            return [p for p in paths if p.startswith(home + \"/\")]\n"
         "        tracked = listed()\n"
         "        with self.subTest(fact=\"no register or reveal home was tracked \"\n"
         "                               \"at this record's landing\"):\n"
         "            before = listed(K12_LANDING)\n"
         "            self.assertEqual(in_home(before, REGISTER_HOME)\n"
         "                             + in_home(before, REVEAL_HOME), [])\n"
         "        with self.subTest(fact=\"the register home holds exactly the \"\n"
         "                               \"published register\"):\n"
         "            self.assertEqual(in_home(tracked, REGISTER_HOME),\n"
         "                             [REGISTER_PATH])\n"
         "        with self.subTest(fact=\"no reveal home is tracked\"):\n"
         "            self.assertEqual(in_home(tracked, REVEAL_HOME), [])\n"
         "        homes = {\"docs/decisions/0057-w8-disposition-reveal-calibration-law.md\",\n"
         "                 \"docs/phases/W8-D3-synthetic-calibration-brief.md\",\n"
         "                 \"tests/w8_review_packet.py\", \"tests/test_w8_calibration_law.py\"}\n"
         "        for marker in (packet.PACKET_SCHEMA, REGISTER_SCHEMA):\n"
         "            allowed = homes | ({REGISTER_PATH} if marker == REGISTER_SCHEMA\n"
         "                               else set())\n"
         "            with self.subTest(fact=\"%s lives only in the law, its code \"\n"
         "                                   \"and its admitted instance\" % marker):\n"
         "                found = []\n"
         "                for p in tracked:\n"
         "                    try:\n"
         "                        data = (ROOT / p).read_bytes()\n"
         "                    except OSError:\n"
         "                        continue\n"
         "                    if marker.encode(\"utf-8\") in data:\n"
         "                        found.append(p)\n"
         "                self.assertTrue(set(found) <= allowed, sorted(found))\n"),
    ),
    RECOVERY: (
        ("R7",
         'REVEAL_HOME = "governance/discriminating-reveal"\n',
         'REVEAL_HOME = "governance/discriminating-reveal"\n'
         "# R7 as succeeded at the session landing (ADR-0059 Part G decision 26).\n"
         'SESSION_REGISTER = REGISTER_HOME + "/W8-D3-disposition-register.json"\n'
         'SESSION_RECORD = "docs/phases/W8-D3-human-disposition-record.md"\n'
         'SESSION_ENTRIES = {"W8-D3-HDR", "W8-D3-DR-01"}\n'),
        ("R9",
         'LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")\n',
         'LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")\n'
         "# R9's board sentence as succeeded at the session landing.\n"
         'R9_EARLIER = "' + R9_EARLIER + '"\n'
         'R9_SENTENCE = "' + R9_SENTENCE + '"\n'),
        ("R7",
         "    def test_r7_no_register_or_session_record(self):\n"
         "        tracked = _git(\"ls-files\").split()\n"
         "        with self.subTest(fact=\"no register home, tracked or on disk\"):\n"
         "            self.assertEqual([p for p in tracked\n"
         "                              if p.startswith(REGISTER_HOME + \"/\")], [])\n"
         "            self.assertFalse((ROOT / REGISTER_HOME).exists())\n"
         "        with self.subTest(fact=\"no session record or register file anywhere\"):\n"
         "            self.assertEqual([p for p in tracked if re.search(\n"
         "                r\"disposition-register|human-disposition-record\", p)], [])\n"
         "        entries = load_registry()[\"entries\"]\n"
         "        with self.subTest(fact=\"no registry entry in either home\"):\n"
         "            self.assertEqual([e[\"id\"] for e in entries if e[\"path\"].startswith(\n"
         "                (REGISTER_HOME, REVEAL_HOME))], [])\n"
         "        with self.subTest(fact=\"W8-D3 entries are the brief, the law and this \"\n"
         "                               \"recovery law only\"):\n"
         "            self.assertEqual({e[\"id\"] for e in entries\n"
         "                              if e[\"deliverable\"] == \"W8-D3\"}, D3_ENTRIES)\n",
         "    def test_r7_exactly_the_register_and_session_record(self):\n"
         "        # Succeeded at the session landing: the former absence stays\n"
         "        # proven at this record's own landing commit, and the present\n"
         "        # admits exactly the register, the session record and the two\n"
         "        # W8-D3 registry entries they add.\n"
         "        before = _git(\"ls-tree\", \"-r\", \"--name-only\", LANDING).split()\n"
         "        before_entries = json.loads(packet.committed_object_bytes(\n"
         "            ROOT, LANDING, \"governance/registry.json\"))[\"entries\"]\n"
         "        with self.subTest(fact=\"none of them at this record's landing\"):\n"
         "            self.assertEqual([p for p in before\n"
         "                              if p.startswith(REGISTER_HOME + \"/\")\n"
         "                              or re.search(r\"disposition-register|\"\n"
         "                                           r\"human-disposition-record\", p)],\n"
         "                             [])\n"
         "            self.assertEqual([e[\"id\"] for e in before_entries\n"
         "                              if e[\"path\"].startswith((REGISTER_HOME,\n"
         "                                                       REVEAL_HOME))], [])\n"
         "            self.assertEqual({e[\"id\"] for e in before_entries\n"
         "                              if e[\"deliverable\"] == \"W8-D3\"}, D3_ENTRIES)\n"
         "        tracked = _git(\"ls-files\").split()\n"
         "        with self.subTest(fact=\"the register home holds exactly the \"\n"
         "                               \"register, tracked and on disk\"):\n"
         "            self.assertEqual([p for p in tracked\n"
         "                              if p.startswith(REGISTER_HOME + \"/\")],\n"
         "                             [SESSION_REGISTER])\n"
         "            self.assertEqual(sorted(p.name for p in\n"
         "                                    (ROOT / REGISTER_HOME).iterdir()),\n"
         "                             [SESSION_REGISTER.rsplit(\"/\", 1)[1]])\n"
         "        with self.subTest(fact=\"exactly the register and the session \"\n"
         "                               \"record\"):\n"
         "            self.assertEqual(sorted(p for p in tracked if re.search(\n"
         "                r\"disposition-register|human-disposition-record\", p)),\n"
         "                sorted((SESSION_REGISTER, SESSION_RECORD)))\n"
         "        entries = load_registry()[\"entries\"]\n"
         "        with self.subTest(fact=\"one registry entry in the register home \"\n"
         "                               \"and none in the reveal home\"):\n"
         "            self.assertEqual([e[\"id\"] for e in entries if e[\"path\"].startswith(\n"
         "                (REGISTER_HOME, REVEAL_HOME))], [\"W8-D3-DR-01\"])\n"
         "        with self.subTest(fact=\"W8-D3 entries are the brief, the two laws \"\n"
         "                               \"and the two session entries only\"):\n"
         "            self.assertEqual({e[\"id\"] for e in entries\n"
         "                              if e[\"deliverable\"] == \"W8-D3\"},\n"
         "                             D3_ENTRIES | SESSION_ENTRIES)\n"),
        ("R9",
         "        with self.subTest(fact=\"the board still states no session exists\"):\n"
         "            self.assertIn(\"No session, disposition, reveal or calibration \"\n"
         "                          \"exists yet.\", _lf_text(BOARD))\n",
         "        # Succeeded at the session landing: the earlier sentence stays\n"
         "        # proven at the derived baseline, and the board now carries the\n"
         "        # session landing's exact wording.\n"
         "        with self.subTest(fact=\"the board stated no session existed at \"\n"
         "                               \"the derived baseline\"):\n"
         "            self.assertIn(R9_EARLIER, packet.committed_object_bytes(\n"
         "                ROOT, LANDING, \"docs/phases/README.md\").decode(\"utf-8\"))\n"
         "        with self.subTest(fact=\"the board now states no reveal exists, \"\n"
         "                               \"in the session landing's wording\"):\n"
         "            board = _lf_text(BOARD)\n"
         "            self.assertIn(R9_SENTENCE, board)\n"
         "            self.assertNotIn(R9_EARLIER, board)\n"),
    ),
}

# --------------------------------------- board and registry: authorised edits
HDR_LINK = ("([`W8-D3-human-disposition-record.md`]"
            "(W8-D3-human-disposition-record.md))")
HDR_STATUS_TAIL = (
    "the human authority's twelve individual dispositions on the session "
    "corpus, one lawful token per case, in governed register `W8-D3-DR-01`, "
    "with the packet hash, the corpus binding and the reviewer's own "
    "procedural account; nothing withheld was read, the dispositions are "
    "fixed on publication, and D3-D stays unopened until this record is "
    "published and independently remote-verified.")
HDR_STATUS = {
    "draft": ("**A draft human disposition record, `W8-D3-HDR`, is before the "
              "human reviewer** " + HDR_LINK + ": if accepted, it would "
              "record " + HDR_STATUS_TAIL),
    "accepted": ("**The human disposition record, `W8-D3-HDR`, is "
                 "accepted** " + HDR_LINK + " — accepted %s: it records "
                 + HDR_STATUS_TAIL),
}
HDR_ROW = ("| W8-D3 — Human Disposition Record (W8-D3-HDR) | "
           "[`W8-D3-human-disposition-record.md`]"
           "(W8-D3-human-disposition-record.md) | ")
HDR_ROW_BODY = (
    "Tier J: **the D3-C session record** — the human authority's twelve "
    "individual dispositions on the supplementary session corpus, one lawful "
    "token per case, returned complete from the session packet rendered by "
    "the published renderer from committed Git objects and transcribed "
    "exactly into governed register `W8-D3-DR-01`, whose acceptance this "
    "record carries; it binds the act's date, the reviewer role, the packet "
    "hash, the register and the session corpus, states that every token is "
    "an individual human act, and carries the reviewer's procedural "
    "account verbatim, the initial attestation and its dated continuation, "
    "with publication conditional on that account remaining complete and "
    "accurate and no test claimed to prove the absence of influence. "
    "Custody checked for existence only. **No withheld byte read; "
    "no reproduction, reveal, comparison or count; D3-D stays unopened until "
    "this record is published and remotely verified.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
HPC_STATUS_CLOSE = ("the rebuilt D3-C session landing waits for it to be "
                    "effective. ")
BOARD_STATUS_ANCHOR = HPC_STATUS_CLOSE + "**" + R9_EARLIER
BOARD_ROW_ANCHOR = ("the rebuilt D3-C session landing waits for this "
                    "correction to be effective.** |\n")
HDR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
HDR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRIES = (
    {"id": "W8-D3-HDR", "path": RECORD, "type": "phase-record",
     "title": "W8-D3 - Human Disposition Record",
     "role": (
         "The W8-D3 session record of landing D3-C on the session corpus "
         "that ADR-0059 binds: the human authority's twelve individual "
         "dispositions, one lawful token per case, returned complete from "
         "the session packet rendered by the published renderer from "
         "committed Git objects, and bound exactly into the disposition "
         "register whose acceptance this record carries as governed register "
         "W8-D3-DR-01. Carries the act's date, the reviewer role, the packet "
         "SHA-256, the register binding, the session-corpus binding "
         "(authoring-landing commit, supplement home tree and manifest "
         "SHA-256), the statement that every token is an individual human "
         "act, and the reviewer's procedural account under ADR-0059 "
         "verbatim, the initial attestation and its dated continuation, with "
         "the human authority's determination on the initial account and "
         "publication conditional on the account remaining complete and "
         "accurate; no test "
         "proves the absence of influence, and none is claimed. Records the "
         "existence-only custody check, and moves exactly the disposition-law "
         "K12 register limb and ADR-0058's R7 and R9 by exact transformation, "
         "with proof obligations H1 to H12, prepared over the effective "
         "proof correction W8-HPC. No withheld byte read; no "
         "reproduction, reveal, comparison or count; D3-D stays unopened."),
     "depends_on": ["ADR-0057", "ADR-0059", "W8-D3-SCB", "W8-S1-SOB",
                    "W8-S1-SCR", "W8-S1-CM-01", "W8-HPC", "ADR-0058",
                    "ADR-0054",
                    "ADR-0055", "W8-D2-CBC", "ADR-0056", "W8-AR", "W7-CR"]},
    {"id": "W8-D3-DR-01", "path": REGISTER, "type": "governed-register",
     "title": "W8-D3 - Disposition Register",
     "role": (
         "The disposition register of W8-D3 landing D3-C: one closed "
         "canonical-bytes object under ADR-0057 decision 9, one row per case "
         "of the session corpus that ADR-0059 binds, sorted by case identity, "
         "each row exactly the case identity and the human reviewer's "
         "returned token; it carries no authored class, intended disposition, "
         "construction map, rationale, confidence, timestamp or other "
         "withheld authoring metadata, and binds this corpus only. Its "
         "acceptance is carried by the record W8-D3-HDR; after publication "
         "every disposition is fixed."),
     "depends_on": ["W8-D3-HDR", "ADR-0057", "ADR-0059", "W8-S1-CM-01",
                    "ADR-0054"]},
)

# -------------------------------------------- the record's fixed carriage
BINDING_KEYS = ("Act date", "Reviewer role", "Packet SHA-256", "Register",
                "Register LF SHA-256", "Session-corpus commit",
                "Supplement home tree at that commit", "Manifest LF SHA-256")
BINDING_ROW = re.compile(r"^\| (?P<key>[A-Za-z][A-Za-z0-9 -]*?) \| "
                         r"(?P<value>[^|]+?) \|$", re.MULTILINE)
# The attestation is exactly the reviewer's four quoted statements, as
# supplied, together and nothing else.
QUOTATIONS = (
    "“The cases were not reviewed in isolation from each other. They arrived "
    "in sequence in one conversation, with my earlier dispositions and "
    "reasoning visible to me throughout.”",
    "“My doctrine review preceded the cases. It included my own views on "
    "where the law pulls toward particular tokens, which I carried into the "
    "reading.”",
    "“individually verified.”",
    "“No, it was mine.”",
)
ATTESTATION = ">\n".join("> %s\n" % q for q in QUOTATIONS)
# The framing assembled with the architect's help, which introduced the
# third and fourth statements: carried only as separately attributed
# context, outside every quotation block, with roles in place of names.
FRAMING = (
    "To clarify how I assessed the cases, my words were:",
    "When the architect asked whether anyone had supplied case-level "
    "judgements, preferred answers, rationales or withheld authoring "
    "information, covering my first access to the supplementary material "
    "including the L2 review, I answered:",
)
CONTEXT_ITEM = "11. **Procedural context, separately attributed.**"
# The reviewer's dated continuation of the account, verbatim (three
# paragraphs, one block of its own), and the architect's drafting help
# with it, carried only in the separately attributed context.
CONTINUATION_DATE = "2026-10-13"
CONTINUATION_LABEL = ("8. **The reviewer's continuation of the procedural "
                      "account, given on %s, verbatim:**"
                      % CONTINUATION_DATE)
CONTINUATION_PARAGRAPHS = (
    "Since my account of 2026-10-12, I have received further mechanical "
    "review, clarification of the governing requirements, and drafting "
    "assistance from the architect and implementer concerning the "
    "candidate, the A3 correction and the rebuild. This has included their "
    "reports and reviews, and draft diffs containing my own submitted "
    "register rows.",
    "During this period, I have received no case-level judgements, "
    "preferred or predicted dispositions, case-level rationales, withheld "
    "authoring information or aggregate feedback about the cases from "
    "anyone else. Nothing has occurred that requires a correction to my "
    "earlier account.",
    "My earlier account, together with this continuation, is complete and "
    "accurate as at the date above. I will report any further relevant "
    "event before publication, and publication must pause if that event "
    "requires an updated account or review.",
)
CONTINUATION = ">\n".join("> %s\n" % p for p in CONTINUATION_PARAGRAPHS)
CONTINUATION_ASSISTANCE = ("The architect also helped the reviewer put the "
                           "continuation in item 8 into words.")
CLARIFICATION = (
    "> My statement about the cases not being reviewed in isolation "
    "described their sequential presentation in one conversation, with "
    "earlier responses visible. Please read it together with my "
    "clarification, “individually verified”, and my statement that the "
    "judgements were mine.\n")
DETERMINATION = (
    "> I have considered the architect’s review and determine that my "
    "reported process fits the governing provisions.\n")
REQUIRED_HDR = (
    "Every token in the register is an individual human act.",
    "The implementer transcribed the returned tokens exactly, and inferred, "
    "defaulted, filled, bulk-selected, recommended or substituted none.",
    "It is a human statement. No test proves the absence of influence, "
    "semantic independence or reviewer blinding, and none is claimed.",
    "is the reviewer's four quoted statements, reproduced verbatim and "
    "together, and nothing else.",
    "The initial attestation and its continuation together are the "
    "reviewer's procedural account under ADR-0059 decision 15, which the "
    "reviewer states is complete and accurate as at 2026-10-13.",
    "Publication of this record is conditional on that account remaining "
    "complete and accurate through publication: any further relevant event "
    "is reported before publication, and an event that requires an updated "
    "account or review pauses publication.",
    "This condition is a continuing process duty, not a machine proof and "
    "not an advance assertion about future events.",
    "it is not part of the attestation.",
    "the separately governed `W8-HPC` corrected A3, and this landing was "
    "rebuilt over it.",
    "the implementer made no determination.",
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
    "D3-D stays unopened until this record is published and independently "
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


def committed(commit, rel):
    return packet.committed_object_bytes(ROOT, commit, rel)


def worktree(rel):
    return _lf((ROOT / rel).read_bytes())


def l3_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added the register, whose sole
    parent must be BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                REGISTER).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the register was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return worktree(rel) if commit is None else _lf(committed(commit, rel))


def manifest_ids():
    return [r["case_id"]
            for r in json.loads(committed(CORPUS, MANIFEST))["rows"]]


def original_ids():
    return [r["case_id"]
            for r in json.loads(committed(CORPUS, ORIGINAL_MANIFEST))["rows"]]


def bound_case_paths(commit):
    """The case files in the supplement home's committed tree: the
    renderer's inputs, observed independently of the manifest."""
    return [p for p in _git("ls-tree", "--name-only", commit,
                            HOME + "/").split()
            if p != MANIFEST]


def register_violations(raw, ids):
    """The register's exact bytes: one closed canonical object under the
    law, LF only with exactly one terminal LF, twelve rows one-to-one with
    the session corpus."""
    v = []
    if b"\r" in raw or not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        v.append("the register is not LF with exactly one terminal LF")
    try:
        obj = json.loads(raw)
    except ValueError:
        return v + ["the register is not JSON"]
    if envelope.canonical_bytes(obj) != raw:
        v.append("the register is not in canonical bytes")
    v += calibration.register_violations(obj, ids)
    if isinstance(obj, dict) and isinstance(obj.get("rows"), list) \
            and len(obj["rows"]) != TOTAL:
        v.append("the register does not hold exactly twelve rows")
    return v


def register_ids(raw):
    return [r["case_id"] for r in json.loads(raw)["rows"]]


def record_bindings(text):
    """The record's binding table as a dict, or None if a key repeats or a
    required key is missing."""
    out = {}
    for m in BINDING_ROW.finditer(text):
        key = m.group("key")
        if key not in BINDING_KEYS:
            continue
        if key in out:
            return None
        out[key] = m.group("value").strip().strip("`")
    return out if set(out) == set(BINDING_KEYS) else None


def observed_binding():
    commit, _ = supplement.l2_snapshot()
    return {"commit": commit,
            "home_tree": _git("rev-parse", "%s:%s" % (commit, HOME)).strip(),
            "manifest_sha256": _sha(_lf(committed(commit, MANIFEST)))}


def recorded_binding(bindings):
    b = bindings or {}
    return {"commit": b.get("Session-corpus commit"),
            "home_tree": b.get("Supplement home tree at that commit"),
            "manifest_sha256": b.get("Manifest LF SHA-256")}


def chain_input(record_text, register_raw):
    return {"recorded_binding": recorded_binding(record_bindings(record_text)),
            "observed_binding": observed_binding(),
            "manifest_ids": manifest_ids(), "original_ids": original_ids(),
            "packet_paths": bound_case_paths(CORPUS),
            "register_ids": register_ids(register_raw)}


def expected_bindings(register_raw):
    o = observed_binding()
    return {"Act date": ACT_DATE, "Reviewer role": REVIEWER_ROLE,
            "Packet SHA-256": PACKET_SHA256, "Register": REGISTER,
            "Register LF SHA-256": _sha(register_raw),
            "Session-corpus commit": o["commit"],
            "Supplement home tree at that commit": o["home_tree"],
            "Manifest LF SHA-256": o["manifest_sha256"]}


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


def attestation_violations(text):
    """The attribution boundary: the four quoted statements alone, verbatim
    and together, in one block of their own; the clarification and the
    determination each verbatim in a block of their own; the dated
    continuation verbatim in a block of its own under its dated label; and
    the assisted framing and the continuation's drafting assistance each
    only once, outside every block, inside the separately attributed
    context item."""
    v = []
    blocks = quotation_blocks(text)
    holding = [b for b in blocks if any(q in b for q in QUOTATIONS)]
    if holding != [ATTESTATION]:
        v.append("the four quoted statements are not exactly one block of "
                 "their own, verbatim and together")
    for name, block in (("clarification", CLARIFICATION),
                        ("determination", DETERMINATION)):
        if blocks.count(block) != 1:
            v.append("the %s is not exactly one verbatim block of its own"
                     % name)
    if blocks.count(CONTINUATION) != 1:
        v.append("the continuation is not exactly one verbatim block of "
                 "its own")
    if text.count(CONTINUATION_LABEL) != 1 or (
            CONTINUATION in text and text.index(CONTINUATION_LABEL)
            > text.index(CONTINUATION)):
        v.append("the continuation is not under its dated label")
    context = [l for l in text.split("\n") if l.startswith(CONTEXT_ITEM)]
    for f in FRAMING + (CONTINUATION_ASSISTANCE,):
        if text.count(f) != 1:
            v.append("assisted framing occurs %d times" % text.count(f))
        if any(f in b for b in blocks):
            v.append("assisted framing sits inside a quotation block")
        if len(context) != 1 or f not in context[0]:
            v.append("assisted framing is not in the separately attributed "
                     "context")
    return v


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


def hdr_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and HDR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (HDR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         HPC_STATUS_CLOSE + fill(HDR_STATUS[state]) + " **" + R9_SENTENCE),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + HDR_ROW + fill(ROW_PREFIX[state]) + HDR_ROW_BODY
         + " |\n"),
    )


def new_entry(spec, state, date, content_hash):
    return {
        "id": spec["id"], "aliases": [], "title": spec["title"],
        "type": spec["type"], "phase": "W8", "deliverable": "W8-D3",
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
            + ",\n".join(authority._indent(json.dumps(e, indent=2,
                                                      ensure_ascii=False), 4)
                         for e in added)
            + "\n  ]\n}\n")


def added_board_wording():
    return " ".join([HDR_ROW, HDR_ROW_BODY, R9_SENTENCE]
                    + list(HDR_STATUS.values()))


def exposure_violations(text, pins=()):
    """No case identity, no digest-shaped string apart from the exact pins,
    no disposition token, no reserved authoring label, no schema literal and
    no count statement."""
    v = recovery.exposure_violations(text, pins)
    v += ["a reserved label: %s" % s
          for s in corpus.reserved_channel_hits(text)]
    v += ["a schema literal is present" for s in
          (packet.PACKET_SCHEMA, calibration.REGISTER_SCHEMA,
           envelope.AUTHORING_SCHEMA) if s in text]
    if calibration.COUNT_STATEMENT in text:
        v.append("a count statement is present")
    return v


def load_registry(commit):
    return json.loads(snapshot_bytes(commit, REGISTRY))


# ------------------------------------------------------------------ proofs
class H1_RegisterShape(unittest.TestCase):
    def test_h1_register_is_closed_canonical_and_complete(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        raw = snapshot_bytes(commit, REGISTER)
        ids = manifest_ids()
        self.assertEqual(register_violations(raw, ids), [])
        obj = json.loads(raw)
        good = envelope.canonical_bytes(obj)
        mutants = {
            "pretty-printed bytes": (json.dumps(obj, indent=2) + "\n")
            .encode("utf-8"),
            "a carriage return": good.replace(b"\n", b"\r\n"),
            "a second terminal LF": good + b"\n",
            "an unlawful token": envelope.canonical_bytes(
                dict(obj, rows=[dict(obj["rows"][0], disposition="pass")]
                     + obj["rows"][1:])),
            "a withheld field on a row": envelope.canonical_bytes(
                dict(obj, rows=[dict(obj["rows"][0], authored_class="A")]
                     + obj["rows"][1:])),
            "a missing row": envelope.canonical_bytes(
                dict(obj, rows=obj["rows"][1:])),
            "an extra outer field": envelope.canonical_bytes(
                dict(obj, note="x")),
            "a wrong schema": envelope.canonical_bytes(
                dict(obj, schema=obj["schema"] + "x")),
        }
        for name, mutated in mutants.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(register_violations(mutated, ids))


class H2_ValidationChain(unittest.TestCase):
    def test_h2_membership_through_the_register(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        record = snapshot_bytes(commit, RECORD).decode("utf-8")
        raw = snapshot_bytes(commit, REGISTER)
        c = chain_input(record, raw)
        with self.subTest(fact="the chain holds through the register, in "
                               "order"):
            self.assertEqual(authority.session_chain_violations(
                c, upto="register"), [])
        with self.subTest(fact="the bound commit is the corpus commit, "
                               "never the session baseline"):
            self.assertEqual(c["observed_binding"]["commit"], CORPUS)
            self.assertNotEqual(CORPUS, BASELINE)
        ids, orig = c["manifest_ids"], c["original_ids"]
        planted = {
            "an original-corpus row": dict(
                c, register_ids=c["register_ids"][1:] + orig[:1]),
            "a missing row": dict(c, register_ids=c["register_ids"][1:]),
            "a duplicate row": dict(
                c, register_ids=c["register_ids"][:-1]
                + c["register_ids"][:1]),
            "a wrong recorded commit": dict(c, recorded_binding=dict(
                c["recorded_binding"], commit=supplement.L1)),
            "a missing recorded value": dict(c, recorded_binding=dict(
                c["recorded_binding"], home_tree=None)),
            "the manifest among the packet inputs": dict(
                c, packet_paths=c["packet_paths"] + [MANIFEST]),
            "an original case among the packet inputs": dict(
                c, packet_paths=c["packet_paths"][1:]
                + [ORIGINAL_MANIFEST.rsplit("/", 1)[0] + "/%s.json"
                   % orig[0]]),
        }
        for name, mutated in planted.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(authority.session_chain_violations(
                    mutated, upto="register"))
        with self.subTest(fact="the register's identities are the bound "
                               "manifest's, in ascending order"):
            self.assertEqual(c["register_ids"], sorted(ids))


class H3_CommittedObjectReading(unittest.TestCase):
    def test_h3_working_copy_equals_committed_bytes(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        for rel in (REGISTER, RECORD):
            with self.subTest(path=rel):
                self.assertEqual(worktree(rel), snapshot_bytes(commit, rel))
        with self.subTest(control="a one-byte working-copy change is "
                                  "detected"):
            raw = snapshot_bytes(commit, REGISTER)
            self.assertNotEqual(raw.replace(b"[", b"[ ", 1), raw)


class H4_RecordBindings(unittest.TestCase):
    def test_h4_record_binds_exactly(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        record = snapshot_bytes(commit, RECORD).decode("utf-8")
        raw = snapshot_bytes(commit, REGISTER)
        expected = expected_bindings(raw)
        self.assertEqual(record_bindings(record), expected)
        with self.subTest(fact="the corpus binding is the published one"):
            self.assertEqual(authority.binding_violations(
                recorded_binding(record_bindings(record)),
                observed_binding()), [])
        for key in BINDING_KEYS:
            with self.subTest(control="an altered %s is detected" % key):
                row = "| %s | " % key
                start = record.index(row) + len(row)
                altered = record[:start] + "x" + record[start:]
                self.assertNotEqual(record_bindings(altered), expected)
        with self.subTest(control="a repeated row is refused"):
            row = next(l for l in record.split("\n")
                       if l.startswith("| Act date |"))
            self.assertIsNone(record_bindings(record + "\n" + row + "\n"))


class H5_RecordCarriage(unittest.TestCase):
    def test_h5_record_carries_its_statements(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        flat = _flat(snapshot_bytes(commit, RECORD).decode("utf-8"))
        for s in REQUIRED_HDR:
            with self.subTest(carried=s[:44]):
                self.assertEqual(flat.count(s), 1)
        with self.subTest(control="a removed statement is detected"):
            self.assertNotIn(REQUIRED_HDR[0],
                             flat.replace(REQUIRED_HDR[0], ""))
        with self.subTest(carried="nine-rule block byte-identical"):
            nine = re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                             r"failure\.\*\*)", _lf(committed(
                                 BASELINE, "docs/decisions/0054-generative-"
                                 "evaluation-maturity-doctrine.md"))
                             .decode("utf-8")).group(1)
            self.assertIn(nine, flat)


class H6_Attestation(unittest.TestCase):
    def test_h6_attestation_verbatim_and_together(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        text = snapshot_bytes(commit, RECORD).decode("utf-8")
        self.assertEqual(attestation_violations(text), [])
        with self.subTest(fact="the attestation block is exactly the four "
                               "quoted statements"):
            self.assertEqual(ATTESTATION.count("> “"), 4)
            self.assertEqual(len(QUOTATIONS), 4)
        first, second = ATTESTATION.split("\n>\n", 1)
        framed = ATTESTATION.replace(
            "> " + QUOTATIONS[2], "> " + FRAMING[0] + " " + QUOTATIONS[2])
        mutants = {
            "a one-character change to a quotation": text.replace(
                QUOTATIONS[2], QUOTATIONS[2].replace(".", ""), 1),
            "reordered statements": text.replace(
                ATTESTATION, second.rstrip("\n") + "\n>\n" + first + "\n"),
            "inserted material between statements": text.replace(
                ATTESTATION, ATTESTATION.replace(
                    "\n>\n", "\n>\n> (summary)\n>\n", 1)),
            "assisted framing moved back inside the attestation": text
            .replace(FRAMING[0], "the assembled framing", 1)
            .replace(ATTESTATION, framed),
            "assisted framing removed from the context": text.replace(
                FRAMING[1], "the architect's question", 1),
            "the clarification merged into the attestation block": text
            .replace(CLARIFICATION, "", 1)
            .replace(ATTESTATION, ATTESTATION + ">\n" + CLARIFICATION, 1),
            "an omitted continuation": text.replace(CONTINUATION, "", 1),
            "an altered continuation": text.replace(
                "as at the date above", "as at today", 1),
            "the continuation merged into the initial attestation": text
            .replace(CONTINUATION, "", 1)
            .replace(ATTESTATION, ATTESTATION + ">\n" + CONTINUATION, 1),
            "the clarification merged into the continuation": text
            .replace(CLARIFICATION, "", 1)
            .replace(CONTINUATION, CONTINUATION + ">\n" + CLARIFICATION, 1),
            "the continuation's drafting assistance moved into its block":
            text.replace(" " + CONTINUATION_ASSISTANCE, "", 1).replace(
                CONTINUATION, CONTINUATION + ">\n> "
                + CONTINUATION_ASSISTANCE + "\n", 1),
            "the continuation's dated label removed": text.replace(
                CONTINUATION_LABEL, "8. **The reviewer's continuation, "
                "verbatim:**", 1),
            "a dropped clarification": text.replace(CLARIFICATION, ""),
            "a reworded determination": text.replace(
                DETERMINATION, DETERMINATION.replace("fits", "meets")),
        }
        for name, mutated in mutants.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(attestation_violations(mutated))


class H7_NoExposure(unittest.TestCase):
    def test_h7_no_case_token_label_schema_or_count_exposed(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        record = snapshot_bytes(commit, RECORD).decode("utf-8")
        raw = snapshot_bytes(commit, REGISTER)
        by_id = {e["id"]: e for e in load_registry(commit)["entries"]}
        pins = [PACKET_SHA256, _sha(raw),
                observed_binding()["manifest_sha256"]]
        pins += [p for _, p, _ in PREIMAGE.values()]
        pins += [m.group("post") for m in
                 supplement.SUCCESSION_ROW.finditer(record)]
        pins = [p.split(":", 1)[1] for p in pins]
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
                self.assertEqual(exposure_violations(text, excused), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([t for t in packet.TOKENS if t in src], [])
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([s for s in (packet.PACKET_SCHEMA,
                                          calibration.REGISTER_SCHEMA,
                                          envelope.AUTHORING_SCHEMA)
                              if s in src], [])
        planted = {
            "a case identity": manifest_ids()[0],
            "a disposition token": sorted(packet.TOKENS)[0],
            "a bare digest": "e" * 64,
            "a reserved label": sorted(envelope.ALL_CHECKS)[0],
            "the register schema": calibration.REGISTER_SCHEMA,
            "a count statement": calibration.COUNT_STATEMENT,
        }
        for name, plant in planted.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(record + "\n" + plant,
                                                    pins))


class H8_Successions(unittest.TestCase):
    def test_h8_staged_successions_are_exact(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        record = snapshot_bytes(commit, RECORD).decode("utf-8")
        for rel in (CALIBRATION, RECOVERY):
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(),
                                 PREIMAGE[rel][2])
            with self.subTest(exact_succession=PREIMAGE[rel][0]):
                self.assertEqual(succession_violations(
                    rel, snapshot_bytes(commit, rel).decode("utf-8"),
                    record), [])
        with self.subTest(fact="ADR-0059 Part G decision 26 stages exactly "
                               "these"):
            a59 = _flat(_lf(committed(BASELINE, ADR59)).decode("utf-8"))
            for clause in (
                    "the disposition-law module's K12 register limb and "
                    "register-schema homes admit exactly the published "
                    "register",
                    "ADR-0058's R7 admits exactly the register, the session "
                    "record and the W8-D3 registry entries they add",
                    "ADR-0058's R9 board sentence succeeds to that landing's "
                    "exact wording, its earlier form staying proven at the "
                    "derived baseline"):
                self.assertIn(clause, a59)
        with self.subTest(fact="the succeeded modules carry this landing's "
                               "constants"):
            self.assertEqual(calibration.REGISTER_PATH, REGISTER)
            self.assertEqual(recovery.SESSION_REGISTER, REGISTER)
            self.assertEqual(recovery.SESSION_RECORD, RECORD)
            self.assertEqual(recovery.SESSION_ENTRIES, SESSION_ENTRIES)
            self.assertEqual(recovery.R9_SENTENCE, R9_SENTENCE)
        present = snapshot_bytes(commit, RECOVERY).decode("utf-8")
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


class H9_AbsenceAndFutureRefusal(unittest.TestCase):
    def test_h9_nothing_before_and_nothing_later(self):
        before = _git("ls-tree", "-r", "--name-only", BASELINE).split()
        base_entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
        base_board = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        with self.subTest(fact="at the baseline: no register, record or "
                               "reveal home"):
            self.assertEqual([p for p in before if p.startswith(
                (REGISTER_HOME + "/", REVEAL_HOME + "/")) or p == RECORD],
                [])
            self.assertEqual([e["id"] for e in base_entries
                              if e["id"] in SESSION_ENTRIES], [])
        with self.subTest(fact="at the baseline: the board's earlier "
                               "sentence only"):
            self.assertIn(R9_EARLIER, base_board)
            self.assertNotIn(R9_SENTENCE, base_board)
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        tracked = (_git("ls-tree", "-r", "--name-only", commit).split()
                   if commit else _git("ls-files").split())
        entries = load_registry(commit)["entries"]
        with self.subTest(fact="no reveal home, tracked or on disk"):
            self.assertEqual([p for p in tracked
                              if p.startswith(REVEAL_HOME + "/")], [])
            if commit is None:
                self.assertFalse((ROOT / REVEAL_HOME).exists())
        with self.subTest(fact="no completion record and no later entry"):
            self.assertNotIn(COMPLETION_RECORD, tracked)
            if commit is None:
                self.assertFalse((ROOT / COMPLETION_RECORD).exists())
            self.assertEqual({e["id"] for e in entries
                              if e["deliverable"] == "W8-D3"},
                             recovery.D3_ENTRIES | SESSION_ENTRIES)
            self.assertEqual([e["id"] for e in entries
                              if e["deliverable"] in recovery.LATER], [])
        with self.subTest(control="a planted completion entry is refused"):
            planted = entries + [dict(entries[-1], id="W8-D3-CCR",
                                      deliverable="W8-D3")]
            self.assertNotEqual({e["id"] for e in planted
                                 if e["deliverable"] == "W8-D3"},
                                recovery.D3_ENTRIES | SESSION_ENTRIES)


class H10_Registration(unittest.TestCase):
    def test_h10_record_and_register_are_bound(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        by_id = {e["id"]: e for e in load_registry(commit)["entries"]}
        state, date, v = hdr_state(snapshot_bytes(commit, RECORD)
                                   .decode("utf-8"))
        self.assertEqual(v, [])
        for spec in NEW_ENTRIES:
            e = by_id.get(spec["id"])
            with self.subTest(entry=spec["id"]):
                self.assertIsNotNone(e)
                self.assertEqual((e["path"], e["type"], e["phase"],
                                  e["deliverable"]),
                                 (spec["path"], spec["type"], "W8", "W8-D3"))
                self.assertEqual(e["content_hash"],
                                 _sha(snapshot_bytes(commit, e["path"])))
                if commit is None:
                    self.assertEqual(e["content_hash"],
                                     lf_hash(ROOT / e["path"]))
                self.assertEqual((e["status"], e["accepted_date"]),
                                 (state, date))
                self.assertTrue({"ADR-0057", "ADR-0059", "ADR-0054"}
                                <= set(e["depends_on"]))
        with self.subTest(fact="the register's acceptance is carried by the "
                               "record"):
            self.assertIn("W8-D3-HDR", by_id["W8-D3-DR-01"]["depends_on"])
        with self.subTest(control="a register status apart from the record "
                                  "is refused"):
            e = by_id["W8-D3-DR-01"]
            flipped = ("accepted", "2000-01-01") if state == "draft" \
                else ("draft", None)
            self.assertNotEqual((e["status"], e["accepted_date"]), flipped)


class H11_RegistryAndBoard(unittest.TestCase):
    def test_h11_registry_and_board_change_exactly(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        state, date, v = hdr_state(snapshot_bytes(commit, RECORD)
                                   .decode("utf-8"))
        self.assertEqual(v, [])
        board_pre = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(BASELINE, REGISTRY)).decode("utf-8")
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = snapshot_bytes(commit, BOARD).decode("utf-8")
        expected, problems = authority.apply_sites(board_pre,
                                                   board_sites(state, date))
        with self.subTest(fact="exact authorised board", state=state):
            self.assertEqual(problems, [])
            self.assertEqual(board, expected)
            self.assertEqual(recovery.board_surfaces(board)[2], [])
            self.assertIn(supplement.COUNT_SENTENCE, board)
        hashes = {rel: _sha(snapshot_bytes(commit, rel))
                  for rel in (RECORD, REGISTER)}
        reg = snapshot_bytes(commit, REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, hashes, state,
                                                    date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, hashes, other, "2000-01-01"))
            wrong, _ = authority.apply_sites(board_pre,
                                             board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)
        with self.subTest(fact="the W8-HPC entry and board row are "
                               "preserved"):
            hpc = {e["id"]: e for e in json.loads(reg)["entries"]}["W8-HPC"]
            self.assertEqual((hpc["status"], hpc["accepted_date"]),
                             ("accepted", "2026-10-13"))
            self.assertEqual(board.count("| W8 — Historical-Pin Proof "
                                         "Correction (W8-HPC) |"), 1)
        with self.subTest(control="an unauthorised registry edit is "
                                  "refused"):
            self.assertNotEqual(reg.replace('"W8-D3-HDR"', '"W8-D3-HDRx"'),
                                expected_registry(reg_pre, hashes, state,
                                                  date))


class H12_Census(unittest.TestCase):
    def test_h12_census_is_exactly_seven_paths(self):
        commit, problems = l3_snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly seven paths"):
            self.assertEqual(len(FIXED_CENSUS), 7)
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {CALIBRATION, RECOVERY, SELF_REL})
        with self.subTest(fact="neither corpus home is touched"):
            self.assertEqual([p for p in paths if p.startswith(
                (HOME + "/", supplement.ORIGINAL_HOME + "/"))], [])
        record = _flat(snapshot_bytes(commit, RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly seven "
                          r"paths:\*\* (.*?) ## ", record)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
