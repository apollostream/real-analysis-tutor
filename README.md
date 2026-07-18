# Real Analysis Tutor

A Claude Code plugin that tutors you through Real Analysis (Baby Rudin +
Strichartz + Alcock, methodology V2.1) — Socratic by architecture: it will
never hand you a proof, it tracks your mastery across sessions, probes the
documented misconceptions for every topic, and verifies mathematics with
Lean 4 when available.

**Author: Don Kearney.** This AI tutor system and the V2.1 methodology it
operationalizes (the *Real Analysis Complete Study Guide* and the
*Low-Friction Setup & Workflow Guide*, vendored in `docs/source-guides/`)
are the work and property of Don Kearney.

## Install

Run Claude Code, and at its prompt, type:

```
/plugin marketplace add apollostream/real-analysis-tutor
/plugin install real-analysis-tutor@real-analysis-tutor
```

## That's it

Open Claude Code anywhere and say `hello` — the tutor takes it from there.
It introduces itself, interviews you to pick a starting point, creates its
own workspace, and offers Lean 4 setup only when you need it. You never
need to read anything else in this repository.

## Development

In the terminal at the `bash` prompt:

```
pip install -r requirements-dev.txt && pytest
```

**Developer's Manual:** [browse online](https://apollostream.github.io/real-analysis-tutor/) ·
[download PDF](https://apollostream.github.io/real-analysis-tutor/real-analysis-tutor-manual.pdf)
— how the tutor works, the pedagogical frameworks, engine generality, and how to
extend it to new subjects. (Source in `manual/`.)

Design docs: `docs/superpowers/`.     
Source methodology: `docs/source-guides/`.

## License

MIT
