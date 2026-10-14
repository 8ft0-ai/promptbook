# Engineering Thinking Shortcuts for AI-Assisted Development

**Status:** Research note — exploratory; no implementation or process change authorised  
**Prepared:** 15 October 2026  
**Origin:** [@Voxyz_ai X post](https://x.com/Voxyz_ai/status/2110324749557784946) and subsequent discussion  
**Potential owner:** `8ft0-ai/promptbook` for reusable workflow guidance

## Executive summary

Five established engineering and scientific methods can be invoked with short, context-aware instructions to improve AI-assisted design and review:

1. **First-principles reasoning** — question the problem framing and reconstruct the need from evidence.
2. **Adversarial review** — search for counterexamples to central assumptions rather than merely checking whether a plan seems sound.
3. **Ablation testing** — isolate the contribution of individual interventions where credible controlled comparisons are possible.
4. **Occam's razor** — select the simplest solution that preserves required guarantees.
5. **High cohesion and low coupling** — organise responsibilities around meaningful boundaries and minimise unnecessary dependencies.

These are *reasoning cues*, not guaranteed shortcuts. A short instruction is most useful when the repository already contains clear requirements, source, tests, measurements and relevant context. An AI reviewing its own plan does not automatically constitute an independent review.

**Recommendation:** First examine how these principles already appear in Promptbook. Prefer modest guidance within existing `/plan`, `/review`, `/fix`, `/go` and reflection/effectiveness activities over additional commands, agents, mandatory review stages or governance processes. The agent must be able to conclude that the existing approach is already appropriate.

## 1. First-principles reasoning

**Question:** What is the actual problem, and which facts justify the proposed solution?

Start with verified requirements, observations and constraints rather than a favoured technology. Distinguish symptoms, causes, assumptions and interventions. Develop and test competing explanations.

**Example:** An endpoint takes 800 ms and somebody proposes Redis. An investigation could reveal that most of the time is spent in a poorly indexed SQL query. An appropriate index might remove the bottleneck without caching infrastructure. Values here are illustrative, not measured results.

**Short prompt:**

> Reanalyse this problem from first principles. Separate verified facts from assumptions, identify the underlying cause and challenge whether the proposed solution is necessary.

**Best suited to:** performance investigations, technology selection, incident analysis, architectural design and early planning.

**Evidence:** Google SRE's [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) discusses systematic hypotheses and testing in operational diagnosis.

## 2. Adversarial review

**Question:** What would make this plan incorrect, unnecessary or unsafe?

Try to disprove essential assumptions, consider realistic counterexamples, and identify lower-complexity solutions with the same guarantees. This is related to the premortem technique and scenario-driven architecture review.

**Example:** Instead of optimising a proposed distributed lock implementation, ask whether idempotent request handling plus a database unique constraint would satisfy the duplicate-processing requirement. The answer depends on the actual concurrency, consistency and durability requirements; the simpler option is not universally adequate.

**Short prompt:**

> Conduct an adversarial review. Find counterexamples to the central assumptions, identify plausible failure scenarios and determine whether a simpler alternative would satisfy the requirements.

**Best suited to:** independent design review, significant architectural changes, consequential security and reliability decisions, and challenging implementation plans before code changes.

**Limitation:** An adversarial prompt to the authoring model is useful but does **not** replace a genuinely independent reviewer where required.

**References:** Gary Klein, [Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem); Carnegie Mellon SEI, [Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/).

## 3. Ablation testing

**Question:** Which component of a multi-part change actually caused the observed improvement?

Compare a baseline with controlled configurations that remove or introduce individual mechanisms. Measure both primary outcomes and relevant trade-offs. Allow for interactions and confounders; simple one-at-a-time comparisons do not always isolate all effects.

**Illustrative latency example:**

| Configuration | Endpoint latency |
| --- | ---: |
| Baseline | 800 ms |
| Database index only | 125 ms |
| Index + cache | 122 ms |
| Index + cache + connection pooling | 120 ms |

*These figures are invented to illustrate experimental design, not empirical measurements.*

Such a result would suggest that the index accounts for most of the latency reduction under the tested workload. The other mechanisms may still have benefits under different loads or failure conditions.

**Short prompt:**

> Design the smallest useful ablation experiment to establish which changes actually contribute to the result. Control for confounding factors and identify interactions between changes.

**Best suited to:** ML model components, performance interventions, prompting experiments, and architecture components whose effects can be safely isolated.

**Limitation:** Ablation is not always feasible or safe in production. Observational effectiveness studies should not be relabelled as controlled ablation experiments, and existing sampling or attribution rules should not be retrospectively changed.

## 4. Occam's razor and operational simplicity

**Question:** What is the least complicated design that satisfies all real requirements?

Minimise unnecessary assumptions, infrastructure, abstractions, components and process steps **without** weakening security, correctness, availability, maintainability or other required properties.

**Example:** A proposed API → Kafka → worker → distributed lock → database pipeline may be unnecessary if one database transaction and a unique constraint meet the actual requirements. It may be entirely justified if asynchronous durability, backpressure or independent scaling are real requirements.

**Short prompt:**

> Apply Occam's razor. Identify unnecessary components, abstractions, dependencies and process steps. Propose the simplest solution that preserves all required guarantees.

**Best suited to:** architecture planning, infrastructure design, proposed new services, and reviewing the engineering workflow itself.

**Workflow relevance:** Procedural complexity is still complexity. Extra handovers, reviews or documentation can impose a cost even when individual steps sound defensible. Simplification must not silently erase genuine evidence, independent assurance or authority boundaries.

**Reference:** Google SRE Workbook, [Simplicity](https://sre.google/workbook/simplicity/).

## 5. High cohesion and low coupling

**Question:** Are responsibilities grouped sensibly, and can components evolve without excessive coordination?

Prefer boundaries that conceal decisions likely to change. Separate genuinely distinct concerns, but do not split a coherent component simply to make files smaller.

**Example:** A 2,000-line service class may need decomposition if it mixes unrelated responsibilities. Splitting it into many mutually dependent classes solely to reduce line counts can make maintainability worse.

**Short prompt:**

> Review responsibility boundaries for high cohesion and low coupling. Extract only genuinely independent responsibilities. Do not introduce abstractions or split components merely to reduce their size.

**Best suited to:** refactoring, service boundaries, APIs, ownership design and architecture reviews.

**Workflow relevance:** Keep reusable workflow guidance separate from application repositories' authority over their own implementation.

**Reference:** D. L. Parnas, [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623) (1972).

## Why short prompts can work — and where they fail

A named methodology can provide a compact cue for a model that already recognises the concept. But the model still needs the project's context and evidence. A memorable phrase is not proof that the requested method has been correctly applied.

| Style | Example | Limitation or value |
| --- | --- | --- |
| Vague | “Think harder.” | No concrete target. |
| Named method | “Apply Occam's razor.” | Identifies a reasoning method, not the requirements. |
| Method + objective | “Remove unnecessary architectural dependencies.” | More actionable. |
| Method + evidence | “Use actual requirements, source and tests; preserve reliability guarantees.” | Best grounded for consequential decisions. |

Prefer verifiable artefacts such as tests, execution traces, benchmark data and source references over unsupported self-evaluation. Repository documentation and tests provide durable context that can make interactive prompts substantially shorter.

**Further guidance:** [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## Optional related framework: Six Thinking Hats

Edward de Bono's **Six Thinking Hats** is a way of separating perspectives, not an engineering substitute for evidence or independence.

| Hat | Perspective | Example use |
| --- | --- | --- |
| White | Facts and evidence | What is verified? |
| Red | Intuition and concerns | What feels risky or awkward? |
| Black | Weaknesses | What could fail? |
| Yellow | Benefits | Why might this work? |
| Green | Alternatives | What else could solve it? |
| Blue | Process and decision | What should be concluded? |

A single structured review should be tried before introducing six separate agents. Additional agents create complexity and do not by themselves guarantee independent reasoning.

## Possible use in existing Promptbook workflows

| Existing stage | Selective technique | Intended outcome |
| --- | --- | --- |
| `/plan` | First principles; Occam's razor | Correct framing and minimal feasible approach. |
| `/review` | Adversarial review | Find counterexamples and unjustified mechanisms. |
| `/fix` | Cohesion/coupling | Correct responsibility boundaries without gratuitous restructuring. |
| `/go` | Evidence-backed validation | Execute the already authorised scope; do not add ceremony. |
| `/reflect` or an effectiveness evaluation | Ablation reasoning where appropriate | Separate mechanism contribution from coincidental outcomes. |

This table is a *candidate mapping*, not a request to add commands or change Promptbook's existing semantics.

## Suggested pre-implementation design challenge

> Reassess the current plan using first-principles reasoning and an adversarial review.
>
> Challenge its assumptions, identify unnecessary complexity and apply Occam's razor to find the simplest design that meets the requirements.
>
> Preserve high cohesion, low coupling and all required safety and reliability guarantees.
>
> Where several mechanisms contribute to an outcome, identify how their individual effects could be verified.
>
> If the existing plan is already appropriate, say so. Do not introduce additional process, architecture or tests without a specific justification.

**Use selectively**, especially when the plan introduces significant new architecture or operational complexity. Do not require this prompt for routine, low-risk work.

## Recommended follow-up

Create **one exploratory, design-only Promptbook issue** to:

1. Inventory where these five principles already exist in current Promptbook guidance.
2. Identify a concrete gap, if any, supported by examples.
3. Prefer one small clarification to existing guidance over new commands, agents or mandatory stages.
4. Specify how to recognise improved outcomes without pretending observational evidence establishes causal attribution.
5. Explicitly permit a **NO CHANGE NEEDED** conclusion.

**Boundaries:** No implementation authority, no automatic workflow changes, no new recurring monitoring and no child-repository changes. If an issue is created, use this note as source material; avoid duplicate copies of the same research as separate canonical documents.

## References

- [Original @Voxyz_ai post on X](https://x.com/Voxyz_ai/status/2110324749557784946) — claim about five short methodology prompts; user-provided text.
- Google SRE, [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/).
- Google SRE Workbook, [Simplicity](https://sre.google/workbook/simplicity/).
- Gary Klein, [Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem) (2007).
- Carnegie Mellon SEI, [Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/).
- D. L. Parnas, [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623) (1972).
- Anthropic, [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

*This is a research and discussion note. The illustrative examples are not outcome evidence, and the references do not validate the X post's stronger claims about the effectiveness of short prompts.*
