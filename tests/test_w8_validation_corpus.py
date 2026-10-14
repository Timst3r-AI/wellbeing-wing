"""W8-D4-C — validation corpus proofs (W8-D4-VCR, VC1–VC13).

The corpus landing of W8-D4 under the effective ADR-0060: exactly eighteen
reviewer-visible validation cases and two class-opaque manifests,
W8-V1-CM-01 and W8-V1-CM-02, in their own home, with the two proof
successions ADR-0060 Part J decision 38 stages for this landing. This module
proves the corpus's shape, identity, binding and closure at its landing,
its textual non-reuse, its exposure limits, its registration and the exact
transformations of everything this landing changes, each with planted-mutant
or negative controls.

Following ADR-0060 decision 39, every proof here reads this landing's fixed
snapshot - the candidate over the baseline before the commit exists, the
one commit that added the corpus record afterwards - except the
committed-object reads with working-copy correspondence that these immutable
artefacts require (VC1). Before the commit exists, the twenty immutable
corpus files are read as their raw, unconverted bytes: a new object's
canonical form and every binding over it are established on the bytes as
written, never after a line-ending conversion; every other surface keeps
its LF treatment. This module holds no live gate on the absence or
admission of any future artefact; those gates stay in the validation law's
VL10.

THIS MODULE READS NO CUSTODY. It names no case as a literal, holds no
disposition token, method label or published schema literal as a literal,
renders no packet and opens no withheld record. It reads the published
validation cases and manifests, and, for identity disjointness and textual
non-reuse only, the published cases and manifests of both earlier corpora.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any case's authored class, method, family, intended
disposition or construction; the corpus's composition; that any case is
fresh or semantically independent of anything; that any retained record
exists, is intact or was handled as the record states; anything about the
reviewer or the reviewer's prior exposure; that the instrument is valid,
mature or ready; or that any session, reproduction, reveal, count or
diagnosis may now begin.
"""

import hashlib
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import test_w8_discriminating_instrument_corpus as corpus
import test_w8_discriminating_instrument_envelope as envelope
import test_w8_recovery_authority as authority
import test_w8_reveal_calibration as reveal
import test_w8_session_recovery_law as recovery
import test_w8_supplementary_corpus as supplement
import test_w8_validation_law as vlaw
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified ADR-0060 landing: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "054f1270b8206a059636e18e012223ddfe52d5ea"

HOME = "governance/validation-cases"
MANIFEST = HOME + "/W8-V1-commitment-manifest.json"
CMANIFEST = HOME + "/W8-V1-construction-manifest.json"
RECORD = "docs/phases/W8-D4-validation-corpus-record.md"
SELF_REL = "tests/test_w8_validation_corpus.py"
ENVELOPE = "tests/test_w8_discriminating_instrument_envelope.py"
LAWMOD = "tests/test_w8_validation_law.py"
LAW = "docs/decisions/0060-w8-instrument-validation-law.md"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
D2_MANIFEST = "governance/discriminating-instrument/W8-D2-commitment-manifest.json"
S1_MANIFEST = supplement.MANIFEST
TOTAL = 18
COUNT_SENTENCE = "exactly eighteen reviewer-visible validation cases"
FIXED_CENSUS = frozenset({MANIFEST, CMANIFEST, RECORD, SELF_REL, ENVELOPE,
                          LAWMOD, REGISTRY, BOARD})
CASE_FILE = re.compile(r"W8-C-[0-9a-f]{64}\.json")
CROW_FIELDS = frozenset({"case_id", "construction_commitment_sha256"})

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    ENVELOPE: ("envelope module",
               "sha256:99047ceb3f58f5209598d9eb84cd6972cc2786ca4e7a43ce1dfbfe8f592d7323",
               "25a1c2d75cfdc18a5ce2c8b318d6e7d72050aef8"),
    LAWMOD: ("validation-law module",
             "sha256:b07e367761654ad3856f64598e513bea8b81badadab1fb2dd66b6a30082a88d9",
             "cdd015d7070e39a06929ea45ebb0e9ec818f47ae"),
    REGISTRY: ("registry",
               "sha256:de4e441fa75bd94840d2ba1c9a76d4b3e1d18062073b58b8b4207dd25ba84bad",
               "f0a36b16a15a5572c86891980850bb5434695b0c"),
    BOARD: ("board",
            "sha256:a0161dab57c9424d2848f1d9bae1ad637f07f4cc5c39423755c2115c9b5f2511",
            "a36bb5d3cabcf965e99403a4b80dacb8d6ef4162"),
}
# The reviewed post-images of the two successions: (LF SHA-256, blob).
POSTIMAGE = {
    ENVELOPE: ("sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80", "f579b93fc107fad5c55455ff65353081fd456795"),
    LAWMOD: ("sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02", "ce39f6c0812cae5c36d646f3db211547544560ce"),
}
# Section 4's succession table, read whole: exactly this header, this
# separator and the two rows built from the trusted pins (succession_rows).
SUCCESSION_SECTION = "## 4. Proof successions (ADR-0060 Part J decision 38)"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"

# --------------------------------- the two staged successions (decision 38)
SITES = {
    ENVELOPE: (
        ('V12',
         '                      "governance/discriminating-reveal/"))], [])\n',
         '                      "governance/discriminating-reveal/",\n                      # Succeeded at the W8-D4 corpus landing (ADR-0060\n                      # Part J decision 38).\n                      "governance/validation-cases/"))], [])\n'),
    ),
    LAWMOD: (
        ('VL10',
         '                 "docs/phases/W8-D4-completion-record.md")\n',
         '                 "docs/phases/W8-D4-completion-record.md")\n# Admitted at the corpus landing (ADR-0060 Part J decision 38): the case\n# home its commitment manifest binds, the two manifests, the corpus record\n# and its three W8-D4 entries, the construction manifest joining the\n# holders of its own schema literal. The former absence stays proven at\n# the D4-B landing commit.\nD4B_LANDING = "054f1270b8206a059636e18e012223ddfe52d5ea"\nCORPUS_MANIFEST = VALIDATION_HOMES[0] + "/W8-V1-commitment-manifest.json"\nCONSTRUCTION_MANIFEST = (VALIDATION_HOMES[0]\n                         + "/W8-V1-construction-manifest.json")\nCORPUS_RECORD = LATER_RECORDS[0]\nCORPUS_IDS = frozenset({"W8-D4-VCR", "W8-V1-CM-01", "W8-V1-CM-02"})\n'),
        ('VL10',
         'def staged_absence_violations(tracked, exists, entries, holders):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing."""\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes)]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS if exists(p)]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != \\\n            D4_ENTRIES:\n        v.append("the W8-D4 entries are not exactly the brief\'s and this "\n                 "record\'s")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS]\n    v += ["a new schema literal is carried outside this record and its "\n          "module: %s" % p for p in holders if p not in (LAW, SELF_REL)]\n    return v\n',
         'def staged_absence_violations(tracked, exists, entries, holders,\n                              corpus=None):\n    """VL10\'s present-state gates: no later home, record, registry entry or\n    new schema literal before its own landing. Succeeded at the corpus\n    landing: `corpus` is that landing\'s admitted path set - the two\n    manifests, the corpus record and the case files its commitment manifest\n    binds - or None for the state before it."""\n    admitted = frozenset(corpus or ())\n    landed = corpus is not None\n    ids = D4_ENTRIES | (CORPUS_IDS if landed else frozenset())\n    holders_ok = {LAW, SELF_REL} | ({CONSTRUCTION_MANIFEST} if landed\n                                    else set())\n    on_disk_ok = admitted | ({VALIDATION_HOMES[0]} if landed else set())\n    v = []\n    homes = tuple(h + "/" for h in VALIDATION_HOMES)\n    v += ["a later home is tracked: %s" % p for p in tracked\n          if p.startswith(homes) and p not in admitted]\n    v += ["a later record is tracked: %s" % p for p in tracked\n          if p in LATER_RECORDS and p not in admitted]\n    v += ["a later home or record exists on disk: %s" % p\n          for p in VALIDATION_HOMES + LATER_RECORDS\n          if exists(p) and p not in on_disk_ok]\n    if {e["id"] for e in entries if e["deliverable"] == "W8-D4"} != ids:\n        v.append("the W8-D4 entries are not exactly the admitted set")\n    v += ["a later registry entry exists: %s" % e["id"] for e in entries\n          if e["id"] in LATER_IDS - ids]\n    v += ["a new schema literal is carried outside its admitted holders: "\n          "%s" % p for p in holders if p not in holders_ok]\n    return v\n\n\ndef corpus_admitted(read):\n    """The corpus landing\'s admitted paths, from its commitment manifest as\n    `read` gives it: the committed object once that landing exists."""\n    rows = json.loads(read(CORPUS_MANIFEST))["rows"]\n    return ({CORPUS_MANIFEST, CONSTRUCTION_MANIFEST, CORPUS_RECORD}\n            | {"%s/%s.json" % (VALIDATION_HOMES[0], r["case_id"])\n               for r in rows})'),
        ('VL10',
         '        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names.\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        with self.subTest(fact="no later home, record, entry or new schema "\n                               "literal yet"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders), [])\n        with self.subTest(fact="the new schema literals live in the law and "\n                               "this module"):\n            self.assertEqual(sorted(holders), sorted([LAW, SELF_REL]))\n        planted_entry = dict(entries[-1], id="W8-D4-VCR", deliverable="W8-D4")\n        for name, args in {\n                "a tracked case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders),\n                "a record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[1], entries,\n                    holders),\n                "a premature entry": (tracked, exists,\n                                      entries + [planted_entry], holders),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD])}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))\n',
         '        # Present-state gates, each succeeded only by the later landing\n        # ADR-0060 Part J names. Succeeded at the corpus landing: the former\n        # absence stays proven at the D4-B landing commit, and the present\n        # admits exactly that landing\'s artefacts.\n        before = _git("ls-tree", "-r", "--name-only", D4B_LANDING).split()\n        before_entries = json.loads(committed(D4B_LANDING, REGISTRY))[\n            "entries"]\n        before_holders = schema_holders(\n            before, lambda p: committed(D4B_LANDING, p))\n        with self.subTest(fact="nothing later existed at the D4-B landing"):\n            self.assertEqual(staged_absence_violations(\n                before, lambda p: False, before_entries, before_holders), [])\n            self.assertEqual(sorted(before_holders), sorted([LAW, SELF_REL]))\n        tracked = _git("ls-files").split()\n        entries = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n\n        def exists(p):\n            return (ROOT / p).exists()\n\n        def read(p):\n            return (ROOT / p).read_bytes()\n        holders = schema_holders(tracked, read)\n        adds = _git("log", "--diff-filter=A", "--format=%H", "--",\n                    CORPUS_RECORD).split()\n        corpus = corpus_admitted(\n            (lambda rel: committed(adds[-1], rel)) if adds\n            else (lambda rel: _lf(read(rel))))\n        with self.subTest(fact="exactly the corpus landing\'s artefacts are "\n                               "admitted"):\n            self.assertEqual(staged_absence_violations(\n                tracked, exists, entries, holders, corpus), [])\n        with self.subTest(fact="the new schema literals live in the law, "\n                               "this module and the construction manifest"):\n            self.assertEqual(sorted(holders), sorted(\n                [LAW, SELF_REL, CONSTRUCTION_MANIFEST]))\n        planted_entry = dict(entries[-1], id="W8-D4-VSR", deliverable="W8-D4")\n        for name, args in {\n                "an unbound case file": (\n                    tracked + [VALIDATION_HOMES[0] + "/W8-C-x.json"], exists,\n                    entries, holders, corpus),\n                "a tracked register home": (\n                    tracked + [VALIDATION_HOMES[1] + "/x.json"], exists,\n                    entries, holders, corpus),\n                "a session record on disk": (\n                    tracked, lambda p: p == LATER_RECORDS[1], entries,\n                    holders, corpus),\n                "a premature session entry": (\n                    tracked, exists, entries + [planted_entry], holders,\n                    corpus),\n                "a schema literal elsewhere": (\n                    tracked, exists, entries, holders + [BOARD], corpus),\n                "the corpus artefacts without their landing": (\n                    tracked, exists, entries, holders, None)}.items():\n            with self.subTest(control="%s is refused" % name):\n                self.assertTrue(staged_absence_violations(*args))'),
    ),
}
# --------------------------------------- board and registry: authorised edits
VCR_LINK = ("([`W8-D4-validation-corpus-record.md`]"
            "(W8-D4-validation-corpus-record.md))")
VCR_STATUS_TAIL = (
    COUNT_SENTENCE + " and two class-opaque manifests, `W8-V1-CM-01` and "
    "`W8-V1-CM-02`, authored freshly under ADR-0060, with every authoring "
    "and construction record in the corpus's own custody and every "
    "commitment reproduced before landing; composition stays withheld "
    "until the corpus's own reveal.")
VCR_STATUS = {
    "draft": ("**A draft validation corpus record, `W8-D4-VCR`, is before "
              "the human reviewer** " + VCR_LINK + ": if accepted, it would "
              "publish " + VCR_STATUS_TAIL),
    "accepted": ("**`W8-D4-VCR` — the validation corpus record — is "
                 "accepted** " + VCR_LINK + " — accepted %s: it publishes "
                 + VCR_STATUS_TAIL),
}
VCR_ROW = ("| W8-D4 — Validation Corpus (record, W8-D4-VCR) | "
           "[`W8-D4-validation-corpus-record.md`]"
           "(W8-D4-validation-corpus-record.md) | ")
VCR_ROW_BODY = (
    "Tier J: **the validation corpus materialised** — " + COUNT_SENTENCE
    + " in Part C canonical bytes under evidence-derived identities and "
    "mechanical filenames, in their own home, with a class-opaque commitment "
    "manifest, `W8-V1-CM-01`, and a construction manifest, `W8-V1-CM-02`, "
    "whose acceptance this record carries; every authoring and construction "
    "record frozen once in the corpus's own custody after its durability "
    "exercise, and every commitment of both kinds reproduced from the exact "
    "retained bytes at authoring and at freeze; authored freshly under "
    "ADR-0060, with textual non-reuse proven in both directions and "
    "semantic independence never claimed; both earlier corpora and their "
    "custody untouched. The envelope case-home limb and the validation "
    "law's VL10 gates succeed at this landing. Composition withheld until "
    "the corpus's own reveal. **No packet, session, disposition, reveal, "
    "count or diagnosis; W8-D5 to W8-D7 stay closed; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = ("touches no custody and diagnoses nothing. "
                       "**No divergence is diagnosed")
BOARD_ROW_ANCHOR = vlaw.LAW_ROW_BODY + " |\n"
VCR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
VCR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRIES = (
    {"id": "W8-D4-VCR", "path": RECORD, "type": "phase-record",
     "title": "W8-D4 - Validation Corpus Record",
     "role": (
         "The record of the W8-D4 corpus landing under ADR-0060: exactly "
         "eighteen reviewer-visible validation cases in Part C canonical "
         "bytes under evidence-derived identities and mechanical filenames in "
         "their own home, a class-opaque commitment manifest and a "
         "construction manifest, whose acceptance this record carries as "
         "governed registers W8-V1-CM-01 and W8-V1-CM-02. Records the "
         "corpus custody sub-location's sentinel durability exercise before "
         "any case, nonce or retained record; authoring and construction "
         "records frozen once with exclusive create after once-only nonces; "
         "every commitment of both kinds reproduced from the exact retained "
         "bytes at authoring and at freeze; fresh authoring under ADR-0060 "
         "in a blinded authoring context, adapting no published case; textual "
         "non-reuse in both directions, never semantic independence; both "
         "earlier corpora and their custody untouched; and the reviewer's "
         "access to the visible cases at this landing beginning the conduct "
         "interval. Moves exactly the envelope V12 case-home limb and the "
         "validation law's VL10 gates by exact transformation, with proof "
         "obligations VC1 to VC13. Composition is withheld until the "
         "corpus's own reveal; no packet, session, disposition, reveal, "
         "comparison, count or diagnosis."),
     "depends_on": ["ADR-0060", "W8-D4-IVB", "ADR-0055", "ADR-0054",
                    "ADR-0058", "ADR-0059", "W8-D2-CBC", "ADR-0056", "W8-AR",
                    "W7-CR"]},
    {"id": "W8-V1-CM-01", "path": MANIFEST, "type": "governed-register",
     "title": "W8-V1 - Validation Corpus: Commitment Manifest",
     "role": (
         "The class-opaque commitment manifest of the validation corpus "
         "W8-V1: one closed two-field object under the ADR-0055 decision 28 "
         "container law as ADR-0060 decision 20 carries it, one row per "
         "validation case in lexical case identity order, each binding the "
         "case's reviewer-visible digest and its authoring commitment; it "
         "binds this corpus only. Its acceptance is carried by the record "
         "W8-D4-VCR."),
     "depends_on": ["W8-D4-VCR", "ADR-0060", "ADR-0055", "ADR-0054"]},
    {"id": "W8-V1-CM-02", "path": CMANIFEST, "type": "governed-register",
     "title": "W8-V1 - Validation Corpus: Construction Manifest",
     "role": (
         "The construction manifest of the validation corpus W8-V1 under "
         "ADR-0060 decision 19: one closed two-field object, one row per "
         "validation case in lexical case identity order, each binding the "
         "case's construction commitment, one-to-one with W8-V1-CM-01; it "
         "discloses nothing beyond the corpus size. Its acceptance is "
         "carried by the record W8-D4-VCR."),
     "depends_on": ["W8-D4-VCR", "W8-V1-CM-01", "ADR-0060", "ADR-0055"]},
)
REQUIRED_VCR = (
    "This landing publishes exactly eighteen reviewer-visible validation "
    "cases and two class-opaque manifests in the validation case home",
    "Every case passes the published envelope validator, and every identity "
    "is distinct and disjoint from every published identity of either "
    "earlier corpus.",
    "Composition is withheld until the corpus's own reveal:",
    "The corpus was authored by the authoring implementer in a separate, "
    "blinded authoring context, from the public doctrine, the accepted "
    "brief and ADR-0060 alone.",
    "Before any case, nonce or retained record existed, the corpus's own "
    "custody sub-location passed its sentinel durability exercise",
    "The location is never named in any surface.",
    "Every commitment of both kinds was reproduced by hashing the exact "
    "retained bytes directly, before any parse, twice before landing:",
    "No retained record of either earlier corpus was listed, opened, "
    "parsed, hashed, copied or moved by any act of this landing.",
    "A proof over named custody records establishes binding mechanics only;",
    "These establish textual non-reuse and distinct identities only, never "
    "semantic independence or the absence of influence",
    "it begins the conduct interval of ADR-0060 decision 27",
    "No other existing proof moves at this landing.",
    COUNT_SENTENCE,
)
CONSTRUCTION_SCHEMAS = (vlaw.CONSTRUCTION_SCHEMA,
                        vlaw.CONSTRUCTION_MANIFEST_SCHEMA)
SCHEMAS = (packet.PACKET_SCHEMA, envelope.AUTHORING_SCHEMA,
           vlaw.calibration.REGISTER_SCHEMA)


# ----------------------------------------------------------------- helpers
def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


_lf = vlaw._lf
_sha = vlaw._sha
_flat = vlaw._flat
_blob = vlaw._blob
_is = vlaw._is


def committed(commit, rel):
    return packet.committed_object_bytes(ROOT, commit, rel)


def worktree(rel, root=ROOT):
    """A candidate surface before this landing's commit exists. The twenty
    immutable corpus files under the case home are read as their raw,
    unconverted bytes, so their canonical form and every binding over them
    are proven on the bytes as written (ADR-0060 decisions 10 and 39); every
    other surface keeps its LF treatment."""
    raw = (Path(root) / rel).read_bytes()
    return raw if rel.startswith(HOME + "/") else _lf(raw)


def l7_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be BASELINE;
    afterwards it is the one commit that added the corpus record, whose sole
    parent must be BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the corpus record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel, root=ROOT):
    """The candidate bytes before the landing commit exists; afterwards the
    committed object, never a working copy, whose checkout-display
    correspondence is VC1's."""
    if commit is None:
        return worktree(rel, root)
    return packet.committed_object_bytes(root, commit, rel)


def snapshot():
    commit, problems = l7_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def manifest_rows(read):
    return json.loads(read(MANIFEST))["rows"]


def manifest_ids(read):
    return [r["case_id"] for r in manifest_rows(read)]


def case_rel(case_id):
    return "%s/%s.json" % (HOME, case_id)


def published_rows():
    rows = []
    for rel in (D2_MANIFEST, S1_MANIFEST):
        rows += json.loads(committed(BASELINE, rel))["rows"]
    return rows


def published_ids():
    return frozenset(r["case_id"] for r in published_rows())


def published_case_bytes():
    return [committed(BASELINE, "%s/%s.json" % (rel.rsplit("/", 1)[0],
                                                r["case_id"]))
            for rel in (D2_MANIFEST, S1_MANIFEST)
            for r in json.loads(committed(BASELINE, rel))["rows"]]


def home_paths(commit):
    if commit is None:
        tracked = _git("ls-files", "--", HOME + "/").split()
        home = ROOT / HOME
        on_disk = ([HOME + "/" + p.name for p in home.iterdir()]
                   if home.is_dir() else [])
        return tracked, on_disk
    tracked = _git("ls-tree", "-r", "--name-only", commit, "--",
                   HOME + "/").split()
    return tracked, tracked


def closure_from(tracked, on_disk, ids):
    expected = {MANIFEST, CMANIFEST} | {case_rel(c) for c in ids}
    v = []
    if set(tracked) != expected:
        v.append("the tracked case home differs from the closed set")
    if set(on_disk) != expected:
        v.append("the case home on disk differs from the closed set")
    if len(ids) != TOTAL or len(set(ids)) != TOTAL:
        v.append("the commitment manifest does not hold exactly eighteen "
                 "distinct rows")
    return v


def correspondence_violations(commit, ids):
    """Immutable-artefact correspondence (ADR-0057 decision 19; W8-D2-CBC):
    once committed, every corpus file at HEAD is the landing's committed
    object and every working copy equals it, line-ending display apart."""
    if commit is None:
        return []
    rels = [MANIFEST, CMANIFEST] + [case_rel(c) for c in ids]
    v = [("%s: HEAD differs from the landing's committed object" % rel)
         for rel in rels
         if _git("rev-parse", "HEAD:" + rel).strip()
         != _git("rev-parse", commit + ":" + rel).strip()]
    return v + supplement.fidelity_violations(ROOT, "HEAD", rels)


def case_violations(raw, rel):
    """One case over its exact bytes: a lawful review case, the canonical
    bytes byte for byte, mechanically named, free of packet structure."""
    try:
        case = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return ["not JSON"]
    if not isinstance(case, dict):
        return ["not a JSON object"]
    v = []
    if envelope.review_case_violations(case):
        v.append("not a lawful review case")
    if raw != envelope.canonical_bytes(case):
        v.append("not canonical bytes")
    if "%s.json" % case.get("case_id") != Path(rel).name:
        v.append("not mechanically named")
    if supplement.structural_hits(case):
        v.append("packet structure")
    return v


def commitment_manifest_violations(raw, read):
    """The commitment manifest over its exact bytes: the closed container,
    canonical bytes, the row law, eighteen rows, and each row binding its
    case's exact bytes as `read` yields them."""
    try:
        obj = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return ["not JSON"]
    if not isinstance(obj, dict) or set(obj) != {"schema", "rows"}:
        return ["outer shape"]
    v = []
    if obj["schema"] != corpus.MANIFEST_SCHEMA:
        v.append("schema")
    if raw != envelope.canonical_bytes(obj):
        v.append("not canonical bytes")
    rows = obj["rows"] if isinstance(obj["rows"], list) else []
    if envelope.manifest_violations(rows):
        v.append("row law")
    if len(rows) != TOTAL:
        v.append("not exactly eighteen rows")
    for r in rows:
        try:
            bound = r["reviewer_visible_sha256"] == envelope.sha256_bytes(
                read(case_rel(r["case_id"])))
        except (KeyError, TypeError, OSError, subprocess.CalledProcessError):
            bound = False
        if not bound:
            v.append("a row does not bind its case's exact bytes")
    return v


def candidate_copy(ws, read, rels, crlf=()):
    """Disposable copies of corpus files as `read` yields them, placed under
    a temporary root; each path in `crlf` has only its terminal line ending
    changed from LF to CRLF. Returns the candidate-reading path over that
    root - the same reader the snapshot uses before the landing commit."""
    for rel in rels:
        raw = read(rel)
        if rel in crlf:
            raw = raw[:-1] + b"\r\n"
        path = Path(ws) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    return lambda rel: snapshot_bytes(None, rel, ws)


def construction_manifest_shape_violations(raw, commitment_rows):
    """ADR-0060 decision 19 at the corpus landing: the closed two-field
    object, canonical bytes, whole-string row shapes, lexical order,
    uniqueness and one-to-one correspondence with the commitment manifest.
    The construction records themselves stay in custody; their binding is
    proven at reveal."""
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
    if obj["schema"] != vlaw.CONSTRUCTION_MANIFEST_SCHEMA:
        v.append("schema")
    rows = obj["rows"] if isinstance(obj["rows"], list) else []
    ids = []
    for r in rows:
        if not isinstance(r, dict) or set(r) != CROW_FIELDS:
            v.append("row shape")
            continue
        if not _is(envelope.CASE_ID_RE, r["case_id"]):
            v.append("row case_id shape")
            continue
        if not _is(envelope.SHA_FIELD_RE, r["construction_commitment_sha256"]):
            v.append("row commitment shape")
        ids.append(r["case_id"])
    if len(ids) != len(set(ids)):
        v.append("duplicate case_id")
    if ids != sorted(ids):
        v.append("rows not in lexical case_id order")
    bound = [r.get("case_id") for r in commitment_rows]
    if ids != bound:
        v.append("not one-to-one with the commitment manifest")
    return v


def shared_text_violations(cases):
    """The visible face of decision 14: a variant text carried by two or
    more cases is carried by at most three. Whether each such text is a
    declared family seed is proven over the revealed records at reveal."""
    carriers = {}
    for case in cases:
        for t in set(vlaw.variants(case)):
            carriers.setdefault(t, set()).add(case["case_id"])
    return ["a variant text is shared by %d cases" % len(c)
            for c in carriers.values() if len(c) > 3]


def variant_ngrams(case_bytes):
    return supplement.variant_ngrams(case_bytes)


def surfaces_text(read):
    return {"cases": " ".join(read(case_rel(c)).decode("utf-8")
                              for c in manifest_ids(read)),
            "commitment manifest": read(MANIFEST).decode("utf-8"),
            "record": read(RECORD).decode("utf-8"),
            "board wording this landing adds": added_board_wording()}


def channel_violations(text, construction_manifest_ok=False):
    v = ["a reserved label: %s" % s
         for s in corpus.reserved_channel_hits(text)]
    v += ["a token: %s" % t for t in envelope.TOKENS if t in text]
    v += ["a published schema literal: %s" % s for s in SCHEMAS if s in text]
    v += ["a method label: %s" % m for m in vlaw.ADMITS
          if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]
    v += ["a construction schema literal: %s" % s
          for s in CONSTRUCTION_SCHEMAS
          if s in text and not (construction_manifest_ok
                                and s == vlaw.CONSTRUCTION_MANIFEST_SCHEMA)]
    return v


def total_violations(ids, record, board, surfaces):
    v = []
    if len(ids) != TOTAL or len(set(ids)) != TOTAL:
        v.append("the commitment manifest does not hold exactly eighteen "
                 "distinct identities")
    for name, text in (("record", record), ("board", board)):
        if COUNT_SENTENCE not in _flat(text):
            v.append("the %s does not carry the total sentence" % name)
    for name, text in surfaces.items():
        wrong = [w for w in supplement.case_counts(text) if w != "eighteen"]
        if wrong:
            v.append("%s states another total: %s" % (name, wrong))
    return v


def succession_rows():
    """Section 4's two rows, built from the trusted site tables and pins
    alone, in their fixed order."""
    return [["`%s`" % rel, ", ".join(authority.labels(SITES[rel])),
             "`%s`" % PREIMAGE[rel][1], "`%s`" % POSTIMAGE[rel][0]]
            for rel in (ENVELOPE, LAWMOD)]


def succession_table_violations(record):
    """Section 4's succession table, read whole by the reviewed closed-table
    reader before any row is used: one contiguous block of exactly the
    header, the separator and the two trusted rows, in order. An indented,
    tab-prefixed, unpiped, surplus, duplicate, reordered or malformed row,
    an altered header or separator, or non-blank material touching either
    boundary is a violation; no row is selected by pattern."""
    rows, v = reveal.closed_table(record, SUCCESSION_SECTION,
                                  SUCCESSION_HEADER, SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows():
        v.append("the succession table is not exactly its two trusted rows, "
                 "in order")
    return v


def succession_violations(rel, present, record, sites=None):
    """The exact staged transformation of a proof module: its fixed
    pre-image under the site table yields exactly the present bytes, each
    site occurs once, the table reverses, the result is the reviewed
    post-image, and the record's closed succession table pins it."""
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
    return v + succession_table_violations(record)


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def vcr_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and VCR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (VCR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "touches no custody and diagnoses nothing. " + fill(VCR_STATUS[state])
         + " **No divergence is diagnosed"),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + VCR_ROW + fill(ROW_PREFIX[state]) + VCR_ROW_BODY
         + " |\n"),
    )


def added_board_wording():
    return " ".join([VCR_ROW, VCR_ROW_BODY] + list(VCR_STATUS.values()))


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
            + ",\n".join(authority._indent(json.dumps(e, indent=2,
                                                      ensure_ascii=False), 4)
                         for e in added)
            + "\n  ]\n}\n")


def census_line_paths(record):
    lines = [l for l in record.split("\n")
             if "**This landing's census is exactly twenty-six paths:**" in l]
    if len(lines) != 1:
        return None
    return set(re.findall(r"`([^`]+)`", lines[0]))


# ------------------------------------------------------------------ proofs
class VC1_HomeClosureAndCorrespondence(unittest.TestCase):
    def test_vc1_the_home_holds_exactly_the_corpus_at_its_landing(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        ids = manifest_ids(read)
        tracked, on_disk = home_paths(commit)
        with self.subTest(fact="the case home is exactly the corpus at this "
                               "landing"):
            self.assertEqual(closure_from(tracked, on_disk, ids), [])
        with self.subTest(fact="immutable corpus files correspond to their "
                               "committed objects"):
            self.assertEqual(correspondence_violations(commit, ids), [])
        good = {MANIFEST, CMANIFEST} | {case_rel(c) for c in ids}
        for name, (t, d, i) in {
                "an extra tracked path": (good | {HOME + "/x.json"}, good,
                                          ids),
                "an extra file on disk": (good, good | {HOME + "/y"}, ids),
                "a missing case": (good - {case_rel(ids[0])},
                                   good - {case_rel(ids[0])}, ids),
                "a missing construction manifest": (good - {CMANIFEST},
                                                    good - {CMANIFEST}, ids),
                "a seventeen-row manifest": (good, good, ids[1:])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(closure_from(t, d, i))

    def test_vc1_committed_correspondence_over_a_mechanics_fixture(self):
        """Committed-state controls over a disposable labelled sentinel
        repository: the correspondence verdict VC1 applies once committed."""
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            case, manifest = supplement._fixture_repo(ws)
            rels = [supplement.MANIFEST, case]
            with self.subTest(fact="the committed fixture corresponds"):
                self.assertEqual(supplement.fidelity_violations(
                    ws, "HEAD", rels), [])
            raw = (Path(ws) / case).read_bytes()
            (Path(ws) / case).write_bytes(raw + b" ")
            with self.subTest(control="an altered working case is refused"):
                self.assertTrue(supplement.fidelity_violations(
                    ws, "HEAD", rels))
            (Path(ws) / case).write_bytes(raw.replace(b"\n", b"\r\n"))
            with self.subTest(fact="a line-ending rewrite is display only"):
                self.assertEqual(supplement.fidelity_violations(
                    ws, "HEAD", rels), [])
            with self.subTest(fact="once committed, the canonical proof reads "
                                   "the committed object, not the display"):
                self.assertEqual(snapshot_bytes("HEAD", case, ws), raw)
                self.assertEqual(case_violations(
                    snapshot_bytes("HEAD", case, ws), case), [])


class VC2_CaseShape(unittest.TestCase):
    def test_vc2_every_case_is_lawful_byte_for_byte(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        ids = manifest_ids(read)
        bad = [cid[:16] for cid in ids
               if case_violations(read(case_rel(cid)), case_rel(cid))]
        with self.subTest(fact="all eighteen cases are lawful, canonical, "
                               "mechanically named and free of packet "
                               "structure"):
            self.assertEqual(len(ids), TOTAL)
            self.assertEqual(bad, [])
        target = case_rel(ids[0])
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            same = candidate_copy(ws, read, [target])
            with self.subTest(fact="the candidate-reading path yields the "
                                   "bytes as written"):
                self.assertEqual(same(target), read(target))
                self.assertEqual(case_violations(same(target), target), [])
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            crlf = candidate_copy(ws, read, [target], {target})
            with self.subTest(control="a case ending in CRLF is refused on the "
                                      "candidate-reading path"):
                self.assertTrue(case_violations(crlf(target), target))
        case = json.loads(read(case_rel(ids[0])))
        with self.subTest(control="a re-serialised case is refused"):
            raw = read(case_rel(ids[0]))
            self.assertNotEqual(raw, json.dumps(json.loads(raw)).encode())
        with self.subTest(control="a packet-structure line is detected"):
            planted = json.loads(json.dumps(case))
            planted["admissible_source_evidence"]["variant_a"] += (
                "\n" + packet.CASE_PREFIX + "x ====")
            self.assertTrue(supplement.structural_hits(planted))
        with self.subTest(control="an extra visible field is refused"):
            self.assertTrue(envelope.review_case_violations(
                dict(case, authored_class="A")))


class VC3_IdentityAndMembership(unittest.TestCase):
    def test_vc3_identities_are_the_manifest_and_disjoint(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        ids = manifest_ids(read)
        foreign = published_ids()
        tracked, _ = home_paths(commit)
        files = sorted(p.split("/")[-1][:-len(".json")] for p in tracked
                       if CASE_FILE.fullmatch(p.split("/")[-1]))
        with self.subTest(fact="eighteen distinct identities, the case files "
                               "exactly, none published before"):
            self.assertEqual(len(foreign), 24)
            self.assertEqual(vlaw.membership_violations(
                ids, [("case files", files)], foreign), [])
            self.assertEqual(len(set(ids)), TOTAL)
        for name, (b, steps) in {
                "a published identity": (ids[1:] + sorted(foreign)[:1],
                                         [("case files", files)]),
                "a duplicated identity": (ids[:-1] + ids[:1],
                                          [("case files", files)]),
                "a missing case file": (ids, [("case files", files[1:])]),
                "an identity followed by a newline": (
                    ids[:-1] + [ids[-1] + "\n"], [("case files", files)])
                }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(vlaw.membership_violations(b, steps, foreign))


class VC4_CommitmentManifest(unittest.TestCase):
    def test_vc4_closed_container_bound_and_distinct(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        raw = read(MANIFEST)
        obj = json.loads(raw)
        rows = obj["rows"]
        with self.subTest(fact="the closed container, canonical, ordered and "
                               "binding each case's exact bytes"):
            self.assertEqual(commitment_manifest_violations(raw, read), [])
        corpus_rels = [MANIFEST] + [case_rel(r["case_id"]) for r in rows]
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            same = candidate_copy(ws, read, corpus_rels)
            with self.subTest(fact="the candidate-reading path passes the "
                                   "bytes as written"):
                self.assertEqual(commitment_manifest_violations(
                    same(MANIFEST), same), [])
        for name, target in (("the manifest", MANIFEST),
                             ("a bound case", corpus_rels[1])):
            with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
                crlf = candidate_copy(ws, read, corpus_rels, {target})
                with self.subTest(control="%s ending in CRLF is refused on the "
                                          "candidate-reading path" % name):
                    self.assertTrue(commitment_manifest_violations(
                        crlf(MANIFEST), crlf))
        commits = [r["authoring_commitment_sha256"] for r in rows]
        visible = {r["reviewer_visible_sha256"] for r in rows}
        earlier = {r["authoring_commitment_sha256"] for r in published_rows()}
        with self.subTest(fact="commitments are whole-string, distinct and "
                               "disjoint from every digest and earlier "
                               "commitment"):
            self.assertTrue(all(_is(envelope.SHA_FIELD_RE, c)
                                for c in commits))
            self.assertEqual(len(set(commits)), TOTAL)
            self.assertEqual(set(commits) & visible, set())
            self.assertEqual(set(commits) & earlier, set())
        with self.subTest(control="reversed rows are refused"):
            self.assertTrue(envelope.manifest_violations(rows[::-1]))
        with self.subTest(control="a commitment followed by a newline is "
                                  "refused"):
            self.assertFalse(_is(envelope.SHA_FIELD_RE, commits[0] + "\n"))
        with self.subTest(control="a one-byte change to a case is detected"):
            self.assertNotEqual(rows[0]["reviewer_visible_sha256"],
                                envelope.sha256_bytes(read(case_rel(
                                    rows[0]["case_id"])) + b" "))


class VC5_ConstructionManifest(unittest.TestCase):
    def test_vc5_closed_shape_one_to_one_and_distinct(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        rows = manifest_rows(read)
        raw = read(CMANIFEST)
        with self.subTest(fact="the closed construction manifest, one-to-one "
                               "with the commitment manifest"):
            self.assertEqual(construction_manifest_shape_violations(
                raw, rows), [])
        crows = json.loads(raw)["rows"]
        ccommits = [r["construction_commitment_sha256"] for r in crows]
        others = ({r["authoring_commitment_sha256"] for r in rows}
                  | {r["reviewer_visible_sha256"] for r in rows})
        with self.subTest(fact="construction commitments are distinct and "
                               "disjoint from every other digest"):
            self.assertEqual(len(set(ccommits)), TOTAL)
            self.assertEqual(set(ccommits) & others, set())
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            same = candidate_copy(ws, read, [CMANIFEST])
            with self.subTest(fact="the candidate-reading path passes the "
                                   "bytes as written"):
                self.assertEqual(construction_manifest_shape_violations(
                    same(CMANIFEST), rows), [])
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            crlf = candidate_copy(ws, read, [CMANIFEST], {CMANIFEST})
            with self.subTest(control="the construction manifest ending in "
                                      "CRLF is refused on the "
                                      "candidate-reading path"):
                self.assertTrue(construction_manifest_shape_violations(
                    crlf(CMANIFEST), rows))
        obj = json.loads(raw)

        def canon(o):
            return envelope.canonical_bytes(o)
        for name, mutant in {
                "a missing row": canon(dict(obj, rows=crows[1:])),
                "a duplicate row": canon(dict(obj, rows=crows + crows[:1])),
                "unsorted rows": canon(dict(obj, rows=crows[::-1])),
                "an extra row field": canon(dict(obj, rows=[dict(
                    crows[0], note="x")] + crows[1:])),
                "a row identity followed by a newline": canon(dict(
                    obj, rows=[dict(crows[0], case_id=crows[0]["case_id"]
                                    + "\n")] + crows[1:])),
                "a wrong schema": canon(dict(obj, schema="w8-other-v1")),
                "non-canonical bytes": json.dumps(obj, indent=1).encode(
                    "utf-8")}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(construction_manifest_shape_violations(
                    mutant, rows))


class VC6_SharedTextBound(unittest.TestCase):
    def test_vc6_no_variant_text_carried_by_more_than_three_cases(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        cases = [json.loads(read(case_rel(c))) for c in manifest_ids(read)]
        with self.subTest(fact="shared text, if any, stays within a family "
                               "of at most three"):
            self.assertEqual(shared_text_violations(cases), [])
        seed = vlaw.SENTINEL_TEXTS[0]
        planted = [envelope.build_review_case(seed, t + " x")
                   for t in vlaw.SENTINEL_TEXTS[1:]]
        with self.subTest(control="a text carried by four cases is refused"):
            self.assertTrue(shared_text_violations(planted))


class VC7_TextualNonReuse(unittest.TestCase):
    """Textual non-reuse only, never semantic independence: at this landing,
    no ten-word sequence is shared in either direction between the
    validation corpus and any published case of either earlier corpus, and
    no validation sequence occurs in any other tracked md or json text."""

    def test_vc7_no_shared_sequence_at_this_landing(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        grams = variant_ngrams(read(case_rel(c)) for c in manifest_ids(read))
        earlier = variant_ngrams(published_case_bytes())
        self.assertTrue(grams and earlier)
        with self.subTest(fact="no sequence shared with either earlier "
                               "corpus, in either direction"):
            self.assertEqual(grams & earlier, set())
        tracked = (_git("ls-files").split() if commit is None else
                   _git("ls-tree", "-r", "--name-only", commit).split())
        others = [p for p in tracked if p.endswith((".md", ".json"))
                  and not p.startswith(HOME + "/")]
        hits = []
        for rel in others:
            try:
                words = corpus._normalise_words(read(rel).decode("utf-8"))
            except (UnicodeDecodeError, OSError,
                    subprocess.CalledProcessError):
                continue
            if grams & corpus._ngrams(words):
                hits.append(rel)
        with self.subTest(fact="no validation sequence elsewhere at this "
                               "landing"):
            self.assertEqual(hits, [])
        sample = next(iter(grams))
        with self.subTest(control="the sweep detects a real reuse"):
            self.assertIn(sample, corpus._ngrams(list(sample)))


class VC8_NoReservedChannel(unittest.TestCase):
    def test_vc8_no_label_token_schema_or_method_on_visible_surfaces(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        reg = json.loads(read(REGISTRY))
        roles = " ".join(e["role"] + " " + e["title"] for e in reg["entries"]
                         if e["id"] in {s["id"] for s in NEW_ENTRIES})
        surfaces = dict(surfaces_text(read), **{"registry roles": roles})
        for name, text in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(channel_violations(text), [])
        with self.subTest(surface="construction manifest"):
            self.assertEqual(channel_violations(
                read(CMANIFEST).decode("utf-8"),
                construction_manifest_ok=True), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([t for t in envelope.TOKENS if t in src], [])
            self.assertEqual([s for s in SCHEMAS if s in src], [])
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
        for name, plant in {
                "a reserved label": sorted(envelope.ALL_CHECKS)[0],
                "a token": sorted(envelope.TOKENS)[0],
                "a method label": sorted(vlaw.ADMITS)[0],
                "the construction schema": vlaw.CONSTRUCTION_SCHEMA}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(channel_violations("x " + plant + " y"))


class VC9_Total(unittest.TestCase):
    def test_vc9_the_stated_total_is_eighteen(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        ids = manifest_ids(read)
        record = read(RECORD).decode("utf-8")
        board = read(BOARD).decode("utf-8")
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        surfaces = {"record": record,
                    "board wording this landing adds": " ".join(
                        [VCR_ROW_BODY] + list(VCR_STATUS.values())),
                    "new registry roles": " ".join(
                        by_id[s["id"]]["role"] for s in NEW_ENTRIES)}
        self.assertEqual(total_violations(ids, record, board, surfaces), [])
        for name, args in {
                "a seventeen-identity manifest": (ids[1:], record, board,
                                                  surfaces),
                "a record without the total sentence": (
                    ids, record.replace(COUNT_SENTENCE, "the cases"), board,
                    surfaces),
                "a contradictory total in words": (
                    ids, record, board, dict(surfaces, record=record
                                             + "\nIt holds twelve cases.")),
                "a contradictory total in numerals": (
                    ids, record, board, dict(surfaces, record=record
                                             + "\nIt holds 19 validation "
                                             "cases."))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(total_violations(*args))


class VC10_RecordCarriage(unittest.TestCase):
    def test_vc10_record_carries_its_statements_and_no_exposure(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        flat = _flat(text)
        missing = [s[:44] for s in REQUIRED_VCR if flat.count(s) < 1]
        with self.subTest(fact="every required statement is carried"):
            self.assertEqual(missing, [])
        pins = [p.split(":", 1)[1] for _, p, _ in PREIMAGE.values()
                if p.startswith("sha256:")]
        pins += [POSTIMAGE[r][0].split(":", 1)[1] for r in POSTIMAGE]
        pins += [_sha(_lf(read(r))).split(":", 1)[1]
                 for r in (MANIFEST, CMANIFEST)]
        with self.subTest(fact="no identity, unpinned digest or token"):
            self.assertEqual(recovery.exposure_violations(text, pins), [])
        with self.subTest(fact="both manifest LF pins are carried"):
            for r in (MANIFEST, CMANIFEST):
                self.assertIn(_sha(_lf(read(r))), text)
        for name, plant in {"a case identity": manifest_ids(read)[0],
                            "an unpinned digest": "d" * 64}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(recovery.exposure_violations(
                    text + "\n" + plant, pins))
        with self.subTest(control="a removed statement is detected"):
            self.assertNotIn(REQUIRED_VCR[0],
                             _flat(text.replace(REQUIRED_VCR[0], "")))


class VC11_Successions(unittest.TestCase):
    def test_vc11_the_two_staged_successions_are_exact(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        record = read(RECORD).decode("utf-8")
        for rel in (ENVELOPE, LAWMOD):
            present = read(rel).decode("utf-8")
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", BASELINE + ":" + rel)
                                 .strip(), PREIMAGE[rel][2])
            with self.subTest(exact_succession=PREIMAGE[rel][0]):
                self.assertEqual(succession_violations(rel, present, record),
                                 [])
                self.assertEqual(_blob(present.encode("utf-8")),
                                 POSTIMAGE[rel][1])
        with self.subTest(fact="ADR-0060 decision 38 stages exactly these"):
            law = _flat(_lf(committed(BASELINE, LAW)).decode("utf-8"))
            self.assertIn("the envelope module's case-home limb admits "
                          "exactly the validation case home beside its three "
                          "existing homes, its vacancy limb unchanged", law)
            self.assertIn("this record's VL10 gates admit exactly the case "
                          "home, the two manifests, the corpus record and "
                          "the three W8-D4 entries that landing adds", law)
        present = read(ENVELOPE).decode("utf-8")
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, ()),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[ENVELOPE] + (("V12", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(ENVELOPE, text, record,
                                                      table))
        with self.subTest(control="a record row with a wrong pin is refused"):
            wrong = record.replace(POSTIMAGE[LAWMOD][0],
                                   "sha256:" + "0" * 64, 1)
            self.assertTrue(succession_violations(
                LAWMOD, read(LAWMOD).decode("utf-8"), wrong))
        with self.subTest(fact="section 4's table is exactly its trusted "
                               "lines, read whole"):
            self.assertEqual(succession_table_violations(record), [])
        first, last = ("| " + " | ".join(r) + " |" for r in succession_rows())
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        lawmod = read(LAWMOD).decode("utf-8")
        for name, mutated in (
                ("a space-prefixed duplicate row", record.replace(
                    last + "\n", last + "\n " + last + "\n", 1)),
                ("a tab-prefixed duplicate row", record.replace(
                    last + "\n", last + "\n\t" + last + "\n", 1)),
                ("an exact duplicate row", record.replace(
                    last + "\n", last + "\n" + last + "\n", 1)),
                ("a row with no opening pipe", record.replace(
                    last, last[2:], 1)),
                ("a row with a fifth cell", record.replace(
                    last, last[:-2] + " | mechanics sentinel |", 1)),
                ("a dropped row", record.replace(last + "\n", "", 1)),
                ("reversed rows", record.replace(
                    first + "\n" + last + "\n", last + "\n" + first + "\n",
                    1)),
                ("an altered header", record.replace(
                    top, SUCCESSION_HEADER + " Note |\n"
                    + SUCCESSION_SEPARATOR + "\n", 1)),
                ("an altered separator", record.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the top", record.replace(
                    top, "mechanics sentinel\n" + top, 1)),
                ("delimiter-free material touching the bottom",
                 record.replace(last + "\n",
                                last + "\nmechanics sentinel\n", 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated))
                self.assertTrue(succession_violations(LAWMOD, lawmod,
                                                      mutated))
        for name, mutated in reveal.boundary_mutants(
                record, SUCCESSION_SECTION, last).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated))


class VC12_RegistryAndBoard(unittest.TestCase):
    def test_vc12_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        state, date, v = vcr_state(read(RECORD).decode("utf-8"))
        self.assertEqual(v, [])
        board_pre = _lf(committed(BASELINE, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(BASELINE, REGISTRY)).decode("utf-8")
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")
        expected, problems = authority.apply_sites(board_pre,
                                                   board_sites(state, date))
        with self.subTest(fact="exact authorised board", state=state):
            self.assertEqual(problems, [])
            self.assertEqual(board, expected)
            self.assertIn(recovery.R9_REVEAL, board)
        hashes = {rel: _sha(_lf(read(rel))) for rel in (RECORD, MANIFEST,
                                                         CMANIFEST)}
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, hashes, state,
                                                    date))
        by_id = {e["id"]: e for e in json.loads(reg)["entries"]}
        for spec in NEW_ENTRIES:
            e = by_id.get(spec["id"])
            with self.subTest(entry=spec["id"]):
                self.assertIsNotNone(e)
                self.assertEqual((e["path"], e["type"], e["phase"],
                                  e["deliverable"]),
                                 (spec["path"], spec["type"], "W8", "W8-D4"))
                self.assertEqual((e["status"], e["accepted_date"]),
                                 (state, date))
                if commit is None:
                    self.assertEqual(e["content_hash"],
                                     lf_hash(ROOT / e["path"]))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, hashes, other, "2000-01-01"))
            wrong, _ = authority.apply_sites(board_pre,
                                             board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)


class VC13_Census(unittest.TestCase):
    def test_vc13_census_is_exactly_twenty_six_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        ids = manifest_ids(read)
        expected = set(FIXED_CENSUS) | {case_rel(c) for c in ids}
        with self.subTest(fact="the census is exactly twenty-six paths"):
            self.assertEqual(len(FIXED_CENSUS), 8)
            self.assertEqual(len(expected), 26)
            self.assertEqual(paths, expected)
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {ENVELOPE, LAWMOD, SELF_REL})
        named = census_line_paths(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            self.assertIsNotNone(named)
            self.assertEqual(named - {HOME + "/W8-C-<64-hex>.json"},
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {"docs/x.md"},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, expected)


if __name__ == "__main__":
    unittest.main()
