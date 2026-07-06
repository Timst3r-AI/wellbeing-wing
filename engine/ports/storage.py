"""Storage port: whole-blob persistence behind an interface.

Milestone 1 stores a single sealed blob; the envelope question
(per-record vs whole-store) is an open decision, and this seam is
where its answer will land without touching the doctrine core.
Residue doctrine binds: this module writes exactly the intended
file and nothing else - no temp files, no caches, no logs.

Extended under the durable-ledger doctrine (per its Tier J milestone
authorisation): append_blob exists for the ledger's independently
sealed frames - appending, never rewriting, so prior history is
never re-encrypted or re-written - and erase exists so that
whole-ledger erasure is an explicit, testable act rather than a
side effect. Appends are not atomic on this platform; the torn-tail
honesty for that lives in the ledger store's doctrine and tests.
"""

from pathlib import Path
from typing import Protocol


class StoragePort(Protocol):
    def write_blob(self, blob: bytes) -> None: ...
    def read_blob(self) -> bytes: ...
    def append_blob(self, blob: bytes) -> None: ...
    def erase(self) -> None: ...
    def exists(self) -> bool: ...


class FileStorage:
    """One sealed artifact at one caller-chosen path. Nothing else, ever."""

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    def write_blob(self, blob: bytes) -> None:
        self._path.write_bytes(blob)

    def read_blob(self) -> bytes:
        return self._path.read_bytes()

    def append_blob(self, blob: bytes) -> None:
        with open(self._path, "ab") as f:
            f.write(blob)

    def erase(self) -> None:
        self._path.unlink()

    def exists(self) -> bool:
        return self._path.exists()
