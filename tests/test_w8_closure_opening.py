"""W8-D7-A — closure opening brief proofs (W8-D7-CAB, CA1–CA8).

The opening landing of W8-D7: the brief that fixes the closure question and
the bounded claim closure may test, the standard of closure without false
resolution and its seven postures, the three-landing programme, the pinned
governing sources, the inventories, audits and log the closure assessment
must publish, the human-review-only duties, the stop conditions, the scope
rule and the human decision points; and the one proof succession the
placeholder probe found a W8-D7 opening to need - ADR-0058's R9
later-deliverable limb, its sentence, constant and tuple unchanged, its last
absence proven at the W8-D6 completion. This module proves the brief's
carriage, its closed posture list, its closed programme table and the
absence of closure-presuming wording, of the withdrawn mechanical-conformance
formula and of any universal session or reveal claim; its
non-authorisations; its exposure
limits, with the one trusted succession row and the trusted source rows as
the only digest exemptions; that every case home, register, revealed record
and every registered record at the baseline is byte-unchanged and that the
source table is exactly its trusted rows resolving to their pinned objects;
the exact R9 succession and its closed table; and the exact registry, board
and census - each with planted-mutant or negative controls. Closed
validators compare against trusted expected values held here and refuse
unrecognised material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the brief
afterwards - and executes the helpers it relies on from that snapshot's
bytes, in a private namespace. CA7's W8-D7 entry set was the one
present-state gate, as the W8-D4, W8-D5 and W8-D6 openings' were, until
the assessment landing (W8-D7-CAR) succeeded it to a historical proof at
this landing's own published commit. The residual live reach is
disclosed exactly: each snapshot-executed helper module imports, at its own
top level, the live modules it aliases for the fixed-law values it reads
from them, and no more independence than that is claimed.

CA1's numbered-item pattern admits exactly CommonMark's ordered marker in
this brief's form - one to nine ASCII digits, a full stop and a space - so
that a line a Markdown reader folds into a protected item is never taken
for the next item's boundary. CA1's closure-presumption scan sets aside the
pinned drafting-target line, whose exact text the closed carriage already
proves, and the runway's own quoted sentence, and reads everything else
through a bounded fold - emphasis and code marks and the invisible code
points removed, every whitespace run one space, case folded - so that
ordinary formatting hides no inventoried phrase. Conformance to that
bounded inventory is never proof that arbitrary prose draws no conclusion.

CA3 reads every surface as logical prose paragraphs - blocks parted by
blank lines, empty or SPACE/TAB-only as CommonMark defines them, with every
whitespace run inside a block made one space - so that a soft line break,
continuation indentation or a separator line of no-break spaces, em spaces
or form feeds hides no figure or count from it. The paragraph helper is
locally owned and mirrors the published review-law helper; the exempt
exact rows survive the paragraph form unchanged.

This landing's derived public baseline is the published W8-D6 completion,
which is also the R9 succession's historical anchor, D6_COMPLETION, as the
W8-D5 completion was the W8-D6 opening's; CA5 proves the two equal, proves
that no W8-D7 entry existed at it, and proves that the succeeded module
carries the W8-D7 absence as a historical proof and no live
later-deliverable limb.

CA2 reads section 19 as one whole block - heading, blank separator,
introducing item, the sixteen non-authorisations, blank separator, closing
sentence and trailing separator, in that order and nothing else - so that
unmarked prose, a permission sentence, a differently indented bullet or a
line at either edge of the block is refused rather than skipped.

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity,
schema literal or method label as a literal, and no disposition token. It
declares no closure and assigns no posture.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: that W8 may close, or any closure posture; that any
inventory is complete; anything about the instrument's maturity,
adequacy, readiness, safety or usefulness; anything about any model, case,
disposition, divergence or reviewer; that any model was or was not
contacted; that any ADR-0047 precondition moved; or that any later phase
may open.
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

# The published, remotely verified W8-D6 completion: this landing's sole
# parent and the commit every pre-image below is read from.
BASELINE = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"
# The R9 succession's historical anchor: the W8-D6 completion, which is this
# landing's baseline (as the W8-D5 completion was the W8-D6 opening's).
D6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"
D5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"
D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"
D3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"
D6A_LANDING = "753e6abea8d67a16332799af615fdcfa4aefa7b9"
W7_CLOSURE = "7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3"
# Succeeded at the W8-D7 assessment landing (W8-D7-CAR; W8-D7-CAB section
# 15, item 60): CA7's W8-D7 entry set and its no-later-phase limb stay
# proven at this landing's own published commit; the live gates move to
# the assessment landing's proof module.
D7A_LANDING = "cf2012669b97b323cdbfb182bc10865d444c79c1"

BRIEF = "docs/phases/W8-D7-A-closure-authorisation-brief.md"
SELF_REL = "tests/test_w8_closure_opening.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({BRIEF, SELF_REL, RECOVERY, REGISTRY, BOARD})
D7_ENTRIES = frozenset({"W8-D7-CAB"})
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
    RECOVERY: ("session-recovery module",
               "sha256:25bc3f70d043c854471748bdf6a6c1fe6e7864ce047007df19348dbd66293261",
               "055f57d7e07311f6a6224fc7e173d2c8bbe4dd1f"),
    REGISTRY: ("registry",
               "sha256:318a933ad727b8a38c5ba6110af216967a9f3aed62d5dbaa78eeb2ce901b0056",
               "a5ddb0cce399801134bb319c14078e24d7444477"),
    BOARD: ("board",
            "sha256:957f0756629669d9403fddfd4447f13c0c4bae2bfa54050379af16cf4de9be48",
            "83349eccb9aa71010ec6a1ce376a6fe27a891598"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {RECOVERY: ("sha256:dbedab0e9f9d5e381c2770914ee056cb4d05695ccd9afd30cc54dcb52e976276", "3ec9548ad2b334a2ac927dfc501d9720cedc819e")}

# ------------------------------------------ the one succession: ADR-0058 R9
SITES = {
    RECOVERY: (
        ('R9',
         '# Succeeded again at the W8-D6 opening (W8-D6-CDB section 9): the\n# absence of every W8-D6 and W8-D7 entry stays proven at the W8-D5\n# completion.\nD5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"\n',
         '# Succeeded again at the W8-D6 opening (W8-D6-CDB section 9): the\n# absence of every W8-D6 and W8-D7 entry stays proven at the W8-D5\n# completion.\nD5_COMPLETION = "2aa2c75d20363ca7e54095f49b328bdd4db1350a"\n# Succeeded again at the W8-D7 opening (W8-D7-CAB section 15): the\n# absence of every W8-D7 entry stays proven at the W8-D6 completion.\nD6_COMPLETION = "e76be12b537f67a1041422ee73c22cbbfcf8b8c5"\n'),
        ('R9',
         '        with self.subTest(fact="no registry entry opens W8-D7"):\n            self.assertEqual([e["id"] for e in entries\n                              if e["deliverable"] in LATER[3:]], [])\n',
         '        # Succeeded again at the W8-D7 opening landing: the absence of\n        # every W8-D7 entry stays proven at the W8-D6 completion commit;\n        # W8-D7\'s entry set moves to that landing\'s own proof module. No\n        # deliverable later than W8-D7 exists in the runway\'s table, so\n        # no live later-deliverable limb remains here.\n        with self.subTest(fact="no registry entry opened W8-D7 at the "\n                               "W8-D6 completion"):\n            at_d6 = json.loads(packet.committed_object_bytes(\n                ROOT, D6_COMPLETION, "governance/registry.json"))[\n                "entries"]\n            self.assertEqual([e["id"] for e in at_d6\n                              if e["deliverable"] in LATER[3:]], [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_LINE = 'R9_REVEAL = "%s"\n' % R9_SENTENCE
LATER_LINE = 'LATER = ("W8-D4", "W8-D5", "W8-D6", "W8-D7")\n'

# -------------------------------------------------------------- the sources
# Trusted rows of the brief's section 5 table: (number, identity, path,
# commit at which the path's published bytes last changed, blob, raw
# SHA-256 of the committed bytes). Every object is byte-identical at
# BASELINE.
BASIS_SECTION = "## 5. The governing sources, pinned"
BASIS_HEADER = "| # | Identity | Published path | Commit | Object | Raw SHA-256 |"
BASIS_SEPARATOR = "|---|---|---|---|---|---|"
BASIS_ROWS = (
    (1, 'W8-AR', 'docs/phases/W8-runway-generative-evaluation-maturity.md',
     '117a192091bfafa80cb3f6ae567b63204b6c7676', 'da34be5dee7db4a94b4276f4024dd48e3076883a',
     'sha256:fda68f9d1e69c166587cfb746d7d1830b39ea99d9c4c6a9129a0b75d34eba24e'),
    (2, 'W7-CR', 'docs/phases/W7-closure-record.md',
     '7d4ff5792b20a037fdb73ec6a2c5813d744d5bf3', 'f57ea174237205f2d4e0783f48469ab84abe5c97',
     'sha256:8086966f2355c59d2c8ea34593d177446cac0ec9707977b27d186b7e0d96200a'),
    (3, 'W7-D7-CAR', 'docs/phases/W7-D7-B-closure-assessment-record.md',
     '03ca823b5accfc5616b2e22ff642066882fe5274', '318a3bc5b8d79e666e4829b3068e9e7fbbf717d3',
     'sha256:8c2a5412b44b594bd2133321f47fcc0a2c209082e5877091a486dd5cdb21860c'),
    (4, 'W7-D7-CAB', 'docs/phases/W7-D7-A-closure-authorisation-brief.md',
     '1d4b19c45c4e12e777de654358d2c4a7562cd60a', '7d1b609764ca3b8ad5171a113477b5df4a32cd1f',
     'sha256:76b6e0c45d3e6384736d4aabbd7db3ff0923d36d33d188b37da2a9ab8fb1f080'),
    (5, 'W6-D6-CAB', 'docs/phases/W6-D6-A-closure-authorisation-brief.md',
     '8a764e92a04b8fbcabb2b2fba1eb0b7f3646c3da', '535d2443ab1f613691022a7f6590c14c27619fd0',
     'sha256:2e4098691c6fe45772855e49d74464ac8e45dab6fedb4779319178d2a30da57f'),
    (6, 'ADR-0047', 'docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md',
     '02b58ccc9f37f46a72b79b9e61e6028057d313b7', '5f1fb5581a98ea8d9f03d97ad39a4bc39158c079',
     'sha256:63f8c84fe2a3235d69340e4bcbcb4cd1d2497ff46b89876ac128b097f6c72a35'),
    (7, 'ADR-0052', 'docs/decisions/0052-exclusion-list-conformance-p4-decomposition.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', 'e3d917edbf7b0cca131bbd5e0a5884e696bb0246',
     'sha256:46299e137b86a91bf76e964017a103e03da5b3d71830b86390d369e7b1327050'),
    (8, 'ADR-0046', 'docs/decisions/0046-synthetic-only-public-law-and-adoption-boundary.md',
     '953efc928867f9a05321065b7ef4cc6515a09b3d', '14c1208e81fb59763a1f78ee3676276149b75b08',
     'sha256:b2bac9e3bbf3fd3cd3991c174671f2dbbbde3832363ef3df93cb67cde3de5270'),
    (9, 'ADR-0051', 'docs/decisions/0051-model-boundary-no-public-contact.md',
     'e1dd86d561e458babdcfa56e6923aba9fb6f63b2', '2800a8260fc4379133fce418ea3e20fe5929e607',
     'sha256:a1af46b27a52fed4a1bb0f30c9b449148ba8178ddffddbcc76a1acbb634efda6'),
    (10, 'ADR-0054', 'docs/decisions/0054-generative-evaluation-maturity-doctrine.md',
     '6e9e0f155944bea3117b82a5b4216ce6c50abaa4', '77c4b4802ea2bc4a80fe2190d8b1dfb69ca30e43',
     'sha256:4cd552df3be6ad7e0e06b4c54ea2beb11ee85dc1e5e6fe61a2e33be3d1b4ecbd'),
    (11, 'ADR-0056', 'docs/decisions/0056-public-repository-identity-attribution-boundary.md',
     '797e839ac9484a04ac84e1f7bb5f84851f539579', '891e737e32960bae4fc48d6852bf935ffdb33d85',
     'sha256:ed0f3ab7e5828c2c7be408b2712a491f68d635bb80efc42e2328d83792a3084d'),
    (12, 'ADR-0058', 'docs/decisions/0058-w8-d3-session-recovery-law.md',
     '897f0b14a66ee956bd9fe36e63975b04d5dc9663', '5f8f0786b1bd8091696fe45cb05a388bb776b8b6',
     'sha256:6291da0206c576be10c6c5eea8a1e71490f836e20430663a8eb5038f49877cd3'),
    (13, 'ADR-0059', 'docs/decisions/0059-w8-supplementary-corpus-recovery-authority.md',
     '2bb87a308d4cc1ce795869bb94370d3bdc75ae0e', 'd06e2f56a25ee80abd678bfe706721ba7df8e70d',
     'sha256:05dc46e0b9b17d96f316aa5dcb545c5ba7e99031cdc169277d6ee12abcf06b59'),
    (14, 'ADR-0061', 'docs/decisions/0061-w8-evidence-adequacy-review-law.md',
     '18d6230b5f7281577c18892dd7b95e9448f310c2', 'aec015d014c098b183deeb119a6c6293f4e4b6bb',
     'sha256:b81af71545cfc21d3311275110e66dc0768d87d24f1954138e95783773cf95d9'),
    (15, 'W8-D3-CCR', 'docs/phases/W8-D3-calibration-completion-record.md',
     '3c34246a5b6989aaa6c5e19621964fa0c7799cdd', 'ae3c662051ea716eee43076b10034868cbb1da8b',
     'sha256:b6e958ba42c59b5c45774eb5bbc66e5a1f8a8f19100f1b580c218e2509addf82'),
    (16, 'W8-D4-CPR', 'docs/phases/W8-D4-completion-record.md',
     'ce78a242df25898d90debee9513bdce7e511471b', '14e49308ed63a4411400f769f25fda8095d74efb',
     'sha256:dd8a577de367946f5a7f5331a06a6a8df49fbe1b899dd6e6db2d527e62618471'),
    (17, 'W8-D5-AFR', 'docs/phases/W8-D5-adequacy-finding-record.md',
     '2aa2c75d20363ca7e54095f49b328bdd4db1350a', '9fbd1016bb58ae06d9e557ebd281f707f54b8fc5',
     'sha256:197254b69161aacef79dbb93c86939c4cc1b82e9cc39ac2fa0584207ea6cc558'),
    (18, 'W8-D6-CDB', 'docs/phases/W8-D6-contact-decision-brief.md',
     '753e6abea8d67a16332799af615fdcfa4aefa7b9', 'ddde7b3553b5f21dc929010c5c90dba701a70980',
     'sha256:034483363a210df7a736749d5f30e6cf68a6e57c77b7b07001f3770f8567a196'),
    (19, 'W8-D6-CDR', 'docs/phases/W8-D6-contact-decision-record.md',
     'e76be12b537f67a1041422ee73c22cbbfcf8b8c5', '842472148111e78abd9d7fc7273fa1b19426dc75',
     'sha256:c7381ac0bbfeac59b94057b9de359fdd072cc2003e1f06179e833492be71bfa3'),
    (20, 'W8-DER', 'docs/phases/W8-documentation-erratum.md',
     '6704649ed80c27112c00c14093c82645e8d090cf', '371f80be2d1abca01b0ff7fa0da9065c2c63e1bc',
     'sha256:0eec519ea3d1d369bfd3f8231d09c8f09a24dde9749fa59480f900d5da45fd07'),
)

# --------------------------------------------------------------- carriage
RUNWAY_SENTENCE = ("Whole-phase source re-derivation and closure under the "
                   "discipline established through W2–W7")
REQUIRED = (
    "W8-D7 opens for closure work only, through the landing programme of "
    "section 4. This brief does not close W8.",
    "No later phase is opened, designed, scheduled or named as assigned",
    "Closure of W8 exists only after the W8 closure record of section 4 has "
    "itself been accepted, published and independently remote-verified.",
    "Completion of the governed programme and a conclusion about the "
    "instrument are different propositions.",
    "The claim is about governed handling",
    "The W7 closure's contact sentence is not available to W8 in W7's form.",
    "no W8 act prepared, authorised or performed model contact, and no W8 "
    "record classifies any exchange.",
    "if and only if each is named, classified, and never represented as "
    "resolved.",
    "Phase completion and universal resolution are not the same proposition.",
    "The W8-D5 finding is undetermined, complete and fixed.",
    "The W8-D6 decision is contact, as the human authority's stated choice, "
    "and it authorises nothing.",
    "The reported authority gap stays reported.",
    "An outstanding conditional gate is not a defect merely because its "
    "triggering act did not occur.",
    "A recorded divergence stays recorded and undiagnosed.",
    "This is the standing non-diagnosis condition, and it survives closure.",
    "The void attempt stays void and the reservation stays.",
    "The retained records stay sealed.",
    "Historical facts are preserved at full size.",
    "The inherited W7 inventory travels item-for-item.",
    "A derivative is reconciled to its source, never the reverse.",
    "Phase reasoning explains; the inventory answers.",
    "no declaration of closure may appear in it",
    "Closure is effective on the closure record's publication and "
    "independent remote verification, and not before.",
    "W8-D7 reads its law and its carried-state authority only from published "
    "bytes at fixed commits",
    "The rows are pinned entry points, not a choice of which law governs.",
    "ceases to bind only by its own lawful amendment",
    "The rows pin the entry points; they bound neither the law nor the "
    "inventory.",
    "decomposed as ADR-0052 decomposes P4",
    "Each result is evidence only for the property it tests.",
    "no clean ordinary scan is evidence for either P4 clause",
    "belong to human review over the whole prohibition set",
    "No W8-D7 record states or implies that a mechanical run established "
    "conformance to any family.",
    "every case of the supplementary corpus in the lawful W8-D3 calibration "
    "session and every case of the validation corpus in the W8-D4 validation "
    "session",
    "the original corpus stands authored and published at its existing "
    "standing",
    "the two inherited discrepancies of items 20, 52 and 65 are "
    "accounted-for carried items, not a stop, while they stay named, "
    "unrepaired and unchanged",
    "to which rule 4's root-file condition does not apply",
    "A derivative board row is never evidence for the source it describes.",
    "The north star is assessed as the design intention the instrument was "
    "built toward and tested against, never as achieved.",
    "The assessment states exactly, and no more:",
    "P4a and P4b are carried separately, always",
    "Landing C requires a fresh closure-time P4b act by the human reviewer "
    "against the exact final closure candidate, across all eleven families "
    "of ADR-0046 decision 11",
    "A proof being green is evidence only for the property the proof "
    "actually tests.",
    "This review is not inferred from a green mechanical scan and is not a "
    "machine act.",
    "W8-D7 must not rewrite W8 history to make closure simpler.",
    "Only facts supportable from public repository records may enter the "
    "closure log.",
    "W8-D7 records both discrepancies without repairing either.",
    "No future phase is assigned an obligation merely because W8-D7 wants "
    "somewhere to put it.",
    "Closure authorises nothing beyond closure.",
    "The W8-D7 entry set moves to this landing's own proof module",
    "Each later landing runs a placeholder probe over every existing check "
    "before its census is fixed, and a refusal outside its authorised "
    "successions is a stop.",
    "Discovery is not scope authority.",
    "The root `README.md` and `docs/governance/registry.md` lie outside every "
    "W8-D7 census.",
    "Silence is never a decision, and a green suite is never an acceptance.",
    "Model contact and the closure of W8 remain outside this brief.",
    "Acceptance of this brief adopts these positions.",
    "drafting target only",
)
POSTURES = ("satisfied", "satisfied with named carried item",
            "outstanding in lawful resting state",
            "unresolved and bounded under named doctrine",
            "deferred under named doctrine",
            "external / outside repository authority",
            "unopened, named and not supplied")
POSTURE_LINES = (
    "**The permitted closure postures are exactly these**, the first six "
    "consuming the W6 formula and the published W7 posture language and the "
    "seventh consuming the published `W8-D6-CDR` instrument language, and the "
    "assessment uses no other:",
    "    - **satisfied**;",
    "    - **satisfied with named carried item**;",
    "    - **outstanding in lawful resting state**;",
    "    - **unresolved and bounded under named doctrine**;",
    "    - **deferred under named doctrine**;",
    "    - **external / outside repository authority**;",
    "    - **unopened, named and not supplied**.",
    "",
    "    **No item moves from an open posture to a closed one merely because "
    "the phase is closing.**",
)
SECTION_3 = "## 3. Closure without false resolution"
PROGRAMME_SECTION = "## 4. The W8-D7 programme — exactly three landings"
PROGRAMME_HEADER = "| Landing | Purpose | Anticipated paths |"
PROGRAMME_SEPARATOR = "|---|---|---|"
PROGRAMME_ROWS = (
    ["**D7-A** — this brief",
     "open W8-D7 and fix the closure question, the claim closure may test, "
     "the standard of closure without false resolution, the inventories, "
     "audits and log the assessment must publish, the human-review-only "
     "duties, the stop conditions and the proof successions",
     "this brief · its proof module · the R9 succession · the registry · "
     "the board"],
    ["**D7-B** — whole-phase closure assessment",
     "one evidence-gathering landing over the already-published W8 corpus, "
     "`W8-D7-CAR` at `docs/phases/W8-D7-B-closure-assessment-record.md`, "
     "carrying the complete inventories, assessments, audits and log of "
     "sections 6 to 13; **no declaration of closure may appear in it**",
     "the assessment record · its proof module · the authorised successions "
     "· the registry · the board"],
    ["**D7-C** — W8 closure record",
     "one final phase record, `W8-CR` at `docs/phases/W8-closure-record.md`, "
     "drafted from the published assessment and the live public repository "
     "state, declaring W8 complete and closed only on its own acceptance, "
     "publication and independent remote verification; W8-D7's completion",
     "the closure record · its proof module · the authorised successions · "
     "the registry · the board"],
)
DRAFTING_TARGET = (
    "> **W8 closes because the governance work assigned to the phase is "
    "complete and publicly evidenced, not because the question it was built "
    "to sharpen has been answered: the Wing fixed an evaluation doctrine "
    "before any case existed, authored its synthetic corpora under it, took "
    "the human authority's dispositions on the supplementary and validation "
    "corpora in sessions with the authoring records withheld, revealed every "
    "withheld record of those two session corpora byte-exact and compared "
    "case by case, left the original corpus published at its standing with "
    "its retained records sealed, left every divergence undiagnosed by "
    "decision, answered "
    "the evidence-adequacy question as undetermined, and recorded a contact "
    "decision that authorises nothing; no W8 act prepared, authorised or "
    "performed model contact, the published records classify no exchange and "
    "state neither way whether contact occurred, and every finding, decision, "
    "instrument, precondition, divergence, seam, carried item and historical "
    "unknown that remains open stands named at its true standing.**")
# A numbered item as this brief writes it and CommonMark admits it: one to
# nine ASCII digits, a full stop and a space. Unicode digits and longer
# runs are text, which a Markdown reader folds into the item above.
ITEM = re.compile(r"^[0-9]{1,9}\. ")
BOLD_BULLET = re.compile(r"^\s*[-*+]\s+\*\*")
# A CommonMark blank line: empty or SPACE/TAB only. A line of no-break
# spaces, em spaces or form feeds is not blank and parts no paragraph.
BLANK_LINE = re.compile(r"^[ \t]*$")
# Marks a reader folds away or a writer may vary when naming a phrase:
# emphasis and code marks, the zero-width and soft-hyphen code points. The
# fold removes them, makes every whitespace run one space and folds case -
# a bounded textual fold, never a Markdown parser.
FOLDED_MARKS = re.compile("[*_`~\u200b\u200c\u200d\u2060\ufeff\u00ad]")
# Wording that would presume the closure or a conclusion about the
# instrument, a model or adoption; none may appear anywhere in the brief
# outside the pinned drafting-target line and the runway's quoted sentence.
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
# The formula the architect's r1 review withdrew: a mechanical surface, a
# scan or a guard said to establish the absence or conformance of a
# prohibited family (ADR-0052 decisions 3, 4, 6 and 8). None may appear
# anywhere in the brief, the pinned drafting target included.
WITHDRAWN = ("its mechanical surface establishes", "the mechanical surface "
             "establishes", "mechanically establishes that no", "p4 green",
             "mechanical run established complete", "scan establishes that",
             "a green p4a establishes", "p4a establishes",
             "scan established that", "establishes complete exclusion-list "
             "conformance", "established complete exclusion-list conformance")
# Universal session or reveal claims the r1 review found false for the
# original corpus (ADR-0059 decisions 9, 10 and 19; ADR-0058 decision 5):
# every lawful session and reveal is bounded to its own corpus, and none
# of these forms may appear anywhere in the brief, the drafting target
# included.
UNIVERSAL = ("every case of each corpus", "every case of every corpus",
             "every withheld record was revealed", "revealed every withheld "
             "record byte-exact", "every retained record was revealed",
             "revealed every retained record", "every withheld record of each "
             "corpus", "every withheld record of every corpus", "all withheld "
             "records were revealed", "revealed all withheld records",
             "revealed every withheld record as exact")
WITHHELD = ("This brief does not close W8", "contacts no model",
            "No later phase is opened",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "the closure itself, at this landing",
            "any selection of a provider, route or model class, or any opening "
            "or narrowing of the hosted class",
            "any Tier F crossing, any amendment of ADR-0051, any implementation "
            "brief or any performing deliverable",
            "any reopening, re-weighing or amendment of the W8-D5 finding, or "
            "any second adequacy finding",
            "any reopening, re-weighing or amendment of the W8-D6 decision",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record",
            "any repair of `docs/governance/registry.md` or of the root "
            "`README.md`",
            "any later phase's runway, brief, deliverable or gate")
SUCCESSION_SECTION = "## 15. Proof successions, each authorised only in its own landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
SECTION_REF = re.compile(r"§\d+(?:\.\d+)*")

# --------------------------------------- board and registry: authorised edits
CAB_LINK = ("([`W8-D7-A-closure-authorisation-brief.md`]"
            "(W8-D7-A-closure-authorisation-brief.md))")
CAB_STATUS_TAIL = (
    "W8-D7 for closure work only, as three landings behind their own "
    "acceptances: this brief, a whole-phase closure assessment that declares "
    "no closure, and the W8 closure record, effective only on its own "
    "publication and independent remote verification. It fixes the closure "
    "question and the claim closure may test — completion of the governed "
    "programme, never a conclusion about the instrument's maturity, "
    "readiness, safety or usefulness or about any adoption; the standard of "
    "closure without false resolution and its seven postures; the "
    "inventories, audits and log the assessment must publish, every one "
    "re-derived from published source and never from a board row or session "
    "memory; the human-review-only duties, a fresh closure-time P4b act at "
    "the closure record among them; the stop conditions; and what W8-D7 may "
    "not become. The W8-D5 finding stays undetermined as recorded, the W8-D6 "
    "decision stays a decision that authorises nothing, every separate "
    "instrument stays unopened, every precondition stays unchanged, every "
    "divergence stays undiagnosed and every inherited item stays named and "
    "unresolved; the stale root README and registry rendering are named and "
    "not repaired; no later phase is opened; no model is contacted.")
CAB_STATUS = {
    "draft": ("**A draft W8-D7 opening brief, `W8-D7-CAB`, is before the "
              "human reviewer** " + CAB_LINK + ": if accepted, it would open "
              + CAB_STATUS_TAIL),
    "accepted": ("**The W8-D7 opening brief, `W8-D7-CAB`, is accepted** "
                 + CAB_LINK + " — accepted %s: it opens " + CAB_STATUS_TAIL),
}
CAB_ROW = ("| W8-D7 — Closure (opening brief, W8-D7-CAB) | "
           "[`W8-D7-A-closure-authorisation-brief.md`]"
           "(W8-D7-A-closure-authorisation-brief.md) | ")
CAB_ROW_BODY = (
    "Tier J: **opens W8-D7 for closure work only** — a three-landing closure "
    "programme behind its own acceptances: this brief, a whole-phase closure "
    "assessment that declares no closure, and the W8 closure record, "
    "effective only on its own publication and independent remote "
    "verification. Closure is tested as completion of the governed programme "
    "under the W2–W7 standard of closure without false resolution, never as "
    "a conclusion about the instrument's maturity, readiness, safety or "
    "usefulness or about any adoption; every inventory is re-derived from "
    "published source. ADR-0058's R9 later-deliverable limb succeeds at this "
    "landing, its sentence, constant and tuple unchanged, the W8-D6 "
    "completion kept as its historical anchor and no live later-deliverable "
    "limb remaining; the W8-D7 entry set moves to this brief's module. **No "
    "closure, contact capability, diagnosis or custody access; the W8-D5 "
    "finding stays undetermined as recorded; the W8-D6 decision stays a "
    "decision that authorises nothing; every separate instrument stays "
    "unopened; no later phase opens; no model contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**" + R9_SENTENCE + " W8-D7 remains closed behind its own "
                 "brief.**")
# The closing sentence this landing leaves, by state: a draft moves
# nothing; an accepted brief opens W8-D7 and nothing more.
CLOSED_AFTER = {
    "draft": ("**" + R9_SENTENCE + " W8-D7 remains closed behind its own "
              "brief; W8 is not closed.**"),
    "accepted": ("**" + R9_SENTENCE + " W8-D7 is open for closure work only; "
                 "W8 is not closed.**"),
}
# The decision record's status sentence closes directly before the retained
# R9 sentence, and its row is the table's last.
CDR_CLOSE = "is selected and no precondition moves. "
BOARD_STATUS_ANCHOR = CDR_CLOSE + CLOSED_BEFORE
BOARD_ROW_ANCHOR = ("**No contact, provider, route, diagnosis or custody "
                    "access; the W8-D5 finding stays as recorded; W8-D7 stays "
                    "closed; no model contact.** |\n")
CAB_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
CAB_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D7-CAB", "path": BRIEF, "type": "phase-brief",
    "title": "W8-D7 - Closure: Opening Brief",
    "role": (
        "The opening brief of W8-D7, the closure, under the W8 runway: opens "
        "W8-D7 for closure work only through a three-landing programme - "
        "this brief, a whole-phase closure assessment that declares no "
        "closure, and the W8 closure record, effective only on its own "
        "publication and independent remote verification. Fixes the closure "
        "question and the bounded claim closure may test - that W8 completed "
        "the governance work its accepted runway and briefs assigned to it, "
        "never a conclusion about the instrument's maturity, adequacy, "
        "readiness, safety or usefulness, about any model or about any "
        "adoption; carries the W2 to W7 standard of closure without false "
        "resolution with seven permitted postures; carries the W8-D5 finding "
        "undetermined as recorded, the W8-D6 decision as a decision that "
        "authorises nothing with its separate instruments named, not "
        "supplied and unopened, every ADR-0047 precondition unchanged with "
        "precondition 3 outstanding in its lawful resting state, every "
        "recorded divergence undiagnosed, ADR-0058's void-attempt exclusion "
        "and Part F reservation, the retained records sealed, the public "
        "history preserved, the inherited W7 inventory item-for-item and the "
        "two stale derivatives named and not repaired; fixes the inventories, "
        "assessments, audits and log the assessment must publish from "
        "published source, the P4a and P4b carriage with a fresh closure-time "
        "P4b act at the closure record, the stop conditions, the landing "
        "scope and the human decision points; pins twenty governing entry "
        "points, every effective governing law remaining binding. Carries "
        "ADR-0058's R9 later-deliverable succession at "
        "its own landing, R9's sentence, constant and tuple unchanged and the "
        "W8-D6 completion kept as its historical anchor, the W8-D7 entry set "
        "moving to this brief's module, with proof obligations CA1 to CA8. "
        "Declares no closure, diagnoses nothing, reads no custody, opens no "
        "later phase and contacts no model."),
    "depends_on": ["W8-AR", "W8-D6-CDB", "W8-D6-CDR", "W8-D5-EAB", "ADR-0061",
                   "W8-D5-AFR", "W8-D4-IVB", "ADR-0060", "W8-D4-VRC",
                   "W8-D4-CPR", "W8-D3-SCB", "ADR-0057", "ADR-0058",
                   "W8-D3-CCR", "ADR-0059", "W8-S1-SCR", "W8-D2-DIB",
                   "ADR-0055", "W8-D2-DIC", "W8-D2-CBC", "W8-D1-EDB",
                   "ADR-0054", "ADR-0056", "W8-DER", "W8-HPC", "W8-HAC",
                   "W8-CHC", "ADR-0047", "ADR-0046", "ADR-0052", "ADR-0051",
                   "ADR-0033", "ADR-0034", "W7-CR", "W7-D7-CAB", "W7-D7-CAR",
                   "W6-D6-CAB"],
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


def prose_paragraphs(text):
    """Markdown's logical paragraphs: blocks parted by blank lines - empty or
    SPACE/TAB-only, as CommonMark defines a blank line - with every run of
    whitespace inside a block made one space: a soft line break,
    continuation indentation, a tab, a no-break space, an em space or a
    form feed among them. Nothing is joined across a blank line, so a
    heading stays apart from the item below it. Locally owned; the same
    form the published review-law module gives its EL3."""
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


def d7a_snapshot():
    """(commit, violations). Before this landing's commit exists the
    snapshot is the candidate over a HEAD that must be BASELINE; afterwards
    it is the one commit that added the brief, whose sole parent must be
    BASELINE."""
    adds = _git("log", "--diff-filter=A", "--format=%H", "--", BRIEF).split()
    if not adds:
        head = _git("rev-parse", "HEAD").strip()
        return None, ([] if head == BASELINE else
                      ["uncommitted candidate is not over the baseline"])
    if len(adds) != 1:
        return None, ["the brief was added more than once"]
    parents = _git("rev-list", "--parents", "-n", "1", adds[0]).split()[1:]
    if parents != [BASELINE]:
        return adds[0], ["the landing commit's sole parent is not the "
                         "baseline"]
    return adds[0], []


def snapshot_bytes(commit, rel):
    return (_lf((ROOT / rel).read_bytes()) if commit is None
            else committed(commit, rel))


def snapshot():
    commit, problems = d7a_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_cab_historical_" + Path(rel).stem,
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
    """ADR-0047 decision 18's chain block, found by its closing link. The
    chain's opening link is never written here: the W7 chain-integrity
    proof treats every occurrence of it as a reach that must carry the
    whole chain, and this module carries none."""
    ends = [line[2:] for line in baseline_text(CONTACT_LAW).split("\n")
            if line.startswith("> **")
            and line.endswith("no contact ≠ nothing proven.**")]
    return ends[0] if len(ends) == 1 else None


def closed_list_violations(text, lines, names, label, above=()):
    """A closed bold-bullet list carried as one numbered item: from the
    item's number up to the next numbered item, exactly `lines`, with
    numbered items directly either side, and each bold name once in the
    whole brief. `above` names the exact lines, besides a numbered item,
    that may lawfully sit directly above the item."""
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows)
             if ITEM.match(l) and l[ITEM.match(l).end():] == lines[0]]
    if len(heads) != 1:
        return ["the %s item is not present exactly once" % label]
    i = heads[0]
    end = next((j for j in range(i + 1, len(rows))
                if ITEM.match(rows[j]) or rows[j].startswith("#")), len(rows))
    v = []
    if tuple([lines[0]] + rows[i + 1:end]) != lines:
        v.append("the %s item is not exactly its members, each once" % label)
    if i == 0 or not (ITEM.match(rows[i - 1]) or rows[i - 1] in above):
        v.append("a line other than a numbered item abuts the %s item's top"
                 % label)
    if end >= len(rows) or not ITEM.match(rows[end]):
        v.append("the %s item is not followed directly by the next numbered "
                 "item" % label)
    v += ["%s %s is named %d times" % (label, n, text.count("**%s**" % n))
          for n in names if text.count("**%s**" % n) != 1]
    return v


def section_lines(text, heading):
    rows = text.split("\n")
    heads = [i for i, l in enumerate(rows) if l == heading]
    if len(heads) != 1:
        return None
    end = next((j for j in range(heads[0] + 1, len(rows))
                if rows[j].startswith("## ")), len(rows))
    return rows[heads[0]:end]


def programme_rows():
    return [list(r) for r in PROGRAMME_ROWS]


def programme_row_lines():
    return ["| " + " | ".join(r) + " |" for r in programme_rows()]


def programme_table_violations(text, h):
    rows, v = h.rev.closed_table(text, PROGRAMME_SECTION, PROGRAMME_HEADER,
                                 PROGRAMME_SEPARATOR, 3)
    if rows != programme_rows():
        v.append("the programme table is not exactly its trusted rows")
    return v


def carriage_violations(text, h):
    """CA1: the runway's sentence, the nine rules, the contact chain and the
    load-bearing statements, each once; the closed posture list; section
    3's bold-led bullets exactly the postures; the closed programme table;
    the drafting target once; no closure-presuming wording."""
    flat = _flat(text)
    v = []
    runway = _flat(baseline_text(RUNWAY))
    if RUNWAY_SENTENCE not in runway:
        v.append("the runway's sentence is not in the runway")
    if flat.count('"%s"' % RUNWAY_SENTENCE) != 1:
        v.append("the runway's sentence is not carried exactly once")
    for name, block in (("nine-rule", nine_rules()),
                        ("contact-chain", contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    v += closed_list_violations(text, POSTURE_LINES, POSTURES, "posture")
    sec = section_lines(text, SECTION_3)
    if sec is None:
        v.append("section 3 is not present exactly once")
    else:
        bold = [l for l in sec if BOLD_BULLET.match(l)]
        if bold != list(POSTURE_LINES[1:8]):
            v.append("section 3's bold-led bullets are not exactly the "
                     "postures")
    v += programme_table_violations(text, h)
    if text.count(DRAFTING_TARGET + "\n") != 1:
        v.append("the drafting target is not carried exactly once")
    # The drafting target is the one pinned closure sentence, whose exact
    # text is proved above and which the brief names a target only; the
    # runway's own sentence is carried verbatim and is not the brief's
    # wording. Every other occurrence is checked through the bounded fold,
    # so that emphasis, code marks, invisible code points, wrapping and
    # case hide no inventoried phrase. A bounded textual inventory: it
    # proves nothing about other prose.
    outside = text.replace(DRAFTING_TARGET, "", 1)
    low = folded(outside).replace(folded(RUNWAY_SENTENCE), "")
    v += ["closure-presuming wording: %s" % p for p in PRESUMPTION if p in low]
    # The withdrawn mechanical-conformance formula and the universal session
    # or reveal claim are refused everywhere, the drafting target included:
    # the same bounded fold, the same bounded claim.
    whole = folded(text)
    v += ["withdrawn mechanical-conformance formula: %s" % p
          for p in WITHDRAWN if p in whole]
    v += ["universal session or reveal claim: %s" % p
          for p in UNIVERSAL if p in whole]
    return v


def boundary_mutants(text):
    """The numbered-item boundary regressions for the protected item: a line
    that is not a CommonMark ordered marker - Unicode digits, ten ASCII
    digits, a closing parenthesis, or a hash with no space - placed at the
    posture item's top and after it; and the item's own number replaced by
    a non-marker prefix."""
    rows = text.split("\n")
    out_i = next(i for i, l in enumerate(rows)
                 if ITEM.match(l) and l[ITEM.match(l).end():] == POSTURE_LINES[0])
    after = out_i + len(POSTURE_LINES)
    lines = {"unicode digits": "\u0661. mechanics sentinel",
             "ten ASCII digits": "1234567890. mechanics sentinel",
             "a closing parenthesis": "1) mechanics sentinel",
             "a hash with no space": "#1 mechanics sentinel"}
    out = {}
    for form_name, line in lines.items():
        for place, at in (("above the posture item", out_i),
                          ("after the posture item", after)):
            out["%s, %s" % (form_name, place)] = "\n".join(
                rows[:at] + [line] + rows[at:])
    body = rows[out_i][ITEM.match(rows[out_i]).end():]
    for prefix in ("\u0661\u0669. ", "1234567890. "):
        out["the posture item numbered %r" % prefix.strip()] = "\n".join(
            rows[:out_i] + [prefix + body] + rows[out_i + 1:])
    return out


NON_AUTH_SECTION = "## 19. Explicit non-authorisations"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - the closure itself, at this landing, or any declaration before the "
    "closure record's own acceptance, publication and independent remote "
    "verification that W8 or W8-D7 is finished;",
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
    "    - any repair of `docs/governance/registry.md` or of the root "
    "`README.md`, or any correction, conversion or pending-stub ceremony;",
    "    - any score, rate, ranking, threshold, maturity, readiness, safety, "
    "usefulness, correctness, approval, `certif-` or `complian-` claim;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any discharge, waiver or satisfaction of any ADR-0047 Part D "
    "precondition, any resolution of precondition 3, or any movement of any "
    "carried state;",
    "    - any later phase's runway, brief, deliverable or gate, or any "
    "assignment of an unresolved item to a later phase.",
)
NON_AUTH_CLOSE = "    **Model contact and the closure of W8 remain outside this brief.**"
NON_AUTH_INTRO = "69. This brief and W8-D7 do not authorise:"
# Section 19 whole: heading, blank, introducing item, the sixteen lines,
# blank, closing sentence, trailing blank - compared as one block, nothing
# skipped.
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))


def withholding_violations(text):
    """CA2: every non-authorisation phrase present anywhere, and section 19
    exactly its authorised whole block - heading, blank, introducing item,
    the sixteen lines in order, blank, closing sentence, trailing blank -
    with no other line anywhere in it."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["section 19 is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("section 19 is not exactly its authorised whole block")
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
    """CA3: over the text's logical prose paragraphs - so that a soft line
    break, continuation indentation or a non-blank separator hides nothing -
    no case identity, no digest outside the exempt exact lines (each
    surviving the paragraph form unchanged), no reserved authoring label,
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
    """CA4: every fixed home's file set and bytes, and every registered
    record's bytes, identical to the baseline."""
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


def basis_table_violations(text, h):
    rows, v = h.rev.closed_table(text, BASIS_SECTION, BASIS_HEADER,
                                 BASIS_SEPARATOR, 6)
    if rows != basis_rows():
        v.append("the source table is not exactly its trusted rows")
    return v


def basis_object_violations(rows=None, resolve=None, registered=None):
    """Each trusted row's path names its pinned object at its cited commit
    and at the baseline, the committed bytes carry the pinned raw SHA-256,
    and the identity is registered at that path at the baseline. `resolve`
    and `registered` are injectable for the controls."""
    rows = BASIS_ROWS if rows is None else rows
    if resolve is None:
        def resolve(commit, path):
            try:
                return (_git("rev-parse", "%s:%s" % (commit, path)).strip(),
                        _sha(committed(commit, path)))
            except subprocess.CalledProcessError:
                return (None, None)
    if registered is None:
        reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
        registered = {e["id"]: e["path"] for e in reg}
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
        if registered.get(ident) != path:
            v.append("row %d: the identity is not registered at that path" % n)
    return v


def succession_rows(h):
    return [["`%s`" % RECOVERY, ", ".join(h.auth.labels(SITES[RECOVERY])),
             "`%s`" % PREIMAGE[RECOVERY][1], "`%s`" % POSTIMAGE[RECOVERY][0]]]


def succession_row_line(h):
    return "| " + " | ".join(succession_rows(h)[0]) + " |"


def succession_table_violations(text, h):
    rows, v = h.rev.closed_table(text, SUCCESSION_SECTION, SUCCESSION_HEADER,
                                 SUCCESSION_SEPARATOR, 4)
    if rows != succession_rows(h):
        v.append("the succession table is not exactly its trusted row")
    return v


def succession_violations(present, brief, h, sites=None):
    sites = SITES[RECOVERY] if sites is None else sites
    v = []
    pre = baseline_text(RECOVERY)
    if _sha(pre.encode("utf-8")) != PREIMAGE[RECOVERY][1]:
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
    if _sha(present.encode("utf-8")) != POSTIMAGE[RECOVERY][0]:
        v.append("the bytes are not the reviewed post-image")
    if h.auth.labels(sites) != ("R9",):
        v.append("the sites are not R9's alone")
    if present.count(R9_LINE) != 1 or pre.count(R9_LINE) != 1:
        v.append("R9's constant is not carried unchanged")
    if present.count(LATER_LINE) != 1 or pre.count(LATER_LINE) != 1:
        v.append("R9's LATER tuple is not carried unchanged")
    return v + succession_table_violations(brief, h)


def cab_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and CAB_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (CAB_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         CDR_CLOSE + fill(CAB_STATUS[state]) + " " + CLOSED_AFTER[state]),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + CAB_ROW + fill(ROW_PREFIX[state]) + CAB_ROW_BODY
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


def expected_registry(base_text, brief_hash, state, date):
    tail = "\n    }\n  ]\n}\n"
    if not base_text.endswith(tail):
        return None
    return (base_text[:-len(tail)] + "\n    },\n"
            + _indent(json.dumps(new_entry(state, date, brief_hash),
                                 indent=2, ensure_ascii=False), 4)
            + "\n  ]\n}\n")


def added_board_wording():
    """The wording this landing adds to the board in both lawful states, the
    accepted forms dated with a sample so that no format sign remains."""
    sample = "2026-01-01"
    return " ".join([CAB_ROW, CAB_ROW_BODY, CLOSED_AFTER["draft"],
                     CLOSED_AFTER["accepted"], CAB_STATUS["draft"],
                     CAB_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, brief_text, h):
    """CA7: this brief's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D7 entries are exactly this brief's; no
    entry of a later phase exists."""
    v = []
    e = {x["id"]: x for x in entries}.get("W8-D7-CAB")
    state, date = h.rec.header_state(brief_text)
    if e is None:
        return ["no W8-D7-CAB entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            BRIEF, "phase-brief", "W8", "W8-D7"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(brief_text.encode("utf-8")):
        v.append("the entry's hash differs from the brief")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D7"} != D7_ENTRIES:
        v.append("the W8-D7 entries are not exactly this brief's")
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
class CA1_Carriage(unittest.TestCase):
    def test_ca1_brief_carries_question_postures_programme_and_statements(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="sentence, blocks, statements, closed list, "
                               "closed table and no presumption"):
            self.assertEqual(carriage_violations(text, h), [])
        for name, mutated in boundary_mutants(text).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h))
        first = POSTURE_LINES[1]
        row = programme_row_lines()[1]
        for name, mutated in (
                ("an eighth posture", text.replace(
                    first + "\n", first + "\n    - **passed**;\n", 1)),
                ("a dropped posture", text.replace(first + "\n", "", 1)),
                ("a stray line inside the posture list", text.replace(
                    POSTURE_LINES[3] + "\n", POSTURE_LINES[3] + "\nsentinel\n", 1)),
                ("a verdict posture in place of a permitted one", text.replace(
                    first, "    - **passed**;", 1)),
                ("a dropped programme row", text.replace(row + "\n", "", 1)),
                ("a fourth landing", text.replace(
                    row + "\n", row + "\n| **D7-D** — sentinel | sentinel | "
                    "sentinel |\n", 1)),
                ("a closure-presuming sentence", text.replace(
                    "\n## 3.", "\nW8 is closed.\n\n## 3.", 1)),
                ("a closure-presuming sentence inside section 2", text.replace(
                    "\n7. **The claim is about",
                    "\nThe instrument is mature.\n\n7. **The claim is about", 1)),
                ("a second drafting target", text.replace(
                    DRAFTING_TARGET + "\n",
                    DRAFTING_TARGET + "\n\n" + DRAFTING_TARGET + "\n", 1)),
                ("the drafting target rewritten as a declaration", text.replace(
                    DRAFTING_TARGET, DRAFTING_TARGET.replace(
                        "W8 closes because", "W8 is closed because", 1), 1)),
                ("an inventoried phrase in bold", text
                 + "\nW8 **is complete**.\n"),
                ("an inventoried phrase in italics", text
                 + "\nW8 *is complete*.\n"),
                ("an inventoried phrase in underscore emphasis", text
                 + "\nW8 _is complete_.\n"),
                ("an inventoried phrase in code marks", text
                 + "\nW8 `is complete`.\n"),
                ("an inventoried phrase with a zero-width space", text
                 + "\nW8 is\u200b complete.\n"),
                ("an inventoried phrase wrapped over a soft break", text
                 + "\nW8 is\ncomplete.\n"),
                ("an inventoried phrase in capitals", text
                 + "\nW8 IS COMPLETE.\n"),
                ("a later phase named", text + "\nW9 follows.\n"),
                ("a removed statement", text.replace(REQUIRED[6], "", 1)),
                ("an altered runway sentence", text.replace(
                    RUNWAY_SENTENCE, RUNWAY_SENTENCE.replace("Whole-phase",
                                                             "Phase"), 1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1)),
                # The r1 review's withdrawn formula (F-1) and universal
                # claims (F-3): reinstated in any of these forms, refused.
                ("the withdrawn mechanical-conformance formula appended", text
                 + "\nIts mechanical surface establishes that no real-person "
                 "evaluation channel exists.\n"),
                ("the withdrawn formula in emphasis", text
                 + "\nIts *mechanical surface establishes* that no "
                 "private-adoption implementation detail exists.\n"),
                ("the withdrawn formula in place of the decomposed clause",
                 text.replace("Its mechanical clause reports exactly",
                              "Its mechanical surface establishes exactly", 1)),
                ("a universal reveal claim appended", text
                 + "\nEvery withheld record was revealed.\n"),
                ("a universal session claim appended", text
                 + "\nThe human authority dispositioned every case of each "
                 "corpus.\n"),
                ("item 56's session qualifier dropped", text.replace(
                    REQUIRED[REQUIRED.index(
                        "every case of the supplementary corpus in the lawful "
                        "W8-D3 calibration session and every case of the "
                        "validation corpus in the W8-D4 validation session")],
                    "every case of each corpus in one session", 1)),
                ("item 56's reveal qualifier dropped", text.replace(
                    "every withheld authoring record of the supplementary "
                    "corpus and every withheld authoring and construction "
                    "record of the validation corpus was revealed",
                    "every withheld record was revealed", 1)),
                ("the drafting target universalised", text.replace(
                    DRAFTING_TARGET, DRAFTING_TARGET.replace(
                        "revealed every withheld record of those two session "
                        "corpora byte-exact",
                        "revealed every withheld record byte-exact", 1), 1)),
                ("the entry points restated as the law closure reads",
                 text.replace("The rows are pinned entry points, not a choice "
                              "of which law governs.",
                              "The rows fix the law W8-D7 reads.", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated, h))
        for name, added in (("a phrase outside the inventory",
                             "\nW8 is nearly finished.\n"),
                            ("the quoted runway sentence in bold",
                             '\n**"%s"**\n' % RUNWAY_SENTENCE),
                            ("a reveal claim bounded to its session corpus",
                             "\nEvery withheld record of the session corpus "
                             "was revealed.\n"),
                            ("the audit's own limit sentence",
                             "\nNo mechanical result establishes that any "
                             "family is clear.\n")):
            with self.subTest(positive="%s is not what the inventories refuse"
                                       % name):
                self.assertEqual(
                    [x for x in carriage_violations(text + added, h)
                     if x.startswith(("closure-presuming wording",
                                      "withdrawn mechanical-conformance",
                                      "universal session or reveal"))], [])
        with self.subTest(fact="the fold is the bounded fold: marks, "
                               "whitespace and case"):
            self.assertEqual(folded("W8 **is**\n  _com\u200bplete_."),
                             "w8 is complete.")
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(carriage_violations(text, hh), [])
                self.assertTrue(carriage_violations(
                    text.replace(row + "\n", "", 1), hh))


class CA2_NonAuthorisations(unittest.TestCase):
    def test_ca2_brief_carries_its_non_authorisations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="every non-authorisation carried"):
            self.assertEqual(withholding_violations(text), [])
        for s in WITHHELD[:3]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, "")))
        grouped = NON_AUTH_LINES[9] + "\n"
        pair = NON_AUTH_LINES[6] + "\n" + NON_AUTH_LINES[7] + "\n"
        tail = NON_AUTH_LINES[15] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this section.\n"
        for name, mutated in (
                ("the grouped-count non-authorisation dropped", text.replace(
                    grouped + NON_AUTH_LINES[10], NON_AUTH_LINES[10], 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[7] + "\n" + NON_AUTH_LINES[6] + "\n", 1)),
                ("a seventeenth non-authorisation", text.replace(
                    grouped + NON_AUTH_LINES[10],
                    grouped + "    - any sentinel line;\n" + NON_AUTH_LINES[10],
                    1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[15] + "\n" + neutral
                              + "\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[15] + "\n    This landing "
                              "authorises the closure.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a differently indented extra bullet",
                 text.replace(tail, NON_AUTH_LINES[15] + "\n  - any sentinel "
                              "line;\n\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a line between the heading and the introducing item",
                 text.replace(NON_AUTH_SECTION + "\n\n" + NON_AUTH_INTRO
                              + "\n", NON_AUTH_SECTION + "\n\n" + neutral
                              + NON_AUTH_INTRO + "\n", 1)),
                ("a line between the introducing item and the first "
                 "non-authorisation",
                 text.replace(NON_AUTH_INTRO + "\n" + NON_AUTH_LINES[0]
                              + "\n", NON_AUTH_INTRO + "\n" + neutral
                              + NON_AUTH_LINES[0] + "\n", 1)),
                ("a line after the closing sentence",
                 text.replace(tail, tail + neutral, 1)),
                ("a non-breaking-space line as the blank separator",
                 text.replace(tail, NON_AUTH_LINES[15] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated))


class CA3_NoExposure(unittest.TestCase):
    def test_ca3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr")
        text = read(BRIEF).decode("utf-8")
        exempt = (succession_row_line(helpers(read, "auth")),) + tuple(
            basis_row_lines())
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D7-CAB"]["role"] + " " + by_id["W8-D7-CAB"]["title"]
        for name, surface, ex in (("brief", text, exempt),
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
        with self.subTest(control="a source row with an altered digest is not "
                                  "exempt"):
            altered = basis_row_lines()[0].replace("sha256:f", "sha256:0", 1)
            self.assertNotEqual(altered, basis_row_lines()[0])
            self.assertTrue(exposure_violations(
                text.replace(basis_row_lines()[0], altered, 1), h, exempt))
        for name, route in {
                "a figure word and its value on one line": "\nscore: 5\n",
                "a figure word, a soft line break, its value": "\nscore\n5\n",
                "a figure word, a worded connector, a soft break, its value":
                    "\nscore is\n5\n",
                "a figure word, a soft break, a space-indented value":
                    "\nscore\n    5\n",
                "a figure word, a soft break, a tab-indented value":
                    "\nscore\n\t5\n",
                "a no-break-space separator line between them":
                    "\nscore\n\u00a0\n5\n",
                "an em-space separator line between them":
                    "\nscore\n\u2003\n5\n",
                "a form-feed separator line between them":
                    "\nscore\n\u000c\n5\n",
                "a token, a soft line break, a count": "\n%s\n5\n" % tok,
                "a relation name, a soft line break, a count":
                    "\nagreements\n11\n"}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(exposure_violations(text + route, h, exempt))
        for name, route in {
                "a figure word, a genuine blank line, a value":
                    "\nscore\n\n5\n",
                "a figure word, a space-only line, a value":
                    "\nscore\n   \n5\n",
                "a figure word, a tab-only line, a value":
                    "\nscore\n\t\n5\n"}.items():
            with self.subTest(positive="%s keeps two paragraphs apart" % name):
                self.assertEqual(exposure_violations(text + route, h, exempt),
                                 [])
        with self.subTest(fact="the paragraph form parts blocks only at "
                               "blank lines and makes each whitespace run "
                               "one space"):
            self.assertEqual(prose_paragraphs("a\n  b\tc\n\u00a0\nd\n\ne\n \nf"),
                             "a b c d\n\ne\n\nf")
        with self.subTest(fact="every exempt row survives the paragraph form"):
            folded_text = prose_paragraphs(text)
            for line in exempt:
                self.assertEqual(folded_text.count(line), 1)
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr")
                self.assertEqual(exposure_violations(text, hh, exempt), [])
                self.assertTrue(exposure_violations(text + "\n0.5\n", hh,
                                                    exempt))


class CA4_FixedArtefactsAndBasis(unittest.TestCase):
    def test_ca4_every_case_home_register_and_record_unchanged(self):
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
        with self.subTest(fact="the registered records cover the finding, "
                               "the decision and the W7 closure"):
            for p in ("docs/phases/W8-D5-adequacy-finding-record.md",
                      "docs/phases/W8-D6-contact-decision-record.md",
                      "docs/phases/W7-closure-record.md"):
                self.assertIn(p, records)
            self.assertNotIn(REGISTRY, records)
        reveal_file = homes["governance/validation-reveal"][0]
        decision = "docs/phases/W8-D6-contact-decision-record.md"
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed decision record": (
                    dict(now, **{decision: now[decision] + b" "}), tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))

    def test_ca4_source_table_is_exactly_its_trusted_rows_resolving(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rev")
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="the table read whole is the trusted rows"):
            self.assertEqual(basis_table_violations(text, h), [])
        with self.subTest(fact="every row resolves at its commit and at the "
                               "baseline, and is registered"):
            self.assertEqual(basis_object_violations(), [])
        with self.subTest(fact="the rows cover the runway, the closure "
                               "precedent, the contact law, the P4 "
                               "decomposition, the recovery law, the finding "
                               "and the decision"):
            idents = [r[1] for r in BASIS_ROWS]
            for i in ("W8-AR", "W7-CR", "W7-D7-CAR", "W7-D7-CAB", "W6-D6-CAB",
                      "ADR-0047", "ADR-0052", "ADR-0058", "W8-D5-AFR",
                      "W8-D6-CDR"):
                self.assertIn(i, idents)
            self.assertEqual(len(set(idents)), len(idents))
        line = basis_row_lines()[0]
        top = BASIS_HEADER + "\n" + BASIS_SEPARATOR + "\n"
        for name, mutated in (
                ("a dropped row", text.replace(line + "\n", "", 1)),
                ("a duplicated row", text.replace(line + "\n", line + "\n"
                                                  + line + "\n", 1)),
                ("an altered commit", text.replace(
                    line, line.replace(BASIS_ROWS[0][3], "0" * 40, 1), 1)),
                ("an altered separator", text.replace(
                    top, BASIS_HEADER + "\n|---|---|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom", text.replace(
                    basis_row_lines()[-1] + "\n",
                    basis_row_lines()[-1] + "\nmechanics sentinel\n", 1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(basis_table_violations(mutated, h))
        good = BASIS_ROWS[0]
        wrong_blob = (good[0], good[1], good[2], good[3], "0" * 40, good[5])
        wrong_sha = (good[0], good[1], good[2], good[3], good[4],
                     "sha256:" + "0" * 64)
        wrong_commit = (good[0], good[1], good[2], W7_CLOSURE, good[4],
                        good[5])
        unregistered = (good[0], "W8-D7-SNT") + good[2:]
        for name, rows in (("a wrong object", (wrong_blob,)),
                           ("a wrong digest", (wrong_sha,)),
                           ("a commit at which the object differs",
                            (wrong_commit,)),
                           ("an identity not registered at the path",
                            (unregistered,)),
                           ("a gap in the numbering", (good, BASIS_ROWS[2]))):
            with self.subTest(object_control="%s is refused" % name):
                self.assertTrue(basis_object_violations(rows))
        with self.subTest(control="a resolver returning the pins verbatim "
                                  "is not what is trusted"):
            self.assertEqual(basis_object_violations(
                resolve=lambda c, p: (good[4], good[5]),
                registered={good[1]: good[2]}, rows=(good,)), [])
            self.assertTrue(basis_object_violations(
                resolve=lambda c, p: (good[4], good[5]),
                registered={}, rows=(good,)))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rev")
                self.assertEqual(basis_table_violations(text, hh), [])


class CA5_R9Succession(unittest.TestCase):
    def test_ca5_r9_succession_is_exact_and_its_sentence_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "auth", "rev", "rec")
        brief = read(BRIEF).decode("utf-8")
        present = read(RECOVERY).decode("utf-8")
        with self.subTest(baseline_object=PREIMAGE[RECOVERY][0]):
            self.assertEqual(_git("rev-parse", BASELINE + ":" + RECOVERY)
                             .strip(), PREIMAGE[RECOVERY][2])
        with self.subTest(exact_succession=PREIMAGE[RECOVERY][0]):
            self.assertEqual(succession_violations(present, brief, h), [])
            self.assertEqual(_blob(present.encode("utf-8")),
                             POSTIMAGE[RECOVERY][1])
        with self.subTest(fact="R9's sentence and constants unchanged, the "
                               "new anchor the W8-D6 completion"):
            self.assertEqual(h.rec.R9_REVEAL, R9_SENTENCE)
            self.assertEqual(h.rec.D3_COMPLETION, D3_COMPLETION)
            self.assertEqual(h.rec.D4_COMPLETION, D4_COMPLETION)
            self.assertEqual(h.rec.D5_COMPLETION, D5_COMPLETION)
            self.assertEqual(h.rec.D6_COMPLETION, D6_COMPLETION)
            self.assertEqual(h.rec.LATER, ("W8-D4", "W8-D5", "W8-D6", "W8-D7"))
        with self.subTest(fact="the W8-D6 completion anchor is this "
                               "landing's baseline, at which no W8-D7 entry "
                               "existed"):
            self.assertEqual(D6_COMPLETION, BASELINE)
            self.assertEqual(_git("rev-list", "--parents", "-n", "1",
                                  D6_COMPLETION).split()[1:], [D6A_LANDING])
            self.assertEqual([e["id"] for e in json.loads(
                committed(D6_COMPLETION, REGISTRY))["entries"]
                if e["deliverable"] == "W8-D7"], [])
        with self.subTest(fact="the succeeded module carries the W8-D7 "
                               "absence as a historical proof and no live "
                               "later-deliverable limb"):
            self.assertEqual(present.count("LATER[3:]"), 1)
            self.assertIn(SITES[RECOVERY][1][2], present)
            self.assertNotIn(SITES[RECOVERY][1][1], present)
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[RECOVERY][1:]),
                "an altered R9 constant": (present.replace(
                    R9_LINE, R9_LINE.replace("corrected", "repaired"), 1),
                    None),
                "an altered LATER tuple": (present.replace(
                    LATER_LINE, LATER_LINE.replace('"W8-D7")', '"W8-D7", '
                                                   '"W8-D8")'), 1), None),
                "the anchor collapsed onto the W8-D5 completion": (
                    present.replace('D6_COMPLETION = "%s"' % D6_COMPLETION,
                                    'D6_COMPLETION = "%s"' % D5_COMPLETION, 1),
                    None),
                "the live limb restored beside the historical one": (
                    present.replace(SITES[RECOVERY][1][2],
                                    SITES[RECOVERY][1][2]
                                    + SITES[RECOVERY][1][1], 1), None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[RECOVERY] + (("R9", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
                if table is None:
                    self.assertNotEqual(text, present)
                self.assertTrue(succession_violations(text, brief, h, table))
        row = succession_row_line(h)
        top = SUCCESSION_HEADER + "\n" + SUCCESSION_SEPARATOR + "\n"
        for name, mutated in (
                ("a space-prefixed duplicate row", brief.replace(
                    row + "\n", row + "\n " + row + "\n", 1)),
                ("a row with no opening pipe", brief.replace(row, row[2:], 1)),
                ("an altered separator", brief.replace(
                    top, SUCCESSION_HEADER + "\n|---|---|---|\n", 1)),
                ("delimiter-free material touching the bottom",
                 brief.replace(row + "\n", row + "\nmechanics sentinel\n",
                               1))):
            with self.subTest(table_control="%s is refused" % name):
                self.assertNotEqual(mutated, brief)
                self.assertTrue(succession_table_violations(mutated, h))
        for name, mutated in h.rev.boundary_mutants(
                brief, SUCCESSION_SECTION, row).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertTrue(succession_table_violations(mutated, h))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "auth", "rev", "rec")
                self.assertEqual(succession_violations(present, brief, hh), [])
                self.assertEqual(hh.rec.R9_REVEAL, R9_SENTENCE)


class CA6_RegistryAndBoard(unittest.TestCase):
    def test_ca6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = cab_state(read(BRIEF).decode("utf-8"), h)
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
                               "once, the closing sentence moved", state=state):
            self.assertEqual(board_pre.count(BOARD_STATUS_ANCHOR), 1)
            self.assertEqual(board_pre.count(BOARD_ROW_ANCHOR), 1)
            self.assertTrue(board_ok(h.auth.apply_sites))
            self.assertEqual(board.count(R9_SENTENCE), 1)
            self.assertEqual(board.count(CLOSED_AFTER[state]), 1)
            self.assertNotIn(CLOSED_BEFORE, board)
        brief_hash = _sha(read(BRIEF))
        reg = read(REGISTRY).decode("utf-8")
        with self.subTest(fact="exact authorised registry", state=state):
            self.assertEqual(reg, expected_registry(reg_pre, brief_hash,
                                                    state, date))
        other = "accepted" if state == "draft" else "draft"
        with self.subTest(control="the other acceptance form is refused"):
            self.assertNotEqual(reg, expected_registry(
                reg_pre, brief_hash, other, "2000-01-01"))
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


class CA7_EntrySet(unittest.TestCase):
    def test_ca7_registered_and_the_w8_d7_entry_set_is_this_briefs(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        brief = read(BRIEF).decode("utf-8")
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, brief, h), [])
        with self.subTest(fact="no W8-D7 entry at the baseline"):
            self.assertEqual([e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] == "W8-D7"], [])
        # Succeeded at the assessment landing (W8-D7-CAR): the W8-D7 entry
        # set and the no-later-phase limb stay proven at this landing's own
        # published commit, D7A_LANDING; the live gates live in the
        # assessment landing's proof module until the closure record's
        # landing succeeds them in turn.
        at_landing = json.loads(committed(D7A_LANDING, REGISTRY))["entries"]
        with self.subTest(fact="the W8-D7 entries were this brief's alone at "
                               "this landing's published commit"):
            self.assertEqual(commit, D7A_LANDING)
            self.assertEqual(entry_violations(at_landing, brief, h), [])
        base = at_snapshot[-1]
        for name, entries in {
                "a premature second W8-D7 entry": at_snapshot + [dict(
                    base, id="W8-D7-SNT", deliverable="W8-D7")],
                "a wrong brief hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                       if e["id"] == "W8-D7-CAB" else e
                                       for e in at_snapshot],
                "a wrong deliverable": [dict(e, deliverable="W8-D6")
                                        if e["id"] == "W8-D7-CAB" else e
                                        for e in at_snapshot],
                "a later phase's entry": at_snapshot + [dict(
                    base, id="W9-D1-SNT", phase="W9",
                    deliverable="W9-D1")]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, brief, h))


class CA8_Census(unittest.TestCase):
    def test_ca8_census_is_exactly_five_paths(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        paths = landing_paths(commit)
        with self.subTest(fact="the census is exactly five paths"):
            self.assertEqual(paths, set(FIXED_CENSUS))
        with self.subTest(fact="only this module and R9's change among the "
                               "proofs"):
            self.assertEqual({p for p in paths if p.startswith("tests/")},
                             {SELF_REL, RECOVERY})
        flat = _flat(read(BRIEF).decode("utf-8"))
        with self.subTest(fact="the brief names the fixed census"):
            m = re.search(r"\*\*This landing's census is exactly five "
                          r"paths:\*\* (.*?) ## ", flat)
            self.assertIsNotNone(m)
            self.assertEqual(set(re.findall(r"`([^`]+)`", m.group(1))),
                             set(FIXED_CENSUS))
        for name, p in {"an extra path": paths | {RUNWAY},
                        "a missing path": paths - {REGISTRY}}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(p, set(FIXED_CENSUS))


if __name__ == "__main__":
    unittest.main()
