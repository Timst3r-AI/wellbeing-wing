"""Storage port: whole-blob persistence behind an interface.

Milestone 1 stores a single sealed blob; the envelope question
(per-record vs whole-store) is an open decision, and this seam is
where its answer will land without touching the doctrine core.
Residue doctrine binds: this module writes exactly the one intended
file and nothing else - no temp files, no caches, no logs.
"""

from pathlib import Path
from typing import Protocol


class StoragePort(Protocol):
    def write_blob(self, blob: bytes) -> None: ...
    def read_blob(self) -> bytes: ...
    def exists(self) -> bool: ...


class FileStorage:
    """One sealed blob at one caller-chosen path. Nothing else, ever."""

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    def write_blob(self, blob: bytes) -> None:
        self._path.write_bytes(blob)

    def read_blob(self) -> bytes:
        return self._path.read_bytes()

    def exists(self) -> bool:
        return self._path.exists()
