# Assess objective alignment

## Purpose

Determine whether ongoing work still advances its governing objective, or whether direction drift, expanding scope, diminishing returns or opportunity cost warrant a change. This is a read-only decision aid, not a new lifecycle gate.

## When to use

Use for `/assess [target]` when the question is "are we still pursuing the right goal, by a worthwhile route?" Unlike `/status`, this judges alignment and value rather than reporting current state; unlike `/reflect`, it need not be retrospective; unlike `/challenge`, it need not be adversarial. Use `/verify` for observed delivery evidence, `/simplify` for a specifically subtractive design proposal, and `/decide` only if separately adopted later.

## Prompt

```text
Assess <TARGET> without changing its scope, artefacts, state or authority.

1. BIND: Reconstruct the original user objective, intended benefit, success criteria, constraints and present governing state from available authoritative evidence. Distinguish original requirements, later authorised changes and assumptions; do not invent a baseline when records are missing.
2. COMPARE: Set the original goal beside what work is currently doing and delivering. Check for direction drift, unnecessary scope expansion, diminishing returns, unproven detours, recurring friction, opportunity cost and alternative routes. Distinguish evidence of real misalignment from ordinary progress, exploration or justified changes.
3. WEIGH: Assess whether the remaining effort and risk are proportionate to expected value. Make contrary evidence and uncertainty visible; do not infer failure merely from slow progress or complexity. A justified NO DRIFT finding is valid.
4. RECOMMEND one: CONTINUE (goal aligned and worthwhile), CORRECT COURSE (goal still sound, route misaligned), SIMPLIFY (remove disproportionate effort or scope without losing essentials), STOP (objective no longer justified on available evidence), or INCONCLUSIVE (missing, stale or conflicting decision-critical evidence). For an owner-reserved choice, recommend rather than decide.
5. REPORT: State the original objective, observed current direction, alignment finding (NO DRIFT / DRIFT / INCONCLUSIVE), decisive evidence and limitations, one recommended disposition with rationale, and the smallest useful next action or evidence check. Explicitly say when no change is warranted.
6. STOP: Read-only assessment only. Do not remediate, close an issue, edit files, author a PR, merge, deploy, spend, alter permissions, accept risk or claim independent review. Recommendation labels are not `/go` terminal states or lifecycle approvals; further actions require their own applicable authority and workflow.
```

## Inputs

- `<TARGET>` — objective, issue, project or bounded workstream; infer only when the current target is unambiguous.
- Current authoritative goal and progress evidence; absent evidence must be reported, not fabricated.

## What it does

Produces one concise, evidence-linked alignment finding and a justified continuation recommendation, including defensible no-drift and inconclusive results. Reuses the same governing objective/evidence sources as the [Workflow router](README.md), without changing its progression decisions.

## Boundaries / limitations

No mutation or implementation authority. Does not replace `/status`, `/verify`, `/reflect`, `/challenge`, `/review`, a formal decision or an owner-reserved approval. Static source-contract tests cannot prove live agent behaviour.

## Status

`experimental`
