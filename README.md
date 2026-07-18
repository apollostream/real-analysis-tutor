# Real Analysis Tutor

A Claude Code plugin that tutors you through Real Analysis (Baby Rudin +
Strichartz + Alcock, methodology V2.1) — Socratic by architecture: it will
never hand you a proof, it tracks your mastery across sessions, probes the
documented misconceptions for every topic, and verifies mathematics with
Lean 4 when available.

## Install

/plugin marketplace add apollostream/real-analysis-tutor
/plugin install real-analysis-tutor@real-analysis-tutor

## That's it

Open Claude Code anywhere and say hello — the tutor takes it from there.
It introduces itself, interviews you to pick a starting point, creates its
own workspace, and offers Lean 4 setup only when you need it. You never
need to read anything else in this repository.

## Development

pip install -r requirements-dev.txt && pytest

Design docs: docs/superpowers/. Source methodology: docs/source-guides/.

## License

MIT
