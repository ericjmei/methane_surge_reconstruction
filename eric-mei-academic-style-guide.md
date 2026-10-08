# Eric Mei Academic Writing Style Guide

Use this guide when drafting, revising, or reviewing academic writing in Eric Mei's voice. It is based on the following publications:

- Mei et al., 2025, "Emulating chemistry-climate dynamics with a linear inverse model," *Atmospheric Chemistry and Physics*
- Mei et al., 2026, "Multidecadal preindustrial methane variability can be explained by noise in the source–sink imbalance," *PNAS*

Both are lead-author papers. The ACP paper shows the voice in a conventional methods-results-conclusions structure; the PNAS paper shows it in a compressed, question-driven structure. The guide is written to apply to any paper in climate dynamics, atmospheric chemistry, paleoclimate, or data assimilation, not only to those two topics.

## Core Voice

Eric's academic style is parsimonious, quantitative, and model-driven. The prose builds the simplest model that could explain a signal, tests whether it does, and then asks what the model implies about the real system. The tone is direct when describing what was calculated and what a model reproduces, and measured when moving from model behavior to claims about nature.

Prioritize:

1. A simple model with few parameters and a stated null hypothesis.
2. A visible test of that model against observations or a more complex model.
3. Quantitative statements of skill, variance, timescale, and magnitude.
4. Explicit sensitivity checks and stated limitations.
5. A bounded implication that names what the result enables next.

Do not write like a proposal abstract, press release, or broad review. Avoid generic urgency. The writing should feel like a careful scientist showing that a low-dimensional description captures the essential dynamics of a high-dimensional system, and being precise about where it does not.

## Argument Pattern

Most papers follow this logic:

1. Start from an important Earth-system quantity and why it matters.
2. Name the tool or record normally used to study it.
3. State the limitation of that tool: cost, a missing ingredient such as memory or feedbacks, or an untested assumption.
4. Introduce a simpler model that keeps the essential dynamics.
5. Say what was calibrated or tuned, and to what.
6. Validate the model: statistics, spectra, spatial patterns, or forecast skill.
7. Use the model to run an experiment that would be hard in the full system.
8. Interpret the result as a constraint, a regime boundary, or a baseline for attribution.
9. End with what the model enables next.

The paper's central question may be stated outright. A section heading can be a question, and a paragraph can pose a question before answering it, when the question is the actual hypothesis being tested. Do not use questions as decoration.

Use causal connectives deliberately. "Thus" and "Therefore" mark a real consequence of the preceding sentence. "In contrast" sets two models or regimes against each other. "However" introduces a limitation or tension. "Notably" and "In particular" flag the result the reader should keep. "In other words" and "That is" restate a technical result in plainer terms.

## Section-Level Style

### Titles

Titles take one of two forms:

- A gerund phrase naming the task and the method: "[Verb-ing] [system or quantity] with [method]."
- A declarative sentence stating the result: "[Phenomenon] can be explained by [mechanism]."

Prefer the declarative form when the paper has one clear finding. Prefer the gerund form when the paper introduces a tool. Avoid question titles and colon-subtitle titles.

### Abstracts

Use the abstract as a compact version of the argument pattern. A typical structure is:

1. The quantity of interest and the standard tool or record.
2. The limitation of that tool, or the prior assumption being tested.
3. "Here, we present/use/explore..." statement of what was done.
4. One or two sentences on what the model is and how it was calibrated.
5. Main results, with numbers or thresholds.
6. The experiment that isolates a mechanism, and what it showed.
7. What the result implies and what it enables.

Define acronyms on first use, including in the abstract. Name key quantities in plain terms before using symbols.

Use active contribution verbs:

- "Here, we present..."
- "Here, we explore..."
- "We show that..."
- "We use this model to..."
- "Our results show that..."

"Demonstrate" is acceptable when the result follows directly from a calculation or model experiment. Do not use it for an inference about the real system.

### Significance Statements and Plain-Language Summaries

When a journal asks for one, write four to six sentences for a general scientific reader. State what the record or model shows, what prior work assumed, what this work shows instead, and the one consequence that matters. Use "We show that..." once. Avoid acronyms and equations. Give scale in plain units where useful.

### Introductions

Open with the Earth-system quantity and its importance, then narrow to the tool and its limitation within the first paragraph. State the contribution early, often by the end of the first paragraph, and return to it in more detail at the end of the introduction.

Preferred sequence:

1. "[Quantity] matters because [consequence]. [Tool or record] is used to study it, but [limitation]."
2. What is known about the drivers of variability, cited densely.
3. What prior methods have and have not captured, and why the missing ingredient matters.
4. The method, its lineage, and what it will be used for here.

A roadmap paragraph ("The remainder of the paper is organized as follows...") is acceptable when the paper has several distinct parts.

Citations are dense in the context paragraphs and sparse once the paper's own logic begins. Cite in clusters with "e.g.," for general points and by name when building on a specific result ("Following [Author] (year), ...").

### Model and Methods Sections

State the governing equation early and interpret every symbol immediately after. Define symbols with "in which," not "where":

> "[Equation], in which [symbol] is [meaning] and [symbol] represents [meaning]."

A good model paragraph does the following:

1. States the equation.
2. Defines each symbol and its physical meaning.
3. States the assumption that makes the equation valid (linearity, stationarity, timescale separation, Gaussian white noise).
4. Says what the assumption represents physically.
5. Names the limiting case and what simpler model it recovers.

When describing a data source or a complex model, open with "Briefly," and give the essentials in a few sentences: resolution, components, forcing, output frequency, and which part of the record is used. State any train/test split explicitly.

Describe preprocessing as a sequence of named steps. For each step, say why it was needed and what fraction of the signal or variance it removes or retains.

State what was tuned and to what. If an amplitude was scaled to match an observed quantity, say so in the main text, not only in the methods.

Put derivations in the methods section or supplement and refer to them by equation number. Keep the main text focused on what each equation means.

### Results

Results sections are figure-driven and quantitative. Each paragraph begins by saying what is compared, reports the main feature with a number, then explains why.

Use this pattern:

1. "Fig. N shows [quantity] as a function of [parameter]" or "[Model A] outperforms [Model B] for [range] (Fig. N)."
2. The specific numbers.
3. "This behavior occurs because [mechanism]."
4. "Therefore, [bounded inference]."

Describe each experiment as an explicit manipulation of the model: remove a mode, hold a parameter fixed, sweep a timescale, swap an input. Then report what the manipulation changed.

Name regimes, limits, and coined quantities with a short quoted label on first use, then use the label without quotes. Choose labels that are physically descriptive.

Report robustness inline and briefly:

- "Our conclusions are not sensitive to [choice] (Fig. SN)."
- "Retaining more [components] does not notably change our results."
- "Conclusions are invariant to the choice of [metric]."
- "(not shown)"

Say when a feature is a property of the model or the sample rather than of nature.

### Discussion and Limitations

A standalone discussion section is optional. Limitations may be placed where they arise: at the end of the relevant results subsection or in the conclusions. Each limitation gets a sentence naming the assumption, a sentence on what it affects, and a sentence on what future work should do about it.

When discussing alternatives, state what each would predict and do not caricature them. A useful construction is "This does not rule out [alternative], but it suggests that [constraint]."

When two explanations are possible, name both and say which is more likely and why: "This result suggests either that [A] or that [B]. The latter is more likely, as [reason]."

### Conclusions

Conclusions restate the contribution, list what the model reproduces, state the central result, and then spend most of the section on what the result enables. The usual sequence is:

1. "We present [model or framework] to [purpose]."
2. What it reproduces and how cheaply.
3. The central result and the mechanism it isolates.
4. The conditions under which the method is valid, as an enumerated list: "Provided that [model] (1) [condition], (2) [condition], and (3) [condition], it can be used to..."
5. What the framework serves as a baseline for, and what it rules in or out.
6. Future applications, each with a reason it is now feasible.
7. A closing sentence on what new observations or models would help.

Good final implications sound like:

- "A clear next step is to..."
- "Such [reconstructions/experiments] could correct..."
- "Observations of [quantity] from [setting] would be useful to..."
- "Future work should assess..."

Avoid ending with a claim about transforming the field or solving a societal problem.

## Claim Strength

Keep the distinction between observation, model output, calculation, inference, and speculation explicit.

Use:

- "observed," "measured," "recorded" for data.
- "simulate," "calibrate," "calculate," "derive," "estimate" for what was done.
- "reproduces," "captures," "matches," "is consistent with," "is statistically indistinguishable from" for model-data comparison.
- "suggests," "implies," "indicates," "is likely," "probably occurs because," "it is plausible that" for inference.
- "could," "may," "would," "potentially" for future applications and speculative mechanisms.

"Show" and "demonstrate" are fine for results that follow directly from the model. Reserve "suggests" for the step from model to nature. Do not write "proves."

Good:

- "The existence of [mode] in the model suggests that [simple dynamics] can capture [the dominant driver]."
- "Therefore, it is plausible that [process] could significantly affect [interpretation]."
- "These components are likely sufficient to reproduce [observed quantity] in our framework."

Avoid:

- "The model reveals the true dynamics of the system."
- "This proves that [process] drives [signal]."
- "This finding transforms our understanding of..."

## Sentence Style

The typical sentence is long, often 25 to 35 words, and carries one complete causal step. Shorter sentences open paragraphs and state conclusions. Long sentences are acceptable when they chain a condition, an action, and a consequence in order.

Characteristic constructions:

- Sentence-initial "Here," to mark the contribution or the current step.
- "Though..." or "While..." at the start of a sentence to concede before the main clause.
- "Given that..." or "Given [noun]," to state the premise for the next step.
- "To [verb] ..., we ..." to open a paragraph with its purpose.
- "That is," or "In other words," to restate a technical sentence plainly.
- Inline enumeration with (1), (2), (3) for conditions, criteria, or penalties.
- Parenthetical asides with "e.g.," and "i.e.," and parenthetical pointers to figures and supplement.

Common transition words that fit this style:

- "Thus"
- "Therefore"
- "However"
- "In contrast"
- "Notably"
- "In particular"
- "Similarly"
- "Conversely"
- "As such"
- "For example"
- "Interestingly" (sparingly, for a genuinely unexpected feature)

Use these only when the logical relation is real.

Avoid:

- Marketing adjectives: "groundbreaking," "transformative," "unprecedented" unless literally true.
- Vague intensifiers when a number can be given.
- Generic openers: "Recently, there has been growing interest..."
- Rhetorical questions that are not the paper's actual hypothesis.

## Paragraph Style

A paragraph does one job: define a model, describe one preprocessing choice, report one figure comparison, run one experiment, or state one limitation.

Preferred structure:

1. Topic sentence stating the purpose or the comparison.
2. Setup, numbers, or figure reference.
3. Mechanism or explanation.
4. Inference, often a "Therefore" or "This suggests" sentence.
5. Optionally, a handoff to the next question ("This motivates the next question: ...").

Keep the setup of an experiment and its result together when the result is one or two sentences. Split when the result needs its own mechanism paragraph.

## Figures and Captions

Captions are long and self-contained. A reader should be able to interpret the figure from the caption alone. A caption includes:

- A first sentence naming what is compared or shown across the whole figure.
- One clause per panel, by letter.
- Colors, line styles, and shading, named explicitly.
- Normalization, scaling, and sampling choices.
- Parameter values used, including which line is the reference case.
- Reference lines and what they mark.

In the main text, refer to figures as evidence and use them to anchor numbers:

- "Fig. N shows that..."
- "...which is evident in Fig. N."
- "(compare [panels] of Fig. N)"

Every figure validates a statistic, shows a mode or regime, compares skill, or maps a parameter space. Avoid figures that only illustrate.

## Quantitative and Technical Conventions

Anchor claims with numbers early: variance fractions, correlations, skill scores, damping times, periods, lifetimes, concentrations, computational cost.

Use:

- SI units, with timescales in whatever unit matches the process.
- Both absolute and relative scale when helpful: "[value] ([percent])."
- Approximate values with "∼" or "about" when precision is not warranted.
- Inequalities for regime boundaries.
- Acronyms defined at first use in the abstract and again in the main text.
- A short quoted label for a coined quantity or regime on first use.
- Explicit statements of what fraction of variance a choice removes or retains.
- Computational cost with enough hardware detail to be reproducible.

For equations:

- Number every displayed equation and refer to it by number.
- Define symbols with "in which" immediately after the equation.
- Give the physical meaning of every timescale and rate.
- State the limiting case and what it recovers.
- State whether each quantity is prescribed, tuned, calibrated, or derived.
- Keep long derivations in the methods or supplement, and summarize the result in one sentence in the main text.

For stochastic and linear models, use the standard vocabulary consistently: e-folding time, decorrelation timescale, white noise, memory, damped, stationary, power spectral density, lead time, skill.

## Citations

Citations support specific claims. Use clustered parenthetical citations with "e.g.," for general background, and name authors in prose when building on a specific result:

- "Following [Author] (year), ..."
- "[Author] estimate that..."
- "This result is consistent with [class of models] (e.g., ...)."

The introduction carries the highest citation density. Results cite when a feature matches or contradicts prior work. Follow the target journal's format.

## Reusable Templates

### Abstract Contribution

"Here, we present [simple model] to [emulate/explain] [system or record]. [Model] is a [low-dimensional/linear/stochastic] model that [reproduces statistic] at [cost]. We show that [main result with number], and [experiment] shows that [mechanism] is responsible for [fraction of the effect]."

### Introduction Gap

"[Tool or record] is a powerful means to study [quantity], but [limitation] limits its use for [application]. Prior work has relied on [alternative], which [removes/assumes] [essential ingredient]. Here, we present [simple model] that [retains the ingredient] at [low cost]."

### Model Setup

"[Governing equation], in which [symbol] is [meaning] and [symbol] represents [meaning]. We assume [assumption], which represents [physical process]. In the limit where [parameter] is [small/large], we recover [simpler case]."

### Result Paragraph

"To [purpose], we [experiment]. [Model] [outperforms/reproduces/captures] [target] for [range] (Fig. N). [Specific numbers.] This behavior occurs because [mechanism]. Therefore, [bounded inference]."

### Robustness Sentence

"Our conclusions are not sensitive to [choice] (Fig. SN)."

### Limitation

"A fundamental assumption of [model] is [assumption]. [Condition that violates it] could challenge [calibration/skill]. Future work should assess [model] under [conditions]."

### Conclusion

"We present [model] to [purpose]. [Model] [reproduces statistics] and can be decomposed into [interpretable components]. [Central result with numbers.] Provided that [model] (1) [condition], (2) [condition], and (3) [condition], it can be used to [applications]. A future application enabled by [property] is [application], which could [consequence]."

## Revision Checklist

Before considering a draft finished, check:

1. Does the first paragraph name the quantity, the standard tool, its limitation, and the contribution?
2. Is the model stated as an equation with every symbol defined using "in which"?
3. Is every assumption named, given a physical interpretation, and either tested or flagged for future work?
4. Is it stated what was tuned, calibrated, prescribed, or derived?
5. Does every results paragraph contain at least one number?
6. Is each experiment described as an explicit manipulation of the model?
7. Are regimes, limits, and coined quantities given short descriptive labels?
8. Are robustness checks reported inline with a pointer to the supplement?
9. Are model features distinguished from features of the real system?
10. Do captions name every panel, color, normalization, and parameter value?
11. Does the conclusion list the conditions under which the method is valid?
12. Does the paper end with a concrete next application or observation, not a sweeping claim?

## Things to Avoid

Avoid:

- "This paper explores..." when the paper calibrates, tests, or constrains.
- Novelty language without a specific contribution. "First application of..." is fine when literally true.
- Reporting skill or agreement qualitatively when a metric, variance fraction, or timescale can be given.
- Hiding the tuning step.
- Treating a reproduced statistic as proof of the underlying mechanism.
- Long literature summaries that do not sharpen the limitation being addressed.
- Discussion sections that repeat the results.
- Mixing hyphenation or spelling conventions within a manuscript. Pick one and follow the journal.

Prefer:

- "Here, we present..."
- "We show that..."
- "This behavior occurs because..."
- "Our conclusions are not sensitive to..."
- "This result suggests..."
- "Future work should..."
- "A clear next step is to..."

## AGENTS.md Snippet

Use this line from an AGENTS.md file when you want writing agents to follow the guide:

```markdown
For Eric Mei academic writing, follow the style guide in `eric-mei-academic-style-guide.md`.
```
