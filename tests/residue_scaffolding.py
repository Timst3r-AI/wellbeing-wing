"""ADR 0035 residue-test scaffolding — utilities only.

Established at W5-D2-M01 with ZERO boundary operations registered, by
design. Later milestones (W5-D2-M04 through W5-D2-M07) register each
boundary operation that transiently holds governed plaintext here and
inherit the discipline: create synthetic content, run the operation,
terminate normally and by kill, then sweep. A boundary feature without
its residue tests does not merge (ADR 0035).

Sweep results report location and category only, never content.
"""

from pathlib import Path

# (operation_name, milestone_id) pairs — amended by record per
# milestone. Empty at W5-D2-M01 by design. W5-D2-M04 registers the
# processing-context lifecycle: the first boundary operation that
# transiently holds governed plaintext, carrying the full ADR 0035
# tax (create / run / terminate normally and by kill / sweep).
REGISTERED_BOUNDARY_OPERATIONS = (
    ("processing-context-lifecycle", "W5-D2-M04"),
)


def sweep_locations(root, marker):
    """Return relative paths of files under root containing marker bytes.

    Reports locations only — callers assert the list is empty; nothing
    here ever returns or prints the content it found (ADR 0004 / ADR
    0035: a residue test that prints residue is a leak with a test
    badge).
    """
    found = []
    for path in Path(root).rglob("*"):
        if path.is_file() and marker in path.read_bytes():
            found.append(path.relative_to(root).as_posix())
    return sorted(found)
