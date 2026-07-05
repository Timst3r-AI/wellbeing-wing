"""Ports: the engine's only doors to the world.

Crypto, storage, clock, and ledger live behind these interfaces so
the doctrine core stays pure and every worldly behaviour is swappable
and testable. Milestone 1 ships minimal implementations of crypto and
storage; clock and ledger are interfaces with trivial stand-ins,
present so the architecture is real from the first commit.
"""

from engine.ports.clock import ClockPort, SystemClock
from engine.ports.crypto import KEY_SIZE, CryptoPort, PyNaClCrypto
from engine.ports.ledger import LedgerPort, MemoryLedger
from engine.ports.storage import FileStorage, StoragePort

__all__ = [
    "KEY_SIZE",
    "CryptoPort",
    "PyNaClCrypto",
    "StoragePort",
    "FileStorage",
    "ClockPort",
    "SystemClock",
    "LedgerPort",
    "MemoryLedger",
]
