"""Export as a right (W3-D6 M2): the user's own bytes, theirs to take.

Single-record plaintext export at the data layer - a right, not a
transition: no user-act machinery, no review or approval machinery,
no gate but the owner's act of calling it. The bytes that entered at
import leave byte-identical; the user's own provenance is always
returned as structured data, and is written as a legible JSON sidecar
**only when a provenance destination is explicitly supplied - never
silently**. The policy governs what the engine leaves behind, never
what the user takes (the residue record's own rule).

Refusals, all write-free and content-free, with every destination
validated before any write: an existing payload or provenance
destination refuses before either file is written; a wrong key
refuses through the store's standing integrity refusal; foreign
formats (envelope, ledger, backup) refuse at the header; and
profile-class records refuse - this operation exports evidence
records only, and profile export is deferred to its own future
governed path. No whole-vault export, no batch export, no discovery:
one record, named by its owner, out.
"""

import json

from engine.core.record import decode_record
from engine.core.store import unseal


class ExportError(ValueError):
    """The export was refused; nothing was written. Messages never
    contain record content or key material."""


def export_record(record_storage, crypto, key: bytes, destination,
                  provenance_destination=None):
    """Export one evidence record's payload to the destination.

    Returns {"provenance": ...} always; writes the provenance sidecar
    only when provenance_destination is explicitly supplied. All
    destinations are validated before any write.
    """
    if destination.exists():
        raise ExportError(
            "the export destination already exists; nothing was written")
    if provenance_destination is not None and provenance_destination.exists():
        raise ExportError(
            "the provenance destination already exists; nothing was written")
    provenance, payload = decode_record(unseal(record_storage, crypto, key))
    if isinstance(provenance, dict) and "record_class" in provenance:
        raise ExportError(
            "this record class exports through its own future path; "
            "nothing was written")
    destination.write_blob(payload)
    if provenance_destination is not None:
        provenance_destination.write_blob(
            json.dumps(provenance, sort_keys=True,
                       indent=2).encode("utf-8"))
    return {"provenance": provenance}
