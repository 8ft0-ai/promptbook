# Stateful invariant analysis

## Purpose

Reconstruct the complete applicable invariant or lifecycle model for a materially stateful behavioural problem before another remediation attempt, without creating mutation or redesign authority.

## When to use

Use proportionately when the target is materially stateful, lifecycle-sensitive, cross-component, concurrency-sensitive, retry/recovery-sensitive, cache/inference-sensitive, or when the workflow router has established the mandatory repeated-review escalation rule.

Do not impose this workflow on a simple local defect whose correct behaviour and bounded correction are already safely determined.

## Prompt

```text
Analyse <ANALYSIS_TARGET> against <GOVERNING_CONTRACT> as a read-only stateful/invariant analysis.

Reconstruct current authoritative state from production code, governing requirements, current candidate identity, durable review/remediation evidence and repository-local instructions. Do not treat a remediation narrative, prior summary, passing tests or the number of findings as proof of the underlying invariant.

First determine whether stateful/invariant analysis is materially applicable. It is applicable when correctness depends on a state machine or lifecycle, cross-component coordination, concurrent or in-flight work, retries or recovery, cache/expiry behaviour, positive-versus-negative inference, partial success, stale completion, or an equivalent behavioural mechanism. It is also mandatory when the workflow router has established the repeated-review escalation trigger.

When applicable:

1. Reconstruct the current state machine or lifecycle from production integration paths, not only helper abstractions or tests.
2. State the authoritative invariants before proposing any correction.
3. Distinguish positive observation from negative inference and identify what evidence is sufficient for each.
4. Enumerate the applicable success, failure, partial-success, stale-completion, interruption, retry, prolonged-failure and recovery paths.
5. Identify which events/transitions are authoritative, which are non-authoritative or stale, and which must be ignored.
6. Search across the decision-critical implementation surface for duplicate/raw implementations of the same semantic rule, including predicates, expiry/absence inference, retry gates and lifecycle transitions.
7. Identify production integration paths that can bypass or disagree with a shared policy/helper.
8. Where the evidence permits, distinguish a pre-existing escape from behaviour introduced by the intervening remediation.
9. Determine whether the existing abstraction remains sound. Recurrence or finding count alone never proves an abstraction failure.
10. Produce the smallest bounded invariant-level remediation plan that follows from the governing contract and current evidence. If the necessary correction requires materially new product, architecture, security, scope, owner or other authority, expose that boundary instead of manufacturing remediation authority.

When this analysis is mandatory because two materially related substantive review rounds failed, bind the analysis record to:
- the current exact candidate;
- the R1 and R2 review identities and dispositions;
- the evidence-based materially related blocker set or behavioural/invariant domain;
- the current governing contract.

The repeated-review trigger is process-driven, not conclusion-driven. It requires analysis before another remediation attempt; it does not establish that redesign is needed, does not widen `/fix`, and creates no mutation, approval, merge, release, deployment, credential, production or other consequential authority.

If the candidate or governing contract moves materially before remediation, the candidate-bound analysis must be refreshed or invalidated under the normal Promptbook freshness/state rules. Once an authorised remediation based on the current analysis produces a new exact candidate, this escalation requirement is satisfied for that remediation attempt; the next genuinely fresh substantive review starts a new failure sequence.

Return a concise analysis record containing:
- applicability and reason;
- exact candidate and governing contract;
- reconstructed state/lifecycle model and authoritative invariants;
- positive-observation versus negative-inference rules;
- applicable failure/retry/recovery and stale/in-flight behaviours;
- duplicate/raw semantic implementations and production bypass paths;
- R1/R2 binding when mandatory escalation applies;
- bounded remediation plan;
- required validation and explicitly untested surface;
- any product/architecture/security/scope/authority boundary.

This record is read-only analysis/synthesis evidence. Return control to the workflow router after producing it. Do not mutate source, create a candidate, approve the target, or treat completion of analysis as implementation authority.
```

## Inputs

- `<ANALYSIS_TARGET>` — the exact candidate, behavioural area, issue, PR, or other stateful target to analyse.
- `<GOVERNING_CONTRACT>` — the current issue, design, acceptance criteria, policy, review records, or other requirements that determine intended behaviour.

## What it does

This workflow forces stateful remediation to begin from the governing invariant rather than from the latest reported symptom while keeping analysis separate from mutation authority.

For example, consider a wireless observation interface whose history view pauses scanning and requests a fresh scan when observation resumes. A complete analysis reconstructs the lifecycle around active observation, pause, awaiting a fresh scan, a fresh scan in progress, and resumed observation. It checks that scan completeness is established only when all required scan components succeed; that absence or disappearance is inferred only from a complete authoritative observation; that a stale scan completing after the pause cannot release reacquisition; that repeated failed scans remain in the retry/recovery state rather than inventing absence; and that duplicate expiry or inference predicates elsewhere in production cannot bypass the shared policy. Passing helper tests for one transition would not by itself establish those invariants across the integration surface.

## Boundaries / limitations

This workflow is read-only. It does not create repository-mutation, remediation, architecture, product, security, scope, approval, review, merge, release, deployment, credential or production authority. The mandatory repeated-review trigger requires deeper analysis but does not decide in advance that an abstraction is unsound. A simple/local defect should retain the shorter existing path when stateful analysis is not materially applicable.

Fresh independent substantive review remains owned by the ordinary Promptbook review workflow. This analysis must not be represented as fresh approval evidence, and an executable runtime skill may assist analysis without becoming the normative source of these semantics.

## Status

`tested`
