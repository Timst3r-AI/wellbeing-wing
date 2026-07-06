"""Pure doctrine core: no I/O, no clock, no library calls.

Everything here is decidable from bytes in, bytes out. Worldly
behaviour (cryptography, storage, time, the ledger) enters only
through the ports package.
"""

from engine.core.custody import (
    CustodyError,
    change_passphrase,
    create_vault_key,
    unlock,
)
from engine.core.envelope import (
    ENVELOPE_VERSION,
    EnvelopeError,
    decode_envelope,
    encode_envelope,
)
from engine.core.header import (
    HEADER_SIZE,
    HeaderError,
    build_header,
    parse_header,
)
from engine.core.intake import (
    ACCEPTED_TYPES,
    MAX_IMPORT_BYTES,
    ImportRefused,
    import_record,
    verify_type,
)
from engine.core.profile import (
    AGENT_ASSIGNABLE_LABELS,
    AUTHORITY_LABELS,
    PROVENANCE_KINDS,
    STALENESS_DECAY_ORDER,
    STALENESS_LABELS,
    TRUTH_LABELS,
    BoundedUnknown,
    Contradiction,
    LedgerEvent,
    ProfileItem,
    ProfileModelError,
    ProvenanceRef,
    Supersession,
    staleness_of,
)
from engine.core.record import (
    RECORD_VERSION,
    RecordError,
    decode_record,
    encode_record,
)
from engine.core.store import StoreIntegrityError, seal, unseal

__all__ = [
    "HEADER_SIZE",
    "HeaderError",
    "build_header",
    "parse_header",
    "StoreIntegrityError",
    "seal",
    "unseal",
    "RECORD_VERSION",
    "RecordError",
    "encode_record",
    "decode_record",
    "ACCEPTED_TYPES",
    "MAX_IMPORT_BYTES",
    "ImportRefused",
    "import_record",
    "verify_type",
    "ENVELOPE_VERSION",
    "EnvelopeError",
    "encode_envelope",
    "decode_envelope",
    "CustodyError",
    "create_vault_key",
    "unlock",
    "change_passphrase",
    "AUTHORITY_LABELS",
    "AGENT_ASSIGNABLE_LABELS",
    "TRUTH_LABELS",
    "STALENESS_LABELS",
    "STALENESS_DECAY_ORDER",
    "PROVENANCE_KINDS",
    "ProfileModelError",
    "ProfileItem",
    "ProvenanceRef",
    "BoundedUnknown",
    "Contradiction",
    "Supersession",
    "LedgerEvent",
    "staleness_of",
]
