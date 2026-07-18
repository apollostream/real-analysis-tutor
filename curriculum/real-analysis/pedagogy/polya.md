# Pólya's How to Solve It — Pros, Cons, and Mesh with Solow

Source of truth: `docs/source-guides/RealAnalysis_CompleteGuide_V2.1.md`,
Part III B, "Pólya's How to Solve It — Pros, Cons, and Mesh with Solow";
Part III E, "The Complete Stuck-State Management System" (Level 2 —
Revised Recovery Protocol, D-L-M-K + Pólya); and
`docs/source-guides/Setup_Workflow_Guide_V2.1.md`, Part VII B, "Pólya's
Recovery Protocol" (effective-from-phase table).

## Pros, cons, and mesh with Solow

Pólya's project is fundamentally heuristic — cataloguing the mental
moves that skilled problem solvers make. His four-phase framework
(Understand, Plan, Execute, Look Back) is a descriptive map of the
problem-solving process, populated with specific heuristics.

**Strengths:** Makes tacit knowledge explicit. The Look Back phase
consolidates genuine mathematical understanding. Domain-independent.
Validates productive struggle as part of the process.

**Weaknesses:** Heuristics are hard to apply without domain knowledge.
The four phases are descriptive, not procedural. "Devise a Plan" carries
most of the weight but gets the least specific guidance. Oriented toward
competition-style problems; transfers less cleanly to epsilon-delta
proof-writing.

**How Pólya and Solow relate:** They are complementary but operating at
different levels. Solow addresses Pólya's weakest point: where Pólya is
vaguest — devising the plan — Solow is most concrete, providing a
systematic procedure for exactly that transition.

## Level 2 — The Revised Recovery Protocol (D-L-M-K + Pólya)

Applied when Level 1 (Solow's Forward-Backward method) stalls.

| Step | Source | Claude's Instruction or Question |
|---|---|---|
| D — Diagnostic | Mason, Burton & Stacey | Ask: STUCK (blank wall) or CONFUSED (progress but unclear)? If CONFUSED: re-examine all definitions before proceeding. If STUCK: proceed. |
| L — Load Reduction | Sweller (cognitive load) | Write out on paper: every definition of every object, every hypothesis, and exactly what you need to prove — all quantifiers explicit. Do this first. |
| M — Monitoring | Schoenfeld | Genuine progress in the last 10 minutes? If yes: continue. If no: current strategy is not working. A deliberate change is needed. |
| K — Counterexample | Lakatos | Construct the most dangerous object satisfying the hypotheses. Does your current argument handle it? If not: what does the proof need to do that it is not? |
| 1 — Specialisation | Pólya | What happens in the simplest non-trivial case? |
| 2 — Work backwards | Pólya | What would you need to already have for this to work? |
| 3 — Analogy (Phase 4+) | Pólya | Similar logical form in your Ledger? (Repertoire-dependent.) |
| 4 — Decomposition | Pólya | Can you remove a condition and solve a simpler version first? |
| 5 — Auxiliary element | Pólya | Is there a function, sequence, or set you could introduce? |
| 6 — Repertoire | Pólya + Ledger | Which Theorem Ledger entry or proof technique might apply here? |

## Effective-from-phase table

When Solow's method stalls, these heuristics are applied in order.
Critically, the analogy heuristic (Step 3) requires a repertoire — it is
only effective from Phase 4 onward, once the Theorem Ledger has
accumulated depth.

| Step | Heuristic | Effective From |
|---|---|---|
| 1 | Specialisation: what happens in the simplest non-trivial case? | Phase 1 onward |
| 2 | Work backwards: what would I need to already have? | Phase 1 onward |
| 3 | Analogy: have I proved anything with a similar logical form? (check Ledger) | Phase 4 onward |
| 4 | Decomposition: can I remove a condition and solve a simpler version? | Phase 1 onward |
| 5 | Auxiliary element: is there an object I could introduce to bridge the gap? | Phase 2 onward |
| 6 | Repertoire: which Theorem Ledger entry might apply here? | Phase 3 onward |
