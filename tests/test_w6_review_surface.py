"""W6 — review-surface structural proofs (the W6-D4-F landing, merged
with D/E per the accepted opening record).

Proves the static review surface against ADR-0043's obligations and
the W6-D4-A/B/C contract: reads only declared inputs, writes nothing
but its two outputs, holds no state, opens no channel, carries no
affordance, grades nothing, and renders every governed item with its
own mandatory trace row (Tara's state-family directive: family
reasoning is explanatory; the per-item trace is the accountability).
A green run means contract conformance only — never that anything
shown is approved, correct, safe, or authorised for any other display.
"""

import ast
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "scripts" / "generate_review_surface.py"
SURF = ROOT / "docs" / "surface"
HTML = SURF / "review-surface.html"
DECL = SURF / "surface-declarations.json"
TRACE = SURF / "surface-trace.json"

EXPECTED_SECTIONS = {"register": 33, "evidence": 65,
                     "evaluation-fixtures": 23,
                     "evaluation-unknowns": 26,
                     "evaluation-routed": 25,
                     "pending-stubs": 9, "carried-questions": 7}
LAWFUL_PASSED = ["review interval has passed",
                 "renewal grace period has passed"]


def page():
    return HTML.read_text(encoding="utf-8")


def trace_rows():
    return json.loads(TRACE.read_text(encoding="utf-8"))["rows"]


def decl():
    return json.loads(DECL.read_text(encoding="utf-8"))


class GeneratorBoundaries(unittest.TestCase):
    def test_imports_are_stdlib_read_only_and_clockless(self):
        tree = ast.parse(GEN.read_text(encoding="utf-8"))
        banned = {"socket", "ssl", "http", "urllib", "requests",
                  "subprocess", "time", "datetime", "sched",
                  "threading", "asyncio", "logging", "os", "random",
                  "uuid", "shutil", "tempfile", "sqlite3", "pickle",
                  "shelve"}
        seen = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    seen.add(a.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                seen.add(node.module.split(".")[0])
        self.assertFalse(seen & banned, seen & banned)
        self.assertTrue(seen <= {"html", "json", "re", "sys",
                                 "pathlib"}, seen)

    def test_no_discovery_no_walk_no_env(self):
        src = GEN.read_text(encoding="utf-8")
        for token in ("os.walk", "rglob", "os.environ", "getenv",
                      "iterdir", "scandir"):
            self.assertNotIn(token, src)
        # exactly one declared glob: the evaluation-records pattern
        self.assertEqual(src.count(".glob("), 1)

    def test_write_paths_are_exactly_the_two_outputs(self):
        tree = ast.parse(GEN.read_text(encoding="utf-8"))
        writes = [n for n in ast.walk(tree)
                  if isinstance(n, ast.Call)
                  and isinstance(n.func, ast.Attribute)
                  and n.func.attr in ("write_text", "write_bytes")]
        self.assertEqual(len(writes), 2)

    def test_undeclared_input_refuses(self):
        src = GEN.read_text(encoding="utf-8")
        self.assertIn("undeclared input refused", src)
        self.assertIn("PermissionError", src)

    def test_declared_inputs_match_the_contract(self):
        src = GEN.read_text(encoding="utf-8")
        for rel in decl()["source_inputs"]:
            self.assertIn(rel.rstrip("/").split("/")[-1], src)


class Determinism(unittest.TestCase):
    def test_regeneration_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "surface"
            r = subprocess.run(
                [sys.executable, str(GEN), str(ROOT), str(out)],
                capture_output=True)
            self.assertEqual(r.returncode, 0, r.stderr[-300:])
            self.assertEqual((out / "review-surface.html").read_bytes(),
                             HTML.read_bytes())
            self.assertEqual((out / "surface-trace.json").read_bytes(),
                             TRACE.read_bytes())


class NoAffordances(unittest.TestCase):
    def test_no_scripts_forms_controls_or_links(self):
        h = page().lower()
        for bad in ("<script", "<form", "<input", "<button", "<select",
                    "<textarea", "<a ", "<a>", "onclick", "onload",
                    "javascript:"):
            self.assertNotIn(bad, h)

    def test_no_external_references(self):
        self.assertNotIn("://", page())

    def test_no_verdict_glyphs(self):
        h = page()
        for glyph in ("✓", "✗", "✔", "✘",
                      "❌", "✅"):
            self.assertNotIn(glyph, h)

    def test_no_ceremony_words_as_controls(self):
        # the words appear only inside negations/accompaniments; no
        # markup element carries them as an action label
        h = page().lower()
        for phrase in ("approve all", "convert all", "resolve all",
                       "retire all", "mark done", "mark as done"):
            self.assertNotIn(phrase, h)


class VisualLaw(unittest.TestCase):
    def test_palette_is_declared_and_neutral(self):
        css = re.search(r"<style>(.*?)</style>", page(), re.S).group(1)
        colours = set(re.findall(r"#[0-9a-fA-F]{6}", css))
        declared = set(decl()["declared_palette"])
        self.assertTrue(colours <= declared, colours - declared)
        for c in colours:
            r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
            self.assertTrue(abs(r - g) < 8 and abs(g - b) < 8,
                            c + " is not neutral grey")

    def test_colour_semantic_mapping_is_none(self):
        self.assertTrue(decl()["colour_semantic_mapping"]
                        .startswith("none"))

    def test_inventories_are_empty_as_declared(self):
        d = decl()
        self.assertEqual(d["glyph_inventory"], [])
        self.assertEqual(d["affordance_inventory"], [])
        for key in ("write_paths", "persistence_paths",
                    "external_paths"):
            self.assertEqual(d[key], "none")


class TraceBijection(unittest.TestCase):
    def test_section_counts_exact(self):
        from collections import Counter
        counts = Counter(r["section"] for r in trace_rows())
        self.assertEqual(dict(counts), EXPECTED_SECTIONS)

    def test_every_trace_row_is_rendered(self):
        import html as _html
        h = page()
        for r in trace_rows():
            item = str(r["item_id"])
            self.assertTrue(
                item in h or _html.escape(item, quote=True) in h,
                item)

    def test_every_governed_item_has_a_trace_row(self):
        ids = {r["item_id"] for r in trace_rows()}
        cat = json.loads((ROOT / "governance" / "string-catalogue.json")
                         .read_text(encoding="utf-8"))
        for e in cat["entries"]:
            self.assertIn(e["id"], ids)
        phdar = (ROOT / "docs" / "governance" /
                 "privacy-health-data-assurance-record.md"
                 ).read_text(encoding="utf-8")
        for row_id in re.findall(r'"row_id": "(AR-[A-Z]+-\d\d)"',
                                 phdar):
            self.assertIn(row_id, ids)
        for p in sorted((ROOT / "governance" / "evaluation")
                        .glob("*FIX-*.json")):
            rec = json.loads(p.read_text(encoding="utf-8"))
            self.assertIn(rec["evaluation_record"]["fixture_id"], ids)

    def test_every_row_carries_the_mandatory_fields(self):
        for r in trace_rows():
            for field in ("section", "item_id", "source", "state",
                          "accompaniment", "rendered_wording", "proof",
                          "non_authority"):
                self.assertTrue(r.get(field) or field == "cat_id",
                                (r["item_id"], field))
            self.assertEqual(r["proof"], "rendered-and-traced")
            self.assertIn("nothing rendered is approval",
                          r["non_authority"])

    def test_register_rows_carry_cat_ids_and_others_do_not(self):
        for r in trace_rows():
            if r["section"] == "register":
                self.assertRegex(r["cat_id"], r"^CAT-\d{4}$")
            else:
                self.assertIsNone(r["cat_id"])


class HonestStateRendering(unittest.TestCase):
    def test_accompaniments_render_inline(self):
        h = page()
        import html as _html
        for a in decl()["mandatory_accompaniments"]:
            needle = _html.escape(a["text"], quote=True)[:40]
            self.assertIn(needle, h, a["state"])

    def test_aphorisms_render(self):
        h = page().lower()
        for phrase in ("viewing is not reviewing",
                       "clicking is not deciding",
                       "selecting is not approving"):
            self.assertIn(phrase, h)

    def test_uncomfortable_states_render_at_full_size(self):
        h = page()
        self.assertIn("not evidenced", h)
        self.assertIn("applicability unresolved", h)
        self.assertIn("unknown-not-absent", h)
        self.assertIn("pending — not converted", h)
        self.assertIn("carried — still alive", h)

    def test_routed_deltas_carry_both_variants_whole(self):
        h = page()
        for r in trace_rows():
            if r["section"] == "evaluation-routed":
                self.assertIn("With bait", h)
                self.assertIn("Without bait", h)
        self.assertIn("No selected "
                      "variant exists unless a human record later "
                      "creates one", h.replace("\n", " "))

    def test_ceiling_and_grading_ceiling_render(self):
        h = page()
        self.assertIn("never sufficient for display", h)
        self.assertIn("a grade is not approval and not display "
                      "permission", h)

    def test_no_display_authorisation_claim(self):
        h = page().lower()
        for claim in ("authorises display", "approved for display",
                      "display permitted", "safe to display"):
            self.assertNotIn(claim, h)


class BarredWording(unittest.TestCase):
    def test_no_barred_affirmatives_outside_lawful_contexts(self):
        h = page().lower()
        for coll in LAWFUL_PASSED:
            h = h.replace(coll, " ")
        # the ADR-0037 decision 11 named mechanical exception: the
        # runtime's crossing event name, carried verbatim in the
        # routed-delta variant captures — an event name, never a claim
        h = h.replace("authority-checks-passed", " ")
        # lawful negation carriers removed before the scan
        for neg in ("is not passed", "not passed",
                    "executed-is-not-passed", "never a pass",
                    "never sufficient", "not approval",
                    "not a claim", "no pass is implied"):
            h = h.replace(neg, " ")
        for phrase in ("clinically safe", "medically safe",
                       "legally satisfied", "production-ready",
                       "certif", "complian", "all-green",
                       "success verdict", "approved by the system"):
            self.assertNotIn(phrase, h)
        self.assertEqual(re.findall(r"\bpassed\b", h), [])


class OutputHome(unittest.TestCase):
    def test_artefacts_live_only_under_docs_surface(self):
        names = sorted(p.name for p in SURF.iterdir() if p.is_file())
        self.assertEqual(names, ["review-surface.html",
                                 "surface-declarations.json",
                                 "surface-trace.json"])


if __name__ == "__main__":
    unittest.main()
