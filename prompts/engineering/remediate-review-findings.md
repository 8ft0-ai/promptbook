# Remediate review findings

## Purpose

Turn blocking review findings into the minimum safe correction without reopening unrelated design work, using explicit reconstructable mutation authority rather than tool availability or remembered conversation state.

## When to use

Use after a substantive review has identified concrete defects and the existing task or design already determines the intended behaviour closely enough to repair them.

## Prompt

```text
Remediate the blocking findings on <REVIEWED_CANDIDATE>.

First re-read the exact findings, the governing task/design, the current candidate, applicable repository instructions, and current authority. Before substantive mutation, resolve the `/fix` Resolved Agent Run Context defined by `prompts/workflows/resolved-agent-run-context.md` from current authoritative inputs rather than conversation memory.

When review-response synthesis has already selected `BOUNDED_REMEDIATION`, consume its candidate-bound remediation plan as the authoritative synthesis input to `/fix`. Reconcile that plan against the current candidate, findings, governing design and authority, but do not silently rediscover a different repair or re-adjudicate the completed review. If the plan is stale, conflicts with current authoritative evidence, no longer covers the complete blocker set, or now requires materially broader product, architecture, security, scope or authority, stop mutation and return to response routing. If direct `/fix` follows `CHANGES REQUIRED` and no valid plan exists, the router must perform the non-mutating synthesis transition first.

Before material mutation, reconcile both the workflow router's mandatory repeated-review escalation and any durable post-closure lineage for the material blocker family. If durable evidence shows R1 `CHANGES REQUIRED` in behavioural/invariant domain X, authorised remediation changed the candidate, and a genuinely fresh R2 again found a material evidence-based blocker in the same domain X, do not perform another `/fix` until a current [Stateful invariant analysis](../workflows/stateful-invariant-analysis.md) record is bound to the exact candidate, R1/R2 review identities/dispositions, materially related blocker/domain evidence, and governing contract. Return control to the router instead of mutating when that analysis is missing or stale. The escalation requirement creates no redesign or mutation authority and does not widen the `/fix` action gateway.

Separately, if current authoritative evidence establishes that domain X already underwent an invariant-closure attempt and a genuinely fresh substantive review now establishes `CLOSURE_FALSIFIED` or `POST_CLOSURE_SAME_FAMILY_RECURRENCE` within that closure boundary, ordinary `/fix` is ineligible while the architecture boundary is unresolved. Stop before material mutation with `ARCHITECTURE_RECONSIDERATION_REQUIRED` and return control to the router. A previous invariant-closure analysis/remediation plan does not satisfy this stronger boundary merely because it authorised the last remediation attempt. The boundary remains unresolved unless current authoritative evidence contains both (a) a current `ARCHITECTURE_RECONSIDERATION_COMPLETED` record, or reconstructable equivalent, produced under separately governed read-only reconsideration authority and bound to the recurrence, prior closure lineage, exact candidate and governing contract, and (b) separate current bounded remediation or design-mutation authority for the resulting proposal. Authority to perform the read-only architecture reconsideration is not remediation authority. When both are present, return to response routing and require a new candidate-bound remediation plan derived from the architecture result; never revive the pre-recurrence invariant-closure remediation plan.

Do not mechanically classify every later X-labelled finding as architecture recurrence. If intervening evidence demonstrably shows that a later candidate change broke an already-established X contract, use the regression/restoration path unless broader evidence independently establishes post-closure recurrence. Likewise preserve the existing routes for new defect families, unrelated domains, newly applicable governing requirements and materially out-of-boundary changes.

If current authoritative evidence establishes `CLOSURE_METHOD_FALSIFIED` / `ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED`, ordinary isolated `/fix` is ineligible. Stop before material mutation and return control to the router. The earlier architecture-reconsideration authority and its closure result do not authorise another closure reconstruction or a patch that merely inserts the newly discovered primitive. Require a separately authorised current [Architecture closure analysis](../workflows/architecture-closure-analysis.md) reconstruction record bound to the falsifying review, prior closure artefact, exact candidate and governing contract. Even after that read-only gate is satisfied, mutation still requires separately established remediation/design authority and a new candidate-bound plan derived from the reconstructed closure model.

For any authorised architecture candidate whose correctness depends on an architecture-closure model, remediation completion must establish all three layers: `FINDING_CLOSURE` (every reported blocker addressed), `MODEL_CLOSURE` (the closed source/obligation universe is independently rederived, every applicable obligation has source → primitive coverage, the five closure inventories remain complete, extensional consequence ownership/disjointness remains proved, and no newly introduced or newly exposed applicable primitive sits outside the model), and `PARENT_NON_REGRESSION` (previously established identity/authority/state/effect/recovery invariants remain satisfied). Patching all reported findings is not enough to claim architecture closure.

For work subject to the proactive architecture-closure publication gate, treat material governing-contract or architecture-scope movement as a closure-evidence freshness question before another closure-ready claim. A newly introduced decision-critical primitive, authority edge, irreversible-effect class, state family, identity dependency, equivalence/overlap claim, recovery obligation or migration/fence obligation must enter the closure universe and receive affected global closure checks before publication. Do not mechanically force full closure reconstruction for every candidate edit: a local correction wholly inside an already-modelled primitive may retain the existing closure artefact when current evidence establishes that its governing source obligations, primitive universe and affected coverage remain current.

When the initial R1/R2 mandatory analysis requirement is satisfied by a current analysis record and no post-closure architecture boundary is established, consume its bounded remediation plan as the authoritative synthesis input to `/fix`. Reconcile it against any earlier review-response-synthesis plan, the current candidate, findings, governing design and authority. If the analysis materially refines or corrects the earlier plan, the analysis-produced plan supersedes that earlier plan for this remediation while remaining subject to the same stale-plan, scope, action-gateway and authority checks. Do not silently choose between conflicting plans or rediscover a different repair; if they cannot be reconciled within existing authority, stop mutation and return to response routing.

Bind the run context to the repository/work item, exact starting candidate identity, authority sources, instruction provenance, bounded remediation scope, effective and prohibited capabilities, owner-decision boundaries, required validation, and required evidence. Treat the context as ephemeral derived execution state, not as a new authority source.

Immediately before the first material write, refresh the starting candidate identity. If it moved, invalidate the stale candidate-specific context and re-resolve before applying findings to unexpected bytes.

Classify each finding as:
- valid and bounded by the existing contract;
- invalid or already resolved by current evidence; or
- requiring a genuinely new product, architecture, authority, security, or scope decision.

When the review evidence identifies a material relationship among findings, preserve that diagnosis while deriving remediation. Determine whether the corrections are genuinely isolated local changes or one shared invariant/boundary correction. Do not count findings mechanically or infer redesign merely from recurrence.

For every valid bounded finding, derive the smallest safe correction. The smallest safe correction is not necessarily the smallest textual or most local patch. Where a shared invariant/boundary correction is objectively determined by the governing contract and findings and is already within the resolved remediation scope and `/fix` authority, that correction may be the minimum safe change. If the appropriate invariant/boundary correction requires materially new product, architecture, security, scope, owner, or other separate authority, classify that boundary honestly rather than decomposing it into superficially local exceptions or silently redesigning. Do not broaden scope, redesign adjacent components, weaken validation, or treat review suggestions as requirements unless the governing contract makes them necessary.

When the current remediation is materially stateful, lifecycle-sensitive, cross-component, concurrency/retry/cache/inference-sensitive, or follows a mandatory stateful/invariant analysis, apply the additional completeness work proportionately. Search the codebase-wide decision-critical surface for related call sites, duplicated raw predicates and policy bypasses; construct the applicable failure/recovery matrix; cover the original defect plus materially adjacent state transitions identified by the analysis; examine repeated or prolonged failure behaviour where relevant; exercise production integration paths as well as shared-policy helpers where feasible; gather applicable build, compile, static, sanitizer or runtime evidence that is available and required; and state explicitly which material surface remains untested. These requirements do not make a simple/local `/fix` heavyweight when stateful analysis is not materially applicable.

Before each material action, apply the `/fix` action gateway and classify the action as:
- `ALLOW` — current authoritative sources permit the action within the resolved remediation scope and `/fix` operation ceiling;
- `REQUIRE OWNER / SEPARATE AUTHORITY` — the action is outside the resolved remediation scope or needs missing product, architecture, security, scope, owner, or other separate authority;
- `FORBID` — higher-precedence authority or the `/fix` operation ceiling prohibits the action under this `/fix` authority.

Missing or ambiguous authority never defaults to `ALLOW`. Keep authority classification separate from execution feasibility: a technically available tool never grants authority, while an `ALLOW` action whose required execution capability is unavailable follows the governing router's capability/external-action boundary without inventing a new owner decision.

When foreground-execution exhaustion becomes a material risk during an authorised bounded remediation, apply [Foreground execution resilience](../workflows/foreground-execution-resilience.md). Finish the smallest coherent bounded remediation state, perform the minimum pre-publication safety checks needed to preserve it safely, and establish an exact immutable candidate before spending the remaining practical foreground budget on assurance or reconciliation that can safely continue later. Candidate or pull-request mutation remains subject to the resolved `/fix` authority and action gateway; foreground-budget pressure grants no new mutation, publication, execution-surface, merge, release, deployment, credential, settings, production, or other lifecycle authority. Treat the checkpoint as persistence/reconstruction only: required validation and fresh re-review remain bound to the resulting exact candidate and cannot be inferred from the checkpoint itself.

Execute only `ALLOW` actions that are actually available. Implement the bounded corrections, add or adjust regression coverage that would have caught the defect, run the relevant required validation, and inspect the complete resulting diff for accidental scope expansion. If unexpected external candidate movement is detected during remediation, fail closed and reconcile/re-resolve before continuing.

Treat remediation as an immutable candidate transition: starting candidate A plus authorised bounded remediation produces candidate B. Once bytes change, candidate-A-specific review and validation do not silently transfer to B. Bind the resulting validation and evidence to B's exact immutable identity.

Return a remediation record reconstructable as:
- governing finding/remediation authority;
- starting candidate identity;
- bounded implementation delta;
- resulting candidate identity;
- validation/evidence bound to the resulting candidate;
- any `REQUIRE OWNER / SEPARATE AUTHORITY` or `FORBID` boundaries encountered;
- any authorised action that could not execute because of a capability boundary;
- remaining boundaries and next governed state.

Classify evidence honestly as `STATIC`, `EXECUTED`, or `DURABLE` according to the Resolved Agent Run Context contract. Do not imply execution occurred where only static reasoning was performed. Clearly identify any finding that still requires a separate decision rather than pretending remediation is complete.

That remediation record is the workflow record, not a routed terminal state. When this workflow is invoked through the workflow router, return control to the router after recording it so the router can apply the effective continuation mode.

Preserve any required independent re-review boundary; do not present author-side remediation as fresh approval evidence. If this context changed the candidate and independent re-review is required, do not enter that review here. Treat the re-review as a hard fresh-context boundary and return control to the router so it can resolve an eligible genuinely isolated fresh-review context. If such a context is eligible, the review is performed there under the ordinary `/review` ceiling and fresh-review contract. Only when no eligible/provable isolated context can be established should the existing manual fallback be used; when the durable target is sufficient for reconstruction, hand it off as `Next chat: /review <REVIEWED_CANDIDATE>`. That navigation is not review or merge authority.
```

## Inputs

- `<REVIEWED_CANDIDATE>` — the PR/branch/candidate plus the blocking review findings.

## What it does

Keeps remediation narrow, makes mutation authority explicit, classifies material actions before execution, makes review findings traceable to regression evidence, and prevents a repair cycle from becoming an unbounded redesign. It also preserves review-level diagnosis of materially related findings so an already-authorised invariant/boundary correction may be recognised as the minimum safe change instead of forcing repeated example-by-example patches. It binds remediation to starting candidate A and the resulting validation/evidence to candidate B, preventing candidate-specific review or validation from silently carrying across changed bytes. When foreground-execution exhaustion becomes a material risk, it applies the shared resilience contract so a coherent immutable remediation candidate is preserved before deferrable assurance without widening `/fix` authority.

When routed, it returns the remediation record to the governing workflow while preserving the mandatory fresh-context boundary for re-review of a candidate changed in this context. The router may satisfy that boundary through an eligible isolated fresh-review context before requiring the owner to transport the review manually.

## Boundaries / limitations

Use only where the expected correction is objectively bounded by existing requirements and authority. An invariant/boundary-level correction is permitted only when it is objectively determined by the governing contract/findings and already within the resolved remediation scope; materially new architecture, authority, security, product, or scope decisions should be resolved separately. Repeated findings never create redesign authority by themselves. Merge, release/tag, deployment, unrelated repository mutation, infrastructure/provider mutation, and settings/credential/secret mutation are not granted by this workflow merely because a capability exists.

Author-side remediation cannot substitute for fresh independent review when that gate is required. Automatic fresh-context resolution changes only how an eligible independent context is reached; it never makes this remediation context fresh or bypasses repository rules that require another human or formal reviewer. The action gateway is a workflow contract, not a new approval service, sandbox, or persisted policy object.

## Status

`tested`
