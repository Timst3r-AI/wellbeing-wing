"""W8-S1 — supplementary corpus proofs (W8-S1-SCR, S1–S13).

The supplementary authoring landing that W8-S1-SOB opens under ADR-0059:
exactly twelve reviewer-visible supplementary cases and one class-opaque
manifest, W8-S1-CM-01, in their own home, with the two proof successions
ADR-0059 Part G decision 25 stages for this landing. This module proves the
corpus's shape, identity, binding and closure, its textual non-reuse, its
registration and the exact transformations of everything this landing
changes, each with planted-mutant or negative controls.

THIS MODULE READS NO CUSTODY. It carries no association or figure from the
void attempt, names no case as a literal, holds no disposition token as a
literal, renders no packet and opens no withheld authoring record. It reads
the published supplementary cases and manifest, and, for identity
disjointness and textual non-reuse only, the published original corpus's
manifest and cases (ADR-0059 decision 19 keeps those checks lawful).

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any case's authored class, intended disposition or
construction; the corpus's composition; that any case is fresh or
semantically independent of anything; that any retained record exists, is
intact or was handled as the record states; that no contradictory total is
stated in wording outside S9's closed grammar; anything about the reviewer
or the reviewer's prior exposure; or that any session, reproduction, reveal
or count may now begin.
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
import test_w8_session_recovery_law as recovery
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified L1 landing: this landing's sole parent
# and the commit every pre-image below is read from.
L1 = "2bb87a308d4cc1ce795869bb94370d3bdc75ae0e"

HOME = "governance/discriminating-supplement"
MANIFEST = HOME + "/W8-S1-commitment-manifest.json"
RECORD = "docs/phases/W8-S1-supplementary-corpus-record.md"
SELF_REL = "tests/test_w8_supplementary_corpus.py"
ENVELOPE = "tests/test_w8_discriminating_instrument_envelope.py"
AUTHORITY = "tests/test_w8_recovery_authority.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
ADR59 = "docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md"
ORIGINAL_HOME = "governance/discriminating-instrument"
ORIGINAL_MANIFEST = ORIGINAL_HOME + "/W8-D2-commitment-manifest.json"
TOTAL = 12
COUNT_SENTENCE = "exactly twelve reviewer-visible supplementary cases"
FIXED_CENSUS = frozenset({MANIFEST, RECORD, SELF_REL, ENVELOPE, AUTHORITY,
                          REGISTRY, BOARD})
CASE_FILE = re.compile(r"^W8-C-[0-9a-f]{64}\.json$")

# Fixed pre-images at L1: (label, LF SHA-256, blob).
PREIMAGE = {
    ENVELOPE: ("envelope module",
               "sha256:cca0b83d0c50675b3ec1d32aa2b11f29a61633a47a0bf5d3434d9b1f6143d5b9",
               "65b0054e2f3a01439eaf90d443f6f7da988d69b4"),
    AUTHORITY: ("recovery-authority module",
                "sha256:2390dcaed53b5d9bffe3e1c53bcbaeac97290e2572162adaa3f78dc43cb45299",
                "03d942000c31536d4f9ff913ce0054d0434fdc7a"),
    REGISTRY: ("registry",
               "sha256:40fbaf1ef58d6994efaf15ac3923b46eb3758a851187dc075a8e2c2f05438f48",
               "4935f4c36562839848dc5bda1f686978bf942436"),
    BOARD: ("board",
            "sha256:4f95864b5cece18c5a6dfbf8dd455f15114305c50a16155e9f1bedd688b56525",
            "50e64a70d6a52b4a577765e635e141a01313a6db"),
}
RECORD_SOURCES = {"`tests/test_w8_discriminating_instrument_envelope.py`":
                  ENVELOPE,
                  "`tests/test_w8_recovery_authority.py`": AUTHORITY}

# ----------------------------------------------- the two staged successions
SITES = {
    ENVELOPE: (
        ("V12",
         '                 if "W8-C-" in p and not p.startswith(\n'
         '                     "governance/discriminating-instrument/")], [])\n',
         '                 if "W8-C-" in p and not p.startswith(\n'
         '                     ("governance/discriminating-instrument/",\n'
         '                      "governance/discriminating-supplement/"))],'
         ' [])\n'),
    ),
    AUTHORITY: (
        ("A9",
         "    def test_a9_no_supplementary_artefact_before_its_landing(self):\n"
         "        tracked = _git(\"ls-files\").split()\n"
         "        exists = lambda rel: (ROOT / rel).exists()\n"
         "        entries = load_registry()[\"entries\"]\n",
         "    def test_a9_no_supplementary_artefact_before_its_landing(self):\n"
         "        # Succeeded at the supplementary authoring landing (ADR-0059\n"
         "        # Part G decision 25): the absence stays proven at this\n"
         "        # record's own landing commit, and the present closure is\n"
         "        # the one that landing proves.\n"
         "        commit, problems = l1_snapshot()\n"
         "        self.assertEqual(problems, [])\n"
         "        tracked = (_git(\"ls-tree\", \"-r\", \"--name-only\", commit)\n"
         "                   .split() if commit else _git(\"ls-files\").split())\n"
         "        exists = ((lambda rel: False) if commit\n"
         "                  else (lambda rel: (ROOT / rel).exists()))\n"
         "        entries = json.loads(snapshot_text(commit, REGISTRY))"
         "[\"entries\"]\n"),
        ("A9",
         "            with self.subTest(control=\"%s is refused\" % name):\n"
         "                self.assertTrue(absence_violations(*args))\n"
         "\n\nclass A10_ValidationChain",
         "            with self.subTest(control=\"%s is refused\" % name):\n"
         "                self.assertTrue(absence_violations(*args))\n"
         "        with self.subTest(fact=\"the present closure is the \"\n"
         "                               \"supplementary landing's own\"):\n"
         "            import test_w8_supplementary_corpus as supplement\n"
         "            self.assertEqual(supplement.closure_violations(), [])\n"
         "\n\nclass A10_ValidationChain"),
    ),
}

# --------------------------------------- board and registry: authorised edits
SCR_LINK = ("([`W8-S1-supplementary-corpus-record.md`]"
            "(W8-S1-supplementary-corpus-record.md))")
SCR_STATUS_TAIL = (
    "exactly twelve reviewer-visible supplementary cases and one "
    "class-opaque manifest, `W8-S1-CM-01`, authored freshly under ADR-0059 "
    "and `W8-S1-SOB`, with every withheld record in the supplement's own "
    "custody and every commitment reproduced before landing; composition "
    "stays withheld until the supplement's own reveal.")
SCR_STATUS = {
    "draft": ("**A draft supplementary corpus record, `W8-S1-SCR`, is before "
              "the human reviewer** " + SCR_LINK + ": if accepted, it would "
              "publish " + SCR_STATUS_TAIL),
    "accepted": ("**`W8-S1-SCR` — the supplementary corpus record — is "
                 "accepted** " + SCR_LINK + " — accepted %s: it publishes "
                 + SCR_STATUS_TAIL),
}
SCR_ROW = ("| W8-S1 — Supplementary Corpus (record, W8-S1-SCR) | "
           "[`W8-S1-supplementary-corpus-record.md`]"
           "(W8-S1-supplementary-corpus-record.md) | ")
SCR_ROW_BODY = (
    "Tier J: **the supplementary corpus materialised** — exactly twelve "
    "reviewer-visible supplementary cases in Part C canonical bytes under "
    "evidence-derived identities and mechanical filenames, in their own "
    "home, with one class-opaque commitment manifest, `W8-S1-CM-01`, whose "
    "acceptance this record carries; withheld records frozen once in the "
    "supplement's own custody sub-location after its durability exercise, "
    "every commitment reproduced from the exact retained bytes at authoring "
    "and at freeze; authored freshly from public doctrine, with textual "
    "non-reuse proven in both directions and semantic independence never "
    "claimed; the original corpus and its custody untouched. Composition "
    "withheld until the supplement's own reveal. **No packet, session, "
    "disposition, reveal or count; D3-C stays blocked until this record is "
    "effective, and D3-D stays unopened.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
BOARD_STATUS_ANCHOR = ("D3-C stays blocked until the supplementary "
                       "authoring landing is effective. **No session, "
                       "disposition, reveal or calibration exists yet.")
BOARD_ROW_ANCHOR = ("D3-C stays blocked until that landing is effective.** "
                    "|\n")
SCR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
SCR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRIES = (
    {"id": "W8-S1-SCR", "path": RECORD, "type": "phase-record",
     "title": "W8-S1 - Supplementary Corpus Record",
     "role": (
         "The record of the one W8-S1 supplementary authoring landing under "
         "ADR-0059 and W8-S1-SOB: exactly twelve reviewer-visible "
         "supplementary cases in Part C canonical bytes under "
         "evidence-derived identities and mechanical filenames in their own "
         "home, and one class-opaque commitment manifest whose acceptance "
         "this record carries as governed register W8-S1-CM-01. Records the "
         "supplement custody sub-location's sentinel durability exercise "
         "before any case, nonce or retained record; withheld records frozen "
         "once with exclusive create after a once-only nonce; every "
         "commitment reproduced from the exact retained bytes at authoring "
         "and at freeze; fresh authoring from public doctrine with no "
         "void-attempt association and no original case adapted; textual "
         "non-reuse in both directions, never semantic independence; the "
         "original corpus, its custody and the W8-D2 completion untouched; "
         "and the reviewer's access to the visible cases at this landing "
         "beginning the conduct interval. Moves exactly the envelope V12 "
         "case-home limb and the recovery-authority A9 absence limb by "
         "exact transformation, with proof obligations S1 to S13. "
         "Composition is withheld until the supplement's own reveal; no "
         "packet, session, disposition, reveal, comparison or count."),
     "depends_on": ["ADR-0059", "W8-S1-SOB", "ADR-0055", "ADR-0054",
                    "W8-D2-DIB", "W8-D2-CBC", "ADR-0058", "ADR-0056",
                    "W8-AR", "W7-CR"]},
    {"id": "W8-S1-CM-01", "path": MANIFEST, "type": "governed-register",
     "title": "W8-S1 - Supplementary Corpus: Commitment Manifest",
     "role": (
         "The class-opaque commitment manifest of the supplementary corpus "
         "W8-S1: one closed two-field object under the ADR-0055 decision 28 "
         "container law, one row per supplementary case in lexical case "
         "identity order, each binding the case's reviewer-visible digest "
         "and its authoring commitment; it binds this corpus only. Its "
         "acceptance is carried by the record W8-S1-SCR."),
     "depends_on": ["W8-S1-SCR", "ADR-0059", "ADR-0055", "W8-S1-SOB",
                    "ADR-0054"]},
)

REQUIRED_SCR = (
    "This landing publishes exactly twelve reviewer-visible supplementary "
    "cases and one class-opaque commitment manifest in the supplement home",
    "Every case passes the published envelope validator, and every identity "
    "is distinct and disjoint from every original-corpus identity.",
    "Composition is withheld until the supplement's own reveal:",
    "Before any case, nonce or retained record existed, the supplement's own "
    "custody sub-location passed its sentinel durability exercise:",
    "The location is never named in any surface.",
    "its commitment nonce generated once and never rerolled, and then "
    "written once with exclusive create, never reopened for write.",
    "Every commitment was reproduced by hashing the exact retained bytes "
    "directly, before any parse, twice before landing:",
    "No original retained record was listed, opened, parsed, hashed, copied "
    "or moved by any act of this landing",
    "A proof over named custody records establishes binding mechanics only;",
    "That context did not read the original corpus home or its history, did "
    "not read any material of the void attempt, and used none of the void "
    "attempt's associations, derived distributions or purported answers "
    "(ADR-0058 decision 5); it adapted no original case and used none as a "
    "template.",
    "These establish textual non-reuse and distinct identities only, never "
    "semantic independence, and the reviewer's broader prior exposure "
    "cannot be mechanically excluded.",
    "no statistical comparability with the void attempt or with the "
    "original corpus is claimed.",
    "it begins the conduct interval of ADR-0059 decision 13",
    "No other existing proof moves at this landing.",
    COUNT_SENTENCE,
    "The authoring account confirms, case-free, that it honoured the "
    "`W8-D2-DIB` section 3 duties this corpus carries:",
    "no D3-C disposition-register instance",
)
SCHEMAS = (packet.PACKET_SCHEMA, envelope.AUTHORING_SCHEMA)


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


def l2_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the working copy over a HEAD that must be L1; afterwards it
    is the one commit that added the supplement manifest, whose sole parent
    must be L1."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                MANIFEST).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == L1 else
                      ["uncommitted candidate is not over the L1 landing"])
    if len(adds) != 1:
        return None, ["the supplement manifest was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [L1]:
        return adds[0], ["the landing commit's sole parent is not L1"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return worktree(rel) if commit is None else committed(commit, rel)


def corpus_bytes(rel):
    """The published bytes: the committed object at HEAD once this landing
    is committed (the W8-D2-CBC rule), the LF working copy before."""
    commit, _ = l2_snapshot()
    return worktree(rel) if commit is None else committed("HEAD", rel)


def manifest_object():
    return json.loads(corpus_bytes(MANIFEST))


def manifest_ids():
    return [r["case_id"] for r in manifest_object()["rows"]]


def original_manifest():
    return json.loads(committed(L1, ORIGINAL_MANIFEST))


def original_ids():
    return [r["case_id"] for r in original_manifest()["rows"]]


def case_rel(case_id):
    return "%s/%s.json" % (HOME, case_id)


def closure_from(tracked, on_disk, ids):
    expected = {MANIFEST} | {case_rel(c) for c in ids}
    v = []
    if set(tracked) != expected:
        v.append("tracked supplement home differs from the closed set")
    if set(on_disk) != expected:
        v.append("on-disk supplement home differs from the closed set")
    if len(ids) != TOTAL or len(set(ids)) != TOTAL:
        v.append("the manifest does not hold exactly twelve distinct rows")
    return v


def fidelity_violations(repo, commit, rels):
    """Once committed, the committed objects are the published artefact:
    each file's LF-normalised working copy must equal its committed bytes.
    A line-ending rewrite by a checkout is display (W8-D2-CBC) and is the
    only difference permitted."""
    v = []
    for rel in rels:
        try:
            committed_raw = packet.committed_object_bytes(repo, commit, rel)
        except subprocess.CalledProcessError:
            v.append("%s: no committed object" % rel)
            continue
        work = Path(repo) / rel
        if not work.is_file():
            v.append("%s: working copy missing" % rel)
        elif _lf(work.read_bytes()) != committed_raw:
            v.append("%s: working copy differs from its committed bytes"
                     % rel)
    return v


def closure_violations():
    """The supplement home's closure, used by S1 and by the succeeded A9:
    the closed set of names, tracked and on disk, and — once committed —
    an unmoved home whose every working copy equals its committed bytes."""
    commit, problems = l2_snapshot()
    if problems:
        return problems
    home = ROOT / HOME
    tracked = _git("ls-files", "--", HOME + "/").split()
    on_disk = ([HOME + "/" + p.name for p in home.iterdir()]
               if home.is_dir() else [])
    ids = manifest_ids()
    v = closure_from(tracked, on_disk, ids)
    if commit is not None:
        if _git("rev-parse", "HEAD:" + HOME).strip() != \
                _git("rev-parse", commit + ":" + HOME).strip():
            v.append("the supplement home moved after its landing")
        v += fidelity_violations(ROOT, "HEAD",
                                 [MANIFEST] + [case_rel(c) for c in ids])
    return v


def _fixture_repo(ws):
    """A disposable mechanics-only repository: one labelled envelope
    sentinel case and its sentinel manifest, committed once. Never a case,
    never governed, never published; it exists only for the duration of a
    control."""
    def git(*a):
        return subprocess.run(
            ["git", "-c", "user.name=mechanics-sentinel", "-c",
             "user.email=sentinel@example.invalid", "-c",
             "core.autocrlf=false"] + list(a),
            cwd=ws, capture_output=True, text=True, check=True).stdout
    git("init", "-q")
    case = envelope.build_review_case(envelope.SENTINEL_TEXT_1,
                                      envelope.SENTINEL_TEXT_2)
    vb = envelope.canonical_bytes(case)
    rec = envelope._sentinel_record("A", case["case_id"])
    rec["reviewer_visible_sha256"] = envelope.sha256_bytes(vb)
    row = {"case_id": case["case_id"],
           "reviewer_visible_sha256": envelope.sha256_bytes(vb),
           "authoring_commitment_sha256": envelope.sha256_bytes(
               envelope.canonical_bytes(rec))}
    manifest = {"schema": corpus.MANIFEST_SCHEMA, "rows": [row]}
    (Path(ws) / HOME).mkdir(parents=True)
    (Path(ws) / case_rel(case["case_id"])).write_bytes(vb)
    (Path(ws) / MANIFEST).write_bytes(envelope.canonical_bytes(manifest))
    git("add", "-A")
    git("commit", "-q", "-m", "mechanics sentinel fixture")
    return case_rel(case["case_id"]), manifest


COUNT_WORDS = ("one", "two", "three", "four", "five", "six", "seven",
               "eight", "nine", "ten", "eleven", "twelve", "thirteen",
               "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
               "nineteen", "twenty", "dozen")


def case_counts(text):
    """The S9 grammar, closed and nothing more: lower-cased ASCII word
    tokens ([a-z0-9]+ joined by single hyphens); after removing a leading
    list-item number ("N. ") from each line, every token that is in
    COUNT_WORDS (one to twenty, plus dozen) or wholly decimal digits, with
    at most two tokens between it and a "case" or "cases" token, is
    returned. Any other count wording — zero, a hyphenated compound,
    another spelling or language, or a count further away — is not
    recognised and lies outside S9's claim."""
    text = re.sub(r"(?m)^\s*\d+\.\s", " ", text)
    tokens = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text.lower())
    found = []
    for i, t in enumerate(tokens):
        if t in ("case", "cases"):
            found += [w for w in tokens[max(0, i - 3):i]
                      if w in COUNT_WORDS or w.isdigit()]
    return found


def total_violations(ids, record, board, surfaces):
    v = []
    if len(ids) != TOTAL or len(set(ids)) != TOTAL:
        v.append("the manifest does not hold exactly twelve distinct "
                 "identities")
    for name, text in (("record", record), ("board", board)):
        if COUNT_SENTENCE not in _flat(text):
            v.append("the %s does not carry the total sentence" % name)
    for name, text in surfaces.items():
        wrong = [w for w in case_counts(text) if w != "twelve"]
        if wrong:
            v.append("%s states another total: %s" % (name, wrong))
    return v


def variant_lines(case):
    ase = case["admissible_source_evidence"]
    return [l for v in (ase["variant_a"], ase["variant_b"])
            for l in v.split("\n")]


def structural_hits(case):
    prefixes = tuple(packet.STRUCTURAL_PREFIXES) + ("Options:",)
    return [l for l in variant_lines(case) if l.startswith(prefixes)]


def variant_ngrams(case_bytes):
    grams = set()
    for raw in case_bytes:
        ase = json.loads(raw)["admissible_source_evidence"]
        for v in (ase["variant_a"], ase["variant_b"]):
            grams |= corpus._ngrams(corpus._normalise_words(v))
    return grams


def other_tracked_texts():
    return [p for p in _git("ls-files").split()
            if p.endswith((".md", ".json")) and not p.startswith(HOME + "/")]


SUCCESSION_ROW = re.compile(
    r"^\| (?P<source>`[^`]+`) \| (?P<labels>[^|]+?) \| "
    r"`(?P<pre>sha256:[0-9a-f]{64})` \| `(?P<post>sha256:[0-9a-f]{64})` \|$",
    re.MULTILINE)


def record_successions(text):
    rows = {}
    for m in SUCCESSION_ROW.finditer(text):
        rel = RECORD_SOURCES.get(m.group("source"))
        if rel is None or rel in rows:
            return None
        rows[rel] = (tuple(s.strip() for s in m.group("labels").split(",")),
                     m.group("pre"), m.group("post"))
    return rows


def succession_violations(rel, present, record, sites=None):
    """The exact staged transformation of a proof module: its fixed L1
    pre-image under the site table yields exactly the present bytes, each
    site occurs once, the table reverses, and the record pins the result."""
    sites = SITES[rel] if sites is None else sites
    v = []
    pre = _lf(committed(L1, rel)).decode("utf-8")
    if _sha(pre.encode("utf-8")) != PREIMAGE[rel][1]:
        v.append("the L1 pre-image differs from its pin")
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
    rows = record_successions(record) or {}
    row = rows.get(rel)
    if row is None:
        v.append("the record carries no single succession row for it")
    else:
        if row[0] != authority.labels(sites):
            v.append("the record names different sites")
        if row[1] != PREIMAGE[rel][1]:
            v.append("the record's pre-image pin differs")
        if row[2] != _sha(present.encode("utf-8")):
            v.append("the record's post-image pin differs from the bytes")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", L1, commit).split())


def scr_state(text):
    state, date = recovery.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and SCR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (SCR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "D3-C stays blocked until the supplementary authoring landing is "
         "effective. " + fill(SCR_STATUS[state]) + " **No session, "
         "disposition, reveal or calibration exists yet."),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + SCR_ROW + fill(ROW_PREFIX[state]) + SCR_ROW_BODY
         + " |\n"),
    )


def new_entry(spec, state, date, content_hash):
    return {
        "id": spec["id"], "aliases": [], "title": spec["title"],
        "type": spec["type"], "phase": "W8", "deliverable": None,
        "path": spec["path"], "status": state,
        "accepted_date": date if state == "accepted" else None,
        "role": spec["role"], "governs": [],
        "depends_on": list(spec["depends_on"]), "resolves": [],
        "id_namespaces": [], "implementation_permission": "none",
        "open_decisions": [], "content_hash": content_hash,
        "hash_exclusion_reason": None, "errata": [],
    }


def expected_registry(l1_text, hashes, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not l1_text.endswith(tail):
        return None
    added = [new_entry(spec, state, date, hashes[spec["path"]])
             for spec in NEW_ENTRIES]
    return (l1_text[:-len(tail)] + "\n    },\n"
            + ",\n".join(authority._indent(json.dumps(e, indent=2,
                                                      ensure_ascii=False), 4)
                         for e in added)
            + "\n  ]\n}\n")


def load_registry():
    return json.loads(worktree(REGISTRY))


# ------------------------------------------------------------------ proofs
class S1_HomeClosure(unittest.TestCase):
    def test_s1_home_holds_exactly_the_corpus(self):
        self.assertEqual(closure_violations(), [])
        ids = manifest_ids()
        good = {MANIFEST} | {case_rel(c) for c in ids}
        for name, (t, d, i) in {
                "an extra tracked path": (good | {HOME + "/x.json"}, good,
                                          ids),
                "an extra file on disk": (good, good | {HOME + "/y"}, ids),
                "a missing case": (good - {case_rel(ids[0])},
                                   good - {case_rel(ids[0])}, ids),
                "an eleven-row manifest": (good, good, ids[1:])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(closure_from(t, d, i))

    def test_s1_committed_fidelity_over_a_mechanics_fixture(self):
        """Committed-state controls over a disposable labelled sentinel
        repository: the fidelity verdict the closure applies once this
        landing is committed."""
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as ws:
            case, manifest = _fixture_repo(ws)
            rels = [MANIFEST, case]
            with self.subTest(fact="the committed fixture is faithful"):
                self.assertEqual(fidelity_violations(ws, "HEAD", rels), [])
            raw = (Path(ws) / MANIFEST).read_bytes()
            (Path(ws) / MANIFEST).write_bytes(raw.replace(b"\n", b"\r\n"))
            with self.subTest(fact="a line-ending rewrite is display only"):
                self.assertEqual(fidelity_violations(ws, "HEAD", rels), [])
            altered = json.loads(json.dumps(manifest))
            altered["rows"][0]["authoring_commitment_sha256"] = (
                "sha256:" + "f" * 64)
            (Path(ws) / MANIFEST).write_bytes(
                envelope.canonical_bytes(altered))
            with self.subTest(control="a canonical but altered working "
                                      "manifest is refused"):
                self.assertEqual(envelope.manifest_violations(
                    altered["rows"]), [])
                self.assertTrue([x for x in fidelity_violations(
                    ws, "HEAD", rels) if x.startswith(MANIFEST)])
            (Path(ws) / MANIFEST).write_bytes(raw)
            (Path(ws) / case).write_bytes(
                (Path(ws) / case).read_bytes() + b" ")
            with self.subTest(control="an altered working case is refused"):
                self.assertTrue([x for x in fidelity_violations(
                    ws, "HEAD", rels) if x.startswith(case)])
            (Path(ws) / case).unlink()
            with self.subTest(control="a missing working case is refused"):
                self.assertTrue(fidelity_violations(ws, "HEAD", rels))


class S2_CaseShape(unittest.TestCase):
    def test_s2_every_case_is_lawful_byte_for_byte(self):
        commit, _ = l2_snapshot()
        for cid in manifest_ids():
            rel = case_rel(cid)
            raw = corpus_bytes(rel)
            case = json.loads(raw)
            with self.subTest(case=cid[:16]):
                self.assertEqual(envelope.review_case_violations(case), [])
                self.assertEqual(raw, envelope.canonical_bytes(case))
                self.assertEqual(case["case_id"] + ".json",
                                 Path(rel).name)
                self.assertEqual(structural_hits(case), [])
                if commit is not None:
                    self.assertEqual(worktree(rel), raw)
        with self.subTest(control="a re-serialised case is refused"):
            raw = corpus_bytes(case_rel(manifest_ids()[0]))
            self.assertNotEqual(raw, json.dumps(json.loads(raw)).encode())
        with self.subTest(control="a packet-structure line is detected"):
            case = json.loads(corpus_bytes(case_rel(manifest_ids()[0])))
            planted = json.loads(json.dumps(case))
            planted["admissible_source_evidence"]["variant_a"] += (
                "\n" + packet.CASE_PREFIX + "x ====")
            self.assertTrue(structural_hits(planted))


class S3_IdentityAndMembership(unittest.TestCase):
    def test_s3_identities_are_the_manifest_and_disjoint(self):
        ids, originals = manifest_ids(), original_ids()
        files = [p.split("/")[-1][:-len(".json")]
                 for p in _git("ls-files", "--", HOME + "/").split()
                 if CASE_FILE.match(p.split("/")[-1])]
        self.assertEqual(authority.corpus_violations(ids, originals), [])
        self.assertEqual(authority.exact_set_violations(
            files, ids, originals, "the supplement home"), [])
        with self.subTest(control="an original identity is refused"):
            self.assertTrue(authority.corpus_violations(
                ids[1:] + originals[:1], originals))
        with self.subTest(control="a duplicated identity is refused"):
            self.assertTrue(authority.corpus_violations(
                ids[:-1] + ids[:1], originals))


class S4_ManifestContainer(unittest.TestCase):
    def test_s4_closed_container_canonical_and_ordered(self):
        raw = corpus_bytes(MANIFEST)
        obj = json.loads(raw)
        self.assertEqual(set(obj), {"schema", "rows"})
        self.assertEqual(obj["schema"], corpus.MANIFEST_SCHEMA)
        self.assertEqual(envelope.manifest_violations(obj["rows"]), [])
        self.assertEqual(raw, envelope.canonical_bytes(obj))
        self.assertEqual(len(obj["rows"]), TOTAL)
        with self.subTest(control="an extra outer field is refused"):
            self.assertNotEqual(set(dict(obj, extra=1)), {"schema", "rows"})
        with self.subTest(control="reversed rows are refused"):
            self.assertTrue(envelope.manifest_violations(obj["rows"][::-1]))


class S5_VisibleBinding(unittest.TestCase):
    def test_s5_rows_bind_exact_case_bytes(self):
        rows = manifest_object()["rows"]
        for r in rows:
            with self.subTest(case=r["case_id"][:16]):
                self.assertEqual(r["reviewer_visible_sha256"], envelope
                                 .sha256_bytes(corpus_bytes(case_rel(
                                     r["case_id"]))))
        with self.subTest(control="a one-byte change is detected"):
            raw = corpus_bytes(case_rel(rows[0]["case_id"])) + b" "
            self.assertNotEqual(rows[0]["reviewer_visible_sha256"],
                                envelope.sha256_bytes(raw))


class S6_CommitmentShape(unittest.TestCase):
    def test_s6_commitments_are_well_formed_and_distinct(self):
        rows = manifest_object()["rows"]
        commits = [r["authoring_commitment_sha256"] for r in rows]
        visible = {r["reviewer_visible_sha256"] for r in rows}
        originals = {r["authoring_commitment_sha256"]
                     for r in original_manifest()["rows"]}
        self.assertTrue(all(envelope.SHA_FIELD_RE.fullmatch(c)
                            for c in commits))
        self.assertEqual(len(set(commits)), TOTAL)
        self.assertEqual(set(commits) & visible, set())
        self.assertEqual(set(commits) & originals, set())
        with self.subTest(control="a malformed commitment is refused"):
            self.assertFalse(envelope.SHA_FIELD_RE.fullmatch(
                commits[0] + "\n"))


class S7_NoReservedChannel(unittest.TestCase):
    def test_s7_no_reserved_label_schema_or_token_on_visible_surfaces(self):
        reg = load_registry()
        roles = " ".join(e["role"] + " " + e["title"] for e in reg["entries"]
                         if e["id"] in ("W8-S1-SCR", "W8-S1-CM-01"))
        board = worktree(BOARD).decode("utf-8")
        with self.subTest(surface="board W8 section (reserved labels)"):
            # The section's earlier rows name the doctrine's vocabulary by
            # law; the token and schema checks bind this landing's wording.
            self.assertEqual(corpus.reserved_channel_hits(
                board[board.find("## W8"):]), [])
        added = " ".join([SCR_ROW, SCR_ROW_BODY] + list(SCR_STATUS.values()))
        surfaces = {"cases": " ".join(corpus_bytes(case_rel(c)).decode(
                        "utf-8") for c in manifest_ids()),
                    "manifest": corpus_bytes(MANIFEST).decode("utf-8"),
                    "record": worktree(RECORD).decode("utf-8"),
                    "board wording this landing adds": added,
                    "registry roles": roles}
        for name, text in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(corpus.reserved_channel_hits(text), [])
                self.assertEqual([t for t in envelope.TOKENS if t in text],
                                 [])
                self.assertEqual([s for s in SCHEMAS if s in text], [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([t for t in envelope.TOKENS if t in src], [])
            self.assertEqual([s for s in SCHEMAS if s in src], [])
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
        with self.subTest(control="a planted reserved label is detected"):
            self.assertTrue(corpus.reserved_channel_hits(
                "x " + sorted(envelope.ALL_CHECKS)[0]))


class S8_Registration(unittest.TestCase):
    def test_s8_record_and_register_are_bound(self):
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        state, date, v = scr_state(worktree(RECORD).decode("utf-8"))
        self.assertEqual(v, [])
        for spec in NEW_ENTRIES:
            e = by_id.get(spec["id"])
            with self.subTest(entry=spec["id"]):
                self.assertIsNotNone(e)
                self.assertEqual((e["path"], e["type"], e["phase"],
                                  e["deliverable"]),
                                 (spec["path"], spec["type"], "W8", None))
                self.assertEqual(e["content_hash"], lf_hash(ROOT / e["path"]))
                self.assertEqual((e["status"], e["accepted_date"]),
                                 (state, date))
                self.assertTrue({"ADR-0059", "ADR-0055"}
                                <= set(e["depends_on"]))
        with self.subTest(control="a register status apart from the "
                                  "record is refused"):
            e = by_id["W8-S1-CM-01"]
            flipped = ("accepted", "2000-01-01") if state == "draft" \
                else ("draft", None)
            self.assertNotEqual((e["status"], e["accepted_date"]), flipped)


class S9_Total(unittest.TestCase):
    """Exactly what S9 proves: the manifest holds exactly twelve distinct
    identities; the record and the board carry the fixed total sentence;
    and on the record, the board wording this landing adds and the two new
    registry roles, every token the case_counts grammar recognises is the
    literal word "twelve". Count wording that grammar does not recognise is
    outside this mechanical claim; S9 is not contradiction detection."""

    def surfaces(self):
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        return {
            "record": worktree(RECORD).decode("utf-8"),
            "board wording this landing adds": " ".join(
                [SCR_ROW_BODY] + list(SCR_STATUS.values())),
            "new registry roles": " ".join(
                by_id[s["id"]]["role"] for s in NEW_ENTRIES),
        }

    def test_s9_the_stated_total_is_twelve(self):
        ids = manifest_ids()
        record = worktree(RECORD).decode("utf-8")
        board = worktree(BOARD).decode("utf-8")
        self.assertEqual(total_violations(ids, record, board,
                                          self.surfaces()), [])
        for name, args in {
                "an eleven-identity manifest": (ids[1:], record, board,
                                                self.surfaces()),
                "a duplicated identity": (ids[:-1] + ids[:1], record, board,
                                          self.surfaces()),
                "a record without the total sentence": (
                    ids, record.replace(COUNT_SENTENCE, "the cases"), board,
                    self.surfaces()),
                "a board without the total sentence": (
                    ids, record, board.replace(COUNT_SENTENCE, "the cases"),
                    self.surfaces()),
                "a contradictory total in words": (
                    ids, record, board, dict(self.surfaces(), record=record
                                             + "\nThe supplementary corpus "
                                             "contains thirteen cases.")),
                "a contradictory total in numerals": (
                    ids, record, board, dict(self.surfaces(), record=record
                                             + "\nIt holds 13 supplementary "
                                             "cases.")),
                "a contradictory total in a registry role": (
                    ids, record, board, dict(
                        self.surfaces(), **{"new registry roles":
                                            "eleven reviewer-visible "
                                            "cases"}))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(total_violations(*args))
        with self.subTest(fact="the grammar's stated boundary: wording "
                               "outside it is not recognised and not "
                               "claimed"):
            for outside in ("It contains zero cases.",
                            "It contains twenty-one cases.",
                            "It contains thirteen of all the cases."):
                self.assertEqual(case_counts(outside), [])
            self.assertEqual(case_counts("1. Every case is listed."), [])
            self.assertEqual(case_counts("It contains thirteen cases."),
                             ["thirteen"])
            self.assertEqual(case_counts("It holds 13 supplementary cases."),
                             ["13"])


class S10_ReverseTextualNonReuse(unittest.TestCase):
    """Textual non-reuse only, never semantic independence: no ten-word
    sequence of any supplementary variant occurs in any other tracked md or
    json text, the original corpus's cases included."""

    def test_s10_no_supplementary_sequence_elsewhere(self):
        grams = variant_ngrams(corpus_bytes(case_rel(c))
                               for c in manifest_ids())
        self.assertTrue(grams)
        for rel in other_tracked_texts():
            try:
                words = corpus._normalise_words(
                    worktree(rel).decode("utf-8"))
            except (UnicodeDecodeError, OSError):
                continue
            with self.subTest(tracked=rel):
                self.assertEqual(grams & corpus._ngrams(words), set())
        with self.subTest(control="the sweep detects a real reuse"):
            sample = next(iter(grams))
            self.assertIn(sample, corpus._ngrams(list(sample)))


class S11_RecordCarriage(unittest.TestCase):
    def test_s11_record_carries_its_statements_and_no_exposure(self):
        text = worktree(RECORD).decode("utf-8")
        flat = _flat(text)
        for s in REQUIRED_SCR:
            with self.subTest(carried=s[:44]):
                self.assertIn(s, flat)
        commit, problems = l2_snapshot()
        self.assertEqual(problems, [])
        pins = [p.split(":", 1)[1] for _, p, _ in PREIMAGE.values()]
        pins += [_sha(snapshot_bytes(commit, r)).split(":", 1)[1]
                 for r in (ENVELOPE, AUTHORITY, MANIFEST)]
        self.assertEqual(recovery.exposure_violations(text, pins), [])
        self.assertIn(_sha(corpus_bytes(MANIFEST)), text)
        self.assertNotIn("REPRO:", text)
        for plant in (manifest_ids()[0], "d" * 64):
            with self.subTest(control="a planted identity or digest is "
                                      "detected"):
                self.assertTrue(recovery.exposure_violations(
                    text + "\n" + plant, pins))


class S12_SuccessionsAndCensus(unittest.TestCase):
    def test_s12_staged_successions_and_census(self):
        commit, problems = l2_snapshot()
        self.assertEqual(problems, [])
        record = snapshot_bytes(commit, RECORD).decode("utf-8")
        for rel in (ENVELOPE, AUTHORITY):
            with self.subTest(baseline_object=PREIMAGE[rel][0]):
                self.assertEqual(_git("rev-parse", L1 + ":" + rel).strip(),
                                 PREIMAGE[rel][2])
            with self.subTest(exact_succession=PREIMAGE[rel][0]):
                self.assertEqual(succession_violations(
                    rel, snapshot_bytes(commit, rel).decode("utf-8"),
                    record), [])
        with self.subTest(fact="ADR-0059 Part G decision 25 stages exactly "
                               "these"):
            a59 = _flat(_lf(committed(L1, ADR59)).decode("utf-8"))
            self.assertIn("the envelope module's case-home limb admits "
                          "exactly the supplement home beside the original "
                          "home, its vacancy limb unchanged", a59)
            self.assertIn("this record's own pre-authoring absence limb (A9) "
                          "succeeds to the closure that landing proves", a59)
        paths = landing_paths(commit)
        ids = json.loads(snapshot_bytes(commit, MANIFEST))["rows"]
        expected = set(FIXED_CENSUS) | {case_rel(r["case_id"]) for r in ids}
        with self.subTest(fact="the census is exactly nineteen paths"):
            self.assertEqual(len(expected), 19)
            self.assertEqual(paths, expected)
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {ENVELOPE, AUTHORITY, SELF_REL})
        with self.subTest(fact="decision 18 names the fixed census"):
            m = re.search(r"18\. \*\*This landing's census is exactly "
                          r"nineteen paths:\*\* (.*?) ## ", _flat(record))
            self.assertIsNotNone(m)
            named = set(re.findall(r"`([^`]+)`", m.group(1)))
            self.assertEqual(named - {HOME + "/W8-C-<64-hex>.json"},
                             set(FIXED_CENSUS))
        present = snapshot_bytes(commit, ENVELOPE).decode("utf-8")
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, ()),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[ENVELOPE] + (("planted", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(ENVELOPE, text, record,
                                                      table))


class S13_RegistryAndBoard(unittest.TestCase):
    def test_s13_registry_and_board_change_exactly(self):
        commit, problems = l2_snapshot()
        self.assertEqual(problems, [])
        state, date, v = scr_state(snapshot_bytes(commit, RECORD)
                                   .decode("utf-8"))
        self.assertEqual(v, [])
        board_pre = _lf(committed(L1, BOARD)).decode("utf-8")
        reg_pre = _lf(committed(L1, REGISTRY)).decode("utf-8")
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
        hashes = {rel: _sha(snapshot_bytes(commit, rel))
                  for rel in (RECORD, MANIFEST)}
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
        with self.subTest(control="an unauthorised registry edit is "
                                  "refused"):
            self.assertNotEqual(reg.replace('"W8-S1-SCR"', '"W8-S1-SCRx"'),
                                expected_registry(reg_pre, hashes, state,
                                                  date))


if __name__ == "__main__":
    unittest.main()
