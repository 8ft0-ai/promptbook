# Challenge assumptions

Use this workflow when the operator wants an adversarial examination of a proposition, design, assumption set, governing contract, or proposed course.

This is read-only adversarial reasoning. It is deliberately distinct from qualified review: challenge may question the adequacy of the governing contract itself, but cannot approve a candidate or satisfy a fresh-review gate.

## Purpose

Actively seek material counterexamples, omitted dimensions, unsupported inferences, and failure paths before the operator relies on the challenged proposition or course.

## Inputs and evidence

Bind the exact target being challenged and recover the material evidence/current state needed to test it. Preserve explicit exact-target assertions.

If target identity or decision-critical evidence is stale or ambiguous, surface that condition rather than silently substituting another target.

## Operation

1. State the target and the material assumptions being tested.
2. Seek counterexamples and hostile-but-valid cases proportionately to the target.
3. Test whether the evidence supports the claimed conclusion.
4. Look for omitted state, identity, authority, lifecycle, recovery, scope, or equivalence dimensions when materially applicable.
5. Distinguish a flaw in the candidate/proposal from a flaw or omission in the governing contract.
6. Record assumptions that survive the challenge and material uncertainty that remains.
7. Recommend further investigation or change only when justified.

Challenge depth should remain proportional. Do not turn a simple proposition into a universal architecture exercise without evidence that broader modelling is necessary.

## Output

Report, proportionately:

```text
TARGET
ASSUMPTIONS TESTED
MATERIAL CHALLENGES / COUNTEREXAMPLES
SURVIVING ASSUMPTIONS
UNCERTAINTY
RECOMMENDATION
```

## Authority boundary

Challenge may read evidence and produce adversarial findings. It cannot approve or reject a qualified gate, amend a governing contract, establish owner decisions, remediate findings, mutate governed state, cause external effects, persist authority, or delegate authority.

A result of `NO_MATERIAL_CHALLENGE_FOUND` is not `APPROVED` and is not review evidence.

## Terminal behaviour

A valid result may be `NO_MATERIAL_CHALLENGE_FOUND`, `INDETERMINATE`, `BLOCKED_BY_MISSING_INPUT`, `STALE_INPUT`, or `NO_CHANGE_RECOMMENDED`.

Do not invent a blocker merely to demonstrate adversarial depth.
