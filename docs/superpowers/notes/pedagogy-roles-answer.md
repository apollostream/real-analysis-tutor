# Source note: explicit roles of pedagogical frameworks (chat answer, 2026-07-18)

Bloom's taxonomy is wired into four distinct mechanisms; other frameworks have equally
explicit but different jobs, mirroring the Complete Guide's Part III division of labor.

## Bloom's taxonomy — four operative roles

1. **Per-reply calibration.** The tutor skill's hidden pre-response plan — run silently
   before every pedagogical reply — includes "diagnosis → Bloom level + ladder rung →
   withhold-list → the one question." Every question is pitched at a chosen cognitive
   level. This directly targets the failure mode the guide names: AI tutors defaulting
   to Remember/Understand forever.
2. **Progression gating.** `curriculum/real-analysis/ladder.yaml` maps each proof-ladder
   rung to Bloom levels (Rung 1 → Remember/Understand, 2 → Apply, 3 → Analyze,
   4 → Evaluate, 5 → Create); the ladder gates ("Rungs 1–2 fluent before 3; Rung 4
   reliable before 5") mean the learner's Bloom level controls which problems are
   offered next.
3. **Assessment structure.** The Four-Part Consolidation Assessment is Bloom-indexed:
   applied problem → Apply; conceptual/quantifier question → Analyze; derivation step →
   Evaluate; misconception check → Analyze + Evaluate simultaneously. Escalation
   discipline: advance only on demonstrated mastery, stop at the first level that fails.
4. **Persistent measurement.** `bloom_level` is one of the fourteen required Theorem
   Ledger fields (pass threshold: grade ≥ 3 on the SM-2 scale); `learner.json` tracks a
   Bloom level per concept. The taxonomy is the unit in which mastery is stored and
   recalled across sessions.

## Other frameworks — explicit jobs

- **Solow's Forward-Backward method**: Level 1 of the stuck-state system (always first,
  own reference card `skills/stuck/reference/solow.md`); structures the `prime` skill's
  definition/theorem interrogation.
- **Pólya**: owns recovery. Stuck Level 2 embeds the full D-L-M-K + six-heuristic
  sequence with exact question texts, phase-gated as the guide specifies (analogy step
  disabled before Phase 4 — it needs a repertoire). The "Look Back" closes every proof
  and every session.
- **Alcock's research**: the self-explanation protocol with independence milestones
  (unprompted by Phase 3, automatic by Phase 5); the informal-image audit in `prime`;
  the misconception catalogue, grounded in the Hodds–Alcock–Inglis and
  Weber–Mejía-Ramos research programs.

## What makes these "explicit" rather than aspirational

Where they live: instruction text loaded at the moment it applies (skill bodies and
reference cards); machine-checked data (`ladder.yaml`, the ledger schema — CI fails if
they drift from the vendored guides); deterministic state the model cannot improvise
away (`learner.json`, `reviews.json`); and the per-turn UserPromptSubmit hook
re-anchoring the contract every time the learner speaks.
