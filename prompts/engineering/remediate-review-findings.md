# Remediate review findings

## Purpose

Turn blocking review findings into the minimum safe correction without reopening unrelated design work, using explicit reconstructable mutation authority rather than tool availability or remembered conversation state.

## When to use

Use after a substantive review has identified concrete defects and the existing task or design already determines the intended behaviour closely enough to repair them.

## Prompt

```text
Remediate the blocking findings on <REVIEWED_CANDIDATE>.

First re-read the exact findings, the governing task/design, the current candidate, applicable repository instructions, and current authority. Before substantive mutation, resolve the `/fix` Resolved Agent Run Context defined by `prompts/workflows/resolved-agent-run-context.md` from current authoritative inputs rather than conversation memory.

Bind the run context to the repository/work item, exact starting candidate identity, authority sources, instruction provenance, bounded remediation scope, effective and prohibited capabilities, owner-decision boundaries, required validation, and required evidence. Treat the context as ephemeral derived execution state, not as a new authority source.

Immediately before the first material write, refresh the starting candidate identity. If it moved, invalidate the stale candidate-specific context and re-resolve before applying findings to unexpected bytes.

Classify each finding as:
- valid and bounded by the existing contract;
- invalid or already resolved by current evidence; or
- requiring a genuinely new product, architecture, authority, security, or scope decision.

When the review evidence identifies a material relationship among findings, preserve that diagnosis while deriving remediation. Determine whether the corrections are genuinely isolated local changes or one shared invariant/boundary correction. Do not count findings mechanically or infer redesign merely from recurrence.

For every valid bounded finding, derive the smallest safe correction. The smallest safe correction is not necessarily the smallest textual or most local patch. Where a shared invariant/boundary correction is objectively determined by the governing contract and findings and is already within the resolved remediation scope and `/fix` authority, that correction may be the minimum safe change. If the appropriate invariant/boundary correction requires materially new product, architecture, security, scope, owner, or other separate authority, classify that boundary honestly rather than decomposing it into superficially local exceptions or silently redesigning. Do not broaden scope, redesign adjacent components, weaken validation, or treat review suggestions as requirements unless the governing contract makes them necessary.

Before each material action, apply the `/fix` action gateway and classify the action as:
- `ALLOW` — current authoritative sources permit the action within the resolved remediation scope and `/fix` operation ceiling;
- `REQUIRE OWNER / SEPARATE AUTHORITY` — the action is outside the resolved remediation scope or needs missing product, architecture, security, scope, owner, or other separate authority;
- `FORBID` — higher-precedence authority or the `/fix` operation ceiling prohibits the action under this `/fix` authority.

Missing or ambiguous authority never defaults to `ALLOW`. Keep authority classification separate from execution feasibility: a technically available tool never grants authority, while an `ALLOW` action whose required execution capability is unavailable follows the governing router's capability/external-action boundary without inventing a new owner decision.

Execute only `ALLOW` actions that are actually available. Implement the bounded corrections, add or adjust regression coverage that would have caught the defect, run the relevant required validation, and inspect the complete resulting diff for accidental scope expansion. If unexpected external candidate movement is detected during remediation, fail closed and reconcile/re-resolve before continuing.

Treat remediation as an immutable candidate transition: starting candidate A plus authorised bounded remediation produces candidate B. Once bytes change, candidate-A-specific review and validation do not silently transfer to B. Bind the resulting validation and evidence to B's exact immutable identity.

Return a remediation record reconstructable as:
- governing finding/remediation authority;
- starting candidate identity;
- bounded implementation delta;
- resulting candidate identity;
- validation/evidence bound to the resulting candidate;
- any `REQUIRE OWNER / SEPARATE AUTHORITY` or `FORBID` boundaries encountered;
- any authorised action that could not execute because of a capability boundary;
- remaining boundaries and next governed state.

Classify evidence honestly as `STATIC`, `EXECUTED`, or `DURABLE` according to the Resolved Agent Run Context contract. Do not imply execution occurred where only static reasoning was performed. Clearly identify any finding that still requires a separate decision rather than pretending remediation is complete.

That remediation record is the workflow record, not a routed terminal state. When this workflow is invoked through the workflow router, return control to the router after recording it so the router can apply the effective continuation mode.

Preserve any required independent re-review boundary; do not present author-side remediation as fresh approval evidence. If this context changed the candidate and independent re-review is required, do not enter that review here. Treat the re-review as a hard fresh-context boundary and, when the durable target is sufficient for reconstruction, hand it off as `Next chat: /review <REVIEWED_CANDIDATE>`. That navigation is not review or merge authority.
```

## Inputs

- `<REVIEWED_CANDIDATE>` — the PR/branch/candidate plus the blocking review findings.

## What it does

Keeps remediation narrow, makes mutation authority explicit, classifies material actions before execution, makes review findings traceable to regression evidence, and prevents a repair cycle from becoming an unbounded redesign. It also preserves review-level diagnosis of materially related findings so an already-authorised invariant/boundary correction may be recognised as the minimum safe change instead of forcing repeated example-by-example patches. It binds remediation to starting candidate A and the resulting validation/evidence to candidate B, preventing candidate-specific review or validation from silently carrying across changed bytes.

When routed, it returns the remediation record to the governing workflow while preserving the mandatory fresh-context boundary for re-review of a candidate changed in this context.

## Boundaries / limitations

Use only where the expected correction is objectively bounded by existing requirements and authority. An invariant/boundary-level correction is permitted only when it is objectively determined by the governing contract/findings and already within the resolved remediation scope; materially new architecture, authority, security, product, or scope decisions should be resolved separately. Repeated findings never create redesign authority by themselves. Merge, release/tag, deployment, unrelated repository mutation, infrastructure/provider mutation, and settings/credential/secret mutation are not granted by this workflow merely because a capability exists.

Author-side remediation cannot substitute for fresh independent review when that gate is required. The action gateway is a workflow contract, not a new approval service, sandbox, or persisted policy object.

## Status

`tested`
