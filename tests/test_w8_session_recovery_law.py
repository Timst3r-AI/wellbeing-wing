"""W8-D3 — session recovery law proofs (ADR-0058, R1–R10).

ADR-0058 records an attempted D3-C session as void and non-recordable,
leaves the published cases, the manifest and the published commitments
byte-untouched, bars any association or figure derived from the attempt
from becoming a source for governed state, classifies no exchange under
ADR-0047, and leaves D3-C blocked and D3-D unopened without creating any
reviewer route. This module proves that carriage and those absences, each
with planted-mutant controls.

THIS MODULE CARRIES NO ASSOCIATION OR FIGURE FROM THE VOID ATTEMPT. It
names no case, holds no disposition token as a literal, renders no packet,
opens no published case file, names, reads or reaches no custody location,
opens, parses, hashes or relays no withheld authoring record, and reproduces
no commitment. The published-case check reads git's own tree identity and
working-copy status for that home, and nothing inside it.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any disposition, any authored intent or any relation;
anything about the void attempt's material or the reviewer; that any
session was held or may now be held; that any custody record exists or is
intact; whether any exchange falls within ADR-0047 decision 3; that any
model was or was not contacted; that ADR-0047 precondition 3 moved; or that
W8-D3-C or W8-D3-D is authorised.
"""

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

import test_w8_discriminating_instrument_envelope as envelope
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
ADR58_REL = "docs/decisions/0058-w8-d3-session-recovery-law.md"
ADR58 = ROOT / ADR58_REL
ADR54 = ROOT / "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
REGISTRY = ROOT / "governance/registry.json"
BOARD = ROOT / "docs/phases/README.md"
SELF = Path(__file__).resolve()

# Published pins at the derived public baseline 372287ba: every law decision
# 8 names. LF SHA-256 of the source and the committed blob identity; neither
# is ever recomputed into a pin by this module. ADR-0055 is pinned at its
# effective reconciled state, as last changed by the W8-D2-MSA landing.
UNTOUCHED = {
    "docs/decisions/0054-generative-evaluation-maturity-doctrine.md": (
        "ADR-0054",
        "sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd",
        "77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43"),
    "docs/decisions/0057-w8-disposition-reveal-calibration-law.md": (
        "ADR-0057",
        "sha256:0954293ff1ebb8ba1fb66230f8673a3778c09b9c04762e3bc983cc1cc8c7c585",
        "abe344233f52929a934eabde689866fa25513201"),
    "docs/phases/W8-D3-synthetic-calibration-brief.md": (
        "W8-D3-SCB",
        "sha256:ce93c54735a09acf5a2e966628101538912d2faf4e09ad010a7606e293bc6068",
        "8b995003ff7628e2887f837d6cddb6ae8b6141f8"),
    "docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md": (
        "ADR-0055",
        "sha256:e23ddd60e197b8eadda50f1400cf0064a4665dd235edb96a05079ef606171d2b",
        "0da892b2a5aab4f271095c3515518d9c45a620bf"),
    "docs/phases/W8-D2-committed-blob-proof-correction.md": (
        "W8-D2-CBC",
        "sha256:f1d18113a61c9fbf27e9705a613881485fa6fa801f977327bb6db56588a1173c",
        "bc3cba96a1c366879420a3e97724221c348d1885"),
}
DECISION_8 = {"ADR-0054", "ADR-0055", "ADR-0057", "W8-D3-SCB", "W8-D2-CBC"}
# R5 succession under ADR-0059 Part G: every pin above stays proven at this
# record's own published landing commit, and the present state of exactly
# three of decision 8's laws is the exact reconciliation ADR-0059 pins.
LANDING = "897f0b14a66ee956bd9fe36e63975b04d5dc9663"
RECONCILED_BY_ADR_0059 = {"ADR-0055", "ADR-0057", "W8-D3-SCB"}
CASE_HOME = "governance/discriminating-instrument"
CASE_HOME_TREE = "ecf232275c81adffbc7335f0115ef501b2c92449"
REGISTER_HOME = "governance/discriminating-review"
REVEAL_HOME = "governance/discriminating-reveal"
D3_ENTRIES = {"W8-D3-SCB", "ADR-0057", "ADR-0058"}
LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")

REQUIRED = (
    "The attempted D3-C session is void and non-recordable.",
    "Nothing from it may be recorded as a session, in whole or in part.",
    "No D3-C disposition exists from the attempted session.",
    "No case-to-disposition association from the void attempt, and no "
    "distribution, position, count or aggregate derived from that attempt, "
    "may be copied, cited, bound or otherwise treated as a source for "
    "governed state",
    "This record carries no such association or figure",
    "it does not pre-judge the content of any future lawful human act, "
    "creates no reviewer route and authorises no future session.",
    "The void attempt did not open, read, hash, write or disclose retained "
    "authoring material.",
    "The twelve published cases, the commitment manifest and the published "
    "commitments are byte-untouched by this landing",
    "this record makes no new claim about retained-byte integrity, which "
    "remains subject to ADR-0055 decision 29's lawful reproduction gate.",
    "This record does not classify any exchange associated with the void "
    "attempt under ADR-0047 decision 3, and does not state whether model "
    "contact occurred.",
    "Q3 remains a fresh human-review duty at this landing.",
    "The void attempt performs and authorises no custody access, no "
    "commitment reproduction, no reveal, no comparison and no count.",
    "ADR-0054 decision 18 and ADR-0057 decision 6 stand exactly as "
    "published.",
    "may not repeat the D3-C review on this packet and represent the "
    "resulting act as a blind ADR-0057 session.",
)
GATE = (
    "D3-C remains open and is blocked at its human-review gate.",
    "D3-D remains unopened.",
    "Progress requires a separately governed authority or doctrine amendment "
    "outside the authority presently granted by W8-D3.",
)
# Board anchors that hold in both lawful states of this record. The status
# passage opens with exactly one of two alternatives - the draft wording, or
# the wording the human reviewer's acceptance substitutes - and both end at
# the same stable clause; the board row is anchored on its fixed first cell.
BOARD_ROW_ANCHOR = "| W8-D3 — Session Recovery Law (ADR-0058) |"
BOARD_STATUS_STARTS = (
    "**A draft session recovery law, ADR-0058, is before the human "
    "reviewer**",
    "**ADR-0058 — the session recovery law — is law**",
)
BOARD_STATUS_END = "creating no reviewer route."
DRAFT_STATUS = "**Status:** Draft for human review. Not accepted."
ACCEPTED_STATUS = re.compile(r"\*\*Status:\*\* Accepted by human reviewer, "
                             r"(\d{4}-\d{2}-\d{2})\. ")
NO_ROUTE = ("This record creates no substitute reviewer, no delegation "
            "mechanism, no new disposition source and no exception to "
            "ADR-0054 decision 18 or ADR-0057 decision 6.")

NEGATION = re.compile(r"\b(no|not|never|nothing|none|neither|nor|unopened)\b",
                      re.IGNORECASE)
ROUTE = re.compile(r"designat\w*|delegat\w*|substitut\w*|reviewer route|"
                   r"\b(alternate|alternative|independent|second|another|"
                   r"replacement) (human )?reviewer", re.IGNORECASE)
AUTHORITY = re.compile(r"\b(custody|reproduc\w*|reveal\w*|compar\w*|"
                       r"count|counts)\b", re.IGNORECASE)
CASE_ID_ANYWHERE = re.compile(r"W8-C-[0-9a-f]{64}")
# Q3 neutrality: wording that would attribute the void attempt's material to
# a model. Its absence is mechanical; whether any sentence asserts contact
# remains the review-only Q3 duty.
PROVENANCE_ASSERTION = re.compile(
    r"produced by a model|generated by a model|model[- ]dispositions?|"
    r"model[- ]generated|model output|dispositions? (from|by) a model",
    re.IGNORECASE)
# Statements this record must never carry, about the void attempt's values
# or about retained-byte integrity.
RETIRED = ("remain unchanged and valid", "None of the exposed values",
           "The seal on the hypotheses is intact", "retracted by the architect")
DIGEST = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")


def _lf_text(p):
    return p.read_bytes().replace(b"\r\n", b"\n").decode("utf-8")


def _flat(text):
    return " ".join(text.split())


def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def sentences(text):
    out = []
    for line in text.split("\n"):
        out += [s for s in re.split(r"(?<=[.;])\s+", line.strip()) if s]
    return out


# ------------------------------------------------------------- verdicts
def carriage_violations(text):
    flat = _flat(text)
    return ["missing: %s" % s[:48] for s in REQUIRED + GATE + (NO_ROUTE,)
            if s not in flat]


def exposure_violations(text, pins=()):
    """Pins are this module's own published law pins, excused by exact
    value only; nothing else digest-shaped is excused."""
    v = []
    if CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    for pin in pins:
        text = text.replace(pin, "")
    if DIGEST.search(text):
        v.append("a digest-shaped string is present")
    for token in packet.TOKENS:
        if token in text:
            v.append("a disposition token is present")
    return v


def provenance_violations(text):
    v = ["model-provenance wording: %s" % m.group(0)
         for m in PROVENANCE_ASSERTION.finditer(text)]
    v += ["retired statement: %s" % r for r in RETIRED if r in _flat(text)]
    return v


def case_home_violations(tree_identity, worktree_status):
    """R6 verdict over two observed values only: git's committed tree
    identity for the published case home, and git's porcelain working-copy
    status for that home. It opens no file inside the home."""
    v = []
    if tree_identity.strip() != CASE_HOME_TREE:
        v.append("committed tree identity differs from the published pin")
    lines = [l for l in worktree_status.split("\n") if l.strip()]
    if lines:
        v.append("working copy differs from the commit (%d path%s)"
                 % (len(lines), "" if len(lines) == 1 else "s"))
    return v


def observed_case_home():
    return (_git("rev-parse", "HEAD:" + CASE_HOME),
            _git("status", "--porcelain", "--untracked-files=all", "--",
                 CASE_HOME))


def unguarded(text, pattern):
    return [s for s in sentences(text)
            if pattern.search(s) and not NEGATION.search(s)]


def board_surfaces(board):
    """Return (row, status passage, violations) for this record's board
    surfaces, in either lawful state of the record."""
    v = []
    rows = [l for l in board.split("\n") if l.startswith(BOARD_ROW_ANCHOR)]
    if len(rows) != 1:
        v.append("exactly one board row is required, found %d" % len(rows))
    starts = [(board.find(a), a) for a in BOARD_STATUS_STARTS
              if board.count(a)]
    if len(starts) != 1 or any(board.count(a) > 1 for a in
                               BOARD_STATUS_STARTS):
        v.append("exactly one status-passage opening is required, found %d"
                 % sum(board.count(a) for a in BOARD_STATUS_STARTS))
        return ("\n".join(rows), "", v)
    start = starts[0][0]
    end = board.find(BOARD_STATUS_END, start)
    if end < 0:
        v.append("the status passage does not reach its stable close")
        return ("\n".join(rows), "", v)
    return ("\n".join(rows), board[start:end + len(BOARD_STATUS_END)], v)


def header_state(header_text):
    """("accepted", date), ("draft", None) or (None, None), read from this
    record's status line only."""
    head = "\n".join(header_text.split("\n")[:8])
    m = ACCEPTED_STATUS.search(head)
    if m:
        return ("accepted", m.group(1))
    if DRAFT_STATUS in head:
        return ("draft", None)
    return (None, None)


def with_status_line(text, line):
    """Mechanics only: the same record with its status line replaced."""
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines[:8]) if l.startswith("**Status:**")]
    if len(idx) != 1:
        raise ValueError("exactly one status line is required")
    lines[idx[0]] = line
    return "\n".join(lines)


def registry_entry_violations(entry, header_text):
    v = []
    if entry is None:
        return ["no registry entry"]
    if entry["path"] != ADR58_REL or entry["type"] != "adr":
        v.append("path or type")
    if entry["deliverable"] != "W8-D3" or entry["phase"] != "W8":
        v.append("phase or deliverable")
    state, date = header_state(header_text)
    if state == "accepted":
        if entry["status"] != "accepted":
            v.append("header accepted but registry is not")
        elif entry["accepted_date"] != date:
            v.append("registry acceptance date differs from the header")
    elif state == "draft":
        if entry["status"] != "draft" or entry["accepted_date"] is not None:
            v.append("header is a draft but registry is not draft")
    else:
        v.append("header status is neither the draft nor an accepted line")
    for ref in ("ADR-0057", "ADR-0054", "W8-D3-SCB"):
        if ref not in entry["depends_on"]:
            v.append("missing dependency %s" % ref)
    return v


def load_registry():
    return json.loads(_lf_text(REGISTRY))


# ------------------------------------------------------------------ proofs
class R1_VoidSessionCarriage(unittest.TestCase):
    def test_r1_void_session_and_exclusion_law_carried(self):
        text = _lf_text(ADR58)
        self.assertEqual(carriage_violations(text), [])
        with self.subTest(carried="nine-rule block byte-identical"):
            nine = re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                             r"failure\.\*\*)", _lf_text(ADR54)).group(1)
            self.assertIn(nine, text)
        for sentence in REQUIRED + GATE:
            with self.subTest(control="removing '%s' is detected"
                                      % sentence[:36]):
                mutated = _flat(text).replace(sentence, "")
                self.assertTrue(carriage_violations(mutated))


class R2_NoExposedValue(unittest.TestCase):
    def test_r2_no_case_identity_digest_or_token(self):
        reg = load_registry()
        role = " ".join(e["role"] + " " + e["title"] for e in reg["entries"]
                        if e["id"] == "ADR-0058")
        board = _lf_text(BOARD)
        row, passage, problems = board_surfaces(board)
        self.assertEqual(problems, [],
                         "the board row and status passage must both exist")
        self.assertTrue(row and passage)
        row += "\n" + passage
        with self.subTest(fact="the accepted alternative is anchored too"):
            for a, b in ((BOARD_STATUS_STARTS[0], BOARD_STATUS_STARTS[1]),
                         (BOARD_STATUS_STARTS[1], BOARD_STATUS_STARTS[0])):
                if a in board:
                    swapped = board.replace(a, b)
                    r2, p2, v2 = board_surfaces(swapped)
                    self.assertEqual(v2, [])
                    self.assertTrue(p2.startswith(b))
                    self.assertEqual(r2, board_surfaces(board)[0])
        for name, mutated in (
                ("a missing board row", "\n".join(
                    l for l in board.split("\n")
                    if not l.startswith(BOARD_ROW_ANCHOR))),
                ("a missing status passage", board.replace(
                    BOARD_STATUS_STARTS[0], "").replace(
                    BOARD_STATUS_STARTS[1], "")),
                ("both status openings at once", board + "\n"
                 + BOARD_STATUS_STARTS[0] + " " + BOARD_STATUS_STARTS[1]),
                ("a passage without its close", board.replace(
                    BOARD_STATUS_END, "creating nothing further."))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(board_surfaces(mutated)[2])
        surfaces = {"ADR-0058": _lf_text(ADR58), "registry role": role,
                    "board rows": row,
                    "this module": SELF.read_text(encoding="utf-8")}
        pins = tuple(lf.split(":", 1)[1] for _, lf, _ in UNTOUCHED.values())
        for name, text in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(exposure_violations(
                    text, pins if name == "this module" else ()), [])
            if name != "this module":
                with self.subTest(q3_neutral=name):
                    self.assertEqual(provenance_violations(text), [])
        clean = _lf_text(ADR58)
        planted = {
            "a case identity": "W8-C-" + "a" * 64,
            "a bare digest": "b" * 64,
            "a disposition token": packet.TOKENS[1],
        }
        for name, plant in planted.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(clean + "\n" + plant))
        for plant in ("The material was produced by a model.",
                      "The reviewer saw model dispositions.",
                      "Every retained authoring record remains unchanged and "
                      "valid.".replace("remains", "remain")):
            with self.subTest(control="detected: " + plant[:36]):
                self.assertTrue(provenance_violations(clean + "\n" + plant))


class R3_NoReviewerRoute(unittest.TestCase):
    def test_r3_route_terms_appear_only_as_prohibitions(self):
        text = _lf_text(ADR58)
        self.assertIn(NO_ROUTE, _flat(text))
        self.assertEqual(unguarded(text, ROUTE), [])
        self.assertTrue([s for s in sentences(text) if ROUTE.search(s)],
                        "the prohibition must itself be present")
        for plant in ("The human authority may designate one reviewer.",
                      "A reviewer may delegate the session.",
                      "An independent human reviewer supplies the tokens.",
                      "A substitute may return the tokens."):
            with self.subTest(control="detected: " + plant[:40]):
                self.assertTrue(unguarded(text + "\n" + plant, ROUTE))


class R4_NoCustodyRevealOrCountAuthority(unittest.TestCase):
    def test_r4_authority_terms_appear_only_as_prohibitions(self):
        text = _lf_text(ADR58)
        self.assertEqual(unguarded(text, AUTHORITY), [])
        for plant in ("The implementer reproduces each commitment.",
                      "Custody is opened for the replacement session.",
                      "The reveal landing may begin.",
                      "Per-token counts are published here."):
            with self.subTest(control="detected: " + plant[:40]):
                self.assertTrue(unguarded(text + "\n" + plant, AUTHORITY))


class R5_PublishedLawUntouched(unittest.TestCase):
    def test_r5_decision_8_law_byte_untouched(self):
        import test_w8_recovery_authority as authority
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        with self.subTest(fact="the pin set is exactly decision 8's law"):
            self.assertEqual({eid for eid, _, _ in UNTOUCHED.values()},
                             DECISION_8)
        with self.subTest(fact="ADR-0059 reconciles exactly three of them"):
            self.assertEqual(set(authority.RECONCILED_LAW),
                             RECONCILED_BY_ADR_0059)
        for rel, (eid, lf, blob) in UNTOUCHED.items():
            with self.subTest(landing_object=eid):
                self.assertEqual(
                    _git("rev-parse", LANDING + ":" + rel).strip(), blob)
                self.assertEqual(authority.committed_lf_hash(LANDING, rel), lf)
            if eid in RECONCILED_BY_ADR_0059:
                with self.subTest(exact_reconciliation=eid):
                    self.assertEqual(
                        authority.reconciliation_violations(rel), [])
                with self.subTest(registry=eid):
                    self.assertEqual(by_id[eid]["content_hash"],
                                     lf_hash(ROOT / rel))
                continue
            with self.subTest(working_copy=eid):
                self.assertEqual(lf_hash(ROOT / rel), lf)
            with self.subTest(committed_object=eid):
                self.assertEqual(_git("rev-parse", "HEAD:" + rel).strip(), blob)
            with self.subTest(registry=eid):
                self.assertEqual(by_id[eid]["content_hash"], lf)
        with self.subTest(control="a one-byte change is detected"):
            rel = next(iter(UNTOUCHED))
            raw = (ROOT / rel).read_bytes() + b" "
            self.assertNotEqual("sha256:" + hashlib.sha256(
                raw.replace(b"\r\n", b"\n")).hexdigest(), UNTOUCHED[rel][1])
        with self.subTest(control="an unauthorised edit to a reconciled law "
                                  "is detected"):
            rel = next(r for r, (e, _, _) in UNTOUCHED.items()
                       if e in RECONCILED_BY_ADR_0059)
            text = _lf_text(ROOT / rel)
            self.assertTrue(authority.reconciliation_violations(
                rel, present=text + " "))


class R6_PublishedCaseHomeDidNotMove(unittest.TestCase):
    """The published W8-D2 case home did not move, and nothing broader:
    that this landing changes no other W8-D2 path is evidenced by the
    candidate's four-path census, not by this proof."""

    def test_r6_case_home_tree_and_working_copy(self):
        tree, status = observed_case_home()
        with self.subTest(fact="the observed tree and status pass the "
                               "verdict"):
            self.assertEqual(case_home_violations(tree, status), [])
        wrong = tree.strip()[:-1] + ("0" if tree.strip()[-1] != "0" else "1")
        planted = {
            "a wrong tree identity": (wrong + "\n", status),
            "a non-identity tree value": ("HEAD\n", status),
            "a modified-path status": (
                tree, " M " + CASE_HOME + "/W8-D2-commitment-manifest.json\n"),
            "an untracked-path status": (
                tree, "?? " + CASE_HOME + "/planted.json\n"),
            "any other non-empty status": (tree, "garbage\n"),
        }
        for name, (t, st) in planted.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(case_home_violations(t, st))


class R7R8_NoRegisterRecordOrRevealHome(unittest.TestCase):
    def test_r7_no_register_or_session_record(self):
        tracked = _git("ls-files").split()
        with self.subTest(fact="no register home, tracked or on disk"):
            self.assertEqual([p for p in tracked
                              if p.startswith(REGISTER_HOME + "/")], [])
            self.assertFalse((ROOT / REGISTER_HOME).exists())
        with self.subTest(fact="no session record or register file anywhere"):
            self.assertEqual([p for p in tracked if re.search(
                r"disposition-register|human-disposition-record", p)], [])
        entries = load_registry()["entries"]
        with self.subTest(fact="no registry entry in either home"):
            self.assertEqual([e["id"] for e in entries if e["path"].startswith(
                (REGISTER_HOME, REVEAL_HOME))], [])
        with self.subTest(fact="W8-D3 entries are the brief, the law and this "
                               "recovery law only"):
            self.assertEqual({e["id"] for e in entries
                              if e["deliverable"] == "W8-D3"}, D3_ENTRIES)

    def test_r8_no_reveal_home(self):
        tracked = _git("ls-files").split()
        self.assertEqual([p for p in tracked
                          if p.startswith(REVEAL_HOME + "/")], [])
        self.assertFalse((ROOT / REVEAL_HOME).exists())


class R9_LaterLandingsBlocked(unittest.TestCase):
    def test_r9_d3d_blocked_and_nothing_later_opened(self):
        flat = _flat(_lf_text(ADR58))
        for s in GATE:
            with self.subTest(carried=s[:40]):
                self.assertIn(s, flat)
        with self.subTest(fact="ADR-0057's ordering safeguard carries"):
            self.assertIn("nothing in the reveal landing begins until a lawful "
                          "session record is published and independently "
                          "remote-verified", flat)
        entries = load_registry()["entries"]
        with self.subTest(fact="no registry entry opens a later deliverable"):
            self.assertEqual([e["id"] for e in entries
                              if e["deliverable"] in LATER], [])
        with self.subTest(fact="the board still states no session exists"):
            self.assertIn("No session, disposition, reveal or calibration "
                          "exists yet.", _lf_text(BOARD))


class R10_RegistryBinding(unittest.TestCase):
    def test_r10_registered_with_matching_hash_and_status(self):
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        entry = by_id.get("ADR-0058")
        text = _lf_text(ADR58)
        self.assertEqual(registry_entry_violations(entry, text), [])
        self.assertEqual(entry["content_hash"], lf_hash(ADR58))
        state, date = header_state(text)
        self.assertIn(state, ("draft", "accepted"))
        with self.subTest(control="the opposite status to this header is "
                                  "detected"):
            flipped = (dict(entry, status="accepted",
                            accepted_date="2000-01-01")
                       if state == "draft" else
                       dict(entry, status="draft", accepted_date=None))
            self.assertTrue(registry_entry_violations(flipped, text))
        synthetic = "2000-01-01"
        draft_text = with_status_line(
            text, DRAFT_STATUS + " **If accepted, effective only on "
            "publication and remote verification.**")
        accepted_text = with_status_line(
            text, "**Status:** Accepted by human reviewer, %s. **Effective "
            "only on publication and remote verification.**" % synthetic)
        draft_entry = dict(entry, status="draft", accepted_date=None)
        accepted_entry = dict(entry, status="accepted",
                              accepted_date=synthetic)
        with self.subTest(binding="clean draft"):
            self.assertEqual(header_state(draft_text), ("draft", None))
            self.assertEqual(registry_entry_violations(draft_entry,
                                                       draft_text), [])
        with self.subTest(binding="clean accepted"):
            self.assertEqual(header_state(accepted_text),
                             ("accepted", synthetic))
            self.assertEqual(registry_entry_violations(accepted_entry,
                                                       accepted_text), [])
        for name, (e, t) in {
                "draft header, accepted registry": (accepted_entry,
                                                    draft_text),
                "accepted header, draft registry": (draft_entry,
                                                    accepted_text),
                "accepted header, draft status carrying the header date": (
                    dict(draft_entry, accepted_date=synthetic),
                    accepted_text),
                "accepted header, different registry date": (
                    dict(accepted_entry, accepted_date="2000-01-02"),
                    accepted_text),
                "unrecognised header, draft registry": (
                    draft_entry, with_status_line(text, "**Status:** Other.")),
        }.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(registry_entry_violations(e, t))
        with self.subTest(control="a dropped dependency is detected"):
            dropped = dict(entry, depends_on=[d for d in entry["depends_on"]
                                              if d != "ADR-0057"])
            self.assertTrue(registry_entry_violations(dropped, text))
        with self.subTest(fact="green-does-not-mean clauses are carried"):
            flat = _flat(__doc__)
            for clause in ("anything about the void attempt's material or "
                           "the reviewer",
                           "that any session was held or may now be held",
                           "whether any exchange falls within ADR-0047 "
                           "decision 3",
                           "W8-D3-C or W8-D3-D is authorised"):
                self.assertIn(clause, flat)
        with self.subTest(fact="the reserved withheld-record schema string is "
                               "absent from the law"):
            self.assertNotIn(envelope.AUTHORING_SCHEMA, text)


if __name__ == "__main__":
    unittest.main()
