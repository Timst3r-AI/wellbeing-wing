"""W8-D5-B — evidence-adequacy review law proofs (ADR-0061, EL1–EL9).

The review law that the effective W8-D5 opening brief places at D5-B, before
any finding: the review question, the reception threshold, the criteria and
the finding form carried byte-identically from the brief; the finding
record's shape; the attribution of assistance; the evidence index - every
admissible item of the brief's item 14 by published path and commit, bound
to its bytes and carrying no judgement; and the closed, staged succession of
the finding landing. This module proves the law's carriage and its closed
lists byte-identical to the effective brief's; its withholding and its
non-authorisations as one whole block; its exposure limits, applied over the
law's logical prose paragraphs so that wrapping hides nothing, with the
succession row and the index rows as the only digest exemptions; the index
exactly its trusted rows, each object bound at its cited commit and at the
baseline; that every fixed home, record and module is byte-unchanged; the
exact EA7 succession and its table; the staged absences; and the exact
registry, board and census - each with planted-mutant or negative controls.
Closed validators compare against trusted expected values held here and
refuse unrecognised material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the law
afterwards - and executes the helpers it relies on, the opening module among
them, from that snapshot's bytes, in a private namespace. EL7's staged
absences were the present-state gates until the finding landing (D5-C)
succeeded them under ADR-0061 Part J: each former absence stays proven at
this landing's own snapshot, and the admission of exactly the finding
record, its proof module and the one W8-D5 entry that landing added - and
still no W8-D6 or W8-D7 entry - is proven at that landing's own fixed
snapshot. No present-state gate remains: W8-D6 and W8-D7 stay refused by
ADR-0058's R9 alone. The residual live reach is disclosed exactly: each
snapshot-executed helper module imports, at its own top level,
the live modules it aliases for the fixed-law values it reads from them, and
no more independence than that is claimed.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity, token
name, schema literal or method label as a literal: the lists it checks are
the opening module's pins, executed from the snapshot. It performs no review
and makes no finding.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any adequacy finding, or which finding is right; any
answer to the reception threshold or to any criterion; that the instrument
is mature, valid or ready; that model contact would or would not add useful
evidence; anything about any case, disposition, divergence or reviewer;
that any model was contacted; or that W8-D6 or W8-D7 may open.
"""

import hashlib
import importlib
import json
import re
import subprocess
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

# The published, remotely verified W8-D5 opening brief: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "c8e13d47f305e0378609ffec1d31f890f629239d"

LAW = "docs/decisions/0061-w8-evidence-adequacy-review-law.md"
SELF_REL = "tests/test_w8_evidence_adequacy_law.py"
OPENING = "tests/test_w8_evidence_adequacy_opening.py"
BRIEF = "docs/phases/W8-D5-evidence-adequacy-brief.md"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
FIXED_CENSUS = frozenset({LAW, SELF_REL, OPENING, REGISTRY, BOARD})
D5_ENTRIES = frozenset({"W8-D5-EAB", "ADR-0061"})
LATER_THAN_D5 = ("W8-D6", "W8-D7")
# The finding landing's artefacts: the record's identity and path are fixed
# by ADR-0061 decision 17, the landing's order and scope by decisions 27 and
# 34; both absent until that landing.
FINDING_RECORD = "docs/phases/W8-D5-adequacy-finding-record.md"
FINDING_MODULE = "tests/test_w8_evidence_adequacy_finding.py"
# The finding landing's one W8-D5 entry, admitted with the record and its
# module once that landing succeeded EL7's staged absences (Part J).
FINDING_ENTRY = "W8-D5-AFR"
D5_ENTRIES_AT_FINDING = D5_ENTRIES | {FINDING_ENTRY}
FIXED_HOMES = ("governance/validation-cases", "governance/validation-review",
               "governance/validation-reveal",
               "governance/discriminating-instrument",
               "governance/discriminating-supplement",
               "governance/discriminating-reveal",
               "governance/discriminating-review")
FIXED_RECORD_IDS = ("W8-AR", "ADR-0046", "ADR-0047", "ADR-0054", "ADR-0055",
                    "ADR-0057", "ADR-0058", "ADR-0059", "ADR-0060",
                    "W8-D2-DIB", "W8-D2-DIC", "W8-D3-SCB", "W8-S1-SOB",
                    "W8-S1-SCR", "W8-D3-HDR", "W8-D3-CCR", "W8-D4-IVB",
                    "W8-D4-VCR", "W8-D4-VSR", "W8-D4-VRC", "W8-D4-CPR",
                    "W8-CHC", "W8-DER", "W8-D5-EAB")
FIXED_MODULES = (RECOVERY,)
CASE_HOMES = ("governance/discriminating-supplement", "governance/validation-cases")
BULLETS = ("1", "2", "3", "4", "5", "6")

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py",
           "ea": OPENING}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    OPENING: ("opening module",
              "sha256:84df93a8e79ec5ffe477756e126993b240d57ee2f848019ddce8191071f61a61",
              "63f11f27a77b945809aa03b960ea7c3b157f4ece"),
    REGISTRY: ("registry",
               "sha256:fddcf9393bcf9e0fc8d2812e6c12cf6762e47434dab2a5e84859700e775ac163",
               "1e964a09c17a0e2f52fb37a2051962cfe3417613"),
    BOARD: ("board",
            "sha256:155455afd19d7a0cedb4e0684b2d92694206e6159d80ad4bb5f33dc2cb4c7d1d",
            "52b6bf768a1804c839c198ab43b680507f7a9e3c"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {OPENING: ("sha256:bb118225a9ae95a48a3424b997202fe29e154ab655888dea45e2a44fcdfa56b7", "3f4618de92871e3470d33737f2a03cb5f1a71911")}

# ------------------------------------------ the one succession: EA7's gate
# The one proof succession the W8-D5-B landing proposes: EA7's present-state
# W8-D5 entry set moves to the review-law proof module and stays proven at the
# D5-A landing commit. Three sites, each an exact transformation of the
# opening module's fixed pre-image at c8e13d47. OPENING is the module's path.
SITES = {OPENING: (
    ("EA7",
     "bytes, in a private namespace. The one present-state gate is EA7's W8-D5\n"
     "entry set, which the review law's landing is expected to move, as the\n"
     "W8-D4 opening's moved. The residual live reach is disclosed exactly: each\n",
     "bytes, in a private namespace. EA7's W8-D5 entry set was a present-state\n"
     "gate until the D5-B landing moved it to the review-law proof module\n"
     "(ADR-0061); it stays proven at the D5-A landing commit. The residual live\n"
     "reach is disclosed exactly: each\n"),
    ("EA7",
     'D5_ENTRIES = frozenset({"W8-D5-EAB"})\n'
     'LATER_THAN_D5 = ("W8-D6", "W8-D7")\n',
     'D5_ENTRIES = frozenset({"W8-D5-EAB"})\n'
     'LATER_THAN_D5 = ("W8-D6", "W8-D7")\n'
     "# The D5-A landing commit, at which EA7's W8-D5 entry set stays proven\n"
     "# after its succession at the D5-B landing (ADR-0061 Part J).\n"
     'D5A_LANDING = "c8e13d47f305e0378609ffec1d31f890f629239d"\n'),
    ("EA7",
     "        # The one present-state gate, until the review law's landing moves\n"
     "        # it: the W8-D5 entries are exactly this brief's, and no W8-D6 or\n"
     "        # W8-D7 entry exists.\n"
     '        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n'
     '        with self.subTest(fact="present state: the W8-D5 entries are this "\n'
     '                               "brief\'s alone"):\n'
     '            self.assertEqual({e["id"] for e in live\n'
     '                              if e["deliverable"] == "W8-D5"}, D5_ENTRIES)\n'
     '            self.assertEqual([e["id"] for e in live\n'
     '                              if e["deliverable"] in LATER_THAN_D5], [])\n',
     "        # Succeeded at the D5-B landing (ADR-0061 Part J): the W8-D5 entry\n"
     "        # set stays proven at the D5-A landing commit, and its present-state\n"
     "        # gate moves to the review-law proof module.\n"
     '        at_landing = json.loads(committed(D5A_LANDING, REGISTRY))["entries"]\n'
     '        with self.subTest(fact="at the D5-A landing: the W8-D5 entries were "\n'
     '                               "this brief\'s alone"):\n'
     '            self.assertEqual({e["id"] for e in at_landing\n'
     '                              if e["deliverable"] == "W8-D5"}, D5_ENTRIES)\n'
     '            self.assertEqual([e["id"] for e in at_landing\n'
     '                              if e["deliverable"] in LATER_THAN_D5], [])\n'),
)}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."

# --------------------------------------------------- the evidence index pins
# The evidence index of W8-D5-EAB item 14, pinned at the effective W8-D5-A
# baseline c8e13d47: (item-14 bullet, registry id or home label, published
# path, commit at which the published bytes last changed, Git object there
# - identical at the baseline -, raw SHA-256 of a blob or None, file count
# of a tree or None). Trusted constants: never read from the text checked.
INDEX = (
    ('1', 'ADR-0054',
     'docs/decisions/0054-generative-evaluation-maturity-doctrine.md',
     '6e9e0f155944bea3117b82a5b4216ce6c50abaa4',
     '77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43',
     'sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd', None),
    ('1', 'ADR-0055',
     'docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     '9e08d3141796df3318de82dfd1d93baef235f11f',
     'sha256:fc967a9c4c4a799dfcd593e05ae5d2db881d47e0a0bf0de6a6fb74fa11dd284b', None),
    ('1', 'ADR-0057',
     'docs/decisions/0057-w8-disposition-reveal-calibration-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     '873fd0c22ba93fb45b321e57513145e0c34d074e',
     'sha256:4222454a1c68ea3b6056b9d8f5e6e720cf2f1f36f967dd8d9154259802f8e358', None),
    ('1', 'ADR-0058',
     'docs/decisions/0058-w8-d3-session-recovery-law.md',
     '897f0b14a66ee956bd9fe36e63975b04d5dc9663',
     '5f8f0786b1bd8091696fe45cb05a388bb776b8b6',
     'sha256:6291da0206c576be10c6c5eea8a1e71490f836e20430663a8eb5038f49877cd3', None),
    ('1', 'ADR-0059',
     'docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     'd06e2f56a25ee80abd678bfe706721ba7df8e70d',
     'sha256:05dc46e0b9b17d96f316aa5dcb545c5ba7e99031cdc169277d6ee12abcf06b59', None),
    ('1', 'ADR-0060',
     'docs/decisions/0060-w8-instrument-validation-law.md',
     '054f1270b8206a059636e18e012223ddfe52d5ea',
     'f6955c079ec323a9dd5e6d20854c9b226e59b79a',
     'sha256:f4440effdab671b49572d14cf8ef14c7d2b1b711e33361cf4ddd59c7c855aae8', None),
    ('2', 'W8-S1 case home',
     'governance/discriminating-supplement',
     '83253039ec274a2496b37b618949fd00d3cd7c8e',
     'a00a0be832ba597ec2f2b68e19ca37d29af58f6d',
     None, 13),
    ('2', 'W8-S1-CM-01',
     'governance/discriminating-supplement/W8-S1-commitment-manifest.json',
     '83253039ec274a2496b37b618949fd00d3cd7c8e',
     '5c32eea50c619d1a7949cd4b29411e17f6b39b42',
     'sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28', None),
    ('2', 'W8-V1 case home',
     'governance/validation-cases',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9',
     '77e9a5c8fa760753278e9df3b696bd4647ad5e9f',
     None, 20),
    ('2', 'W8-V1-CM-01',
     'governance/validation-cases/W8-V1-commitment-manifest.json',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9',
     '4b10c869efea4d7617ae7f3eb866c779d62e0f3b',
     'sha256:c9d35040a45140c0b5bdd7724f04f0922d213ee3cfff9de9f7f13d6b08f6576f', None),
    ('2', 'W8-V1-CM-02',
     'governance/validation-cases/W8-V1-construction-manifest.json',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9',
     'c8d6abdefe4e20495e3e346b616df0f8d2cbeba5',
     'sha256:9c4c3e9d24953fb08458afacc504066fa4b21ae76b0d75a2d7d7b901103a57b3', None),
    ('3', 'W8-D3-DR-01',
     'governance/discriminating-review/W8-D3-disposition-register.json',
     '66b6e6ca7e33e5e0fd326d61653a0c13d1679878',
     '779cbd281eaca6a94d84863ff814a0320dae75b9',
     'sha256:3a1846c02434739c641c58f6428f6b7da4bab2e6a3b24e6b8bff4b4337df2b5a', None),
    ('3', 'W8-D4-DR-01',
     'governance/validation-review/W8-D4-validation-register.json',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89',
     'cb875af9f74f4bd797515e0839e4d601d31fa07b',
     'sha256:89d55e2ac9de9531330faa9687385c0cedf2efcfff855d56b0b6e35ee01b25a0', None),
    ('3', 'W8-D3-HDR',
     'docs/phases/W8-D3-human-disposition-record.md',
     '66b6e6ca7e33e5e0fd326d61653a0c13d1679878',
     '6b832dc72bfaf26145a310aa3397e2545cfc88f8',
     'sha256:f438b825e18b6a0e625bfd8079b02d1350594f46e65aa307f4bddb12f2fddd3e', None),
    ('3', 'W8-D4-VSR',
     'docs/phases/W8-D4-validation-session-record.md',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89',
     'b0064ca82b218691fab18909450b7a4f4c3a8edc',
     'sha256:c5a35c6fd29dd11bed3b2fa706ffb4d056f159441cb0881897c61e677a383cae', None),
    ('4', 'W8-D3 reveal home',
     'governance/discriminating-reveal',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd',
     'c009fef24f746a9ff0daedb05129e82dd6c0bf8a',
     None, 12),
    ('4', 'W8-D4 reveal home',
     'governance/validation-reveal',
     '67ed076503f1087cefed31dd163a706a87d3b8a6',
     'aeafaa63ed4e77b2b7142343d34320429e7f6948',
     None, 36),
    ('4', 'W8-D3-CCR',
     'docs/phases/W8-D3-calibration-completion-record.md',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd',
     'ae3c662051ea716eee43076b10034868cbb1da8b',
     'sha256:b6e958ba42c59b5c45774eb5bbc66e5a1f8a8f19100f1b580c218e2509addf82', None),
    ('4', 'W8-D4-VRC',
     'docs/phases/W8-D4-validation-record.md',
     '67ed076503f1087cefed31dd163a706a87d3b8a6',
     '0cadf57bbb6869323318e9cdd5cb474f59583189',
     'sha256:55e680c31b3983be8b52bb2750dcb7f27fa812f4deb83439d50cf7358d5e327b', None),
    ('5', 'W8-D2-DIB',
     'docs/phases/W8-D2-discriminating-instrument-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     '3e36e29e938a6bca525da22bbd7f95034e9c6b29',
     'sha256:c35dc0fdaeedd7f8a63a840edde34d95e3fa97a4a575e5e2fef70bc4ce3b0f7e', None),
    ('5', 'W8-D2-DIC',
     'docs/phases/W8-D2-discriminating-instrument-record.md',
     '756d3d3512202a905a5d3b689d75bf06ae31ccf5',
     'a2a2b876f2e389857431df873945a58e2992b08c',
     'sha256:62df368528b973a590e300267bab89a634894d8e3fe4604815082d99137af93c', None),
    ('5', 'W8-D3-SCB',
     'docs/phases/W8-D3-synthetic-calibration-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     'b8617c4d1712b940ff5200bba7dd3519afc93096',
     'sha256:11cf050e4c0d820868d9dd1f4e852d23f79c509e833ec565dd98ef354b6521dd', None),
    ('5', 'W8-S1-SOB',
     'docs/phases/W8-S1-supplementary-opening-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e',
     'bf0e33a85bf63f088cb23efd5d30df1fda05249d',
     'sha256:408f4df23a0452dd42ca9615785858f5a31905ef007dc9a130ba72f5b1b1f97a', None),
    ('5', 'W8-S1-SCR',
     'docs/phases/W8-S1-supplementary-corpus-record.md',
     '83253039ec274a2496b37b618949fd00d3cd7c8e',
     '3c59d0de1a816071260a772f63f1889f4237a112',
     'sha256:562bd94979a07b213575493e7f8159f6868065bbaa87b06ad0d5a9dd69eadfa6', None),
    ('5', 'W8-D4-IVB',
     'docs/phases/W8-D4-instrument-validation-brief.md',
     'ad59925813f8b0c39789dac3b29383a5f6e25cea',
     '0a4b5edde06593f0ab9476f4498dd232a57ebce2',
     'sha256:30a956dc21d98d20a6e9daf6c18d1e92dc76342b5522d8f3e0aafc0008c574eb', None),
    ('5', 'W8-D4-VCR',
     'docs/phases/W8-D4-validation-corpus-record.md',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9',
     '9e5f71153ed4e66c1d1c1e0cdc3f1011d7df431d',
     'sha256:80ca992d602e83cd4d1c83fd86d8f05dca344d0ac7e1407ea3c6014e845287eb', None),
    ('5', 'W8-D4-CPR',
     'docs/phases/W8-D4-completion-record.md',
     'ce78a242df25898d90debee9513bdce7e511471b',
     '14e49308ed63a4411400f769f25fda8095d74efb',
     'sha256:dd8a577de367946f5a7f5331a06a6a8df49fbe1b899dd6e6db2d527e62618471', None),
    ('6', 'W8-AR',
     'docs/phases/W8-runway-generative-evaluation-maturity.md',
     '117a192091bfafa80cb3f6ae567b63204b6c7676',
     'da34be5dee7db4a94b4276f4024dd48e3076883a',
     'sha256:fda68f9d1e69c166587cfb746d7d1830b39ea99d9c4c6a9129a0b75d34eba24e', None),
    ('6', 'W7-CR',
     'docs/phases/W7-closure-record.md',
     '7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3',
     'f57ea174237205f2d4e0783f48469ab84abe5c97',
     'sha256:8086966f2355c59d2c8ea34593d177446cac0ec9707977b27d186b7e0d96200a', None),
)

# --------------------------------------------------------------- carriage
REVIEW_QUESTION = (
    "*on the published evidence alone, is the instrument mature enough — "
    "adequate, in the meaning of item 4 — that actual model contact would "
    "add useful evidence: evidence of the kind section 4 shows contact could "
    "lawfully contribute, that the published synthetic record does not "
    "already supply, and that the instrument as published could lawfully "
    "receive?*")
REQUIRED = (
    "It performs no adequacy review, makes no finding, answers no criterion, "
    "names no gap, reads no custody, changes no case, disposition, register, "
    "revealed record or earlier record, diagnoses no divergence, contacts no "
    "model and opens no later deliverable.",
    "the index says what the evidence is and where it is fixed, never what "
    "it means.",
    "Nothing else is authorised by this record",
    "Carried text keeps the brief's references.",
    "The human authority remains the sole source of the finding",
    "The published W8-D3 and W8-D4 records stay fixed",
    "The bounded meaning stands",
    "The review question is the runway's question in its bounded meaning, "
    "carried byte-identically from `W8-D5-EAB` item 21:",
    "Lawful reception is addressed first.",
    "The threshold answer settles no finding form by itself.",
    "What contact could and could not contribute carries whole from "
    "`W8-D5-EAB` section 4.",
    "The criteria are questions, not thresholds.",
    "a criterion the evidence cannot answer is recorded as unanswerable, not "
    "as answered",
    "W8-D5 introduces no new grouped outcome count, rate or ranking by "
    "corpus, authored class or validation method",
    "The finding form is closed.",
    "The finding record is one record, `W8-D5-AFR`, at "
    "`docs/phases/W8-D5-adequacy-finding-record.md`, landed at D5-C together "
    "with W8-D5's completion.",
    "it cites only rows of the index of Part F, by their published path and "
    "commit.",
    "do not enlarge that evidential set and may not stand as substitute "
    "evidence.",
    "A reference that identifies the governing law, the human act or the "
    "finding landing's own provenance is not evidence and enlarges nothing.",
    "The finding decides nothing about W8-D6.",
    "The admissible evidence is exactly the published items of `W8-D5-EAB` "
    "item 14, indexed here by published path and commit and bound to their "
    "bytes.",
    "The index carries no judgement.",
    "Inadmissible, always",
    "The rows are the index's whole.",
    "The finding is the human authority's own act",
    "AI assistance is attributed, never substituted.",
    "Silence is never a finding.",
    "The sole reviewer assesses their own record",
    "Once this record is effective, it permits exactly one further "
    "preparation: the finding record's mechanics, on the human authority's "
    "explicit instruction, binding the human authority's own finding and "
    "nothing else.",
    "W8-D6 and W8-D7 remain closed behind their own briefs.",
    "Counts only, each carrying its statement, and never a percentage, rate, "
    "score, grade, ranking, threshold, pass/fail result or readiness "
    "interpretation",
    "At this landing, only the W8-D5 entry set moves.",
    "This is the one existing proof the placeholder probe found to refuse "
    "this landing; no other existing proof moves.",
    "ADR-0058's R9 limb does not move:",
    "Every later succession is an exact transformation proven against a "
    "fixed historical pre-image, keeps each former absence proven at its own "
    "fixed commit, and refuses every future artefact before its own landing. "
    "No other proof moves.",
    "Model contact, W8-D6 and W8-D7 remain outside this record.",
    "Every EL row proves mechanics and carriage only.",
    "Its index is a list of what is published and where it is fixed, and "
    "nothing more.",
    "No act governed by W8-D5 prepares, authorises or performs model contact, "
    "and this record introduces no model-contact implementation",
    "This record classifies no exchange under ADR-0047 decision 3 and does "
    "not state whether model contact occurred",
    "The finding landing runs its own placeholder probe over every existing "
    "check before fixing its census",
)
# The contact overstatement the r1 review withdrew, in favour of ADR-0058
# decision 15's reservation: never again in this record, in any letter case.
WITHDRAWN = ("no model contact, prompt for contact, provider, credential, "
             "transport, binary or contact harness exists",)
PART_D = "## Part D — The criteria"
PART_E = "## Part E — The finding form and the finding record"
WITHHELD = ("performs no adequacy review", "makes no finding",
            "diagnoses no divergence", "contacts no model",
            "W8-D6 and W8-D7 remain closed",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "any contact decision (W8-D6) or closure (W8-D7)",
            "any finding at this landing, or any finding by anyone but the "
            "human authority",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record",
            "any new grouped outcome count, rate or ranking by corpus, "
            "authored class or validation method",
            "any use, as evidence, of any path, commit or object outside the "
            "index of Part F")
NON_AUTH_SECTION = "## Part K — Explicit non-authorisations"
NON_AUTH_INTRO = ("36. This record and the finding landing it governs do not "
                  "authorise:")
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - any contact decision (W8-D6) or closure (W8-D7);",
    "    - any finding at this landing, or any finding by anyone but the "
    "human authority;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition or reveal, or any "
    "change to an existing one, including any made from captured generated "
    "material;",
    "    - any new grouped outcome count, rate or ranking by corpus, authored "
    "class or validation method;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059 or ADR-0060, or of `W8-D5-EAB`;",
    "    - any score, rate, ranking, threshold, readiness, safety, "
    "correctness, approval, `certif-` or `complian-` claim;",
    "    - any use, as evidence, of any path, commit or object outside the "
    "index of Part F;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any resolution of ADR-0047 precondition 3 or of any carried state.",
)
NON_AUTH_CLOSE = ("    **Model contact, W8-D6 and W8-D7 remain outside this "
                  "record.**")
# Part K whole: heading, blank, introducing item, the twelve lines, blank,
# closing sentence, trailing blank - compared as one block, nothing skipped.
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))
SUCCESSION_SECTION = "## Part J — Proof successions"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
INDEX_SECTION = "## Part F — The evidence index"
INDEX_HEADER = ("| # | Item 14 | Identity or home | Published path | Commit | "
                "Object | Raw SHA-256 or files |")
INDEX_SEPARATOR = "|---|---|---|---|---|---|---|"
CENSUS_LEAD = "**This landing's census is exactly five paths:** "

# --------------------------------------- board and registry: authorised edits
LAW_LINK = ("([`../decisions/0061-w8-evidence-adequacy-review-law.md`]"
            "(../decisions/0061-w8-evidence-adequacy-review-law.md))")
LAW_STATUS_TAIL = (
    "as law the review question in its bounded meaning, the reception "
    "threshold, the seven criteria and the closed three-form finding carried "
    "byte-identically from the opening brief, the finding record's shape, "
    "the attribution of any assistance and its express adoption, and the "
    "evidence index — every admissible item by published path and commit, "
    "bound to its bytes and carrying no judgement; the opening brief's EA7 "
    "entry set succeeds at this landing, R9's sentence and constant "
    "unchanged; it performs no review, makes no finding, diagnoses nothing, "
    "reads no custody and contacts no model, and the finding remains the "
    "human authority's own act at the finding landing.")
LAW_STATUS = {
    "draft": ("**A draft W8-D5 review law, `ADR-0061`, is before the human "
              "reviewer** " + LAW_LINK + ": if accepted, it would fix "
              + LAW_STATUS_TAIL),
    "accepted": ("**The W8-D5 review law, `ADR-0061`, is accepted** "
                 + LAW_LINK + " — accepted %s: it fixes " + LAW_STATUS_TAIL),
}
LAW_ROW = ("| W8-D5 — Evidence-Adequacy Review Law (ADR-0061) | "
           "[`../decisions/0061-w8-evidence-adequacy-review-law.md`]"
           "(../decisions/0061-w8-evidence-adequacy-review-law.md) | ")
LAW_ROW_BODY = (
    "Tier J: **fixes the review law before any finding** — the review "
    "question in its bounded meaning, the reception threshold, the seven "
    "criteria and the closed three-form finding, carried byte-identically "
    "from the opening brief; the finding record's shape; the attribution of "
    "any assistance, adopted only by the human authority's express act; and "
    "the evidence index — every admissible item by published path and "
    "commit, bound to its bytes, carrying no judgement, with the case and "
    "reveal homes indexed as whole trees and no case named. The opening "
    "brief's EA7 W8-D5 entry set succeeds at this landing; ADR-0058's R9 "
    "sentence and constant stay unchanged. **No finding, criterion answered, "
    "diagnosis, custody access or contact capability; every W8-D3, W8-D4 and "
    "W8-D5 record stays fixed; W8-D6 and W8-D7 stay closed; no model "
    "contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_AFTER = ("**" + R9_SENTENCE + " W8-D6 and W8-D7 remain closed behind "
                "their own briefs.**")
# The opening brief's status sentence closes directly before the retained R9
# sentence, and its row is the table's last.
EAB_CLOSE = "preselects no contact decision. "
BOARD_STATUS_ANCHOR = EAB_CLOSE + CLOSED_AFTER
BOARD_ROW_ANCHOR = ("every W8-D3 and W8-D4 record stays fixed; W8-D6 and "
                    "W8-D7 stay closed; no model contact.** |\n")
LAW_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
LAW_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "ADR-0061", "path": LAW, "type": "adr",
    "title": "0061 - W8 Evidence-Adequacy Review Law",
    "role": (
        "The W8-D5 evidence-adequacy review law, landed at D5-B before any "
        "finding as the effective W8-D5-EAB requires: fixes as law the review "
        "question in its bounded meaning, the reception threshold, the seven "
        "criteria and the closed three-form finding, carried byte-identically "
        "from the opening brief; the finding record's shape; the attribution "
        "of any assistance, adopted only by the human authority's express "
        "act; the evidence index - every admissible item of the brief's item "
        "14 by published path and commit, bound to its bytes and carrying no "
        "judgement, with the case and reveal homes indexed as whole trees and "
        "no case named; and the closed, staged succession of the finding "
        "landing, with proof obligations EL1 to EL9. The opening brief's EA7 "
        "W8-D5 entry set succeeds at this landing; ADR-0058's R9 sentence and "
        "constant stay unchanged. Performs no review, makes no finding, "
        "answers no criterion, diagnoses nothing, reads no custody and "
        "contacts no model; the finding remains the human authority's own "
        "act at the finding landing; W8-D6 and W8-D7 stay closed."),
    "depends_on": ["W8-D5-EAB", "W8-AR", "ADR-0054", "ADR-0047", "ADR-0046",
                   "ADR-0055", "ADR-0057", "ADR-0058", "ADR-0059", "ADR-0060",
                   "W8-D2-DIB", "W8-D2-DIC", "W8-D3-SCB", "W8-S1-SOB",
                   "W8-S1-SCR", "W8-S1-CM-01", "W8-D3-HDR", "W8-D3-DR-01",
                   "W8-D3-CCR", "W8-D4-IVB", "W8-D4-VCR", "W8-V1-CM-01",
                   "W8-V1-CM-02", "W8-D4-VSR", "W8-D4-DR-01", "W8-D4-VRC",
                   "W8-D4-CPR", "W8-D2-CBC", "ADR-0056", "W7-CR"],
}


# ----------------------------------------------------------------- helpers
def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def _git_or_none(*args):
    r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True,
                       text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def _lf(raw):
    return raw.replace(b"\r\n", b"\n")


def _sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _flat(text):
    return " ".join(text.split())


def _blob(raw):
    return subprocess.run(["git", "hash-object", "--stdin"], input=raw,
                          cwd=ROOT, capture_output=True,
                          check=True).stdout.decode().strip()


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def object_bytes(obj):
    return subprocess.run(["git", "cat-file", "-p", obj], cwd=ROOT,
                          capture_output=True, check=True).stdout


def d5b_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the law, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", LAW).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the law was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = d5b_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def finding_snapshot(law_commit):
    """(commit, violations) for the finding landing (D5-C), the one landing
    ADR-0061 Part J lets succeed EL7's staged absences. Before its commit
    exists the snapshot is the candidate over a HEAD that must be this
    landing's commit; afterwards it is the one commit that added the finding
    record, whose sole parent must be this landing's commit. Once that
    commit exists the snapshot is fixed: no later entry or path moves it."""
    if law_commit is None:
        return None, ["this landing is not yet committed"]
    adds = _git("log", "--diff-filter=A", "--format=%H", "--",
                FINDING_RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == law_commit else
                      ["uncommitted finding candidate is not over this "
                       "landing's commit"])
    if len(adds) != 1:
        return None, ["the finding record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [law_commit]:
        return adds[0], ["the finding landing's sole parent is not this "
                         "landing's commit"]
    return adds[0], []


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_eal_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def carriage_violations(text, ea):
    """EL1: the runway's question, the nine rules, the contact chain, the
    review question and the load-bearing statements, each once; the closed
    criteria and finding lists exactly the opening module's pins, which the
    effective brief carries at the baseline; Parts D and E's bold-led bullets
    exactly theirs; no preselecting wording."""
    flat = _flat(text)
    v = []
    runway = _flat(baseline_text(RUNWAY))
    if ea.RUNWAY_QUESTION not in runway:
        v.append("the runway's question is not in the runway")
    if flat.count('"%s"' % ea.RUNWAY_QUESTION) != 1:
        v.append("the runway's question is not carried exactly once")
    for name, block in (("nine-rule", ea.nine_rules()),
                        ("contact-chain", ea.contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    brief = baseline_text(BRIEF)
    if _flat(brief).count(REVIEW_QUESTION) != 1:
        v.append("the review question is not in the effective brief once")
    if flat.count(REVIEW_QUESTION) != 1:
        v.append("the review question is not carried exactly once")
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    v += ["a withdrawn overstatement recurs: %s" % s[:44]
          for s in WITHDRAWN if s in flat.lower()]
    v += ea.closed_list_violations(text, ea.CRITERIA_LINES, ea.CRITERIA,
                                   "criterion")
    v += ea.closed_list_violations(text, ea.FORM_LINES, ea.FORMS,
                                   "finding form",
                                   above=(ea.CRITERIA_LINES[-1],))
    if (ea.closed_list_violations(brief, ea.CRITERIA_LINES, ea.CRITERIA,
                                  "criterion")
            or ea.closed_list_violations(brief, ea.FORM_LINES, ea.FORMS,
                                         "finding form",
                                         above=(ea.CRITERIA_LINES[-1],))):
        v.append("the effective brief does not carry the pinned lists")
    for heading, lines, label in ((PART_D, ea.CRITERIA_LINES[1:], "criteria"),
                                  (PART_E, ea.FORM_LINES[1:4],
                                   "finding forms")):
        sec = ea.section_lines(text, heading)
        if sec is None:
            v.append("%s is not present exactly once" % heading)
        else:
            bold = [l for l in sec if ea.BOLD_BULLET.match(l)]
            if bold != list(lines):
                v.append("the part's bold-led bullets are not exactly the %s"
                         % label)
    outside = text
    for line in ea.FORM_LINES:
        outside = outside.replace(line, "", 1)
    low = _flat(outside).lower().replace(ea.RUNWAY_QUESTION.lower(), "")
    v += ["preselecting wording: %s" % p for p in ea.PRESELECTION if p in low]
    return v


def withholding_violations(text, ea):
    """EL2: every withheld phrase present, and Part K exactly its authorised
    whole block - heading, blank, introducing item, the twelve lines in
    order, blank, closing sentence, trailing blank - with no other line in
    it."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = ea.section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["Part K is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("Part K is not exactly its authorised whole block")
    return v


def index_rows():
    rows = []
    for n, (bullet, label, path, commit, obj, sha, files) in enumerate(INDEX,
                                                                      1):
        ident = label if label.endswith(" home") else "`%s`" % label
        last = "`%s`" % sha if sha is not None else "%d files" % files
        rows.append([str(n), bullet, ident, "`%s`" % path, "`%s`" % commit,
                     "`%s`" % obj, last])
    return rows


def index_row_lines():
    return ["| " + " | ".join(r) + " |" for r in index_rows()]


def index_table_violations(text, h):
    """EL4: Part F's one table, read whole, is exactly the trusted rows."""
    rows, v = h.rev.closed_table(text, INDEX_SECTION, INDEX_HEADER,
                                 INDEX_SEPARATOR, 7)
    if rows != index_rows():
        v.append("the index table is not exactly its trusted rows")
    return v


def index_binding_violations(index=None, entries=None):
    """EL4: each row's path names its pinned object at its cited commit - the
    commit at which the path's published bytes last changed - and at the
    baseline; a blob's raw digest and a tree's file count are as pinned;
    each registry identity is registered at that path at the baseline; the
    case homes hold their indexed manifests; no path is indexed twice."""
    index = INDEX if index is None else index
    if entries is None:
        entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
    reg = {e["id"]: e for e in entries}
    v = []
    paths = [r[2] for r in index]
    if len(set(paths)) != len(paths):
        v.append("a path is indexed twice")
    for bullet, label, path, commit, obj, sha, files in index:
        if bullet not in BULLETS:
            v.append("an unknown item-14 bullet: %s" % path)
        for rev in (commit, BASELINE):
            if _git_or_none("rev-parse", "%s:%s" % (rev, path)) != obj:
                v.append("%s does not name its pinned object at %s"
                         % (path, rev[:8]))
        last = _git_or_none("log", "-1", "--format=%H", BASELINE, "--", path)
        if last != commit:
            v.append("%s cites a commit other than its last change" % path)
        kind = _git_or_none("cat-file", "-t", obj)
        if sha is not None:
            if files is not None:
                v.append("a blob row carries a file count: %s" % path)
            if kind != "blob" or _sha(object_bytes(obj)) != sha:
                v.append("blob digest differs: %s" % path)
        elif kind != "tree" or files is None or len(
                _git("ls-tree", "-r", "--name-only", obj).split()) != files:
            v.append("tree file count differs: %s" % path)
        if not label.endswith(" home"):
            e = reg.get(label)
            if e is None or e["path"] != path:
                v.append("%s is not registered at %s" % (label, path))
    for home in CASE_HOMES:
        if home not in paths or not any(p.startswith(home + "/")
                                        for p in paths):
            v.append("a case home is not indexed with its manifest: %s" % home)
    return v


BLANK_LINE = re.compile(r"^[ \t]*$")


def prose_paragraphs(text):
    """Markdown's logical paragraphs: blocks parted by blank lines - empty or
    SPACE/TAB-only, as CommonMark defines a blank line - with every run of
    whitespace inside a block made one space: a soft line break,
    continuation indentation, a tab, a no-break space, an em space or a
    form feed among them. Nothing is joined across a blank line, so a
    heading stays apart from the item below it."""
    blocks, cur = [], []
    for line in text.split("\n"):
        if BLANK_LINE.match(line):
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return "\n\n".join(re.sub(r"\s+", " ", " ".join(b)).strip()
                       for b in blocks)


def exposure_violations(text, h):
    """EL3: the opening module's textual guard over the text's logical prose
    paragraphs, so that ordinary wrapping and continuation indentation hide
    no figure from it, with the succession row and the index rows as the
    exempt exact lines - each survives the paragraph form unchanged."""
    return h.ea.exposure_violations(prose_paragraphs(text), h,
                                    exempt=(succession_row_line(h),)
                                    + tuple(index_row_lines()))


def batch(commit, paths):
    """{path: LF bytes} for many paths in one process: the working copy
    before this landing's commit exists, committed objects otherwise."""
    if commit is None:
        return {p: _lf((ROOT / p).read_bytes()) for p in paths
                if (ROOT / p).is_file()}
    out = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT,
                         input="".join("%s:%s\n" % (commit, p)
                                       for p in paths).encode(),
                         capture_output=True, check=True).stdout
    got, i = {}, 0
    for p in paths:
        head_end = out.index(b"\n", i)
        head = out[i:head_end].split()
        if head[-1] == b"missing":
            i = head_end + 1
            continue
        size = int(head[2])
        got[p] = _lf(out[head_end + 1:head_end + 1 + size])
        i = head_end + 1 + size + 1
    return got


def fixed_paths():
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
    paths = {e["id"]: e["path"] for e in reg}
    homes = {h: sorted(p for p in base_tracked if p.startswith(h + "/"))
             for h in FIXED_HOMES}
    return homes, [paths[r] for r in FIXED_RECORD_IDS] + list(FIXED_MODULES)


def succession_rows(h):
    return [["`%s`" % OPENING, ", ".join(h.auth.labels(SITES[OPENING])),
             "`%s`" % PREIMAGE[OPENING][1], "`%s`" % POSTIMAGE[OPENING][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def succession_table_violations(text, h):
    rows, v = h.rev.closed_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                                 SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, law, h, sites=None):
    """EL6: the opening module is the exact reviewed post-image of its fixed
    pre-image under the EA7 sites, reversible, and Part J's table is exactly
    its trusted row."""
    sites = SITES[OPENING] if sites is None else sites
    v = []
    pre = baseline_text(OPENING)
    if _sha(pre.encode("utf-8")) != PREIMAGE[OPENING][1]:
        v.append("the baseline pre-image differs from its pin")
    expected, problems = h.auth.apply_sites(pre, sites)
    v += problems
    if expected != present:
        v.append("the bytes are not the exact authorised post-image")
    for label, _, new in sites:
        if present.count(new) != 1:
            v.append("%s: post-image site occurs %d times"
                     % (label, present.count(new)))
    restored, problems = h.auth.reverse_sites(present, sites)
    v += problems
    if restored != pre:
        v.append("reversing the table does not restore the pre-image")
    if _sha(present.encode("utf-8")) != POSTIMAGE[OPENING][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("EA7",):
        v.append("the sites are not EA7's alone")
    return v + succession_table_violations(law, h)


def staged_absence_violations(tracked, exists, entries, landed=False):
    """EL7: no finding record, no finding proof module, the W8-D5 entries
    exactly the brief's and this record's, no W8-D6 or W8-D7 entry - or,
    once the finding landing has succeeded these absences (`landed`),
    exactly that landing's record, module and one W8-D5 entry admitted,
    and still no W8-D6 or W8-D7 entry."""
    v = []
    for p in (FINDING_RECORD, FINDING_MODULE):
        if landed and not (p in tracked and exists(p)):
            v.append("a finding-landing path is missing: %s" % p)
        if not landed and (p in tracked or exists(p)):
            v.append("a finding-landing path exists: %s" % p)
    expected = D5_ENTRIES_AT_FINDING if landed else D5_ENTRIES
    if {e["id"] for e in entries if e["deliverable"] == "W8-D5"} != expected:
        v.append("the W8-D5 entries are not exactly the brief's and this "
                 "record's" + (" and the finding record's" if landed
                               else ""))
    if [e["id"] for e in entries if e["deliverable"] in LATER_THAN_D5]:
        v.append("a W8-D6 or W8-D7 entry exists")
    return v


def law_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and LAW_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (LAW_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         EAB_CLOSE + fill(LAW_STATUS[state]) + " " + CLOSED_AFTER),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + LAW_ROW + fill(ROW_PREFIX[state]) + LAW_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D5",
        "path": NEW_ENTRY["path"], "status": state,
        "accepted_date": date if state == "accepted" else None,
        "role": NEW_ENTRY["role"], "governs": [],
        "depends_on": list(NEW_ENTRY["depends_on"]), "resolves": [],
        "id_namespaces": [], "implementation_permission": "none",
        "open_decisions": [], "content_hash": content_hash,
        "hash_exclusion_reason": None, "errata": [],
    }


def expected_registry(base_text, law_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, law_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    """The wording this landing adds to the board in both lawful states, the
    accepted forms dated with a sample so that no format sign remains."""
    sample = "2026-01-01"
    return " ".join([LAW_ROW, LAW_ROW_BODY, LAW_STATUS["draft"],
                     LAW_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, law_text, h):
    """EL8: this record's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D5 entries are exactly the brief's and this
    record's; no W8-D6 or W8-D7 entry."""
    v = []
    e = {x["id"]: x for x in entries}.get("ADR-0061")
    state, date = h.rec.header_state(law_text)
    if e is None:
        return ["no ADR-0061 entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            LAW, "adr", "W8", "W8-D5"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(law_text.encode("utf-8")):
        v.append("the entry's hash differs from the law")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D5"} != D5_ENTRIES:
        v.append("the W8-D5 entries are not exactly the brief's and this "
                 "record's")
    if [x["id"] for x in entries if x["deliverable"] in LATER_THAN_D5]:
        v.append("a W8-D6 or W8-D7 entry exists")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted to
    call is replaced and the previous state restored on exit, tolerating a
    name a later landing has renamed or removed."""

    ABSENT = object()
    TARGETS = (
        ("test_w8_session_recovery_law", "R9_REVEAL", "mechanics sentinel"),
        ("test_w8_session_recovery_law", "header_state",
         lambda *a, **k: (None, None)),
        ("test_w8_recovery_authority", "apply_sites",
         lambda text, sites: (text, [])),
        ("test_w8_reveal_calibration", "closed_table",
         lambda *a, **k: ([], [])),
        ("test_w8_validation_reveal", "figure_hits", lambda *a, **k: []),
        ("test_w8_discriminating_instrument_corpus", "reserved_channel_hits",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_opening", "closed_list_violations",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_opening", "exposure_violations",
         lambda *a, **k: []),
        ("test_w8_evidence_adequacy_opening", "CRITERIA_LINES", ()),
    )

    def __enter__(self):
        self.saved = []
        for module, name, value in self.TARGETS:
            mod = importlib.import_module(module)
            self.saved.append((mod, name, getattr(mod, name, self.ABSENT)))
            setattr(mod, name, value)
        return self

    def __exit__(self, *exc):
        for mod, name, value in reversed(self.saved):
            if value is self.ABSENT:
                mod.__dict__.pop(name, None)
            else:
                setattr(mod, name, value)
        return False


# ------------------------------------------------------------------ proofs
class EL1_Carriage(unittest.TestCase):
    def test_el1_law_carries_question_criteria_and_finding_form(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ea")
        text = read(LAW).decode("utf-8")
        with self.subTest(fact="question, blocks, statements, closed lists "
                               "byte-identical to the brief's, and no "
                               "preselection"):
            self.assertEqual(carriage_violations(text, h.ea), [])
        for name, mutated in h.ea.boundary_mutants(text).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h.ea))
        crit, form = h.ea.CRITERIA_LINES[1], h.ea.FORM_LINES[1]
        for name, mutated in (
                ("an eighth criterion", text.replace(
                    crit + "\n", crit + "\n    - **coverage** — sentinel;\n",
                    1)),
                ("a dropped criterion", text.replace(crit + "\n", "", 1)),
                ("a criterion differing from the brief's by one word",
                 text.replace(crit, crit.replace("no detection",
                                                 "no proof"), 1)),
                ("a fourth finding form", text.replace(
                    form + "\n", form + "\n    - **partial** — sentinel;\n",
                    1)),
                ("a dropped finding form", text.replace(form + "\n", "", 1)),
                ("a stray line inside the finding list", text.replace(
                    h.ea.FORM_LINES[3] + "\n", h.ea.FORM_LINES[3]
                    + "\nsentinel\n", 1)),
                ("a preselecting sentence", text.replace(
                    "\n" + PART_D, "\nThe instrument is mature.\n\n" + PART_D,
                    1)),
                ("a finding form rewritten as an assertion", text.replace(
                    form, form.replace("on the published evidence, ", "", 1),
                    1)),
                ("a recommendation of contact", text.replace(
                    "\n" + PART_D, "\nThis record would recommend contact.\n\n"
                    + PART_D, 1)),
                ("a removed statement", text.replace(REQUIRED[8], "", 1)),
                ("the contact reservation dropped", text.replace(
                    " This record classifies no exchange under ADR-0047 "
                    "decision 3 and does not state whether model contact "
                    "occurred;", "", 1)),
                ("the withdrawn contact overstatement reinstated",
                 text.replace("\n" + PART_D, "\nNo model contact, prompt "
                              "for contact, provider, credential, "
                              "transport, binary or contact harness exists "
                              "or is authorised.\n\n" + PART_D, 1)),
                ("the evidence-only rule widened to every reference",
                 text.replace("do not enlarge that evidential set and may "
                              "not stand as substitute evidence.",
                              "may stand as evidence.", 1)),
                ("an altered review question", text.replace(
                    "could lawfully receive?*", "could receive?*", 1)),
                ("an altered runway question", text.replace(
                    h.ea.RUNWAY_QUESTION,
                    h.ea.RUNWAY_QUESTION.replace("useful", "new"), 1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h.ea))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "ea")
                self.assertEqual(carriage_violations(text, hh.ea), [])


class EL2_Withholding(unittest.TestCase):
    def test_el2_law_withholds_every_later_act(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ea")
        text = read(LAW).decode("utf-8")
        with self.subTest(fact="every withheld phrase carried, Part K whole"):
            self.assertEqual(withholding_violations(text, h.ea), [])
        for s in WITHHELD[:4]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, ""), h.ea))
        pair = NON_AUTH_LINES[3] + "\n" + NON_AUTH_LINES[4] + "\n"
        tail = NON_AUTH_LINES[-1] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this part.\n"
        for name, mutated in (
                ("a dropped non-authorisation", text.replace(
                    NON_AUTH_LINES[9] + "\n", "", 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[4] + "\n" + NON_AUTH_LINES[3] + "\n", 1)),
                ("a thirteenth non-authorisation", text.replace(
                    tail, NON_AUTH_LINES[-1] + "\n    - any sentinel line;\n\n"
                    + NON_AUTH_CLOSE + "\n", 1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n" + neutral + "\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n    This landing "
                              "authorises an additional session.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a differently indented extra bullet",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n  - any sentinel "
                              "line;\n\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a line between the heading and the introducing item",
                 text.replace(NON_AUTH_SECTION + "\n\n" + NON_AUTH_INTRO
                              + "\n", NON_AUTH_SECTION + "\n\n" + neutral
                              + NON_AUTH_INTRO + "\n", 1)),
                ("a line after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a non-breaking-space line as the blank separator",
                 text.replace(tail, NON_AUTH_LINES[-1] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated, h.ea))


class EL3_NoExposure(unittest.TestCase):
    def test_el3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr",
                    "rev", "auth", "ea")
        text = read(LAW).decode("utf-8")
        for surface, body in (("law", text),
                              ("registry role", NEW_ENTRY["role"]),
                              ("board wording", added_board_wording())):
            with self.subTest(surface=surface):
                self.assertEqual(exposure_violations(body, h), [])
        token = sorted(h.pkt.TOKENS)[0]
        method = sorted(h.law.ADMITS)[0]
        for name, planted in {
                "case identity": text + "\nW8-C-" + "0" * 64 + "\n",
                "unpinned digest": text + "\nsha256:" + "f" * 64 + "\n",
                "schema literal": text + "\n" + h.pkt.PACKET_SCHEMA + "\n",
                "method label": text + "\n" + method + "\n",
                "count beside a token": text + "\n3 " + token + "\n",
                "count beside a relation": text + "\nagreements: 7\n",
                "percentage": text + "\n50%\n",
                "decimal": text + "\n0.5\n",
                "index row altered to another digest": text.replace(
                    index_row_lines()[0], index_row_lines()[0].replace(
                        INDEX[0][5], "sha256:" + "f" * 64, 1), 1),
                "score split by a soft line break": text + "\nscore\n5\n",
                "worded score split by a soft line break":
                    text + "\nscore is\n5\n",
                "score with an equals connector split":
                    text + "\nscore =\n5\n",
                "ratio split by a soft line break": text + "\nratio\n3\n",
                "continuation indentation under a figure word":
                    text + "\nscore\n    5\n",
                "tab-indented continuation under a figure word":
                    text + "\nscore\n\t5\n",
                "wider horizontal spacing before a value":
                    text + "\nscore \t  5\n",
                "no-break-space line between word and value":
                    text + "\nscore\n\u00a0\n5\n",
                "em-space line between word and value":
                    text + "\nscore\n\u2003\n5\n",
                "form-feed line between word and value":
                    text + "\nscore\n\f\n5\n"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertNotEqual(planted, text)
                self.assertTrue(exposure_violations(planted, h))
        for name, sep in (("an empty line", ""), ("a SPACE-only line", " "),
                          ("a TAB-only line", "\t"),
                          ("a mixed SPACE/TAB line", " \t ")):
            with self.subTest(control="a figure word and a numbered item "
                                      "parted by %s stay apart" % name):
                parted = (text + "\nthreshold\n" + sep
                          + "\n9. A numbered item.\n")
                self.assertEqual(exposure_violations(parted, h), [])
        with self.subTest(control="the same pair unparted is detected"):
            self.assertTrue(exposure_violations(
                text + "\nthreshold\n9. A numbered item.\n", h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr", "rev", "auth", "ea")
                self.assertEqual(exposure_violations(text, hh), [])


class EL4_EvidenceIndex(unittest.TestCase):
    def test_el4_index_is_exactly_its_trusted_rows_bound_at_both_commits(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(LAW).decode("utf-8")
        with self.subTest(fact="Part F's table is exactly the trusted rows"):
            self.assertEqual(index_table_violations(text, h), [])
        with self.subTest(fact="every row bound at its commit and at the "
                               "baseline, digests, counts, identities and "
                               "manifests"):
            self.assertEqual(index_binding_violations(), [])
            self.assertEqual(len(INDEX), 29)
        row0, row1 = index_row_lines()[0], index_row_lines()[1]
        for name, mutant in {
                "an extra row": text.replace(
                    row1 + "\n", row1 + "\n" + row1.replace("| 2 |", "| 30 |", 1)
                    + "\n", 1),
                "a missing row": text.replace(row1 + "\n", "", 1),
                "two rows swapped": text.replace(
                    row0 + "\n" + row1 + "\n", row1 + "\n" + row0 + "\n", 1),
                "an altered file count": text.replace(" files |", " file |", 1),
                "an extra field": text.replace(row0, row0 + " extra |", 1),
                "an indented row": text.replace(row0, "  " + row0, 1),
                "a non-blank line under the table": text.replace(
                    index_row_lines()[-1] + "\n",
                    index_row_lines()[-1] + "\nA stray line.\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, text)
                self.assertTrue(index_table_violations(mutant, h))
        blob_row = next(r for r in INDEX if r[5] is not None)
        tree_row = next(r for r in INDEX if r[5] is None)
        other = next(r for r in INDEX if r[5] is not None and r != blob_row)
        home_row = next(r for r in INDEX if r[1].endswith(" home"))
        rows = list(INDEX)

        def swap(row, **changes):
            fields = ["bullet", "label", "path", "commit", "obj", "sha",
                      "files"]
            d = dict(zip(fields, row))
            d.update(changes)
            return tuple(d[f] for f in fields)
        for name, index in {
                "the baseline cited instead of the last change": [
                    swap(r, commit=BASELINE) if r == blob_row else r
                    for r in rows],
                "another row's object": [
                    swap(r, obj=other[4]) if r == blob_row else r
                    for r in rows],
                "an altered blob digest": [
                    swap(r, sha="sha256:" + "0" * 64) if r == blob_row else r
                    for r in rows],
                "an altered tree file count": [
                    swap(r, files=r[6] + 1) if r == tree_row else r
                    for r in rows],
                "an identity registered elsewhere": [
                    swap(r, label=other[1]) if r == blob_row else r
                    for r in rows],
                "a home renamed to a file": [
                    swap(r, path=blob_row[2], obj=blob_row[4])
                    if r == home_row else r for r in rows],
                "a path indexed twice": rows + [blob_row],
                "a case home without its manifest": [
                    r for r in rows
                    if not r[2].startswith(CASE_HOMES[0] + "/")],
                "an unknown bullet": [
                    swap(r, bullet="7") if r == blob_row else r
                    for r in rows]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(index, rows)
                self.assertTrue(index_binding_violations(index))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(index_table_violations(text, hh), [])


class EL5_FixedArtefactsUnchanged(unittest.TestCase):
    def test_el5_every_home_record_brief_and_module_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "ea")
        tracked = snapshot_tracked(commit)
        homes, records = fixed_paths()
        every = [f for files in homes.values() for f in files] + records
        base = batch(BASELINE, every)
        now = batch(commit, every)
        with self.subTest(fact="fixed homes, records, the opening brief and "
                               "the session-recovery module byte-identical "
                               "to the baseline"):
            self.assertEqual(len(base), len(every))
            self.assertEqual(set(now), set(every))
            self.assertEqual(h.ea.fixed_artefact_violations(
                now, tracked, homes, records, base), [])
            self.assertIn(BRIEF, records)
            self.assertIn(RECOVERY, records)
            self.assertNotIn(OPENING, records)
        reveal_file = homes["governance/validation-reveal"][0]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed opening brief": (
                    dict(now, **{BRIEF: now[BRIEF] + b" "}), tracked),
                "a changed session-recovery module": (
                    dict(now, **{RECOVERY: now[RECOVERY] + b" "}), tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(h.ea.fixed_artefact_violations(
                    n, t, homes, records, base))


class EL6_EA7Succession(unittest.TestCase):
    def test_el6_ea7_succession_is_exact_and_the_set_stays_proven(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "ea")
        law = read(LAW).decode("utf-8")
        present = read(OPENING).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[OPENING][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + OPENING)
                             .strip(), PREIMAGE[OPENING][2])
        with self.subTest(exact_succession="opening module"):
            self.assertEqual(succession_violations(present, law, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[OPENING][1])
        with self.subTest(fact="the succeeded module keeps the W8-D5 entry "
                               "set proven at the D5-A landing commit"):
            self.assertEqual(h.ea.D5A_LANDING, BASELINE)
            at_landing = json.loads(committed(BASELINE, REGISTRY))["entries"]
            self.assertEqual({e["id"] for e in at_landing
                              if e["deliverable"] == "W8-D5"}, h.ea.D5_ENTRIES)
            self.assertEqual(h.ea.D5_ENTRIES | {"ADR-0061"}, D5_ENTRIES)
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[OPENING][1:]),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[OPENING] + (("EA7", first,
                                       first + "# planted\n"),)),
                "a site labelled for another proof": (
                    present, SITES[OPENING][:2] + (("EA6",)
                                                   + SITES[OPENING][2][1:],))}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(succession_violations(text, law, h, table))
        row = succession_row_line(h)
        rogue = ("| `tests/placeholder.py` | extra | `sha256:%s` | "
                 "`sha256:%s` |" % ("d" * 64, "e" * 64))
        for name, mutant in {
                "an unknown source row": law.replace(
                    row + "\n", row + "\n" + rogue + "\n", 1),
                "a duplicate authorised row": law.replace(
                    row + "\n", row + "\n" + row + "\n", 1),
                "an extra field": law.replace(row, row + " extra |", 1),
                "an indented row": law.replace(row, "  " + row, 1),
                "a row without its opening pipe": law.replace(row, row[2:],
                                                              1),
                "a non-blank line under the table": law.replace(
                    row + "\n", row + "\nA stray line.\n", 1)}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutant, law)
                self.assertTrue(succession_table_violations(mutant, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "ea")
                self.assertEqual(succession_violations(present, law, hh), [])


class EL7_StagedAbsences(unittest.TestCase):
    def test_el7_no_finding_artefact_before_its_own_landing(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        tracked = snapshot_tracked(commit)
        with self.subTest(fact="nothing of the finding landing exists at "
                               "this landing's snapshot"):
            self.assertEqual(staged_absence_violations(
                tracked, lambda p: False, at_snapshot), [])
        # Succeeded at the finding landing (ADR-0061 Part J, decisions 34
        # and 35): each former absence stays proven at this landing's
        # snapshot above, and the admission of exactly the finding record,
        # its proof module and the one W8-D5 entry that landing added - and
        # still no W8-D6 or W8-D7 entry - is proven at that landing's own
        # fixed snapshot. No present-state gate remains here: W8-D6 and
        # W8-D7 stay refused by ADR-0058's R9 alone.
        landing, problems = finding_snapshot(commit)
        self.assertEqual(problems, [])
        at_landing = json.loads(snapshot_bytes(landing, REGISTRY))["entries"]
        landed_tracked = snapshot_tracked(landing)
        with self.subTest(fact="at the finding landing's snapshot: exactly "
                               "its record, module and W8-D5 entry admitted"):
            self.assertEqual(staged_absence_violations(
                landed_tracked, lambda p: p in landed_tracked, at_landing,
                landed=True), [])
        base = at_snapshot[-1]
        for name, args in {
                "a finding record path": (
                    tracked + [FINDING_RECORD], lambda p: False, at_snapshot),
                "a finding module on disk": (
                    tracked, lambda p: p == FINDING_MODULE, at_snapshot),
                "a premature W8-D5 entry": (
                    tracked, lambda p: False, at_snapshot + [dict(
                        base, id="W8-D5-SNT", deliverable="W8-D5")]),
                "a W8-D6 entry": (
                    tracked, lambda p: False, at_snapshot + [dict(
                        base, id="W8-D6-SNT", deliverable="W8-D6")]),
                "the brief's entry removed": (
                    tracked, lambda p: False,
                    [e for e in at_snapshot if e["id"] != "W8-D5-EAB"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(staged_absence_violations(*args))
        # Historical controls over mutated copies of the finding landing's
        # fixed snapshot: none reads the present registry or tree, and none
        # demands the refusal of any genuinely later entry.
        with self.subTest(control="the former absences at the finding "
                                  "landing's snapshot are refused"):
            self.assertTrue(staged_absence_violations(
                landed_tracked, lambda p: p in landed_tracked, at_landing))
        for name, args in {
                "a fourth W8-D5 entry at the finding landing's snapshot": (
                    landed_tracked, lambda p: p in landed_tracked,
                    at_landing + [dict(base, id="W8-D5-SNT",
                                       deliverable="W8-D5")]),
                "a W8-D6 entry at the finding landing's snapshot": (
                    landed_tracked, lambda p: p in landed_tracked,
                    at_landing + [dict(base, id="W8-D6-SNT",
                                       deliverable="W8-D6")]),
                "the finding record missing at the finding landing's "
                "snapshot": (
                    [p for p in landed_tracked if p != FINDING_RECORD],
                    lambda p: p != FINDING_RECORD and p in landed_tracked,
                    at_landing),
                "the finding entry missing at the finding landing's "
                "snapshot": (
                    landed_tracked, lambda p: p in landed_tracked,
                    [e for e in at_landing if e["id"] != FINDING_ENTRY])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(staged_absence_violations(*args, landed=True))


class EL8_RegistryAndBoard(unittest.TestCase):
    def test_el8_registered_and_changed_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        law = read(LAW).decode("utf-8")
        state, date, v = law_state(law, h)
        self.assertEqual(v, [])
        board_pre = baseline_text(BOARD)
        reg_pre = baseline_text(REGISTRY)
        for rel, pre in ((BOARD, board_pre), (REGISTRY, reg_pre)):
            with self.subTest(pre_image=rel):
                self.assertEqual(_sha(pre.encode("utf-8")), PREIMAGE[rel][1])
        board = read(BOARD).decode("utf-8")

        def board_ok(apply_sites):
            expected, problems = apply_sites(
                board_pre, board_sites(state, date, board_pre))
            return problems == [] and board == expected
        with self.subTest(fact="exact authorised board, R9's sentence kept "
                               "once", state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED_AFTER), 1)
        law_hash = _sha(read(LAW))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, law_hash,
                                                    state, date))
        at_snapshot = json.loads(reg)["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, law, h), [])
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, law_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        base = at_snapshot[-1]
        for name, entries in {
                "a premature W8-D5 entry": at_snapshot + [dict(
                    base, id="W8-D5-SNT", deliverable="W8-D5")],
                "a W8-D6 entry": at_snapshot + [dict(
                    base, id="W8-D6-SNT", deliverable="W8-D6")],
                "a wrong law hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                     if e["id"] == "ADR-0061" else e
                                     for e in at_snapshot],
                "a wrong type": [dict(e, type="phase-record")
                                 if e["id"] == "ADR-0061" else e
                                 for e in at_snapshot]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, law, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))
                self.assertEqual(entry_violations(at_snapshot, law, hh), [])


class EL9_Census(unittest.TestCase):
    def test_el9_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the opening module "
                               "change among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, OPENING})
        flat = _flat(read(LAW).decode("utf-8"))
        with self.subTest(fact="the law names the fixed census"):
            m = re.search(re.escape(CENSUS_LEAD) + r"(.*?) 39\. ", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RUNWAY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
