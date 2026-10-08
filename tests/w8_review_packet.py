"""W8-D3 review-packet renderer (ADR-0057 Part A).

Renders the blind-session packet for the W8-D3 human disposition session from
the committed Git object bytes of published W8 review cases, as W8-D2-CBC
requires. It is deterministic and has no third-party dependency: it uses only
the Python standard library apart from the published ADR-0055 envelope
validator. It reads nothing but the committed objects it is handed, and it
refuses anything that is not an exact, lawful reviewer-visible case - so it
cannot carry withheld authoring material, structural provenance support, a
default, a tally or any derived figure into the packet. The packet is
transient: it lives outside the repository, and its SHA-256 is what the
session record carries.
"""

import hashlib
import json
import subprocess

import test_w8_discriminating_instrument_envelope as envelope

PACKET_SCHEMA = "w8-review-packet-v1"
REVIEW_QUESTION = (
    "on the admissible source evidence alone, does a recognised governed "
    "property differ between the paired variants in a way that changes a "
    "downstream obligation, permission, authority, treatment or state?")
TOKENS = ("governance_delta_present", "no_governance_delta",
          "review_inconclusive")
VARIANTS = ("variant_a", "variant_b")

HEADER = "\n".join((
    "W8 REVIEW PACKET (%s)" % PACKET_SCHEMA,
    "",
    "Review question:",
    REVIEW_QUESTION,
    "",
    "Each case is reviewed independently, on its two variants alone. All "
    "three lawful dispositions are available on every case."))
OPTIONS_LINE = "Options: " + " | ".join(TOKENS)
CASE_PREFIX = "==== CASE "
RESPONSE_PREFIX = "Disposition for "
STRUCTURAL_PREFIXES = ("---- BEGIN ", "---- END ", CASE_PREFIX,
                       RESPONSE_PREFIX)
WITHHELD_FIELDS = envelope.AUTHORING_FIELDS - envelope.REVIEW_FIELDS


class PacketRefusal(ValueError):
    """The input is not renderable into a lawful session packet."""


def case_header(case_id):
    return "%s%s ====" % (CASE_PREFIX, case_id)


def begin_marker(label):
    return "---- BEGIN %s ----" % label


def end_marker(label):
    return "---- END %s ----" % label


def response_line(case_id):
    return "%s%s:" % (RESPONSE_PREFIX, case_id)


def committed_object_bytes(repo, commit, rel):
    """The committed blob bytes at commit:rel - never a working-tree copy."""
    sha = subprocess.run(["git", "rev-parse", "--verify", commit + "^{commit}"],
                         cwd=repo, capture_output=True, text=True,
                         check=True).stdout.strip()
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (sha, rel)],
                          cwd=repo, capture_output=True, check=True).stdout


def load_review_case(raw):
    try:
        obj = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        raise PacketRefusal("input is not JSON")
    if not isinstance(obj, dict):
        raise PacketRefusal("input is not one JSON object")
    if obj.get("schema") == envelope.AUTHORING_SCHEMA or \
            set(obj) & WITHHELD_FIELDS:
        raise PacketRefusal("withheld authoring material is never renderable")
    violations = envelope.review_case_violations(obj)
    if violations:
        raise PacketRefusal("not a lawful reviewer-visible case: %s"
                            % "; ".join(violations))
    if raw != envelope.canonical_bytes(obj):
        raise PacketRefusal("input is not the exact canonical case bytes")
    for label in VARIANTS:
        for line in obj["admissible_source_evidence"][label].split("\n"):
            if line.startswith(STRUCTURAL_PREFIXES) or line == OPTIONS_LINE:
                raise PacketRefusal("a variant line would be read as packet "
                                    "structure")
    return obj


def render_packet(case_bytes):
    cases = [load_review_case(raw) for raw in case_bytes]
    if not cases:
        raise PacketRefusal("no case to render")
    ids = [c["case_id"] for c in cases]
    if len(set(ids)) != len(ids):
        raise PacketRefusal("duplicate case identity")
    blocks = [HEADER]
    for case in sorted(cases, key=lambda c: c["case_id"]):
        lines = [case_header(case["case_id"])]
        for label in VARIANTS:
            lines += [begin_marker(label),
                      case["admissible_source_evidence"][label],
                      end_marker(label)]
        lines += [OPTIONS_LINE, response_line(case["case_id"])]
        blocks.append("\n".join(lines))
    return ("\n\n".join(blocks) + "\n").encode("utf-8")


def render_packet_from_commit(repo, commit, rel_paths):
    return render_packet([committed_object_bytes(repo, commit, rel)
                          for rel in rel_paths])


def packet_sha256(packet):
    return "sha256:" + hashlib.sha256(packet).hexdigest()
