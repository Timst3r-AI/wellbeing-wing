"""Custody: the two-layer wrap, per the key-architecture record.

Records are sealed under a random master key; the passphrase-derived
key seals only the master, inside the versioned key envelope. The
product path selects only the moderate named profile; opening honours
whatever parameters the envelope records. Passphrase change re-seals
the one small envelope with a fresh salt - no record is ever touched
by a custody event.

There is no recovery path here and none may ever be added: no
keyfile, no escrow, no recovery service, no secret questions, no
cloud recovery. A lost passphrase leaves the master unreachable and
the vault unrecoverable, exactly as the published key-loss wording
promises.

Passphrases, derived keys, and the master pass through the narrowest
possible scopes; nothing here retains, logs, or emits any of them.
The language-level honest residual (in-memory copies until
collection) is the runtime-selection record's documented caveat.
"""

from engine.core.envelope import decode_envelope, encode_envelope


class CustodyError(Exception):
    """The vault key could not be created or unlocked.

    The message never contains passphrase, key material, or content.
    """


def create_vault_key(storage, crypto, passphrase: bytes) -> bytes:
    """Create the sealed key envelope and return the new master key.

    Writes exactly one file. Refuses to overwrite an existing envelope:
    replacing an envelope would orphan every record sealed under its
    master, and destruction of access is never a silent side effect.
    """
    if storage.exists():
        raise CustodyError(
            "an envelope already exists at this location; nothing was written")
    profile, opslimit, memlimit = crypto.KDF_MODERATE
    salt = crypto.random_salt()
    kek = crypto.derive_key(passphrase, salt, opslimit, memlimit)
    master = crypto.random_key()
    storage.write_blob(encode_envelope(
        profile, opslimit, memlimit, salt, crypto.encrypt(kek, master)))
    return master


def unlock(storage, crypto, passphrase: bytes) -> bytes:
    """Open the envelope with the passphrase and return the master key.

    Honours the parameters the envelope records. Writes nothing.
    Fails clean, never partial.
    """
    envelope = decode_envelope(storage.read_blob())
    kek = crypto.derive_key(
        passphrase, envelope["salt"],
        envelope["opslimit"], envelope["memlimit"])
    try:
        return crypto.decrypt(kek, envelope["sealed_master"])
    except crypto.IntegrityError:
        raise CustodyError(
            "vault could not be unlocked (wrong passphrase, tampering, or damage)"
        ) from None


def change_passphrase(storage, crypto,
                      old_passphrase: bytes, new_passphrase: bytes) -> None:
    """Re-seal the envelope under the new passphrase. Records untouched.

    Fresh salt, fresh derivation, same master; rewrites only the one
    envelope file. A wrong old passphrase fails clean and writes nothing.
    """
    master = unlock(storage, crypto, old_passphrase)
    profile, opslimit, memlimit = crypto.KDF_MODERATE
    salt = crypto.random_salt()
    kek = crypto.derive_key(new_passphrase, salt, opslimit, memlimit)
    storage.write_blob(encode_envelope(
        profile, opslimit, memlimit, salt, crypto.encrypt(kek, master)))
