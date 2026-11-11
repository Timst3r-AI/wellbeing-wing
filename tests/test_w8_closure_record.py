"""W8-D7-C — W8 closure record proofs (W8-CR, CC1–CC9).

Landing C of W8-D7: the W8 closure record, drafted from the published and
independently verified closure assessment and the live public repository
state, declaring W8 complete and closed only on its own acceptance,
publication and independent remote verification. This module proves the
record's carriage - its load-bearing statements, the nine rules, the chain
and the invariant; that its closure is declared only in its status line,
its proposed sentence and its inventoried conditioned sentences, each once
and each conditioned sentence carrying its own effectiveness or acceptance
condition, and that no inventoried closure form appears outside them; that its proposed closure sentence is exactly the
brief's drafting target, once; that its precondition table and inventory
rows one to twenty-nine are byte-identical to the published assessment's and
row thirty exactly its fixed closure-time row; that its runway posture tally
is the count the published assessment's table yields; and the absence of
inventoried conclusions about the instrument, any model or adoption, of
verdict forms as postures, of the withdrawn mechanical-conformance formula,
of any universal session or reveal claim, of any inventoried statement
whether model contact occurred and of any inventoried attestation that a
human act was performed; its non-authorisations; its exposure limits, with
the provenance rows, the file rows and this landing's one succession row as
the only digest exemptions; that every fixed home and every registered
record at the baseline is byte-unchanged and that the three provenance
tables resolve, every registered identity and every repository path of a
listed extension the record names in code marks and every law it cites in
any written form provenanced, the two laws marked read directly being the
two this module executes and each relied-on law's row the published
assessment's own row, object for object; the exact CB7
succession of the closure assessment module and the historical claims of
the succeeded modules at their commits; the exact registry and board; the
W8-D7 entry set and the no-later-phase limb; the census; and the
evidence-integrity identities - each with planted-mutant or negative
controls. Closed validators compare against trusted expected values held
here and refuse unrecognised material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the record
afterwards - and executes the helpers it relies on from that snapshot's
bytes, in a private namespace. CC7's W8-D7 entry set and its no-later-phase
limb were this module's present-state gates, moved here from the assessment
module's CB7 at this landing, until the W9 runway's landing (W9-AR)
succeeded them to a historical proof at this landing's own published
commit. The residual live reach is disclosed exactly: each snapshot-executed
helper module imports, at its own top level, the live modules it aliases for
the fixed-law values it reads from them, and no more independence than that
is claimed.

CC1's inventories read the whole record through a bounded fold - emphasis
and code marks and the invisible code points removed, every whitespace run
one space, case folded - so that ordinary formatting hides no inventoried
phrase; the status line, the proposed sentence and the inventoried
conditioned sentences are set aside once each before the closure forms are
sought, and nothing else is, and each inventoried conditioned sentence must
itself carry one of the inventoried condition phrases. Conformance to a bounded
inventory is never proof that arbitrary prose draws no conclusion. CC3 reads
every surface as logical prose paragraphs - blocks parted by blank lines,
empty or SPACE/TAB-only as CommonMark defines them, with every whitespace
run inside a block made one space - so that a soft line break, continuation
indentation or a separator line of no-break spaces, em spaces or form feeds
hides no figure or count from it; the exempt exact rows survive the
paragraph form unchanged.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity, schema
literal or method label as a literal, and no disposition token. It declares
no closure: the record's status line declares it, and only the human
reviewer's acceptance makes that line effective.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that W8 may close, or that any closure sentence is
accepted; any closure posture; that any inventory is complete; anything
about the instrument's maturity, adequacy, readiness, safety or usefulness;
anything about any model, case, disposition, divergence or reviewer; that
any model was or was not contacted; that any ADR-0047 precondition moved;
or that any later phase may open.
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

# ------------------------------------------------------------ fixed anchors
# The derived public baseline: the W8-D7 Landing B seal, the published and
# remotely verified closure assessment W8-D7-CAR.
BASELINE = "6ee0127e91f755d39b7fdc5af08bb1bcf1b16437"
# Succeeded at the W9 runway's landing (W9-AR; W8-CR section 12, item 35,
# and section 14, items 40 and 41): CC7's W8-D7 entry set and its
# no-later-phase limb stay proven at this landing's own published commit;
# this module holds no executable live registry read.
D7C_LANDING = "c6de8a99f09d60164def9f330f72437b2812c370"
D7B_LANDING = "6ee0127e91f755d39b7fdc5af08bb1bcf1b16437"
D7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"
D6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"
D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"
D5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"
D3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"
W7_CLOSURE = "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3"
W7_D6_SEAL = "a32579361f19556520e188cb8220b23d95323a4c"

RECORD = "docs/phases/W8-closure-record.md"
SELF_REL = "tests/test_w8_closure_record.py"
ASSESSMENT = "tests/test_w8_closure_assessment.py"
ASSESSMENT_RECORD = "docs/phases/W8-D7-B-closure-assessment-record.md"
OPENING = "tests/test_w8_closure_opening.py"
BRIEF = "docs/phases/W8-D7-A-closure-authorisation-brief.md"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({RECORD, SELF_REL, ASSESSMENT, REGISTRY, BOARD})
D7_ENTRIES = frozenset({"W8-D7-CAB", "W8-D7-CAR", "W8-CR"})
D7_ENTRIES_AT_BASELINE = frozenset({"W8-D7-CAB", "W8-D7-CAR"})
D7_ENTRIES_AT_OPENING = frozenset({"W8-D7-CAB"})
# The phases the registry may hold: no later phase is opened, designed or
# named as assigned by any W8-D7 landing, this one included.
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
    ASSESSMENT: ("closure assessment module", "sha256:5f504f2abc944eb6a9a24cec5780f14a0cb19df46a00bb95a89bd36d887e74b6", "928809e6d1dfb02992dedb4af3567099f4339112"),
    REGISTRY: ("registry", "sha256:d29a9072c3d4e0f0c46c9ae20177c4ede5ebc317a3e3916d3f03a0d8cdfdb625", "54388bcfd298e92bdc7427c55f89609842599b79"),
    BOARD: ("board", "sha256:32dda534bf3ff479dfff9ed1301b98be8eb5e966a551e80671fd335d4707b631", "37e05f296442ccf12d5e369de698a830a7ad06d9"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {ASSESSMENT: ("sha256:0f79a0ce3f8aa8764ac789454761dd473e315784ab2bdb21830b7d87f9f653df", "719baa4fc3736350c69b86ed344fdd0dd590462a")}

# ------------------------------- the one succession: the assessment module's CB7
SITES = {
    ASSESSMENT: (
        ('CB7',
         "bytes, in a private namespace. CB7's W8-D7 entry set and its no-later-phase\nlimb are this module's present-state gates, moved here from the opening\nmodule's CA7 at this landing, until the closure record's landing succeeds\nthem. The residual live reach is disclosed exactly: each snapshot-executed\n",
         "bytes, in a private namespace. CB7's W8-D7 entry set and its no-later-phase\nlimb were this module's present-state gates, moved here from the opening\nmodule's CA7 at this landing, until the closure record's landing (W8-CR)\nsucceeded them to a historical proof at this landing's own published\ncommit. The residual live reach is disclosed exactly: each snapshot-executed\n"),
        ('CB7',
         'D7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"\nD6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"\n',
         'D7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"\n# Succeeded at the W8 closure landing (W8-CR; W8-D7-CAB section 15, item\n# 60; W8-D7-CAR section 11, item 46): CB7\'s W8-D7 entry set and its\n# no-later-phase limb stay proven at this landing\'s own published commit;\n# the live gates move to the closure record\'s proof module.\nD7B_LANDING = "6ee0127e91f755d39b7fdc5af08bb1bcf1b16437"\nD6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"\n'),
        ('CB7',
         '        # The present-state gates of this module, moved here from the\n        # opening module\'s CA7, until the closure record\'s landing\n        # succeeds them to a historical proof at this landing\'s commit.\n        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]\n        with self.subTest(fact="the W8-D7 entries are the brief\'s and this "\n                               "record\'s, and no later phase\'s entry exists"):\n            self.assertEqual(entry_violations(live, record, h), [])\n',
         '        # Succeeded at the closure landing (W8-CR): the W8-D7 entry set and\n        # the no-later-phase limb stay proven at this landing\'s own published\n        # commit, D7B_LANDING; the live gates live in the closure record\'s\n        # proof module until a later accepted act lawfully succeeds them.\n        at_landing = json.loads(committed(D7B_LANDING, REGISTRY))["entries"]\n        with self.subTest(fact="the W8-D7 entries were the brief\'s and this "\n                               "record\'s, and no later phase\'s entry existed, "\n                               "at this landing\'s published commit"):\n            self.assertEqual(commit, D7B_LANDING)\n            self.assertEqual(entry_violations(at_landing, record, h), [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_LINE = 'R9_REVEAL = "%s"\n' % R9_SENTENCE
LATER_LINE = 'LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")\n'
D7B_LINE = 'D7B_LANDING = "%s"\n' % D7B_LANDING
HISTORICAL_READ = 'json.loads(committed(D7B_LANDING, REGISTRY))["entries"]'
# The executable live registry read of the pre-image's CB7, and the phrase
# the succeeded module keeps only inside the two string literals by which it
# proves the opening module's own succession.
LIVE_READ_LINE = ('        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))'
                  '["entries"]\n')
LIVE_PHRASE = "(ROOT / REGISTRY).read_bytes()"
LIVE_LITERAL = "LIVE_READ = '%s'\n" % LIVE_PHRASE

# ------------------------------------------------------------- the sources
# Trusted rows of the record's section 1 identity table: (number, identity,
# path, commit at which the path's published bytes last changed on the
# first-parent line to the baseline, blob at the baseline, raw SHA-256 of
# the committed bytes).
BASIS_SECTION = "## 1. Method and sources"
BASIS_HEADER = "| # | Identity | Published path | Commit | Object | Raw SHA-256 |"
BASIS_SEPARATOR = "|---|---|---|---|---|---|"
BASIS_ROWS = (
    (1, 'REGISTRY-JSON', 'governance/registry.json',
     '6ee0127e91f755d39b7fdc5af08bb1bcf1b16437', '54388bcfd298e92bdc7427c55f89609842599b79',
     'sha256:d29a9072c3d4e0f0c46c9ae20177c4ede5ebc317a3e3916d3f03a0d8cdfdb625'),
    (2, 'REGISTRY-MD', 'docs/governance/registry.md',
     'a3dce11c8e1b8785160c443ad9ed8d47c4df98ee', '7c8eb0ed4ca54329a5a3141c9b279f1950dd9326',
     'sha256:0c0b63cbd54ec6b30fc37076ba4919ba20ffa8409e67d600e473a3e6007f02df'),
    (3, 'W6-D6-CAB', 'docs/phases/W6-D6-A-closure-authorisation-brief.md',
     '8a764e92a04b8fbcabb2b2fba1eb0b7f3646c3da', '535d2443ab1f613691022a7f6590c14c27619fd0',
     'sha256:2e4098691c6fe45772855e49d74464ac8e45dab6fedb4779319178d2a30da57f'),
    (4, 'W6-CR', 'docs/phases/W6-closure-record.md',
     '508ea5729d05ae838b15761d4d56ecc65bc61f91', '9f3d15847f210421f0ff38845d9391f61059659b',
     'sha256:a720fb1970235965c3a978410c9adc0176ab2d2f5152c056d2197ff6b11eb80e'),
    (5, 'W7-D2-E', 'docs/phases/W7-D2-E-proof-completion-record.md',
     '59dfcb685b84de56499a57b1ff91402ed4d864b7', 'fe20be6e7c630063a2be045208703facc2267e33',
     'sha256:a75cdb36e61edaf33452f349e10163d691551c47314787fbf6e82063dea791b8'),
    (6, 'W7-D4-SHR', 'docs/phases/W7-D4-synthetic-harness-binding-record.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', '2bc7288be8a4312d4adf56ef9b2f2cc63ba89c5d',
     'sha256:0ed7151f4f845f463a52f423809694b96d47d0e78cf5e9843a32a3688a136bf1'),
    (7, 'W7-D6-HDR', 'docs/phases/W7-D6-human-review-disposition-record.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'fc3746b06b8529d085814cef45747f16c9cce0ed',
     'sha256:8bd96c1f22c9664e4c891ad3827a6c818fd1ac82f2e62df1990a977e5216fea8'),
    (8, 'W7-D7-CAR', 'docs/phases/W7-D7-B-closure-assessment-record.md',
     '03ca823b5accfc5616b2e22ff642066882fe5274', '318a3bc5b8d79e666e4829b3068e9e7fbbf717d3',
     'sha256:8c2a5412b44b594bd2133321f47fcc0a2c209082e5877091a486dd5cdb21860c'),
    (9, 'W7-CR', 'docs/phases/W7-closure-record.md',
     '7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3', 'f57ea174237205f2d4e0783f48469ab84abe5c97',
     'sha256:8086966f2355c59d2c8ea34593d177446cac0ec9707977b27d186b7e0d96200a'),
    (10, 'W8-AR', 'docs/phases/W8-runway-generative-evaluation-maturity.md',
     '117a192091bfafa80cb3f6ae567b63204b6c7676', 'da34be5dee7db4a94b4276f4024dd48e3076883a',
     'sha256:fda68f9d1e69c166587cfb746d7d1830b39ea99d9c4c6a9129a0b75d34eba24e'),
    (11, 'W8-D2-MSA', 'docs/phases/W8-D2-manifest-shape-amendment.md',
     'df406d4030a8c6ae6cf273a0cf18097a49c66f0c', 'a83489f989645935d8414f172afa8d8ac1a1a238',
     'sha256:2a7ea0f53bc75b9ee45afd148732f7b5a2f05ccbe3b13518d99e9084c2ccf388'),
    (12, 'W8-D2-DIC', 'docs/phases/W8-D2-discriminating-instrument-record.md',
     '756d3d3512202a905a5d3b689d75bf06ae31ccf5', 'a2a2b876f2e389857431df873945a58e2992b08c',
     'sha256:62df368528b973a590e300267bab89a634894d8e3fe4604815082d99137af93c'),
    (13, 'W8-D2-CBC', 'docs/phases/W8-D2-committed-blob-proof-correction.md',
     'a4997128055462bb4791cfa5c5d06c3a3f51b0ba', 'bc3cba96a1c366879420a3e97724221c348d1885',
     'sha256:f1d18113a61c9fbf27e9705a613881485fa6fa801f977327bb6db56588a1173c'),
    (14, 'W8-D3-SCB', 'docs/phases/W8-D3-synthetic-calibration-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'b8617c4d1712b940ff5200bba7dd3519afc93096',
     'sha256:11cf050e4c0d820868d9dd1f4e852d23f79c509e833ec565dd98ef354b6521dd'),
    (15, 'W8-S1-SOB', 'docs/phases/W8-S1-supplementary-opening-brief.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'bf0e33a85bf63f088cb23efd5d30df1fda05249d',
     'sha256:408f4df23a0452dd42ca9615785858f5a31905ef007dc9a130ba72f5b1b1f97a'),
    (16, 'W8-S1-SCR', 'docs/phases/W8-S1-supplementary-corpus-record.md',
     '83253039ec274a2496b37b618949fd00d3cd7c8e', '3c59d0de1a816071260a772f63f1889f4237a112',
     'sha256:562bd94979a07b213575493e7f8159f6868065bbaa87b06ad0d5a9dd69eadfa6'),
    (17, 'W8-HPC', 'docs/phases/W8-historical-pin-proof-correction.md',
     '9ded8c44abfd4c911d938814a7f551944998ec53', 'ccb94754798e7432d0e3090773f1c9cffda50a5b',
     'sha256:14746269c7af18556b6ee92d6aeb6c760b4835749beb8f0314afb041e4d650b9'),
    (18, 'W8-D3-HDR', 'docs/phases/W8-D3-human-disposition-record.md',
     '66b6e6ca7e33e5e0fd326d61653a0c13d1679878', '6b832dc72bfaf26145a310aa3397e2545cfc88f8',
     'sha256:f438b825e18b6a0e625bfd8079b02d1350594f46e65aa307f4bddb12f2fddd3e'),
    (19, 'W8-HAC', 'docs/phases/W8-historical-absence-proof-correction.md',
     '317c0ba9de76853d454774085cdf18f3a638c02f', 'c4700ca800242a133308f43ac26d9a579b3eca15',
     'sha256:a061bab8660d1c3c01e7003b05f89fe92d931b04d76c8d8f9b7aa0d33dab6cd9'),
    (20, 'W8-D3-CCR', 'docs/phases/W8-D3-calibration-completion-record.md',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'ae3c662051ea716eee43076b10034868cbb1da8b',
     'sha256:b6e958ba42c59b5c45774eb5bbc66e5a1f8a8f19100f1b580c218e2509addf82'),
    (21, 'W8-D4-VCR', 'docs/phases/W8-D4-validation-corpus-record.md',
     'f638cca75ec4a192685bf5cd53f29451cfdbbdd9', '9e5f71153ed4e66c1d1c1e0cdc3f1011d7df431d',
     'sha256:80ca992d602e83cd4d1c83fd86d8f05dca344d0ac7e1407ea3c6014e845287eb'),
    (22, 'W8-CHC', 'docs/phases/W8-case-home-scope-correction.md',
     'a08ba584bea8e2576dd7450c6374a4ff4f0aa149', '5690aac90ff4e5a11c068ab55c0881c0dbbe1293',
     'sha256:1c416856a69d81a7d8f719b946787b98a98f25f76e1db5fec51ee0f346901925'),
    (23, 'W8-D4-VSR', 'docs/phases/W8-D4-validation-session-record.md',
     '44947adf9b60f2ce462be97a2c0e628a3ecbdd89', 'b0064ca82b218691fab18909450b7a4f4c3a8edc',
     'sha256:c5a35c6fd29dd11bed3b2fa706ffb4d056f159441cb0881897c61e677a383cae'),
    (24, 'W8-D4-VRC', 'docs/phases/W8-D4-validation-record.md',
     '67ed076503f1087cefed31dd163a706a87d3b8a6', '0cadf57bbb6869323318e9cdd5cb474f59583189',
     'sha256:55e680c31b3983be8b52bb2750dcb7f27fa812f4deb83439d50cf7358d5e327b'),
    (25, 'W8-D4-CPR', 'docs/phases/W8-D4-completion-record.md',
     'ce78a242df25898d90debee9513bdce7e511471b', '14e49308ed63a4411400f769f25fda8095d74efb',
     'sha256:dd8a577de367946f5a7f5331a06a6a8df49fbe1b899dd6e6db2d527e62618471'),
    (26, 'W8-DER', 'docs/phases/W8-documentation-erratum.md',
     '6704649ed80c27112c00c14093c82645e8d090cf', '371f80be2d1abca01b0ff7fa0da9065c2c63e1bc',
     'sha256:0eec519ea3d1d369bfd3f8231d09c8f09a24dde9749fa59480f900d5da45fd07'),
    (27, 'W8-D5-EAB', 'docs/phases/W8-D5-evidence-adequacy-brief.md',
     'c8e13d47f305e0378609ffec1d31f890f629239d', '78a78b2179740e769ef42bd2ed5944cb04fd71b8',
     'sha256:339c93d624f56f07165aa81696fb2f464cfec1fef2148ceace2b4222b8efe60a'),
    (28, 'W8-D5-AFR', 'docs/phases/W8-D5-adequacy-finding-record.md',
     '2aa2c75d20363ca7e54095f49b328bdd4db1350a', '9fbd1016bb58ae06d9e557ebd281f707f54b8fc5',
     'sha256:197254b69161aacef79dbb93c86939c4cc1b82e9cc39ac2fa0584207ea6cc558'),
    (29, 'W8-D6-CDB', 'docs/phases/W8-D6-contact-decision-brief.md',
     '753e6abea8d67a16332799af615fdcfa4aefa7b9', 'ddde7b3553b5f21dc929010c5c90dba701a70980',
     'sha256:034483363a210df7a736749d5f30e6cf68a6e57c77b7b07001f3770f8567a196'),
    (30, 'W8-D6-CDR', 'docs/phases/W8-D6-contact-decision-record.md',
     'e76be12b537f67a1041422ee73c22cbbfcf8b8c5', '842472148111e78abd9d7fc7273fa1b19426dc75',
     'sha256:c7381ac0bbfeac59b94057b9de359fdd072cc2003e1f06179e833492be71bfa3'),
    (31, 'W8-D7-CAB', 'docs/phases/W8-D7-A-closure-authorisation-brief.md',
     'cf2012669b97b323cdbfb182bc10865d444c79c1', '50ee207397b4c772e8a479004f507f46ed821026',
     'sha256:28011515753cb45c66a3ef0dd8999bd6b7758f352b01bf03ebc1ea5ed824246f'),
    (32, 'W8-D7-CAR', 'docs/phases/W8-D7-B-closure-assessment-record.md',
     '6ee0127e91f755d39b7fdc5af08bb1bcf1b16437', '0357f56a2ce78d7fd8188b470a65a83b42aa3910',
     'sha256:dcc8e0492bef579564ac753099f52378f3c4286947bdb5bfb53ee8ece5336f62'),
)
FILES_HEADER = "| # | Published path | Commit | Object | Raw SHA-256 |"
FILES_SEPARATOR = "|---|---|---|---|---|"
FILE_ROWS = (
    (1, 'README.md',
     '6704649ed80c27112c00c14093c82645e8d090cf', '0845e4a0b06126bafb094918a899c24e255a0e93',
     'sha256:32c9bd765ad3942dc2312f5d6bcac12f2fe642a98956ec13d0e801cf92310931'),
    (2, 'docs/phases/README.md',
     '6ee0127e91f755d39b7fdc5af08bb1bcf1b16437', '37e05f296442ccf12d5e369de698a830a7ad06d9',
     'sha256:32dda534bf3ff479dfff9ed1301b98be8eb5e966a551e80671fd335d4707b631'),
    (3, 'docs/wellbeing-wing-concept-overview.md',
     '571ac0076590c6b3346f53ef828bc0c1ad2f9cad', '0c88c7b71e687ed00f5775a9c14c763f856e4a3f',
     'sha256:a07f55b97bf90c8d11fc17796b3866b6cfe236ee972bb5b271fe4dda579acf32'),
    (4, 'scripts/scan-allowlist.txt',
     'a3dce11c8e1b8785160c443ad9ed8d47c4df98ee', 'a5984cb8b781cfabc4032d166e651c69606513b2',
     'sha256:72a1c836bee59d310dd453e96085a9543b04bc23746dd4ba7f1db718655586f6'),
    (5, 'tests/test_pending_ledger.py',
     '8465c538a76f628c86f097eea3942b993147a548', '86eeb87cd9e3733a5aa177c5c8b3642ec5a06884',
     'sha256:78c681b9fd49c76a3bd66304f1098b9fafa1b29414741c080839bedf15a4dd76'),
    (6, 'tests/test_w8_closure_assessment.py',
     '6ee0127e91f755d39b7fdc5af08bb1bcf1b16437', '928809e6d1dfb02992dedb4af3567099f4339112',
     'sha256:5f504f2abc944eb6a9a24cec5780f14a0cb19df46a00bb95a89bd36d887e74b6'),
)
LAWS_HEADER = "| # | Law | Published path | Commit | Object | Raw SHA-256 | Route |"
LAWS_SEPARATOR = "|---|---|---|---|---|---|---|"
# The laws the record cites by identity: (number, identity, path, commit,
# object, digest, route, the published assessment's source-table row).
LAW_ROWS = (
    (1, 'ADR-0033', 'docs/decisions/0033-model-access.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', 'aefac956a771819d9116c22fc2dd49084efb97e8',
     'sha256:1ce7c980b3e45342e5fe485d053d9f4ef3ab887015914158a5146345a076ceba', 'via', 58),
    (2, 'ADR-0046', 'docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', '14c1208e81fb59763a1f78ee3676276149b75b08',
     'sha256:b2bac9e3bbf3fd3cd3991c174671f2dbbbde3832363ef3df93cb67cde3de5270', 'via', 51),
    (3, 'ADR-0047', 'docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md',
     '02b58ccc9f37f46a72b79b9e61e6028057d313b7', '5f1fb5581a98ea8d9f03d97ad39a4bc39158c079',
     'sha256:63f8c84fe2a3235d69340e4bcbcb4cd1d2497ff46b89876ac128b097f6c72a35', 'direct', 52),
    (4, 'ADR-0050', 'docs/decisions/0050-finding-is-an-event-and-finding-disposition-mechanism.md',
     '6c8a0e6c35eb58beb190bc50793ecf55948ec6d1', 'ec158f01e1e9486db7d45a483a674cdf7d5eb655',
     'sha256:8244509cb6578b92ff0dfc024d51cdeaf7bb11fca983df71424ad348e29276f0', 'via', 57),
    (5, 'ADR-0051', 'docs/decisions/0051-model-boundary-no-public-contact.md',
     'e1dd86d561e458babdcfa56e6923aba9fb6f63b2', '2800a8260fc4379133fce418ea3e20fe5929e607',
     'sha256:a1af46b27a52fed4a1bb0f30c9b449148ba8178ddffddbcc76a1acbb634efda6', 'via', 54),
    (6, 'ADR-0052', 'docs/decisions/0052-exclusion-list-conformance-p4-decomposition.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', 'e3d917edbf7b0cca131bbd5e0a5884e696bb0246',
     'sha256:46299e137b86a91bf76e964017a103e03da5b3d71830b86390d369e7b1327050', 'via', 55),
    (7, 'ADR-0054', 'docs/decisions/0054-generative-evaluation-maturity-doctrine.md',
     '6e9e0f155944bea3117b82a5b4216ce6c50abaa4', '77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43',
     'sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd', 'direct', 3),
    (8, 'ADR-0055', 'docs/decisions/0055-w8-case-shape-evidence-separation-blinding-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', '9e08d3141796df3318de82dfd1d93baef235f11f',
     'sha256:fc967a9c4c4a799dfcd593e05ae5d2db881d47e0a0bf0de6a6fb74fa11dd284b', 'via', 5),
    (9, 'ADR-0056', 'docs/decisions/0056-public-repository-identity-attribution-boundary.md',
     '797e839ac9484a04ac84e1f7bb5f84851f539579', '891e737e32960bae4fc48d6852bf935ffdb33d85',
     'sha256:ed0f3ab7e5828c2c7be408b2712a491f68d635bb80efc42e2328d83792a3084d', 'via', 9),
    (10, 'ADR-0057', 'docs/decisions/0057-w8-disposition-reveal-calibration-law.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', '873fd0c22ba93fb45b321e57513145e0c34d074e',
     'sha256:4222454a1c68ea3b6056b9d8f5e6e720cf2f1f36f967dd8d9154259802f8e358', 'via', 12),
    (11, 'ADR-0058', 'docs/decisions/0058-w8-d3-session-recovery-law.md',
     '897f0b14a66ee956bd9fe36e63975b04d5dc9663', '5f8f0786b1bd8091696fe45cb05a388bb776b8b6',
     'sha256:6291da0206c576be10c6c5eea8a1e71490f836e20430663a8eb5038f49877cd3', 'via', 13),
    (12, 'ADR-0059', 'docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'd06e2f56a25ee80abd678bfe706721ba7df8e70d',
     'sha256:05dc46e0b9b17d96f316aa5dcb545c5ba7e99031cdc169277d6ee12abcf06b59', 'via', 14),
    (13, 'ADR-0060', 'docs/decisions/0060-w8-instrument-validation-law.md',
     '054f1270b8206a059636e18e012223ddfe52d5ea', 'f6955c079ec323a9dd5e6d20854c9b226e59b79a',
     'sha256:f4440effdab671b49572d14cf8ef14c7d2b1b711e33361cf4ddd59c7c855aae8', 'via', 24),
    (14, 'ADR-0061', 'docs/decisions/0061-w8-evidence-adequacy-review-law.md',
     '18d6230b5f7281577c18892dd7b95e9448f310c2', 'aec015d014c098b183deeb119a6c6293f4e4b6bb',
     'sha256:b81af71545cfc21d3311275110e66dc0768d87d24f1954138e95783773cf95d9', 'via', 35),
)
# The two laws this module executes from their committed bytes - the
# doctrine's nine-rule block and the contact law's chain - and so the two
# the record may mark as read directly.
DIRECT_LAWS = {"ADR-0054": DOCTRINE, "ADR-0047": CONTACT_LAW}
# The published assessment's section holding its registered-source table.
ASSESSMENT_SOURCE_SECTION = "## 1. Method and evidence law"

# ------------------------------------------- the tables carried from the assessment
ASSESSMENT_PRECONDITION_SECTION = "## 4. Contact-boundary accounting"
PRECONDITION_SECTION = "## 5. The preconditions, and the sentence this phase does not say"
PRECONDITION_HEADER = "| # | Precondition | Closure-time state | Source evidence |"
PRECONDITION_SEPARATOR = "|---|---|---|---|"
ASSESSMENT_INVENTORY_SECTION = "## 9. Inherited, unresolved and next-gate inventory"
INVENTORY_SECTION = "## 9. The inherited, unresolved and next-gate inventory at closure"
INVENTORY_HEADER = ("| # | Item | Source | Current state | Did W8 change it? | Smallest "
                    "lawful future gate, where the source names one | What W8-D7 is "
                    "forbidden to imply |")
INVENTORY_SEPARATOR = "|---|---|---|---|---|---|---|"
INVENTORY_ROWS = 30
CARRIED_ROWS = 29
# The one row this record restates: the assessment's row thirty described its
# own programme's remaining landings; this landing is that programme's last.
ROW_30 = ["30", "The W8-D7 closure programme's remaining landings",
          "`W8-D7-CAB` §4; `W8-D7-CAR` §9 row thirty",
          "**Landing C is this record**: the W8 closure record, its proof module, the "
          "succession of the assessment module's W8-D7 entry gate, the registry and the "
          "board, effective only on this record's own acceptance, publication and "
          "independent remote verification",
          "this record is Landing C; the programme ends with it",
          "none — the programme's last landing is this record, and no later landing exists",
          "that any closure sentence is accepted before the human reviewer's acceptance of "
          "this exact record, or that closure authorises anything beyond closure"]
ASSESSMENT_RUNWAY_SECTION = "## 3. Runway obligation assessment"
RUNWAY_HEADER = "| # | Runway obligation | Proposed posture | Source evidence |"
RUNWAY_SEPARATOR = "|---|---|---|---|"
RUNWAY_ROWS = 68
# The posture tally the record states, in words, against the count the
# published assessment's table yields.
TALLY = (("satisfied", 61, "**sixty-one satisfied; four satisfied with named carried item**"),
         ("satisfied with named carried item", 4, "**and three external / outside repository authority**"),
         ("external / outside repository authority", 3, "**None uses an unresolved, deferred or unopened posture, and none is satisfied by weakening a record.**"))
LIMB_SECTION = "## 2. Closure statement"
LIMB_HEADER = "| Limb | Evidence in `W8-D7-CAR` |"
LIMB_SEPARATOR = "|---|---|"
LIMB_ROWS = 12
SUCCESSION_SECTION = "## 14. Proof successions at this landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
OBLIGATIONS_SECTION = "## 15. Proof obligations for this landing"
OBLIGATIONS_HEADER = "| # | Obligation | Decidability |"
OBLIGATIONS_SEPARATOR = "|---|---|---|"
ASSESSMENT_SECTIONS = 16
ASSESSMENT_ITEMS = 57
BRIEF_SECTIONS = 23
BRIEF_ITEMS = 79
SECTION_REF = re.compile(r"§\d+(?:\.\d+)*")

# ------------------------------------------------------- the record's carriage
POSTURES = ("satisfied", "satisfied with named carried item",
            "outstanding in lawful resting state",
            "unresolved and bounded under named doctrine",
            "deferred under named doctrine",
            "external / outside repository authority",
            "unopened, named and not supplied")
POSTURE_LINE = (
    "**Only the seven accepted closure postures are used,** each as the human "
    "reviewer's acceptance of `W8-D7-CAR` adopted it: **satisfied** · **satisfied "
    "with named carried item** · **outstanding in lawful resting state** · "
    "**unresolved and bounded under named doctrine** · **deferred under named "
    "doctrine** · **external / outside repository authority** · **unopened, named "
    "and not supplied**. No verdict vocabulary is introduced as closure shorthand.")
INVARIANT = ("Any real-person adoption is a separate governed authority outside this "
             "repository.")
REQUIRED = (
    "A derivative board row is never evidence for the source it describes.",
    "No item moves from an open posture to a closed one because the phase is "
    "closing.",
    "A proof being green is evidence only for the property the proof actually "
    "tests.",
    "Every registered identity this record names in code marks has a row:",
    "Unqualified section and item references inside the carried cells of "
    "sections 5 and 9 keep their scope in the published `W8-D7-CAR`, and a "
    "reference that names another record keeps its stated scope.",
    "Every law binds in full whichever route it took:",
    "The closure sentence this record carries is proposed by the implementer from "
    "the published evidence, for the human reviewer's use, revision or rejection",
    "W8 completed its governed programme without concluding the instrument's "
    "maturity, readiness, safety or usefulness.",
    "The contact sentence this record carries is the one the published record "
    "supports, and no other",
    "this record does not state that no model was contacted in W8, which the "
    "record does not support in that form, and it does not state the contrary.",
    "The reported authority gap stays reported.",
    "This is the standing non-diagnosis condition, and it survives closure.",
    "W8-D7 rewrote no history to make closure simpler.",
    "P4a and P4b are carried separately, always",
    "P4a green is no evidence for P4b, in any degree.",
    "Neither result implies the other, and the fresh act establishes semantic "
    "conformance to the public prohibition set only.",
    "W8 resolved none of rows one to fifteen by existing",
    "their repair decisions remain unmade, and this record presumes neither.",
    "It means the phase's own governance obligations are discharged or honestly "
    "carried at their named standing — and nothing more.",
    "Closure authorises nothing beyond closure.",
    "This record creates no later-phase artefact and no later-phase authority.",
    "No future phase is assigned an obligation merely because this closure wanted "
    "somewhere to put it.",
    "Silence is never a decision, and a green suite is never an acceptance.",
    "ADR-0058's R9 does not move",
    "Every CC row proves mechanics and carriage only.",
    "Every unfinished matter leaves this phase named, classified, and represented "
    "as resolved nowhere.",
    "nothing in it is declared until the human reviewer's acceptance makes its "
    "status line effective.",
)
# A bounded fold: emphasis and code marks and the invisible code points
# removed, whitespace runs made one space, case folded.
FOLDED_MARKS = re.compile("[*_`~​‌‍⁠﻿­]")
BLANK_LINE = re.compile(r"^[ \t]*$")
# The closure forms this record may use only inside its inventoried
# conditioned sentences (W8-D7-CAB items 2 and 25): read after the fold.
CLOSURE_FORMS = ("w8 is closed", "w8 is complete", "w8 closes because",
                 "w8 closes complete", "complete and closed", "w8-d7 is complete",
                 "w8-d7 is satisfied", "closure is declared", "w8 has closed",
                 "w8 closed", "maturity — closed", "is closed under",
                 "closes under this record")
# The sentences in which the forms may stand, each exactly once; the status
# line is set aside by its own form (draft or accepted) and the proposed
# closure sentence by the brief's drafting target before these.
CONDITIONED = (
    "declaring W8 complete and closed only on its own acceptance, publication and "
    "independent remote verification.",
    "**W8 — Generative Evaluation Maturity — closes under this record, effective per "
    "its status line and not before,**",
    "**W8-D7 is complete by this record, effective per its status line.**",
    "**W8 closes complete, not perfect — effective per the status line of this "
    "record.**",
    "**W8 — Generative Evaluation Maturity — CLOSED**, effective per the status line "
    "of this record and not before.",
    "**It establishes, on its own acceptance, publication and independent remote "
    "verification, that W8 is complete and closed in the accepted sense**",
)
# Each inventoried conditioned sentence carries one of these local conditions,
# read after the fold. The status line carries the record's state and the
# proposed sentence is marked proposed by the record's item 8; neither is in
# the inventory above, and both are set aside by their own forms.
CONDITION_PHRASES = (
    "effective per its status line", "effective per the status line",
    "on its own acceptance, publication and independent remote verification",
)


def unconditioned_inventory(sentences=None):
    """The inventoried conditioned sentences carrying none of the condition
    phrases - a check over the inventory's own entries."""
    sentences = CONDITIONED if sentences is None else sentences
    return [s for s in sentences
            if not any(c in folded(s) for c in CONDITION_PHRASES)]
# Wording that would presume a conclusion about the instrument, a model or
# adoption, or name a later phase; none may appear anywhere in the record.
PRESUMPTION = ("the instrument is mature", "the instrument is adequate",
               "the instrument is validated", "the instrument is ready",
               "the instrument is safe", "the instrument is useful",
               "the instrument discriminates correctly",
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
# brief's items 8, 37 and 61 bar: the record states only that no W8 act
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
                "performed at each landing", "each recorded in its own record",
                "was performed by the human reviewer")
# Verdict vocabulary as a bold form - the shape a posture cell would take -
# refused anywhere in the record (ADR-0054 decision 31; W8-D7-CAB item 22),
# read after the bounded verdict fold.
VERDICT_WORDS = ("pass", "passed", "fail", "failed", "safe", "approved",
                 "ready", "mature", "valid", "winner", "score", "grade")
INVISIBLE = re.compile("[​‌‍⁠﻿­]")
BOLD_SPAN = re.compile(r"(\*\*|__)(.+?)\1", re.S)
SPAN_MARKS = re.compile(r"[*_`~\s]+")
WITHHELD = ("contacts no model and opens no later phase",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "any declaration before this record's own acceptance, publication and "
            "independent remote verification that W8 or W8-D7 is finished",
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
            "what closure authorises is closure, and nothing beyond it")

NON_AUTH_SECTION = "## 18. Explicit non-authorisations"
NON_AUTH_INTRO = "51. This record and the closure of W8 do not authorise:"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - any declaration before this record's own acceptance, publication and "
    "independent remote verification that W8 or W8-D7 is finished;",
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
    "    - any act after closure: what closure authorises is closure, and nothing "
    "beyond it.",
)
NON_AUTH_CLOSE = ("    **Model contact remains outside this record; closure authorises "
                  "nothing new.**")
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))

# --------------------------------------- board and registry: authorised edits
CR_LINK = "([`W8-closure-record.md`](W8-closure-record.md))"
CR_STATUS_TAIL = (
    "under the standing closure-without-false-resolution standard, effective on "
    "publication and independent remote verification and not before, drafted from "
    "the published closure assessment and the live public repository state: every "
    "runway obligation satisfied, satisfied with its named carried item or honestly "
    "recorded as external across the sixty-eight published assessment rows; the "
    "seven deliverables landed in the runway's order, each behind its own accepted "
    "brief; the W8-D5 finding undetermined as recorded; the W8-D6 decision a "
    "decision that authorises nothing, its four separate instruments unopened and "
    "its authority question unanswered; ADR-0047 precondition 3 outstanding in its "
    "lawful resting state and no other precondition moved; every recorded "
    "divergence undiagnosed; the void attempt void and ADR-0058's reservation "
    "standing; the retained records sealed; Part Q and the `local-wordlist` seam "
    "unresolved and bounded; the inherited W7 inventory carried item-for-item; the "
    "three stale derivatives named and not repaired, their repair decisions unmade; "
    "no W8 act prepared, authorised or performed model contact and no exchange "
    "classified; the fresh closure-time P4b act the human reviewer's at acceptance, "
    "separate from P4a and never inferred from it; no later phase opened, designed, "
    "scheduled or named as assigned. The assessment module's CB7 succeeds, its "
    "W8-D7 entry set and no-later-phase limb, to a historical proof at the Landing "
    "B seal, the live gates moving to this record's module; R9's sentence, constant "
    "and tuple stay unchanged. Closure authorises nothing beyond closure.")
CR_STATUS = {
    "draft": ("**A draft W8 closure record, `W8-CR`, is before the human reviewer** "
              + CR_LINK + ": if accepted, it would close W8 " + CR_STATUS_TAIL),
    "accepted": ("**The W8 closure record, `W8-CR`, is accepted** " + CR_LINK
                 + " — accepted %s: it closes W8 " + CR_STATUS_TAIL),
}
HEAD_BEFORE = ("**Status:** **The W8 entry gate is complete — three documents, three "
               "acceptances:**")
HEAD_AFTER = {
    "draft": ("**Status:** **A draft W8 closure record, `W8-CR`, is before the human "
              "reviewer** " + CR_LINK + " — **W8 is not closed.** **The W8 entry gate is "
              "complete — three documents, three acceptances:**"),
    "accepted": ("**Status:** **W8 — Generative Evaluation Maturity — is complete and "
                 "closed — in the accepted sense, effective on publication and remote "
                 "verification, sealed under `W8-CR`** " + CR_LINK + " — accepted %s. "
                 "**The W8 entry gate was complete — three documents, three "
                 "acceptances:**"),
}
CAR_ROW_HEAD = "| W8-D7 — Closure (assessment record, W8-D7-CAR) | "
CR_ROW = ("| W8 — Closure Record (W8-CR) | [`W8-closure-record.md`]"
          "(W8-closure-record.md) | ")
CR_ROW_BODY = (
    "Tier J: **W8 — Generative Evaluation Maturity — closes under this record, in the "
    "accepted sense, effective on publication and independent remote verification "
    "and not before**, under the standing closure-without-false-resolution standard "
    "and drafted from the published closure assessment. Every runway obligation "
    "satisfied, satisfied with its named carried item or honestly recorded as "
    "external across the sixty-eight published rows; the seven deliverables landed "
    "in the runway's order under their own accepted briefs; **the W8-D5 finding "
    "undetermined as recorded; the W8-D6 decision a decision that authorises "
    "nothing, its instruments unopened; precondition 3 outstanding in its lawful "
    "resting state; every divergence undiagnosed; the void attempt void and the "
    "reservation standing; the retained records sealed; Part Q and the "
    "`local-wordlist` seam unresolved and bounded; the inherited W7 inventory "
    "carried item-for-item; the three stale derivatives named and not repaired.** "
    "No W8 act prepared, authorised or performed model contact, and the published "
    "records classify no exchange. P4a reported separately in the record; the fresh "
    "closure-time P4b act across all eleven families is the human reviewer's at "
    "acceptance, separate from P4a and never inferred from it. The assessment "
    "module's CB7 succeeds to a historical proof at the Landing B seal, the live "
    "gates moving to this record's module; R9 unchanged. **Closure authorises "
    "nothing beyond closure; no later phase opens; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**" + R9_SENTENCE + " W8-D7 is open for closure work only and its "
                 "closure assessment is published; W8 is not closed.**")
# The closing sentence this landing leaves, by state: a draft moves nothing;
# an accepted closure record completes W8-D7 and closes W8 in the accepted sense.
CLOSED_AFTER = {
    "draft": CLOSED_BEFORE,
    "accepted": ("**" + R9_SENTENCE + " W8-D7 is complete and W8 is closed under "
                 "`W8-CR` — in the accepted sense, effective on publication and "
                 "independent remote verification; closure authorises nothing beyond "
                 "closure.**"),
}
CR_DRAFT = ("**Status:** Draft for human review. Not accepted. **If accepted, effective "
            "only on publication and independent remote verification, at which point "
            "W8 — Generative Evaluation Maturity — is complete and closed and W8-D7 is "
            "complete.** Not a build instruction. No status is flipped by the "
            "implementer; acceptance is the human reviewer's dated act, and until that "
            "act this record closes nothing.")
CR_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective only on "
               "publication and independent remote verification, at which point W8 — "
               "Generative Evaluation Maturity — is complete and closed and W8-D7 is "
               "complete.** Not a build instruction.")
NEW_ENTRY = {
    "id": "W8-CR", "path": RECORD, "type": "phase-record",
    "title": "W8 Closure Record",
    "role": (
        "The W8 closure record and audit seal, completing W8-D7 and closing W8 - "
        "effective on acceptance, publication and independent remote verification, "
        "and not before. Drafted from the published and independently verified "
        "whole-phase closure assessment W8-D7-CAR, which is the evidence base for "
        "every claim it makes, and from the live public repository state, under the "
        "standing W2-through-W7 closure standard restated as closure without false "
        "resolution. It declares W8 complete and closed in the accepted sense: the "
        "governance work assigned to the phase under its accepted runway and "
        "deliverable briefs completed in the runway's order and publicly evidenced - "
        "a doctrine before any case, an instrument before calibration, calibration "
        "before validation, validation before the adequacy review, the review before "
        "the contact decision - each landed by its own accepted brief and "
        "authorisation; the public/private boundary held; no W8 act prepared, "
        "authorised or performed model contact, and the published records, under "
        "ADR-0058's standing reservation, classify no exchange and do not state "
        "whether model contact occurred. It carries every open matter at its true "
        "standing and represents none as resolved: the W8-D5 finding undetermined as "
        "recorded; the W8-D6 decision a decision that authorises nothing, its four "
        "separate instruments unopened, named and not supplied and its authority "
        "question unanswered; ADR-0047 precondition 3 outstanding in its lawful "
        "resting state and no other precondition moved; every recorded divergence "
        "undiagnosed; the void attempt void and the reservation standing; the "
        "retained records sealed; Part Q and the local-wordlist seam unresolved and "
        "bounded; the twenty-six historical unknowns unanswered; the inherited W7 "
        "inventory item-for-item; the stale root README, registry rendering and "
        "concept overview named and not repaired. It carries the brief's drafting "
        "target as its closure sentence, used only through the human reviewer's "
        "acceptance; states P4a and the fresh closure-time P4b act separately; and "
        "carries the exact succession of the assessment module's CB7 to a historical "
        "proof at the Landing B seal, the W8-D7 entry set and no-later-phase limb "
        "moving to this record's module, with proof obligations CC1 to CC9. It opens "
        "no later phase and names none as assigned, diagnoses nothing, reads no "
        "custody, contacts no model, and authorises nothing beyond closure."),
    "depends_on": ["W8-D7-CAR", "W8-D7-CAB", "W8-AR", "W8-D6-CDR", "W8-D6-CDB",
                   "W8-D5-AFR", "ADR-0061", "W8-D5-EAB", "W8-D4-CPR", "W8-D4-VRC",
                   "W8-D4-VSR", "W8-D4-VCR", "ADR-0060", "W8-D4-IVB", "W8-D3-CCR",
                   "W8-D3-HDR", "W8-S1-SCR", "W8-S1-SOB", "ADR-0059", "ADR-0058",
                   "ADR-0057", "W8-D3-SCB", "W8-D2-CBC", "W8-D2-DIC", "W8-D2-MSA",
                   "ADR-0055", "W8-D2-DIB", "ADR-0054", "W8-D1-EDB", "ADR-0056",
                   "W8-DER", "W8-HPC", "W8-HAC", "W8-CHC", "ADR-0047", "ADR-0046",
                   "ADR-0052", "ADR-0051", "ADR-0033", "ADR-0034", "W7-CR",
                   "W7-D7-CAR", "W7-D7-CAB", "W6-D6-CAB", "W6-CR", "W7-D6-HDR"],
}

# ------------------------------------------------- the evidence homes and pins
HOMES_SECTION = None  # this record carries no homes table; CC9 proves the identities
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
    """The bounded fold: marks removed, whitespace runs made one space, case
    folded."""
    return " ".join(FOLDED_MARKS.sub("", text).split()).casefold()


def verdict_forms(text):
    """The inventoried verdict words standing alone as bold postures, read
    after the bounded verdict fold."""
    found = []
    for m in BOLD_SPAN.finditer(INVISIBLE.sub("", text)):
        inner = SPAN_MARKS.sub("", m.group(2)).strip(".:;,!?").casefold()
        if inner in VERDICT_WORDS:
            found.append(inner)
    return found


def prose_paragraphs(text):
    """Markdown's logical paragraphs: blocks parted by blank lines - empty or
    SPACE/TAB-only, as CommonMark defines a blank line - with every run of
    whitespace inside a block made one space."""
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


def d7c_snapshot():
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
    commit, problems = d7c_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_cr_historical_" + Path(rel).stem,
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


def drafting_target():
    """The brief's drafting target (W8-D7-CAB section 22), the one blockquote
    line of the published brief that opens with the closure sentence."""
    lines = [line for line in baseline_text(BRIEF).split("\n")
             if line.startswith("> **W8 closes because")]
    return lines[0] if len(lines) == 1 else None


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
    the non-blank lines adjacent to it, in order. Nothing is filtered."""
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


def one_table(text, heading, header, separator, width):
    """The one table of a section, read whole."""
    blocks, v = section_blocks(text, heading, ((header, separator, width),))
    return (blocks[0] if blocks else []), v


def first_bold(cell):
    m = re.match(r"\*\*([^*]+)\*\*", cell)
    return m.group(1) if m else None


# ------------------------------------------ the published assessment's tables
def assessment_text():
    return baseline_text(ASSESSMENT_RECORD)


def assessment_preconditions(text=None):
    rows, v = one_table(assessment_text() if text is None else text,
                        ASSESSMENT_PRECONDITION_SECTION, PRECONDITION_HEADER,
                        PRECONDITION_SEPARATOR, 4)
    return rows, v


def assessment_inventory(text=None):
    rows, v = one_table(assessment_text() if text is None else text,
                        ASSESSMENT_INVENTORY_SECTION, INVENTORY_HEADER,
                        INVENTORY_SEPARATOR, 7)
    return rows, v


def assessment_tally(text=None):
    rows, v = one_table(assessment_text() if text is None else text,
                        ASSESSMENT_RUNWAY_SECTION, RUNWAY_HEADER, RUNWAY_SEPARATOR, 4)
    tally = {}
    for cells in rows:
        tally[first_bold(cells[2])] = tally.get(first_bold(cells[2]), 0) + 1
    return tally, len(rows), v


def carried_row_lines(rows):
    return ["| " + " | ".join(r) + " |" for r in rows]


def carried_violations(text, assessment=None):
    """CC1: the precondition table byte-identical to the published
    assessment's; inventory rows one to twenty-nine byte-identical to the
    published rows and row thirty exactly the fixed closure-time row; the
    runway tally the count the published table yields."""
    v = []
    pre_a, p1 = assessment_preconditions(assessment)
    pre_r, p2 = one_table(text, PRECONDITION_SECTION, PRECONDITION_HEADER,
                          PRECONDITION_SEPARATOR, 4)
    v += p1 + p2
    if len(pre_a) != 7 or pre_r != pre_a:
        v.append("the precondition table is not the published assessment's")
    inv_a, p3 = assessment_inventory(assessment)
    inv_r, p4 = one_table(text, INVENTORY_SECTION, INVENTORY_HEADER,
                          INVENTORY_SEPARATOR, 7)
    v += p3 + p4
    if len(inv_a) != INVENTORY_ROWS or len(inv_r) != INVENTORY_ROWS:
        v.append("the inventory is not thirty rows on both sides")
    elif inv_r[:CARRIED_ROWS] != inv_a[:CARRIED_ROWS]:
        v.append("an inventory row one to twenty-nine differs from the published row")
    elif inv_r[CARRIED_ROWS] != ROW_30:
        v.append("row thirty is not the fixed closure-time row")
    if [r[0] for r in inv_r] != ["%d" % n for n in range(1, INVENTORY_ROWS + 1)]:
        v.append("the inventory rows are not numbered one to thirty")
    if any(first_bold(r[3]) is None for r in inv_r):
        v.append("an inventory state cell does not open with its bold state")
    tally, n, p5 = assessment_tally(assessment)
    v += p5
    if n != RUNWAY_ROWS:
        v.append("the published runway table is not sixty-eight rows")
    expected = {k: c for k, c, _ in TALLY}
    if tally != expected:
        v.append("the published runway tally is not the tally this record states")
    for _, _, phrase in TALLY:
        if text.count(phrase) != 1:
            v.append("the tally phrase is not carried once: %s" % phrase[:40])
    return v


def closure_form_violations(text, h):
    """CC1: the closure forms stand only in the inventoried conditioned
    sentences, each present exactly once, and in the status line of the
    record's own state."""
    state, date = h.rec.header_state(text)
    status = {"draft": CR_DRAFT, "accepted": CR_ACCEPTED % date if date else None}.get(state)
    v = []
    if status is None or text.count(status) != 1:
        return ["the status line is neither form, or not once"]
    target = drafting_target()
    if target is None:
        return ["the brief's drafting target is not found at the baseline"]
    low = folded(text)
    for sentence in (status, target) + CONDITIONED:
        f = folded(sentence)
        if low.count(f) != 1:
            v.append("a conditioned sentence is not present once: %s" % sentence[:40])
            continue
        low = low.replace(f, " ", 1)
    v += ["a closure form outside its conditioned sentences: %s" % p
          for p in CLOSURE_FORMS if p in low]
    v += ["a conditioned sentence carries no local condition: %s" % s[:40]
          for s in unconditioned_inventory()]
    return v


def reference_violations(text):
    """CC1: every section of the published assessment and of the brief this
    record cites exists, and every cited assessment item is within its
    numbering - bounded syntactic checks over the citation forms used."""
    v = []
    for m in re.finditer(r"`W8-D7-CAR` §(\d+)(?: item (\d+))?", text):
        if not 1 <= int(m.group(1)) <= ASSESSMENT_SECTIONS:
            v.append("a cited assessment section does not exist: §" + m.group(1))
        if m.group(2) and not 1 <= int(m.group(2)) <= ASSESSMENT_ITEMS:
            v.append("a cited assessment item does not exist: item " + m.group(2))
    for m in re.finditer(r"`W8-D7-CAR` item (\d+)", text):
        if not 1 <= int(m.group(1)) <= ASSESSMENT_ITEMS:
            v.append("a cited assessment item does not exist: item " + m.group(1))
    for m in re.finditer(r"`W8-D7-CAB` §(\d+)", text):
        if not 1 <= int(m.group(1)) <= BRIEF_SECTIONS:
            v.append("a cited brief section does not exist: §" + m.group(1))
    for m in re.finditer(r"`W8-D7-CAB` items? (\d+(?:, \d+)*(?: and \d+)?)", text):
        for n in re.findall(r"\d+", m.group(1)):
            if not 1 <= int(n) <= BRIEF_ITEMS:
                v.append("a cited brief item does not exist: item " + n)
    rows, problems = one_table(text, LIMB_SECTION, LIMB_HEADER, LIMB_SEPARATOR, 2)
    v += problems
    if len(rows) != LIMB_ROWS:
        v.append("the limb table is not twelve rows")
    for cells in rows:
        for m in re.finditer(r"§(\d+)(?: item (\d+))?", cells[1]):
            if not 1 <= int(m.group(1)) <= ASSESSMENT_SECTIONS:
                v.append("a limb cites a section that does not exist: §" + m.group(1))
            if m.group(2) and not 1 <= int(m.group(2)) <= ASSESSMENT_ITEMS:
                v.append("a limb cites an item that does not exist: item " + m.group(2))
    return v


def carriage_violations(text, h):
    """CC1: the load-bearing statements each once; the nine rules, the chain
    and the posture sentence once; the invariant exactly; the closure forms
    conditioned; the drafting target once; the carried tables exact; the
    inventories of refused forms empty; the references resolving."""
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
    target = drafting_target()
    if target is None or text.count(target + "\n") != 1:
        v.append("the proposed closure sentence is not the brief's drafting target, once")
    v += closure_form_violations(text, h)
    v += carried_violations(text)
    v += reference_violations(text)
    low = folded(text)
    v += ["a presuming conclusion: %s" % p for p in PRESUMPTION if p in low]
    v += ["withdrawn mechanical-conformance formula: %s" % p
          for p in WITHDRAWN if p in low]
    v += ["universal session or reveal claim: %s" % p for p in UNIVERSAL if p in low]
    v += ["a statement whether contact occurred: %s" % p
          for p in CONTACT_STATEMENTS if p in low]
    v += ["an attestation of a performed act: %s" % p for p in ATTESTATIONS if p in low]
    v += ["a verdict form as a bold posture: %s" % b for b in verdict_forms(text)]
    rows, problems = one_table(text, OBLIGATIONS_SECTION, OBLIGATIONS_HEADER,
                               OBLIGATIONS_SEPARATOR, 3)
    v += problems
    if [r[0] for r in rows] != ["**CC%d**" % n for n in range(1, 10)]:
        v.append("the obligations table is not CC1 to CC9")
    return v


def withholding_violations(text):
    """CC2: every non-authorisation phrase present, and section 18 exactly its
    authorised whole block."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["section 18 is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("section 18 is not exactly its authorised whole block")
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
    """CC3: over the text's logical prose paragraphs - no case identity, no
    digest outside the exempt exact lines, no reserved authoring label,
    schema literal or method label, no number beside a token or relation
    name, and no derived-figure form. A textual guard only."""
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


ONES = ("", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen")
TENS = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety")


def words(n):
    """A count from one to ninety-nine in words, as the record writes them."""
    if n < 20:
        return ONES[n]
    return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")


LAW_ROUTE_DIRECT = ("read directly at the baseline object; its block in "
                    "section 17 is these bytes (CC1)")


def law_route(mode, assessment_row):
    """The route cell of a law row: read directly, or relied on through the
    published assessment's source account at its row."""
    if mode == "direct":
        return LAW_ROUTE_DIRECT
    return ("relied on through the published assessment's account, "
            "`W8-D7-CAR` §1 row %s, the same object" % words(assessment_row))


def law_rows(rows=None):
    rows = LAW_ROWS if rows is None else rows
    return [["%d" % n, "`%s`" % i, "`%s`" % p, "`%s`" % c, "`%s`" % b, "`%s`" % s,
             law_route(mode, row)]
            for n, i, p, c, b, s, mode, row in rows]


def law_row_lines(rows=None):
    return ["| " + " | ".join(r) + " |" for r in law_rows(rows)]


def method_tables(text):
    """Section 1 read whole: its three table blocks are the identity
    provenance table, the law provenance table and the file-provenance
    table, in that order."""
    return section_blocks(text, BASIS_SECTION, (
        (BASIS_HEADER, BASIS_SEPARATOR, 6), (LAWS_HEADER, LAWS_SEPARATOR, 7),
        (FILES_HEADER, FILES_SEPARATOR, 5)))


def basis_table_violations(text):
    blocks, v = method_tables(text)
    if not blocks or blocks[0] != basis_rows():
        v.append("the provenance table is not exactly its trusted rows")
    return v


def files_table_violations(text):
    blocks, v = method_tables(text)
    if len(blocks) < 3 or blocks[2] != file_rows():
        v.append("the file-provenance table is not exactly its trusted rows")
    return v


def laws_table_violations(text):
    """CC4: the law table is exactly its trusted rows, and the lead's counts in
    words are the inventory's."""
    blocks, v = method_tables(text)
    if len(blocks) < 2 or blocks[1] != law_rows():
        v.append("the law-provenance table is not exactly its trusted rows")
    direct = sum(1 for r in LAW_ROWS if r[6] == "direct")
    lead = "%s were read directly at their baseline objects" % words(direct).capitalize()
    other = "The other %s are relied on through the published" % words(len(LAW_ROWS) - direct)
    if text.count(lead) != 1 or text.count(other) != 1:
        v.append("the law lead's counts are not the inventory's")
    return v


def assessment_source_rows():
    """The published assessment's registered-source table at the baseline,
    read whole from its committed bytes: {identity: (row, path, commit,
    object, digest)}."""
    section = section_lines(baseline_text(ASSESSMENT_RECORD),
                            ASSESSMENT_SOURCE_SECTION)
    blocks = pipe_blocks(section) if section else []
    if not blocks:
        return {}
    rows, problems = closed_block(blocks[0], BASIS_HEADER, BASIS_SEPARATOR, 6)
    if problems:
        return {}
    return {i.strip("`"): (int(n), p.strip("`"), c.strip("`"), b.strip("`"),
                           s.strip("`")) for n, i, p, c, b, s in rows}


def law_object_violations(rows=None, resolve=None, registered=None, last=None,
                          assessment_rows=None, direct=None):
    """CC4: every law row resolves as the identity rows do; a law marked read
    directly is one this module executes, at its executed path; a law marked
    relied on is not one this module executes; and every row is the published
    assessment's own row for that law - number, path, commit, object and
    digest."""
    rows = LAW_ROWS if rows is None else rows
    resolve, last, registered = _resolvers(resolve, last, registered)
    assessment_rows = (assessment_source_rows() if assessment_rows is None
                       else assessment_rows)
    direct = DIRECT_LAWS if direct is None else direct
    v = []
    if [r[0] for r in rows] != list(range(1, len(rows) + 1)):
        v.append("the law rows are not numbered consecutively from one")
    if len({r[1] for r in rows}) != len(rows):
        v.append("a law is listed twice")
    for n, ident, path, commit, blob, sha, mode, row in rows:
        got_blob, got_sha = resolve(commit, path)
        if got_blob != blob:
            v.append("law row %d: the object at the cited commit differs" % n)
        if got_sha != sha:
            v.append("law row %d: the committed bytes differ from the pin" % n)
        if resolve(BASELINE, path)[0] != blob:
            v.append("law row %d: the object at the baseline differs" % n)
        if last(path) != commit:
            v.append("law row %d: the cited commit is not the last first-parent "
                     "change" % n)
        if registered.get(ident) != path:
            v.append("law row %d: the law is not registered at that path" % n)
        if mode == "direct" and direct.get(ident) != path:
            v.append("law row %d: marked read directly, but this module executes "
                     "no block of it" % n)
        if mode == "via" and ident in direct:
            v.append("law row %d: a law this module executes is marked relied on" % n)
        if mode not in ("direct", "via"):
            v.append("law row %d: an unknown route" % n)
        if assessment_rows.get(ident) != (row, path, commit, blob, sha):
            v.append("law row %d: not the published assessment's own row for "
                     "this law" % n)
    return v


def direct_law_violations(rows=None, direct=None):
    """CC4: the laws marked read directly are exactly the ones this module
    executes."""
    rows = LAW_ROWS if rows is None else rows
    direct = DIRECT_LAWS if direct is None else direct
    marked = {r[1] for r in rows if r[6] == "direct"}
    return ([] if marked == set(direct) else
            ["the laws marked read directly are not exactly the executed laws"])


LAW_ID = re.compile(r"ADR-\d{4}")


def cited_law_violations(text, rows=None):
    """CC4: every law the record cites, in any written form, has a law row, and
    every law row is cited outside the table. A check over identity tokens
    of the law form only; it decides nothing about what a citation means."""
    rows = LAW_ROWS if rows is None else rows
    body = text
    for line in law_row_lines(rows):
        body = body.replace(line + "\n", "", 1)
    cited = set(LAW_ID.findall(body))
    known = {r[1] for r in rows}
    return (sorted("a cited law without a provenance row: %s" % i
                   for i in cited - known)
            + sorted("a law row for a law the record does not cite: %s" % i
                     for i in known - cited))


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
    """CC4: every provenance row resolves - the object at the cited commit
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
    """CC4: every file-provenance row resolves the same way and names no
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


NAMED_PATH = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*"
                        r"\.(?:md|py|txt|json|yml|yaml|toml|cfg|ini))`")
NAMED_IDENTITY = re.compile(r"`([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)`")


def named_path_violations(text):
    """CC4: every repository path this record names in code marks, with one of
    NAMED_PATH's listed extensions, has a provenance row, other than the two
    files this landing adds. A bounded syntactic check: a path in plain prose
    is outside it, and it decides neither whether a source was read nor
    whether it governs."""
    known = ({r[2] for r in BASIS_ROWS} | {r[2] for r in LAW_ROWS}
             | {r[1] for r in FILE_ROWS} | {RECORD, SELF_REL})
    return sorted({"a named path without provenance: %s" % p
                   for p in NAMED_PATH.findall(text) if p not in known})


def named_identity_violations(text, registered=None):
    """CC4: every registered identity this record names in code marks has a
    provenance row, other than this record's own. A bounded syntactic check."""
    if registered is None:
        registered = {e["id"] for e in json.loads(committed(BASELINE, REGISTRY))["entries"]}
    known = {r[1] for r in BASIS_ROWS} | {r[1] for r in LAW_ROWS} | {NEW_ENTRY["id"]}
    return sorted({"a named identity without provenance: %s" % i
                   for i in NAMED_IDENTITY.findall(text)
                   if i in registered and i not in known})


def succession_rows(h):
    return [["`%s`" % ASSESSMENT, ", ".join(h.auth.labels(SITES[ASSESSMENT])),
             "`%s`" % PREIMAGE[ASSESSMENT][1], "`%s`" % POSTIMAGE[ASSESSMENT][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def succession_table_violations(text, h):
    rows, v = one_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                        SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, record, h, sites=None):
    """CC5's first limb: the CB7 succession is the exact reviewed
    transformation of the assessment module's fixed pre-image, reversible,
    its sites CB7's alone, the pinned anchor the baseline, the succeeded
    module holding no executable live registry read."""
    sites = SITES[ASSESSMENT] if sites is None else sites
    v = []
    pre = baseline_text(ASSESSMENT)
    if _sha(pre.encode("utf-8")) != PREIMAGE[ASSESSMENT][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[ASSESSMENT][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("CB7",):
        v.append("the sites are not CB7's alone")
    if present.count(D7B_LINE) != 1 or D7B_LANDING != BASELINE:
        v.append("the succession's anchor is not this landing's baseline")
    if present.count(HISTORICAL_READ) != 1 or LIVE_READ_LINE in present:
        v.append("the succeeded CB7 does not read the D7-B landing commit alone")
    if present.count(LIVE_PHRASE) != 2 or present.count(LIVE_LITERAL) != 1:
        v.append("the live-read phrase is not confined to its two string literals")
    if pre.count(LIVE_READ_LINE) != 1 or HISTORICAL_READ in pre:
        v.append("the pre-image is not the live-gated module")
    return v + succession_table_violations(record, h)


def historical_claim_violations():
    """CC5's second limb: the succeeded modules' claims hold at their own
    commits - the W8-D7 entries exactly the brief's at the W8-D7 opening and
    exactly the brief's and the assessment's at the Landing B seal, no later
    phase at either."""
    v = []
    for commit, expected in ((D7A_LANDING, D7_ENTRIES_AT_OPENING),
                             (D7B_LANDING, D7_ENTRIES_AT_BASELINE)):
        at = json.loads(committed(commit, REGISTRY))["entries"]
        if {e["id"] for e in at if e["deliverable"] == "W8-D7"} != expected:
            v.append("the W8-D7 entry set at %s is not the succeeded claim" % commit[:8])
        if {e["phase"] for e in at} - KNOWN_PHASES:
            v.append("a later phase's entry exists at %s" % commit[:8])
    return v


def cr_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CR_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CR_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def car_row_line(board_pre):
    """The assessment's board row, the table's last line at the baseline,
    found by its fixed head."""
    lines = [l for l in board_pre.split("\n") if l.startswith(CAR_ROW_HEAD)]
    return lines[0] if len(lines) == 1 else None


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    car = car_row_line(board_pre) or ""
    return (
        ("status-head", HEAD_BEFORE, fill(HEAD_AFTER[state])),
        ("status-tail", CLOSED_BEFORE, fill(CR_STATUS[state]) + " " + CLOSED_AFTER[state]),
        ("row", car + "\n", car + "\n" + CR_ROW + fill(ROW_PREFIX[state]) + CR_ROW_BODY
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
    return " ".join([CR_ROW, CR_ROW_BODY, CLOSED_AFTER["draft"],
                     CLOSED_AFTER["accepted"], CR_STATUS["draft"],
                     CR_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample, HEAD_AFTER["draft"],
                     HEAD_AFTER["accepted"] % sample])


def entry_violations(entries, record_text, h, base_entries=None):
    """CC7: this record's entry binds its path, type, phase, deliverable,
    status, date and hash; the brief's and the assessment's entries are
    byte-unchanged from the baseline; the W8-D7 entries are exactly the
    brief's, the assessment's and this record's; no entry of a later phase
    exists."""
    v = []
    by_id = {x["id"]: x for x in entries}
    e = by_id.get("W8-CR")
    state, date = h.rec.header_state(record_text)
    if e is None:
        return ["no W8-CR entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            RECORD, "phase-record", "W8", "W8-D7"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(record_text.encode("utf-8")):
        v.append("the entry's hash differs from the record")
    if base_entries is None:
        base_entries = json.loads(committed(BASELINE, REGISTRY))["entries"]
    base_by_id = {x["id"]: x for x in base_entries}
    for earlier in sorted(D7_ENTRIES_AT_BASELINE):
        if base_by_id.get(earlier) is None or by_id.get(earlier) != base_by_id[earlier]:
            v.append("an earlier W8-D7 entry is not byte-unchanged from the baseline: "
                     + earlier)
    if {x["id"] for x in entries if x["deliverable"] == "W8-D7"} != D7_ENTRIES:
        v.append("the W8-D7 entries are not exactly the brief's, the assessment's "
                 "and this record's")
    if {x["phase"] for x in entries} - KNOWN_PHASES:
        v.append("an entry of a later phase exists")
    return v


def landing_paths(commit):
    if commit is None:
        out = _git("status", "--porcelain", "--untracked-files=all")
        return {line[3:].strip('"') for line in out.splitlines() if line}
    return set(_git("diff", "--name-only", BASELINE, commit).split())


def integrity_violations(commit, tree_at=None, count_at=None, sha_of=None,
                         entries=None, homes=None, pins=None):
    """CC9: each home's tree at the snapshot equals its pinned tree and its
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
class CC1_Carriage(unittest.TestCase):
    def test_cc1_record_carries_statements_conditioned_closure_and_carried_tables(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="statements, blocks, conditioned closure, carried "
                               "tables, references and no refused form"):
            self.assertEqual(carriage_violations(text, h), [])
        inv_rows, _ = one_table(text, INVENTORY_SECTION, INVENTORY_HEADER,
                                INVENTORY_SEPARATOR, 7)
        first_inv = "| " + " | ".join(inv_rows[0]) + " |"
        last_inv = "| " + " | ".join(inv_rows[-1]) + " |"
        pre_rows, _ = one_table(text, PRECONDITION_SECTION, PRECONDITION_HEADER,
                                PRECONDITION_SEPARATOR, 4)
        third_pre = "| " + " | ".join(pre_rows[2]) + " |"
        target = drafting_target()
        for name, mutated in (
                ("a dropped inventory row", text.replace(first_inv + "\n", "", 1)),
                ("an altered inventory state", text.replace(
                    first_inv, first_inv.replace("**outstanding in lawful resting "
                                                 "state**", "**discharged**", 1), 1)),
                ("row thirty altered", text.replace(
                    last_inv, last_inv.replace("**Landing C is this record**",
                                               "**Landing C is unbegun**", 1), 1)),
                ("precondition 3 shown discharged", text.replace(
                    third_pre, third_pre.replace("**outstanding in lawful resting "
                                                 "state**", "**discharged**", 1), 1)),
                ("a dropped precondition row", text.replace(third_pre + "\n", "", 1)),
                ("an unconditioned closure sentence", text.replace(
                    "\n## 3.", "\nW8 is closed.\n\n## 3.", 1)),
                ("an unconditioned closure sentence in bold", text
                 + "\nW8 **is complete**.\n"),
                ("an unconditioned closure sentence in code marks", text
                 + "\nW8 `is complete`.\n"),
                ("an unconditioned closure sentence with a zero-width space", text
                 + "\nW8 is​ complete.\n"),
                ("an unconditioned closure sentence over a soft break", text
                 + "\nW8 is\ncomplete.\n"),
                ("an unconditioned closure sentence in capitals", text
                 + "\nW8 IS COMPLETE.\n"),
                ("a conditioned sentence doubled", text + "\n" + CONDITIONED[3] + "\n"),
                ("a conditioned sentence removed", text.replace(
                    CONDITIONED[3] + " ", "", 1)),
                ("the complete-not-perfect sentence stripped of its condition",
                 text.replace(CONDITIONED[3],
                              "**W8 closes complete, not perfect.**", 1)),
                ("the carried-cell scoping statement removed", text.replace(
                    REQUIRED[4] + " ", "", 1)),
                ("the drafting target altered", text.replace(
                    target, target.replace("authorises nothing", "authorises contact",
                                           1), 1)),
                ("the drafting target doubled", text + "\n" + target + "\n"),
                ("a later phase named", text + "\nW9 follows.\n"),
                ("the tally altered", text.replace("**sixty-one satisfied;",
                                                   "**sixty satisfied;", 1)),
                ("a cited assessment section that does not exist", text
                 + "\nSee `W8-D7-CAR` §17.\n"),
                ("a cited brief item that does not exist", text
                 + "\nSee `W8-D7-CAB` item 80.\n"),
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
                ("a statement that contact occurred", text
                 + "\nA model was contacted during W8.\n"),
                ("a statement that contact did not occur, in bold", text
                 + "\n**No model has been contacted.**\n"),
                ("the W7 closure's contact sentence", text
                 + "\nNo model contacted at any point.\n"),
                ("a performance attestation in code marks", text
                 + "\nP4b was `recorded as performed` at each landing.\n"),
                ("an eighth posture in the posture sentence", text.replace(
                    "· **unopened, named and not supplied**. No verdict",
                    "· **unopened, named and not supplied** · **passed**. No "
                    "verdict", 1)),
                ("a presuming conclusion", text + "\nThe instrument is mature.\n")):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h))
        for name, added in (("a phrase outside the inventories",
                             "\nW8 is nearly finished.\n"),
                            ("a reveal claim bounded to its session corpora",
                             "\nEvery withheld record of the two session corpora "
                             "was revealed.\n"),
                            ("a negation that is not a form",
                             "\nNothing here says that closure is near.\n"),
                            ("a verdict word in plain prose",
                             "\nNo pass or fail is declared here.\n"),
                            ("a different bold word", "\n**passage**\n"),
                            ("the lawful contact account",
                             "\nNo W8 act prepared, authorised or performed model "
                             "contact; this record states neither way whether "
                             "contact occurred.\n"),
                            ("a duty stated and not attested",
                             "\nA fresh P4b human act is owed at acceptance; its "
                             "discharge is held as this record's acceptance.\n")):
            with self.subTest(positive="%s is not what the inventories refuse"
                                       % name):
                self.assertEqual(
                    [x for x in carriage_violations(text + added, h)
                     if x.startswith(("a closure form outside",
                                      "a presuming conclusion",
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
                ("a zero-width space inside the bold", "\n**pa​ss**\n"),
                ("code marks inside the bold", "\n**`pass`**\n"),
                ("underscore bold", "\n__passed__\n"),
                ("spacing, capitals and punctuation", "\n** Fail. **\n"),
                ("bold italics", "\n***safe***\n"),
                ("a soft break inside the bold", "\n**ap\nproved**\n"),
                ("a soft hyphen inside the bold", "\n**ma­ture**\n")):
            with self.subTest(control="a verdict posture with %s is refused by "
                                      "the verdict inventory" % name):
                self.assertTrue([x for x in carriage_violations(text + route, h)
                                 if x.startswith("a verdict form")])
        with self.subTest(fact="the carried tables are read from the published "
                               "assessment's committed bytes, and a planted "
                               "assessment is not what is trusted"):
            planted = assessment_text().replace(
                "**outstanding in lawful resting state** — no deliverable",
                "**discharged** — no deliverable", 1)
            self.assertNotEqual(planted, assessment_text())
            self.assertTrue(carried_violations(text, planted))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec")
                self.assertEqual(carriage_violations(text, hh), [])
                self.assertTrue(carriage_violations(
                    text.replace(first_inv + "\n", "", 1), hh))

        with self.subTest(control="an inventory entry without a local condition "
                                  "is refused"):
            self.assertEqual(unconditioned_inventory(), [])
            self.assertTrue(unconditioned_inventory(
                CONDITIONED + ("**W8 closes complete, not perfect.**",)))
            self.assertEqual(unconditioned_inventory(("x effective per the status "
                                                      "line y",)), [])


class CC2_NonAuthorisations(unittest.TestCase):
    def test_cc2_record_carries_its_non_authorisations(self):
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
                ("the nothing-beyond-closure line dropped", text.replace(
                    NON_AUTH_LINES[16] + "\n", "", 1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[16] + "\n" + neutral
                              + "\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[16] + "\n    This landing "
                              "authorises contact.\n\n"
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


class CC3_NoExposure(unittest.TestCase):
    def test_cc3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr", "auth")
        text = read(RECORD).decode("utf-8")
        exempt = ((succession_row_line(h),) + tuple(basis_row_lines())
                  + tuple(law_row_lines()) + tuple(file_row_lines()))
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-CR"]["role"] + " " + by_id["W8-CR"]["title"]
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
            digest = BASIS_ROWS[0][5]
            altered = line.replace(digest, digest[:7] + ("0" if digest[7] != "0" else "1")
                                   + digest[8:], 1)
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


class CC4_FixedArtefactsAndBasis(unittest.TestCase):
    def test_cc4_every_home_and_record_unchanged_and_provenance_resolving(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
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
        with self.subTest(fact="the registered records cover the assessment, the "
                               "brief, the decision, the finding and the W7 closure"):
            for p in (ASSESSMENT_RECORD, BRIEF,
                      "docs/phases/W8-D6-contact-decision-record.md",
                      "docs/phases/W8-D5-adequacy-finding-record.md",
                      "docs/phases/W7-closure-record.md"):
                self.assertIn(p, records)
            self.assertNotIn(REGISTRY, records)
        text = read(RECORD).decode("utf-8")
        with self.subTest(fact="the provenance tables read whole are the trusted "
                               "rows, each resolving, each identity registered, and "
                               "every named identity and path provenanced"):
            self.assertEqual(basis_table_violations(text), [])
            self.assertEqual(basis_object_violations(), [])
            idents = [r[1] for r in BASIS_ROWS]
            self.assertEqual(len(set(idents)), len(idents))
            self.assertIn("W8-D7-CAR", idents)
            self.assertIn("W8-D7-CAB", idents)
            self.assertEqual(files_table_violations(text), [])
            self.assertEqual(file_object_violations(), [])
            self.assertEqual(named_path_violations(text), [])
            self.assertEqual(named_identity_violations(text), [])
        with self.subTest(fact="the law table is its trusted rows, each resolving "
                               "and each the published assessment's own row, the "
                               "directly read laws exactly the executed two, and "
                               "every cited law provenanced"):
            self.assertEqual(laws_table_violations(text), [])
            self.assertEqual(law_object_violations(), [])
            self.assertEqual(direct_law_violations(), [])
            self.assertEqual(cited_law_violations(text), [])
            self.assertEqual(len(LAW_ROWS), 14)
            self.assertEqual(len(assessment_source_rows()), 62)
        reveal_file = homes["governance/validation-reveal"][0]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed assessment record": (
                    dict(now, **{ASSESSMENT_RECORD: now[ASSESSMENT_RECORD] + b" "}),
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
                self.assertTrue(basis_table_violations(mutated))
        good = BASIS_ROWS[0]
        for name, rows in (("a wrong object", ((good[0], good[1], good[2],
                                                 good[3], "0" * 40, good[5]),)),
                           ("a wrong digest", ((good[0], good[1], good[2],
                                                 good[3], good[4],
                                                 "sha256:" + "0" * 64),)),
                           ("an identity not registered at the path",
                            ((good[0], "W8-D7-SNT") + good[2:],)),
                           ("a gap in the numbering", (good, BASIS_ROWS[2])),
                           ("a provenance commit that is not the last change",
                            ((good[0], good[1], good[2], W7_CLOSURE, good[4],
                              good[5]),))):
            with self.subTest(object_control="%s is refused" % name):
                self.assertTrue(basis_object_violations(rows))
        fline = file_row_lines()[0]
        for name, mutated in (
                ("a dropped file-provenance row", text.replace(fline + "\n", "", 1)),
                ("an altered file commit", text.replace(
                    fline, fline.replace(FILE_ROWS[0][2], "0" * 40, 1), 1))):
            with self.subTest(file_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(files_table_violations(mutated))
        with self.subTest(file_control="a repository file named without a row is "
                                       "refused"):
            self.assertTrue(named_path_violations(
                text + "\nSee `tests/test_w6_review_surface.py`.\n"))
        with self.subTest(identity_control="a registered identity named without a "
                                           "row is refused"):
            self.assertTrue(named_identity_violations(text + "\nSee `W6-D2-CD`.\n"))
            self.assertEqual(named_identity_violations(text + "\nSee `W8-D7-SNT`.\n"),
                             [])
        fgood = FILE_ROWS[0]
        for name, rows in (
                ("a wrong file object", ((fgood[0], fgood[1], fgood[2], "0" * 40,
                                          fgood[4]),)),
                ("a cited commit that is not the last change",
                 ((fgood[0], fgood[1], W7_CLOSURE, fgood[3], fgood[4]),)),
                ("a registered path in the file table",
                 ((fgood[0], BRIEF) + fgood[2:],))):
            with self.subTest(file_control="%s is refused" % name):
                self.assertTrue(file_object_violations(rows))

        lline = law_row_lines()[0]
        for name, mutated in (
                ("a dropped law row", text.replace(lline + "\n", "", 1)),
                ("an altered law commit", text.replace(
                    lline, lline.replace(LAW_ROWS[0][3], "0" * 40, 1), 1)),
                ("an altered law route", text.replace(
                    lline, lline.replace(law_route(LAW_ROWS[0][6], LAW_ROWS[0][7]),
                                         "relied on nowhere", 1), 1)),
                ("the lead's direct count altered", text.replace(
                    "Two were read directly", "Three were read directly", 1))):
            with self.subTest(law_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(laws_table_violations(mutated))
        with self.subTest(law_control="a law cited without a row is refused"):
            self.assertTrue(cited_law_violations(text + "\nSee ADR-0049.\n"))
        with self.subTest(law_control="a law row for a law the record does not cite "
                                      "is refused"):
            self.assertTrue(cited_law_violations(
                text, LAW_ROWS + ((15, "ADR-0049") + LAW_ROWS[0][2:],)))
        lgood = LAW_ROWS[0]
        via = next(r for r in LAW_ROWS if r[6] == "via")
        direct = next(r for r in LAW_ROWS if r[6] == "direct")
        for name, rows in (
                ("a wrong law object", (lgood[:4] + ("0" * 40,) + lgood[5:],)),
                ("a wrong law digest", (lgood[:5] + ("sha256:" + "0" * 64,)
                                        + lgood[6:],)),
                ("a law commit that is not the last change",
                 (lgood[:3] + (W7_CLOSURE,) + lgood[4:],)),
                ("a law marked read directly that this module does not execute",
                 ((1,) + via[1:6] + ("direct", via[7]),)),
                ("an executed law marked relied on",
                 ((1,) + direct[1:6] + ("via", direct[7]),)),
                ("an unknown route", ((1,) + via[1:6] + ("elsewhere", via[7]),)),
                ("a wrong assessment row", ((1,) + via[1:7] + (via[7] + 1,),)),
                ("a law not registered at its path",
                 ((lgood[0], "W8-D7-SNT") + lgood[2:],)),
                ("a gap in the law numbering", (lgood, LAW_ROWS[2]))):
            with self.subTest(law_control="%s is refused" % name):
                self.assertTrue(law_object_violations(rows))
        for name, rows in (
                ("the executed laws not both marked direct",
                 tuple(r[:6] + ("via", r[7]) for r in LAW_ROWS)),
                ("a third law marked direct",
                 tuple(r[:6] + ("direct", r[7]) if r[6] == "via" and r is via else r
                       for r in LAW_ROWS))):
            with self.subTest(law_control="%s is refused" % name):
                self.assertTrue(direct_law_violations(rows))


class CC5_Successions(unittest.TestCase):
    def test_cc5_cb7_succession_exact_and_the_chain_of_claims_holds(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rec")
        record = read(RECORD).decode("utf-8")
        present = read(ASSESSMENT).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[ASSESSMENT][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + ASSESSMENT)
                             .strip(), PREIMAGE[ASSESSMENT][2])
        with self.subTest(exact_succession=PREIMAGE[ASSESSMENT][0]):
            self.assertEqual(succession_violations(present, record, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[ASSESSMENT][1])
        with self.subTest(fact="R9's sentence, constants and tuple unchanged; the "
                               "session-recovery and opening modules untouched"):
            self.assertEqual(h.rec.R9_REVEAL, R9_SENTENCE)
            self.assertEqual(h.rec.LATER, ("W8-D4", "W8-D5", "W8-D6", "W8-D7"))
            for rel in (RECOVERY, OPENING):
                self.assertEqual(_sha(read(rel)), _sha(committed(BASELINE, rel)))
        with self.subTest(fact="the succeeded modules' claims hold at their own "
                               "commits"):
            self.assertEqual(historical_claim_violations(), [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[ASSESSMENT][1:]),
                "the live read restored beside the historical one": (
                    present.replace(SITES[ASSESSMENT][2][2],
                                    SITES[ASSESSMENT][2][2]
                                    + SITES[ASSESSMENT][2][1], 1), None),
                "the anchor collapsed onto the W8-D7 opening": (
                    present.replace(D7B_LINE, 'D7B_LANDING = "%s"\n'
                                    % D7A_LANDING, 1), None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[ASSESSMENT] + (("CB7", first,
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
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rec")
                self.assertEqual(succession_violations(present, record, hh), [])


class CC6_RegistryAndBoard(unittest.TestCase):
    def test_cc6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = cr_state(read(RECORD).decode("utf-8"), h)
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
            self.assertEqual(board_pre.count(HEAD_BEFORE), 1)
            self.assertEqual(board_pre.count(CLOSED_BEFORE), 1)
            self.assertIsNotNone(car_row_line(board_pre))
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


class CC7_EntrySet(unittest.TestCase):
    def test_cc7_registered_and_the_w8_d7_entry_set_is_the_three_records(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        record = read(RECORD).decode("utf-8")
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, record, h), [])
        with self.subTest(fact="at the baseline the W8-D7 entries were the "
                               "brief's and the assessment's"):
            self.assertEqual({e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] == "W8-D7"}, set(D7_ENTRIES_AT_BASELINE))
        # Succeeded at the W9 runway's landing (W9-AR): the W8-D7 entry set
        # and the no-later-phase limb stay proven at this landing's own
        # published commit, D7C_LANDING.
        at_landing = json.loads(committed(D7C_LANDING, REGISTRY))["entries"]
        with self.subTest(fact="the W8-D7 entries were the brief's, the "
                               "assessment's and this record's, and no later "
                               "phase's entry existed, at this landing's "
                               "published commit"):
            self.assertEqual(commit, D7C_LANDING)
            self.assertEqual(entry_violations(at_landing, record, h), [])
        base = at_snapshot[-1]
        for name, entries in {
                "a fourth W8-D7 entry": at_snapshot + [dict(
                    base, id="W8-D7-SNT", deliverable="W8-D7")],
                "a wrong record hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                        if e["id"] == "W8-CR" else e
                                        for e in at_snapshot],
                "a wrong deliverable": [dict(e, deliverable="W8-D6")
                                        if e["id"] == "W8-CR" else e
                                        for e in at_snapshot],
                "the brief's entry altered": [dict(e, status="draft")
                                              if e["id"] == "W8-D7-CAB" else e
                                              for e in at_snapshot],
                "the assessment's entry altered": [dict(e, status="draft")
                                                   if e["id"] == "W8-D7-CAR" else e
                                                   for e in at_snapshot],
                "a later phase's entry": at_snapshot + [dict(
                    base, id="W9-D1-SNT", phase="W9",
                    deliverable="W9-D1")]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, record, h))


class CC8_Census(unittest.TestCase):
    def test_cc8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and the assessment module change "
                               "among the proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, ASSESSMENT})
        flat = _flat(read(RECORD).decode("utf-8"))
        with self.subTest(fact="the record names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?)\. No case", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {BRIEF},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


class CC9_EvidenceIntegrity(unittest.TestCase):
    def test_cc9_homes_w7_class_and_registry_hashes_identical(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        with self.subTest(fact="every home at its landing tree, the W7 home at "
                               "its seal, the W7 pins exact, every registry "
                               "hash recomputing"):
            self.assertEqual(integrity_violations(commit), [])
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
                    if e["id"] == "W8-D7-CAR" else e
                    for e in json.loads(read(REGISTRY))["entries"]])),
                ("a third null hash", dict(entries=[
                    dict(e, content_hash=None) if e["id"] == "W8-D7-CAR" else e
                    for e in json.loads(read(REGISTRY))["entries"]])),
                ("a resolver returning the pins verbatim is not what is "
                 "trusted", dict(tree_at=lambda rev, home: "0" * 40))):
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(integrity_violations(commit, **kwargs))


if __name__ == "__main__":
    unittest.main()
