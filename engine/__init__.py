"""The governed engine spine.

One headless core, many callers, no privileged path. The doctrine core
is pure; everything worldly lives behind ports. Governed by the
project's accepted decision records (ADR 0004 through ADR 0012): no
decrypted content persists past task end; keys are held by the user
and appear in no store, log, or output; nothing here interprets what
it carries, contacts any model, or approves anything into truth.

Milestone 1 scope: encrypted store skeleton with test-supplied keys
only. No key derivation, custody, import, export, or persistence of
key material exists in this milestone by decision.
"""

__all__ = ["core", "ports"]
