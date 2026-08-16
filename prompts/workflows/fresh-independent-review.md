# Fresh independent review

## Purpose

Review a candidate, design, or evidence record from a genuinely fresh context without inheriting the previous session's substantive conclusion.

## When to use

Use when independence is part of the quality or governance boundary: substantive PR review, design review, evidence adjudication, close-out review, or another decision where author-side reasoning should not be treated as approval evidence.

## Prompt

```text
Conduct a fresh independent review of <REVIEW_TARGET> against <GOVERNING_CONTRACT>.

Treat prior summaries, recommendations, and conclusions only as navigation aids. Reconstruct the material authoritative state directly from the actual candidate and decision-critical evidence. Establish the current identities, revisions, checks, review state, and governing requirements needed for this decision.

Reach the substantive conclusion from freshly inspected evidence. Do not inherit the prior session's approval/rejection reasoning, do not weaken the governing contract to obtain approval, and distinguish blocking findings from non-blocking observations.

If expected state changed, determine what changed and whether the review remains safely decidable; do not fail mechanically merely because an identity moved when the governing contract permits reconciliation.

Return exactly one clear disposition appropriate to the gate (for example APPROVED / CHANGES REQUIRED), followed by concise decisive rationale. For a negative disposition, identify only material blockers that must be resolved.
```

## Inputs

- `<REVIEW_TARGET>` — the exact PR, commit, design, evidence record, or other candidate to assess.
- `<GOVERNING_CONTRACT>` — the issue, specification, acceptance criteria, design, policy, or explicit review contract.

## What it does

Creates an information boundary between authoring and adjudication and forces the reviewer to inspect the real evidence rather than merely validating a handover summary.

## Boundaries / limitations

Freshness is a property of prior information, not a prompt incantation. A context that substantially authored the candidate or already saw the expected answer cannot become independent merely by being told to forget it.

## Status

`tested`
