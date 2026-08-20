"""W7-D2-E — proofs for the generated-evaluation shape law (ADR-0048, ADR-0049, ADR-0050).

ABSENCE MAY PROVE DORMANCY; ABSENCE MAY NOT DISCHARGE A DEBT WHOSE SUBJECT DOES NOT EXIST.

Nineteen obligations are inherited. This module implements what a machine can
honestly decide today and refuses to imply the rest:

  LIVE (5)          S1 T1 T2 T3 U1 — the subject exists; the proof establishes the obligation.
  READY / DEBT (10) S2 T4 T5 T7 T8 T9 U2 U3 U4 U5 — the predicate runs and its
                    negative controls bite, but no generated-evaluation record
                    exists, so the obligation is OUTSTANDING, not satisfied.
  REVIEW-ONLY (4)   S3 S4 T6 U6 — human duties. They are not tests here, not
                    skips, not TODOs, and not pending-ledger rows.

WHAT GREEN DOES NOT MEAN. A green run of this module NEVER establishes:
that a generated-evaluation record exists; that a manifest exists; that any
record-dependent debt has been discharged merely because there are no records;
that model contact occurred or is authorised; that a specimen exists or is
authorised; that generated output was imported; that a harness exists; that any
evaluation result is correct; that anything is safe, clinically valid, approved,
production-ready or authoritative; that ADR-0050's Part Q publication seam has
been resolved; or that W7-D3 is open.

SOURCE AUTHORITY. The landed records are the source of truth. Expected shapes are
PARSED from ADR-0049 and ADR-0050, never re-expressed here. No canonical expected
field name or expected object shape is independently declared by this module.
Synthetic mutant keys used solely as negative controls do not become schema
authority. Every governed constant this module uses — the reserved home, the
non-authority ceiling, the disposition set, the locus field — is DERIVED from
landed source at import, and where landed law states the same fact in two
authoritative places the two are reconciled against each other. Source document
wins; the validator is derived proof, never doctrine.

NO ARTEFACT SHAPE IS INVENTED HERE. Where a governed artefact does not yet exist
— the manifest above all — its predicate operates on neutral relation inputs and
names no key, no entry object and no field of the artefact to come.
"""

import copy
import inspect
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADR_BOUNDARY = ROOT / "docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md"
ADR_RECORD_SHAPE = ROOT / "docs/decisions/0048-generated-evaluation-record-shape-doctrine.md"
ADR_FIELD_LAW = ROOT / "docs/decisions/0049-generated-evaluation-field-law.md"
ADR_FINDINGS = ROOT / "docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md"
ALLOWLIST = ROOT / "scripts/scan-allowlist.txt"

ARROW = "→"


def _src(path):
    return path.read_text(encoding="utf-8")


def _anchored(path, pattern, what, flags=re.S):
    """Read one governed fact from landed source. A moved anchor is source drift."""
    m = re.search(pattern, _src(path), flags)
    if m is None:
        raise AssertionError(f"{path.name}: {what} anchor not found (source drift)")
    return m


def _tables(path, header):
    lines = _src(path).split("\n")
    found = []
    for i, line in enumerate(lines):
        if line.startswith(header):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append([c.strip() for c in row.strip().strip("|").split("|")])
            found.append(rows)
    return found


def _plain(cell):
    return re.sub(r"[`*]", "", cell).split(" —")[0].strip()


def _ticked(text):
    return re.findall(r"`([^`]+)`", text)


# --------------------------------------------------------------------------
# Governed constants, every one derived from landed source. Nothing transcribed.
# --------------------------------------------------------------------------

def reserved_home():
    """ADR-0048 decision 7 fixes the home of the future class."""
    return _anchored(ADR_RECORD_SHAPE, r"The home of the future class is `([^`]+)`",
                     "decision 7 home").group(1)


def barred_allowlist_prefix():
    """ADR-0050 decision 32 states the same path as the barred allowlist prefix."""
    return _anchored(ADR_FINDINGS,
                     r"may never contain an entry whose path lies under `([^`]+)`",
                     "decision 32 allowlist bar").group(1)


def ceiling_from(path, anchor):
    """The ADR-0046 decision 23 ceiling sentence, read from a record that carries it."""
    lines = _src(path).split("\n")
    for i, line in enumerate(lines):
        if anchor in line:
            for nxt in lines[i + 1:i + 4]:
                stripped = nxt.strip()
                if stripped.startswith("> **") and stripped.endswith("**"):
                    return stripped[4:-2]
    raise AssertionError(f"{path.name}: ceiling anchor not found (source drift)")


CEILING_ANCHOR_FIELD_LAW = "carries the ADR-0046 decision 23 sentence"
CEILING_ANCHOR_BOUNDARY = "carries this sentence, byte-identically, inside itself"


def disposition_table():
    """ADR-0050 Part F. Value and its own landability column, both source-read."""
    tables = _tables(ADR_FINDINGS, "| Value | Exact meaning |")
    if len(tables) != 1:
        raise AssertionError("ADR-0050 Part F disposition table not found (source drift)")
    return {_plain(r[0]): _plain(r[3]) for r in tables[0]}


def locus_field():
    """ADR-0050 Part D. The single inner position of `locus`."""
    tables = _tables(ADR_FINDINGS, "| Field | Type | Meaning |")
    if len(tables) != 1 or len(tables[0]) != 1:
        raise AssertionError("ADR-0050 Part D locus table not found as one row (source drift)")
    return _plain(tables[0][0][0])


RESERVED_HOME = reserved_home()
NON_AUTHORITY_CEILING = ceiling_from(ADR_FIELD_LAW, CEILING_ANCHOR_FIELD_LAW)
DISPOSITION_LANDABILITY = disposition_table()
DISPOSITIONS = tuple(DISPOSITION_LANDABILITY)
LOCUS_FIELD = locus_field()


# --------------------------------------------------------------------------
# Source-derived schema. Parsed from landed authority; nothing declared here.
# --------------------------------------------------------------------------

def field_tables():
    """ADR-0049's two accepted field tables: record-level, then capture-level."""
    tables = _tables(ADR_FIELD_LAW, "| # | Field | Holds | Nullable |")
    if len(tables) != 2:
        raise AssertionError(f"ADR-0049 field tables not found as expected: {len(tables)}")
    return tables[0], tables[1]


def nested_shapes():
    """The eight nested shapes, parsed from the accepted `Holds` cells themselves."""
    record, _ = field_tables()
    shapes = {}
    for row in record:
        name = _plain(row[1])
        braced = re.search(r"\{([^}]*)\}", row[2])
        if braced:
            shapes[name] = [f.split(":")[0].strip().strip("`")
                            for f in braced.group(1).split(",")]
    return shapes


def wrapper_key():
    """Narrow anchor: ADR-0049 decision 4. Fails if the anchor moves."""
    return _anchored(ADR_FIELD_LAW, r"One top-level wrapper key, `([a-z_]+)`",
                     "decision 4 wrapper").group(1)


def finding_event_fields():
    """Narrow anchor for the finding-event shape.

    Source-fidelity note: the five-field set is FIXED by ADR-0049 ("carries exactly
    the five fields ... and no sixth"); ADR-0050 carries it as a quoted fixed input.
    The anchor therefore reads ADR-0049, where the law actually sits, and the
    cross-record agreement is asserted separately. Either anchor moving is drift.
    """
    m = _anchored(ADR_FIELD_LAW, r"exactly the five fields \*\*`\{([^}]*)\}`\*\*",
                  "finding-event five-field set")
    return [f.strip() for f in m.group(1).split(",")]


def finding_event_fields_as_carried():
    """The same set as ADR-0050 carries it, for cross-record agreement."""
    m = _anchored(ADR_FINDINGS, r"the finding event is exactly `\{([^}]*)\}`",
                  "carried finding-event set")
    return [f.strip() for f in m.group(1).split(",")]


def canonical_shapes():
    """The twelve object shapes ADR-0049 fixes, every one source-derived."""
    record, capture = field_tables()
    shapes = {"wrapper": [wrapper_key()], "record": [_plain(r[1]) for r in record]}
    shapes.update(nested_shapes())
    shapes["capture"] = [_plain(r[1]) for r in capture]
    shapes["finding_event"] = finding_event_fields()
    return shapes


def counting_table():
    rows = _tables(ADR_FIELD_LAW, "| Level | Positions |")[0]
    return {r[0]: int(re.sub(r"\D", "", r[1])) for r in rows}


def count_key(counts, prefix):
    keys = [k for k in counts if k.startswith(prefix)]
    if len(keys) != 1:
        raise AssertionError(f"ADR-0049 counting row {prefix!r} not unique (source drift)")
    return keys[0]


def stated_nested_counts():
    """The per-shape counts the counting row states in its own label.

    A third authoritative statement, and the one that stops a compensating pair
    of errors inside the nested level from preserving the level total.
    """
    counts = counting_table()
    label = count_key(counts, "Nested")
    pairs = re.findall(r"`([a-z_\[\]]+)`(?: item)? (\d+)", label)
    return {name.replace("[]", ""): int(n) for name, n in pairs}


def nullability_positions():
    """ADR-0049's nullability table, as dotted positions."""
    rows = _tables(ADR_FIELD_LAW, "| Position | Null when | Lifecycle reason |")[0]
    return [_plain(r[0]) for r in rows]


_NULLABLE_WORDS = {"no": 0, "one": 1, "two": 2, "yes": 1}


def declared_nullable_counts():
    """Per-shape nullable counts, read from the field tables' own Nullable column."""
    record, capture = field_tables()
    declared = {}
    for row in record:
        cell = _plain(row[3]).lower()
        word = cell.split()[0] if cell else ""
        if word not in _NULLABLE_WORDS:
            raise AssertionError(f"ADR-0049 nullability cell unparsed: {cell!r}")
        declared[_plain(row[1])] = _NULLABLE_WORDS[word]
    capture_nullable = 0
    for row in capture:
        cell = _plain(row[3]).lower()
        word = cell.split()[0] if cell else ""
        if word not in _NULLABLE_WORDS:
            raise AssertionError(f"ADR-0049 capture nullability cell unparsed: {cell!r}")
        capture_nullable += _NULLABLE_WORDS[word]
    declared["capture"] = capture_nullable
    return declared


def vocabulary_table():
    rows = _tables(ADR_FIELD_LAW, "| Vocabulary | Values | Source |")[0]
    return {_plain(r[0]): _ticked(r[1]) for r in rows}


# Where ADR-0049 states the same vocabulary twice, both statements are located
# here by anchor. The anchors say WHERE to read; the values come from the source.
_RESTATEMENTS = (
    ("text_class", "ticked",
     r"`text_class` is a closed two-value set on each capture:\*\*(.*?)ADR-0047 decision 3\(b\)"),
    ("inputs[].origin", "ticked",
     r"declares `origin` from the closed three-value set\*\*(.*?)carried from ADR-0046"),
    ("delta.outcome", "ticked",
     r"`outcome` is the closed three-value set already in use\*\*(.*?)none of which means"),
    ("scan_status", "quoted", r'`scan_status == "([a-z_]+)"`'),
)


def restated_vocabularies():
    out = {}
    for name, mode, pattern in _RESTATEMENTS:
        if mode == "ticked":
            out[name] = _ticked(_anchored(ADR_FIELD_LAW, pattern, f"{name} restatement").group(1))
        else:
            values = re.findall(pattern, _src(ADR_FIELD_LAW))
            if not values:
                raise AssertionError(f"ADR-0049: {name} restatement anchor not found (source drift)")
            seen = []
            for v in values:
                if v not in seen:
                    seen.append(v)
            out[name] = seen
    return out


def order_claims():
    """Part C decision 9's three orderings, parsed as claims rather than assumed."""
    precedes = _anchored(ADR_FIELD_LAW, r"\*\*`(\w+)` precedes `(\w+)`\*\*",
                         "order claim: precedes")
    checks = _anchored(ADR_FIELD_LAW, r"\*\*`(\w+)` precedes the standing checks\*\*",
                       "order claim: standing checks")
    between = _anchored(ADR_FIELD_LAW, r"the two standing checks and `(\w+)` sit between them",
                        "order claim: the two standing checks")
    last = _anchored(ADR_FIELD_LAW, r"\*\*`(\w+)` is last, always\*\*", "order claim: last")
    return {
        "precedes": (precedes.group(1), precedes.group(2)),
        "before_checks": checks.group(1),
        "checks_end_before": between.group(1),
        "checks_cardinality": 2,
        "last": last.group(1),
    }


def integrity_chain():
    """ADR-0049 decision 41 states the dependency chain literally. It is parsed, not built."""
    m = _anchored(ADR_FIELD_LAW, r"the dependency runs `([^`]+)` and never returns",
                  "decision 41 dependency chain")
    return [n.strip() for n in m.group(1).split(ARROW)]


def integrity_graph():
    """ADR-0049 Part M's graph, derived from landed authority rather than constructed.

    Nodes and direction come from decision 41's literal chain; the positions the
    record's bytes depend on come from the field tables. This module invents no
    edge and asserts no dependency the records do not state.
    """
    chain = integrity_chain()
    record, capture = field_tables()
    record_fields = [_plain(r[1]) for r in record]
    capture_fields = [_plain(r[1]) for r in capture]

    graph = {chain[0]: []}
    for i in range(1, len(chain)):
        graph[chain[i]] = [chain[i - 1]]
    for name in record_fields + capture_fields:
        graph.setdefault(name, [])
    # The record's bytes depend on every position the record declares.
    graph[chain[-2]] = [chain[-3]] + record_fields
    if "captures" in graph:
        graph["captures"] = capture_fields
    return graph


def in_record_positions():
    """ADR-0049 decision 42: the positions that live in the record, not the manifest."""
    m = _anchored(ADR_FIELD_LAW, r"\*\*In the record:\*\*(.*?)— identity and provenance",
                  "decision 42 record side")
    return _ticked(m.group(1))


def governed_names():
    """Every governed name this module's predicates address, all source-derived.

    A predicate may address governed field names; what it may not do is let a
    transcription become a second authority. Each debt test cross-checks the
    names and values its predicate uses against this source-derived map.
    """
    record, capture = field_tables()
    names = {"record": [_plain(r[1]) for r in record],
             "capture": [_plain(r[1]) for r in capture],
             "finding_event": finding_event_fields()}
    names.update(nested_shapes())
    return names


def cyclic(graph):
    state = {}

    def visit(node):
        if state.get(node) == 1:
            return True
        if state.get(node) == 2:
            return False
        state[node] = 1
        for nxt in graph.get(node, []):
            if visit(nxt):
                return True
        state[node] = 2
        return False

    return any(visit(n) for n in graph)


def tracked_records():
    """Tracked files under the reserved home. The subject of every record-level debt."""
    out = subprocess.run(["git", "ls-files", "--", RESERVED_HOME],
                         cwd=ROOT, capture_output=True, text=True, check=True)
    return [p for p in out.stdout.split() if p]


def allowlist_paths():
    rows = []
    for line in _src(ALLOWLIST).splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            rows.append(stripped.split("|")[0].strip())
    return rows


# --------------------------------------------------------------------------
# T1's single integrity checker. The live structure and every mutant go through
# this one function, so a control it would not catch cannot pass for one it would.
# --------------------------------------------------------------------------

def schema_statement_sources():
    """Everything T1 reconciles, read once from ADR-0049. No expectation declared."""
    record, capture = field_tables()
    return {
        "wrapper": [wrapper_key()],
        "record_fields": [_plain(r[1]) for r in record],
        "capture_fields": [_plain(r[1]) for r in capture],
        "finding_fields": finding_event_fields(),
        "nested": nested_shapes(),
        "nested_stated": stated_nested_counts(),
        "counts": counting_table(),
        "nullability": nullability_positions(),
        "nullable_declared": declared_nullable_counts(),
        "vocabulary": vocabulary_table(),
        "restated": restated_vocabularies(),
        "order": order_claims(),
    }


def schema_statement_disagreements(s):
    """T1 in one function: every statement ADR-0049 makes about its own schema,
    reconciled against every other. Returns the disagreements; empty means agreed."""
    out = []
    counts = s["counts"]

    levels = {
        "Wrapper": len(s["wrapper"]),
        "Top-level": len(s["record_fields"]),
        "Nested": sum(len(v) for v in s["nested"].values()),
        "Capture-object": len(s["capture_fields"]),
        "Finding-event": len(s["finding_fields"]),
    }
    for prefix, actual in levels.items():
        stated = counts[count_key(counts, prefix)]
        if stated != actual:
            out.append(f"count[{prefix}]: record states {stated}, shapes give {actual}")
    stated_total = counts[count_key(counts, "**Total")]
    if stated_total != sum(levels.values()):
        out.append(f"total: record states {stated_total}, levels sum to {sum(levels.values())}")

    for name, stated in s["nested_stated"].items():
        if name not in s["nested"]:
            out.append(f"nested[{name}]: counted in the label but no shape is declared")
        elif len(s["nested"][name]) != stated:
            out.append(f"nested[{name}]: label states {stated}, "
                       f"shape gives {len(s['nested'][name])}")
    for name in s["nested"]:
        if name not in s["nested_stated"]:
            out.append(f"nested[{name}]: shape declared but the counting label omits it")

    order, claim = s["record_fields"], s["order"]
    first, second = claim["precedes"]
    if first not in order or second not in order:
        out.append(f"order: claim names {first}/{second}, absent from the table")
    elif order.index(first) >= order.index(second):
        out.append(f"order: {first} must precede {second}")
    if not order or order[-1] != claim["last"]:
        out.append(f"order: {claim['last']} must be last, always")
    anchor, before = claim["checks_end_before"], claim["before_checks"]
    if anchor not in order or before not in order:
        out.append("order: the standing-check claim names a field absent from the table")
    else:
        checks = order[order.index(before) + 1:order.index(anchor)]
        if len(checks) != claim["checks_cardinality"]:
            out.append(f"order: {claim['checks_cardinality']} standing checks must sit "
                       f"between {before} and {anchor}, found {len(checks)}")

    shapes = dict(s["nested"])
    shapes["capture"] = s["capture_fields"]
    resolved = {}
    for position in s["nullability"]:
        parent, _, leaf = position.rpartition(".")
        shape = parent if parent in s["nested"] else ("capture" if leaf in s["capture_fields"] else None)
        if shape is None or leaf not in shapes.get(shape, []):
            out.append(f"nullable[{position}]: resolves to no declared shape position")
            continue
        resolved[shape] = resolved.get(shape, 0) + 1
    for shape, declared in s["nullable_declared"].items():
        if declared and resolved.get(shape, 0) != declared:
            out.append(f"nullable[{shape}]: field table declares {declared}, "
                       f"nullability table lists {resolved.get(shape, 0)}")
        if not declared and resolved.get(shape, 0):
            out.append(f"nullable[{shape}]: field table declares none, "
                       f"nullability table lists {resolved[shape]}")

    for name, values in s["restated"].items():
        tabled = s["vocabulary"].get(name)
        if tabled is None:
            out.append(f"vocabulary[{name}]: restated but absent from the vocabulary table")
        elif set(tabled) != set(values):
            out.append(f"vocabulary[{name}]: enumerated twice differently "
                       f"({sorted(tabled)} against {sorted(values)})")
    return out


# --------------------------------------------------------------------------
# Predicates. Pure functions over structures; none reads repository source.
# --------------------------------------------------------------------------

class _HashAbsent:
    """Sentinel: no hash is stated for this identity. Not a field, not a value."""

    def __repr__(self):
        return "<no hash stated>"


HASH_ABSENT = _HashAbsent()


def listing_and_hash_relation_holds(listed_hashes, present_hashes):
    """S2 (narrow): ADR-0048's set-and-hash RELATION only, over neutral inputs.

    No governed manifest artefact shape exists, so this predicate has none. Both
    arguments are plain mappings from a neutral identity token to a hash value,
    or to HASH_ABSENT where no hash is stated. It declares no manifest key, no
    entry object, no field name and no parser: it decides only whether the four
    ADR-0048 relations hold between a listing and what is present.
    """
    if set(listed_hashes) != set(present_hashes):
        return False
    for token, stated in listed_hashes.items():
        if stated is HASH_ABSENT:
            return False
        if stated != present_hashes[token]:
            return False
    return True


def pair_bijection(record):
    return set(record["captures"]) == set(record["pairing"]["variant_labels"])


def ceiling_verbatim_and_last(record):
    keys = list(record)
    return bool(keys) and keys[-1] == "non_authority" and \
        record.get("non_authority") == NON_AUTHORITY_CEILING


def delta_routing_coherent(record):
    if record["delta"]["outcome"] == "routed-to-review":
        return record["human_review"]["routed"] is True
    return True


def scan_status_coherent(record):
    refs = [f["capture_ref"] for f in record["findings"]]
    for label, capture in record["captures"].items():
        hits = refs.count(label)
        if capture["scan_status"] == "no_findings" and hits:
            return False
        if capture["scan_status"] == "findings_present" and not hits:
            return False
    return True


def input_source_lawful(value):
    """T9 mechanical limb only. The re-authoring limb is T6, review-only."""
    return not (re.search(r"\bGER-\d{4}\b", value) or RESERVED_HOME in value)


def exclusion_not_overridden(record):
    return record["exclusion_check"]["result"] != "listed_item_present"


def locus_valid(locus, capture_length):
    if set(locus) != {LOCUS_FIELD}:
        return False
    value = locus[LOCUS_FIELD]
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        return False
    return value <= capture_length


def findings_permit_landing(record):
    """U4: every disposition is in-set AND no finding-bearing record may land."""
    if any(f["disposition"] not in DISPOSITIONS for f in record["findings"]):
        return False
    return len(record["findings"]) == 0


def finding_refs_resolve(record):
    return all(f["capture_ref"] in record["captures"] for f in record["findings"])


# ==========================================================================
class LiveShapeLaw(unittest.TestCase):
    """T1, T2, T3 — LIVE. The subject is the landed declaration itself."""

    def test_t1_schema_statement_integrity(self):
        source = schema_statement_sources()

        with self.subTest(limb="every statement agrees"):
            self.assertEqual(schema_statement_disagreements(source), [])

        with self.subTest(control="a stated total diverges"):
            mutant = copy.deepcopy(source)
            key = count_key(mutant["counts"], "**Total")
            mutant["counts"][key] -= 1
            self.assertTrue(any(p.startswith("total:")
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(control="compensating level errors preserve the total"):
            mutant = copy.deepcopy(source)
            mutant["record_fields"].insert(0, mutant["capture_fields"].pop())
            problems = schema_statement_disagreements(mutant)
            self.assertEqual(len(problems), 2, problems)
            self.assertTrue(any("count[Top-level]" in p for p in problems))
            self.assertTrue(any("count[Capture-object]" in p for p in problems))
            self.assertFalse(any(p.startswith("total:") for p in problems),
                             "the total survives — the per-level checks are what bite")

        with self.subTest(control="compensating nested errors preserve the level"):
            mutant = copy.deepcopy(source)
            donor = next(k for k, v in mutant["nested"].items() if len(v) > 1)
            taker = next(k for k in mutant["nested"] if k != donor)
            mutant["nested"][taker].append(mutant["nested"][donor].pop())
            problems = schema_statement_disagreements(mutant)
            self.assertEqual(len(problems), 2, problems)
            self.assertTrue(any(f"nested[{donor}]" in p for p in problems))
            self.assertTrue(any(f"nested[{taker}]" in p for p in problems))
            self.assertFalse(any("count[Nested]" in p for p in problems),
                             "the nested level survives — the per-shape labels are what bite")

        with self.subTest(control="the final field is displaced"):
            mutant = copy.deepcopy(source)
            displaced = mutant["record_fields"].pop()
            mutant["record_fields"].insert(len(mutant["record_fields"]) - 1, displaced)
            self.assertTrue(any("must be last" in p
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(control="a precedence claim is contradicted"):
            mutant = copy.deepcopy(source)
            first, second = mutant["order"]["precedes"]
            i, j = mutant["record_fields"].index(first), mutant["record_fields"].index(second)
            mutant["record_fields"][i], mutant["record_fields"][j] = second, first
            self.assertTrue(any("must precede" in p
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(control="a standing check is moved out of place"):
            mutant = copy.deepcopy(source)
            anchor = mutant["record_fields"].index(mutant["order"]["checks_end_before"])
            mutant["record_fields"].insert(0, mutant["record_fields"].pop(anchor - 1))
            self.assertTrue(any("standing checks must sit" in p
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(control="a nullable position is dropped from the table"):
            mutant = copy.deepcopy(source)
            mutant["nullability"].pop()
            self.assertTrue(any(p.startswith("nullable[")
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(control="a nullable position names no declared field"):
            mutant = copy.deepcopy(source)
            parent = mutant["nullability"][0].rpartition(".")[0]
            mutant["nullability"][0] = parent + ".note"
            problems = schema_statement_disagreements(mutant)
            self.assertTrue(any("resolves to no declared shape position" in p
                                for p in problems))

        with self.subTest(control="a vocabulary is enumerated twice differently"):
            mutant = copy.deepcopy(source)
            name = next(iter(mutant["restated"]))
            mutant["restated"][name] = mutant["restated"][name][:-1]
            self.assertTrue(any("enumerated twice differently" in p
                                for p in schema_statement_disagreements(mutant)))

        with self.subTest(limb="the reconciled statements are the ones ADR-0049 names"):
            self.assertEqual(len(source["restated"]), 4)
            self.assertEqual(sum(source["nested_stated"].values()),
                             sum(len(v) for v in source["nested"].values()))
            self.assertEqual(len(source["nullability"]),
                             sum(source["nullable_declared"].values()))

    def test_t2_canonical_field_sets_over_twelve_shapes(self):
        shapes = canonical_shapes()
        self.assertEqual(len(shapes), 12, "ADR-0049 fixes twelve object shapes")
        for name, fields in shapes.items():
            with self.subTest(shape=name):
                self.assertTrue(fields, f"{name} derived no fields from its source")
                self.assertEqual(len(fields), len(set(fields)), f"{name} has a repeated field")
        every = {f for fields in shapes.values() for f in fields}
        for mutant in ("selected_variant", "capture_origin", "matched_text",
                       "best_answer", "basis", "note"):
            with self.subTest(control=mutant):
                self.assertNotIn(mutant, every,
                                 "control: an unlisted key must be rejected by the closed set")
        # Source-drift guards for the anchored extractions. If an anchor moves,
        # this fails rather than silently retaining a stale transcription.
        with self.subTest(anchor="ADR-0049 decision 4 wrapper"):
            self.assertEqual(wrapper_key(), "generated_evaluation_record")
        with self.subTest(anchor="ADR-0049 finding-event five-field set"):
            self.assertEqual(len(finding_event_fields()), 5)
            self.assertIn("locus", finding_event_fields())
        with self.subTest(anchor="ADR-0050 carries the same set"):
            self.assertEqual(finding_event_fields_as_carried(), finding_event_fields(),
                             "the two records must agree on the finding-event shape")

    def test_t3_integrity_graph_is_acyclic(self):
        chain = integrity_chain()
        graph = integrity_graph()
        record_fields = [_plain(r[1]) for r in field_tables()[0]]

        with self.subTest(anchor="ADR-0049 decision 41 states the chain"):
            self.assertEqual(len(chain), 4)
            self.assertEqual(chain[0], "text")
            self.assertEqual(chain[1], "text_digest")
            self.assertEqual(chain[-1], "manifest hash")
        with self.subTest(anchor="ADR-0049 decision 40 forbids an own content hash"):
            self.assertIn("The record never contains its own content hash",
                          _src(ADR_FIELD_LAW))
        with self.subTest(fact="text_digest depends on the text alone"):
            self.assertEqual(graph[chain[1]], [chain[0]])
        with self.subTest(fact="the manifest hash lies outside the record"):
            self.assertNotIn(chain[-1], record_fields)
            self.assertIn("**In the manifest only:**", _src(ADR_FIELD_LAW))
            self.assertNotIn(chain[-1], graph[chain[-2]],
                             "the record's bytes must not depend on the manifest hash")
        with self.subTest(fact="ADR-0049 decision 42 keeps identity in the record"):
            positions = in_record_positions()
            self.assertEqual(len(positions), 4)
            for name in positions:
                self.assertIn(name, record_fields)
        with self.subTest(case="the source-derived graph is acyclic"):
            self.assertFalse(cyclic(graph), "the declared integrity graph must be acyclic")
        with self.subTest(control="a planted self-hash is detected in the same graph"):
            planted = {k: list(v) for k, v in graph.items()}
            planted[chain[-2]] = planted[chain[-2]] + [chain[-1]]
            self.assertTrue(cyclic(planted), "control: a planted self-hash must be detected")


# ==========================================================================
class LiveHomeAndAllowlist(unittest.TestCase):
    """S1, U1 — LIVE. The home and the allowlist both exist as subjects today."""

    def test_s1_reserved_home_is_vacant(self):
        with self.subTest(anchor="ADR-0048 decision 7 states the home"):
            self.assertEqual(RESERVED_HOME, "governance/generated-evaluation/")
        self.assertEqual(tracked_records(), [])
        on_disk = ROOT / RESERVED_HOME
        self.assertFalse(on_disk.exists(), "the reserved home must not have been created")
        planted = RESERVED_HOME + "GER-0001.json"
        self.assertTrue(planted.startswith(RESERVED_HOME),
                        "control: a planted path under the home must be detectable")

    def test_u1_no_allowlist_entry_under_reserved_home(self):
        with self.subTest(anchor="ADR-0050 decision 32 bars the same path"):
            self.assertEqual(barred_allowlist_prefix(), RESERVED_HOME,
                             "the two records must agree on the barred prefix")
        rows = allowlist_paths()
        self.assertTrue(rows, "the allowlist must be readable")
        offenders = [p for p in rows if p.startswith(RESERVED_HOME)]
        self.assertEqual(offenders, [], "ADR-0050 Part I bars any such entry")
        planted = rows + [RESERVED_HOME + "GER-0001.json"]
        self.assertTrue([p for p in planted if p.startswith(RESERVED_HOME)],
                        "control: a planted allowlist row must be detected")


# ==========================================================================
class ReadyPredicatesForAbsentSubjects(unittest.TestCase):
    """S2 T4 T5 T7 T8 T9 U2 U3 U4 U5 — READY / DEBT.

    These prove the rule machinery is built and bites. They do NOT prove the
    obligation holds, because no generated-evaluation record exists to hold it.
    """

    def test_s2_listing_and_hash_relation_predicate(self):
        # Neutral identity tokens. Not record identifiers, not manifest keys and
        # not field names of any artefact: only the relation is under test.
        listed = {"one": "sha256:aa"}
        present = {"one": "sha256:aa"}
        with self.subTest(boundary="the predicate encodes no manifest shape"):
            doc = " ".join(listing_and_hash_relation_holds.__doc__.split())
            self.assertIn("No governed manifest artefact shape exists, so this "
                          "predicate has none", doc)
            body = inspect.getsource(listing_and_hash_relation_holds).split('"""')[2]
            self.assertNotIn('["', body,
                             "the predicate must index no named field of any artefact")
        with self.subTest(case="all four relations hold"):
            self.assertTrue(listing_and_hash_relation_holds(listed, present))
        with self.subTest(control="unlisted record present"):
            self.assertFalse(listing_and_hash_relation_holds(
                listed, {"one": "sha256:aa", "two": "sha256:bb"}))
        with self.subTest(control="listed record absent"):
            self.assertFalse(listing_and_hash_relation_holds(
                {"one": "sha256:aa", "two": "sha256:bb"}, present))
        with self.subTest(control="missing hash"):
            self.assertFalse(listing_and_hash_relation_holds({"one": HASH_ABSENT}, present))
        with self.subTest(control="hash mismatch"):
            self.assertFalse(listing_and_hash_relation_holds(listed, {"one": "sha256:zz"}))

    def test_t4_pair_bijection_predicate(self):
        base = {"pairing": {"variant_labels": ["a", "b"]}, "captures": {"a": {}, "b": {}}}
        with self.subTest(anchor="the names the predicate addresses are source-declared"):
            names = governed_names()
            self.assertIn("captures", names["record"])
            self.assertIn("variant_labels", names["pairing"])
        with self.subTest(case="both captures present"):
            self.assertTrue(pair_bijection(base))
        with self.subTest(control="one capture missing"):
            self.assertFalse(pair_bijection(
                {"pairing": {"variant_labels": ["a", "b"]}, "captures": {"a": {}}}))
        with self.subTest(control="undeclared extra capture"):
            self.assertFalse(pair_bijection(
                {"pairing": {"variant_labels": ["a", "b"]},
                 "captures": {"a": {}, "b": {}, "c": {}}}))

    def test_t5_ceiling_verbatim_and_last_predicate(self):
        with self.subTest(anchor="ADR-0049 and ADR-0046 state the same ceiling"):
            self.assertEqual(NON_AUTHORITY_CEILING,
                             ceiling_from(ADR_BOUNDARY, CEILING_ANCHOR_BOUNDARY),
                             "the two records must carry the ceiling byte-identically")
        with self.subTest(anchor="the ceiling is the record's last declared field"):
            self.assertEqual(governed_names()["record"][-1], "non_authority")
        with self.subTest(case="verbatim and final"):
            self.assertTrue(ceiling_verbatim_and_last(
                {"delta": 1, "non_authority": NON_AUTHORITY_CEILING}))
        with self.subTest(control="ceiling absent"):
            self.assertFalse(ceiling_verbatim_and_last({"delta": 1}))
        with self.subTest(control="ceiling changed"):
            self.assertFalse(ceiling_verbatim_and_last(
                {"delta": 1, "non_authority": NON_AUTHORITY_CEILING.replace("only", "mostly")}))
        with self.subTest(control="a field after the ceiling"):
            self.assertFalse(ceiling_verbatim_and_last(
                {"non_authority": NON_AUTHORITY_CEILING, "human_review": 1}))

    def test_t7_delta_routing_predicate(self):
        with self.subTest(anchor="the names and value the predicate uses are source-declared"):
            names = governed_names()
            self.assertIn("outcome", names["delta"])
            self.assertIn("routed", names["human_review"])
            self.assertIn("routed-to-review", vocabulary_table()["delta.outcome"])
        with self.subTest(case="routed outcome with routing true"):
            self.assertTrue(delta_routing_coherent(
                {"delta": {"outcome": "routed-to-review"}, "human_review": {"routed": True}}))
        with self.subTest(control="routed outcome with routing false"):
            self.assertFalse(delta_routing_coherent(
                {"delta": {"outcome": "routed-to-review"}, "human_review": {"routed": False}}))
        with self.subTest(case="reverse is lawful, one-way rule"):
            self.assertTrue(delta_routing_coherent(
                {"delta": {"outcome": "no-delta-observed"}, "human_review": {"routed": True}}))

    def test_t8_scan_status_predicate(self):
        with self.subTest(anchor="the names and values the predicate uses are source-declared"):
            names = governed_names()
            self.assertIn("scan_status", names["capture"])
            self.assertIn("capture_ref", names["finding_event"])
            self.assertEqual(set(vocabulary_table()["scan_status"]),
                             {"no_findings", "findings_present"})
        with self.subTest(case="clean capture, no findings"):
            self.assertTrue(scan_status_coherent(
                {"captures": {"a": {"scan_status": "no_findings"}}, "findings": []}))
        with self.subTest(control="says clean but carries a finding"):
            self.assertFalse(scan_status_coherent(
                {"captures": {"a": {"scan_status": "no_findings"}},
                 "findings": [{"capture_ref": "a"}]}))
        with self.subTest(control="says flagged with no finding"):
            self.assertFalse(scan_status_coherent(
                {"captures": {"a": {"scan_status": "findings_present"}}, "findings": []}))

    def test_t9_input_source_predicate(self):
        with self.subTest(anchor="the identifier form the predicate matches is source-declared"):
            self.assertIn("`GER-####`", _src(ADR_FIELD_LAW))
        with self.subTest(case="authored-synthetic citation"):
            self.assertTrue(input_source_lawful("W7-D4 probe set, item 3"))
        with self.subTest(case="repository fixture path"):
            self.assertTrue(input_source_lawful("fixtures/SYNTHETIC-d3-staleness-ladder.json"))
        with self.subTest(control="route: GER identifier"):
            self.assertFalse(input_source_lawful("GER-0001"))
        with self.subTest(control="route: class-home path"):
            self.assertFalse(input_source_lawful(RESERVED_HOME + "GER-0001.json"))
        with self.subTest(control="route: capture address"):
            self.assertFalse(input_source_lawful(
                RESERVED_HOME + "GER-0001.json#captures.variant_a"))
        with self.subTest(control="route: finding address"):
            self.assertFalse(input_source_lawful(
                RESERVED_HOME + "GER-0001.json#findings.F1"))

    def test_u2_exclusion_override_predicate(self):
        with self.subTest(anchor="the name and value the predicate uses are source-declared"):
            self.assertIn("result", governed_names()["exclusion_check"])
            self.assertIn("listed_item_present",
                          vocabulary_table()["exclusion_check.result"])
        with self.subTest(case="clean exclusion check"):
            self.assertTrue(exclusion_not_overridden(
                {"exclusion_check": {"result": "no_listed_item_present"}}))
        for disposition in DISPOSITIONS:
            with self.subTest(control=f"breach is non-landable under {disposition}"):
                self.assertFalse(exclusion_not_overridden(
                    {"exclusion_check": {"result": "listed_item_present"},
                     "findings": [{"disposition": disposition}]}))

    def test_u3_locus_predicate(self):
        with self.subTest(anchor="ADR-0050 decision 10 fixes one integer field"):
            self.assertEqual(LOCUS_FIELD, "character_start")
            self.assertIn("`locus` is an object with exactly one field, an integer",
                          _src(ADR_FINDINGS))
        with self.subTest(case="valid coordinate"):
            self.assertTrue(locus_valid({LOCUS_FIELD: 4}, 10))
        with self.subTest(control="extra key"):
            self.assertFalse(locus_valid({LOCUS_FIELD: 4, "note": "x"}, 10))
        with self.subTest(control="non-integer"):
            self.assertFalse(locus_valid({LOCUS_FIELD: 4.5}, 10))
        with self.subTest(control="bool rejected as int"):
            self.assertFalse(locus_valid({LOCUS_FIELD: True}, 10))
        with self.subTest(control="non-positive"):
            self.assertFalse(locus_valid({LOCUS_FIELD: 0}, 10))
        with self.subTest(control="string-bearing shape"):
            self.assertFalse(locus_valid({LOCUS_FIELD: "four"}, 10))
        with self.subTest(control="out-of-range coordinate"):
            self.assertFalse(locus_valid({LOCUS_FIELD: 11}, 10))

    def test_u4_disposition_predicate(self):
        with self.subTest(anchor="ADR-0050 Part F closes the set at three"):
            self.assertEqual(len(DISPOSITIONS), 3)
            self.assertIn("The three-value set is closed by this record", _src(ADR_FINDINGS))
        with self.subTest(anchor="no disposition permits a record to land"):
            self.assertEqual(set(DISPOSITION_LANDABILITY.values()), {"No"})
        with self.subTest(anchor="the names the predicate addresses are source-declared"):
            names = governed_names()
            self.assertIn("findings", names["record"])
            self.assertIn("disposition", names["finding_event"])
        with self.subTest(case="no findings"):
            self.assertTrue(findings_permit_landing({"findings": []}))
        for disposition in DISPOSITIONS:
            with self.subTest(control=f"{disposition} is non-landable"):
                self.assertFalse(findings_permit_landing(
                    {"findings": [{"disposition": disposition}]}))
        with self.subTest(control="out-of-set value rejected"):
            self.assertFalse(findings_permit_landing(
                {"findings": [{"disposition": "accepted"}]}))

    def test_u5_finding_reference_predicate(self):
        with self.subTest(anchor="the name the predicate addresses is source-declared"):
            self.assertIn("capture_ref", governed_names()["finding_event"])
        with self.subTest(case="reference present"):
            self.assertTrue(finding_refs_resolve(
                {"captures": {"a": {}}, "findings": [{"capture_ref": "a"}]}))
        with self.subTest(control="reference absent"):
            self.assertFalse(finding_refs_resolve(
                {"captures": {"a": {}}, "findings": [{"capture_ref": "z"}]}))


# ==========================================================================
class DebtsRemainOutstanding(unittest.TestCase):
    """Anti-vacuity. The distinction between LIVE and READY/DEBT is asserted."""

    def test_no_generated_evaluation_record_exists(self):
        self.assertEqual(tracked_records(), [],
                         "a record would change every record-level obligation's status")
        self.assertFalse((ROOT / RESERVED_HOME).exists())

    def test_absence_does_not_discharge_record_dependent_debts(self):
        self.assertIn("ABSENCE MAY PROVE DORMANCY", __doc__)
        self.assertIn("MAY NOT DISCHARGE A DEBT WHOSE SUBJECT DOES NOT EXIST", __doc__)
        self.assertIn("OUTSTANDING, not satisfied", __doc__)
        self.assertEqual(tracked_records(), [],
                         "the ten record-level obligations remain outstanding debts")


# ==========================================================================
class WhatGreenDoesNotMean(unittest.TestCase):
    """The boundary contract, asserted so it cannot be deleted while green."""

    def test_module_states_its_boundary(self):
        flat = " ".join(__doc__.split())
        for clause in ("that a generated-evaluation record exists",
                       "that a manifest exists",
                       "that model contact occurred or is authorised",
                       "that a specimen exists or is authorised",
                       "that generated output was imported",
                       "that a harness exists",
                       "Part Q publication seam has been resolved",
                       "that W7-D3 is open"):
            with self.subTest(clause=clause[:40]):
                self.assertIn(clause, flat)
        for duty in ("S3", "S4", "T6", "U6"):
            with self.subTest(review_only=duty):
                self.assertIn(duty, __doc__)


if __name__ == "__main__":
    unittest.main()
