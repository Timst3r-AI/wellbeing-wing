"""Key envelope: the second versioned format, per the key-architecture record.

The envelope is one small file holding everything needed to re-derive
the key-encryption key and open the sealed master: profile name,
resolved derivation parameters, per-vault salt (not a secret, stored
in the clear per standard practice), and the master key sealed under
the passphrase-derived key. It lives in its own file beside the
records, never inside a record header - key custody and record
content are different subjects and stay structurally separate.

The encoding is parameter-agnostic by design: opening honours the
parameters the envelope records, so profile changes are versioned
migrations, never breaks. Which parameters may be *selected* is the
product path's doctrine, not this format's.

Layout, version 1:
    magic            4 bytes
    envelope version 2 bytes, big-endian
    profile name     1-byte length + UTF-8 bytes
    opslimit         4 bytes, big-endian
    memlimit         8 bytes, big-endian
    salt             1-byte length + bytes
    sealed master    4-byte length + bytes

No I/O, no clock, no library calls: bytes and structure only.
"""

ENVELOPE_MAGIC = b"WBWK"
ENVELOPE_VERSION = 1
_MIN_SIZE = 4 + 2 + 1 + 4 + 8 + 1 + 4


class EnvelopeError(ValueError):
    """The bytes do not form a readable envelope of a known version."""


def encode_envelope(profile: str, opslimit: int, memlimit: int,
                    salt: bytes, sealed_master: bytes) -> bytes:
    name = profile.encode("utf-8")
    return (ENVELOPE_MAGIC
            + ENVELOPE_VERSION.to_bytes(2, "big")
            + len(name).to_bytes(1, "big") + name
            + opslimit.to_bytes(4, "big")
            + memlimit.to_bytes(8, "big")
            + len(salt).to_bytes(1, "big") + salt
            + len(sealed_master).to_bytes(4, "big") + sealed_master)


def decode_envelope(blob: bytes) -> dict:
    if len(blob) < _MIN_SIZE:
        raise EnvelopeError("envelope shorter than its fixed fields")
    if blob[:4] != ENVELOPE_MAGIC:
        raise EnvelopeError("unrecognised envelope format")
    version = int.from_bytes(blob[4:6], "big")
    if version != ENVELOPE_VERSION:
        raise EnvelopeError(f"unsupported envelope version: {version}")
    at = 6
    name_len = blob[at]
    at += 1
    if len(blob) < at + name_len + 4 + 8 + 1:
        raise EnvelopeError("envelope truncated inside its profile name")
    try:
        profile = blob[at:at + name_len].decode("utf-8")
    except UnicodeDecodeError:
        raise EnvelopeError("envelope profile name is not readable") from None
    at += name_len
    opslimit = int.from_bytes(blob[at:at + 4], "big")
    at += 4
    memlimit = int.from_bytes(blob[at:at + 8], "big")
    at += 8
    salt_len = blob[at]
    at += 1
    if len(blob) < at + salt_len + 4:
        raise EnvelopeError("envelope truncated inside its salt")
    salt = blob[at:at + salt_len]
    at += salt_len
    sealed_len = int.from_bytes(blob[at:at + 4], "big")
    at += 4
    if len(blob) != at + sealed_len:
        raise EnvelopeError("envelope length does not match its declared sizes")
    return {
        "profile": profile,
        "opslimit": opslimit,
        "memlimit": memlimit,
        "salt": salt,
        "sealed_master": blob[at:],
    }
