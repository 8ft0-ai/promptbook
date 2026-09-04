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

That implementation record is the workflow record, not a routed terminal state. When this workflow is invoked through the workflow router, return control to the router after recording it so the router can apply the effective continuation mode to the next governed gate. If required independent review is the next gate and this context authored or materially shaped the candidate, preserve the fresh-context boundary rather than reviewing the candidate here. Return control to the router so it can resolve an eligible genuinely isolated fresh-review context under the fresh-review context-resolution contract. Only when no eligible/provable isolated context can be established should the existing manual fallback be used; a durable target may then be handed off as `Next chat: /review <APPROVED_TASK>` when that target is sufficient for reconstruction.

Do not merge, deploy, release, or broaden scope unless that action is already authorised separately. Continuation metadata never creates that authority.
```

## Inputs

- `<APPROVED_TASK>` — the issue, task, or bounded implementation objective.
- `<APPROVED_PLAN>` — the accepted implementation plan or exact reference to it.

## What it does

Keeps implementation tied to the approved outcome, makes validation part of completion, and forces plan drift to be reconciled before speculative code changes. When routed, the implementation record returns control to the governing workflow instead of accidentally ending the broader objective. A context that authored the candidate remains ineligible to review it independently; the router may satisfy that hard boundary through an eligible isolated fresh-review context before requiring manual context transport.

## Boundaries / limitations

This prompt does not grant repository mutation, merge, deployment, credential, or production authority. The receiving environment must already have those capabilities and permissions where needed. A required fresh independent review remains a hard boundary after this context authors or materially shapes the candidate. Automatic context resolution may change how that boundary is satisfied, but it never makes the authoring context fresh and never weakens a repository requirement for another human or formal reviewer.

## Status

`tested`
