---
name: prime
description: "Concept priming before reading (Stage 1). Use before the learner opens any text on a new topic: network positioning, intuition surfacing, informal-image audit."
---

# Concept Priming (Stage 1)

Run this before the learner opens Rudin, Strichartz, or any other text on
the new topic. Nothing formal has been read yet. Your job is to surface
what the learner already believes, in their own words, before the book can
overwrite it.

**ABSOLUTE RULE: never reveal theorem content or proofs during priming.**
Not the statement, not a hint at the statement, not the proof strategy. If
the learner asks what the theorem says, decline and redirect to the
questions below — the whole point of priming is that it happens before the
formal content exists in the room.

## 1. Network positioning question — ask this first

Ask, and let the learner answer before you say anything else:

> "Where does this topic sit in the logical structure of Analysis so far?
> What will depend on it?"

This is a priming question, not a test — a rough or wrong answer is fine
and expected. Do not correct it now. Note internally that you will return
to this same question at the end of the week to see how the answer has
sharpened; do not reveal the correct dependency structure today.

## 2. Intuition surfacing questions

Ask questions that surface what the learner already knows and what their
intuitions are, without telling them the proof or the definition. Draw
from what they've done before: prior courses, related topics already
mastered, physical or geometric intuition. Examples of the shape these
take (adapt to the actual topic):

- "What do you already associate with this idea, from calculus or
  elsewhere?"
- "If you had to guess what could go wrong here, what would you guess?"
- "What's the simplest case where you're confident you know the answer?"

Keep asking until the learner has committed to something concrete — a
guess, an example, a rule of thumb — not a shrug.

## 3. Alcock informal-image audit

Ask directly:

> "What is your informal picture of this concept? Let's find the example
> that breaks it before you read the formal definition."

Get the learner's picture in their own words before supplying anything.
Then determine the current phase's known-dangerous image: find the
learner's current phase from workspace state,

```
python3 -c "
import sys; sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import state
st = state.load_state(state.find_workspace(Path.cwd()))
print(st['position']['phase'])
"
```

then read `${CLAUDE_PLUGIN_ROOT}/curriculum/real-analysis/misconceptions.yaml` If no entry exists for the current phase (prelim, phase8, phase9), proceed without one — the informal-image audit still runs on the learner's own stated picture.
and locate the entry whose `phase` field matches. Its `statement` field is
the known-dangerous informal image for this phase — hold it in reserve as
your working hypothesis for what the learner's picture is likely to be,
but do not recite it to the learner. Instead:

- If the learner's stated picture already matches the dangerous image,
  say so is not your move — ask them to construct, themselves, an example
  that satisfies their picture but that they suspect might misbehave.
- Guide the search toward the entry's `counterexample`, but make the
  learner find or construct it — do not hand it over. Ask questions that
  narrow the search ("what if the object weren't X?") rather than
  supplying the object.
- Do not reveal the entry's `refutation` or `corrupted_step` during
  priming — those belong to Stage 3 (`check-proof`) and later
  misconception probes, after the learner has actually attempted proofs
  against this idea. Priming ends once the informal picture has visibly
  cracked, not once it has been repaired.

## Closing the stage

Priming is done when the learner has: answered the network positioning
question in their own words, committed to at least one concrete intuition
or guess, and either found a counterexample to their informal picture or
made a genuine, recorded attempt to find one. Only then move on — the
learner opens the text next (Stage 2), not you.
