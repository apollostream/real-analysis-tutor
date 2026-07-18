# Smoke Test Notes — 2026-07-17

Local marketplace add + install: PASS (`claude plugin marketplace add <repo>` → `claude plugin install real-analysis-tutor@real-analysis-tutor`, user scope).

Component inventory (`claude plugin details`): 10 skills, 5 agents, 3 hooks (SessionStart, UserPromptSubmit, Stop) — all auto-discovered with no explicit skills/agents manifest fields. Always-on token cost ~1.1k.

Live session probes (claude -p, haiku):
- Fresh dir WITH `.ra-tutor-workspace` marker, no learner.json → model reports it must introduce itself and run the real-analysis-tutor:tutor onboarding interview on the first message. FIRST-RUN directive delivered end-to-end. PASS
- Plain dir, no workspace → model reports no tutor context present. Hooks stay silent outside tutoring contexts. PASS

`claude plugin validate .` → Validation passed.
`pytest -q` → 38 passed.
