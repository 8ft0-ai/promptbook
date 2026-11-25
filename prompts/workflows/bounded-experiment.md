# Run a bounded experiment

## Purpose

Answer one falsifiable engineering or research question using a finite, reproducible experiment. Use existing tools and data; do not add an experiment service, scheduler or new approval stage.

## When to use

Use when the governing objective explicitly calls for a bounded experiment, feasibility test or measurable hypothesis. Route via ordinary `/go` and the existing authority model. Do not confuse this with [Bounded concern lifecycle](bounded-concern-lifecycle.md), a separately selected high-consequence review-preparation protocol.

## Prompt

```text
Run a bounded experiment for <OBJECTIVE> within current authority.

1. SPECIFY before observing outcomes: state the falsifiable hypothesis and null/negative result; intended decision, fixed input/source and eligibility criteria, exact version/identity, measurement/metric, baseline or control, predeclared success/failure threshold, sampling window and independent test/holdout boundary where relevant.
2. BOUND: state the maximum trials, duration, compute/API spend, data access, rate/concurrency limits and stop conditions. No unstated retries or paid fallback. An unspecified resource or permission ceiling does not confer authority to execute. Preserve any governing scientific preregistration or protected holdout rules.
3. EXECUTE only permitted steps: establish a minimal reproducible procedure with parameters, environment/version, random seeds where used, observation timestamps, source receipts and failure handling. Do not silently tune thresholds, alter cohort inclusion or extend the window after observing results; such changes require a labelled new experiment under appropriate authority.
4. EVALUATE against the predeclared test, including negative findings and uncertainty. Distinguish data/transport success from hypothesis success, exploratory from confirmatory evidence, and missing/invalid observations from favourable results. Report attempted and valid trials, exclusions, deviations, limitations and actual resource use.
5. DECIDE: GO only when the predeclared evidence is sufficient for the stated next decision; NO-GO when the hypothesis or eligibility fails; HOLD for insufficient, confounded, stale or unavailable evidence. A GO finding is not permission to trade, deploy, spend, publish or cross a required review gate.
6. STOP at the first completed result, finite ceiling or real authority/capability boundary. Preserve a reproducible evidence record and the smallest justified next action. No automatic new infrastructure or repeated test cycle.
```

## Inputs

- `<OBJECTIVE>` — the specific empirical question and decision.
- Predeclared source, baseline, metrics, constraints and available execution authority. Missing essentials produce a bounded protocol or HOLD, not speculative execution.

## What it does

Supports hypothesis testing without optimistic retrospective selection. The finite limits and outcome evidence are part of the experiment, not new platform policy. Use [Autonomous progression](autonomous-progression.md) for already-authorised execution and [Verify delivered outcome](verify-outcome.md) for a later read-only outcome check.

## Boundaries / limitations

The workflow grants no repository mutation, data entitlement, new permission, paid inference, trading, deployment or approval. A test result is not fresh independent review. Applicable project-specific scientific, security and resource controls prevail.

## Status

`experimental`
