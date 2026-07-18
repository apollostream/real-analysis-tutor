# The six-stage tutoring loop

Run a topic through these six stages in order (CG Part IX). Each stage names its goal, the
sibling skill you delegate to, and the criteria for entering and exiting. Never skip a
stage; escalate only when the current stage is genuinely exhausted.

## Two gates that apply throughout

- **Example / Non-Example gate.** Before any theorem work on a new definition, require the
  learner to construct one object that satisfies the definition AND one that fails it by
  violating exactly one condition. This gate must clear before Stage 1 advances to theorems —
  an informal image the learner cannot instantiate is an image that will mislead them.
- **Converse reflex.** For every theorem, ask — as a reflex, not an occasional probe —
  whether the converse is true, and if not, ask for the canonical counterexample. Fold this
  into Stage 5 and the ledger entry, and raise it any time a conditional statement appears.

## Stage 1 — Concept Priming

- **Goal:** surface what the learner already knows and their informal image, and find the
  example that breaks that image, before any text is opened. Ask the network-positioning
  question: where does this topic sit in the logical structure so far?
- **Delegate to:** `real-analysis-tutor:prime`.
- **Entry:** a topic is chosen. **Exit:** intuitions surfaced, the Example/Non-Example gate
  cleared for the topic's definitions, and the misleading informal image named.

## Stage 2 — Active Reading

- **Goal:** the learner attempts the proof themselves (20–30 minutes) before reading Rudin,
  applying the self-explanation protocol line by line.
- **Delegate to:** guide the reading yourself; on a genuine impasse, invoke
  `real-analysis-tutor:stuck` (the D-L-M-K + Pólya recovery ladder). Do not supply the next
  step — supply the next question.
- **Entry:** Stage 1 complete. **Exit:** the learner has a proof attempt (complete or
  stalled) to submit, or has consciously chosen to read after a real attempt.

## Stage 3 — Proof Checking

- **Goal:** diagnose the attempt line by line — implicit steps, unjustified "clearly",
  quantifier order, delta-independence, unverified hypotheses. Do NOT rewrite the proof.
- **Delegate to:** `real-analysis-tutor:check-proof`.
- **Entry:** a proof attempt exists. **Exit:** zero unjustified steps remain, OR the learner
  consciously defers a specific gap for later. Log each error surfaced through the engine
  under one of the six categories.

## Stage 4 — Formal Verification

- **Goal:** translate the proof to Lean 4 and let the compiler deliver ground truth — a proof
  that compiles is correct.
- **Delegate to:** `real-analysis-tutor:formalize`. If Lean is not set up, offer
  `real-analysis-tutor:setup`; if the learner declines, note the stage as deferred and move on.
- **Entry:** the paper proof passes Stage 3. **Exit:** the target compiles, OR formalization
  is consciously deferred (this stage is an amplifier, not a gate).

## Stage 5 — Counterexample and Converse Check

- **Goal:** try to break the proof — remove one hypothesis and construct a failing case —
  and settle the converse.
- **Delegate to:** `real-analysis-tutor:attack`.
- **Entry:** a proof the learner believes is correct. **Exit:** each hypothesis probed for
  load-bearing status with a counterexample when removed, and the converse reflex answered
  (true, or false with its canonical counterexample).

## Stage 6 — Four-Part Consolidation Assessment

- **Goal:** consolidate to mastery through all four parts, in this fixed order — never skip
  ahead to part (4) or treat it as optional:
  1. **Applied problem** — a non-trivial epsilon-delta or construction task (Bloom Apply).
  2. **Conceptual question** — target quantifier structure or logical form (Bloom Analyze).
  3. **Derivation step** — reconstruct a key lemma from logical structure, not memory
     (Bloom Evaluate).
  4. **Misconception check** — present the topic's named misconception (from
     `$CLAUDE_PLUGIN_ROOT/curriculum/real-analysis/misconceptions.yaml`) as a plausible
     student argument; require the precise invalid step and the canonical counterexample,
     not mere recognition (Bloom Analyze + Evaluate).
- **Delegate to:** `real-analysis-tutor:assess` for all four parts in order, then
  `real-analysis-tutor:ledger` to record the entry.
- **Entry:** Stages 1–5 complete for the topic. **Exit:** all four parts answered, the
  Theorem Ledger entry written (all V2.1 fields including converse and misconception), and
  the Pólya Look Back asked. This exit feeds the close ritual in `SKILL.md`.
