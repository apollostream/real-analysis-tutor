# Targeted Prompts for Real Analysis

Source of truth: `docs/source-guides/RealAnalysis_CompleteGuide_V2.1.md`,
Part IX, "The AI-Assisted Tutoring Framework" — "Targeted Prompts for
Real Analysis."

This is the tutor's internal move library: nine named prompts Claude
deploys at the appropriate moment in a tutoring session, independent of
the six-stage tutoring loop and the stuck-state escalation levels.

| Prompt Name | Prompt Text |
|---|---|
| Quantifier checking | Write the statement with all quantifiers explicit. Is this what I mean? What does it say if I swap the first universal and existential quantifier? |
| Delta-x diagnostic | Does my delta depend on x or only on epsilon? Trace: if \|x-a\| < delta, does my argument deliver \|f(x)-L\| < epsilon? |
| Hypothesis audit | Have I verified every hypothesis? Which is load-bearing? Give me a counterexample for each one removed. |
| Converse check | Is the converse of this theorem true? If not, what is the canonical counterexample? If yes, is it a known named result? |
| Misconception check (NEW 2.1) | Present the named misconception from the Ledger for this theorem as a plausible student argument. Ask me to identify the specific logical step that is invalid — not just that something is wrong — and to give the canonical counterexample. |
| Compactness interrogation | Have I verified the set is actually compact? Which property of compact sets am I using and why does the proof fail without it? |
| Knowledge graph | What does this theorem depend on? What later results depend on it? What breaks in analysis if we do not have this result? |
| Adversarial sequence | Give me the most dangerous sequence/function satisfying my hypotheses but that my proof would struggle with. |
| Informal image audit | What is my informal image of this concept? Let us find an example that matches my image but fails the formal definition. |
