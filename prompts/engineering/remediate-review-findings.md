# Remediate review findings

## Purpose

Turn blocking review findings into the minimum safe correction without reopening unrelated design work.

## When to use

Use after a substantive review has identified concrete defects and the existing task or design already determines the intended behaviour closely enough to repair them.

## Prompt

```text
Remediate the blocking findings on <REVIEWED_CANDIDATE>.

First re-read the exact findings, the governing task/design, and the current candidate. Classify each finding as:
- valid and bounded by the existing contract;
- invalid or already resolved by current evidence; or
- requiring a genuinely new product, architecture, authority, or scope decision.

For every valid bounded finding, derive the smallest safe correction. Do not broaden scope, redesign adjacent components, weaken validation, or treat review suggestions as requirements unless the governing contract makes them necessary.

Implement the bounded corrections, add or adjust regression coverage that would have caught the defect, run the relevant validation, and inspect the complete resulting diff for accidental scope expansion.

Return a remediation record mapping each blocking finding to the change and proof that resolves it. Clearly identify any finding that still requires a separate decision rather than pretending remediation is complete.

That remediation record is the workflow record, not a routed terminal state. When this workflow is invoked through the workflow router, return control to the router after recording it so the router can apply the effective continuation mode.

Preserve any required independent re-review boundary; do not present author-side remediation as fresh approval evidence. If this context changed the candidate and independent re-review is required, do not enter that review here. Treat the re-review as a hard fresh-context boundary and, when the durable target is sufficient for reconstruction, hand it off as `Next chat: /review <REVIEWED_CANDIDATE>`. That navigation is not review or merge authority.
```

## Inputs

- `<REVIEWED_CANDIDATE>` — the PR/branch/candidate plus the blocking review findings.

## What it does

Keeps remediation narrow, makes review findings traceable to regression evidence, and prevents a repair cycle from becoming an unbounded redesign. When routed, it returns the remediation record to the governing workflow while preserving the mandatory fresh-context boundary for re-review of a candidate changed in this context.

## Boundaries / limitations

Use only where the expected correction is objectively bounded by existing requirements. Materially new architecture, authority, security, product, or scope decisions should be resolved separately. Author-side remediation cannot substitute for fresh independent review when that gate is required.

## Status

`tested`
