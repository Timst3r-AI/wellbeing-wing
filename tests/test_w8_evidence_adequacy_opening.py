"""W8-D5-A — evidence-adequacy opening brief proofs (W8-D5-EAB, EA1–EA8).

The opening landing of W8-D5: the brief that fixes the evidence-adequacy
review's question, admissible evidence, criteria, closed finding form,
limitations, human decision points and stop conditions; and the one proof
succession the placeholder probe found a W8-D5 opening to need - ADR-0058's
R9 later-deliverable limb, its sentence and constant unchanged. This module
proves the brief's carriage, its closed criteria and finding lists and the
absence of preselecting wording; its non-authorisations; its exposure
limits, with the one trusted succession row as the only digest exemption;
that every case home, register, revealed record and earlier W8-D3 and
W8-D4 record is byte-unchanged; the exact R9 succession and its closed
table; and the exact registry, board and census - each with planted-mutant
or negative controls. Closed validators compare against trusted expected
values held here and refuse unrecognised material rather than skip it.

Every proof reads this landing's fixed snapshot - the candidate over the
baseline before the commit exists, the one commit that added the brief
afterwards - and executes the helpers it relies on from that snapshot's
bytes, in a private namespace. The one present-state gate is EA7's W8-D5
entry set, which the review law's landing is expected to move, as the
W8-D4 opening's moved. The residual live reach is disclosed exactly: each
snapshot-executed helper module imports, at its own top level, the live
modules it aliases for the fixed-law values it reads from them, and no
more independence than that is claimed.

EA1's numbered-item pattern admits exactly CommonMark's ordered marker in
this brief's form - one to nine ASCII digits, a full stop and a space - so
that a line a Markdown reader folds into a protected item is never taken
for the next item's boundary (the r1 review's F-1). EA1's preselection
scan sets aside the pinned finding-form lines, whose exact text the closed
list already proves, and reads everything else.

This landing's derived public baseline is the published documentation
erratum W8-DER, landed over the W8-D4 completion. The R9 succession names
the W8-D4 completion as its historical anchor, D4_COMPLETION, and EA5
proves that anchor distinct from, and the sole parent of, this baseline.

EA2 reads section 12 as one whole block - heading, blank separator,
introducing item, the eleven non-authorisations, blank separator, closing
sentence and trailing separator, in that order and nothing else - so that
unmarked prose, a permission sentence, a differently indented bullet or a
line at either edge of the block is refused rather than skipped (the r3
review's F-1).

THIS MODULE READS NO CUSTODY AND NO CASE. It holds no case identity,
schema literal or method label as a literal; the one token name it holds is
inside the brief's criterion line it pins. It performs no review and makes
no finding.

WHAT GREEN DOES NOT MEAN. A green run proves mechanics and carriage only. It
NEVER establishes: any adequacy finding, or which finding is right; that
the instrument is mature, valid or ready; that model contact would or would
not add useful evidence; anything about any case, disposition, divergence
or reviewer; that any model was contacted; or that W8-D6 or W8-D7 may open.
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

# The published, remotely verified documentation erratum W8-DER: this
# landing's sole parent and the commit every pre-image below is read from.
BASELINE = "6704649ed80c27112c00c14093c82645e8d090cf"
# The published, remotely verified W8-D4 completion: the R9 succession's
# historical anchor, kept distinct from BASELINE (it is BASELINE's sole
# parent).
D4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"

BRIEF = "docs/phases/W8-D5-evidence-adequacy-brief.md"
SELF_REL = "tests/test_w8_evidence_adequacy_opening.py"
RECOVERY = "tests/test_w8_session_recovery_law.py"
REGISTRY = "governance/registry.json"
BOARD = "docs/phases/README.md"
RUNWAY = "docs/phases/W8-runway-generative-evaluation-maturity.md"
DOCTRINE = "docs/decisions/0054-generative-evaluation-maturity-doctrine.md"
CONTACT_LAW = "docs/decisions/0047-first-contact-doctrine-and-named-not-performed-gate.md"
FIXED_CENSUS = frozenset({BRIEF, SELF_REL, RECOVERY, REGISTRY, BOARD})
D5_ENTRIES = frozenset({"W8-D5-EAB"})
LATER_THAN_D5 = ("W8-D6", "W8-D7")
FIXED_HOMES = ("governance/validation-cases", "governance/validation-review",
               "governance/validation-reveal",
               "governance/discriminating-instrument",
               "governance/discriminating-supplement",
               "governance/discriminating-reveal",
               "governance/discriminating-review")
FIXED_RECORD_IDS = ("W8-AR", "ADR-0047", "ADR-0054", "ADR-0057", "ADR-0058",
                    "ADR-0060", "W8-D3-SCB", "W8-D3-HDR", "W8-D3-CCR",
                    "W8-D4-IVB", "W8-D4-VCR", "W8-D4-VSR", "W8-D4-VRC",
                    "W8-D4-CPR", "W8-CHC", "W8-DER")

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
               "sha256:6873de43760267cb51366078818cbc33ac5e50bbfd8cabe9eb840dd05d910b97",
               "d0bafd22b15f949d980ab3dc0884250ed325c4aa"),
    REGISTRY: ("registry",
               "sha256:1ffaedd207dec09b4466ad75b65f2b7e0e0265550a1df75ce6b49bac44a8ed43",
               "6274277fe618c04dbc33699f4692f5e77302730b"),
    BOARD: ("board",
            "sha256:51eb2cf014e1d9a642864de7737b2124474c49f56145b3a84c9adb680d820948",
            "626015cc834b707e2ba3c2516666b135fe786dff"),
}
# The reviewed post-image of the one succession: (LF SHA-256, blob).
POSTIMAGE = {RECOVERY: ("sha256:a1efe9fb15e75868acfb763c37735e648baa7bea62fe1b1357d80f078c2e6537", "b8a20d4b97585b6ef51476ebbcf407a7b6d32246")}

# ------------------------------------------ the one succession: ADR-0058 R9
SITES = {
    RECOVERY: (
        ('R9',
         '# R9\'s later-deliverable limb as succeeded at the W8-D4 opening\n# (W8-D4-IVB section 8).\nD3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"\n',
         '# R9\'s later-deliverable limb as succeeded at the W8-D4 opening\n# (W8-D4-IVB section 8).\nD3_COMPLETION = "3c34246a5b6989aaa6c5e19621964fa0c7799cdd"\n# Succeeded again at the W8-D5 opening (W8-D5-EAB section 8): the\n# absence of every W8-D5 to W8-D7 entry stays proven at the W8-D4\n# completion.\nD4_COMPLETION = "ce78a242df25898d90debee9513bdce7e511471b"\n'),
        ('R9',
         '        with self.subTest(fact="no registry entry opens W8-D5 to "\n                               "W8-D7"):\n            self.assertEqual([e["id"] for e in entries\n                              if e["deliverable"] in LATER[1:]], [])\n',
         '        # Succeeded again at the W8-D5 opening landing: the absence of\n        # every W8-D5 to W8-D7 entry stays proven at the W8-D4\n        # completion commit; W8-D5\'s entry set moves to that landing\'s\n        # own proof module, and W8-D6 and W8-D7 stay unopened.\n        with self.subTest(fact="no registry entry opened W8-D5 to "\n                               "W8-D7 at the W8-D4 completion"):\n            at_d4 = json.loads(packet.committed_object_bytes(\n                ROOT, D4_COMPLETION, "governance/registry.json"))[\n                "entries"]\n            self.assertEqual([e["id"] for e in at_d4\n                              if e["deliverable"] in LATER[1:]], [])\n        with self.subTest(fact="no registry entry opens W8-D6 or "\n                               "W8-D7"):\n            self.assertEqual([e["id"] for e in entries\n                              if e["deliverable"] in LATER[2:]], [])\n'),
    ),
}
R9_SENTENCE = "No divergence is diagnosed, explained away or corrected."
R9_LINE = 'R9_REVEAL = "%s"\n' % R9_SENTENCE

# --------------------------------------------------------------- carriage
RUNWAY_QUESTION = ("Whether the instrument is mature enough that actual model "
                   "contact would add useful evidence")
REQUIRED = (
    "W8-D5 opens for evidence-adequacy review work only, through the landing "
    "programme of section 10. W8-D6 and W8-D7 remain closed.",
    "This brief itself performs no adequacy review, makes no finding, reads "
    "no custody, changes no case, disposition or record, diagnoses no "
    "divergence and contacts no model.",
    "never a readiness, safety, correctness, approval, `certif-` or "
    "`complian-` claim about the instrument, any model or anything else",
    "No W8-D5 act contacts a model, prepares credentials, providers, "
    "transport, prompts or implementation for contact, or treats future "
    "contact as inevitable",
    "no W8-D5 finding discharges, waives or satisfies any of them.",
    "No finding preselects the contact decision.",
    "it decides, recommends, requires, schedules and forecloses nothing.",
    "a finding that contact would add no useful evidence is not a failure "
    "of W8, and a finding that it would add useful evidence authorises no "
    "step towards contact.",
    "The finding is the human authority's own act.",
    "No mechanical result, count, scan or test establishes a finding",
    "No W8-D5 act amends, re-dispositions, re-reveals or diagnoses any case.",
    "No W8-D5 act accesses custody or lists, opens, parses, hashes, copies "
    "or reveals any retained record.",
    "The review rests only on published bytes at fixed commits",
    "The published W7 record class is not the W8 instrument",
    "No arrangement may stand in for the case-level record.",
    "The criteria are questions, not thresholds.",
    "Each form is equally lawful, and none is preselected, expected or "
    "recommended by this brief. An undetermined finding is complete, never "
    "a failure.",
    "Nothing is corrected inside W8-D5.",
    "The review cannot exceed its evidence.",
    "AI assistance is attributed, never substituted.",
    "Silence is never a finding.",
    "Each later landing runs a placeholder probe over every existing check "
    "before its census is fixed, and a refusal outside its authorised "
    "successions is a stop.",
    "Model contact, W8-D6 and W8-D7 remain outside this brief.",
    "Acceptance of this brief adopts these positions.",
    "It is retained in the runway's own terms, and the three finding forms of "
    "item 23 answer it directly.",
    "\"Mature enough\" is expressly adopted in its bounded meaning: whether the "
    "instrument is adequate for actual model contact to add useful evidence",
    "W8-D5 introduces no new grouped outcome count, rate or ranking by corpus, "
    "authored class or validation method",
    "Captured generated material cannot become a new W8 case or a calibration "
    "comparison.",
    "Lawful reception is addressed first.",
    "The threshold answer settles no finding form by itself.",
    "Alternative evidence routes are named so that the finding is not read "
    "against an empty comparison.",
    "An undiagnosed divergence cuts in no direction.",
    "The sole reviewer assesses their own record.",
)
CRITERIA = ("discrimination", "uncertainty", "challenge", "limits",
            "reception", "marginal value", "independence")
CRITERIA_LINES = (
    "**The criteria are questions, not thresholds.** Each is addressed in "
    "words in the finding record; none is scored, weighted, ranked or "
    "reduced to a figure, and none determines the finding mechanically. "
    "They are exactly:",
    "    - **discrimination** — what the published case-level comparisons "
    "record, read case by case beside the revealed construction records and "
    "described in words across the authored classes, under ADR-0060 "
    "decision 34: an agreement establishes no detection, and a divergence "
    "is no reviewer error;",
    "    - **uncertainty** — whether `review_inconclusive` stayed "
    "structurally available in the packet, the procedure and the published "
    "record, and whether it occurs in the published record (ADR-0054 "
    "decisions 11 and 12); never whether any fixed disposition was correct;",
    "    - **challenge** — what the published case-level records show, in "
    "words, of the six validation methods, and what they cannot show;",
    "    - **limits** — the bounds the published record itself states and "
    "the limits of section 6, including that every recorded divergence "
    "stays undiagnosed;",
    "    - **reception** — the threshold answer of item 20, carried into the "
    "finding: whether material a model produced could be received under the "
    "published doctrine, case shape and review procedure without changing "
    "them, given the identical governed handling of ADR-0047 decision 6;",
    "    - **marginal value** — what actual contact could add that the "
    "published synthetic record cannot, what it could not add under section "
    "4, and what the alternative routes of item 26 could add instead, read "
    "under the last link of ADR-0047 decision 18 in both directions;",
    "    - **independence** — that the finding neither decides nor narrows "
    "the W8-D6 contact decision.",
)
FORMS = ("mature enough", "not mature enough", "undetermined")
FORM_LINES = (
    "**The finding form is closed.** The human authority's finding answers "
    "the runway's question, in the bounded meaning of item 4, with exactly "
    "one of:",
    "    - **mature enough** — on the published evidence, the instrument is "
    "mature enough that actual model contact would add useful evidence of "
    "the kind item 21 names; this is the bounded adequacy judgement, and no "
    "readiness, safety, correctness or approval claim;",
    "    - **not mature enough** — on the published evidence, it is not: "
    "contact would add no useful evidence of that kind, because the "
    "published record already supplies what contact could lawfully "
    "contribute, or because what contact could contribute is not evidence "
    "about the instrument; this is not a failure of W8;",
    "    - **undetermined** — the published evidence does not settle the "
    "question.",
    "",
    "    **Each form is equally lawful, and none is preselected, expected or "
    "recommended by this brief. An undetermined finding is complete, never a "
    "failure.**",
)
# A numbered item as this brief writes it and CommonMark admits it: one to
# nine ASCII digits, a full stop and a space. Unicode digits and longer
# runs are text, which a Markdown reader folds into the item above.
ITEM = re.compile(r"^[0-9]{1,9}\. ")
BOLD_BULLET = re.compile(r"^\s*[-*+]\s+\*\*")
# Wording that would preselect a finding or the contact decision; none may
# appear anywhere in the brief.
PRESELECTION = ("contact is warranted", "contact is not warranted",
                "should be contacted", "should contact", "should not contact",
                "recommend contact", "recommends contact",
                "is ready for contact", "the instrument is mature",
                "the instrument is not mature", "the finding will be",
                "is expected to find", "will add useful evidence",
                "will not add useful evidence")
WITHHELD = ("performs no adequacy review", "makes no finding",
            "diagnoses no divergence", "contacts no model",
            "W8-D6 and W8-D7 remain closed",
            "any model contact, credential, provider, transport, prompt, "
            "harness, implementation or contact surface",
            "any contact decision (W8-D6) or closure (W8-D7)",
            "the adequacy review itself, or any finding, at this landing",
            "any diagnosis of any divergence",
            "any custody access or act on any retained record",
            "any new grouped outcome count, rate or ranking by corpus, "
            "authored class or validation method")
SECTION_5 = "## 5. The review question, criteria and finding form"
SUCCESSION_SECTION = "## 9. Proof successions, each authorised only in its own landing"
SUCCESSION_HEADER = ("| Proof module | Site | Pre-image LF SHA-256 | "
                     "Post-image LF SHA-256 |")
SUCCESSION_SEPARATOR = "|---|---|---|---|"
SECTION_REF = re.compile(r"§\d+(?:\.\d+)*")

# --------------------------------------- board and registry: authorised edits
EAB_LINK = ("([`W8-D5-evidence-adequacy-brief.md`]"
            "(W8-D5-evidence-adequacy-brief.md))")
EAB_STATUS_TAIL = (
    "W8-D5 for evidence-adequacy review work only, as three landings behind "
    "their own acceptances: this brief; the evidence-adequacy review law, "
    "carrying the exact evidence index; and the human authority's adequacy "
    "finding and completion. It retains the runway's question in its bounded "
    "meaning, states what model contact could and could not lawfully "
    "contribute with lawful reception addressed first, fixes the admissible "
    "published evidence with no new grouped outcome count, seven review "
    "criteria answered in words, a closed three-form finding answering the "
    "runway's question with no form preselected, the limits — the "
    "undiagnosed divergences and the sole reviewer assessing their own "
    "record among them — the alternative evidence routes as possibilities "
    "requiring separate authority, and the human decision points; and "
    "performs no review, makes no finding, contacts no model and preselects "
    "no contact decision.")
EAB_STATUS = {
    "draft": ("**A draft W8-D5 opening brief, `W8-D5-EAB`, is before the "
              "human reviewer** " + EAB_LINK + ": if accepted, it would open "
              + EAB_STATUS_TAIL),
    "accepted": ("**The W8-D5 opening brief, `W8-D5-EAB`, is accepted** "
                 + EAB_LINK + " — accepted %s: it opens " + EAB_STATUS_TAIL),
}
EAB_ROW = ("| W8-D5 — Evidence Adequacy Review (opening brief, W8-D5-EAB) | "
           "[`W8-D5-evidence-adequacy-brief.md`]"
           "(W8-D5-evidence-adequacy-brief.md) | ")
EAB_ROW_BODY = (
    "Tier J: **opens W8-D5 for evidence-adequacy review work only** — "
    "whether the instrument is mature enough that actual model contact "
    "would add useful evidence, in the runway's bounded meaning, judged by "
    "the human authority alone from published evidence only, against seven "
    "criteria answered in words, with a closed three-form finding and no "
    "form preselected; what contact could and could not lawfully contribute "
    "is stated, lawful reception is addressed first, and no new grouped "
    "outcome count, rate or ranking is introduced. Three landings behind "
    "their own acceptances; the review law carries the evidence index before "
    "any finding; any assistance is separately attributed and adopted only "
    "by the human authority's express act. ADR-0058's R9 later-deliverable "
    "limb succeeds at this landing, its sentence and constant unchanged, the "
    "W8-D4 completion kept as its historical anchor. **No review, finding, "
    "diagnosis, custody access or contact capability yet; every W8-D3 and "
    "W8-D4 record stays fixed; W8-D6 and W8-D7 stay closed; no model "
    "contact.**")
ROW_PREFIX = {"draft": "Draft for human review — not accepted — ",
              "accepted": "Accepted by human reviewer, %s — "}
CLOSED_BEFORE = ("**" + R9_SENTENCE + " W8-D5 through W8-D7 remain closed "
                 "behind their own briefs.**")
CLOSED_AFTER = ("**" + R9_SENTENCE + " W8-D6 and W8-D7 remain closed behind "
                "their own briefs.**")
# The erratum's status sentence closes directly before the retained R9
# sentence, and its row is the table's last.
DER_CLOSE = "other than its own. "
BOARD_STATUS_ANCHOR = DER_CLOSE + CLOSED_BEFORE
BOARD_ROW_ANCHOR = ("the concept overview is named as a separate "
                    "decision.** |\n")
EAB_DRAFT = ("**Status:** Draft for human review. Not accepted. **If "
             "accepted, effective only on publication and remote "
             "verification.** No status is flipped by the implementer; "
             "acceptance is the human reviewer's dated act.")
EAB_ACCEPTED = ("**Status:** Accepted by human reviewer, %s. **Effective "
                "only on publication and remote verification.**")
NEW_ENTRY = {
    "id": "W8-D5-EAB", "path": BRIEF, "type": "phase-brief",
    "title": "W8-D5 - Evidence Adequacy Review: Opening Brief",
    "role": (
        "The opening brief of W8-D5, the evidence-adequacy review, under the "
        "W8 runway: opens W8-D5 for evidence-adequacy review work only "
        "through a three-landing programme - this brief, the review law "
        "carrying the exact evidence index, and the human authority's "
        "adequacy finding and completion. Retains the runway's question "
        "whether the instrument is mature enough that actual model contact "
        "would add useful evidence in its bounded meaning - whether the "
        "instrument is adequate for contact to add useful evidence, never a "
        "readiness, safety, correctness or approval claim - and makes the "
        "three finding forms answer it directly; states what model contact "
        "could and could not lawfully contribute, with captured generated "
        "material never a new case or comparison and lawful reception "
        "addressed first; fixes the admissible published evidence with no "
        "new grouped outcome count, rate or ranking, seven review criteria "
        "answered in words, the limits including the undiagnosed divergences "
        "and the sole reviewer assessing their own record, the alternative "
        "evidence routes as possibilities requiring separate authority, the "
        "human decision points and the stop conditions. Carries ADR-0058's "
        "R9 later-deliverable succession at its own landing, R9's sentence "
        "and constant unchanged and the W8-D4 completion kept as its "
        "historical anchor, with proof obligations EA1 to EA8. Performs no "
        "review, makes no finding, diagnoses nothing, reads no custody and "
        "contacts no model; no finding preselects the W8-D6 contact "
        "decision; W8-D6 and W8-D7 stay closed."),
    "depends_on": ["W8-AR", "ADR-0054", "ADR-0047", "ADR-0046", "ADR-0055",
                   "ADR-0057", "ADR-0058", "ADR-0059", "ADR-0060",
                   "W8-D3-SCB", "W8-D3-HDR", "W8-D3-DR-01", "W8-D3-CCR",
                   "W8-S1-SCR", "W8-S1-CM-01", "W8-D4-IVB", "W8-D4-VCR",
                   "W8-V1-CM-01", "W8-V1-CM-02", "W8-D4-VSR", "W8-D4-DR-01",
                   "W8-D4-VRC", "W8-D4-CPR", "W8-CHC", "W8-D2-CBC",
                   "ADR-0056", "W7-CR", "W8-DER"],
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


def committed(commit, rel):
    """The committed blob bytes at commit:rel - never a working copy."""
    return subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, rel)],
                          cwd=ROOT, capture_output=True, check=True).stdout


def d5a_snapshot():
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
    commit, problems = d5a_snapshot()
    return commit, problems, (lambda rel: snapshot_bytes(commit, rel))


def snapshot_tracked(commit):
    if commit is None:
        return _git("ls-files").split()
    return _git("ls-tree", "-r", "--name-only", commit).split()


def historical(read, rel):
    """One helper module as it stands in this landing's snapshot, executed in
    a fresh private namespace that is registered nowhere."""
    ns = {"__name__": "_w8_eab_historical_" + Path(rel).stem,
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


def carriage_violations(text):
    """EA1: the runway's question, the nine rules, the contact chain and the
    load-bearing statements, each once; the closed criteria and finding
    lists; section 4's bold-led bullets exactly theirs; no preselecting
    wording."""
    flat = _flat(text)
    v = []
    runway = _flat(baseline_text(RUNWAY))
    if RUNWAY_QUESTION not in runway:
        v.append("the runway's question is not in the runway")
    if flat.count('"%s"' % RUNWAY_QUESTION) != 1:
        v.append("the runway's question is not carried exactly once")
    for name, block in (("nine-rule", nine_rules()),
                        ("contact-chain", contact_chain())):
        if block is None or text.count("> %s\n" % block) != 1:
            v.append("the %s block is not carried once, byte-identical" % name)
    v += ["a statement is carried %d times: %s" % (flat.count(s), s[:44])
          for s in REQUIRED if flat.count(s) != 1]
    v += closed_list_violations(text, CRITERIA_LINES, CRITERIA, "criterion")
    v += closed_list_violations(text, FORM_LINES, FORMS, "finding form",
                                above=(CRITERIA_LINES[-1],))
    sec = section_lines(text, SECTION_5)
    if sec is None:
        v.append("section 5 is not present exactly once")
    else:
        bold = [l for l in sec if BOLD_BULLET.match(l)]
        if bold != list(CRITERIA_LINES[1:]) + list(FORM_LINES[1:4]):
            v.append("section 5's bold-led bullets are not exactly the "
                     "criteria and the finding forms")
    # The runway's own question is carried verbatim and is not the brief's
    # wording, and the pinned finding-form lines define the lawful forms
    # whose exact text the closed list proves; every other occurrence is
    # checked.
    outside = text
    for line in FORM_LINES:
        outside = outside.replace(line, "", 1)
    low = _flat(outside).lower().replace(RUNWAY_QUESTION.lower(), "")
    v += ["preselecting wording: %s" % p for p in PRESELECTION if p in low]
    return v


def boundary_mutants(text):
    """The numbered-item boundary regressions for both protected items: a
    line that is not a CommonMark ordered marker - Unicode digits, ten ASCII
    digits, a closing parenthesis, or a hash with no space - placed at the
    criteria item's top, between the two items and after the finding item;
    and each protected item's own number replaced by a non-marker prefix."""
    rows = text.split("\n")
    crit = next(i for i, l in enumerate(rows)
                if ITEM.match(l) and l[ITEM.match(l).end():] == CRITERIA_LINES[0])
    form = next(i for i, l in enumerate(rows)
                if ITEM.match(l) and l[ITEM.match(l).end():] == FORM_LINES[0])
    after = form + len(FORM_LINES)
    lines = {"unicode digits": "\u0661. mechanics sentinel",
             "ten ASCII digits": "1234567890. mechanics sentinel",
             "a closing parenthesis": "1) mechanics sentinel",
             "a hash with no space": "#1 mechanics sentinel"}
    out = {}
    for form_name, line in lines.items():
        for place, at in (("above the criteria item", crit),
                          ("between the criteria and finding items", form),
                          ("after the finding item", after)):
            out["%s, %s" % (form_name, place)] = "\n".join(
                rows[:at] + [line] + rows[at:])
    for item, at in (("criteria", crit), ("finding", form)):
        body = rows[at][ITEM.match(rows[at]).end():]
        for prefix in ("\u0661\u0669. ", "1234567890. "):
            out["the %s item numbered %r" % (item, prefix.strip())] = "\n".join(
                rows[:at] + [prefix + body] + rows[at + 1:])
    return out


NON_AUTH_SECTION = "## 12. Explicit non-authorisations"
NON_AUTH_LINES = (
    "    - any model contact, credential, provider, transport, prompt, "
    "harness, implementation or contact surface;",
    "    - any contact decision (W8-D6) or closure (W8-D7);",
    "    - the adequacy review itself, or any finding, at this landing;",
    "    - any diagnosis of any divergence;",
    "    - any custody access or act on any retained record;",
    "    - any new case, corpus, session, disposition or reveal, or any "
    "change to an existing one, including any made from captured generated "
    "material;",
    "    - any new grouped outcome count, rate or ranking by corpus, authored "
    "class or validation method;",
    "    - any amendment of ADR-0046, ADR-0047, ADR-0054, ADR-0055, ADR-0057, "
    "ADR-0058, ADR-0059 or ADR-0060;",
    "    - any score, rate, ranking, threshold, readiness, safety, "
    "correctness, approval, `certif-` or `complian-` claim;",
    "    - any real-person material, or any act of the separate adoption "
    "authority;",
    "    - any resolution of ADR-0047 precondition 3 or of any carried state.",
)
NON_AUTH_CLOSE = "    **Model contact, W8-D6 and W8-D7 remain outside this brief.**"
NON_AUTH_INTRO = "41. This brief and W8-D5 do not authorise:"
# Section 12 whole: heading, blank, introducing item, the eleven lines, blank,
# closing sentence, trailing blank - compared as one block, nothing skipped.
NON_AUTH_BLOCK = ((NON_AUTH_SECTION, "", NON_AUTH_INTRO) + NON_AUTH_LINES
                  + ("", NON_AUTH_CLOSE, ""))


def withholding_violations(text):
    """EA2: every non-authorisation phrase present anywhere, and section 12
    exactly its authorised whole block - heading, blank, introducing item,
    the eleven lines in order, blank, closing sentence, trailing blank - with
    no other line anywhere in it, so that a non-authorisation sharing its
    words with a stop condition cannot be dropped unnoticed and nothing can
    be added to the section unnoticed."""
    flat = _flat(text)
    v = ["not withheld: %s" % s[:44] for s in WITHHELD if s not in flat]
    sec = section_lines(text, NON_AUTH_SECTION)
    if sec is None:
        return v + ["section 12 is not present exactly once"]
    if tuple(sec) != NON_AUTH_BLOCK:
        v.append("section 12 is not exactly its authorised whole block")
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
    """EA3: no case identity, no digest outside the exempt exact lines, no
    reserved authoring label, schema literal or method label, no number
    beside a token or relation name, and no derived-figure form."""
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
    base_tracked = _git("ls-tree", "-r", "--name-only", BASELINE).split()
    reg = json.loads(committed(BASELINE, REGISTRY))["entries"]
    paths = {e["id"]: e["path"] for e in reg}
    homes = {h: sorted(p for p in base_tracked if p.startswith(h + "/"))
             for h in FIXED_HOMES}
    return homes, [paths[r] for r in FIXED_RECORD_IDS]


def fixed_artefact_violations(now, tracked, homes, records, base):
    """EA4: every fixed home's file set and bytes, and every fixed record's
    bytes - the erratum record among them - identical to the baseline."""
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
    return v + succession_table_violations(brief, h)


def eab_state(text, h):
    state, date = h.rec.header_state(text)
    head = "\n".join(text.split("\n")[:8])
    v = []
    if state == "draft" and EAB_DRAFT not in head:
        v.append("draft status line differs")
    if state == "accepted" and (EAB_ACCEPTED % date) not in head:
        v.append("accepted status line differs")
    if state not in ("draft", "accepted"):
        v.append("status is neither draft nor accepted")
    return state, date, v


def board_sites(state, date, board_pre):
    fill = (lambda s: s % date) if state == "accepted" else (lambda s: s)
    return (
        ("status", BOARD_STATUS_ANCHOR,
         DER_CLOSE + fill(EAB_STATUS[state]) + " " + CLOSED_AFTER),
        ("row", BOARD_ROW_ANCHOR,
         BOARD_ROW_ANCHOR + EAB_ROW + fill(ROW_PREFIX[state]) + EAB_ROW_BODY
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
    return " ".join([EAB_ROW, EAB_ROW_BODY, CLOSED_AFTER, EAB_STATUS["draft"],
                     EAB_STATUS["accepted"] % sample, ROW_PREFIX["draft"],
                     ROW_PREFIX["accepted"] % sample])


def entry_violations(entries, brief_text, h):
    """EA7: this brief's entry binds its path, type, phase, deliverable,
    status, date and hash; the W8-D5 entries are exactly this brief's; no
    W8-D6 or W8-D7 entry."""
    v = []
    e = {x["id"]: x for x in entries}.get("W8-D5-EAB")
    state, date = h.rec.header_state(brief_text)
    if e is None:
        return ["no W8-D5-EAB entry"]
    if (e["path"], e["type"], e["phase"], e["deliverable"]) != (
            BRIEF, "phase-brief", "W8", "W8-D5"):
        v.append("the entry's binding fields differ")
    if (e["status"], e["accepted_date"]) != (state, date):
        v.append("the entry's status or date differs from the header")
    if e["content_hash"] != _sha(brief_text.encode("utf-8")):
        v.append("the entry's hash differs from the brief")
    if {x["id"] for x in entries if x["deliverable"] == "W8-D5"} != D5_ENTRIES:
        v.append("the W8-D5 entries are not exactly this brief's")
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
class EA1_Carriage(unittest.TestCase):
    def test_ea1_brief_carries_question_criteria_and_finding_form(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="question, blocks, statements, closed lists "
                               "and no preselection"):
            self.assertEqual(carriage_violations(text), [])
        for name, mutated in boundary_mutants(text).items():
            with self.subTest(boundary_control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated))
        crit, form = CRITERIA_LINES[1], FORM_LINES[1]
        for name, mutated in (
                ("an eighth criterion", text.replace(
                    crit + "\n", crit + "\n    - **coverage** — sentinel;\n", 1)),
                ("a dropped criterion", text.replace(crit + "\n", "", 1)),
                ("a fourth finding form", text.replace(
                    form + "\n", form + "\n    - **partial** — sentinel;\n", 1)),
                ("a dropped finding form", text.replace(form + "\n", "", 1)),
                ("a stray line inside the finding list", text.replace(
                    FORM_LINES[3] + "\n", FORM_LINES[3] + "\nsentinel\n", 1)),
                ("a preselecting sentence", text.replace(
                    "\n## 5.", "\nThe instrument is mature.\n\n## 5.", 1)),
                ("a preselecting sentence inside section 5, outside the "
                 "pinned forms", text.replace(
                    "\n24. **Every finding states",
                    "\nThe instrument is mature.\n\n24. **Every finding "
                    "states", 1)),
                ("a finding form rewritten as an assertion", text.replace(
                    FORM_LINES[1], FORM_LINES[1].replace(
                        "on the published evidence, ", "", 1), 1)),
                ("a recommendation of contact", text.replace(
                    "\n## 5.", "\nThis brief would recommend contact.\n\n## 5.",
                    1)),
                ("a removed statement", text.replace(REQUIRED[5], "", 1)),
                ("an altered runway question", text.replace(
                    RUNWAY_QUESTION, RUNWAY_QUESTION.replace("useful", "new"),
                    1)),
                ("an altered contact chain", text.replace(
                    "no contact ≠ nothing proven", "no contact = nothing "
                    "proven", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(carriage_violations(mutated))


class EA2_NonAuthorisations(unittest.TestCase):
    def test_ea2_brief_carries_its_non_authorisations(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        text = read(BRIEF).decode("utf-8")
        with self.subTest(fact="every non-authorisation carried"):
            self.assertEqual(withholding_violations(text), [])
        for s in WITHHELD[:3]:
            with self.subTest(control="removing %r is refused" % s[:30]):
                self.assertTrue(withholding_violations(
                    _flat(text).replace(s, "")))
        grouped = NON_AUTH_LINES[6] + "\n"
        pair = NON_AUTH_LINES[3] + "\n" + NON_AUTH_LINES[4] + "\n"
        tail = NON_AUTH_LINES[10] + "\n\n" + NON_AUTH_CLOSE + "\n"
        neutral = "    Mechanics sentinel remains in this section.\n"
        for name, mutated in (
                ("the grouped-count non-authorisation dropped while the "
                 "identically worded stop condition stays", text.replace(
                    grouped + NON_AUTH_LINES[7], NON_AUTH_LINES[7], 1)),
                ("two non-authorisations swapped", text.replace(
                    pair, NON_AUTH_LINES[4] + "\n" + NON_AUTH_LINES[3] + "\n", 1)),
                ("a twelfth non-authorisation", text.replace(
                    grouped + NON_AUTH_LINES[7],
                    grouped + "    - any sentinel line;\n" + NON_AUTH_LINES[7],
                    1)),
                ("the closing sentence removed", text.replace(
                    NON_AUTH_CLOSE + "\n", "", 1)),
                ("unmarked prose after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[10] + "\n" + neutral
                              + "\n" + NON_AUTH_CLOSE + "\n", 1)),
                ("a permission sentence after the last non-authorisation",
                 text.replace(tail, NON_AUTH_LINES[10] + "\n    This landing "
                              "authorises an additional session.\n\n"
                              + NON_AUTH_CLOSE + "\n", 1)),
                ("a differently indented extra bullet",
                 text.replace(tail, NON_AUTH_LINES[10] + "\n  - any sentinel "
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
                 text.replace(tail, NON_AUTH_LINES[10] + "\n" + chr(160)
                              + "\n" + NON_AUTH_CLOSE + "\n", 1))):
            with self.subTest(control="%s is refused" % name):
                self.assertNotEqual(mutated, text)
                self.assertTrue(withholding_violations(mutated))


class EA3_NoExposure(unittest.TestCase):
    def test_ea3_no_case_level_material_or_figure_in_any_surface(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "env", "law", "pkt", "cal", "rec", "cor", "vr")
        text = read(BRIEF).decode("utf-8")
        row = succession_row_line(helpers(read, "auth"))
        by_id = {e["id"]: e for e in json.loads(read(REGISTRY))["entries"]}
        role = by_id["W8-D5-EAB"]["role"] + " " + by_id["W8-D5-EAB"]["title"]
        for name, surface, exempt in (("brief", text, (row,)),
                                      ("registry role and title", role, ()),
                                      ("board wording this landing adds",
                                       added_board_wording(), ())):
            with self.subTest(surface=name):
                self.assertTrue(surface)
                self.assertEqual(exposure_violations(surface, h, exempt), [])
        with self.subTest(surface="this module"):
            src = SELF.read_text(encoding="utf-8")
            self.assertIsNone(h.rec.CASE_ID_ANYWHERE.search(src))
            self.assertEqual([m for m in sorted(h.law.ADMITS) if re.search(
                r"(?<![A-Za-z_])%s(?![A-Za-z_])" % re.escape(m), src)], [])
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
                                                    h, (row,)))
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "env", "law", "pkt", "cal", "rec", "cor",
                             "vr")
                self.assertEqual(exposure_violations(text, hh, (row,)), [])
                self.assertTrue(exposure_violations(text + "\n0.5\n", hh,
                                                    (row,)))


class EA4_FixedArtefactsUnchanged(unittest.TestCase):
    def test_ea4_every_case_home_register_and_record_unchanged(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        tracked = snapshot_tracked(commit)
        homes, records = fixed_paths()
        every = [f for files in homes.values() for f in files] + records
        base = batch(BASELINE, every)
        now = batch(commit, every)
        with self.subTest(fact="fixed homes and records byte-identical to "
                               "the baseline"):
            self.assertEqual(len(base), len(every))
            self.assertEqual(set(now), set(every))
            self.assertEqual(fixed_artefact_violations(
                now, tracked, homes, records, base), [])
        reveal_file = homes["governance/validation-reveal"][0]
        for name, (n, t) in {
                "a revealed record with one byte added": (
                    dict(now, **{reveal_file: now[reveal_file] + b" "}),
                    tracked),
                "a changed completion record": (
                    dict(now, **{records[-2]: now[records[-2]] + b" "}),
                    tracked),
                "a removed revealed record": (
                    now, [p for p in tracked if p != reveal_file]),
                "an extra file in a fixed home": (
                    now, tracked + ["governance/validation-review/x.json"])}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(fixed_artefact_violations(
                    n, t, homes, records, base))


class EA5_R9Succession(unittest.TestCase):
    def test_ea5_r9_succession_is_exact_and_its_sentence_unchanged(self):
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
        with self.subTest(fact="R9's sentence and constant unchanged"):
            self.assertEqual(h.rec.R9_REVEAL, R9_SENTENCE)
            self.assertEqual(h.rec.D4_COMPLETION, D4_COMPLETION)
        with self.subTest(fact="the W8-D4 completion anchor is distinct "
                               "from, and the sole parent of, this "
                               "landing's baseline"):
            self.assertNotEqual(D4_COMPLETION, BASELINE)
            self.assertEqual(_git("rev-list", "--parents", "-n", "1",
                                  BASELINE).split()[1:], [D4_COMPLETION])
            self.assertEqual([e["id"] for e in json.loads(
                committed(D4_COMPLETION, REGISTRY))["entries"]
                if e["deliverable"] in ("W8-D5",) + LATER_THAN_D5], [])
        first = present.split("\n", 1)[0] + "\n"
        for name, (text, table) in {
                "an extra byte": (present + " ", None),
                "a missing site": (present, SITES[RECOVERY][1:]),
                "an altered R9 constant": (present.replace(
                    R9_LINE, R9_LINE.replace("corrected", "repaired"), 1),
                    None),
                "a self-consistent but unpinned edit": (
                    present.replace(first, first + "# planted\n", 1),
                    SITES[RECOVERY] + (("R9", first,
                                        first + "# planted\n"),))}.items():
            with self.subTest(control="%s is refused" % name):
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


class EA6_RegistryAndBoard(unittest.TestCase):
    def test_ea6_registry_and_board_change_exactly(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec", "auth")
        state, date, v = eab_state(read(BRIEF).decode("utf-8"), h)
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
        with self.subTest(control="sabotaged live helpers leave the verdict "
                                  "unchanged"):
            with LiveHelpersSabotaged():
                hh = helpers(read, "rec", "auth")
                self.assertTrue(board_ok(hh.auth.apply_sites))


class EA7_EntrySet(unittest.TestCase):
    def test_ea7_registered_and_the_w8_d5_entry_set_is_this_briefs(self):
        commit, problems, read = snapshot()
        self.assertEqual(problems, [])
        h = helpers(read, "rec")
        brief = read(BRIEF).decode("utf-8")
        at_snapshot = json.loads(read(REGISTRY))["entries"]
        with self.subTest(fact="bound at this landing's snapshot"):
            self.assertEqual(entry_violations(at_snapshot, brief, h), [])
        with self.subTest(fact="no W8-D5 to W8-D7 entry at the baseline"):
            self.assertEqual([e["id"] for e in json.loads(
                committed(BASELINE, REGISTRY))["entries"]
                if e["deliverable"] in ("W8-D5",) + LATER_THAN_D5], [])
        # The one present-state gate, until the review law's landing moves
        # it: the W8-D5 entries are exactly this brief's, and no W8-D6 or
        # W8-D7 entry exists.
        live = json.loads(_lf((ROOT / REGISTRY).read_bytes()))["entries"]
        with self.subTest(fact="present state: the W8-D5 entries are this "
                               "brief's alone"):
            self.assertEqual({e["id"] for e in live
                              if e["deliverable"] == "W8-D5"}, D5_ENTRIES)
            self.assertEqual([e["id"] for e in live
                              if e["deliverable"] in LATER_THAN_D5], [])
        base = at_snapshot[-1]
        for name, entries in {
                "a premature W8-D5 entry": at_snapshot + [dict(
                    base, id="W8-D5-SNT", deliverable="W8-D5")],
                "a W8-D6 entry": at_snapshot + [dict(
                    base, id="W8-D6-SNT", deliverable="W8-D6")],
                "a wrong brief hash": [dict(e, content_hash="sha256:" + "0" * 64)
                                       if e["id"] == "W8-D5-EAB" else e
                                       for e in at_snapshot]}.items():
            with self.subTest(control="%s is refused" % name):
                self.assertTrue(entry_violations(entries, brief, h))


class EA8_Census(unittest.TestCase):
    def test_ea8_census_is_exactly_five_paths(self):
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
