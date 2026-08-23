"""W7-D5 — the pure authority-and-identity binding layer.

THIS MODULE NEVER WRITES, NEVER CONTACTS ANYTHING, AND NEVER ALLOCATES AN
IDENTIFIER BY ITSELF.

The frozen W7-D4 harness assembles a candidate record under one
`authorising_record` argument, which flows into both the record's top-level run
authority and every capture's `authoring_record`. Under the accepted W7-D5 brief
(v1.2, section 12) those are two different facts that must not stay collapsed:
the harness is invoked with `W7-D4-SHB`, the specimen-authoring authority the
exam itself declares, and this binder is the governed step that separates the
facts before canonical D5 bytes exist — it replaces ONLY the top-level run
authority with `W7-D5-SEB`, and refuses a candidate whose captures do not carry
`W7-D4-SHB`.

The binder MAY bind: the proposed `GER-####` record identity, the run identity,
the run's UTC `as_of` date, and the top-level `authorising_record`. It may then
serialise the exact canonical bytes: UTF-8, no BOM, LF, repository indentation
(one space per level, `ensure_ascii` off), final newline.

The binder MAY NOT: change a capture text, change a capture digest except by
refusing a mismatch, change `text_class`, origin declarations or pairing labels,
add or remove a finding, write a human-review disposition, create a winner or
rank or score or verdict or selected variant, write to the repository, contact
anything, or allocate identifiers by itself — the proposed identity arrives as
an argument, and a proposed binding has no repository authority until a
successfully published authoritative commit carries it (brief section 10.4).
"""

import copy
import hashlib
import json
import re

RUN_AUTHORITY = "W7-D5-SEB"
SPECIMEN_AUTHORING_RECORD = "W7-D4-SHB"
WRAPPER_KEY = "generated_evaluation_record"

_GER_ID = re.compile(r"^GER-\d{4}$")
_RUN_ID = re.compile(r"^W7-D5-RUN-\d{2}$")
_AS_OF = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# The four top-level positions the binder owns. Everything else must survive
# byte-identically, and the comparison below enforces that as a refusal, not a
# convention.
_BOUND_FIELDS = ("record_id", "run_id", "authorising_record", "as_of")


class BindingRefusal(Exception):
    """Raised when the binder refuses. Never carries capture text."""


def _digest(text):
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def bind_final_record(candidate, *, record_id, run_id, as_of):
    """Return the final D5 record object. Pure: the input is not mutated.

    `candidate` is the in-memory wrapped record produced by the frozen D4
    harness invoked with `authorising_record = W7-D4-SHB`.
    """
    if not _GER_ID.match(record_id or ""):
        raise BindingRefusal("proposed record identity is not GER-#### shaped")
    if not _RUN_ID.match(run_id or ""):
        raise BindingRefusal("run identity is not a W7-D5 run identity")
    if not _AS_OF.match(as_of or ""):
        raise BindingRefusal("as_of is not a calendar date")
    if not isinstance(candidate, dict) or set(candidate) != {WRAPPER_KEY}:
        raise BindingRefusal("candidate is not a wrapped generated-evaluation record")

    record = candidate[WRAPPER_KEY]
    if record.get("authorising_record") != SPECIMEN_AUTHORING_RECORD:
        raise BindingRefusal("candidate was not assembled under the D4 specimen-authoring "
                             "authority; the binder does not repair a wrong invocation")
    captures = record.get("captures")
    if not isinstance(captures, dict) or not captures:
        raise BindingRefusal("candidate carries no captures")
    for label, cap in captures.items():
        if cap.get("authoring_record") != SPECIMEN_AUTHORING_RECORD:
            raise BindingRefusal("a capture does not carry the D4 authoring authority")
        text = cap.get("text")
        if not isinstance(text, str) or not text:
            raise BindingRefusal("a capture text is missing")
        if cap.get("text_digest") != _digest(text):
            raise BindingRefusal("a capture digest does not match its text; refused, "
                                 "never recomputed")

    bound = copy.deepcopy(candidate)
    inner = bound[WRAPPER_KEY]
    inner["record_id"] = record_id
    inner["run_id"] = run_id
    inner["authorising_record"] = RUN_AUTHORITY
    inner["as_of"] = as_of

    # Everything the binder does not own must be untouched. Compare the whole
    # record minus the four bound positions, including every capture byte.
    strip_a = {k: v for k, v in record.items() if k not in _BOUND_FIELDS}
    strip_b = {k: v for k, v in inner.items() if k not in _BOUND_FIELDS}
    if strip_a != strip_b:
        raise BindingRefusal("binding altered a position the binder does not own")
    return bound


def canonical_bytes(bound):
    """Serialise the exact canonical D5 bytes: UTF-8, no BOM, LF, indent 1,
    ensure_ascii off, final newline. Returns bytes; writes nothing."""
    if not isinstance(bound, dict) or set(bound) != {WRAPPER_KEY}:
        raise BindingRefusal("only a wrapped record is serialisable")
    out = json.dumps(bound, indent=1, ensure_ascii=False) + "\n"
    return out.encode("utf-8")
