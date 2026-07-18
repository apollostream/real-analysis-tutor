---
name: formalize
description: Lean 4 formalization loop (Stage 4). Use after a proof survives gap analysis, or for [Lean] checklist targets.
---

Use this skill for Stage 4 of the six-stage tutoring loop: after a proof has survived gap analysis (Stage 3), or whenever the current chapter checklist names a `[Lean]` target. Your job is to get the theorem verified against Mathlib without ever writing the learner's mathematics for them.

## Step 1 — Check whether Lean is available

Run, in the learner's workspace:

```
cd <workspace> && lake --version
```

If that fails, fall back to `elan --version`. Both failing means Lean is not set up.

**Lean absent:**
- Track internally, for this session only, whether you have already offered setup once. If you have not, offer it now: dispatch the learner to `real-analysis-tutor:setup` (or simply describe what it would do and ask if they want it now). This offer happens at most once per session — if you already made it earlier and the learner declined or deferred, do not offer again; just proceed.
- Either way, record `lean_status: unverified` in the pending ledger entry for this theorem and move on. Say something warm and unworried — nothing is lost, we'll verify this in Lean once it's set up — and continue the session on the informal proof alone. Never let a missing Lean toolchain stall or shame the learner.

**Lean present:** continue to Step 2.

## Step 2 — The learner translates first, at Rung ≥3

Check the learner's current position (`position.rung` in learner state).

- **Rung ≥3 (Conceptual and above):** before you dispatch anything, ask the learner to attempt the Lean 4 theorem *statement* themselves — the formal signature, not the proof. This is the same never-do-it-for-them contract that governs every other stage: you do not write it for them. Discuss their attempt Socratically if it's off (wrong quantifier shape, wrong type, missing hypothesis) — ask what's missing, don't supply the fix. Once they have a genuine attempt (right or wrong), move to Step 3.
- **Rung 1–2 (Mechanical, Structural):** Lean is not yet the pedagogically load-bearing part of these rungs — skip straight to Step 3.

## Step 3 — Dispatch the `lean-verifier` agent

Dispatch the `lean-verifier` agent (fresh context) with exactly:
- the theorem statement
- the learner's informal proof (as it stood when it survived gap analysis)
- the target file: `src/Chapter<N>.lean` in the workspace, where `<N>` is the learner's current chapter

Do not hand the agent your own assessment of the proof's correctness, and do not pre-judge the outcome for the learner. The agent owns the compile loop: it runs `lake build`, tries at most three tactic variations on a stuck goal, and reports what it tried and why each attempt failed. Let it finish before you say anything to the learner.

## Step 4 — Handle the result

**Compile succeeded:** update the pending ledger entry's `lean_status` to `compiled`. Tell the learner plainly — the compiler agrees, this proof is correct by construction. This is a good moment to note that a compiling Lean proof is the "infallible ground truth" layer; the informal proof is now independently confirmed, not just judged correct by you.

**Compile failed:** repeat, in substance, the mandatory framing rule — a compilation failure means the *formalization* failed, it does NOT by itself mean the learner's mathematics is wrong. The gap could be an unresolved lemma name, a missing import, a formalization choice that doesn't match the informal argument's structure, or a genuine mathematical gap; a Lean error alone often can't tell you which. Never report the failure to the learner as "your proof is wrong."

Then convert the agent's report into Socratic questions, not a verdict. Take the specific goal state at the point of failure and map it back to the corresponding step of the learner's *informal* proof: ask them to re-justify that step in their own words, in light of what the compiler could not confirm. Leave `lean_status` as `in_progress` (not `compiled`, not reset to `unverified`) so it's clear this theorem was attempted and can be retried once the informal step is revisited — either later this session or after the learner strengthens the argument.

Never dispatch the agent a second time on the same attempt without the learner first re-examining the flagged step; a second blind dispatch just reproduces the same failure without teaching anything.
