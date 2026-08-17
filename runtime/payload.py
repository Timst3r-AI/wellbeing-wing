"""Wellbeing Wing runtime payload assembly and equality (W5-D2-M05).

ADR 0031 made real: a payload is a derived object whose permitted
content is fully determined by the grant — the granted scope is the
whole payload, with no residue, no envelope, no accompanying context,
and no "and also". Assembly happens only inside a live processing
context (the user-initiated granted operation), from the context's
grant-bound holdings and from nowhere else; there is no parameter by
which anything extra could enter.

ADR 0036's cascade obligations are carried at the door: assembly
refuses invalidated inputs by their content-free section references,
every payload records its grant lineage at creation, and no API
exists that deletes user-owned material or derives a payload from a
payload (no re-derivation laundering).

Equality is ADR 0031's governed canonical comparison: deterministic
canonical serialisation, byte-level identity at the last controllable
point, and content-free fingerprints under the five recorded
conditions. Similarity never suffices; unproven refuses the
dependent operation; a refusal is never resolved by narrowing the
proof.

No transmission, no crossing, no recipient, and no model exists here:
Z4 remains dormant, the Z4 limb of the payload-equality obligation
remains visibly pending, and nothing in this module claims it
discharged. No file, network, clock, or logging facility is used.
"""

import hashlib
import json
import uuid
from dataclasses import dataclass

from runtime.context import ProcessingContext


class PayloadRefused(Exception):
    """Content-free refusal: a fixed reason code, never held content."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


@dataclass(frozen=True)
class Payload:
    """One grant's whole payload: exact scope plus governed metadata
    (the ADR 0031 A4 categories), with grant lineage recorded at
    creation. No field exists for device identity, history, room
    state, or any A3 category."""

    payload_id: str
    grant_id: str
    predecessor_grant_id: str
    edge: str
    domain: str
    recipient_class: str
    zones: tuple
    plaintext_flag: bool
    vendor_involvement: str
    purpose: str
    operation: str
    sections: tuple  # ((section_name, content_bytes), ...) sorted
    freshness_labels: tuple  # ((section_name, label_name), ...) governed


@dataclass(frozen=True)
class ComparisonRecord:
    """A content-free comparison outcome under ADR 0031 B4's five
    conditions: fingerprints only, no reconstruction, C0 use."""

    comparison: str
    outcome: bool
    fingerprint_a: str
    fingerprint_b: str


def assemble_payload(context, invalidated_refs=(), freshness_labels=()):
    """The only assembly door. Builds one payload from one live
    processing context's grant-bound holdings — the granted scope is
    the whole payload, proven at the door, and invalidated inputs are
    refused by reference (ADR 0036)."""
    if not isinstance(context, ProcessingContext):
        raise PayloadRefused("no_context_no_payload")
    if context.ended:
        raise PayloadRefused("context_ended")
    holdings = context.post_context_state()
    if not holdings:
        raise PayloadRefused("nothing_held_to_assemble")
    names = [item.section for item in holdings]
    if len(names) != len(set(names)):
        raise PayloadRefused("duplicate_section")
    invalidated = frozenset(invalidated_refs)
    for name in names:
        if name in invalidated:
            raise PayloadRefused("invalidated_input")
    if set(names) != set(context.grant.scope):
        raise PayloadRefused("payload_scope_mismatch")
    for section, _label in freshness_labels:
        if section not in names:
            raise PayloadRefused("label_outside_payload")
    grant = context.grant
    return Payload(
        payload_id=str(uuid.uuid4()),
        grant_id=grant.grant_id,
        predecessor_grant_id=grant.predecessor_id or "",
        edge=grant.edge,
        domain=context.domain,
        recipient_class=grant.recipient_class,
        zones=tuple(grant.zones),
        plaintext_flag=grant.plaintext_flag,
        vendor_involvement=grant.vendor_involvement,
        purpose=grant.purpose,
        operation=grant.operation,
        sections=tuple(sorted((item.section, item.content)
                              for item in holdings)),
        freshness_labels=tuple(sorted(freshness_labels)))


def serialise_payload(payload):
    """The governed canonical form: deterministic, sorted, explicit.
    Two serialisations of the same payload are byte-identical, and
    the serialised bytes are what byte-level equality compares at the
    last controllable point (ADR 0031 decision 19)."""
    body = {
        "grant_id": payload.grant_id,
        "predecessor_grant_id": payload.predecessor_grant_id,
        "edge": payload.edge,
        "domain": payload.domain,
        "recipient_class": payload.recipient_class,
        "zones": list(payload.zones),
        "plaintext_flag": payload.plaintext_flag,
        "vendor_involvement": payload.vendor_involvement,
        "purpose": payload.purpose,
        "operation": payload.operation,
        "sections": [[name, content.hex()]
                     for name, content in payload.sections],
        "freshness_labels": [list(pair)
                             for pair in payload.freshness_labels],
    }
    return json.dumps(body, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def payload_fingerprint(serialised):
    """Content-free by construction: a fixed-length digest that
    reveals nothing and reconstructs nothing."""
    return hashlib.sha256(serialised).hexdigest()


def compare_scope_to_payload(grant, payload):
    """Comparison one: what was authorised is what was built."""
    outcome = (set(name for name, _ in payload.sections)
               == set(grant.scope)
               and payload.grant_id == grant.grant_id)
    return ComparisonRecord(
        comparison="grant-scope-to-assembled-payload", outcome=outcome,
        fingerprint_a=payload_fingerprint(
            json.dumps(sorted(grant.scope)).encode("utf-8")),
        fingerprint_b=payload_fingerprint(serialise_payload(payload)))


def compare_at_last_controllable_point(payload, presented_bytes):
    """Comparison two: nothing was added between assembly and the
    last point at which the Wing can observe and refuse. Byte-level."""
    ours = serialise_payload(payload)
    return ComparisonRecord(
        comparison="assembled-to-last-controllable-point",
        outcome=ours == presented_bytes,
        fingerprint_a=payload_fingerprint(ours),
        fingerprint_b=payload_fingerprint(presented_bytes))


def compare_across_transformation(before_bytes, after_bytes):
    """Comparison three: wherever a transformation exists, it
    preserved scope and added nothing. Byte-level identity of the
    governed canonical form; representation differences are ignored
    only where the canonical form already says they are irrelevant,
    never by runtime discretion."""
    return ComparisonRecord(
        comparison="pre-to-post-transformation",
        outcome=before_bytes == after_bytes,
        fingerprint_a=payload_fingerprint(before_bytes),
        fingerprint_b=payload_fingerprint(after_bytes))


def require_equal(record):
    """Unproven is not presumed-equal: a failed or absent comparison
    refuses the dependent operation, content-free, and the refusal is
    never resolved by narrowing the proof."""
    if not isinstance(record, ComparisonRecord) or not record.outcome:
        raise PayloadRefused("equality_unproven")
    return record
