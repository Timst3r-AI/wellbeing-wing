"""W4-D6 Lane B — deterministic corpus validator (static conformance only).

Proves the behavioural-evaluation fixture corpus conforms to the published
strategy (W4-D6-BEF) and its accepted rulings: corpus and map cardinality,
referential integrity, schema and marker fidelity, pinned provenance and quote
fidelity, probe floors and silent-channel structure, placeholder discipline,
and execution-deferral truth.

Boundary (B-R60, B-R42, B-R46, B-R54, B-R55): this module executes no
behavioural test, interprets no runtime delta, claims no behavioural success,
creates no placeholder rule, infers no placeholder authority from family, and
contains no W5 runtime logic. A green run means the traps are well-formed and
referenced — nothing more. Every fixture is, and remains, behaviourally
unexecuted in W4. Validator output does not mint doctrine.
"""

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRATEGY_PATH = ROOT / "docs" / "governance" / "behavioural-evaluation-fixtures.md"
FIXTURES_DOC = ROOT / "docs" / "governance" / "fixtures.md"
REGISTRY_PATH = ROOT / "governance" / "registry.json"
FIXTURE_DIR = ROOT / "fixtures"

FIX_RE = re.compile(r"^FIX-(WELL|KITCH|GYM|MED)-\d\d$")
CONTRACT_FOR_ROOM = {"WELL": "W4-D2", "KITCH": "W4-D3", "GYM": "W4-D4", "MED": "W4-D5"}
ROOM_NAME = {"WELL": "Wellness", "KITCH": "Kitchen", "GYM": "Gym", "MED": "Meditation"}
STATUS = "behaviourally_unexecuted"
SURFACES = ["spoken_output", "persisted_state", "routing_propagation",
            "behaviour_selection_ranking_framing_omission"]
# accepted probe floors: two per bait unless a ruling derived more
FLOORS = {"KITCH-B5": 4, "MED-B4": 4, "MED-B7": 3}
LIMBED = {"KITCH-B5": ["preference", "confirmed-dietary-tier"], "MED-B4": ["absence", "pattern"]}
FAMILY_COUNTS = {"F-ABS": 4, "F-PAT": 6, "F-ELEV": 5, "F-REF": 3, "F-CM": 3, "F-ISO": 2}
SHORTHAND = re.compile(r"\bas (?:in )?P[0-9]\b")
# concrete accepted-corpus token conformance (B-R55): the canonical placeholder
# register plus the specifically accepted Ingredient-X precedent — no family law
ALLOWED_TOKEN = re.compile(r"^(Persona-K[0-9]+|Allergen-X|Ingredient-X|Condition-Q|Medication-A17)$")
TOKEN_SHAPE = re.compile(r"\b[A-Z][a-z]+-[A-Z][0-9]*\b")
NAME_PAIR = re.compile(r"\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b")
# B-R54: only actual behavioural-result payload keys are prohibited;
# result_location is mandatory lawful metadata and is not matched by this rule
RESULT_PAYLOAD_KEY = re.compile(r"^(results?|outcomes?|verdicts?|scores?|passed|failed|pass_fail|execution_results?|observations?)$")
SCHEMA_KEYS = ["fixture_id", "room", "contract_registry_id", "contract_path", "bait_label",
               "bait_title", "source_declaration", "forbidden_move", "lawful_boundary",
               "family", "priority_note", "channels_under_test", "probes",
               "execution_status", "execution_dependency", "result_location"]
QUOTE_PREFIXES = {
    "forbidden_move": ["- **Forbidden system move:** "],
    "lawful_boundary": ["- **Lawful response boundary:** "],
    "source_declaration": ["- **Future fixture declaration:** ", "- **Future fixture:** "],
}


def _read(path):
    return path.read_text(encoding="utf-8")


def _strategy():
    return _read(STRATEGY_PATH)


def _live_map():
    blocks = re.findall(r"```json\n(.*?)\n```", _strategy(), re.S)
    arrays = [b for b in blocks if b.strip().startswith("[")]
    return json.loads(arrays[-1])


def _fixture_files():
    return sorted(FIXTURE_DIR.glob("SYNTHETIC-fix-*.json"))


def _fixtures():
    out = []
    for p in _fixture_files():
        out.append((p, json.loads(_read(p))))
    return out


def _strategy_string(field):
    m = re.search(r'"%s": "([^"]+)"' % field, _strategy())
    return m.group(1) if m else None


def _git_show(ref):
    r = subprocess.run(["git", "-C", str(ROOT), "show", ref], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


class MapIntegrity(unittest.TestCase):
    def test_map_cardinality_and_bijection(self):
        rows = _live_map()
        self.assertEqual(len(rows), 23)
        baits = [r["bait_label"] for r in rows]
        fixes = [r["fixture_id"] for r in rows]
        self.assertEqual(len(set(baits)), 23, "duplicate or missing bait")
        self.assertEqual(len(set(fixes)), 23, "duplicate or missing fixture reference")
        by_id = {d["evaluation_fixture"]["fixture_id"]: (p, d) for p, d in _fixtures()}
        for row in rows:
            with self.subTest(bait=row["bait_label"]):
                self.assertEqual(sorted(row.keys()),
                                 sorted(["bait_label", "contract_registry_id", "fixture_id",
                                         "fixture_path", "family", "execution_status",
                                         "superseded_by"]))
                room = row["bait_label"].split("-")[0]
                self.assertEqual(row["contract_registry_id"], CONTRACT_FOR_ROOM[room])
                self.assertTrue(row["fixture_id"].startswith("FIX-%s-" % room))
                self.assertEqual(row["execution_status"], STATUS)
                self.assertIsNone(row["superseded_by"])
                self.assertIn(row["fixture_id"], by_id, "orphan map row")
                path, data = by_id[row["fixture_id"]]
                self.assertEqual(row["fixture_path"], "fixtures/" + path.name)
                ev = data["evaluation_fixture"]
                self.assertEqual(row["family"], ev["family"], "map/fixture family disagreement")
                self.assertEqual(ev["execution_status"], STATUS, "map/fixture status disagreement")
                self.assertEqual(ev["bait_label"], row["bait_label"])

    def test_no_orphan_fixture(self):
        mapped = {r["fixture_id"] for r in _live_map()}
        for p, d in _fixtures():
            with self.subTest(file=p.name):
                self.assertIn(d["evaluation_fixture"]["fixture_id"], mapped, "orphan fixture file")


class CorpusShape(unittest.TestCase):
    def test_fixture_file_cardinality(self):
        self.assertEqual(len(_fixture_files()), 23)

    def test_fix_grammar_uniqueness_and_filename(self):
        seen = set()
        for p, d in _fixtures():
            with self.subTest(file=p.name):
                fid = d["evaluation_fixture"]["fixture_id"]
                self.assertRegex(fid, FIX_RE)
                self.assertNotIn(fid, seen, "duplicate FIX id")
                seen.add(fid)
                self.assertTrue(p.name.startswith("SYNTHETIC-%s-" % fid.lower()),
                                "filename does not carry its fixture id")

    def test_family_membership_and_counts(self):
        counts = {}
        for p, d in _fixtures():
            fam = d["evaluation_fixture"]["family"]
            with self.subTest(file=p.name):
                self.assertIn(fam, FAMILY_COUNTS)
            counts[fam] = counts.get(fam, 0) + 1
        self.assertEqual(counts, FAMILY_COUNTS)

    def test_schema_and_marker(self):
        notice = re.search(r'"notice": "([^"]+)"', _read(FIXTURES_DOC)).group(1)
        for p, d in _fixtures():
            with self.subTest(file=p.name):
                self.assertEqual(list(d.keys()), ["synthetic_marker", "evaluation_fixture"])
                marker = d["synthetic_marker"]
                self.assertIs(marker["synthetic"], True)
                self.assertEqual(marker["notice"], notice)
                self.assertTrue(marker["exercises"], "exercises must be non-empty")
                self.assertTrue(marker["persona"])
                ev = d["evaluation_fixture"]
                self.assertEqual(list(ev.keys()), SCHEMA_KEYS)
                room = ev["fixture_id"].split("-")[1]
                self.assertEqual(ev["room"], ROOM_NAME[room])
                self.assertEqual(ev["contract_registry_id"], CONTRACT_FOR_ROOM[room])


class ProvenanceAndQuotes(unittest.TestCase):
    def test_pinned_provenance_and_quote_fidelity(self):
        for p, d in _fixtures():
            ev = d["evaluation_fixture"]
            with self.subTest(file=p.name):
                for key in QUOTE_PREFIXES:
                    prov = ev[key]["provenance"]
                    self.assertRegex(prov["accepted_commit"], r"^[0-9a-f]{40}$")
                    self.assertRegex(prov["accepted_content_hash"], r"^sha256:[0-9a-f]{64}$")
                commit = ev["forbidden_move"]["provenance"]["accepted_commit"]
                chash = ev["forbidden_move"]["provenance"]["accepted_content_hash"]
                blob = _git_show("%s:%s" % (commit, ev["contract_path"]))
                self.assertIsNotNone(blob, "pinned contract blob unavailable")
                norm = blob.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
                self.assertEqual("sha256:" + hashlib.sha256(norm).hexdigest(), chash,
                                 "pinned blob does not match accepted content hash")
                for key, prefixes in QUOTE_PREFIXES.items():
                    quote = ev[key]["quote"]
                    self.assertTrue(any((pref + quote) in blob for pref in prefixes),
                                    "%s quote is not byte-exact in pinned source" % key)
                # drift against the live governed contract is a diagnostic, never a failure
                live = _read(ROOT / ev["contract_path"])
                for key, prefixes in QUOTE_PREFIXES.items():
                    quote = ev[key]["quote"]
                    if not any((pref + quote) in live for pref in prefixes):
                        print("DIAGNOSTIC (not a failure): %s %s quote drifts from live governed contract"
                              % (ev["fixture_id"], key))


class ProbeStructure(unittest.TestCase):
    def test_floors_channels_limbs_and_silent_contract(self):
        base = None
        m = re.search(r'"pass_condition": "([^"]+)"', _strategy())
        if m:
            base = m.group(1)
        for p, d in _fixtures():
            ev = d["evaluation_fixture"]
            probes = ev["probes"]
            bait = ev["bait_label"]
            with self.subTest(file=p.name):
                self.assertEqual(len(probes), FLOORS.get(bait, 2), "probe floor violated")
                self.assertEqual({pr["channel"] for pr in probes}, {"overt", "silent"})
                pids = [pr["probe_id"] for pr in probes]
                self.assertEqual(len(set(pids)), len(pids), "probe ids must be locally unique")
                if bait in LIMBED:
                    expected = [(limb, ch) for limb in LIMBED[bait] for ch in ("overt", "silent")]
                    self.assertEqual([(pr["limb"], pr["channel"]) for pr in probes], expected)
                if bait == "MED-B7":
                    self.assertIn("consent does not create authority",
                                  probes[2]["required_outcome_class"],
                                  "MED-B7 consent special-case probe missing")
                for pr in probes:
                    self.assertTrue(pr["scenario"], "scenario must be self-contained data")
                    if pr["channel"] == "silent":
                        sp = pr["silent_probe"]
                        self.assertIsNotNone(sp)
                        self.assertEqual(sp["observed_surfaces"], SURFACES)
                        self.assertTrue(sp["context_present_variant"])
                        self.assertTrue(sp["context_absent_variant"])
                        if base:
                            self.assertTrue(sp["pass_condition"].startswith(base),
                                            "silent pass condition must open with the strategy base sentence")
                    else:
                        self.assertIsNone(pr["silent_probe"])


class DisciplineAndDeferral(unittest.TestCase):
    def test_zero_cross_probe_shorthand(self):
        for p, _ in _fixtures():
            with self.subTest(file=p.name):
                self.assertIsNone(SHORTHAND.search(_read(p)), "cross-probe shorthand found")

    def test_concrete_placeholder_conformance(self):
        for p, _ in _fixtures():
            text = _read(p)
            with self.subTest(file=p.name):
                for tok in set(TOKEN_SHAPE.findall(text)):
                    self.assertRegex(tok, ALLOWED_TOKEN,
                                     "token outside the accepted concrete corpus vocabulary")
                names = [m for m in NAME_PAIR.findall(text) if not TOKEN_SHAPE.match(m)]
                self.assertEqual(names, [], "human-plausible name pair in fixture")

    def test_execution_deferral_truth(self):
        dep = _strategy_string("execution_dependency")
        loc = _strategy_string("result_location")
        self.assertTrue(dep and loc, "strategy must carry the deferral strings")
        for p, d in _fixtures():
            ev = d["evaluation_fixture"]
            with self.subTest(file=p.name):
                self.assertEqual(ev["execution_status"], STATUS)
                self.assertEqual(ev["execution_dependency"], dep)
                self.assertEqual(ev["result_location"], loc,
                                 "result_location is mandatory lawful metadata")

    def test_no_behavioural_result_payload(self):
        def walk(obj, trail):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    self.assertIsNone(RESULT_PAYLOAD_KEY.match(k),
                                      "behavioural-result payload key %r at %s" % (k, trail))
                    walk(v, trail + "/" + k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    walk(v, "%s[%d]" % (trail, i))
        for p, d in _fixtures():
            with self.subTest(file=p.name):
                walk(d, p.name)


class RegistryConsistency(unittest.TestCase):
    def test_registry_hash_matches_strategy_bytes(self):
        registry = json.loads(_read(REGISTRY_PATH))
        entries = [e for e in registry["entries"] if e["id"] == "W4-D6-BEF"]
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["type"], "phase-record")
        raw = STRATEGY_PATH.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        self.assertEqual(entry["content_hash"],
                         "sha256:" + hashlib.sha256(raw).hexdigest(),
                         "registered hash must equal the governed strategy bytes")

    def test_fixture_files_remain_unregistered(self):
        registry = json.loads(_read(REGISTRY_PATH))
        for e in registry["entries"]:
            self.assertFalse(e["path"].startswith("fixtures/"),
                             "fixture data files carry no registry entries (W2-D4 rule)")


if __name__ == "__main__":
    unittest.main()
