# Developer's Manual (Quarto) — Design & Plan

**Date:** 2026-07-18 · **Approved:** user chose the lean Quarto manual (option 3) with fan-out build.

## Purpose & audience

A rendered Developer's Manual for the `real-analysis-tutor` repo. Audience: developers,
curriculum authors, and Don Kearney — NOT learners. The learner-facing zero-documentation
principle is untouched: README stays install-only, with one added pointer to the manual
under Development.

## Shape

- Quarto **book** project in `manual/` (HTML site + single downloadable PDF `real-analysis-tutor-manual.pdf`), rendered by CI to GitHub Pages (`gh-pages` branch).
- Six pages + FAQ. Lean chapters (300–700 words each except reference), no filler.
- Theme: built-in `cosmo` + small `manual/styles.scss` (textbook-blue accent #2B4C7E,
  Charter/Georgia body — matches the project's artifact identity), dark theme via `darkly`.

## Pages

| File | Title | Content source |
|---|---|---|
| `index.qmd` | Overview | What it is; 2-command install; the zero-doc promise; authorship (Don Kearney); map of the manual |
| `pedagogy.qmd` | The Pedagogical Frameworks | `docs/superpowers/notes/pedagogy-roles-answer.md` expanded with file references; division-of-labor table (Solow/Pólya/Bloom/Alcock) |
| `architecture.qmd` | Architecture | Three layers (deterministic/judgment/fresh-context); hooks; agents & information asymmetry; state files; anti-leakage design incl. red-team hardening summary |
| `generality.qmd` | Engine Generality | `docs/superpowers/notes/generality-answer.md` — the honest engine-vs-curriculum assessment, three hardwired tiers, scope caveat, accurate public phrasing |
| `extending.qmd` | Extending to a New Subject | What a curriculum pack contains (YAML schemas by example); the three tiers to edit today; the v2.2 decoupling roadmap; guides' Part XV alignment |
| `reference.qmd` | Reference | Engine API (state/scheduler/ledger signatures); hook contracts & events; workspace layout; ledger 14 fields; 6 error categories; curriculum YAML schemas |
| `faq.qmd` | FAQ | Short answers linking into chapters: subject-independent? Bloom's role? need Lean? where's my data? why won't it give answers? how do I reset? |

## Rules for authors

- Truth source is the repo + the two source notes; no invented capabilities; the
  generality page must keep the honest limits (do not oversell).
- Every factual claim about a file cites its repo path.
- Don Kearney credited as methodology/system author on index page.
- Tone: plain, precise, no marketing voice.

## Delivery

1. Scaffold `manual/` (`_quarto.yml`, `styles.scss`), CI workflow `.github/workflows/docs.yml`
   (quarto-actions setup → render → deploy `manual/_site` to `gh-pages`), README pointer.
2. Fan-out: one agent per page (7), parallel; each verifies its claims against the repo.
3. Review pass: accuracy/link/tone reviewer + local `quarto render` must pass.
4. Enable GitHub Pages on `gh-pages`; verify deploy; CHANGELOG entry.

Out of scope: learner-facing docs; API docs generation; versioned manuals.

## Addendum (2026-07-18, user-directed enrichment)

- Diagrams: standardized on Graphviz dot pre-rendered to SVG (HTML) + PDF (LaTeX), committed
  under `manual/figures/` with sources in `manual/figures/src/*.dot`. Rationale: vector output in
  both formats; no Chromium dependency in CI (mermaid rasterizes for PDF and needs Chrome).
  Liberal, informative visualization encouraged per user, incl. infographic-style figures.
- `bibliography.qmd`: formal APA bibliography; every entry carries a URL verified live (HTTP 200)
  at authoring time. Inline links from claim-bearing pages.
