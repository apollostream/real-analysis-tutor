---
name: ledger
description: "Theorem Ledger V2.1 — add an entry or quiz from the ledger. Use after consolidation, or when the learner asks to be quizzed."
---

# Ledger

Two modes. Entry mode runs at the end of a topic session, after the Four-Part
Consolidation Assessment (`assess` skill), to record what was just proved.
Quiz mode runs any time the learner wants to be tested against entries
already on file — including as the first step of a monthly `review`.

You never author ledger content. Every field in Entry mode is a question you
put to the learner; your only job is formatting their answer into the JSON
shape `engine.ledger.append_theorem` expects. If you catch yourself typing a
statement, proof idea, or refutation before the learner has said it in their
own words, stop — you are not the authority here, Rudin and the mathematical
community are.

## Entry mode

Elicit all 14 `LEDGER_FIELDS` from the learner, one at a time or in a short
batch, in their own words:

| Field | Ask the learner for |
|---|---|
| `theorem` | A short name (e.g. `heine_cantor`). |
| `statement` | The theorem in their own words — never copied from Rudin. If they recite Rudin's phrasing, ask them to say it again without the book open. |
| `proof_idea` | One sentence: the essential move the proof turns on. |
| `load_bearing_hypothesis` | Which hypothesis is essential? |
| `counterexample_if_removed` | The counterexample when that hypothesis is dropped. |
| `converse_true` | `true` / `false` / `partial`. |
| `converse_example` | If false, the canonical counterexample; if true, is it a named result? |
| `misconception` | The named misconception for this theorem, drawn from `curriculum/real-analysis/misconceptions.yaml` for the current phase. |
| `misconception_refutation` | The precise invalid logical step plus the counterexample that breaks it. |
| `depends_on` | Which earlier ledger entries this proof invokes. |
| `downstream` | Which later results (so far) depend on this theorem. |
| `analogues` | Which earlier theorem shares this one's logical form or proof strategy. |
| `lean_status` | `compiled` / `in_progress` / `planned` / `unverified`. |
| `bloom_level` | Apply / Analyze / Evaluate / Create — carry over the level reached in the Four-Part Assessment. |

`misconception` and `misconception_refutation` are the one pair where a
catalogue exists (`misconceptions.yaml`) — but the catalogue is your
reference, not the learner's script. Tell the learner which misconception is
named for this theorem's topic if they don't already know, then require them
to restate the corrupted step and its refutation in their own words before
it goes in the ledger. A pasted catalogue sentence is not an entry; ask them
to say it again as if explaining it to someone else.

Once you have all 14 fields, validate and persist with the engine — never
hand-write `ledger.json`:

```
python3 -c "
import sys, json
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import ledger, state
ws = state.find_workspace(Path.cwd())
entry = {
    'theorem': 'heine_cantor',
    'statement': '...',
    'proof_idea': '...',
    'load_bearing_hypothesis': '...',
    'counterexample_if_removed': '...',
    'converse_true': 'false',
    'converse_example': '...',
    'misconception': 'continuity-implies-uniform-continuity',
    'misconception_refutation': '...',
    'depends_on': ['...'],
    'downstream': [],
    'analogues': '...',
    'lean_status': 'unverified',
    'bloom_level': 'Analyze',
}
ledger.append_theorem(ws, entry)
"
```

If `append_theorem` raises a `ValueError`, it names every missing field. Do
not fill those in yourself — turn the error straight back into questions for
the learner ("You're missing `analogues` and `downstream` — which earlier
theorem does this one resemble, and does anything you've proved so far
depend on it yet?") and retry once you have real answers.

## Quiz mode

Pick entries to quiz: concepts due for review first (`scheduler.due` against
`reviews.json`), then fill any remaining slots with random entries from
`ledger.load_ledger`. Never let the learner pick which entry — that defeats
the point of spaced review.

```
python3 -c "
import sys, json, random, datetime
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import ledger, scheduler, state
ws = state.find_workspace(Path.cwd())
led = ledger.load_ledger(ws)
reviews = scheduler.load_reviews(ws)
due_concepts = scheduler.due(reviews, datetime.date.today())
by_theorem = {e['theorem']: e for e in led}
order = [t for t in due_concepts if t in by_theorem]
rest = [t for t in by_theorem if t not in order]
random.shuffle(rest)
order += rest
print(json.dumps(order))
"
```

For each entry in that order, run the fixed four-step sequence — do not
skip a step or reorder it, and do not reveal the ledger's stored answer
before the learner has attempted it:

1. **State the theorem from memory.** No notes, no ledger open. Compare
   what they say against `statement` for substance, not word-for-word
   phrasing.
2. **Is the converse true?** If they say no, require the counterexample. If
   they say yes, ask whether it's a named result. Compare against
   `converse_true` / `converse_example`.
3. **Which hypothesis is load-bearing?** Require the counterexample that
   appears when it's removed. Compare against `load_bearing_hypothesis` /
   `counterexample_if_removed`.
4. **Refute the named misconception precisely.** Present `misconception` as
   a plausible student argument (never flag in advance which part is
   wrong) and require the specific invalid step plus the counterexample —
   "something's wrong" is not a refutation. Compare against
   `misconception_refutation`. Consider delegating this step to the
   `misconception-prober` agent when the catalogue entry (not just the
   ledger's restated version) is available — it's built for exactly this
   staged-argument-and-score exchange.

Grade the whole entry 0–5 (SM-2 scale: 5 perfect recall, 3 correct but
effortful, below 3 counts as a lapse) and record it — the interval math
lives in the scheduler, not in your judgment:

```
python3 -c "
import sys, datetime
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import scheduler, state
ws = state.find_workspace(Path.cwd())
reviews = scheduler.load_reviews(ws)
reviews = scheduler.record_review(reviews, 'heine_cantor', 4, datetime.date.today())
scheduler.save_reviews(ws, reviews)
"
```

Grade honestly. A learner who half-remembers the converse but nails the
misconception refutation earned something in between — don't round up to
make the session feel good, and don't round down to manufacture struggle
that isn't there.
