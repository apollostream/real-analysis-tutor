# Source note: engine generality — honest assessment (chat answer, 2026-07-18)

Question: is the tutor engine independent of the subject being learned — could a user
point it at any subject?

Answer: mostly, but not quite. Be precise.

## Genuinely subject-independent (the architecture)

Learner state, the SM-2 review scheduler, the Theorem Ledger machinery, the per-turn
Socratic guard, the stuck-state escalation, Bloom calibration, the misconception-probe
pattern, the four-part assessment, and the volunteering/zero-doc UX know nothing about
the subject. The curriculum lives as data in `curriculum/real-analysis/`. The source
guides' Part XV says exactly this: the methodology transfers to Topology and Abstract
Algebra with new content and near-zero process changes.

## Currently hardwired to Real Analysis — three tiers

1. **Content that doesn't exist for other subjects.** Only one curriculum pack ships,
   and the guides stress a new subject needs its own *researched* misconception
   catalogue, checklists, and text pairings. Authorship work, not code work.
2. **RA specifics baked into skill prose.** check-proof's "does your delta depend only
   on epsilon"; Lean/Mathlib specifics in formalize; the six error categories (one is
   literally `delta_depends_on_x`); the phase→misconception map hardcoded in the
   SessionStart hook. Straightforwardly editable, but today they'd talk about epsilons
   to a group-theory student.
3. **No selection mechanism.** The workspace marker records
   `"curriculum": "real-analysis"`, but nothing reads that field to switch packs.
   Dropping in `curriculum/topology/` would not activate it.

## Scope caveat

Even fully generalized, the engine is tuned to **proof-based mathematics** — converse
reflexes, proof ladders, formal verification. It is not a
point-it-at-French-or-history tutor.

## Accurate public phrasing

"The pedagogical engine is deliberately separated from the subject matter — extending
it to Topology or Abstract Algebra, as the guides' Part XV envisions, is mostly a
matter of authoring a new curriculum pack rather than rebuilding the tutor. Real
Analysis is the curriculum it ships with today."

## v2.2 decoupling roadmap (would make the strong claim fully true)

Make hooks and skills read subject specifics (misconception map, error categories,
diagnostic prompts) from the active curriculum pack keyed off the workspace marker;
ship a skeleton `curriculum/topology/` as proof.
