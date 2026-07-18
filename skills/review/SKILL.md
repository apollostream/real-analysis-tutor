---
name: review
description: "Monthly consolidation: full-ledger quiz, error-pattern analysis, dependency-graph re-mapping, misconception re-checks. Use monthly or when the tutor volunteers it."
---

# Review

Operationalizes the monthly consolidation block (CG Part XIII, SG Part X):
"Ideas opaque in Chapter 2 often become clear after Chapter 5." Run this
about once a month, or volunteer it yourself once roughly a month of ledger
entries has accumulated since the last review — don't wait to be asked.

Run the five parts below in order, on a single sitting if the learner has
the time for it. Every part starts with the learner producing something
from memory before you show them anything derived from the ledger or the
error log — the point of consolidation is reconstruction, not a report card.

## (a) Re-quiz the full ledger, due-first

Run the `ledger` skill's quiz mode, but scope it to every entry in
`ledger.json` rather than a handful — due-for-review concepts first (per
`scheduler.due`), then the remainder in random order. Same fixed sequence
per entry: state from memory, converse, load-bearing hypothesis,
misconception refutation. Same rule: never reveal the stored answer before
the learner has attempted it, and grade and record each one via
`scheduler.record_review`.

## (b) Error-pattern analysis

Pull the last 20 entries from the error log and count categories:

```
python3 -c "
import sys, json
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import ledger, state
ws = state.find_workspace(Path.cwd())
print(json.dumps(ledger.error_counts(ws, last_n=20)))
"
```

Report it as a diagnosis, not a table dump: name the single most common
category and say, in one sentence, the single most important thing to
watch for because of it — e.g. "Your most common error category is
delta-depends-on-x — the single most important thing to watch for is
checking, on every uniform-continuity argument, whether your delta survives
being written before you pick x, not after." Tie the advice to the specific
category, not a generic reminder.

## (c) Dependency-graph re-mapping

This is the section-level Forward-Backward pass applied to the whole
curriculum studied to date — run it in that order, not the reverse:

1. **The learner lists the graph first.** Ask them to list, from memory,
   every theorem they've proved so far and what each one depends on. Do
   not open the ledger or show them anything yet. Let gaps and wrong edges
   stand uncorrected while they build it.
2. **Ask which theorems are hubs and which are isolated.** Once they've
   listed it: which results are load-bearing for the most later theorems?
   Which feel most disconnected from everything else? Make them commit to
   an answer before you check it.
3. **Render the ledger's actual graph and compare.** Build a Mermaid
   diagram from every entry's `depends_on` and `downstream` fields:

   ```
   python3 -c "
   import sys, json
   sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
   from pathlib import Path
   from engine import ledger, state
   ws = state.find_workspace(Path.cwd())
   led = ledger.load_ledger(ws)
   edges = set()
   for e in led:
       for dep in e.get('depends_on', []) or []:
           edges.add((dep, e['theorem']))
       for down in e.get('downstream', []) or []:
           edges.add((e['theorem'], down))
   print(json.dumps(sorted(edges)))
   "
   ```

   Turn the edge list into a fenced `mermaid` block (`graph LR`, one arrow
   per edge, e.g. `heine_borel --> heine_cantor`) and show it alongside
   what the learner listed. Discuss the mismatches — a theorem the learner
   called isolated that the graph shows feeding three later results is
   itself a diagnostic finding, not a correction to shrug off.

## (d) Misconception re-checks, all topics studied so far

Not just the current phase — every topic with a `misconception` entry
touched anywhere in the ledger to date. For each one, stage the catalogue
argument again (delegate to the `misconception-prober` agent when you have
the full YAML entry from `curriculum/real-analysis/misconceptions.yaml`
available to hand it) and ask: "Are you still vulnerable to this one?"
Grade the same way as any other misconception probe — precise invalid step,
canonical counterexample, the repair — and don't accept a confident "no, I
remember this" in place of the learner actually producing the refutation
again. Confidence is not evidence; making them redo the refutation is.

## (e) Re-attempt one previously failed exercise

Pick one exercise the learner failed or abandoned in a past session —
without letting them look at their previous attempt or your previous
feedback on it. Hand it back cold. This is deliberate: an idea opaque in
an early chapter often becomes clear once later machinery is in place, and
the only way to find out is to try it again with nothing but what they now
know. If they succeed where they failed before, name that explicitly — it's
evidence the curriculum is compounding, not just accumulating. If they fail
again the same way, that's a real gap worth routing back through `stuck`
rather than something to paper over.
