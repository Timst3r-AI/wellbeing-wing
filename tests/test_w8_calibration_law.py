"""W8-D3-B — disposition, reveal and calibration law proofs (ADR-0057, K1–K12).

The law is real: ADR-0057 fixes the session packet, the disposition register,
immutability, the custody and reproduction order, the reveal sequence, the
calibration relation and the permitted counts before any session exists. This
module proves the published renderer and the register, relation and count
mechanics with planted-mutant controls, and proves the law's carriage.

THIS MODULE RENDERS NO PUBLISHED CASE. Every packet here is built from the
clearly labelled mechanics sentinel below - deliberately meaningless, never a
case, never written to the repository. No custody location is named, read or
reached; no withheld authoring record is opened, parsed, hashed or relayed;
no disposition, register instance, reveal, comparison or count of human acts
exists or is produced.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any disposition, any authored intent or any relation; that
any session was held or is open; that any custody record exists or is intact;
that any model was contacted; that ADR-0047 precondition 3 moved; or that
W8-D3-C or W8-D3-D is authorised.
"""

import ast
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import test_w8_discriminating_instrument_envelope as envelope
import w8_review_packet as packet

ROOT = Path(__file__).resolve().parents[1]
ADR57 = ROOT / "docs/decisions/0057-w8-disposition-reveal-calibration-law.md"
ADR54 = ROOT / "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
RENDERER = Path(packet.__file__).resolve()
SELF = Path(__file__).resolve()

REGISTER_SCHEMA = "w8-disposition-register-v1"
REGISTER_ROW_FIELDS = frozenset({"case_id", "disposition"})
RELATIONS = ("agreement", "divergence")
COUNT_STATEMENT = "a count of individual human acts and nothing more"

# Mechanics fixtures only — NOT cases, NOT authored, NOT governed content.
SENTINEL_PAIRS = (
    ("mechanics sentinel one — not a case\nsecond  line, double space ",
     "mechanics sentinel one-b — not a case\n- a list-shaped line\n"),
    ("mechanics sentinel two — not a case",
     "mechanics sentinel two-b — not a case,   three spaces"),
)


def _lf_text(p):
    return p.read_bytes().replace(b"\r\n", b"\n").decode("utf-8")


def sentinel_cases():
    return [envelope.build_review_case(a, b) for a, b in SENTINEL_PAIRS]


def sentinel_bytes():
    return [envelope.canonical_bytes(c) for c in sentinel_cases()]


# ------------------------------------------------------- packet checker
def packet_violations(raw, cases):
    """Structural verdict over a packet against the law's skeleton. It parses
    the packet; it never re-renders it."""
    v = []
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return ["packet is not UTF-8"]
    if "\r" in text:
        v.append("carriage return in packet")
    if not text.endswith("\n") or text.endswith("\n\n"):
        v.append("packet must end with exactly one LF")
    if not text.startswith(packet.HEADER + "\n\n"):
        v.append("header is not the law's header")
    lines = text[len(packet.HEADER) + 2:].rstrip("\n").split("\n")
    expected = sorted(cases, key=lambda c: c["case_id"])
    starts = [i for i, l in enumerate(lines) if l.startswith(packet.CASE_PREFIX)]
    if [lines[i] for i in starts] != [packet.case_header(c["case_id"])
                                      for c in expected]:
        v.append("case blocks are missing, extra or out of ascending order")
        return v
    bounds = starts + [len(lines) + 1]
    for case, s, e in zip(expected, bounds, bounds[1:]):
        block = lines[s + 1:e - 1] if e <= len(lines) else lines[s + 1:]
        cid = case["case_id"]
        cursor = 0
        for label in packet.VARIANTS:
            try:
                b = block.index(packet.begin_marker(label), cursor)
                f = block.index(packet.end_marker(label), b + 1)
            except ValueError:
                v.append("%s: %s frame missing or altered" % (cid[:13], label))
                break
            if b != cursor:
                v.append("%s: unexpected material before %s" % (cid[:13], label))
            if "\n".join(block[b + 1:f]) != \
                    case["admissible_source_evidence"][label]:
                v.append("%s: %s is not whole and verbatim" % (cid[:13], label))
            cursor = f + 1
        if block[cursor:] != [packet.OPTIONS_LINE, packet.response_line(cid)]:
            v.append("%s: options or response line is not exactly the law's"
                     % cid[:13])
    for token in packet.TOKENS:
        if text.count(token) != len(cases):
            v.append("token %s does not occur exactly once per case" % token)
    for s in sorted(envelope.SPS_FIELDS | packet.WITHHELD_FIELDS
                    | envelope.ALL_CHECKS | envelope.INCONCLUSIVE_LABELS
                    | {envelope.AUTHORING_SCHEMA, "sha256:"}):
        if s in text:
            v.append("forbidden material in packet: %s" % s)
    for case in cases:
        digest = case["structural_provenance_support"]["source_evidence_sha256"]
        if text.replace(case["case_id"], "").count(digest):
            v.append("a digest appears outside the case identity")
    return v


# --------------------------------------------- register, relation, counts
def register_violations(obj, case_ids=None):
    v = []
    if not isinstance(obj, dict) or set(obj) != {"schema", "rows"}:
        return ["register must be one closed object with exactly schema and "
                "rows"]
    if obj["schema"] != REGISTER_SCHEMA:
        v.append("register schema")
    rows = obj["rows"]
    if not isinstance(rows, list):
        return v + ["rows must be an array"]
    for r in rows:
        if not isinstance(r, dict) or set(r) != REGISTER_ROW_FIELDS:
            v.append("row shape")
            continue
        if not envelope.CASE_ID_RE.match(str(r["case_id"])):
            v.append("row case_id shape")
        if r["disposition"] not in packet.TOKENS:
            v.append("row disposition is not a lawful token")
    ids = [r.get("case_id") for r in rows if isinstance(r, dict)]
    if len(ids) != len(set(ids)):
        v.append("duplicate case_id")
    if ids != sorted(ids):
        v.append("rows not in ascending case_id order")
    if case_ids is not None and set(ids) != set(case_ids):
        v.append("rows are not one-to-one with the published cases")
    return v


def relation(human_token, intended_token):
    if human_token not in packet.TOKENS or intended_token not in packet.TOKENS:
        raise ValueError("both sides must be lawful tokens")
    return "agreement" if human_token == intended_token else "divergence"


def counts(register_rows, relations):
    out = {t: {"count": sum(r["disposition"] == t for r in register_rows),
               "statement": COUNT_STATEMENT} for t in packet.TOKENS}
    for name in RELATIONS:
        out[name] = {"count": sum(x == name for x in relations),
                     "statement": COUNT_STATEMENT}
    return out


def count_violations(c):
    v = []
    if set(c) != set(packet.TOKENS) | set(RELATIONS):
        v.append("counts must be exactly the per-token and per-relation kinds")
    for k, entry in c.items():
        if not isinstance(entry, dict) or set(entry) != {"count", "statement"}:
            v.append("%s: count entry shape" % k)
            continue
        if type(entry["count"]) is not int or entry["count"] < 0:
            v.append("%s: a count is a non-negative integer, never a rate" % k)
        if entry["statement"] != COUNT_STATEMENT:
            v.append("%s: the decision-31 statement is missing" % k)
    return v


def subprocess_reach_violations(source):
    """Static verdict on the renderer's whole subprocess reach: run alone,
    exactly twice, inside committed_object_bytes, each a literal git
    argument list of the rev-parse or cat-file shape, never a shell."""
    tree = ast.parse(source)
    readers = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
               and n.name == "committed_object_bytes"]
    if len(readers) != 1:
        return ["exactly one committed-object reader is required"]
    inside = {id(n) for n in ast.walk(readers[0])}
    uses = [n for n in ast.walk(tree) if isinstance(n, ast.Attribute)
            and isinstance(n.value, ast.Name) and n.value.id == "subprocess"]
    runs = [n for n in uses if n.attr == "run"]
    v = []
    if {u.attr for u in uses} != {"run"}:
        v.append("a subprocess capability other than run is used")
    if not all(id(u) in inside for u in uses):
        v.append("subprocess is reached outside the committed-object reader")
    if len(runs) != 2:
        v.append("the reader must make exactly two subprocess calls")
    calls = [n for n in ast.walk(readers[0]) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Attribute) and n.func.attr == "run"]
    shapes = {"rev-parse": "--verify", "cat-file": "-p"}
    verbs = []
    for call in calls:
        argv = call.args[0] if call.args else None
        elts = argv.elts if isinstance(argv, ast.List) else []
        consts = [e.value if isinstance(e, ast.Constant) else None
                  for e in elts]
        if len(consts) != 4 or consts[0] != "git" or \
                consts[1] not in shapes or consts[2] != shapes[consts[1]]:
            v.append("a call is not a literal git rev-parse --verify or "
                     "cat-file -p argument list")
            continue
        verbs.append(consts[1])
        if any(k.arg in ("shell", None) for k in call.keywords):
            v.append("a call admits a shell or a keyword splat")
    if sorted(verbs) != ["cat-file", "rev-parse"]:
        v.append("the two calls must be one rev-parse and one cat-file")
    return v


# ------------------------------------------------------------------ proofs
class K1_Carriage(unittest.TestCase):
    def test_k1_law_carriage_and_template_skeleton(self):
        a57, a54 = _lf_text(ADR57), _lf_text(ADR54)
        question = "*" + packet.REVIEW_QUESTION + "*"
        nine = re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                         r"failure\.\*\*)", a54).group(1)
        with self.subTest(carried="review question byte-identical"):
            self.assertIn(question, a54)
            self.assertIn(question, a57)
        with self.subTest(carried="nine-rule block byte-identical"):
            self.assertIn(nine, a57)
        for s in ("`agreement` · `divergence`", COUNT_STATEMENT,
                  "before any parse or reserialisation",
                  "The scanner is never run against the custody location",
                  "Only after a clean scan may the candidate bytes be parsed",
                  "no implementer-created suppression, redaction or byte "
                  "repair is permitted",
                  "nothing in the reveal landing (D3-D) begins until the "
                  "session record is published and independently "
                  "remote-verified",
                  "The packet omits `structural_provenance_support`",
                  REGISTER_SCHEMA):
            with self.subTest(carried=s[:44]):
                self.assertIn(s, " ".join(a57.split()))
        for t in packet.TOKENS:
            with self.subTest(token=t):
                self.assertIn(t, a57)
        with self.subTest(fact="the renderer's template is this record's "
                               "skeleton"):
            for line in (packet.HEADER.split("\n")
                         + [packet.OPTIONS_LINE,
                            packet.begin_marker("variant_a"),
                            packet.end_marker("variant_b"),
                            packet.CASE_PREFIX + "<case_id> ====",
                            packet.RESPONSE_PREFIX + "<case_id>:"]):
                self.assertIn(line, a57)
        with self.subTest(fact="the withheld-record schema string is absent "
                               "from this record"):
            self.assertNotIn(envelope.AUTHORING_SCHEMA, a57)


class K2_Refusals(unittest.TestCase):
    def test_k2_renderer_refuses_everything_but_a_lawful_case(self):
        ok = sentinel_bytes()
        self.assertTrue(packet.render_packet(ok))
        case = sentinel_cases()[0]
        mutants = {
            "a withheld authoring record":
                envelope.canonical_bytes(envelope._sentinel_record("A")),
            "a case carrying a withheld field":
                envelope.canonical_bytes(dict(case, authored_class="A")),
            "a case under the withheld schema":
                envelope.canonical_bytes(
                    dict(case, schema=envelope.AUTHORING_SCHEMA)),
            "non-canonical bytes":
                (json.dumps(case, indent=2) + "\n").encode("utf-8"),
            "malformed JSON": b"{not json\n",
            "a JSON array": b"[]\n",
            "a structural-collision variant": envelope.canonical_bytes(
                envelope.build_review_case(
                    "sentinel\n---- END variant_a ----", "sentinel other")),
        }
        for name, raw in mutants.items():
            with self.subTest(refused=name):
                with self.assertRaises(packet.PacketRefusal):
                    packet.render_packet([raw])
        with self.subTest(refused="a duplicate identity"):
            with self.assertRaises(packet.PacketRefusal):
                packet.render_packet([ok[0], ok[0]])
        with self.subTest(refused="an empty set"):
            with self.assertRaises(packet.PacketRefusal):
                packet.render_packet([])


class K3toK6_PacketLaw(unittest.TestCase):
    def setUp(self):
        self.cases = sentinel_cases()
        self.raw = packet.render_packet(sentinel_bytes())

    def test_k3_to_k6_the_rendered_packet_satisfies_the_law(self):
        self.assertEqual(packet_violations(self.raw, self.cases), [])

    def _detects(self, mutated):
        self.assertTrue(packet_violations(mutated.encode("utf-8"), self.cases))

    def test_k3_no_default_and_no_preselection(self):
        text = self.raw.decode("utf-8")
        cid = sorted(c["case_id"] for c in self.cases)[0]
        with self.subTest(control="a pre-filled response is detected"):
            self._detects(text.replace(packet.response_line(cid),
                                       packet.response_line(cid)
                                       + " review_inconclusive"))
        with self.subTest(control="a pre-marked option is detected"):
            self._detects(text.replace(packet.OPTIONS_LINE, packet.OPTIONS_LINE
                                       .replace("no_governance_delta",
                                                "[x] no_governance_delta"), 1))
        with self.subTest(control="a reordered option list is detected"):
            self._detects(text.replace(
                packet.OPTIONS_LINE, "Options: " + " | ".join(
                    reversed(packet.TOKENS)), 1))

    def test_k4_both_variants_whole_and_verbatim(self):
        text = self.raw.decode("utf-8")
        b = sorted(self.cases, key=lambda c: c["case_id"])[0]
        vb = b["admissible_source_evidence"]["variant_b"]
        with self.subTest(control="an omitted variant is detected"):
            self._detects(text.replace(
                "%s\n%s\n%s\n" % (packet.begin_marker("variant_b"), vb,
                                  packet.end_marker("variant_b")), "", 1))
        with self.subTest(control="collapsed whitespace is detected"):
            self._detects(text.replace("double space", "double  space", 1)
                          .replace("second  line", "second line", 1))
        with self.subTest(fact="whitespace survives verbatim"):
            self.assertIn("second  line, double space \n", text)
            self.assertIn("three spaces", text)

    def test_k5_symmetric_framing(self):
        text = self.raw.decode("utf-8")
        with self.subTest(fact="the two frames differ only in their label"):
            self.assertEqual(packet.begin_marker("variant_a").replace("_a", ""),
                             packet.begin_marker("variant_b").replace("_b", ""))
        with self.subTest(control="an asymmetric frame is detected"):
            self._detects(text.replace(packet.begin_marker("variant_b"),
                                       "**" + packet.begin_marker("variant_b")
                                       + "**", 1))

    def test_k6_omissions(self):
        text = self.raw.decode("utf-8")
        for s in sorted(envelope.SPS_FIELDS):
            with self.subTest(absent=s):
                self.assertNotIn(s, text)
        cid = sorted(c["case_id"] for c in self.cases)[0]
        digest = cid[len("W8-C-"):]
        for name, line in (("provenance support",
                            "source_evidence_sha256: " + digest),
                           ("a tally", "governance_delta_present: 0"),
                           ("a timestamp", "Rendered: 2026-01-01"),
                           ("a summary", "Summary: the variants differ")):
            with self.subTest(control="added %s is detected" % name):
                self._detects(text.replace(packet.case_header(cid),
                                           packet.case_header(cid) + "\n"
                                           + line, 1))


class K7K8_DeterminismAndOrder(unittest.TestCase):
    def test_k7_determinism_and_committed_object_reading(self):
        raws = sentinel_bytes()
        first = packet.render_packet(raws)
        with self.subTest(fact="identical input, identical packet"):
            self.assertEqual(first, packet.render_packet(list(raws)))
        with self.subTest(fact="input order does not move the packet"):
            self.assertEqual(first, packet.render_packet(list(reversed(raws))))
        with tempfile.TemporaryDirectory() as ws:
            def git(*args):
                subprocess.run(["git", "-c", "core.autocrlf=false", "-c",
                                "user.name=mechanics-sentinel", "-c",
                                "user.email=sentinel@example.invalid", "-c",
                                "commit.gpgsign=false"] + list(args),
                               cwd=ws, capture_output=True, check=True)
            git("init", "-q")
            rels = []
            for i, raw in enumerate(raws):
                rel = "sentinel-%d.json" % i
                (Path(ws) / rel).write_bytes(raw)
                rels.append(rel)
            git("add", "-A")
            git("commit", "-q", "-m", "mechanics sentinel")
            with self.subTest(fact="committed objects render the same packet"):
                self.assertEqual(
                    packet.render_packet_from_commit(ws, "HEAD", rels), first)
            for rel in rels:
                p = Path(ws) / rel
                p.write_bytes(p.read_bytes().replace(b"\n", b"\r\n")
                              .replace(b"sentinel", b"SENTINEL"))
            with self.subTest(fact="working-copy rewrites never reach the "
                                   "packet"):
                self.assertEqual(
                    packet.render_packet_from_commit(ws, "HEAD", rels), first)
        with self.subTest(fact="the packet hash is reproducible"):
            self.assertEqual(packet.packet_sha256(first),
                             packet.packet_sha256(packet.render_packet(raws)))

    def test_k8_ascending_case_identity_order(self):
        cases = sentinel_cases()
        text = packet.render_packet(sentinel_bytes()).decode("utf-8")
        ids = sorted(c["case_id"] for c in cases)
        self.assertLess(text.index(ids[0]), text.index(ids[1]))
        with self.subTest(control="swapped case blocks are detected"):
            blocks = text.rstrip("\n").split("\n\n" + packet.CASE_PREFIX)
            swapped = "\n\n".join([blocks[0]] + [packet.CASE_PREFIX + b
                                                 for b in reversed(blocks[1:])]
                                  ) + "\n"
            self.assertTrue(packet_violations(swapped.encode("utf-8"), cases))


class K9K10_RegisterRelationCounts(unittest.TestCase):
    IDS = ("W8-C-" + "1" * 64, "W8-C-" + "2" * 64)

    def register(self):
        return {"schema": REGISTER_SCHEMA,
                "rows": [{"case_id": self.IDS[0],
                          "disposition": "review_inconclusive"},
                         {"case_id": self.IDS[1],
                          "disposition": "no_governance_delta"}]}

    def test_k9_register_shape_order_and_binding(self):
        reg = self.register()
        self.assertEqual(register_violations(reg, self.IDS), [])
        self.assertEqual(envelope.canonical_bytes(reg),
                         envelope.canonical_bytes(json.loads(
                             envelope.canonical_bytes(reg))))
        mutants = {
            "a withheld field on a row":
                lambda r: r["rows"][0].update(authored_class="A"),
            "an unlawful token": lambda r: r["rows"][0].update(
                disposition="pass"),
            "an extra outer field": lambda r: r.update(note="x"),
            "a wrong schema": lambda r: r.update(schema=REGISTER_SCHEMA + "x"),
            "unsorted rows": lambda r: r["rows"].reverse(),
            "a duplicate row": lambda r: r["rows"].append(dict(r["rows"][0])),
            "a missing row": lambda r: r["rows"].pop(),
        }
        for name, mutate in mutants.items():
            with self.subTest(control=name):
                reg = self.register()
                mutate(reg)
                self.assertTrue(register_violations(reg, self.IDS))

    def test_k10_relation_and_counts(self):
        with self.subTest(fact="agreement only on byte-identical tokens"):
            for t in packet.TOKENS:
                self.assertEqual(relation(t, t), "agreement")
            self.assertEqual(relation(packet.TOKENS[0], packet.TOKENS[2]),
                             "divergence")
        with self.subTest(control="an unlawful token is refused"):
            with self.assertRaises(ValueError):
                relation("pass", packet.TOKENS[0])
        c = counts(self.register()["rows"], ["agreement", "divergence"])
        self.assertEqual(count_violations(c), [])
        self.assertEqual(c["governance_delta_present"]["count"], 0)
        with self.subTest(control="a rate is detected"):
            m = json.loads(json.dumps(c)); m["agreement"]["count"] = 0.5
            self.assertTrue(count_violations(m))
        with self.subTest(control="a score kind is detected"):
            m = json.loads(json.dumps(c))
            m["score"] = {"count": 1, "statement": COUNT_STATEMENT}
            self.assertTrue(count_violations(m))
        with self.subTest(control="a missing statement is detected"):
            m = json.loads(json.dumps(c)); m["divergence"]["statement"] = ""
            self.assertTrue(count_violations(m))


class K11K12_ReachAndAbsence(unittest.TestCase):
    def test_k11_renderer_reach_is_committed_objects_only(self):
        tree = ast.parse(RENDERER.read_text(encoding="utf-8"))
        imported = set()
        calls = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom):
                imported.add((node.module or "").split(".")[0])
            elif isinstance(node, ast.Call):
                f = node.func
                calls.add(f.attr if isinstance(f, ast.Attribute)
                          else getattr(f, "id", ""))
        with self.subTest(fact="standard library plus the envelope law only"):
            self.assertEqual(imported, {"hashlib", "json", "subprocess",
                                        "test_w8_discriminating_instrument_"
                                        "envelope"})
        with self.subTest(fact="no file, environment, clock or network "
                               "reach"):
            self.assertEqual(calls & {"open", "read_bytes", "read_text",
                                      "home", "expanduser", "getenv",
                                      "now", "time", "urlopen"}, set())
        for source in (RENDERER, SELF):
            with self.subTest(fact="no published case path in %s"
                                   % source.name):
                self.assertNotIn("discriminating-" "instrument",
                                 source.read_text(encoding="utf-8"))

    def test_k11_subprocess_reach_is_exactly_two_local_git_shapes(self):
        src = RENDERER.read_text(encoding="utf-8")
        with self.subTest(fact="statically: only subprocess.run, twice, "
                               "inside the object reader, as literal git "
                               "rev-parse and cat-file lists with no shell"):
            self.assertEqual(subprocess_reach_violations(src), [])
        mutants = {
            "an added shell=True": src.replace(
                "capture_output=True, check=True)",
                "capture_output=True, check=True, shell=True)", 1),
            "a swapped git verb": src.replace('"cat-file", "-p"',
                                              '"show", "-p"', 1),
            "a run outside the object reader": src + (
                "\n\ndef sneak():\n"
                "    return subprocess.run([\"git\", \"status\"], "
                "check=True)\n"),
            "an alternative subprocess capability": src + (
                "\n\ndef sneak():\n"
                "    return subprocess.Popen([\"git\", \"status\"])\n"),
            "a string command": src.replace(
                '["git", "cat-file", "-p", "%s:%s" % (sha, rel)]',
                '"git cat-file -p %s:%s" % (sha, rel)', 1),
        }
        for name, mutated in mutants.items():
            with self.subTest(control="%s is detected" % name):
                self.assertNotEqual(mutated, src)
                self.assertTrue(subprocess_reach_violations(mutated))

        object_id = "0123456789abcdef0123456789abcdef01234567"
        raws = {"sentinel-%d.json" % i: raw
                for i, raw in enumerate(sentinel_bytes())}
        captured = []

        class _Completed:
            def __init__(self, stdout):
                self.stdout = stdout

        def fake_run(*args, **kwargs):
            captured.append((args, kwargs))
            argv = args[0]
            if argv[1] == "rev-parse":
                return _Completed(object_id + "\n")
            return _Completed(raws[argv[3].split(":", 1)[1]])

        with mock.patch.object(packet.subprocess, "run", side_effect=fake_run):
            got = packet.committed_object_bytes("sentinel-repo", "HEAD",
                                                "sentinel-0.json")
        with self.subTest(fact="exactly the two intended command shapes, "
                               "in order"):
            self.assertEqual(got, raws["sentinel-0.json"])
            self.assertEqual([a[0] for a, _ in captured],
                             [["git", "rev-parse", "--verify", "HEAD^{commit}"],
                              ["git", "cat-file", "-p",
                               object_id + ":sentinel-0.json"]])
        with self.subTest(fact="argument lists only, no shell, local "
                               "repository, checked"):
            for args, kwargs in captured:
                self.assertEqual(len(args), 1)
                self.assertIsInstance(args[0], list)
                self.assertFalse(kwargs.get("shell", False))
                self.assertEqual(kwargs.get("cwd"), "sentinel-repo")
                self.assertIs(kwargs.get("check"), True)
        with self.subTest(fact="rendering from bytes makes no subprocess "
                               "call at all"):
            with mock.patch.object(packet.subprocess, "run",
                                   side_effect=AssertionError("unlawful")):
                self.assertTrue(packet.render_packet(list(raws.values())))
        with self.subTest(fact="rendering from a commit makes only those two "
                               "shapes, once per object"):
            captured.clear()
            with mock.patch.object(packet.subprocess, "run",
                                   side_effect=fake_run):
                packet.render_packet_from_commit("sentinel-repo", "HEAD",
                                                 sorted(raws))
            shapes = [a[0] for a, _ in captured]
            self.assertEqual(len(shapes), 2 * len(raws))
            for argv in shapes:
                self.assertIn(argv, [["git", "rev-parse", "--verify",
                                      "HEAD^{commit}"]]
                              + [["git", "cat-file", "-p",
                                  object_id + ":" + rel] for rel in raws])

    def test_k12_no_packet_register_or_reveal_artefact_exists(self):
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT,
                                 capture_output=True, text=True,
                                 check=True).stdout.split()
        with self.subTest(fact="no register or reveal home is tracked"):
            self.assertEqual(
                [p for p in tracked if p.startswith(
                    ("governance/discriminating-review/",
                     "governance/discriminating-reveal/"))], [])
        homes = {"docs/decisions/0057-w8-disposition-reveal-calibration-law.md",
                 "docs/phases/W8-D3-synthetic-calibration-brief.md",
                 "tests/w8_review_packet.py", "tests/test_w8_calibration_law.py"}
        for marker in (packet.PACKET_SCHEMA, REGISTER_SCHEMA):
            with self.subTest(fact="%s lives only in the law and its code"
                                   % marker):
                found = []
                for p in tracked:
                    try:
                        data = (ROOT / p).read_bytes()
                    except OSError:
                        continue
                    if marker.encode("utf-8") in data:
                        found.append(p)
                self.assertTrue(set(found) <= homes, sorted(found))
        flat = " ".join(__doc__.split())
        for clause in ("any disposition, any authored intent or any relation",
                       "that any custody record exists or is intact",
                       "that any model was contacted",
                       "W8-D3-C or W8-D3-D is authorised"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)


if __name__ == "__main__":
    unittest.main()
