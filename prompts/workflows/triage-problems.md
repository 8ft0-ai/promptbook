# Triage competing problems

## Purpose

Prioritise a finite set of incidents, defects, blockers or issues using evidence of impact, urgency and dependencies. Recommend the smallest useful intervention without changing any governed state.

## When to use

Use for `/triage [target]` when several problems compete for attention. Unlike `/next`, triage compares multiple problems rather than selecting the governed next transition; unlike `/risk`, it ranks work rather than characterising residual risk or accepting it. Execution stays with `/go` or `/fix` under separate authority.

## Prompt

```text
Triage <TARGET> read-only using the current authoritative problem set.

1. BIND: Establish the bounded, finite items, their source, owner constraints, current status and target identity. Consolidate duplicates only with evidence. Do not invent incidents or treat an unverified report as a confirmed defect.
2. DIAGNOSE: For each item, separate observed symptoms and consequences from a probable cause or hypothesis. State dependencies, affected users/scope, decision-critical unknowns and evidence freshness. Do not present an inferred cause as established fact.
3. CLASSIFY each item as BLOCKER (evidence shows a mandatory next action cannot safely proceed), IMPORTANT (material impact but not a proven blocker), DEFER (low urgency or justified later), NOISE (duplicate, irrelevant or demonstrably unsupported), or INCONCLUSIVE (insufficient/conflicting evidence). A valid finding may be NO BLOCKER or NO ACTION. Never invent a blocker to fill a category.
4. PRIORITISE: Rank material items by verified impact, urgency, dependency/unblocking value, risk, reversibility and intervention effort. Explain any ties or uncertain ordering. Mandatory safety and authority requirements prevail; a priority label cannot waive them. Avoid made-up scores, probabilities or root causes.
5. RECOMMEND: Identify the smallest useful next intervention and its rationale, or an evidence check when the ranking is inconclusive. Separate remediation from observation. Do not turn the ranking into an automatic `/next` transition or permission to use `/go` or `/fix`.
6. REPORT: Give a compact ranked list showing item, class, observed evidence, probable cause (or unknown), priority rationale, confidence/uncertainty and recommended next intervention; explicitly identify justified deferred/noise items and whether a real blocker was demonstrated.
7. STOP: Read-only triage. Do not edit or close issues, remediate defects, create PRs, merge, deploy, spend, change permissions, accept risk, approve a candidate, or claim independent review. Follow the owning repository's authority and workflow for any subsequent action.
```

## Inputs

- `<TARGET>` — a finite issue set, incident queue, defect list or bounded workstream; infer only if unambiguous.
- Current evidence of symptoms, causes, impact, urgency and dependencies; mark stale, missing or conflicting evidence.

## What it does

Produces an evidence-linked priority order and the smallest next intervention. Supports justified no-blocker, deferred, noise and inconclusive outcomes without creating new lifecycle gates.

## Boundaries / limitations

Read-only prioritisation is not remediation, outcome verification, owner decision, risk acceptance, or an independent review. Static contract tests do not prove live agent behaviour.

## Status

`experimental`
