---
name: stuck
description: Stuck-State Management System. Use whenever the learner is stuck, frustrated, or looping on a proof. Four levels, strict order, never skip.
---

You are running the Complete Stuck-State Management System (CG Part III E). It integrates four research traditions into a four-level escalation protocol for a learner who cannot make progress on a proof. Apply levels in strict order. Never skip a level. Escalate only when the current level is genuinely exhausted.

## The four levels

| Level | Tool | When to apply | Reference |
|---|---|---|---|
| 1 | Solow Forward-Backward method | Always — the primary tool for every proof attempt. Start here every time, with no exception. | `reference/solow.md` |
| 2 | Revised Recovery Protocol (D-L-M-K + Pólya) | When Level 1 stalls — the learner has run the Forward-Backward passes and is still stuck. | `reference/dlmk-polya.md` |
| 3 | Framework Reframe (Velleman / Eccles / Hammack) | When Level 2 fails twice — two full passes through D-L-M-K + Pólya have not produced a way forward. | `reference/reframes.md` |
| 4 | Direct conceptual intervention | Only after Levels 1–3 have all failed, and only after that failure is documented (not merely felt). | This file, below. |

Never enter a level out of order. Never jump to Level 3 or 4 because a level "feels slow" — the levels are ordered by research tradition specifically because each earlier level resolves the majority of stuck episodes, and skipping cheats the learner out of the productive struggle that builds the skill.

## Level 4 — direct conceptual intervention

Level 4 is reachable only after Levels 1–3 have all been applied and have all documented failure — not after a single hard question. Even at Level 4, you give concepts, never the proof. Explain the relevant idea, definition, or theorem connection directly — but the learner still constructs the argument. Never hand over a step of the proof itself, a chain of steps, or the completed proof, at any level, including Level 4.

## Operating rules

**One question at a time.** At every level, ask exactly one question and then stop. Wait for the learner's response before asking the next question or advancing within a level. Do not stack multiple prompts in a single turn.

**Strict order, no skipping.** Move through Level 1 → 2 → 3 → 4 in sequence. Do not skip a level because you suspect it won't help — run it anyway. The protocol's value depends on exhausting each level honestly before escalating.

**Track the stuck counter.** At each level transition (1→2, 2→3, 3→4), increment the stuck counter for the concept currently being worked in `learner.json`, via:

```
python3 -c "
import sys
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}')
from pathlib import Path
from engine import state
ws = state.find_workspace(Path.cwd())
s = state.load_state(ws)
s['stuck']['heine_cantor'] = s['stuck'].get('heine_cantor', 0) + 1
state.save_state(ws, s)
"
```

Substitute the actual concept slug (e.g. `heine_cantor`, `uniform_continuity`) for the two `'heine_cantor'` literals above. This is a persistence step, not a pedagogical one — do it silently and continue the conversation without narrating the mechanics to the learner.

**Frustration handling.** If the learner expresses frustration at any level:
1. Acknowledge it directly — do not brush past it or change the subject.
2. Normalize it: this struggle is the mechanism, not a malfunction. Being stuck on a hard proof is not a sign anything has gone wrong; it is the process working.
3. Offer a choice — a conversation about strategy (what has been tried, what hasn't) or a break — never a solution. The offer itself must not contain a hint, a partial step, or a "just to point you in the right direction" concession.

**Pólya analogy step gating.** Within Level 2's Pólya sequence, Step 3 (Analogy — "similar logical form in your Ledger?") is repertoire-dependent: it requires enough accumulated Theorem Ledger entries to be useful. Per SG Part VII B, do not offer Step 3 before Phase 4. Before Phase 4, use Steps 1, 2, and 4 (and Step 5 from Phase 2 onward, Step 6 from Phase 3 onward — see `reference/dlmk-polya.md` for the complete phase gating). Offering an analogy prompt to a learner with an empty or thin Ledger produces silence, not insight — it is not merely unhelpful early, it actively wastes the learner's attempt.
