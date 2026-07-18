# Open ritual — returning learner

Run this at the very start of every returning session, on the learner's first message
whatever it says, before you address that message. Greet by progress, never by flattery.

## Step 1 — Read state through the engine

```bash
python3 -c "import sys,datetime;sys.path.insert(0,'$CLAUDE_PLUGIN_ROOT');from pathlib import Path;from engine import state,scheduler; ws=state.find_workspace(Path('.')); s=state.load_state(ws); rev=scheduler.load_reviews(ws); d=scheduler.due(rev, datetime.date.today()); print(state.state_digest(s,d))"
```

This gives you position (phase / chapter / rung), sessions completed, weakest concepts,
and concepts due for review.

## Step 2 — Report position, not praise

Greet by where they are in the work: name the phase and topic they reached and the number
of sessions completed. Do not open with "great job" or "you're doing amazing" — open with
"you left off at X."

## Step 3 — Surface due reviews

If concepts are due, name the top three (the engine returns them oldest-first). Frame them
as consolidation the spacing schedule has surfaced, not as a test.

## Step 4 — Propose today's agenda

Ask how much time they have today, then propose an agenda scaled to it from the
`weekly_rhythm` in `$CLAUDE_PLUGIN_ROOT/curriculum/real-analysis/curriculum.yaml`: pick the
rhythm day matching their position (network positioning, Strichartz first pass, mastery
checklist, Rudin reading, proof ladder, or the Four-Part Assessment) and trim it to fit
their available minutes. Propose, do not impose.

## Step 5 — The one question, then reconcile

Ask exactly one question: "What did you work on since last time?" Use their answer to
reconcile state — if they progressed past what `learner.json` records (finished a chapter,
raised a rung, mastered a due concept), update position and concepts through the engine
(`state.save_state`) before you begin the day's work. Then hand off to the six-stage loop.
