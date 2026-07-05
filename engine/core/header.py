"""Versioned store header: magic(4) + version(2, big-endian) + reserved(10).

The reserved bytes are deliberate room (multi-device and format
evolution questions are open decisions); they must be zero in version
1 and are never interpreted. An unknown version or bad magic refuses
cleanly - format agility means user-side migration under user keys,
never guessing.
"""

MAGIC = b"WBWG"
VERSION = 1
_RESERVED = bytes(10)
HEADER_SIZE = 16


class HeaderError(ValueError):
    """The blob does not carry a well-formed, supported header."""


def build_header(version: int = VERSION) -> bytes:
    return MAGIC + version.to_bytes(2, "big") + _RESERVED


def parse_header(blob: bytes) -> int:
    """Return the version. Refuse anything unfamiliar, without guessing."""
    if len(blob) < HEADER_SIZE:
        raise HeaderError("blob shorter than a header")
    if blob[:4] != MAGIC:
        raise HeaderError("unrecognised store format")
    version = int.from_bytes(blob[4:6], "big")
    if version != VERSION:
        raise HeaderError(f"unsupported store version: {version}")
    return version
