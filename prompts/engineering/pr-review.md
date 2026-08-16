# Review a pull request

## Purpose

Perform a substantive engineering review of a pull request against its intended outcome and current evidence.

## When to use

Use for code, configuration, documentation, or workflow changes when the reviewer can inspect the complete candidate and its linked requirements.

## Prompt

```text
Act as the principal engineer reviewing <PULL_REQUEST>.

Inspect the complete current diff, linked issue/specification, accepted design or implementation plan when available, unresolved review threads, relevant repository conventions, and current CI/test/validation results.

Review for correctness, completeness, requirement alignment, unintended scope expansion, regressions, edge cases, security and operational risk, maintainability, compatibility, test quality, documentation, migration, and rollback implications.

Specifically verify that:
- the change delivers the promised outcome rather than merely changing code;
- unrelated refactoring or speculative improvements have not entered the candidate;
- validation is sufficient for the risks introduced;
- tests prove the required behaviour and important negative paths;
- tests, assertions, thresholds, or checks were not weakened or bypassed;
- automated success is not masking an unresolved functional problem.

Distinguish blockers from non-blocking observations, questions, optional suggestions, and follow-up ideas. Prefer concrete, evidence-backed findings over stylistic preference.

Conclude with exactly one disposition: APPROVED, CHANGES REQUIRED, or CANNOT ASSESS. For CHANGES REQUIRED, list blocking findings only after the concise rationale.
```

## Inputs

- `<PULL_REQUEST>` — the PR URL/number and repository context if it is not otherwise available.

## What it does

Shifts review from line-by-line style commentary toward outcome, contract, risk, and proof while still permitting precise findings where they matter.

## Boundaries / limitations

A useful review requires access to the actual candidate and decision-critical evidence. Do not claim independent review if the context substantially authored the candidate or inherited its substantive conclusion.

## Status

`tested`
