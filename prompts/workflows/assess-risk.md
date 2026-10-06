# Assess risk

Use this workflow when the operator asks what material risk exists around a bounded state, action, proposal, or decision and what dispositions are legitimately available.

This is a read-only reasoning workflow. It does not accept risk, establish a decision, satisfy a violated invariant, mutate governed state, or create execution authority.

## Purpose

Produce a structured, evidence-bound assessment of material risk while keeping risk truth separate from owner acceptance and from invariant satisfaction.

## Inputs and evidence

Identify the exact subject of the assessment and reconstruct only the evidence needed to assess it. Preserve material target identity, provenance, scope, currentness, uncertainty, and governing hard requirements.

If decision-critical evidence is missing or stale, say so rather than filling the gap with assumptions.

## Operation

1. Identify material hazards or failure modes supported by the evidence.
2. Establish exposure or reachability when the evidence permits it.
3. Characterise material consequences without inventing numeric likelihood or confidence.
4. Identify existing controls and mitigations and what they actually establish.
5. Identify residual risk and material uncertainty.
6. Distinguish non-waivable requirements or violated invariants from owner-disposable residual risk.
7. Recommend legitimate dispositions only where justified.

Preserve these distinctions:

```text
risk assessment != risk acceptance
risk acceptance != invariant satisfaction
```

An owner's willingness to proceed may be relevant to a disposable residual risk. It cannot make a violated hard requirement true.

## Output

Report, proportionately:

```text
RISK
EVIDENCE / BASIS
CONTROLS
RESIDUAL RISK / UNCERTAINTY
DISPOSABILITY / HARD BOUNDARY
RECOMMENDATION
```

Use observations, interpretations, recommendations and results distinctly enough that a later consumer can tell what the evidence established and what was judgement.

## Authority boundary

The workflow may read evidence and produce an assessment artefact. It carries no authority to accept risk, establish an owner decision, persist a decision, remediate a defect, mutate governed state, cause an external effect, delegate authority, or satisfy a review/approval gate.

A separately authorised decision mechanism must record any owner risk acceptance that matters to later governed work.

## Terminal behaviour

A valid result may be `INDETERMINATE`, `BLOCKED_BY_MISSING_INPUT`, `STALE_INPUT`, or `NO_CHANGE_RECOMMENDED`.

Do not manufacture a risk rating, recommendation, acceptance, or coherent disposition merely to complete the workflow.
