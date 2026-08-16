# Documentation assessment workflow

## Purpose

Run a governed, evidence-led repository documentation assessment when the right reader tasks still need to be discovered or validated before any documentation change is justified.

## When to use

Use for broad repository documentation assessment, navigation or authority problems, documentation-quality questions, or when the smallest justified response depends on discovering representative reader tasks. For one already-known reader task, prefer the narrower [Repository documentation assessment](../documentation/repository-assessment.md). Do not use this workflow merely because an already-bounded documentation edit or drafting task is involved.

## Prompt

```text
Assess the documentation of <TARGET_REPOSITORY> using the Promptbook documentation-assessment route.

Method authority

Use `8ft0-ai/diataxis-for-ai-repos` release `v0.1.2`, pinned to exact commit `c1e1982dd448b3574bb7e14667363ba9db326c5c`, as the external assessment-method authority. The exact commit governs. Do not follow external `main` or silently move to a later release.

Promptbook remains the governing workflow and authority layer. Repository-local instructions, explicit task authority, platform safety constraints and current target-repository evidence take precedence. Do not import a second IssueOps or governance lifecycle from the external method.

Adoption level

Use Level 2 task evidence by default for a substantive repository assessment. If one narrow reader task or documentation question is already known and can be assessed proportionately, use the existing Promptbook Level 1 single-task assessment instead. Use Level 3 controls only when method evaluation, higher-risk execution, repository-local policy or a separately governed experiment actually requires them.

Assessment setup

1. Reconstruct the target repository identity and a sufficiently current pinned evidence state.
2. Treat repository evidence as evidence, not complete truth.
3. Distinguish Observation, Authority, Inference and Uncertainty for material conclusions.
4. Identify evidence-supported reader groups. Do not invent personas from directory shape.
5. Propose a small set of representative reader tasks based on real reader outcomes, not Diátaxis categories.
6. Give each task a realistic starting context and answer-neutral completion condition.
7. Identify command, network, credential, freshness, isolation or prerequisite constraints only where they materially affect that task.
8. Identify protected decisions involving intent, policy, priority, ownership, rationale or disputed authority.
9. Do not manufacture tasks merely to justify a documentation change. Retain and no-change are valid outcomes.

Human task-set gate

Before executing task walkthroughs, present one Promptbook decision capsule covering only the material owner judgements:

DECISION_REQUIRED — Documentation assessment task set

Recommended: ACCEPT

ACCEPT — approve the proposed readers, tasks and bounded execution conditions
CHANGE — revise the proposed assessment
REJECT — stop this assessment

The proposal must make clear the reader groups, representative tasks and priority, starting contexts, answer-neutral completion conditions, any material execution/freshness boundaries, and protected decisions. Do not require separate owner approval of Level-3 experimental bookkeeping when it is not material to the Level-2 task.

After acceptance

After an unambiguous accepted task set, refresh decision-critical state and continue without routine `proceed` confirmations through:

1. approved task-path walkthroughs or execution;
2. evidence recording with accurate primary results: Complete, Partial, Blocked or Not tested;
3. classification of failures, retained paths and no-change outcomes;
4. selection of the smallest sufficient response;
5. a bounded remediation backlog where evidence justifies change;
6. limitations and close-out.

Preserve prerequisite, freshness and isolation checks only when the actual task depends on them. Stop rather than invent unavailable intent or authority.

Remediation handoff

Assessment does not create target-repository mutation authority.

- If no change is justified, finish as COMPLETE.
- If remediation is justified and implementation authority already exists under the target repository's governing task, return control to Promptbook's normal workflow router and continue only within that authority.
- If remediation mutation is not yet authorised, present one bounded Promptbook decision capsule for the remediation scope. On acceptance, route to the normal Promptbook planning/implementation lifecycle.

Do not create or invoke a parallel external governance lifecycle.

Proportionality and no-route behaviour

Use the lightest route that supports the decision. Do not route ordinary bounded documentation edits, known corrections or explicit drafting tasks through a new assessment. If repository evidence supports no material assessment need, record retain/no-change and finish. If the requested outcome is already an accepted implementation problem, route it to the normal governed engineering path instead of reassessing it.
```

## Inputs

- `<TARGET_REPOSITORY>` — the repository whose documentation needs a substantive evidence-led assessment.

## What it does

Adapts the released Diátaxis assessment method into Promptbook's governed workflow model: Level 2 by default, one genuine human task-set gate, autonomous continuation after acceptance, and a clean handoff back to Promptbook for any separately authorised remediation.

## Boundaries / limitations

This workflow is assessment-only. It does not grant target-repository mutation, documentation drafting, release, deployment, credential or merge authority. It intentionally does not import external IssueOps, mandatory durable assessment publication, blanket evidence budgets, mutation-class machinery, blinded fixtures or independent-review experiments unless the actual governed task requires those controls.

## Status

`experimental`
