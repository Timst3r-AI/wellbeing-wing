"""W7-D6 — human-review disposition proofs (H1–H16).

The dispositions are real: every published W7-D5 generated-evaluation record now
carries an explicit human disposition under ADR-0053, sourced from the single
governing human-review record W7-D6-HDR. This module binds that state to the law
mechanically. It is derived proof, never doctrine: the governed vocabulary is
PARSED from the landed ADR-0053 bytes, the disposition rows are PARSED from the
landed W7-D6-HDR bytes, and nothing here re-expresses either authority.

WHAT GREEN DOES NOT MEAN. A green run of this module proves disposition-state
conformance only. It NEVER establishes: anything about model behaviour or
quality; that any trap was passed or failed behaviourally; that anything is
safe, correct, clinically valid, approved or production-ready; that either
variant of any pair is preferred or a winner; any fact about any real person;
that the twenty-six historical generative-era unknowns are resolved; that
ADR-0050's Part Q publication seam has been resolved; that the local-wordlist
coordinate seam has been resolved; that ADR-0047 precondition 3 is discharged;
that W7-D7 is open; or that W8 is open.

DUAL STATE. History-facing proofs handle both lawful states: the
proposed-candidate state, where the D6 changes exist in the working tree and the
disposition commit does not yet exist (the pre-D6 reference is then HEAD), and
the published state, where it does (the reference is then its parent). The
pre-D6 interval's universal nullness is proven from history in either state.
"""

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

import w7_synthetic_evaluation_harness as H

ROOT = Path(__file__).resolve().parents[1]
HOME_REL = "governance/generated-evaluation/"
HOME = ROOT / "governance" / "generated-evaluation"
ADR = ROOT / "docs/decisions/0053-human-review-generated-evaluation-disposition-law.md"
HDR = ROOT / "docs/phases/W7-D6-human-review-disposition-record.md"
HDR_ID = "W7-D6-HDR"
MANIFEST = HOME / "W7-D5-RUN-01-manifest.json"
EXPECTED_IDS = tuple("GER-%04d" % i for i in range(1, 27))


def _lf(b):
    return b.replace(b"\r\n", b"\n")


def _text(p):
    return _lf(Path(p).read_bytes()).decode("utf-8")


def _git(*args, cwd=ROOT):
    return subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True,
                          text=True, check=True).stdout


def _git_bytes(*args, cwd=ROOT):
    return subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True,
                          check=True).stdout


def adr_vocabulary():
    """The three governed members, parsed from ADR-0053 decisions 8–10 by their
    own backticked definitional headers. Never hard-coded."""
    src = _text(ADR)
    toks = re.findall(r"\n\d+\. \*\*`([a-z_]+)`\*\* means exactly:", src)
    return tuple(toks)


def hdr_rows():
    """{record_id: (probe_id, disposition)} parsed from the HDR table."""
    src = _text(HDR)
    rows = {}
    for m in re.finditer(r"\| (GER-\d{4}) \| (D4-P\d{2}) \| ([a-z_]+) \|", src):
        rid, pid, tok = m.groups()
        if rid in rows:
            rows[rid] = None  # duplicate marker
        else:
            rows[rid] = (pid, tok)
    return rows


def load_records():
    out = {}
    for p in sorted(HOME.glob("GER-*.json")):
        body = _lf(p.read_bytes())
        rec = json.loads(body.decode("utf-8"))[H.WRAPPER_KEY]
        out[rec["record_id"]] = (rec, body)
    return out


def _blob(ref, rel, cwd=ROOT):
    """Read ref:rel via rev-parse + cat-file so git never stats the spec as a
    filesystem path (a deep-worktree failure mode on Windows)."""
    sha = _git("rev-parse", ref, cwd=cwd).strip()
    return _git_bytes("cat-file", "-p", "%s:%s" % (sha, rel), cwd=cwd)


def pre_d6_ref(cwd=ROOT):
    """The last pre-disposition point in history: HEAD in the candidate state,
    else the parent of the first commit whose tree carries a non-null pair."""
    commits = _git("rev-list", "--reverse", "HEAD", "--", HOME_REL, cwd=cwd).split()
    for c in commits:
        body = _blob(c, HOME_REL + "GER-0001.json", cwd=cwd)
        rec = json.loads(_lf(body).decode("utf-8"))[H.WRAPPER_KEY]
        if rec["human_review"]["disposition"] is not None:
            return c + "^"
    return "HEAD"


# ------------------------------------------------------------- validators ---

def review_state_violations(records, rows, vocab):
    """H1–H5 as one pure relation over supplied state."""
    out = []
    ids = sorted(records)
    if ids != sorted(EXPECTED_IDS):
        out.append("review set is not exactly the twenty-six published records")
    for rid in sorted(set(rows) - set(EXPECTED_IDS)):
        out.append("review record covers an unknown record: %s" % rid)
    for rid, (rec, _) in sorted(records.items()):
        hr = rec["human_review"]
        row = rows.get(rid)
        if row is None and rid in rows:
            out.append("duplicate review row: %s" % rid)
            continue
        if (hr["disposition"] is None) != (hr["disposition_record"] is None):
            out.append("half-filled review pair: %s" % rid)
            continue
        if hr["disposition"] is None:
            if row is not None:
                out.append("a review row exists for an undispositioned record: %s" % rid)
            continue
        if hr["disposition"] not in vocab:
            out.append("out-of-vocabulary disposition: %s" % rid)
        if hr["disposition_record"] != HDR_ID:
            out.append("disposition cites the wrong governing record: %s" % rid)
        if row is None:
            out.append("no review row for a dispositioned record: %s" % rid)
        else:
            pid, tok = row
            if tok != hr["disposition"]:
                out.append("review row and record disagree: %s" % rid)
            if pid != rec["pairing"]["probe_id"]:
                out.append("review row cites the wrong probe: %s" % rid)
    return out


def immutability_violations(old_rec, new_rec):
    """H6/H7: only the two later-owned positions may differ."""
    out = []
    a = json.loads(json.dumps(old_rec))
    b = json.loads(json.dumps(new_rec))
    for side in (a, b):
        side["human_review"] = {"routed": side["human_review"].get("routed")}
    if a != b:
        out.append("a position outside the two later-owned fields differs")
    for label in old_rec.get("captures", {}):
        oc = old_rec["captures"].get(label, {})
        nc = new_rec.get("captures", {}).get(label, {})
        if oc.get("text") != nc.get("text"):
            out.append("capture text differs: %s" % label)
        if oc.get("text_digest") != nc.get("text_digest"):
            out.append("capture digest differs: %s" % label)
        if oc != nc:
            out.append("a capture field differs: %s" % label)
    if new_rec.get("human_review", {}).get("routed") is not True:
        out.append("routed is no longer true")
    return out


def no_return_to_null_violations(history_states):
    """H8: ordered [(disposition, disposition_record)] per record across history."""
    out = []
    seen_non_null = False
    for disp, rec_id in history_states:
        if seen_non_null and (disp is None or rec_id is None):
            out.append("a review field returned to null after a published disposition")
        if disp is not None:
            seen_non_null = True
    return out


def supersession_violations(history_states, governing_records):
    """H9: once non-null, any change to either later-owned field is lawful only
    as governed supersession - both fields move atomically to a NEW governing
    human-review record that EXISTS, is ACCEPTED, and EXPRESSLY SUPERSEDES the
    prior one. `governing_records` maps record identity to
    {"exists": bool, "accepted": bool, "supersedes": prior-record-id-or-None}.
    """
    out = []
    prev = None
    for disp, rec_id in history_states:
        if prev is not None and disp is not None and prev[0] is not None:
            changed_disp = disp != prev[0]
            changed_rec = rec_id != prev[1]
            if changed_disp and not changed_rec:
                out.append("disposition changed without a new governing review record")
            if changed_rec:
                meta = governing_records.get(rec_id)
                if meta is None or not meta.get("exists"):
                    out.append("superseding record does not exist")
                elif not meta.get("accepted"):
                    out.append("superseding record is not accepted")
                elif meta.get("supersedes") != prev[1]:
                    out.append("superseding record does not expressly supersede "
                               "the prior human act")
        prev = (disp, rec_id)
    return out


def anti_collapse_violations(rec, vocab, finding_vocab):
    """H13: no cross-contamination between the two disposition vocabularies."""
    out = []
    hr = rec.get("human_review", {})
    if hr.get("disposition") in finding_vocab:
        out.append("a finding disposition appears in human review")
    for f in rec.get("findings", []) or []:
        if f.get("disposition") in vocab:
            out.append("a human-review token appears in a finding event")
    return out


BARRED_FIELD_NAMES = ("selected_variant", "winner", "score", "ranking",
                      "preferred", "preferred_variant", "selection")


def winner_absence_violations(rec):
    out = []
    flat = json.dumps(rec).lower()
    for name in BARRED_FIELD_NAMES:
        if '"%s"' % name in flat:
            out.append("a machine-selection field is present: %s" % name)
    return out


# ==========================================================================
class H1toH5_ReviewState(unittest.TestCase):
    def test_h1_h5_completeness_vocabulary_source_and_atomic_pair(self):
        vocab = adr_vocabulary()
        with self.subTest(anchor="ADR-0053 closes exactly three members"):
            self.assertEqual(len(vocab), 3)
            self.assertEqual(len(set(vocab)), 3)
        records = load_records()
        rows = hdr_rows()
        with self.subTest(fact="H1: exactly the twenty-six records"):
            self.assertEqual(sorted(records), sorted(EXPECTED_IDS))
        with self.subTest(fact="H2: one row per record, none duplicate"):
            self.assertEqual(sorted(k for k, v in rows.items() if v is not None),
                             sorted(EXPECTED_IDS))
        self.assertEqual(review_state_violations(records, rows, vocab), [])
        rec0 = json.loads(json.dumps(records["GER-0001"][0]))
        base = {rid: (json.loads(json.dumps(r)), b) for rid, (r, b) in records.items()}
        with self.subTest(control="H3: a synthetic fourth value fails"):
            m = {k: (json.loads(json.dumps(v[0])), v[1]) for k, v in base.items()}
            m["GER-0001"][0]["human_review"]["disposition"] = "approved_variant"
            self.assertTrue(review_state_violations(m, rows, vocab))
        with self.subTest(control="H4: a wrong governing record fails"):
            m = {k: (json.loads(json.dumps(v[0])), v[1]) for k, v in base.items()}
            m["GER-0001"][0]["human_review"]["disposition_record"] = "W7-D5-SEC"
            self.assertTrue(review_state_violations(m, rows, vocab))
        with self.subTest(control="H4: a missing review row fails"):
            r2 = dict(rows); del r2["GER-0007"]
            self.assertTrue(review_state_violations(records, r2, vocab))
        with self.subTest(control="H4: a mismatched token fails"):
            r2 = dict(rows)
            r2["GER-0003"] = (r2["GER-0003"][0], "review_inconclusive")
            self.assertTrue(review_state_violations(records, r2, vocab))
        with self.subTest(control="H5: a half-filled pair fails"):
            m = {k: (json.loads(json.dumps(v[0])), v[1]) for k, v in base.items()}
            m["GER-0002"][0]["human_review"]["disposition_record"] = None
            self.assertTrue(review_state_violations(m, rows, vocab))
        with self.subTest(control="H2: an unknown record in the review fails"):
            r2 = dict(rows); r2["GER-9999"] = ("D4-P99", vocab[0])
            self.assertTrue(review_state_violations(records, r2, vocab))


# ==========================================================================
class H6toH7_Immutability(unittest.TestCase):
    def test_h6_h7_captures_and_non_review_fields_identical_to_first_publication(self):
        ref = pre_d6_ref()
        for rid, (new_rec, _) in sorted(load_records().items()):
            old = json.loads(_lf(_blob(
                ref, "%s%s.json" % (HOME_REL, rid))).decode("utf-8"))[H.WRAPPER_KEY]
            with self.subTest(record=rid):
                self.assertEqual(immutability_violations(old, new_rec), [])
        old = json.loads(_lf(_blob(
            ref, HOME_REL + "GER-0001.json")).decode("utf-8"))[H.WRAPPER_KEY]
        with self.subTest(control="a capture edit is detected"):
            m = json.loads(json.dumps(load_records()["GER-0001"][0]))
            m["captures"]["variant_a"]["text"] += " "
            self.assertTrue(immutability_violations(old, m))
        with self.subTest(control="a capture digest edit is detected"):
            m = json.loads(json.dumps(load_records()["GER-0001"][0]))
            m["captures"]["variant_b"]["text_digest"] = "sha256:" + "0" * 64
            self.assertTrue(immutability_violations(old, m))
        with self.subTest(control="a non-review field edit is detected"):
            m = json.loads(json.dumps(load_records()["GER-0001"][0]))
            m["as_of"] = "2027-01-01"
            self.assertTrue(immutability_violations(old, m))


# ==========================================================================
class H8toH9_Lifecycle(unittest.TestCase):
    def test_h8_h9_no_return_to_null_and_governed_supersession(self):
        with self.subTest(case="the real history has no unlawful transition"):
            ref_states = []
            for c in _git("rev-list", "--reverse", "HEAD", "--",
                          HOME_REL + "GER-0001.json").split():
                rec = json.loads(_lf(_blob(
                    c, HOME_REL + "GER-0001.json")).decode("utf-8"))[H.WRAPPER_KEY]
                hr = rec["human_review"]
                ref_states.append((hr["disposition"], hr["disposition_record"]))
            cur = load_records()["GER-0001"][0]["human_review"]
            ref_states.append((cur["disposition"], cur["disposition_record"]))
            self.assertEqual(no_return_to_null_violations(ref_states), [])
            self.assertEqual(supersession_violations(ref_states, {}), [])
        with self.subTest(control="H8: a return to null is detected"):
            states = [(None, None), ("governance_delta_present", HDR_ID), (None, None)]
            self.assertTrue(no_return_to_null_violations(states))
        future = {"W7-D9-FUTURE-REVIEW": {"exists": True, "accepted": True,
                                          "supersedes": HDR_ID}}
        with self.subTest(control="H9: a token change without a new record is detected"):
            states = [("governance_delta_present", HDR_ID),
                      ("review_inconclusive", HDR_ID)]
            self.assertTrue(supersession_violations(states, future))
        with self.subTest(control="H9: a non-existent superseding record is detected"):
            states = [("governance_delta_present", HDR_ID),
                      ("review_inconclusive", "W7-D9-GHOST")]
            self.assertTrue(supersession_violations(states, future))
        with self.subTest(control="H9: an unaccepted superseding record is detected"):
            states = [("governance_delta_present", HDR_ID),
                      ("review_inconclusive", "W7-D9-DRAFT")]
            self.assertTrue(supersession_violations(
                states, {"W7-D9-DRAFT": {"exists": True, "accepted": False,
                                         "supersedes": HDR_ID}}))
        with self.subTest(control="H9: a record without express supersession is detected"):
            self.assertTrue(supersession_violations(
                [("governance_delta_present", HDR_ID),
                 ("review_inconclusive", "W7-D9-UNRELATED")],
                {"W7-D9-UNRELATED": {"exists": True, "accepted": True,
                                     "supersedes": None}}))
        with self.subTest(case="H9: a lawful express supersession is accepted"):
            states = [("governance_delta_present", HDR_ID),
                      ("review_inconclusive", "W7-D9-FUTURE-REVIEW")]
            self.assertEqual(supersession_violations(states, future), [])


# ==========================================================================
class H10toH12_ManifestAndRegistry(unittest.TestCase):
    def test_h10_manifest_lists_exact_final_bytes(self):
        man = json.loads(_lf(MANIFEST.read_bytes()).decode("utf-8"))
        present = {}
        for rid, (rec, body) in load_records().items():
            present[rid] = {"content_hash":
                            "sha256:" + hashlib.sha256(body).hexdigest(),
                            "run_id": rec["run_id"]}
        exam_bytes = _lf((ROOT / "fixtures/SYNTHETIC-w7-d4-exam.json").read_bytes())
        self.assertEqual(H.validate_manifest(man, present, exam_bytes=exam_bytes), [])

    def test_h11_manifest_bounded_change_from_the_d5_version(self):
        ref = pre_d6_ref()
        old = json.loads(_lf(_blob(
            ref, HOME_REL + "W7-D5-RUN-01-manifest.json")).decode("utf-8"))
        new = json.loads(_lf(MANIFEST.read_bytes()).decode("utf-8"))
        om, nm = old["generated_evaluation_run_manifest"], new["generated_evaluation_run_manifest"]
        for key in ("run_id", "authorising_record", "as_of", "exam", "scan_environment"):
            with self.subTest(unchanged=key):
                self.assertEqual(om[key], nm[key])
        with self.subTest(fact="record identities, order and paths unchanged"):
            self.assertEqual([(e["record_id"], e["path"]) for e in om["records"]],
                             [(e["record_id"], e["path"]) for e in nm["records"]])
        with self.subTest(fact="only content hashes moved, and every one is real"):
            for e in nm["records"]:
                body = _lf((ROOT / e["path"]).read_bytes())
                self.assertEqual(e["content_hash"],
                                 "sha256:" + hashlib.sha256(body).hexdigest())

    def test_h12_registry_reconciliation(self):
        reg = json.loads(_text(ROOT / "governance/registry.json"))
        entries = {e["id"]: e for e in reg["entries"]}
        with self.subTest(fact="no per-GER rows and no new GER identity"):
            self.assertEqual([i for i in entries if i.startswith("GER-")], [])
        run = entries["W7-D5-RUN-01"]
        with self.subTest(fact="register hash equals the exact D6 manifest bytes"):
            want = "sha256:" + hashlib.sha256(_lf(MANIFEST.read_bytes())).hexdigest()
            self.assertEqual(run["content_hash"], want)
        with self.subTest(fact="the register names its later governing authority"):
            self.assertIn(HDR_ID, run["depends_on"])
        hdr = entries[HDR_ID]
        with self.subTest(fact="no circular authority dependency"):
            self.assertNotIn("W7-D5-RUN-01", hdr["depends_on"])
        with self.subTest(fact="the governing record is a prose phase-record"):
            self.assertEqual(hdr["type"], "phase-record")
        ns = [n for e in reg["entries"] for n in e.get("id_namespaces", [])
              if n.startswith("GER-####")]
        with self.subTest(fact="namespace wording unchanged from W7-D5"):
            self.assertEqual(len(ns), 1)
            self.assertIn("allocation begun under W7-D5", ns[0])


# ==========================================================================
class H13toH15_Boundaries(unittest.TestCase):
    def test_h13_h14_anti_collapse_and_no_machine_winner(self):
        vocab = adr_vocabulary()
        src = _text(ROOT / "docs/decisions/"
                    "0050-finding-is-an-event-and-finding-disposition-mechanism.md")
        finding_vocab = tuple(sorted(set(re.findall(
            r"`(open|routed_for_public_safety_review|withheld_from_publication)`", src))))
        with self.subTest(anchor="ADR-0050's three finding values are live-parsed"):
            self.assertEqual(len(finding_vocab), 3)
        for rid, (rec, _) in sorted(load_records().items()):
            with self.subTest(record=rid):
                self.assertEqual(anti_collapse_violations(rec, vocab, finding_vocab), [])
                self.assertEqual(winner_absence_violations(rec), [])
        rec = json.loads(json.dumps(load_records()["GER-0001"][0]))
        with self.subTest(control="a finding token in human review is detected"):
            m = json.loads(json.dumps(rec))
            m["human_review"]["disposition"] = finding_vocab[0]
            self.assertTrue(anti_collapse_violations(m, vocab, finding_vocab))
        with self.subTest(control="a review token in a finding is detected"):
            m = json.loads(json.dumps(rec))
            m["findings"] = [{"disposition": vocab[0]}]
            self.assertTrue(anti_collapse_violations(m, vocab, finding_vocab))
        with self.subTest(control="a planted selection field is detected"):
            m = json.loads(json.dumps(rec))
            m["selected" + "_variant"] = "variant_a"
            self.assertTrue(winner_absence_violations(m))

    def test_h15_boundary_preservation(self):
        # The boundaries are proven against the candidate's actual bytes, not
        # merely asserted in prose: every seam-owning artefact is byte-identical
        # to the pre-D6 published reference, and no out-of-phase artefact exists.
        ref = pre_d6_ref()
        for rel in ("scripts/public-safety-scan.py",
                    "scripts/scan-allowlist.txt",
                    "requirements.txt",
                    "docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md",
                    "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md",
                    "docs/decisions/0051-model-boundary-no-public-contact.md",
                    "docs/phases/W7-D5-synthetic-execution-materialisation-record.md",
                    "fixtures/SYNTHETIC-w7-d4-exam.json",
                    "tests/w7_synthetic_evaluation_harness.py"):
            with self.subTest(byte_identical_to_pre_d6=rel):
                self.assertEqual(_lf(_blob(ref, rel)),
                                 _lf((ROOT / rel).read_bytes()))
        with self.subTest(fact="ADR-0047 precondition 3 remains OUTSTANDING in the "
                               "published precondition table"):
            src = _text(ROOT / "docs/decisions/0051-model-boundary-no-public-contact.md")
            m = re.search(r"\| \*\*3\*\* \|[^|]+\| \*?\*?([A-Z]+)\*?\*? \|", src)
            self.assertIsNotNone(m)
            self.assertEqual(m.group(1), "OUTSTANDING")
        with self.subTest(fact="no W7-D7 or W8 artefact exists"):
            tracked = _git("ls-files").split()
            self.assertEqual([p for p in tracked
                              if "W7-D7" in p or p.startswith("docs/phases/W8")], [])
        with self.subTest(fact="every record still declares no model contact"):
            for rid, (rec, _) in sorted(load_records().items()):
                self.assertIs(rec["model_contact"]["occurred"], False)
                self.assertEqual(rec["model_contact"]["contact_class"], "none")
        flat = " ".join(__doc__.split())
        for clause in ("Part Q publication seam has been resolved",
                       "local-wordlist coordinate seam has been resolved",
                       "ADR-0047 precondition 3 is discharged",
                       "that W7-D7 is open",
                       "that W8 is open",
                       "preferred or a winner",
                       "generative-era unknowns are resolved"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)


# ==========================================================================
class H16_HumanActSource(unittest.TestCase):
    def test_h16_dispositions_cite_an_accepted_governing_source(self):
        head = _text(HDR).split("\n")[2]
        any_non_null = any(rec["human_review"]["disposition"] is not None
                           for rec, _ in load_records().values())
        if any_non_null:
            self.assertIn("Accepted by human reviewer", head,
                          "non-null GER review fields require an accepted "
                          "governing record; a candidate source cannot authorise "
                          "the final state")
        with self.subTest(anchor="the registry records the source as accepted"):
            reg = json.loads(_text(ROOT / "governance/registry.json"))
            hdr = [e for e in reg["entries"] if e["id"] == HDR_ID][0]
            self.assertEqual(hdr["status"], "accepted")


if __name__ == "__main__":
    unittest.main()
