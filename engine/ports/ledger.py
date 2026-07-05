"""Ledger port: append-only, content-free governance events.

Doctrine: ledger entries reference categories, identifiers, and
counts - never contents (the record of governance must never become
a behavioural dataset, and must never hold plaintext). Milestone 1
ships the interface and an in-memory stand-in for tests; durable
ledger storage arrives with the milestone that needs it.
"""

from typing import Protocol


class LedgerPort(Protocol):
    def append(self, event: dict) -> None: ...


class MemoryLedger:
    """Test stand-in: append-only list, no persistence, no processing."""

    def __init__(self) -> None:
        self.events: list[dict] = []

    def append(self, event: dict) -> None:
        self.events.append(dict(event))
