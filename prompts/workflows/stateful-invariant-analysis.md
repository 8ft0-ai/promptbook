# Stateful invariant analysis

## Purpose

Reconstruct the complete applicable invariant or lifecycle model for a materially stateful behavioural problem before another remediation attempt, and perform explicit architecture reconsideration when a prior invariant-closure claim has been falsified, without creating mutation or redesign authority.

## When to use

Use proportionately when the target is materially stateful, lifecycle-sensitive, cross-component, concurrency-sensitive, retry/recovery-sensitive, cache/inference-sensitive, when the workflow router has established the mandatory repeated-review escalation rule, or when durable evidence establishes post-closure same-family recurrence and `ARCHITECTURE_RECONSIDERATION_REQUIRED`.

Also use it when the router establishes `ADJACENT_MODEL_OMISSION`: a fresh blocker may be a distinct defect family yet still prove that the immediately preceding remediation omitted a necessary dimension of the shared state, ownership, identity/currentness, transition, recovery, equivalence or effect model. That classification is evidence-based; adjacency or finding count alone is insufficient.

Do not impose this workflow on a simple local defect whose correct behaviour and bounded correction are already safely determined.

## Prompt

```text
Analyse <ANALYSIS_TARGET> against <GOVERNING_CONTRACT> as a read-only stateful/invariant analysis.

Reconstruct current authoritative state from production code, governing requirements, current candidate identity, durable review/remediation evidence and repository-local instructions. Do not treat a remediation narrative, prior summary, passing tests or the number of findings as proof of the underlying invariant.

First determine whether stateful/invariant analysis is materially applicable. It is applicable when correctness depends on a state machine or lifecycle, cross-component coordination, concurrent or in-flight work, retries or recovery, cache/expiry behaviour, positive-versus-negative inference, partial success, stale completion, or an equivalent behavioural mechanism. It is also mandatory when the workflow router has established the repeated-review escalation trigger or post-closure same-family recurrence requiring architecture reconsideration.

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

When analysis is mandatory because `ADJACENT_MODEL_OMISSION` was established, do not stop at the latest counterexample. Reconstruct the complete relevant semantic-owner/state/currentness model and derive a bounded consistency matrix that covers authoritative state dimensions, ownership, supersession/currentness, global transitions, adversarial interleavings, failure/recovery and positive reachability. For multi-owner intent/currentness problems, retain outputs equivalent to `CANONICAL_MULTI_OWNER_INTENT_MODEL`, `DESIRED_STATE_MODEL`, `CURRENTNESS_AND_SUPERSESSION_MODEL`, `GLOBAL_TRANSITION_MATRIX`, `ADVERSARIAL_INTERLEAVING_MATRIX` and `POSITIVE_REACHABILITY_CHECK`; these names are illustrative rather than a mandatory schema. The resulting plan must be one encompassing model-driven remediation, not a list of patches for the reported reproductions.

If this adjacent-model analysis concerns a materially security-, authority-, identity- or recovery-sensitive architecture that is being treated as closure-ready, invoke [Architecture closure analysis](architecture-closure-analysis.md) within the same bounded read-only analysis authority so the independently derived source/obligation universe, primitive coverage and global closure checks constrain the remediation model. Do not infer `CLOSURE_METHOD_FALSIFIED` unless the stronger existing falsification conditions are independently established.

When this analysis is mandatory because two materially related substantive review rounds failed, bind the analysis record to:
- the current exact candidate;
- the R1 and R2 review identities and dispositions;
- the evidence-based materially related blocker set or behavioural/invariant domain;
- the current governing contract.

The repeated-review trigger is process-driven, not conclusion-driven. It requires analysis before another remediation attempt; it does not establish that redesign is needed, does not widen `/fix`, and creates no mutation, approval, merge, release, deployment, credential, production or other consequential authority.

When this analysis is required because a materially same-family blocker recurred after closure and the router has established `ARCHITECTURE_RECONSIDERATION_REQUIRED`, treat it as explicit architecture reconsideration. Before performing that reconsideration, require and bind a separately governed authority source that specifically permits this bounded read-only architecture assessment; recurrence and `ARCHITECTURE_RECONSIDERATION_REQUIRED` do not themselves supply that authority. Bind the record to the prior invariant-closure lineage, including the earlier R1/R2 sequence, the closure analysis, the analysis-backed remediation/candidate, the closure-challenge review where one exists, the recurrence review, the materially shared defect family/invariant, the current governing contract and the reconsideration-authority source. Independently assess whether the representation or implementation architecture is responsible for the instability; recurrence alone does not prove that it is. Distinguish genuine post-closure same-family recurrence from an intervening regression, a new family, an unrelated domain, a newly applicable requirement or a materially out-of-boundary change.

Do not enter this architecture-reconsideration branch merely because a recurrence is also a structural falsification. If fresh review classifies the recurrence as `EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION` of a prior `APPROVED_FOR_CANDIDATE_PROJECTION` closure artefact, that structural classification takes precedence and routes first to `GOVERNING_DISPOSITION_REQUIRED`. The governing disposition owns the required `COMPLEXITY_DISPOSITION_REQUIRED` simplification/decomposition decision and may separately authorise architecture reconsideration or a successor generation afterwards. Only if that later disposition establishes a new `ARCHITECTURE_RECONSIDERATION_REQUIRED` boundary does this workflow enter the reconsideration branch. A local regression inside a still-sound represented model does not satisfy this structural trigger.

If that authorised architecture reconsideration needs to establish architecture closure before a proposal can be treated as closure-ready, do not infer completeness from the candidate's own prose, object registry, transition table or known blocker list. Invoke [Architecture closure analysis](architecture-closure-analysis.md) within the same one-shot read-only reconsideration authority. Require its independently derived closed source/obligation universe, total source → primitive coverage, closed primitive classification, five closure inventories, extensional consequence-ownership proof and remaining global closure checks before returning an architecture-closure claim. The architecture-closure result is part of the architecture assessment; it does not create additional mutation authority.

This reconsideration route is the reactive architecture-governance branch. The workflow router may also enter [Architecture closure analysis](architecture-closure-analysis.md) proactively before a new materially high-risk architecture is authored/published with a strong closure-ready completeness claim. Do not manufacture repeated-review, closure-falsification or architecture-reconsideration lineage merely because that proactive publication gate applies; both entry paths share the same closure method but retain their distinct authority and lifecycle semantics.

If the candidate or governing contract moves materially before remediation, candidate-bound analysis must be refreshed or invalidated under the normal Promptbook freshness/state rules. After ordinary invariant-closure analysis, authorised analysis-backed remediation may satisfy the initial R1/R2 analysis gate for that remediation attempt, but the historical `INVARIANT_CLOSURE_ATTEMPTED(X)` lineage remains reconstructable. A subsequent fresh review may establish `CLOSURE_SURVIVED_THIS_REVIEW` without erasing that lineage, or may establish closure falsification/post-closure recurrence and the architecture-reconsideration boundary.

On completion, retain the architecture result as `ARCHITECTURE_RECONSIDERATION_COMPLETED` (or a reconstructable equivalent) bound to the recurrence review, prior closure lineage, exact candidate, governing contract and reconsideration-authority source. That current record satisfies the architecture-reconsideration analysis gate for those exact bindings; do not repeat or re-enter the reconsideration while the record remains current. When architecture closure was required, also bind the resulting architecture-closure record/artefact and its `ARCHITECTURE_CLOSURE_READY` or `ARCHITECTURE_CLOSURE_NOT_READY` disposition. `ARCHITECTURE_CLOSURE_READY` satisfies the author-side closure-analysis gate only and establishes `CLOSURE_REVIEW_REQUIRED` for that exact artefact; it does not make replacement-candidate authoring eligible. Candidate projection stays blocked until a genuinely fresh closure review returns `APPROVED_FOR_CANDIDATE_PROJECTION` for the exact current closure artefact. Material movement of any decision-critical binding invalidates or requires refresh of the affected record under the normal freshness/state rules.

A later fresh substantive review may independently establish `CLOSURE_METHOD_FALSIFIED` if it finds an applicable `UNMODELLED_DECISION_CRITICAL_PRIMITIVE` that should have been represented in the closure universe. That is not authority to rerun this reconsideration or to create another closure generation. It routes the current strong-closure generation to `GOVERNING_DISPOSITION_REQUIRED`. A successor may enter [Architecture closure analysis](architecture-closure-analysis.md) only after a separate governing disposition explicitly authorises a new strong-closure generation and preserves the terminal predecessor evidence.

Architecture reconsideration is read-only analysis/decision evidence. Its completion must not silently become another analysis-backed `/fix`; authority to perform the read-only architecture reconsideration is not remediation or design-mutation authority. Return the architecture assessment, the smallest defensible next proposal and any separate decision/remediation authority required before mutation.

Return a concise analysis record containing:
- applicability and reason;
- exact candidate and governing contract;
- reconstructed state/lifecycle model and authoritative invariants;
- any required `COMPLEXITY_DISPOSITION_REQUIRED` result and its `SIMPLIFY_OR_DECOMPOSE` / `ADDITIONAL_MODEL_COMPLEXITY_JUSTIFIED` disposition;
- positive-observation versus negative-inference rules;
- applicable failure/retry/recovery and stale/in-flight behaviours;
- duplicate/raw semantic implementations and production bypass paths;
- R1/R2 binding when initial mandatory escalation applies;
- prior closure-lineage binding and architecture assessment when post-closure recurrence applies;
- bounded remediation plan for an ordinary closure analysis, or smallest defensible next proposal for architecture reconsideration;
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
