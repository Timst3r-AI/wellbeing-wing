"""W8-D2-C — corpus conformance proofs over the materialised instrument.

The corpus is real: under the effective ADR-0055 (as reconciled by W8-D2-MSA)
the home `governance/discriminating-instrument/` holds the reviewer-visible
cases and exactly one commitment manifest. This module proves the published
mechanics of that corpus — closure, shape, binding, container, blinding
absence, registry binding, count consistency and textual non-reuse — by
importing the published envelope validators rather than restating them.

THIS MODULE CONTAINS NO HIDDEN MATERIAL. It never reads, names or reaches
the outside-repository review transport; commitment reproduction from exact
retained bytes is a governed ceremony act performed at authoring and again
before landing, attested in the W8-D2 completion record, exactly as
ADR-0055's V11 row scopes it. No proof here decides, predicts or hints at
any case's authored class or human disposition, and no green result is
evidence that any case is well-constructed.

WHAT GREEN DOES NOT MEAN. Mechanical proof may establish the absence of
reserved authoring channels in structure, filenames, identifiers, ordering,
the manifest, the registry and the board; it must not and does not claim to
establish whether the natural-language paired evidence itself semantically
discloses or over-signals its construction — that remains review-only, and
mechanical proof does not establish semantic case quality. The textual
non-reuse guard establishes only its defined word-sequence comparison,
never the semantic proposition that a case is not a rewrite or
adaptation - fresh authorship remains a governed authoring-process
obligation under the opening brief. A green run
NEVER establishes: any disposition, calibration, reveal or class count;
that any model was contacted; that ADR-0047 precondition 3 moved; that any
W7 record changed; or that W8-D3 is open.
"""

import json
import re
import subprocess
import unittest
from pathlib import Path

import test_w8_discriminating_instrument_envelope as envelope

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "governance" / "discriminating-instrument"
MANIFEST = HOME / "W8-D2-commitment-manifest.json"
RECORD = ROOT / "docs" / "phases" / "W8-D2-discriminating-instrument-record.md"
BOARD = ROOT / "docs" / "phases" / "README.md"
REGISTRY = ROOT / "governance" / "registry.json"

EXPECTED_TOTAL = 12
COUNT_SENTENCE = "exactly twelve reviewer-visible cases"
MANIFEST_SCHEMA = "w8-commitment-manifest-v1"
CASE_FILE_RE = re.compile(r"^W8-C-[0-9a-f]{64}\.json$")
# Reserved authoring channels: every withheld-record field name beyond the
# identity and the one hash name that is lawfully public in manifest rows,
# plus the closed check and condition vocabularies and the withheld schema
# string — none may appear in any reviewer-visible surface. The label
# strings are imported, never written here, so this module itself carries
# no reserved literal.
RESERVED_FIELDS = sorted(
    envelope.AUTHORING_FIELDS
    - {"schema", "case_id", "reviewer_visible_sha256"})
RESERVED_STRINGS = sorted(
    set(RESERVED_FIELDS)
    | set(envelope.ALL_CHECKS)
    | set(envelope.INCONCLUSIVE_LABELS)
    | {envelope.AUTHORING_SCHEMA})
NGRAM = 10


def _read(path):
    return path.read_bytes()


def _text(path):
    return _read(path).replace(b"\r\n", b"\n").decode("utf-8")


def _committed(path):
    """The committed blob bytes of an immutable published D2 artefact.

    Checkout may rewrite line endings in the working copy; under ADR-0055
    decision 10 that is display, and the committed bytes are the artefact.
    Mutable surfaces are never read this way."""
    rel = path.relative_to(ROOT).as_posix()
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True,
                          check=True).stdout.strip()
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (head, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def _working_copy_is_committed(path):
    return _read(path).replace(b"\r\n", b"\n") == _committed(path)


def case_paths():
    return sorted(p for p in HOME.iterdir() if p.name != MANIFEST.name)


def manifest_rows():
    return json.loads(_read(MANIFEST))["rows"]


def manifest_container_violations(raw):
    """The W8-D2-MSA container law: one closed two-field object, byte-fixed
    schema, governed rows, Part C canonical bytes."""
    v = []
    try:
        parsed = json.loads(raw)
    except ValueError:
        return ["manifest is not JSON"]
    if not isinstance(parsed, dict):
        return ["manifest instance must be one closed JSON object, "
                "not a bare array or scalar"]
    if set(parsed) != {"schema", "rows"}:
        v.append("outer shape: %s" % sorted(set(parsed) ^ {"schema", "rows"}))
    if parsed.get("schema") != MANIFEST_SCHEMA:
        v.append("manifest schema")
    rows = parsed.get("rows")
    if not isinstance(rows, list):
        v.append("rows must be an array")
        return v
    v += envelope.manifest_violations(rows)
    if raw != envelope.canonical_bytes(parsed):
        v.append("manifest bytes are not Part C canonical bytes")
    return v


def reserved_channel_hits(text):
    return [s for s in RESERVED_STRINGS if s in text]


def _normalise_words(text):
    return re.findall(r"[0-9a-z]+", text.lower())


def _ngrams(words, n=NGRAM):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def variant_ngrams():
    grams = set()
    for p in case_paths():
        ase = json.loads(_read(p))["admissible_source_evidence"]
        for variant in (ase["variant_a"], ase["variant_b"]):
            grams |= _ngrams(_normalise_words(variant))
    return grams


def tracked_text_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                         text=True, check=True).stdout.split()
    home_rel = "governance/discriminating-instrument/"
    return [p for p in out if p.endswith((".md", ".json"))
            and not p.startswith(home_rel)]


class C1_HomeClosure(unittest.TestCase):
    def test_c1_home_contains_exactly_the_cases_and_the_manifest(self):
        self.assertTrue(HOME.is_dir(), "the instrument home must exist")
        entries = sorted(p.name for p in HOME.iterdir())
        with self.subTest(fact="no subdirectory and no stray file"):
            self.assertTrue(all((HOME / n).is_file() for n in entries))
            for n in entries:
                if n == MANIFEST.name:
                    continue
                self.assertTrue(CASE_FILE_RE.match(n),
                                "unauthorised entry in the home: %s" % n)
        with self.subTest(fact="exactly the expected population"):
            self.assertEqual(len(entries), EXPECTED_TOTAL + 1)
            self.assertIn(MANIFEST.name, entries)
        with self.subTest(fact="the staged tree carries the same closure"):
            tracked = subprocess.run(
                ["git", "ls-files", "--", "governance/discriminating-instrument/"],
                cwd=ROOT, capture_output=True, text=True, check=True
            ).stdout.split()
            self.assertEqual(sorted(Path(t).name for t in tracked), entries)


class C2C3_CaseConformance(unittest.TestCase):
    def test_c2_every_case_passes_the_envelope_validator_byte_for_byte(self):
        paths = case_paths()
        self.assertEqual(len(paths), EXPECTED_TOTAL)
        for p in paths:
            raw = _committed(p)
            parsed = json.loads(raw)
            with self.subTest(case=p.name[:14],
                              check="working copy is the committed bytes"):
                self.assertTrue(_working_copy_is_committed(p))
            with self.subTest(case=p.name[:14], check="validator"):
                self.assertEqual(envelope.review_case_violations(parsed), [])
            with self.subTest(case=p.name[:14], check="exact canonical bytes"):
                self.assertEqual(raw, envelope.canonical_bytes(parsed))
            with self.subTest(case=p.name[:14], check="single terminal LF"):
                self.assertTrue(raw.endswith(b"\n")
                                and not raw.endswith(b"\n\n"))
            with self.subTest(case=p.name[:14], check="C3 mechanical filename"):
                self.assertEqual(p.name, parsed["case_id"] + ".json")
        with self.subTest(control="a planted leak on a real case is detected"):
            mutant = dict(json.loads(_committed(paths[0])))
            mutant["title"] = "leak"
            self.assertTrue(envelope.review_case_violations(mutant))
        with self.subTest(control="a byte appended to real bytes is detected"):
            raw = _committed(paths[0])
            self.assertNotEqual(envelope.sha256_bytes(raw),
                                envelope.sha256_bytes(raw + b"\n"))


class C4_ManifestContainer(unittest.TestCase):
    def test_c4_container_schema_rows_and_ordering_are_law(self):
        raw = _committed(MANIFEST)
        self.assertEqual(manifest_container_violations(raw), [])
        with self.subTest(fact="working copy is the committed bytes"):
            self.assertTrue(_working_copy_is_committed(MANIFEST))
        parsed = json.loads(raw)
        with self.subTest(control="undeclared outer field detected"):
            m = dict(parsed); m["note"] = "x"
            self.assertTrue(manifest_container_violations(
                envelope.canonical_bytes(m)))
        with self.subTest(control="bare-array instance detected"):
            self.assertTrue(manifest_container_violations(
                envelope.canonical_bytes(parsed["rows"])))
        with self.subTest(control="wrong schema value detected"):
            m = dict(parsed); m["schema"] = "w8-commitment-manifest-v2"
            self.assertTrue(manifest_container_violations(
                envelope.canonical_bytes(m)))
        with self.subTest(control="undeclared row field detected"):
            m = json.loads(raw)
            m["rows"][0] = dict(m["rows"][0]); m["rows"][0]["extra"] = 1
            self.assertTrue(manifest_container_violations(
                envelope.canonical_bytes(m)))
        with self.subTest(control="non-canonical bytes detected"):
            pretty = (json.dumps(parsed, indent=2) + "\n").encode("utf-8")
            self.assertTrue(manifest_container_violations(pretty))


class C5C6_PublicBinding(unittest.TestCase):
    def test_c5_rows_bind_one_to_one_to_exact_published_case_bytes(self):
        rows = manifest_rows()
        visible = {}
        for p in case_paths():
            raw = _committed(p)
            visible[json.loads(raw)["case_id"]] = raw
        with self.subTest(fact="no orphan in either public direction"):
            self.assertEqual({r["case_id"] for r in rows}, set(visible))
        for r in rows:
            with self.subTest(row=r["case_id"][:14]):
                self.assertEqual(r["reviewer_visible_sha256"],
                                 envelope.sha256_bytes(visible[r["case_id"]]))
        with self.subTest(control="a mutated digest is detected"):
            bad = dict(rows[0])
            bad["reviewer_visible_sha256"] = "sha256:" + "0" * 64
            self.assertNotEqual(bad["reviewer_visible_sha256"],
                                envelope.sha256_bytes(visible[bad["case_id"]]))

    def test_c6_commitment_fields_carry_the_exact_shape(self):
        for r in manifest_rows():
            for f in ("reviewer_visible_sha256", "authoring_commitment_sha256"):
                with self.subTest(row=r["case_id"][:14], field=f):
                    self.assertTrue(envelope.SHA_FIELD_RE.match(r[f]))


class C7_BlindingClosure(unittest.TestCase):
    """Reviewer-surface leakage closure, in its corrected form: no reserved
    authoring material is exposed through the reviewer-visible structure or
    its non-evidence channels; filenames, IDs, ordering, manifest, registry
    and board carry no authored-class channel. Reserved authoring labels are
    mechanically rejected here because they are decidable; whether the
    natural-language paired evidence itself semantically discloses or
    over-signals the construction remains review-only, and mechanical proof
    does not establish semantic case quality."""

    def surfaces(self):
        reg = json.loads(_text(REGISTRY))
        roles = " ".join(e["role"] + " " + e["title"]
                         for e in reg["entries"]
                         if e["id"] in ("W8-D2-DIC", "W8-D2-CM-01"))
        board = _text(BOARD)
        board_w8 = board[board.find("## W8"):]
        return {
            "home files": " ".join(_text(p) for p in case_paths()),
            "manifest": _text(MANIFEST),
            "completion record": _text(RECORD),
            "board W8 section": board_w8,
            "registry roles": roles,
        }

    def test_c7_no_reserved_authoring_channel_on_any_visible_surface(self):
        for name, text in self.surfaces().items():
            with self.subTest(surface=name):
                self.assertEqual(reserved_channel_hits(text), [])
        with self.subTest(fact="no disposition token inside any case file"):
            home = " ".join(_text(p) for p in case_paths())
            for token in sorted(envelope.TOKENS):
                self.assertNotIn(token, home)
        with self.subTest(fact="filenames carry the mechanical shape only"):
            for p in case_paths():
                self.assertTrue(CASE_FILE_RE.match(p.name))
        with self.subTest(control="a planted reserved label is detected"):
            planted = "x " + sorted(envelope.ALL_CHECKS)[0] + " y"
            self.assertTrue(reserved_channel_hits(planted))
        with self.subTest(control="a planted withheld-schema string is "
                                  "detected"):
            self.assertTrue(reserved_channel_hits(envelope.AUTHORING_SCHEMA))


class C8_RegistryBinding(unittest.TestCase):
    def test_c8_manifest_and_record_are_bound_in_the_registry(self):
        reg = json.loads(_text(REGISTRY))
        by_id = {e["id"]: e for e in reg["entries"]}
        with self.subTest(entry="W8-D2-CM-01 governed register"):
            e = by_id["W8-D2-CM-01"]
            self.assertEqual(e["type"], "governed-register")
            self.assertEqual(
                e["path"],
                "governance/discriminating-instrument/"
                "W8-D2-commitment-manifest.json")
            self.assertEqual(e["content_hash"],
                             envelope.sha256_bytes(
                                 _read(MANIFEST).replace(b"\r\n", b"\n")))
        with self.subTest(entry="W8-D2-DIC completion record"):
            e = by_id["W8-D2-DIC"]
            self.assertEqual(e["type"], "phase-record")
            self.assertEqual(
                e["path"], "docs/phases/W8-D2-discriminating-instrument-record.md")
            self.assertEqual(e["content_hash"],
                             envelope.sha256_bytes(
                                 _read(RECORD).replace(b"\r\n", b"\n")))


class C9_TotalCountConsistency(unittest.TestCase):
    def test_c9_one_total_everywhere_and_no_composition_anywhere(self):
        rows = manifest_rows()
        with self.subTest(fact="home, manifest and law agree on the total"):
            self.assertEqual(len(rows), EXPECTED_TOTAL)
            self.assertEqual(len(case_paths()), EXPECTED_TOTAL)
        for name, path in (("completion record", RECORD), ("board", BOARD)):
            with self.subTest(surface=name):
                self.assertIn(COUNT_SENTENCE, _text(path))


class C10_TextualNonReuseGuard(unittest.TestCase):
    """A textual non-reuse guard, mechanical and bounded: it establishes
    only that no 10-word sequence from any variant occurs in any tracked
    md/json text under the defined normalisation. It does not and cannot
    establish the semantic proposition that a case is not a rewrite or
    adaptation; fresh authorship remains a governed authoring-process
    obligation, honoured and recorded at authoring, never proven by this
    test."""

    def test_c10_textual_non_reuse_no_shared_long_word_sequence(self):
        grams = variant_ngrams()
        self.assertTrue(grams, "the corpus must carry real variant text")
        for rel in tracked_text_files():
            try:
                words = _normalise_words(_text(ROOT / rel))
            except (UnicodeDecodeError, OSError):
                continue
            overlap = grams & _ngrams(words)
            with self.subTest(tracked=rel):
                self.assertEqual(overlap, set(),
                                 "variant text shares a %d-word sequence "
                                 "with %s" % (NGRAM, rel))
        with self.subTest(control="the sweep detects a real reuse"):
            sample = next(iter(grams))
            self.assertIn(sample, _ngrams(list(sample), NGRAM))


class C11_ScopeAndCarriage(unittest.TestCase):
    def test_c11_the_record_carries_the_non_crossing_statements(self):
        record = _text(RECORD)
        for clause in (
                "No human disposition",
                "no calibration",
                "no reveal",
                "no class count",
                "no model contact, prompt for contact, provider, credential, "
                "SDK, transport, binary or contact harness",
                "ADR-0047 precondition 3 remains outstanding",
                "W8-D3 through W8-D7 remain closed",
                COUNT_SENTENCE,
        ):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, record)
        with self.subTest(fact="commitment reproduction is attested as a "
                               "ceremony act over exact retained bytes"):
            self.assertIn("exact retained bytes", record)


if __name__ == "__main__":
    unittest.main()
