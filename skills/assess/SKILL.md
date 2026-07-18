---
name: assess
description: Four-Part Consolidation Assessment (Stage 6). Use at the end of every topic session. All four parts, fixed order, no skipping.
---

Stage 6 of the six-stage loop, and the last thing that happens before the session closes. Replaces the old one-shot "test me" prompt, which only ever reached Bloom Apply. Run all four parts, in this order, every time. Ask one question at a time and wait for the learner's answer before moving on.

## Part 1 — Applied problem (Bloom: Apply)

Give a specific epsilon-delta or construction problem on a non-trivial function or set — something requiring genuine construction, not a template the learner can pattern-match against. The guide's model for the register you're aiming for: "Prove from the definition that f(x) = x sin(1/x), extended by f(0) = 0, is continuous at 0." Write a comparably non-trivial problem for the topic just studied — don't reuse this one verbatim unless the topic is literally continuity at a point.

## Part 2 — Conceptual question (Bloom: Analyze)

Target the quantifier structure or the logical form of the theorem's conclusion; ask why it's formulated the way it is. The guide's pattern: take a definition with a delicate quantifier order (uniform continuity's delta-before-x is the canonical case) and ask what changes, precisely, if the quantifier order is swapped — require both statements written with all quantifiers explicit, and a description of how the set of objects satisfying each one differs. Build the analogous question for this session's topic; this must force engagement with logical architecture, not surface recall.

## Part 3 — Derivation step (Bloom: Evaluate)

Ask the learner to reconstruct a key lemma from logical structure, starting only from definitions and earlier results — not from a memorized proof sequence. Ask them to identify the exact line where the critical hypothesis enters.

If the learner starts reciting a memorized proof instead of rebuilding it, interrupt immediately: stop them, and redirect — "Don't recite it. Start from [the definition / the earlier result] only, and rebuild the step from there." Do this every time recitation starts, not just once.

## Part 4 — Misconception check (Bloom: Analyze + Evaluate)

If the current phase has no catalogue entry (prelim, phase8, phase9), skip the prober dispatch and instead probe the most recently studied phase's misconception, or omit Part 4 for prelim work — say so plainly. Dispatch the `misconception-prober` subagent with the current phase's full misconceptions.yaml entry — every field: `id`, `phase`, `topic`, `statement`, `corrupted_step`, `refutation`, `counterexample`, `presentation_note`. The prober stages the misconception as a plausible student argument and requires the three-part precise refutation: the exact invalid logical step, the canonical counterexample, and the hypothesis or repair that would make the argument valid. Relay the prober's rubric result (`located-step` / `counterexample-given` / `repair-stated`, each yes/partial/no) rather than re-grading it yourself — the prober already did the diagnostic work.

> **Do not skip to part (4) early or treat it as optional — it does the most diagnostic work and works best after parts 1–3.** Run all four parts, in sequence, every time.

## After part 4: grade, schedule, update, look back

**Grade.** Score each of the four parts 0–5. You are grading recall/performance quality; you are never computing an interval or a due date yourself — that is code's job, not the model's.

**Schedule.** For each part, identify the concept it actually exercised — usually this session's theorem or topic, but the derivation step or the misconception check may have exercised a prerequisite concept instead. Record one review per concept with the engine snippet pattern (never hand-compute a date):

```
python3 -c "
import sys, datetime
sys.path.insert(0, '<plugin-root>')
from pathlib import Path
from engine import scheduler
workspace = Path('<workspace>')
reviews = scheduler.load_reviews(workspace)
reviews = scheduler.record_review(reviews, '<concept>', <grade>, datetime.date.today())
scheduler.save_reviews(workspace, reviews)
"
```

**Update the pending ledger entry.** Set `bloom_level` to the highest level demonstrated this pass: Part 1 grade ≥ 3 demonstrates Apply; Part 2 grade ≥ 3 demonstrates Analyze; Part 3 grade ≥ 3 demonstrates Evaluate; Part 4 grade ≥ 3 on all three rubric dimensions reinforces Analyze/Evaluate. Record the single highest level actually cleared, not the level attempted.

**Pólya Look Back.** Ask these, one at a time, waiting for each answer before the next:

- "Could you have approached this differently?"
- "What was the key insight?"
- "Does this argument generalize?"
- "What's the weakest hypothesis you could have assumed?"

**Hand off.** The pending ledger entry now carries every field this session touched — statement, proof idea, load-bearing hypothesis and its counterexample, converse fields from `attack`, misconception and refutation from Part 4, and the `bloom_level` you just set. Invoke `real-analysis-tutor:ledger` to elicit and append the entry properly; do not append it yourself from here.

## Style

Imperative, you-form. One question at a time. Never reveal the answer to any of the four parts, the Look Back questions, or the misconception's resolution — the prober and this skill exist to make the learner produce the answer, not to supply it.
