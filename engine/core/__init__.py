"""Pure doctrine core: no I/O, no clock, no library calls.

Everything here is decidable from bytes in, bytes out. Worldly
behaviour (cryptography, storage, time, the ledger) enters only
through the ports package.
"""

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
]
