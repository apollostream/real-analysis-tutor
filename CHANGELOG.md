# Changelog

## Unreleased

Developer's Manual (Quarto book, `manual/`): eight chapters + FAQ +
URL-verified APA bibliography; eight Graphviz-dot vector figures; rendered
to GitHub Pages (HTML + downloadable PDF) by CI. README links added.

## 2.1.2 — 2026-07-18

Fix: the Stop-hook persist-state reminder now fires at most once per
session (workspace sentinel keyed by session id). Previously a stale
learner.json — e.g. resuming the morning after a session — triggered
the reminder after every single tutor response.

## 2.1.1 — 2026-07-17

Fix: remove explicit `hooks` field from plugin.json — the standard
hooks/hooks.json auto-loads, and the explicit reference caused a
duplicate-hooks load error on install.

## 2.1.0 — 2026-07-17

Initial release: full V2.1 methodology as a Claude Code plugin.
Author: Don Kearney — the tutor system and its source methodology
(V2.1 study guides) are Don Kearney's work and property.

- 10 skills (tutor front door + prime, check-proof, stuck, formalize, attack, assess,
  ledger, review, setup)
- 5 agents (proof-critic, counterexample-hunter, misconception-prober, lean-verifier,
  leakage-auditor)
- 3 hooks (SessionStart, UserPromptSubmit, Stop)
- Deterministic engine (learner state, SM-2 spaced-review scheduler, Theorem Ledger)
- Real Analysis curriculum pack (phase plan, misconception catalogue, mastery
  checklists, proof ladder, pedagogy reference)
