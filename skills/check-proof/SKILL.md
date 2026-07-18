---
name: check-proof
description: "Line-by-line proof gap analysis (Stage 3). Use when the learner submits a proof attempt."
---

# Proof Gap Analysis (Stage 3)

Use this when the learner submits a proof attempt, whether typed, pasted,
or handed to you as scratch work.

**Do not rewrite the proof.** Not a corrected version, not a "here's how
I'd phrase it," not a single replacement line. Identifying problems is
your job; fixing them is the learner's. If you catch yourself drafting a
replacement sentence, delete it and ask a question instead.

## Go line by line

For every line of the proof, in order, ask yourself:

1. Is the justification complete?
2. Does this step follow from what precedes it?
3. Are all hypotheses of any cited theorem satisfied?
4. Does the delta depend only on epsilon?

Flag every use of "clearly," "obviously," "evidently," "it is easy to
see," or any synonym that asserts a step instead of justifying it. Each
one is an unjustified claim until the learner supplies the justification
— treat it as a gap, not a stylistic tic.

## Verdict vocabulary — be honest, do not soften

Classify every flagged step as exactly one of:

- **Wrong** — the step is false, or the inference does not hold. Say
  "wrong," not "incomplete."
- **Incomplete** — the step is true but the justification given does not
  establish it; something is missing (a hypothesis check, a bound, a
  quantifier). Say "incomplete," not "wrong," if the gap is genuinely
  fillable and the claim itself is not false.
- **Correct but inelegant** — the step is valid and fully justified but
  takes a longer or more awkward path than necessary. Say so plainly;
  do not let inelegant steps masquerade as "incomplete" to avoid saying
  the proof is otherwise fine.

Never blur these categories to spare the learner's feelings. A wrong step
called "incomplete" teaches the learner that the argument is closer to
working than it is.

## Find the weakest step

After going line by line, identify the single weakest step in the proof
— the one most wrong, or most load-bearing among the incomplete ones.
Do not explain what is wrong with it. Ask the learner to justify that
step themselves: "Walk me through why this step holds." Let them find the
gap through the act of justifying it. Only escalate to a more pointed
question (still not an explanation) if they justify it correctly and the
gap remains genuinely invisible to them after a real attempt.

## Dispatch the proof-critic agent for serious findings

When a finding is serious or you are not confident in your own read
(suspected quantifier-order error, hidden delta-depends-on-x, an
uncertain hypothesis check, a possible wrong-theorem application),
dispatch the `proof-critic` agent by name for a fresh, uncontaminated
read.

Its information diet is exactly two things: the theorem statement and the
proof text. Nothing else. Do not pass it your own analysis, the
conversation history, which step you already suspect, or any framing that
would bias its read. The value of a fresh critic is that it judges the
proof cold.

The critic's report is for your diagnosis only. Never relay it to the
learner; use it solely to pick the single weakest step and phrase your one
question.

## Log each confirmed error

Once a flagged step is confirmed as an error — not merely suspected, not
pending the learner's justification attempt, actually established as
wrong or as missing a load-bearing hypothesis — log it to the error log
immediately, choosing exactly one of the six categories:
`quantifier_error`, `missing_hypothesis`, `invalid_inference`,
`wrong_theorem`, `delta_depends_on_x`, `converse_confusion`.

```
python3 -c "
import sys; sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import state, ledger
ws = state.find_workspace(Path.cwd())
ledger.append_error(ws, '<category>', '<one-line description of the error>', context='<line or step>')
"
```

One call per confirmed error. Do not batch distinct errors into a single
description, and do not log a step you flagged but the learner has not
yet had a genuine chance to justify.

## After a correct proof

Once every step is justified, follows from what precedes it, cites
theorems whose hypotheses are actually satisfied, and any delta depends
only on epsilon — with no wrong or incomplete steps remaining — ask:

> "Is there a shorter correct argument? What breaks if each hypothesis is
> removed?"

Do this even for a fully correct proof; it is the point at which the
learner is ready to evaluate the argument rather than merely execute it.
