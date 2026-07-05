"""Crypto port: authenticated encryption and key derivation behind one interface.

Doctrine (per the encryption, selection, and key-architecture records):
an audited library through its highest-level safe interfaces;
authenticated encryption only; clean failure with no partial
plaintext; key material never logged, stored, or echoed. Key
derivation exists as of the key-architecture record: memory-hard,
named profiles only - the moderate profile is the v1 review-dated
provisional, and the product path selects no other. Derived keys,
passphrases, and salts pass through as arguments in the narrowest
scope; this module retains nothing.
"""

from typing import Protocol

import nacl.exceptions
import nacl.pwhash
import nacl.secret
import nacl.utils

KEY_SIZE = nacl.secret.SecretBox.KEY_SIZE  # 32
SALT_SIZE = nacl.pwhash.argon2id.SALTBYTES  # 16
# The v1 named profile (per the key-architecture record): the library's
# own moderate constants, never hand-tuned numbers.
KDF_MODERATE = ("moderate",
                nacl.pwhash.argon2id.OPSLIMIT_MODERATE,
                nacl.pwhash.argon2id.MEMLIMIT_MODERATE)


class CryptoPort(Protocol):
    IntegrityError: type[Exception]
    KDF_MODERATE: tuple

    def random_key(self) -> bytes: ...
    def random_salt(self) -> bytes: ...
    def encrypt(self, key: bytes, plaintext: bytes) -> bytes: ...
    def decrypt(self, key: bytes, blob: bytes) -> bytes: ...
    def derive_key(self, passphrase: bytes, salt: bytes,
                   opslimit: int, memlimit: int) -> bytes: ...


class PyNaClCrypto:
    """Authenticated secretbox encryption and memory-hard derivation."""

    IntegrityError = nacl.exceptions.CryptoError
    KDF_MODERATE = KDF_MODERATE

    def random_key(self) -> bytes:
        return nacl.utils.random(KEY_SIZE)

    def random_salt(self) -> bytes:
        return nacl.utils.random(SALT_SIZE)

    def encrypt(self, key: bytes, plaintext: bytes) -> bytes:
        return bytes(nacl.secret.SecretBox(key).encrypt(plaintext))

    def decrypt(self, key: bytes, blob: bytes) -> bytes:
        return nacl.secret.SecretBox(key).decrypt(blob)

    def derive_key(self, passphrase: bytes, salt: bytes,
                   opslimit: int, memlimit: int) -> bytes:
        return nacl.pwhash.argon2id.kdf(
            KEY_SIZE, passphrase, salt, opslimit=opslimit, memlimit=memlimit)
