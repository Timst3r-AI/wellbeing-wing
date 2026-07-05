"""Intake: the import operation - boundary edge E1 as code.

Import stores bytes plus user-supplied provenance, nothing else, per
the import-boundary record. Inspection is capped at type verification
- magic-number / file-shape depth - because refusing a mistyped file
is integrity work, not reading. A refused import writes nothing.
Provenance is stored verbatim as the user supplied it, unvalidated
and unnormalised; absence of both source and date is stored inside
the sealed record as an explicit unprovenanced-by-user label, because
labelling is doctrine, not presentation. System facts are limited to
what requires no content reading: import timestamp (via the clock
port), byte size, and the verified type.

The size cap is a provisional v1 operational limit, not doctrine.
"""

from engine.core.record import encode_record
from engine.core.store import seal

MAX_IMPORT_BYTES = 25 * 1024 * 1024  # provisional v1 operational cap

_MAGIC_PREFIXES = {
    "pdf": b"%PDF-",
    "png": b"\x89PNG\r\n\x1a\n",
    "jpeg": b"\xff\xd8\xff",
}
# Shape check only: UTF-8 well-formedness; the decoded value is discarded.
_SHAPE_CHECKED = frozenset({"text", "markdown"})
ACCEPTED_TYPES = frozenset(_MAGIC_PREFIXES) | _SHAPE_CHECKED


class ImportRefused(Exception):
    """The import was refused and nothing was written.

    Messages are honest and non-blaming, and never echo file content.
    """


def verify_type(data: bytes, claimed_type: str) -> str:
    """Verify the bytes have the shape of the declared type. No deeper."""
    if claimed_type not in ACCEPTED_TYPES:
        raise ImportRefused(
            "import refused: the declared type is not one this version "
            "accepts (pdf, png, jpeg, text, markdown); nothing was stored")
    if claimed_type in _MAGIC_PREFIXES:
        if not data.startswith(_MAGIC_PREFIXES[claimed_type]):
            raise ImportRefused(
                f"import refused: the file does not have the shape of a "
                f"{claimed_type} file; nothing was stored")
    else:
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            raise ImportRefused(
                f"import refused: the file is not readable as "
                f"{claimed_type}; nothing was stored") from None
    return claimed_type


def import_record(storage, crypto, clock, key: bytes, data: bytes,
                  claimed_type: str, *, source: str | None = None,
                  date: str | None = None, note: str | None = None) -> None:
    """Verify, label, seal, store - or refuse and write nothing."""
    if len(data) > MAX_IMPORT_BYTES:
        raise ImportRefused(
            "import refused: the file is larger than this version can "
            "accept (25 MB); nothing was stored")
    verified = verify_type(data, claimed_type)
    provenance = {
        "user": {"source": source, "date": date, "note": note},
        "unprovenanced_by_user": source is None and date is None,
        "system": {
            "imported_at": clock.now_iso(),
            "byte_size": len(data),
            "verified_type": verified,
        },
    }
    seal(storage, crypto, key, encode_record(provenance, data))
