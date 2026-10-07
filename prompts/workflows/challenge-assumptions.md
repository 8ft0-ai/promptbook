# Challenge assumptions

## Purpose

Adversarially test a proposition, design, assumption set, governing contract, or proposed course for material counterexamples, omitted dimensions, and unsupported inferences.

## When to use

Use when the operator wants to question whether the current model, evidence, contract, or proposed course is actually robust, including when the adequacy of the governing contract itself should be open to challenge.

## Prompt

```text
Challenge <TARGET> adversarially using current material evidence.

bind the exact target and preserve explicit exact-target assertions and evidence provenance. if target identity, provenance, or decision-critical evidence is stale or ambiguous, surface that condition rather than silently substituting another target.

State the material assumptions being tested. Seek proportionate counterexamples and hostile-but-valid cases. Test whether the evidence supports the claimed conclusion. Look for omitted state, identity, authority, lifecycle, recovery, scope, or equivalence dimensions when materially applicable.

Distinguish a flaw in the candidate or proposal from a flaw or omission in the governing contract. Record assumptions that survive the challenge and material uncertainty that remains. Recommend further investigation or change only when justified. Do not turn a simple proposition into a universal architecture exercise without evidence that broader modelling is necessary.

Report proportionately:

TARGET
ASSUMPTIONS TESTED
MATERIAL CHALLENGES / COUNTEREXAMPLES
SURVIVING ASSUMPTIONS
UNCERTAINTY
RECOMMENDATION

This is read-only adversarial reasoning. It cannot approve or reject a qualified gate, amend a governing contract, establish owner decisions, remediate findings, mutate governed state, cause external effects, persist authority, or delegate authority.

A valid result may be NO_MATERIAL_CHALLENGE_FOUND, INDETERMINATE, BLOCKED_BY_MISSING_INPUT, STALE_INPUT, or NO_CHANGE_RECOMMENDED. NO_MATERIAL_CHALLENGE_FOUND is not APPROVED and is not review evidence. Do not invent a blocker merely to demonstrate adversarial depth.
```

## Inputs

- `<TARGET>` — the exact proposition, design, assumption set, governing contract, or proposed course to challenge.

## What it does

Tests assumptions and governing models more broadly than contract-bound review while preserving the critical distinction between adversarial reasoning and qualified approval evidence.

## Boundaries / limitations

This workflow is read-only. It cannot approve a candidate, satisfy a qualified review gate, amend the contract it challenges, establish decisions, remediate findings, mutate governed state, cause external effects, or create/delegate authority.

## Status

`experimental`
