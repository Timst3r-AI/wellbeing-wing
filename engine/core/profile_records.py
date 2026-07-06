"""Profile record persistence: the shapes sealed, the grammar guarded both ways.

Profile items and bounded unknowns persist through the existing
sealed store path, unchanged: the same seal/unseal, the same inner
record encoding, caller-chosen paths, no layout, no naming, no index.
A profile record declares itself inside the record's provenance JSON
(record class and payload version); imported evidence records remain
exactly as published and carry no record class - evidence-by-absence
is the accepted v1 distinguishability rule, documented, not hidden.

Two guards define this module:

1. **No truth-label item persists.** Per the minimal-review-posture
   record, no review path exists, so no confirmed item can
   legitimately exist outside tests - the only profile write path
   refuses truth labels, writes nothing, and echoes nothing.
2. **Loading reconstructs through the object-model constructors**, so
   a sealed payload that decodes to an illegal state refuses at
   reconstruction: the grammar holds on the way out as well as the
   way in.

Content is str-only in this milestone by decision; contradiction,
supersession, and ledger-event persistence belong to the transition
deliverable that creates them. No format version 2, no transition
engine, no review or approval path, no extraction, no model contact,
no durable ledger.
"""

import json

from engine.core.profile import (
    TRUTH_LABELS,
    BoundedUnknown,
    ProfileItem,
    ProvenanceRef,
)
from engine.core.record import decode_record, encode_record
from engine.core.store import seal, unseal

PROFILE_PAYLOAD_VERSION = 1
RECORD_CLASSES = frozenset({"profile-item", "bounded-unknown"})

_ITEM_FIELDS = ("section", "content", "authority", "assigned_by",
                "staleness", "last_reviewed", "provenance")
_UNKNOWN_FIELDS = ("scope", "source_set", "as_of")


class ProfileRecordError(ValueError):
    """The shape may not persist, or the bytes are not a readable
    profile record of a known class and version. Messages never
    contain item content."""


def _sealed_payload(record_class, payload):
    provenance = {"record_class": record_class,
                  "profile_payload_version": PROFILE_PAYLOAD_VERSION}
    body = json.dumps(payload, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")
    return encode_record(provenance, body)


def _opened_payload(storage, crypto, key, expected_class):
    provenance, body = decode_record(unseal(storage, crypto, key))
    record_class = provenance.get("record_class")
    if record_class is None:
        raise ProfileRecordError(
            "not a profile record (no record class declared)")
    if record_class != expected_class:
        raise ProfileRecordError(
            f"record class {record_class!r} is not {expected_class!r}")
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ProfileRecordError(
            "profile payload is not readable") from None
    version = payload.get("profile_payload_version")
    if version != PROFILE_PAYLOAD_VERSION:
        raise ProfileRecordError(
            f"unsupported profile payload version: {version}")
    if payload.get("kind") != expected_class:
        raise ProfileRecordError(
            "profile payload kind does not match its record class")
    return payload


def _field(payload, name):
    if name not in payload:
        raise ProfileRecordError(f"profile payload missing field: {name}")
    return payload[name]


def persist_item(storage, crypto, key: bytes, item) -> None:
    """Seal one profile item at the caller's path. Refuses truth labels."""
    if not isinstance(item, ProfileItem):
        raise ProfileRecordError("persist_item takes a profile item")
    if item.authority in TRUTH_LABELS:
        raise ProfileRecordError(
            "a confirmed item cannot be persisted: no review path exists "
            "in this milestone; nothing was stored")
    if not isinstance(item.content, str):
        raise ProfileRecordError(
            "profile content persists as text only in this milestone; "
            "nothing was stored")
    provenance = None
    if item.provenance is not None:
        provenance = {"kind": item.provenance.kind,
                      "reference": item.provenance.reference,
                      "stated_at": item.provenance.stated_at}
    payload = {
        "profile_payload_version": PROFILE_PAYLOAD_VERSION,
        "kind": "profile-item",
        "section": item.section,
        "content": item.content,
        "authority": item.authority,
        "assigned_by": item.assigned_by,
        "staleness": item.staleness,
        "last_reviewed": item.last_reviewed,
        "provenance": provenance,
    }
    seal(storage, crypto, key, _sealed_payload("profile-item", payload))


def load_item(storage, crypto, key: bytes):
    """Open one profile item, reconstructed through the object model.

    An illegal persisted state refuses at reconstruction - the
    constructors are the gate on the way out too.
    """
    payload = _opened_payload(storage, crypto, key, "profile-item")
    fields = {name: _field(payload, name) for name in _ITEM_FIELDS}
    provenance = None
    if fields["provenance"] is not None:
        p = fields["provenance"]
        provenance = ProvenanceRef(p.get("kind"), p.get("reference"),
                                   p.get("stated_at"))
    return ProfileItem(fields["section"], fields["content"],
                       fields["authority"], fields["assigned_by"],
                       fields["staleness"],
                       last_reviewed=fields["last_reviewed"],
                       provenance=provenance)


def persist_unknown(storage, crypto, key: bytes, unknown) -> None:
    """Seal one bounded unknown at the caller's path."""
    if not isinstance(unknown, BoundedUnknown):
        raise ProfileRecordError("persist_unknown takes a bounded unknown")
    payload = {
        "profile_payload_version": PROFILE_PAYLOAD_VERSION,
        "kind": "bounded-unknown",
        "scope": unknown.scope,
        "source_set": list(unknown.source_set),
        "as_of": unknown.as_of,
    }
    seal(storage, crypto, key, _sealed_payload("bounded-unknown", payload))


def load_unknown(storage, crypto, key: bytes):
    """Open one bounded unknown, reconstructed through the object model."""
    payload = _opened_payload(storage, crypto, key, "bounded-unknown")
    fields = {name: _field(payload, name) for name in _UNKNOWN_FIELDS}
    return BoundedUnknown(fields["scope"], fields["source_set"],
                          fields["as_of"])
