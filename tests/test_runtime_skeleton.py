"""Tier 1 — W5-D2-M01 runtime-skeleton structural proofs.

Structure only, never behaviour: the runtime tree exists exactly as
authorised, owns no capability, and can reach no network facility.
"""

import ast
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))  # scaffolding import under any runner
RUNTIME = ROOT / "runtime"
# The authorised runtime tree — amended by record per milestone, on the
# top-level fence pattern. W5-D2-M01: the capability-empty skeleton.
# W5-D2-M02: grants.py (grant machinery, under its accepted opening
# brief and landing scope). W5-D2-M03: freshness.py (freshness runtime
# wiring, under its accepted opening brief and landing scope). Any
# further file is a new milestone's to authorise here, by record.
AUTHORISED_RUNTIME_FILES = ["__init__.py", "grants.py", "freshness.py"]
NETWORK_FACILITY_PREFIXES = (
    "socket", "ssl", "http", "urllib", "ftplib", "smtplib", "poplib",
    "imaplib", "xmlrpc", "requests", "aiohttp", "websockets", "grpc",
)


def runtime_modules():
    return sorted(p for p in RUNTIME.rglob("*.py"))


class RuntimeSkeleton(unittest.TestCase):
    def test_runtime_package_contains_exactly_the_authorised_files(self):
        files = sorted(p.relative_to(RUNTIME).as_posix()
                       for p in RUNTIME.rglob("*")
                       if p.is_file() and "__pycache__" not in p.parts)
        self.assertEqual(files, sorted(AUTHORISED_RUNTIME_FILES),
                         "runtime tree must match the record-authorised set")

    def test_skeleton_init_owns_no_capability(self):
        tree = ast.parse((RUNTIME / "__init__.py").read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            self.assertNotIsInstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                       ast.Import, ast.ImportFrom),
                "the skeleton stays capability-free; capability modules "
                "carry their own structural proofs")

    def test_runtime_tree_reaches_no_network_facility(self):
        for mod in runtime_modules():
            text = mod.read_text(encoding="utf-8")
            tree = ast.parse(text)
            for node in ast.walk(tree):
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names = [node.module]
                for name in names:
                    self.assertFalse(
                        name.split(".")[0] in NETWORK_FACILITY_PREFIXES,
                        f"network facility import in runtime tree: {name}")

    def test_residue_scaffolding_registers_no_boundary_operation_yet(self):
        from residue_scaffolding import REGISTERED_BOUNDARY_OPERATIONS
        self.assertEqual(REGISTERED_BOUNDARY_OPERATIONS, (),
                         "W5-D2-M01 registers no boundary operation; "
                         "registration arrives with the milestone that "
                         "lands the operation and its residue tests")
