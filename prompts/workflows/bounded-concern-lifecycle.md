# Bounded concern lifecycle

## Purpose

Provide a bounded pre-review lifecycle for explicitly selected high-consequence governed work without claiming universal semantic completeness. Each frozen declared concern receives an externally owned finite closure contract and reconstructable evidence before genuinely fresh substantive review. Empirical convergence is measured across durable case-linked outcomes, including negative and non-convergent outcomes.

## When to use

Use only when current governing authority explicitly selects this lifecycle for a bounded generation or experiment. Do not infer applicability merely from task size, security terminology, or complexity.

This workflow is intentionally weaker than architecture closure. It does not establish an exhaustive concern universe, universal semantic primitive inventory, complete dependency graph, or proof that no new concern can exist. A newly discovered concern, scope/assurance movement, authority movement, or ambiguity involving those classes exits bounded correction and requires governing disposition.

## Prompt

```text
Run the bounded concern lifecycle for <GOVERNED_GENERATION> under <GOVERNING_OBJECTIVE>.

Before progression, bind an immutable empirical CASE_ID supplied by separately governed case-selection authority, the generation/predecessor identity, frozen objective and assurance claim, frozen CONCERN_REGISTER, and each externally owned CONCERN_CONTRACT identity.

Maintain a generation-lifetime append-only OUTCOME_RECORD from generation creation. Record material lifecycle events, correction consumption, admission attempts/failures, fresh reviews and classifications, governing-disposition events, effort/timing measurements, pending/terminal outcomes, and later governing disposition. Preserve negative, null, abandoned, decomposed, and non-convergent outcomes.

Use this lifecycle:

S0 SCOPE_DECLARED
→ S1 CONCERNS_FROZEN
→ S2 AUTHOR_CLOSURE
→ S3 PACKAGE_FROZEN
→ S4 ADMISSION_CHECK
→ S5 READY_FOR_FRESH_REVIEW
→ S6 FRESH_REVIEW_DISPOSITION
→ S7 TERMINAL

Bounded correction states are AC AUTHOR_CORRECTION and PC POST_REVIEW_CORRECTION. Governing exit is GD GOVERNING_DISPOSITION_REQUIRED.

AUTHOR_CORRECTION_ALLOWANCE=1
POST_REVIEW_CORRECTION_ALLOWANCE=1

Consume the applicable allowance before entering AC or PC. Allowances are generation-owned monotone values and are never restored by backward transitions, package regeneration, re-review, relabelling, issue recreation, repackaging, or candidate replacement.

Admission at S4 establishes REVIEW_PACKAGE_REPRODUCIBLE only. It is not correctness, architecture completeness, approval, or fresh review.

Fresh substantive review owns its blocking finding and routing classification. A finding is correction-eligible only when it is unambiguously wholly inside the frozen objective/assurance, frozen concern register, applicable frozen concern-contract correction boundary, and existing authority boundary. If it plausibly overlaps NEW_CONCERN, SCOPE_OR_ASSURANCE_CHANGE, or AUTHORITY_CHANGE, or correction eligibility is ambiguous, route fail-closed to GD. Author evidence may inform but cannot downgrade that route.

Every material correction invalidates the old REVIEW_PACKAGE. If AC or PC mutates the exact candidate or any input on which declared concern closure can depend, invalidate every frozen declared concern result, return to S2, rerun every frozen concern, then freeze a new package and independently repeat S4. Do not retain pre-correction concern evidence with a materially corrected candidate.

A correction confined solely to package representation/reconstruction may avoid semantic concern reruns only when the exact candidate and all concern-closure inputs and outputs are unchanged. It still requires a new package identity/integrity witness and independent S4 admission.

An eligible post-review correction consumes P before PC, returns through S2/S3/S4, and requires another genuinely fresh substantive review. If the applicable correction allowance is exhausted, route GD.

Create and bind OUTCOME_RECORD when the generation is created, not only at terminal S7. Append the GD event before active progression stops. A later governing-authority decision appends/finalises the disposition and never erases predecessor outcome.

CASE_ID is established only by separately governed pilot case-selection/baseline authority. A successor generation, decomposition branch, repackaged generation, or authorised continuation arising from the same governed experimental case inherits the CASE_ID and predecessor/disposition linkage. Generation naming, issue recreation, branching, repackaging, candidate replacement, or ordinary governing disposition cannot create a new CASE_ID. A genuinely new CASE_ID requires separately authorised case selection. If continuity inside an already-started case is ambiguous, preserve continuity until pilot authority explicitly establishes a new case; this is accounting conservatism, not Promptbook ownership of domain-semantic sameness.

Contract owner/version movement, objective/assurance movement, and authority movement route GD rather than bounded correction. NEW_CONCERN also routes GD. A successor after GD requires a durable predecessor governing disposition before it can count as empirical continuation.

Keep concern-contract semantic ownership external. Promptbook coordinates lifecycle routing, currentness, package reconstruction, outcome accounting, and authority separation only.

Do not infer implementation, pull-request, merge, pilot, consumer-mutation, normative-adoption, risk-acceptance, or concern-specific engineering authority from lifecycle progression.
```

## Inputs

- `<GOVERNED_GENERATION>` — the exact bounded generation selected by current authority.
- `<GOVERNING_OBJECTIVE>` — the frozen bounded process-assurance objective and authority constraints.

## What it does

Provides finite concern-specific closure packaging, conservative correction currentness, deterministic fail-closed routing, durable negative-outcome accounting, and empirical lineage continuity while preserving genuinely fresh substantive review and external concern ownership.

It is designed for empirical convergence measurement rather than self-certification. Repeated novel concerns remain visible under one case lineage instead of being hidden by generation resets.

## Boundaries / limitations

This workflow does not claim an exhaustive concern set, universal primitive universe, dependency completeness, domain-semantic truth, universal convergence, or replacement for architecture closure when a strong closure-ready claim is actually required. It does not make the lifecycle portfolio-wide mandatory and does not add a public command.

The lifecycle itself creates no implementation, PR, merge, release, deployment, pilot, consumer-repository mutation, normative-adoption, credential, production, risk-acceptance, or external-effect authority. Concern contracts and case-selection semantics remain owned by their separately governed authorities.

## Status

`experimental`
