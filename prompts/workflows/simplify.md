# Simplify a governed design or workflow

## Purpose

Find the **smallest credible subtractive change** that reduces unnecessary complexity, cost or operator friction while retaining the behaviour, evidence and safeguards required by the governing objective.

## When to use

Use for read-only `/simplify [target]` when an implementation, workflow, configuration or proposal appears more complex than necessary. Unlike [Assess risk](assess-risk.md), this focuses on subtractive alternatives; unlike [Challenge assumptions](challenge-assumptions.md), it seeks a smaller working design. It is neither remediation nor approval.

## Prompt

```text
Simplify <TARGET> using authoritative current evidence. Read-only; do not implement changes.

1. BIND: Identify the exact current artefact/design, user goal, required behaviour, operating context, constraints and current evidence. Avoid reconstructing private history from guesses.
2. INVENTORY: Identify material components, dependencies, configuration, processes, permissions, approval loops and maintenance burden. Separate actual requirements from accidental complexity, duplication and speculative future-proofing.
3. SUBTRACT: Consider removing, consolidating or reusing existing elements first. Prefer one credible minimal alternative over several elaborate redesigns. Ask which layer, service, option, gate or abstraction can disappear without sacrificing the intended outcome.
4. PRESERVE: Explicitly retain applicable security, data integrity, authority, scope, independent review, rollback, verification and operational requirements. Never recommend bypassing a hard gate merely to reduce friction. Distinguish genuinely mandatory controls from discretionary ceremony.
5. TEST THE PROPOSAL: Compare baseline versus alternative on required behaviour, failure modes, effort, reversibility, cost and residual risk, using evidence rather than invented measurements. If there is no worthwhile reduction or evidence is insufficient, recommend NO CHANGE or INCONCLUSIVE.
6. REPORT: Give (a) the smallest proposed removal/consolidation, (b) why it is safe or what remains unproved, (c) expected benefit and trade-offs, (d) the least costly way to validate it and (e) whether separate approval or qualified review would be required for implementation.
7. STOP: Do not edit files, remove safeguards, merge, deploy, alter permissions, decide risk acceptance or claim independent review or measured savings without evidence. The recommendation creates no implementation authority.
```

## Inputs

- `<TARGET>` — the design, artefact, workflow, configuration or proposal to simplify; infer only when unambiguous.

## What it does

Provides a bounded, evidence-based recommendation for **less**, rather than adding a new framework or process. It can validly recommend retaining the current design. Subsequent implementation belongs to normal governed `/go` and required review.

## Boundaries / limitations

Read-only advisory output, not an execution, risk-acceptance or review gate. Preserve current exact-identity and repository-local requirements. Distinguish demonstrated simplification from estimated benefit and avoid unsupported claims of equivalent safety or performance.

## Status

`experimental`
