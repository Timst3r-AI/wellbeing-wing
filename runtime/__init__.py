"""Wellbeing Wing runtime — the W5 enforcement layer.

Authorised by the W5-D2-M01 Tier F opening brief (accepted 2026-08-17)
under the accepted W5-D2 milestone brief. This tree holds the W5-D2
runtime implementation, landed milestone by milestone; it lives outside
the sealed engine with separation both ways (ADR 0024 decision 4).

At W5-D2-M01 this package owns no capability, holds no governed
content, and performs no I/O. Later milestones add exactly what their
own briefs authorise, each with same-commit deterministic proofs and
ADR 0035 residue tests.
"""
