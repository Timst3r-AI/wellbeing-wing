"""Tier 1 — repo-state assertions.

The subject of these tests is the repository itself: registry
consistency, directory fences, the public-safety scan, and fixture
discipline. They run against the real repo, now, with no
implementation required.
"""

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "governance" / "registry.json"
SCOPE_DIRS = [
    "docs/constitution", "docs/decisions", "docs/architecture",
    "docs/phases", "docs/governance",
]
REGISTRY_ARTIFACT_IDS = {"REGISTRY-JSON", "REGISTRY-MD"}
EXCLUSION_REASON = "registry artifact — self-reference exclusion"
# Amended under the W3-D2 milestone-1 Tier F authorisation: admits
# exactly the engine directory and the single pinned manifest, nothing
# else. Any further product directory or dependency is a new named
# fence-crossing requiring its own record-backed amendment here.
ALLOWED_TOP_LEVEL = {"docs", "governance", "tests", "fixtures", "scripts",
                     "engine",
                     "README.md", ".gitignore", ".git",
                     "requirements.txt",
                     ".public-safety.local.txt"}
APPROVED_MANIFEST = "requirements.txt"
APPROVED_MANIFEST_LINES = {"PyNaCl==1.6.2", "cffi==2.0.0", "pycparser==3.0"}
FORBIDDEN_MANIFESTS = {
    "package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "Pipfile", "Pipfile.lock", "pyproject.toml",
    "poetry.lock", "Cargo.toml", "go.mod", "Gemfile",
}
FORBIDDEN_TOP_DIRS = {"src", "app", "ui", ".github", ".circleci", "node_modules"}
NOTICE = ("SYNTHETIC fixture authored for governance testing. Corresponds "
          "to no real person. Values are grammar placeholders, not medical content.")


def lf_hash(path):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    return "sha256:" + hashlib.sha256(
        raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


class RegistryConsistency(unittest.TestCase):
    def setUp(self):
        self.doc = load_registry()
        self.entries = self.doc["entries"]
        self.by_path = {e["path"]: e for e in self.entries}
        self.ids = {e["id"] for e in self.entries}

    def test_every_in_scope_governance_file_has_an_entry(self):
        for d in SCOPE_DIRS:
            for f in sorted((ROOT / d).glob("*.md")):
                if f.name == "README.md":
                    continue  # narrative index surfaces, not governance entries
                rel = f.relative_to(ROOT).as_posix()
                self.assertIn(rel, self.by_path,
                              f"in-scope governance file has no registry entry: {rel}")

    def test_every_registry_path_resolves(self):
        for e in self.entries:
            self.assertTrue((ROOT / e["path"]).exists(),
                            f"registry path does not resolve: {e['path']}")

    def test_statuses_match_source_headers(self):
        for e in self.entries:
            if e["id"] in REGISTRY_ARTIFACT_IDS or e["status"] == "template":
                continue
            head = "\n".join(
                (ROOT / e["path"]).read_text(encoding="utf-8").splitlines()[:8])
            if e["status"] == "accepted":
                self.assertIn("Accepted by human reviewer", head,
                              f"{e['id']}: registry says accepted but header does not")

    def test_hashes_recompute_with_lf_normalisation(self):
        for e in self.entries:
            if e["content_hash"] is None:
                continue
            self.assertEqual(e["content_hash"], lf_hash(ROOT / e["path"]),
                             f"{e['id']}: content hash mismatch")

    def test_null_hashes_only_on_registry_artifacts_with_reason(self):
        for e in self.entries:
            if e["content_hash"] is None:
                self.assertIn(e["id"], REGISTRY_ARTIFACT_IDS,
                              f"{e['id']}: null hash outside registry artifacts")
                self.assertEqual(e["hash_exclusion_reason"], EXCLUSION_REASON)
            else:
                self.assertTrue(re.fullmatch(r"sha256:[0-9a-f]{64}", e["content_hash"]),
                                f"{e['id']}: bad hash format")

    def test_reference_fields_resolve(self):
        for e in self.entries:
            for field in ("depends_on", "governs"):
                for ref in e[field]:
                    self.assertIn(ref, self.ids,
                                  f"{e['id']}.{field}: dangling reference {ref}")


class DirectoryFence(unittest.TestCase):
    def test_top_level_contains_only_authorised_entries(self):
        for item in ROOT.iterdir():
            self.assertIn(item.name, ALLOWED_TOP_LEVEL,
                          f"unauthorised top-level entry: {item.name}")

    def test_no_forbidden_top_level_directories(self):
        for name in FORBIDDEN_TOP_DIRS:
            self.assertFalse((ROOT / name).exists(), f"forbidden directory exists: {name}")

    def test_no_dependency_manifests_beyond_the_approved_one(self):
        for f in ROOT.rglob("*"):
            if ".git" in f.parts:
                continue
            self.assertNotIn(f.name, FORBIDDEN_MANIFESTS,
                             f"dependency manifest present: {f.relative_to(ROOT)}")
            if f.name == APPROVED_MANIFEST:
                self.assertEqual(f.parent, ROOT,
                                 f"manifest outside root: {f.relative_to(ROOT)}")

    def test_approved_manifest_contains_exactly_the_authorised_lines(self):
        manifest = ROOT / APPROVED_MANIFEST
        self.assertTrue(manifest.exists(), "approved manifest missing")
        lines = {ln.strip() for ln in manifest.read_text(encoding="utf-8").splitlines()
                 if ln.strip() and not ln.strip().startswith("#")}
        self.assertEqual(lines, APPROVED_MANIFEST_LINES,
                         "manifest deviates from the authorised pinned set - "
                         "any change is a named fence-crossing")

    def test_no_test_files_outside_the_test_tree(self):
        for f in ROOT.rglob("test_*.py"):
            if ".git" in f.parts:
                continue
            self.assertEqual(f.parts[len(ROOT.parts)], "tests",
                             f"test file outside tests/: {f.relative_to(ROOT)}")


class PublicSafetyScan(unittest.TestCase):
    def test_scan_normal_mode_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "public-safety-scan.py")],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0,
                         f"public-safety scan failed:\n{result.stdout}")


class FixtureDiscipline(unittest.TestCase):
    def setUp(self):
        self.files = sorted((ROOT / "fixtures").glob("*"))

    def test_fixture_files_exist(self):
        self.assertTrue(self.files, "fixtures directory is empty")

    def test_every_fixture_is_marked_synthetic_and_valid(self):
        for f in self.files:
            self.assertTrue(f.name.startswith("SYNTHETIC-"),
                            f"fixture not marked in filename: {f.name}")
            data = json.loads(f.read_text(encoding="utf-8"))
            marker = data["synthetic_marker"]
            self.assertIs(marker["synthetic"], True, f.name)
            self.assertEqual(marker["notice"], NOTICE, f.name)
            self.assertTrue(marker["exercises"], f"{f.name}: empty exercises map")
            self.assertTrue(marker["persona"].startswith("Persona-"), f.name)


if __name__ == "__main__":
    unittest.main()
