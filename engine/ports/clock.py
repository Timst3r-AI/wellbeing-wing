"""Clock port: time enters the engine only through this interface.

Staleness decay (a later milestone) must be deterministically
testable; an injected clock is what makes label decay provable in
milliseconds instead of months. Milestone 1 ships the interface and
the trivial system implementation only.
"""

from datetime import datetime, timezone
from typing import Protocol


class ClockPort(Protocol):
    def now_iso(self) -> str: ...


class SystemClock:
    def now_iso(self) -> str:
        return datetime.now(timezone.utc).isoformat()
