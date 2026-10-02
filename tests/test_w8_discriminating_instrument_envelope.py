"""W8-D2-B — envelope structural proofs (ADR-0055 Part M, V1–V12).

The envelope law is real: ADR-0055 fixes the reviewer-visible case shape, the
withheld authoring-record shape, the canonical-byte law, the neutral identity
and ordering law, the nonce and commitment mechanics, the manifest's
cross-artefact binding and the custody contract, before any case exists. This
module implements those mechanics as executable law and proves them with
planted-mutant controls. Custody verification operates on exact retained
bytes, hashed directly before any parse or canonical reserialisation, so a
semantics-preserving byte mutation is a stop and repair by reserialisation is
mechanically impossible here. Before custody begins, a pre-freeze bundle
binding proves the whole composition atomically - validated visible case,
exact canonical visible bytes, validated hidden record, exact canonical
hidden bytes at freeze time only, one shared identity, and manifest-row
digests over those exact bytes - so no artefact can enter custody bound to
the wrong case or keyed by an independently trusted identifier.

THIS MODULE CONTAINS NO W8 CASE. The two SENTINEL variant strings below are
mechanics fixtures only — deliberately meaningless, clearly labelled, never
written to any file, never a specimen, never authored under Parts B–D of
ADR-0054, and carrying no governed meaning. No authoring record exists, no
nonce is generated (a labelled all-zero sentinel stands in for shape checks
only), and no real commitment is computed over any real record.

WHAT GREEN DOES NOT MEAN. A green run proves envelope mechanics and doctrine
carriage only. It NEVER establishes: any case's authored class or human
disposition — no proof here decides, predicts or hints at either; that any
authoring declaration is semantically true; that any future case is
well-constructed; that any case, corpus, authoring record, nonce, commitment,
manifest instance, calibration, disposition or reveal exists or is lawful;
that any model was contacted; that ADR-0047 precondition 3 moved; that any
W7 record changed; or that D2-C is open.
"""

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADR55 = ROOT / "docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md"
ADR54 = ROOT / "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"


def _lf(b):
    return b.replace(b"\r\n", b"\n")


def _text(p):
    return _lf(Path(p).read_bytes()).decode("utf-8")


# ---------------------------------------------------------------- mechanics
REVIEW_SCHEMA = "w8-review-case-v1"
AUTHORING_SCHEMA = "w8-authoring-record-v1"
REVIEW_FIELDS = frozenset(
    {"schema", "case_id", "admissible_source_evidence",
     "structural_provenance_support"})
ASE_FIELDS = frozenset({"variant_a", "variant_b"})
SPS_FIELDS = frozenset({"synthetic", "source_evidence_sha256", "governed_by"})
GOVERNED_BY = ["ADR-0054", "ADR-0055"]
FORBIDDEN_REVIEW_FIELDS = frozenset(
    {"title", "authored_class", "intended_disposition", "intended_answer",
     "governed_property", "property_construction", "rationale",
     "authoring_rationale", "expected_token", "surface_feature",
     "summary", "diff", "highlight", "timestamp", "authoring_sequence"})
AUTHORING_FIELDS = frozenset(
    {"schema", "case_id", "authored_class", "intended_disposition",
     "property_construction", "surface_features_varied",
     "inconclusive_conditions", "authoring_checks", "authoring_rationale",
     "reviewer_visible_sha256", "commitment_nonce"})
CLASSES = frozenset({"A", "B", "C"})
TOKENS = frozenset({"governance_delta_present", "no_governance_delta",
                    "review_inconclusive"})
CLASS_TOKEN = {"A": "governance_delta_present", "B": "no_governance_delta",
               "C": "review_inconclusive"}
PROPERTIES = ("authority", "provenance", "permission", "persistence",
              "memory treatment", "decision status", "boundary crossing",
              "attribution", "review state")
STATES = frozenset({"same", "different", "underdetermined", "not_engaged"})
INCONCLUSIVE_LABELS = frozenset(
    {"insufficient_source_evidence",
     "multiple_material_governed_interpretations",
     "unresolved_conflict_within_source_evidence",
     "requires_unavailable_external_authority"})
SURFACE_FEATURES = frozenset(
    {"tone", "warmth", "confidence", "verbosity", "phrasing", "formatting",
     "politeness", "explanatory depth"})
CLASS_CHECKS = {
    "A": frozenset({"delta_property_identified", "delta_evidence_located",
                    "delta_reachable_from_visible_evidence_checked"}),
    "B": frozenset({"equivalence_all_nine_checked",
                    "surface_variation_recorded",
                    "non_delta_reachable_from_visible_evidence_checked"}),
    "C": frozenset({"engaged_property_named", "part_d_condition_identified",
                    "substantive_answer_unavailable_recorded"}),
}
ALL_CHECKS = frozenset().union(*CLASS_CHECKS.values())
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CASE_ID_RE = re.compile(r"^W8-C-[0-9a-f]{64}$")
SHA_FIELD_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
MANIFEST_ROW_FIELDS = frozenset(
    {"case_id", "reviewer_visible_sha256", "authoring_commitment_sha256"})

# Mechanics fixtures only — NOT a case, NOT authored, NOT governed content.
SENTINEL_TEXT_1 = "mechanics sentinel text one — not a case, carries no governed meaning"
SENTINEL_TEXT_2 = "mechanics sentinel text two — not a case, carries no governed meaning"
SENTINEL_TEXT_3 = "mechanics sentinel text three — not a case, carries no governed meaning"
SENTINEL_NONCE = "0" * 64  # deterministic mechanics-only sentinel, never a generated nonce


def canonical_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n"
            ).encode("utf-8")


def sha256_bytes(raw):
    """The custody digest: exact bytes in, digest out — no parse, ever."""
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def orient(text_1, text_2):
    d1 = hashlib.sha256(text_1.encode("utf-8")).hexdigest()
    d2 = hashlib.sha256(text_2.encode("utf-8")).hexdigest()
    if d1 == d2:
        raise ValueError("identical byte sequences are invalid")
    return (text_1, text_2) if d1 < d2 else (text_2, text_1)


def evidence_digest(variant_a, variant_b):
    return hashlib.sha256(canonical_bytes(
        {"variant_a": variant_a, "variant_b": variant_b})).hexdigest()


def case_identity(variant_a, variant_b):
    return "W8-C-" + evidence_digest(variant_a, variant_b)


def build_review_case(text_1, text_2):
    variant_a, variant_b = orient(text_1, text_2)
    return {
        "schema": REVIEW_SCHEMA,
        "case_id": case_identity(variant_a, variant_b),
        "admissible_source_evidence": {"variant_a": variant_a,
                                       "variant_b": variant_b},
        "structural_provenance_support": {
            "synthetic": True,
            "source_evidence_sha256": evidence_digest(variant_a, variant_b),
            "governed_by": list(GOVERNED_BY),
        },
    }


def review_case_violations(obj):
    v = []
    if set(obj) != REVIEW_FIELDS:
        v.append("top-level shape: %s" % sorted(set(obj) ^ REVIEW_FIELDS))
    leaked = set(obj) & FORBIDDEN_REVIEW_FIELDS
    if leaked:
        v.append("forbidden reviewer-visible field: %s" % sorted(leaked))
    if obj.get("schema") != REVIEW_SCHEMA:
        v.append("schema")
    if not CASE_ID_RE.match(obj.get("case_id", "")):
        v.append("case_id shape")
    ase = obj.get("admissible_source_evidence", {})
    if set(ase) != ASE_FIELDS:
        v.append("admissible_source_evidence shape")
    else:
        a, b = ase["variant_a"], ase["variant_b"]
        if not (isinstance(a, str) and a and isinstance(b, str) and b):
            v.append("variants must be whole non-empty strings")
        elif a == b:
            v.append("variants byte-identical")
        else:
            da = hashlib.sha256(a.encode("utf-8")).hexdigest()
            db = hashlib.sha256(b.encode("utf-8")).hexdigest()
            if not da < db:
                v.append("orientation: variant_a digest must sort first")
            expected = "W8-C-" + evidence_digest(a, b)
            if obj.get("case_id") != expected:
                v.append("case_id does not derive from evidence")
    sps = obj.get("structural_provenance_support", {})
    if set(sps) != SPS_FIELDS:
        v.append("structural_provenance_support shape")
    else:
        if sps["synthetic"] is not True:
            v.append("synthetic must be true")
        if sps["governed_by"] != GOVERNED_BY:
            v.append("governed_by")
        if set(ase) == ASE_FIELDS and sps["source_evidence_sha256"] != \
                evidence_digest(ase["variant_a"], ase["variant_b"]):
            v.append("source_evidence_sha256 mismatch")
    return v


def _unique_list_of(value, allowed, label):
    v = []
    if not isinstance(value, list):
        return ["%s must be a list" % label]
    if len(value) != len(set(value)):
        v.append("%s entries must be unique" % label)
    if not set(value) <= allowed:
        v.append("%s vocabulary" % label)
    return v


def authoring_record_violations(rec):
    v = []
    if set(rec) != AUTHORING_FIELDS:
        v.append("record shape: %s" % sorted(set(rec) ^ AUTHORING_FIELDS))
        return v
    if rec["schema"] != AUTHORING_SCHEMA:
        v.append("schema")
    if not CASE_ID_RE.match(rec.get("case_id", "")):
        v.append("case_id shape")
    cls = rec["authored_class"]
    if cls not in CLASSES:
        v.append("authored_class")
        return v
    if rec["intended_disposition"] not in TOKENS:
        v.append("intended_disposition token")
    elif rec["intended_disposition"] != CLASS_TOKEN[cls]:
        v.append("class-to-token binding")
    pc = rec["property_construction"]
    if tuple(sorted(pc)) != tuple(sorted(PROPERTIES)):
        v.append("property map keys: %s"
                 % sorted(set(pc) ^ set(PROPERTIES)))
    else:
        if not all(s in STATES for s in pc.values()):
            v.append("property state vocabulary")
        diff = [p for p, s in pc.items() if s == "different"]
        und = [p for p, s in pc.items() if s == "underdetermined"]
        if cls == "A" and (not diff or und):
            v.append("class A requires >=1 different and no underdetermined")
        if cls == "B" and any(s not in ("same", "not_engaged")
                              for s in pc.values()):
            v.append("class B permits only same or not_engaged")
        if cls == "C" and (not und or diff):
            v.append("class C requires >=1 underdetermined and no "
                     "established different")
    v += _unique_list_of(rec["surface_features_varied"], SURFACE_FEATURES,
                         "surface_features_varied")
    if cls == "B" and not rec["surface_features_varied"]:
        v.append("class B requires >=1 materially varied surface feature")
    v += _unique_list_of(rec["inconclusive_conditions"], INCONCLUSIVE_LABELS,
                         "inconclusive_conditions")
    labels = set(rec["inconclusive_conditions"]) \
        if isinstance(rec["inconclusive_conditions"], list) else set()
    if cls == "C" and not labels:
        v.append("class C requires >=1 inconclusive condition")
    if cls in ("A", "B") and labels:
        v.append("classes A and B require no inconclusive condition")
    v += _unique_list_of(rec["authoring_checks"], ALL_CHECKS,
                         "authoring_checks")
    if isinstance(rec["authoring_checks"], list) and \
            set(rec["authoring_checks"]) <= ALL_CHECKS and \
            set(rec["authoring_checks"]) != CLASS_CHECKS[cls]:
        v.append("authoring_checks must be exactly the class-%s set" % cls)
    if not (isinstance(rec["authoring_rationale"], str)
            and rec["authoring_rationale"].strip()):
        v.append("authoring_rationale must be a whole non-empty string")
    if not (isinstance(rec["reviewer_visible_sha256"], str)
            and SHA_FIELD_RE.match(rec["reviewer_visible_sha256"])):
        v.append("reviewer_visible_sha256 format")
    if not (isinstance(rec["commitment_nonce"], str)
            and HEX64.match(rec["commitment_nonce"])):
        v.append("commitment_nonce shape")
    return v


def cross_binding_violations(visible_case, visible_bytes, hidden_record):
    """The record seals exactly this case: byte-equal identity and the
    digest of the exact final reviewer-visible bytes."""
    v = []
    if hidden_record.get("case_id") != visible_case.get("case_id"):
        v.append("hidden case_id does not byte-equal the visible identity")
    if hidden_record.get("reviewer_visible_sha256") != \
            sha256_bytes(visible_bytes):
        v.append("reviewer_visible_sha256 does not equal the digest of the "
                 "exact final reviewer-visible bytes")
    return v


def bundle_binding_violations(visible_case, visible_bytes, hidden_record,
                              hidden_bytes, manifest_row, external_key=None):
    """Pre-freeze compositional closure, atomic, BEFORE retained bytes enter
    custody. Freeze time is the only moment hidden bytes are lawfully derived
    from the parsed record; once frozen, custody and reveal are raw retained
    bytes only (V11), with no parse and no reserialisation anywhere."""
    v = []
    v += ["visible: " + x for x in review_case_violations(visible_case)]
    if visible_bytes != canonical_bytes(visible_case):
        v.append("visible_bytes are not the canonical bytes of this visible "
                 "case")
    v += ["hidden: " + x for x in authoring_record_violations(hidden_record)]
    if hidden_bytes != canonical_bytes(hidden_record):
        v.append("hidden_bytes are not the canonical bytes of this hidden "
                 "record at freeze time")
    cid = visible_case.get("case_id")
    if hidden_record.get("case_id") != cid:
        v.append("hidden case_id does not byte-equal the visible identity")
    if hidden_record.get("reviewer_visible_sha256") != sha256_bytes(
            visible_bytes):
        v.append("hidden reviewer_visible_sha256 does not equal the exact "
                 "visible bytes' digest")
    if manifest_row.get("case_id") != cid:
        v.append("manifest case_id does not equal the bundle identity")
    if manifest_row.get("reviewer_visible_sha256") != sha256_bytes(
            visible_bytes):
        v.append("manifest visible digest does not equal the exact visible "
                 "bytes")
    if manifest_row.get("authoring_commitment_sha256") != sha256_bytes(
            hidden_bytes):
        v.append("manifest commitment does not equal the exact hidden bytes")
    if external_key is not None and external_key != cid:
        v.append("externally keyed entry does not use the bundle identity")
    return v


def manifest_violations(rows):
    v = []
    ids = [r.get("case_id") for r in rows]
    for r in rows:
        if set(r) != MANIFEST_ROW_FIELDS:
            v.append("row shape: %s" % sorted(set(r) ^ MANIFEST_ROW_FIELDS))
            continue
        if not CASE_ID_RE.match(r["case_id"]):
            v.append("row case_id shape")
        for f in ("reviewer_visible_sha256", "authoring_commitment_sha256"):
            if not SHA_FIELD_RE.match(r[f]):
                v.append("row %s shape" % f)
    if len(ids) != len(set(ids)):
        v.append("duplicate case_id")
    if ids != sorted(i for i in ids if i is not None):
        v.append("rows not in lexical case_id order")
    return v


def manifest_binding_violations(rows, visible_bytes_by_id, retained_bytes_by_id):
    """One row <-> exactly one visible case and exactly one retained record,
    bound by exact bytes in both directions. Retained material is hashed
    directly - it is never parsed here."""
    v = manifest_violations(rows)
    row_ids = {r.get("case_id") for r in rows}
    for extra in sorted(row_ids - set(visible_bytes_by_id)):
        v.append("orphan row (no visible case): %s" % extra)
    for extra in sorted(set(visible_bytes_by_id) - row_ids):
        v.append("orphan visible case (no row): %s" % extra)
    for extra in sorted(row_ids ^ set(retained_bytes_by_id)):
        if extra in row_ids - set(retained_bytes_by_id):
            v.append("orphan row (no retained record): %s" % extra)
        elif extra in set(retained_bytes_by_id) - row_ids:
            v.append("orphan retained record (no row): %s" % extra)
    for r in rows:
        cid = r.get("case_id")
        if cid in visible_bytes_by_id and \
                r.get("reviewer_visible_sha256") != \
                sha256_bytes(visible_bytes_by_id[cid]):
            v.append("row visible-bytes digest mismatch: %s" % cid)
        if cid in retained_bytes_by_id and \
                r.get("authoring_commitment_sha256") != \
                sha256_bytes(retained_bytes_by_id[cid]):
            v.append("row retained-bytes commitment mismatch: %s" % cid)
    return v


def reveal_violations(published_commitments, retained_bytes_by_id):
    """Custody law over EXACT RETAINED BYTES: every published commitment must
    reproduce by hashing the retained byte sequence directly, before any
    parse or canonical reserialisation. Published commitments are immutable
    inputs; no parse happens here, so repair by reserialisation does not
    exist as an operation."""
    v = []
    if set(published_commitments) != set(retained_bytes_by_id):
        v.append("missing or extra retained record")
        return v
    for cid, committed in published_commitments.items():
        if sha256_bytes(retained_bytes_by_id[cid]) != committed:
            v.append("commitment mismatch: %s" % cid)
    return v


def _sentinel_record(cls, case_id=None):
    pc = {p: ("same" if p != "authority" else
              {"A": "different", "B": "same", "C": "underdetermined"}[cls])
          for p in PROPERTIES}
    if cls == "B":
        pc["review state"] = "not_engaged"
    return {
        "schema": AUTHORING_SCHEMA,
        "case_id": case_id or ("W8-C-" + "0" * 64),
        "authored_class": cls,
        "intended_disposition": CLASS_TOKEN[cls],
        "property_construction": pc,
        "surface_features_varied": ["verbosity"] if cls == "B" else [],
        "inconclusive_conditions":
            ["insufficient_source_evidence"] if cls == "C" else [],
        "authoring_checks": sorted(CLASS_CHECKS[cls]),
        "authoring_rationale": "mechanics sentinel - not a case",
        "reviewer_visible_sha256": "sha256:" + "0" * 64,
        "commitment_nonce": SENTINEL_NONCE,
    }


# ------------------------------------------------------------------- proofs
class V1toV3_ReviewerVisibleShape(unittest.TestCase):
    def test_v1_closed_top_level_shape(self):
        case = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        self.assertEqual(review_case_violations(case), [])
        with self.subTest(control="extra field detected"):
            m = dict(case); m["note"] = "x"
            self.assertTrue(review_case_violations(m))
        with self.subTest(control="missing field detected"):
            m = dict(case); del m["structural_provenance_support"]
            self.assertTrue(review_case_violations(m))
        with self.subTest(control="wrong schema detected"):
            m = dict(case); m["schema"] = "w8-review-case-v2"
            self.assertIn("schema", review_case_violations(m))
        with self.subTest(control="malformed case_id shape detected"):
            m = dict(case); m["case_id"] = "W8-C-" + "0" * 63
            self.assertIn("case_id shape", review_case_violations(m))

    def test_v2_admissible_evidence_shape(self):
        case = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        with self.subTest(control="empty variant detected"):
            m = json.loads(json.dumps(case))
            m["admissible_source_evidence"]["variant_a"] = ""
            self.assertTrue(review_case_violations(m))
        with self.subTest(control="identical variants rejected at orientation"):
            with self.assertRaises(ValueError):
                orient(SENTINEL_TEXT_1, SENTINEL_TEXT_1)
        with self.subTest(control="extra evidence field detected"):
            m = json.loads(json.dumps(case))
            m["admissible_source_evidence"]["variant_c"] = "x"
            self.assertTrue(review_case_violations(m))

    def test_v3_forbidden_predisposition_fields_detected(self):
        case = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        for leak in ("authored_class", "intended_disposition",
                     "governed_property", "authoring_rationale", "title",
                     "timestamp"):
            with self.subTest(planted=leak):
                m = dict(case); m[leak] = "leak"
                v = review_case_violations(m)
                self.assertTrue(any("forbidden" in x or "shape" in x
                                    for x in v))


class V4_IdentityAndOrdering(unittest.TestCase):
    def test_v4_orientation_identity_and_order_are_mechanical(self):
        with self.subTest(fact="orientation is argument-order independent"):
            self.assertEqual(orient(SENTINEL_TEXT_1, SENTINEL_TEXT_2),
                             orient(SENTINEL_TEXT_2, SENTINEL_TEXT_1))
        a, b = orient(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        cid = case_identity(a, b)
        with self.subTest(fact="identity is the full untruncated digest"):
            self.assertTrue(CASE_ID_RE.match(cid))
        with self.subTest(fact="identity derives from evidence alone - "
                               "hidden-material changes cannot move it"):
            self.assertEqual(case_identity(a, b), cid)  # no other inputs exist
        with self.subTest(control="author-preferred order detected"):
            rows = [{"case_id": "W8-C-" + "f" * 64,
                     "reviewer_visible_sha256": "sha256:" + "0" * 64,
                     "authoring_commitment_sha256": "sha256:" + "0" * 64},
                    {"case_id": "W8-C-" + "0" * 64,
                     "reviewer_visible_sha256": "sha256:" + "1" * 64,
                     "authoring_commitment_sha256": "sha256:" + "1" * 64}]
            self.assertIn("rows not in lexical case_id order",
                          manifest_violations(rows))


class V5toV7_WithheldRecord(unittest.TestCase):
    def test_v5_closed_schema_and_vocabularies(self):
        for cls in sorted(CLASSES):
            with self.subTest(sentinel_class=cls):
                self.assertEqual(
                    authoring_record_violations(_sentinel_record(cls)), [])
        with self.subTest(control="extra field detected"):
            m = _sentinel_record("A"); m["expected_score"] = 1
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="missing field detected"):
            m = _sentinel_record("A"); del m["commitment_nonce"]
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="fourth class detected"):
            m = _sentinel_record("A"); m["authored_class"] = "D"
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="fourth token detected"):
            m = _sentinel_record("A")
            m["intended_disposition"] = "governance_delta_not_established"
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="malformed hidden case_id detected"):
            m = _sentinel_record("A", case_id="case-1")
            self.assertIn("case_id shape", authoring_record_violations(m))
        with self.subTest(control="empty rationale detected"):
            m = _sentinel_record("A"); m["authoring_rationale"] = "  "
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="unknown surface feature detected"):
            m = _sentinel_record("B")
            m["surface_features_varied"] = ["verbosity", "charisma"]
            self.assertTrue(any("surface_features_varied vocabulary" in x
                                for x in authoring_record_violations(m)))
        with self.subTest(control="duplicate inconclusive label detected"):
            m = _sentinel_record("C")
            m["inconclusive_conditions"] = ["insufficient_source_evidence",
                                            "insufficient_source_evidence"]
            self.assertTrue(any("unique" in x
                                for x in authoring_record_violations(m)))

    def test_v5_closed_authoring_checks_vocabulary(self):
        with self.subTest(control="unknown declaration label detected"):
            m = _sentinel_record("A")
            m["authoring_checks"] = sorted(CLASS_CHECKS["A"]) + ["vibes_good"]
            self.assertTrue(any("authoring_checks vocabulary" in x
                                for x in authoring_record_violations(m)))
        with self.subTest(control="missing required class declaration "
                                  "detected"):
            m = _sentinel_record("A")
            m["authoring_checks"] = sorted(CLASS_CHECKS["A"])[:-1]
            self.assertTrue(any("exactly the class-A set" in x
                                for x in authoring_record_violations(m)))
        with self.subTest(control="foreign-class declaration detected"):
            m = _sentinel_record("B")
            m["authoring_checks"] = sorted(CLASS_CHECKS["B"]
                                           | {"delta_property_identified"})
            self.assertTrue(any("exactly the class-B set" in x
                                for x in authoring_record_violations(m)))

    def test_v6_exact_nine_property_map(self):
        with self.subTest(control="tenth property detected"):
            m = _sentinel_record("A")
            m["property_construction"]["continuity"] = "same"
            self.assertTrue(any("property map keys" in x
                                for x in authoring_record_violations(m)))
        with self.subTest(control="missing property detected"):
            m = _sentinel_record("A")
            del m["property_construction"]["attribution"]
            self.assertTrue(any("property map keys" in x
                                for x in authoring_record_violations(m)))
        with self.subTest(control="unknown state detected"):
            m = _sentinel_record("A")
            m["property_construction"]["authority"] = "probably_different"
            self.assertTrue(authoring_record_violations(m))

    def test_v7_class_bindings_constraints_and_cross_binding(self):
        with self.subTest(control="wrong class-token binding detected"):
            m = _sentinel_record("A")
            m["intended_disposition"] = "no_governance_delta"
            self.assertIn("class-to-token binding",
                          authoring_record_violations(m))
        with self.subTest(control="class A with underdetermined detected"):
            m = _sentinel_record("A")
            m["property_construction"]["permission"] = "underdetermined"
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="class B with different detected"):
            m = _sentinel_record("B")
            m["property_construction"]["authority"] = "different"
            self.assertTrue(authoring_record_violations(m))
        with self.subTest(control="class C without inconclusive label "
                                  "detected"):
            m = _sentinel_record("C"); m["inconclusive_conditions"] = []
            self.assertTrue(authoring_record_violations(m))
        case = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        case_bytes = canonical_bytes(case)
        rec = _sentinel_record("A", case_id=case["case_id"])
        rec["reviewer_visible_sha256"] = sha256_bytes(case_bytes)
        with self.subTest(fact="a correctly sealed record binds"):
            self.assertEqual(
                cross_binding_violations(case, case_bytes, rec), [])
        with self.subTest(control="identity mismatch detected"):
            m = dict(rec); m["case_id"] = "W8-C-" + "1" * 64
            self.assertTrue(cross_binding_violations(case, case_bytes, m))
        with self.subTest(control="visible-bytes digest mismatch detected"):
            m = dict(rec); m["reviewer_visible_sha256"] = "sha256:" + "2" * 64
            self.assertTrue(cross_binding_violations(case, case_bytes, m))


class V8toV9_CanonicalBytesAndNonce(unittest.TestCase):
    def test_v8_canonical_reproducibility_and_mutation_detection(self):
        rec = _sentinel_record("A")
        b1, b2 = canonical_bytes(rec), canonical_bytes(rec)
        with self.subTest(fact="same value, same bytes, same digest"):
            self.assertEqual(b1, b2)
            self.assertEqual(sha256_bytes(b1), sha256_bytes(b2))
        with self.subTest(fact="exactly one terminal LF, no BOM, "
                               "compact separators"):
            self.assertTrue(b1.endswith(b"\n") and not b1.endswith(b"\n\n"))
            self.assertFalse(b1.startswith(b"\xef\xbb\xbf"))
            self.assertNotIn(b": ", b1)
        with self.subTest(fact="non-ASCII survives unescaped"):
            self.assertIn("—", canonical_bytes(
                {"x": "em — dash"}).decode("utf-8"))
        with self.subTest(control="one-byte mutation detected"):
            mutated = b1[:-2] + b"X\n"
            self.assertNotEqual(sha256_bytes(b1), sha256_bytes(mutated))
        with self.subTest(control="NaN refused"):
            with self.assertRaises(ValueError):
                canonical_bytes({"x": float("nan")})

    def test_v9_nonce_shape_mechanics_sentinel_only(self):
        with self.subTest(fact="the sentinel is shape-valid and labelled"):
            self.assertTrue(HEX64.match(SENTINEL_NONCE))
            self.assertIn("mechanics-only sentinel",
                          Path(__file__).read_text(encoding="utf-8"))
        for bad in ("0" * 63, "0" * 65, "G" + "0" * 63, "0" * 32):
            with self.subTest(control="bad nonce shape detected", value=bad[:8]):
                m = _sentinel_record("A"); m["commitment_nonce"] = bad
                self.assertIn("commitment_nonce shape",
                              authoring_record_violations(m))


class V10toV11_ManifestBindingAndCustody(unittest.TestCase):
    def _sentinel_world(self):
        case = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_2)
        case_bytes = canonical_bytes(case)
        rec = _sentinel_record("C", case_id=case["case_id"])
        rec["reviewer_visible_sha256"] = sha256_bytes(case_bytes)
        rec_bytes = canonical_bytes(rec)
        row = {"case_id": case["case_id"],
               "reviewer_visible_sha256": sha256_bytes(case_bytes),
               "authoring_commitment_sha256": sha256_bytes(rec_bytes)}
        return case, case_bytes, rec_bytes, row

    def test_v10_manifest_cross_artefact_binding(self):
        case, case_bytes, rec_bytes, row = self._sentinel_world()
        visible = {case["case_id"]: case_bytes}
        retained = {case["case_id"]: rec_bytes}
        self.assertEqual(
            manifest_binding_violations([row], visible, retained), [])
        with self.subTest(control="orphan row detected"):
            self.assertTrue(manifest_binding_violations([row], {}, retained))
        with self.subTest(control="orphan visible case detected"):
            extra = dict(visible); extra["W8-C-" + "9" * 64] = b"x\n"
            self.assertTrue(
                manifest_binding_violations([row], extra, retained))
        with self.subTest(control="orphan retained record detected"):
            extra = dict(retained); extra["W8-C-" + "9" * 64] = b"x\n"
            self.assertTrue(
                manifest_binding_violations([row], visible, extra))
        with self.subTest(control="visible-bytes digest mismatch detected"):
            m = dict(row); m["reviewer_visible_sha256"] = "sha256:" + "3" * 64
            self.assertTrue(
                manifest_binding_violations([m], visible, retained))
        with self.subTest(control="retained-bytes commitment mismatch "
                                  "detected"):
            m = dict(row)
            m["authoring_commitment_sha256"] = "sha256:" + "4" * 64
            self.assertTrue(
                manifest_binding_violations([m], visible, retained))
        with self.subTest(control="class leakage field detected"):
            m = dict(row); m["authored_class"] = "A"
            self.assertTrue(any("row shape" in x
                                for x in manifest_binding_violations(
                                    [m], visible, retained)))
        with self.subTest(control="duplicate case_id detected"):
            self.assertIn("duplicate case_id",
                          manifest_violations([row, dict(row)]))

    def test_v10_prefreeze_bundle_binding_is_atomic(self):
        case_a, bytes_a, rec_bytes_a, row_a = self._sentinel_world()
        rec_a = json.loads(rec_bytes_a)
        with self.subTest(fact="a coherent bundle passes atomically, keyed "
                               "by its own identity"):
            self.assertEqual(
                bundle_binding_violations(case_a, bytes_a, rec_a,
                                          rec_bytes_a, row_a,
                                          external_key=case_a["case_id"]),
                [])
        case_b = build_review_case(SENTINEL_TEXT_1, SENTINEL_TEXT_3)
        bytes_b = canonical_bytes(case_b)
        with self.subTest(control="parsed visible case A with canonical "
                                  "visible bytes from case B fails"):
            self.assertTrue(
                bundle_binding_violations(case_a, bytes_b, rec_a,
                                          rec_bytes_a, row_a))
        rec_b = _sentinel_record("C", case_id=case_b["case_id"])
        rec_b["reviewer_visible_sha256"] = sha256_bytes(bytes_b)
        rec_bytes_b = canonical_bytes(rec_b)
        with self.subTest(control="manifest and key for A with canonical "
                                  "hidden bytes whose record says case B "
                                  "fails"):
            self.assertTrue(
                bundle_binding_violations(case_a, bytes_a, rec_b,
                                          rec_bytes_b, row_a,
                                          external_key=case_a["case_id"]))
        with self.subTest(control="an independently trusted external key "
                                  "fails"):
            self.assertIn("externally keyed entry does not use the bundle "
                          "identity",
                          bundle_binding_violations(case_a, bytes_a, rec_a,
                                                    rec_bytes_a, row_a,
                                                    external_key="case-007"))
        with self.subTest(control="freeze-time byte drift fails even when "
                                  "everything else agrees"):
            drifted = rec_bytes_a[:-1] + b" \n"
            self.assertTrue(
                bundle_binding_violations(case_a, bytes_a, rec_a,
                                          drifted, row_a))

    def test_v11_custody_on_exact_bytes_with_no_reserialisation_repair(self):
        _, _, rec_bytes, _ = self._sentinel_world()
        other = canonical_bytes(_sentinel_record("A"))
        retained = {"one": rec_bytes, "two": other}
        published = {cid: sha256_bytes(raw) for cid, raw in retained.items()}
        with self.subTest(fact="byte-exact reproduction permits reveal"):
            self.assertEqual(reveal_violations(published, retained), [])
        with self.subTest(control="a missing record is a stop"):
            self.assertTrue(reveal_violations(published,
                                              {"one": rec_bytes}))
        mutated = rec_bytes[:-1] + b" \n"  # semantics-preserving whitespace
        with self.subTest(fact="the planted mutation is JSON-equivalent "
                               "but byte-different"):
            self.assertEqual(json.loads(rec_bytes), json.loads(mutated))
            self.assertNotEqual(rec_bytes, mutated)
        with self.subTest(control="the semantics-preserving byte mutation "
                                  "is a STOP"):
            self.assertTrue(reveal_violations(
                published, {"one": mutated, "two": other}))
        with self.subTest(fact="reserialisation would have masked it - "
                               "which is exactly why parsing retained "
                               "material is unlawful"):
            self.assertEqual(canonical_bytes(json.loads(mutated)), rec_bytes)
            self.assertNotEqual(sha256_bytes(mutated),
                                published["one"])


class V12_DoctrineCarriageAndAbsence(unittest.TestCase):
    def test_v12_carriage_is_byte_identical_to_adr0054(self):
        a55, a54 = _text(ADR55), _text(ADR54)
        QUESTION = ("*on the admissible source evidence alone, does a "
                    "recognised governed property differ between the paired "
                    "variants in a way that changes a downstream obligation, "
                    "permission, authority, treatment or state?*")
        NINE = ("**confidence ≠ authority · verbosity ≠ governance "
                "significance · warmth ≠ permission · explanation ≠ "
                "evidence · textual difference ≠ governance difference · "
                "textual similarity ≠ governance equivalence · absence of "
                "explicit wording ≠ absence of governed effect · mechanical "
                "agreement ≠ human acceptance · uncertainty ≠ failure.**")
        for name, s in (("human review question", QUESTION),
                        ("nine-rule block", NINE)):
            with self.subTest(carried=name):
                self.assertIn(s, a55)
                self.assertIn(s, a54)
        with self.subTest(fact="four evidence categories carried with no "
                               "conversion"):
            for cat in ("admissible source evidence",
                        "support material", "withheld authoring material",
                        "post-disposition calibration material"):
                self.assertIn(cat, a55)
            self.assertIn("no category conversion", a55)
        with self.subTest(fact="no-contact and standing duties carried"):
            self.assertIn("no model contact, prompt for contact, provider, "
                          "credential, SDK, transport, binary or contact "
                          "harness", a55)
            self.assertIn("a fresh P4b human act at every landing", a55)
        with self.subTest(fact="direct-bytes custody law carried"):
            self.assertIn("hashes the exact retained bytes directly", a55)

    def test_v12_d2b_contains_no_case_corpus_record_nonce_or_commitment(self):
        tracked = subprocess.run(
            ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
            check=True).stdout.split()
        with self.subTest(fact="no tracked W8 case file exists"):
            self.assertEqual([p for p in tracked if "W8-C-" in p], [])
        with self.subTest(fact="no tracked file carries the authoring "
                               "schema except this module and the law"):
            offenders = []
            for p in tracked:
                if p in ("docs/decisions/0055-w8-case-shape-evidence-"
                         "separation-blinding-law.md",
                         "tests/test_w8_discriminating_instrument_"
                         "envelope.py"):
                    continue
                try:
                    data = (ROOT / p).read_bytes()
                except OSError:
                    continue
                if b"w8-authoring-record-v1" in data:
                    offenders.append(p)
            self.assertEqual(offenders, [])
        flat = " ".join(__doc__.split())
        for clause in ("any case's authored class or human disposition",
                       "that any authoring declaration is semantically true",
                       "that any model was contacted",
                       "that ADR-0047 precondition 3 moved",
                       "that D2-C is open"):
            with self.subTest(clause=clause[:44]):
                self.assertIn(clause, flat)


if __name__ == "__main__":
    unittest.main()
