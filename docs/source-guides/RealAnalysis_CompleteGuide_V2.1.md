**Real Analysis**

**A Complete Self-Study Guide**

Revised & Expanded Edition --- Version 2.1

Baby Rudin · Strichartz · Alcock · Proof Foundations

Pedagogical Frameworks: Solow · Pólya · Bloom

Research-Grounded Tutoring · Mastery Checklists · Misconception
Catalogue

Proof-Practice Ladder · AI-Assisted Socratic Tutoring

Lean 4 Formal Verification · Free Stack Workflow

This guide integrates a comprehensive learning programme for Real
Analysis with a mastery-based Strichartz--Rudin study plan, full chapter
alignment, per-topic mastery checklists with converse fields and a
seven-topic misconception catalogue, and a five-rung proof-practice
ladder. The tutoring framework incorporates three pedagogical frameworks
(Solow, Pólya, Bloom), key findings from Alcock\'s research-based
pedagogy, and the undergraduate mathematics education literature. The
AI-assisted workflow uses Claude with a structured Socratic methodology,
Lean 4 formal verification, and both paid and free tool stacks.

> **Contents**

**Part I** The Texts --- A Complete Survey (Nine Texts)

**Part II** The Proof Foundations Library

**Part III** Pedagogical Frameworks: Solow, Pólya, and Bloom

**Part IV** Chapter Alignment: Strichartz ↔ Rudin

**Part V** Mastery Checklists with Misconception Catalogue and Lean 4
Targets

**Part VI** The Proof-Practice Ladder --- Five Rungs

**Part VII** The Combined Reading Workflow

**Part VIII** The Master Reading Plan --- All Phases

**Part IX** The AI-Assisted Tutoring Framework

**Part X** Research Literature: What the Evidence Shows

**Part XI** Formal Verification with Lean 4

**Part XII** Tool Stack --- Claude Code and Free Stack Workflows

**Part XIII** The Complete Weekly Rhythm

**Part XIV** Key Principles and Final Recommendations

> **Part I --- The Texts --- A Complete Survey**

Nine texts form the core of this curriculum, organised by function:
primary one-variable analysis texts, advanced multivariable texts,
supplementary references, and a metacognitive preparation text. Each is
described with its strengths, weaknesses, and precise role.

**1. Rudin --- Principles of Mathematical Analysis**

Role: Primary rigour text and the destination of the entire programme.

**Strengths:**

-   Unmatched logical precision; every hypothesis is necessary.

-   The worldwide graduate standard --- Rudin\'s theorem numbering has
    direct professional value.

-   Chapter 7 (sequences and series of functions) is one of the finest
    treatments of uniform convergence available.

-   Exercises are curriculum, not supplement --- many key results appear
    only there.

**Weaknesses:**

-   No motivation --- definitions appear without explanation of why they
    are formulated as they are.

-   Chapters 1 and 2 are brutal as openers.

-   Chapters 9--10 (multivariable) are weaker than the one-variable
    material; NSS and Loomis--Sternberg do multivariable better.

  -----------------------------------------------------------------------
  **The Golden Rule:** Supply every implicit step. When Rudin writes \"it
  follows that...\" or \"clearly...\", prove the missing step on scratch
  paper. A one-page Rudin proof may require three or four pages of your
  own work to fully justify. Realistic pace: 3--8 pages per day of fully
  engaged reading.

  -----------------------------------------------------------------------

**2. Strichartz --- The Way of Analysis**

Role: Primary motivation and companion text throughout Chapters 1--8.

**Strengths:**

-   Best available motivation for why analysis is structured as it is.

-   Definitions emerge after you have seen why they are needed.

-   Fourier series context makes abstract machinery feel necessary
    rather than arbitrary.

-   Graduated exercises with more scaffolding than Rudin.

**Weaknesses:**

-   Long --- motivation costs concision.

-   Lower aesthetic elegance than Rudin.

-   Less universally known --- limited reference value in graduate
    programmes.

  -----------------------------------------------------------------------
  **Pairing rule:** Always read Strichartz first on any topic, then Rudin
  immediately. Never reverse this order. The Strichartz chapter builds
  the mental model; the Rudin chapter provides the rigorous treatment.

  -----------------------------------------------------------------------

**3. Abbott --- Understanding Analysis**

Role: Optional gentle opener for students who find Strichartz too
demanding as a first encounter.

**Strengths:**

-   Most accessible rigorous analysis text.

-   Excellent for a first encounter with epsilon-delta reasoning.

-   More motivation, more examples, and gentler proofs than either
    Strichartz or Rudin.

**Weaknesses:**

-   Limited scope compared to Strichartz.

-   Not the reference your graduate programme will assume.

For students who struggle with Strichartz in the early chapters, Abbott
→ Strichartz → Rudin is a viable three-pass approach. For students who
engage Strichartz without difficulty, Abbott is optional.

**4. Tao --- Analysis I and II (free online)**

Role: Alternative foundations text --- best available explanation of why
the axioms are chosen as they are.

**Strengths:**

-   Constructs the real numbers from the Peano axioms upward.

-   Explains at each step why the axiom is needed and what fails without
    it.

-   Explains Rudin-style arguments with more detail than Rudin provides.

-   Free from Tao\'s UCLA website.

**Weaknesses:**

-   Two-volume scope is broader than the one-variable focus of this
    plan.

-   Some students find the axiomatic development slow.

Particularly valuable during Phase 1 (Real Numbers) and whenever
Rudin\'s logical foundations feel arbitrary.

**5. Pugh --- Real Mathematical Analysis**

Role: Alternative rigour text at Rudin\'s level --- consult when
Rudin\'s approach is opaque.

**Strengths:**

-   Geometric intuition that Rudin systematically omits.

-   More figures than Rudin --- Rudin contains almost no diagrams.

-   Full rigour at graduate level.

-   Different proof style for the same results --- useful when Rudin\'s
    approach is impenetrable.

**Weaknesses:**

-   Less standard than Rudin --- not the reference your graduate
    programme will assume.

-   More verbose than Rudin, which some students find slower.

Best use: Keep on the shelf. When you have spent three serious attempts
understanding a Rudin proof and it remains opaque, read Pugh\'s version.
The different perspective often breaks the logjam.

**6. Nickerson, Spencer & Steenrod --- Advanced Calculus (NSS)**

Role: Primary multivariable analysis text --- use after completing Rudin
Chapters 1--8.

**Strengths:**

-   Conceptually the most coherent treatment of multivariable calculus
    available.

-   The derivative is a linear transformation; the chain rule is
    composition of linear maps.

-   Treatment of differential forms is superb.

-   The progression from linear algebra through differentiation to
    Stokes\' theorem is internally consistent.

**Weaknesses:**

-   High abstraction from page one.

-   Requires proof-based linear algebra as a genuine prerequisite.

-   Out of print --- PDF copies circulate.

  -----------------------------------------------------------------------
  **Sequencing warning:** Do NOT read NSS before or alongside Rudin
  Chapters 1--8. Complete the Strichartz--Rudin plan first. NSS does
  multivariable analysis better than Rudin Chapters 9--10.

  -----------------------------------------------------------------------

**7. Loomis & Sternberg --- Advanced Calculus (free online)**

Role: Encyclopedic advanced text --- for students heading toward
mathematical physics or differential geometry.

**Strengths:**

-   Unique in connecting abstract analysis to classical mechanics and
    physics.

-   Nearly 600 pages of graduate mathematics at no cost. Free from
    Sternberg\'s Harvard webpage.

**Weaknesses:**

-   Breadth means depth is thinner per topic. High density throughout
    --- not linear reading.

Best used as a reference alongside NSS for multivariable work, or for
students with physics or geometry goals.

**8. Spivak --- Calculus on Manifolds**

Role: Short, accessible bridge to multivariable analysis --- read before
NSS or Loomis--Sternberg.

**Strengths:**

-   Covers implicit function theorem, differential forms, and Stokes\'
    theorem with clarity and rigour.

-   Significantly more accessible than either NSS or Loomis--Sternberg
    as a first encounter. 146 pages --- a manageable entry point.

**Weaknesses:**

-   Short scope --- not a complete multivariable treatment. Assumes
    strong one-variable background.

**9. Alcock --- How to Think About Analysis (Metacognitive Preparation
Text)**

Role: Metacognitive preparation text --- the only book in this
curriculum concerned with how to study Analysis rather than the content
of Analysis itself.

**Strengths:**

-   Research-based advice grounded in empirical studies of how students
    actually read proofs.

-   Explicitly identifies the specific difficulty zones in every major
    topic.

-   Introduces the Hodds--Alcock--Inglis self-explanation training
    protocol.

-   Short Part 1 (four chapters, \~50 pages) can be read before any
    other text in this curriculum.

**Weaknesses:**

-   Not a rigour text --- does not replace Rudin or Strichartz. Does not
    develop proof-writing fluency --- does not replace Solow.

Positioning: Read Part 1 of Alcock before beginning Solow. Use Part 2 as
a chapter-by-chapter companion during the corresponding phases of the
main plan.

> **Part II --- The Proof Foundations Library**

Four texts develop proof-writing fluency before Real Analysis begins.
Each occupies a distinct position. The integrated sequence uses all four
in a specific order grounded in four pedagogical reasons specific to the
destination of Baby Rudin.

**1. Solow --- How to Read and Do Proofs**

Role: The procedural scaffold --- teaches exactly what to write on the
blank page. Solow\'s insight: most students fail at proofs not from lack
of ability but from lack of an explicit, nameable system for what to do
next. The Forward-Backward Method maps directly onto epsilon-delta
proofs. Named techniques include: Choose Method (universal conclusions),
Construction Method (existence statements), Specialization Method,
Contradiction, and Contrapositive.

Strength: Gives students something concrete to do at each step. Named
vocabulary is genuinely useful for diagnosis. Most valuable at the
earliest stages when no repertoire exists.

Weakness: Can become a crutch. Mathematical content is thin.
Deliberately repetitive pace.

**2. Hammack --- Book of Proof (free online)**

Role: Breadth, worked models, and the cardinality bridge to Rudin
Chapter 2. Free at richardhammack.net. Covers sets, logic, all proof
methods, relations, functions, and cardinality. The cardinality chapter
(Cantor\'s diagonal argument, countability, uncountability) directly
preludes Rudin Chapter 2.

Strength: Breadth of proof types. Worked examples show what finished
proofs look like. Cardinality chapter is the specific bridge to Rudin
Ch. 2.

Weakness: Gentle approach may not fully prepare for Rudin\'s abruptness.

**3. Eccles --- An Introduction to Mathematical Reasoning**

Role: Logical rigour and quantifier precision --- the most direct
preparation for the for-all-epsilon-there-exists-delta machinery of Real
Analysis. Eccles spends serious time on propositional logic and the
precise logical structure of quantified statements.

Strength: Strongest quantifier treatment of the four books. Substantive
mathematical content (number theory, combinatorics).

Weakness: Harder and faster than it appears --- better for students with
some prior proof exposure than for complete beginners.

**4. Velleman --- How to Prove It**

Role: The deepening text --- most thorough treatment of proof strategy
available. More systematic about proof strategy than Hammack, more
accessible than Eccles, and particularly strong on the relationship
between logical structure and proof construction.

Strength: Especially good on proofs involving quantifiers and on proof
by contradiction.

Weakness: Solow is the more forgiving starting point for beginners;
Velleman rewards prior proof experience.

**The Integrated Preliminary Plan --- Sequencing**

  -----------------------------------------------------------------------------------
  **Step**   **Text**        **Duration**   **What It Provides**   **Why This
                                                                   Position**
  ---------- --------------- -------------- ---------------------- ------------------
  1          Solow Ch. 1--13 2 wks (new) 1  Forward-Backward       Procedural
                             wk (exp.)      method, named          scaffold before
                                            vocabulary             models --- avoids
                                                                   pattern-matching
                                                                   without
                                                                   constructive
                                                                   understanding

  2          Hammack Ch.     2--3 wks (new) Breadth of proof       Solow\'s
             1--12           skip (exp.)    types, worked models,  vocabulary makes
                                            cardinality chapter    Hammack\'s
                                                                   examples mutually
                                                                   reinforcing;
                                                                   cardinality is the
                                                                   bridge to Rudin
                                                                   Ch. 2

  3          Eccles Ch. 1--5 1 wk           Quantifier precision,  Logical rigour as
                                            for-all/there-exists   targeted
                                            structure              preparation after
                                                                   fluency exists

  4          Velleman        2--3 wks       Deepest proof strategy For students with
             (optional)                     treatment available    strong
                                                                   mathematical
                                                                   appetite; read
                                                                   after Solow +
                                                                   Hammack if time
                                                                   allows
  -----------------------------------------------------------------------------------

> **Part III --- Pedagogical Frameworks: Solow, Pólya, and Bloom**

Three pedagogical frameworks underlie this guide\'s tutoring
methodology. They are not redundant --- each governs a different
dimension of the learning process. Understanding how they divide labour
and reinforce each other is essential for using this guide effectively.

**A. Solow\'s Forward-Backward Method**

Solow\'s Forward-Backward method is the primary procedural framework for
this guide. It applies not only to constructing proofs but to
understanding definitions and theorems before any proof work begins.

**Applying the Method to Definitions**

Backward pass --- unpack the structure: ask what the definition is
actually asserting. Identify the key terms; rephrase the definition; ask
what logical form it takes (conjunction? implication? quantified
statement?).

Forward pass --- connect to known ground: what examples do you already
know should satisfy this? What should NOT satisfy this? What simpler or
related definition does this generalise or specialise?

**Applying the Method to Theorems (Before Proving Them)**

Backward pass --- understand the conclusion: identify its form
(existence claim? equality? implication? bound?). Ask what technique or
object would be needed to make this true. Ask what quantifier structure
the conclusion has.

Forward pass --- interrogate the hypotheses: list every hypothesis
explicitly --- stated and unstated. Ask why each hypothesis is there.
Imagine what breaks without it. Ask what each hypothesis immediately
lets you conclude.

**Section-Level Application: Build the Map Before the Territory**

Before attempting a single proof in a section, run the Forward-Backward
method over the entire section first. Start from the END --- find the
section\'s main result and ask what it is claiming. Then work backward
through the section. Then start from the BEGINNING with the destination
in mind. This turns mathematical reading from a linear march into
building a map before exploring the territory.

  -----------------------------------------------------------------------
  When you finally sit down to prove exercises, you have already done
  most of the hard conceptual work. You know what the section is
  fundamentally about, which definitions are critical, how the theorems
  relate, and where the logical pressure points are.

  -----------------------------------------------------------------------

**B. Pólya\'s How to Solve It --- Pros, Cons, and Mesh with Solow**

Pólya\'s project is fundamentally heuristic --- cataloguing the mental
moves that skilled problem solvers make. His four-phase framework
(Understand, Plan, Execute, Look Back) is a descriptive map of the
problem-solving process, populated with specific heuristics.

Strengths: Makes tacit knowledge explicit. The Look Back phase
consolidates genuine mathematical understanding. Domain-independent.
Validates productive struggle as part of the process.

Weaknesses: Heuristics are hard to apply without domain knowledge. The
four phases are descriptive, not procedural. \"Devise a Plan\" carries
most of the weight but gets the least specific guidance. Oriented toward
competition-style problems; transfers less cleanly to epsilon-delta
proof-writing.

How Pólya and Solow relate: They are complementary but operating at
different levels. Solow addresses Pólya\'s weakest point: where Pólya is
vaguest --- devising the plan --- Solow is most concrete, providing a
systematic procedure for exactly that transition.

**C. Bloom\'s Taxonomy Applied to Real Analysis**

Bloom\'s Taxonomy provides a framework for calibrating question depth.
The critical failure mode of most AI tutors --- and most students
studying alone --- is defaulting to the bottom two levels: Remember and
Understand. Real Analysis mastery requires systematic progression
through all six levels for each major result.

  ------------------------------------------------------------------------
  **Bloom      **Example (Uniform         **Example          **Target
  Level**      Continuity)**              (Compactness)**    Phase**
  ------------ -------------------------- ------------------ -------------
  Remember     State the definition with  State the open     Every phase
               all quantifiers explicit.  cover definition   
                                          of compactness.    

  Understand   Explain why delta must not Explain what       Every phase
               depend on x. What breaks   \"every open cover 
               if it does?                has a finite       
                                          subcover\" is      
                                          asserting.         

  Apply        Prove f(x) = sqrt(x) is    Use Heine-Borel to Rungs 1--2
               uniformly continuous on    determine whether  
               \[1, ∞).                   (0,1\] is compact. 

  Analyze      Which hypothesis in        Where exactly does Rungs 3--4
               Heine-Cantor is essential? EVT invoke         
               Trace where compactness is compactness?       
               invoked.                                      

  Evaluate     Is your proof the minimum  Is there a shorter Rung 4
               correct argument? Where is proof of           
               it doing unnecessary work? Heine-Borel?       

  Create       Construct a function       Construct a set    Rung 5
               continuous on R but not    bounded but not    
               uniformly continuous.      compact in an      
                                          unusual metric.    
  ------------------------------------------------------------------------

**D. Synthesis: How the Three Frameworks Divide Labour**

  ------------------------------------------------------------------------------
  **Framework**      **Governs**                              **Primary Tool**
  ------------------ ---------------------------------------- ------------------
  Solow              Proof strategy --- how the tutor guides  Forward-Backward
                     a student through the logical structure  Method
                     of a specific argument                   

  Pólya              Problem-solving recovery --- what        Heuristic
                     questions to ask when the student is     catalogue
                     stuck and needs a new idea               

  Bloom              Question calibration --- ensuring        Six-level taxonomy
                     development across all cognitive levels, 
                     not just surface recall                  
  ------------------------------------------------------------------------------

**E. The Complete Stuck-State Management System**

When a student is genuinely stuck, a more structured intervention is
needed. The Complete Stuck-State Management System integrates four
research traditions into a four-level escalation protocol. It is the
most comprehensive treatment of stuck-ness available for this curriculum
and is embedded in both the CLAUDE.md tutoring instructions and the AI
Tutoring Framework in Part IX.

  --------------------------------------------------------------------------
  **Level**   **Tool**                  **When to Apply**     **Research
                                                              Basis**
  ----------- ------------------------- --------------------- --------------
  Level 1     Solow Forward-Backward    Always --- the        Solow (2014)
              method                    primary tool for      
                                        every proof attempt   

  Level 2     Revised Recovery Protocol When Level 1 stalls   Mason et al.;
              (D-L-M-K + Pólya)                               Sweller;
                                                              Schoenfeld;
                                                              Lakatos; Pólya

  Level 3     Framework Reframe         When Level 2 fails    Velleman;
              (Velleman / Eccles /      twice                 Eccles;
              Hammack)                                        Hammack

  Level 4     Direct conceptual         Only after Levels     Responsive
              intervention              1--3 all fail         tutoring
                                                              research
  --------------------------------------------------------------------------

**Level 2 --- The Revised Recovery Protocol (D-L-M-K + Pólya)**

  ----------------------------------------------------------------------------
  **Step**         **Source**      **Claude\'s Instruction or Question**
  ---------------- --------------- -------------------------------------------
  D --- Diagnostic Mason, Burton & Ask: STUCK (blank wall) or CONFUSED
                   Stacey          (progress but unclear)? If CONFUSED:
                                   re-examine all definitions before
                                   proceeding. If STUCK: proceed.

  L --- Load       Sweller         Write out on paper: every definition of
  Reduction        (cognitive      every object, every hypothesis, and exactly
                   load)           what you need to prove --- all quantifiers
                                   explicit. Do this first.

  M --- Monitoring Schoenfeld      Genuine progress in the last 10 minutes? If
                                   yes: continue. If no: current strategy is
                                   not working. A deliberate change is needed.

  K ---            Lakatos         Construct the most dangerous object
  Counterexample                   satisfying the hypotheses. Does your
                                   current argument handle it? If not: what
                                   does the proof need to do that it is not?

  1 ---            Pólya           What happens in the simplest non-trivial
  Specialisation                   case?

  2 --- Work       Pólya           What would you need to already have for
  backwards                        this to work?

  3 --- Analogy    Pólya           Similar logical form in your Ledger?
  (Phase 4+)                       (Repertoire-dependent.)

  4 ---            Pólya           Can you remove a condition and solve a
  Decomposition                    simpler version first?

  5 --- Auxiliary  Pólya           Is there a function, sequence, or set you
  element                          could introduce?

  6 --- Repertoire Pólya + Ledger  Which Theorem Ledger entry or proof
                                   technique might apply here?
  ----------------------------------------------------------------------------

**Level 3 --- Framework Reframes (Velleman / Eccles / Hammack)**

  -----------------------------------------------------------------------
  **Reframe**        **Claude\'s Instruction**
  ------------------ ----------------------------------------------------
  Velleman ---       Set aside mathematical content. State the complete
  Logical Form       logical form of your conclusion with ALL quantifiers
                     explicit and in order. What proof structure does
                     this quantifier sequence call for, independently of
                     what the variables represent?

  Eccles --- Logical Write the logical skeleton of the entire statement
  Skeleton           using only logical symbols and quantifiers. Replace
                     every mathematical predicate with a letter. Strip
                     all content. What does the skeleton alone tell you
                     about proof strategy?

  Hammack ---        Describe this proof in the most elementary terms
  Elementary         possible, as if explaining to someone who knows only
  Restatement        basic logic. Strip all analysis-specific language.
                     At its simplest, what are you trying to show?
  -----------------------------------------------------------------------

> **Part IV --- Chapter Alignment: Strichartz ↔ Rudin**

The table below maps each Strichartz chapter to the corresponding Rudin
chapter. Topology gap: Rudin Chapter 2 has no direct Strichartz
counterpart --- Strichartz integrates topological ideas throughout.
Supplement with Munkres Topology Chapter 2 (Sections 12--21). Workflow
rule: Read the Strichartz chapter first for motivation, then the
corresponding Rudin chapter immediately after. Do not delay Rudin until
full Strichartz mastery.

  --------------------------------------------------------------------------------------
  **Strichartz**    **Rudin**           **Core Concepts**            **Supplement**
  ----------------- ------------------- ---------------------------- -------------------
  Ch. 1 Real        Ch. 1 Real &        Completeness, sup/inf,       Tao Analysis I
  Numbers           Complex Fields      Archimedean property,        
                                        Dedekind cuts                

  (topology         Ch. 2 Basic         Metric spaces, open/closed   REQUIRED: Munkres
  throughout)       Topology            sets, compactness (open      Ch. 2 ss.12--21
                                        cover), Heine-Borel,         
                                        connected sets, Cantor set   

  Ch. 2 Sequences   Ch. 3 Sequences &   epsilon-N limits, Cauchy     Pugh Ch. 2 if
                    Series              sequences, monotone          opaque
                                        convergence, limsup/liminf,  
                                        rearrangements               

  Ch. 3 Series      Ch. 3 (cont.)       Convergence tests, absolute  ---
                                        vs conditional, alternating  
                                        series, rearrangements       

  Ch. 4 Continuity  Ch. 4 Continuity    epsilon-delta continuity,    ---
                                        uniform continuity,          
                                        compactness, connectedness,  
                                        IVT, EVT, Heine-Cantor       

  Ch. 5             Ch. 5               Derivative as linear         ---
  Differentiation   Differentiation     approx., MVT, Rolle, Taylor, 
                                        L\'Hôpital                   

  Ch. 6 Integration Ch. 6               Upper/lower sums,            Note: Rudin
                    Riemann-Stieltjes   integrability of continuous  generalizes to
                                        functions, FTC I and II      Stieltjes

  Ch. 7 Seq. &      Ch. 7 Seq. & Series Uniform vs pointwise         Strichartz Fourier
  Series of Fns     of Fns              convergence, Weierstrass     series chs.
                                        M-test, Arzela-Ascoli,       
                                        Weierstrass approximation    

  ---               Ch. 8 Special       Power series, exp/log/trig   Read alongside
                    Functions           via power series, gamma      Strichartz Fourier
                                        function, Fourier            chs.
                                        completeness                 

  Ch. 8             Ch. 9 Several       Frechet derivative,          NSS or
  Multivariable     Variables           Jacobian, chain rule,        Loomis--Sternberg
                                        inverse/implicit function    
                                        theorems                     
  --------------------------------------------------------------------------------------

> **Part V --- Mastery Checklists with Misconception Catalogue and Lean
> 4 Targets**

For each topic, the checklist defines mastery: every item should be
explainable from memory before moving to the next chapter. Items marked
\[Lean\] are Lean 4 formalization targets. Every checklist includes (1)
a Converse field for each major theorem --- state whether the converse
is true and, if not, the canonical counterexample; (2) an
Example/Non-Example requirement before theorem work begins; and (3) a
Misconception entry --- the single most common named misconception for
that topic, with its precise logical refutation and the counterexample
that breaks it. The misconception entry is grounded in the
Weber--Mejía-Ramos and Hodds--Alcock--Inglis research programmes; each
named error is a documented pattern from empirical studies of
undergraduate proof comprehension.

**Real Numbers & Completeness --- Strichartz Ch. 1 + Rudin Ch. 1**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ State the completeness axiom precisely and explain what fails
> without it.
>
> ☐ Prove the Archimedean property from completeness.
>
> ☐ Prove density of Q in R: between any two reals lies a rational.
>
> ☐ Compute sup and inf for non-trivial sets (e.g., {1/n : n ∈ N}).
>
> ☐ Explain why the Dedekind cut construction works.
>
> ☐ Prove Cantor\'s diagonal argument --- uncountability of R.
>
> ☐ State and prove the nested intervals theorem.

**Converse checks:**

> ☐ Completeness axiom: the converse (every non-empty bounded set has a
> sup) is true by definition --- the axiom is biconditional.
>
> ☐ Archimedean property: is the converse (if N is unbounded then R is
> Archimedean) meaningful? Discuss.
>
> ☐ Nested intervals theorem: fails in Q. State the exact failure
> mechanism.

+-----------------------------------------------------------------------+
| **Misconception --- The completeness axiom says every sequence        |
| converges.**                                                          |
|                                                                       |
| The misconception occurs when students apply completeness: they treat |
| it as a universal convergence guarantee rather than a conditional     |
| one. The precise logical error is the omission of the boundedness     |
| hypothesis --- completeness asserts that every non-empty set that is  |
| bounded above has a supremum; it says nothing about unbounded sets,   |
| and nothing directly about sequences.                                 |
|                                                                       |
| The sequence aₙ = n is non-empty and real-valued; it does not         |
| converge. The sequence aₙ = (−1)ⁿ is bounded; it does not converge.   |
| Completeness does not imply convergence. What it implies, via the     |
| monotone convergence theorem, is that every bounded monotone sequence |
| converges --- a result requiring both boundedness AND monotonicity,   |
| neither of which completeness alone supplies.                         |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize the Archimedean property using Mathlib.

-   \[Lean\] Prove density of Q in R in a Lean theorem statement.

Key Rudin exercises: 1, 2, 3, 5, 6, 8

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Basic Topology --- Rudin Ch. 2 + Munkres Supplement**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ Define a metric space and give three non-trivial examples.
>
> ☐ State the open cover definition of compactness precisely.
>
> ☐ Prove Heine-Borel: closed and bounded if and only if compact in Rⁿ.
>
> ☐ Explain why Heine-Borel fails in infinite-dimensional spaces.
>
> ☐ Prove every compact metric space is sequentially compact.
>
> ☐ Prove Bolzano-Weierstrass from compactness.
>
> ☐ Define connectedness and prove R is connected.
>
> ☐ Describe the Cantor set and prove it is compact, perfect, and
> uncountable.

**Converse checks:**

> ☐ Heine-Borel converse: compact implies closed and bounded in Rⁿ.
> True. Verify.
>
> ☐ Sequential compactness and compactness: equivalent in metric spaces;
> not in general. State where equivalence breaks.
>
> ☐ Connectedness: the converse of \"continuous image of connected set
> is connected\" --- is the pre-image connected? Construct
> counterexample.

+-----------------------------------------------------------------------+
| **Misconception --- A set is compact if and only if it is closed and  |
| bounded.**                                                            |
|                                                                       |
| The misconception occurs when students apply Heine-Borel outside its  |
| domain: the theorem holds in Rⁿ with the standard metric, but         |
| students routinely apply it as a definition valid in all metric       |
| spaces. The precise logical error is treating a theorem as a          |
| definition.                                                           |
|                                                                       |
| In the metric space C(\[0,1\]) of continuous functions with the       |
| sup-norm, the closed unit ball {f : ‖f‖∞ ≤ 1} is closed and bounded   |
| but not compact --- the sequence fₙ(x) = xⁿ is bounded, has no        |
| uniformly convergent subsequence (the only candidate limit is         |
| discontinuous), and the open cover argument fails. Compactness is     |
| defined by the open cover property; closed-and-bounded is a theorem   |
| whose proof uses specific properties of Rⁿ and fails in general       |
| metric spaces.                                                        |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize Heine-Borel --- Mathlib has supporting machinery.

-   \[Lean\] Prove sequential compactness of \[0,1\].

Key Rudin exercises: 2, 3, 4, 9, 11, 12, 16, 19, 22, 25

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Sequences, Limits & Series --- Strichartz Ch. 2--3 + Rudin Ch. 3**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ Write a complete epsilon-N proof for a non-trivial sequence limit.
>
> ☐ Prove that every Cauchy sequence in R converges.
>
> ☐ Prove the monotone convergence theorem.
>
> ☐ Construct a sequence with a prescribed set of subsequential limits.
>
> ☐ Compute limsup and liminf from the definition.
>
> ☐ Prove: limsup aₙ = inf{sup{aₖ : k ≥ n} : n ∈ N}.
>
> ☐ Apply the comparison, ratio, and root tests correctly.
>
> ☐ Explain why the harmonic series diverges and sum 1/n² converges.
>
> ☐ State the rearrangement theorem and explain what it says about
> conditional convergence.

**Converse checks:**

> ☐ Cauchy converse: in R, every convergent sequence is Cauchy. True.
> Prove it.
>
> ☐ Monotone convergence: what breaks if the sequence is not bounded?
> Construct a monotone unbounded sequence.
>
> ☐ Rearrangement theorem: does it apply to absolutely convergent
> series? State the positive result.

+-----------------------------------------------------------------------+
| **Misconception --- If the terms of a sequence get closer together,   |
| the sequence converges.**                                             |
|                                                                       |
| The misconception occurs at the step where a student concludes from   |
| \|aₙ₊₁ − aₙ\| → 0 that the sequence is Cauchy, and therefore          |
| convergent. The precise logical error is the confusion between        |
| consecutive-term closeness and the Cauchy condition. The Cauchy       |
| condition requires \|aₘ − aₙ\| \< ε for ALL m, n ≥ N simultaneously   |
| --- not just for adjacent terms.                                      |
|                                                                       |
| The harmonic series partial sums provide the counterexample: sₙ = 1 + |
| 1/2 + ... + 1/n satisfies \|sₙ₊₁ − sₙ\| = 1/(n+1) → 0, so consecutive |
| terms become arbitrarily close, yet sₙ → ∞. The sequence diverges     |
| despite adjacent terms converging to the same value.                  |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize the Cauchy criterion for series convergence.

-   \[Lean\] Prove monotone convergence theorem in Lean.

Key Rudin exercises: 3, 5, 6, 7, 11, 14, 16, 20, 21, 23

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Continuity --- Strichartz Ch. 4 + Rudin Ch. 4**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ Write a complete epsilon-delta proof for a non-trivial continuous
> function.
>
> ☐ Distinguish continuity from uniform continuity --- state both
> precisely.
>
> ☐ Prove that your delta in a uniform continuity proof does not depend
> on x.
>
> ☐ Prove Heine-Cantor: continuous on compact implies uniformly
> continuous.
>
> ☐ Prove IVT as a consequence of connectedness.
>
> ☐ Prove EVT: continuous on compact implies achieves max and min.
>
> ☐ Prove continuous image of compact set is compact.
>
> ☐ Exhibit a function continuous everywhere but differentiable nowhere
> (cite).

**Converse checks:**

> ☐ Heine-Cantor converse: uniformly continuous on compact implies
> continuous. True (trivially). What about the converse on non-compact
> sets? Construct f continuous but not uniformly continuous on (0,1\].
>
> ☐ IVT converse: if f takes all values between f(a) and f(b), is f
> continuous? No --- construct counterexample (Darboux function).

+-----------------------------------------------------------------------+
| **Misconception --- A function is continuous if you can draw its      |
| graph without lifting your pencil.**                                  |
|                                                                       |
| The misconception occurs at the point of formalisation: the           |
| pencil-lifting image encodes a property of graphs on bounded closed   |
| intervals drawn left to right --- not a property of arbitrary         |
| functions on arbitrary domains. The precise logical error is that the |
| image smuggles in connectedness of the domain, finite range, and      |
| left-to-right traversal, none of which appear in the epsilon-delta    |
| definition.                                                           |
|                                                                       |
| The function f : Q → R defined by f(x) = 0 if x² \< 2 and f(x) = 1 if |
| x² \> 2 is continuous on Q (the domain is disconnected; there is no   |
| path along which to \"lift a pencil\") yet satisfies the              |
| epsilon-delta definition at every point of Q. More directly: the      |
| topologist\'s sine curve sin(1/x) fails the pencil-lifting test near  |
| 0 precisely because it is discontinuous there --- the image works for |
| that case but for the wrong reason, and fails to distinguish          |
| continuity from path-connectedness of the graph.                      |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize Heine-Cantor (uniform continuity on compact
    sets).

-   \[Lean\] Prove IVT using Mathlib\'s connectedness machinery.

Key Rudin exercises: 1, 2, 3, 4, 6, 8, 14, 15, 16, 19, 20

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Differentiation --- Strichartz Ch. 5 + Rudin Ch. 5**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ State and prove the Mean Value Theorem from Rolle\'s theorem.
>
> ☐ Prove Rolle\'s theorem from EVT.
>
> ☐ State Taylor\'s theorem with the correct remainder form.
>
> ☐ Explain the derivative as a linear approximation --- what the error
> term says.
>
> ☐ Prove that differentiability implies continuity (but not vice
> versa).
>
> ☐ Use MVT to prove: monotone derivative implies convex function.
>
> ☐ Prove L\'Hôpital\'s rule from the generalized MVT.
>
> ☐ Exhibit a function differentiable everywhere with discontinuous
> derivative.

**Converse checks:**

> ☐ MVT converse: if f\'(c) = 0 for some c ∈ (a,b), does f(a) = f(b)?
> No. Construct counterexample.
>
> ☐ Differentiability implies continuity: the converse is false.
> Construct f continuous everywhere, differentiable nowhere.
>
> ☐ Rolle\'s theorem: what breaks if f is not continuous on \[a,b\]? If
> not differentiable on (a,b)?

+-----------------------------------------------------------------------+
| **Misconception --- Uniform continuity is just continuity with the    |
| same delta used everywhere, so any continuous function on a closed    |
| interval is automatically uniformly continuous for a fixed delta.**   |
|                                                                       |
| The misconception occurs at the hypothesis-verification step of       |
| Heine-Cantor: students treat the conclusion (uniform continuity on a  |
| compact set) as a tautology following from continuity alone, without  |
| recognising that compactness is doing essential work. The precise     |
| logical error is the claim that a single delta can be read off the    |
| continuity condition without further argument.                        |
|                                                                       |
| Continuity at each point x gives a delta(x) depending on x;           |
| extracting a uniform delta requires compactness to reduce the open    |
| cover {B(x, delta(x)/2)} to a finite subcover and take the minimum.   |
| The function f(x) = 1/x on (0,1\] is continuous at every point with a |
| valid delta at each point, yet no single delta works for all x        |
| simultaneously: given any δ \> 0, take x = δ/2 and the argument       |
| collapses. Uniform continuity requires compactness; continuity alone  |
| does not suffice.                                                     |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize the Mean Value Theorem --- Mathlib has it;
    compare to your proof.

Key Rudin exercises: 1, 2, 3, 4, 6, 14, 15, 26, 27

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Riemann-Stieltjes Integration --- Strichartz Ch. 6 + Rudin Ch. 6**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ Define upper and lower Riemann sums and the Riemann integral
> precisely.
>
> ☐ State the Riemann condition and prove continuous implies integrable.
>
> ☐ Explain what the Stieltjes generalization adds over Riemann.
>
> ☐ Prove the Fundamental Theorem of Calculus in both directions.
>
> ☐ State the class of Riemann-integrable functions precisely.
>
> ☐ Explain what \"measure-zero set of discontinuities\" means
> informally.
>
> ☐ Prove integration by parts for the Stieltjes integral.

**Converse checks:**

> ☐ FTC Part I converse: if F\' = f everywhere, does F = integral of f?
> What additional hypotheses are needed?
>
> ☐ Integrability: construct a bounded function that is not
> Riemann-integrable (Dirichlet function). What is its set of
> discontinuities?

+-----------------------------------------------------------------------+
| **Misconception --- If the terms of a series go to zero, the series   |
| converges.**                                                          |
|                                                                       |
| The misconception occurs at the necessary-condition step: the term    |
| test (divergence test) establishes that aₙ → 0 is necessary for       |
| convergence, and students invert this as sufficient. The precise      |
| logical error is converse confusion --- mistaking a necessary         |
| condition for a sufficient one.                                       |
|                                                                       |
| The harmonic series is the canonical counterexample: 1/n → 0, yet Σ   |
| 1/n diverges, as shown by the comparison 1/(n+1) + ... + 1/(2n) ≥ 1/2 |
| for all n, so partial sums grow without bound. The p-series Σ 1/nᵖ    |
| provides a parametric family: aₙ = 1/nᵖ → 0 for all p \> 0, yet the   |
| series converges if and only if p \> 1. The rate at which terms       |
| approach zero determines convergence --- the limit being zero is not  |
| enough.                                                               |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize FTC Part I using Mathlib.Analysis.Calculus.

Key Rudin exercises: 1, 2, 3, 4, 5, 7, 8, 10, 11, 16

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

**Sequences & Series of Functions --- Strichartz Ch. 7 + Rudin Ch. 7**

How to use: Work through each checklist item actively. Ask Claude to
test you on each item in Socratic mode --- state the definition from
memory, attempt the proof before Claude asks anything, then request gap
analysis only after a genuine attempt. On first reading, move through
strategically. On consolidation, hold firm --- do not advance until
every item is explainable without the book.

> ☐ Define pointwise and uniform convergence --- state both precisely.
>
> ☐ Prove: uniform convergence + continuous functions implies continuous
> limit.
>
> ☐ Prove: uniform convergence preserves Riemann integrability.
>
> ☐ State and prove the Weierstrass M-test.
>
> ☐ State the Arzela-Ascoli theorem and identify what equicontinuity
> buys.
>
> ☐ State the Weierstrass approximation theorem.
>
> ☐ Exhibit a sequence converging pointwise but not uniformly.
>
> ☐ Exhibit a sequence of continuous functions with a discontinuous
> pointwise limit.
>
> ☐ Construct the nowhere-differentiable continuous function (Rudin
> Exercise 24).

**Converse checks:**

> ☐ Uniform limit theorem converse: if the limit of continuous functions
> is continuous, was the convergence uniform? No --- construct
> counterexample on \[0,1\].
>
> ☐ Weierstrass M-test: what breaks if Σ Mₙ diverges but the series
> still converges? Give example.

+-----------------------------------------------------------------------+
| **Misconception --- If fₙ → f pointwise and each fₙ is continuous,    |
| then f is continuous.**                                               |
|                                                                       |
| The misconception occurs at the step where students apply the uniform |
| limit theorem without verifying its hypothesis. The precise logical   |
| error is the omission of uniformity: the theorem requires uniform     |
| convergence, not merely pointwise convergence, and these are not      |
| equivalent.                                                           |
|                                                                       |
| The counterexample is fₙ(x) = xⁿ on \[0,1\]: each fₙ is continuous,   |
| fₙ → f pointwise where f(x) = 0 for x ∈ \[0,1) and f(1) = 1, and f is |
| discontinuous at x = 1. The convergence is not uniform --- for any N, |
| taking x close enough to 1 gives fₙ(x) \> 1/2. The hypothesis of the  |
| uniform limit theorem is doing all the work; pointwise convergence    |
| alone preserves nothing.                                              |
+-----------------------------------------------------------------------+

**Lean 4 targets:**

-   \[Lean\] Formalize the Weierstrass M-test --- important and
    achievable.

-   \[Lean\] Prove uniform limit of continuous functions is continuous.

Key Rudin exercises: 1, 2, 3, 4, 5, 6, 9, 12, 14, 15, 20, 24

  -----------------------------------------------------------------------
  **Example/Non-Example:** Before any theorem work, self-generate one
  object satisfying each new definition and one that fails by violating
  exactly one condition.

  -----------------------------------------------------------------------

> **Part VI --- The Proof-Practice Ladder --- Five Rungs**

The proof-practice ladder organises problems by cognitive demand, not by
difficulty in the conventional sense. A student should be able to
execute Rungs 1--2 fluently before attempting Rung 3, and should not
attempt Rung 5 until Rung 4 is reliable. The ladder applies to every
topic --- work through all five rungs for each chapter before moving on.

  -----------------------------------------------------------------------
  **AI integration:** Use Claude to scaffold your ascent. For Rungs 1--2,
  ask Claude to check your work. For Rungs 3--4, ask Claude to play
  devil\'s advocate and apply the Pólya recovery protocol when you are
  stuck. For Rung 5, ask Claude to try to break your construction before
  you finalise it. Lean 4 is particularly valuable at Rungs 3--4, where
  the compiler catches the subtle gaps that feel correct but are not.

  -----------------------------------------------------------------------

**Rung 1 --- Mechanical**

Direct application of definitions. No creativity required --- follow the
definition mechanically.

-   epsilon-delta proofs for simple functions: lim(x→2) 3x = 6, lim(x→0)
    x² = 0.

-   Basic sup and inf computations for explicitly defined sets.

-   Derivative and integral definitions applied to polynomials.

-   Basic sequence limit proofs: 1/n → 0, (n+1)/n → 1.

-   Simple Cauchy sequence verification.

Claude\'s role: Check your epsilon-delta arithmetic and verify the
quantifier order is correct. Ask: \"Does my delta depend only on
epsilon?\" Apply Bloom Remember and Understand levels.

**Rung 2 --- Structural**

Apply theorems and standard techniques to non-trivial situations.
Requires selecting the right tool.

-   Monotone convergence theorem --- prove a specific monotone sequence
    converges.

-   Alternating series test --- proof and application.

-   Uniform continuity on compact sets --- verify for a specific
    function.

-   Integration by parts via FTC.

-   Weierstrass M-test --- apply to a specific series of functions.

-   Ratio and root test proofs.

Claude\'s role: After your attempt, ask: \"Which theorem did I use and
have I verified all its hypotheses?\" Then ask for a case where one
hypothesis fails and the conclusion breaks. Apply Bloom Apply level.

**Rung 3 --- Conceptual**

Understand the logical architecture --- why theorems are true, what each
hypothesis buys, how results connect.

-   limsup/liminf arguments --- prove the characterization theorem.

-   Rearrangement phenomena --- why rearranging a conditionally
    convergent series can produce any sum.

-   FTC proofs in both directions --- understand the asymmetry.

-   Uniform vs pointwise convergence --- prove a result holds for one
    but not the other.

-   Compactness machinery --- trace a proof and identify the exact
    moment compactness is invoked.

Claude\'s role: After each proof, ask Claude to map the dependencies:
\"What earlier results does this proof invoke and what breaks if I
remove each one?\" Apply Bloom Analyze level. Begin Converse checks.

**Rung 4 --- Rudin-Style**

Compressed, elegant proofs at the level Rudin presents. No unnecessary
steps --- the minimum correct argument.

-   Compactness arguments --- Heine-Borel, Arzela-Ascoli.

-   Connectedness proofs --- IVT, continuous image of connected set.

-   Uniform convergence theorems with full rigour.

-   Taylor\'s theorem with remainder in its strongest form.

-   Rudin Chapter 7 Exercises 9, 15, 20 --- each requires substantial
    independent proof construction.

Claude\'s role: Submit your proof and ask: \"Is there a shorter correct
argument? Is every step necessary?\" Apply Bloom Evaluate level. Check
the same proof in Lean 4 --- the compiler will find remaining gaps.

**Rung 5 --- Creative**

Construct objects with prescribed properties. Requires genuine
mathematical invention --- no template exists.

-   Construct a sequence with a prescribed set of subsequential limits.

-   Build a function continuous on Q, discontinuous on R \\ Q (or vice
    versa).

-   Construct a conditionally convergent series that rearranges to +∞.

-   Build a continuous function on \[0,1\] not uniformly continuous on
    (0,1) --- explain the exact failure mechanism.

-   Exhibit a series of continuous functions converging pointwise to a
    discontinuous limit.

-   Construct the nowhere-differentiable continuous function explicitly
    (Rudin Exercise 7.24).

-   Build a counterexample to a theorem when one hypothesis is removed.

Claude\'s role: Before finalising any construction, ask: \"Try to break
this. Does my construction actually have the property I claim? Is there
an edge case I missed?\" Apply Bloom Create level. Verify in Lean 4 if
possible.

> **Part VII --- The Combined Reading Workflow**

This workflow integrates Strichartz, Rudin, Alcock, the mastery
checklists, and the proof ladder into a coherent chapter-by-chapter
cycle. Key principle: on first reading (Strichartz pass), read
strategically and move through. On consolidation (end of week), hold
firm --- do not advance until every checklist item is explainable
without the book.

**Step 0 --- Network Positioning**

Before opening any text: ask \"Where does this topic sit in the logical
structure of Analysis so far? What depends on what we are about to
learn?\" You cannot fully answer this yet --- it is a priming question.
At the end of the week, ask it again: \"Can you now answer the question
you could not answer on Day 1?\"

**Step 1 --- Read Alcock (First)**

If the corresponding Alcock chapter exists for this topic, read it
first. Alcock identifies the specific difficulty zones and explicitly
names the informal images that will mislead you --- including the
misconceptions now catalogued in Part V. Particularly important for:
sequences (list vs function confusion), continuity (pencil-lifting
image), series (terms vs partial sums confusion).

**Step 2 --- Read Strichartz (First Pass)**

Build intuition, geometric understanding, and motivating examples.
Before reading, ask Claude to prime your intuitions. Read actively ---
take notes on the WHY at every step. If bogged down anywhere: put a
marker and move forward.

**Step 3 --- Attempt the Mastery Checklist (Strichartz Pass)**

After Strichartz, work through the checklist for the topic. Include the
Example/Non-Example requirement. Read the Misconception entry for this
topic and write a one-sentence refutation in your own words before
attempting any proof --- surface and explicitly refute the named
misconception before the formal work begins.

**Step 4 --- Read Rudin (Immediately After Strichartz)**

Open Rudin on the same topic while the Strichartz motivation is fresh.
Attempt each theorem before reading Rudin\'s proof. Supply every
implicit step on scratch paper. Apply self-explanation to each line. For
each theorem, immediately ask: is the converse true? Is there a named
misconception in the Part V checklist that applies here?

**Step 5 --- Climb Rungs 1--4 of the Proof Ladder**

Work through the proof ladder for this topic systematically. Rungs 1--2
should flow from the Strichartz + Rudin reading. Rungs 3--4 require
independent construction and are where most students need to slow down
significantly.

**Step 6 --- Rung 5 --- Creative Problems**

After Rung 4 is reliable, attempt one or two Rung 5 constructions. Ask
Claude to try to break your construction. Return to these problems
monthly as the subject develops.

**Step 7 --- Update Theorem Ledger & Error Log**

Record major results in your Theorem Ledger using the revised Version
2.1 format (see Part IX), including the Misconception field. Record any
proof errors in your Error Log with category. After several chapters,
ask Claude to analyze your error patterns.

> **Part VIII --- The Master Reading Plan --- All Phases**

The plan assumes 10--15 hours of serious work per week. Times are
guides, not deadlines. Completing Chapters 1--8 with full engagement on
exercises should budget one full academic year. Students who \"finish\"
Rudin in a semester have almost always skipped exercises or not fully
worked through the proofs.

  --------------------------------------------------------------------------------------
  **Phase**   **Topic**           **Time**   **Texts**            **Key Notes**
  ----------- ------------------- ---------- -------------------- ----------------------
  Prelim      Proof Foundations   2--6 wks   Solow → Hammack →    Forward-Backward
                                             Eccles (see Part II) method, named
                                                                  techniques, quantifier
                                                                  precision, cardinality
                                                                  bridge. Also read
                                                                  Alcock Part 1 (\~50
                                                                  pages) before or
                                                                  during this phase.

  Phase 1     Real Numbers        3--4 wks   Alcock Ch. 10 →      Completeness, sup/inf,
                                             Strichartz Ch. 1 →   Archimedean property,
                                             Rudin Ch. 1 +        Dedekind construction,
                                             Appendix             countability. Read Ch.
                                                                  1 twice.

  Phase 2     Basic Topology      4--6 wks   Strichartz (topology Metric spaces, open
                                             integrated) +        cover compactness,
                                             Munkres Ch. 2 →      Heine-Borel,
                                             Rudin Ch. 2          Bolzano-Weierstrass,
                                                                  Cantor set. Read Rudin
                                                                  Ch. 2 twice. Budget 6
                                                                  weeks, not 4. Munkres
                                                                  is non-optional for
                                                                  most students.

  Phase 3     Sequences & Series  4--5 wks   Alcock Ch. 5--6 →    Cauchy implies
                                             Strichartz Ch. 2--3  convergent,
                                             → Rudin Ch. 3        limsup/liminf,
                                                                  absolute vs
                                                                  conditional
                                                                  convergence,
                                                                  rearrangement.
                                                                  Quantifier
                                                                  interrogation is
                                                                  critical here.

  Phase 4     Continuity          3--4 wks   Alcock Ch. 7 →       epsilon-delta
                                             Strichartz Ch. 4 →   continuity, uniform
                                             Rudin Ch. 4          continuity,
                                                                  Heine-Cantor, IVT,
                                                                  EVT. Read Alcock Ch. 7
                                                                  first --- it
                                                                  explicitly refutes the
                                                                  pencil-lifting image.
                                                                  The delta-depends-on-x
                                                                  error is the most
                                                                  common mistake here.

  Phase 5     Differentiation     2--3 wks   Alcock Ch. 8 →       MVT, Rolle, Taylor,
                                             Strichartz Ch. 5 →   L\'Hôpital. One of
                                             Rudin Ch. 5          Rudin\'s most elegant
                                                                  chapters. Ex. 26
                                                                  (differentiable
                                                                  everywhere, derivative
                                                                  discontinuous) is a
                                                                  must.

  Phase 6     Riemann-Stieltjes   4--5 wks   Alcock Ch. 9 →       Upper/lower sums,
                                             Strichartz Ch. 6 →   Riemann condition, FTC
                                             Rudin Ch. 6          I and II, integration
                                                                  by parts. The
                                                                  Stieltjes
                                                                  generalization
                                                                  surprises most
                                                                  students. Read
                                                                  Strichartz carefully
                                                                  before Rudin here.

  Phase 7     Sequences & Series  4--5 wks   Strichartz Ch. 7 (+  Pointwise vs uniform,
              of Functions                   Fourier) → Rudin Ch. M-test, Arzela-Ascoli,
                                             7                    Weierstrass
                                                                  approximation.
                                                                  Exercise 24 (nowhere
                                                                  differentiable) is one
                                                                  of the most celebrated
                                                                  in the book.

  Phase 8     Power Series &      2--3 wks   Strichartz Fourier   Power series,
              Special Functions              chs. + Rudin Ch. 8   exp/log/trig, gamma
                                             (read together)      function, Fourier
                                                                  series completeness.
                                                                  Completing Phases 1--8
                                                                  is a major
                                                                  achievement.

  Phase 9     Multivariable       6--8 wks   Spivak → NSS or      Frechet derivative,
              (Advanced)                     Loomis--Sternberg    inverse/implicit
                                             (Rudin Ch. 9 for     function theorems,
                                             reference only)      differential forms,
                                                                  Stokes. Requires
                                                                  proof-based linear
                                                                  algebra first.
  --------------------------------------------------------------------------------------

> **Part IX --- The AI-Assisted Tutoring Framework**

Claude functions as a Socratic tutor --- questioning, probing, and
diagnosing rather than lecturing. The critical reframe: Claude is not
the authority in Real Analysis. Rudin and the mathematical community
are. Claude can make mistakes, particularly subtle ones that look right.
The combination of Claude for reasoning and Lean 4 as the infallible
formal authority is the right architecture precisely because it does not
trust Claude alone. Version 2.1 integrates three pedagogical frameworks
(Solow, Pólya, Bloom), Alcock\'s research-based guidance, and the
seven-topic Misconception Catalogue throughout.

**The Standing System Prompt (Version 2.1)**

+-----------------------------------------------------------------------+
| **Open every serious tutoring session with:**                         |
|                                                                       |
| \"You are my Real Analysis tutor working through Baby Rudin, Chapter  |
| \[X\]. Style: ask me questions before explaining anything; never give |
| a complete proof unless I have attempted it first; when I give you a  |
| proof, find the weakest step and ask me to justify it rather than     |
| rewriting; flag every \'clearly\' and \'obviously\'; tell me honestly |
| whether my proof is wrong, incomplete, or correct but inelegant. For  |
| every new definition, ask me to construct one example satisfying it   |
| and one failing by violating exactly one condition before we discuss  |
| any theorem. For every theorem, ask me whether the converse is true   |
| and, if not, for the canonical counterexample. Probe the named        |
| misconception in the Theorem Ledger for this theorem before the       |
| session ends --- present the misconception as a plausible student     |
| argument and ask me to identify precisely what is wrong with it, not  |
| just that something is wrong. When I am stuck, do not give the next   |
| step --- instead ask: (1) what happens in the simplest non-trivial    |
| case; (2) what I would need to already have to make the argument      |
| work; (3) whether I have proved anything with a similar logical form. |
| For every proof we complete, ask me: is there a shorter correct       |
| argument, and what breaks if each hypothesis is removed? When I am    |
| stuck, apply the Complete Stuck-State Management System (D-L-M-K +    |
| Pólya, then Framework Reframes if needed) rather than repeating the   |
| same approach.\"                                                      |
+-----------------------------------------------------------------------+

**The Four-Part Consolidation Assessment**

The previous single-prompt consolidation (\"Test me. Ask me to state
\[definition\] from memory, then prove \[theorem\] without notes.\") is
one-dimensional --- it reaches Bloom Apply and occasionally Evaluate,
but misses the conceptual and misconception dimensions. Replace it with
this four-part structure, applied at the end of every topic session.

+-----------------------------------------------------------------------+
| **(1) Applied problem**                                               |
|                                                                       |
| A specific epsilon-delta or construction problem on a non-trivial     |
| function or set. Targets Bloom Apply --- verifies that the student    |
| can execute the technique, not merely state it. Example: \"Prove from |
| the definition that f(x) = x sin(1/x) extended by f(0) = 0 is         |
| continuous at 0.\" This must be a problem requiring genuine work, not |
| a template application.                                               |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(2) Conceptual question**                                           |
|                                                                       |
| Target the quantifier structure or the logical form of the            |
| conclusion; ask why the theorem is formulated as it is. Targets Bloom |
| Analyze. Example: \"The definition of uniform continuity has delta    |
| appearing before x in the quantifier order. Explain in precise        |
| logical terms what changes if we swap the quantifier order. Write     |
| both statements with all quantifiers explicit and describe the set of |
| functions satisfying each.\" This forces engagement with logical      |
| architecture, not surface recall.                                     |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(3) Derivation step**                                               |
|                                                                       |
| Reproduce a key lemma from logical structure, not from memorised      |
| proof sequence. Targets Bloom Evaluate. Example: \"Without looking at |
| your notes, derive the inequality used in the Weierstrass M-test      |
| proof. Start only from the triangle inequality and the definition of  |
| uniform convergence. Identify the exact line where the boundedness    |
| hypothesis enters.\" The student must reconstruct, not recite.        |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **(4) Misconception check**                                           |
|                                                                       |
| Present the named misconception from the Ledger as a plausible but    |
| wrong student argument. Ask for precise refutation --- the specific   |
| logical step that is invalid --- not just identification that         |
| something is wrong. Targets Bloom Analyze and Evaluate                |
| simultaneously. Example: \"A student argues: I know fₙ → f pointwise  |
| and each fₙ is continuous, so f must be continuous --- after all, the |
| limit of continuous functions is continuous. Where precisely does     |
| this argument fail? Identify the specific logical step that is        |
| invalid, give the counterexample, and state exactly what additional   |
| hypothesis would make the argument valid.\" The misconception check   |
| does the most new work of the four parts: it forces engagement with   |
| the logical step the misconception corrupts, not just recognition     |
| that something is wrong.                                              |
+-----------------------------------------------------------------------+

**The Complete Stuck-State Management System**

Apply levels in strict order. Never skip a level. Escalate only when the
current level is genuinely exhausted.

  --------------------------------------------------------------------------
  **Level**   **Tool**                 **Trigger**          **Research
                                                            Basis**
  ----------- ------------------------ -------------------- ----------------
  Level 1     Solow Forward-Backward   Always --- the       Solow (2014)
              method                   primary tool for     
                                       every proof attempt  

  Level 2     Revised Recovery         When Level 1 stalls  Mason et al.;
              Protocol (D-L-M-K +                           Sweller;
              Pólya)                                        Schoenfeld;
                                                            Lakatos; Pólya

  Level 3     Framework Reframe        When Level 2 fails   Velleman;
              (Velleman / Eccles /     twice                Eccles; Hammack
              Hammack)                                      

  Level 4     Direct conceptual        Only after all three Responsive
              intervention             levels fail          tutoring
                                                            research
  --------------------------------------------------------------------------

**The Revised Theorem Ledger (Version 2.1)**

One entry per major result. The Misconception field is new in Version
2.1 --- it sits alongside the existing Converse, Analogues, and Proof
Structure fields. One entry per major result: the named misconception
for that theorem and its precise refutation. This means Claude can probe
the known misconception preemptively during Socratic sessions, rather
than waiting for it to surface.

  -----------------------------------------------------------------------
  **Field**           **What to Record**
  ------------------- ---------------------------------------------------
  Statement           In your own words --- no copying from Rudin.

  Key proof idea      One sentence: the essential move the proof turns
                      on.

  Load-bearing        Which hypothesis is essential? Counterexample when
  hypothesis          it is removed.

  Converse            Is the converse true? If false, the canonical
                      counterexample. If true, is it a named result?

  Misconception (NEW  The named misconception for this theorem and its
  2.1)                precise refutation --- the specific logical step
                      that is invalid and the counterexample that breaks
                      it. Drawn from the Part V catalogue for this topic.

  Dependencies        Which earlier results does this proof invoke?

  Downstream          Which later results depend on this theorem?

  Analogues           Which earlier theorem has the same logical form or
                      a similar proof strategy?

  Lean 4 status       Formalized / in progress / planned.

  Proof Structure     The logical form of the conclusion in
                      framework-neutral terms, e.g.: \"Universal (for all
                      epsilon) then Existence (there exists delta
                      independent of x) --- Choose Method on epsilon,
                      Construction Method for delta using compactness
                      argument.\"

  Bloom level         \[ \] Apply \[ \] Analyze \[ \] Evaluate \[ \]
  achieved            Create
  -----------------------------------------------------------------------

**Alcock\'s Self-Explanation Protocol (As a Named Habit)**

The Hodds--Alcock--Inglis research (2014) demonstrated that
self-explanation training improves proof comprehension with an effect
size of d = 0.95 --- an unusually large effect --- and that the gains
persist after a single training session. The key finding is that
students must develop this as an independent habit, not only when
prompted by a tutor.

  -----------------------------------------------------------------------
  **The Self-Explanation Protocol (to internalize and apply
  independently):** Before proceeding to the next line of any proof, ask
  yourself: (1) Do I understand the ideas used in this line? (2) Do I
  understand WHY those ideas have been used? (3) Can I explain this line
  in terms of earlier ideas in this proof, earlier theorems, or my own
  prior knowledge? (4) If this line contradicts something I believed,
  what needs updating? A concrete marker of progress: by Phase 3, you
  should be self-explaining without waiting for Claude to ask. By Phase
  5, the protocol should be automatic on every proof you read.

  -----------------------------------------------------------------------

**The Six-Stage Tutoring Loop**

  ------------------------------------------------------------------------
  **Stage**        **Description**
  ---------------- -------------------------------------------------------
  Stage 1 ---      Before opening any text: \"I am about to study
  Concept Priming  \[theorem\]. Ask me questions to surface what I already
                   know and what my intuitions are.\" Include the Alcock
                   question: \"What is my informal image of this concept?
                   Let us find the example that breaks that image.\"

  Stage 2 ---      Attempt the proof yourself 20--30 minutes before
  Active Reading   reading Rudin. Apply the self-explanation protocol to
                   each line. If stuck: \"I am stuck here: \[describe\].
                   Apply the Pólya recovery protocol.\"

  Stage 3 ---      Submit your proof with: \"Do not rewrite it. Go line by
  Proof Checking   line: (1) is the justification complete? (2) does this
                   step follow from what precedes it? (3) are all
                   hypotheses of any cited theorem satisfied? (4) does my
                   delta depend only on epsilon?\" The do-not-rewrite
                   instruction is essential.

  Stage 4 ---      Translate to Lean 4 tactics, run the compiler, paste
  Formal           errors back. The compiler provides ground truth Claude
  Verification     cannot. A proof that compiles is correct.

  Stage 5 ---      Fresh session: \"Try to break my proof. Construct a
  Counterexample & case where my argument fails if one hypothesis is
  Converse Check   removed.\" Then: \"Is the converse of this theorem
                   true? If not, what is the canonical counterexample?\"

  Stage 6 ---      Apply the four-part assessment (Applied problem →
  Four-Part        Conceptual question → Derivation step → Misconception
  Consolidation    check). Then update the Theorem Ledger V2.1 with all
  Assessment       fields including Misconception. Then the Pólya Look
                   Back: \"Could you have approached this differently?
                   What was the key insight? Does this argument
                   generalize?\"
  ------------------------------------------------------------------------

**Targeted Prompts for Real Analysis**

  -----------------------------------------------------------------------
  **Prompt Name**     **Prompt Text**
  ------------------- ---------------------------------------------------
  Quantifier checking Write the statement with all quantifiers explicit.
                      Is this what I mean? What does it say if I swap the
                      first universal and existential quantifier?

  Delta-x diagnostic  Does my delta depend on x or only on epsilon?
                      Trace: if \|x-a\| \< delta, does my argument
                      deliver \|f(x)-L\| \< epsilon?

  Hypothesis audit    Have I verified every hypothesis? Which is
                      load-bearing? Give me a counterexample for each one
                      removed.

  Converse check      Is the converse of this theorem true? If not, what
                      is the canonical counterexample? If yes, is it a
                      known named result?

  Misconception check Present the named misconception from the Ledger for
  (NEW 2.1)           this theorem as a plausible student argument. Ask
                      me to identify the specific logical step that is
                      invalid --- not just that something is wrong ---
                      and to give the canonical counterexample.

  Compactness         Have I verified the set is actually compact? Which
  interrogation       property of compact sets am I using and why does
                      the proof fail without it?

  Knowledge graph     What does this theorem depend on? What later
                      results depend on it? What breaks in analysis if we
                      do not have this result?

  Adversarial         Give me the most dangerous sequence/function
  sequence            satisfying my hypotheses but that my proof would
                      struggle with.

  Informal image      What is my informal image of this concept? Let us
  audit               find an example that matches my image but fails the
                      formal definition.
  -----------------------------------------------------------------------

**Error Log**

Record every proof error with its category. After several chapters, ask
Claude: \"What patterns do you see? What is the single most important
thing for me to watch for?\"

  ---------------------------------------------------------------------------
  **Category**         **Description**              **Example**
  -------------------- ---------------------------- -------------------------
  Quantifier error     Wrong order of quantifiers;  Writing delta before
                       swapping for-all and         epsilon in a uniform
                       there-exists                 continuity proof

  Missing hypothesis   Applying a theorem without   Using MVT without
                       verifying all its conditions checking
                                                    differentiability on open
                                                    interval

  Invalid inference    A step that does not follow  Concluding f is uniformly
                       logically from what precedes continuous from
                       it                           continuity alone on (0,1)

  Wrong theorem        Citing a theorem whose       Using pointwise
  applied              conclusion does not match    convergence theorem when
                       what is needed               uniform is required

  Delta-depends-on-x   Choosing delta that depends  delta = epsilon /
                       on the point x in a uniform  (2\|x\| + 1) in a uniform
                       continuity proof             continuity argument on R

  Converse confusion   Assuming the converse of a   Concluding convergence
                       conditional theorem          from terms going to zero
                                                    (harmonic series)
  ---------------------------------------------------------------------------

> **Part X --- Research Literature: What the Evidence Shows**

A genuine and growing body of research exists in undergraduate
mathematics education (UME) with several researchers whose work is
directly actionable for this guide. The seven-topic Misconception
Catalogue embedded in Part V is grounded in the Weber--Mejía-Ramos and
Hodds--Alcock--Inglis research programmes described below --- each named
misconception corresponds to a documented student error pattern from
those empirical programmes.

**A. The Weber--Mejía-Ramos Research Programme (Rutgers)**

Keith Weber and Juan Pablo Mejía-Ramos have spent roughly fifteen years
studying proof comprehension in undergraduate mathematics, with much of
the work situated in Real Analysis. Their foundational finding:
mathematics majors learn little from the proofs they read in their
advanced courses because students and their teachers have different
perceptions about what students\' responsibilities are when reading a
mathematical proof. Students think they are done when they can follow
each line. Mathematicians think comprehension means something far
richer.

Their multi-component proof comprehension model includes: verifying
logical validity line by line; identifying the modular structure of the
argument; recognising the key idea or insight; understanding how the
proof fits into the broader mathematical context; and being able to
apply or transfer the proof strategy to a new problem. This maps
directly onto the Theorem Ledger and mastery checklists in this guide.

**B. Hodds, Alcock & Inglis --- Self-Explanation Training (2014)**

This is arguably the single most important empirical finding for
tutoring Real Analysis. Published in the Journal for Research in
Mathematics Education (Vol. 45, 2014), the study ran three experiments
demonstrating that self-explanation training significantly improved
proof comprehension. Effect size d = 0.95 --- an unusually large effect
for an educational intervention. Eye-tracking evidence that trained
students spent more time on each line and more time on between-line
transitions. Persistence: the effect persisted over several weeks after
only a single training session.

The critical implication: this is a trainable habit, not an innate
ability. The guide enacts self-explanation conversationally through
Claude\'s line-by-line questioning, but the research shows the gains
come from students doing it independently. This is why Part IX presents
the self-explanation protocol as a named habit to internalize.

**C. Inquiry-Based Learning and the Moore Method**

A substantial research literature exists on Inquiry-Based Learning (IBL)
in undergraduate mathematics. The Laursen et al. large-scale study (four
research universities) found that the impact of IBL on previously
low-achieving students\' grades is sizable and persistent. For strong
students, the Moore Method research found benefits in: confidence,
independence in proving theorems, mathematical identity, and willingness
to try and fail and recognise its value.

This guide\'s overall philosophy is deeply IBL in spirit --- the
prohibition on Claude giving complete proofs, the requirement that
students attempt theorems before reading Rudin, the emphasis on
productive struggle. What the IBL research adds is evidence that the
social dimension matters. A Claude tutor can approximate the questioning
function of a Moore Method course, but cannot replicate peer
accountability. This is a genuine limitation of AI-assisted solo study.

**D. Responsive Tutoring Research**

Research on undergraduate peer mathematics tutoring identifies
responsive teaching practices as central: tutors should ask probing and
scaffolding questions, listen to understand what the student is
thinking, and then respond in a way that uses student thinking rather
than replacing it.

The known failure mode: analysis of tutor talk turns found that tutors
engaged in higher cognitive demand work more often than students --- the
tutor performs the planning phase rather than pushing the student to do
it. This is a known failure mode for AI tutors as well. The guide\'s
instruction \"do not rewrite my proof\" and \"ask me the next question
rather than giving the answer\" are direct countermeasures, grounded in
this research.

**E. Alcock\'s Six Key Findings**

Alcock\'s How to Think About Analysis (Oxford, 2014) synthesizes the
research tradition into student-facing guidance. Six key findings from
this work have been integrated throughout this guide.

**Finding 1: The Two Meanings of \"Example\"**

When students say \"we want more examples\" they mean worked examples
(procedural). When textbooks provide \"examples\" they mean instances of
objects satisfying a definition. Advanced mathematics requires the
latter. This is why every definition in the Version 2 checklists
requires self-generated examples before any theorem work begins.

**Finding 2: Self-Explanation as a Trainable Habit**

See Section B above. Students must practice self-explanation
independently, not only when prompted. The self-explanation protocol in
Part IX is the curriculum-facing implementation.

**Finding 3: Analysis as a Network, Not a List**

Students are disoriented by encountering Analysis as a finished
deductive system. Alcock recommends making the network structure itself
a cognitive object worth attending to. This is implemented through the
network positioning question (Step 0 of the combined workflow) and the
Dependencies and Downstream fields of the Theorem Ledger.

**Finding 4: The Converse Habit**

Whenever students see a conditional statement, they should ask about its
converse as a reflex --- not an occasional probe. Students routinely
conflate a theorem with its converse. This is why the Version 2 Theorem
Ledger includes a Converse field for every entry, and why the Standing
System Prompt includes converse checking as a required step.

**Finding 5: Strategic First Reading**

Alcock advises: read strategically, have a proper attempt at every
section, but if bogged down put a marker and move on. This applies to
the FIRST PASS (Strichartz pass, Days 1--2). The checklist standard
applies to the CONSOLIDATED PASS (end of week). Mixing these modes
produces the anxiety and paralysis Alcock documents as a primary failure
mode.

**Finding 6: Topic-Specific Difficulty Zones and Named Misconceptions**

Alcock identifies specific points where students characteristically
struggle in each topic. Key zones: (Sequences) list vs function
confusion; (Series) terms vs partial sums confusion; (Continuity) the
pencil-lifting informal image actively misleads and must be explicitly
refuted before formalisation; (Real Numbers) the purpose of axioms is
opaque. The misconception catalogue in Part V operationalises this
finding: each checklist embeds the named misconception for that topic
--- with precise logical refutation and the canonical counterexample ---
so it is encountered and refuted at the moment the relevant mathematics
is studied, not retrospectively.

> **Part XI --- Formal Verification with Lean 4**

Lean 4 provides the infallible verification layer. A proof that compiles
is correct by construction. Claude tells you what is wrong; the compiler
tells you whether it is wrong. The two together are more reliable than
either alone.

**Three Interaction Modes**

**Mode 1 --- Chat (Standard Session)**

Claude writes Lean 4 proof scripts without executing them. You run the
compiler, paste errors back to Claude. Claude interprets error messages
and suggests fixes. Available right now in any chat window.

**Mode 2 --- Shell Access (Claude Code / Aider)**

Claude writes proof, runs lake build, reads compiler output, revises,
compiles again. Fully autonomous loop. Lean\'s error messages are
precise --- they include the full proof state, local hypotheses, and
current goal at the point of failure.

**Mode 3 --- Research Frontier**

Tightly coupled LLM + prover systems use the Lean 4 compiler as a reward
signal in a reinforcement learning loop. These systems achieve
olympiad-level formal proving. Claude is not specifically fine-tuned for
this but the capability is present with appropriate scaffolding.

**Reliability by Topic**

  ------------------------------------------------------------------------
  **Topic**                   **Claude        **Notes**
                              Reliability in  
                              Lean 4**        
  --------------------------- --------------- ----------------------------
  epsilon-delta proofs of     High            Well-structured; strong
  limits                                      Mathlib support

  Sequential                  High            Convergence, continuity,
  characterizations                           compactness

  Standard theorems (BW, IVT, High            In Mathlib; API generally
  MVT, Heine-Cantor)                          known

  Series convergence tests    High            M-test, Cauchy criterion in
                                              Mathlib

  Measure theory / Lebesgue   Moderate        More room for error; verify
                                              carefully

  Novel constructions / Rung  Lower           Plausible but verify
  5 problems                                  independently

  Mathlib API currency        Variable        Use exact? and apply? at
                                              runtime for correct names
  ------------------------------------------------------------------------

> **Part XII --- Tool Stack --- Claude Code and Free Stack Workflows**

Two complete tool stacks are described: the Claude Code paid stack and
the Aider + DeepSeek free stack. Both are viable. The key differences
are model quality, session management smoothness, and the depth of the
autonomous proof-revision loop.

**The Three-Layer Architecture (Both Stacks)**

  ------------------------------------------------------------------------
  **Layer**          **Tool**                  **Function**
  ------------------ ------------------------- ---------------------------
  Layer 1 ---        Claude chat (this         Proof outlining,
  Strategy &         interface)                counterexample hunting,
  Intuition                                    definition interrogation,
                                               Socratic tutoring. No file
                                               access required.

  Layer 2 --- Proof  Claude Code or Aider      With actual .lean and .md
  Checking & File                              files open. Writes,
  Management                                   compiles, reads errors,
                                               revises. CLAUDE.md provides
                                               full session context
                                               automatically.

  Layer 3 --- Formal Lean 4 compiler (free)    The infallible ground
  Verification                                 truth. A proof that
                                               compiles is correct. Claude
                                               tells you what is wrong;
                                               the compiler tells you
                                               WHETHER it is wrong.
  ------------------------------------------------------------------------

**Workflow Comparison**

  ------------------------------------------------------------------------
  **Capability**           **Claude Code**         **Aider + DeepSeek
                                                   (Scripted)**
  ------------------------ ----------------------- -----------------------
  File context at launch   Automatic via CLAUDE.md Automatic via
                                                   .aider.conf.yml

  Plan Mode (read-only)    Architectural           Enforced by prompt
                                                   discipline

  Role separation (critic) Subagent ---            Separate session via
                           architecturally fresh   critic.sh

  Lemma lookup             Seamless                10-second lookup.sh ---
                                                   manageable

  Lean error               Claude Sonnet --- root  DeepSeek --- sometimes
  interpretation           cause                   treats symptom

  Complex proof cycle      2--4 cycles typical     5--8 cycles typical
  count                                            

  Cost                     Claude Pro/Max          Free within rate limits
                           subscription            
  ------------------------------------------------------------------------

**Free Stack Friction Reduction --- Key Scripts**

The following system eliminates the five primary friction sources in the
free stack.

**Re-establishing context each session**

Solution: Use .aider.conf.yml with model, read files, and auto-commits:
false specified. Launch becomes: aider src/Chapter3.lean

**Manual role switching**

Solution: Create critic.sh: aider \--model \... \--read PROJECT.md
\--no-auto-commits \--message \"Critic mode: find every implicit step.
No edits.\" /dev/null

**Forgetting relevant files**

Solution: Create launch.sh that auto-discovers earlier chapter files:
EARLIER=\$(find src/ -name \"\*.lean\" \| sort \| awk -v t=\"\$1\"
\'\$0\<t\')

**Manual lemma lookup**

Solution: Create lookup.sh that writes a scratch Lean file with exact?,
runs lean \--run, and greps the output. Correct lemma name in 10
seconds.

**Rate limit pauses**

Solution: Makefile + Ollama fallback: aider \--model
ollama/deepseek-r1:14b for cleanup work when API rate limits hit.

> **Part XIII --- The Complete Weekly Rhythm**

For any given chapter, the weekly rhythm integrates Alcock, Strichartz,
Rudin, the mastery checklist, the proof ladder, formalization, and
review into a coherent cycle. Version 2.1 additions: the Misconception
review is now an explicit Day 3 activity; Day 7 consolidation uses the
Four-Part Assessment rather than the previous single-prompt approach.

  ------------------------------------------------------------------------------------
  **Day(s)**   **Activity**                       **Duration**   **Key Instruction**
  ------------ ---------------------------------- -------------- ---------------------
  Day 1        Network positioning + Alcock       1--1.5 hrs     Ask: where does this
               chapter                                           topic sit in the
                                                                 logical structure so
                                                                 far? Read the
                                                                 corresponding Alcock
                                                                 chapter. Identify the
                                                                 informal image Alcock
                                                                 warns against.

  Days 1--2    Strichartz reading (first pass)    1.5--2 hrs/day Read strategically.
                                                                 Take notes on the
                                                                 WHY. If bogged down,
                                                                 put a marker and
                                                                 continue --- do not
                                                                 halt for a single
                                                                 difficult passage.

  Day 3        Mastery Checklist (Strichartz      1.5--2 hrs     Work through
               pass) + Misconception review                      checklist items
                                                                 Strichartz covered.
                                                                 Read the
                                                                 Misconception entry
                                                                 and write a
                                                                 one-sentence
                                                                 refutation in your
                                                                 own words before any
                                                                 proof work begins.
                                                                 Include
                                                                 Example/Non-Example
                                                                 for every new
                                                                 definition. Ask
                                                                 Claude to quiz you
                                                                 Socratically.

  Days 4--5    Rudin reading + Proof Ladder Rungs 2--3 hrs/day   Read Rudin while
               1--2                                              Strichartz motivation
                                                                 is fresh.
                                                                 Self-explain each
                                                                 line. Apply converse
                                                                 check to every
                                                                 theorem. Work Rung
                                                                 1--2 exercises.

  Day 6        Proof Ladder Rungs 3--4 + Lean 4   2.5--3 hrs     Attempt one Rung 3
                                                                 and one Rung 4
                                                                 problem. Formalize
                                                                 the week\'s major
                                                                 theorem in Lean 4.
                                                                 Apply Bloom Analyze
                                                                 and Evaluate.

  Day 7        Four-Part Assessment + Rung 5 +    2--2.5 hrs     Apply the full
               Ledger update                                     Four-Part Assessment:
                                                                 (1) Applied problem;
                                                                 (2) Conceptual
                                                                 question; (3)
                                                                 Derivation step; (4)
                                                                 Misconception check.
                                                                 Attempt one Rung 5
                                                                 construction. Update
                                                                 Theorem Ledger V2.1
                                                                 (all fields including
                                                                 Misconception). Ask
                                                                 Claude to quiz from
                                                                 Ledger.
  ------------------------------------------------------------------------------------

**Monthly Consolidation**

Return to earlier chapters and re-read theorems you struggled with.
Ideas opaque in Chapter 2 often become clear after Chapter 5. Re-attempt
failed exercises without looking at previous attempts. Ask Claude to
quiz you on the full Theorem Ledger built to date. Ask Claude to analyse
your Error Log for patterns: \"What is the single most common error type
across my last 20 proofs?\"

  -----------------------------------------------------------------------
  **Network re-mapping:** Once per month, ask Claude to help you draw the
  full dependency graph of everything you have proved so far. Which
  theorems are load-bearing for the most results? Which results are most
  isolated? Where are the logical hubs? This is the section-level
  Forward-Backward pass applied to the entire curriculum studied to date.

  -----------------------------------------------------------------------

> **Part XIV --- Key Principles and Final Recommendations**

  -----------------------------------------------------------------------
  **The Overriding Rule:** The productive struggle --- sitting with
  confusion, returning to a problem after sleeping on it, trying a wrong
  approach and understanding why it failed --- is not a bug in the
  learning process. It is the learning process. Use Claude to make the
  struggle more productive, not to eliminate it. Every time you are
  tempted to ask for a complete solution, ask instead: \"What is the one
  question you would ask me right now to help me find the next step
  myself?\" The proof must come from you.

  -----------------------------------------------------------------------

**Fourteen Principles for the Journey**

**1. Slow is fast.** Three pages of Rudin read with full engagement are
worth more than thirty skimmed. Realistic pace: 3--8 pages per day.

**2. Supply every implicit step.** Rudin\'s \"clearly\" and \"it follows
that\" are the curriculum --- each elision is a proof you must write
yourself.

**3. Alcock before Strichartz, Strichartz before Rudin, always.** Build
metacognitive awareness before motivation, and motivation before rigour.
Never reverse this order.

**4. Attempt every theorem before reading the proof.** Failure during
this attempt is not wasted time --- it is the most valuable part of the
process.

**5. Self-explain every line.** Before proceeding to the next line of
any proof, explain the current line in terms of previous ideas. This is
a trainable habit with a large empirical effect (d = 0.95).

**6. Check the converse of every theorem as a reflex.** Whenever you see
a conditional statement, ask whether the converse is true and, if not,
construct the canonical counterexample.

**7. Work the proof ladder for every chapter.** Rungs 1--2 for fluency,
Rungs 3--4 for understanding, Rung 5 for genuine mastery.

**8. Understand every hypothesis.** For every theorem, construct a
counterexample when each hypothesis is removed. This is the deepest
level of understanding.

**9. Complete the mastery checklist before moving on.** Do not advance
to the next chapter until every item is explainable from memory,
including Converse checks, Example/Non-Example generation, and
Misconception refutation.

**10. Do not skip exercises.** Many important results appear only in the
exercises. 60--70% solved independently is a high standard.

**11. Use Claude to make the struggle more productive, not to eliminate
it.** Ask for the next question, not the answer. When stuck, apply the
Complete Stuck-State Management System (D-L-M-K + Pólya at Level 2;
Framework Reframes at Level 3). Use the Four-Part Assessment at the end
of every topic.

**12. The Lean 4 compiler is the authority, not Claude.** A proof that
compiles is correct. Claude can make mistakes; the compiler cannot.

**13. Know your named misconceptions --- and refute them precisely.**
Each topic in Part V carries a named misconception with its precise
logical refutation and the counterexample that breaks it. Before
formalising any concept, surface the named misconception and articulate
exactly why it fails at the logical level. Recognition that something is
wrong is not enough --- you must identify the specific logical step that
is invalid. The gap between informal image and formal definition is
where most errors in Real Analysis are born; the misconception catalogue
makes that gap explicit and navigable.

**14. Keep all proof frameworks active.** Solow is your working language
but not your only tool. When the Forward-Backward method stalls,
escalate through the Complete Stuck-State Management System: the Revised
Recovery Protocol (D-L-M-K + Pólya) at Level 2, then the Velleman,
Eccles, and Hammack Framework Reframes at Level 3. The student who moves
fluently between proof vocabularies is better equipped than one who has
mastered only one, precisely because Real Analysis presents proof
situations that resist any single framework\'s framing.

**Complete Book Reference**

  -----------------------------------------------------------------------------------------------
  **Book**               **Author(s)**                  **Role in       **Level**     **Free?**
                                                        Programme**                   
  ---------------------- ------------------------------ --------------- ------------- -----------
  Principles of          Rudin                          Primary rigour  Graduate      No
  Mathematical Analysis                                 text Ch. 1--8                 

  The Way of Analysis    Strichartz                     Motivation      Adv. UG       No
                                                        companion                     
                                                        throughout                    

  Understanding Analysis Abbott                         Optional gentle Undergrad     No
                                                        opener                        

  Analysis I & II        Tao                            Foundations &   Adv. UG       Yes
                                                        axiom                         
                                                        motivation                    

  Real Mathematical      Pugh                           Rudin           Graduate      No
  Analysis                                              alternative ---               
                                                        geometric                     
                                                        intuition                     

  Advanced Calculus      Nickerson--Spencer--Steenrod   Multivariable   Graduate      PDF
  (NSS)                                                 after Ch. 8                   

  Advanced Calculus      Loomis--Sternberg              Encyclopedic    Graduate      Yes
                                                        advanced text                 

  Calculus on Manifolds  Spivak                         Bridge to       Adv. UG       No
                                                        multivariable                 

  How to Think About     Alcock                         Metacognitive   UG prep       No
  Analysis                                              preparation                   
                                                        text                          

  How to Read & Do       Solow                          Procedural      Intro         No
  Proofs                                                proof scaffold                

  Book of Proof          Hammack                        Breadth +       Intro         Yes
                                                        cardinality                   
                                                        bridge                        

  Intro to Mathematical  Eccles                         Quantifier      Intro         No
  Reasoning                                             rigour                        

  How to Prove It        Velleman                       Deep proof      Intro/Inter   No
                                                        strategy                      
  -----------------------------------------------------------------------------------------------

**Quick-Start Guide by Student Profile**

  -----------------------------------------------------------------------
  **Profile**        **Recommended Path**
  ------------------ ----------------------------------------------------
  New to             Alcock Part 1 (1 week) → Solow Ch. 1--13 (2 weeks) →
  proof-writing      Hammack Ch. 1--12 (2--3 weeks) → Eccles Ch. 1--5 (1
                     week) → Phase 1 of main plan with Abbott as optional
                     opener.

  Some proof         Alcock Part 1 (3 days) → Solow Ch. 1--7 selectively
  experience         (1 week) → Eccles Ch. 1--10 (2 weeks) → Hammack Ch.
                     12 cardinality (3 days) → Phase 1 of main plan.

  Proof-fluent,      Alcock Part 1 (2 days) → Skip Preliminary Phase →
  first analysis     Strichartz Ch. 1 + Rudin Ch. 1 in parallel → Use
  course             Munkres supplement at Phase 2 → Lean 4: start
                     formalizing from Phase 3 onward.

  Revisiting for     Alcock Part 2 as companion → Skim Strichartz for
  graduate           motivation gaps → Focus: Rudin exercises at Rung
  preparation        4--5 level → Lean 4: formalize all major theorems
                     Phases 1--8 → Proceed to Phase 9: NSS or
                     Loomis--Sternberg.
  -----------------------------------------------------------------------

Revised and expanded edition integrating the Strichartz--Rudin Mastery
Plan with Alcock\'s research-based pedagogy, the Complete Stuck-State
Management System (Mason, Sweller, Schoenfeld, Lakatos, Pólya), Bloom\'s
Taxonomy, framework pluralism (Velleman, Eccles, Hammack), the
undergraduate mathematics education literature, and a seven-topic
Misconception Catalogue grounded in the Weber--Mejía-Ramos and
Hodds--Alcock--Inglis research programmes. Lean 4 and Mathlib4 are
open-source and freely available at leanprover.github.io. Book of Proof
(Hammack), Analysis I & II (Tao), and Advanced Calculus
(Loomis--Sternberg) are available free online.
