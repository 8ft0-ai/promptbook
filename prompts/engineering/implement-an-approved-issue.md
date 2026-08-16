# Implement an approved issue

## Purpose

Implement a bounded task from an accepted plan while preserving scope, traceability, and validation discipline.

## When to use

Use when the intended outcome and implementation approach are already approved or otherwise sufficiently determined, and the receiving agent has an authorised repository write path.

## Prompt

```text
Implement <APPROVED_TASK> using <APPROVED_PLAN>.

Before modifying anything, inspect the current task and acceptance criteria, the approved plan, relevant repository instructions, architecture, code, tests, branch state, and any material changes since the plan was accepted.

If current evidence materially invalidates the plan, stop before speculative mutation and state the smallest decision or replanning step required.

Otherwise implement the smallest sufficient change. Preserve existing architecture and conventions unless the plan explicitly changes them. Add or update tests with behavioural changes, cover relevant negative paths, validate incrementally, and avoid unrelated refactoring or opportunistic dependency changes. Do not weaken tests, assertions, thresholds, or checks to make the candidate pass.

Before declaring completion:
1. inspect the complete diff;
2. map the result back to every acceptance criterion;
3. check for scope expansion, generated artefacts, secrets, and unrelated changes;
4. run all relevant tests, static checks, builds, and required integration/manual validation;
5. verify compatibility, migration, rollback, and residual risks;
6. leave the candidate in a coherent reviewable state.

Return a concise implementation record: outcome delivered, principal changes, acceptance-criterion coverage, validation and results, justified plan deviations, and remaining limitations.

Do not merge, deploy, release, or broaden scope unless that action is already authorised separately.
```

## Inputs

- `<APPROVED_TASK>` — the issue, task, or bounded implementation objective.
- `<APPROVED_PLAN>` — the accepted implementation plan or exact reference to it.

## What it does

Keeps implementation tied to the approved outcome, makes validation part of completion, and forces plan drift to be reconciled before speculative code changes.

## Boundaries / limitations

This prompt does not grant repository mutation, merge, deployment, credential, or production authority. The receiving environment must already have those capabilities and permissions where needed.

## Status

`tested`
