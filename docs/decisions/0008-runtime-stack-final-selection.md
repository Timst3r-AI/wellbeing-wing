# 0008 — Runtime Stack — Final Selection

**Status:** Accepted by human reviewer, 2026-07-05. Not a build instruction.
**Date:** July 2026 · **Phase:** W3 (D1 cluster — the final-selection record required by ADR 0005 and ADR 0006) · **Blocks:** the W3-D2 engine brief; the first repo dependency (a future Tier F event)
**Decision mode:** selection on first-pass spike evidence, under standing doctrine. This record selects the **engine spine's** runtime and crypto binding; it selects no app shell, no surface stack, and reopens no doctrine.

## Decision question

Which runtime class and crypto-binding path does the governed engine build on — decided from the first evidence pass, honestly caveated, with everything unevidenced left explicitly open?

## Controlling law

ADR 0005 (encryption doctrine; requires this selection record with evidence attached); ADR 0006 (platform doctrine, spike plan, scored criteria; classes-not-products in landed doctrine, with this record carrying the one public-safe evidence summary); ADR 0007 (artifact law governing what the spike could leave behind — which is: this summary and nothing else); ADR 0004 (residue doctrine informing the criteria); the kickoff review decisions (Windows-class single target; three named primaries; alternates held).

## Evidence summary — first spike pass (Windows-class, single OS target)

Three primaries were authorised. Each was to build an identical thin slice — create an encrypted store with a versioned-and-reserved header using a libsodium-class binding, import one synthetic file, read it back with tamper and wrong-key checks, terminate — in disposable workspaces outside the repository, since deleted in full. Declared timing budgets were reported against honestly (all within budget; the bundled-runtime candidate consumed one diagnosis/retry cycle).

**Local-process candidate (Python 3.14-class, PyNaCl 1.6-class binding): completed.** Roundtrip, tamper-rejection (authenticated encryption), wrong-key clean-failure, and header parse all passed. Zero TCP connections and zero UDP endpoints observed during a held run (connection-table sampling; full packet capture unavailable this pass — method limitation recorded). Zero new temporary-directory items; the only artifact written was the intended store file. Working set ~11 MB; slice wall time ~271 ms including interpreter start; environment ~17 MB with a **three-package** transitive surface. Finding: caller-held key bytes are not zeroable at the language level (immutable objects; possible runtime copies).

**Bundled-runtime candidate (Electron 33-class, sodium-native 5-class binding): completed, with findings.** Same crypto checks all passed — but only after fallback: **secure-buffer allocation (`sodium_malloc`) is unavailable under the runtime's V8 memory cage** (external-buffer restriction); keys ran in V8-managed memory with explicit zeroing callable but secure-allocation guarantees lost. Even fully headless with no window, the runtime **wrote serialized state unprompted** to its user-data area (observed via redirect; the default profile location was not created). Zero TCP/UDP observed across its three-process tree during the hold. Working-set tree ~234 MB; ~577 ms wall; ~295 MB installed with an **89-package** surface. Maintenance note: the newest major's install tooling was incompatible with the present Node 20-class runtime; a version pin was required merely to install.

**Native-shell candidate (Tauri): failed fast at the toolchain gate.** The Rust toolchain is entirely absent from the Windows-class evaluation environment and no MSVC toolchain is present (the system webview runtime *is* present). Per the kickoff rules, execution paused and no alternate was promoted. Recorded as evidence of **entry cost** — the highest of the three classes on a fresh Windows-class environment — not as product evaluation.

**Format-header observation (both completed slices):** a 16-byte header — magic(4) + version(2) + reserved(10) — cost a constant and two assertions in each language; reserved room parses cleanly and costs nothing at rest.

## Criteria-by-criteria comparison

| Criterion (ADR 0006 table) | Local-process (Python/PyNaCl) | Bundled-runtime (Electron/sodium-native) | Native-shell (Tauri) |
| :---- | :---- | :---- | :---- |
| Telemetry silence | 0 connections observed | 0 connections observed (3-process tree) | not observed |
| Residue behaviour | zero beyond the intended store | wrote runtime state unprompted, even headless | not observed |
| Crypto binding & memory honesty | most-audited path in class; language-level key-zeroing limitation (caveated below) | secure buffers **structurally unavailable** (memory cage); fallback weakens key handling | not observed |
| Footprint / startup | ~11 MB / ~271 ms | ~234 MB / ~577 ms | not observed |
| Packaging/signing posture | freezer tools + standard signing (assessed, not exercised) | mature builder + signing; large artifacts (assessed) | small artifacts per documentation (assessed) |
| Accessibility posture | inherits OS console accessibility (headless) | Chromium accessibility tree, at its footprint cost | system-webview tree (documented) |
| Update posture | nothing built in — shippable with none | none by default; updater opt-in | updater optional plugin (documented) |
| Transitive dependency surface | **3 packages / 17 MB** | 89 packages / 295 MB | not measured; toolchain entry cost highest |

## Selection

**Selected for the engine spine (W3-D2): the local-process / headless engine class — Python 3 local process with the PyNaCl (libsodium) binding**, as evidenced by the completed first-pass slice.

**Why it wins for the spine:** the engine is headless by accepted shape — one governed core, many callers, no privileged path — and on every criterion that matters to a *spine*, the local-process candidate was decisively superior: residue-silent by default (the only candidate whose runtime wrote nothing unbidden — ADR 0004's posture as an observed property, not an aspiration), a dependency surface small enough to audit in one sitting, a twentieth of the memory, the most-audited binding in its class, and zero observed network behaviour. Its one honest weakness is named below and designed for, not hidden.

**Rejected for the spine: the bundled-runtime class.** It completed the slice honorably, and the rejection is specific, not dismissive: unprompted runtime state-writing (a standing residue liability the engine would fight forever), a large and churning dependency surface, version/tooling friction at install, and — decisive for a vault — the secure-buffer limitation under its memory cage, which structurally weakens the strongest key-handling tool the libsodium family offers. **It may remain a future surface candidate** only if a later review-package phase chooses to revisit it; nothing here forecloses that.

**Deferred, not rejected: the native-shell class.** Its toolchain gate is real evidence about entry cost in the current environment, and no product judgment can honestly be made from an unrun slice. Native-shell evaluation belongs to the future review-package / app-shell phase, where its documented strengths (small artifacts, system webview) are actually relevant. The engine spine does not need it, so its absence blocks nothing.

## Single-OS sufficiency

**Windows-class-only evidence is sufficient for this selection, and this record says so explicitly** per the kickoff decision: W3-D2 needs a local, headless, governed engine in the environment where development actually happens — not cross-platform release confidence. The selected class is the most portable of the three by nature (interpreter + one audited C library), and macOS/Linux verification is deferred until packaging/release confidence requires it — at which point a further evidence pass runs under the same rules.

## Key-handling caveat and required W3-D2 mitigations

**The selected path's known weakness is stated, not softened:** Python-level key bytes cannot be zeroed at the language level, and the runtime may copy immutable objects. This record binds the W3-D2 engine design to mitigate structurally: **short-lived key objects** (derived, used, released within the narrowest scope the operation permits); **narrow process-lifetime scoping** (long-lived processes never hold long-lived key material); **minimal plaintext windows** per ADR 0004's task-end discipline; residue tests covering key-material handling paths as far as the platform allows; and honest documentation of the residual (in-memory copies until garbage collection and OS paging) in the threat-model register — mitigations where the platform offers them, no claim of totality, per ADR 0004 decision 5. **The engine brief must carry these as design requirements, and this weakness must never disappear from the record.**

## Non-goals

No app-shell selection (deferred with the native-shell class to the review-package phase); no macOS/Linux claims; no packaging or distribution decisions; no UI; no reopening of ADR 0005 doctrine (which continues to bind: authenticated encryption, memory-hard KDF class, versioned format, no escrow); no engine code, which waits for the W3-D2 brief through its own gate.

## Implementation gates

No engine code until the W3-D2 brief is accepted. The first installation of the selected binding **into the repo's toolchain** is a named Tier F fence-crossing at engine start, with pinned versions, and is not authorised by this record. ADR 0005's remaining specifics — KDF parameters, envelope structure (per-record vs whole-store), custody form (passphrase/keyfile/both) — were **not exercised by the first-pass slice** and remain open: they bind at W3-D2 design time under ADR 0005 doctrine, with a micro-evidence pass authorised by the W3-D2 brief if design needs it.

## Public-safety considerations

This record carries the spike's only lasting public trace, per ADR 0006/0007: summary language throughout; environment described as Windows-class only; no raw logs, no local paths, no screenshots, no machine-identifying detail; no spike artifact copied or pasted into this record; product names and version classes appear only as needed to justify the choice.

## Open questions

1. Envelope structure and KDF parameters — to the W3-D2 design gate (not evidenced by the first pass; the slice used random keys, not derived keys).
2. Custody form (passphrase / keyfile / both) — W3-D2 design gate with ADR 0005's user-experience lens.
3. The 16-byte reserved header — recommended for adoption as the format baseline at W3-D2 (evidenced trivial in two languages); confirm at the engine brief.
4. Cross-OS verification trigger — define at packaging/release planning, not before.
5. Native-shell revisit trigger — the review-package phase's kickoff should say whether the class re-enters evaluation there.

---

*The spine gets the quietest runtime the evidence could find: the one that wrote nothing it wasn't asked to write, carried three packages instead of eighty-nine, and told the truth about its one weakness. The record keeps that weakness in ink — which is the only place weaknesses stay harmless.*
