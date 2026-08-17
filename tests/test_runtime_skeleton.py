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
# wiring, under its accepted opening brief and landing scope).
# W5-D2-M04: context.py (processing context, under the accepted
# combined-pipeline authorisation and its landing scope).
# W5-D2-M05: payload.py (payload assembly and equality, under the
# accepted combined-pipeline authorisation and its landing scope).
# W5-D2-M06: transmission.py (transmission and disclosure mechanics,
# under the accepted combined-pipeline authorisation and its landing
# scope). Any further file is a new milestone's to authorise here, by
# record.
AUTHORISED_RUNTIME_FILES = ["__init__.py", "grants.py",
                            "freshness.py", "context.py", "payload.py",
                            "transmission.py"]
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

    # Amended by record: W5-D2-M04 registers the processing-context
    # lifecycle with its full ADR 0035 residue tax. Any further
    # registration is a new milestone's to authorise here, by record.
    AUTHORISED_BOUNDARY_OPERATIONS = (
        ("processing-context-lifecycle", "W5-D2-M04"),
        ("payload-assembly", "W5-D2-M05"),
        ("transmission-crossing", "W5-D2-M06"),
    )

    def test_residue_scaffolding_registers_exactly_the_authorised(self):
        from residue_scaffolding import REGISTERED_BOUNDARY_OPERATIONS
        self.assertEqual(REGISTERED_BOUNDARY_OPERATIONS,
                         self.AUTHORISED_BOUNDARY_OPERATIONS,
                         "boundary operations must match the "
                         "record-authorised set")
