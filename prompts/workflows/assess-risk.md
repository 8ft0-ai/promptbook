# Assess risk

## Purpose

Produce a structured, evidence-bound assessment of material risk while keeping risk truth separate from owner acceptance and invariant satisfaction.

## When to use

Use when the operator asks what material risk exists around a bounded state, action, proposal, or decision and what dispositions are legitimately available.

## Prompt

```text
Assess risk for <TARGET> using current authoritative evidence.

Bind the exact subject and preserve material target identity, provenance, scope, currentness, uncertainty, and governing hard requirements. If decision-critical evidence is missing or stale, say so rather than filling the gap with assumptions.

Identify material hazards or failure modes supported by evidence. Establish exposure or reachability when supportable. Characterise material consequences without inventing numeric likelihood or confidence. Identify controls and mitigations and what they actually establish, then residual risk and uncertainty.

Distinguish non-waivable requirements or violated invariants from owner-disposable residual risk. Preserve:

risk assessment != risk acceptance
risk acceptance != invariant satisfaction

An owner's willingness to proceed cannot make a violated hard requirement true.

Recommend legitimate dispositions only where justified. Report proportionately:

RISK
EVIDENCE / BASIS
CONTROLS
RESIDUAL RISK / UNCERTAINTY
DISPOSABILITY / HARD BOUNDARY
RECOMMENDATION

Keep observations, interpretations, recommendations and results distinguishable enough for later consumers to know what evidence established.

This is read-only reasoning. There is no authority to accept risk, establish an owner decision, persist a decision, remediate a defect, mutate governed state, cause an external effect, delegate authority, or satisfy a review/approval gate. Any material owner acceptance requires a separately authorised decision mechanism.

A valid result may be INDETERMINATE, BLOCKED_BY_MISSING_INPUT, STALE_INPUT, or NO_CHANGE_RECOMMENDED. Do not manufacture a rating, recommendation, acceptance, or coherent disposition merely to complete the assessment.
```

## Inputs

- `<TARGET>` — the bounded state, action, proposal, or decision whose material risk should be assessed.

## What it does

Separates evidence-backed risk assessment from risk acceptance and hard-requirement satisfaction, while producing a compact assessment that preserves uncertainty and legitimate disposition boundaries.

## Boundaries / limitations

This workflow is read-only. It cannot accept risk, establish decisions, satisfy violated invariants, remediate findings, mutate governed state, cause external effects, delegate authority, or satisfy qualified review/approval gates. Insufficient or stale evidence may legitimately produce an indeterminate result.

## Status

`experimental`
