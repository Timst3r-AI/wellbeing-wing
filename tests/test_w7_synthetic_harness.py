"""W7-D4 — proofs for the synthetic harness, exam and manifest contract.

THE SUBJECT OF THIS MODULE IS AN INSTRUMENT AND A DOCUMENT, NEVER A MODEL.

Fourteen proof families, per the W7-D4 brief section 21. Expectations are derived
from landed law wherever a source states them; the two byte-fixed values, the
ADR-0049 synthetic notice and the ADR-0046 ceiling, are read from their records at
run time and never transcribed here.

WHAT GREEN DOES NOT MEAN. A green run of this module NEVER establishes:
that any model was contacted; that any model behaviour, quality, correctness or
safety was tested; that any trap has been behaviourally passed; that any of the
twenty-six unknowns has been answered about a real model; that Part Q is
resolved; that the local-wordlist coordinate seam is resolved; that ADR-0047
precondition 3 is discharged; that precondition 7 is discharged; that a
generated-evaluation record or run manifest exists; or that W7-D5 is open.
It establishes only that an instrument refuses what it should refuse.

ADR-0052 governs exclusion-list conformance here. P4a is necessary and not
sufficient: it decides bounded surface forms named by a governed inventory, and
a green P4a is no evidence for P4b in any degree. P4b is complete exclusion-list
conformance, review-only in full across all eleven decision 11 families, and
guard adequacy is P4b's question, not P4a's.
"""

import collections
import hashlib
import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import w7_synthetic_evaluation_harness as H

ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "fixtures" / "SYNTHETIC-w7-d4-exam.json"
ADR_FIELD_LAW = ROOT / "docs/decisions/0049-generated-evaluation-field-law.md"
EVAL_HOME = ROOT / "governance" / "evaluation"
FIXTURES = ROOT / "fixtures"

RUN = dict(run_id="W7-D4-PROOF", authorising_record="W7-D4-SHB", as_of="2026-08-22",
           exclusion_list_reference="ADR-0046 decision 11")


def exam_doc():
    return json.loads(EXAM.read_text(encoding="utf-8"))


def exam():
    return exam_doc()["w7_d4_exam"]


def source_unknowns():
    """Re-derive the 26 from live W5-D4 records. Never trusted from the exam."""
    rows = []
    for f in sorted(EVAL_HOME.glob("W5-D4-RUN-01-*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))["evaluation_record"]
        for p in r["probes"]:
            if (p["channel"] == "overt"
                    and p["delta_finding"]["outcome"] == "unknown-not-absent"
                    and p.get("basis") == "generative_respondent_required_and_not_authorised"):
                rows.append(r["record_id"] + "/" + p["probe_id"])
    return rows


def live_traps():
    return {json.loads(f.read_text(encoding="utf-8"))["evaluation_fixture"]["fixture_id"]
            for f in FIXTURES.glob("SYNTHETIC-fix-*.json")}


def field_tables():
    tables, lines = [], ADR_FIELD_LAW.read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(lines):
        if line.startswith("| # | Field | Holds | Nullable |"):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append([c.strip() for c in row.strip().strip("|").split("|")])
            tables.append(rows)
    return tables


def _plain(cell):
    return re.sub(r"[`*]", "", cell).split(" —")[0].strip()


def workspace():
    return tempfile.TemporaryDirectory(prefix="w7d4-proof-")


def one_probe():
    return exam()["probes"][0]


ORIGINS = {"variant_a": "authored_synthetic", "variant_b": "authored_synthetic"}


def spec(text, **over):
    """A fully declared specimen variant. Nothing here is defaulted by the harness."""
    v = {"origin": "authored_synthetic", "text_class": H.SPECIMEN_CLASS, "specimen_text": text}
    v.update(over)
    return v


# ---------------------------------------------------------------------------
# ADR-0052 P4a — the GOVERNED guard inventory.
#
# Every row below is a governed declaration, never an inference. Each names the
# decision 11 family it covers BY ITS EXACT TEXT, the guard that covers it, the
# governed POSITIVE controls that must trigger, and the governed CLEAN controls
# that must not. A row whose detector is None declares explicitly that the family
# currently has no useful mechanical guard and is carried by P4b alone.
#
# Nothing here is positional: no guard is matched to a family by list order, and no
# guard semantics are read out of decision 11's prose. The LIVE family inventory is
# source-read from the record and mechanically reconciled against the `family`
# column, so a change to decision 11 fails P4a until the inventory is governed again.
#
# ADR-0052 P4a is NECESSARY AND NOT SUFFICIENT. A green run here is no evidence for
# P4b, which is review-only in full across all eleven families.
ADR_BOUNDARY = ROOT / "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md"

# This module carries the barred surface forms, so scanning it would report its own
# vocabulary. It excludes exactly itself, asserted to one path, per the ADR-0046 P1
# precedent at tests/test_w7_boundary_invariant.py.
P4_SELF_EXCLUDED = frozenset({"tests/test_w7_synthetic_harness.py"})
P4_CLASS_ARTEFACT = "fixtures/SYNTHETIC-w7-d4-exam.json"
P4_SCOPE = (P4_CLASS_ARTEFACT, "tests/w7_synthetic_evaluation_harness.py")

# The one line in the harness that names what the harness refuses. A statement of a
# refusal is not the thing refused, but it carries the vocabulary, so it is declared
# as an exact literal and asserted to be the only such line.
P4_DECLARED_REFUSAL_LINE = (
    "provider, client, credential or binary. It accepts no `generated_output` input")

_SERIAL = re.compile(r"\b[A-Z]{2,}-?\d{5,}\b")
_NAME_PAIR = re.compile(r"\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b")
_REAL_DATA = re.compile(
    r"\bDOB\b|\bMRN\b|\bdate of birth\b|\bmedical record number\b|\b\d{3}-\d{2}-\d{4}\b",
    re.IGNORECASE)
_SECRET = re.compile(
    r"(?i)\b(api[_-]?key|secret|secrets|token|tokens|password|passwd|bearer|credential|"
    r"credentials|private[_-]key)\b|-----BEGIN")
_MACHINE = re.compile(r"(?i)(?:^|[^\w])(?:[a-z]:[\\/]|/users/|/home/|/root/|\\\\[a-z])")
_BINARY = re.compile(r"(?i)\.(?:gguf|safetensors|onnx|ckpt|pth|pt|bin|weights)\b")
_LIVE_CHANNEL = re.compile(r"(?i)https?://|\bendpoint\b|\bwebhook\b|\blocalhost\b|:\d{4,5}\b")

# Declared family texts. Authored once from the record and thereafter reconciled.
_F00 = "real-person data of any kind"
_F01 = ("any identified person's room, health, movement, food, device, contemplative, or "
        "journal material")
_F02 = "real wearable or device data"
_F03 = "private relationship or lived-interaction material"
_F04 = "private model transcripts"
_F05 = "credentials, tokens, keys, secrets, or private configuration"
_F06 = ("machine-identifying detail beyond OS class \u2014 hostnames, usernames, device names, "
        "serial numbers, or local folder paths (ADR-0007 decision 4; repository-relative paths "
        "are not machine-identifying and are unaffected)")
_F07 = "a model binary"
_F08 = "a real-person evaluation channel"
_F09 = "private adoption implementation detail"
_F10 = "or anything that would turn the public Wing into a live personal instrument"

Guard = collections.namedtuple("Guard", "guard_id family detector positive clean")


def _d_real_data(text, rel):
    return bool(_REAL_DATA.search(text))


def _d_name_pair(text, rel):
    if not rel.startswith("fixtures/"):
        return False
    return any(not n.startswith(("Persona", "Generated", "SYNTHETIC"))
               for n in _NAME_PAIR.findall(text))


def _d_serial(text, rel):
    return bool(_SERIAL.search(text))


def _d_generated_token(text, rel):
    return "generated_output" in text


def _d_secret(text, rel):
    return bool(_SECRET.search(text))


def _d_machine(text, rel):
    return bool(_MACHINE.search(text))


def _d_binary(text, rel):
    return bool(_BINARY.search(text))


def _d_live_channel(text, rel):
    return bool(_LIVE_CHANNEL.search(text))


# Controls are assembled at run time, so no tracked line carries a violating string.
GUARD_INVENTORY = (
    Guard("G01-real-data", _F00, _d_real_data,
          (lambda: "recorded D" + "OB: 1980-01-01", lambda: "id 123" + "-45-6789"),
          (lambda: "recorded in 1980 with no marker of any kind",)),
    Guard("G02-name-pair", _F01, _d_name_pair,
          (lambda: "Jane" + " " + "Doe attended",),
          (lambda: "Persona-K5 attended", lambda: "SYNTHETIC Fixture authored here")),
    Guard("G03-serial", _F02, _d_serial,
          (lambda: "device " + "SN" + "-123456",),
          (lambda: "device AB-1234 is too short to be a serial",)),
    Guard("G04-generated-token", _F04, _d_generated_token,
          (lambda: "text_class: generated" + "_output",),
          (lambda: "text_class: authored_synthetic_specimen",)),
    Guard("G05-credential", _F05, _d_secret,
          (lambda: "api" + "_key = " + "x" * 24, lambda: "-----BEGIN" + " PRIVATE BLOCK"),
          (lambda: "a governed key-value entry in the register",)),
    Guard("G06-machine-path", _F06, _d_machine,
          (lambda: "C" + ":" + chr(92) + "Users" + chr(92) + "someone" + chr(92) + "notes.txt",
           lambda: "stored under /" + "home/" + "someone/notes.txt"),
          # Decision 11's own parenthesis: repository-relative paths are unaffected.
          (lambda: "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md",
           lambda: "tests/w7_synthetic_evaluation_harness.py")),
    Guard("G07-model-binary", _F07, _d_binary,
          (lambda: "loaded model" + ".safe" + "tensors",),
          (lambda: "a binary decision about the boundary",)),
    Guard("G08-live-channel", _F08, _d_live_channel,
          (lambda: "posted to " + "http" + "s://example.invalid/live",),
          (lambda: "the overt channel declared by the source record",)),
    # Declared unguarded. P4b carries these alone; see ADR-0052 decision 29A(b).
    Guard("U01-relationship", _F03, None, (), ()),
    Guard("U02-adoption-detail", _F09, None, (), ()),
    Guard("U03-live-instrument", _F10, None, (), ()),
)

# P4a's non-claims, declared as data so they can be asserted rather than merely written.
P4A_NON_CLAIMS = (
    "P4a makes no claim that a guarded family is clear of violations",
    "P4a makes no claim that an unguarded family is clear of anything",
    "P4a makes no claim that the guard inventory is complete or ever will be",
    "P4a makes no claim to detect every possible semantic narrowing of a guard beyond its "
    "governed controls; guard adequacy is P4b's question, not P4a's",
    "a green P4a is no evidence for P4b in any degree",
)


def exclusion_items():
    """The LIVE decision 11 family inventory, split on the record's own separators."""
    src = ADR_BOUNDARY.read_text(encoding="utf-8")
    line = next(l for l in src.split("\n") if l.startswith("11. **No public W7 record"))
    body = line.split(":**", 1)[1]
    return [re.sub(r"[*`]", "", x).strip().strip(".") for x in body.split("\u00b7")]


def p4a_evaluate(scope, inventory=GUARD_INVENTORY, live=None):
    """Return P4a's failures. Empty means green. The five ADR-0052 conditions, in order.

    `scope` is a sequence of (rel, text) pairs. Nothing here decides a family; each
    guard decides one bounded surface form, and that is all a green result means.
    """
    out = []

    # (1) the live family inventory must reconcile against the governed inventory.
    # Reconciliation is by COVERAGE, not by order: tying the governed inventory to
    # decision 11's ordering would be the positional coupling ADR-0052 forbids.
    live = exclusion_items() if live is None else live
    declared = [g.family for g in inventory]
    for fam in live:
        n = declared.count(fam)
        if n != 1:
            out.append("live family is declared %d times, not once: %s" % (n, fam[:48]))
    for fam in declared:
        if fam not in live:
            out.append("governed inventory declares a family that is not live: %s" % fam[:48])
    if len(declared) != len(live):
        out.append("inventory size %d does not match the live family count %d"
                   % (len(declared), len(live)))

    for g in inventory:
        if g.detector is None:
            # (2) an unguarded family must not pretend to carry controls
            if g.positive or g.clean:
                out.append("unguarded family declares controls: %s" % g.guard_id)
            continue
        # (2) a required guard or its controls must be present and enabled
        if not callable(g.detector):
            out.append("required guard is absent or disabled: %s" % g.guard_id)
            continue
        if not g.positive or not g.clean:
            out.append("required control is absent: %s" % g.guard_id)
            continue
        # (3) every governed positive control must trigger
        for probe in g.positive:
            if not g.detector(probe(), "fixtures/probe.json"):
                out.append("governed positive control failed to trigger: %s" % g.guard_id)
        # (4) no governed clean control may begin triggering
        for probe in g.clean:
            if g.detector(probe(), "fixtures/probe.json"):
                out.append("governed clean control began triggering: %s" % g.guard_id)

    # (5) no guarded surface form may be present in the bytes of the class artefact
    for rel, text in scope:
        for g in inventory:
            if g.detector is not None and g.detector(text, rel):
                out.append("guarded surface detected in %s: %s" % (rel, g.guard_id))
    return out


def guard_scope():
    """The bytes P4a runs over: the class artefact, and the harness less its one
    declared refusal line, which names the vocabulary rather than carrying the thing."""
    scope = []
    for rel in P4_SCOPE:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if rel.endswith("w7_synthetic_evaluation_harness.py"):
            text = "\n".join(l for l in text.split("\n") if l != P4_DECLARED_REFUSAL_LINE)
        scope.append((rel, text))
    return scope


def live_scan_categories(text):
    """What the ordinary public-safety scan would report for this text, if anything."""
    scanner = H._scanner()
    with workspace() as ws:
        p = Path(ws) / "probe.txt"
        p.write_text(text, encoding="utf-8", newline="\n")
        findings, _ = scanner.scan_file(p, "probe.txt", scanner.load_wordlist(), {})
    return sorted({f[2] for f in (findings or [])})


def git_out(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def introducing_commit(rel):
    """The commit that first added a path, or None if it is not yet in history."""
    out = git_out("log", "--diff-filter=A", "--format=%H", "--", rel).split()
    return out[-1] if out else None


def precedes(earlier, later):
    """True when `earlier` is a strict ancestor of `later`. Read from history."""
    if earlier is None or later is None or earlier == later:
        return False
    return subprocess.run(["git", "merge-base", "--is-ancestor", earlier, later],
                          cwd=ROOT, capture_output=True).returncode == 0


def law_ceiling():
    """ADR-0046 decision 23, read from the record. Transcribed in no test."""
    return H._law_text("ceiling")


def load_doc(doc):
    """Run a whole exam document through the live loader, from outside the repository."""
    with workspace() as ws:
        p = Path(ws) / "exam.json"
        p.write_text(json.dumps(doc), encoding="utf-8")
        return H.load_exam(p)


def link_trigger():
    """A string the live scanner must flag, assembled at run time.

    Brief section 6.2: no D4 test should commit scan-sensitive payload text merely
    to prove the stop path. Assembling the trigger here keeps every tracked line
    clean while still driving the real scanner rather than a stand-in.
    """
    return "see " + "http" + "s://example.invalid/x"


# ==========================================================================
class H1_ExamSourceCompleteness(unittest.TestCase):
    def test_h1_source_coverage_is_complete_and_unique(self):
        e, unknowns, traps = exam(), source_unknowns(), live_traps()
        cited = [p["source_unknown"]["citation"] for p in e["probes"]]
        with self.subTest(limb="exactly 26 live source unknowns"):
            self.assertEqual(len(unknowns), 26)
        with self.subTest(limb="every exam citation resolves to a live unknown"):
            self.assertEqual(sorted(cited), sorted(unknowns))
        with self.subTest(limb="no duplicate source identity"):
            self.assertEqual(len(set(cited)), len(cited))
        with self.subTest(limb="all 23 live traps accounted"):
            self.assertEqual({p["source_trap"]["fixture_id"] for p in e["probes"]}, traps)
            self.assertEqual(len(traps), 23)
        with self.subTest(limb="declared counts match the mapping"):
            c = e["source_coverage"]
            self.assertEqual(c["unknowns_accounted"], 26)
            self.assertEqual(c["traps_accounted"], 23)
            self.assertEqual(c["unique_probes"], len(e["probes"]))
            self.assertEqual(c["expected_captures"], 2 * len(e["probes"]))
        with self.subTest(control="an omitted unknown is detected"):
            d = exam_doc()
            d["w7_d4_exam"]["probes"].pop()
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(control="a duplicated source identity is detected"):
            d = exam_doc()
            d["w7_d4_exam"]["probes"][1]["source_unknown"]["citation"] = \
                d["w7_d4_exam"]["probes"][0]["source_unknown"]["citation"]
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(control="an omitted trap is detected by coverage arithmetic"):
            d = exam_doc()
            d["w7_d4_exam"]["source_coverage"]["traps_accounted"] = 22
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(limb="the shipped exam fixture loads through the live loader"):
            loaded = H.load_exam(EXAM)
            self.assertEqual(len(loaded["probes"]), 26)
        with self.subTest(control="a verdict-bearing exam is refused by the loader"):
            d = exam_doc()
            d["w7_d4_exam"]["probes"][0]["verdict"] = "variant_a"
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(control="a result-bearing exam is refused by the loader"):
            d = exam_doc()
            d["w7_d4_exam"]["probes"][0]["result"] = "pass"
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(control="an exam variant with no declared text class is refused"):
            d = exam_doc()
            del d["w7_d4_exam"]["probes"][0]["variants"]["variant_a"]["text_class"]
            self.assertRaises(H.HarnessRefusal, self._load, d)
        with self.subTest(control="an exam variant with a non-authored origin is refused"):
            d = exam_doc()
            d["w7_d4_exam"]["probes"][0]["variants"]["variant_b"]["origin"] = "repository_fixture"
            self.assertRaises(H.HarnessRefusal, self._load, d)

    def _load(self, doc):
        with workspace() as ws:
            p = Path(ws) / "exam.json"
            p.write_text(json.dumps(doc), encoding="utf-8")
            return H.load_exam(p)


# ==========================================================================
class H2_PairVocabularyAndBijection(unittest.TestCase):
    def test_h2_labels_are_the_closed_pair_and_captures_biject(self):
        e = exam()
        with self.subTest(limb="exam declares exactly the closed pair"):
            self.assertEqual(tuple(e["variant_labels"]), H.VARIANT_LABELS)
            self.assertEqual(len(set(H.VARIANT_LABELS)), 2)
        with self.subTest(limb="every probe carries exactly the two labels"):
            for p in e["probes"]:
                self.assertEqual(tuple(p["variants"].keys()), H.VARIANT_LABELS)
        with self.subTest(limb="assembled captures key set equals the labels"):
            rec = self._assemble({"variant_a": "alpha", "variant_b": "beta"})
            self.assertEqual(sorted(rec["captures"]), list(H.VARIANT_LABELS))
            self.assertEqual(rec["pairing"]["variant_labels"], list(H.VARIANT_LABELS))
        with self.subTest(control="a third label is refused"):
            self.assertRaises(H.HarnessRefusal, self._assemble,
                              {"variant_a": "a", "variant_b": "b", "variant_c": "c"})
        with self.subTest(control="a missing capture is refused"):
            self.assertRaises(H.HarnessRefusal, self._assemble, {"variant_a": "a"})
        with self.subTest(control="a renamed label is refused"):
            self.assertRaises(H.HarnessRefusal, self._assemble,
                              {"variant_a": "a", "variant_z": "b"})

    def _assemble(self, texts, origins=None):
        origins = origins if origins is not None else {k: "authored_synthetic" for k in texts}
        return H.assemble_candidate_record(one_probe(), texts, origins=origins,
                                           placeholder_id="D4-CAND-01",
                                           **RUN)[H.WRAPPER_KEY]


# ==========================================================================
class H3_OptionDProvenance(unittest.TestCase):
    def test_h3_every_capture_is_an_authored_specimen_with_no_contact(self):
        rec = H.assemble_candidate_record(one_probe(),
                                          {"variant_a": "a", "variant_b": "b"},
                                          origins=ORIGINS,
                                          placeholder_id="D4-CAND-01", **RUN)[H.WRAPPER_KEY]
        with self.subTest(limb="every capture is an authored synthetic specimen"):
            for c in rec["captures"].values():
                self.assertEqual(c["text_class"], H.SPECIMEN_CLASS)
        with self.subTest(limb="authoring record is non-null on every capture"):
            for c in rec["captures"].values():
                self.assertTrue(c["authoring_record"])
        with self.subTest(limb="model contact is false / none / null"):
            self.assertEqual(rec["model_contact"],
                             {"occurred": False, "contact_class": "none",
                              "authorising_record": None})
        with self.subTest(control="a generated-output class is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              spec("x", text_class="generated_output"), "W7-D4-SHB")
        with self.subTest(control="a missing authoring record is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen, spec("x"), None)
        with self.subTest(control="an undeclared text class is refused, never defaulted"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              {"origin": "authored_synthetic", "specimen_text": "x"},
                              "W7-D4-SHB")
        with self.subTest(limb="admission returns the origin it admitted"):
            self.assertEqual(H.admit_specimen(spec("x", origin="repository_fixture"),
                                              "W7-D4-SHB"),
                             ("x", "repository_fixture"))
        with self.subTest(limb="the origin recorded is the origin admitted, not a default"):
            texts = {"variant_a": "a", "variant_b": "b"}
            admitted = {"variant_a": "repository_fixture", "variant_b": "repository_fixture"}
            r = H.assemble_candidate_record(one_probe(), texts, origins=admitted,
                                            placeholder_id="D4-CAND-01", **RUN)[H.WRAPPER_KEY]
            self.assertEqual([i["origin"] for i in r["inputs"]], ["repository_fixture"])
        with self.subTest(limb="two admitted origins are both declared, never flattened"):
            r = H.assemble_candidate_record(
                one_probe(), {"variant_a": "a", "variant_b": "b"},
                origins={"variant_a": "authored_synthetic", "variant_b": "governed_public_record"},
                placeholder_id="D4-CAND-01", **RUN)[H.WRAPPER_KEY]
            self.assertEqual([i["origin"] for i in r["inputs"]],
                             ["authored_synthetic", "governed_public_record"])
        with self.subTest(control="an origin outside the closed set cannot be assembled"):
            self.assertRaises(H.HarnessRefusal, H.assemble_candidate_record,
                              one_probe(), {"variant_a": "a", "variant_b": "b"},
                              origins={"variant_a": "model_transcript",
                                       "variant_b": "authored_synthetic"},
                              placeholder_id="D4-CAND-01", **RUN)
        with self.subTest(limb="a run carries admission's own answer into the record"):
            with workspace() as ws:
                state, rec2 = H.run_probe(one_probe(), H.ScanGateway(ws),
                                          placeholder_id="D4-CAND-02", **RUN)
            self.assertEqual(state, "candidate")
            self.assertEqual([i["origin"] for i in rec2[H.WRAPPER_KEY]["inputs"]],
                             ["authored_synthetic"])
        # ---- ADR-0046 P3: origin declaration, over the artefact that now exists ----
        with self.subTest(obligation="P3", limb="all 52 shipped specimens declare a closed origin"):
            n = 0
            for probe in exam()["probes"]:
                for v in probe["variants"].values():
                    self.assertIn(v["origin"], H.LAWFUL_ORIGINS)
                    n += 1
            self.assertEqual(n, 52)
            self.assertEqual(len(H.LAWFUL_ORIGINS), 3)
        with self.subTest(obligation="P3", limb="every assembled input declares one of the three"):
            self.assertTrue(rec["inputs"])
            for i in rec["inputs"]:
                self.assertIn(i["origin"], H.LAWFUL_ORIGINS)
        with self.subTest(obligation="P3", control="missing, empty and fourth-value origins refused"):
            for bad in (None, "", "model_transcript", "generated_output"):
                v = spec("x")
                v["origin"] = bad
                self.assertRaises(H.HarnessRefusal, H.admit_specimen, v, "W7-D4-SHB")
            v = spec("x")
            del v["origin"]
            self.assertRaises(H.HarnessRefusal, H.admit_specimen, v, "W7-D4-SHB")
        with self.subTest(control="no generated-output route exists in the module source"):
            src = Path(H.__file__).read_text(encoding="utf-8")
            self.assertNotIn('== "generated_output"', src)


# ==========================================================================
class H4_SyntheticOnlyConstruction(unittest.TestCase):
    def test_h4_no_real_person_or_private_intake_exists(self):
        raw = EXAM.read_text(encoding="utf-8")
        d = exam_doc()
        with self.subTest(limb="fixture carries the live synthetic marker law"):
            m = d["synthetic_marker"]
            self.assertIs(m["synthetic"], True)
            self.assertTrue(m["persona"].startswith("Persona-"))
            self.assertTrue(m["exercises"])
        with self.subTest(limb="every declared input origin is an ADR-0046 lawful origin"):
            rec = H.assemble_candidate_record(one_probe(), {"variant_a": "a", "variant_b": "b"},
                                              origins=ORIGINS,
                                              placeholder_id="D4-CAND-01", **RUN)[H.WRAPPER_KEY]
            for i in rec["inputs"]:
                self.assertIn(i["origin"], H.LAWFUL_ORIGINS)
        with self.subTest(limb="every exam variant declares a lawful origin and specimen class"):
            for probe in d["w7_d4_exam"]["probes"]:
                for v in probe["variants"].values():
                    self.assertIn(v["origin"], H.LAWFUL_ORIGINS)
                    self.assertEqual(v["text_class"], H.SPECIMEN_CLASS)
        with self.subTest(control="an unlawful declared origin is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              spec("x", origin="model_transcript"), "W7-D4-SHB")
        with self.subTest(control="an undeclared origin is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              {"text_class": H.SPECIMEN_CLASS, "specimen_text": "x"},
                              "W7-D4-SHB")
        with self.subTest(limb="no generated-evaluation source origin appears in the exam"):
            self.assertNotIn("governance/generated-evaluation", raw)
            self.assertFalse(re.search(r"\bGER-\d{4}\b", raw))
        with self.subTest(control="a recirculating specimen is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              spec("see GER-0001 for the earlier capture"), "W7-D4-SHB")
        with self.subTest(control="a home-referencing specimen is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              spec("under governance/generated-evaluation/x"), "W7-D4-SHB")
        # ---- ADR-0052 P4a: mechanical exclusion surface guards -------------------
        items = exclusion_items()
        with self.subTest(obligation="P4a", limb="the live decision 11 inventory is source-read"):
            self.assertEqual(len(items), 11)
            self.assertEqual(items[0], "real-person data of any kind")
            self.assertEqual(items[7], "a model binary")
        with self.subTest(obligation="P4a", limb="the guard inventory is governed, not derived"):
            # One governed row per live family, matched by declared text and never by
            # list position: the inventory's own order differs from decision 11's.
            self.assertEqual(len(GUARD_INVENTORY), 11)
            self.assertEqual(sorted(g.family for g in GUARD_INVENTORY), sorted(items))
            self.assertNotEqual([g.family for g in GUARD_INVENTORY], items)
            self.assertEqual(len({g.guard_id for g in GUARD_INVENTORY}), 11)
        with self.subTest(obligation="P4a", limb="green over the class artefact and the harness"):
            self.assertEqual(p4a_evaluate(guard_scope()), [])
        with self.subTest(obligation="P4a", limb="eight guarded, three declared unguarded"):
            guarded = [g for g in GUARD_INVENTORY if g.detector is not None]
            unguarded = [g for g in GUARD_INVENTORY if g.detector is None]
            self.assertEqual((len(guarded), len(unguarded)), (8, 3))
            for g in unguarded:
                self.assertEqual((g.positive, g.clean), ((), ()))
            for g in guarded:
                self.assertTrue(g.positive and g.clean, g.guard_id)
        with self.subTest(obligation="P4a", limb="the harness is clean but for one declared line"):
            src = Path(H.__file__).read_text(encoding="utf-8")
            hits = [l for l in src.split("\n")
                    if any(g.detector and g.detector(l, "tests/h.py") for g in GUARD_INVENTORY)]
            self.assertEqual(hits, [P4_DECLARED_REFUSAL_LINE])
        with self.subTest(obligation="P4a", limb="this module excludes exactly itself"):
            self.assertEqual(len(P4_SELF_EXCLUDED), 1)
            self.assertTrue((ROOT / next(iter(P4_SELF_EXCLUDED))).samefile(Path(__file__)))

        # the five accepted failure conditions, each shown to be detected
        with self.subTest(obligation="P4a", control="C1 reconciliation failure is detected"):
            out = p4a_evaluate([], live=items + ["a twelfth family added by a later record"])
            self.assertTrue(any("does not match the live family count" in x for x in out))
            out = p4a_evaluate([], live=[x for x in items if x != "a model binary"])
            self.assertTrue(any("not live" in x for x in out))
        with self.subTest(obligation="P4a", control="C2 an absent or disabled guard is detected"):
            broken = tuple(g._replace(detector=None) if g.guard_id == "G05-credential" else g
                           for g in GUARD_INVENTORY)
            self.assertTrue(any("unguarded family declares controls" in x
                                for x in p4a_evaluate([], inventory=broken)))
            stripped = tuple(g._replace(positive=()) if g.guard_id == "G05-credential" else g
                             for g in GUARD_INVENTORY)
            self.assertTrue(any("required control is absent" in x
                                for x in p4a_evaluate([], inventory=stripped)))
        with self.subTest(obligation="P4a", control="C3 a positive control that stops triggering"):
            deaf = tuple(g._replace(detector=lambda text, rel: False)
                         if g.guard_id == "G07-model-binary" else g for g in GUARD_INVENTORY)
            self.assertTrue(any("governed positive control failed to trigger" in x
                                for x in p4a_evaluate([], inventory=deaf)))
        with self.subTest(obligation="P4a", control="C4 a clean control that starts triggering"):
            greedy = tuple(g._replace(detector=lambda text, rel: True)
                           if g.guard_id == "G03-serial" else g for g in GUARD_INVENTORY)
            self.assertTrue(any("governed clean control began triggering" in x
                                for x in p4a_evaluate([], inventory=greedy)))
        with self.subTest(obligation="P4a", control="C5 a guarded surface in scope is detected"):
            for g in GUARD_INVENTORY:
                if g.detector is None:
                    continue
                planted = [(P4_CLASS_ARTEFACT, g.positive[0]())]
                self.assertTrue(any("guarded surface detected" in x and g.guard_id in x
                                    for x in p4a_evaluate(planted)), g.guard_id)

        with self.subTest(obligation="P4a", limb="the ordinary scan is NOT sufficient for P4a"):
            # Demonstrated rather than asserted: for these families the live scanner
            # reports nothing at all, so a clean scan cannot stand in for the guard.
            for gid in ("G05-credential", "G06-machine-path", "G07-model-binary"):
                g = next(x for x in GUARD_INVENTORY if x.guard_id == gid)
                planted = g.positive[0]()
                self.assertEqual(live_scan_categories(planted), [])
                self.assertTrue(g.detector(planted, "fixtures/probe.json"))
        with self.subTest(obligation="P4a", limb="the non-claims are declared and carried"):
            self.assertEqual(len(P4A_NON_CLAIMS), 5)
            flat = " ".join(__doc__.split())
            for clause in ("P4a is necessary and not sufficient",
                           "a green P4a is no evidence for P4b",
                           "guard adequacy is P4b's question"):
                self.assertIn(clause, flat)
            self.assertIn("guard adequacy is P4b's question, not P4a's",
                          " ".join(" ".join(P4A_NON_CLAIMS).split()))

        # ---- ADR-0052 P4b: review-only in full, across all eleven families -------
        with self.subTest(obligation="P4b", limb="all eleven families are inside P4b"):
            self.assertEqual(len(items), 11)
            self.assertEqual(len(GUARD_INVENTORY), 11)
        with self.subTest(obligation="P4b", limb="no mechanical result claims P4b"):
            src = Path(__file__).read_text(encoding="utf-8")
            # Assembled, so the module that forbids the phrase does not contain it.
            self.assertNotIn("P4" + " green", src)
            # Assembled for the same reason: no mechanical P4b evaluator may exist,
            # and the check must not create the very name it forbids.
            self.assertNotIn("p4b" + "_evaluate", src)
            self.assertNotIn("def " + "p4b_", src)
        with self.subTest(obligation="P4b", limb="the three unguarded families are named"):
            unguarded = {g.family for g in GUARD_INVENTORY if g.detector is None}
            self.assertEqual(len(unguarded), 3)
            self.assertTrue(any("relationship" in f for f in unguarded))
            self.assertTrue(any("adoption" in f for f in unguarded))
            self.assertTrue(any("live personal instrument" in f for f in unguarded))

        # ---- ADR-0046 P6: no-recirculation, over the artefact that now exists ----
        with self.subTest(obligation="P6", limb="no exam source reference resolves into the class"):
            for probe in d["w7_d4_exam"]["probes"]:
                for field in (probe["source_unknown"]["citation"],
                              probe["source_unknown"]["record"],
                              probe["source_trap"]["fixture_id"]):
                    self.assertNotIn("governance/generated-evaluation", field)
                    self.assertIsNone(re.match(r"GER-\d{4}", field))
        with self.subTest(obligation="P6", limb="every assembled input cites live sources only"):
            r = H.assemble_candidate_record(one_probe(), {"variant_a": "a", "variant_b": "b"},
                                            origins=ORIGINS, placeholder_id="D4-CAND-01",
                                            **RUN)[H.WRAPPER_KEY]
            for i in r["inputs"]:
                self.assertTrue(i["citation"].startswith("W5-D4-RUN-01/"))
                self.assertTrue(i["reference"].startswith("FIX-"))
                self.assertNotIn("GER-", i["citation"] + i["reference"])
        with self.subTest(obligation="P6", control="a capture-derived specimen is refused"):
            self.assertRaises(H.HarnessRefusal, H.admit_specimen,
                              spec("carried over from GER-0007's variant_a capture"),
                              "W7-D4-SHB")


# ==========================================================================
class H5_ScannerBinding(unittest.TestCase):
    def test_h5_capture_scan_uses_live_logic_with_no_allowlist(self):
        src = Path(H.__file__).read_text(encoding="utf-8")
        with self.subTest(limb="the gateway imports the live scanner, not a copy"):
            self.assertIn("public-safety-scan.py", src)
            self.assertNotIn("re.compile(r\"https?://", src)
        with self.subTest(limb="no allowlist is passed for a capture"):
            self.assertIn("self._s.load_wordlist(), {})", src)
        with self.subTest(limb="the branch bit is derived, not declared"):
            with workspace() as ws:
                gw = H.ScanGateway(ws)
                self.assertIn(gw.branch_state, ("active", "inactive"))
                self.assertEqual(gw.branch_state, gw.sample_branch())
        with self.subTest(limb="a clean capture returns clean with no categories"):
            with workspace() as ws:
                clean, cats = H.ScanGateway(ws).scan_capture("entries are listed as recorded")
                self.assertTrue(clean)
                self.assertEqual(cats, [])
        with self.subTest(limb="a finding returns categories only, never matched text"):
            with workspace() as ws:
                clean, cats = H.ScanGateway(ws).scan_capture(link_trigger())
                self.assertFalse(clean)
                self.assertEqual(cats, ["external-link"])
                for c in cats:
                    self.assertNotIn("example.invalid", c)


# ==========================================================================
class H6_PartQ(unittest.TestCase):
    def test_h6_a_finding_stops_before_any_candidate_exists(self):
        probe = json.loads(json.dumps(one_probe()))
        with self.subTest(limb="a clean pair reaches candidate"):
            with workspace() as ws:
                state, payload = H.run_probe(probe, H.ScanGateway(ws),
                                             placeholder_id="D4-CAND-01", **RUN)
                self.assertEqual(state, "candidate")
                self.assertEqual(payload[H.WRAPPER_KEY]["findings"], [])
                self.assertEqual(
                    {c["scan_status"] for c in payload[H.WRAPPER_KEY]["captures"].values()},
                    {"no_findings"})
        with self.subTest(control="a finding-bearing capture yields stop_and_report"):
            dirty = json.loads(json.dumps(one_probe()))
            dirty["variants"]["variant_a"]["specimen_text"] = link_trigger()
            with workspace() as ws:
                state, payload = H.run_probe(dirty, H.ScanGateway(ws),
                                             placeholder_id="D4-CAND-01", **RUN)
                self.assertEqual(state, "stop_and_report")
                self.assertNotIn(H.WRAPPER_KEY, payload)
                self.assertEqual(payload["categories"], ["external-link"])
        with self.subTest(limb="the stop payload carries no capture text"):
            self.assertNotIn("specimen_text", json.dumps(payload))
        with self.subTest(control="no suppression route exists in the module"):
            src = Path(H.__file__).read_text(encoding="utf-8")
            self.assertIn("if suppressed:", src)
            self.assertNotIn("load_allowlist()", src)


# ==========================================================================
class H7_LocalWordlistPosture(unittest.TestCase):
    def test_h7_one_bit_only_and_a_change_stops_the_run(self):
        with workspace() as ws:
            gw = H.ScanGateway(ws)
            with self.subTest(limb="state is exactly one of the closed pair"):
                self.assertIn(gw.branch_state, ("active", "inactive"))
            with self.subTest(limb="stability check passes when unchanged"):
                self.assertEqual(gw.assert_branch_stable(), gw.branch_state)
            with self.subTest(control="a mid-run change stops before assembly"):
                gw.branch_state = "active" if gw.branch_state == "inactive" else "inactive"
                self.assertRaises(H.HarnessRefusal, gw.assert_branch_stable)
        with self.subTest(limb="the manifest carries the bit and nothing more revealing"):
            man = self._manifest("inactive")["generated_evaluation_run_manifest"]
            self.assertEqual(set(man["scan_environment"]), {"local_wordlist"})
        with self.subTest(control="an out-of-set branch value is refused"):
            self.assertRaises(H.HarnessRefusal, self._manifest, "partially-active")
        with self.subTest(control="extra scan-environment detail is detected"):
            m = self._manifest("inactive")
            m["generated_evaluation_run_manifest"]["scan_environment"]["term_count"] = 3
            self.assertTrue(any("more than the one governed bit" in x
                                for x in H.validate_manifest(m, {})))
        with self.subTest(limb="no wordlist content can reach a caller"):
            src = Path(H.__file__).read_text(encoding="utf-8")
            self.assertNotIn("wordlist)", src.split("def scan_capture")[1].split("return")[0]
                             .replace("self._s.load_wordlist(), {})", ""))

    def _manifest(self, state):
        return H.build_manifest_candidate(run_id="R", authorising_record="W7-D4-SHB",
                                          as_of="2026-08-22", exam_path=EXAM,
                                          branch_state=state, records=[])


# ==========================================================================
class H8_WorkingStateFence(unittest.TestCase):
    def test_h8_every_transient_path_is_outside_the_repository(self):
        with self.subTest(control="no workspace at all is refused"):
            self.assertRaises(H.HarnessRefusal, H.require_external_workspace, None)
        with self.subTest(control="the repository root is refused"):
            self.assertRaises(H.HarnessRefusal, H.require_external_workspace, ROOT)
        with self.subTest(control="a path inside the repository is refused"):
            self.assertRaises(H.HarnessRefusal, H.require_external_workspace, ROOT / "tests")
        with self.subTest(control="the reserved home inside the repository is refused"):
            self.assertRaises(H.HarnessRefusal, H.require_external_workspace,
                              ROOT / "governance" / "generated-evaluation" / "scratch")
        with self.subTest(control="the reserved NAME is refused even outside the repository"):
            # The path above is already caught by the repository rule, so this control
            # exercises the name rule independently: a scratch directory called
            # generated-evaluation anywhere at all is refused.
            with workspace() as ws:
                named = Path(ws) / "generated-evaluation"
                named.mkdir()
                self.assertRaises(H.HarnessRefusal, H.require_external_workspace, named)
        with self.subTest(limb="an external workspace is accepted"):
            with workspace() as ws:
                self.assertEqual(H.require_external_workspace(ws), Path(ws).resolve())
        with self.subTest(limb="a full run leaves no residue in the workspace or the repo"):
            before = self._repo_state()
            with workspace() as ws:
                gw = H.ScanGateway(ws)
                for n, p in enumerate(exam()["probes"][:3], 1):
                    H.run_probe(p, gw, placeholder_id="D4-CAND-%02d" % n, **RUN)
                self.assertEqual(os.listdir(ws), [])
            self.assertEqual(self._repo_state(), before)

    @staticmethod
    def _repo_state():
        out = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                             capture_output=True, text=True, check=True)
        return sorted(out.stdout.split("\n"))


# ==========================================================================
class H9_RecordShapeAssembly(unittest.TestCase):
    def test_h9_assembled_record_satisfies_the_landed_field_law(self):
        record_tbl, capture_tbl = field_tables()
        rec = H.assemble_candidate_record(one_probe(), {"variant_a": "a", "variant_b": "b"},
                                          origins=ORIGINS,
                                          placeholder_id="D4-CAND-01", **RUN)[H.WRAPPER_KEY]
        with self.subTest(limb="record fields match ADR-0049 in order"):
            self.assertEqual(list(rec), [_plain(r[1]) for r in record_tbl])
        with self.subTest(limb="capture fields match ADR-0049 in order"):
            for c in rec["captures"].values():
                self.assertEqual(list(c), [_plain(r[1]) for r in capture_tbl])
        with self.subTest(limb="the ceiling is last and byte-identical to ADR-0046"):
            self.assertEqual(list(rec)[-1], "non_authority")
            self.assertEqual(rec["non_authority"], H._law_text("ceiling"))
        with self.subTest(limb="the synthetic notice is byte-identical to ADR-0049 Part T"):
            self.assertEqual(rec["synthetic_marker"]["notice"], H._law_text("notice"))
            self.assertIs(rec["synthetic_marker"]["synthetic"], True)
        with self.subTest(limb="nullability holds: review disposition stays null before D6"):
            self.assertIsNone(rec["human_review"]["disposition"])
            self.assertIsNone(rec["human_review"]["disposition_record"])
        with self.subTest(limb="no-recirculation and exclusion check are asserted"):
            self.assertIs(rec["no_recirculation"]["capture_terminal"], True)
            self.assertEqual(rec["exclusion_check"]["result"], "no_listed_item_present")
        with self.subTest(limb="text digests are over the decoded text alone"):
            for label, c in rec["captures"].items():
                self.assertEqual(c["text_digest"],
                                 "sha256:" + hashlib.sha256(c["text"].encode()).hexdigest())
        # ---- ADR-0046 P5: the ceiling, verbatim and inside, with specimen parity ----
        ceiling = law_ceiling()
        e = exam()
        with self.subTest(obligation="P5", limb="the exam carries the ceiling at its own level"):
            self.assertEqual(e["non_authority"], ceiling)
        with self.subTest(obligation="P5", limb="all 52 specimens carry it byte-identically"):
            carried = [v["non_authority"] for p in e["probes"] for v in p["variants"].values()]
            self.assertEqual(len(carried), 52)
            self.assertEqual(set(carried), {ceiling})
        with self.subTest(obligation="P5", limb="specimen parity with the generated-output record"):
            self.assertEqual(rec["non_authority"], ceiling)
        with self.subTest(obligation="P5", control="a reworded exam ceiling is refused at load"):
            bad = exam_doc()
            bad["w7_d4_exam"]["probes"][0]["variants"]["variant_a"]["non_authority"] = \
                ceiling.replace("evaluation evidence only", "evaluation evidence")
            self.assertRaises(H.HarnessRefusal, load_doc, bad)
        with self.subTest(obligation="P5", control="an abbreviated ceiling is refused"):
            bad = exam_doc()
            bad["w7_d4_exam"]["probes"][0]["variants"]["variant_b"]["non_authority"] = \
                ceiling.split(".")[0] + "."
            self.assertRaises(H.HarnessRefusal, load_doc, bad)
        with self.subTest(obligation="P5", control="a ceiling moved outside the specimen is refused"):
            bad = exam_doc()
            del bad["w7_d4_exam"]["probes"][0]["variants"]["variant_a"]["non_authority"]
            self.assertRaises(H.HarnessRefusal, load_doc, bad)
        with self.subTest(obligation="P5", control="an exam-level ceiling alone is refused"):
            bad = exam_doc()
            del bad["w7_d4_exam"]["non_authority"]
            self.assertRaises(H.HarnessRefusal, load_doc, bad)


# ==========================================================================
class H10_ManifestShape(unittest.TestCase):
    def test_h10_manifest_is_an_index_and_never_a_summary(self):
        man = H.build_manifest_candidate(run_id="R", authorising_record="W7-D4-SHB",
                                         as_of="2026-08-22", exam_path=EXAM,
                                         branch_state="inactive", records=[])
        m = man["generated_evaluation_run_manifest"]
        with self.subTest(limb="closed top-level shape"):
            self.assertEqual(set(m), {"run_id", "authorising_record", "as_of", "exam",
                                      "scan_environment", "records"})
        with self.subTest(limb="exam reference and hash over exact bytes"):
            self.assertEqual(m["exam"]["content_hash"],
                             "sha256:" + hashlib.sha256(EXAM.read_bytes()).hexdigest())
        with self.subTest(limb="a clean manifest validates"):
            self.assertEqual(H.validate_manifest(man, {}, exam_bytes=EXAM.read_bytes()), [])
        for key in ("summary", "verdict", "score", "winner", "pass_count", "finding_count"):
            with self.subTest(control="forbidden key %s is detected" % key):
                bad = json.loads(json.dumps(man))
                bad["generated_evaluation_run_manifest"][key] = 1
                self.assertTrue(any("forbidden key" in x for x in H.validate_manifest(bad, {})))
        with self.subTest(control="an exam hash mismatch is detected"):
            self.assertTrue(any("exam hash" in x
                                for x in H.validate_manifest(man, {}, exam_bytes=b"other")))
        with self.subTest(control="an arbitrary extra manifest key is detected on shape alone"):
            # "note" is on no blacklist. Only the closed key set can refuse it.
            bad = json.loads(json.dumps(man))
            bad["generated_evaluation_run_manifest"]["note"] = "harmless-looking"
            out = H.validate_manifest(bad, {})
            self.assertTrue(any("closed run-manifest shape" in x for x in out))
            self.assertFalse(any("forbidden key" in x for x in out))
        with self.subTest(control="an arbitrary extra exam-block key is detected"):
            bad = json.loads(json.dumps(man))
            bad["generated_evaluation_run_manifest"]["exam"]["note"] = 1
            self.assertTrue(any("exam block is not the closed shape" in x
                                for x in H.validate_manifest(bad, {})))
        with self.subTest(control="a missing manifest key is detected"):
            bad = json.loads(json.dumps(man))
            del bad["generated_evaluation_run_manifest"]["authorising_record"]
            self.assertTrue(any("closed run-manifest shape" in x
                                for x in H.validate_manifest(bad, {})))
        with self.subTest(control="a reordered manifest is detected"):
            m2 = json.loads(json.dumps(man))["generated_evaluation_run_manifest"]
            reordered = {k: m2[k] for k in reversed(list(m2))}
            self.assertTrue(any("closed run-manifest shape" in x for x in
                                H.validate_manifest(
                                    {"generated_evaluation_run_manifest": reordered}, {})))
        with self.subTest(control="a forbidden name used as a VALUE is caught by the blacklist"):
            # No key set can refuse this: the shape is exact and only the value lies.
            bad = self._entry_manifest("summary")
            out = H.validate_manifest(bad, {"summary": {"content_hash": "sha256:aa",
                                                        "run_id": "R"}})
            self.assertTrue(any("forbidden key" in x for x in out))
        with self.subTest(control="an arbitrary extra record-entry key is detected"):
            bad = self._entry_manifest("X-0001", note="harmless-looking")
            out = H.validate_manifest(bad, {"X-0001": {"content_hash": "sha256:aa",
                                                       "run_id": "R"}})
            self.assertTrue(any("record entry is not the closed shape" in x for x in out))
            self.assertFalse(any("forbidden key" in x for x in out))

    @staticmethod
    def _entry_manifest(record_id, **extra):
        entry = {"record_id": record_id,
                 "path": "governance/generated-evaluation/%s.json" % record_id,
                 "content_hash": "sha256:aa"}
        entry.update(extra)
        return H.build_manifest_candidate(run_id="R", authorising_record="W7-D4-SHB",
                                          as_of="2026-08-22", exam_path=EXAM,
                                          branch_state="inactive", records=[entry])


# ==========================================================================
class H11_ManifestRelation(unittest.TestCase):
    HOME = "governance/generated-evaluation/"

    def _man(self, records, run_id="R"):
        return H.build_manifest_candidate(run_id=run_id, authorising_record="W7-D4-SHB",
                                          as_of="2026-08-22", exam_path=EXAM,
                                          branch_state="inactive", records=records)

    @staticmethod
    def _present(record_id="X-0001", content_hash="sha256:aa", run_id="R"):
        """What a real home would yield: each record's OWN hash and OWN run identity."""
        return {record_id: {"content_hash": content_hash, "run_id": run_id}}

    def test_h11_set_hash_and_run_membership_bite_on_every_named_form(self):
        rec = [{"record_id": "X-0001", "path": self.HOME + "X-0001.json",
                "content_hash": "sha256:aa"}]
        with self.subTest(limb="a complete relation holds"):
            self.assertEqual(H.validate_manifest(self._man(rec), self._present()), [])
        with self.subTest(control="an unlisted present record"):
            present = dict(self._present(), **{"X-0002": {"content_hash": "sha256:bb",
                                                          "run_id": "R"}})
            self.assertTrue(any("unlisted" in x for x in
                                H.validate_manifest(self._man(rec), present)))
        with self.subTest(control="a listed record that is absent"):
            self.assertTrue(any("absent" in x for x in H.validate_manifest(self._man(rec), {})))
        with self.subTest(control="a missing content hash"):
            bad = [{"record_id": "X-0001", "path": self.HOME + "X-0001.json"}]
            self.assertTrue(any("no content hash" in x for x in
                                H.validate_manifest(self._man(bad), self._present())))
        with self.subTest(control="a hash mismatch"):
            self.assertTrue(any("hash mismatch" in x for x in H.validate_manifest(
                self._man(rec), self._present(content_hash="sha256:zz"))))
        with self.subTest(control="a record belonging to another run"):
            # Identifier, path and hash all agree with this manifest. Only the record's
            # own run_id disagrees, so nothing but real membership can catch it.
            out = H.validate_manifest(self._man(rec), self._present(run_id="OTHER-RUN"))
            self.assertTrue(any("belongs to another run" in x for x in out))
            self.assertFalse(any("hash mismatch" in x or "unlisted" in x or "absent" in x
                                 for x in out))
        with self.subTest(control="a record declaring no run at all"):
            present = {"X-0001": {"content_hash": "sha256:aa"}}
            self.assertTrue(any("belongs to another run" in x for x in
                                H.validate_manifest(self._man(rec), present)))
        with self.subTest(limb="run membership is read, never inferred from the identifier"):
            # Same record id, same path, same hash, and a manifest whose run_id was
            # renamed: agreement must follow the record's own declaration.
            self.assertEqual(H.validate_manifest(self._man(rec, run_id="RUN-2"),
                                                 self._present(run_id="RUN-2")), [])
        with self.subTest(control="a duplicate listing"):
            self.assertTrue(any("more than once" in x for x in
                                H.validate_manifest(self._man(rec + rec), self._present())))
        with self.subTest(control="a record path outside the reserved home"):
            out = [{"record_id": "X-0001", "path": "docs/X-0001.json",
                    "content_hash": "sha256:aa"}]
            self.assertTrue(any("outside the reserved home" in x for x in
                                H.validate_manifest(self._man(out), self._present())))
        for label, path in (("traversal", self.HOME + "../../etc/X-0001.json"),
                            ("root-absolute", "/" + self.HOME + "X-0001.json"),
                            ("drive-rooted", "C:/" + self.HOME + "X-0001.json"),
                            ("backslash", self.HOME + ".." + chr(92) + "X-0001.json")):
            with self.subTest(control="a %s path cannot escape the home" % label):
                esc = [{"record_id": "X-0001", "path": path, "content_hash": "sha256:aa"}]
                self.assertTrue(any("outside the reserved home" in x for x in
                                    H.validate_manifest(self._man(esc), self._present())))
        with self.subTest(control="the manifest listing itself"):
            self_listed = [{"record_id": "R", "path": self.HOME + "R.json",
                            "content_hash": "sha256:aa"}]
            self.assertTrue(any("lists itself" in x for x in H.validate_manifest(
                self._man(self_listed), self._present(record_id="R"))))


# ==========================================================================
class H12_ProofSuccession(unittest.TestCase):
    """The successor invariant runs now against disposable homes. It is not yet
    live over a real home, and this module does not claim that it is."""

    @staticmethod
    def successor(home, manifest, *, exam_bytes):
        """Read the home as D5 would: each record's own bytes and its own run identity."""
        present = {}
        for f in sorted(Path(home).glob("*.json")):
            body = f.read_bytes()
            try:
                doc = json.loads(body.decode("utf-8"))
                run_id = (doc.get(H.WRAPPER_KEY) or {}).get("run_id")
            except (ValueError, AttributeError):
                run_id = None
            present[f.stem] = {"content_hash": "sha256:" + hashlib.sha256(body).hexdigest(),
                               "run_id": run_id}
        return H.validate_manifest(manifest, present, exam_bytes=exam_bytes,
                                   home_prefix=Path(home).name + "/")

    @staticmethod
    def _record_bytes(run_id, marker):
        return json.dumps({H.WRAPPER_KEY: {"run_id": run_id, "x": marker}}).encode("utf-8")

    def test_h12_vacancy_holds_now_and_the_successor_bites_on_fakes(self):
        with self.subTest(limb="the reserved home is still absent in the live repository"):
            self.assertFalse(H.RESERVED_HOME.exists())
            out = subprocess.run(["git", "ls-files", "--", "governance/generated-evaluation/"],
                                 cwd=ROOT, capture_output=True, text=True, check=True)
            self.assertEqual(out.stdout.split(), [])
        with workspace() as ws:
            home = Path(ws) / "generated-evaluation"
            home.mkdir()
            body = self._record_bytes("R", 1)
            (home / "X-0001.json").write_bytes(body)
            good = H.build_manifest_candidate(
                run_id="R", authorising_record="W7-D4-SHB", as_of="2026-08-22", exam_path=EXAM,
                branch_state="inactive",
                records=[{"record_id": "X-0001", "path": "generated-evaluation/X-0001.json",
                          "content_hash": "sha256:" + hashlib.sha256(body).hexdigest()}])
            with self.subTest(limb="a lawful disposable home validates"):
                self.assertEqual(self.successor(home, good, exam_bytes=EXAM.read_bytes()), [])
            with self.subTest(control="an unlisted file in the home is detected"):
                (home / "X-0002.json").write_bytes(self._record_bytes("R", 2))
                self.assertTrue(any("unlisted" in x for x in
                                    self.successor(home, good, exam_bytes=EXAM.read_bytes())))
            with self.subTest(control="a silently edited record is detected"):
                (home / "X-0002.json").unlink()
                (home / "X-0001.json").write_bytes(self._record_bytes("R", 2))
                self.assertTrue(any("hash mismatch" in x for x in
                                    self.successor(home, good, exam_bytes=EXAM.read_bytes())))
            with self.subTest(control="a record from another run in the home is detected"):
                # Written to the listed hash so the index agrees on every other count.
                other = self._record_bytes("OTHER-RUN", 1)
                (home / "X-0001.json").write_bytes(other)
                listed = H.build_manifest_candidate(
                    run_id="R", authorising_record="W7-D4-SHB", as_of="2026-08-22",
                    exam_path=EXAM, branch_state="inactive",
                    records=[{"record_id": "X-0001",
                              "path": "generated-evaluation/X-0001.json",
                              "content_hash": "sha256:" + hashlib.sha256(other).hexdigest()}])
                out = self.successor(home, listed, exam_bytes=EXAM.read_bytes())
                self.assertTrue(any("belongs to another run" in x for x in out))
                self.assertFalse(any("hash mismatch" in x for x in out))
        with self.subTest(boundary="the successor is not claimed live over a real home"):
            doc = " ".join(H12_ProofSuccession.__doc__.split())
            self.assertIn("It is not yet live over a real home", doc)
            self.assertIn("this module does not claim that it is", doc)


# ==========================================================================
class H13_MaterialisationFenceAndGatePrecedence(unittest.TestCase):
    def test_h13_no_production_path_can_write_into_the_repository(self):
        src = Path(H.__file__).read_text(encoding="utf-8")
        with self.subTest(limb="no write call targets the reserved home"):
            self.assertNotIn("RESERVED_HOME /", src)
            self.assertNotIn("RESERVED_HOME.mkdir", src)
        with self.subTest(limb="the only file write is into a validated external workspace"):
            self.assertEqual(src.count("os.fdopen"), 1)
            self.assertIn("dir=str(self.workspace)", src)
        with self.subTest(control="a GER-shaped placeholder is refused"):
            self.assertRaises(H.HarnessRefusal, H.assemble_candidate_record,
                              one_probe(), {"variant_a": "a", "variant_b": "b"},
                              origins=ORIGINS, placeholder_id="GER-0001", **RUN)
        with self.subTest(limb="no GER identifier is allocated anywhere in the repository"):
            reg = json.loads((ROOT / "governance/registry.json").read_bytes().decode("utf-8"))
            self.assertEqual([e["id"] for e in reg["entries"]
                              if e["id"].startswith("GER-")], [])
        with self.subTest(limb="the harness declares no run-manifest writer"):
            self.assertNotIn("def write_manifest", src)
            self.assertNotIn("def materialise", src)
        # ---- ADR-0047 Q4: gate precedence, read from history, not asserted --------
        gates = {
            "record shape ADR-0048":
                "docs/decisions/0048-generated-evaluation-record-shape-doctrine.md",
            "record shape ADR-0049": "docs/decisions/0049-generated-evaluation-field-law.md",
            "record shape ADR-0050":
                "docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md",
            "record shape W7-D2-E": "docs/phases/W7-D2-E-proof-completion-record.md",
            "model boundary ADR-0051": "docs/decisions/0051-model-boundary-no-public-contact.md",
        }
        head = git_out("rev-parse", "HEAD").strip()
        commits = {k: introducing_commit(v) for k, v in gates.items()}
        registry = json.loads((ROOT / "governance/registry.json").read_bytes().decode("utf-8"))
        status = {e["path"]: e["status"] for e in registry["entries"]}
        with self.subTest(obligation="Q4", limb="every gate is published in this history"):
            for name, commit in commits.items():
                self.assertIsNotNone(commit, name)
                self.assertTrue(precedes(commit, head) or commit == head, name)
        with self.subTest(obligation="Q4", limb="every gate is accepted, not merely present"):
            for name, path in gates.items():
                self.assertEqual(status.get(path), "accepted", name)
        with self.subTest(obligation="Q4", limb="the record-shape gate precedes the boundary gate"):
            boundary = commits["model boundary ADR-0051"]
            for name in [k for k in gates if k.startswith("record shape")]:
                self.assertTrue(precedes(commits[name], boundary), name)
        artefact = introducing_commit(P4_CLASS_ARTEFACT)
        with self.subTest(obligation="Q4", limb="the first class artefact comes after both gates"):
            if artefact is None:
                # Not yet landed. It can only enter history as a descendant of HEAD, and
                # HEAD already contains every gate, so precedence holds by construction
                # rather than by promise.
                for name, commit in commits.items():
                    self.assertTrue(precedes(commit, head), name)
            else:
                for name, commit in commits.items():
                    self.assertTrue(precedes(commit, artefact), name)
                    self.assertFalse(precedes(artefact, commit), name)
        with self.subTest(obligation="Q4", control="the precedence predicate is directional"):
            first = commits["record shape ADR-0048"]
            later = commits["model boundary ADR-0051"]
            self.assertTrue(precedes(first, later))
            self.assertFalse(precedes(later, first))
            self.assertFalse(precedes(first, first))
        with self.subTest(obligation="Q4", control="an unpublished gate would be detected"):
            self.assertIsNone(introducing_commit("docs/decisions/0099-not-a-record.md"))


# ==========================================================================
class H14_BoundaryContract(unittest.TestCase):
    def test_h14_module_states_what_green_does_not_mean(self):
        flat = " ".join(__doc__.split())
        for clause in ("that any model was contacted",
                       "that any model behaviour, quality, correctness or safety was tested",
                       "that any trap has been behaviourally passed",
                       "that any of the twenty-six unknowns has been answered about a real model",
                       "that Part Q is resolved",
                       "that the local-wordlist coordinate seam is resolved",
                       "that ADR-0047 precondition 3 is discharged",
                       "that precondition 7 is discharged",
                       "that W7-D5 is open"):
            with self.subTest(clause=clause[:46]):
                self.assertIn(clause, flat)
        with self.subTest(limb="the subject is named as an instrument, never a model"):
            self.assertIn("THE SUBJECT OF THIS MODULE IS AN INSTRUMENT AND A DOCUMENT, "
                          "NEVER A MODEL", __doc__)


if __name__ == "__main__":
    unittest.main()
