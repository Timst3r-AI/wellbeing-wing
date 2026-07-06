"""Durable ledger store: the record of governance, sealed and kept.

Implements the durable-ledger doctrine record. The ledger is one
versioned file - magic WBWL - of independently sealed append frames:
each frame is a length-prefixed small ciphertext that decrypts to
exactly one ledger event. Frames seal under the master-key custody
boundary directly (a ledger-purpose subkey remains a future-record
option). Ledger content is governance metadata - identifiers,
vocabulary, timestamps, counts - privacy-sensitive by pattern, which
is why nothing here is ever readable at rest.

Doctrine held by construction and by test:

- **Append-only.** Frames are appended, never rewritten; prior bytes
  are byte-identical after every append. History is not edited.
- **Torn-tail honesty.** Appends are not atomic on this platform; a
  crash may tear the final frame. Reading returns every intact event
  in append order plus an explicit torn-tail signal - the tail is
  refused and never parsed, and intact history is never held hostage.
  The blast radius is one event.
- **Erasure is the user's knowing act.** erase_ledger removes the
  whole ledger file and nothing else, only when called; erasing a
  profile item never touches this file, and nothing erases it as a
  side effect. Copies the user has taken are the user's own.
- **The writer is caller-side.** Transition appliers stay pure and
  never see this module; they emit, callers keep. The writer accepts
  the existing data-only event shape and nothing else - what may not
  be emitted may never be stored.

v1 scope is the events that exist today (emitted transition events);
import/custody event emission is a named future extension, not built
here. Backup/export mechanics belong to a later deliverable; this
module only produces the sealed file that will one day travel.
"""

import json

from engine.core.profile import LedgerEvent

LEDGER_MAGIC = b"WBWL"
LEDGER_VERSION = 1
_RESERVED = bytes(10)
LEDGER_HEADER_SIZE = 16
_FRAME_LEN_SIZE = 4


class LedgerError(ValueError):
    """The ledger could not be written, read, or opened. Messages are
    content-free: they never contain event data or key material."""


def _header() -> bytes:
    return LEDGER_MAGIC + LEDGER_VERSION.to_bytes(2, "big") + _RESERVED


def _check_header(blob: bytes) -> None:
    if len(blob) < LEDGER_HEADER_SIZE:
        raise LedgerError("ledger shorter than its header")
    if blob[:4] != LEDGER_MAGIC:
        raise LedgerError("unrecognised ledger format")
    version = int.from_bytes(blob[4:6], "big")
    if version != LEDGER_VERSION:
        raise LedgerError(f"unsupported ledger version: {version}")


def append_event(storage, crypto, key: bytes, event) -> None:
    """Seal one event as its own frame and append it. Never rewrites."""
    if not isinstance(event, LedgerEvent):
        raise LedgerError("the ledger accepts ledger events only")
    if not storage.exists():
        storage.write_blob(_header())
    else:
        _check_header(storage.read_blob())
    payload = json.dumps(
        {"kind": event.kind, "refs": list(event.refs),
         "recorded_at": event.recorded_at},
        sort_keys=True, separators=(",", ":")).encode("utf-8")
    frame = crypto.encrypt(key, payload)
    storage.append_blob(
        len(frame).to_bytes(_FRAME_LEN_SIZE, "big") + frame)


def read_events(storage, crypto, key: bytes):
    """Open the ledger: every intact event in append order, plus an
    explicit torn-tail signal.

    Returns (events, tail_intact). A torn tail is refused and never
    parsed; intact prior history is always returned. A frame that
    fails authentication raises - wrong key or tampering is not a
    torn tail and is never silently skipped.
    """
    blob = storage.read_blob()
    _check_header(blob)
    events = []
    at = LEDGER_HEADER_SIZE
    tail_intact = True
    while at < len(blob):
        if at + _FRAME_LEN_SIZE > len(blob):
            tail_intact = False
            break
        frame_len = int.from_bytes(blob[at:at + _FRAME_LEN_SIZE], "big")
        at += _FRAME_LEN_SIZE
        if at + frame_len > len(blob):
            tail_intact = False
            break
        sealed = blob[at:at + frame_len]
        at += frame_len
        try:
            payload = crypto.decrypt(key, sealed)
        except crypto.IntegrityError:
            raise LedgerError(
                "ledger frame could not be opened (wrong key, tampering, "
                "or damage)") from None
        try:
            data = json.loads(payload.decode("utf-8"))
            events.append(LedgerEvent(data["kind"], data["refs"],
                                      data["recorded_at"]))
        except (UnicodeDecodeError, ValueError, KeyError, TypeError):
            raise LedgerError("ledger frame payload is not readable") from None
    return tuple(events), tail_intact


def erase_ledger(storage) -> None:
    """Whole-ledger erasure: the user's explicit, knowing act.

    Removes the ledger file and nothing else. Nothing calls this as
    a side effect of anything.
    """
    storage.erase()
