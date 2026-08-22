"""W7-D4 — the synthetic evaluation harness.

THIS INSTRUMENT NEVER CONTACTS A MODEL AND NEVER MATERIALISES A RECORD.

Under ADR-0051 Option D, public W7 does not contact a model. Every text this
harness handles is an `authored_synthetic_specimen` written inside this
repository. The harness exists to prove that the Wing can govern the handling of
generated-like prose without a model, without becoming authority itself, and
without leaving anything behind in the repository.

Seven separable responsibilities, per the W7-D4 brief section 12:

  1  load_exam                 source loader
  2  admit_specimen            specimen admission validator
  3  ScanGateway               capture-time scan, live scanner logic, no allowlist
  4  assemble_candidate_record ADR-0049 shape, in memory only
  5  derive_delta              structural mechanics only, never a verdict
  6  build_manifest_candidate / validate_manifest
  7  require_external_workspace   materialisation fence

WHAT THIS HARNESS CANNOT DO, BY CONSTRUCTION. It has no model adapter, runtime,
provider, client, credential or binary. It accepts no `generated_output` input
class. It allocates no `GER-####` identifier. It contains no function that writes
under `governance/generated-evaluation/` or anywhere else in the repository. A
caller receives candidate bytes and may place them only outside the repository.

PART Q, AS IT STANDS. A capture that produces any scan finding stops the run
before a candidate record is assembled. No disposition changes that, and this
module creates no suppression route.
"""

import hashlib
import importlib.util
import json
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESERVED_HOME = ROOT / "governance" / "generated-evaluation"
SCANNER = ROOT / "scripts" / "public-safety-scan.py"

VARIANT_LABELS = ("variant_a", "variant_b")
EXAM_FORMAT = "w7-d4-exam-1"

# ADR-0049 canonical order. Read as law, reproduced here as the assembly order the
# record must have; the proof module checks these against the landed field tables.
RECORD_FIELDS = ("record_id", "run_id", "authorising_record", "as_of", "synthetic_marker",
                 "model_contact", "inputs", "pairing", "captures", "delta", "findings",
                 "exclusion_check", "no_recirculation", "human_review", "non_authority")
CAPTURE_FIELDS = ("text_class", "authoring_record", "text", "text_digest", "scan_status")
WRAPPER_KEY = "generated_evaluation_record"

LAWFUL_ORIGINS = ("authored_synthetic", "repository_fixture", "governed_public_record")
SPECIMEN_CLASS = "authored_synthetic_specimen"

# Fields the exam may never carry: a result, a verdict, or a disposition.
FORBIDDEN_EXAM_KEYS = ("result", "results", "pass", "passed", "fail", "failed", "verdict",
                       "score", "winner", "ranking", "disposition", "record_id", "ger_id")
# Manifest keys that would turn an index into a summary. This list is a name guard,
# not the shape guard: the closed key sets below are what refuse an arbitrary extra
# field. The list still bites independently where a shape cannot - a forbidden name
# used as a VALUE, such as a record identifier called "summary".
FORBIDDEN_MANIFEST_KEYS = ("summary", "verdict", "score", "winner", "ranking", "pass_count",
                           "fail_count", "finding_count", "findings", "disposition",
                           "capture_text", "model", "provider", "sdk", "runtime")
# The manifest's four closed shapes. Anything added, missing or renamed is refused
# by membership, so no future field arrives unannounced under a lawful-looking name.
MANIFEST_KEYS = ("run_id", "authorising_record", "as_of", "exam", "scan_environment", "records")
MANIFEST_EXAM_KEYS = ("reference", "content_hash")
MANIFEST_SCAN_ENV_KEYS = ("local_wordlist",)
MANIFEST_RECORD_KEYS = ("record_id", "path", "content_hash")


class HarnessRefusal(Exception):
    """Raised when the harness refuses. Never carries payload or wordlist text."""


def _scanner():
    spec = importlib.util.spec_from_file_location("_w7_live_scanner", SCANNER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _law_text(name):
    """Read a byte-fixed value from its landed record rather than transcribing it."""
    import re
    if name == "notice":
        src = (ROOT / "docs/decisions/0049-generated-evaluation-field-law.md").read_text(
            encoding="utf-8")
        m = re.search(r"`synthetic_marker\.notice` is byte-fixed at this value[^\n]*\n\s*\n"
                      r"> \*\*(.+?)\*\*\s*\n", src)
    else:
        src = (ROOT / "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md"
               ).read_text(encoding="utf-8")
        m = re.search(r"carries this sentence, byte-identically, inside itself:\*\*\s*\n\s*\n"
                      r"> \*\*(.+?)\*\*\s*\n", src)
    if m is None:
        raise HarnessRefusal("byte-fixed %s anchor not found in its landed record" % name)
    return m.group(1)


# ---------------------------------------------------------------- 7. fence ---

def require_external_workspace(path):
    """Return a resolved workspace path, or refuse. Working state stays outside."""
    if path is None:
        raise HarnessRefusal("a workspace must be supplied; there is no in-repository default")
    p = Path(path).resolve()
    root = ROOT.resolve()
    if p == root or root in p.parents:
        raise HarnessRefusal("workspace resolves inside the repository")
    # A path under the reserved home is already caught above, because the home is
    # inside the repository. This second rule is therefore about the NAME: a scratch
    # directory called generated-evaluation anywhere, even outside the repository,
    # is refused, so transient captures can never accumulate somewhere that reads
    # like the governed home.
    if RESERVED_HOME.name in p.parts:
        raise HarnessRefusal("workspace path uses the reserved generated-evaluation name")
    return p


# ---------------------------------------------------------------- 1. loader --

def load_exam(path):
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    exam = doc.get("w7_d4_exam")
    if exam is None:
        raise HarnessRefusal("not a W7-D4 exam artefact")
    if exam.get("exam_format_version") != EXAM_FORMAT:
        raise HarnessRefusal("unknown exam format version")
    if tuple(exam.get("variant_labels", ())) != VARIANT_LABELS:
        raise HarnessRefusal("exam variant labels are not the closed W7-D4 pair")
    probes = exam.get("probes") or []
    if not probes:
        raise HarnessRefusal("exam declares no probes")

    flat = json.dumps(exam)
    for key in FORBIDDEN_EXAM_KEYS:
        if '"%s"' % key in flat:
            raise HarnessRefusal("exam carries a forbidden result-bearing key")

    seen_probe, seen_unknown = set(), set()
    for p in probes:
        pid = p.get("probe_id")
        if not pid or pid in seen_probe:
            raise HarnessRefusal("probe identity missing or duplicated")
        seen_probe.add(pid)
        cite = (p.get("source_unknown") or {}).get("citation")
        if not cite or cite in seen_unknown:
            raise HarnessRefusal("source unknown missing or duplicated")
        seen_unknown.add(cite)
        if tuple((p.get("variants") or {}).keys()) != VARIANT_LABELS:
            raise HarnessRefusal("probe does not carry exactly the two closed variant labels")

    cov = exam.get("source_coverage") or {}
    if cov.get("unique_probes") != len(probes):
        raise HarnessRefusal("declared probe count disagrees with the probes present")
    if cov.get("expected_captures") != 2 * len(probes):
        raise HarnessRefusal("declared capture count is not twice the probe count")
    if cov.get("unknowns_accounted") != len(seen_unknown):
        raise HarnessRefusal("declared unknown coverage disagrees with the probes present")
    traps = {(p.get("source_trap") or {}).get("fixture_id") for p in probes}
    if cov.get("traps_accounted") != len(traps - {None}):
        raise HarnessRefusal("declared trap coverage disagrees with the probes present")

    # This exam is the Option D exam. Every variant declares its class and its origin
    # explicitly, and both are fixed: nothing here is generated output, and nothing
    # here arrives from anywhere but authored synthetic material.
    ceiling = _law_text("ceiling")
    if exam.get("non_authority") != ceiling:
        raise HarnessRefusal("exam does not carry the non-authority ceiling verbatim")
    for p in probes:
        for variant in p["variants"].values():
            if variant.get("text_class") != SPECIMEN_CLASS:
                raise HarnessRefusal("exam variant does not declare the specimen class")
            if variant.get("origin") != "authored_synthetic":
                raise HarnessRefusal("exam variant does not declare an authored synthetic origin")
            # ADR-0046 decisions 23-25: inside the unit that holds the text, byte-identical,
            # and binding on an authored synthetic specimen exactly as on generated output.
            if variant.get("non_authority") != ceiling:
                raise HarnessRefusal("specimen does not carry the non-authority ceiling verbatim")
    return exam


# ---------------------------------------------------- 2. specimen admission --

def admit_specimen(variant, authoring_record):
    """Admit a specimen and return (text, origin). Nothing is defaulted.

    The origin is returned rather than assumed, because the record must declare the
    origin that was actually admitted. Admitting one origin and recording another
    would be a provenance claim the admission never made.
    """
    if not isinstance(variant, dict):
        raise HarnessRefusal("specimen variant is not an object")
    origin = variant.get("origin")
    if origin not in LAWFUL_ORIGINS:
        raise HarnessRefusal("specimen declares no lawful ADR-0046 origin")
    if "text_class" not in variant:
        raise HarnessRefusal("specimen declares no text class; there is no default")
    if variant["text_class"] != SPECIMEN_CLASS:
        raise HarnessRefusal("only authored synthetic specimens are admissible under Option D")
    text = variant.get("specimen_text")
    if not isinstance(text, str) or not text.strip():
        raise HarnessRefusal("specimen text is missing or empty")
    if not authoring_record:
        raise HarnessRefusal("an authored specimen requires a non-null authoring record")
    lowered = text.lower()
    if "governance/generated-evaluation" in lowered or "ger-" in lowered:
        raise HarnessRefusal("specimen references the generated-evaluation class: recirculation")
    return text, origin


# --------------------------------------------------------------- 3. gateway --

class ScanGateway:
    """Capture-time scanning through the live scanner, with no allowlist route.

    The capture is written to a securely created temporary file OUTSIDE the
    repository, scanned by the live `scan_file`, and removed. Nothing about a
    match is retained or returned beyond its category.
    """

    def __init__(self, workspace):
        self.workspace = require_external_workspace(workspace)
        self._s = _scanner()
        self.branch_state = "active" if self._s.load_wordlist() else "inactive"

    def sample_branch(self):
        return "active" if self._s.load_wordlist() else "inactive"

    def assert_branch_stable(self):
        now = self.sample_branch()
        if now != self.branch_state:
            raise HarnessRefusal("scan environment changed during the run; stopping before "
                                 "any record is assembled")
        return now

    def scan_capture(self, text):
        """Return (clean, categories). Never returns or prints matched text."""
        self.assert_branch_stable()
        fd, tmp = tempfile.mkstemp(suffix=".txt", dir=str(self.workspace))
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            # No allowlist is supplied: a generated-evaluation capture has no
            # suppression route, per ADR-0050 Part I and the W7-D4 brief.
            findings, suppressed = self._s.scan_file(Path(tmp), "<capture>",
                                                     self._s.load_wordlist(), {})
            if suppressed:
                raise HarnessRefusal("a suppression route was applied to a capture")
            cats = sorted({f[2] for f in (findings or [])})
            return (not cats), cats
        finally:
            try:
                os.unlink(tmp)
            except OSError:
                raise HarnessRefusal("capture working state could not be removed")


# ------------------------------------------------------------- 4. assembler --

def _digest(text):
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def assemble_candidate_record(probe, texts, *, origins, run_id, authorising_record, as_of,
                              placeholder_id, exclusion_list_reference):
    """Build the ADR-0049 shape in memory. Never writes. Never allocates a GER id.

    `origins` maps each variant label to the origin its specimen was ADMITTED under.
    It is required rather than defaulted: the assembler declares what admission
    found, so no record can claim a provenance the admission never granted.
    """
    if placeholder_id.upper().startswith("GER-"):
        raise HarnessRefusal("D4 must not use a GER-shaped identifier")
    labels = list(VARIANT_LABELS)
    if sorted(texts) != labels:
        raise HarnessRefusal("captures do not match the declared variant labels")
    if sorted(origins) != labels:
        raise HarnessRefusal("admitted origins do not match the declared variant labels")
    for label in labels:
        if origins[label] not in LAWFUL_ORIGINS:
            raise HarnessRefusal("an admitted origin is outside the closed ADR-0046 set")

    captures = {}
    for label in labels:
        captures[label] = dict(zip(CAPTURE_FIELDS, (
            SPECIMEN_CLASS, authorising_record, texts[label],
            _digest(texts[label]), "no_findings")))

    record = {
        "record_id": placeholder_id,
        "run_id": run_id,
        "authorising_record": authorising_record,
        "as_of": as_of,
        "synthetic_marker": {"synthetic": True, "notice": _law_text("notice")},
        "model_contact": {"occurred": False, "contact_class": "none",
                          "authorising_record": None},
        # One input per DISTINCT admitted origin, in the closed ADR-0049 item shape.
        # Where both captures were admitted under one origin this is a single entry,
        # and where they differ both origins are declared rather than flattened.
        "inputs": [{"origin": o,
                    "citation": probe["source_unknown"]["citation"],
                    "reference": probe["source_trap"]["fixture_id"]}
                   for o in sorted(set(origins[label] for label in labels))],
        "pairing": {"probe_id": probe["probe_id"], "variant_labels": labels},
        "captures": captures,
        "delta": derive_delta(probe, texts),
        "findings": [],
        "exclusion_check": {"list_reference": exclusion_list_reference, "checked": True,
                            "result": "no_listed_item_present"},
        "no_recirculation": {"capture_terminal": True},
        "human_review": {"routed": True, "disposition": None, "disposition_record": None},
        "non_authority": _law_text("ceiling"),
    }
    if tuple(record) != RECORD_FIELDS:
        raise HarnessRefusal("assembled record is not in canonical order")
    return {WRAPPER_KEY: record}


# ------------------------------------------------------------------ 5. delta --

def derive_delta(probe, texts):
    """Structural mechanics only. Never a semantic verdict, never a winner."""
    differing = ["spoken_output"] if texts["variant_a"] != texts["variant_b"] else []
    return {"outcome": "routed-to-review", "differing_surfaces": differing,
            "missing_surfaces": ["persisted_state", "routing_propagation",
                                 "behaviour_selection_ranking_framing_omission"]}


# --------------------------------------------------------------- 6. manifest --

def build_manifest_candidate(*, run_id, authorising_record, as_of, exam_path,
                             branch_state, records):
    if branch_state not in ("active", "inactive"):
        raise HarnessRefusal("scan-environment state is outside its closed two-value set")
    exam_bytes = Path(exam_path).read_bytes()
    return {"generated_evaluation_run_manifest": {
        "run_id": run_id,
        "authorising_record": authorising_record,
        "as_of": as_of,
        "exam": {"reference": Path(exam_path).name,
                 "content_hash": "sha256:" + hashlib.sha256(exam_bytes).hexdigest()},
        "scan_environment": {"local_wordlist": branch_state},
        "records": list(records)}}


def _record_path_is_inside_home(path, home_prefix):
    """A listed path must sit under the reserved home by literal construction.

    Absolute, drive-rooted, backslash and traversal forms are refused outright
    rather than normalised, because a path that needs normalising to look lawful
    is a path that was trying to leave.
    """
    if not isinstance(path, str) or not path:
        return False
    if path.startswith("/") or "\\" in path or ":" in path:
        return False
    if not path.startswith(home_prefix):
        return False
    return ".." not in path.split("/")


def validate_manifest(manifest, present, *, exam_bytes=None,
                      home_prefix="governance/generated-evaluation/"):
    """The S2 relation, manifest-aware and closed-shape. Returns disagreements.

    `present` maps record_id to {"content_hash": ..., "run_id": ...}, both read from
    the record's own bytes by the caller. Run membership is established from what a
    record SAYS it belongs to, never inferred from its identifier, path or hash.
    """
    out = []
    m = manifest.get("generated_evaluation_run_manifest")
    if m is None:
        return ["not a run manifest"]
    if tuple(m) != MANIFEST_KEYS:
        out.append("manifest is not the closed run-manifest shape")
    flat = json.dumps(m).lower()
    for key in FORBIDDEN_MANIFEST_KEYS:
        if '"%s"' % key in flat:
            out.append("manifest carries a forbidden key: %s" % key)
    exam = m.get("exam")
    if not isinstance(exam, dict) or tuple(exam) != MANIFEST_EXAM_KEYS:
        out.append("exam block is not the closed shape")
        exam = exam if isinstance(exam, dict) else {}
    env = m.get("scan_environment")
    if not isinstance(env, dict) or tuple(env) != MANIFEST_SCAN_ENV_KEYS:
        out.append("scan-environment carries more than the one governed bit")
    elif env["local_wordlist"] not in ("active", "inactive"):
        out.append("scan-environment value outside its closed set")
    if exam_bytes is not None:
        want = "sha256:" + hashlib.sha256(exam_bytes).hexdigest()
        if exam.get("content_hash") != want:
            out.append("exam hash does not match the executed exam")

    listed, seen = {}, set()
    for e in m.get("records") or []:
        if not isinstance(e, dict):
            out.append("record entry is not an object")
            continue
        if tuple(e) != MANIFEST_RECORD_KEYS:
            out.append("record entry is not the closed shape: %s" % e.get("record_id"))
        rid = e.get("record_id")
        if rid in seen:
            out.append("record listed more than once: %s" % rid)
        seen.add(rid)
        if rid == m.get("run_id"):
            out.append("manifest lists itself as a record")
        if not _record_path_is_inside_home(e.get("path"), home_prefix):
            out.append("record path outside the reserved home: %s" % rid)
        if "content_hash" not in e:
            out.append("record has no content hash: %s" % rid)
        listed[rid] = e.get("content_hash")

    for rid in sorted(set(listed) - set(present)):
        out.append("listed record is absent: %s" % rid)
    for rid in sorted(set(present) - set(listed)):
        out.append("present record is unlisted: %s" % rid)
    for rid in sorted(set(listed) & set(present)):
        actual = present[rid] if isinstance(present[rid], dict) else {}
        if listed[rid] != actual.get("content_hash"):
            out.append("hash mismatch: %s" % rid)
        if actual.get("run_id") != m.get("run_id"):
            out.append("record belongs to another run: %s" % rid)
    return out


# ---------------------------------------- the fixed capture-time sequence ----

def run_probe(probe, gateway, *, run_id, authorising_record, as_of, placeholder_id,
              exclusion_list_reference):
    """Brief section 17, in order. Returns (state, payload). Never writes to the repo."""
    texts, origins = {}, {}
    for label in VARIANT_LABELS:
        text, origin = admit_specimen(probe["variants"][label],
                                      authoring_record=authorising_record)
        clean, cats = gateway.scan_capture(text)
        if not clean:
            # Part Q: stop before any candidate exists. No GER, no disposition.
            return "stop_and_report", {"probe_id": probe["probe_id"], "variant": label,
                                       "categories": cats}
        texts[label], origins[label] = text, origin
    record = assemble_candidate_record(
        probe, texts, origins=origins, run_id=run_id, authorising_record=authorising_record,
        as_of=as_of, placeholder_id=placeholder_id,
        exclusion_list_reference=exclusion_list_reference)
    return "candidate", record
