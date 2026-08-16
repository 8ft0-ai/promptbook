# Plan an issue

## Purpose

Turn a sufficiently shaped issue or task into a bounded, evidence-backed implementation plan.

## When to use

Use before implementation when the desired outcome is known but the technical approach, affected components, validation, or delivery sequence still needs to be worked out.

## Prompt

```text
Act as the principal engineer planning <ISSUE_OR_TASK> for implementation.

Inspect the complete task, relevant discussion, current repository architecture, code, tests, configuration, existing implementation patterns, related accepted decisions, and available validation/CI mechanisms.

First decide whether the task is sufficiently shaped. If a material product, architecture, ownership, security, or scope decision prevents a credible plan, identify that blocker instead of inventing an answer.

Otherwise produce the smallest sufficient implementation plan covering:
- intended outcome, scope, and non-goals;
- repository evidence and constraints that shape the design;
- principal implementation decisions and affected components/files;
- ordered implementation steps and dependencies;
- mapping from acceptance criteria to implementation and proof;
- tests, validation, negative paths, and operational evidence;
- compatibility, migration, rollback, security, reliability, and maintainability risks;
- assumptions, deferred work, and unresolved decisions;
- whether the work is one coherent change or should be decomposed.

Do not begin implementation while planning. End with one disposition: READY FOR IMPLEMENTATION, BLOCKED PENDING DECISION/EVIDENCE, or DECOMPOSE BEFORE IMPLEMENTATION.
```

## Inputs

- `<ISSUE_OR_TASK>` — the issue URL/number, specification, or task statement to plan.

## What it does

Forces the plan to be grounded in current repository evidence and ties each acceptance criterion to both work and validation rather than producing a generic checklist.

## Boundaries / limitations

The prompt does not resolve genuinely missing product or authority decisions. It assumes the assistant can inspect the relevant repository or that the user supplies equivalent evidence.

## Status

`tested`
