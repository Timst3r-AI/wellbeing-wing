"""Backup container: the vault's promises, taught to travel (W3-D6 M1).

One portable ciphertext file, per the backup-guidance record, in the
ruled WBWB shape:

1. a minimal public header carrying no vault information;
2. the reachable encrypted key envelope (the same WBWK ciphertext
   that rests beside the vault - reachable because restore must
   derive the master from it before anything else can open; never
   trapped inside the payload it unlocks);
3. the sealed payload, authenticated under the restored master key,
   holding the manifest, member structure, sealed records, and the
   durable ledger. No record names, cardinality, manifest, or
   structure appears outside the sealed payload; the travelling file
   tells nothing beyond "a backup of some vault, this format, this
   derivation cost."

Restore is symmetric and user-performed: file plus passphrase, into
an empty target only - no merge, no overwrite. Validation strictly
precedes writing: magic/version, envelope unwrap (reusing the
published custody path through a bytes-backed shim, so wrong-
passphrase refusal never forks), payload authentication, structural
manifest validation - and only then are members written, as the
sealed bytes they are. **No health-record plaintext is decrypted in
the restore path**; sealed records move verbatim.

The member set is caller-supplied, always: the engine is headless
and never crawls, guesses, or discovers files. A complete vault unit
of this era includes the key envelope, the sealed records, and the
durable ledger - when the caller identifies them. Ciphertext
travels; keys never; a backup file plus no passphrase is nothing.
"""

import json

from engine.core.custody import unlock
from engine.core.envelope import decode_envelope

BACKUP_MAGIC = b"WBWB"
BACKUP_VERSION = 1
_RESERVED = bytes(10)
_HEADER_SIZE = 16
_LEN_SIZE = 4
BACKUP_PAYLOAD_VERSION = 1
MEMBER_KINDS = frozenset({"record", "ledger"})


class BackupError(ValueError):
    """The backup could not be exported or restored. Messages are
    content-free: never member names, contents, or key material."""


class _BytesStorage:
    """Bytes-backed read-only shim so restore reuses published unlock."""

    def __init__(self, blob: bytes) -> None:
        self._blob = blob

    def read_blob(self) -> bytes:
        return self._blob

    def exists(self) -> bool:
        return True


def _plain_name(name) -> bool:
    return (isinstance(name, str) and bool(name)
            and "/" not in name and "\\" not in name
            and name not in (".", "..") and "\x00" not in name)


def export_backup(destination, crypto, key: bytes, envelope_storage,
                  members, envelope_name: str = "key.envelope") -> None:
    """Assemble one portable ciphertext backup file.

    members: caller-supplied sequence of (name, kind, storage) -
    kinds are 'record' or 'ledger'. Nothing is discovered; nothing
    is read beyond what the caller identifies. Sources are read,
    never modified.
    """
    envelope_bytes = envelope_storage.read_blob()
    decode_envelope(envelope_bytes)  # sanity: a real key envelope
    if not _plain_name(envelope_name):
        raise BackupError("the envelope name must be a plain file name")
    seen = {envelope_name}
    entries = []
    blobs = []
    for name, kind, storage in members:
        if not _plain_name(name):
            raise BackupError("every member requires a plain file name")
        if name in seen:
            raise BackupError("member names must be unique")
        if kind not in MEMBER_KINDS:
            raise BackupError("unknown member kind")
        seen.add(name)
        blob = storage.read_blob()
        entries.append({"name": name, "kind": kind, "size": len(blob)})
        blobs.append(blob)
    manifest = json.dumps(
        {"backup_payload_version": BACKUP_PAYLOAD_VERSION,
         "envelope_name": envelope_name, "members": entries},
        sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload = (len(manifest).to_bytes(_LEN_SIZE, "big") + manifest
               + b"".join(blobs))
    sealed = crypto.encrypt(key, payload)
    destination.write_blob(
        BACKUP_MAGIC + BACKUP_VERSION.to_bytes(2, "big") + _RESERVED
        + len(envelope_bytes).to_bytes(_LEN_SIZE, "big") + envelope_bytes
        + sealed)


def restore_backup(backup_storage, crypto, passphrase: bytes, target):
    """Restore a backup into an empty target: file plus passphrase, done.

    The ruled validation order, writes only after every step succeeds:
    (1) magic/version; (2) envelope unwrap with the passphrase (the
    wrong-passphrase refusal lives in the published custody path and
    propagates content-free); (3) payload authentication under the
    restored master; (4) structural manifest validation; (5) writes.
    Sealed members are written verbatim - nothing is decrypted to
    restore beyond the payload authentication itself.
    """
    blob = backup_storage.read_blob()
    if len(blob) < _HEADER_SIZE + _LEN_SIZE:
        raise BackupError("backup shorter than its header")
    if blob[:4] != BACKUP_MAGIC:
        raise BackupError("unrecognised backup format")
    version = int.from_bytes(blob[4:6], "big")
    if version != BACKUP_VERSION:
        raise BackupError(f"unsupported backup version: {version}")
    if not target.is_empty():
        raise BackupError("restore requires an empty target; "
                          "nothing was written")
    at = _HEADER_SIZE
    envelope_len = int.from_bytes(blob[at:at + _LEN_SIZE], "big")
    at += _LEN_SIZE
    if len(blob) < at + envelope_len:
        raise BackupError("backup truncated inside its key envelope")
    envelope_bytes = blob[at:at + envelope_len]
    at += envelope_len
    sealed = blob[at:]
    if not sealed:
        raise BackupError("backup carries no sealed payload")
    master = unlock(_BytesStorage(envelope_bytes), crypto, passphrase)
    try:
        payload = crypto.decrypt(master, sealed)
    except crypto.IntegrityError:
        raise BackupError(
            "backup payload could not be authenticated (wrong key, "
            "tampering, or damage)") from None
    if len(payload) < _LEN_SIZE:
        raise BackupError("backup payload is not readable")
    manifest_len = int.from_bytes(payload[:_LEN_SIZE], "big")
    if len(payload) < _LEN_SIZE + manifest_len:
        raise BackupError("backup payload truncated inside its manifest")
    try:
        manifest = json.loads(
            payload[_LEN_SIZE:_LEN_SIZE + manifest_len].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise BackupError("backup manifest is not readable") from None
    if manifest.get("backup_payload_version") != BACKUP_PAYLOAD_VERSION:
        raise BackupError("unsupported backup payload version")
    envelope_name = manifest.get("envelope_name")
    entries = manifest.get("members")
    if not _plain_name(envelope_name) or not isinstance(entries, list):
        raise BackupError("backup manifest is structurally invalid")
    at = _LEN_SIZE + manifest_len
    seen = {envelope_name}
    slices = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise BackupError("backup manifest is structurally invalid")
        name = entry.get("name")
        kind = entry.get("kind")
        size = entry.get("size")
        if (not _plain_name(name) or name in seen
                or kind not in MEMBER_KINDS
                or not isinstance(size, int) or size < 0):
            raise BackupError("backup manifest is structurally invalid")
        seen.add(name)
        if at + size > len(payload):
            raise BackupError("backup payload truncated inside its members")
        slices.append((name, payload[at:at + size]))
        at += size
    if at != len(payload):
        raise BackupError(
            "backup payload length does not match its manifest")
    target.child(envelope_name).write_blob(envelope_bytes)
    for name, data in slices:
        target.child(name).write_blob(data)
    return {"members": len(slices)}
