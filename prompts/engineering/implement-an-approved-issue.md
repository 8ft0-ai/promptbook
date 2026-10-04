# Implement an approved issue

## Purpose

Implement a bounded task from an accepted plan while preserving scope, traceability, and validation discipline.

## When to use

Use when the intended outcome and implementation approach are already approved or otherwise sufficiently determined, and the receiving agent has an authorised repository write path.

## Prompt

```text
Implement <APPROVED_TASK> using <APPROVED_PLAN>.

Before modifying anything, inspect the current task and acceptance criteria, the approved plan, relevant repository instructions, architecture, code, tests, branch state, and any material changes since the plan was accepted.

If current evidence materially invalidates the plan, stop before speculative mutation and state the smallest decision or replanning step required.

Before authoring or publishing an architecture candidate as closed-world, architecture-closed, closure-ready, complete over its decision-critical authority/effect universe, or an equivalent strong completeness claim, determine whether the work is materially security-, authority-, identity-, recovery/ambiguity-, irreversible-effect-, or migration/cutover-sensitive. When both the material-risk condition and strong-completeness condition apply, require a current independently derived [Architecture closure analysis](../workflows/architecture-closure-analysis.md) artefact that covers the governing contract and architecture scope **and** a genuinely fresh architecture-closure review of that exact artefact with disposition `APPROVED_FOR_CANDIDATE_PROJECTION`. `ARCHITECTURE_CLOSURE_READY` is author-side analysis evidence only and does not make candidate authoring eligible. Bind candidate projection to the exact approved closure artefact and closure-review record; consume/project that artefact into the candidate and do not reconstruct the completeness universe from candidate prose. If the artefact or its fresh approval is absent or stale because the governing contract or covered decision-critical scope moved materially, stop before the closure-ready publication boundary and return control to the router. If projection would introduce a new decision-critical primitive, authority edge, state family, effect class, identity dependency, recovery rule, equivalence claim, migration obligation or external boundary, stop projection and return to closure analysis/review rather than silently expanding the approved universe. A local change wholly inside an already-modelled primitive does not automatically require full reconstruction when current evidence proves the approved closure coverage remains applicable.

Otherwise implement the smallest sufficient change. Preserve existing architecture and conventions unless the plan explicitly changes them. Add or update tests with behavioural changes, cover relevant negative paths, validate incrementally, and avoid unrelated refactoring or opportunistic dependency changes. Do not weaken tests, assertions, thresholds, or checks to make the candidate pass.

When foreground-execution exhaustion becomes a material risk, apply [Foreground execution resilience](../workflows/foreground-execution-resilience.md). Finish the smallest coherent scoped state, perform the minimum pre-publication safety checks needed to preserve it safely, and establish an exact immutable candidate commit before spending the remaining practical foreground budget on assurance or reconciliation that can safely continue later. A PR bound to that exact candidate is preferred only when PR creation is already authorised and appropriate. Treat the checkpoint as persistence/reconstruction only: authoritative tests, static checks, CI, integration evidence and other required assurance remain candidate-bound, and evidence for different bytes does not transfer. Do not publish incoherent or unsafe work merely to beat a timer.

Before declaring completion:
1. inspect the complete diff;
2. map the result back to every acceptance criterion;
3. check for scope expansion, generated artefacts, secrets, and unrelated changes;
4. run all relevant tests, static checks, builds, and required integration/manual validation;
5. verify compatibility, migration, rollback, and residual risks;
6. leave the candidate in a coherent reviewable state.

Return a concise implementation record: outcome delivered, principal changes, acceptance-criterion coverage, validation and results, justified plan deviations, and remaining limitations.

That implementation record is the workflow record, not a routed terminal state. When this workflow is invoked through the workflow router, return control to the router after recording it so the router can apply the effective continuation mode to the next governed gate. If required independent review is the next gate and this context authored or materially shaped the candidate, preserve the fresh-context boundary rather than reviewing the candidate here. Return control to the router so it can resolve an eligible genuinely isolated fresh-review context under the fresh-review context-resolution contract. Only when no eligible/provable isolated context can be established should the existing manual fallback be used; a durable target may then be handed off as `Next chat: /review <APPROVED_TASK>` when that target is sufficient for reconstruction.

Do not merge, deploy, release, or broaden scope unless that action is already authorised separately. Continuation metadata never creates that authority.
```

## Inputs

- `<APPROVED_TASK>` — the issue, task, or bounded implementation objective.
- `<APPROVED_PLAN>` — the accepted implementation plan or exact reference to it.

## What it does

Keeps implementation tied to the approved outcome, makes validation part of completion, and forces plan drift to be reconciled before speculative code changes. When foreground exhaustion is a material risk, it establishes a coherent immutable candidate before deferrable assurance while keeping preservation safety checks distinct from authoritative candidate-bound validation. When routed, the implementation record returns control to the governing workflow instead of accidentally ending the broader objective. A context that authored the candidate remains ineligible to review it independently; the router may satisfy that hard boundary through an eligible isolated fresh-review context before requiring manual context transport.

## Boundaries / limitations

This prompt does not grant repository mutation, pull-request creation, merge, deployment, credential, production, or execution-surface authority. Foreground-budget pressure cannot create any of those authorities. The receiving environment must already have the required capabilities and permissions where needed. A durable checkpoint is not validation, approval, completion, or review-readiness by itself. A required fresh independent review remains a hard boundary after this context authors or materially shapes the candidate. Automatic context resolution may change how that boundary is satisfied, but it never makes the authoring context fresh and never weakens a repository requirement for another human or formal reviewer.

## Status

`tested`
