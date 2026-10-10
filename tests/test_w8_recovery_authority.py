"""W8 — supplementary recovery authority proofs (ADR-0059, A1–A12).

ADR-0059 is the phase-level authority that ADR-0058 decision 13 requires.
It reconciles ADR-0055, ADR-0057, the W8-D3 opening brief and the W8-D2
opening brief in place, opens exactly one supplementary corpus through the
opening brief W8-S1-SOB, and fixes a closed, staged list of proof
successions, of which only ADR-0058's R5 moves at its own landing. This
module proves that every reconciliation is the exact transformation of its
fixed published pre-image, that the landing changes nothing else, and that
the binding, membership, scope and ordering verdicts later landings must
apply refuse what they must refuse — each with planted-mutant or negative
controls.

THIS MODULE CARRIES NO ASSOCIATION OR FIGURE FROM THE VOID ATTEMPT. It
names no case, holds no disposition token as a literal, renders no packet,
opens no published case or manifest file, names, reads or reaches no
custody location, opens, parses, hashes or relays no withheld authoring
record, and reproduces no commitment. Its binding verdicts run over
labelled sentinel identities only.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any disposition, any authored intent or any relation;
that any supplementary case exists, is fresh or is semantically
independent of anything; anything about the reviewer, the reviewer's prior
exposure or the absence of influence; that any custody record exists, is
intact or was never touched; that any session, reproduction, reveal or
count may now begin; or that the human authority has accepted the reading
of ADR-0058 decision 8, which only the human acceptance act supplies.
"""

import hashlib
import json
import re
import subprocess
import unittest
from collections import Counter
from pathlib import Path

import test_w8_calibration_law as calibration
import test_w8_discriminating_instrument_corpus as corpus
import test_w8_discriminating_instrument_envelope as envelope
import test_w8_session_recovery_law as recovery
import w8_review_packet as packet
from test_repo_state import lf_hash

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The derived public baseline: ADR-0058's published landing commit. Every
# pre-image below is read from this fixed commit, never from a movable ref.
LANDING = "897f0b14a66ee956bd9fe36e63975b04d5dc9663"

ADR59 = "docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md"
SOB = "docs/phases/W8-S1-supplementary-opening-brief.md"
SELF_REL = "tests/test_w8_recovery_authority.py"
A54 = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
A55 = "docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md"
A57 = "docs/decisions/0057-w8-disposition-reveal-calibration-law.md"
SCB = "docs/phases/W8-D3-synthetic-calibration-brief.md"
DIB = "docs/phases/W8-D2-discriminating-instrument-brief.md"
R58 = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"

CENSUS = frozenset({ADR59, SOB, SELF_REL, A55, A57, SCB, DIB, R58, REGISTRY,
                    BOARD})
SUPPLEMENT_HOME = "governance/discriminating-supplement"
SUPPLEMENT_RECORD = "docs/phases/W8-S1-supplementary-corpus-record.md"
SUPPLEMENT_MODULE = "tests/test_w8_supplementary_corpus.py"
SUPPLEMENT_ENTRIES = frozenset({"W8-S1-SCR", "W8-S1-CM-01"})
SUPPLEMENT_TOTAL = 12
ORIGINAL_HOME = "governance/discriminating-instrument"

# Fixed published pre-images at LANDING: (identity, LF SHA-256, blob).
PREIMAGE = {
    A55: ("ADR-0055",
          "sha256:e23ddd60e197b8eadda50f1400cf0064a4665dd235edb96a05079ef606171d2b",
          "0da892b2a5aab4f271095c3515518d9c45a620bf"),
    A57: ("ADR-0057",
          "sha256:0954293ff1ebb8ba1fb66230f8673a3778c09b9c04762e3bc983cc1cc8c7c585",
          "abe344233f52929a934eabde689866fa25513201"),
    SCB: ("W8-D3-SCB",
          "sha256:ce93c54735a09acf5a2e966628101538912d2faf4e09ad010a7606e293bc6068",
          "8b995003ff7628e2887f837d6cddb6ae8b6141f8"),
    DIB: ("W8-D2-DIB",
          "sha256:1b5be8d2207b06c44a40191e0ebcc785a8daad811103d120eca4029a2da19a83",
          "14d65ef1a632d6ff2e0e1277b4301caf8baa9a3e"),
    R58: ("ADR-0058 proof module",
          "sha256:0471aa9ad53b84a07a784e3376f30e9b444b698d359559937f765f69fb209163",
          "1beab6aa683d94ff7c4d2786a62df2e46b4601bd"),
    REGISTRY: ("registry",
               "sha256:ca723aa5bf8adfd91dedea4ba1f52f9a6c2ca9afb2777a36f75d0738a3e0c353",
               "2c3bb9449347c47cfe8f5245faf92897e9625e37"),
    BOARD: ("board",
            "sha256:13d10333b8ade85cab0e31b89195ac85c8ff6bd6561836efed22888a836ed72a",
            "d23a0204beb3ee0460fc93d3c12327019c7e07f8"),
}
# The three of ADR-0058 decision 8's five laws that ADR-0059 reconciles.
RECONCILED_LAW = {"ADR-0055": A55, "ADR-0057": A57, "W8-D3-SCB": SCB}
RECONCILED_ENTRIES = (("ADR-0055", A55), ("ADR-0057", A57),
                      ("W8-D3-SCB", SCB), ("W8-D2-DIB", DIB))
# Part F rows of ADR-0059: source cell -> path.
PART_F_SOURCES = {"ADR-0055": A55, "ADR-0057": A57, "`W8-D3-SCB`": SCB,
                  "`W8-D2-DIB`": DIB, "ADR-0058 proof module": R58}

PUBLIC_SAFETY = "\n## Public-safety note\n"

# ------------------------------------------------------------ edit tables
# Each site is (label, exact pre-image text, exact post-image text). The
# table authorises nothing by itself: ADR-0059 Part F names every label and
# pins every post-image, and A4/A5 bind table, pin and bytes together.
SITES = {
    A55: (
        ("d26",
         "**The commitment nonce:** for future D2-C authoring, each case "
         "receives",
         "**The commitment nonce:** for future D2-C authoring, and for the "
         "one supplementary corpus authored under ADR-0059, each case "
         "receives"),
        ("d26",
         "and remains withheld until the D3 reveal.",
         "and remains withheld until the reveal of its own corpus."),
        ("d27",
         "**Once published by D2-C, neither the hidden record nor the nonce "
         "may move.**",
         "**Once published by D2-C — or, for the supplementary corpus, by "
         "its own authoring landing — neither the hidden record nor the "
         "nonce may move.**"),
        ("d28",
         "ordering, or any other law of this record.)* **It contains no "
         "authored class",
         "ordering, or any other law of this record.)* **The one "
         "supplementary corpus authored under ADR-0059 has exactly one "
         "manifest instance of its own, under this same container law, at "
         "`governance/discriminating-supplement/W8-S1-commitment-manifest."
         "json`; each manifest instance binds its own corpus only, and no "
         "row of one corpus appears in the other's.** **It contains no "
         "authored class"),
        ("d29",
         "29. **From the D2-C landing until the D3 review session is "
         "complete:**",
         "29. **For each corpus, from its authoring landing until its "
         "custody ends by a separately governed act — for the supplementary "
         "corpus authored under ADR-0059, its own reveal; for the D2-C "
         "corpus, only its own separately governed act, which no session, "
         "reproduction or reveal of another corpus supplies:**"),
        ("d29",
         "**D2-C must read the retained bytes back and reproduce every "
         "proposed commitment before landing**",
         "**each authoring landing — D2-C, and the supplementary authoring "
         "landing — must read its retained bytes back and reproduce every "
         "proposed commitment before landing**"),
        ("d29",
         "**D3 must reproduce every published commitment from the same "
         "retained bytes before reveal and before any calibration "
         "comparison**",
         "**D3 must reproduce every published commitment of the corpus being "
         "revealed — and of no other corpus — from the same retained bytes "
         "before reveal and before any calibration comparison**"),
        ("d30",
         "If the existing outside-repository review transport cannot "
         "guarantee byte-stability across D2 to D3, **STOP before the first "
         "case is authored.**",
         "If the existing outside-repository review transport cannot "
         "guarantee byte-stability across D2 to D3 — or, for the "
         "supplementary corpus, from its authoring to its reveal, in a "
         "custody sub-location of its own — **STOP before the first case of "
         "that corpus is authored.**"),
        ("note", PUBLIC_SAFETY,
         "\n## Reconciliation note (ADR-0059)\n\nDecisions 26 to 30 are "
         "reconciled in place by ADR-0059, the phase-level supplementary "
         "recovery authority, so that their nonce, commitment, manifest, "
         "custody and transport provisions bind each corpus separately: the "
         "D2-C corpus exactly as before, and the one supplementary corpus "
         "that record opens. The reconciliation is effective only on "
         "ADR-0059's acceptance, publication and remote verification. Every "
         "other decision of this record is unchanged; the published D2-C "
         "corpus, manifest and commitments are byte-untouched; and nothing "
         "in it changes the case shape, canonical bytes, identity, "
         "ordering, withheld-record shape or class opacity.\n"
         + PUBLIC_SAFETY),
    ),
    A57: (
        ("d1",
         "only from the committed Git object bytes of the published W8 "
         "review cases, as the effective `W8-D2-CBC` requires**",
         "only from the committed Git object bytes of the published W8 "
         "review cases of the session corpus that ADR-0059 binds, at that "
         "corpus's pinned commit, as the effective `W8-D2-CBC` requires**"),
        ("d5",
         "so that anyone can regenerate it from the published renderer and "
         "the published cases and confirm it.",
         "so that anyone can regenerate it from the published renderer and "
         "the session corpus's published cases at its pinned commit and "
         "confirm it."),
        ("d8",
         "8. **No authored class, intended disposition, construction map, "
         "authoring check, rationale, inconclusive-condition selection, "
         "nonce, expected distribution, class count, aggregate, "
         "recommendation, default, ranking, highlight, summary, diff or "
         "mechanical inference reaches the reviewer before all twelve "
         "dispositions exist and are recorded.**",
         "8. **No authored class, intended disposition, construction map, "
         "authoring check, rationale, inconclusive-condition selection, "
         "nonce, expected distribution, class count, aggregate, "
         "recommendation, default, ranking, highlight, summary, diff or "
         "mechanical inference — and no case-level judgment, preferred or "
         "predicted disposition or rationale about any case from anyone "
         "other than the reviewer — reaches the reviewer from the "
         "reviewer's first access to any case material of the session "
         "corpus, in any form and including review of that corpus's "
         "authoring candidate, until the session record is published, "
         "including the whole interval in which a returned token may still "
         "be revised.** The withheld-material and composition prohibitions "
         "bind throughout authoring and custody as well. **Permitted "
         "throughout, and nothing more:** the approved rendering and "
         "delivery operation; structural completeness, one lawful token "
         "returned for every case, without any per-token tally or "
         "distribution before the reveal landing; exact transcription and "
         "binding; and source-grounded clarification of governing law that "
         "names no case and suggests no disposition. Sharing material with "
         "the architect or implementer for those purposes alone is not "
         "itself a breach."),
        ("d9",
         "`rows` holds exactly one row per published case, sorted solely by "
         "`case_id`",
         "`rows` holds exactly one row per case of the session corpus that "
         "ADR-0059 binds — no missing, extra, duplicate, original-corpus or "
         "mixed-corpus row — sorted solely by `case_id`"),
        ("d11",
         "carries the act's date, the reviewer role, the packet SHA-256, the "
         "register binding, and the statement that every token is an "
         "individual human act",
         "carries the act's date, the reviewer role, the packet SHA-256, the "
         "register binding, the session-corpus binding — the commit "
         "identity of that corpus's authoring landing, its home's committed "
         "tree identity at that commit and its manifest's SHA-256 — the "
         "reviewer's procedural attestation under ADR-0059, and the "
         "statement that every token is an individual human act"),
        ("d13",
         "**The session landing (D3-C) checks custody for existence only** — "
         "the expected records present by name, nothing opened, parsed or "
         "hashed.",
         "**The session landing (D3-C) checks custody for existence only** — "
         "the session corpus's expected records present by name in that "
         "corpus's own custody sub-location, nothing opened, parsed or "
         "hashed, and no retained record of any other corpus listed, opened, "
         "parsed or hashed."),
        ("d15",
         "**Every published authoring commitment is reproduced by hashing the "
         "exact retained bytes directly",
         "**Every published authoring commitment of the session corpus — and "
         "of no other corpus — is reproduced by hashing the exact retained "
         "bytes directly"),
        ("d16",
         "to the untracked repository-relative reveal-candidate paths "
         "`governance/discriminating-reveal/<case_id>.json`, and each copy "
         "must hash to its published commitment.**",
         "to the untracked repository-relative reveal-candidate paths "
         "`governance/discriminating-reveal/<case_id>.json`, for the session "
         "corpus's case identities only, and each copy must hash to its "
         "published commitment.**"),
        ("d18",
         "for cross-binding of each record to its case identity, filename, "
         "manifest row and published visible digest",
         "for cross-binding of each record to its case identity, filename, "
         "row in the session corpus's manifest and published visible "
         "digest"),
        ("d20",
         "**For each case the comparison records exactly:",
         "**For each case of the session corpus the comparison records "
         "exactly:"),
        ("d22",
         "per-token counts of the human dispositions — all three tokens, "
         "zero counts included —",
         "per-token counts of the session corpus's human dispositions — all "
         "three tokens, zero counts included —"),
        ("d24",
         "cannot avoid a reserved field name. **No other proof moves.**",
         "cannot avoid a reserved field name. **Also authorised, each only in "
         "its own landing and only in the exact transformation that record "
         "fixes: the closed, staged proof successions of ADR-0059 Part G. No "
         "other proof moves.**"),
        ("d28",
         "| **K12** | Absence: no tracked packet, register or reveal artefact "
         "exists |",
         "| **K12** | Absence: no tracked packet exists, and no register or "
         "reveal artefact exists before its own landing — after which only "
         "the exact artefacts ADR-0059 Part G admits |"),
        ("note", PUBLIC_SAFETY,
         "\n## Reconciliation note (ADR-0059)\n\nDecisions 1, 5, 8, 9, 11, "
         "13, 15, 16, 18, 20, 22 and 24 and the K12 row of decision 28 are "
         "reconciled in place by ADR-0059, so that every packet, register, "
         "existence check, reproduction, reveal, comparison and count binds "
         "exactly the session corpus that record fixes and never draws the "
         "published D2-C corpus in, and so that decision 8's exclusions "
         "carry whole over a longer interval. The reconciliation is "
         "effective only on ADR-0059's acceptance, publication and remote "
         "verification. Decision 6 and every other decision of this record "
         "are unchanged.\n" + PUBLIC_SAFETY),
    ),
    SCB: (
        ("header",
         "**Governed by:** the W8 runway (`W8-AR`) whole, especially §6.1 and "
         "§12;",
         "**Governed by:** the W8 runway (`W8-AR`) whole, especially §6.1 and "
         "§12; ADR-0059 and the supplementary opening brief `W8-S1-SOB`, "
         "which select the session corpus and reconcile this brief in "
         "place;"),
        ("§1 item 3",
         "The twelve published W8-D2 cases are the whole of D3's material; "
         "D3 authors no case, edits no case and adds no case.",
         "**D3's session material is exactly the session corpus ADR-0059 "
         "binds — the twelve published cases of the supplementary corpus "
         "`W8-S1`, at their pinned commit.** The twelve published W8-D2 "
         "cases remain published, their retained records stay sealed, and "
         "neither enters any D3 session, register, existence check, "
         "reproduction, reveal or comparison. D3 authors no case, edits no "
         "case and adds no case."),
        ("§2 item 8",
         "8. **Blinding holds until the session is complete and recorded.** "
         "No authored class, intended disposition, construction map, "
         "authoring check, rationale, inconclusive-condition selection, "
         "nonce, expected distribution, class count, aggregate, "
         "recommendation, default, ranking, highlight, summary, diff or "
         "mechanical inference may reach the reviewer before all twelve "
         "individual dispositions exist and are recorded (ADR-0054 decisions "
         "27–28; ADR-0055 Part K).",
         "8. **Blinding holds from the reviewer's first access to any case "
         "material of the session corpus, in any form, until the session "
         "record is published.** No authored class, intended disposition, "
         "construction map, authoring check, rationale, "
         "inconclusive-condition selection, nonce, expected distribution, "
         "class count, aggregate, recommendation, default, ranking, "
         "highlight, summary, diff or mechanical inference — and no "
         "case-level judgment, preferred or predicted disposition or "
         "rationale about any case from anyone other than the reviewer — "
         "may reach the reviewer in that interval, including while a "
         "returned token may still be revised (ADR-0054 decisions 27–28; "
         "ADR-0055 Part K; ADR-0057 decision 8 as reconciled by ADR-0059)."),
        ("§2 item 12",
         "every published authoring commitment is reproduced by hashing the "
         "exact retained bytes directly, before any parse or "
         "reserialisation.**",
         "every published authoring commitment of the session corpus — and "
         "of no other corpus — is reproduced by hashing the exact retained "
         "bytes directly, before any parse or reserialisation.**"),
        ("§2 item 16",
         "Every D3 rendering of, and every D3 proof over, the immutable "
         "published D2 cases and commitment manifest reads their committed "
         "Git object bytes, as the effective `W8-D2-CBC` requires;",
         "Every D3 rendering of, and every D3 proof over, the immutable "
         "published D2 cases and commitment manifest — and, under the same "
         "discipline, the immutable published cases and manifest of the "
         "session corpus — reads their committed Git object bytes, as the "
         "effective `W8-D2-CBC` requires;"),
        ("§3 item 18",
         "and that every commitment is reproduced from the exact retained "
         "bytes before any reveal or calibration comparison (ADR-0055 "
         "decision 29).",
         "and that every commitment of the corpus being revealed is "
         "reproduced from the exact retained bytes before any reveal or "
         "calibration comparison (ADR-0055 decision 29)."),
        ("§3.3",
         "- **Prerequisites:** ADR-0057 effective; a read-only custody "
         "**existence** check — twelve records present by name, nothing "
         "opened, parsed or hashed — so that a session is not spent on an "
         "instrument that could not later be revealed.",
         "- **Prerequisites:** ADR-0057 effective; ADR-0059, `W8-S1-SOB` and "
         "the supplementary authoring landing effective; a read-only custody "
         "**existence** check of the session corpus's own custody "
         "sub-location — its twelve records present by name, nothing "
         "opened, parsed or hashed, and no retained record of any other "
         "corpus listed or touched — so that a session is not spent on an "
         "instrument that could not later be revealed."),
        ("§3.3",
         "(1) render the session packet with the published renderer from the "
         "**committed Git object bytes** of the twelve cases, and record the "
         "packet's SHA-256;",
         "(1) prove that the renderer's input paths are exactly the session "
         "corpus manifest's case paths at its pinned commit, then render the "
         "session packet with the published renderer from the **committed "
         "Git object bytes** of those twelve cases, and record the packet's "
         "SHA-256 with the corpus binding;"),
        ("§3.3",
         "NEW `tests/test_w8_disposition_record.py` · MODIFY "
         "`governance/registry.json` · MODIFY `docs/phases/README.md`. **The "
         "instrument home is not touched**: its C1 closure forbids any new "
         "file there.",
         "NEW `tests/test_w8_disposition_record.py` · MODIFY "
         "`tests/test_w8_calibration_law.py` (the K12 register limb) · "
         "MODIFY `tests/test_w8_session_recovery_law.py` (R7 and R9) · "
         "MODIFY `governance/registry.json` · MODIFY "
         "`docs/phases/README.md`, as ADR-0059 Part G stages them. **Neither "
         "the instrument home nor the supplement home is touched**: their "
         "closures forbid any new file there."),
        ("§3.3",
         "(twelve rows, closed token set, one row per published case, "
         "ascending order, canonical bytes)",
         "(twelve rows, closed token set, one row per case of the session "
         "corpus and none of any other, ascending order, canonical bytes)"),
        ("§3.3",
         "- **Visible to the reviewer:** the session packet only, until all "
         "twelve tokens are returned; then their own recorded tokens in the "
         "candidate. **Never** any withheld material.",
         "- **Visible to the reviewer:** the session corpus's "
         "reviewer-visible case material only — in the session packet, and "
         "earlier only as that corpus's authoring landing lawfully showed "
         "it — until all twelve tokens are returned; then their own "
         "recorded tokens in the candidate. **Never** any withheld "
         "material, and never any case-level judgment from anyone else."),
        ("§3.4",
         "1. **Reproduce all twelve commitments** by hashing the exact "
         "retained bytes directly, read-only, before any parse.",
         "1. **Reproduce all twelve commitments of the session corpus**, and "
         "of no other corpus, by hashing the exact retained bytes directly, "
         "read-only, before any parse."),
        ("§3.4",
         "(exact retained bytes; not individually registered; bound by the "
         "`W8-D2-CM-01` commitments)",
         "(exact retained bytes of the session corpus only; not individually "
         "registered; bound by that corpus's manifest register "
         "`W8-S1-CM-01`)"),
        ("§3.4",
         "· MODIFY `tests/test_w8_discriminating_instrument_corpus.py` (the "
         "C10 scope succession of section 8) · MODIFY "
         "`governance/registry.json` · MODIFY `docs/phases/README.md`. "
         "Anticipated census eighteen; fixed by the candidate.",
         "· MODIFY `tests/test_w8_discriminating_instrument_corpus.py` (the "
         "C10 scope succession of section 8) · MODIFY "
         "`tests/test_w8_calibration_law.py` (the K12 reveal limb) · MODIFY "
         "`tests/test_w8_session_recovery_law.py` (R7 and R8) · MODIFY the "
         "supplementary corpus proof module (its freshness scope) · MODIFY "
         "`governance/registry.json` · MODIFY `docs/phases/README.md`. "
         "Anticipated census twenty-one; fixed by the candidate."),
        ("§3.4",
         "- **Custody:** the read-only reproduction and the byte copy. "
         "Retained records are not deleted, rewritten or moved by D3; any "
         "retirement is a separate act.",
         "- **Custody:** the read-only reproduction and the byte copy, of the "
         "session corpus's records only. Retained records are not deleted, "
         "rewritten or moved by D3; any retirement is a separate act, and no "
         "D3 landing lists, opens, hashes or copies any retained record of "
         "the D2-C corpus."),
        ("§4 item 20",
         "from the committed Git object bytes** of the twelve published "
         "cases, under `W8-D2-CBC`",
         "from the committed Git object bytes** of the twelve published "
         "cases of the session corpus, at its pinned commit, under "
         "`W8-D2-CBC`"),
        ("§5 item 25",
         "25. **Record:** the act's date, the reviewer role, the packet "
         "SHA-256, the register binding, the statement that every token is "
         "an individual human act,",
         "25. **Record:** the act's date, the reviewer role, the packet "
         "SHA-256, the register binding, the session-corpus binding "
         "(authoring-landing commit, home tree identity, manifest SHA-256), "
         "the reviewer's procedural attestation under ADR-0059, the "
         "statement that every token is an individual human act,"),
        ("§7 item 30",
         "30. For each case, the comparison records exactly:",
         "30. For each case of the session corpus, the comparison records "
         "exactly:"),
        ("§8",
         "36. The committed-object reading rule is **not** a D3 succession: "
         "it is already effective through `W8-D2-CBC`, and D3 consumes it.\n",
         "36. The committed-object reading rule is **not** a D3 succession: "
         "it is already effective through `W8-D2-CBC`, and D3 consumes it.\n"
         "\n**Reconciled by ADR-0059:** items 33 to 36, together with the "
         "staged successions of ADR-0059 Part G, are the complete and closed "
         "list. Each is authorised only in its own landing and only in the "
         "exact transformation that record fixes; no other proof moves.\n"),
        ("§9",
         "| D3-C session | the packet of the twelve published cases | any "
         "withheld byte; any tally; any commentary on case content |",
         "| supplementary authoring landing (under ADR-0059 and `W8-S1-SOB`) "
         "| the supplement's reviewer-visible cases, for the reviewer's own "
         "landing review only | any withheld byte, beyond the authoring "
         "implementer's own construction and custody duties; any case-level "
         "judgment, preferred disposition, rationale or construction "
         "information |\n"
         "| D3-C session | the packet of the session corpus's twelve "
         "published cases | any withheld byte; any tally; any commentary on "
         "case content |"),
        ("§11",
         "· any carried state moving.",
         "· any carried state moving · any original-corpus or mixed-corpus "
         "membership in a packet, register, existence check, reproduction, "
         "reveal or comparison · any act by a D3 landing on a retained record "
         "of the D2-C corpus · any association or figure from the void "
         "attempt used as a source (ADR-0058 decision 5)."),
        ("§12",
         "· any custody retirement · any disclosure of the custody location.",
         "· any custody retirement · any disclosure of the custody location. "
         "**The supplementary corpus and the in-place reconciliation of "
         "ADR-0055, ADR-0057, this brief and `W8-D2-DIB` come only from "
         "amendment and opening authority outside W8-D3 — the phase-level "
         "ADR-0059 and `W8-S1-SOB`; W8-D3 itself still authors, edits and "
         "adds no case and amends no law.**"),
        ("§15",
         "· the named proof successions are bounded and authorised only in "
         "their own landings ·",
         "· the named proof successions — as reconciled by ADR-0059 into one "
         "closed, staged list — are bounded and authorised only in their own "
         "landings ·"),
        ("note", PUBLIC_SAFETY,
         "\n## Reconciliation note (ADR-0059)\n\nThe header, section 1 item "
         "3, section 2 items 8, 12 and 16, section 3 item 18 and its D3-C "
         "and D3-D landings, section 4 item 20, section 5 item 25, section 7 "
         "item 30, and sections 8, 9, 11, 12 and 15 are reconciled in place "
         "by ADR-0059, so that D3's session, existence check, reproduction, "
         "reveal and comparison bind exactly the session corpus that record "
         "fixes. The reconciliation is effective only on ADR-0059's "
         "acceptance, publication and remote verification. Every other "
         "provision is unchanged; the lede, sections 3.1 and 3.2 and section "
         "13 remain historical statements of this brief's own landing and "
         "of D3-B, and section 14's builder-autonomy rule stands unchanged."
         "\n" + PUBLIC_SAFETY),
    ),
    DIB: (
        ("§12",
         "12. **Custody:** from D2-C's landing until the D3 review session is "
         "complete, the exact withheld authoring records remain",
         "12. **Custody:** from D2-C's landing until the D2-C corpus's "
         "custody ends by its own separately governed act — which no "
         "session, reproduction or reveal of another corpus supplies — the "
         "exact withheld authoring records remain"),
        ("§14",
         "14. **Reveal belongs to D3, not D2.** Only after the required "
         "individual dispositions exist does D3 reveal the exact authoring "
         "records — and **reveal must reproduce every previously published "
         "commitment byte-exactly before any calibration comparison is "
         "made.",
         "14. **Reveal belongs to D3, not D2.** Only after the required "
         "individual dispositions on a corpus exist may that corpus be "
         "revealed, and only under governed authority: the D2-C corpus's "
         "reveal, retirement or other custody end requires its own "
         "separately governed act, and a D3 reveal of the supplementary "
         "corpus authored under ADR-0059 reveals that corpus only — and "
         "**reveal must reproduce every previously published commitment of "
         "the corpus revealed byte-exactly before any calibration "
         "comparison is made."),
        ("note", PUBLIC_SAFETY,
         "\n## Reconciliation note (ADR-0059)\n\nSections 12 and 14 are "
         "reconciled in place by ADR-0059, so that custody and reveal bind "
         "each corpus separately: no session, reproduction or reveal of the "
         "one supplementary corpus that record opens ends, opens or reveals "
         "the D2-C corpus's custody. The reconciliation is effective only on "
         "ADR-0059's acceptance, publication and remote verification. Every "
         "other provision is unchanged, and the D2-C completion record stays "
         "as built.\n" + PUBLIC_SAFETY),
    ),
    R58: (
        ("R5",
         'DECISION_8 = {"ADR-0054", "ADR-0055", "ADR-0057", "W8-D3-SCB", '
         '"W8-D2-CBC"}\n',
         'DECISION_8 = {"ADR-0054", "ADR-0055", "ADR-0057", "W8-D3-SCB", '
         '"W8-D2-CBC"}\n'
         "# R5 succession under ADR-0059 Part G: every pin above stays proven "
         "at this\n# record's own published landing commit, and the present "
         "state of exactly\n# three of decision 8's laws is the exact "
         "reconciliation ADR-0059 pins.\n"
         'LANDING = "897f0b14a66ee956bd9fe36e63975b04d5dc9663"\n'
         'RECONCILED_BY_ADR_0059 = {"ADR-0055", "ADR-0057", "W8-D3-SCB"}\n'),
        ("R5", r'''class R5_PublishedLawUntouched(unittest.TestCase):
    def test_r5_decision_8_law_byte_untouched(self):
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        with self.subTest(fact="the pin set is exactly decision 8's law"):
            self.assertEqual({eid for eid, _, _ in UNTOUCHED.values()},
                             DECISION_8)
        for rel, (eid, lf, blob) in UNTOUCHED.items():
            with self.subTest(working_copy=eid):
                self.assertEqual(lf_hash(ROOT / rel), lf)
            with self.subTest(committed_object=eid):
                self.assertEqual(_git("rev-parse", "HEAD:" + rel).strip(), blob)
            with self.subTest(registry=eid):
                self.assertEqual(by_id[eid]["content_hash"], lf)
        with self.subTest(control="a one-byte change is detected"):
            rel = next(iter(UNTOUCHED))
            raw = (ROOT / rel).read_bytes() + b" "
            self.assertNotEqual("sha256:" + hashlib.sha256(
                raw.replace(b"\r\n", b"\n")).hexdigest(), UNTOUCHED[rel][1])
''', r'''class R5_PublishedLawUntouched(unittest.TestCase):
    def test_r5_decision_8_law_byte_untouched(self):
        import test_w8_recovery_authority as authority
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        with self.subTest(fact="the pin set is exactly decision 8's law"):
            self.assertEqual({eid for eid, _, _ in UNTOUCHED.values()},
                             DECISION_8)
        with self.subTest(fact="ADR-0059 reconciles exactly three of them"):
            self.assertEqual(set(authority.RECONCILED_LAW),
                             RECONCILED_BY_ADR_0059)
        for rel, (eid, lf, blob) in UNTOUCHED.items():
            with self.subTest(landing_object=eid):
                self.assertEqual(
                    _git("rev-parse", LANDING + ":" + rel).strip(), blob)
                self.assertEqual(authority.committed_lf_hash(LANDING, rel), lf)
            if eid in RECONCILED_BY_ADR_0059:
                with self.subTest(exact_reconciliation=eid):
                    self.assertEqual(
                        authority.reconciliation_violations(rel), [])
                with self.subTest(registry=eid):
                    self.assertEqual(by_id[eid]["content_hash"],
                                     lf_hash(ROOT / rel))
                continue
            with self.subTest(working_copy=eid):
                self.assertEqual(lf_hash(ROOT / rel), lf)
            with self.subTest(committed_object=eid):
                self.assertEqual(_git("rev-parse", "HEAD:" + rel).strip(), blob)
            with self.subTest(registry=eid):
                self.assertEqual(by_id[eid]["content_hash"], lf)
        with self.subTest(control="a one-byte change is detected"):
            rel = next(iter(UNTOUCHED))
            raw = (ROOT / rel).read_bytes() + b" "
            self.assertNotEqual("sha256:" + hashlib.sha256(
                raw.replace(b"\r\n", b"\n")).hexdigest(), UNTOUCHED[rel][1])
        with self.subTest(control="an unauthorised edit to a reconciled law "
                                  "is detected"):
            rel = next(r for r, (e, _, _) in UNTOUCHED.items()
                       if e in RECONCILED_BY_ADR_0059)
            text = _lf_text(ROOT / rel)
            self.assertTrue(authority.reconciliation_violations(
                rel, present=text + " "))
'''),
    ),
}

# ------------------------------------------------- board: authorised sites
BOARD_LINKS = (
    "([`../decisions/0059-w8-supplementary-corpus-recovery-authority.md`]"
    "(../decisions/0059-w8-supplementary-corpus-recovery-authority.md); "
    "[`W8-S1-supplementary-opening-brief.md`]"
    "(W8-S1-supplementary-opening-brief.md))")
BOARD_STATUS_TAIL = (
    "one fresh twelve-case supplementary corpus as the D3 session corpus, "
    "keep the human authority the sole source of dispositions, reconcile "
    "ADR-0055, ADR-0057, the D3 brief and the D2 brief in place by exact, "
    "proven transformations, and fix a closed, staged list of proof "
    "successions, while the original corpus's retained records stay sealed "
    "and D3-C stays blocked until the supplementary authoring landing is "
    "effective.")
BOARD_STATUS = {
    "draft": ("**A draft phase-level recovery authority, ADR-0059, and a "
              "draft supplementary opening brief, `W8-S1-SOB`, are before "
              "the human reviewer** " + BOARD_LINKS + ": if accepted, they "
              "would open " + BOARD_STATUS_TAIL),
    "accepted": ("**ADR-0059 — the supplementary recovery authority — is "
                 "law, and `W8-S1-SOB` opens the supplementary corpus** "
                 + BOARD_LINKS + " — accepted %s: they open "
                 + BOARD_STATUS_TAIL),
}
ROW59_BODY = (
    "Tier J: **phase-level recovery authority** — answers ADR-0058's "
    "requirement of a separately governed authority outside W8-D3: one "
    "fresh twelve-case supplementary corpus becomes the D3 session corpus, "
    "bound by its authoring commit, home tree and manifest, with original "
    "or mixed membership refused; the human authority remains the sole "
    "source of dispositions, and no comparability with the void attempt or "
    "the original corpus is claimed; the conduct interval runs from the "
    "reviewer's first access to supplementary case material until the "
    "session record is published; ADR-0055, ADR-0057, the D3 brief and the "
    "D2 brief are reconciled in place by exact, proven transformations, and "
    "ADR-0058 decision 8 is read as landing-scoped only by express "
    "acceptance; the original corpus stays sealed, its custody, retirement "
    "or reveal left to its own act. **No case, nonce, custody act, session, "
    "reproduction, reveal or count is authorised by this record; D3-C stays "
    "blocked and D3-D unopened.**")
ROWSOB_BODY = (
    "Tier J: **opens one supplementary corpus, `W8-S1`, at phase level** — "
    "exactly twelve fresh synthetic cases authored under ADR-0054 and "
    "ADR-0055 as reconciled, from public doctrine only, never from the void "
    "attempt's associations or adaptations of the original cases; its own "
    "home, manifest, record and custody sub-location; construction and "
    "composition withheld until its own reveal. **W8-D2 stays complete as "
    "built. First-case authoring needs this brief and ADR-0059 effective "
    "and the human authority's explicit instruction to prepare the "
    "authoring candidate; the supplementary corpus becomes governed and "
    "published only through its separately accepted, published and "
    "independently remote-verified authoring landing, and D3-C stays "
    "blocked until that landing is effective.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
ROW59 = ("| W8 — Supplementary Corpus Recovery Authority (ADR-0059) | "
         "[`../decisions/0059-w8-supplementary-corpus-recovery-authority.md`]"
         "(../decisions/0059-w8-supplementary-corpus-recovery-authority.md) "
         "| ")
ROWSOB = ("| W8 — Supplementary Corpus (opening brief, W8-S1-SOB) | "
          "[`W8-S1-supplementary-opening-brief.md`]"
          "(W8-S1-supplementary-opening-brief.md) | ")
BOARD_STATUS_ANCHOR = ("creating no reviewer route. **No session, "
                       "disposition, reveal or calibration exists yet.")
BOARD_ROW_ANCHOR = ("progress needs a separately governed authority outside "
                    "W8-D3.** |\n")


def board_sites(state, date=None):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         "creating no reviewer route. " + fill(BOARD_STATUS[state])
         + " **No session, disposition, reveal or calibration exists yet."),
        ("rows", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR
         + ROW59 + fill(ROW_PREFIX[state]) + ROW59_BODY + " |\n"
         + ROWSOB + fill(ROW_PREFIX[state]) + ROWSOB_BODY + " |\n"),
    )


# ---------------------------------------------- registry: authorised edits
ERRATA_DRAFT_DATE = "2026-10-10"
ERRATA = {
    "ADR-0055": (
        "Decisions 26 to 30 reconciled in place by ADR-0059 "
        "(docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md), "
        "the phase-level supplementary recovery authority: the nonce, "
        "commitment, manifest-instance, custody-window, reproduction and "
        "transport provisions now bind each corpus separately - the D2-C "
        "corpus exactly as before, and the one supplementary corpus W8-S1 - "
        "with a reconciliation note added. The exact transformation of the "
        "published pre-image is proven by tests/test_w8_recovery_authority.py "
        "against the post-image ADR-0059 pins. Effective only on ADR-0059's "
        "acceptance, publication and remote verification; case shape, "
        "canonical bytes, identity, ordering, withheld-record shape and class "
        "opacity unchanged. Hash recomputed in the same commit."),
    "ADR-0057": (
        "Decisions 1, 5, 8, 9, 11, 13, 15, 16, 18, 20, 22 and 24 and the K12 "
        "row of decision 28 reconciled in place by ADR-0059 "
        "(docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md): "
        "every packet, register, existence check, reproduction, reveal, "
        "comparison and count binds exactly the session corpus ADR-0059 "
        "fixes and never the published D2-C corpus; decision 8's exclusions "
        "carry whole over an interval running from the reviewer's first "
        "access to session-corpus case material until the session record is "
        "published, with a closed list of permitted assistance; the session "
        "record adds the corpus binding and the reviewer's procedural "
        "attestation; decision 24 admits ADR-0059's closed, staged "
        "successions. Decision 6 unchanged. The exact transformation of the "
        "published pre-image is proven by tests/test_w8_recovery_authority.py "
        "against the post-image ADR-0059 pins. Effective only on ADR-0059's "
        "acceptance, publication and remote verification. Hash recomputed in "
        "the same commit."),
    "W8-D3-SCB": (
        "Header and sections 1, 2, 3, 4, 5, 7, 8, 9, 11, 12 and 15 reconciled "
        "in place by ADR-0059 "
        "(docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md): "
        "D3's session material is exactly the session corpus ADR-0059 binds; "
        "the existence check, packet, register, reproduction, reveal and "
        "comparison never draw in the published D2-C corpus; blinding runs "
        "from the reviewer's first access to session-corpus case material "
        "until the session record is published; section 8 joins ADR-0059's "
        "staged successions into one closed list; section 12 names the "
        "outside amendment and opening authority while W8-D3 still authors "
        "no case and amends no law. The exact transformation of the "
        "published pre-image is proven by tests/test_w8_recovery_authority.py "
        "against the post-image ADR-0059 pins. Effective only on ADR-0059's "
        "acceptance, publication and remote verification. Hash recomputed in "
        "the same commit."),
    "W8-D2-DIB": (
        "Sections 12 and 14 reconciled in place by ADR-0059 "
        "(docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md): "
        "the D2-C corpus's custody now runs until its own separately "
        "governed custody act, and its reveal, retirement or other custody "
        "end requires that act - no session, reproduction or reveal of the "
        "supplementary corpus supplies it. Role updated in the same commit, "
        "because it repeated the superseded custody window. The exact "
        "transformation of the published pre-image is proven by "
        "tests/test_w8_recovery_authority.py against the post-image ADR-0059 "
        "pins. Effective only on ADR-0059's acceptance, publication and "
        "remote verification; the D2-C completion record stays as built. "
        "Hash recomputed in the same commit."),
}
DIB_ROLE_SITE = (
    "remain byte-fixed in governed external review transport until the D3 "
    "review session is complete;",
    "remain byte-fixed in governed external review transport until the "
    "D2-C corpus's own separately governed custody act, which no session, "
    "reproduction or reveal of another corpus supplies (reconciled by "
    "ADR-0059);")
NEW_ENTRY_FIELDS = {
    ADR59: {
        "id": "ADR-0059",
        "title": "0059 - W8 Supplementary Corpus Recovery Authority",
        "type": "adr",
        "role": (
            "The phase-level W8 supplementary recovery authority that "
            "ADR-0058 decision 13 requires, held outside W8-D3. Authorises "
            "exactly: bounded in-place reconciliations of ADR-0055 decisions "
            "26 to 30, of ADR-0057 decisions 1, 5, 8, 9, 11, 13, 15, 16, 18, "
            "20, 22 and 24 and its K12 row, of the W8-D3 opening brief and "
            "of the W8-D2 opening brief, each proven as an exact "
            "transformation of its published pre-image against a pinned "
            "post-image; the opening, through W8-S1-SOB, of exactly one "
            "supplementary corpus W8-S1 of exactly twelve fresh cases, with "
            "no comparability claimed; and a closed, staged list of proof "
            "successions, of which only ADR-0058's R5 moves at this landing. "
            "Binds every later D3 act to the session corpus by its authoring "
            "commit, home tree and manifest, refusing original or mixed "
            "membership; keeps the human authority the sole source of "
            "dispositions and creates no reviewer route; runs the conduct "
            "interval from the reviewer's first access to supplementary case "
            "material until the session record is published, preserving "
            "ADR-0057 decision 8's exclusions whole and permitting only "
            "closed mechanical and law-only assistance, with the reviewer's "
            "attestation a human statement no test can prove; cites ADR-0058 "
            "decision 5 as operative; reads ADR-0058 decision 8 as "
            "landing-scoped, narrowly, only by express acceptance; keeps the "
            "original corpus sealed, its custody, retirement or reveal left "
            "to its own act; and records that broader influence from prior "
            "exposure cannot be mechanically excluded. Lands with proof "
            "obligations A1 to A12 and authorises no case, nonce, custody "
            "act, session, reproduction, reveal or count by itself."),
        "depends_on": ["ADR-0058", "ADR-0057", "ADR-0055", "W8-D3-SCB",
                       "W8-D2-DIB", "W8-D2-MSA", "W8-D2-CBC", "W8-D2-DIC",
                       "W8-D2-CM-01", "ADR-0054", "ADR-0047", "ADR-0056",
                       "W8-AR", "W7-CR"],
    },
    SOB: {
        "id": "W8-S1-SOB",
        "title": "W8-S1 - Supplementary Corpus: Opening Brief",
        "type": "phase-brief",
        "role": (
            "The phase-level opening brief of the one supplementary corpus "
            "W8-S1 under ADR-0059, effective with that record on publication "
            "and remote verification: opens exactly twelve fresh synthetic "
            "cases for authoring work only, through one authoring landing, as "
            "the accepted opening authority runway section 6.1 requires, with "
            "no exemption inferred from its empty deliverable field. "
            "Authoring is grounded in public doctrine and approved "
            "construction law only - never the void attempt's associations, "
            "derived distributions or purported answers, never an adaptation "
            "of or template from the original cases; composition stays "
            "withheld until the supplement's own reveal; custody is a "
            "sub-location of its own in the existing outside-repository "
            "transport, in force before the first case; the reviewer's "
            "conduct interval begins at first access to supplementary case "
            "material, the authoring candidate included; and the original "
            "corpus stays sealed, its custody, retirement or reveal left to "
            "its own act. W8-D2 stays complete as built; W8-D3 stays open "
            "with D3-C blocked until the authoring landing is effective; "
            "W8-D4 through W8-D7 remain closed."),
        "depends_on": ["ADR-0059", "ADR-0058", "ADR-0055", "ADR-0054",
                       "W8-D2-DIB", "W8-D2-MSA", "W8-D2-DIC", "W8-D2-CM-01",
                       "W8-D2-CBC", "ADR-0056", "W8-AR", "W7-CR"],
    },
}
NEW_ENTRY_DEPENDENCIES = {
    "ADR-0059": {"ADR-0058", "ADR-0057", "ADR-0055", "W8-D3-SCB",
                 "W8-D2-DIB", "ADR-0054"},
    "W8-S1-SOB": {"ADR-0059", "ADR-0058", "ADR-0055", "ADR-0054",
                  "W8-D2-DIB"},
}

# ------------------------------------------------------- carried sentences
NO_ROUTE_59 = ("This record creates no substitute reviewer, no delegation "
               "mechanism, no new disposition source and no exception to "
               "ADR-0054 decision 18 or ADR-0057 decision 6.")
EXCLUSIONS = ("authored class, intended disposition, construction map, "
              "authoring check, rationale, inconclusive-condition selection, "
              "nonce, expected distribution, class count, aggregate, "
              "recommendation, default, ranking, highlight, summary, diff or "
              "mechanical inference")
CASE_LEVEL = ("no case-level judgment, preferred or predicted disposition or "
              "rationale about any case")
PERMITTED = ("the approved rendering and delivery operation; structural "
             "completeness, one lawful token returned for every case, "
             "without any per-token tally or distribution before the reveal "
             "landing; exact transcription and binding; and source-grounded "
             "clarification of governing law that names no case and suggests "
             "no disposition")
NOT_A_BREACH = ("Sharing material with the architect or implementer for "
                "those purposes alone is not itself a breach.")
REQUIRED_59 = (
    "This record is that authority, held at phase level: it is not a W8-D3 "
    "landing, and W8-D3 does not grant it to itself.",
    "exactly one supplementary corpus, `W8-S1`, of exactly twelve fresh "
    "cases",
    "Nothing else is authorised by this record — no case, nonce, retained "
    "record, custody exercise, packet, session, disposition, reproduction, "
    "reveal, comparison or count.",
    "Twelve is fixed for workload and for continuity of the session "
    "mechanics only.",
    "No statistical comparability with the void attempt or with the "
    "original corpus is claimed, no comparison between the two corpora is "
    "authorised",
    NO_ROUTE_59,
    "ADR-0058 decision 5 is operative and is cited, not reopened",
    "This record carries no such association or figure and names no case.",
    "This record reads decision 8 as landing-scoped, and narrowly:",
    "the byte state of those five laws at ADR-0058's landing commit remains "
    "proven at that fixed commit, permanently;",
    "the recovery landing made and authorised none of the later "
    "reconciliations;",
    "this record independently authorises only the exact bounded changes "
    "of Part F, and no other change to any of those laws;",
    "ADR-0054 decision 18, ADR-0057 decision 6, ADR-0058's provenance "
    "exclusion and its reviewer prohibitions remain effective",
    "the exact permitted proof successions are enumerated and staged in "
    "Part G.",
    "ADR-0058's text is unchanged, and its narrative summaries are not "
    "reopened.",
    "This reading takes effect only through the human authority's express "
    "acceptance of this record, and that acceptance names it;",
    "A missing, extra or duplicate case, any case of the original corpus, "
    "any mixed set, and any wrong commit, tree or manifest is refused.",
    "the renderer's input paths are first proven to be exactly the bound "
    "manifest's case paths in the supplement home at the bound commit, and "
    "only then is the packet hash recomputed and recorded.",
    "The conduct interval runs from the reviewer's first access to any case "
    "material of the supplementary corpus, in any form and including review "
    "of that corpus's authoring candidate, until the session record is "
    "published, including the whole interval in which a returned token may "
    "still be revised.",
    "The attestation is a human statement. No test proves the absence of "
    "influence, semantic independence or reviewer blinding, and none is "
    "claimed.",
    "does not adapt the original cases, and does not use them as a "
    "template.",
    "broader influence from that prior exposure cannot be mechanically "
    "excluded.",
    "Publication of the supplementary session does not unseal those "
    "retained records, and no act on the supplement lists, opens, parses, "
    "hashes, copies or reveals any original retained record.",
    "Public identity, integrity and textual non-reuse checks over the "
    "original published cases and manifest remain lawful",
    "The original retained records' custody, retirement or eventual reveal "
    "requires its own separately governed act, which this record does not "
    "choose",
    "The validation chain is fixed and runs in this order, each step "
    "refusing missing, malformed, empty and duplicate input before the next "
    "may run",
    "and before that gate the lawful reveal set is empty.",
    "its section 14 builder-autonomy rule — sections 2 through 12 not "
    "builder-variable — stands unchanged as a generic standing rule.",
    "actual custody access, read-back and any non-access are governed "
    "process duties, honoured and recorded, never proven by a test.",
    "No other existing proof moves at this landing.",
    "No green proof supplies a disposition or completes D3-C.",
)
REQUIRED_SOB = (
    "this brief opens exactly one supplementary corpus, `W8-S1`, of exactly "
    "twelve fresh cases, for authoring work only",
    "no exemption from §6.1 is inferred from this record's empty "
    "deliverable field.",
    "W8-D2 stays complete as built:",
    "W8-D3 stays open, with D3-C blocked until the supplementary authoring "
    "landing is effective and D3-D unopened.",
    "It uses none of the void attempt's associations, derived distributions "
    "or purported answers (ADR-0058 decision 5), does not adapt the "
    "original W8 cases, and does not use them as a template.",
    "Authoring assistance creates no reviewer and no disposition route.",
    "Composition is chosen afresh under ADR-0054 and ADR-0055 and stays "
    "withheld until the supplement's own reveal.",
    "These establish textual non-reuse and distinct identities only, never "
    "semantic independence, and the reviewer's broader prior exposure "
    "cannot be mechanically excluded.",
    "it begins the conduct interval of ADR-0059 decision 13",
    "The original corpus's retained records are not listed, opened, parsed, "
    "hashed, copied or moved by any supplementary act, and the supplement's "
    "later session does not unseal them.",
    "except the one authorised proof succession of section 4 item 13 — the "
    "envelope module's case-home limb, exactly as ADR-0059 Part G stages it "
    "— with the original cases, manifest, commitments, completion record "
    "and register unchanged",
    "The architect's review of the authoring candidate is law and mechanics "
    "review only: ADR-0057 decision 6 and the D3 brief's section 2 item 4 "
    "stand unchanged, and the architect gives no likely disposition, "
    "case-level judgment, ranking or preferred outcome to anyone, by any "
    "route.",
    "A case-free architect outcome establishes law and mechanics review "
    "only — never semantic freshness and never the absence of influence.",
    "D3-D, only after the session record is published and independently "
    "remote-verified, every commitment of the supplement reproduces, and the "
    "exact candidate copies scan clean",
    "The exclusions bind reviewer-visible surfaces.",
    "Remote verification of the session record alone permits no parse and "
    "no disclosure.",
)
DRAFT_59 = ("**Status:** Draft for human review. Not accepted. **If accepted, "
            "effective only on publication and remote verification.** No "
            "status is flipped by the implementer; acceptance is the human "
            "reviewer's dated act.")
ACCEPTED_59 = ("**Status:** Accepted by human reviewer, %s. **Effective only "
               "on publication and remote verification.**")
DRAFT_SOB = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification**, together with ADR-0059, at which point it "
             "opens exactly one supplementary corpus, `W8-S1`, for authoring "
             "work only, and nothing beyond it. No status is flipped by the "
             "implementer; acceptance is the human reviewer's dated act.")
ACCEPTED_SOB = ("**Status:** Accepted by human reviewer, %s. **Effective on "
                "publication and remote verification**, together with "
                "ADR-0059, at which point it opens exactly one supplementary "
                "corpus, `W8-S1`, for authoring work only, and nothing beyond "
                "it.")


# ----------------------------------------------------------------- helpers
def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def _lf(raw):
    return raw.replace(b"\r\n", b"\n")


def _sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _flat(text):
    return " ".join(text.split())


def committed_bytes(commit, rel):
    return packet.committed_object_bytes(ROOT, commit, rel)


def committed_lf_hash(commit, rel):
    return _sha(_lf(committed_bytes(commit, rel)))


def preimage(rel):
    return _lf(committed_bytes(LANDING, rel)).decode("utf-8")


def worktree_text(rel):
    return _lf((ROOT / rel).read_bytes()).decode("utf-8")


def apply_sites(text, sites):
    v = []
    for label, old, new in sites:
        n = text.count(old)
        if n != 1:
            v.append("%s: pre-image site occurs %d times" % (label, n))
            continue
        text = text.replace(old, new)
    return text, v


def reverse_sites(text, sites):
    v = []
    for label, old, new in reversed(sites):
        n = text.count(new)
        if n != 1:
            v.append("%s: post-image site occurs %d times" % (label, n))
            continue
        text = text.replace(new, old)
    return text, v


def labels(sites):
    return tuple(dict.fromkeys(label for label, _, _ in sites))


PART_F_ROW = re.compile(
    r"^\| (?P<source>[^|]+?) \| (?P<labels>[^|]+?) \| "
    r"`(?P<pre>sha256:[0-9a-f]{64})` \| `(?P<post>sha256:[0-9a-f]{64})` \|$",
    re.MULTILINE)


def part_f(adr59_text):
    """ADR-0059's Part F rows: path -> (labels, pre-image pin, post pin)."""
    rows = {}
    for m in PART_F_ROW.finditer(adr59_text):
        rel = PART_F_SOURCES.get(m.group("source"))
        if rel is None or rel in rows:
            return None
        rows[rel] = (tuple(s.strip() for s in m.group("labels").split(",")),
                     m.group("pre"), m.group("post"))
    return rows


def reconciliation_violations(rel, present=None, adr59=None, sites=None):
    """The exact-transformation verdict: the fixed pre-image under the edit
    table yields exactly the present bytes and ADR-0059's pinned
    post-image, every edited site occurs exactly once, and reversing the
    table restores the pre-image."""
    sites = SITES[rel] if sites is None else sites
    present = worktree_text(rel) if present is None else present
    adr59 = worktree_text(ADR59) if adr59 is None else adr59
    v = []
    pre = preimage(rel)
    if _sha(pre.encode("utf-8")) != PREIMAGE[rel][1]:
        v.append("the pre-image read at the baseline differs from its pin")
    expected, problems = apply_sites(pre, sites)
    v += problems
    if expected != present:
        v.append("the bytes are not the exact authorised post-image")
    for label, _, new in sites:
        if present.count(new) != 1:
            v.append("%s: post-image site occurs %d times"
                     % (label, present.count(new)))
    restored, problems = reverse_sites(present, sites)
    v += problems
    if restored != pre:
        v.append("reversing the table does not restore the pre-image")
    rows = part_f(adr59)
    row = None if rows is None else rows.get(rel)
    if row is None:
        v.append("ADR-0059 Part F carries no single row for this source")
    else:
        row_labels, pre_pin, post_pin = row
        if row_labels != labels(sites):
            v.append("Part F names different sites from the edit table")
        if pre_pin != PREIMAGE[rel][1]:
            v.append("Part F pre-image pin differs from the fixed pin")
        if post_pin != _sha(present.encode("utf-8")):
            v.append("Part F post-image pin differs from the bytes")
    return v


def header_state(text):
    return recovery.header_state(text)


def l1_snapshot():
    """(commit, violations). Before the landing commit exists the snapshot
    is the working copy over a HEAD that must be the derived baseline;
    afterwards it is the one commit that added ADR-0059, whose sole parent
    must be the derived baseline. Never a movable ref."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                ADR59).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == LANDING else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["ADR-0059 was added by more than one commit"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [LANDING]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "derived baseline"]
    return adds[0], []


def snapshot_text(commit, rel):
    if commit is None:
        return worktree_text(rel)
    return _lf(committed_bytes(commit, rel)).decode("utf-8")


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", LANDING, commit).split())


def acceptance_state(adr59_text, sob_text):
    """(state, date, violations): both records draft, or both accepted on
    the same date."""
    s59, d59 = header_state(adr59_text)
    ssob, dsob = header_state(sob_text)
    v = []
    if s59 not in ("draft", "accepted"):
        v.append("ADR-0059 header is neither draft nor accepted")
    if (s59, d59) != (ssob, dsob):
        v.append("ADR-0059 and W8-S1-SOB are not in the same acceptance "
                 "state")
    head59 = "\n".join(adr59_text.split("\n")[:8])
    headsob = "\n".join(sob_text.split("\n")[:8])
    if s59 == "draft" and DRAFT_59 not in head59:
        v.append("ADR-0059 draft status line differs")
    if s59 == "accepted" and (ACCEPTED_59 % d59) not in head59:
        v.append("ADR-0059 accepted status line differs")
    if ssob == "draft" and DRAFT_SOB not in headsob:
        v.append("W8-S1-SOB draft status line differs")
    if ssob == "accepted" and (ACCEPTED_SOB % dsob) not in headsob:
        v.append("W8-S1-SOB accepted status line differs")
    return s59, d59, v


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def _entry_span(text, eid):
    start = text.index('      "id": "%s",' % eid)
    end = text.index("\n    }", start)
    return start, end


def _replace_once(text, old, new, what, v):
    if text.count(old) != 1:
        v.append("%s: site occurs %d times" % (what, text.count(old)))
        return text
    return text.replace(old, new)


def new_entry(rel, state, date, content_hash):
    f = NEW_ENTRY_FIELDS[rel]
    return {
        "id": f["id"], "aliases": [], "title": f["title"], "type": f["type"],
        "phase": "W8", "deliverable": None, "path": rel,
        "status": state, "accepted_date": date if state == "accepted" else None,
        "role": f["role"], "governs": [], "depends_on": list(f["depends_on"]),
        "resolves": [], "id_namespaces": [],
        "implementation_permission": "none", "open_decisions": [],
        "content_hash": content_hash, "hash_exclusion_reason": None,
        "errata": [],
    }


def expected_registry(landing_text, hashes, state, date):
    """The exact authorised registry bytes for this landing's state:
    four rebinds with one erratum each, one role rewrite, two appended
    entries, and nothing else."""
    v = []
    t = landing_text
    errata_date = date if state == "accepted" else ERRATA_DRAFT_DATE
    for eid, rel in RECONCILED_ENTRIES:
        start, end = _entry_span(t, eid)
        span = t[start:end]
        span = _replace_once(
            span, '"content_hash": "%s"' % PREIMAGE[rel][1],
            '"content_hash": "%s"' % hashes[rel], eid + " hash", v)
        erratum = _indent(json.dumps({"date": errata_date,
                                      "note": ERRATA[eid]}, indent=2), 8)
        if span.endswith('"errata": []'):
            span = span[:-len("[]")] + "[\n" + erratum + "\n      ]"
        elif span.endswith("\n        }\n      ]"):
            span = (span[:-len("\n      ]")] + ",\n" + erratum
                    + "\n      ]")
        else:
            v.append(eid + ": errata field not found at the entry's end")
        if eid == "W8-D2-DIB":
            span = _replace_once(span, *DIB_ROLE_SITE, what="DIB role", v=v)
        t = t[:start] + span + t[end:]
    tail = "\n    }\n  ]\n}\n"
    if not t.endswith(tail):
        return None, v + ["registry tail differs"]
    added = [new_entry(rel, state, date, hashes[rel]) for rel in (ADR59, SOB)]
    t = (t[:-len(tail)] + "\n    },\n"
         + ",\n".join(_indent(json.dumps(e, indent=2, ensure_ascii=False), 4)
                      for e in added)
         + "\n  ]\n}\n")
    return t, v


# ----------------------------------------- A2 audited prohibition forms
# Every sentence of ADR-0059 and W8-S1-SOB that carries route, disposition,
# token or actor vocabulary must be exactly one of the audited forms below,
# each audited as a prohibition or a non-grant. A grant cannot hide behind
# an unrelated negation: an unaudited sentence is refused whatever else it
# says, and a missing audited form is refused too. ADR-0058's R3 and R4 are
# not changed by this local contract.
ROUTE_VOCABULARY = re.compile(
    recovery.ROUTE.pattern
    + r"|\b(dispositions?|tokens?)\b"
    r"|\b(another|second|alternate|alternative|independent|replacement|"
    r"additional|different|other) (human|person|people|party|reviewer|"
    r"individual|authority|source)\b"
    r"|\bon (its|their|his|her|the reviewer's|the human authority's) "
    r"behalf\b|\bin place of\b|\bproxy\b|\bstand-in\b",
    re.IGNORECASE)


def route_sentences(text):
    return [s for s in recovery.sentences(text)
            if ROUTE_VOCABULARY.search(s)]


def route_violations(text, audited):
    found, expected = Counter(route_sentences(text)), Counter(audited)
    v = ["unaudited sentence: %s" % s[:72]
         for s in sorted((found - expected).elements())]
    v += ["audited form missing: %s" % s[:72]
          for s in sorted((expected - found).elements())]
    return v


AUDITED_ROUTE_FORMS = {
    ADR59: (
        ("**It authors no case, generates no nonce, writes no retained "
         "record, touches no custody location, renders no packet, holds no "
         "session, records no disposition, reproduces no commitment, reveals "
         "nothing, compares nothing, counts nothing and contacts no model.** "
         "D3-C stays open and blocked until the supplementary corpus is "
         "effective;"),
        ("**What separately governed authority lets W8-D3 hold a lawful "
         "blind session after ADR-0058 — with the human authority still the "
         "sole source of every disposition, without reusing anything from "
         "the void attempt, without unsealing the original corpus, and with "
         "every changed law and proof bound to an exact, provable "
         "transformation?**"),
        ("**Nothing else is authorised by this record — no case, nonce, "
         "retained record, custody exercise, packet, session, disposition, "
         "reproduction, reveal, comparison or count.**"),
        ("**The human authority remains the sole source of every "
         "disposition, and ADR-0054 decision 18 and ADR-0057 decision 6 "
         "stand exactly as published.** **This record creates no substitute "
         "reviewer, no delegation mechanism, no new disposition source and "
         "no exception to ADR-0054 decision 18 or ADR-0057 decision 6.**"),
        ("**ADR-0058 decision 5 is operative and is cited, not reopened: no "
         "case-to-disposition association from the void attempt, and no "
         "distribution, position, count or aggregate derived from it, "
         "becomes a source for any act this record permits, supplementary "
         "authoring included.** This record carries no such association or "
         "figure and names no case."),
        ("**Identities, as design conventions that confer no disposition "
         "authority and encode no class:** corpus label `W8-S1`;"),
        ("The disposition-law proof module and its sentinel-only, "
         "mechanics-only remit (K11) are not expanded."),
        ("**The conduct interval runs from the reviewer's first access to "
         "any case material of the supplementary corpus, in any form and "
         "including review of that corpus's authoring candidate, until the "
         "session record is published, including the whole interval in which "
         "a returned token may still be revised.** Throughout it, ADR-0057 "
         "decision 8's exclusions carry whole: no authored class, intended "
         "disposition, construction map, authoring check, rationale, "
         "inconclusive-condition selection, nonce, expected distribution, "
         "class count, aggregate, recommendation, default, ranking, "
         "highlight, summary, diff or mechanical inference reaches the "
         "reviewer — **and no case-level judgment, preferred or predicted "
         "disposition or rationale about any case reaches the reviewer from "
         "anyone other than the reviewer.** The withheld-material and "
         "composition prohibitions bind throughout authoring and custody as "
         "well, not only from a packet's arrival."),
        ("structural completeness, one lawful token returned for every case, "
         "without any per-token tally or distribution before the reveal "
         "landing;"),
        ("and source-grounded clarification of governing law that names no "
         "case and suggests no disposition.** **Sharing material with the "
         "architect or implementer for those purposes alone is not itself a "
         "breach.**"),
        ("It uses none of the void attempt's associations, derived "
         "distributions or purported answers, does not adapt the original "
         "cases, and does not use them as a template.** Authoring assistance "
         "creates no reviewer and no disposition route, and its visible "
         "reports expose no authored class, intended token, construction "
         "map, rationale or class count."),
        ("**Textual non-reuse and identity checks support freshness, but "
         "they establish textual non-reuse and distinct identities only, "
         "never semantic independence.** **The reviewer has seen case-level "
         "disposition material for the original corpus, and broader "
         "influence from that prior exposure cannot be mechanically "
         "excluded.** This record removes case-level exposure for the "
         "supplement and claims no more."),
        ("**At the session landing:** the disposition-law module's K12 "
         "register limb and register-schema homes admit exactly the "
         "published register;"),
        "**No green proof supplies a disposition or completes D3-C.**",
        ("| **A2** | No reviewer route: every sentence of this record and "
         "the brief that carries route, disposition or actor vocabulary is "
         "exactly one of a closed, audited set of prohibition and non-grant "
         "forms, so an unrelated negation conceals nothing;"),
        ("| **A3** | No case identity, disposition token, reserved schema "
         "literal or reserved authoring label, and no digest-shaped string "
         "except the Part F pins, in this record, the brief, or the board "
         "and registry wording this landing adds | **Mechanical** |"),
        ("**This landing's census is exactly ten paths:** NEW "
         "`docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md` "
         "· NEW `docs/phases/W8-S1-supplementary-opening-brief.md` · NEW "
         "`tests/test_w8_recovery_authority.py` · MODIFY "
         "`docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md` "
         "· MODIFY "
         "`docs/decisions/0057-w8-disposition-reveal-calibration-law.md` · "
         "MODIFY `docs/phases/W8-D3-synthetic-calibration-brief.md` · MODIFY "
         "`docs/phases/W8-D2-discriminating-instrument-brief.md` · MODIFY "
         "`tests/test_w8_session_recovery_law.py` · MODIFY "
         "`governance/registry.json` · MODIFY `docs/phases/README.md`."),
        ("**Every A-row proves mechanics and carriage only.** No proof "
         "decides, predicts or hints at any disposition, any authored intent "
         "or any relation, and no green result is evidence about any case, "
         "any reviewer, the reviewer's independence or the void attempt's "
         "material."),
        ("This record establishes no case, no corpus, no nonce, no retained "
         "record, no custody exercise, no packet, no session, no "
         "disposition, no register instance, no commitment reproduction, no "
         "reveal, no comparison and no count;"),
        ("no reviewer route, designation, delegation or substitute of any "
         "kind;"),
        ("**No disposition ever made may cite this record as evidence for "
         "any of those propositions.**"),
    ),
    SOB: (
        ("On its acceptance, publication and independent remote verification "
         "together with ADR-0059 — and only then — **exactly one "
         "supplementary corpus, `W8-S1`, opens for authoring work only, "
         "through the one authoring landing of section 4.** This brief "
         "itself authors no case, generates no nonce, writes no retained "
         "record, touches no custody location and authorises no session, "
         "disposition, reveal, comparison, count or contact surface."),
        ("Effective `W8-S1-SOB` does **not** mean: that any case, nonce or "
         "retained record exists or may be created before the human "
         "authority's explicit instruction to prepare the authoring "
         "candidate · that any session may begin · that any disposition "
         "exists or may be inferred · that any reveal, comparison or count "
         "is authorised · that the original corpus's custody may be touched "
         "· or that any model contact is authorised."),
        ("**Authoring assistance creates no reviewer and no disposition "
         "route.** Its visible reports expose no authored class, intended "
         "token, construction map, rationale or class count;"),
        ("**The architect's review of the authoring candidate is law and "
         "mechanics review only: ADR-0057 decision 6 and the D3 brief's "
         "section 2 item 4 stand unchanged, and the architect gives no "
         "likely disposition, case-level judgment, ranking or preferred "
         "outcome to anyone, by any route.** A case-free architect outcome "
         "establishes law and mechanics review only — never semantic "
         "freshness and never the absence of influence."),
        "No finding of any kind is ever a disposition or a recommendation.",
        ("**Does not authorise:** a session, a packet, a disposition, a "
         "reveal, a comparison or a count;"),
        ("| the authoring candidate | the twelve visible supplementary "
         "cases, for the reviewer's own landing review | any withheld byte, "
         "class, intended token, construction map, rationale or class count;"),
        ("This brief does not authorise: a second supplementary corpus · any "
         "change to a W8-D2 artefact or to W8-D2's completion, except the "
         "one authorised proof succession of section 4 item 13 — the "
         "envelope module's case-home limb, exactly as ADR-0059 Part G "
         "stages it — with the original cases, manifest, commitments, "
         "completion record and register unchanged · any act on the original "
         "corpus's retained records, or on their custody, retirement or "
         "reveal, public identity, integrity and textual non-reuse checks "
         "over its published cases and manifest excepted · any session, "
         "packet, disposition, reveal, comparison or count · any score, "
         "rate, grade, ranking, pass/fail, winner, model verdict or "
         "readiness claim · any instrument validation, mutation, near-miss "
         "or adversarial work (W8-D4) · any adequacy judgement (W8-D5) · any "
         "contact decision (W8-D6) · any closure (W8-D7) · any disclosure of "
         "a custody location."),
    ),
}


# --------------------------------------------- A10 the validation chain
# ADR-0059 decision 10, in order. Each step refuses missing, malformed,
# empty and duplicate input before the next step may run, and every step
# after the corpus step is proven against the validated corpus only.
CASE_ID = re.compile(r"^W8-C-[0-9a-f]{64}$")
OBJECT_ID = re.compile(r"^[0-9a-f]{40}$")
LF_PIN = re.compile(r"^sha256:[0-9a-f]{64}$")
BINDING_FIELDS = (("commit", OBJECT_ID), ("home_tree", OBJECT_ID),
                  ("manifest_sha256", LF_PIN))
REVEAL_GATE = ("session_record_verified", "commitments_reproduced",
               "copies_scanned_clean")


def _id_list_violations(ids, what, allow_empty=False):
    if not isinstance(ids, (list, tuple)):
        return ["%s is missing or not a list" % what]
    v = []
    if not ids and not allow_empty:
        v.append("%s is empty" % what)
    if any(not (isinstance(i, str) and CASE_ID.fullmatch(i)) for i in ids):
        v.append("%s holds a malformed identity" % what)
    names = [i for i in ids if isinstance(i, str)]
    if len(names) != len(set(names)):
        v.append("%s holds a duplicate" % what)
    return v


def binding_violations(recorded, observed):
    """Both bindings carry exactly the three well-formed values, and they
    are equal; a missing or malformed value on either side is refused even
    when both sides agree."""
    v = []
    for side, binding in (("recorded", recorded), ("observed", observed)):
        if (not isinstance(binding, dict)
                or set(binding) != {k for k, _ in BINDING_FIELDS}):
            v.append("the %s binding does not carry exactly the three "
                     "fields" % side)
            continue
        for key, shape in BINDING_FIELDS:
            if not (isinstance(binding[key], str)
                    and shape.fullmatch(binding[key])):
                v.append("the %s %s is missing or malformed" % (side, key))
    if not v:
        v += ["wrong %s" % key for key, _ in BINDING_FIELDS
              if recorded[key] != observed[key]]
    return v


def corpus_violations(manifest_ids, original_ids):
    """The bound manifest: exactly twelve distinct well-formed identities,
    none of them an original-corpus identity."""
    v = _id_list_violations(manifest_ids, "the bound manifest")
    v += _id_list_violations(original_ids, "the original identity set")
    if not v:
        if len(manifest_ids) != SUPPLEMENT_TOTAL:
            v.append("the bound manifest does not hold exactly twelve "
                     "identities")
        if set(manifest_ids) & set(original_ids):
            v.append("the bound manifest overlaps the original corpus")
    return v


def exact_set_violations(ids, manifest_ids, original_ids, what):
    """A set that must equal the validated corpus exactly: no missing,
    extra, duplicate, malformed, original-corpus or mixed member."""
    v = corpus_violations(manifest_ids, original_ids)
    if v:
        return ["the corpus does not validate"] + v
    v = _id_list_violations(ids, what)
    if v:
        return v
    if set(ids) & set(original_ids):
        v.append("%s holds an original-corpus identity" % what)
    if set(ids) - set(manifest_ids) - set(original_ids):
        v.append("%s holds an identity outside the session corpus" % what)
    if set(manifest_ids) - set(ids):
        v.append("%s misses a session-corpus identity" % what)
    return v


def packet_input_violations(rel_paths, manifest_ids, original_ids):
    """Membership before recomputation: the renderer's inputs are exactly
    the validated corpus's case paths in the supplement home."""
    v = corpus_violations(manifest_ids, original_ids)
    if v:
        return ["the corpus does not validate"] + v
    if not isinstance(rel_paths, (list, tuple)) or not rel_paths:
        return ["the packet inputs are missing or empty"]
    if any(not isinstance(p, str) for p in rel_paths):
        return ["the packet inputs hold a malformed path"]
    if len(rel_paths) != len(set(rel_paths)):
        v.append("the packet inputs hold a duplicate")
    expected = sorted("%s/%s.json" % (SUPPLEMENT_HOME, cid)
                      for cid in manifest_ids)
    if sorted(set(rel_paths)) != expected:
        v.append("the packet inputs are not exactly the bound manifest's "
                 "case paths")
    return v


def custody_scope_violations(names_touched, manifest_ids, original_ids):
    """Any operation on retained records touches only well-formed session
    names and never an original retained record; touching nothing is
    lawful scope."""
    v = corpus_violations(manifest_ids, original_ids)
    if v:
        return ["the corpus does not validate"] + v
    v = _id_list_violations(names_touched, "the custody names",
                            allow_empty=True)
    if v:
        return v
    if set(names_touched) & set(original_ids):
        v.append("an original retained record was touched")
    if set(names_touched) - set(manifest_ids) - set(original_ids):
        v.append("a custody name outside the session corpus")
    return v


def reveal_violations(reveal_ids, manifest_ids, original_ids, gate):
    """Before the full gate the lawful reveal set is empty; once the
    session record is published and remote-verified, every commitment is
    reproduced and the exact candidate copies are scanned clean, a reveal
    must be complete and exact."""
    v = corpus_violations(manifest_ids, original_ids)
    if v:
        return ["the corpus does not validate"] + v
    if (not isinstance(gate, dict) or set(gate) != set(REVEAL_GATE)
            or any(not isinstance(gate[k], bool) for k in REVEAL_GATE)):
        return ["the reveal gate is missing or malformed"]
    if not isinstance(reveal_ids, (list, tuple)):
        return ["the reveal set is missing or not a list"]
    if not all(gate.values()):
        return ["a premature reveal"] if reveal_ids else []
    return exact_set_violations(reveal_ids, manifest_ids, original_ids,
                                "the reveal set")


CHAIN_STEPS = ("binding", "corpus", "packet inputs", "register",
               "existence check", "reproduction", "reveal")


def session_chain_violations(c, upto="reveal"):
    """The complete validation chain, in order; the first failing step
    stops it, and missing inputs arrive as None and are refused. A landing
    applies the chain through its own act: the session landing through the
    register and existence check, the reveal landing through the reveal."""
    m, o = c.get("manifest_ids"), c.get("original_ids")
    steps = (
        ("binding", lambda: binding_violations(c.get("recorded_binding"),
                                               c.get("observed_binding"))),
        ("corpus", lambda: corpus_violations(m, o)),
        ("packet inputs", lambda: packet_input_violations(
            c.get("packet_paths"), m, o)),
        ("register", lambda: exact_set_violations(
            c.get("register_ids"), m, o, "the register")),
        ("existence check", lambda: exact_set_violations(
            c.get("existence_names"), m, o, "the existence check")),
        ("reproduction", lambda: exact_set_violations(
            c.get("reproduction_ids"), m, o, "the reproduction set")),
        ("reveal", lambda: reveal_violations(c.get("reveal_ids"), m, o,
                                             c.get("reveal_gate"))),
    )
    assert tuple(n for n, _ in steps) == CHAIN_STEPS
    for name, step in steps[:CHAIN_STEPS.index(upto) + 1]:
        v = step()
        if v:
            return ["%s: %s" % (name, x) for x in v]
    return []


def absence_violations(tracked, exists, entries):
    """Before the supplementary authoring landing: no supplement home,
    manifest, corpus record, corpus proof module or registry entry."""
    v = []
    if [p for p in tracked if p.startswith(SUPPLEMENT_HOME + "/")]:
        v.append("a tracked path in the supplement home")
    if exists(SUPPLEMENT_HOME):
        v.append("the supplement home exists on disk")
    for rel in (SUPPLEMENT_RECORD, SUPPLEMENT_MODULE):
        if rel in tracked or exists(rel):
            v.append("%s exists" % rel)
    for e in entries:
        if (e["id"] in SUPPLEMENT_ENTRIES
                or e["path"].startswith(SUPPLEMENT_HOME + "/")
                or e["path"] in (SUPPLEMENT_RECORD, SUPPLEMENT_MODULE)):
            v.append("registry entry %s" % e["id"])
    return v


def _sentinels(label, n):
    return ["W8-C-" + hashlib.sha256(("%s-%d" % (label, i)).encode())
            .hexdigest() for i in range(n)]


def load_registry():
    return json.loads(worktree_text(REGISTRY))


# ------------------------------------------------------------------ proofs
class A1_Carriage(unittest.TestCase):
    def test_a1_authority_and_brief_carry_their_law(self):
        nine = re.search(r"> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                         r"failure\.\*\*)", worktree_text(A54)).group(1)
        for rel, required in ((ADR59, REQUIRED_59), (SOB, REQUIRED_SOB)):
            flat = _flat(worktree_text(rel))
            for sentence in required:
                with self.subTest(record=rel[-40:], carried=sentence[:44]):
                    self.assertIn(sentence, flat)
            with self.subTest(record=rel[-40:], carried="nine rules"):
                self.assertIn(nine, worktree_text(rel))
            for sentence in required[:3]:
                with self.subTest(control="removing '%s' is detected"
                                          % sentence[:32]):
                    self.assertNotIn(sentence, flat.replace(sentence, ""))


class A2_NoReviewerRoute(unittest.TestCase):
    # Labelled mutation sentences, never governed content.
    UNRELATED_NEGATION = ("An independent human reviewer supplies the "
                          "tokens, with no custody access.")
    MIXED = ("This record creates no substitute reviewer, but an alternate "
             "reviewer may supply the tokens.")
    STANDALONE = "A second human reviewer supplies the dispositions."
    PLAIN_ACTOR = "Another person returns the tokens."

    def test_a2_route_sentences_are_exactly_the_audited_forms(self):
        for rel in (ADR59, SOB):
            text = worktree_text(rel)
            with self.subTest(record=rel[-40:]):
                self.assertEqual(route_violations(text,
                                                  AUDITED_ROUTE_FORMS[rel]),
                                 [])
        self.assertIn(NO_ROUTE_59, _flat(worktree_text(ADR59)))
        sob, a59 = worktree_text(SOB), worktree_text(ADR59)
        with self.subTest(fact="the published negation helper alone misses "
                               "an unrelated negation"):
            self.assertEqual(recovery.unguarded(self.UNRELATED_NEGATION,
                                                recovery.ROUTE), [])
        plants = {
            "an unrelated negation": (SOB, sob + "\n"
                                      + self.UNRELATED_NEGATION),
            "a mixed prohibition and grant": (ADR59, a59 + "\n"
                                              + self.MIXED),
            "a standalone grant": (SOB, sob + "\n" + self.STANDALONE),
            "a grant in plain actor words": (ADR59, a59 + "\n"
                                             + self.PLAIN_ACTOR),
            "an audited prohibition reworded": (ADR59, a59.replace(
                "no substitute reviewer, no delegation",
                "a substitute reviewer, no delegation")),
            "an audited form duplicated": (ADR59, a59 + "\n"
                                           + AUDITED_ROUTE_FORMS[ADR59][0]),
            "an audited form removed": (SOB, sob.replace(
                AUDITED_ROUTE_FORMS[SOB][0], "")),
        }
        for name, (rel, mutated) in plants.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, worktree_text(rel))
                self.assertTrue(route_violations(mutated,
                                                 AUDITED_ROUTE_FORMS[rel]))


class A3_NoExposureOrReservedLiteral(unittest.TestCase):
    SCHEMAS = (packet.PACKET_SCHEMA, calibration.REGISTER_SCHEMA,
               envelope.AUTHORING_SCHEMA, corpus.MANIFEST_SCHEMA)

    def added_wording(self):
        """The registry and board wording this landing added, read from
        its own snapshot so that a later landing's lawful board or registry
        change cannot hide it."""
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        reg = json.loads(snapshot_text(commit, REGISTRY))
        added = [e for e in reg["entries"]
                 if e["id"] in ("ADR-0059", "W8-S1-SOB")]
        errata = [x["note"] for e in reg["entries"]
                  for x in e["errata"] if "ADR-0059" in x["note"]]
        board = snapshot_text(commit, BOARD)
        rows = [l for l in board.split("\n")
                if l.startswith((ROW59, ROWSOB))]
        status = [s for s in BOARD_STATUS.values()
                  if (s.split("**")[1]) in board]
        return {"registry roles": " ".join(e["role"] + " " + e["title"]
                                           for e in added),
                "registry errata": " ".join(errata),
                "board rows": "\n".join(rows),
                "board status": " ".join(status)}

    def test_a3_no_case_token_schema_or_unpinned_digest(self):
        pins = [p.split(":", 1)[1] for _, p, _ in PREIMAGE.values()]
        pins += [_sha(worktree_text(rel).encode("utf-8")).split(":", 1)[1]
                 for rel in (A55, A57, SCB, DIB, R58)]
        surfaces = {"ADR-0059": (worktree_text(ADR59), pins),
                    "W8-S1-SOB": (worktree_text(SOB), [])}
        surfaces.update({k: (t, []) for k, t in self.added_wording().items()})
        for name, (text, allowed) in surfaces.items():
            with self.subTest(surface=name):
                self.assertTrue(text)
                self.assertEqual(recovery.exposure_violations(text, allowed),
                                 [])
                self.assertEqual([s for s in self.SCHEMAS if s in text], [])
                self.assertEqual(corpus.reserved_channel_hits(text), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertEqual([s for s in self.SCHEMAS if s in src], [])
            self.assertEqual([t for t in packet.TOKENS if t in src], [])
            self.assertIsNone(recovery.CASE_ID_ANYWHERE.search(src))
        clean = worktree_text(ADR59)
        for name, plant in {"a case identity": _sentinels("plant", 1)[0],
                            "a bare digest": "c" * 64,
                            "a disposition token": packet.TOKENS[0]}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(recovery.exposure_violations(
                    clean + "\n" + plant, pins))


class A4_ExactReconciliations(unittest.TestCase):
    def test_a4_each_reconciled_source_is_its_exact_post_image(self):
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        for eid, rel in RECONCILED_ENTRIES:
            with self.subTest(baseline_object=eid):
                self.assertEqual(
                    _git("rev-parse", LANDING + ":" + rel).strip(),
                    PREIMAGE[rel][2])
            with self.subTest(at_this_landing=eid):
                self.assertEqual(reconciliation_violations(
                    rel, snapshot_text(commit, rel),
                    snapshot_text(commit, ADR59)), [])
            with self.subTest(present_state=eid):
                self.assertEqual(reconciliation_violations(rel), [])
                self.assertEqual(by_id[eid]["content_hash"],
                                 lf_hash(ROOT / rel))
        with self.subTest(fact="Part F names exactly the five sources"):
            self.assertEqual(set(part_f(worktree_text(ADR59)) or {}),
                             {A55, A57, SCB, DIB, R58})
        rel = A57
        text, sites = worktree_text(rel), SITES[rel]
        label, old, new = sites[0]
        controls = {
            "an extra byte": (text + " ", sites),
            "a missing site": (text, sites[1:]),
            "an altered site": (text.replace(new, new.replace(
                "session corpus", "session  corpus")), sites),
            "a duplicated site": (text + "\n" + new, sites),
            "a self-consistent but unpinned edit": (
                text.replace(PUBLIC_SAFETY, "\nplanted\n" + PUBLIC_SAFETY),
                sites + (("planted", PUBLIC_SAFETY,
                          "\nplanted\n" + PUBLIC_SAFETY),)),
        }
        for name, (present, table) in controls.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(reconciliation_violations(
                    rel, present=present, sites=table))


class A5_RecoveryModuleChangesInR5Only(unittest.TestCase):
    def test_a5_the_adr0058_module_moves_exactly_as_pinned(self):
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        with self.subTest(baseline_object="ADR-0058 proof module"):
            self.assertEqual(_git("rev-parse", LANDING + ":" + R58).strip(),
                             PREIMAGE[R58][2])
        with self.subTest(at_this_landing="R5 only"):
            self.assertEqual(reconciliation_violations(
                R58, snapshot_text(commit, R58),
                snapshot_text(commit, ADR59)), [])
            self.assertEqual(labels(SITES[R58]), ("R5",))
        with self.subTest(fact="the module's own succession constants"):
            self.assertEqual(recovery.LANDING, LANDING)
            self.assertEqual(recovery.RECONCILED_BY_ADR_0059,
                             set(RECONCILED_LAW))
            self.assertEqual(set(RECONCILED_LAW.values()), {A55, A57, SCB})
        with self.subTest(control="an edit outside R5 is refused"):
            text = snapshot_text(commit, R58)
            self.assertTrue(reconciliation_violations(
                R58, text.replace("class R6_", "class R6x_"),
                snapshot_text(commit, ADR59)))


class A6_BoardTransformation(unittest.TestCase):
    def test_a6_board_changes_exactly_at_authorised_sites(self):
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        state, date, v = acceptance_state(snapshot_text(commit, ADR59),
                                          snapshot_text(commit, SOB))
        self.assertEqual(v, [])
        board = snapshot_text(commit, BOARD)
        pre = preimage(BOARD)
        with self.subTest(fact="the board pre-image is the pinned one"):
            self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[BOARD][1])
        expected, problems = apply_sites(pre, board_sites(state, date))
        with self.subTest(fact="exact authorised board", state=state):
            self.assertEqual(problems, [])
            self.assertEqual(board, expected)
        with self.subTest(fact="ADR-0058's anchors and absence sentences"):
            self.assertEqual(recovery.board_surfaces(board)[2], [])
            self.assertIn("No session, disposition, reveal or calibration "
                          "exists yet.", board)
            self.assertIn(corpus.COUNT_SENTENCE, board)
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            wrong, _ = apply_sites(pre, board_sites(other, "2000-01-01"))
            self.assertNotEqual(board, wrong)
        with self.subTest(control="an unauthorised board edit is refused"):
            self.assertNotEqual(board.replace("W8-D2 is complete as built",
                                              "W8-D2 is complete"), expected)


class A7_RegistryTransformation(unittest.TestCase):
    def test_a7_registry_changes_exactly_as_authorised(self):
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        state, date, v = acceptance_state(snapshot_text(commit, ADR59),
                                          snapshot_text(commit, SOB))
        self.assertEqual(v, [])
        landing = preimage(REGISTRY)
        with self.subTest(fact="the registry pre-image is the pinned one"):
            self.assertEqual(_sha(landing.encode("utf-8")),
                             PREIMAGE[REGISTRY][1])
        hashes = {rel: _sha(snapshot_text(commit, rel).encode("utf-8"))
                  for rel in (A55, A57, SCB, DIB, ADR59, SOB)}
        expected, problems = expected_registry(landing, hashes, state, date)
        present = snapshot_text(commit, REGISTRY)
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(problems, [])
            self.assertEqual(present, expected)
            json.loads(present)
        with self.subTest(fact="only the authorised entries differ"):
            before = {e["id"]: e for e in json.loads(landing)["entries"]}
            after = {e["id"]: e for e in json.loads(present)["entries"]}
            changed = {k for k in before if before[k] != after.get(k)}
            self.assertEqual(changed, {eid for eid, _ in RECONCILED_ENTRIES})
            self.assertEqual(set(after) - set(before),
                             {"ADR-0059", "W8-S1-SOB"})
            for eid, _ in RECONCILED_ENTRIES:
                keys = {k for k in after[eid] if after[eid][k] != before[eid][k]}
                allowed = {"content_hash", "errata"} | (
                    {"role"} if eid == "W8-D2-DIB" else set())
                self.assertEqual(keys, allowed)
        for name, mutated in {
                "an extra role edit": present.replace(
                    "The W8-D3 opening brief, opening W8-D3",
                    "The W8-D3 opening brief, now opening W8-D3"),
                "a dropped erratum": present.replace(
                    json.dumps(ERRATA["ADR-0057"]), '"x"'),
                "a wrong status": present.replace(
                    '"id": "ADR-0059"', '"id": "ADR-0059x"')}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, expected)


class A8_LandingCensus(unittest.TestCase):
    def test_a8_census_is_exactly_the_ten_paths(self):
        commit, problems = l1_snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        self.assertEqual(paths, set(CENSUS))
        with self.subTest(fact="no other proof module changed"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {R58, SELF_REL})
        with self.subTest(fact="decision 34 names the same ten paths"):
            flat = _flat(snapshot_text(commit, ADR59))
            m = re.search(r"34\. \*\*This landing's census is exactly ten "
                          r"paths:\*\* (.*?)\n?35\. ", flat + "\n35. ")
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(CENSUS))


class A9_NothingSupplementaryYet(unittest.TestCase):
    def test_a9_no_supplementary_artefact_before_its_landing(self):
        tracked = _git("ls-files").split()
        exists = lambda rel: (ROOT / rel).exists()
        entries = load_registry()["entries"]
        self.assertEqual(absence_violations(tracked, exists, entries), [])
        planted = {
            "a tracked case path": (tracked + [SUPPLEMENT_HOME + "/x.json"],
                                    exists, entries),
            "a home on disk": (tracked, lambda r: r == SUPPLEMENT_HOME,
                               entries),
            "a corpus record": (tracked + [SUPPLEMENT_RECORD], exists,
                                entries),
            "a manifest register entry": (tracked, exists, entries + [
                {"id": "W8-S1-CM-01", "path": SUPPLEMENT_HOME + "/m.json"}]),
        }
        for name, args in planted.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(absence_violations(*args))


class A10_ValidationChain(unittest.TestCase):
    """Sentinel identities only — labelled mechanics fixtures, never cases."""

    def good_chain(self):
        session = _sentinels("sentinel-session", SUPPLEMENT_TOTAL)
        original = _sentinels("sentinel-original", SUPPLEMENT_TOTAL)
        binding = {"commit": "a" * 40, "home_tree": "b" * 40,
                   "manifest_sha256": "sha256:" + "c" * 64}
        return {
            "recorded_binding": dict(binding),
            "observed_binding": dict(binding),
            "manifest_ids": list(session), "original_ids": list(original),
            "packet_paths": ["%s/%s.json" % (SUPPLEMENT_HOME, c)
                             for c in session],
            "register_ids": list(session), "existence_names": list(session),
            "reproduction_ids": list(session), "reveal_ids": list(session),
            "reveal_gate": {k: True for k in REVEAL_GATE},
        }

    def test_a10_the_chain_refuses_what_it_must(self):
        good = self.good_chain()
        session, original = good["manifest_ids"], good["original_ids"]
        self.assertEqual(session_chain_violations(good), [])
        for upto in CHAIN_STEPS:
            with self.subTest(fact="the chain prefix through %s is clean"
                                   % upto):
                self.assertEqual(session_chain_violations(good, upto), [])
        dup_manifest = session[:SUPPLEMENT_TOTAL - 1] + session[:1]
        # Whole-string shape: a terminal newline is malformed on every
        # field and identity, even when both sides or every set agree.
        nl = [c + "\n" for c in session]
        newline_chain = {
            "manifest_ids": nl,
            "packet_paths": ["%s/%s.json" % (SUPPLEMENT_HOME, c) for c in nl],
            "register_ids": list(nl), "existence_names": list(nl),
            "reproduction_ids": list(nl), "reveal_ids": list(nl)}
        newline_binding = {
            field: {side: dict(good[side], **{field: good[side][field]
                                                + "\n"})
                    for side in ("recorded_binding", "observed_binding")}
            for field in ("commit", "home_tree", "manifest_sha256")}
        mutations = {
            "a trailing newline in both commits": (
                newline_binding["commit"], "binding"),
            "a trailing newline in both home trees": (
                newline_binding["home_tree"], "binding"),
            "a trailing newline in both manifest pins": (
                newline_binding["manifest_sha256"], "binding"),
            "consistently newline-terminated identities across the chain": (
                newline_chain, "corpus"),
            "newline-terminated original identities": (
                {"original_ids": [c + "\n" for c in original]}, "corpus"),
            "one newline-terminated register row": (
                {"register_ids": session[1:] + [session[0] + "\n"]},
                "register"),
            # (label): (field changes, the step that must refuse)
            "a duplicated manifest identity": (
                {"manifest_ids": dup_manifest}, "corpus"),
            "both bindings all None": (
                {"recorded_binding": dict.fromkeys(good["recorded_binding"]),
                 "observed_binding": dict.fromkeys(
                     good["observed_binding"])}, "binding"),
            "recorded None, observed empty": (
                {"recorded_binding": dict.fromkeys(good["recorded_binding"]),
                 "observed_binding": {}}, "binding"),
            "a missing binding": ({"recorded_binding": None}, "binding"),
            "a malformed tree identity": (
                {"observed_binding": dict(good["observed_binding"],
                                          home_tree="HEAD"),
                 "recorded_binding": dict(good["recorded_binding"],
                                          home_tree="HEAD")}, "binding"),
            "an extra binding field": (
                {"observed_binding": dict(good["observed_binding"],
                                          extra="x")}, "binding"),
            "a wrong commit": (
                {"observed_binding": dict(good["observed_binding"],
                                          commit="d" * 40)}, "binding"),
            "a wrong manifest pin": (
                {"observed_binding": dict(
                    good["observed_binding"],
                    manifest_sha256="sha256:" + "e" * 64)}, "binding"),
            "an empty manifest": ({"manifest_ids": []}, "corpus"),
            "a missing manifest": ({"manifest_ids": None}, "corpus"),
            "a malformed manifest identity": (
                {"manifest_ids": session[1:] + ["W8-C-xyz"]}, "corpus"),
            "an eleven-case manifest": ({"manifest_ids": session[1:]},
                                        "corpus"),
            "a manifest overlapping the original": (
                {"manifest_ids": session[1:] + original[:1]}, "corpus"),
            "empty packet paths": ({"packet_paths": []}, "packet inputs"),
            "missing packet paths": ({"packet_paths": None},
                                     "packet inputs"),
            "a duplicated packet path": (
                {"packet_paths": good["packet_paths"]
                 + good["packet_paths"][:1]}, "packet inputs"),
            "an original-home packet path": (
                {"packet_paths": good["packet_paths"][:-1] + [
                    "%s/%s.json" % (ORIGINAL_HOME, session[-1])]},
                "packet inputs"),
            "a wrong-manifest packet path": (
                {"packet_paths": good["packet_paths"][:-1] + [
                    "%s/%s.json" % (SUPPLEMENT_HOME, original[0])]},
                "packet inputs"),
            "a missing register row": ({"register_ids": session[1:]},
                                       "register"),
            "a duplicated register row": (
                {"register_ids": session + session[:1]}, "register"),
            "an original-corpus register row": (
                {"register_ids": session[1:] + original[:1]}, "register"),
            "a mixed register": ({"register_ids": session[:6] + original[:6]},
                                 "register"),
            "an empty existence check": ({"existence_names": []},
                                         "existence check"),
            "an existence check naming an original record": (
                {"existence_names": session + original[:1]},
                "existence check"),
            "a short reproduction set": ({"reproduction_ids": session[:11]},
                                         "reproduction"),
            "an empty reveal after the gate": ({"reveal_ids": []}, "reveal"),
            "a duplicated identity in a complete reveal": (
                {"reveal_ids": session + session[:1]}, "reveal"),
            "a partial reveal": ({"reveal_ids": session[:6]}, "reveal"),
            "an original-corpus reveal": ({"reveal_ids": original},
                                          "reveal"),
            "a missing reveal gate": ({"reveal_gate": None}, "reveal"),
            "a reveal before the copies scan clean": (
                {"reveal_gate": dict(good["reveal_gate"],
                                     copies_scanned_clean=False)}, "reveal"),
            "a reveal on remote verification alone": (
                {"reveal_gate": {"session_record_verified": True,
                                 "commitments_reproduced": False,
                                 "copies_scanned_clean": False}}, "reveal"),
        }
        for name, (change, step) in mutations.items():
            with self.subTest(control="%s is refused at the %s step"
                                      % (name, step)):
                v = session_chain_violations(dict(good, **change))
                self.assertTrue(v)
                self.assertTrue(v[0].startswith(step + ": "), v[0])
        with self.subTest(fact="before the gate, the lawful reveal set is "
                               "empty"):
            closed = {k: False for k in REVEAL_GATE}
            self.assertEqual(session_chain_violations(
                dict(good, reveal_ids=[], reveal_gate=closed)), [])
        with self.subTest(control="before the gate, any reveal is "
                                  "premature"):
            closed = {k: False for k in REVEAL_GATE}
            self.assertTrue(session_chain_violations(
                dict(good, reveal_gate=closed)))
        with self.subTest(fact="custody scope: session names only, never "
                               "an original retained record"):
            self.assertEqual(custody_scope_violations([], session, original),
                             [])
            self.assertEqual(custody_scope_violations(session[:3], session,
                                                      original), [])
            for name, names in {
                    "an original retained record": session[:3] + original[:1],
                    "a malformed name": ["W8-C-zz"],
                    "a missing list": None,
                    "a duplicated name": session[:1] * 2,
                    "a newline-terminated session name": [session[0] + "\n"],
                    "a newline-terminated original name": [
                        original[0] + "\n"]}.items():
                with self.subTest(control="custody scope refuses %s" % name):
                    self.assertTrue(custody_scope_violations(names, session,
                                                             original))
            with self.subTest(control="custody scope refuses newline-"
                                      "terminated original identities"):
                self.assertTrue(custody_scope_violations(
                    session[:1], session, [o + "\n" for o in original]))
        with self.subTest(fact="malformed values are refused, never "
                               "normalised"):
            raw = [session[0] + "\n"]
            self.assertTrue(_id_list_violations(raw, "the sentinel set"))
            self.assertEqual(raw, [session[0] + "\n"])
            self.assertEqual(_id_list_violations([session[0]],
                                                 "the sentinel set"), [])
            pinned = dict(good["recorded_binding"])
            self.assertTrue(binding_violations(
                dict(pinned, commit=pinned["commit"] + "\n"),
                dict(pinned, commit=pinned["commit"] + "\n")))
            self.assertEqual(pinned, good["recorded_binding"])


class A11_ConductCarriage(unittest.TestCase):
    def test_a11_exclusions_carry_whole_over_the_extended_interval(self):
        a57 = _flat(worktree_text(A57))
        scb = _flat(worktree_text(SCB))
        a59 = _flat(worktree_text(ADR59))
        checks = {
            "ADR-0057 decision 8": (a57, (
                "No " + EXCLUSIONS, CASE_LEVEL,
                "from the reviewer's first access to any case material of "
                "the session corpus",
                "until the session record is published, including the whole "
                "interval in which a returned token may still be revised.",
                PERMITTED, NOT_A_BREACH)),
            "the D3 brief's blinding item": (scb, (
                "No " + EXCLUSIONS, CASE_LEVEL,
                "Blinding holds from the reviewer's first access to any case "
                "material of the session corpus, in any form, until the "
                "session record is published.")),
            "ADR-0059": (a59, (
                "no " + EXCLUSIONS, CASE_LEVEL, PERMITTED,
                NOT_A_BREACH)),
        }
        for name, (text, needed) in checks.items():
            for s in needed:
                with self.subTest(source=name, carried=s[:40]):
                    self.assertIn(s, text)
        with self.subTest(control="dropping one exclusion is detected"):
            self.assertNotIn("No " + EXCLUSIONS,
                             a57.replace("highlight, ", ""))
        with self.subTest(fact="ADR-0057 decision 6 is unchanged"):
            d6 = re.search(r"\n6\. .*", preimage(A57)).group(0)
            self.assertIn(d6, worktree_text(A57))


class A12_Registration(unittest.TestCase):
    def test_a12_registered_with_matching_hash_and_status(self):
        by_id = {e["id"]: e for e in load_registry()["entries"]}
        for rel in (ADR59, SOB):
            f = NEW_ENTRY_FIELDS[rel]
            e = by_id.get(f["id"])
            text = worktree_text(rel)
            state, date = header_state(text)
            with self.subTest(entry=f["id"]):
                self.assertIsNotNone(e)
                self.assertEqual((e["path"], e["type"], e["phase"],
                                  e["deliverable"]),
                                 (rel, f["type"], "W8", None))
                self.assertEqual(e["content_hash"], lf_hash(ROOT / rel))
                self.assertIn(state, ("draft", "accepted"))
                self.assertEqual((e["status"], e["accepted_date"]),
                                 (state, date))
                self.assertTrue(NEW_ENTRY_DEPENDENCIES[f["id"]]
                                <= set(e["depends_on"]))
            with self.subTest(control="the opposite status is refused",
                              entry=f["id"]):
                flipped = ("accepted", "2000-01-01") if state == "draft" \
                    else ("draft", None)
                self.assertNotEqual((e["status"], e["accepted_date"]),
                                    flipped)
        state, date, v = acceptance_state(worktree_text(ADR59),
                                          worktree_text(SOB))
        with self.subTest(fact="one acceptance state for both records"):
            self.assertEqual(v, [])
        with self.subTest(control="split acceptance states are refused"):
            sob = recovery.with_status_line(
                worktree_text(SOB), ACCEPTED_SOB % "2000-01-01"
                if state == "draft" else DRAFT_SOB)
            self.assertTrue(acceptance_state(worktree_text(ADR59), sob)[2])
        with self.subTest(fact="green-does-not-mean clauses are carried"):
            flat = _flat(__doc__)
            for clause in ("that any supplementary case exists, is fresh or "
                           "is semantically independent of anything",
                           "the reviewer's prior exposure or the absence of "
                           "influence",
                           "that any custody record exists, is intact or was "
                           "never touched",
                           "which only the human acceptance act supplies"):
                self.assertIn(clause, flat)


if __name__ == "__main__":
    unittest.main()
