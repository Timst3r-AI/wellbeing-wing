"""W8 — documentation erratum proofs (W8-DER, DE1–DE6).

A phase-level erratum under the phase entry checklist's rules 2, 4 and 10:
six W8 statements in the root README and the tests README's dependency
statement and family note are corrected to what the published record
states, deciding no question the record reserves. This module proves the
two files are exact pinned transformations of their baseline pre-images,
that every corrected statement's source mapping holds mechanically at the
baseline, that the tests README's pins equal the approved manifest and its
named families exist, that the README's W8 statements agree with the
registry, that no case-level material or figure enters the corrected files
or this record, that the registry and board change exactly, and the census
- each with planted-mutant or negative controls.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the erratum
record afterwards - and executes the helpers it relies on from that
snapshot's bytes in a private namespace. This module imports no other proof
module and holds no live gate. The residual live reach is disclosed exactly:
each snapshot-executed helper module imports, at its own top level, the
live modules it aliases for the fixed-law values it reads from them, and no
more independence than that is claimed.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity,
disposition token, schema literal or method label as a literal.

WHAT GREEN DOES NOT MEAN. A green run proves that the corrected bytes are
the pinned ones, that nothing else changed, and that each row of the
record's source mapping holds in the mechanical sense DE2 defines: a
cited fragment is present verbatim in its tracked source at the baseline,
a cited identity is accepted at that path, a file row's path has no
registry entry, a registry or tree fact holds, and the table read whole is
exactly the trusted rows. DE2 proves presence
and structure, NEVER entailment: it does not establish that any fragment
supports the whole of the statement beside it. Matching a source's scope
to a statement's scope is the reviewer's reading, which the record lays
out row by row for review. A green run NEVER establishes anything about
any case, disposition, divergence, reviewer or model, never classifies any
exchange or states whether model contact occurred, and never shows that
any later deliverable may open.
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

# The published, remotely verified W8-D4 completion: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "ce78a242df25898d90debee9513bdce7e511471b"

README = "README.md"
TESTS_README = "tests/README.md"
RECORD = "docs/phases/W8-documentation-erratum.md"
SELF_REL = "tests/test_w8_documentation_erratum.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
MANIFEST = "requirements.txt"
CHECKLIST = "docs/governance/checklist.md"
TREE = "tests/"
FIXED_CENSUS = frozenset({README, TESTS_README, RECORD, SELF_REL, REGISTRY,
                          BOARD})
D4_DELIVERABLES = ("W8-D1", "W8-D2", "W8-D3", "W8-D4")
LATER_DELIVERABLES = ("W8-D5", "W8-D6", "W8-D7")
COMPLETION_IDS = ("W8-D3-CCR", "W8-D4-CPR")
FAMILIES = ("test_w4_", "test_w6_", "test_w7_", "test_w8_", "test_engine_",
            "test_runtime_", "test_evaluation_")
DISCLAIMERS = (
    "Not a medical device. Not a treatment platform. Not an AI therapist.",
    "No medical, therapeutic, diagnostic, safety-intervention, crisis-response, "
    "clinical-validity or production-readiness claim is made.",
    "Where this README and a governing record disagree, the governing record "
    "wins.",
)
# The README's licence name carries a version that the decimal form would
# otherwise read as a figure; it is a name, set aside before the figure scan
# only where it occurs whole between token boundaries, exactly as the
# manifest's own pins are, read from requirements.txt at the baseline (see
# pin_free()). Nothing else is set aside: a longer string that merely begins
# with the name, or a pin at another version, stays in the scanned text.
LICENCE_NAME = "Apache License 2.0"
PIN_EDGE = r"[A-Za-z0-9_.-]"

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": "tests/test_w8_session_recovery_law.py",
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py"}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    README: ("root README",
             "sha256:698fef49ca5b27a10e913cbf51cd2ea8921a7656dbd8f5dcc33da8f71c65dbed",
             "f7e9145799d5d4f1d2452eae78c01937eb89c516"),
    TESTS_README: ("tests README",
                   "sha256:0ed30ec8b37fd4f1a33984e079ed2a9f276f41aefd532704b7bc370e27bc6fbe",
                   "931562e3753732e3aabf80d0cafacde208ff3e6c"),
    REGISTRY: ("registry",
               "sha256:30cbfe7742f2e049f2e8eacc37ccac502df42fcfdc2c8c41e01815f1c23b22e4",
               "6b1afbcb2df047544a56d249976e6f013f6364cd"),
    BOARD: ("board",
            "sha256:8c4162b95b953d6cb9e7bc6a19cbf72b410b94d3292063edfc3ebc75c3377028",
            "f87a31905e4c28ad1c65066b8eddc8f80d61143b"),
}
# The reviewed post-images of the two corrected files: (LF SHA-256, blob).
POSTIMAGE = {README: ("sha256:32c9bd765ad3942dc2312f5d6bcac12f2fe642a98956ec13d0e801cf92310931", "0845e4a0b06126bafb094918a899c24e255a0e93"),
             TESTS_README: ("sha256:2c71f4f680c488d042200a742c3b12c99d890bf24a4128a96883d88fa37f24cc", "167a00c7baa7cd68e82fb96ecdd2e9601e53b075")}

# ------------------------------------------------------ the exact sites
SITES = {
    README: (
        ('R1',
         '**W0 is accepted; W1 through W7 are complete and closed. W8-D1 and W8-D2 are complete; W8-D3 through W8-D7 remain closed behind their own gates.**',
         '**W0 is accepted; W1 through W7 are complete and closed. W8-D1 through W8-D4 are complete; W8-D5 through W8-D7 remain closed behind their own gates.**'),
        ('R2',
         'synthetic generated-evaluation records with individual human dispositions, and a class-opaque W8 discriminating instrument. **No public model has been contacted at any point.**',
         "synthetic generated-evaluation records with individual human dispositions, a class-opaque W8 discriminating instrument, and two further W8 corpora — a twelve-case supplementary corpus for synthetic calibration and an eighteen-case validation corpus — each dispositioned by the human authority in one session with the authoring records withheld, then revealed as exact retained bytes and compared case by case, with every recorded divergence left undiagnosed by the human authority's decision. **W7 closed without model contact; W8-D6, the contact decision, remains unopened and no W8 contact implementation is authorised before it; and the published W8 records, under ADR-0058's standing reservation, classify no exchange under ADR-0047 decision 3 and do not state whether model contact occurred.**"),
        ('R3',
         '| **W8** | Generative evaluation maturity | 🟡 In progress — D1 doctrine and D2 discriminating instrument complete; D3–D7 closed |',
         '| **W8** | Generative evaluation maturity | 🟡 In progress — D1 doctrine, D2 discriminating instrument, D3 synthetic calibration and D4 instrument validation complete; D5–D7 closed |'),
        ('R4',
         '- A W8 evaluation doctrine and a twelve-case, class-opaque discriminating instrument with published integrity commitments and withheld authoring records held outside the repository until a separately gated reveal.',
         '- A W8 evaluation doctrine; a twelve-case, class-opaque discriminating instrument whose withheld authoring records stay sealed outside the repository under their own authority; and two further corpora — twelve supplementary cases and eighteen validation cases — each with published integrity commitments, one human disposition session with the authoring records withheld, a byte-exact reveal of every withheld record, and a published case-level comparison carrying only the two permitted count kinds.'),
        ('R5',
         '- No W8-D3 review session, calibration, reveal or later contact decision. Those remain separately gated.',
         '- No diagnosis of any recorded divergence, no W8-D5 evidence-adequacy finding, no W8-D6 contact decision and no W8-D7 closure. Those remain separately gated.'),
        ('R6',
         '- No public model contact, model runtime, provider integration or model-generated public evidence.',
         "- No public model runtime, provider integration, transport, credentials or model-generated public evidence, and no W8 contact implementation before a lawful W8-D6 decision; ADR-0058's reservation on classifying any exchange stands."),
    ),
    TESTS_README: (
        ('T1',
         '**Run:** `python -m unittest discover -s tests -v` — Python 3 standard library only. No dependencies, no manifest, ever. The verbose flag renders the Tier 3 skip ledger.',
         "**Run:** `python -m unittest discover -s tests -v` — Python 3 standard library plus the engine's entire third-party runtime surface, exact-pinned in `requirements.txt` (`PyNaCl==1.6.2`, `cffi==2.0.0`, `pycparser==3.0`), which the engine's crypto port imports and the engine tests need; no other dependency manifest is admitted. The verbose flag renders the Tier 3 skip ledger."),
        ('T2',
         'The skip list is the outstanding-proof ledger; a skipped test is honest, a missing test is invisible.\n',
         'The skip list is the outstanding-proof ledger; a skipped test is honest, a missing test is invisible.\n\nLater phases added their own proof modules beside these three tiers: `test_w4_*`, `test_w6_*`, `test_w7_*`, `test_w8_*`, `test_engine_*`, `test_runtime_*` and `test_evaluation_*`. The three tiers remain the W2 skeleton they stand on.\n'),
    ),
}

# ------------------------------------------------- the grounding of each
# statement: (statement fragment in the corrected file, file, kind, source
# registry id or None, source path, evidence). Kinds: "record" - verbatim
# fragment of a registered accepted record or decision, cited by identity
# and path; "file" - verbatim fragment of a tracked file at the baseline
# that no registry entry names (a README pre-image carrying an earlier
# statement unchanged, or a tooling file), cited by path alone;
# "registry" - a fixed fact over the baseline registry; "tree" - a fixed
# fact over the baseline tracked tree. A statement resting on several
# sources has one row per source; a source's limit on a statement's
# meaning is its own row.
CPR = "docs/phases/W8-D4-completion-record.md"
CCR = "docs/phases/W8-D3-calibration-completion-record.md"
HDR = "docs/phases/W8-D3-human-disposition-record.md"
VSR = "docs/phases/W8-D4-validation-session-record.md"
VRC = "docs/phases/W8-D4-validation-record.md"
VCR = "docs/phases/W8-D4-validation-corpus-record.md"
SCR = "docs/phases/W8-S1-supplementary-corpus-record.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
W7CR = "docs/phases/W7-closure-record.md"
ADR58 = "docs/decisions/0058-w8-d3-session-recovery-law.md"
ADR59 = "docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md"
RESERVATION = ("does not classify any exchange under ADR-0047 decision 3 and "
               "does not state whether model contact occurred")
ADR58_RESERVATION = ("does not classify any exchange associated with the void "
                     "attempt under ADR-0047 decision 3, and does not state "
                     "whether model contact occurred")
NO_BLINDING = ("No test proves the absence of influence, semantic independence "
               "or reviewer blinding, and none is claimed.")
REVEAL_BYTES = "The reveal publishes the exact retained bytes"
COMPARISON = "the comparison records exactly the case identity"
TWO_KINDS = "Exactly two kinds of count are published"
CLOSED_GATES = "W8-D5 through W8-D7 remain closed behind their own briefs"
ALL_ACCEPTED = "every entry of deliverables W8-D1 to W8-D4 is accepted"
NO_LATER = "no entry of deliverable W8-D5, W8-D6 or W8-D7"
SEVEN_FAMILIES = ("seven proof families, each matching a tracked "
                  "tests/test_*.py module")

S_COMPLETE = "W8-D1 through W8-D4 are complete"
S_GATES = "W8-D5 through W8-D7 remain closed behind their own gates"
S_SESSION = ("each dispositioned by the human authority in one session with "
             "the authoring records withheld")
S_REVEALED = "then revealed as exact retained bytes"
S_COMPARED = "compared case by case"
S_W7 = "W7 closed without model contact"
S_D6 = "W8-D6, the contact decision, remains unopened"
S_NO_IMPL = "no W8 contact implementation is authorised before it"
S_RESERVE = ("classify no exchange under ADR-0047 decision 3 and do not state "
             "whether model contact occurred")
S_ROW = "D3 synthetic calibration and D4 instrument validation complete"
S_COMMIT = "each with published integrity commitments"
S_ONE_SESSION = ("one human disposition session with the authoring records "
                 "withheld")
S_BYTE_EXACT = "a byte-exact reveal of every withheld record"
S_COUNTS = ("a published case-level comparison carrying only the two "
            "permitted count kinds")
S_LATER = ("no W8-D5 evidence-adequacy finding, no W8-D6 contact decision and "
           "no W8-D7 closure")
S_RUNTIME = ("No public model runtime, provider integration, transport, "
             "credentials or model-generated public evidence")
S_BEFORE_D6 = "no W8 contact implementation before a lawful W8-D6 decision"
S_STANDS = "ADR-0058's reservation on classifying any exchange stands"
S_FAMILIES = ("Later phases added their own proof modules beside these three "
              "tiers")
S_SKELETON = "The three tiers remain the W2 skeleton they stand on"

GROUNDING = (
    # R1
    (S_COMPLETE, README, "file", None, README, "W8-D1 and W8-D2 are complete"),
    (S_COMPLETE, README, "record", "W8-D3-CCR", CCR,
     "W8-D3 is complete in the accepted sense"),
    (S_COMPLETE, README, "record", "W8-D4-CPR", CPR, "W8-D4 is complete"),
    (S_COMPLETE, README, "registry", None, REGISTRY, ALL_ACCEPTED),
    (S_GATES, README, "record", "W8-D4-CPR", CPR, CLOSED_GATES),
    (S_GATES, README, "registry", None, REGISTRY, NO_LATER),
    # R2
    ("a twelve-case supplementary corpus for synthetic calibration", README,
     "record", "W8-S1-SCR", SCR,
     "exactly twelve reviewer-visible supplementary cases"),
    ("an eighteen-case validation corpus", README, "record", "W8-D4-VCR", VCR,
     "exactly eighteen reviewer-visible validation cases"),
    (S_SESSION, README, "record", "W8-D3-HDR", HDR,
     "acting as the sole human reviewer, returned exactly one lawful token "
     "for each of the twelve cases"),
    (S_SESSION, README, "record", "W8-D4-VSR", VSR,
     "returned exactly one lawful token for each of the eighteen cases"),
    (S_SESSION, README, "record", "W8-D4-VSR", VSR,
     "This was the validation corpus's one session"),
    (S_SESSION, README, "record", "W8-D3-CCR", CCR,
     "twelve withheld authoring records"),
    (S_SESSION, README, "record", "W8-D3-HDR", HDR, NO_BLINDING),
    (S_SESSION, README, "record", "W8-D4-VSR", VSR, NO_BLINDING),
    (S_REVEALED, README, "record", "W8-D3-CCR", CCR, REVEAL_BYTES),
    (S_REVEALED, README, "record", "W8-D4-VRC", VRC, REVEAL_BYTES),
    (S_COMPARED, README, "record", "W8-D3-CCR", CCR, COMPARISON),
    (S_COMPARED, README, "record", "W8-D4-VRC", VRC, COMPARISON),
    ("with every recorded divergence left undiagnosed by the human "
     "authority's decision", README, "record", "W8-D4-CPR", CPR,
     "every recorded divergence stays recorded and undiagnosed"),
    (S_W7, README, "record", "W7-CR", W7CR,
     "No model contact occurred anywhere in W7"),
    (S_D6, README, "record", "W8-AR", RUNWAY, "Contact decision"),
    (S_D6, README, "record", "W8-D4-CPR", CPR, CLOSED_GATES),
    (S_D6, README, "registry", None, REGISTRY, NO_LATER),
    (S_NO_IMPL, README, "record", "W8-AR", RUNWAY,
     "No W8 deliverable before W8-D6 may contact a model, prepare "
     "credentials, providers, transport or implementation for contact"),
    (S_RESERVE, README, "record", "ADR-0058", ADR58, ADR58_RESERVATION),
    (S_RESERVE, README, "record", "W8-D3-HDR", HDR, RESERVATION),
    (S_RESERVE, README, "record", "W8-D4-VSR", VSR, RESERVATION),
    (S_RESERVE, README, "record", "W8-D4-CPR", CPR,
     "no classification of any exchange under ADR-0047 decision 3"),
    # R3
    (S_ROW, README, "record", "W8-D3-CCR", CCR,
     "W8-D3 is complete in the accepted sense"),
    (S_ROW, README, "record", "W8-D4-CPR", CPR, "W8-D4 is complete"),
    # R4
    ("whose withheld authoring records stay sealed outside the repository "
     "under their own authority", README, "record", "ADR-0059", ADR59,
     "its retained records stay sealed in their existing custody"),
    (S_COMMIT, README, "record", "W8-D3-CCR", CCR,
     "They are bound by `W8-S1-CM-01`"),
    (S_COMMIT, README, "record", "W8-D4-VRC", VRC,
     "They are bound by `W8-V1-CM-01` and `W8-V1-CM-02`"),
    (S_ONE_SESSION, README, "record", "W8-D3-HDR", HDR,
     "acting as the sole human reviewer, returned exactly one lawful token "
     "for each of the twelve cases"),
    (S_ONE_SESSION, README, "record", "W8-D4-VSR", VSR,
     "This was the validation corpus's one session"),
    (S_ONE_SESSION, README, "record", "W8-D4-VSR", VSR, NO_BLINDING),
    (S_BYTE_EXACT, README, "record", "W8-D3-CCR", CCR, REVEAL_BYTES),
    (S_BYTE_EXACT, README, "record", "W8-D4-VRC", VRC, REVEAL_BYTES),
    (S_COUNTS, README, "record", "W8-D3-CCR", CCR, TWO_KINDS),
    (S_COUNTS, README, "record", "W8-D4-VRC", VRC, TWO_KINDS),
    # R5
    ("No diagnosis of any recorded divergence", README, "record", "W8-D4-CPR",
     CPR, "No divergence is diagnosed."),
    (S_LATER, README, "record", "W8-D4-CPR", CPR,
     CLOSED_GATES + "; this record opens none of them"),
    (S_LATER, README, "registry", None, REGISTRY, NO_LATER),
    # R6
    (S_RUNTIME, README, "record", "W8-AR", RUNWAY,
     "choose a provider · build a model transport · create credentials"),
    (S_RUNTIME, README, "file", None, README, "model-generated public evidence"),
    (S_BEFORE_D6, README, "record", "W8-AR", RUNWAY,
     "contact a model before a lawful W8-D6 decision and a separately "
     "accepted implementation brief"),
    (S_STANDS, README, "record", "ADR-0058", ADR58, ADR58_RESERVATION),
    (S_STANDS, README, "record", "W8-D3-HDR", HDR,
     "ADR-0058 Part F carries whole"),
    # T1
    ("the engine's entire third-party runtime surface, exact-pinned in "
     "`requirements.txt`", TESTS_README, "file", None, MANIFEST,
     "The engine's entire third-party runtime surface, exact-pinned."),
    ("which the engine's crypto port imports", TESTS_README, "file", None,
     "engine/ports/crypto.py", "import nacl.secret"),
    ("and the engine tests need", TESTS_README, "file", None,
     "tests/test_engine_custody.py", "import nacl.pwhash"),
    ("no other dependency manifest is admitted", TESTS_README, "file", None,
     "tests/test_repo_state.py",
     "exactly the engine directory and the single pinned manifest, nothing"),
    # T2
    (S_FAMILIES, TESTS_README, "tree", None, TREE, SEVEN_FAMILIES),
    (S_SKELETON, TESTS_README, "record", "W2-D3", CHECKLIST,
     "`tests/` (W2-D5)"),
    (S_SKELETON, TESTS_README, "file", None, TESTS_README,
     "## The three tiers"),
)
KINDS = ("record", "file", "registry", "tree")
GROUNDING_SECTION = "## 3. Grounding"
GROUNDING_HEADER = ("| Statement (fragment in the corrected file) | Kind | "
                    "Source | Evidence |")
GROUNDING_SEPARATOR = "|---|---|---|---|"


def registry_fact(evidence, entries):
    if evidence == ALL_ACCEPTED:
        earlier = [e for e in entries if e["deliverable"] in D4_DELIVERABLES]
        return bool(earlier) and all(e["status"] == "accepted"
                                     for e in earlier)
    if evidence == NO_LATER:
        return not any(e["deliverable"] in LATER_DELIVERABLES
                       for e in entries)
    return None


def tree_fact(evidence, tracked):
    if evidence == SEVEN_FAMILIES:
        return len(FAMILIES) == 7 and all(
            any(p.startswith("tests/" + f) and p.endswith(".py")
                for p in tracked) for f in FAMILIES)
    return None


# --------------------------------------- board and registry: authorised edits
DER_LINK = "([`W8-documentation-erratum.md`](W8-documentation-erratum.md))"
DER_TAIL = (
    "six W8 statements in the root README and the tests README's dependency "
    "statement and family note to what the published record states, each "
    "mapped to cited published sources and deciding no reserved question, "
    "changing no governing record, proof, case, register or registry entry "
    "other than its own.")
DER_STATUS = {
    "draft": ("**A draft documentation erratum, `W8-DER`, is before the human "
              "reviewer** " + DER_LINK + ": if accepted, it would correct "
              + DER_TAIL),
    "accepted": ("**`W8-DER` — the documentation erratum — is accepted** "
                 + DER_LINK + " — accepted %s: it corrects " + DER_TAIL),
}
DER_ROW = ("| W8 — Documentation Erratum (W8-DER) | "
           "[`W8-documentation-erratum.md`](W8-documentation-erratum.md) | ")
DER_ROW_BODY = (
    "Tier J: **a phase-level documentation erratum** under the phase entry "
    "checklist's rules 2, 4 and 10 — six W8 statements in the root README "
    "and the tests README's dependency statement and family note corrected "
    "to the published record as exact pinned transformations, every "
    "statement mapped to cited published sources at the baseline with the "
    "ADR-0058 reservation preserved, with proof obligations DE1 to DE6. **No "
    "governing record, proof, case, register, revealed record or custody "
    "changes; no status flips; no capability claim; no exchange classified; "
    "the concept overview is named as a separate decision.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
BOARD_STATUS_ANCHOR = "stay exactly as published. **" + R9_SENTENCE[:-1]
BOARD_ROW_ANCHOR = "**W8-D5 to W8-D7 stay closed.** |\n"
DER_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
DER_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-DER", "path": RECORD, "type": "phase-record",
    "title": "W8 - Documentation Erratum",
    "role": (
        "A phase-level documentation erratum under the phase entry "
        "checklist's rules 2, 4 and 10, outside every W8 deliverable: "
        "corrects six W8 statements in the root README and the tests "
        "README's dependency statement and family note to what the "
        "published record states, as exact pinned transformations of their "
        "baseline pre-images, every corrected statement mapped to cited "
        "published sources at the baseline, the ADR-0058 reservation on "
        "classifying any exchange preserved, with proof obligations DE1 to "
        "DE6. Changes no governing record, no proof module other than its "
        "own, no case, manifest, register, revealed record, custody or "
        "registry entry other than its own; flips no status; adds no "
        "capability, readiness, safety, correctness or approval claim; "
        "classifies no exchange and does not state whether model contact "
        "occurred; names the concept overview as a separate decision."),
    "depends_on": ["ADR-0056", "W8-AR", "W8-D4-CPR", "W8-D4-VRC",
                   "W8-D4-VSR", "W8-D4-VCR", "W8-D3-CCR", "W8-D3-HDR",
                   "W8-S1-SCR", "ADR-0058", "ADR-0059", "ADR-0008", "W7-CR"],
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


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def committed(commit, rel):
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def der_snapshot():
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the erratum record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = der_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def historical(read, rel):
    ns = {"__name__": "_w8_der_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def baseline_tracked():
    return _git("ls-tree", "-r", "--name-only", BASELINE).split()


def site_violations(rel, present, h, sites=None):
    """DE1 for one file: the baseline pre-image under the site table yields
    exactly the present bytes, each site occurs once before and after, the
    table reverses, and the result is the reviewed post-image."""
    sites = SITES[rel] if sites is None else sites
    v = []
    pre = baseline_text(rel)
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
    return v


def record_sites_violations(record):
    """The record carries each site's new wording exactly once."""
    return ["%s: new wording occurs %d times in the record"
            % (label, record.count(new.rstrip("\n")))
            for rel in (README, TESTS_README)
            for label, _, new in SITES[rel]
            if record.count(new.rstrip("\n")) != 1]


def _cell(text):
    """A code span, unless the text already carries a backtick, in which
    case it stands verbatim: a cell never nests code spans."""
    return text if "`" in text else "`%s`" % text


def grounding_rows(grounding=None):
    return [[_cell(s), kind,
             ("`%s` · `%s`" % (rid, path)) if rid else "`%s`" % path,
             _cell(ev)]
            for s, _, kind, rid, path, ev in (GROUNDING if grounding is None
                                              else grounding)]


def grounding_violations(texts, record, entries, tracked, h, grounding=None):
    """DE2: each statement once in its corrected file; each record/file row's
    fragment present verbatim in its tracked source at the baseline, a
    record row's identity accepted at that path, a file row carrying no
    identity and naming no registered path; each registry/tree row's fixed
    fact holding at the baseline; the record's table read whole equal to the
    trusted rows. Presence and structure only - never entailment."""
    grounding = GROUNDING if grounding is None else grounding
    v = []
    by_id = {e["id"]: e for e in entries}
    registered = {e["path"] for e in entries}
    for s, rel, kind, rid, path, ev in grounding:
        n = _flat(texts[rel]).count(s)
        if n != 1:
            v.append("statement occurs %d times: %s" % (n, s[:40]))
        if kind not in KINDS:
            v.append("unknown kind: %s" % kind)
            continue
        if kind in ("record", "file"):
            if path not in tracked:
                v.append("source not tracked at the baseline: %s" % path)
                continue
            if ev not in _flat(baseline_text(path)):
                v.append("fragment absent from its source: %s" % ev[:40])
            if kind == "record":
                e = by_id.get(rid)
                if (rid is None or e is None or e["status"] != "accepted"
                        or e["path"] != path):
                    v.append("%s is not an accepted entry at that path" % rid)
            else:
                if rid is not None:
                    v.append("a file row carries a registry identity: %s"
                             % rid)
                if path in registered:
                    v.append("a file row names a registered path: %s" % path)
        elif kind == "registry":
            if rid is not None or path != REGISTRY:
                v.append("a registry row is not over the registry")
            if registry_fact(ev, entries) is not True:
                v.append("a registry fact does not hold: %s" % ev)
        else:
            if rid is not None or path != TREE:
                v.append("a tree row is not over the tracked tree")
            if tree_fact(ev, tracked) is not True:
                v.append("a tree fact does not hold: %s" % ev)
    rows, problems = h.rev.closed_table(record, GROUNDING_SECTION,
                                       GROUNDING_HEADER, GROUNDING_SEPARATOR, 4)
    v += problems
    if rows != grounding_rows():
        v.append("the grounding table is not exactly its trusted rows")
    return v


def manifest_pins(manifest_text):
    return [l.strip() for l in manifest_text.split("\n")
            if l.strip() and not l.lstrip().startswith("#")]


def consistency_violations(tests_readme, readme, manifest_text, entries,
                           tracked):
    """DE3: the tests README's pinned lines are exactly the manifest's; each
    named family matches a tracked module and no other family is named; the
    README's W8 statements agree with the registry at the baseline."""
    v = []
    pins = manifest_pins(manifest_text)
    cited = re.findall(r"`([A-Za-z0-9_-]+==[0-9][0-9A-Za-z.]*)`", tests_readme)
    if sorted(cited) != sorted(pins) or len(cited) != len(set(cited)):
        v.append("the tests README's pinned lines are not exactly the "
                 "manifest's")
    for fam in FAMILIES:
        if tests_readme.count("`%s*`" % fam) != 1:
            v.append("a family is not named once: %s" % fam)
        if not any(p.startswith("tests/" + fam) and p.endswith(".py")
                   for p in tracked):
            v.append("a named family matches no tracked module: %s" % fam)
    named = set(re.findall(r"`(test_[a-z0-9]+_)\*`", tests_readme))
    if named != set(FAMILIES):
        v.append("the tests README names a family outside the fixed set")
    by_id = {e["id"]: e for e in entries}
    for cid in COMPLETION_IDS:
        if cid not in by_id or by_id[cid]["status"] != "accepted":
            v.append("a completion record is not accepted: %s" % cid)
    for e in entries:
        if e["deliverable"] in D4_DELIVERABLES and e["status"] != "accepted":
            v.append("an earlier W8 entry is not accepted: %s" % e["id"])
        if e["deliverable"] in LATER_DELIVERABLES:
            v.append("a later W8 entry exists: %s" % e["id"])
    flat = _flat(readme)
    for s in (S_COMPLETE, S_ROW, "D5–D7 closed"):
        if flat.count(s) != 1:
            v.append("the README's W8 statement is not carried once: %s" % s)
    return v


def count_beside(tokens):
    name = (r"(?<![A-Za-z0-9])(?:%s|agreements?|divergences?)(?![A-Za-z0-9])"
            % "|".join(re.escape(t) for t in sorted(tokens)))
    number = (r"(?<![A-Za-z0-9])(?:\d+|one|two|three|four|five|six|seven|"
              r"eight|nine|ten|eleven|twelve)(?![A-Za-z0-9])")
    gap = r"[^A-Za-z0-9\n]{0,8}"
    return re.compile("(?i)" + name + gap + number + "|" + number + gap + name)


def pin_free(text, pins):
    """The text with each given string - the manifest's own pins, and the
    licence name - removed only where it occurs whole between token
    boundaries; a longer string that merely begins with one, or a pin at
    another version, is left in place for the scan."""
    for pin in pins:
        text = re.sub(r"(?<!%s)%s(?!%s)" % (PIN_EDGE, re.escape(pin), PIN_EDGE),
                      "", text)
    return text


def exposure_violations(text, h, pins=None):
    """DE4 over a whole surface: no case identity, token, count beside a
    kind or token, reserved label, schema literal or derived-figure form.
    Only the licence name and the manifest's own pins are set aside, each
    matched whole."""
    pins = manifest_pins(baseline_text(MANIFEST)) if pins is None else pins
    v = []
    if h.rec.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    v += ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    schemas = ((h.pkt.PACKET_SCHEMA, h.cal.REGISTER_SCHEMA,
                h.env.AUTHORING_SCHEMA) + tuple(h.law.NEW_SCHEMAS))
    v += ["a schema literal is present" for s in schemas if s in text]
    v += ["a token is present" for t in h.pkt.TOKENS if t in text]
    if count_beside(h.pkt.TOKENS).search(text):
        v.append("a count beside a token or relation")
    stripped = pin_free(text, (LICENCE_NAME,) + tuple(pins))
    stripped = re.sub(r"(?<![0-9a-f])[0-9a-f]{40,64}(?![0-9a-f])", "", stripped)
    v += h.vr.figure_hits(stripped, h.pkt.TOKENS)
    return v


def method_label_hits(text, h):
    """DE4 over the wording this landing adds: no method label. The README's
    pre-existing prose is not this landing's to police."""
    return ["a method label: %s" % m for m in sorted(h.law.ADMITS)
            if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]


def added_wording():
    return "\n".join(new for rel in (README, TESTS_README)
                     for _, _, new in SITES[rel])


def der_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and DER_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (DER_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "stay exactly as published. " + fill(DER_STATUS[state])
         + " **" + R9_SENTENCE[:-1]),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + DER_ROW + fill(ROW_PREFIX[state]) + DER_ROW_BODY
         + " |\n"),
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


def added_board_wording():
    sample = "2026-01-01"
    return " ".join([DER_ROW, DER_ROW_BODY, DER_STATUS["draft"],
                     DER_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


class LiveHelpersSabotaged:
    ABSENT = object()
    TARGETS = (
        ("test_w8_recovery_authority", "apply_sites",
         lambda text, sites: (text, [])),
        ("test_w8_reveal_calibration", "closed_table",
         lambda *a, **k: ([], [])),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_validation_reveal", "figure_hits", lambda *a, **k: []),
        ("test_w8_discriminating_instrument_corpus", "reserved_channel_hits",
         lambda *a, **k: []),
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


# ------------------------------------------------------------------ proofs
class DE1_ExactSites(unittest.TestCase):
    def test_de1_both_files_are_exact_pinned_transformations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth")
        record = read(RECORD).decode("utf-8")
        for rel in (README, TESTS_README):
            present = read(rel).decode("utf-8")
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(), PREIMAGE[rel][2])
            with self.subTest(exact_sites=PREIMAGE[rel][0]):
                self.assertEqual(site_violations(rel, present, h), [])
                self.assertEqual(_blob(present.encode("utf-8")),
                                 POSTIMAGE[rel][1])
            first = present.split("\n", 1)[0] + "\n"
            for name, (text, table) in {
                    "an extra byte": (present + " ", None),
                    "a missing site": (present, SITES[rel][1:]),
                    "a self-consistent but unpinned edit": (
                        present.replace(first, first + "<!-- planted -->\n", 1),
                        SITES[rel] + (("planted", first,
                                       first + "<!-- planted -->\n"),))}.items():
                with self.subTest(control="%s is refused" % name,
                                  file=PREIMAGE[rel][0]):
                    self.assertTrue(site_violations(rel, text, h, table))
        with self.subTest(fact="the record carries each new wording once"):
            self.assertEqual(record_sites_violations(record), [])
        with self.subTest(control="a dropped wording is refused"):
            self.assertTrue(record_sites_violations(
                record.replace(SITES[README][0][2], "", 1)))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth")
                for rel in (README, TESTS_README):
                    self.assertEqual(site_violations(
                        rel, read(rel).decode("utf-8"), hh), [])


class DE2_Grounding(unittest.TestCase):
    def test_de2_every_statement_is_mapped_to_published_sources(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        texts = {rel: read(rel).decode("utf-8") for rel in (README, TESTS_README)}
        record = read(RECORD).decode("utf-8")
        entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
        tracked = baseline_tracked()
        with self.subTest(fact="every statement once, every fragment in its "
                               "source, every fact at the baseline, the "
                               "table read whole"):
            self.assertEqual(grounding_violations(texts, record, entries,
                                                  tracked, h), [])
        with self.subTest(fact="every kind is used and every row is kinded"):
            self.assertEqual({r[2] for r in GROUNDING}, set(KINDS))
        s0 = GROUNDING[0][0]
        rows = ["| " + " | ".join(r) + " |" for r in grounding_rows()]
        for name, (t, r) in {
                "a statement reworded": (
                    dict(texts, **{README: texts[README].replace(
                        s0, s0.replace("complete", "done"), 1)}), record),
                "a statement duplicated": (
                    dict(texts, **{README: texts[README] + "\n" + s0 + "\n"}),
                    record),
                "a dropped table row": (texts, record.replace(
                    rows[0] + "\n", "", 1)),
                "a stray table row": (texts, record.replace(
                    rows[-1] + "\n",
                    rows[-1] + "\n| `w` | record | `x` | `z` |\n", 1)),
                "a reordered table": (texts, record.replace(
                    rows[0] + "\n" + rows[1], rows[1] + "\n" + rows[0], 1))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(grounding_violations(t, r, entries, tracked, h))
        rec0 = next(g for g in GROUNDING if g[2] == "record")
        file0 = next(g for g in GROUNDING if g[2] == "file")
        for name, (g, e, tr) in {
                "an absent fragment": (
                    GROUNDING[:1] + ((rec0[0], rec0[1], "record", rec0[3],
                                      rec0[4], "mechanics sentinel absent"),),
                    entries, tracked),
                "a record row's source not accepted": (
                    GROUNDING, [dict(x, status="draft")
                                if x["id"] == "W8-D4-CPR" else x
                                for x in entries], tracked),
                "a record row's source at another path": (
                    GROUNDING, [dict(x, path="docs/phases/other.md")
                                if x["id"] == "W8-D4-CPR" else x
                                for x in entries], tracked),
                "a record row without an identity": (
                    GROUNDING[:1] + ((rec0[0], rec0[1], "record", None,
                                      rec0[4], rec0[5]),), entries, tracked),
                "a file row carrying an identity": (
                    GROUNDING[:1] + ((file0[0], file0[1], "file", "W8-D4-CPR",
                                      file0[4], file0[5]),), entries, tracked),
                "a file row naming a registered path": (
                    GROUNDING[:1] + ((S_SKELETON, TESTS_README, "file", None,
                                      CHECKLIST, "`tests/` (W2-D5)"),),
                    entries, tracked),
                "a file row naming a path registered later": (
                    GROUNDING, entries + [dict(entries[-1], id="W2-D5-RM",
                                               path=TESTS_README)], tracked),
                "an unknown kind": (
                    GROUNDING[:1] + ((rec0[0], rec0[1], "reading", rec0[3],
                                      rec0[4], rec0[5]),), entries, tracked),
                "a registry fact failing": (
                    GROUNDING, entries + [dict(entries[-1], id="W8-D5-SNT",
                                               deliverable="W8-D5")], tracked),
                "a tree fact failing": (
                    GROUNDING, entries,
                    [p for p in tracked if not p.startswith("tests/test_w6_")]),
                "an untracked source": (
                    GROUNDING, entries,
                    [p for p in tracked if p != rec0[4]])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(grounding_violations(texts, record, e, tr,
                                                     h, g))
        with self.subTest(control="a file row naming a registered path is "
                                  "refused for that reason alone"):
            self.assertEqual(grounding_violations(
                texts, record, entries, tracked, h,
                ((S_SKELETON, TESTS_README, "file", None, CHECKLIST,
                  "`tests/` (W2-D5)"),)),
                ["a file row names a registered path: " + CHECKLIST])
        with self.subTest(fact="every file row's path is unregistered and "
                               "every record row's path is registered"):
            registered = {e["path"] for e in entries}
            for s, _, kind, rid, path, _ in GROUNDING:
                if kind == "file":
                    self.assertNotIn(path, registered)
                elif kind == "record":
                    self.assertIn(path, registered)
        for name, mutated in h.rev.boundary_mutants(
                record, GROUNDING_SECTION, rows[-1]).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(grounding_violations(texts, mutated, entries,
                                                     tracked, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(grounding_violations(texts, record, entries,
                                                      tracked, hh), [])


class DE3_Consistency(unittest.TestCase):
    def test_de3_pins_families_and_registry_agree(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tests_readme = read(TESTS_README).decode("utf-8")
        readme = read(README).decode("utf-8")
        manifest = baseline_text(MANIFEST)
        entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
        tracked = baseline_tracked()
        with self.subTest(fact="pins equal the manifest; families tracked; "
                               "registry agrees"):
            self.assertEqual(consistency_violations(
                tests_readme, readme, manifest, entries, tracked), [])
            self.assertEqual(len(manifest_pins(manifest)), 3)
        for name, args in {
                "a pin missing from the README": (
                    tests_readme.replace("`cffi==2.0.0`, ", "", 1), readme,
                    manifest, entries, tracked),
                "a pin not in the manifest": (
                    tests_readme.replace("`cffi==2.0.0`", "`cffi==2.0.1`", 1),
                    readme, manifest, entries, tracked),
                "a family not tracked": (
                    tests_readme, readme, manifest, entries,
                    [p for p in tracked if not p.startswith("tests/test_w6_")]),
                "a family outside the fixed set": (
                    tests_readme.replace("`test_w4_*`", "`test_w4_*`, "
                                         "`test_w9_*`", 1), readme, manifest,
                    entries, tracked),
                "a later W8 entry": (
                    tests_readme, readme, manifest,
                    entries + [dict(entries[-1], id="W8-D5-SNT",
                                    deliverable="W8-D5")], tracked),
                "a completion record not accepted": (
                    tests_readme, readme, manifest,
                    [dict(e, status="draft") if e["id"] == "W8-D4-CPR" else e
                     for e in entries], tracked),
                "a changed W8 statement": (
                    tests_readme, readme.replace("D5–D7 closed", "D5–D7 open",
                                                 1), manifest, entries, tracked)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(consistency_violations(*args))


class DE4_NoExposure(unittest.TestCase):
    def test_de4_no_case_level_material_and_disclaimers_retained(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr")
        readme = read(README).decode("utf-8")
        record = read(RECORD).decode("utf-8")
        pins = manifest_pins(baseline_text(MANIFEST))
        for name, text in (("root README", readme),
                           ("tests README", read(TESTS_README).decode("utf-8")),
                           ("record", record),
                           ("board wording this landing adds",
                            added_board_wording())):
            with self.subTest(surface=name):
                self.assertEqual(exposure_violations(text, h), [])
        for name, text in (("record", record),
                           ("wording this landing adds", added_wording()),
                           ("board wording this landing adds",
                            added_board_wording())):
            with self.subTest(no_method_label=name):
                self.assertEqual(method_label_hits(text, h), [])
        with self.subTest(fact="the README's disclaimers are retained"):
            for d in DISCLAIMERS:
                self.assertEqual(_flat(readme).count(d), 1)
                self.assertEqual(_flat(baseline_text(README)).count(d), 1)
        with self.subTest(fact="only the manifest's pins and the licence name "
                               "are set aside"):
            self.assertEqual(len(pins), 3)
            self.assertEqual(exposure_violations(
                "the pins `%s` under the %s" % ("`, `".join(pins),
                                                 LICENCE_NAME), h), [])
        tok = sorted(h.pkt.TOKENS)[0]
        for name, plant in {"a case identity": "W8-C-" + "a" * 64,
                            "a token": tok, "a count beside a kind": "11 agreements",
                            "a decimal rate": "agreement rate 0.5",
                            "a reserved label": sorted(h.cor.RESERVED_FIELDS)[0],
                            "a pin-shaped figure": "`score==0.5`",
                            "a pin-shaped figure word": "metric==0.5",
                            "an approved name at an unapproved version":
                                "PyNaCl==0.5",
                            "an unapproved pin": "other==0.5",
                            "a licence-name prefix at another version":
                                "`%s5`" % LICENCE_NAME,
                            "a licence-name prefix at a further version":
                                LICENCE_NAME + "1",
                            "a licence name not matched whole":
                                "x" + LICENCE_NAME,
                            "a licence-name prefix not matched whole":
                                "x" + LICENCE_NAME + "5"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(readme + "\n" + plant, h))
        with self.subTest(control="a pin is set aside only when matched whole"):
            self.assertNotIn(pins[0], pin_free("a %s b" % pins[0], pins))
            self.assertIn(pins[0], pin_free(pins[0] + "1", pins))
            self.assertIn(pins[0], pin_free("x-" + pins[0], pins))
            self.assertIn(pins[0], pin_free(pins[0] + ".post1", pins))
        with self.subTest(control="the licence name is set aside only when "
                                  "matched whole"):
            name = (LICENCE_NAME,)
            self.assertNotIn("2.0", pin_free("the [%s](LICENSE)" % LICENCE_NAME,
                                             name))
            self.assertIn(LICENCE_NAME + "5", pin_free(LICENCE_NAME + "5", name))
            self.assertIn(LICENCE_NAME + "1", pin_free(LICENCE_NAME + "1", name))
            self.assertIn(LICENCE_NAME, pin_free("x" + LICENCE_NAME, name))
            self.assertIn(LICENCE_NAME, pin_free(LICENCE_NAME + ".1", name))
        with self.subTest(control="a planted method label is detected"):
            self.assertTrue(method_label_hits(
                record + "\n" + sorted(h.law.ADMITS)[0], h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr")
                self.assertEqual(exposure_violations(readme, hh), [])
                self.assertTrue(exposure_violations(record + "\n`score==0.5`",
                                                    hh))
                self.assertTrue(exposure_violations(
                    record + "\n`%s5`" % LICENCE_NAME, hh))


class DE5_RegistryAndBoard(unittest.TestCase):
    def test_de5_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = der_state(read(RECORD).decode("utf-8"), h)
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
        with self.subTest(fact="exact authorised board, R9's sentence once",
                          state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        entries = json.loads(reg)["entries"]
        e = {x["id"]: x for x in entries}.get("W8-DER")
        with self.subTest(entry="W8-DER"):
            self.assertIsNotNone(e)
            self.assertEqual((e["path"], e["type"], e["phase"],
                              e["deliverable"]), (RECORD, "phase-record", "W8",
                                                  None))
            self.assertEqual((e["status"], e["accepted_date"]), (state, date))
            self.assertEqual(e["content_hash"], record_hash)
        with self.subTest(fact="neither README is registered"):
            self.assertEqual([x["id"] for x in entries
                              if x["path"] in (README, TESTS_README)], [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))


class DE6_Census(unittest.TestCase):
    def test_de6_census_is_exactly_six_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly six paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module changes among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")
                              and p.endswith(".py")}, {SELF_REL})
        flat = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly six "
                          r"paths:\*\* (.*?) No governing record", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {MANIFEST},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
