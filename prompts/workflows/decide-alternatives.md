# Decide among alternatives

## Purpose

Provide evidence-based decision support between materially different alternatives without exercising owner-reserved authority. Distinguish a defensible recommendation from an actual decision.

## When to use

Use for `/decide [target]` when a bounded choice among alternatives is required. Unlike `/assess`, this compares options rather than asking whether an objective remains worthwhile; unlike `/triage`, it evaluates courses rather than ranking problems. Use `/risk` for residual-risk characterisation; `/review` for qualified independent candidate assessment. This command is not an approval gate.

## Prompt

```text
Advise on <TARGET> as read-only decision support.

1. BIND: Establish the decision question, original goal, accountable decision owner, candidate alternatives (including status quo or defer where relevant), hard constraints, exact evidence sources, freshness and scope. Do not invent authority, options, requirements or deadlines.
2. CRITERIA: State explicit, decision-relevant criteria and mandatory disqualifiers before judging options. Include goal fit, expected benefit, cost/effort, risk and reversibility where material. Distinguish a hard constraint from a weighted preference; do not assign numerical weights without a justified basis.
3. COMPARE: Evaluate each viable alternative against the same criteria using current evidence. Identify trade-offs, dependency/implementation assumptions, upside, downside, uncertainty and counter-evidence. Mark unknowns rather than treating absence of evidence as zero risk or a poor score.
4. RECOMMEND one: PREFER <OPTION> when evidence and constraints justify a defensible choice; DEFER when material evidence or a time-sensitive dependency must be resolved; NO DECISION when alternatives, requirements, authority or evidence are too ambiguous for a justified recommendation. A recommendation does not bind the owner. If no option satisfies a mandatory constraint, say so without selecting an ineligible winner.
5. REPORT: Present the decision question, alternatives, criteria/constraints, concise comparative evidence, decisive trade-offs, assumptions, confidence/uncertainty, recommendation and rationale, plus the smallest useful evidence check or next owner action. State what would change the recommendation.
6. STOP: Read-only analysis. Do not make or persist an owner-reserved decision, approve or reject a candidate as an independent reviewer, accept risk, waive hard requirements, remediate, create or close issues/PRs, merge, deploy, spend, trade, alter permissions or trigger further work. Subsequent action requires its own authority and workflow.
```

## Inputs

- `<TARGET>` — a bounded decision or set of alternatives; infer only when unambiguous.
- `<OPTION>` — the selected alternative's name in a conditional recommendation; never an automatically approved choice.
- Governing requirements, current evidence, constraints, preferences and decision ownership; explicitly note unavailable inputs.

## What it does

Produces an evidence-linked comparison with a defensible preference, defer or no-decision outcome. Reuses authoritative sources and keeps choices with their legitimate owner.

## Boundaries / limitations

No decision, risk-acceptance, mutation, approval, independent-review or execution authority. Qualitative confidence is not measured probability. Static tests do not prove live behaviour.

## Status

`experimental`
