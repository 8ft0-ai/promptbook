# Evaluate models and agent implementations

## Purpose

Compare models or agent implementations fairly on the same decision-relevant tasks using fixed scoring, reproducible inputs, bounded budgets and transparent uncertainty. Do not assume faster, cheaper or more accurate without measured evidence.

## When to use

Use when the current objective explicitly calls for a model/agent comparison. Enter through existing `/go` and use [Bounded experiment](bounded-experiment.md) for the common finite trial, limits and evidence contract; no new public shorthand, runner, hosted evaluator or mandatory infrastructure is created.

## Prompt

```text
Evaluate <CANDIDATES> for <DECISION> within the governing authority.

1. FREEZE before candidate results: the task population, sampling/cohort eligibility, comparable prompt and instruction hierarchy, tools/data permissions, context and system constraints, output format, rubric, primary metric, secondary costs/latency metrics, weighting, tie-breaks, minimum meaningful difference and decision threshold. Reserve any protected test set before tuning.
2. CONTROL FAIRNESS: use the same eligible tasks, input versions, time windows and environmental conditions for each candidate. Pin model/provider/version or report an unpinnable alias; record temperature/seeds where supported, tool availability, inference endpoints and deviations. Treat unequal tool access or time-varying models as limitations, not equivalent comparisons.
3. BOUND RUNS: set trials/replicates, rate limits, token/time/cost ceilings and stop conditions before execution. Free-tier eligibility and authorised model access must be established rather than inferred. Do not use paid fallback, create credentials or consume protected holdouts without authority.
4. SCORE: apply the predeclared rubric consistently. Prefer blinded grading where practical; record evaluator identity, judge/model bias, human adjudication or deterministic checks, failures and abstentions. Retain per-task result/score provenance and aggregate with paired comparisons and uncertainty appropriate to sample size. Never exclude failures or tune the rubric after viewing rankings without explicitly labelling a new exploratory analysis.
5. INTERPRET: separate task quality, reliability, cost, latency and operator effort. Report sample sizes, variance/uncertainty, ties and material limitations; distinguish descriptive rankings from evidence of real-world superiority. A small or confounded sample is INCONCLUSIVE, not an invented winner.
6. DECIDE: choose GO for adoption consideration only if predefined requirements and evidence thresholds are met; NO-GO if candidates fail required criteria; otherwise HOLD. Preserve the existing authorised choice when no demonstrated improvement justifies change. Model selection is not deployment approval, review acceptance, or spending authority.
7. RECORD: write or report the minimal reconstructable comparison protocol, candidate/input identities, raw/derived result locations, scoring method, usage receipts and deviations at an already-authorised destination. Stop at the experiment ceiling or lifecycle boundary.
```

## Inputs

- `<CANDIDATES>` — named model/agent implementations and exact usable identities where available.
- `<DECISION>` — the use case and adoption threshold.
- Common task data, rubric, available access and finite budget limits.

## What it does

Produces a decision-focused, paired comparison rather than a marketing-style leaderboard. Reuses the finite experimental discipline of [Bounded experiment](bounded-experiment.md) and existing `/go` permissions and evidence rules.

## Boundaries / limitations

No inference budget, external credential, runner installation, new service, deployment or repository mutation authority follows from selecting this workflow. No self-scored success or unmeasured savings are treated as independent or observed behaviour. Follow repository-local privacy, fairness, holdout and review requirements.

## Status

`experimental`
