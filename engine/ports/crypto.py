"""Crypto port: authenticated encryption behind an interface.

Doctrine (per the encryption and selection records): an audited
library through its highest-level safe interfaces; authenticated
encryption only; clean failure with no partial plaintext; key
material never logged, stored, or echoed. Key derivation, custody,
and persistence do not exist in this milestone by decision -
callers supply raw keys and own their lifetime.
"""

from typing import Protocol

import nacl.exceptions
import nacl.secret
import nacl.utils

KEY_SIZE = nacl.secret.SecretBox.KEY_SIZE  # 32


class CryptoPort(Protocol):
    IntegrityError: type[Exception]

    def random_key(self) -> bytes: ...
    def encrypt(self, key: bytes, plaintext: bytes) -> bytes: ...
    def decrypt(self, key: bytes, blob: bytes) -> bytes: ...


class PyNaClCrypto:
    """Authenticated secretbox encryption via the audited binding."""

    IntegrityError = nacl.exceptions.CryptoError

    def random_key(self) -> bytes:
        return nacl.utils.random(KEY_SIZE)

    def encrypt(self, key: bytes, plaintext: bytes) -> bytes:
        return bytes(nacl.secret.SecretBox(key).encrypt(plaintext))

    def decrypt(self, key: bytes, blob: bytes) -> bytes:
        return nacl.secret.SecretBox(key).decrypt(blob)
