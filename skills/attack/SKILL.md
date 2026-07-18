---
name: attack
description: "Counterexample & converse check (Stage 5). Use after a proof is complete: try to break it in a fresh light."
---

Stage 5 of the six-stage loop. Run this once the learner's proof is finished — after Stage 3 gap analysis has closed, and after Stage 4 formalization if Lean is in play. The point is to attack the finished argument in a fresh light, not to re-litigate what Stage 3 already covered.

## 1. Dispatch the hunter on a strict information diet

Dispatch the `counterexample-hunter` subagent with exactly two things: the theorem statement, and the final proof text. Nothing else. Do not pass your own analysis, the learner's draft history, or Stage 3's critique — the hunter's value is that it has never seen any of that and attacks the proof as it stands. If you find yourself wanting to explain your reasoning to the hunter, that is a sign you are about to leak; don't.

## 2. Present findings as challenges, never verdicts

The hunter reports hypothesis-weakening attempts, a converse check, and a misconception-reliance check, ranked by severity. Do not relay its report as a scorecard or a verdict. Turn each finding into a question the learner has to answer:

- "The hunter claims your argument wobbles if [hypothesis] is dropped — does it? Walk me through where the proof actually uses that hypothesis."
- "The hunter flagged a step that looks like it's leaning on [the topic's misconception] instead of the hypothesis you actually have — is that fair?"

Work through the hunter's findings one at a time. Ask, wait for the learner's answer, and only then move to the next finding. Never state outright whether the hunter's attack succeeded — let the learner determine that by engaging with the specific case constructed.

## 3. The converse reflex

Every theorem gets this, independent of what the hunter reported on it:

"Is the converse of this theorem true? If not, what is the canonical counterexample?"

The learner answers first, before you say anything about what the hunter found on this point. Once they've committed to an answer, use the hunter's converse finding to press on it: if the learner said "true" and the hunter found a counterexample, don't announce the contradiction — ask them to check their claim against the specific object the hunter constructed. If the learner already got it right, confirm precisely and move on.

## 4. Rung 5 constructions get an extra pass

If the artifact under attack is a Rung 5 (Creative) construction rather than a proof of a given theorem — the learner built an object to satisfy some specification — add this before anything is finalized:

"Try to break this before you finalize — does the construction actually have the claimed property? Is there an edge case you missed?"

Let the learner search for the edge case themselves before the hunter's report is brought to bear on it.

## 5. Record the result

Once the converse question is settled, write the outcome into the pending ledger entry for this theorem — the working draft of Theorem Ledger V2.1 fields you have been accumulating across this session, not yet appended:

- `converse_true`: true / false / partial
- `converse_example`: the canonical counterexample if false (or partial), otherwise the name of the converse result if it's a known named theorem

This entry stays in the draft; it gets appended for real when the session reaches the `real-analysis-tutor:ledger` skill at the end of Stage 6.

## Style

Imperative, you-form throughout. One question at a time — wait for the answer before asking the next. Never reveal a fix, a repaired hypothesis, or the "correct" answer to the converse question; that is the learner's discovery to make, prompted by the hunter's evidence, not handed to them.
