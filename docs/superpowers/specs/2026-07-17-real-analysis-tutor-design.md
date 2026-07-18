# Real Analysis Tutor — Claude Code Plugin Design

**Date:** 2026-07-17
**Status:** Approved by user (scope, repo target, Lean posture, architecture, name, license)
**Sources of truth:** `RealAnalysis_CompleteGuide_V2.1.docx` and `Setup_Workflow_Guide_V2.1.docx` (converted copies vendored in `docs/source-guides/`)

## 1. Purpose

A Claude Code plugin that operationalizes the V2.1 Real Analysis self-study methodology as an AI tutor. The tutor is Socratic by architecture, not by request: it never gives complete proofs, probes named misconceptions, escalates through research-grounded stuck-state protocols, tracks learner state across sessions, verifies mathematics with Lean 4 where available, and — critically — **volunteers every piece of usage information itself**. The learner never reads documentation about the tutor; the README covers installation only.

## 2. Decisions (locked)

| Decision | Choice |
|---|---|
| Scope | Subject-agnostic pedagogical engine + Real Analysis content pack (`curriculum/real-analysis/`) |
| Repo | **Private** GitHub repo `apollostream/real-analysis-tutor`, flip to public later at user's discretion |
| Name / version | Plugin `real-analysis-tutor`, semver starting `2.1.0` (matches guide version) |
| License | MIT |
| Lean 4 | Guided setup offered at onboarding; graceful degradation — tutoring fully functional without Lean; unverified proofs are marked and formalization re-offered later |
| Build process | Max agent fan-out (user's standing Rule 7); TDD for deterministic backend scripts (Rule 3) |

## 3. Architecture overview

Three cooperating layers, mirroring the guides' four-layer stack:

1. **Deterministic layer (hooks + scripts):** guarantees the things that must never depend on model judgment — state loading/saving, per-turn Socratic reinforcement, spaced-review scheduling, Lean compilation.
2. **Judgment layer (skills):** the pedagogy — six-stage tutoring loop, stuck-state escalation, four-part assessment, ledger discipline — encoded as skills with progressive-disclosure reference files.
3. **Fresh-context layer (subagents):** critic, counterexample hunter, misconception prober, Lean verifier, leakage auditor — each with deliberate information asymmetry (they see the artifact under review, never the tutor's reasoning), operationalizing the Setup Guide's role-script separation (`critic.sh`, `attack.sh`, …) with modern plugin machinery.

### Research grounding (from 2026 SOTA review)

- **Per-turn reminder injection** (UserPromptSubmit hook) counters instruction decay — the best-documented failure of LLM tutors; forced pedagogical pre-planning reduced answer leakage 46%→2% in adversarial benchmarks.
- **Separate-context verification** (MARCH): same-context self-checks inherit generator bias; critics get decomposed claims only.
- **Scheduler-in-code** (LECTOR/IntelliCode): the LLM grades recall quality; SM-2-family code computes intervals and due dates. Never LLM-improvised scheduling.
- **Sycophancy defenses** (EduFrameTrap): the tutor prompt names the four pressure patterns (authority claims, context-switch jargon, face-saving, direct endorsement) and treats "my professor said X" as a claim to check.
- **Stuck-counter in state**, not model-sensed affect: N failed attempts on a step triggers scaffolding-level changes deterministically.
- **LeanTutor precedent:** compiler failure is never presented as "you're wrong" (could be autoformalization failure); hedged feedback required.

## 4. Repository layout

```
real-analysis-tutor/
├── .claude-plugin/
│   ├── plugin.json                  # name, version 2.1.0, MIT, skills/agents/hooks paths
│   └── marketplace.json             # self-hosted single-plugin marketplace
├── skills/
│   ├── tutor/                       # THE front door; onboarding + open ritual + orchestration
│   │   ├── SKILL.md
│   │   └── reference/               # onboarding-interview.md, open-ritual.md, weekly-rhythm.md
│   ├── prime/SKILL.md               # Stage 1: concept priming + network positioning
│   ├── check-proof/SKILL.md         # Stage 3: line-by-line gap analysis; DO-NOT-REWRITE contract
│   ├── stuck/                       # Stuck-State Management System, Levels 1–4
│   │   ├── SKILL.md
│   │   └── reference/               # solow.md, dlmk-polya.md, reframes.md (Velleman/Eccles/Hammack)
│   ├── formalize/SKILL.md           # Stage 4: Lean 4 loop (lake build, error interpretation)
│   ├── attack/SKILL.md              # Stage 5: counterexample & converse via fresh subagent
│   ├── assess/SKILL.md              # Stage 6: Four-Part Consolidation Assessment
│   ├── ledger/SKILL.md              # Theorem Ledger V2.1 update + quiz-from-ledger
│   ├── review/SKILL.md              # monthly consolidation, error-pattern analysis, dependency graph
│   └── setup/SKILL.md               # environment doctor + guided Lean/Mathlib install (Setup Guide III–IV)
├── agents/
│   ├── proof-critic.md              # fresh-context critic; read-only tools
│   ├── counterexample-hunter.md     # attack role; hypothesis-removal probes
│   ├── misconception-prober.md      # presents catalogue entry as plausible argument
│   ├── lean-verifier.md             # writes .lean, runs lake build, interprets errors
│   └── leakage-auditor.md           # scores drafted tutor feedback for answer-revealing
├── hooks/
│   ├── hooks.json
│   └── scripts/
│       ├── session_start.py         # load state + due reviews → additionalContext; first-run detection
│       ├── prompt_guard.py          # per-turn Socratic contract; escalation on answer-fishing patterns
│       └── session_end.py           # state-serialization reminder
├── engine/                          # deterministic Python, subject-agnostic, TDD'd
│   ├── state.py                     # learner.json CRUD (versioned schema)
│   ├── scheduler.py                 # SM-2/FSRS-lite intervals; LLM supplies grade 0–5 only
│   └── ledger.py                    # ledger.json / error_log.json append + query helpers
├── curriculum/
│   └── real-analysis/
│       ├── curriculum.yaml          # phases Prelim–9: topics, texts-in-order, durations, focus notes
│       ├── misconceptions.yaml      # seven-topic catalogue: name, corrupted step, refutation, counterexample
│       ├── checklists/              # phase1..phase8.yaml: mastery items, converse checks, Lean targets, Rudin exercises
│       ├── ladder.yaml              # five rungs: problem classes + Claude's role per rung + Bloom mapping
│       ├── ledger-schema.yaml       # Theorem Ledger V2.1 field definitions
│       └── pedagogy/                # bloom.md, polya.md, self-explanation.md, texts.md (book survey + pairing rules)
├── templates/
│   └── workspace/                   # scaffold for learner workspace (see §6)
├── tests/                           # pytest: engine/*, hook scripts, curriculum YAML schema validation
├── .github/workflows/ci.yml        # pytest + claude plugin validate + YAML lint
├── docs/
│   ├── superpowers/specs/           # this spec + plan
│   └── source-guides/               # markdown conversions of the two V2.1 docx guides (provenance)
├── README.md                        # install instructions ONLY + "the tutor teaches you everything else"
├── CHANGELOG.md
└── LICENSE                          # MIT
```

## 5. Component specifications

### 5.1 `/tutor` skill (front door)

- **First run** (no `learner.json` in workspace): onboarding interview mapped from the guide's Quick-Start student profiles (new to proofs / some proof experience / proof-fluent / revisiting for grad prep) → sets starting phase; creates workspace from `templates/workspace/`; detects Lean (`lake --version`), offers guided setup via `/real-analysis-tutor:setup`, proceeds happily without it; ends with a 60-second orientation the tutor *speaks* (what sessions look like, what it will and won't do — "I will never hand you a proof"), and starts Stage 1 on the learner's first topic.
- **Every subsequent run:** open ritual — greet; state summary (phase, chapter, rung, streak); due reviews from `scheduler.py`; propose today's agenda from the weekly-rhythm day mapping; then follow the six-stage loop, invoking sibling skills as stages are reached.
- Session close: Pólya Look Back, ledger/error-log updates, next-session preview, state save.
- The skill embeds the **hidden pre-response plan** rubric (diagnosis → scaffolding level → withhold-list → the one question) the tutor must run before every pedagogical reply.

### 5.2 Pedagogy skills

Each is small, single-responsibility, model-invocable (the tutor triggers them at the right stage) *and* user-invocable (power users can call them directly, but nothing requires it):

- **prime:** network positioning question, informal-image audit, intuition surfacing. Refuses to reveal theorem content.
- **check-proof:** the guide's Stage 3 contract verbatim: line-by-line; justification complete? follows from prior? hypotheses of cited theorems verified? delta depends only on epsilon? Flags every "clearly"/"obviously". Never rewrites. Errors are categorized into the six Error Log categories and appended via `ledger.py`.
- **stuck:** strict Level 1→4 escalation. L1 Solow Forward-Backward; L2 D-L-M-K + six Pólya steps in order (analogy step gated on Phase ≥4 per the guide); L3 the three Framework Reframes; L4 direct conceptual intervention only after documented failure of 1–3. Level transitions recorded in `learner.json` stuck counters.
- **formalize:** Lean loop with the guide's proof-style conventions (tactic mode, linarith/norm_num preferences, `exact?` for lemma names, ≤3 tactic variations before asking direction). Absent Lean: marks ledger entry `lean_status: unverified`, offers setup.
- **attack:** dispatches `counterexample-hunter` with only the theorem + proof text. Hypothesis-removal probes, converse check, misconception-reliance check.
- **assess:** Four-Part Consolidation in fixed order (applied problem → conceptual/quantifier question → derivation step → misconception check); refuses to skip to part 4; grades recall for `scheduler.py`; updates Bloom-level-achieved in ledger.
- **ledger:** V2.1 entry creation (all 14 fields incl. misconception + refutation), quiz-from-ledger mode.
- **review:** monthly consolidation — full-ledger quiz, error-pattern analysis ("most common category across last 20 proofs"), dependency-graph re-mapping, misconception re-checks across all studied topics.
- **setup:** environment doctor; guided elan/Lean/Mathlib/VS Code walk-through operationalizing Setup Guide Parts II–IV (WSL 2 guidance included but platform-detected; native Linux/macOS paths too).

### 5.3 Subagents

All read-only tool sets except `lean-verifier` (needs Write+Bash for `.lean` files and `lake build`). Each prompt states its information diet explicitly (what it must NOT be told). `leakage-auditor` scores drafted feedback against the MRBench-style dimensions with a hard gate on "reveals the answer."

### 5.4 Hooks

- **SessionStart** (`session_start.py`, <1 s): locate workspace (marker file `.ra-tutor-workspace` walked up from cwd, else configured path in `~/.claude/real-analysis-tutor.json`); emit additionalContext: learner state digest, due reviews, current phase focus + named misconception for the phase, and the standing instruction *"On the user's first message this session, whatever it says, first deliver the session-open ritual."* If no workspace: emit first-run onboarding directive instead. If not a tutoring context (no workspace and user is doing unrelated work), emit nothing — the plugin must be a good citizen.
- **UserPromptSubmit** (`prompt_guard.py`): when a workspace is active, append the 2–3 line Socratic contract ("Still Socratic mode. Do not reveal the next proof step. One question per turn. Pre-plan: diagnosis → level → withhold → question."). Regex escalation tier for answer-fishing ("just tell me", "give me the answer/proof/solution", authority-pressure phrases) → stronger reminder naming the guide's overriding rule. No workspace → no-op (zero overhead outside tutoring).
- **Stop/SessionEnd** (`session_end.py`): if ledger/error-log/state changed flags are pending, remind to serialize; append session narrative pointer.

### 5.5 Engine scripts (TDD scope)

- `state.py`: schema-versioned `learner.json` (per-concept mastery 0–1, Bloom level, misconception-vulnerability log with evidence quotes, stuck counters, preferences, phase/chapter/rung position). Atomic writes.
- `scheduler.py`: SM-2 with FSRS-style ease adjustments; API: `due(date)`, `record_review(concept, grade)`; intervals computed in code only.
- `ledger.py`: append/query for `ledger.json` and `error_log.json`; six error categories enforced.

Tests: pytest for all engine modules + `prompt_guard.py` pattern tiers + YAML schema validation of every curriculum file + a fidelity test asserting all seven misconceptions and all phase tables match a checked-in extraction of the guides. CI runs tests + `claude plugin validate`.

### 5.6 Curriculum content pack

Faithful encodings (not paraphrases) of: Part IV chapter alignment; Part V checklists incl. converse checks, misconception entries (occurrence step + precise refutation + canonical counterexample), Lean targets, key Rudin exercises, Example/Non-Example rule; Part VI ladder with Claude's role per rung; Part VIII master plan; Part XIII weekly rhythm; Part IX prompts (quantifier check, delta-x diagnostic, hypothesis audit, converse check, misconception check, compactness interrogation, knowledge graph, adversarial sequence, informal-image audit) as the tutor's internal move library; text survey and the three iron sequencing rules (Alcock → Strichartz → Rudin; never reverse; Munkres supplement at Phase 2).

### 5.7 Learner workspace (created by tutor, never by hand)

```
<workspace>/
├── .ra-tutor-workspace         # marker (JSON: schema version, curriculum id)
├── learner.json  ├── ledger.json  ├── error_log.json  ├── reviews.json
├── sessions/NNN.md             # narrative session log
├── src/ChapterN.lean  ├── notes/chN.md  └── scratch/lookup.lean
```

CLAUDE.md is intentionally NOT written into the workspace — hooks supply context; this avoids drift between plugin versions and stale workspace files.

## 6. Zero-documentation UX contract

1. README teaches installation only; final line: "Open Claude Code and say hello — the tutor takes it from there."
2. SessionStart guarantees the tutor speaks first-in-effect (open ritual on first user message).
3. Every capability is offered at the moment it becomes relevant (Lean setup when formalization first arises; `/review` when a month of entries exists; voice/Unicode input tips when the learner first types math painfully).
4. The tutor explains *why* it is withholding answers the first time a learner pushes, citing the productive-struggle rule in plain language — the contract is negotiated openly, once.
5. All slash commands are conveniences, not requirements; the tutor names them as shortcuts after the learner has experienced the behavior once.

## 7. Error handling

- Missing/corrupt state files: engine scripts back up the corrupt file, regenerate from schema, tutor tells the learner what happened.
- Lean failures: never equated with mathematical wrongness (LeanTutor rule); hedged language mandated.
- Hook scripts: fail-open (exit 0 with no output on any internal error) so tutoring is never blocked by harness bugs; errors logged to `${CLAUDE_PLUGIN_DATA}/errors.log`.
- Guide-fidelity drift: CI fidelity tests pin curriculum data to the source-guide extraction.

## 8. Build & delivery plan (summary)

1. Scaffold repo, manifest, CI; engine scripts TDD-first.
2. Fan-out authoring: parallel subagents write curriculum YAML per phase and skills per style contract; adversarial verification stage checks fidelity to the guides and leakage-resistance of tutor prompts.
3. `claude plugin validate` + local install smoke test (first-run onboarding, open ritual, stuck escalation, assessment).
4. Private GitHub repo `apollostream/real-analysis-tutor`; push; tag v2.1.0.

## 9. Out of scope (v2.1.0)

- API Proof Studio web app (Setup Guide Part XII) — the plugin supersedes most of it; revisit later.
- Topology/Abstract Algebra content packs (engine supports them; content not researched per guide Part XV).
- MCP server, channels, statusline, output styles — deferred until a concrete need appears.
- Automated Windows/WSL installer execution — setup skill guides; it does not run `wsl --install` for the user.
