"""W8-D7-B — closure assessment proofs (W8-D7-CAR, CB1–CB9).

Landing B of W8-D7: the whole-phase closure assessment, the evidence record
on which any closure decision must rest, containing no declaration of
closure. This module proves the record's carriage - its load-bearing
statements, the nine rules, the chain and the invariant, its closed posture
vocabulary over the proposed-posture tables, and the absence of
closure-presuming wording, of verdict forms as postures, of the withdrawn
mechanical-conformance formula, of any universal session or reveal claim, of
any inventoried statement whether model contact occurred, of any inventoried
attestation that a human act was performed, and of the brief's drafting
target; its non-authorisations; its exposure limits,
with the provenance rows, the file-provenance rows, the succession-audit
rows and this landing's one succession row as the only digest exemptions;
that every fixed home and
every registered record at the baseline is byte-unchanged, that the three
provenance tables resolve - the registered sources read, the governing-
dependency trace and the unregistered files read - with every repository
path the record names in code marks, of a listed extension, provenanced, and
that the deliverable inventory accounts for every W8
commit and every W8 registry entry exactly once, each commit bound to its
row from history; the exact CA7
succession of the closure opening module and the recomputation from history
of every proof-module change in the W8 range; the exact registry and board;
the W8-D7 entry set and the no-later-phase limb; the census; and the
evidence-integrity identities - each with planted-mutant or negative
controls. Closed validators compare against trusted expected values held
here and refuse unrecognised material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the record
afterwards - and executes the helpers it relies on from that snapshot's
bytes, in a private namespace. CB7's W8-D7 entry set and its no-later-phase
limb were this module's present-state gates, moved here from the opening
module's CA7 at this landing, until the closure record's landing (W8-CR)
succeeded them to a historical proof at this landing's own published
commit. The residual live reach is disclosed exactly: each snapshot-executed
helper module imports, at its own top level, the live modules it aliases for
the fixed-law values it reads from them, and no more independence than that
is claimed.

CB1's closure-presumption scan reads the whole record through a bounded fold
- emphasis and code marks and the invisible code points removed, every
whitespace run one space, case folded - so that ordinary formatting hides
no inventoried phrase; the record carries no drafting target, so nothing is
set aside. Conformance to that bounded inventory is never proof that
arbitrary prose draws no conclusion. CB3 reads every surface as logical
prose paragraphs - blocks parted by blank lines, empty or SPACE/TAB-only as
CommonMark defines them, with every whitespace run inside a block made one
space - so that a soft line break, continuation indentation or a separator
line of no-break spaces, em spaces or form feeds hides no figure or count
from it; the exempt exact rows survive the paragraph form unchanged.

Sections of the record that hold more than one table are read block by
block: every delimiter-bearing line of the section must belong to one of
the expected contiguous blocks, each exactly its header, its separator and
its rows, and nothing is filtered out.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity, schema
literal or method label as a literal, and no disposition token. It declares
no closure and assigns no posture.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that W8 may close, or any closure posture; that any
inventory is complete or any proposed posture right; anything about the
instrument's maturity, adequacy, readiness, safety or usefulness; anything
about any model, case, disposition, divergence or reviewer; that any model
was or was not contacted; that any ADR-0047 precondition moved; or that any
later phase may open.
"""

import ast
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

# The published, remotely verified W8-D7 opening brief: this landing's sole
# parent and the commit every pre-image below is read from. It is also the
# commit at which the opening module's CA7 keeps the W8-D7 entry set and
# the no-later-phase limb proven after this landing's succession.
BASELINE = "cf2012669b97b323cdbfb182bc10865d444c79c1"
D7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"
# Succeeded at the W8 closure landing (W8-CR; W8-D7-CAB section 15, item
# 60; W8-D7-CAR section 11, item 46): CB7's W8-D7 entry set and its
# no-later-phase limb stay proven at this landing's own published commit;
# the live gates move to the closure record's proof module.
D7B_LANDING = "6ee0127e91f755d39b7fdc5af08bb1bcf1b16437"
D6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"
D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"
D5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"
D3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"
W7_CLOSURE = "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3"
W7_D6_SEAL = "a32579361f19556520e188cb8220b23d95323a4c"

RECORD = "docs/phases/W8-D7-B-closure-assessment-record.md"
SELF_REL = "tests/test_w8_closure_assessment.py"
OPENING = "tests/test_w8_closure_opening.py"
BRIEF = "docs/phases/W8-D7-A-closure-authorisation-brief.md"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, OPENING, REGISTRY, BOARD})
D7_ENTRIES = frozenset({"W8-D7-CAB", "W8-D7-CAR"})
# The phases the registry may hold while W8 is open: no later phase is
# opened, designed or named as assigned by any W8-D7 landing.
KNOWN_PHASES = frozenset("W%d" % n for n in range(9))
FIXED_HOMES = ("governance/validation-cases", "governance/validation-review",
               "governance/validation-reveal",
               "governance/discriminating-instrument",
               "governance/discriminating-supplement",
               "governance/discriminating-reveal",
               "governance/discriminating-review",
               "governance/generated-evaluation",
               "governance/evaluation")

HELPERS = {"env": "tests/test_w8_discriminating_instrument_envelope.py",
           "law": "tests/test_w8_validation_law.py",
           "pkt": "tests/w8_review_packet.py",
           "cal": "tests/test_w8_calibration_law.py",
           "rec": RECOVERY,
           "auth": "tests/test_w8_recovery_authority.py",
           "rev": "tests/test_w8_reveal_calibration.py",
           "cor": "tests/test_w8_discriminating_instrument_corpus.py",
           "vr": "tests/test_w8_validation_reveal.py"}

# Fixed pre-images at BASELINE: (label, LF SHA-256, blob).
PREIMAGE = {
    OPENING: ("closure opening module",
              "sha256:f16c74c26cba7f2ad9655aa9068a762531d4d60f0680a7cf9af72a2ac15207dd",
              "dfa8fde2929d2ba6edccdc52367d7f95c6412499"),
    REGISTRY: ("registry",
               "sha256:621bb53129dda239b27aead54961787ea1dd04cee395b369e137486da18d9dd2",
               "7e57cf81ddae4088af0f8ee9f15d1dc5ce662d0a"),
    BOARD: ("board",
            "sha256:564c057c4cecf97bee51caa78a7d80439dc707df7b24c60fff66ada55b11577d",
            "28b550c5afe1e9063d8f8223ffffe8e140b33b63"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {OPENING: ("sha256:5e425bb77673696f5c4deb8925f33228b2627ca45aa35fdc5cea6b3580501819", "8ac0f49ef210e5c179c0dd8bbed3fe89344f7f30")}

# ---------------------------------- the one succession: the opening module's CA7
SITES = {
    OPENING: (
        ('CA7',
         "bytes, in a private namespace. CA7's W8-D7 entry set is the one\npresent-state gate, as the W8-D4, W8-D5 and W8-D6 openings' were, until\nthe assessment landing (W8-D7-CAR) succeeds it. The residual live reach is\n",
         "bytes, in a private namespace. CA7's W8-D7 entry set was the one\npresent-state gate, as the W8-D4, W8-D5 and W8-D6 openings' were, until\nthe assessment landing (W8-D7-CAR) succeeded it to a historical proof at\nthis landing's own published commit. The residual live reach is\n"),
        ('CA7',
         'D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"\nW7_CLOSURE = "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3"\n',
         'D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"\nW7_CLOSURE = "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3"\n# Succeeded at the W8-D7 assessment landing (W8-D7-CAR; W8-D7-CAB section\n# 15, item 60): CA7\'s W8-D7 entry set and its no-later-phase limb stay\n# proven at this landing\'s own published commit; the live gates move to\n# the assessment landing\'s proof module.\nD7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"\n'),
        ('CA7',
         '        # The one present-state gate of this module, until the assessment\n        # landing (W8-D7-CAR) succeeds it to a historical proof at this\n        # landing\'s commit.\n        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n        with self.subTest(fact="the W8-D7 entries are this brief\'s alone"):\n            self.assertEqual(entry_violations(live, brief, h), [])\n',
         '        # Succeeded at the assessment landing (W8-D7-CAR): the W8-D7 entry\n        # set and the no-later-phase limb stay proven at this landing\'s own\n        # published commit, D7A_LANDING; the live gates live in the\n        # assessment landing\'s proof module until the closure record\'s\n        # landing succeeds them in turn.\n        at_landing = json.loads(committed(D7A_LANDING, REGISTRY))["entries"]\n        with self.subTest(fact="the W8-D7 entries were this brief\'s alone at "\n                               "this landing\'s published commit"):\n            self.assertEqual(commit, D7A_LANDING)\n            self.assertEqual(entry_violations(at_landing, brief, h), [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_LINE = 'R9_REVEAL = "%s"\n' % R9_SENTENCE
LATER_LINE = 'LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")\n'
D7A_LINE = 'D7A_LANDING = "%s"\n' % D7A_LANDING
HISTORICAL_READ = 'json.loads(committed(D7A_LANDING, REGISTRY))["entries"]'
LIVE_READ = '(ROOT / REGISTRY).read_bytes()'

# ------------------------------------------------------------- the sources
# Trusted rows of the record's section 1 table: (number, identity, path,
# commit at which the path's published bytes last changed on the
# first-parent line to the baseline, blob at the baseline, raw SHA-256 of
# the committed bytes).
BASIS_SECTION = "## 1. Method and evidence law"
BASIS_HEADER = "| # | Identity | Published path | Commit | Object | Raw SHA-256 |"
BASIS_SEPARATOR = "|---|---|---|---|---|---|"
BASIS_ROWS = (
    (1, 'W8-AR', 'docs/phases/W8-runway-generative-evaluation-maturity.md',
     '117a192091bfafa80cb3f6ae567b63204b6c7676', 'da34be5dee7db4a94b4276f4024dd48e3076883a',
     'sha256:fda68f9d1e69c166587cfb746d7d1830b39ea99d9c4c6a9129a0b75d34eba24e'),
    (2, 'W8-D1-EDB', 'docs/phases/W8-D1-evaluation-doctrine-brief.md',
     '26a06627fda128dd10aeb38c958e9916b818c391', 'e416353f3fc426ad3cc2cb0e3c37ab7bc27e5d3e',
     'sha256:b0b6ff972f6ef9350f02783e20d825b4769ed801bdb36d2597d60bb02ec56f6e'),
    (3, 'ADR-0054', 'docs/decisions/0054-generative-evaluation-maturity-doctrine.md',
     '6e9e0f155944bea3117b82a5b4216ce6c50abaa4', '77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43',
     'sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd'),
    (4, 'W8-D2-DIB', 'docs/phases/W8-D2-discriminating-instrument-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', '3e36e29e938a6bca525da22bbd7f95034e9c6b29',
     'sha256:c35dc0fdaeedd7f8a63a840edde34d95e3fa97a4a575e5e2fef70bc4ce3b0f7e'),
    (5, 'ADR-0055', 'docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', '9e08d3141796df3318de82dfd1d93baef235f11f',
     'sha256:fc967a9c4c4a799dfcd593e05ae5d2db881d47e0a0bf0de6a6fb74fa11dd284b'),
    (6, 'W8-D2-MSA', 'docs/phases/W8-D2-manifest-shape-amendment.md',
     'df406d4030a8c6ae6cf273a0cf18097a49c66f0c', 'a83489f989645935d8414f172afa8d8ac1a1a238',
     'sha256:2a7ea0f53bc75b9ee45afd148732f7b5a2f05ccbe3b13518d99e9084c2ccf388'),
    (7, 'W8-D2-DIC', 'docs/phases/W8-D2-discriminating-instrument-record.md',
     '756d3d3512202a905a5d3b689d75bf06ae31ccf5', 'a2a2b876f2e389857431df873945a58e2992b08c',
     'sha256:62df368528b973a590e300267bab89a634894d8e3fe4604815082d99137af93c'),
    (8, 'W8-D2-CM-01', 'governance/discriminating-instrument/W8-D2-commitment-manifest.json',
     '756d3d3512202a905a5d3b689d75bf06ae31ccf5', '4f2e9ade3b8fb131bf90309d9dc986a8f1a57f8b',
     'sha256:3eb1178037827996c136075f1ffa2ee617134423890d030adc80094cd8a4f459'),
    (9, 'ADR-0056', 'docs/decisions/0056-public-repository-identity-attribution-boundary.md',
     '797e839ac9484a04ac84e1f7bb5f84851f539579', '891e737e32960bae4fc48d6852bf935ffdb33d85',
     'sha256:ed0f3ab7e5828c2c7be408b2712a491f68d635bb80efc42e2328d83792a3084d'),
    (10, 'W8-D2-CBC', 'docs/phases/W8-D2-committed-blob-proof-correction.md',
     'a4997128055462bb4791cfa5c5d06c3a3f51b0ba', 'bc3cba96a1c366879420a3e97724221c348d1885',
     'sha256:f1d18113a61c9fbf27e9705a613881485fa6fa801f977327bb6db56588a1173c'),
    (11, 'W8-D3-SCB', 'docs/phases/W8-D3-synthetic-calibration-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'b8617c4d1712b940ff5200bba7dd3519afc93096',
     'sha256:11cf050e4c0d820868d9dd1f4e852d23f79c509e833ec565dd98ef354b6521dd'),
    (12, 'ADR-0057', 'docs/decisions/0057-w8-disposition-reveal-calibration-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', '873fd0c22ba93fb45b321e57513145e0c34d074e',
     'sha256:4222454a1c68ea3b6056b9d8f5e6e720cf2f1f36f967dd8d9154259802f8e358'),
    (13, 'ADR-0058', 'docs/decisions/0058-w8-d3-session-recovery-law.md',
     '897f0b14a66ee956bd9fe36e63975b04d5dc9663', '5f8f0786b1bd8091696fe45cb05a388bb776b8b6',
     'sha256:6291da0206c576be10c6c5eea8a1e71490f836e20430663a8eb5038f49877cd3'),
    (14, 'ADR-0059', 'docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'd06e2f56a25ee80abd678bfe706721ba7df8e70d',
     'sha256:05dc46e0b9b17d96f316aa5dcb545c5ba7e99031cdc169277d6ee12abcf06b59'),
    (15, 'W8-S1-SOB', 'docs/phases/W8-S1-supplementary-opening-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'bf0e33a85bf63f088cb23efd5d30df1fda05249d',
     'sha256:408f4df23a0452dd42ca9615785858f5a31905ef007dc9a130ba72f5b1b1f97a'),
    (16, 'W8-S1-SCR', 'docs/phases/W8-S1-supplementary-corpus-record.md',
     '83253039ec274a2496b37b618949fd00d3cd7c8e', '3c59d0de1a816071260a772f63f1889f4237a112',
     'sha256:562bd94979a07b213575493e7f8159f6868065bbaa87b06ad0d5a9dd69eadfa6'),
    (17, 'W8-S1-CM-01', 'governance/discriminating-supplement/W8-S1-commitment-manifest.json',
     '83253039ec274a2496b37b618949fd00d3cd7c8e', '5c32eea50c619d1a7949cd4b29411e17f6b39b42',
     'sha256:ff59d15345df7c6eb8602c33f1832cc9512e66e880c218f4b3158dd4ad0a6d28'),
    (18, 'W8-HPC', 'docs/phases/W8-historical-pin-proof-correction.md',
     '9ded8c44abfd4c911d938814a7f551944998ec53', 'ccb94754798e7432d0e3090773f1c9cffda50a5b',
     'sha256:14746269c7af18556b6ee92d6aeb6c760b4835749beb8f0314afb041e4d650b9'),
    (19, 'W8-D3-HDR', 'docs/phases/W8-D3-human-disposition-record.md',
     '66b6e6ca7e33e5e0fd326d61653a0c13d1679878', '6b832dc72bfaf26145a310aa3397e2545cfc88f8',
     'sha256:f438b825e18b6a0e625bfd8079b02d1350594f46e65aa307f4bddb12f2fddd3e'),
    (20, 'W8-D3-DR-01', 'governance/discriminating-review/W8-D3-disposition-register.json',
     '66b6e6ca7e33e5e0fd326d61653a0c13d1679878', '779cbd281eaca6a94d84863ff814a0320dae75b9',
     'sha256:3a1846c02434739c641c58f6428f6b7da4bab2e6a3b24e6b8bff4b4337df2b5a'),
    (21, 'W8-HAC', 'docs/phases/W8-historical-absence-proof-correction.md',
     '317c0ba9de76853d454774085cdf18f3a638c02f', 'c4700ca800242a133308f43ac26d9a579b3eca15',
     'sha256:a061bab8660d1c3c01e7003b05f89fe92d931b04d76c8d8f9b7aa0d33dab6cd9'),
    (22, 'W8-D3-CCR', 'docs/phases/W8-D3-calibration-completion-record.md',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'ae3c662051ea716eee43076b10034868cbb1da8b',
     'sha256:b6e958ba42c59b5c45774eb5bbc66e5a1f8a8f19100f1b580c218e2509addf82'),
    (23, 'W8-D4-IVB', 'docs/phases/W8-D4-instrument-validation-brief.md',
     'ad59925813f8b0c39789dac3b29383a5f6e25cea', '0a4b5edde06593f0ab9476f4498dd232a57ebce2',
     'sha256:30a956dc21d98d20a6e9daf6c18d1e92dc76342b5522d8f3e0aafc0008c574eb'),
    (24, 'ADR-0060', 'docs/decisions/0060-w8-instrument-validation-law.md',
     '054f1270b8206a059636e18e012223ddfe52d5ea', 'f6955c079ec323a9dd5e6d20854c9b226e59b79a',
     'sha256:f4440effdab671b49572d14cf8ef14c7d2b1b711e33361cf4ddd59c7c855aae8'),
    (25, 'W8-D4-VCR', 'docs/phases/W8-D4-validation-corpus-record.md',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9', '9e5f71153ed4e66c1d1c1e0cdc3f1011d7df431d',
     'sha256:80ca992d602e83cd4d1c83fd86d8f05dca344d0ac7e1407ea3c6014e845287eb'),
    (26, 'W8-V1-CM-01', 'governance/validation-cases/W8-V1-commitment-manifest.json',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9', '4b10c869efea4d7617ae7f3eb866c779d62e0f3b',
     'sha256:c9d35040a45140c0b5bdd7724f04f0922d213ee3cfff9de9f7f13d6b08f6576f'),
    (27, 'W8-V1-CM-02', 'governance/validation-cases/W8-V1-construction-manifest.json',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9', 'c8d6abdefe4e20495e3e346b616df0f8d2cbeba5',
     'sha256:9c4c3e9d24953fb08458afacc504066fa4b21ae76b0d75a2d7d7b901103a57b3'),
    (28, 'W8-CHC', 'docs/phases/W8-case-home-scope-correction.md',
     'a08ba584bea8e2576dd7450c6374a4ff4f0aa149', '5690aac90ff4e5a11c068ab55c0881c0dbbe1293',
     'sha256:1c416856a69d81a7d8f719b946787b98a98f25f76e1db5fec51ee0f346901925'),
    (29, 'W8-D4-VSR', 'docs/phases/W8-D4-validation-session-record.md',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'b0064ca82b218691fab18909450b7a4f4c3a8edc',
     'sha256:c5a35c6fd29dd11bed3b2fa706ffb4d056f159441cb0881897c61e677a383cae'),
    (30, 'W8-D4-DR-01', 'governance/validation-review/W8-D4-validation-register.json',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'cb875af9f74f4bd797515e0839e4d601d31fa07b',
     'sha256:89d55e2ac9de9531330faa9687385c0cedf2efcfff855d56b0b6e35ee01b25a0'),
    (31, 'W8-D4-VRC', 'docs/phases/W8-D4-validation-record.md',
     '67ed076503f1087cefed31dd163a706a87d3b8a6', '0cadf57bbb6869323318e9cdd5cb474f59583189',
     'sha256:55e680c31b3983be8b52bb2750dcb7f27fa812f4deb83439d50cf7358d5e327b'),
    (32, 'W8-D4-CPR', 'docs/phases/W8-D4-completion-record.md',
     'ce78a242df25898d90debee9513bdce7e511471b', '14e49308ed63a4411400f769f25fda8095d74efb',
     'sha256:dd8a577de367946f5a7f5331a06a6a8df49fbe1b899dd6e6db2d527e62618471'),
    (33, 'W8-DER', 'docs/phases/W8-documentation-erratum.md',
     '6704649ed80c27112c00c14093c82645e8d090cf', '371f80be2d1abca01b0ff7fa0da9065c2c63e1bc',
     'sha256:0eec519ea3d1d369bfd3f8231d09c8f09a24dde9749fa59480f900d5da45fd07'),
    (34, 'W8-D5-EAB', 'docs/phases/W8-D5-evidence-adequacy-brief.md',
     'c8e13d47f305e0378609ffec1d31f890f629239d', '78a78b2179740e769ef42bd2ed5944cb04fd71b8',
     'sha256:339c93d624f56f07165aa81696fb2f464cfec1fef2148ceace2b4222b8efe60a'),
    (35, 'ADR-0061', 'docs/decisions/0061-w8-evidence-adequacy-review-law.md',
     '18d6230b5f7281577c18892dd7b95e9448f310c2', 'aec015d014c098b183deeb119a6c6293f4e4b6bb',
     'sha256:b81af71545cfc21d3311275110e66dc0768d87d24f1954138e95783773cf95d9'),
    (36, 'W8-D5-AFR', 'docs/phases/W8-D5-adequacy-finding-record.md',
     '2aa2c75d20363ca7e54095f49b328bdd4db1350a', '9fbd1016bb58ae06d9e557ebd281f707f54b8fc5',
     'sha256:197254b69161aacef79dbb93c86939c4cc1b82e9cc39ac2fa0584207ea6cc558'),
    (37, 'W8-D6-CDB', 'docs/phases/W8-D6-contact-decision-brief.md',
     '753e6abea8d67a16332799af615fdcfa4aefa7b9', 'ddde7b3553b5f21dc929010c5c90dba701a70980',
     'sha256:034483363a210df7a736749d5f30e6cf68a6e57c77b7b07001f3770f8567a196'),
    (38, 'W8-D6-CDR', 'docs/phases/W8-D6-contact-decision-record.md',
     'e76be12b537f67a1041422ee73c22cbbfcf8b8c5', '842472148111e78abd9d7fc7273fa1b19426dc75',
     'sha256:c7381ac0bbfeac59b94057b9de359fdd072cc2003e1f06179e833492be71bfa3'),
    (39, 'W8-D7-CAB', 'docs/phases/W8-D7-A-closure-authorisation-brief.md',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', '50ee207397b4c772e8a479004f507f46ed821026',
     'sha256:28011515753cb45c66a3ef0dd8999bd6b7758f352b01bf03ebc1ea5ed824246f'),
    (40, 'W7-CR', 'docs/phases/W7-closure-record.md',
     '7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3', 'f57ea174237205f2d4e0783f48469ab84abe5c97',
     'sha256:8086966f2355c59d2c8ea34593d177446cac0ec9707977b27d186b7e0d96200a'),
    (41, 'W7-D7-CAR', 'docs/phases/W7-D7-B-closure-assessment-record.md',
     '03ca823b5accfc5616b2e22ff642066882fe5274', '318a3bc5b8d79e666e4829b3068e9e7fbbf717d3',
     'sha256:8c2a5412b44b594bd2133321f47fcc0a2c209082e5877091a486dd5cdb21860c'),
    (42, 'W7-D7-CAB', 'docs/phases/W7-D7-A-closure-authorisation-brief.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', '7d1b609764ca3b8ad5171a113477b5df4a32cd1f',
     'sha256:76b6e0c45d3e6384736d4aabbd7db3ff0923d36d33d188b37da2a9ab8fb1f080'),
    (43, 'W6-D6-CAB', 'docs/phases/W6-D6-A-closure-authorisation-brief.md',
     '8a764e92a04b8fbcabb2b2fba1eb0b7f3646c3da', '535d2443ab1f613691022a7f6590c14c27619fd0',
     'sha256:2e4098691c6fe45772855e49d74464ac8e45dab6fedb4779319178d2a30da57f'),
    (44, 'W6-CR', 'docs/phases/W6-closure-record.md',
     '508ea5729d05ae838b15761d4d56ecc65bc61f91', '9f3d15847f210421f0ff38845d9391f61059659b',
     'sha256:a720fb1970235965c3a978410c9adc0176ab2d2f5152c056d2197ff6b11eb80e'),
    (45, 'W7-D6-HDR', 'docs/phases/W7-D6-human-review-disposition-record.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'fc3746b06b8529d085814cef45747f16c9cce0ed',
     'sha256:8bd96c1f22c9664e4c891ad3827a6c818fd1ac82f2e62df1990a977e5216fea8'),
    (46, 'W7-D5-SEC', 'docs/phases/W7-D5-synthetic-execution-materialisation-record.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', '5398844cc752554562175e653eedebb9c2acb57f',
     'sha256:1e8ac6895e216ac1ad54c034a8303dcdcd3ec40d5a1c8ee8c043b3478ae70f65'),
    (47, 'W7-D5-RUN-01', 'governance/generated-evaluation/W7-D5-RUN-01-manifest.json',
     'a32579361f19556520e188cb8220b23d95323a4c', '73128202ebf9ae9f2428a330eff2453093589029',
     'sha256:ed8ea66b8de389bf5c7afeffb852b7c116e56da4031d97e8af713763c449afa7'),
    (48, 'W7-D4-SHR', 'docs/phases/W7-D4-synthetic-harness-binding-record.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', '2bc7288be8a4312d4adf56ef9b2f2cc63ba89c5d',
     'sha256:0ed7151f4f845f463a52f423809694b96d47d0e78cf5e9843a32a3688a136bf1'),
    (49, 'W7-D3-MBB', 'docs/phases/W7-D3-model-boundary-opening-brief.md',
     '5ce8a923e8a52bf17e9b4c1bd81d1e714c79b135', 'dd05f5732bdbaf50971b2fd898c162ca5eeb0524',
     'sha256:593a4b49605672301c1f15bfe5affe8f60cbc0ab737a3e2c6ac4192616487e30'),
    (50, 'W7-D2-E', 'docs/phases/W7-D2-E-proof-completion-record.md',
     '59dfcb685b84de56499a57b1ff91402ed4d864b7', 'fe20be6e7c630063a2be045208703facc2267e33',
     'sha256:a75cdb36e61edaf33452f349e10163d691551c47314787fbf6e82063dea791b8'),
    (51, 'ADR-0046', 'docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', '14c1208e81fb59763a1f78ee3676276149b75b08',
     'sha256:b2bac9e3bbf3fd3cd3991c174671f2dbbbde3832363ef3df93cb67cde3de5270'),
    (52, 'ADR-0047', 'docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md',
     '02b58ccc9f37f46a72b79b9e61e6028057d313b7', '5f1fb5581a98ea8d9f03d97ad39a4bc39158c079',
     'sha256:63f8c84fe2a3235d69340e4bcbcb4cd1d2497ff46b89876ac128b097f6c72a35'),
    (53, 'ADR-0049', 'docs/decisions/0049-generated-evaluation-field-law.md',
     'a6de4c6e84d6691e0ddce6a9a30b5adada1d27bd', 'abdfc33fab988e80dd0012a6dd23fbc38d73e28a',
     'sha256:bca3d94732bc95737ef77a5a0ae74561b91ddf3d62b0862d76cdfef9618af1d9'),
    (54, 'ADR-0051', 'docs/decisions/0051-model-boundary-no-public-contact.md',
     'e1dd86d561e458babdcfa56e6923aba9fb6f63b2', '2800a8260fc4379133fce418ea3e20fe5929e607',
     'sha256:a1af46b27a52fed4a1bb0f30c9b449148ba8178ddffddbcc76a1acbb634efda6'),
    (55, 'ADR-0052', 'docs/decisions/0052-exclusion-list-conformance-p4-decomposition.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', 'e3d917edbf7b0cca131bbd5e0a5884e696bb0246',
     'sha256:46299e137b86a91bf76e964017a103e03da5b3d71830b86390d369e7b1327050'),
    (56, 'ADR-0053', 'docs/decisions/0053-human-review-generated-evaluation-disposition-law.md',
     '329a9b03f34104876a1fcfac47aefc76f7cc08cd', '20d6fd1349ed170508dca822f0a00fc78ec9ceb9',
     'sha256:d03333fa6e1b1b3363ccd4aa5bffcd16bba794e997705460776ac004900f3ff2'),
    (57, 'ADR-0050', 'docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md',
     '6c8a0e6c35eb58beb190bc50793ecf55948ec6d1', 'ec158f01e1e9486db7d45a483a674cdf7d5eb655',
     'sha256:8244509cb6578b92ff0dfc024d51cdeaf7bb11fca983df71424ad348e29276f0'),
    (58, 'ADR-0033', 'docs/decisions/0033-model-access.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'aefac956a771819d9116c22fc2dd49084efb97e8',
     'sha256:1ce7c980b3e45342e5fe485d053d9f4ef3ab887015914158a5146345a076ceba'),
    (59, 'ADR-0034', 'docs/decisions/0034-behavioural-evaluation-architecture.md',
     '6230d42649c0bc5d55250952c7b49d26412a8bb0', '92ad83d996e64f7671fb108fae0efe4766fc63a5',
     'sha256:650d51c916a74618a9967b9238d5acd727ba7d5b2c1362d94ed92255d906e982'),
    (60, 'W2-D3', 'docs/governance/checklist.md',
     '7e9c200d6d4efaa29bcd1052180aa557f0ef6e5c', 'f53817352446e1a28af4f57d7ff348427c2017cf',
     'sha256:3d074684d31364802a614e8b87f48f6ae6396ddb026989f1c3d8b3ad53a51ab9'),
    (61, 'REGISTRY-MD', 'docs/governance/registry.md',
     'a3dce11c8e1b8785160c443ad9ed8d47c4df98ee', '7c8eb0ed4ca54329a5a3141c9b279f1950dd9326',
     'sha256:0c0b63cbd54ec6b30fc37076ba4919ba20ffa8409e67d600e473a3e6007f02df'),
    (62, 'REGISTRY-JSON', 'governance/registry.json',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', '7e57cf81ddae4088af0f8ee9f15d1dc5ce662d0a',
     'sha256:621bb53129dda239b27aead54961787ea1dd04cee395b369e137486da18d9dd2'),
)
TRACE_HEADER = "| Phase | Traced identities |"
TRACE_SEPARATOR = "|---|---|"
FILES_HEADER = "| # | Published path | Commit | Object | Raw SHA-256 |"
FILES_SEPARATOR = "|---|---|---|---|---|"
PINNED_ENTRY_POINTS = (
    'W8-AR',
    'W7-CR',
    'W7-D7-CAR',
    'W7-D7-CAB',
    'W6-D6-CAB',
    'ADR-0047',
    'ADR-0052',
    'ADR-0046',
    'ADR-0051',
    'ADR-0054',
    'ADR-0056',
    'ADR-0058',
    'ADR-0059',
    'ADR-0061',
    'W8-D3-CCR',
    'W8-D4-CPR',
    'W8-D5-AFR',
    'W8-D6-CDB',
    'W8-D6-CDR',
    'W8-DER',
)
TRACE_ROWS = (
    ('W0', (
        'W0',
    )),
    ('W1', (
        'ADR-0001',
        'ADR-0002',
        'W1-D1',
        'W1-D2',
        'W1-D3',
        'W1-D5',
        'W1-D6',
    )),
    ('W2', (
        'ADR-0003',
        'W2-AR',
        'W2-CR',
        'W2-D1',
        'W2-D2',
        'W2-D3',
        'W2-D4',
    )),
    ('W3', (
        'ADR-0004',
        'ADR-0005',
        'ADR-0006',
        'ADR-0007',
        'ADR-0008',
        'ADR-0009',
        'ADR-0010',
        'ADR-0011',
        'ADR-0012',
        'ADR-0013',
        'ADR-0015',
        'W3-AR',
        'W3-CR',
        'W3-D2-CR',
        'W3-D3-CR',
        'W3-D4-CR',
        'W3-D5-CR',
        'W3-D6-CR',
    )),
    ('W4', (
        'ADR-0016',
        'ADR-0017',
        'ADR-0018',
        'ADR-0019',
        'ADR-0020',
        'ADR-0021',
        'W4-AR',
        'W4-D2',
        'W4-D3',
        'W4-D4',
        'W4-D5',
        'ADR-0022',
        'W4-D6-EASR',
        'W4-D6-PHDAR',
        'W4-D6-BEF',
        'W4-CR',
    )),
    ('W5', (
        'W5-AR',
        'ADR-0023',
        'ADR-0024',
        'ADR-0025',
        'ADR-0026',
        'ADR-0027',
        'ADR-0029',
        'ADR-0030',
        'ADR-0031',
        'ADR-0032',
        'ADR-0033',
        'ADR-0034',
        'ADR-0035',
        'ADR-0036',
        'ADR-0037',
        'W5-D5-LCM',
        'W5-CR',
    )),
    ('W6', (
        'W6-AR',
        'W6-D1-SDB',
        'ADR-0038',
        'ADR-0039',
        'ADR-0040',
        'ADR-0041',
        'ADR-0042',
        'ADR-0043',
        'W6-D2-GSC',
        'ADR-0044',
        'ADR-0045',
        'W6-D2-CD',
        'W6-CAT',
        'W6-D2-CR',
        'W6-D3-LLG',
        'W6-D3-GR',
        'W6-D3-CR',
        'W6-D4-SOB',
        'W6-D4-SMR',
        'W6-D4-CR',
        'W6-D5-PAB',
        'W6-D5-AER',
        'W6-D5-AFR',
        'W6-D5-CR',
        'W6-D6-CAB',
        'W6-D6-CAR',
        'W6-CR',
    )),
    ('W7', (
        'W7-AR',
        'W7-D1-FCB',
        'ADR-0046',
        'ADR-0047',
        'W7-D2-RSB',
        'ADR-0048',
        'ADR-0049',
        'ADR-0050',
        'W7-D2-E',
        'W7-D3-MBB',
        'ADR-0051',
        'W7-D4-SHB',
        'ADR-0052',
        'W7-D4-SHR',
        'W7-D5-SEB',
        'W7-D5-PSA',
        'W7-D5-MRA',
        'W7-D5-SEC',
        'W7-D6-HRB',
        'ADR-0053',
        'W7-D6-HDR',
        'W7-D7-CAB',
        'W7-D7-CAR',
        'W7-CR',
    )),
    ('W8', (
        'W8-AR',
        'W8-D1-EDB',
        'ADR-0054',
        'W8-D2-DIB',
        'ADR-0055',
        'W8-D2-MSA',
        'W8-D2-DIC',
        'W8-D2-CM-01',
        'ADR-0056',
        'W8-D2-CBC',
        'W8-D3-SCB',
        'ADR-0057',
        'ADR-0058',
        'ADR-0059',
        'W8-S1-SOB',
        'W8-S1-SCR',
        'W8-S1-CM-01',
        'W8-HPC',
        'W8-D3-HDR',
        'W8-D3-DR-01',
        'W8-HAC',
        'W8-D3-CCR',
        'W8-D4-IVB',
        'ADR-0060',
        'W8-D4-VCR',
        'W8-V1-CM-01',
        'W8-V1-CM-02',
        'W8-CHC',
        'W8-D4-VSR',
        'W8-D4-DR-01',
        'W8-D4-VRC',
        'W8-D4-CPR',
        'W8-DER',
        'W8-D5-EAB',
        'ADR-0061',
        'W8-D5-AFR',
        'W8-D6-CDB',
        'W8-D6-CDR',
        'W8-D7-CAB',
    )),
)
EXTRA_READ = ('W7-D5-RUN-01', 'REGISTRY-MD', 'REGISTRY-JSON')
FILE_ROWS = (
    (1, 'README.md',
     '6704649ed80c27112c00c14093c82645e8d090cf', '0845e4a0b06126bafb094918a899c24e255a0e93',
     'sha256:32c9bd765ad3942dc2312f5d6bcac12f2fe642a98956ec13d0e801cf92310931'),
    (2, 'docs/wellbeing-wing-concept-overview.md',
     '571ac0076590c6b3346f53ef828bc0c1ad2f9cad', '0c88c7b71e687ed00f5775a9c14c763f856e4a3f',
     'sha256:a07f55b97bf90c8d11fc17796b3866b6cfe236ee972bb5b271fe4dda579acf32'),
    (3, 'docs/phases/README.md',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', '28b550c5afe1e9063d8f8223ffffe8e140b33b63',
     'sha256:564c057c4cecf97bee51caa78a7d80439dc707df7b24c60fff66ada55b11577d'),
    (4, 'requirements.txt',
     'd44095392ff2b3423d3553cb6126281406826217', 'af54e0115de3122f06fa1a4eb842237097f09e04',
     'sha256:5a9d082185d9671e2ee48b45dd2a9e847adaebccdb37a9ec2aaa1558187dc4b3'),
    (5, 'scripts/public-safety-scan.py',
     '7e9c200d6d4efaa29bcd1052180aa557f0ef6e5c', 'f79c87ff8445d1d1dee5b4433a775958d49e8a13',
     'sha256:3dd60c3f16c8e1078e98951203e800aa275af67217d82f289cc28e9a6f9da707'),
    (6, 'scripts/scan-allowlist.txt',
     'a3dce11c8e1b8785160c443ad9ed8d47c4df98ee', 'a5984cb8b781cfabc4032d166e651c69606513b2',
     'sha256:72a1c836bee59d310dd453e96085a9543b04bc23746dd4ba7f1db718655586f6'),
    (7, 'tests/test_repo_state.py',
     '567ffeace14a8abf7396c97ca034ebb77fbcf62d', '2db3c34605a9808a74c8944cfd53c2538d811416',
     'sha256:87458324761da1fa35cd1b690bc4549fed40a63a6749704ad39f9c4c45c245fd'),
    (8, 'tests/test_pending_ledger.py',
     '8465c538a76f628c86f097eea3942b993147a548', '86eeb87cd9e3733a5aa177c5c8b3642ec5a06884',
     'sha256:78c681b9fd49c76a3bd66304f1098b9fafa1b29414741c080839bedf15a4dd76'),
    (9, 'tests/w8_review_packet.py',
     '372287baa4e71bce4353bbdf9ce5e0f2aec93fe1', '763d5e3f1d0dd26fe6ac3f542cf3152f9342e9e1',
     'sha256:6bfc534b65523a0dfb021639179201662853a1bda9235e44c30cee22e48bfbf9'),
    (10, 'tests/test_w8_evaluation_doctrine.py',
     '6e9e0f155944bea3117b82a5b4216ce6c50abaa4', '0e871fb84c048ae59b943f3440cd1bfd1da95cf6',
     'sha256:36d6364e5123e41625ee23c85e41f64a371b2d547d36eb90acc1b3ad0dac1caa'),
    (11, 'tests/test_w8_discriminating_instrument_envelope.py',
     '67ed076503f1087cefed31dd163a706a87d3b8a6', 'ec932062722d07a7d109dc3a3a90d1dfc38f9895',
     'sha256:d4685301e949b072510b38862dc59ebdcef9e383cc549d186712940c3d8fba4c'),
    (12, 'tests/test_w8_discriminating_instrument_corpus.py',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'ca01abea93578c1bcc8fb0c3ada5e208b8f1e616',
     'sha256:1d9ffef924e73d10d70e23e08b54ce5ea8e50051dfcc4f556f88b56321b20652'),
    (13, 'tests/test_w8_calibration_law.py',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'aaba3ce6dd15dfc194d7b8e0f5e2960099df6bc7',
     'sha256:aa3870f66b9fc8b739e35261412f25243aedf29c50b41d4f7ac15a28152b757c'),
    (14, 'tests/test_w8_session_recovery_law.py',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', '3ec9548ad2b334a2ac927dfc501d9720cedc819e',
     'sha256:dbedab0e9f9d5e381c2770914ee056cb4d05695ccd9afd30cc54dcb52e976276'),
    (15, 'tests/test_w8_recovery_authority.py',
     '9ded8c44abfd4c911d938814a7f551944998ec53', '92366ee9d832302a59a4758964d16a628ad106ea',
     'sha256:c1371e53ea1c3828f1a7aa348da3be1f83b63024a362cfcc5aad0b6014e3731b'),
    (16, 'tests/test_w8_supplementary_corpus.py',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', '8f94e3ca0dfa3ceb4d782309dae5956fa712c1fb',
     'sha256:b90ec8624d156579898094fb4996c73d1aad4c7d9e638f4d04ad26f3a72b6731'),
    (17, 'tests/test_w8_disposition_record.py',
     '317c0ba9de76853d454774085cdf18f3a638c02f', 'cca9b78557f205994af4753e9f4c4bc8b6fbdaca',
     'sha256:cbbc829168ee0077b926655557c6bc761c3284ec4b725a3f28b755a74ae3fb9d'),
    (18, 'tests/test_w8_reveal_calibration.py',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'f2170f1eeb3cb27370fb3b75f803452b5c1fee43',
     'sha256:834f59ab7fe33d18a49c6bee53320af9b1f76cd8e8c4ab68173ba9f8e58e8e56'),
    (19, 'tests/test_w8_validation_opening.py',
     '054f1270b8206a059636e18e012223ddfe52d5ea', '71f5072562773b1784c07063fa1b5ea3ec51559e',
     'sha256:d0917547faca6e9ae09ad31dfb9a3516c3578c8a09d7403f678fc9cc10112d52'),
    (20, 'tests/test_w8_validation_law.py',
     'ce78a242df25898d90debee9513bdce7e511471b', '7c3d7e4fb1a5f82a8a38bd09d03f1be5059b491e',
     'sha256:a3bbdad77f375cd91cb5646ea234f01a44fe66e1cbc5aab8de54206e7580c762'),
    (21, 'tests/test_w8_validation_corpus.py',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9', '182211dde1611a59b1e57357167a51b2d5533a63',
     'sha256:c32d7c871ca3a8e52478f5ef0096e2b3d2a3e9f4e46814dc2e0574eb22882ce8'),
    (22, 'tests/test_w8_case_home_scope_correction.py',
     'a08ba584bea8e2576dd7450c6374a4ff4f0aa149', '24cd925f7224af0ec501d68276f43b2d107a9682',
     'sha256:075c15f7bad1f26aacd0d7254d8f25fda560bcd28f452857fed4718dc047bbce'),
    (23, 'tests/test_w8_validation_session.py',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'b991e1a8a234915c1ce5ef8b26b9f29c3173af24',
     'sha256:fbdb5169c6f0cb33f60c37e8ec3287b189196fdc2ce0ea09a77a50eb7a9375c4'),
    (24, 'tests/test_w8_validation_reveal.py',
     '67ed076503f1087cefed31dd163a706a87d3b8a6', '8902cb9b2b015ae70772d711826b5018e522fa98',
     'sha256:71d8cd12848612d30fb108d10da759c673d6efcd4e1055ff5ddbc484a4b5c301'),
    (25, 'tests/test_w8_validation_completion.py',
     'ce78a242df25898d90debee9513bdce7e511471b', '95341e0f19bdace286156ff17b524062cde53088',
     'sha256:be6029a8d2f7f9a4b37709e6e12816d899dae74fc880d4733f01abec1de9f8e1'),
    (26, 'tests/test_w8_documentation_erratum.py',
     '6704649ed80c27112c00c14093c82645e8d090cf', 'ea1be87d053890a741367766fb483341cce96cbd',
     'sha256:ea37b1c41aa990b3e83a10a21f69e3070b58942dd7692aa9ac7e6c71ce19056b'),
    (27, 'tests/test_w8_evidence_adequacy_opening.py',
     '18d6230b5f7281577c18892dd7b95e9448f310c2', '3f4618de92871e3470d33737f2a03cb5f1a71911',
     'sha256:bb118225a9ae95a48a3424b997202fe29e154ab655888dea45e2a44fcdfa56b7'),
    (28, 'tests/test_w8_evidence_adequacy_law.py',
     '2aa2c75d20363ca7e54095f49b328bdd4db1350a', '330658b9c713cea91979aef98323307ba65964da',
     'sha256:2104f9b5d3b1375698c7ec1b13e15817a31bdb9000bf194933dc0c8b3bda7a27'),
    (29, 'tests/test_w8_evidence_adequacy_finding.py',
     '2aa2c75d20363ca7e54095f49b328bdd4db1350a', '6f3ab8795b55a08ece8438a434d0eb96c2dd4929',
     'sha256:320b1227a18184279804289dabb09c070ccedcf826f53e8f81f66d77f7eb81cf'),
    (30, 'tests/test_w8_contact_decision_opening.py',
     'e76be12b537f67a1041422ee73c22cbbfcf8b8c5', '645758e1f53f7ec60c1cac42ff938d5fd1dd41f5',
     'sha256:94572c3ee65f7895b0630c8fe41c736321ae8db030197db79406009947bd0322'),
    (31, 'tests/test_w8_contact_decision_record.py',
     'e76be12b537f67a1041422ee73c22cbbfcf8b8c5', '660cebf91dcabf176ac110b85661f5259680fa26',
     'sha256:f69d2ad99a2818a58862529e2dfc4da045b5936f1305bd781c428f26942f537f'),
    (32, 'tests/test_w8_closure_opening.py',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', 'dfa8fde2929d2ba6edccdc52367d7f95c6412499',
     'sha256:f16c74c26cba7f2ad9655aa9068a762531d4d60f0680a7cf9af72a2ac15207dd'),
)

# ------------------------------------------- every proof-module change in W8
# (landing commit, module, site labels, governing record, kind, pre-image LF
# SHA-256 at the landing's first parent, post-image LF SHA-256 at the
# landing, whether the governing record pins the pair).
AUDIT_SECTION = "## 5. Proof and obligation succession audit"
AUDIT_HEADER = ("| # | Landing | Module | Site | Governing record | Kind | "
                "Pre-image LF SHA-256 | Post-image LF SHA-256 |")
AUDIT_SEPARATOR = "|---|---|---|---|---|---|---|---|"
OBLIGATION_HEADER = "| Obligation | State at this baseline | Source evidence |"
OBLIGATION_SEPARATOR = "|---|---|---|"
MODULE_HEADER = "| Module | Rows | Tests | Live reach at the baseline |"
MODULE_SEPARATOR = "|---|---|---|---|"
SUCCESSIONS = (
    ('117a192091bfafa80cb3f6ae567b63204b6c7676', 'tests/test_w7_human_review_dispositions.py', 'H15', 'W8-AR', 'succession',
     'sha256:d15482050f35ca4f3aff40001ad77d2b6b1e9f5db0b4b8e68a6221f8e4610d80',
     'sha256:914880274400f9637e46543e8f80d4e809a824b7b7a350455e0d9d2407389414', False),
    ('756d3d3512202a905a5d3b689d75bf06ae31ccf5', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-D2-DIC', 'succession',
     'sha256:c552b74eabad81672e571f3e199b532b27e0e66d3da832b112cc87db951658a0',
     'sha256:cca0b83d0c50675b3ec1d32aa2b11f29a61633a47a0bf5d3434d9b1f6143d5b9', False),
    ('1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'tests/test_w6_review_surface.py', 'identity', 'ADR-0056', 'remediation',
     'sha256:58e41307cb39c4b600ca581ba7984d572109358ce51ac7c21c31181f9aaee3ec',
     'sha256:a07e1a1e3e3d8b824f4bcf8b90a19082d2ad2c107f68b051314a396b6b349faf', False),
    ('1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'tests/test_w7_human_review_dispositions.py', 'identity', 'ADR-0056', 'remediation',
     'sha256:914880274400f9637e46543e8f80d4e809a824b7b7a350455e0d9d2407389414',
     'sha256:882f82b2f8e509411802ccc29ccf552b85d925946a108cc295b0ad7e2728a9bd', False),
    ('a4997128055462bb4791cfa5c5d06c3a3f51b0ba', 'tests/test_w8_discriminating_instrument_corpus.py', 'C2, C4, C5', 'W8-D2-CBC', 'correction',
     'sha256:92b27eff25bc00cf4af1d0e7b3faeb5ac809fa84525caf684ac77cbfc9fc29b6',
     'sha256:7e9a5e7d7101c33fa3a79bf5979411b8c8a1da989731fcdbd0ca911766e22698', False),
    ('2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'tests/test_w8_session_recovery_law.py', 'R5', 'ADR-0059', 'succession',
     'sha256:0471aa9ad53b84a07a784e3376f30e9b444b698d359559937f765f69fb209163',
     'sha256:a50c71a2074cf5f31660f1bda5434c6bf592a9ec9a44719ffb47c91fadfdedb9', True),
    ('83253039ec274a2496b37b618949fd00d3cd7c8e', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-S1-SCR', 'succession',
     'sha256:cca0b83d0c50675b3ec1d32aa2b11f29a61633a47a0bf5d3434d9b1f6143d5b9',
     'sha256:e7e80df8dbad8397574b9558a3892ac638e16e0d3549e2662e6181a55bb6944e', True),
    ('83253039ec274a2496b37b618949fd00d3cd7c8e', 'tests/test_w8_recovery_authority.py', 'A9', 'W8-S1-SCR', 'succession',
     'sha256:2390dcaed53b5d9bffe3e1c53bcbaeac97290e2572162adaa3f78dc43cb45299',
     'sha256:ed8b7bdd012d8164e76d5cebc47c4190e3f8adbc254e1da91addd45d56a2901e', True),
    ('9ded8c44abfd4c911d938814a7f551944998ec53', 'tests/test_w8_recovery_authority.py', 'A3', 'W8-HPC', 'correction',
     'sha256:ed8b7bdd012d8164e76d5cebc47c4190e3f8adbc254e1da91addd45d56a2901e',
     'sha256:c1371e53ea1c3828f1a7aa348da3be1f83b63024a362cfcc5aad0b6014e3731b', True),
    ('66b6e6ca7e33e5e0fd326d61653a0c13d1679878', 'tests/test_w8_calibration_law.py', 'K12', 'W8-D3-HDR', 'succession',
     'sha256:d9e372ee85b37adc2b70ba8ff3d08de564debaaadf3b9e98f303b9ea69d4dcc8',
     'sha256:448e1aa056a9ce176d7ae1b1856bb6eb459b8e1180fc0eae341419c5c19dc328', True),
    ('66b6e6ca7e33e5e0fd326d61653a0c13d1679878', 'tests/test_w8_session_recovery_law.py', 'R7, R9', 'W8-D3-HDR', 'succession',
     'sha256:a50c71a2074cf5f31660f1bda5434c6bf592a9ec9a44719ffb47c91fadfdedb9',
     'sha256:8934a5248504228a0950f5afedc523a377e063746d3e18e37dced914855219ea', True),
    ('317c0ba9de76853d454774085cdf18f3a638c02f', 'tests/test_w8_disposition_record.py', 'H9', 'W8-HAC', 'correction',
     'sha256:14e1c88341a387335df6c87ea04546fbfc1714ed987b94b1335b4d5e3429c77d',
     'sha256:cbbc829168ee0077b926655557c6bc761c3284ec4b725a3f28b755a74ae3fb9d', True),
    ('3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-D3-CCR', 'succession',
     'sha256:e7e80df8dbad8397574b9558a3892ac638e16e0d3549e2662e6181a55bb6944e',
     'sha256:99047ceb3f58f5209598d9eb84cd6972cc2786ca4e7a43ce1dfbfe8f592d7323', True),
    ('3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'tests/test_w8_discriminating_instrument_corpus.py', 'C10', 'W8-D3-CCR', 'succession',
     'sha256:7e9a5e7d7101c33fa3a79bf5979411b8c8a1da989731fcdbd0ca911766e22698',
     'sha256:1d9ffef924e73d10d70e23e08b54ce5ea8e50051dfcc4f556f88b56321b20652', True),
    ('3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'tests/test_w8_calibration_law.py', 'K12', 'W8-D3-CCR', 'succession',
     'sha256:448e1aa056a9ce176d7ae1b1856bb6eb459b8e1180fc0eae341419c5c19dc328',
     'sha256:2dca05bbd21544cdd3e524e59c2e431172e88e571441a22588f47a9f2141e36f', True),
    ('3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'tests/test_w8_session_recovery_law.py', 'R7, R8, R9', 'W8-D3-CCR', 'succession',
     'sha256:8934a5248504228a0950f5afedc523a377e063746d3e18e37dced914855219ea',
     'sha256:9c1c6dd6c534ce1fd8400442259e5da87c35821c19708695f513b4265a56bd2b', True),
    ('3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'tests/test_w8_supplementary_corpus.py', 'S10', 'W8-D3-CCR', 'succession',
     'sha256:4a810d1be35c82f556362a9497624174351ce81d3e90b9241b3f88b116fc833e',
     'sha256:b90ec8624d156579898094fb4996c73d1aad4c7d9e638f4d04ad26f3a72b6731', True),
    ('ad59925813f8b0c39789dac3b29383a5f6e25cea', 'tests/test_w8_session_recovery_law.py', 'R9', 'W8-D4-IVB', 'succession',
     'sha256:9c1c6dd6c534ce1fd8400442259e5da87c35821c19708695f513b4265a56bd2b',
     'sha256:6873de43760267cb51366078818cbc33ac5e50bbfd8cabe9eb840dd05d910b97', True),
    ('054f1270b8206a059636e18e012223ddfe52d5ea', 'tests/test_w8_validation_opening.py', 'VB7', 'ADR-0060', 'succession',
     'sha256:d83f21e8afb4965e32741a0bdefebb5dad7d68e6cd569dc0a6e3a2cd1b6b7f4c',
     'sha256:d0917547faca6e9ae09ad31dfb9a3516c3578c8a09d7403f678fc9cc10112d52', True),
    ('f638cca75ec4a192685bf5cd53f29451cfdbbdd9', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-D4-VCR', 'succession',
     'sha256:99047ceb3f58f5209598d9eb84cd6972cc2786ca4e7a43ce1dfbfe8f592d7323',
     'sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80', True),
    ('f638cca75ec4a192685bf5cd53f29451cfdbbdd9', 'tests/test_w8_validation_law.py', 'VL10', 'W8-D4-VCR', 'succession',
     'sha256:b07e367761654ad3856f64598e513bea8b81badadab1fb2dd66b6a30082a88d9',
     'sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02', True),
    ('a08ba584bea8e2576dd7450c6374a4ff4f0aa149', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-CHC', 'correction',
     'sha256:c86bbe23f743e3fb218a0aec47071f747d53bc2f4aee0e2ea589caa02c6d7f80',
     'sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700', True),
    ('44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'tests/test_w8_calibration_law.py', 'K12', 'W8-D4-VSR', 'succession',
     'sha256:2dca05bbd21544cdd3e524e59c2e431172e88e571441a22588f47a9f2141e36f',
     'sha256:aa3870f66b9fc8b739e35261412f25243aedf29c50b41d4f7ac15a28152b757c', True),
    ('44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'tests/test_w8_validation_law.py', 'VL10', 'W8-D4-VSR', 'succession',
     'sha256:0047e9faf3ca8cc75a05b158d3272777386332b758ca0b035aac677cdd825c02',
     'sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113', True),
    ('67ed076503f1087cefed31dd163a706a87d3b8a6', 'tests/test_w8_discriminating_instrument_envelope.py', 'V12', 'W8-D4-VRC', 'succession',
     'sha256:cc5358a394f4c9028f1d326a6f40eada50951c684d3cbd93f19cee540e222700',
     'sha256:d4685301e949b072510b38862dc59ebdcef9e383cc549d186712940c3d8fba4c', True),
    ('67ed076503f1087cefed31dd163a706a87d3b8a6', 'tests/test_w8_validation_law.py', 'VL10', 'W8-D4-VRC', 'succession',
     'sha256:ed4c6fac449e261b637c0d42fb83e7ac45f204f84eaf7db4954fd3b307a7a113',
     'sha256:66a16bf2fe7cd71ff0dd382dbe30ce9b1afc35da5d90060082c7a79960ad6c50', True),
    ('ce78a242df25898d90debee9513bdce7e511471b', 'tests/test_w8_validation_law.py', 'VL10', 'W8-D4-CPR', 'succession',
     'sha256:66a16bf2fe7cd71ff0dd382dbe30ce9b1afc35da5d90060082c7a79960ad6c50',
     'sha256:a3bbdad77f375cd91cb5646ea234f01a44fe66e1cbc5aab8de54206e7580c762', True),
    ('c8e13d47f305e0378609ffec1d31f890f629239d', 'tests/test_w8_session_recovery_law.py', 'R9', 'W8-D5-EAB', 'succession',
     'sha256:6873de43760267cb51366078818cbc33ac5e50bbfd8cabe9eb840dd05d910b97',
     'sha256:a1efe9fb15e75868acfb763c37735e648baa7bea62fe1b1357d80f078c2e6537', True),
    ('18d6230b5f7281577c18892dd7b95e9448f310c2', 'tests/test_w8_evidence_adequacy_opening.py', 'EA7', 'ADR-0061', 'succession',
     'sha256:84df93a8e79ec5ffe477756e126993b240d57ee2f848019ddce8191071f61a61',
     'sha256:bb118225a9ae95a48a3424b997202fe29e154ab655888dea45e2a44fcdfa56b7', True),
    ('2aa2c75d20363ca7e54095f49b328bdd4db1350a', 'tests/test_w8_evidence_adequacy_law.py', 'EL7', 'W8-D5-AFR', 'succession',
     'sha256:84cacb92c68a1fb77ab2a6adb79185c5cc9ae64fef15fe6a3ea894fa7c47be24',
     'sha256:2104f9b5d3b1375698c7ec1b13e15817a31bdb9000bf194933dc0c8b3bda7a27', True),
    ('753e6abea8d67a16332799af615fdcfa4aefa7b9', 'tests/test_w8_session_recovery_law.py', 'R9', 'W8-D6-CDB', 'succession',
     'sha256:a1efe9fb15e75868acfb763c37735e648baa7bea62fe1b1357d80f078c2e6537',
     'sha256:25bc3f70d043c854471748bdf6a6c1fe6e7864ce047007df19348dbd66293261', True),
    ('e76be12b537f67a1041422ee73c22cbbfcf8b8c5', 'tests/test_w8_contact_decision_opening.py', 'CD7', 'W8-D6-CDR', 'succession',
     'sha256:30c5826a9514c6c069dcd408e85823e25b51144d6f57af83b04803817623e7fb',
     'sha256:94572c3ee65f7895b0630c8fe41c736321ae8db030197db79406009947bd0322', True),
    ('cf2012669b97b323cdbfb182bc10865d444c79c1', 'tests/test_w8_session_recovery_law.py', 'R9', 'W8-D7-CAB', 'succession',
     'sha256:25bc3f70d043c854471748bdf6a6c1fe6e7864ce047007df19348dbd66293261',
     'sha256:dbedab0e9f9d5e381c2770914ee056cb4d05695ccd9afd30cc54dcb52e976276', True),
)

# --------------------------------------------------- the evidence integrity
# (home, the landing commit that fixed it, its tree at the baseline, tracked
# files); the three W7 instrument pins as W7-D7-CAR section 1 records them.
HOMES_SECTION = "## 7. Evidence integrity audit"
HOMES_HEADER = "| Home | Fixed at its landing commit | Tree at the baseline | Tracked files |"
HOMES_SEPARATOR = "|---|---|---|---|"
HOMES = (
    ("governance/discriminating-instrument", "756d3d3512202a905a5d3b689d75bf06ae31ccf5",
     "ecf232275c81adffbc7335f0115ef501b2c92449", 13),
    ("governance/discriminating-supplement", "83253039ec274a2496b37b618949fd00d3cd7c8e",
     "a00a0be832ba597ec2f2b68e19ca37d29af58f6d", 13),
    ("governance/discriminating-review", "66b6e6ca7e33e5e0fd326d61653a0c13d1679878",
     "19a340ad54b6d0b9b54ab42b7f3813e6a9e00594", 1),
    ("governance/discriminating-reveal", "3c34246a5b6989aaa6c5e19621964fa0c7799cdd",
     "c009fef24f746a9ff0daedb05129e82dd6c0bf8a", 12),
    ("governance/validation-cases", "f638cca75ec4a192685bf5cd53f29451cfdbbdd9",
     "77e9a5c8fa760753278e9df3b696bd4647ad5e9f", 20),
    ("governance/validation-review", "44947adf9b60f2ce462be97a2c0e628a3ecbdd89",
     "69c8e35700572e1c5130b7d29d9f82078cddbc2a", 1),
    ("governance/validation-reveal", "67ed076503f1087cefed31dd163a706a87d3b8a6",
     "aeafaa63ed4e77b2b7142343d34320429e7f6948", 36),
    ("governance/generated-evaluation", "a32579361f19556520e188cb8220b23d95323a4c",
     "64e78e0873ca8a7e7a7377b927e7d8fffb1fc7fa", 27),
    ("governance/evaluation", "bf7f8c4bfcc86b72d0ea46f557c78f09b0d2290b",
     "f8861c8bc5faadd66aa126b3920c75070695f5c9", 24),
)
W7_PINS = (
    ("fixtures/SYNTHETIC-w7-d4-exam.json",
     "sha256:9755cca1e8f9e41d7c89d532abb2f674a0189ec58935e3a5763fd641c90406a7"),
    ("tests/w7_synthetic_evaluation_harness.py",
     "sha256:e50172f5393a8753c9f4a93e29ef52e50cd366c0539a7c483787c085ea31f1fb"),
    ("governance/generated-evaluation/W7-D5-RUN-01-manifest.json",
     "sha256:ed8ea66b8de389bf5c7afeffb852b7c116e56da4031d97e8af713763c449afa7"),
)

# ------------------------------------------------------- the closed tables
DELIVERABLE_SECTION = "## 2. Whole-phase deliverable inventory"
DELIVERABLE_HEADER = ("| Deliverable or act | Governing brief | Law, records and registers "
                      "landed under it | Completion record | Public commits | Registry "
                      "identities | Proposed closure posture |")
DELIVERABLE_SEPARATOR = "|---|---|---|---|---|---|---|"
D7_ROW_POSTURE = ("open under its effective brief; **not assessed for closure posture — "
                  "it is the closure programme itself**")
RUNWAY_SECTION = "## 3. Runway obligation assessment"
RUNWAY_HEADER = "| # | Runway obligation | Proposed posture | Source evidence |"
RUNWAY_SEPARATOR = "|---|---|---|---|"
RUNWAY_ROWS = 68
PRECONDITION_SECTION = "## 4. Contact-boundary accounting"
PRECONDITION_HEADER = "| # | Precondition | Closure-time state | Source evidence |"
PRECONDITION_SEPARATOR = "|---|---|---|---|"
INVENTORY_SECTION = "## 9. Inherited, unresolved and next-gate inventory"
INVENTORY_HEADER = ("| # | Item | Source | Current state | Did W8 change it? | Smallest "
                    "lawful future gate, where the source names one | What W8-D7 is "
                    "forbidden to imply |")
INVENTORY_SEPARATOR = "|---|---|---|---|---|---|---|"
INVENTORY_ROWS = 30
SUCCESSION_SECTION = "## 11. Proof successions at this landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
OBLIGATIONS_SECTION = "## 12. Proof obligations for this landing"
SECTION_REF = re.compile(r"§\d+(?:\.\d+)*")

# ---------------------------------------------------------------- carriage
POSTURES = ("satisfied", "satisfied with named carried item",
            "outstanding in lawful resting state",
            "unresolved and bounded under named doctrine",
            "deferred under named doctrine",
            "external / outside repository authority",
            "unopened, named and not supplied")
POSTURE_LINE = (
    "**Only the seven accepted closure postures are used,** each only where the "
    "cited source supports it: **satisfied** · **satisfied with named carried "
    "item** · **outstanding in lawful resting state** · **unresolved and bounded "
    "under named doctrine** · **deferred under named doctrine** · **external / "
    "outside repository authority** · **unopened, named and not supplied**. No "
    "verdict vocabulary is introduced as closure shorthand. Family reasoning "
    "explains; every item receives its own row.")
INVARIANT = ("Any real-person adoption is a separate governed authority outside this "
             "repository.")
REQUIRED = (
    "This record is evidence, not closure.",
    "No declaration of W8's closure appears anywhere in this record, and nothing "
    "in it may be read as one.",
    "A derivative board row is never evidence for the source it describes.",
    "Every posture in this record is proposed by the implementer from the cited "
    "source, and becomes this record's posture only by the human reviewer's "
    "acceptance of this exact record, which adopts or amends each one; until "
    "that act none is declared.",
    "A proof being green is evidence only for the property the proof actually "
    "tests.",
    "Both discrepancies are named here and repaired by nothing in W8-D7",
    "The assessment states exactly, and no more:",
    "This record does not state that no model was contacted in W8, which the "
    "record does not support in that form, and it does not state the contrary.",
    "The reported authority gap stays reported.",
    "P4a and P4b are carried separately, always",
    "Landing C requires a fresh closure-time P4b act by the human reviewer "
    "against the exact final closure candidate, across all eleven families",
    "No mechanical result establishes that any family of ADR-0046 decision 11 "
    "is clear",
    "and no clean ordinary scan is evidence for either P4 clause",
    "No W8-D7 record states or implies that a mechanical run established "
    "conformance to any family.",
    "no new case identity exists because W8-D7 opened:",
    "every recorded divergence remains recorded and undiagnosed",
    "W8-D7 rewrote no history to make closure simpler:",
    "W8-D7 records these discrepancies and repairs none:",
    "No future phase is assigned an obligation merely because this record "
    "needs somewhere to put it.",
    "Historically true assertions stay history; present-state assertions stay "
    "present",
    "Silence is never a decision, and a green suite is never an acceptance.",
    "A refusal outside that landing's authorised successions is a stop.",
    "Every CB row proves mechanics and carriage only.",
    "W8 is not closed, and nothing in this record closes it.",
    "Model contact and the closure of W8 remain outside this record.",
    "no posture in it is declared until the human reviewer's acceptance adopts "
    "it.",
    "the preparation of Landing C, which begins only on the human authority's "
    "separate instruction.",
)
# A bounded fold: emphasis and code marks and the invisible code points
# removed, whitespace runs made one space, case folded.
FOLDED_MARKS = re.compile("[*_`~​‌‍⁠﻿­]")
BLANK_LINE = re.compile(r"^[ \t]*$")
# Wording that would presume the closure or a conclusion about the
# instrument, a model or adoption; none may appear anywhere in the record.
PRESUMPTION = ("w8 is closed", "w8 is complete", "w8 closes because",
               "w8-d7 is satisfied", "w8-d7 is complete", "closure is declared",
               "the instrument is mature", "the instrument is adequate",
               "the instrument is validated", "the instrument is ready",
               "the instrument is safe", "the instrument is useful",
               "contact is warranted", "contact is not warranted",
               "ready for contact", "recommend contact", "recommends contact",
               "should contact", "should be contacted", "the model is safe",
               "safe to contact", "fit for adoption", "approved for use",
               "clinically valid", "proven safe", "w9")
# The formula the architect's review of the opening brief withdrew (ADR-0052
# decisions 3, 4, 6 and 8): none of its forms may appear anywhere.
WITHDRAWN = ("its mechanical surface establishes", "the mechanical surface "
             "establishes", "mechanically establishes that no", "p4 green",
             "mechanical run established complete", "scan establishes that",
             "a green p4a establishes", "p4a establishes",
             "scan established that", "establishes complete exclusion-list "
             "conformance", "established complete exclusion-list conformance")
# Universal session or reveal claims, false for the original corpus
# (ADR-0059 decisions 9, 10 and 19; ADR-0058 decision 5).
UNIVERSAL = ("every case of each corpus", "every case of every corpus",
             "every withheld record was revealed", "revealed every withheld "
             "record byte-exact", "every retained record was revealed",
             "revealed every retained record", "every withheld record of each "
             "corpus", "every withheld record of every corpus", "all withheld "
             "records were revealed", "revealed all withheld records",
             "revealed every withheld record as exact")
# Statements whether model contact occurred, in either direction, which the
# brief's items 37 and 61 bar: the record states only that no W8 act
# prepared, authorised or performed model contact and that the published W8
# records classify no exchange. A bounded inventory of forms; the lawful
# account - "does not state that no model was contacted" - is not a form.
CONTACT_STATEMENTS = ("no model contacted", "no model has been contacted",
                      "no models were contacted", "a model was contacted",
                      "a model has been contacted", "models were contacted",
                      "model contact did occur", "model contact did not occur",
                      "contact did occur", "contact did not occur",
                      "contact took place", "contact never occurred",
                      "contact never took place", "no contact occurred",
                      "no contact took place")
# Attestations that a standing human duty was performed, which the published
# record does not hold: it holds each landing's acceptance (ADR-0052 decision
# 8; W8-D7-CAB items 40 and 46). A bounded inventory of forms.
ATTESTATIONS = ("recorded as fresh human acts", "recorded as performed",
                "attested as performed", "performed at every landing",
                "performed at each landing", "each recorded in its own record")
# Verdict vocabulary as a bold form - the shape a posture cell would take -
# refused anywhere in the record (ADR-0054 decision 31; W8-D7-CAB item 22).
# The inventoried verdict words, refused wherever one stands alone as a bold
# posture. The span is read after the bounded verdict fold: invisible code
# points removed from the text, then the inline marks, spacing and trailing
# punctuation inside the bold span stripped and its case folded, so that a
# code mark, a zero-width space, a soft break, spacing or capitals inside
# the bold form do not hide it. A span that merely contains a verdict word
# among other words is not a posture form.
VERDICT_WORDS = ("pass", "passed", "fail", "failed", "safe", "approved",
                 "ready", "mature", "valid", "winner", "score", "grade")
INVISIBLE = re.compile("[\u200b\u200c\u200d\u2060\ufeff\u00ad]")
BOLD_SPAN = re.compile(r"(\*\*|__)(.+?)\1", re.S)
SPAN_MARKS = re.compile(r"[*_`~\s]+")
# The brief's drafting target is Landing C's business and may not appear
# in the assessment in any form; its opening words are the inventory.
DRAFTING_OPENING = "w8 closes because the governance work assigned to the phase"
WITHHELD = ("It is evidence, not closure", "contacts no model",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "the closure itself, or any declaration before the closure record's "
            "own acceptance, publication and independent remote verification "
            "that W8 or W8-D7 is finished",
            "any selection of a provider, route or model class, or any opening "
            "or narrowing of the hosted class",
            "any Tier F crossing, any amendment of ADR-0051, any implementation "
            "brief or any performing deliverable",
            "any reopening, re-weighing or amendment of the W8-D5 finding, or "
            "any second adequacy finding",
            "any reopening, re-weighing or amendment of the W8-D6 decision",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record",
            "any repair of `docs/governance/registry.md`, of the root "
            "`README.md` or of `docs/wellbeing-wing-concept-overview.md`",
            "any later phase's runway, brief, deliverable or gate",
            "the preparation of Landing C")

NON_AUTH_SECTION = "## 16. Explicit non-authorisations"
NON_AUTH_INTRO = "56. This record and Landing B do not authorise:"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - the closure itself, or any declaration before the closure record's "
    "own acceptance, publication and independent remote verification that W8 "
    "or W8-D7 is finished;",
    "    - any selection of a provider, route or model class, or any opening "
    "or narrowing of the hosted class;",
    "    - any Tier F crossing, any amendment of ADR-0051, any implementation "
    "brief or any performing deliverable;",
    "    - any reopening, re-weighing or amendment of the W8-D5 finding, or "
    "any second adequacy finding;",
    "    - any reopening, re-weighing or amendment of the W8-D6 decision, or "
    "any opening, preparation or placement of a separate instrument it left "
    "unopened;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition, reveal or comparison, "
    "or any change to an existing one, including any made from captured "
    "generated material;",
    "    - any new grouped outcome count, rate or ranking by corpus, authored "
    "class or validation method;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059, ADR-0060 or ADR-0061, or of any accepted W8 brief, "
    "law or record;",
    "    - any repair of `docs/governance/registry.md`, of the root "
    "`README.md` or of `docs/wellbeing-wing-concept-overview.md`, or any "
    "correction, conversion or pending-stub ceremony;",
    "    - any score, rate, ranking, threshold, maturity, readiness, safety, "
    "usefulness, correctness, approval, `certif-` or `complian-` claim;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any discharge, waiver or satisfaction of any ADR-0047 Part D "
    "precondition, any resolution of precondition 3, or any movement of any "
    "carried state;",
    "    - any later phase's runway, brief, deliverable or gate, or any "
    "assignment of an unresolved item to a later phase;",
    "    - the preparation of Landing C, which begins only on the human "
    "authority's separate instruction.",
)
NON_AUTH_CLOSE = "    **Model contact and the closure of W8 remain outside this record.**"
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))

# --------------------------------------- board and registry: authorised edits
CAR_LINK = ("([`W8-D7-B-closure-assessment-record.md`]"
            "(W8-D7-B-closure-assessment-record.md))")
CAR_STATUS_TAIL = (
    "the whole-phase closure assessment of W8-D7, landing B: evidence and not "
    "closure, carrying no declaration that W8 is finished. It derives from "
    "published source at the W8-D7 opening the whole-phase deliverable "
    "inventory from the runway through W8-D6 with every phase-level correction "
    "and erratum, the runway obligation assessment with every obligation, "
    "non-goal, tripwire and quality gate in its own row, the seven ADR-0047 "
    "preconditions with precondition 3 outstanding in its lawful resting state, "
    "the proof and obligation succession audit with every proof-module change "
    "of W8 recomputed from history, the public/private boundary audit "
    "decomposed as ADR-0052 decomposes P4, the evidence integrity audit over "
    "every case home and the W7 class, the incident, correction and learning "
    "log, and the inherited, unresolved and next-gate inventory, item by item; "
    "every posture proposed and adopted only by acceptance. The opening "
    "module's CA7 succeeds, its W8-D7 entry set and no-later-phase limb, to a "
    "historical proof at the W8-D7 opening, the live gates moving to this "
    "record's module; R9's sentence, constant and tuple stay unchanged. The "
    "W8-D5 finding stays undetermined as recorded, the W8-D6 decision stays a "
    "decision that authorises nothing, every separate instrument stays "
    "unopened, every precondition stays unchanged, every divergence stays "
    "undiagnosed and every inherited item stays named and unresolved; the "
    "stale root README, the registry rendering and the concept overview are "
    "named and not repaired; no later phase is opened; no model is contacted.")
CAR_STATUS = {
    "draft": ("**A draft W8-D7 closure assessment, `W8-D7-CAR`, is before the "
              "human reviewer** " + CAR_LINK + ": if accepted, it would publish "
              + CAR_STATUS_TAIL),
    "accepted": ("**The W8-D7 closure assessment, `W8-D7-CAR`, is accepted** "
                 + CAR_LINK + " — accepted %s: it publishes " + CAR_STATUS_TAIL),
}
CAR_ROW = ("| W8-D7 — Closure (assessment record, W8-D7-CAR) | "
           "[`W8-D7-B-closure-assessment-record.md`]"
           "(W8-D7-B-closure-assessment-record.md) | ")
CAR_ROW_BODY = (
    "Tier J: **the whole-phase closure assessment, landing B — evidence, not "
    "closure.** Every inventory, assessment, audit and log the opening brief "
    "requires, derived from published source at the W8-D7 opening and never "
    "from a board row or session memory: the deliverable inventory, the runway "
    "obligation assessment, the contact-boundary accounting, the proof and "
    "obligation succession audit, the public/private boundary audit, the "
    "evidence integrity audit, the incident log and the inherited, unresolved "
    "and next-gate inventory, each item at its true standing and every posture "
    "proposed for the human reviewer's acceptance. The opening module's CA7 "
    "succeeds to a historical proof at the W8-D7 opening, the W8-D7 entry set "
    "and the no-later-phase limb moving to this record's module; R9 unchanged. "
    "**No closure declaration, contact capability, diagnosis, custody access or "
    "derivative repair; the W8-D5 finding stays undetermined as recorded; the "
    "W8-D6 decision stays a decision that authorises nothing; every separate "
    "instrument stays unopened; no later phase opens; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**" + R9_SENTENCE + " W8-D7 is open for closure work only; W8 is "
                 "not closed.**")
# The closing sentence this landing leaves, by state: a draft moves nothing;
# an accepted assessment publishes Landing B and nothing more.
CLOSED_AFTER = {
    "draft": CLOSED_BEFORE,
    "accepted": ("**" + R9_SENTENCE + " W8-D7 is open for closure work only and its "
                 "closure assessment is published; W8 is not closed.**"),
}
# The opening brief's status sentence closes directly before the retained
# closing sentence, and its row is the table's last.
CAB_CLOSE = "no later phase is opened; no model is contacted. "
BOARD_STATUS_ANCHOR = CAB_CLOSE + CLOSED_BEFORE
BOARD_ROW_ANCHOR = ("every separate instrument stays unopened; no later phase opens; "
                    "no model contact.** |\n")
CAR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If accepted, "
             "effective only on publication and remote verification, at which "
             "point W8-D7 Landing B is complete.** It does not close W8 and "
             "contains no declaration of closure. No status is flipped by the "
             "implementer; acceptance is the human reviewer's dated act.")
CAR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective only on "
                "publication and remote verification, at which point W8-D7 "
                "Landing B is complete.** It does not close W8 and contains no "
                "declaration of closure.")
NEW_ENTRY = {
    "id": "W8-D7-CAR", "path": RECORD, "type": "phase-record",
    "title": "W8-D7 - Closure: Whole-Phase Closure Assessment",
    "role": (
        "The W8-D7 Landing B whole-phase closure assessment: the evidence "
        "record on which any closure decision must rest, containing no "
        "declaration of closure. Inventories derived from published repository "
        "sources at the W8-D7 opening: the deliverable inventory from the "
        "runway through W8-D6 with every phase-level correction, amendment, "
        "erratum and identity act; the runway obligation assessment with every "
        "obligation, non-goal, tripwire and quality gate in its own row; the "
        "seven ADR-0047 first-contact preconditions with precondition 3 "
        "reported outstanding in its lawful resting state and the W8-D6 "
        "decision carried as a decision that authorises nothing, its separate "
        "instruments unopened, named and not supplied; the proof and obligation "
        "succession audit, every proof-module change of W8 recomputed from "
        "history against its record's pins and ADR-0058's R9 chain whole; the "
        "public/private boundary audit decomposed as ADR-0052 decomposes P4, "
        "its mechanical clause reporting exactly and the human review owed; "
        "the evidence integrity audit proving every case home, register, "
        "revealed record and the W7 class byte-identical to their landings; the "
        "incident, correction and learning log from public source; and the "
        "inherited, unresolved and next-gate inventory, the fifteen inherited "
        "W7 rows item-for-item beside W8's own, each at its true standing - "
        "the W8-D5 finding undetermined as recorded, every recorded divergence "
        "undiagnosed, the retained records sealed, the two carried LF-checkout "
        "findings and the inert allowlist entries accounted from live bytes, "
        "the stale root README, registry rendering and concept overview named "
        "and not repaired. Every posture is proposed and adopted only by the "
        "human reviewer's acceptance. Carries the exact succession of the "
        "opening module's CA7 to a historical proof at the W8-D7 opening, the "
        "W8-D7 entry set and no-later-phase limb moving to this record's "
        "module, with proof obligations CB1 to CB9. Declares no closure, "
        "diagnoses nothing, reads no custody, opens no later phase, contacts no "
        "model and authorises no Landing C preparation."),
    "depends_on": ["W8-D7-CAB", "W8-AR", "W8-D6-CDR", "W8-D6-CDB", "W8-D5-AFR",
                   "ADR-0061", "W8-D5-EAB", "W8-D4-CPR", "W8-D4-VRC", "W8-D4-VSR",
                   "W8-D4-VCR", "ADR-0060", "W8-D4-IVB", "W8-D3-CCR", "W8-D3-HDR",
                   "W8-S1-SCR", "W8-S1-SOB", "ADR-0059", "ADR-0058", "ADR-0057",
                   "W8-D3-SCB", "W8-D2-CBC", "W8-D2-DIC", "W8-D2-MSA", "ADR-0055",
                   "W8-D2-DIB", "ADR-0054", "W8-D1-EDB", "ADR-0056", "W8-DER",
                   "W8-HPC", "W8-HAC", "W8-CHC", "ADR-0047", "ADR-0046",
                   "ADR-0052", "ADR-0051", "ADR-0033", "ADR-0034", "W7-CR",
                   "W7-D7-CAR", "W7-D7-CAB", "W6-D6-CAB", "W6-CR", "W7-D6-HDR"],
}


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


def _blob(raw):
    return subprocess.run(["git", "hash-object", "--stdin"], input=raw,
                          cwd=ROOT, capture_output=True,
                          check=True).stdout.decode().strip()


def _indent(text, n):
    return "\n".join(" " * n + line for line in text.split("\n"))


def folded(text):
    """The bounded fold of the presumption scan: marks removed, whitespace
    runs made one space, case folded."""
    return " ".join(FOLDED_MARKS.sub("", text).split()).casefold()


def verdict_forms(text):
    """The inventoried verdict words standing alone as bold postures, read
    after the bounded verdict fold: invisible code points removed, then
    inside each bold span the inline marks, spacing and trailing punctuation
    stripped and the case folded."""
    found = []
    for m in BOLD_SPAN.finditer(INVISIBLE.sub("", text)):
        inner = SPAN_MARKS.sub("", m.group(2)).strip(".:;,!?").casefold()
        if inner in VERDICT_WORDS:
            found.append(inner)
    return found


def prose_paragraphs(text):
    """Markdown's logical paragraphs: blocks parted by blank lines - empty or
    SPACE/TAB-only, as CommonMark defines a blank line - with every run of
    whitespace inside a block made one space. Locally owned; the same form
    the published review-law module gives its EL3."""
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


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def d7b_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the record, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", RECORD).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the record was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = d7b_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_car_historical_" + Path(rel).stem,
          "__file__": str(ROOT / rel)}
    exec(compile(_lf(read(rel)), str(ROOT / rel), "exec"), ns)
    return types.SimpleNamespace(**{k: v for k, v in ns.items()
                                    if not k.startswith("__")})


def helpers(read, *names):
    return types.SimpleNamespace(**{n: historical(read, HELPERS[n])
                                    for n in names})


def baseline_text(rel):
    return _lf(committed(BASELINE, rel)).decode("utf-8")


def nine_rules():
    m = re.search(r"^> (\*\*confidence ≠ authority.*?uncertainty ≠ "
                  r"failure\.\*\*)$", baseline_text(DOCTRINE), re.M)
    return m.group(1) if m else None


def contact_chain():
    """ADR-0047 decision 18's chain block, found by its closing link."""
    ends = [line[2:] for line in baseline_text(CONTACT_LAW).split("\n")
            if line.startswith("> **")
            and line.endswith("no contact ≠ nothing proven.**")]
    return ends[0] if len(ends) == 1 else None


def section_lines(text, heading):
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows) if l == heading]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(rows))
                if rows[j].startswith("## ")), len(rows))
    return rows[heads[0]:end]


def pipe_blocks(section):
    """The contiguous delimiter-bearing blocks of a section, each extended to
    the non-blank lines adjacent to it, in order. Nothing is filtered: every
    line that holds a delimiter belongs to exactly one returned block."""
    blocks, i = [], 0
    while i < len(section):
        if "|" in section[i]:
            start = i
            while start > 0 and section[start - 1].strip():
                start -= 1
            end = i
            while end < len(section) and section[end].strip():
                end += 1
            blocks.append(section[start:end])
            i = end
        else:
            i += 1
    return blocks


def closed_block(block, header, separator, width):
    """(rows, violations) for one block that must be exactly a header, a
    separator and body rows of `width` cells."""
    v = []
    if not block or block[0] != header:
        v.append("the header line is not exactly the law's")
    if len(block) < 2 or block[1] != separator:
        v.append("the separator line is malformed")
    rows = []
    for line in block[2:]:
        if not (line.startswith("| ") and line.endswith(" |")):
            v.append("a malformed row")
            continue
        cells = line[2:-2].split(" | ")
        if len(cells) != width:
            v.append("a row with %d cells" % len(cells))
            continue
        rows.append(cells)
    return rows, v


def section_blocks(text, heading, expected):
    """The blocks of a section against the expected (header, separator,
    width) list, in order: (rows per block, violations)."""
    section = section_lines(text, heading)
    if section is None:
        return [], ["the section %r is missing or repeated" % heading]
    blocks = pipe_blocks(section)
    if len(blocks) != len(expected):
        return [], ["the section holds %d table blocks, not %d"
                    % (len(blocks), len(expected))]
    out, v = [], []
    for block, (header, separator, width) in zip(blocks, expected):
        rows, problems = closed_block(block, header, separator, width)
        out.append(rows)
        v += problems
    return out, v


def first_bold(cell):
    m = re.match(r"\*\*([^*]+)\*\*", cell)
    return m.group(1) if m else None


def posture_cell_violations(rows, column, label, exception=None):
    v = []
    for cells in rows:
        cell = cells[column]
        if exception is not None and cell == exception:
            continue
        if first_bold(cell) not in POSTURES:
            v.append("%s: a posture cell outside the seven" % label)
    return v


def carriage_violations(text, h):
    """CB1: the load-bearing statements each once; the nine rules, the chain
    and the posture sentence once; the invariant exactly twice; every
    proposed-posture cell one of the seven; no closure-presuming phrase,
    verdict bold form, withdrawn formula, universal claim, contact statement,
    performance attestation or drafting target anywhere."""
    flat = _flat(text)
    v = ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
         for s in REQUIRED if flat.count(s) != 1]
    for name, block in (("nine-rule", nine_rules()),
                        ("contact-chain", contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    if flat.count(POSTURE_LINE) != 1:
        v.append("the posture sentence is not carried once")
    if text.count(INVARIANT) != 2 or text.count("> **%s**\n" % INVARIANT) != 1:
        v.append("the invariant is not carried exactly")
    rows, problems = h.rev.closed_table(text, DELIVERABLE_SECTION, DELIVERABLE_HEADER,
                                        DELIVERABLE_SEPARATOR, 7)
    v += problems + posture_cell_violations(rows, 6, "deliverables", D7_ROW_POSTURE)
    rows, problems = h.rev.closed_table(text, RUNWAY_SECTION, RUNWAY_HEADER,
                                        RUNWAY_SEPARATOR, 4)
    v += problems + posture_cell_violations(rows, 2, "runway")
    if [r[0] for r in rows] != ["%d" % n for n in range(1, RUNWAY_ROWS + 1)]:
        v.append("the runway rows are not numbered one to %d" % RUNWAY_ROWS)
    rows, problems = h.rev.closed_table(text, INVENTORY_SECTION, INVENTORY_HEADER,
                                        INVENTORY_SEPARATOR, 7)
    v += problems
    if [r[0] for r in rows] != ["%d" % n for n in range(1, INVENTORY_ROWS + 1)]:
        v.append("the inventory rows are not numbered one to %d" % INVENTORY_ROWS)
    if any(first_bold(r[3]) is None for r in rows):
        v.append("an inventory state cell does not open with its bold state")
    rows, problems = h.rev.closed_table(text, PRECONDITION_SECTION, PRECONDITION_HEADER,
                                        PRECONDITION_SEPARATOR, 4)
    v += problems
    if [r[0] for r in rows] != ["%d" % n for n in range(1, 8)]:
        v.append("the precondition rows are not exactly seven, numbered")
    if not rows or first_bold(rows[2][2]) != "outstanding in lawful resting state":
        v.append("precondition 3 is not reported outstanding in its lawful "
                 "resting state")
    low = folded(text)
    v += ["closure-presuming wording: %s" % p for p in PRESUMPTION if p in low]
    v += ["withdrawn mechanical-conformance formula: %s" % p
          for p in WITHDRAWN if p in low]
    v += ["universal session or reveal claim: %s" % p for p in UNIVERSAL if p in low]
    v += ["a statement whether contact occurred: %s" % p
          for p in CONTACT_STATEMENTS if p in low]
    v += ["an attestation of a performed act: %s" % p for p in ATTESTATIONS if p in low]
    if DRAFTING_OPENING in low:
        v.append("the brief's drafting target is carried")
    v += ["a verdict form as a bold posture: %s" % b for b in verdict_forms(text)]
    return v


def withholding_violations(text):
    """CB2: every non-authorisation phrase present, and section 16 exactly its
    authorised whole block."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["section 16 is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("section 16 is not exactly its authorised whole block")
    return v


def count_beside(tokens):
    """A number written beside a token or relation name, in either order,
    across up to eight non-alphanumeric characters. A textual guard only."""
    name = (r"(?<![A-Za-z0-9])(?:%s|agreements?|divergences?)(?![A-Za-z0-9])"
            % "|".join(re.escape(t) for t in sorted(tokens)))
    number = (r"(?<![A-Za-z0-9])(?:\d+|one|two|three|four|five|six|seven|"
              r"eight|nine|ten|eleven|twelve)(?![A-Za-z0-9])")
    gap = r"[^A-Za-z0-9\n]{0,8}"
    return re.compile("(?i)" + name + gap + number + "|" + number + gap + name)


def strip_refs(text):
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", "", text)
    text = re.sub(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", "", text)
    return SECTION_REF.sub("", text)


def exposure_violations(text, h, exempt=()):
    """CB3: over the text's logical prose paragraphs - no case identity, no
    digest outside the exempt exact lines (each surviving the paragraph form
    unchanged), no reserved authoring label, schema literal or method label,
    no number beside a token or relation name, and no derived-figure form.
    A textual guard only."""
    text = prose_paragraphs(text)
    v = []
    if h.rec.CASE_ID_ANYWHERE.search(text):
        v.append("a case identity is present")
    stripped = text
    for line in exempt:
        stripped = stripped.replace(line, "", 1)
    if re.search(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", stripped):
        v.append("an unpinned digest is present")
    v += ["a reserved label: %s" % s for s in h.cor.reserved_channel_hits(text)]
    schemas = ((h.pkt.PACKET_SCHEMA, h.cal.REGISTER_SCHEMA,
                h.env.AUTHORING_SCHEMA) + tuple(h.law.NEW_SCHEMAS))
    v += ["a schema literal is present" for s in schemas if s in text]
    v += ["a method label: %s" % m for m in sorted(h.law.ADMITS)
          if re.search(r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), text)]
    if count_beside(h.pkt.TOKENS).search(text):
        v.append("a count beside a token or relation")
    v += h.vr.figure_hits(strip_refs(text), h.pkt.TOKENS)
    return v


def batch(commit, paths):
    """{path: LF bytes} for many paths in one process."""
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
    """Every fixed home's tracked files at the baseline, and the path of
    every record registered at the baseline except the registry itself,
    which this landing lawfully changes."""
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
    homes = {h: sorted(p for p in base_tracked if p.startswith(h + "/"))
             for h in FIXED_HOMES}
    in_homes = {f for files in homes.values() for f in files}
    records = sorted({e["path"] for e in reg if e["path"] != REGISTRY}
                     - in_homes)
    return homes, records


def fixed_artefact_violations(now, tracked, homes, records, base):
    v = []
    for home, files in homes.items():
        if not files:
            v.append("a fixed home is empty at the baseline: %s" % home)
        if sorted(p for p in tracked if p.startswith(home + "/")) != files:
            v.append("a fixed home's file set changed: %s" % home)
    for p in [f for files in homes.values() for f in files] + records:
        if p in now and now[p] != base[p]:
            v.append("a fixed file changed")
    return v


def basis_rows():
    return [["%d" % n, "`%s`" % i, "`%s`" % p, "`%s`" % c, "`%s`" % b, "`%s`" % s]
            for n, i, p, c, b, s in BASIS_ROWS]


def basis_row_lines():
    return ["| " + " | ".join(r) + " |" for r in basis_rows()]


def file_rows():
    return [["%d" % n, "`%s`" % p, "`%s`" % c, "`%s`" % b, "`%s`" % s]
            for n, p, c, b, s in FILE_ROWS]


def file_row_lines():
    return ["| " + " | ".join(r) + " |" for r in file_rows()]


def trace_rows():
    return [[p, " · ".join("`%s`" % i for i in ids)] for p, ids in TRACE_ROWS]


def trace_row_lines():
    return ["| " + " | ".join(r) + " |" for r in trace_rows()]


def method_tables(text):
    """Section 1 read whole: its three table blocks are the identity
    provenance table, the trace table and the file-provenance table, in
    that order."""
    return section_blocks(text, BASIS_SECTION, (
        (BASIS_HEADER, BASIS_SEPARATOR, 6), (TRACE_HEADER, TRACE_SEPARATOR, 2),
        (FILES_HEADER, FILES_SEPARATOR, 5)))


def basis_table_violations(text, h):
    blocks, v = method_tables(text)
    if not blocks or blocks[0] != basis_rows():
        v.append("the provenance table is not exactly its trusted rows")
    return v


def trace_table_violations(text):
    blocks, v = method_tables(text)
    if len(blocks) < 2 or blocks[1] != trace_rows():
        v.append("the trace table is not exactly its trusted rows")
    return v


def files_table_violations(text):
    blocks, v = method_tables(text)
    if len(blocks) < 3 or blocks[2] != file_rows():
        v.append("the file-provenance table is not exactly its trusted rows")
    return v


def _resolvers(resolve, last, registered):
    if resolve is None:
        def resolve(commit, path):
            try:
                return (_git("rev-parse", "%s:%s" % (commit, path)).strip(),
                        _sha(committed(commit, path)))
            except subprocess.CalledProcessError:
                return (None, None)
    if last is None:
        def last(path):
            return _git("log", "-1", "--first-parent", "--format=%H", BASELINE,
                        "--", path).strip()
    if registered is None:
        reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
        registered = {e["id"]: e["path"] for e in reg}
    return resolve, last, registered


def basis_object_violations(rows=None, resolve=None, registered=None, last=None):
    """CB4: every provenance row resolves - the object at the cited commit
    and at the baseline, the raw digest, the cited commit the last
    first-parent change of the path - and its identity is registered at
    that path."""
    rows = BASIS_ROWS if rows is None else rows
    resolve, last, registered = _resolvers(resolve, last, registered)
    v = []
    if [r[0] for r in rows] != list(range(1, len(rows) + 1)):
        v.append("the rows are not numbered consecutively from one")
    for n, ident, path, commit, blob, sha in rows:
        got_blob, got_sha = resolve(commit, path)
        if got_blob != blob:
            v.append("row %d: the object at the cited commit differs" % n)
        if got_sha != sha:
            v.append("row %d: the committed bytes differ from the pin" % n)
        if resolve(BASELINE, path)[0] != blob:
            v.append("row %d: the object at the baseline differs" % n)
        if last(path) != commit:
            v.append("row %d: the cited commit is not the last first-parent "
                     "change" % n)
        if registered.get(ident) != path:
            v.append("row %d: the identity is not registered at that path" % n)
    return v


def file_object_violations(rows=None, resolve=None, last=None, registered=None):
    """CB4: every file-provenance row resolves the same way and names no
    registered path, which belongs in the identity table."""
    rows = FILE_ROWS if rows is None else rows
    resolve, last, registered = _resolvers(resolve, last, registered)
    v = []
    if [r[0] for r in rows] != list(range(1, len(rows) + 1)):
        v.append("the file rows are not numbered consecutively from one")
    if len({r[1] for r in rows}) != len(rows):
        v.append("a file path is listed twice")
    for n, path, commit, blob, sha in rows:
        got_blob, got_sha = resolve(commit, path)
        if got_blob != blob:
            v.append("file row %d: the object at the cited commit differs" % n)
        if got_sha != sha:
            v.append("file row %d: the committed bytes differ from the pin" % n)
        if resolve(BASELINE, path)[0] != blob:
            v.append("file row %d: the object at the baseline differs" % n)
        if last(path) != commit:
            v.append("file row %d: the cited commit is not the last "
                     "first-parent change" % n)
        if path in registered.values():
            v.append("file row %d: a registered path belongs in the identity "
                     "table" % n)
    return v


def trace_closure(entries):
    """The transitive closure of `depends_on` from the brief's pinned entry
    points and every W8 entry, over the registry entries given: (closure,
    unregistered identities met on the way)."""
    by_id = {e["id"]: e for e in entries}
    seen, unregistered = set(), []
    stack = list(PINNED_ENTRY_POINTS) + [e["id"] for e in entries
                                         if e["phase"] == "W8"]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        if x not in by_id:
            unregistered.append(x)
            continue
        stack += by_id[x].get("depends_on", [])
    return seen, unregistered


def trace_violations(rows=None, entries=None, tracked=None):
    """CB4: the trace rows are exactly the closure, grouped by phase in
    registry order, every traced identity registered with its path tracked
    at the baseline, and every read identity traced or named in EXTRA_READ."""
    rows = TRACE_ROWS if rows is None else rows
    if entries is None:
        entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
    if tracked is None:
        tracked = set(_git("ls-tree", "-r", "--name-only", BASELINE).split())
    by_id = {e["id"]: e for e in entries}
    order = {e["id"]: i for i, e in enumerate(entries)}
    closure, unregistered = trace_closure(entries)
    v = ["a traced identity is not registered: %s" % x for x in unregistered]
    listed = [i for _, ids in rows for i in ids]
    if len(listed) != len(set(listed)):
        v.append("a traced identity is listed twice")
    if set(listed) != closure:
        v.append("the trace is not exactly the closure of the governing "
                 "dependencies")
    for phase, ids in rows:
        if any(by_id.get(i, {}).get("phase") != phase for i in ids):
            v.append("a traced identity stands under the wrong phase")
        if list(ids) != sorted(ids, key=lambda i: order.get(i, -1)):
            v.append("a phase's traced identities are not in registry order")
    for i in listed:
        if i in by_id and by_id[i]["path"] not in tracked:
            v.append("a traced identity's path is not tracked at the "
                     "baseline: %s" % i)
    read = [r[1] for r in BASIS_ROWS]
    if [i for i in read if i not in closure] != list(EXTRA_READ):
        v.append("a read identity is neither traced nor named as read "
                 "outside the trace")
    if any(i in closure for i in EXTRA_READ):
        v.append("an identity named as read outside the trace is traced")
    return v


NAMED_PATH = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*"
                        r"\.(?:md|py|txt|json|yml|yaml|toml|cfg|ini))`")


def named_path_violations(text):
    """CB4: every repository path this record names in code marks, with one of
    NAMED_PATH's listed extensions, has a provenance row - the succession-audit
    rows, which pin their own historical objects, excepted - other than the
    two files this landing adds. A bounded syntactic check: a path in plain
    prose is outside it, and it decides neither whether a source was read
    nor whether it governs."""
    for line in audit_row_lines():
        text = text.replace(line, "", 1)
    known = ({r[2] for r in BASIS_ROWS} | {r[1] for r in FILE_ROWS}
             | {RECORD, SELF_REL})
    return sorted({"a named path without provenance: %s" % p
                   for p in NAMED_PATH.findall(text) if p not in known})


def first_parent_range():
    return _git("rev-list", "--reverse", "--first-parent",
                "%s..%s" % (W7_CLOSURE, BASELINE)).split()


def commit_bindings(commits, w8_paths):
    """For each W8 commit, from history: the W8 identities whose registered
    records it added - a landing may add more than one - or, when it added
    none, the leading label of its commit subject."""
    out = {}
    for c in commits:
        added = _git("diff-tree", "--no-commit-id", "--name-only", "-r",
                     "--diff-filter=A", c + "^", c).split()
        ids = sorted(w8_paths[p] for p in added if p in w8_paths)
        if ids:
            out[c[:7]] = ("added", tuple(ids))
        else:
            subject = _git("log", "-1", "--format=%s", c).strip()
            out[c[:7]] = ("subject", subject.split(":", 1)[0].strip())
    return out


def deliverable_table_violations(text, h, commits=None, entries=None,
                                 bindings=None):
    """CB4: the deliverable inventory read whole; its commit cells account
    for every first-parent W8 commit exactly once, each commit bound to its
    row by the registered W8 record it added, whose identity stands in that
    row, or, when it added none, by its subject's leading label, which is
    the row's act; and its identity cells for every W8 registry entry at
    the baseline exactly once, each identity's deliverable matching its row."""
    rows, v = h.rev.closed_table(text, DELIVERABLE_SECTION, DELIVERABLE_HEADER,
                                 DELIVERABLE_SEPARATOR, 7)
    commits = first_parent_range() if commits is None else commits
    if entries is None:
        entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
    w8 = {e["id"]: e for e in entries if e["phase"] == "W8"}
    if bindings is None:
        bindings = commit_bindings(commits, {e["path"]: i for i, e in w8.items()})
    seen_c, seen_i = [], []
    for cells in rows:
        shorts = re.findall(r"`([0-9a-f]{7})`", cells[4])
        idents = re.findall(r"`([A-Z0-9][A-Za-z0-9-]*)`", cells[5])
        seen_c += shorts
        seen_i += idents
        for ident in idents:
            e = w8.get(ident)
            if e is None:
                v.append("an identity not registered at phase W8: %s" % ident)
            elif e.get("deliverable") and e["deliverable"] != cells[0]:
                v.append("%s sits in the wrong deliverable's row" % ident)
        for short in shorts:
            kind, value = bindings.get(short, (None, None))
            if kind == "added" and not set(value) <= set(idents):
                v.append("%s stands in a row other than its added record's"
                         % short)
            elif kind == "subject" and value != cells[0]:
                v.append("%s, which added no registered record, is not bound "
                         "to its row by its subject" % short)
    if len(seen_c) != len(set(seen_c)):
        v.append("a commit appears in more than one row")
    if sorted(seen_c) != sorted(c[:7] for c in commits):
        v.append("the commits do not account for the W8 range exactly once")
    if len(seen_i) != len(set(seen_i)):
        v.append("an identity appears in more than one row")
    if set(seen_i) != set(w8):
        v.append("the identities do not account for the W8 entries exactly once")
    return v


def lf_sha_at(commit, rel):
    return _sha(_lf(committed(commit, rel)))


def succession_audit_violations(rows=None, sha_at=None, modifications=None):
    """CB5: every row recomputes from history - the pre-image at the
    landing's first parent, the post-image at the landing - and the rows
    cover every proof-module modification in the W8 range. Injectable for
    the controls."""
    rows = SUCCESSIONS if rows is None else rows
    sha_at = lf_sha_at if sha_at is None else sha_at
    if modifications is None:
        modifications = []
        for c in first_parent_range():
            out = _git("diff-tree", "--no-commit-id", "--name-status", "-r", c,
                       "--", "tests/")
            for line in out.splitlines():
                status, path = line.split("\t")
                if status == "M" and path.endswith(".py"):
                    modifications.append((c, path))
    v = []
    for commit, module, site, record, kind, pre, post, pinned in rows:
        try:
            parent = _git("rev-parse", commit + "^").strip()
        except subprocess.CalledProcessError:
            v.append("%s: no parent" % commit[:7])
            continue
        if sha_at(parent, module) != pre:
            v.append("%s %s: the pre-image differs" % (commit[:7], module))
        if sha_at(commit, module) != post:
            v.append("%s %s: the post-image differs" % (commit[:7], module))
    covered = {(c, m) for c, m, *_ in rows}
    if covered != set(modifications):
        v.append("the rows do not cover the proof-module changes exactly")
    return v


def audit_rows():
    return [["%d" % n, "`%s`" % c[:12], "`%s`" % m, s, "`%s`" % r, k, "`%s`" % pre,
             "`%s`" % post]
            for n, (c, m, s, r, k, pre, post, _) in enumerate(SUCCESSIONS, 1)]


def audit_row_lines():
    return ["| " + " | ".join(r) + " |" for r in audit_rows()]


def module_test_count(read, rel):
    """The test methods a module defines at the snapshot: functions named
    test_* in the body of a class, counted from the parsed source so that a
    quoted fragment carrying another module's text is never counted."""
    tree = ast.parse(_lf(read(rel)).decode("utf-8"))
    return sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef)
               for f in node.body
               if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))
               and f.name.startswith("test_"))


def audit_section_violations(text, read):
    """The four tables of section 5 read block by block: the P and Q tables
    well formed with their row counts and obligation names, the module table
    with each module present at the snapshot and its test count exact, and
    the succession-audit table exactly its trusted rows."""
    blocks, v = section_blocks(text, AUDIT_SECTION, (
        (OBLIGATION_HEADER, OBLIGATION_SEPARATOR, 3),
        (OBLIGATION_HEADER, OBLIGATION_SEPARATOR, 3),
        (MODULE_HEADER, MODULE_SEPARATOR, 4),
        (AUDIT_HEADER, AUDIT_SEPARATOR, 8)))
    if v:
        return v
    p, q, mods, audit = blocks
    if [r[0].split()[0] for r in p] != ["P1", "P2", "P3", "P4a", "P4b", "P5", "P6"]:
        v.append("the P table is not P1 to P6, with P4 decomposed")
    if [r[0].split()[0] for r in q] != ["Q%d" % n for n in range(1, 5)]:
        v.append("the Q table is not Q1 to Q4")
    for cells in mods:
        m = re.fullmatch(r"`(tests/[A-Za-z0-9_]+\.py)`", cells[0])
        if not m:
            v.append("a malformed module cell")
            continue
        try:
            n = module_test_count(read, m.group(1))
        except (subprocess.CalledProcessError, FileNotFoundError):
            v.append("a module absent at the snapshot: %s" % m.group(1))
            continue
        if cells[2] != "%d" % n:
            v.append("%s: the test count differs" % m.group(1))
    if audit != audit_rows():
        v.append("the succession-audit table is not exactly its trusted rows")
    return v


def homes_rows():
    return [["`%s`" % home, "`%s`" % c, "`%s`" % t, "%d" % n]
            for home, c, t, n in HOMES]


def homes_table_violations(text, h):
    rows, v = h.rev.closed_table(text, HOMES_SECTION, HOMES_HEADER,
                                 HOMES_SEPARATOR, 4)
    if rows != homes_rows():
        v.append("the homes table is not exactly its trusted rows")
    return v


def integrity_violations(commit, tree_at=None, count_at=None, sha_of=None,
                         entries=None, homes=None, pins=None):
    """CB9: each home's tree at the snapshot equals its pinned tree and its
    tree at its landing commit, with its stated file count; the W7 home
    equals its tree at the W7-D6 seal; the W7 pins hash exactly; every
    registry hash recomputes at the snapshot. Injectable for the controls."""
    homes = HOMES if homes is None else homes
    pins = W7_PINS if pins is None else pins

    def _tree(rev, home):
        try:
            return _git("rev-parse", "%s:%s" % (rev, home)).strip()
        except subprocess.CalledProcessError:
            return None
    tree_at = _tree if tree_at is None else tree_at
    if count_at is None:
        def count_at(rev, home):
            return len(_git("ls-tree", "-r", "--name-only", rev, "--", home).split())
    if sha_of is None:
        def sha_of(rel):
            return _sha(_lf(snapshot_bytes(commit, rel)))
    snap = "HEAD" if commit is None else commit
    v = []
    for home, landing, tree, n in homes:
        if tree_at(snap, home) != tree:
            v.append("%s: the tree at the snapshot differs" % home)
        if tree_at(landing, home) != tree:
            v.append("%s: the tree at its landing differs" % home)
        if count_at(snap, home) != n:
            v.append("%s: the file count differs" % home)
    w7 = dict((home, tree) for home, _, tree, _ in homes).get(
        "governance/generated-evaluation")
    if tree_at(W7_D6_SEAL, "governance/generated-evaluation") != w7:
        v.append("the W7 home differs from its tree at the W7-D6 seal")
    for rel, pin in pins:
        if sha_of(rel) != pin:
            v.append("a W7 instrument pin differs: %s" % rel)
    if entries is None:
        entries = json.loads(snapshot_bytes(commit, REGISTRY))["entries"]
    nulls = [e["id"] for e in entries if e["content_hash"] is None]
    if sorted(nulls) != ["REGISTRY-JSON", "REGISTRY-MD"]:
        v.append("the null-hash entries are not exactly the two exclusions")
    for e in entries:
        if e["content_hash"] is not None and sha_of(e["path"]) != e["content_hash"]:
            v.append("a registry hash does not recompute: %s" % e["id"])
    return v


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


def succession_violations(present, record, h, sites=None):
    """CB5's first limb: the CA7 succession is the exact reviewed
    transformation of the opening module's fixed pre-image, reversible, its
    sites CA7's alone, the pinned anchor the baseline, the succeeded module
    holding no live registry read."""
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
    if h.auth.labels(sites) != ("CA7",):
        v.append("the sites are not CA7's alone")
    if present.count(D7A_LINE) != 1 or D7A_LANDING != BASELINE:
        v.append("the succession's anchor is not this landing's baseline")
    if present.count(HISTORICAL_READ) != 1 or LIVE_READ in present:
        v.append("the succeeded CA7 does not read the D7-A landing commit alone")
    if pre.count(LIVE_READ) != 1 or HISTORICAL_READ in pre:
        v.append("the pre-image is not the live-gated module")
    return v + succession_table_violations(record, h)


def car_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CAR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CAR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         CAB_CLOSE + fill(CAR_STATUS[state]) + " " + CLOSED_AFTER[state]),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + CAR_ROW + fill(ROW_PREFIX[state]) + CAR_ROW_BODY
         + " |\n"),
    )


def new_entry(state, date, content_hash):
    return {
        "id": NEW_ENTRY["id"], "aliases": [], "title": NEW_ENTRY["title"],
        "type": NEW_ENTRY["type"], "phase": "W8", "deliverable": "W8-D7",
        "path": NEW_ENTRY["path"], "status": state,
        "accepted_date": date if state == "accepted" else None,
        "role": NEW_ENTRY["role"], "governs": [],
        "depends_on": list(NEW_ENTRY["depends_on"]), "resolves": [],
        "id_namespaces": [], "implementation_permission": "none",
        "open_decisions": [], "content_hash": content_hash,
        "hash_exclusion_reason": None, "errata": [],
    }


def expected_registry(base_text, record_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, record_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    sample = "2026-01-01"
    return " ".join([CAR_ROW, CAR_ROW_BODY, CLOSED_AFTER["draft"],
                     CLOSED_AFTER["accepted"], CAR_STATUS["draft"],
                     CAR_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, record_text, h, base_entries=None):
    """CB7: this record's entry binds its path, type, phase, deliverable,
    status, date and hash; the brief's entry is byte-unchanged from the
    baseline; the W8-D7 entries are exactly the brief's and this record's;
    no entry of a later phase exists."""
    v = []
    by_id = {x["id"]: x for x in entries}
    e = by_id.get("W8-D7-CAR")
    state, date = h.rec.header_state(record_text)
    if e is None:
        return ["no W8-D7-CAR entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            RECORD, "phase-record", "W8", "W8-D7"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(record_text.encode("utf-8")):
        v.append("the entry's hash differs from the record")
    if base_entries is None:
        base_entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
    base_cab = {x["id"]: x for x in base_entries}.get("W8-D7-CAB")
    if by_id.get("W8-D7-CAB") != base_cab or base_cab is None:
        v.append("the brief's entry is not byte-unchanged from the baseline")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D7"} != D7_ENTRIES:
        v.append("the W8-D7 entries are not exactly the brief's and this record's")
    if {x["phase"] for x in entries} - KNOWN_PHASES:
        v.append("an entry of a later phase exists")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


class LiveHelpersSabotaged:
    """A control context: every live helper these proofs could be tempted to
    call is replaced and the previous state restored on exit."""

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
class CB1_Carriage(unittest.TestCase):
    def test_cb1_record_carries_statements_postures_and_no_closure(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="statements, blocks, posture cells and no "
                               "presumption"):
            self.assertEqual(carriage_violations(text, h), [])
        rows, _ = h.rev.closed_table(text, RUNWAY_SECTION, RUNWAY_HEADER,
                                     RUNWAY_SEPARATOR, 4)
        first_runway = "| " + " | ".join(rows[0]) + " |"
        inv_rows, _ = h.rev.closed_table(text, INVENTORY_SECTION, INVENTORY_HEADER,
                                         INVENTORY_SEPARATOR, 7)
        first_inv = "| " + " | ".join(inv_rows[0]) + " |"
        for name, mutated in (
                ("a verdict posture in a runway row", text.replace(
                    first_runway, first_runway.replace("**satisfied**",
                                                       "**passed**", 1), 1)),
                ("an unlisted posture in a runway row", text.replace(
                    first_runway, first_runway.replace("**satisfied**",
                                                       "**complete**", 1), 1)),
                ("a dropped runway row", text.replace(first_runway + "\n", "", 1)),
                ("a dropped inventory row", text.replace(first_inv + "\n", "", 1)),
                ("precondition 3 shown discharged", text.replace(
                    "**outstanding in lawful resting state** — no deliverable",
                    "**discharged** — no deliverable", 1)),
                ("a closure-presuming sentence", text.replace(
                    "\n## 2.", "\nW8 is closed.\n\n## 2.", 1)),
                ("a closure-presuming sentence in bold", text
                 + "\nW8 **is complete**.\n"),
                ("a closure-presuming sentence in code marks", text
                 + "\nW8 `is complete`.\n"),
                ("a closure-presuming sentence with a zero-width space", text
                 + "\nW8 is​ complete.\n"),
                ("a closure-presuming sentence wrapped over a soft break", text
                 + "\nW8 is\ncomplete.\n"),
                ("a closure-presuming sentence in capitals", text
                 + "\nW8 IS COMPLETE.\n"),
                ("a later phase named", text + "\nW9 follows.\n"),
                ("the drafting target carried", text
                 + "\n> **W8 closes because the governance work assigned to the "
                 "phase is complete and publicly evidenced.**\n"),
                ("the drafting target carried in emphasis", text
                 + "\n*W8 closes because the governance work assigned to the "
                 "phase* is complete.\n"),
                ("the withdrawn mechanical-conformance formula", text
                 + "\nIts mechanical surface establishes that no real-person "
                 "evaluation channel exists.\n"),
                ("a universal reveal claim", text
                 + "\nEvery withheld record was revealed.\n"),
                ("a removed statement", text.replace(REQUIRED[0], "", 1)),
                ("a doubled statement", text + "\n" + REQUIRED[2] + "\n"),
                ("an altered nine-rule block", text.replace(
                    "uncertainty ≠ failure", "uncertainty = failure", 1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven.**", "no contact = nothing "
                    "proven.**", 1)),
                ("an expanded invariant", text.replace(
                    "> **" + INVARIANT + "**", "> **" + INVARIANT[:-1]
                    + ", described elsewhere.**", 1)),
                ("the withdrawn contact clause restored", text.replace(
                    "set as the instrument's design intention; no maturity",
                    "set as the instrument's design intention, with no model "
                    "contacted; no maturity", 1)),
                ("a statement that contact occurred", text
                 + "\nA model was contacted during W8.\n"),
                ("a statement that contact did not occur, in bold", text
                 + "\n**No model has been contacted.**\n"),
                ("the withdrawn performance summary restored", text.replace(
                    "P2 and a fresh P4b act are standing human duties stated at "
                    "every W8 landing",
                    "P2 and P4b are recorded as fresh human acts at every W8 "
                    "landing", 1)),
                ("a performance attestation in code marks", text
                 + "\nP4b was `recorded as performed` at each landing.\n"),
                ("an eighth posture in the posture sentence", text.replace(
                    "· **unopened, named and not supplied**. No verdict",
                    "· **unopened, named and not supplied** · **passed**. No "
                    "verdict", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h))
        for name, added in (("a phrase outside the inventory",
                             "\nW8 is nearly finished.\n"),
                            ("a reveal claim bounded to its session corpus",
                             "\nEvery withheld record of the session corpus "
                             "was revealed.\n"),
                            ("the audit's own limit sentence",
                             "\nNo mechanical result establishes that any "
                             "family is clear.\n"),
                            ("a negation of a presuming phrase",
                             "\nW8 is not closed by this record.\n"),
                            ("a verdict word in plain prose",
                             "\nNo pass or fail is declared here.\n"),
                            ("a different bold word", "\n**passage**\n"),
                            ("a bold phrase that merely contains a verdict word",
                             "\n**no verdict word such as pass is used**\n"),
                            ("the lawful contact account",
                             "\nNo W8 act prepared, authorised or performed model "
                             "contact; this record does not state that no model "
                             "was contacted in W8.\n"),
                            ("a duty stated and not attested",
                             "\nA fresh P4b human act is owed at every W8 landing; "
                             "its discharge is held as each record's acceptance.\n")):
            with self.subTest(positive="%s is not what the inventories refuse"
                                       % name):
                self.assertEqual(
                    [x for x in carriage_violations(text + added, h)
                     if x.startswith(("closure-presuming wording",
                                      "withdrawn mechanical-conformance",
                                      "universal session or reveal",
                                      "a statement whether contact",
                                      "an attestation of a performed",
                                      "a verdict form"))], [])
        with self.subTest(fact="the fold is the bounded fold: marks, "
                               "whitespace and case"):
            self.assertEqual(folded("W8 **is**\n  _com​plete_."),
                             "w8 is complete.")
        for name, route in (
                ("a zero-width space inside the bold", "\n**pa\u200bss**\n"),
                ("code marks inside the bold", "\n**`pass`**\n"),
                ("underscore bold", "\n__passed__\n"),
                ("spacing, capitals and punctuation", "\n** Fail. **\n"),
                ("bold italics", "\n***safe***\n"),
                ("a soft break inside the bold", "\n**ap\nproved**\n"),
                ("a soft hyphen inside the bold", "\n**ma\u00adture**\n")):
            with self.subTest(control="a verdict posture with %s is refused by "
                                      "the verdict inventory" % name):
                self.assertTrue([x for x in carriage_violations(text + route, h)
                                 if x.startswith("a verdict form")])
        with self.subTest(fact="the verdict fold: invisible code points, marks, "
                               "spacing, punctuation and case inside the bold"):
            self.assertEqual(verdict_forms("**pa\u200bss**, **`Fail.`**, ** valid **,"
                                           " __grade__ and **passage**"),
                             ["pass", "fail", "valid", "grade"])
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(carriage_violations(text, hh), [])
                self.assertTrue(carriage_violations(
                    text.replace(first_runway + "\n", "", 1), hh))


class CB2_NonAuthorisations(unittest.TestCase):
    def test_cb2_record_carries_its_non_authorisations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="every non-authorisation carried"):
            self.assertEqual(withholding_violations(text), [])
        for s in WITHHELD[:3]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, "")))
        grouped = NON_AUTH_LINES[9] + "\n"
        pair = NON_AUTH_LINES[6] + "\n" + NON_AUTH_LINES[7] + "\n"
        tail = NON_AUTH_LINES[16] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this section.\n"
        for name, mutated in (
                ("the grouped-count non-authorisation dropped", text.replace(
                    grouped + NON_AUTH_LINES[10], NON_AUTH_LINES[10], 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[7] + "\n" + NON_AUTH_LINES[6] + "\n", 1)),
                ("an eighteenth non-authorisation", text.replace(
                    grouped + NON_AUTH_LINES[10],
                    grouped + "    - any sentinel line;\n" + NON_AUTH_LINES[10],
                    1)),
                ("the Landing C line dropped", text.replace(
                    NON_AUTH_LINES[16] + "\n", "", 1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[16] + "\n" + neutral
                              + "\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[16] + "\n    This landing "
                              "authorises the closure.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a line between the heading and the introducing item",
                 text.replace(NON_AUTH_SECTION + "\n\n" + NON_AUTH_INTRO
                              + "\n", NON_AUTH_SECTION + "\n\n" + neutral
                              + NON_AUTH_INTRO + "\n", 1)),
                ("a line after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a non-breaking-space line as the blank separator",
                 text.replace(tail, NON_AUTH_LINES[16] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated))


class CB3_NoExposure(unittest.TestCase):
    def test_cb3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr", "auth")
        text = read(RECORD).decode("utf-8")
        exempt = ((succession_row_line(h),) + tuple(basis_row_lines()) + tuple(file_row_lines())
                  + tuple(audit_row_lines()))
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D7-CAR"]["role"] + " " + by_id["W8-D7-CAR"]["title"]
        for name, surface, ex in (("record", text, exempt),
                                  ("registry role and title", role, ()),
                                  ("board wording this landing adds",
                                   added_board_wording(), ())):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(exposure_violations(surface, h, ex), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertIsNone(h.rec.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([m for m in sorted(h.law.ADMITS) if re.search(
                r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), src)], [])
            for token in h.pkt.TOKENS:
                self.assertNotIn(token, src)
        tok = sorted(h.pkt.TOKENS)[0]
        for name, plant in {
                "a case identity": "W8-C-" + "d" * 64,
                "an unpinned digest": "e" * 64,
                "a reserved label": sorted(h.cor.RESERVED_FIELDS)[0],
                "a schema literal": h.env.AUTHORING_SCHEMA,
                "a method label": sorted(h.law.ADMITS)[0],
                "a count beside a token": "5 " + tok,
                "a count beside a relation": "agreement: 11",
                "a decimal rate": "an agreement rate of 0.5",
                "a percentage": "50%"}.items():
            with self.subTest(control="a planted %s is detected" % name):
                self.assertTrue(exposure_violations(text + "\n" + plant + "\n",
                                                    h, exempt))
        with self.subTest(control="a provenance row with an altered digest is "
                                  "not exempt"):
            line = basis_row_lines()[0]
            altered = line.replace("sha256:f", "sha256:0", 1)
            self.assertNotEqual(altered, line)
            self.assertTrue(exposure_violations(
                text.replace(line, altered, 1), h, exempt))
        for name, route in {
                "a figure word, a soft line break, its value": "\nscore\n5\n",
                "a token, a soft line break, a count": "\n%s\n5\n" % tok,
                "a relation name, a soft line break, a count":
                    "\nagreements\n11\n"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(exposure_violations(text + route, h, exempt))
        with self.subTest(fact="every exempt row survives the paragraph form"):
            folded_text = prose_paragraphs(text)
            for line in exempt:
                self.assertEqual(folded_text.count(line), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr", "auth")
                self.assertEqual(exposure_violations(text, hh, exempt), [])
                self.assertTrue(exposure_violations(text + "\n0.5\n", hh,
                                                    exempt))


class CB4_FixedArtefactsAndBasis(unittest.TestCase):
    def test_cb4_every_home_and_record_unchanged_and_provenance_resolving(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        tracked = snapshot_tracked(commit)
        homes, records = fixed_paths()
        every = [f for files in homes.values() for f in files] + records
        base = batch(BASELINE, every)
        now = batch(commit, every)
        with self.subTest(fact="fixed homes and every registered record "
                               "byte-identical to the baseline"):
            self.assertEqual(len(base), len(every))
            self.assertEqual(set(now), set(every))
            self.assertEqual(fixed_artefact_violations(
                now, tracked, homes, records, base), [])
        with self.subTest(fact="the registered records cover the brief, the "
                               "decision, the finding and the W7 closure"):
            for p in (BRIEF, "docs/phases/W8-D6-contact-decision-record.md",
                      "docs/phases/W8-D5-adequacy-finding-record.md",
                      "docs/phases/W7-closure-record.md"):
                self.assertIn(p, records)
            self.assertNotIn(REGISTRY, records)
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="the provenance table read whole is the "
                               "trusted rows, each resolving and registered"):
            self.assertEqual(basis_table_violations(text, h), [])
            self.assertEqual(basis_object_violations(), [])
            idents = [r[1] for r in BASIS_ROWS]
            self.assertEqual(len(set(idents)), len(idents))
            reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
            self.assertTrue({e["id"] for e in reg if e["phase"] == "W8"}
                            <= set(idents))
        with self.subTest(fact="the deliverable inventory accounts for every "
                               "W8 commit and every W8 entry exactly once, each "
                               "commit bound to its row from history"):
            self.assertEqual(deliverable_table_violations(text, h), [])
        with self.subTest(fact="the trace is exactly the registry's closure from "
                               "the entry points and the W8 entries, each "
                               "identity registered and tracked"):
            self.assertEqual(trace_table_violations(text), [])
            self.assertEqual(trace_violations(), [])
        with self.subTest(fact="every unregistered file read has its resolving "
                               "row and every code-marked path named has provenance"):
            self.assertEqual(files_table_violations(text), [])
            self.assertEqual(file_object_violations(), [])
            self.assertEqual(named_path_violations(text), [])
        reveal_file = homes["governance/validation-reveal"][0]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed brief": (
                    dict(now, **{BRIEF: now[BRIEF] + b" "}), tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))
        line = basis_row_lines()[0]
        for name, mutated in (
                ("a dropped provenance row", text.replace(line + "\n", "", 1)),
                ("a duplicated provenance row", text.replace(
                    line + "\n", line + "\n" + line + "\n", 1)),
                ("an altered commit", text.replace(
                    line, line.replace(BASIS_ROWS[0][3], "0" * 40, 1), 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(basis_table_violations(mutated, h))
        good = BASIS_ROWS[0]
        for name, rows in (("a wrong object", ((good[0], good[1], good[2],
                                                 good[3], "0" * 40, good[5]),)),
                           ("a wrong digest", ((good[0], good[1], good[2],
                                                 good[3], good[4],
                                                 "sha256:" + "0" * 64),)),
                           ("an identity not registered at the path",
                            ((good[0], "W8-D7-SNT") + good[2:],)),
                           ("a gap in the numbering", (good, BASIS_ROWS[2]))):
            with self.subTest(object_control="%s is refused" % name):
                self.assertTrue(basis_object_violations(rows))
        d_rows, _ = h.rev.closed_table(text, DELIVERABLE_SECTION, DELIVERABLE_HEADER,
                                       DELIVERABLE_SEPARATOR, 7)
        row0 = "| " + " | ".join(d_rows[0]) + " |"
        row1 = "| " + " | ".join(d_rows[1]) + " |"
        for name, mutated in (
                ("a commit dropped from the inventory", text.replace(
                    row1, row1.replace("`26a0662` · ", "", 1), 1)),
                ("a commit listed twice", text.replace(
                    row0, row0.replace("`117a192`", "`117a192` · `26a0662`", 1), 1)),
                ("an identity dropped", text.replace(
                    row1, row1.replace("`W8-D1-EDB` · `ADR-0054`",
                                       "`ADR-0054`", 1), 1)),
                ("an identity in the wrong row", text.replace(
                    row0, row0.replace("| `W8-AR` |", "| `W8-AR` · `ADR-0054` |", 1), 1))):
            with self.subTest(inventory_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(deliverable_table_violations(mutated, h))
        fline = file_row_lines()[0]
        for name, mutated in (
                ("a dropped file-provenance row", text.replace(fline + "\n", "", 1)),
                ("an altered file commit", text.replace(
                    fline, fline.replace(FILE_ROWS[0][2], "0" * 40, 1), 1))):
            with self.subTest(file_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(files_table_violations(mutated))
        with self.subTest(file_control="a file read but dropped from its table is "
                                       "refused as a named path without provenance"):
            self.assertTrue([x for x in named_path_violations(
                text.replace(fline + "\n", "", 1)) if FILE_ROWS[0][1] in x]
                or files_table_violations(text.replace(fline + "\n", "", 1)))
        with self.subTest(file_control="a repository file named without a row is "
                                       "refused"):
            self.assertTrue(named_path_violations(
                text + "\nSee `tests/test_w6_review_surface.py`.\n"))
        fgood = FILE_ROWS[0]
        for name, rows in (
                ("a wrong file object", ((fgood[0], fgood[1], fgood[2], "0" * 40,
                                          fgood[4]),)),
                ("a cited commit that is not the last change",
                 ((fgood[0], fgood[1], BASELINE, fgood[3], fgood[4]),)),
                ("a registered path in the file table",
                 ((fgood[0], BRIEF) + fgood[2:],))):
            with self.subTest(file_control="%s is refused" % name):
                self.assertTrue(file_object_violations(rows))
        with self.subTest(object_control="a provenance commit that is not the "
                                         "last change is refused"):
            self.assertTrue(basis_object_violations(
                ((good[0], good[1], good[2], BASELINE, good[4], good[5]),)))
        tline = trace_row_lines()[-1]
        first_w8 = TRACE_ROWS[-1][1][0]
        for name, mutated in (
                ("a traced identity dropped", text.replace(
                    tline, tline.replace("`%s` · " % first_w8, "", 1), 1)),
                ("an identity added to the trace", text.replace(
                    tline, tline.replace("`%s`" % first_w8,
                                         "`W8-D7-SNT` · `%s`" % first_w8, 1), 1))):
            with self.subTest(trace_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(trace_table_violations(mutated))
        dropped = tuple((p, tuple(i for i in ids if i != first_w8))
                        for p, ids in TRACE_ROWS)
        added = tuple((p, ids + ("W8-D7-SNT",)) if p == "W8" else (p, ids)
                      for p, ids in TRACE_ROWS)
        for name, rows in (("a trace missing a dependency", dropped),
                           ("a trace with an unregistered identity", added)):
            with self.subTest(trace_control="%s is refused" % name):
                self.assertTrue(trace_violations(rows))
        d5 = "| " + " | ".join(d_rows[7]) + " |"
        d6 = "| " + " | ".join(d_rows[8]) + " |"
        der = "| " + " | ".join(d_rows[6]) + " |"
        adr = "| " + " | ".join(d_rows[3]) + " |"
        d2 = "| " + " | ".join(d_rows[2]) + " |"
        self.assertEqual((d_rows[7][0], d_rows[8][0], d_rows[6][0], d_rows[3][0],
                          d_rows[2][0]), ("W8-D5", "W8-D6", "W8-DER", "ADR-0056",
                                          "W8-D2"))
        c5, c6 = d_rows[7][4], d_rows[8][4]
        for name, mutated in (
                ("the W8-D5 and W8-D6 commit cells exchanged, membership kept",
                 text.replace(d5, d5.replace(c5, c6, 1), 1)
                 .replace(d6, d6.replace(c6, c5, 1), 1)),
                ("one commit moved to another deliverable's row, membership kept",
                 text.replace(der, der.replace("`6704649`", "`c8e13d4`", 1), 1)
                 .replace(d5, d5.replace("`c8e13d4`", "`6704649`", 1), 1)),
                ("a subject-bound commit moved to another row, membership kept",
                 text.replace(adr, adr.replace(" · `571ac00`", "", 1), 1)
                 .replace(d2, d2.replace("`f8430cc`", "`571ac00` · `f8430cc`", 1),
                          1))):
            with self.subTest(binding_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                found = deliverable_table_violations(mutated, h)
                self.assertTrue([x for x in found if "bound" in x or
                                 "other than its added" in x], found)
        with self.subTest(fact="the bindings come from history: additions of "
                               "registered records, else the subject label"):
            reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
            w8p = {e["path"]: e["id"] for e in reg if e["phase"] == "W8"}
            b = commit_bindings(first_parent_range(), w8p)
            self.assertEqual(len(b), len(first_parent_range()))
            self.assertEqual(b["1d4b19c"], ("subject", "ADR-0056"))
            self.assertEqual(b["571ac00"], ("subject", "ADR-0056"))
            self.assertEqual(b["756d3d3"], ("added", ("W8-D2-CM-01", "W8-D2-DIC")))
            self.assertEqual(sum(1 for k, v in b.items() if v[0] == "subject"), 2)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(basis_table_violations(text, hh), [])


class CB5_Successions(unittest.TestCase):
    def test_cb5_ca7_succession_exact_and_every_w8_change_recomputed(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "rec")
        record = read(RECORD).decode("utf-8")
        present = read(OPENING).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[OPENING][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + OPENING)
                             .strip(), PREIMAGE[OPENING][2])
        with self.subTest(exact_succession=PREIMAGE[OPENING][0]):
            self.assertEqual(succession_violations(present, record, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[OPENING][1])
        with self.subTest(fact="R9's sentence, constants and tuple unchanged; "
                               "the session-recovery module untouched"):
            self.assertEqual(h.rec.R9_REVEAL, R9_SENTENCE)
            self.assertEqual(h.rec.LATER, ("W8-D4", "W8-D5", "W8-D6", "W8-D7"))
            self.assertEqual(_sha(read(RECOVERY)), _sha(committed(BASELINE, RECOVERY)))
        with self.subTest(fact="the opening module's W8-D7 claim holds at the "
                               "D7-A landing commit"):
            at = json.loads(committed(D7A_LANDING, REGISTRY))["entries"]
            self.assertEqual({e["id"] for e in at if e["deliverable"] == "W8-D7"},
                             {"W8-D7-CAB"})
            self.assertEqual({e["phase"] for e in at} - KNOWN_PHASES, set())
        with self.subTest(fact="every proof-module change in W8 recomputes "
                               "from history and is covered"):
            self.assertEqual(succession_audit_violations(), [])
            self.assertEqual(audit_section_violations(record, read), [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[OPENING][1:]),
                "the live read restored beside the historical one": (
                    present.replace(SITES[OPENING][2][2],
                                    SITES[OPENING][2][2]
                                    + SITES[OPENING][2][1], 1), None),
                "the anchor collapsed onto the W8-D6 completion": (
                    present.replace(D7A_LINE, 'D7A_LANDING = "%s"\n'
                                    % D6_COMPLETION, 1), None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[OPENING] + (("CA7", first,
                                       first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                if table is None:
                    self.assertNotEqual(text, present)
                self.assertTrue(succession_violations(text, record, h, table))
        row = succession_row_line(h)
        for name, mutated in (
                ("a space-prefixed duplicate row", record.replace(
                    row + "\n", row + "\n " + row + "\n", 1)),
                ("a row with no opening pipe", record.replace(row, row[2:], 1)),
                ("delimiter-free material touching the bottom",
                 record.replace(row + "\n", row + "\nmechanics sentinel\n", 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(succession_table_violations(mutated, h))
        good = SUCCESSIONS[5]
        wrong_pre = good[:5] + ("sha256:" + "0" * 64,) + good[6:]
        for name, kwargs in (
                ("a wrong pre-image", dict(rows=SUCCESSIONS[:5] + (wrong_pre,)
                                           + SUCCESSIONS[6:])),
                ("a dropped row", dict(rows=SUCCESSIONS[1:])),
                ("a resolver returning the pins verbatim is not what is "
                 "trusted", dict(sha_at=lambda c, m: "sha256:" + "0" * 64))):
            with self.subTest(audit_control="%s is refused" % name):
                self.assertTrue(succession_audit_violations(**kwargs))
        aud = audit_row_lines()[0]
        for name, mutated in (
                ("an audit row dropped", record.replace(aud + "\n", "", 1)),
                ("an audit digest altered", record.replace(
                    aud, aud[:-6] + "0000" + aud[-2:], 1)),
                ("a module test count altered", record.replace(
                    "| `tests/test_w8_closure_opening.py` | CA1 to CA8 | 9 |",
                    "| `tests/test_w8_closure_opening.py` | CA1 to CA8 | 8 |", 1)),
                ("a fifth table in the audit section", record.replace(
                    "\n21. **R9's chain", "\n| a | b |\n|---|---|\n| c | d |\n\n"
                    "21. **R9's chain", 1))):
            with self.subTest(audit_table_control="%s is refused" % name):
                self.assertNotEqual(mutated, record)
                self.assertTrue(audit_section_violations(mutated, read))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "rec")
                self.assertEqual(succession_violations(present, record, hh), [])


class CB6_RegistryAndBoard(unittest.TestCase):
    def test_cb6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = car_state(read(RECORD).decode("utf-8"), h)
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
                               "once, the closing sentence as this state "
                               "leaves it", state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED_AFTER[state]), 1)
        record_hash = _sha(read(RECORD))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, record_hash,
                                                    state, date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, record_hash, other, "2000-01-01"))
            wrong, _ = h.auth.apply_sites(
                board_pre, board_sites(other, "2000-01-01", board_pre))
            self.assertNotEqual(board, wrong)
        with self.subTest(control="the R9 sentence removed from the board is "
                                  "refused"):
            self.assertNotEqual(board.replace(R9_SENTENCE + " ", "", 1)
                                .count(R9_SENTENCE), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))


class CB7_EntrySet(unittest.TestCase):
    def test_cb7_registered_and_the_w8_d7_entry_set_is_the_briefs_and_this_records(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        record = read(RECORD).decode("utf-8")
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, record, h), [])
        with self.subTest(fact="at the baseline the W8-D7 entries were the "
                               "brief's alone"):
            self.assertEqual([e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] == "W8-D7"], ["W8-D7-CAB"])
        # Succeeded at the closure landing (W8-CR): the W8-D7 entry set and
        # the no-later-phase limb stay proven at this landing's own published
        # commit, D7B_LANDING; the live gates live in the closure record's
        # proof module until a later accepted act lawfully succeeds them.
        at_landing = json.loads(committed(D7B_LANDING, REGISTRY))["entries"]
        with self.subTest(fact="the W8-D7 entries were the brief's and this "
                               "record's, and no later phase's entry existed, "
                               "at this landing's published commit"):
            self.assertEqual(commit, D7B_LANDING)
            self.assertEqual(entry_violations(at_landing, record, h), [])
        base = at_snapshot[-1]
        for name, entries in {
                "a premature third W8-D7 entry": at_snapshot + [dict(
                    base, id="W8-D7-SNT", deliverable="W8-D7")],
                "a wrong record hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                        if e["id"] == "W8-D7-CAR" else e
                                        for e in at_snapshot],
                "a wrong deliverable": [dict(e, deliverable="W8-D6")
                                        if e["id"] == "W8-D7-CAR" else e
                                        for e in at_snapshot],
                "the brief's entry altered": [dict(e, status="draft")
                                              if e["id"] == "W8-D7-CAB" else e
                                              for e in at_snapshot],
                "a later phase's entry": at_snapshot + [dict(
                    base, id="W9-D1-SNT", phase="W9",
                    deliverable="W9-D1")]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, record, h))


class CB8_Census(unittest.TestCase):
    def test_cb8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the opening module change "
                               "among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, OPENING})
        flat = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?)\. No case", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RUNWAY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


class CB9_EvidenceIntegrity(unittest.TestCase):
    def test_cb9_homes_w7_class_and_registry_hashes_identical(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="every home at its landing tree, the W7 home at "
                               "its seal, the W7 pins exact, every registry "
                               "hash recomputing"):
            self.assertEqual(integrity_violations(commit), [])
            self.assertEqual(homes_table_violations(text, h), [])
        with self.subTest(fact="the homes cover the three case homes, the two "
                               "register homes, the two reveal homes and the "
                               "W7 home"):
            names = [home for home, *_ in HOMES]
            for home in FIXED_HOMES:
                self.assertIn(home, names)
        good = HOMES[0]
        for name, kwargs in (
                ("a home's tree altered", dict(homes=(
                    (good[0], good[1], "0" * 40, good[3]),) + HOMES[1:])),
                ("a home's file count altered", dict(homes=(
                    (good[0], good[1], good[2], good[3] + 1),) + HOMES[1:])),
                ("a W7 pin altered", dict(pins=(
                    (W7_PINS[0][0], "sha256:" + "0" * 64),) + W7_PINS[1:])),
                ("a registry hash that does not recompute", dict(entries=[
                    dict(e, content_hash="sha256:" + "0" * 64)
                    if e["id"] == "W8-D7-CAB" else e
                    for e in json.loads(read(REGISTRY))["entries"]])),
                ("a third null hash", dict(entries=[
                    dict(e, content_hash=None) if e["id"] == "W8-D7-CAB" else e
                    for e in json.loads(read(REGISTRY))["entries"]])),
                ("a resolver returning the pins verbatim is not what is "
                 "trusted", dict(tree_at=lambda rev, home: "0" * 40))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(integrity_violations(commit, **kwargs))
        line = "| " + " | ".join(homes_rows()[0]) + " |"
        for name, mutated in (
                ("a dropped home row", text.replace(line + "\n", "", 1)),
                ("an altered home tree", text.replace(
                    line, line.replace(HOMES[0][2], "0" * 40, 1), 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(homes_table_violations(mutated, h))


if __name__ == "__main__":
    unittest.main()
