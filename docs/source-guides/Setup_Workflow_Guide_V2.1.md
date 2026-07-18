**Low-Friction Setup**

**& Workflow Guide**

Revised & Expanded Edition --- Version 2.1

Windows 11 · Real Analysis · Lean 4 · Claude Code

Complete laptop configuration for mathematical proof study

WSL 2 · Lean 4 + Mathlib4 · VS Code · Claude Code

Integrated with Real Analysis Complete Study Guide V2.1

Pedagogical Frameworks: Solow · Pólya · Bloom · Misconception Catalogue

Six-Stage Socratic Tutoring Loop · Four-Part Consolidation Assessment

Mathematical Input · Voice Dictation · API Proof Studio

Future: Topology & Abstract Algebra

This guide captures every detail needed to configure a Windows 11 laptop
as a complete mathematical proof study environment, fully integrated
with the Real Analysis Complete Study Guide V2.1. It covers the full
software installation sequence, persistent context files with embedded
pedagogical frameworks (Solow, Pólya, Bloom) and the Misconception
Catalogue, role scripts including a dedicated misconception probe, the
six-stage Socratic tutoring loop with the Four-Part Consolidation
Assessment, the weekly study rhythm, mathematical input, the optional
API proof studio, and extension to Topology and Abstract Algebra. All
commands are specific to Windows 11 with WSL 2.

> **Contents**

**Part I** Architecture Overview --- The Four-Layer Stack

**Part II** The Critical First Decision --- WSL 2 vs Native Windows

**Part III** Complete Installation --- Step by Step

**Part IV** Project Structure & Persistent Context

**Part V** The CLAUDE.md File --- Full Version 2.1 Template

**Part VI** Role Scripts & Automation

**Part VII** The Study Methodology --- Three Pedagogical Frameworks

**Part VIII** The Reading Plan --- All Phases with Computer Integration

**Part IX** The Proof Session Workflow --- Six-Stage Tutoring Loop

**Part X** The Weekly Study Rhythm

**Part XI** Mathematical Input --- Typing, Voice & Symbols

**Part XII** The API-Based Proof Studio

**Part XIII** Session Commands & Complete Tutor Prompts Reference

**Part XIV** Master Setup Checklist

**Part XV** Future Subjects --- Topology & Abstract Algebra

> **Part I --- Architecture Overview --- The Four-Layer Stack**

The entire workflow rests on four layers. Understanding what each layer
does prevents over-engineering and keeps setup minimal. Version 2 adds a
pedagogical layer at the base --- the study methodology that governs how
you interact with the tools.

  -----------------------------------------------------------------------
  **Layer**          **Tool**                **Function / Daily Use**
  ------------------ ----------------------- ----------------------------
  Layer 0 ---        Real Analysis Study     Governs HOW you study: the
  Pedagogy           Guide V2 + Solow +      six-stage tutoring loop,
                     Pólya + Bloom           proof-practice ladder,
                                             weekly rhythm, mastery
                                             checklists, Theorem Ledger.
                                             \~10 min planning.

  Layer 1 ---        Claude chat or Claude   Proof outlining, Socratic
  Strategy &         Code terminal           tutoring, counterexample
  Intuition                                  hunting, gap analysis, Pólya
                                             recovery protocol. No file
                                             access required. \~70% of
                                             daily time.

  Layer 2 --- Proof  Claude Code in WSL 2    With your actual .lean and
  Checking           terminal                .md files open. Writes Lean
                                             proofs, runs lake build,
                                             reads compiler errors,
                                             revises. CLAUDE.md provides
                                             full session context
                                             automatically. \~20% of
                                             daily time.

  Layer 3 --- Formal Lean 4 compiler +       The infallible ground truth.
  Verification       Mathlib4 (free)         A proof that compiles is
                                             correct by construction.
                                             Claude tells you what is
                                             wrong; the compiler tells
                                             you WHETHER it is wrong.
                                             \~10% of daily time.
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  **The key integration:** VS Code is needed specifically for the Lean 4
  infoview --- the panel showing live proof state as you type. There is
  no terminal equivalent. Everything else (file editing, running lake
  build, Socratic tutoring) happens in the Claude Code terminal. VS Code
  is a proof state viewer, not a traditional IDE.

  -----------------------------------------------------------------------

The pedagogical layer (Layer 0) is what distinguishes this setup from a
generic Lean installation. The CLAUDE.md file (Part V) embeds the full
tutoring framework --- Solow\'s Forward-Backward method, Pólya\'s
recovery protocol, Bloom\'s Taxonomy, and the Misconception Catalogue
--- so that every Claude Code session automatically applies
research-grounded pedagogy without manual setup.

> **Part II --- The Critical First Decision --- WSL 2 vs Native
> Windows**

Claude Code on Windows 11 supports three modes: WSL 2, WSL 1, and native
Git for Windows. For this specific workflow --- Real Analysis, Lean 4,
Claude Code --- WSL 2 is the correct choice.

  -----------------------------------------------------------------------
  **Criterion**         **WSL 2 (Recommended)**  **Native Git for
                                                 Windows**
  --------------------- ------------------------ ------------------------
  Lean 4 toolchain      Native Linux --- works   Works but rougher edges
                        perfectly                

  Shell scripts from    Work exactly as written  Need adaptation to .ps1
  this guide                                     or .bat

  Claude Code           Full support ---         Supported but fewer
                        recommended path         features

  lake build            Fast --- native          Slower on Windows
  performance           filesystem               filesystem

  Setup complexity      One command: wsl         Multiple separate
                        \--install               installs

  VS Code integration   Seamless via WSL         Direct --- also seamless
                        extension                

  Role scripts (critic, Run without modification Require rewriting as
  attack)                                        .bat or .ps1
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  **Windows 11 decision:** Use WSL 2. The shell scripting, Lean 4
  toolchain, and Claude Code all work without modification in WSL 2.
  Every command in this guide is written for WSL 2 / Ubuntu.

  -----------------------------------------------------------------------

> **Part III --- Complete Installation --- Step by Step**

Installation order matters. Complete each step fully before proceeding
to the next. Total time from fresh Windows 11: approximately 90 minutes,
most of which is waiting for the Mathlib binary cache to download.

**Step 1 --- Enable WSL 2**

Open PowerShell as Administrator: right-click Start → Terminal (Admin).

+-----------------------------------------------------------------------+
| PowerShell (Administrator)                                            |
|                                                                       |
| wsl \--install                                                        |
|                                                                       |
| \# This installs WSL 2 and Ubuntu automatically on Windows 11.        |
|                                                                       |
| \# Restart your computer when prompted.                               |
|                                                                       |
| \# After restart, Ubuntu opens and asks for username and password.    |
|                                                                       |
| \# Verify WSL 2 is running:                                           |
|                                                                       |
| wsl \--status                                                         |
|                                                                       |
| \# Should show: Default Version: 2                                    |
+-----------------------------------------------------------------------+

From this point forward, all commands run inside WSL 2 --- not in
PowerShell. Open Ubuntu from the Start menu or type wsl in any terminal.

**Step 2 --- Install VS Code on Windows**

Download and install VS Code from code.visualstudio.com --- use the
Windows installer directly, not inside WSL. After installation, install
these extensions (Ctrl+Shift+X):

+-----------------------------------------------------------------------+
| VS Code Extensions (Ctrl+Shift+X)                                     |
|                                                                       |
| WSL by Microsoft \-- connects VS Code into WSL 2                      |
|                                                                       |
| Lean 4 by leanprover \-- inline proof state and infoview              |
|                                                                       |
| GitLens optional \-- git history visualization                        |
+-----------------------------------------------------------------------+

The WSL extension makes VS Code operate inside your Linux environment
while running on Windows. The green WSL: Ubuntu indicator in the
bottom-left corner confirms it is active.

**Step 3 --- Install Prerequisites in WSL 2**

+-----------------------------------------------------------------------+
| WSL 2 / Ubuntu Terminal                                               |
|                                                                       |
| sudo apt update && sudo apt upgrade -y                                |
|                                                                       |
| sudo apt install -y git curl build-essential                          |
|                                                                       |
| \# Verify                                                             |
|                                                                       |
| git \--version                                                        |
|                                                                       |
| curl \--version                                                       |
+-----------------------------------------------------------------------+

**Step 4 --- Install elan and Lean 4**

elan is the Lean version manager --- it automatically manages the
correct Lean version per project.

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| curl https://elan.lean-lang.org/elan-init.sh -sSf \| sh               |
|                                                                       |
| source \~/.profile                                                    |
|                                                                       |
| elan \--version                                                       |
|                                                                       |
| lean \--version                                                       |
+-----------------------------------------------------------------------+

**Step 5 --- Create Your Mathlib Project**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| cd \~/Documents                                                       |
|                                                                       |
| mkdir -p projects                                                     |
|                                                                       |
| cd projects                                                           |
|                                                                       |
| lake +v4.24.0 new real-analysis-lean math                             |
|                                                                       |
| cd real-analysis-lean                                                 |
|                                                                       |
| lake update                                                           |
|                                                                       |
| \# CRITICAL: Download pre-compiled Mathlib binaries.                  |
|                                                                       |
| lake exe cache get                                                    |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
  **Do NOT skip lake exe cache get.** Without it, your first lake build
  compiles all of Mathlib from source --- several hours. With it,
  everything is ready in minutes.

  -----------------------------------------------------------------------

**Step 6 --- Open Project in VS Code and Verify Lean**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| code .                                                                |
|                                                                       |
| VS Code \-- create src/Test.lean to verify the full stack             |
|                                                                       |
| import Mathlib.Analysis.SpecificLimits.Basic                          |
|                                                                       |
| example : Filter.Tendsto (fun n : Nat =\> (1 : Real) / n)             |
|                                                                       |
| Filter.atTop (nhds 0) := by                                           |
|                                                                       |
| exact?                                                                |
+-----------------------------------------------------------------------+

The Lean infoview panel (right side of VS Code) should show proof state
and exact? suggestions within 30 seconds as Mathlib loads. Once a goal
appears, your Lean + Mathlib stack is fully operational.

**Step 7 --- Install Claude Code**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| curl -fsSL https://claude.ai/install.sh \| bash                       |
|                                                                       |
| claude doctor                                                         |
|                                                                       |
| claude                                                                |
+-----------------------------------------------------------------------+

The OAuth authentication prompt opens a browser on your Windows desktop.
Log in with your Claude.ai account. Claude Code requires a Claude Pro or
Max subscription, or direct API access via the Anthropic Console.

> **Part IV --- Project Structure & Persistent Context**

The project directory structure is where low friction is actually
achieved. A well-organized project means every Claude Code session
starts with full context automatically. Version 2 adds study methodology
files: mastery checklists per chapter, the V2.1 Theorem Ledger
(including the Misconception field), and the Error Log.

**Directory Structure**

Project root: \~/Documents/projects/real-analysis-lean/

+-----------------------------------------------------------------------+
| real-analysis-lean/                                                   |
|                                                                       |
| \|\-- CLAUDE.md \<- Claude Code reads this automatically every        |
| session                                                               |
|                                                                       |
| \|\-- lakefile.lean \<- Lean project config (auto-generated)          |
|                                                                       |
| \|\-- lake-manifest.json \<- Mathlib version lock (auto-generated)    |
|                                                                       |
| \|\-- app.py \<- Optional: API Proof Studio (Part XII)                |
|                                                                       |
| \|\-- Makefile \<- One-word access to all workflows                   |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- src/                                                            |
|                                                                       |
| \| \|\-- Chapter1.lean \<- Real Numbers                               |
|                                                                       |
| \| \|\-- Chapter2.lean \<- Basic Topology                             |
|                                                                       |
| \| \|\-- \... \<- One file per chapter                                |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- notes/                                                          |
|                                                                       |
| \| \|\-- ch1.md \<- Prose notes per chapter                           |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- checklists/                                                     |
|                                                                       |
| \| \|\-- ch1_checklist.md \<- Mastery checklist per chapter (includes |
| Misconception entry)                                                  |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- scratch/                                                        |
|                                                                       |
| \| \|\-- lookup.lean \<- Always-ready lemma lookup file               |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- scripts/                                                        |
|                                                                       |
| \| \|\-- critic.sh \<- Fresh-context proof critic role                |
|                                                                       |
| \| \|\-- attack.sh \<- Counterexample finder role                     |
|                                                                       |
| \| \|\-- polya.sh \<- Polya recovery protocol role                    |
|                                                                       |
| \| \|\-- bloom.sh \<- Bloom-level assessment role                     |
|                                                                       |
| \| \|\-- launch.sh \<- Smart launcher with auto file discovery        |
|                                                                       |
| \| \|\-- prompts/                                                     |
|                                                                       |
| \| \|\-- quantifier_check.md                                          |
|                                                                       |
| \| \|\-- delta_check.md                                               |
|                                                                       |
| \| \|\-- converse_check.md                                            |
|                                                                       |
| \| \|\-- misconception_check.md \<- NEW v2.1                          |
|                                                                       |
| \|                                                                    |
|                                                                       |
| \|\-- ledger.json \<- Theorem Ledger V2.1 (auto-updated, incl.        |
| misconception field)                                                  |
|                                                                       |
| \|\-- error_log.json \<- Error Log (auto-updated)                     |
+-----------------------------------------------------------------------+

**Building the Structure**

+-----------------------------------------------------------------------+
| WSL 2 Terminal \-- run from inside your project directory             |
|                                                                       |
| cd \~/Documents/projects/real-analysis-lean                           |
|                                                                       |
| mkdir -p src notes checklists scratch scripts/prompts                 |
|                                                                       |
| touch src/Chapter1.lean src/Chapter2.lean src/Chapter3.lean           |
|                                                                       |
| touch notes/ch1.md notes/ch2.md notes/ch3.md                          |
|                                                                       |
| touch checklists/ch1_checklist.md checklists/ch2_checklist.md         |
|                                                                       |
| cat \> scratch/lookup.lean \<\< \'EOF\'                               |
|                                                                       |
| import Mathlib                                                        |
|                                                                       |
| example (a b : Real) (ha : 0 \< a) (hb : a ≤ b) : 0 \< b := by        |
|                                                                       |
| exact?                                                                |
|                                                                       |
| EOF                                                                   |
|                                                                       |
| echo \"\[\]\" \> ledger.json                                          |
|                                                                       |
| echo \"\[\]\" \> error_log.json                                       |
+-----------------------------------------------------------------------+

> **Part V --- The CLAUDE.md File --- Full Version 2.1 Template**

CLAUDE.md is the most important file in your project. Claude Code reads
it automatically at the start of every session, eliminating the need to
re-establish context. Version 2.1 embeds the full pedagogical framework:
Solow\'s Forward-Backward method, Pólya\'s recovery protocol, Bloom\'s
Taxonomy, Alcock\'s self-explanation protocol, and the Misconception
Catalogue. Update the Current Phase line as you progress.

+-----------------------------------------------------------------------+
| CLAUDE.md \-- save to project root                                    |
|                                                                       |
| \# Real Analysis Proof Project \-- Version 2.1                        |
|                                                                       |
| \# Windows 11 / WSL 2 / Ubuntu                                        |
|                                                                       |
| \# Integrated with Real Analysis Complete Study Guide V2.1            |
|                                                                       |
| \## Environment                                                       |
|                                                                       |
| \- OS: Windows 11 with WSL 2 (Ubuntu)                                 |
|                                                                       |
| \- Lean 4 + Mathlib4                                                  |
|                                                                       |
| \- Build command: lake build                                          |
|                                                                       |
| \- Single file check: lean \--run src/Filename.lean                   |
|                                                                       |
| \- Mathlib cache refresh: lake exe cache get                          |
|                                                                       |
| \- VS Code: open with \"code .\" from project root in WSL 2           |
|                                                                       |
| \## Current Phase (UPDATE AS YOU PROGRESS)                            |
|                                                                       |
| \- Reading plan phase: \[e.g., Phase 1 \-- Real Numbers\]             |
|                                                                       |
| \- Strichartz chapter: \[e.g., Ch.1 \-- Real Numbers & Completeness\] |
|                                                                       |
| \- Rudin chapter: \[e.g., Ch.1 \-- The Real and Complex Number        |
| Fields\]                                                              |
|                                                                       |
| \- Alcock chapter: \[e.g., Ch.10 \-- Real Numbers\]                   |
|                                                                       |
| \- Proof ladder rung: \[e.g., Rung 2 \-- Structural\]                 |
|                                                                       |
| \- Current focus: \[e.g., Archimedean property, supremum arguments\]  |
|                                                                       |
| \## Tutor Mode \-- Core Instructions (Socratic by default)            |
|                                                                       |
| \- Ask me questions before explaining anything                        |
|                                                                       |
| \- Never give a complete proof unless I have made a genuine attempt   |
| first                                                                 |
|                                                                       |
| \- When I give you a proof, find the weakest step and ask me to       |
| justify it                                                            |
|                                                                       |
| \- Do NOT rewrite my proof \-- identify problems only                 |
|                                                                       |
| \- Flag every use of \"clearly\" or \"obviously\" \-- make me justify |
| those steps                                                           |
|                                                                       |
| \- Tell me honestly: wrong vs incomplete vs correct but inelegant     |
|                                                                       |
| \## Misconception Probe (NEW v2.1)                                    |
|                                                                       |
| \- For every theorem, probe the named misconception in the Ledger     |
|                                                                       |
| before the session ends                                               |
|                                                                       |
| \- Present the misconception as a plausible student argument, not as  |
|                                                                       |
| a flagged error \-- the student should not be told in advance which   |
|                                                                       |
| part is wrong                                                         |
|                                                                       |
| \- Ask me to identify the precise logical step that is invalid, not   |
|                                                                       |
| just to recognise that something is wrong                             |
|                                                                       |
| \- Require the canonical counterexample as part of a complete answer  |
|                                                                       |
| \- If I cannot locate the error, escalate by asking what the argument |
|                                                                       |
| would need to be true for it to work \-- do not reveal the answer     |
|                                                                       |
| \## Alcock Self-Explanation Protocol                                  |
|                                                                       |
| \- Before I proceed to the next line of any proof, prompt me:         |
|                                                                       |
| \(1\) Do you understand the ideas used in this line?                  |
|                                                                       |
| \(2\) Do you understand WHY those ideas were used?                    |
|                                                                       |
| \(3\) Can you explain this line in terms of earlier ideas?            |
|                                                                       |
| \- Goal: I apply this independently without prompting by Phase 3      |
|                                                                       |
| \## For Every New Definition                                          |
|                                                                       |
| \- Ask me to construct one example satisfying the definition          |
|                                                                       |
| \- Ask me to construct one example FAILING it (violating exactly one  |
| condition)                                                            |
|                                                                       |
| \- Do this BEFORE discussing any theorem                              |
|                                                                       |
| \## For Every New Theorem                                             |
|                                                                       |
| \- Ask me: is the converse true?                                      |
|                                                                       |
| \- If false: ask for the canonical counterexample                     |
|                                                                       |
| \- Ask: which hypothesis is load-bearing?                             |
|                                                                       |
| \- Ask: what breaks if each hypothesis is removed?                    |
|                                                                       |
| \- Probe the named misconception (see Misconception Probe above)      |
|                                                                       |
| \## Polya Recovery Protocol (when I am stuck)                         |
|                                                                       |
| \- Apply these in order; move to next only if previous fails:         |
|                                                                       |
| Step 1: What happens in the simplest non-trivial case?                |
|                                                                       |
| Step 2: What would I need to already have for this argument to work?  |
|                                                                       |
| Step 3: Have I proved anything with a similar logical form? (check    |
| Ledger)                                                               |
|                                                                       |
| Step 4: Can I remove a condition and solve a simpler version first?   |
|                                                                       |
| Step 5: Is there a function, sequence, or set I could introduce?      |
|                                                                       |
| Step 6: Which earlier Ledger entry might apply here?                  |
|                                                                       |
| \- NOTE: Step 3 (analogy) requires a repertoire.                      |
|                                                                       |
| Prefer Steps 1, 2, 4 in Phases 1-2. From Phase 4 onward, use all      |
| steps.                                                                |
|                                                                       |
| \## Bloom Taxonomy \-- Escalate Through Levels                        |
|                                                                       |
| \- After Remember/Understand questions, push to:                      |
|                                                                       |
| Apply: verify a specific example against the definition               |
|                                                                       |
| Analyze: identify which hypothesis is load-bearing                    |
|                                                                       |
| Evaluate: is my proof the minimum correct argument?                   |
|                                                                       |
| Create: construct an object with prescribed properties                |
|                                                                       |
| \## Four-Part Consolidation Assessment (NEW v2.1)                     |
|                                                                       |
| \- At the end of every topic session, run all four parts in order:    |
|                                                                       |
| \(1\) Applied problem \-- non-trivial epsilon-delta or construction   |
| task                                                                  |
|                                                                       |
| \(2\) Conceptual question \-- target quantifier structure or logical  |
| form                                                                  |
|                                                                       |
| \(3\) Derivation step \-- reconstruct a key lemma from logical        |
| structure,                                                            |
|                                                                       |
| not from memorised sequence                                           |
|                                                                       |
| \(4\) Misconception check \-- present the named misconception as a    |
|                                                                       |
| plausible student argument; require precise refutation                |
|                                                                       |
| \- Do not skip to (4) early or treat it as optional \-- it is the     |
| part                                                                  |
|                                                                       |
| that does the most diagnostic work                                    |
|                                                                       |
| \## Proof Style Conventions (Lean 4)                                  |
|                                                                       |
| \- Always use tactic mode, never term mode unless I specify           |
|                                                                       |
| \- Prefer linarith for inequality chains                              |
|                                                                       |
| \- Prefer norm_num for numerical goals                                |
|                                                                       |
| \- Use exact? when unsure of lemma name \-- never guess a name        |
|                                                                       |
| \- Use apply? when unsure which theorem to apply                      |
|                                                                       |
| \- Import Mathlib.Analysis.SpecificLimits.Basic for limit proofs      |
|                                                                       |
| \- Import Mathlib.Topology.MetricSpace.Basic for metric space proofs  |
|                                                                       |
| \- Import Mathlib.Data.Real.Basic for basic real number facts         |
|                                                                       |
| \## Workflow Rules (Claude Code)                                      |
|                                                                       |
| \- Run lake build after every proof attempt before reporting results  |
|                                                                       |
| \- Try at most 3 tactic variations before asking me for direction     |
|                                                                       |
| \- Always report what was tried and why it failed before asking       |
|                                                                       |
| \- If a lemma name fails, use exact? to find the correct current name |
|                                                                       |
| \- Read scratch/lookup.lean output when searching for lemma names     |
|                                                                       |
| \## Targeted Diagnostic Prompts (apply automatically when relevant)   |
|                                                                       |
| \- Quantifier: write statement with ALL quantifiers explicit          |
|                                                                       |
| \- Delta-x: does my delta depend on x or only on epsilon?             |
|                                                                       |
| \- Hypothesis: have I verified every hypothesis of every cited        |
| theorem?                                                              |
|                                                                       |
| \- Converse: is the converse of this theorem true?                    |
|                                                                       |
| \- Misconception: does this argument rely on the named misconception  |
|                                                                       |
| for this topic? (see ledger.json misconception field)                 |
|                                                                       |
| \- Compact: have I verified the set is actually compact?              |
|                                                                       |
| \- Image: what is my informal picture of this concept?                |
|                                                                       |
| (find the example that breaks it before formalizing)                  |
|                                                                       |
| \## Key Texts (for context)                                           |
|                                                                       |
| \- Primary rigour: Rudin, Principles of Mathematical Analysis         |
|                                                                       |
| \- Motivation: Strichartz, The Way of Analysis                        |
|                                                                       |
| \- Metacognitive prep: Alcock, How to Think About Analysis            |
|                                                                       |
| \- Topology supplement: Munkres, Topology Ch.2 (Phase 2)              |
|                                                                       |
| \- Proof foundations: Solow -\> Hammack -\> Eccles sequence           |
|                                                                       |
| \## Theorem Ledger V2.1                                               |
|                                                                       |
| \- Stored in: ledger.json                                             |
|                                                                       |
| \- Fields: theorem, statement, proof_idea, load_bearing_hypothesis,   |
|                                                                       |
| counterexample_if_removed, converse_true, converse_example,           |
|                                                                       |
| misconception, misconception_refutation, depends_on, downstream,      |
|                                                                       |
| analogues, lean_status, bloom_level                                   |
|                                                                       |
| \## Error Log                                                         |
|                                                                       |
| \- Stored in: error_log.json                                          |
|                                                                       |
| \- Categories: quantifier_error, missing_hypothesis,                  |
| invalid_inference,                                                    |
|                                                                       |
| wrong_theorem, delta_depends_on_x, converse_confusion                 |
|                                                                       |
| \- Analyze patterns monthly: \"What is my most common error type?\"   |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| WSL 2 Terminal \-- create CLAUDE.md                                   |
|                                                                       |
| cd \~/Documents/projects/real-analysis-lean                           |
|                                                                       |
| code CLAUDE.md \# opens in VS Code \-- paste content above, save      |
|                                                                       |
| \# Update the Current Phase line every session                        |
+-----------------------------------------------------------------------+

> **Part VI --- Role Scripts & Automation**

These scripts eliminate session management friction. Each launches a
fresh Claude Code session with a specific role, the right file context,
and correct instructions. Role separation is architecturally enforced by
separate processes rather than just requested by prompt.

**scripts/critic.sh --- Fresh-Context Proof Critic**

+-----------------------------------------------------------------------+
| scripts/critic.sh                                                     |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/critic.sh src/Chapter3.lean                       |
|                                                                       |
| CHAPTER=\${1:-\"src/Chapter3.lean\"}                                  |
|                                                                       |
| claude \--print \\                                                    |
|                                                                       |
| \"You are a proof critic reviewing \$CHAPTER.                         |
|                                                                       |
| Find every implicit step, every unjustified claim,                    |
|                                                                       |
| every use of \'clearly\' or \'obviously\'.                            |
|                                                                       |
| Check quantifier ordering on every convergence and continuity proof.  |
|                                                                       |
| Check that delta does not depend on x in any continuity proof.        |
|                                                                       |
| Check: for every theorem used, are ALL hypotheses verified?           |
|                                                                       |
| Check: for every conditional theorem, note whether converse is        |
| addressed.                                                            |
|                                                                       |
| Check: does the argument rely on a known named misconception for      |
|                                                                       |
| this topic? Flag it explicitly if so.                                 |
|                                                                       |
| Do NOT rewrite anything.                                              |
|                                                                       |
| Report problems ordered from most serious to least serious.\"         |
+-----------------------------------------------------------------------+

**scripts/attack.sh --- Counterexample Finder**

+-----------------------------------------------------------------------+
| scripts/attack.sh                                                     |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/attack.sh src/Chapter3.lean                       |
|                                                                       |
| CHAPTER=\${1:-\"src/Chapter3.lean\"}                                  |
|                                                                       |
| claude \--print \\                                                    |
|                                                                       |
| \"You are searching for counterexamples to the proofs in \$CHAPTER.   |
|                                                                       |
| For each major theorem:                                               |
|                                                                       |
| 1\. Try to construct a case where the argument fails if one           |
| hypothesis                                                            |
|                                                                       |
| is weakened or removed.                                               |
|                                                                       |
| 2\. Check whether the converse is true. If false, construct a         |
|                                                                       |
| canonical counterexample.                                             |
|                                                                       |
| 3\. Check whether the proof implicitly assumes the named              |
| misconception                                                         |
|                                                                       |
| for this topic instead of the correct hypothesis.                     |
|                                                                       |
| 4\. Focus on: nowhere differentiable, unbounded on every interval,    |
|                                                                       |
| continuous but not uniformly continuous.                              |
|                                                                       |
| Do NOT edit any files. Report only.\"                                 |
+-----------------------------------------------------------------------+

**scripts/polya.sh --- Pólya Recovery Protocol**

+-----------------------------------------------------------------------+
| scripts/polya.sh                                                      |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/polya.sh src/Chapter3.lean                        |
|                                                                       |
| \# Use when stuck \-- applies Polya heuristics in order               |
|                                                                       |
| CHAPTER=\${1:-\"src/Chapter3.lean\"}                                  |
|                                                                       |
| claude \--print \\                                                    |
|                                                                       |
| \"I am stuck on a proof in \$CHAPTER. Apply the Polya recovery        |
| protocol.                                                             |
|                                                                       |
| Ask me these questions IN ORDER, moving to the next only if the       |
| previous                                                              |
|                                                                       |
| fails to unlock progress after one exchange:                          |
|                                                                       |
| Step 1: What happens in the simplest non-trivial case?                |
|                                                                       |
| Step 2: What would I need to already have for this to work?           |
|                                                                       |
| Step 3: Have I proved anything with a similar logical form?           |
|                                                                       |
| Step 4: Can I remove a condition and solve a simpler version?         |
|                                                                       |
| Step 5: Is there an auxiliary object I could introduce?               |
|                                                                       |
| Step 6: Which entry in my Theorem Ledger might apply here?            |
|                                                                       |
| Do NOT give the answer or next step directly.                         |
|                                                                       |
| Ask one question at a time and wait for my response.\"                |
+-----------------------------------------------------------------------+

**scripts/bloom.sh --- Bloom-Level Assessment**

+-----------------------------------------------------------------------+
| scripts/bloom.sh                                                      |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/bloom.sh src/Chapter3.lean \"uniform continuity\" |
|                                                                       |
| CHAPTER=\${1:-\"src/Chapter3.lean\"}                                  |
|                                                                       |
| CONCEPT=\${2:-\"the main theorem in this chapter\"}                   |
|                                                                       |
| claude \--print \\                                                    |
|                                                                       |
| \"Assess my understanding of \$CONCEPT from \$CHAPTER using Bloom\'s  |
| Taxonomy.                                                             |
|                                                                       |
| Ask me questions at each level, escalating only when I demonstrate    |
| mastery.                                                              |
|                                                                       |
| Remember level: State the definition from memory.                     |
|                                                                       |
| Understand level: Explain WHY the definition is formulated as it is.  |
|                                                                       |
| Apply level: Verify a specific example against the definition.        |
|                                                                       |
| Analyze level: Identify which hypothesis is load-bearing.             |
|                                                                       |
| Evaluate level: Is my proof the minimum correct argument?             |
|                                                                       |
| Create level: Construct an object with prescribed properties.         |
|                                                                       |
| Stop at the first level where I cannot demonstrate mastery.           |
|                                                                       |
| Report my current Bloom level for this concept.\"                     |
+-----------------------------------------------------------------------+

**scripts/misconception.sh --- Misconception Probe (NEW v2.1)**

+-----------------------------------------------------------------------+
| scripts/misconception.sh                                              |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/misconception.sh src/Chapter4.lean                |
|                                                                       |
| \# Probes the named misconception for the current chapter\'s topic    |
|                                                                       |
| CHAPTER=\${1:-\"src/Chapter4.lean\"}                                  |
|                                                                       |
| claude \--print \\                                                    |
|                                                                       |
| \"Look up the named misconception for the topic of \$CHAPTER in       |
|                                                                       |
| ledger.json or the Real Analysis Study Guide Part V checklist.        |
|                                                                       |
| Present it to me as a plausible student argument \-- do NOT tell me   |
|                                                                       |
| in advance that it is wrong or which part is invalid.                 |
|                                                                       |
| Ask me to:                                                            |
|                                                                       |
| \(1\) identify the precise logical step that is invalid,              |
|                                                                       |
| \(2\) state the canonical counterexample,                             |
|                                                                       |
| \(3\) say what additional hypothesis would make the argument valid.   |
|                                                                       |
| Do not reveal the answer if I get it wrong on the first attempt \--   |
|                                                                       |
| instead ask what the argument would need to be true for it to work.\" |
+-----------------------------------------------------------------------+

**scripts/launch.sh --- Smart Launcher with Auto File Discovery**

+-----------------------------------------------------------------------+
| scripts/launch.sh                                                     |
|                                                                       |
| #!/bin/bash                                                           |
|                                                                       |
| \# Usage: ./scripts/launch.sh src/Chapter4.lean                       |
|                                                                       |
| CHAPTER=\$1                                                           |
|                                                                       |
| if \[ -z \"\$CHAPTER\" \]; then                                       |
|                                                                       |
| echo \"Usage: ./scripts/launch.sh src/ChapterN.lean\"                 |
|                                                                       |
| exit 1                                                                |
|                                                                       |
| fi                                                                    |
|                                                                       |
| \# Find all earlier chapter files automatically                       |
|                                                                       |
| EARLIER_FILES=\$(find src/ -name \"\*.lean\" \| sort \| \\            |
|                                                                       |
| awk -v target=\"\$CHAPTER\" \'\$0 \< target\')                        |
|                                                                       |
| READ_FLAGS=\"\"                                                       |
|                                                                       |
| for f in \$EARLIER_FILES; do                                          |
|                                                                       |
| READ_FLAGS=\"\$READ_FLAGS \--read \$f\"                               |
|                                                                       |
| done                                                                  |
|                                                                       |
| CHAPTER_NUM=\$(echo \"\$CHAPTER\" \| grep -o \'\[0-9\]\*\')           |
|                                                                       |
| if \[ -f \"notes/ch\${CHAPTER_NUM}.md\" \]; then                      |
|                                                                       |
| READ_FLAGS=\"\$READ_FLAGS \--read notes/ch\${CHAPTER_NUM}.md\"        |
|                                                                       |
| fi                                                                    |
|                                                                       |
| if \[ -f \"checklists/ch\${CHAPTER_NUM}\_checklist.md\" \]; then      |
|                                                                       |
| READ_FLAGS=\"\$READ_FLAGS \--read                                     |
| checklists/ch\${CHAPTER_NUM}\_checklist.md\"                          |
|                                                                       |
| fi                                                                    |
|                                                                       |
| echo \"Loading: CLAUDE.md + earlier chapters + notes + checklist\"    |
|                                                                       |
| echo \"Editing: \$CHAPTER\"                                           |
|                                                                       |
| claude \$READ_FLAGS \"\$CHAPTER\"                                     |
+-----------------------------------------------------------------------+

**Makefile --- One-Word Access to Everything**

+-----------------------------------------------------------------------+
| Makefile \-- save to project root                                     |
|                                                                       |
| CHAPTER ?= src/Chapter3.lean                                          |
|                                                                       |
| CONCEPT ?= \"the main theorem\"                                       |
|                                                                       |
| work:                                                                 |
|                                                                       |
| ./scripts/launch.sh \$(CHAPTER)                                       |
|                                                                       |
| draft:                                                                |
|                                                                       |
| claude \$(CHAPTER)                                                    |
|                                                                       |
| critic:                                                               |
|                                                                       |
| ./scripts/critic.sh \$(CHAPTER)                                       |
|                                                                       |
| attack:                                                               |
|                                                                       |
| ./scripts/attack.sh \$(CHAPTER)                                       |
|                                                                       |
| polya:                                                                |
|                                                                       |
| ./scripts/polya.sh \$(CHAPTER)                                        |
|                                                                       |
| bloom:                                                                |
|                                                                       |
| ./scripts/bloom.sh \$(CHAPTER) \$(CONCEPT)                            |
|                                                                       |
| misconception:                                                        |
|                                                                       |
| ./scripts/misconception.sh \$(CHAPTER)                                |
|                                                                       |
| build:                                                                |
|                                                                       |
| lake build                                                            |
|                                                                       |
| check:                                                                |
|                                                                       |
| lean \--run \$(CHAPTER)                                               |
|                                                                       |
| review: critic build                                                  |
|                                                                       |
| .PHONY: work draft critic attack polya bloom misconception build      |
| check review                                                          |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| WSL 2 Terminal \-- make scripts executable and test                   |
|                                                                       |
| chmod +x scripts/\*.sh                                                |
|                                                                       |
| ./scripts/launch.sh src/Chapter1.lean                                 |
|                                                                       |
| \# Example usage                                                      |
|                                                                       |
| make work CHAPTER=src/Chapter3.lean                                   |
|                                                                       |
| make critic CHAPTER=src/Chapter3.lean                                 |
|                                                                       |
| make attack CHAPTER=src/Chapter3.lean                                 |
|                                                                       |
| make polya CHAPTER=src/Chapter3.lean                                  |
|                                                                       |
| make bloom CHAPTER=src/Chapter3.lean CONCEPT=\"uniform continuity\"   |
|                                                                       |
| make misconception CHAPTER=src/Chapter3.lean                          |
|                                                                       |
| make build                                                            |
|                                                                       |
| make review CHAPTER=src/Chapter3.lean                                 |
+-----------------------------------------------------------------------+

> **Part VII --- The Study Methodology --- Three Pedagogical
> Frameworks**

Three pedagogical frameworks are embedded in the CLAUDE.md and role
scripts. Understanding them helps you use the tools deliberately rather
than mechanically. Each governs a different dimension of the study
process.

  --------------------------------------------------------------------------------
  **Framework**      **Governs**               **Primary Tool**      **When
                                                                     Applied**
  ------------------ ------------------------- --------------------- -------------
  Solow\'s           Proof strategy: how to    Forward-Backward      Every proof
  Forward-Backward   work toward a proof from  method in every proof attempt,
                     both the hypothesis and   attempt               every
                     conclusion simultaneously                       definition,
                                                                     every theorem
                                                                     reading

  Pólya\'s           Problem-solving recovery: The Pólya recovery    Rungs 3-5 of
  Heuristics         what to do when stuck and protocol              the proof
                     the Forward-Backward      (scripts/polya.sh)    ladder; any
                     method stalls                                   impasse

  Bloom\'s Taxonomy  Question calibration:     Bloom-calibrated      Every major
                     ensuring all six          question sequences    definition
                     cognitive levels are      (scripts/bloom.sh)    and theorem
                     reached, not just                               
                     Remember/Understand                             
  --------------------------------------------------------------------------------

**A. Solow\'s Forward-Backward Method**

Applied to definitions: before reading any theorem, run a backward pass
(what must be true of an object satisfying this definition?) and a
forward pass (what examples do I know that should satisfy this? what
should fail it?). Applied to theorems before proving them: backward from
the conclusion (what form is it? existence? equality? implication?) and
forward from the hypotheses (what does each hypothesis immediately give
me?).

Applied to entire sections before doing any proof: start from the end of
the section (what is the destination theorem?), work backward (which
lemmas support it?), then start from the beginning (how does each
definition extend what came before?). This builds the dependency map
before you write a single proof.

**B. Pólya\'s Recovery Protocol**

When Solow\'s method stalls, the polya.sh script applies these
heuristics in order. Critically, the analogy heuristic (Step 3) requires
a repertoire --- it is only effective from Phase 4 onward when the
Theorem Ledger has accumulated depth.

  ----------------------------------------------------------------------------
  **Step**                     **Heuristic**                     **Effective
                                                                 From**
  ---------------------------- --------------------------------- -------------
  1                            Specialisation: what happens in   Phase 1
                               the simplest non-trivial case?    onward

  2                            Work backwards: what would I need Phase 1
                               to already have?                  onward

  3                            Analogy: have I proved anything   Phase 4
                               with a similar logical form?      onward
                               (check Ledger)                    

  4                            Decomposition: can I remove a     Phase 1
                               condition and solve a simpler     onward
                               version?                          

  5                            Auxiliary element: is there an    Phase 2
                               object I could introduce to       onward
                               bridge the gap?                   

  6                            Repertoire: which Theorem Ledger  Phase 3
                               entry might apply here?           onward
  ----------------------------------------------------------------------------

**C. Bloom\'s Taxonomy --- Escalation Sequence**

The bloom.sh script systematically escalates through all six levels for
any concept. The critical failure mode of AI tutors is staying at
Remember/Understand. Real Analysis mastery requires reaching Analyze,
Evaluate, and Create for every major result.

  ------------------------------------------------------------------------
  **Level**    **What the Question Does**   **Example (Uniform
                                            Continuity)**
  ------------ ---------------------------- ------------------------------
  Remember     Retrieves the definition     State the definition with all
               from memory                  quantifiers explicit.

  Understand   Explains WHY the formulation Why must delta be independent
               is as it is                  of x?

  Apply        Verifies a specific example  Is f(x) = sqrt(x) uniformly
               against the definition       continuous on \[1, ∞)?

  Analyze      Identifies the load-bearing  Which hypothesis in
               structure                    Heine-Cantor is essential?
                                            Trace where compactness is
                                            invoked.

  Evaluate     Judges whether the proof is  Is your proof the minimum
               minimal                      correct argument? Where is it
                                            doing unnecessary work?

  Create       Constructs an object with    Construct f continuous on R
               prescribed properties        but not uniformly continuous
                                            on any interval.
  ------------------------------------------------------------------------

**D. Alcock\'s Self-Explanation Protocol**

Research by Hodds, Alcock, and Inglis (2014) demonstrated that
self-explanation training improves proof comprehension with effect size
d = 0.95 after a single session. The habit must become independent ---
not just triggered by Claude.

  -----------------------------------------------------------------------
  **Before proceeding to the next line of any proof, ask yourself:** (1)
  Do I understand the ideas used in this line? (2) Do I understand WHY
  those ideas were used? (3) Can I explain this line in terms of earlier
  ideas in this proof? (4) If this line contradicts something I believed,
  what needs updating? Progress marker: by Phase 3, self-explain without
  Claude prompting. By Phase 5, the protocol is automatic.

  -----------------------------------------------------------------------

**E. The Misconception Catalogue (NEW v2.1)**

Seven named misconceptions --- one per major topic --- are catalogued in
the Real Analysis Study Guide Part V and mirrored in ledger.json via the
misconception field. Each entry names the misconception precisely,
identifies the exact logical step where it occurs, and supplies the
counterexample that breaks it.

The misconception probe operates differently from the other three
frameworks: rather than guiding the student toward a correct argument,
it presents a plausible incorrect argument and requires the student to
locate the specific failure. This targets Bloom Analyze and Evaluate
simultaneously, and is the fourth part of the Four-Part Consolidation
Assessment (see Part IX).

> **Part VIII --- The Reading Plan --- All Phases with Computer
> Integration**

The reading plan from the Real Analysis Complete Study Guide V2.1 is
mapped here onto computer workflow steps. For each phase: which Alcock
chapter to read first, which Lean imports to activate, and which
CLAUDE.md fields to update.

  -----------------------------------------------------------------------
  **Alcock before Strichartz, Strichartz before Rudin, always.** Read the
  Alcock chapter to surface difficulty zones and refute misleading
  informal images before the formal treatment. Never reverse this order.

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------
  **Phase**   **Topic**           **Time**   **Texts (in order)** **CLAUDE.md Update**
  ----------- ------------------- ---------- -------------------- -------------------------------------------
  Prelim      Proof Foundations   2-6 wks    Alcock Part 1 (50    Focus: proof foundations
                                             pp) THEN Solow -\>   
                                             Hammack -\> Eccles   

  Phase 1     Real Numbers        3-4 wks    Alcock Ch.10 -\>     Phase 1 \-- Real Numbers. Misconception:
                                             Strichartz Ch.1 -\>  completeness-implies-convergence
                                             Rudin Ch.1+Appendix  

  Phase 2     Basic Topology      4-6 wks    Strichartz (topology Phase 2 \-- Topology. Misconception:
                                             integrated) +        compact-iff-closed-and-bounded
                                             Munkres Ch.2 -\>     
                                             Rudin Ch.2           

  Phase 3     Sequences & Series  4-5 wks    Alcock Ch.5-6 -\>    Phase 3 \-- Sequences. Misconception:
                                             Strichartz Ch.2-3    consecutive-closeness-implies-convergence
                                             -\> Rudin Ch.3       

  Phase 4     Continuity          3-4 wks    Alcock Ch.7 -\>      Phase 4 \-- Continuity. Misconception:
                                             Strichartz Ch.4 -\>  pencil-lifting image
                                             Rudin Ch.4           

  Phase 5     Differentiation     2-3 wks    Alcock Ch.8 -\>      Phase 5 \-- Differentiation. Misconception:
                                             Strichartz Ch.5 -\>  continuity-implies-uniform-continuity
                                             Rudin Ch.5           

  Phase 6     Riemann-Stieltjes   4-5 wks    Alcock Ch.9 -\>      Phase 6 \-- Integration. Misconception:
                                             Strichartz Ch.6 -\>  terms-to-zero-implies-convergence
                                             Rudin Ch.6           

  Phase 7     Seq & Series of Fns 4-5 wks    Strichartz Ch.7 (+   Phase 7 \-- Uniform Convergence.
                                             Fourier) -\> Rudin   Misconception:
                                             Ch.7                 pointwise-limit-preserves-continuity

  Phase 8     Power Series        2-3 wks    Strichartz Fourier + Phase 8 \-- Power Series
                                             Rudin Ch.8           
                                             (together)           

  Phase 9     Multivariable       6-8 wks    Spivak -\> NSS or    Phase 9 \-- Multivariable
                                             Loomis-Sternberg     
  -----------------------------------------------------------------------------------------------------------

**Updating CLAUDE.md for Each Phase**

At the start of each new phase, open CLAUDE.md and update the Current
Phase section and the Lean imports section to match. Also update the
\"Current focus\" line to name the misconception relevant to the new
phase, so Claude probes it without being asked.

> **Part IX --- The Proof Session Workflow --- Six-Stage Tutoring Loop**

A complete proof session runs across two windows: the WSL 2 terminal
running Claude Code, and VS Code showing the Lean infoview. The
six-stage tutoring loop from the Real Analysis Study Guide V2.1 maps
directly onto the computer workflow. Stage 6 now applies the Four-Part
Consolidation Assessment in place of the previous single \"test me\"
prompt.

**Opening a Session**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| cd \~/Documents/projects/real-analysis-lean                           |
|                                                                       |
| make work CHAPTER=src/Chapter3.lean                                   |
|                                                                       |
| \# In a second terminal, open VS Code for the Lean infoview           |
|                                                                       |
| code .                                                                |
|                                                                       |
| \# Then open the chapter file in VS Code                              |
+-----------------------------------------------------------------------+

**Stage 1 --- Concept Priming (Claude Code terminal)**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| Before opening any text: \"I am about to study \[theorem name\].      |
|                                                                       |
| Without telling me the proof, ask me questions to surface what        |
|                                                                       |
| I already know and what my intuitions are. Also ask: what is          |
|                                                                       |
| my informal picture of this concept? Let us find the example          |
|                                                                       |
| that breaks that picture before I read the formal definition.\"       |
+-----------------------------------------------------------------------+

The network positioning question: where does this topic sit in the
logical structure of Analysis so far? Answer this before opening
Strichartz.

**Stage 2 --- Active Reading (scratch paper + VS Code)**

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \# Write your proof attempt in VS Code                                |
|                                                                       |
| \# Watch the Lean infoview for proof state after each tactic          |
|                                                                       |
| \# Apply self-explanation to each line before moving to the next      |
|                                                                       |
| \# When stuck, use the Polya protocol:                                |
|                                                                       |
| make polya CHAPTER=src/Chapter3.lean                                  |
+-----------------------------------------------------------------------+

**Stage 3 --- Proof Gap Analysis (Claude Code terminal)**

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \"Here is my proof attempt. Do not rewrite it.                        |
|                                                                       |
| Go line by line:                                                      |
|                                                                       |
| \(1\) Is the justification complete?                                  |
|                                                                       |
| \(2\) Does this step follow from what precedes it?                    |
|                                                                       |
| \(3\) Are all hypotheses of any cited theorem satisfied?              |
|                                                                       |
| \(4\) Does my delta depend only on epsilon?                           |
|                                                                       |
| Flag every use of \'clearly\' or \'obviously\'.\"                     |
+-----------------------------------------------------------------------+

The do-not-rewrite instruction is essential. Claude identifies problems;
you fix them.

**Stage 4 --- Lean Formalisation Loop (Claude Code terminal)**

+-----------------------------------------------------------------------+
| WSL 2 Terminal                                                        |
|                                                                       |
| \"Now formalise this proof in Lean 4.                                 |
|                                                                       |
| Run lake build after each attempt.                                    |
|                                                                       |
| If it fails, report what error occurred and why,                      |
|                                                                       |
| then try a different approach.\"                                      |
|                                                                       |
| lean \--run scratch/lookup.lean 2\>&1 \| grep \"exact\"               |
+-----------------------------------------------------------------------+

**Stage 5 --- Counterexample & Converse Check (fresh session)**

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \# Fresh session \-- no memory of the drafting session                |
|                                                                       |
| make attack CHAPTER=src/Chapter3.lean                                 |
|                                                                       |
| \# Also run Bloom assessment to verify depth of understanding         |
|                                                                       |
| make bloom CHAPTER=src/Chapter3.lean CONCEPT=\"theorem name\"         |
+-----------------------------------------------------------------------+

**Stage 6 --- Consolidation: The Four-Part Assessment (NEW v2.1)**

The previous single-prompt consolidation (\"Test me. Ask me to state
\[definition\] from memory, then prove \[theorem\] without notes.\") is
one-dimensional --- it reaches Bloom Apply and occasionally Evaluate,
but misses the conceptual and misconception dimensions. Run all four
parts in order at the end of every topic session.

+-----------------------------------------------------------------------+
| **(1) Applied problem**                                               |
|                                                                       |
| A specific epsilon-delta or construction problem on a non-trivial     |
| function or set. Targets Bloom Apply.                                 |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \"Give me a non-trivial applied problem on \[topic\] \-- not a        |
|                                                                       |
| template application. I should have to construct the argument,        |
|                                                                       |
| not recall it.\"                                                      |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(2) Conceptual question**                                           |
|                                                                       |
| Target the quantifier structure or logical form of the conclusion;    |
| ask why the theorem is formulated as it is. Targets Bloom Analyze.    |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \"Ask me a conceptual question about \[topic\] that targets the       |
|                                                                       |
| quantifier order or logical form of the main theorem \-- not a        |
|                                                                       |
| recall question.\"                                                    |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(3) Derivation step**                                               |
|                                                                       |
| Reproduce a key lemma from logical structure, not from memorised      |
| proof sequence. Targets Bloom Evaluate.                               |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \"Without letting me look at my notes, ask me to derive the key       |
|                                                                       |
| inequality or lemma in this week\'s main proof, starting only         |
|                                                                       |
| from definitions and earlier results \-- not from the memorised       |
|                                                                       |
| proof sequence. Identify the exact line where the critical            |
|                                                                       |
| hypothesis enters.\"                                                  |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(4) Misconception check**                                           |
|                                                                       |
| Present the named misconception from the Ledger as a plausible but    |
| wrong student argument. Ask for precise refutation, not just          |
| identification. Targets Bloom Analyze and Evaluate simultaneously.    |
| This is the part that does the most new diagnostic work --- it forces |
| engagement with the logical step the misconception corrupts, not just |
| recognition that something is wrong.                                  |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Claude Code Terminal (or: make misconception                          |
| CHAPTER=src/Chapter3.lean)                                            |
|                                                                       |
| \"Present the named misconception in ledger.json for this topic       |
|                                                                       |
| as a plausible student argument. Do not tell me in advance which      |
|                                                                       |
| part is wrong. Ask me to: (1) identify the precise logical step       |
|                                                                       |
| that is invalid, (2) state the canonical counterexample,              |
|                                                                       |
| \(3\) say what additional hypothesis would make the argument valid.\" |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
  **Do not skip to part (4) early or treat it as optional.** Run all four
  parts in sequence. The misconception check is most effective when the
  student has already engaged with the applied, conceptual, and
  derivation dimensions --- skipping ahead reduces it to a recall
  exercise.

  -----------------------------------------------------------------------

Conclude Stage 6 with the Pólya Look Back and the Theorem Ledger update:

+-----------------------------------------------------------------------+
| Claude Code Terminal                                                  |
|                                                                       |
| \"Could you have approached this differently? What was the key        |
|                                                                       |
| insight? Does this argument generalise?\"                             |
|                                                                       |
| \"Update the Theorem Ledger for this result.                          |
|                                                                       |
| Include all V2.1 fields: converse (true/false + example),             |
|                                                                       |
| misconception (named misconception + precise refutation),             |
|                                                                       |
| analogues (which earlier theorem has a similar logical form?),        |
|                                                                       |
| downstream (what later results depend on this?),                      |
|                                                                       |
| Bloom level achieved.\"                                               |
+-----------------------------------------------------------------------+

**The Lemma Lookup Loop**

+-----------------------------------------------------------------------+
| WSL 2 Terminal 2 (second window \-- always open)                      |
|                                                                       |
| code scratch/lookup.lean                                              |
|                                                                       |
| lean \--run scratch/lookup.lean 2\>&1 \| grep \"exact\"               |
|                                                                       |
| \# Example output:                                                    |
|                                                                       |
| \# Try this: exact lt_of_lt_of_le ha hb                               |
+-----------------------------------------------------------------------+

> **Part X --- The Weekly Study Rhythm**

The weekly rhythm from the Real Analysis Study Guide V2.1 is mapped here
onto specific computer actions. The first-pass / consolidated-pass
distinction is critical: on first reading (Strichartz), read
strategically and move through. On consolidation (end of week), hold
firm. Day 7 now runs the Four-Part Assessment instead of the previous
single consolidation prompt.

  ---------------------------------------------------------------------------------------
  **Day(s)**   **Study Activity**                **Computer Action**     **Duration**
  ------------ --------------------------------- ----------------------- ----------------
  Day 1        Network positioning: where does   make work               1-1.5 hrs
  (morning)    this topic sit in the logical     CHAPTER=src/ChN.lean.   
               structure so far? Read Alcock     Ask Claude the          
               chapter. Identify the informal    positioning question    
               image to refute.                  before opening any      
                                                 text.                   

  Days 1-2     Strichartz first pass. Read       code notes/chN.md       1.5-2 hrs/day
               strategically \-- if bogged down, alongside reading. No   
               put a marker and continue. Notes  Lean yet.               
               on the WHY at every step.                                 

  Day 3        Mastery Checklist \-- Strichartz  make work               1.5-2 hrs
               pass. For every new definition:   CHAPTER=src/ChN.lean.   
               self-generate one satisfying      Ask Claude to quiz each 
               example and one failing example   definition in Socratic  
               before any theorem. Read the      mode.                   
               Misconception entry for this                              
               topic.                                                    

  Days 4-5     Rudin reading. Self-explain each  VS Code open for Lean   2-3 hrs/day
               line. Attempt each theorem before infoview. make work     
               reading proof. Apply converse     CHAPTER=src/ChN.lean.   
               check to every theorem.           Work Rung 1-2 proof     
                                                 ladder exercises.       

  Day 6        Proof Ladder Rungs 3-4 + Lean 4   make work (drafting),   2.5-3 hrs
               formalisation. Bloom: Analyze and make critic             
               Evaluate levels. Converse checks  CHAPTER=src/ChN.lean,   
               for all major theorems.           make build              

  Day 7        Four-Part Consolidation           make misconception      2-2.5 hrs
               Assessment: (1) Applied problem,  CHAPTER=src/ChN.lean    
               (2) Conceptual question, (3)      for part (4). Update    
               Derivation step, (4)              ledger.json with all    
               Misconception check. Update       V2.1 fields including   
               Theorem Ledger V2.1 (all fields). misconception. Ask      
                                                 Claude to quiz from     
                                                 Ledger.                 
  ---------------------------------------------------------------------------------------

**Monthly Consolidation**

+-----------------------------------------------------------------------+
| WSL 2 Terminal \-- monthly session                                    |
|                                                                       |
| make work CHAPTER=src/Chapter1.lean                                   |
|                                                                       |
| \# Ask Claude:                                                        |
|                                                                       |
| \# \"Quiz me on the full Theorem Ledger built to date.\"              |
|                                                                       |
| \# \"Analyse my Error Log: what is my most common error type          |
|                                                                       |
| \# across the last 20 proofs?\"                                       |
|                                                                       |
| \# \"Help me draw the full dependency graph of everything I have      |
|                                                                       |
| \# proved so far. Which theorems are load-bearing for the most        |
| results?\"                                                            |
|                                                                       |
| \# \"Re-run the misconception checks for all topics studied so far    |
| \--                                                                   |
|                                                                       |
| \# am I still vulnerable to any of them?\"                            |
|                                                                       |
| \# Re-attempt failed exercises without looking at previous attempts   |
+-----------------------------------------------------------------------+

**The Theorem Ledger V2.1 --- Field Reference**

Every successfully formalised proof adds an entry to ledger.json. The
API Proof Studio (Part XII) automates this. For manual sessions, ask
Claude to generate the JSON entry. The misconception and
misconception_refutation fields are new in Version 2.1.

  --------------------------------------------------------------------------------
  **Field**                   **What to Record**
  --------------------------- ----------------------------------------------------
  theorem                     Short name (e.g., heine_cantor)

  statement                   In your own words \-- no copying from Rudin

  proof_idea                  One sentence: the essential move the proof turns on

  load_bearing_hypothesis     Which hypothesis is essential?

  counterexample_if_removed   Counterexample when that hypothesis is removed

  converse_true               true / false / partial

  converse_example            Canonical counterexample if converse is false

  misconception (NEW v2.1)    The named misconception for this theorem, drawn from
                              the Part V catalogue

  misconception_refutation    The precise logical step that is invalid, plus the
  (NEW v2.1)                  canonical counterexample that breaks the
                              misconception

  depends_on                  List of earlier Ledger entries this proof invokes

  downstream                  Which later results depend on this theorem

  analogues                   Which earlier theorem has a similar logical form or
                              proof strategy

  lean_status                 compiled / in_progress / planned

  bloom_level                 highest level achieved: apply / analyze / evaluate /
                              create
  --------------------------------------------------------------------------------

> **Part XI --- Mathematical Input --- Typing, Voice & Symbols**

Mathematical notation input has three distinct layers, each with
different requirements and solutions. Matching the right tool to each
layer keeps friction minimal.

  --------------------------------------------------------------------------
  **Layer**   **What You Are Doing**               **Input Method / LaTeX
                                                   Needed?**
  ----------- ------------------------------------ -------------------------
  Layer 1     Talking to Claude (tutoring,         Natural language \-- type
              questions, Polya protocol)           or dictate via Win+H. No
                                                   LaTeX needed.

  Layer 2     Notes and Theorem Ledger (Markdown   Markdown + Unicode
              notes)                               shortcuts or VS Code
                                                   snippets. Optional LaTeX
                                                   only for PDF output.

  Layer 3     Lean 4 formal proofs                 Lean backslash input mode
                                                   in VS Code
                                                   (auto-installed). No
                                                   LaTeX needed.
  --------------------------------------------------------------------------

**Layer 1 --- Voice Dictation for Claude**

+-----------------------------------------------------------------------+
| Windows Voice Dictation \-- activate anywhere                         |
|                                                                       |
| Win + H (press Windows key + H simultaneously)                        |
|                                                                       |
| \"I want to prove that if f is uniformly continuous on the reals      |
|                                                                       |
| and x sub n is a Cauchy sequence then f of x sub n is also Cauchy\"   |
|                                                                       |
| \# Train Windows Speech Recognition for mathematical vocabulary:      |
|                                                                       |
| \# Control Panel -\> Speech Recognition -\> Train your computer       |
|                                                                       |
| \# (15-minute training session)                                       |
+-----------------------------------------------------------------------+

**Layer 2 --- Lean 4 Backslash Input (VS Code)**

The Lean 4 VS Code extension installs backslash input mode
automatically. These symbols cover 90% of Real Analysis notation:

  ---------------------------------------------------------------------------
  **Type**       **Get**   **Type**       **Get**   **Type**       **Get**
  -------------- --------- -------------- --------- -------------- ----------
  \\forall       ∀         \\exists       ∃         \\epsilon      ε

  \\delta        δ         \\to           →         \\le           ≤

  \\ge           ≥         \\ne           ≠         \\in           ∈

  \\subset       ⊂         \\cup          ∪         \\cap          ∩

  \\R            ℝ         \\N            ℕ         \\Q            ℚ
  ---------------------------------------------------------------------------

After one week of use these become automatic. Cognitive overhead drops
to near zero.

**Layer 3 --- VS Code Snippet Library for Notes**

+-----------------------------------------------------------------------+
| .vscode/real-analysis.code-snippets                                   |
|                                                                       |
| {                                                                     |
|                                                                       |
| \"Epsilon-delta opener\": {                                           |
|                                                                       |
| \"prefix\": \"fae\",                                                  |
|                                                                       |
| \"body\": \"∀ ε \> 0, ∃ δ \> 0,\",                                    |
|                                                                       |
| },                                                                    |
|                                                                       |
| \"Uniform continuity\": {                                             |
|                                                                       |
| \"prefix\": \"uc\",                                                   |
|                                                                       |
| \"body\": \"∀ ε \> 0, ∃ δ \> 0, ∀ x y ∈ K, \|x-y\| \< δ -\>           |
| \|f(x)-f(y)\| \< ε\",                                                 |
|                                                                       |
| },                                                                    |
|                                                                       |
| \"Cauchy condition\": {                                               |
|                                                                       |
| \"prefix\": \"cauchy\",                                               |
|                                                                       |
| \"body\": \"∀ ε \> 0, ∃ N, ∀ m,n ≥ N, \|a_m - a_n\| \< ε\",           |
|                                                                       |
| },                                                                    |
|                                                                       |
| \"Converse check\": {                                                 |
|                                                                       |
| \"prefix\": \"conv\",                                                 |
|                                                                       |
| \"body\": \"Converse: true/false. Counterexample or proof.\",         |
|                                                                       |
| },                                                                    |
|                                                                       |
| \"Misconception note (NEW v2.1)\": {                                  |
|                                                                       |
| \"prefix\": \"miscon\",                                               |
|                                                                       |
| \"body\": \"Misconception: NAME. Invalid step: STEP. Counterexample:  |
| EX.\",                                                                |
|                                                                       |
| }                                                                     |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+

> **Part XII --- The API-Based Proof Studio**

The Proof Studio is a local web application running inside WSL 2,
accessible from any browser on your Windows desktop at
http://localhost:5000. It wraps the Claude Code workflow in a browser
interface and automates the V2.1 Theorem Ledger (including the
misconception fields) and Error Log.

  -----------------------------------------------------------------------
  **Timing recommendation:** Build the Proof Studio after 2--3 weeks of
  regular Claude Code use. By then you will know exactly which frictions
  it needs to address.

  -----------------------------------------------------------------------

**The Automatic Loop**

+-----------------------------------------------------------------------+
| Server logic on every proof submission                                |
|                                                                       |
| 1\. Take your Lean code or natural language description               |
|                                                                       |
| 2\. Call Claude API (claude-sonnet-4-6) to generate/revise Lean proof |
|                                                                       |
| 3\. Write to src/CurrentProof.lean                                    |
|                                                                       |
| 4\. Run: lake build (subprocess call)                                 |
|                                                                       |
| 5\. If error: send full error + proof state back to Claude API        |
|                                                                       |
| 6\. Repeat up to 5 cycles                                             |
|                                                                       |
| 7\. Return final result + compilation status to browser               |
|                                                                       |
| \# On successful compile \-- automatic Theorem Ledger V2.1 update:    |
|                                                                       |
| 8\. Claude extracts ALL V2.1 fields:                                  |
|                                                                       |
| theorem, statement, proof_idea, load_bearing_hypothesis,              |
|                                                                       |
| counterexample_if_removed, converse_true, converse_example,           |
|                                                                       |
| misconception, misconception_refutation, depends_on, downstream,      |
|                                                                       |
| analogues, lean_status, bloom_level                                   |
|                                                                       |
| 9\. Appends structured entry to ledger.json                           |
|                                                                       |
| \# On failed proof \-- automatic Error Log entry:                     |
|                                                                       |
| 10\. Claude categorises: quantifier_error, missing_hypothesis,        |
|                                                                       |
| invalid_inference, wrong_theorem, delta_depends_on_x,                 |
|                                                                       |
| converse_confusion                                                    |
|                                                                       |
| 11\. Appends to error_log.json                                        |
+-----------------------------------------------------------------------+

**Build Prompt for Claude Code**

+-----------------------------------------------------------------------+
| Claude Code Terminal \-- use this prompt after 2-3 weeks              |
|                                                                       |
| You: Build a local web proof assistant for my Real Analysis workflow. |
|                                                                       |
| Read CLAUDE.md for full context. Requirements:                        |
|                                                                       |
| 1\. Python FastAPI server on localhost:5000                           |
|                                                                       |
| 2\. Three-panel browser interface \-- plain HTML/JS, no frameworks    |
|                                                                       |
| 3\. Left panel: Lean 4 proof editor with submit button                |
|                                                                       |
| 4\. Center panel: Claude tutoring conversation (Anthropic API)        |
|                                                                       |
| \- Use CLAUDE.md tutor instructions as system prompt                  |
|                                                                       |
| \- Socratic mode by default with Polya recovery protocol              |
|                                                                       |
| \- \"Check my proof\" button triggers critic mode                     |
|                                                                       |
| \- \"Bloom assess\" button triggers Bloom-level assessment            |
|                                                                       |
| \- \"Misconception check\" button triggers the misconception probe    |
|                                                                       |
| 5\. Right panel: live lake build output + Theorem Ledger V2.1 display |
|                                                                       |
| (must show misconception and misconception_refutation fields)         |
|                                                                       |
| Automatic features:                                                   |
|                                                                       |
| \- On proof submit: write to src/CurrentProof.lean, run lake build,   |
|                                                                       |
| send errors back to Claude API, retry up to 5 times                   |
|                                                                       |
| \- On successful compile: extract ALL Theorem Ledger V2.1 fields      |
|                                                                       |
| (including misconception, misconception_refutation, converse,         |
|                                                                       |
| analogues, downstream, bloom_level), append to ledger.json            |
|                                                                       |
| \- On failed proof: categorise error, log to error_log.json           |
|                                                                       |
| Keep dependencies minimal: FastAPI, uvicorn, anthropic Python SDK.    |
|                                                                       |
| No React, no build step. Single python app.py to launch.              |
|                                                                       |
| Read ANTHROPIC_API_KEY from environment.                              |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| WSL 2 Terminal \-- run the Studio                                     |
|                                                                       |
| pip install fastapi uvicorn anthropic \--break-system-packages        |
|                                                                       |
| export ANTHROPIC_API_KEY=your_key_here                                |
|                                                                       |
| python app.py                                                         |
|                                                                       |
| \# Open in Windows browser: http://localhost:5000                     |
+-----------------------------------------------------------------------+

> **Part XIII --- Session Commands & Complete Tutor Prompts Reference**

**Claude Code Session Commands**

  -----------------------------------------------------------------------
  **Command**              **What It Does / When to Use**
  ------------------------ ----------------------------------------------
  make work CHAPTER=\...   Smart launch with auto file discovery. Start
                           of every working session.

  make draft CHAPTER=\...  Plain claude launch for quick proof writing.
                           Minimal context overhead.

  make critic CHAPTER=\... Fresh critic session \-- no drafting memory.
                           After completing a proof attempt.

  make attack CHAPTER=\... Counterexample finder session. After Rung 4
                           proof ladder problems.

  make polya CHAPTER=\...  Pólya recovery protocol session. When stuck
                           \-- heuristic recovery.

  make bloom CHAPTER=\...  Bloom-level assessment session. After
  CONCEPT=\...             mastering a concept.

  make misconception       Misconception probe session. Use as part (4)
  CHAPTER=\... (NEW v2.1)  of the Four-Part Consolidation Assessment, or
                           any time you want to test resistance to a
                           known error pattern.

  make build               Run lake build on entire project. Verify all
                           proofs compile.

  make review CHAPTER=\... Critic + build in sequence. End-of-chapter
                           review.

  lean \--run              Find correct Mathlib lemma name. When a lemma
  scratch/lookup.lean \\\| name fails to compile.
  grep exact               

  claude doctor            Check installation and version.
                           Troubleshooting.

  /exit or Ctrl+C          Exit Claude Code session. End of session or
                           role switch.

  Shift+Tab twice          Toggle auto-accept mode (writes files without
                           asking). Well-defined automation tasks.
  -----------------------------------------------------------------------

**Complete Tutor Prompts --- Copy-Paste Ready**

+-----------------------------------------------------------------------+
| **Concept Priming (before reading)**                                  |
|                                                                       |
| \"I am about to study \[theorem name\]. Without telling me the proof, |
| ask me questions to surface what I already know and what my           |
| intuitions are. Also ask: what is my informal picture of this         |
| concept? Let us find the example that breaks that picture before I    |
| read the formal definition.\"                                         |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Network Positioning (before each chapter)**                         |
|                                                                       |
| \"Where does \[this topic\] sit in the logical structure of Analysis  |
| so far? What depends on what we are about to learn? Ask me this \-- I |
| should try to answer it before opening Strichartz. We will return to  |
| this question at the end of the week.\"                               |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Example/Non-Example Requirement (for each new definition)**         |
|                                                                       |
| \"Before we discuss any theorem, ask me to construct one object       |
| satisfying this definition and one that fails it by violating exactly |
| one condition. Do not accept examples directly from Rudin or          |
| Strichartz.\"                                                         |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Proof Gap Analysis (after attempt)**                                |
|                                                                       |
| \"Here is my proof. Do not rewrite it. Go line by line: (1) is the    |
| justification complete? (2) does this step follow from what precedes  |
| it? (3) are all hypotheses of any cited theorem satisfied? (4) does   |
| my delta depend only on epsilon?\"                                    |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Quantifier Check**                                                  |
|                                                                       |
| \"Write this statement with ALL quantifiers explicit. Is this what I  |
| mean? What does it say if I swap the first forall and exists?\"       |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Delta-x Diagnostic**                                                |
|                                                                       |
| \"Check my epsilon-delta proof: does my delta depend on x or only on  |
| epsilon? Trace through \-- if \|x-a\| \< delta, does my argument      |
| deliver \|f(x)-L\| \< epsilon?\"                                      |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Converse Check**                                                    |
|                                                                       |
| \"Is the converse of this theorem true? If false, what is the         |
| canonical counterexample? If true, is it a named result?\"            |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Misconception Check (NEW v2.1)**                                    |
|                                                                       |
| \"Present the named misconception in ledger.json for this theorem as  |
| a plausible student argument. Do not tell me in advance which part is |
| wrong. Ask me to identify the precise logical step that is invalid,   |
| give the canonical counterexample, and state exactly what additional  |
| hypothesis would make the argument valid. If I am wrong on the first  |
| attempt, do not reveal the answer \-- ask what the argument would     |
| need to be true for it to work.\"                                     |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Hypothesis Audit**                                                  |
|                                                                       |
| \"Have I verified every hypothesis of every theorem I cited? Which    |
| hypothesis is load-bearing? Give me a counterexample for each one     |
| removed.\"                                                            |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Compactness Interrogation**                                         |
|                                                                       |
| \"Have I verified the set is actually compact? Which property of      |
| compact sets am I using and why does the proof fail without it?\"     |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Knowledge Graph**                                                   |
|                                                                       |
| \"What earlier results does this theorem depend on? What later        |
| results will depend on it? What fails in Analysis without this        |
| result?\"                                                             |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Adversarial Probe**                                                 |
|                                                                       |
| \"Give me the most dangerous sequence or function satisfying my       |
| hypotheses but that my proof would struggle with.\"                   |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Informal Image Audit (Alcock)**                                     |
|                                                                       |
| \"What is my informal picture of this concept? Let us find an example |
| that matches my picture but fails the formal definition.\"            |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Bloom Escalation**                                                  |
|                                                                       |
| \"I have stated the definition (Remember) and explained why it is     |
| formulated as it is (Understand). Now push me to Apply: verify a      |
| specific example. Then Analyze: identify the load-bearing hypothesis. |
| Then Evaluate: is my proof minimal? Then Create: construct an object  |
| with prescribed properties.\"                                         |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Pólya Look Back (after each proof)**                                |
|                                                                       |
| \"Could I have approached this differently? What was the key insight  |
| \-- where did the proof actually turn? Does this argument generalise? |
| What is the weakest hypothesis I could have assumed and still proved  |
| this result?\"                                                        |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Four-Part Consolidation Assessment (NEW v2.1 --- replaces \"Test    |
| Me\")**                                                               |
|                                                                       |
| \"Run the Four-Part Consolidation Assessment for this topic. (1) Give |
| me a non-trivial applied problem requiring genuine construction. (2)  |
| Ask a conceptual question targeting the quantifier structure or       |
| logical form of the main theorem. (3) Ask me to derive a key lemma    |
| from logical structure, not memorised sequence \-- interrupt if I     |
| recite rather than reconstruct. (4) Present the named misconception   |
| for this topic as a plausible student argument and require precise    |
| refutation, not just identification.\"                                |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Theorem Ledger Update (V2.1)**                                      |
|                                                                       |
| \"Add this theorem to ledger.json with ALL V2.1 fields: theorem name, |
| plain-English statement, key proof idea, load-bearing hypothesis,     |
| counterexample when removed, converse true/false with example, the    |
| named misconception and its precise refutation, depends_on,           |
| downstream results, analogous theorems, Lean status, and highest      |
| Bloom level I achieved.\"                                             |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Error Pattern Analysis**                                            |
|                                                                       |
| \"Analyse my error_log.json. What is my most common error category    |
| across the last 20 proofs? What is the single most important thing    |
| for me to watch for?\"                                                |
+-----------------------------------------------------------------------+

> **Part XIV --- Master Setup Checklist**

Complete each item in order before proceeding to the next. Total time
from a fresh Windows 11 machine: approximately 90 minutes for the
technical setup, plus 30 minutes for the study methodology files. Items
marked (NEW v2.1) are additions for the Misconception Catalogue and
Four-Part Assessment.

**WSL 2 and Ubuntu**

> ☐ PowerShell (Admin): run wsl \--install
>
> ☐ Restart computer when prompted
>
> ☐ Ubuntu first-run: create username and password (keep it simple)
>
> ☐ Verify: run wsl \--status and confirm Default Version: 2

**VS Code on Windows**

> ☐ Download VS Code from code.visualstudio.com (Windows installer)
>
> ☐ Install VS Code extension: WSL (by Microsoft)
>
> ☐ Install VS Code extension: Lean 4 (by leanprover)
>
> ☐ Install VS Code extension: GitLens (optional)
>
> ☐ Confirm: bottom-left shows WSL: Ubuntu when WSL extension is active

**Prerequisites in WSL 2**

> ☐ Open Ubuntu terminal (Start menu or type wsl)
>
> ☐ Run: sudo apt update && sudo apt upgrade -y
>
> ☐ Run: sudo apt install -y git curl build-essential
>
> ☐ Verify: git \--version shows a version number
>
> ☐ Verify: curl \--version shows a version number

**Lean 4 and elan**

> ☐ Run: curl https://elan.lean-lang.org/elan-init.sh -sSf \| sh
>
> ☐ Run: source \~/.profile
>
> ☐ Verify: elan \--version shows a version number
>
> ☐ Verify: lean \--version shows a version number

**Mathlib Project**

> ☐ Run: cd \~/Documents && mkdir -p projects && cd projects
>
> ☐ Run: lake +v4.24.0 new real-analysis-lean math
>
> ☐ Run: cd real-analysis-lean
>
> ☐ Run: lake update
>
> ☐ Run: lake exe cache get (wait 5-15 minutes \-- do not skip)
>
> ☐ Verify: lake build completes without errors

**VS Code + Lean Verification**

> ☐ Run: code . (from project directory in WSL 2)
>
> ☐ Confirm green WSL: Ubuntu indicator in VS Code bottom-left
>
> ☐ Create src/Test.lean with the test proof from Part III
>
> ☐ Confirm Lean infoview shows proof state within 30 seconds
>
> ☐ Confirm exact? shows suggestions in the infoview

**Claude Code**

> ☐ Run: curl -fsSL https://claude.ai/install.sh \| bash
>
> ☐ Run: claude doctor (confirm installation)
>
> ☐ Run: claude (triggers OAuth \-- authenticate in browser)
>
> ☐ Confirm Claude Code starts and responds
>
> ☐ Type /exit to leave

**Project Structure**

> ☐ Run: mkdir -p src notes checklists scratch scripts/prompts
>
> ☐ Run: touch src/Chapter1.lean notes/ch1.md
> checklists/ch1_checklist.md
>
> ☐ Create scratch/lookup.lean with test content from Part III
>
> ☐ Initialize ledger.json: echo \"\[\]\" \> ledger.json
>
> ☐ Initialize error_log.json: echo \"\[\]\" \> error_log.json

**CLAUDE.md (Version 2.1 Full Template)**

> ☐ Create CLAUDE.md from the full Version 2.1 template in Part V
>
> ☐ Confirm all sections present: Polya Recovery Protocol, Bloom
> Taxonomy,
>
> ☐ Alcock Self-Explanation Protocol, Converse Check requirement,
>
> ☐ Example/Non-Example requirement, Theorem Ledger V2.1 field list
>
> ☐ Confirm Misconception Probe section is present (NEW v2.1)
>
> ☐ Confirm Four-Part Consolidation Assessment section is present (NEW
> v2.1)
>
> ☐ Update Current Phase line for your starting point
>
> ☐ Update the Lean imports section for your starting phase

**Role Scripts (includes misconception.sh --- NEW v2.1)**

> ☐ Create scripts/critic.sh from Part VI
>
> ☐ Create scripts/attack.sh from Part VI
>
> ☐ Create scripts/polya.sh from Part VI
>
> ☐ Create scripts/bloom.sh from Part VI
>
> ☐ Create scripts/misconception.sh from Part VI (NEW v2.1)
>
> ☐ Create scripts/launch.sh from Part VI
>
> ☐ Run: chmod +x scripts/\*.sh
>
> ☐ Create Makefile from Part VI (includes misconception target)
>
> ☐ Test: make build (should succeed)

**Mathematical Input**

> ☐ Enable Win+H voice dictation \-- test it in a text field
>
> ☐ Optional: run Windows Speech Recognition training (15 min)
>
> ☐ Test Lean backslash input: type \\forall in a .lean file in VS Code
>
> ☐ Practice the 15 symbol shortcuts until comfortable (one week)
>
> ☐ Create .vscode/real-analysis.code-snippets from Part XI
>
> ☐ Confirm misconception note snippet is included (NEW v2.1)

**Study Methodology Verification**

> ☐ Read: Alcock, How to Think About Analysis, Part 1 (4 chapters, \~50
> pages)
>
> ☐ Complete: Solow, How to Read and Do Proofs, Ch.1-13
>
> ☐ Complete: Hammack, Book of Proof (free), Ch.1-12
>
> ☐ Complete: Eccles, An Introduction to Mathematical Reasoning, Ch.1-5
>
> ☐ Verify CLAUDE.md Polya Recovery Protocol is working: run make polya
>
> ☐ Verify Bloom assessment is working: run make bloom CONCEPT=\"real
> numbers\"
>
> ☐ Verify misconception probe is working: run make misconception (NEW
> v2.1)
>
> ☐ Create first checklist entry: checklists/ch1_checklist.md

**First Real Session**

> ☐ Run: make work CHAPTER=src/Chapter1.lean
>
> ☐ Ask Claude the network positioning question (Part XIII)
>
> ☐ Ask Claude to prime your intuitions about the Archimedean property
>
> ☐ Attempt your first proof with Lean infoview open in VS Code
>
> ☐ Submit for gap analysis using the prompt from Part XIII
>
> ☐ Run: make critic CHAPTER=src/Chapter1.lean (fresh critic review)
>
> ☐ Run the Four-Part Assessment at end of week (NEW v2.1)
>
> ☐ Update CLAUDE.md Current Phase after session
>
> ☐ Add first Theorem Ledger V2.1 entry to ledger.json, including
> misconception field

**API Proof Studio (after 2-3 weeks)**

> ☐ Run 2-3 weeks of regular Claude Code sessions first
>
> ☐ Identify specific frictions from real experience
>
> ☐ Ask Claude Code to build app.py using the prompt in Part XII
>
> ☐ Confirm: V2.1 Theorem Ledger fields including misconception and
> misconception_refutation
>
> ☐ Run: pip install fastapi uvicorn anthropic \--break-system-packages
>
> ☐ Set ANTHROPIC_API_KEY environment variable
>
> ☐ Run: python app.py and open http://localhost:5000
>
> ☐ Verify three-panel interface and automatic Ledger V2.1 update
>
> **Part XV --- Future Subjects --- Topology & Abstract Algebra**

Almost no changes to the setup are required for Topology and Abstract
Algebra. The four-layer stack, CLAUDE.md discipline, role scripts, and
pedagogical frameworks (including the misconception-probe pattern)
transfer directly. What changes is the content of CLAUDE.md and the Lean
imports.

  -----------------------------------------------------------------------
  **What Changes** **What You Do**                   **Effort**
  ---------------- --------------------------------- --------------------
  CLAUDE.md        Update chapter, subject, Lean     5 minutes per
  subject lines    imports, and current texts        subject

  Project          Create a new one per subject:     mkdir + lake new \--
  directory        \~/projects/topology-lean,        15 minutes
                   \~/projects/algebra-lean          

  Mathlib imports  Claude Code selects automatically Zero \-- automatic
                   from CLAUDE.md subject line       

  Mastery          New checklists per chapter \--    Part of normal
  checklists       same format, different content.   workflow
                   New subjects need their own       
                   misconception entries researched  
                   and added.                        

  Books / text     New motivation + rigour pairings  Just reading
  pairings         \-- same reading plan structure   
  -----------------------------------------------------------------------

**What Stays the Same**

  -----------------------------------------------------------------------
  **Component**          **Status / Notes**
  ---------------------- ------------------------------------------------
  Claude Code + WSL 2 +  Zero changes. Same tools, same workflow.
  VS Code                

  CLAUDE.md discipline   Same format. Different content per subject.

  Polya Recovery         Unchanged. Subject-agnostic heuristics.
  Protocol               

  Bloom Taxonomy         Unchanged. Applies to any mathematical concept.
  escalation             

  Misconception probe    Unchanged mechanism. New subjects require their
  pattern                own catalogue of named misconceptions,
                         researched from the relevant education
                         literature.

  Four-Part              Unchanged structure. Applies to any topic.
  Consolidation          
  Assessment             

  Alcock                 Unchanged. Transferable reading habit.
  self-explanation       
  protocol               

  Proof-practice ladder  Unchanged. Applies to any mathematical subject.
  (Rungs 1-5)            

  Theorem Ledger V2.1 +  Same format, including misconception fields.
  Error Log              Accumulates across subjects.

  Lean 4 + Mathlib4      Same tools. Mathlib covers all three subjects
                         extensively.

  Role scripts (critic,  Unchanged. Subject-agnostic scripts.
  attack, polya, bloom,  
  misconception)         

  Mathematical input     Unchanged. Add new snippets per subject.
  system                 

  API Proof Studio       Unchanged. ledger.json grows across subjects.
  -----------------------------------------------------------------------

**New Lean 4 Imports Per Subject**

+-----------------------------------------------------------------------+
| CLAUDE.md \-- update imports when switching subject                   |
|                                                                       |
| \-- TOPOLOGY (replace Real Analysis imports in CLAUDE.md)             |
|                                                                       |
| import Mathlib.Topology.Basic                                         |
|                                                                       |
| import Mathlib.Topology.Compactness.Compact                           |
|                                                                       |
| import Mathlib.Topology.Connected.Basic                               |
|                                                                       |
| import Mathlib.Topology.ContinuousFunction.Basic                      |
|                                                                       |
| import Mathlib.Topology.MetricSpace.Basic                             |
|                                                                       |
| \-- ABSTRACT ALGEBRA (replace when switching)                         |
|                                                                       |
| import Mathlib.GroupTheory.Subgroup.Basic                             |
|                                                                       |
| import Mathlib.GroupTheory.QuotientGroup                              |
|                                                                       |
| import Mathlib.RingTheory.Ideal.Basic                                 |
|                                                                       |
| import Mathlib.FieldTheory.Galois                                     |
+-----------------------------------------------------------------------+

**Recommended Book Pairings**

  -------------------------------------------------------------------------
  **Subject**   **Metacognitive    **Motivation Text** **Rigour Text**
                Prep**                                 
  ------------- ------------------ ------------------- --------------------
  Real Analysis Alcock \-- How to  Strichartz \-- The  Rudin \-- Principles
                Think About        Way of Analysis     
                Analysis                               

  Topology      Relevant sections  Gamelin & Greene    Munkres \-- Topology
                of Alcock Part 2   \-- Introduction to (2nd ed.)
                \-- many concepts  Topology            
                overlap                                

  Abstract      No direct Alcock   Pinter \-- A Book   Dummit & Foote \--
  Algebra       equivalent \-- use of Abstract Algebra Abstract Algebra
                Polya + Bloom +                        
                misconception                          
                scripts from day                       
                one                                    
  -------------------------------------------------------------------------

Recommended order: Real Analysis first (Year 1), then Topology (Year 2
--- direct continuity with metric space topology from Rudin Ch.2), then
Abstract Algebra (Year 2--3). Your Real Analysis fluency ---
compactness, connectedness, continuity --- arrives at Munkres already
known as special cases, making the generalisation feel natural rather
than foreign.

Revised and expanded edition integrating the Real Analysis Complete
Study Guide V2.1, including the seven-topic Misconception Catalogue, the
misconception field in the Theorem Ledger, and the Four-Part
Consolidation Assessment. Lean 4 and Mathlib4 are open-source and freely
available at leanprover.github.io. Claude Code requires a Claude Pro or
Max subscription or Anthropic API access. The Anthropic API key is
required only for the optional Proof Studio (Part XII). Book of Proof
(Hammack) and Analysis I & II (Tao) are available free online.
Loomis--Sternberg Advanced Calculus is available free from Sternberg\'s
Harvard webpage.
