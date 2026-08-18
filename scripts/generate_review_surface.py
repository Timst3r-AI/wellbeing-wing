#!/usr/bin/env python3
"""W6-D4 static review-surface generator (the window, never a door).

Generates docs/surface/review-surface.html and surface-trace.json from
exactly the six declared inputs of the W6-D4-A/B/C exposure contract.
Python standard library only. Deterministic: byte-identical output on
every run over the same sources. Reads nothing undeclared (the
allowlist below is the whole read surface; access outside it raises).
Writes nothing except the two output artefacts. No network, no clock,
no environment, no state, no cache, no JavaScript, no forms, no
affordances of any kind in the output.

The page shows what the governed records hold — all of it, at full
size, with its accompaniments — and can do nothing else. Viewing it is
not reviewing anything; nothing rendered is approval, safety,
correctness, or display permission for any other context.
"""

import html
import json
import re
import sys
from pathlib import Path

REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else \
    Path(__file__).resolve().parent.parent
OUT_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else \
    REPO / "docs" / "surface"

DECLARED_INPUTS = (
    "governance/string-catalogue.json",
    "docs/governance/privacy-health-data-assurance-record.md",
    "governance/evaluation",          # declared directory, *.json only
    "tests/test_pending_ledger.py",
    "governance/registry.json",
    "docs/surface/surface-declarations.json",
)


def read_declared(rel):
    """The only read path. Access outside the allowlist raises."""
    if rel not in DECLARED_INPUTS:
        raise PermissionError("undeclared input refused: %s" % rel)
    return (REPO / rel).read_text(encoding="utf-8")


def esc(s):
    return html.escape(str(s), quote=True)


# ---- load declared sources -------------------------------------------
decl = json.loads(read_declared("docs/surface/surface-declarations.json"))
catalogue = json.loads(read_declared("governance/string-catalogue.json"))
registry = json.loads(read_declared("governance/registry.json"))
phdar_text = read_declared(
    "docs/governance/privacy-health-data-assurance-record.md")
ledger_text = read_declared("tests/test_pending_ledger.py")

blocks = re.findall(r"```json\n(.*?)\n```", phdar_text, re.S)
arrays = [json.loads(b) for b in blocks if b.strip().startswith("[")]
applicability, lane_c_rows = arrays[0], arrays[1]

eval_dir = REPO / "governance" / "evaluation"
if "governance/evaluation" not in DECLARED_INPUTS:
    raise PermissionError("undeclared input refused: governance/evaluation")
eval_files = sorted(eval_dir.glob("*.json"))
manifest = None
records = []
for p in eval_files:
    data = json.loads(p.read_text(encoding="utf-8"))
    if "evaluation_run" in data:
        manifest = data["evaluation_run"]
    else:
        records.append(data["evaluation_record"])

stub_pat = re.compile(
    r'@pending\("([^"]+)",\s*"([^"]+)"\)\s*\n\s*def (test_[A-Za-z0-9_]+)',
    re.S)
stubs = [{"name": name, "owner": owner, "condition": cond}
         for owner, cond, name in stub_pat.findall(ledger_text)]

titles = {e["id"]: e["title"] for e in registry["entries"]}

ACC = {a["state"]: a for a in decl["mandatory_accompaniments"]}
CEILING = decl["ceiling"]

# ---- build trace rows and page sections ------------------------------
trace = []
S = []  # html fragments


def trace_row(section, item_id, source, cat_id, state, accompaniment,
              wording):
    trace.append({
        "section": section, "item_id": item_id, "source": source,
        "cat_id": cat_id, "state": state,
        "accompaniment": accompaniment, "rendered_wording": wording,
        "proof": "rendered-and-traced",
        "non_authority": "confirmed: nothing rendered is approval, "
                         "display permission for any other context, "
                         "safety, correctness, or a claim of any kind",
    })


S.append("<h1>Wellbeing Wing — Governed Review Surface</h1>")
S.append("<p class='law'>%s</p>" % esc(decl["surface_identity"]))
S.append("<p class='law'><strong>%s.</strong> %s.</p>" % (
    esc(" · ".join(decl["aphorisms"])),
    esc("Closing this page changes no governed state")))
S.append("<p class='law'>This surface is generated deterministically "
         "from six declared governed sources. It has no scripts, no "
         "controls, and no affordances: its entire capability is to be "
         "read. Nothing shown here is a safety, health, clinical, "
         "legal, or production-readiness statement of any kind.</p>")

# Section 1 — the governed string register
S.append("<h2>1. Governed String Register (33 entries)</h2>")
S.append("<p class='law'>Family law: entries render verbatim from the "
         "register with their metadata (ADR-0038 Part B; ADR-0042). "
         "The language-law grading disposition renders with its "
         "ceiling: %s (%s).</p>" % (
             esc(decl["d3_grading_summary"]["ceiling"]),
             esc(decl["d3_grading_summary"]["citation"])))
S.append("<p class='law'>Ceiling carried by every entry: %s</p>"
         % esc(CEILING))
S.append("<table><tr><th>ID</th><th>Class</th><th>String (verbatim)"
         "</th><th>Sources</th><th>Lifecycle</th><th>Grading "
         "disposition</th></tr>")
for e in catalogue["entries"]:
    S.append(
        "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"
        "<td>lawful-as-worded — a grade is not approval and not "
        "display permission</td></tr>" % (
            esc(e["id"]), esc(e["vocabulary_class"]),
            esc(e["string"]),
            esc("; ".join(e["source_authority"])),
            esc(e["supersession_retirement_posture"]["state"])))
    trace_row("register", e["id"], e["source_authority"][0], e["id"],
              "catalogue-entry (%s, %s)" % (
                  e["vocabulary_class"],
                  e["supersession_retirement_posture"]["state"]),
              "; ".join(e["accompaniment_linkage"]) or
              "none required by law", e["string"])
S.append("</table>")

# Section 2 — the evidence map (Lane C)
S.append("<h2>2. Evidence Map (65 assurance rows)</h2>")
S.append("<p class='law'>Family law: rows render in their derived "
         "presentation states per the W4-D6-PHDAR derivation "
         "(authority-non-increasing; an overlay with unresolved "
         "applicability presents as applicability unresolved, never a "
         "pass). Accompaniments: %s · %s.</p>" % (
             esc(ACC["evidenced/not_evidenced"]["text"]),
             esc(ACC["applicability_unresolved"]["text"])))
S.append("<table><tr><th>Row</th><th>Stored state</th><th>Derived "
         "presentation</th><th>Safe wording (source's own)</th></tr>")
for r in lane_c_rows:
    if r["framework_kind"] == "alignment_overlay":
        derived = "applicability unresolved"
        acc = ACC["applicability_unresolved"]["text"]
    else:
        derived = {"evidenced": "evidenced",
                   "not_evidenced": "not evidenced",
                   "deferred_named_dependency":
                       "deferred — named dependency",
                   "external_evidence_required":
                       "external evidence required"}[r["evidence_status"]]
        acc = ACC["evidenced/not_evidenced"]["text"]
    S.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
        esc(r["row_id"]), esc(r["evidence_status"]), esc(derived),
        esc(r["safe_wording"])))
    trace_row("evidence", r["row_id"], "W4-D6-PHDAR section 4", None,
              "%s -> %s" % (r["evidence_status"], derived), acc,
              r["safe_wording"])
S.append("</table>")
S.append("<p class='law'>All four applicability records remain "
         "unresolved with no role or basis asserted; unresolved is "
         "never \"not applicable\", and no pass is implied.</p>")

# Section 3 — evaluation posture
S.append("<h2>3. Behavioural Evaluation Posture (run %s)</h2>"
         % esc(manifest["run_id"]))
S.append("<p class='law'>Family law: execution states render verbatim "
         "(ADR-0040 decision 6): %s. Unknowns render as standing "
         "truths (decision 3): %s. Routed deltas render whole with "
         "both variant captures and no machine conclusion (ADR-0041 "
         "decisions 3-6): %s.</p>" % (
             esc(ACC["behaviourally_executed"]["text"]),
             esc(ACC["unknown"]["text"]),
             esc(ACC["review_routed"]["text"])))
S.append("<table><tr><th>Fixture</th><th>State</th><th>Meaning "
         "(accompaniment, inline)</th></tr>")
for r in records:
    S.append("<tr><td>%s</td><td>behaviourally_executed</td>"
             "<td>%s</td></tr>" % (
                 esc(r["fixture_id"]),
                 esc(ACC["behaviourally_executed"]["text"])))
    trace_row("evaluation-fixtures", r["fixture_id"],
              "governance/evaluation/%s" % manifest["run_id"], None,
              "behaviourally_executed",
              ACC["behaviourally_executed"]["text"],
              "behaviourally_executed — " +
              ACC["behaviourally_executed"]["text"])
S.append("</table>")

S.append("<h3>3a. Honest unknowns (26 overt probes)</h3>")
S.append("<table><tr><th>Probe</th><th>State</th><th>Basis "
         "(source's own)</th></tr>")
unknown_count = 0
routed = []
for r in records:
    for p in r["probes"]:
        if p["channel"] == "overt":
            unknown_count += 1
            item = "%s/%s" % (r["fixture_id"], p["probe_id"])
            S.append("<tr><td>%s</td><td>unknown-not-absent</td>"
                     "<td>%s</td></tr>" % (esc(item), esc(p["basis"])))
            trace_row("evaluation-unknowns", item,
                      "governance/evaluation/%s" % manifest["run_id"],
                      None, "unknown-not-absent",
                      ACC["unknown"]["text"], p["basis"])
        elif p["delta_finding"]["outcome"] == "routed-to-review":
            routed.append((r["fixture_id"], p))
S.append("</table>")
S.append("<p class='law'>An unknown is %s; nothing here resolves one, "
         "because display resolves nothing.</p>"
         % esc(ACC["unknown"]["text"]))

S.append("<h3>3b. Review-routed deltas (%d silent probes) — both "
         "variants, whole</h3>" % len(routed))
for fid, p in routed:
    item = "%s/%s" % (fid, p["probe_id"])
    caps = p["paired_variant_captures"]
    S.append("<h4>%s — routed to human review</h4>" % esc(item))
    S.append("<p class='law'>%s. Differing surfaces: %s. No selected "
             "variant exists unless a human record later creates one."
             "</p>" % (
                 esc(ACC["review_routed"]["text"]),
                 esc(", ".join(p["delta_finding"]["differing_surfaces"]))))
    S.append("<table><tr><th>Surface</th><th>With bait</th><th>Without "
             "bait</th></tr>")
    for srf in caps["with_bait"]:
        S.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            esc(srf), esc("; ".join(map(str, caps["with_bait"][srf]))),
            esc("; ".join(map(str, caps["without_bait"][srf])))))
    S.append("</table>")
    trace_row("evaluation-routed", item,
              "governance/evaluation/%s" % manifest["run_id"], None,
              "routed-to-review", ACC["review_routed"]["text"],
              "both variant captures rendered whole; differing "
              "surfaces: " +
              ", ".join(p["delta_finding"]["differing_surfaces"]))

# Section 4 — pending ledger
S.append("<h2>4. Pending Ledger (%d stubs)</h2>" % len(stubs))
S.append("<p class='law'>Family law: stubs render with identity, "
         "owner, and unblocking condition (ADR-0041 decision 7); "
         "%s. There is no affordance here and none anywhere on this "
         "page: display performs neither eligibility nor conversion."
         "</p>" % esc(ACC["pending_stub"]["text"]))
S.append("<table><tr><th>Stub</th><th>Owner</th><th>Unblocking "
         "condition</th><th>State</th></tr>")
for s in stubs:
    S.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>pending — "
             "not converted</td></tr>" % (
                 esc(s["name"]), esc(s["owner"]), esc(s["condition"])))
    trace_row("pending-stubs", s["name"], "tests/test_pending_ledger.py",
              None, "pending", ACC["pending_stub"]["text"],
              "%s — pending on: %s" % (s["name"], s["condition"]))
S.append("</table>")

# Section 5 — carried open questions
S.append("<h2>5. Carried Open Questions (%d)</h2>"
         % len(decl["carried_open_questions"]))
S.append("<p class='law'>Family law: carried questions render as "
         "carried — %s. The three waits (carried question, pending "
         "stub, deferred dependency) are three different truths and "
         "render in their own sections, never merged.</p>"
         % esc(ACC["carried_question"]["text"]))
S.append("<table><tr><th>Question</th><th>Citation</th><th>State</th>"
         "</tr>")
for q in decl["carried_open_questions"]:
    S.append("<tr><td>%s</td><td>%s</td><td>carried — still alive"
             "</td></tr>" % (esc(q["item"]), esc(q["citation"])))
    trace_row("carried-questions", q["item"], q["citation"], None,
              "carried", ACC["carried_question"]["text"], q["item"])
S.append("</table>")

S.append("<h2>Declarations</h2>")
S.append("<p class='law'>This surface's inputs, derivations, classes, "
         "accompaniments, visual semantics, coverage, ordering, and "
         "(empty) glyph, affordance, write, persistence, and external "
         "inventories are declared as data in "
         "surface-declarations.json and proven in the suite. Colour "
         "encodes nothing. Ordering encodes nothing. %s</p>"
         % esc(CEILING))

CSS = ("body{font-family:Georgia,serif;color:#111111;background:"
       "#ffffff;margin:2em auto;max-width:70em;line-height:1.5}"
       "h1,h2,h3,h4{color:#111111;font-weight:normal}"
       "table{border-collapse:collapse;margin:1em 0;width:100%}"
       "th,td{border:1px solid #dddddd;padding:0.4em;text-align:left;"
       "vertical-align:top;color:#111111}"
       "th{background:#f5f5f5;font-weight:normal}"
       ".law{color:#444444;border-left:3px solid #dddddd;"
       "padding-left:0.8em}")

page = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<title>Wellbeing Wing — Governed Review Surface</title>\n"
        "<style>%s</style>\n</head>\n<body>\n%s\n</body>\n</html>\n"
        % (CSS, "\n".join(S)))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "review-surface.html").write_text(page, encoding="utf-8")
(OUT_DIR / "surface-trace.json").write_text(
    json.dumps({"trace_note": "Mandatory per-item trace for every "
                "rendered item (Tara's state-family directive): family "
                "reasoning is explanatory, these rows are the "
                "accountability.", "rows": trace},
               indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("surface generated: %d trace rows" % len(trace))
