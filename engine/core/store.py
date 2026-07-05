"""Store operations: seal and unseal, orchestrated over ports.

Key-handling doctrine (per the runtime-selection record): keys are
per-operation arguments held in the narrowest possible scope - no
object in this module retains a key, no key is ever written anywhere,
and this module contains no logging by design. The engine's honest
residual (language-level copies until collection) is documented in
the record that selected the stack; nothing here pretends otherwise.
"""

from engine.core.header import HEADER_SIZE, build_header, parse_header


class StoreIntegrityError(Exception):
    """The store could not be opened: wrong key, tampering, or damage.

    The message never contains key material or plaintext.
    """


def seal(storage, crypto, key: bytes, content: bytes) -> None:
    """Encrypt content under the caller's key and persist it whole."""
    blob = build_header() + crypto.encrypt(key, content)
    storage.write_blob(blob)


def unseal(storage, crypto, key: bytes) -> bytes:
    """Read, verify, and decrypt the store. Fails clean, never partial."""
    blob = storage.read_blob()
    parse_header(blob)
    try:
        return crypto.decrypt(key, blob[HEADER_SIZE:])
    except crypto.IntegrityError:
        raise StoreIntegrityError(
            "store could not be opened (wrong key, tampering, or damage)"
        ) from None
