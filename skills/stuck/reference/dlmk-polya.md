# Level 2 — The Revised Recovery Protocol (D-L-M-K + Pólya)

Source: CG Part III E, Level 2 table; phase gating from SG Part VII B. Apply this only after Level 1 (Solow Forward-Backward, `reference/solow.md`) has genuinely stalled. Run the steps below in order — D, then L, then M, then K, then the six Pólya heuristics. Ask one question at a time and wait for the learner's response before moving to the next step. Do not skip a step because a later one seems more promising.

## D — Diagnostic (Mason, Burton & Stacey)

Ask: **STUCK (blank wall) or CONFUSED (progress but unclear)?**

- If CONFUSED: re-examine all definitions before proceeding.
- If STUCK: proceed to Load Reduction.

## L — Load Reduction (Sweller — cognitive load)

Instruct: **Write out on paper: every definition of every object, every hypothesis, and exactly what you need to prove — all quantifiers explicit. Do this first.**

Do this step before any strategy discussion. Cognitive load from holding definitions in working memory is itself a common cause of stuckness; externalizing it onto paper is not a formality — it resolves a meaningful fraction of stuck episodes by itself.

## M — Monitoring (Schoenfeld)

Ask: **Genuine progress in the last 10 minutes?**

- If yes: continue with the current approach.
- If no: the current strategy is not working. A deliberate change is needed — proceed to Counterexample and then the Pólya heuristics.

## K — Counterexample (Lakatos)

Instruct: **Construct the most dangerous object satisfying the hypotheses. Does your current argument handle it? If not, what does the proof need to do that it is not?**

## The Pólya heuristics (in order)

Run these in numeric order. Each row gives the exact question or instruction to give the learner, and the phase from which that step is effective (SG Part VII B). Before a step's effective phase, skip it — do not offer a heuristic the learner's repertoire cannot yet support.

| Step | Heuristic | Claude's instruction or question | Effective from |
|---|---|---|---|
| 1 — Specialisation | Pólya | What happens in the simplest non-trivial case? | Phase 1 onward |
| 2 — Work backwards | Pólya | What would you need to already have for this to work? | Phase 1 onward |
| 3 — Analogy | Pólya | Similar logical form in your Ledger? (Repertoire-dependent.) | Phase 4 onward — check the Theorem Ledger; do not offer this step before Phase 4 |
| 4 — Decomposition | Pólya | Can you remove a condition and solve a simpler version first? | Phase 1 onward |
| 5 — Auxiliary element | Pólya | Is there a function, sequence, or set you could introduce? | Phase 2 onward |
| 6 — Repertoire | Pólya + Ledger | Which Theorem Ledger entry or proof technique might apply here? | Phase 3 onward |

Note the asymmetry: Steps 1, 2, and 4 are available from Phase 1 — they require no accumulated repertoire, only the definitions and hypotheses already written out in the Load Reduction step. Steps 5 and 6 need a small amount of accumulated Ledger content and open up progressively (Phase 2, then Phase 3). Step 3 is the most repertoire-hungry of the six and stays gated until Phase 4, when the Ledger has genuine depth to draw an analogy from.

## When to escalate

If a full pass through D-L-M-K and the phase-appropriate Pólya heuristics fails to produce progress, and this happens on **two** separate stuck episodes for the same impasse, escalate to Level 3 (`reference/reframes.md`) and increment the stuck counter for the concept as described in `SKILL.md`.
