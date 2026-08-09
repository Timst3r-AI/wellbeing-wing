"""W4-D6 Lane A — contract conformance validator.

Subject: the four accepted W4 room contracts as documents.

Doctrine: ADR 0021 (contract validator requirements), as corrected for M10 and
M12 by ADR 0022 (contract validator M10/M12 decidability correction). Every
governed term is mechanically checkable or review-only; there is no third class
and no judging validator. A mechanical pass means only that the decidable
document properties conform -- not that a contract is accepted, a room is safe,
or any implementation is authorised.

Expectation discipline: expected values are frozen in
tests/grammar/w4-contract-expectations.json, derived once from the accepted
baseline. The validator observes the contract under test; it never learns its
expected answer from it. Runtime values are observations only, compared against
frozen expectations.

Structural discipline: quoted and source-transcribed regions (contiguous
markdown blockquote runs) are excluded before any assertion is extracted. No
global text search makes a structural decision.

Corrected Lane A matrix (ADR 0022): 47 mechanical instances --
set-level 2, Wellness 10, Kitchen 11, Gym 11, Meditation 13.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTATIONS = ROOT / "tests" / "grammar" / "w4-contract-expectations.json"
DOCS = ROOT / "docs"

EDGE_TOKEN = re.compile(r"\b(?:E\d+(?:-[WKG])?|M[12])\b")
SECTION_RE = re.compile(r"^## (\d+)\.\s")
NA_RE = re.compile(r"^\*\*Not applicable —")

EXPECTED_TOTAL_INSTANCES = 47
EXPECTED_SCOPE_COUNTS = {"set": 2, "Wellness": 10, "Kitchen": 11, "Gym": 11, "Meditation": 13}


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------

def _load_expectations():
    return json.loads(EXPECTATIONS.read_text(encoding="utf-8"))


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


# --------------------------------------------------------------------------
# parsing -- structural only; quoted regions excluded before extraction
# --------------------------------------------------------------------------

def strip_quoted(lines):
    """Drop contiguous markdown blockquote runs. Mandatory before extraction."""
    return [ln for ln in lines if not ln.lstrip().startswith(">")]


def quoted_lines(text):
    """The quoted/source-transcribed lines, with one leading '> ' removed."""
    out = []
    for ln in text.splitlines():
        s = ln.lstrip()
        if s.startswith(">"):
            body = s[1:]
            out.append(body[1:] if body.startswith(" ") else body)
    return out


def split_sections(text):
    """Top-level '## N. Title' sections, keyed by number, quote-stripped."""
    out, cur = {}, None
    for ln in strip_quoted(text.splitlines()):
        m = SECTION_RE.match(ln)
        if m:
            cur = int(m.group(1))
            out[cur] = []
        elif cur is not None:
            out[cur].append(ln)
    return out


def section_order(text):
    return [int(m.group(1)) for m in
            (SECTION_RE.match(ln) for ln in strip_quoted(text.splitlines())) if m]


def find_na_constructs(sections):
    """ADR-0016 'Not applicable -- <reason>' bodies, structurally, quote-stripped."""
    found = []
    for num, body in sections.items():
        for ln in body:
            t = ln.strip()
            if NA_RE.match(t):
                found.append((str(num), t))
    return found


def extract_bait_blocks(text, prefix):
    """(label, block-text) per bait, block running to the next '### ' or '## '."""
    pat = re.compile(r"^### (" + re.escape(prefix) + r"\d+)", re.M)
    marks = [(m.start(), m.group(1)) for m in pat.finditer(text)]
    blocks = []
    for i, (pos, label) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        blocks.append((label, text[pos:end]))
    return blocks


def extract_edge_ids(lines):
    """Asserted edge identifiers from already quote-stripped lines."""
    return set(EDGE_TOKEN.findall("\n".join(lines)))


def contract_tokens(text, grammar):
    """M10 contract-token recognition, quote-stripped. Lexical only."""
    stripped = "\n".join(strip_quoted(text.splitlines()))
    return sorted(set(re.findall(grammar, stripped)))


def shared_table_block(text):
    """The ADR-0020 shared-table quotation as carried by a contract."""
    marker = "**Verbatim quotation (ADR-0020"
    i = text.find(marker)
    if i < 0:
        return None
    tail = text[text.index("\n", i) + 1:]
    out, started = [], False
    for ln in tail.splitlines():
        s = ln.lstrip()
        if s.startswith(">"):
            started = True
            body = s[1:]
            out.append(body[1:] if body.startswith(" ") else body)
        elif started and s.strip() == "":
            out.append("")
        elif started:
            break
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


# --------------------------------------------------------------------------
# mechanical checks -- each returns a list of "ERRID: bounded evidence"
# --------------------------------------------------------------------------

def check_m01_contract_set(exp):
    f = []
    seen_rooms, seen_paths = set(), set()
    for c in exp["contracts"]:
        if not (ROOT / c["path"]).exists():
            f.append("W4LA-M01-MISSING: %s" % c["path"])
        if c["room"] in seen_rooms:
            f.append("W4LA-M01-DUPLICATE_IDENTITY: %s" % c["room"])
        if c["path"] in seen_paths:
            f.append("W4LA-M01-DUPLICATE_PATH: %s" % c["path"])
        seen_rooms.add(c["room"])
        seen_paths.add(c["path"])
    if len(exp["contracts"]) != 4:
        f.append("W4LA-M01-COUNT: expected 4, observed %d" % len(exp["contracts"]))
    return f


def check_m02_sections(exp, c, text):
    f = []
    observed = section_order(text)
    expected = exp["shared"]["expected_section_numbers"]
    if observed != expected:
        f.append("W4LA-M02-ORDER: expected %s, observed %s" % (expected, observed))
    for num, body in split_sections(text).items():
        if not any(ln.strip() for ln in body):
            f.append("W4LA-M02-BLANK: section %d" % num)
    return f


def check_m03_na_reason(exp, c, text):
    f = []
    found = find_na_constructs(split_sections(text))
    if not c["na_construct_present"]:
        if found:
            f.append("W4LA-M03-UNEXPECTED: sections %s" % [s for s, _ in found])
        return f
    if [s for s, _ in found] != c["na_sections"]:
        f.append("W4LA-M03-LOCATION: expected %s, observed %s"
                 % (c["na_sections"], [s for s, _ in found]))
    for sec, line in found:
        reason = line.split("—", 1)[1].strip(" *") if "—" in line else ""
        if not reason:
            f.append("W4LA-M03-BARE_NA: section %s" % sec)
    return f


def check_m04a_open_questions_present(exp, c, text):
    secs = split_sections(text)
    if 11 not in secs:
        return ["W4LA-M04A-MISSING: section 11 absent"]
    if not any(ln.strip() for ln in secs[11]):
        return ["W4LA-M04A-BLANK: section 11 blank"]
    return []


def check_m04b_open_questions_empty_body(exp, c, text):
    body = [ln.strip() for ln in split_sections(text).get(11, []) if ln.strip()]
    expected = exp["shared"]["open_questions_empty_body"]
    if not body or body[0] != expected:
        return ["W4LA-M04B-BODY_MISMATCH: expected %r, observed %r"
                % (expected, body[0] if body else "")]
    return []


def _s9_observed(text, layout):
    """Observed section 9 entries, per the contract's own frozen layout locator."""
    lines = split_sections(text).get(9, [])
    order = [("mechanical", layout["mechanical"]), ("review_only", layout["review_only"])]
    if layout["boundary"]:
        order.append(("boundary_declarations", layout["boundary"]))
    marks = []
    for name, needle in order:
        for i, ln in enumerate(lines):
            if ln.strip().startswith(needle.strip()):
                marks.append((i, name))
                break
    marks.sort()
    res = {"mechanical": [], "review_only": [], "boundary_declarations": []}
    for idx, (start, name) in enumerate(marks):
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        for ln in lines[start + 1:end]:
            t = ln.strip()
            if t.startswith("- "):
                res[name].append(t[2:].strip())
    return res


def check_m05_hooks_inventory(exp, c, text):
    """Five accepted failure forms; evaluation/boundary text is not a third class."""
    f = []
    obs = _s9_observed(text, c["section9_layout"])
    inv = c["section9_inventory"]
    for cls in ("mechanical", "review_only"):
        expected = [e["entry"] for e in inv[cls]]
        observed = obs[cls]
        for e in expected:
            if e not in observed:
                f.append("W4LA-M05-MISSING_ENTRY: %s/%s" % (cls, e[:60]))
        for o in observed:
            if o not in expected:
                other = [x["entry"] for x in inv["review_only" if cls == "mechanical" else "mechanical"]]
                if o in other:
                    f.append("W4LA-M05-MOVED_ENTRY: %s/%s" % (cls, o[:60]))
                else:
                    f.append("W4LA-M05-UNEXPECTED_ENTRY: %s/%s" % (cls, o[:60]))
    both = set(obs["mechanical"]) & set(obs["review_only"])
    for e in sorted(both):
        f.append("W4LA-M05-DOUBLE_CLASSIFIED: %s" % e[:60])
    return f


def scope_clause_lines(text):
    """The carried verbatim scope clauses: quoted lines inside sections 2-3.

    ADR 0021 gives M6 the artefact 'Sections 2-3' and M7 the artefact 'Scope
    clauses'. A scope clause is the paired-form quotation the contract carries,
    not every sentence in those sections.
    """
    out, cur = [], None
    for ln in text.splitlines():
        m = SECTION_RE.match(ln)
        if m:
            cur = int(m.group(1))
            continue
        if cur in (2, 3):
            s = ln.lstrip()
            if s.startswith(">"):
                body = s[1:]
                out.append(body[1:] if body.startswith(" ") else body)
    return out


def check_m06_scope_integrity(exp, c, text):
    """Sections 2-3: each carried scope clause matches its cited source bytes.

    Strict fidelity (ruling M6-R1 / PR unit): the only permitted parsing is
    removal of Markdown blockquote transport syntax ('>' plus its one following
    space). Source-owned list markers, indentation, punctuation, identifiers,
    lexical content, and ordering are all source content and must match
    byte-for-byte. No normalisation is applied to either side.
    """
    f = []
    corpus = set()
    for p in sorted(DOCS.rglob("*.md")):
        if p.name.endswith("-room-contract.md"):
            continue
        corpus.update(p.read_text(encoding="utf-8").splitlines())
    for line in scope_clause_lines(text):
        if not line.strip():
            continue
        if line not in corpus:
            f.append("W4LA-M06-QUOTATION_MISMATCH: %s" % line[:70])
    return f


def check_m07_load_bearing(exp, c, text):
    """Load-bearing words present, source-backed blur phrases absent, in scope clauses."""
    f = []
    clauses = "\n".join(scope_clause_lines(text))
    for w in c["load_bearing_words"]:
        if w not in clauses:
            f.append("W4LA-M07-MISSING_WORD: %s" % w)
    for phrase in exp["shared"]["prohibited_blur_phrases"]:
        if re.search(r"\b%s\b" % re.escape(phrase), clauses):
            f.append("W4LA-M07-BLUR_PHRASE: %s" % phrase)
    return f


def check_m08_shared_table(exp, c, text):
    src = _read(exp["shared"]["shared_table_source"])
    start = src.index("The foundation is the **verbatim W1-D3 §2 label semantics**")
    end = src.index("\n\n", src.index("**Source-fidelity note (reported, not harmonised):**"))
    expected = src[start:end].strip()
    observed = shared_table_block(text)
    if observed is None:
        return ["W4LA-M08-MISSING: no ADR-0020 quotation block"]
    if observed.strip() != expected:
        exp_l, obs_l = expected.splitlines(), observed.strip().splitlines()
        for i in range(max(len(exp_l), len(obs_l))):
            e = exp_l[i] if i < len(exp_l) else "<absent>"
            o = obs_l[i] if i < len(obs_l) else "<absent>"
            if e != o:
                return ["W4LA-M08-TABLE_MISMATCH: line %d expected %r observed %r"
                        % (i + 1, e[:50], o[:50])]
    return []


def check_m09_bait_declarations(exp, c, text):
    f = []
    decl = exp["shared"]["fixture_declaration_text"]
    blocks = extract_bait_blocks(text, c["bait_prefix"])
    labels = [lab for lab, _ in blocks]
    if labels != c["bait_labels"]:
        f.append("W4LA-M09-LABELS: expected %s, observed %s" % (c["bait_labels"], labels))
    for label, block in blocks:
        n = block.count(decl)
        if n != c["declarations_per_bait_expected"]:
            f.append("W4LA-M09-DECLARATION_COUNT: %s has %d" % (label, n))
    return f


def check_m10_contract_tokens(exp, c, text):
    """ADR 0022: closed-set contract placeholder membership. No rejected-token list."""
    canonical = set(exp["shared"]["canonical_placeholder_set"])
    grammar = exp["shared"]["contract_token_grammar"]
    outside = [t for t in contract_tokens(text, grammar) if t not in canonical]
    return ["W4LA-M10-NON_CANONICAL_TOKEN: %s" % t for t in outside]


def check_m11_citations_resolve(exp, c, text):
    f = []
    for m in re.finditer(r"`(docs/[^`]+\.md|tests/[^`]+|engine/[^`]+|scripts/[^`]+)`", text):
        if not (ROOT / m.group(1)).exists():
            f.append("W4LA-M11-DANGLING_PATH: %s" % m.group(1))
    if "ADR-0017" not in "\n".join(split_sections(text).get(6, [])):
        f.append("W4LA-M11-ISOLATION_CITATION: ADR-0017 not cited in section 6")
    return f


def check_m12a_anti_map(exp, c, text):
    """ADR 0022: anti-map identifier fidelity. No intersection claim."""
    f = []
    observed = extract_edge_ids(split_sections(text).get(8, []))
    expected = set(c["anti_map_identifier_expectation"])
    for i in sorted(expected - observed):
        f.append("W4LA-M12A-MISSING_IDENTIFIER: %s" % i)
    for i in sorted(observed - expected):
        f.append("W4LA-M12A-UNEXPECTED_IDENTIFIER: %s" % i)
    return f


def check_m12b_meditation_edge_set(exp, c, text):
    secs = split_sections(text)
    s2 = extract_edge_ids(secs.get(2, []))
    s8 = extract_edge_ids(secs.get(8, []))
    expected = set(c["asserted_edge_set"])
    f = []
    if s2 != expected:
        f.append("W4LA-M12B-EDGE_SET_MISMATCH: section 2 %s" % sorted(s2))
    if s8 != expected:
        f.append("W4LA-M12B-EDGE_SET_MISMATCH: section 8 %s" % sorted(s8))
    if s2 != s8:
        f.append("W4LA-M12B-SECTION_DISAGREEMENT: %s vs %s" % (sorted(s2), sorted(s8)))
    return f


def check_m13_catalogue_dormancy(exp, texts=None):
    """Dormancy assertion only. No catalogue-ID validation exists.

    `texts` maps room -> contract text, so the check can be exercised against
    in-memory material. No test ever writes to a governed repository file.
    """
    f = []
    for c in exp["contracts"]:
        text = (texts or {}).get(c["room"]) or _read(c["path"])
        sec9 = "\n".join(split_sections(text).get(9, [])).lower()
        if "catalogue" not in sec9:
            f.append("W4LA-M13-NO_DORMANCY_DECLARATION: %s" % c["room"])
        elif "dormant" not in sec9 and "deferred" not in sec9:
            f.append("W4LA-M13-ACTIVE_CLAIM: %s" % c["room"])
    return f


PER_CONTRACT_CHECKS = [
    ("M02", check_m02_sections, None),
    ("M03", check_m03_na_reason, "na_construct_present"),
    ("M04A", check_m04a_open_questions_present, None),
    ("M04B", check_m04b_open_questions_empty_body, "open_questions_empty"),
    ("M05", check_m05_hooks_inventory, None),
    ("M06", check_m06_scope_integrity, None),
    ("M07", check_m07_load_bearing, None),
    ("M08", check_m08_shared_table, None),
    ("M09", check_m09_bait_declarations, None),
    ("M10", check_m10_contract_tokens, None),
    ("M11", check_m11_citations_resolve, None),
    ("M12A", check_m12a_anti_map, None),
    ("M12B", check_m12b_meditation_edge_set, "edge_set_exactness_required"),
]


def applicable_instances(exp):
    """Every executed instance key. Set-level plus per-contract conditionals."""
    keys = ["LA-M01-SET", "LA-M13-SET"]
    for c in exp["contracts"]:
        for name, _fn, flag in PER_CONTRACT_CHECKS:
            if flag is None or c.get(flag):
                keys.append("LA-%s-%s" % (name, c["room"]))
    return keys


# --------------------------------------------------------------------------
# positive canonical tests
# --------------------------------------------------------------------------

class LaneAMatrixShape(unittest.TestCase):
    """The corrected ADR 0022 matrix: 47 instances, by class and by scope."""

    def setUp(self):
        self.exp = _load_expectations()

    def test_instance_count_is_47(self):
        self.assertEqual(len(applicable_instances(self.exp)), EXPECTED_TOTAL_INSTANCES)

    def test_scope_counts_reconcile(self):
        keys = applicable_instances(self.exp)
        counts = {"set": sum(1 for k in keys if k.endswith("-SET"))}
        for c in self.exp["contracts"]:
            counts[c["room"]] = sum(1 for k in keys if k.endswith("-" + c["room"]))
        self.assertEqual(counts, EXPECTED_SCOPE_COUNTS)
        self.assertEqual(sum(counts.values()), EXPECTED_TOTAL_INSTANCES)

    def test_expectation_file_declares_its_governing_records(self):
        gov = self.exp["governing_records"]
        self.assertIn("ADR-0021", gov["base"])
        self.assertIn("ADR-0022", gov["correction"])

    def test_no_rejected_token_field_exists_anywhere(self):
        blob = json.dumps(self.exp)
        self.assertNotIn("rejected_token", blob)


class LaneAProvenance(unittest.TestCase):
    """Dual provenance (PR-R1..R5): immutable acceptance pairs, governed
    baseline pairs, and the three distinct relationships between them.

    These proofs sit OUTSIDE the 47 mechanical instances (PR-R6).
    """

    def setUp(self):
        self.exp = _load_expectations()

    @staticmethod
    def _blob_hash(commit, path):
        """LF-normalised hash of a contract blob at a historical commit."""
        import hashlib
        import subprocess
        out = subprocess.run(["git", "show", "%s:%s" % (commit, path)],
                             capture_output=True, cwd=str(ROOT))
        assert out.returncode == 0, "blob unreadable: %s:%s" % (commit[:10], path)
        return "sha256:" + hashlib.sha256(
            out.stdout.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()

    def test_set_anchor_unchanged(self):
        self.assertEqual(self.exp["baseline"]["contract_set_anchor_commit"],
                         "d237f2b54f8a5db6bf31afb73729260d79763987")

    def test_each_contract_carries_its_own_acceptance_provenance(self):
        commits = set()
        for c in self.exp["contracts"]:
            self.assertRegex(c["accepted_commit"], r"^[0-9a-f]{40}$")
            self.assertTrue(c["accepted_content_hash"].startswith("sha256:"))
            commits.add(c["accepted_commit"])
        self.assertEqual(len(commits), 4, "acceptance histories must stay distinct")

    def test_wellness_acceptance_pair_remains_pinned(self):
        """Immutable history: the E5 erratum must never rewrite acceptance."""
        w = [c for c in self.exp["contracts"] if c["room"] == "Wellness"][0]
        self.assertTrue(w["accepted_commit"].startswith("96ed013e"))
        self.assertTrue(w["accepted_content_hash"].startswith("sha256:c82221e1"))

    def test_acceptance_pair_coherence(self):
        """PR-R2: the accepted bytes really existed at the accepted commit."""
        for c in self.exp["contracts"]:
            with self.subTest(room=c["room"]):
                self.assertEqual(self._blob_hash(c["accepted_commit"], c["path"]),
                                 c["accepted_content_hash"])

    def test_governed_pair_coherence(self):
        """PR-R2: the governed bytes really exist at the governed commit."""
        for c in self.exp["contracts"]:
            with self.subTest(room=c["room"]):
                self.assertEqual(self._blob_hash(c["governed_baseline_commit"], c["path"]),
                                 c["governed_content_hash"])

    def test_governed_hash_equals_live_registry(self):
        """PR-R3: the frozen governed baseline has not fallen behind a lawful landing."""
        reg = json.loads((ROOT / "governance" / "registry.json").read_text(encoding="utf-8"))
        by_path = {e["path"]: e for e in reg["entries"]}
        for c in self.exp["contracts"]:
            with self.subTest(room=c["room"]):
                self.assertEqual(c["governed_content_hash"],
                                 by_path[c["path"]]["content_hash"])

    def test_wellness_dual_provenance_is_the_worked_case(self):
        """Both pairs recompute; they differ; acceptance predates the erratum."""
        w = [c for c in self.exp["contracts"] if c["room"] == "Wellness"][0]
        self.assertNotEqual(w["accepted_content_hash"], w["governed_content_hash"])
        self.assertNotEqual(w["accepted_commit"], w["governed_baseline_commit"])
        self.assertEqual(self._blob_hash(w["accepted_commit"], w["path"]),
                         w["accepted_content_hash"])
        self.assertEqual(self._blob_hash(w["governed_baseline_commit"], w["path"]),
                         w["governed_content_hash"])

    def test_ungoverned_mutation_still_produces_drift(self):
        """An in-memory byte change must show baseline_hash_matches False."""
        import hashlib
        c = self.exp["contracts"][0]
        raw = (ROOT / c["path"]).read_bytes() + b"x"
        observed = "sha256:" + hashlib.sha256(
            raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()
        self.assertFalse(observed == c["governed_content_hash"])


class LaneAContractSet(unittest.TestCase):
    """Set-level instances: M1 and M13."""

    def setUp(self):
        self.exp = _load_expectations()

    def test_m01_contract_set(self):
        self.assertEqual(check_m01_contract_set(self.exp), [])

    def test_m13_catalogue_dormancy(self):
        self.assertEqual(check_m13_catalogue_dormancy(self.exp), [])


class LaneAPerContract(unittest.TestCase):
    """Per-contract instances M2-M12, conditionals driven by expectation flags."""

    def setUp(self):
        self.exp = _load_expectations()

    def test_all_applicable_instances_pass(self):
        executed = []
        for c in self.exp["contracts"]:
            text = _read(c["path"])
            for name, fn, flag in PER_CONTRACT_CHECKS:
                if flag is not None and not c.get(flag):
                    continue
                key = "LA-%s-%s" % (name, c["room"])
                with self.subTest(instance=key):
                    self.assertEqual(fn(self.exp, c, text), [], key)
                executed.append(key)
        self.assertEqual(len(executed) + 2, EXPECTED_TOTAL_INSTANCES)

    def test_baseline_drift_is_orthogonal_diagnostic_only(self):
        """Drift compares observed bytes against the GOVERNED baseline (PR-R4).

        Acceptance provenance rides along as immutable historical context. A
        lawfully amended contract with a refreshed governed pair shows True;
        an ungoverned mutation shows False. Never a check state or an instance.
        """
        import hashlib
        for c in self.exp["contracts"]:
            raw = (ROOT / c["path"]).read_bytes()
            observed = "sha256:" + hashlib.sha256(
                raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()
            diagnostic = {
                "room": c["room"],
                "accepted_content_hash": c["accepted_content_hash"],
                "governed_content_hash": c["governed_content_hash"],
                "observed_content_hash": observed,
                "baseline_hash_matches": observed == c["governed_content_hash"],
            }
            self.assertTrue(diagnostic["baseline_hash_matches"],
                            "%s: lawful governed baseline must match" % c["room"])
            self.assertNotIn("baseline_drift", str(applicable_instances(self.exp)))


# --------------------------------------------------------------------------
# positive regression / false-positive guards
# --------------------------------------------------------------------------

class LaneAFalsePositiveGuards(unittest.TestCase):
    """Conforming contracts must keep passing despite text that fools a naive checker."""

    def setUp(self):
        self.exp = _load_expectations()
        self.by_room = {c["room"]: c for c in self.exp["contracts"]}

    def test_guard1_quoted_not_applicable_is_not_an_na_construct(self):
        for room in ("Wellness", "Kitchen", "Gym"):
            c = self.by_room[room]
            text = _read(c["path"])
            self.assertIn("Not applicable", text, "phrase should be present in the quoted table")
            self.assertEqual(find_na_constructs(split_sections(text)), [], room)
            self.assertEqual(check_m03_na_reason(self.exp, c, text), [], room)

    def test_guard2_quoted_meditation_edge_tokens_are_not_asserted(self):
        c = self.by_room["Meditation"]
        text = _read(c["path"])
        for tok in ("E11-W", "E11-K", "E11-G", "E12"):
            self.assertIn(tok, text, "token should be present inside the quoted E11 rule")
        secs = split_sections(text)
        self.assertEqual(extract_edge_ids(secs[2]), {"M1", "M2"})
        self.assertEqual(extract_edge_ids(secs[8]), {"M1", "M2"})
        self.assertEqual(check_m12b_meditation_edge_set(self.exp, c, text), [])

    def test_guard3_wellness_non_empty_section_11_is_lawful(self):
        c = self.by_room["Wellness"]
        text = _read(c["path"])
        self.assertFalse(c["open_questions_empty"])
        self.assertEqual(check_m04a_open_questions_present(self.exp, c, text), [])
        # M4b must not run for Wellness; if it did, it would fail
        self.assertNotEqual(check_m04b_open_questions_empty_body(self.exp, c, text), [])

    def test_guard4_quoted_table_numerals_are_not_sections(self):
        for c in self.exp["contracts"]:
            text = _read(c["path"])
            self.assertEqual(section_order(text), self.exp["shared"]["expected_section_numbers"],
                             c["room"])

    def test_guard5_gym_e7_reference_preserved_as_reference(self):
        text = _read(self.by_room["Gym"]["path"])
        self.assertIn("Same conditions as E6", text)
        self.assertEqual(check_m07_load_bearing(self.exp, self.by_room["Gym"], text), [])

    def test_guard6_incidental_substrings_are_not_contract_tokens(self):
        grammar = self.exp["shared"]["contract_token_grammar"]
        canonical = set(self.exp["shared"]["canonical_placeholder_set"])
        for c in self.exp["contracts"]:
            found = contract_tokens(_read(c["path"]), grammar)
            self.assertTrue(set(found) <= canonical, "%s: %s" % (c["room"], found))
        self.assertEqual(re.findall(grammar, "Health-Data Room-Contract Wellbeing-Wing"), [])


# --------------------------------------------------------------------------
# negative validator scenarios -- runtime mutations, discarded after use
# --------------------------------------------------------------------------

class LaneANegativeScenarios(unittest.TestCase):
    """One controlled mutation per scenario; expected error identifier asserted."""

    def setUp(self):
        self.exp = _load_expectations()
        self.by_room = {c["room"]: c for c in self.exp["contracts"]}

    def _text(self, room):
        return _read(self.by_room[room]["path"])

    def _assert_fails(self, failures, errid):
        self.assertTrue(failures, "expected a failure carrying %s" % errid)
        self.assertTrue(any(f.startswith(errid) for f in failures),
                        "expected %s, got %s" % (errid, failures[:2]))
        for f in failures:
            self.assertLess(len(f), 200, "failure evidence must stay bounded")

    # --- M1 (2) ---
    def test_neg01_m01_duplicate_room_identity(self):
        exp = _load_expectations()
        exp["contracts"].append(dict(exp["contracts"][0]))
        self._assert_fails(check_m01_contract_set(exp), "W4LA-M01-DUPLICATE_IDENTITY")

    def test_neg02_m01_missing_contract_path(self):
        exp = _load_expectations()
        exp["contracts"][0] = dict(exp["contracts"][0], path="docs/rooms/absent-room-contract.md")
        self._assert_fails(check_m01_contract_set(exp), "W4LA-M01-MISSING")

    # --- M2 (2) ---
    def test_neg03_m02_missing_section(self):
        t = self._text("Gym").replace("\n## 7. Speech rules", "\n### 7x removed", 1)
        self._assert_fails(check_m02_sections(self.exp, self.by_room["Gym"], t), "W4LA-M02-ORDER")

    def test_neg04_m02_misordered_sections(self):
        t = self._text("Gym").replace("\n## 7. Speech rules", "\n## 9. Speech rules", 1)
        self._assert_fails(check_m02_sections(self.exp, self.by_room["Gym"], t), "W4LA-M02-ORDER")

    # --- M3 (2) ---
    def test_neg05_m03_bare_na_without_reason(self):
        c = self.by_room["Meditation"]
        t = self._text("Meditation")
        old = [l for l in t.splitlines() if NA_RE.match(l.strip())][0]
        t = t.replace(old, "**Not applicable —**", 1)
        self._assert_fails(check_m03_na_reason(self.exp, c, t), "W4LA-M03-BARE_NA")

    def test_neg06_m03_unexpected_na_construct(self):
        c = self.by_room["Kitchen"]
        t = self._text("Kitchen").replace("\n## 8.", "\n**Not applicable — invented.**\n\n## 8.", 1)
        self._assert_fails(check_m03_na_reason(self.exp, c, t), "W4LA-M03-UNEXPECTED")

    # --- M4 (2) ---
    def test_neg07_m04a_section_11_removed(self):
        c = self.by_room["Gym"]
        t = self._text("Gym")
        t = t[:t.index("\n## 11.")] + "\n"
        self._assert_fails(check_m04a_open_questions_present(self.exp, c, t), "W4LA-M04A-MISSING")

    def test_neg08_m04b_altered_empty_body(self):
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("None at acceptance.", "**None at acceptance.**", 1)
        self._assert_fails(check_m04b_open_questions_empty_body(self.exp, c, t),
                           "W4LA-M04B-BODY_MISMATCH")

    # --- M5 (5 accepted failure forms) ---
    def _m5_mutate(self, room, old, new):
        c = self.by_room[room]
        return check_m05_hooks_inventory(self.exp, c, self._text(room).replace(old, new, 1))

    def test_neg09_m05_expected_entry_missing(self):
        c = self.by_room["Gym"]
        entry = c["section9_inventory"]["mechanical"][0]["entry"]
        self._assert_fails(self._m5_mutate("Gym", "- " + entry, "(removed)"),
                           "W4LA-M05-MISSING_ENTRY")

    def test_neg10_m05_unexpected_entry_added(self):
        c = self.by_room["Gym"]
        entry = c["section9_inventory"]["mechanical"][0]["entry"]
        self._assert_fails(self._m5_mutate("Gym", "- " + entry,
                                           "- an invented governed term;\n- " + entry),
                           "W4LA-M05-UNEXPECTED_ENTRY")

    def test_neg11_m05_entry_outside_both_classifications(self):
        """An entry removed from its class and placed in the boundary block is 'missing'."""
        c = self.by_room["Kitchen"]
        entry = c["section9_inventory"]["mechanical"][0]["entry"]
        self._assert_fails(self._m5_mutate("Kitchen", "- " + entry, "(moved out of both classes)"),
                           "W4LA-M05-MISSING_ENTRY")

    def test_neg12_m05_double_classified_entry(self):
        c = self.by_room["Gym"]
        mech = c["section9_inventory"]["mechanical"][0]["entry"]
        rev = c["section9_inventory"]["review_only"][0]["entry"]
        f = self._m5_mutate("Gym", "- " + rev, "- " + rev + "\n- " + mech)
        self._assert_fails(f, "W4LA-M05-DOUBLE_CLASSIFIED")

    def test_neg13_m05_entry_moved_between_classifications(self):
        c = self.by_room["Gym"]
        mech = c["section9_inventory"]["mechanical"][0]["entry"]
        rev = c["section9_inventory"]["review_only"][0]["entry"]
        t = self._text("Gym").replace("- " + mech + "\n", "", 1).replace(
            "- " + rev, "- " + mech + "\n- " + rev, 1)
        self._assert_fails(check_m05_hooks_inventory(self.exp, c, t), "W4LA-M05-MOVED_ENTRY")

    # --- M6 (2) ---
    def test_neg14_m06_altered_scope_quotation(self):
        """A changed word inside a carried scope clause still fails."""
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("confirmed injury/physical notes only",
                                      "injury/physical notes only", 1)
        self._assert_fails(check_m06_scope_integrity(self.exp, c, t),
                           "W4LA-M06-QUOTATION_MISMATCH")

    def test_neg27_m06_dropped_source_list_marker(self):
        """Strict M6: dropping a source-owned list marker fails — the E5 class."""
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("> - **E7. Approved Profile",
                                      "> **E7. Approved Profile", 1)
        self._assert_fails(check_m06_scope_integrity(self.exp, c, t),
                           "W4LA-M06-QUOTATION_MISMATCH")

    # --- M7 (2) ---
    def test_neg15_m07_missing_load_bearing_word(self):
        c = self.by_room["Kitchen"]
        t = self._text("Kitchen").replace("confirmed dietary requirements only",
                                          "dietary requirements")
        self._assert_fails(check_m07_load_bearing(self.exp, c, t), "W4LA-M07-MISSING_WORD")

    def test_neg16_m07_blur_phrase_inserted_into_scope_clause(self):
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("> - **E7. Approved Profile",
                                      "> - such as **E7. Approved Profile", 1)
        self._assert_fails(check_m07_load_bearing(self.exp, c, t), "W4LA-M07-BLUR_PHRASE")

    # --- M8 (1) ---
    def test_neg17_m08_altered_shared_table_line(self):
        c = self.by_room["Kitchen"]
        t = self._text("Kitchen").replace("> | **Superseded** | \"Replaced; permanent terminal state\"",
                                          "> | **Superseded** | \"Replaced; terminal state\"", 1)
        self._assert_fails(check_m08_shared_table(self.exp, c, t), "W4LA-M08-TABLE_MISMATCH")

    # --- M9 (2) ---
    def test_neg18_m09_bait_with_two_declarations(self):
        c = self.by_room["Meditation"]
        decl = self.exp["shared"]["fixture_declaration_text"]
        t = self._text("Meditation").replace(decl, decl + " " + decl, 1)
        self._assert_fails(check_m09_bait_declarations(self.exp, c, t),
                           "W4LA-M09-DECLARATION_COUNT")

    def test_neg19_m09_bait_with_zero_declarations(self):
        c = self.by_room["Meditation"]
        decl = self.exp["shared"]["fixture_declaration_text"]
        t = self._text("Meditation").replace(decl, "(declaration removed)", 1)
        self._assert_fails(check_m09_bait_declarations(self.exp, c, t),
                           "W4LA-M09-DECLARATION_COUNT")

    # --- M10 (1) ---
    def test_neg20_m10_non_canonical_contract_token(self):
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("\n## 4. Inference prohibitions",
                                      "\n## 4. Inference prohibitions\n\nSample-Z1 appears.", 1)
        self._assert_fails(check_m10_contract_tokens(self.exp, c, t),
                           "W4LA-M10-NON_CANONICAL_TOKEN")

    # --- M11 (2) ---
    def test_neg21_m11_dangling_cited_path(self):
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("\n## 2. Read scope",
                                      "\n## 2. Read scope\n\nSee `docs/absent/nowhere.md`.", 1)
        self._assert_fails(check_m11_citations_resolve(self.exp, c, t), "W4LA-M11-DANGLING_PATH")

    def test_neg22_m11_isolation_citation_removed(self):
        c = self.by_room["Gym"]
        t = self._text("Gym")
        secs = split_sections(t)
        t = t.replace("ADR-0017", "ADR-XXXX")
        self._assert_fails(check_m11_citations_resolve(self.exp, c, t),
                           "W4LA-M11-ISOLATION_CITATION")

    # --- M12a (2 accepted mismatch classes) ---
    def test_neg23_m12a_missing_anti_map_identifier(self):
        c = self.by_room["Kitchen"]
        t = self._text("Kitchen")
        start = t.index("\n## 8.")
        end = t.index("\n## 9.")
        t = t[:start] + t[start:end].replace("E10", "the vendor edge") + t[end:]
        self._assert_fails(check_m12a_anti_map(self.exp, c, t),
                           "W4LA-M12A-MISSING_IDENTIFIER")

    def test_neg24_m12a_unexpected_anti_map_identifier(self):
        c = self.by_room["Gym"]
        t = self._text("Gym").replace("\n## 8. Forbidden list",
                                      "\n## 8. Forbidden list\n\n- nothing beyond E5;", 1)
        self._assert_fails(check_m12a_anti_map(self.exp, c, t),
                           "W4LA-M12A-UNEXPECTED_IDENTIFIER")

    # --- M13 (1) ---
    def test_neg26_m13_dormancy_declaration_removed(self):
        """A contract that stops declaring catalogue dormancy fails M13.

        Mutated in memory only. No test writes to a governed repository file.
        """
        mutated = {"Gym": re.sub(r"catalogue", "string-index", self._text("Gym"), flags=re.I)}
        self._assert_fails(check_m13_catalogue_dormancy(self.exp, texts=mutated),
                           "W4LA-M13-NO_DORMANCY_DECLARATION")

    # --- M12b (1) ---
    def test_neg25_m12b_meditation_edge_set_altered(self):
        c = self.by_room["Meditation"]
        t = self._text("Meditation").replace("hold or use any edge beyond **M1 and M2**",
                                             "hold or use any edge beyond **M1, M2 and E6**", 1)
        self._assert_fails(check_m12b_meditation_edge_set(self.exp, c, t),
                           "W4LA-M12B-EDGE_SET_MISMATCH")


if __name__ == "__main__":
    unittest.main()
