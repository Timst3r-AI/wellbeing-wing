"""Inner record encoding: provenance and payload, versioned, whole.

A vault record is one sealed unit: the imported bytes exactly as
provided, plus the provenance that entered with them. This module
defines the plaintext layout that travels inside the sealed store -
versioned from record one, like the outer header, so the format can
grow without guessing. Encoding is deterministic; decoding refuses
unknown versions and malformed layouts cleanly.

Layout, version 1:
    record version   2 bytes, big-endian
    provenance size  4 bytes, big-endian
    provenance       UTF-8 JSON, sorted keys
    payload size     8 bytes, big-endian
    payload          the imported bytes, untouched

No I/O, no clock, no interpretation: bytes and structure only.
"""

import json

RECORD_VERSION = 1
_VERSION_SIZE = 2
_PROV_SIZE = 4
_PAYLOAD_SIZE = 8
_MIN_SIZE = _VERSION_SIZE + _PROV_SIZE + _PAYLOAD_SIZE


class RecordError(ValueError):
    """The bytes do not form a readable record of a known version."""


def encode_record(provenance: dict, payload: bytes) -> bytes:
    prov = json.dumps(
        provenance, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return (RECORD_VERSION.to_bytes(_VERSION_SIZE, "big")
            + len(prov).to_bytes(_PROV_SIZE, "big") + prov
            + len(payload).to_bytes(_PAYLOAD_SIZE, "big") + payload)


def decode_record(blob: bytes) -> tuple[dict, bytes]:
    if len(blob) < _MIN_SIZE:
        raise RecordError("record shorter than its fixed fields")
    version = int.from_bytes(blob[:_VERSION_SIZE], "big")
    if version != RECORD_VERSION:
        raise RecordError(f"unsupported record version: {version}")
    at = _VERSION_SIZE
    prov_size = int.from_bytes(blob[at:at + _PROV_SIZE], "big")
    at += _PROV_SIZE
    if len(blob) < at + prov_size + _PAYLOAD_SIZE:
        raise RecordError("record truncated inside its provenance")
    try:
        provenance = json.loads(blob[at:at + prov_size].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise RecordError("record provenance is not readable") from None
    at += prov_size
    payload_size = int.from_bytes(blob[at:at + _PAYLOAD_SIZE], "big")
    at += _PAYLOAD_SIZE
    if len(blob) != at + payload_size:
        raise RecordError("record length does not match its declared sizes")
    return provenance, blob[at:]
