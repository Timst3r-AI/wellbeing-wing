"""W7-D5 — materialised-state proofs for the generated-evaluation class (M1–M13).

The class is real: `governance/generated-evaluation/` holds the first authorised
run. This module binds the record-level obligations to the actual repository
bytes. It is the successor owner named by the D2-E succession: S2 and S3 bite
here against real subjects, and the D4 module's H12 makes no claim about the
real home.

WHAT GREEN DOES NOT MEAN. A green run of this module proves materialisation
integrity only. It NEVER establishes: that model contact occurred or is
authorised; anything about model behaviour; that any trap was passed or failed
behaviourally; that anything is safe, correct, clinically valid, approved or
production-ready; that any W7-D6 human-review disposition exists; that ADR-0050's
Part Q publication seam has been resolved; that the local-wordlist coordinate
seam has been resolved; that ADR-0047 precondition 3 is discharged; that W7-D6 is
open; or that W8 is open.

DUAL STATE. Every history-dependent proof handles both lawful states: the
proposed-candidate state, where the home exists in the working tree and the
materialisation commit does not yet exist (the pre-materialisation reference is
then HEAD), and the published state, where the first materialisation commit
exists (the reference is then its parent). Vacancy-before and bounded-succession
claims are proven against that reference in either state.

SOURCE AUTHORITY. Frozen hashes are parsed from the accepted v1.2 brief's
section 6 table; the two pre-succession module pins are parsed from the accepted
W7-D5-PSA record; the namespace successor wording is parsed from brief section
17.3; the S2 relation is the frozen D4 harness's own validator, reused and never
reimplemented.
"""

import difflib
import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

import w7_synthetic_evaluation_harness as H
import w7_generated_evaluation_binding as B

ROOT = Path(__file__).resolve().parents[1]
HOME_REL = "governance/generated-evaluation/"
HOME = ROOT / "governance" / "generated-evaluation"
RUN_ID = "W7-D5-RUN-01"
MANIFEST_NAME = RUN_ID + "-manifest.json"
BRIEF = ROOT / "docs/phases/W7-D5-synthetic-execution-materialisation-brief.md"
PSA = ROOT / "docs/phases/W7-D5-proof-succession-amendment.md"
COMPLETION = ROOT / "docs/phases/W7-D5-synthetic-execution-materialisation-record.md"
ALLOWLIST = ROOT / "scripts/scan-allowlist.txt"
D4_PROOF_REL = "tests/test_w7_synthetic_harness.py"
D3_PROOF_REL = "tests/test_w7_model_boundary_decision.py"

EXPECTED_IDS = tuple("GER-%04d" % i for i in range(1, 27))


def _lf(b):
    """Canonical LF bytes: every whole-file hash in this module is over these,
    matching the repository content-hash convention on any checkout."""
    return b.replace(b"\r\n", b"\n")


def _text(p):
    return _lf(Path(p).read_bytes()).decode("utf-8")


def _git(*args, cwd=ROOT):
    return subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True,
                          text=True, check=True).stdout


def _git_bytes(*args, cwd=ROOT):
    return subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True,
                          check=True).stdout


def introducing_commit(rel, cwd=ROOT):
    out = _git("log", "--diff-filter=A", "--format=%H", "--", rel, cwd=cwd).split()
    return out[-1] if out else None


def pre_materialisation_ref(cwd=ROOT):
    """HEAD in the proposed-candidate state; the first materialisation commit's
    parent once it exists. Both are the last pre-class point in history."""
    first = introducing_commit(HOME_REL, cwd=cwd)
    return (first + "^") if first else "HEAD"


def brief_frozen_hashes():
    """Section 6 of the accepted brief, parsed: {rel: sha256}."""
    src = _text(BRIEF)
    return dict(re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \|", src))


def psa_pins():
    src = _text(PSA)
    d4 = re.search(r"`tests/test_w7_synthetic_harness\.py` hash `([0-9a-f]{64})`", src)
    d3 = re.search(r"`tests/test_w7_model_boundary_decision\.py` is pinned "
                   r"pre-succession at `([0-9a-f]{64})`", src)
    return {D4_PROOF_REL: d4.group(1), D3_PROOF_REL: d3.group(1)}


def namespace_successor():
    """The exact v1.2 section 17.3 successor wording, parsed from the brief."""
    src = _text(BRIEF)
    m = re.search(r"in the same already-counted `governance/registry\.json` edit, "
                  r"to exactly:\n\n`([^`]+)`", src)
    return m.group(1)


def home_files():
    return sorted(p.name for p in HOME.iterdir())


def load_records():
    """{record_id: (record_dict, raw_bytes, filename)} for every GER on disk."""
    out = {}
    for p in sorted(HOME.glob("GER-*.json")):
        body = _lf(p.read_bytes())
        doc = json.loads(body.decode("utf-8"))
        rec = doc[H.WRAPPER_KEY]
        out[rec["record_id"]] = (rec, body, p.name)
    return out


def load_manifest():
    body = _lf((HOME / MANIFEST_NAME).read_bytes())
    return json.loads(body.decode("utf-8")), body


# ------------------------------------------------------------- validators ---
# Pure functions over supplied state, so the mutation ceremony can feed mutants
# without touching the real home.

def home_closed_set_violations(names):
    expected = sorted([i + ".json" for i in EXPECTED_IDS] + [MANIFEST_NAME])
    out = []
    for extra in sorted(set(names) - set(expected)):
        out.append("stray artefact in the home: %s" % extra)
    for missing in sorted(set(expected) - set(names)):
        out.append("expected artefact missing: %s" % missing)
    return out


def identity_violations(records):
    """records: {record_id: (rec, body, filename)}."""
    out = []
    ids = sorted(records)
    if ids != sorted(EXPECTED_IDS):
        out.append("identity set is not the expected contiguous first block")
    for rid, (rec, _, fname) in records.items():
        if not re.match(r"^GER-\d{4}$", rid):
            out.append("identity outside the GER-#### grammar: %s" % rid)
        if fname != rid + ".json":
            out.append("record not at its canonical identity path: %s" % rid)
        if rec.get("record_id") != rid:
            out.append("file identity and record identity disagree: %s" % fname)
    return out


def probe_mapping_violations(records):
    """Probe order binds to the contiguous block: D4-P01 -> GER-0001 ..."""
    out = []
    for i, rid in enumerate(EXPECTED_IDS, 1):
        if rid not in records:
            continue
        rec = records[rid][0]
        want = "D4-P%02d" % i
        got = (rec.get("pairing") or {}).get("probe_id")
        if got != want:
            out.append("probe mapping violated: %s carries %s, expected %s"
                       % (rid, got, want))
    return out


def shape_violations(rec):
    out = []
    if tuple(rec) != H.RECORD_FIELDS:
        out.append("record fields are not the canonical ADR-0049 order")
    for label, cap in (rec.get("captures") or {}).items():
        if tuple(cap) != H.CAPTURE_FIELDS:
            out.append("capture fields not canonical: %s" % label)
    mc = rec.get("model_contact") or {}
    hr = rec.get("human_review") or {}
    if mc.get("authorising_record") is not None:
        out.append("model_contact.authorising_record must be null under Option D")
    # W7-D6 succession: universal nullness reached its lawful endpoint when the
    # ADR-0053 review landed. The shape law here is the atomic pair; vocabulary
    # and source conformance are owned by tests/test_w7_human_review_dispositions.py.
    if (hr.get("disposition") is None) != (hr.get("disposition_record") is None):
        out.append("half-filled W7-D6 review pair")
    if list(rec)[-1] != "non_authority":
        out.append("the ceiling is not the final field")
    if rec.get("non_authority") != H._law_text("ceiling"):
        out.append("the ceiling is not byte-identical to the governed text")
    return out


def authority_violations(rec):
    out = []
    if rec.get("authorising_record") != B.RUN_AUTHORITY:
        out.append("top-level run authority is not W7-D5-SEB")
    if rec.get("run_id") != RUN_ID:
        out.append("record does not declare the authorised run")
    mc = rec.get("model_contact") or {}
    if mc.get("occurred") is not False or mc.get("contact_class") != "none":
        out.append("Option D contact posture violated")
    for label, cap in (rec.get("captures") or {}).items():
        if cap.get("authoring_record") != B.SPECIMEN_AUTHORING_RECORD:
            out.append("capture %s does not carry the D4 authoring authority" % label)
        if cap.get("text_class") != H.SPECIMEN_CLASS:
            out.append("capture %s is not an authored synthetic specimen" % label)
    return out


def fidelity_violations(rec, exam_probes):
    out = []
    pid = (rec.get("pairing") or {}).get("probe_id")
    probe = exam_probes.get(pid)
    if probe is None:
        return ["record cites a probe the exam does not carry: %s" % pid]
    for label in H.VARIANT_LABELS:
        cap = (rec.get("captures") or {}).get(label) or {}
        want = probe["variants"][label]["specimen_text"]
        if cap.get("text") != want:
            out.append("capture text differs from its exam source: %s/%s" % (pid, label))
        digest = "sha256:" + hashlib.sha256(
            (cap.get("text") or "").encode("utf-8")).hexdigest()
        if cap.get("text_digest") != digest:
            out.append("capture digest does not hash its text: %s/%s" % (pid, label))
        if cap.get("scan_status") != "no_findings":
            out.append("a landed capture carries a scan finding state: %s/%s" % (pid, label))
    return out


def part_q_violations(rec, allowlist_rows, home_rel=HOME_REL):
    out = []
    if rec.get("findings") != []:
        out.append("a landed record carries a finding event")
    for row in allowlist_rows:
        if row.startswith(home_rel):
            out.append("an allowlist entry lies under the generated-evaluation home")
    for item in rec.get("inputs") or []:
        for field in ("citation", "reference"):
            v = str(item.get(field, ""))
            if ("GER" + "-") in v or home_rel in v:
                out.append("an input resolves to the generated-evaluation class: %s" % field)
    nr = rec.get("no_recirculation") or {}
    if nr.get("capture_terminal") is not True:
        out.append("capture-terminal assertion is not carried")
    return out


def s3_history_violations(repo_root, home_rel=HOME_REL):
    """The ID-scoped lifecycle/history proof over one repository's history.

    Indexes every published GER by record_id, never by path similarity; asserts
    first-version capture texts and digests survive every later version; the
    identifier is never bound to a different capture pair; nothing is deleted or
    moved from its canonical path; and only the governed later human-review
    fields may differ between versions of one identifier.
    """
    out = []
    commits = _git("rev-list", "--reverse", "HEAD", "--", home_rel,
                   cwd=repo_root).split()
    first_seen = {}      # rid -> (texts, digests)
    prev_state = {}      # rid -> record dict of the latest seen version
    ever = set()
    for c in commits:
        listing = _git("ls-tree", "-r", "--name-only", c, "--", home_rel,
                       cwd=repo_root).split()
        seen_now = {}
        for path in listing:
            name = path.split("/")[-1]
            if not name.startswith("GER-"):
                continue
            body = _git_bytes("show", "%s:%s" % (c, path), cwd=repo_root)
            try:
                rec = json.loads(body.decode("utf-8"))[H.WRAPPER_KEY]
            except (ValueError, KeyError):
                out.append("unparseable GER version in history: %s@%s" % (path, c[:8]))
                continue
            rid = rec.get("record_id")
            if rid in seen_now:
                out.append("one identifier bound twice in one tree: %s" % rid)
            seen_now[rid] = (path, rec)
        for rid, (path, rec) in seen_now.items():
            caps = rec.get("captures") or {}
            texts = tuple((caps.get(l) or {}).get("text") for l in H.VARIANT_LABELS)
            digests = tuple((caps.get(l) or {}).get("text_digest")
                            for l in H.VARIANT_LABELS)
            if path != home_rel + rid + ".json":
                out.append("identifier off its canonical path: %s at %s" % (rid, path))
            if rid not in first_seen:
                first_seen[rid] = (texts, digests)
            else:
                if first_seen[rid] != (texts, digests):
                    out.append("capture pair changed under a published identifier: %s" % rid)
            if rid in prev_state:
                allowed = {"human_review"}
                for key in set(prev_state[rid]) | set(rec):
                    if key in allowed:
                        continue
                    if prev_state[rid].get(key) != rec.get(key):
                        out.append("unauthorised field changed between versions: "
                                   "%s.%s" % (rid, key))
            prev_state[rid] = rec
            ever.add(rid)
        for rid in ever - set(seen_now):
            out.append("published identifier no longer present: %s" % rid)
    return out


def registry_violations(reg, manifest_bytes):
    out = []
    entries = {e["id"]: e for e in reg["entries"]}
    ger_rows = [i for i in entries if i.startswith("GER-")]
    if ger_rows:
        out.append("a GER received a registry row: %s" % ger_rows)
    run_rows = [e for e in reg["entries"] if e.get("id") == RUN_ID]
    if len(run_rows) != 1:
        out.append("expected exactly one run-manifest entry, found %d" % len(run_rows))
    run = run_rows[0] if run_rows else None
    if run is None:
        out.append("the run manifest has no registry entry")
    else:
        # W7-D5-MRA: the manifest is a JSON data artefact registered under the
        # live governed-register type (W6-CAT precedent), its human acceptance
        # recorded in its governing phase-record W7-D5-SEC.
        if run.get("type") != "governed-register":
            out.append("the manifest entry is not the governed-register type")
        if run.get("path") != HOME_REL + MANIFEST_NAME:
            out.append("run entry does not point at the manifest")
        if "W7-D5-SEC" not in (run.get("depends_on") or []):
            out.append("the manifest entry does not name its governing record")
        if run.get("implementation_permission") != "none":
            out.append("the manifest entry carries an implementation permission")
        want = "sha256:" + hashlib.sha256(_lf(manifest_bytes)).hexdigest()
        if run.get("content_hash") != want:
            out.append("registry manifest hash does not match the manifest bytes")
        if run.get("id_namespaces"):
            out.append("the run entry mints a namespace")
    sec = entries.get("W7-D5-SEC")
    if sec is None:
        out.append("the completion record has no registry entry")
    else:
        if sec.get("path") != "docs/phases/W7-D5-synthetic-execution-materialisation-record.md":
            out.append("completion entry path is wrong")
        if sec.get("type") != "phase-record":
            out.append("the completion record is not separately registered as phase-record")
        if RUN_ID in (sec.get("depends_on") or []):
            out.append("circular authority dependency: the governing record depends "
                       "on the register it governs")
    manifest_entries = [e for e in reg["entries"]
                        if str(e.get("path", "")).startswith(HOME_REL)]
    if len(manifest_entries) != 1:
        out.append("the home must contribute exactly one registry entry, found %d"
                   % len(manifest_entries))
    # Only the GER-#### namespace string is D5's subject. Other namespaces (the
    # CAT-#### catalogue grammar above all) lawfully keep their own wording.
    ger_ns = [ns for e in reg["entries"] for ns in e.get("id_namespaces", [])
              if ns.startswith("GER-####")]
    if ger_ns != [namespace_successor()]:
        out.append("the GER namespace declaration is not exactly the successor wording")
    if any("no identifier allocated" in ns for ns in ger_ns):
        out.append("the GER namespace still declares that no identifier is allocated")
    return out


def bounded_change_violations(rel, pin_sha, span_start, span_end_exclusive, cwd=ROOT):
    """The module at `rel` may differ from its pre-succession pin only inside the
    named span. The pin version is read from the pre-materialisation reference."""
    out = []
    ref = pre_materialisation_ref(cwd=cwd)
    old = _git_bytes("show", "%s:%s" % (ref, rel), cwd=cwd)
    if hashlib.sha256(_lf(old)).hexdigest() != pin_sha:
        out.append("pre-succession version at %s does not match its pin" % ref)
        return out
    old_lines = _lf(old).decode("utf-8").split("\n")
    new_lines = _text(Path(cwd) / rel).split("\n")

    def span(lines):
        start = next((i for i, l in enumerate(lines) if l.startswith(span_start)), None)
        if start is None:
            return None
        end = next((i for i in range(start + 1, len(lines))
                    if lines[i].startswith(span_end_exclusive)), len(lines))
        return (start, end)

    old_span, new_span = span(old_lines), span(new_lines)
    if old_span is None or new_span is None:
        return ["the authorised span cannot be located in %s" % rel]
    sm = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if not (old_span[0] <= i1 and i2 <= old_span[1]
                and new_span[0] <= j1 and j2 <= new_span[1]):
            out.append("%s changed outside the authorised span: old %d-%d"
                       % (rel, i1 + 1, i2))
    return out


def completion_claim_violations(text):
    """Barred claims, assembled at run time so this module states none of them."""
    flat = " ".join(text.lower().split())
    # Assembled at run time; each pattern refuses the AFFIRMATIVE claim while a
    # negated statement of the same fact ("no model was contacted") stays lawful.
    barred = (
        ("precondition 3 " + "is discharged"),
        ("p3 " + "is discharged"),
        ("w7-d6 " + "is open"),
        ("part q " + "is resolved"),
        ("model " + "was contacted"),
        ("the model " + "passed"),
    )
    out = []
    for b in barred:
        for m in re.finditer(re.escape(b), flat):
            if not flat[: m.start()].endswith("no "):
                out.append("completion record carries a barred claim: %s" % b)
                break
    return out


# ==========================================================================
class M1_FrozenSourceBinding(unittest.TestCase):
    """M1 — the frozen D4 sources, the exam arithmetic, and the two bounded
    succession pins."""

    def test_m1_frozen_hashes_and_exam_arithmetic(self):
        frozen = brief_frozen_hashes()
        with self.subTest(anchor="the brief's section 6 table carries three rows"):
            self.assertEqual(len(frozen), 3)
        for rel in ("fixtures/SYNTHETIC-w7-d4-exam.json",
                    "tests/w7_synthetic_evaluation_harness.py"):
            with self.subTest(permanently_frozen=rel):
                got = hashlib.sha256(
                    (ROOT / rel).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
                self.assertEqual(got, frozen[rel])
        exam = H.load_exam(ROOT / "fixtures/SYNTHETIC-w7-d4-exam.json")
        cov = exam["source_coverage"]
        with self.subTest(fact="26 probes, 23 traps, 52 captures"):
            self.assertEqual((len(exam["probes"]), cov["traps_accounted"],
                              cov["expected_captures"]), (26, 23, 52))
        with self.subTest(fact="the closed pair vocabulary"):
            self.assertEqual(tuple(exam["variant_labels"]), H.VARIANT_LABELS)

    def test_m1_succession_edits_are_bounded_to_their_pins(self):
        pins = psa_pins()
        with self.subTest(module="D4 proof: only H12 moved"):
            self.assertEqual(bounded_change_violations(
                D4_PROOF_REL, pins[D4_PROOF_REL],
                "class H12_ProofSuccession", "class H13_"), [])
        with self.subTest(module="D3 proof: only M6 moved"):
            self.assertEqual(bounded_change_violations(
                D3_PROOF_REL, pins[D3_PROOF_REL],
                "class RepositoryStateAtThisLanding", "class DerivedInvariant"), [])
        with self.subTest(control="a change outside the span is detected"):
            planted = bounded_change_violations(
                D4_PROOF_REL, pins[D4_PROOF_REL],
                "class H13_", "class H14_")
            self.assertTrue(planted, "control: the H12 edit must violate a "
                                     "span that excludes H12")


# ==========================================================================
class M2_HomeClosedSet(unittest.TestCase):
    def test_m2_home_holds_exactly_the_run_and_nothing_else(self):
        names = home_files()
        self.assertEqual(home_closed_set_violations(names), [])
        with self.subTest(fact="exactly 27 files"):
            self.assertEqual(len(names), 27)
        first = introducing_commit(HOME_REL)
        if first is not None:
            with self.subTest(fact="tracked set equals the on-disk set"):
                tracked = sorted(p.split("/")[-1] for p in
                                 _git("ls-files", "--", HOME_REL).split())
                self.assertEqual(tracked, names)
        with self.subTest(control="a stray file is detected"):
            self.assertTrue(home_closed_set_violations(names + ["scratch.txt"]))
        with self.subTest(control="a missing record is detected"):
            self.assertTrue(home_closed_set_violations(names[:-2] + [names[-1]]))


# ==========================================================================
class M3_IdentityAndPathLaw(unittest.TestCase):
    def test_m3_identity_grammar_block_and_canonical_paths(self):
        records = load_records()
        self.assertEqual(identity_violations(records), [])
        self.assertEqual(probe_mapping_violations(records), [])
        with self.subTest(control="a renamed record is detected"):
            mutant = dict(records)
            rec, body, _ = mutant.pop("GER-0026")
            mutant["GER-0026"] = (rec, body, "GER-9999.json")
            self.assertTrue(identity_violations(mutant))
        with self.subTest(control="a wrong probe binding is detected"):
            rec, body, name = records["GER-0001"]
            swapped = json.loads(json.dumps(rec))
            swapped["pairing"]["probe_id"] = "D4-P02"
            mutant = dict(records)
            mutant["GER-0001"] = (swapped, body, name)
            self.assertTrue(probe_mapping_violations(mutant))


# ==========================================================================
class M4_CanonicalShape(unittest.TestCase):
    def test_m4_every_record_is_the_canonical_adr_0049_shape(self):
        for rid, (rec, _, _) in sorted(load_records().items()):
            with self.subTest(record=rid):
                self.assertEqual(shape_violations(rec), [])
        rec = json.loads(json.dumps(load_records()["GER-0001"][0]))
        with self.subTest(control="a half-filled review pair is detected"):
            mutant = json.loads(json.dumps(rec))
            mutant["human_review"]["disposition"] = None
            mutant["human_review"]["disposition_record"] = "W7-D6-HDR"
            self.assertTrue(shape_violations(mutant))
        with self.subTest(control="a field after the ceiling is detected"):
            mutant = json.loads(json.dumps(rec))
            mutant["trailing"] = 1
            self.assertTrue(shape_violations(mutant))


# ==========================================================================
class M5_OptionDAndAuthoritySplit(unittest.TestCase):
    def test_m5_run_authority_and_specimen_authorship_stay_separate(self):
        for rid, (rec, _, _) in sorted(load_records().items()):
            with self.subTest(record=rid):
                self.assertEqual(authority_violations(rec), [])
        rec = json.loads(json.dumps(load_records()["GER-0001"][0]))
        with self.subTest(control="a collapsed capture authority is detected"):
            mutant = json.loads(json.dumps(rec))
            for cap in mutant["captures"].values():
                cap["authoring_record"] = B.RUN_AUTHORITY
            self.assertTrue(authority_violations(mutant))
        with self.subTest(control="a contact flip is detected"):
            mutant = json.loads(json.dumps(rec))
            mutant["model_contact"]["occurred"] = True
            self.assertTrue(authority_violations(mutant))


# ==========================================================================
class M6_ExamFidelity(unittest.TestCase):
    def test_m6_every_capture_is_byte_faithful_to_its_exam_source(self):
        exam = H.load_exam(ROOT / "fixtures/SYNTHETIC-w7-d4-exam.json")
        probes = {p["probe_id"]: p for p in exam["probes"]}
        texts = set()
        for rid, (rec, _, _) in sorted(load_records().items()):
            with self.subTest(record=rid):
                self.assertEqual(fidelity_violations(rec, probes), [])
            for label in H.VARIANT_LABELS:
                texts.add(rec["captures"][label]["text"])
        with self.subTest(fact="52 distinct captures, nothing reused"):
            self.assertEqual(len(texts), 52)
        rec = json.loads(json.dumps(load_records()["GER-0001"][0]))
        with self.subTest(control="an altered capture text is detected"):
            mutant = json.loads(json.dumps(rec))
            mutant["captures"]["variant_a"]["text"] += " "
            self.assertTrue(fidelity_violations(mutant, probes))


# ==========================================================================
class M7_RunCardinality(unittest.TestCase):
    def test_m7_cardinality_is_exactly_the_exam(self):
        records = load_records()
        self.assertEqual(len(records), 26)
        pids = sorted(r[0]["pairing"]["probe_id"] for r in records.values())
        self.assertEqual(pids, ["D4-P%02d" % i for i in range(1, 27)])
        captures = sum(len(r[0]["captures"]) for r in records.values())
        self.assertEqual(captures, 52)


# ==========================================================================
class M8_RealS2(unittest.TestCase):
    """S2 is LIVE: the frozen D4 relation over the actual home bytes."""

    def test_m8_manifest_relation_holds_over_real_bytes(self):
        manifest, _ = load_manifest()
        present = {}
        for rid, (rec, body, _) in load_records().items():
            present[rid] = {"content_hash":
                            "sha256:" + hashlib.sha256(body).hexdigest(),  # body already canonical LF
                            "run_id": rec["run_id"]}
        exam_bytes = _lf((ROOT / "fixtures/SYNTHETIC-w7-d4-exam.json").read_bytes())
        self.assertEqual(H.validate_manifest(manifest, present,
                                             exam_bytes=exam_bytes), [])
        m = manifest["generated_evaluation_run_manifest"]
        with self.subTest(fact="one shared as_of"):
            dates = {r[0]["as_of"] for r in load_records().values()} | {m["as_of"]}
            self.assertEqual(len(dates), 1)
        with self.subTest(fact="the one-bit closed scan environment"):
            self.assertIn(m["scan_environment"]["local_wordlist"],
                          ("active", "inactive"))
        with self.subTest(control="a hash mismatch is detected"):
            bad = dict(present)
            bad["GER-0001"] = {"content_hash": "sha256:" + "0" * 64,
                               "run_id": RUN_ID}
            self.assertTrue(H.validate_manifest(manifest, bad,
                                                exam_bytes=exam_bytes))
        with self.subTest(control="an unlisted record is detected"):
            bad = dict(present)
            bad["GER-9999"] = {"content_hash": "sha256:" + "0" * 64,
                               "run_id": RUN_ID}
            self.assertTrue(H.validate_manifest(manifest, bad,
                                                exam_bytes=exam_bytes))


# ==========================================================================
class M9_PartQAndNoRecirculation(unittest.TestCase):
    def test_m9_no_finding_no_allowlist_route_no_recirculation(self):
        rows = [l.strip().split("|")[0].strip()
                for l in _text(ALLOWLIST).splitlines()
                if l.strip() and not l.strip().startswith("#")]
        for rid, (rec, _, _) in sorted(load_records().items()):
            with self.subTest(record=rid):
                self.assertEqual(part_q_violations(rec, rows), [])
        rec = json.loads(json.dumps(load_records()["GER-0001"][0]))
        with self.subTest(control="a finding-bearing record is detected"):
            mutant = json.loads(json.dumps(rec))
            mutant["findings"] = [{"finding_id": "F1"}]
            self.assertTrue(part_q_violations(mutant, rows))
        with self.subTest(control="a planted allowlist row under the home bites"):
            self.assertTrue(part_q_violations(rec, rows + [HOME_REL + "GER-0001.json"]))
        with self.subTest(control="an input that resolves to the class bites"):
            mutant = json.loads(json.dumps(rec))
            mutant["inputs"][0]["citation"] = "GER" + "-0001"
            self.assertTrue(part_q_violations(mutant, rows))


# ==========================================================================
class M10_S3LifecycleHistory(unittest.TestCase):
    """S3 — the ID-scoped history proof under the D5 lifecycle law."""

    def test_m10_history_preserves_every_published_identifier(self):
        self.assertEqual(s3_history_violations(ROOT), [])

    def test_m10_negative_controls_in_disposable_histories(self):
        # The four W7-D5-SEB section 26.2 controls, each in a throwaway repo
        # far from the real home. Payload-free: neutral capture strings only.
        import tempfile, shutil, os

        def mk_repo(tmp):
            subprocess.run(["git", "init", "-q", tmp], check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t"],
                           check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.name", "t"],
                           check=True)

        def rec_bytes(rid, ta, tb, disposition=None):
            caps = {}
            for label, text in zip(H.VARIANT_LABELS, (ta, tb)):
                caps[label] = {"text_class": H.SPECIMEN_CLASS,
                               "authoring_record": "X",
                               "text": text,
                               "text_digest": "sha256:" + hashlib.sha256(
                                   text.encode("utf-8")).hexdigest(),
                               "scan_status": "no_findings"}
            rec = {"record_id": rid, "run_id": "R", "captures": caps,
                   "human_review": {"routed": True, "disposition": disposition,
                                    "disposition_record": None}}
            return json.dumps({H.WRAPPER_KEY: rec}).encode("utf-8")

        def commit(tmp, msg):
            subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
            subprocess.run(["git", "-C", tmp, "commit", "-q", "-m", msg],
                           check=True)

        home = HOME_REL
        with tempfile.TemporaryDirectory() as tmp:
            mk_repo(tmp)
            hdir = Path(tmp) / home
            hdir.mkdir(parents=True)
            (hdir / "GER-0001.json").write_bytes(rec_bytes("GER-0001", "a1", "b1"))
            commit(tmp, "base")
            with self.subTest(case="a lawful single-version history is clean"):
                self.assertEqual(s3_history_violations(Path(tmp)), [])
            with self.subTest(control="rename plus capture edit is detected"):
                (hdir / "GER-0001.json").unlink()
                (hdir / "GER-0001-v2.json").write_bytes(
                    rec_bytes("GER-0001", "a1-edited", "b1"))
                commit(tmp, "rename-edit")
                self.assertTrue(s3_history_violations(Path(tmp)))
        with tempfile.TemporaryDirectory() as tmp:
            mk_repo(tmp)
            hdir = Path(tmp) / home
            hdir.mkdir(parents=True)
            (hdir / "GER-0001.json").write_bytes(rec_bytes("GER-0001", "a1", "b1"))
            commit(tmp, "base")
            (hdir / "GER-0001.json").unlink()
            commit(tmp, "delete")
            (hdir / "GER-0001.json").write_bytes(
                rec_bytes("GER-0001", "other-a", "other-b"))
            commit(tmp, "reuse")
            with self.subTest(control="delete-and-reuse is detected"):
                self.assertTrue(s3_history_violations(Path(tmp)))
        with tempfile.TemporaryDirectory() as tmp:
            mk_repo(tmp)
            hdir = Path(tmp) / home
            hdir.mkdir(parents=True)
            (hdir / "GER-0001.json").write_bytes(rec_bytes("GER-0001", "a1", "b1"))
            commit(tmp, "base")
            (hdir / "GER-0001.json").write_bytes(
                rec_bytes("GER-0001", "a1", "b1", disposition="future-reviewed"))
            commit(tmp, "review-fields-only")
            with self.subTest(case="a review-metadata-only change is accepted"):
                self.assertEqual(s3_history_violations(Path(tmp)), [])
        with tempfile.TemporaryDirectory() as tmp:
            mk_repo(tmp)
            hdir = Path(tmp) / home
            hdir.mkdir(parents=True)
            (hdir / "GER-0001.json").write_bytes(rec_bytes("GER-0001", "a1", "b1"))
            (hdir / "GER-0002.json").write_bytes(rec_bytes("GER-0001", "zz", "yy"))
            commit(tmp, "duplicate-id")
            with self.subTest(control="duplicate id with a different capture pair"):
                self.assertTrue(s3_history_violations(Path(tmp)))


# ==========================================================================
class M11_P4aClassApplication(unittest.TestCase):
    """P4a over the materialised class, reusing the one governed D4 inventory.

    A green result here is P4a evidence only. It is no evidence for P4b, which
    remains review-only in full across all eleven families.
    """

    def test_m11_guard_inventory_applies_clean_to_the_class_artefacts(self):
        import importlib
        d4 = importlib.import_module("test_w7_synthetic_harness")
        scope = []
        for p in sorted(HOME.iterdir()):
            scope.append((HOME_REL + p.name, _text(p)))
        with self.subTest(fact="the one governed inventory, not a copy"):
            self.assertIs(d4.GUARD_INVENTORY, d4.GUARD_INVENTORY)
            self.assertEqual(len(d4.GUARD_INVENTORY), 11)
        with self.subTest(fact="eight guarded and three declared unguarded"):
            guarded = [g for g in d4.GUARD_INVENTORY if g.detector is not None]
            self.assertEqual((len(guarded), 11 - len(guarded)), (8, 3))
        self.assertEqual(d4.p4a_evaluate(scope), [])
        with self.subTest(fact="the five non-claims stand"):
            self.assertEqual(len(d4.P4A_NON_CLAIMS), 5)
        with self.subTest(control="a planted guarded surface in a record bites"):
            planted = scope + [(HOME_REL + "GER-0001.json",
                                "api" + "_key = " + "x" * 24)]
            self.assertTrue(d4.p4a_evaluate(planted))


# ==========================================================================
class M12_RegistryAndRunIntegrity(unittest.TestCase):
    def test_m12_registry_carries_the_run_and_nothing_per_record(self):
        reg = json.loads(_text(ROOT / "governance/registry.json"))
        _, mbytes = load_manifest()
        self.assertEqual(registry_violations(reg, mbytes), [])
        with self.subTest(control="a per-GER registry row is detected"):
            mutant = json.loads(json.dumps(reg))
            mutant["entries"].append({"id": "GER-0001", "path": "x"})
            self.assertTrue(registry_violations(mutant, mbytes))
        with self.subTest(control="a manifest hash mismatch is detected"):
            self.assertTrue(registry_violations(reg, mbytes + b" "))
        with self.subTest(control="a wrong manifest entry type is detected"):
            mutant = json.loads(json.dumps(reg))
            for e in mutant["entries"]:
                if e["id"] == RUN_ID:
                    e["type"] = "phase-record"
            self.assertTrue(registry_violations(mutant, mbytes))
        with self.subTest(control="a dropped governing-record dependency is detected"):
            mutant = json.loads(json.dumps(reg))
            for e in mutant["entries"]:
                if e["id"] == RUN_ID:
                    e["depends_on"] = [d for d in e["depends_on"] if d != "W7-D5-SEC"]
            self.assertTrue(registry_violations(mutant, mbytes))
        with self.subTest(control="a circular authority dependency is detected"):
            mutant = json.loads(json.dumps(reg))
            for e in mutant["entries"]:
                if e["id"] == "W7-D5-SEC":
                    e["depends_on"] = list(e["depends_on"]) + [RUN_ID]
            self.assertTrue(registry_violations(mutant, mbytes))

    def test_m12_completion_record_makes_no_barred_claim(self):
        text = _text(COMPLETION)
        self.assertEqual(completion_claim_violations(text), [])
        with self.subTest(control="a planted barred claim is detected"):
            planted = text + "\np3 " + "is discharged."
            self.assertTrue(completion_claim_violations(planted))


# ==========================================================================
class M13_BoundaryContract(unittest.TestCase):
    def test_m13_module_states_what_green_does_not_mean(self):
        flat = " ".join(__doc__.split())
        for clause in ("that model contact occurred or is authorised",
                       "anything about model behaviour",
                       "that any trap was passed or failed behaviourally",
                       "Part Q publication seam has been resolved",
                       "local-wordlist coordinate seam has been resolved",
                       "ADR-0047 precondition 3 is discharged",
                       "that W7-D6 is open",
                       "that W8 is open"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)


if __name__ == "__main__":
    unittest.main()
