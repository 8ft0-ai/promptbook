# Autonomous progression

## Purpose

Complete already-authorised engineering goals with minimal owner intervention, without weakening any safety, identity or review boundary.

## When to use

Use for governed `/go` and `/step` after the [workflow router](README.md) has selected the operation. Repository-local instructions and explicit task authority take precedence.

## Prompt

```text
Progress <TASK_OR_OBJECTIVE> through one goal-driven execution loop:

1. BIND: Establish the original requested outcome and acceptance evidence, explicitly distinguishing a bounded deliverable from any broader lifecycle. Do not invent a PR, review, publication or adjacent scope when the requested deliverable is only implementation and tests. Reconstruct current repository/task authority, exact identity and legitimate approval boundaries from authoritative evidence; do not rely on stale remembered summaries.
2. SELECT: Determine the smallest safe executable action advancing that goal. Before candidate authoring or other consequential implementation apply the router's **mandatory pre-authoring architecture gate**; a materially high-risk architecture intending a strong closed-world/closure-ready claim needs an eligible independently derived closure artefact or the specialist closure-analysis route **before** authoring. First inspect the current authoritative objective and artefacts, then perform closure analysis when triggered; do not skip reconnaissance. Before an effect, refresh decision-critical state and classify it ALLOW, REQUIRE OWNER / SEPARATE AUTHORITY or FORBID using the [resolved agent run context](resolved-agent-run-context.md). Technical capability never grants permission.
3. EXECUTE: Execute an ALLOW action. Diagnose and resolve routine prerequisites, failing checks and bounded defects within existing authority. Reconnaissance is preparation, not a terminal outcome. An unresolved implementation task, uncertain checkout, or future deployment approval is not inherently BLOCKED. Reconcile observed evidence instead of guessing.
4. VERIFY: Establish the actual effect with tests, exact revision and operational evidence where applicable; **after every observed tool result, check whether all acceptance evidence for the originally requested deliverable is already satisfied before choosing another action**. If so, stop under step 5; do not create an optional PR, review or further workflow merely to keep moving. Rebind any changed candidate/result identity. Under /go (UNTIL_BOUNDARY), select the next authorised action automatically and repeat. Under /step (ONE_TRANSITION), perform one governed transition with its intrinsic verification, re-resolve once, then stop.
5. STOP: Return COMPLETE only for the verified **requested** deliverable and required close-out; do not extend scope after it is satisfied. An opened PR awaiting mandatory independent review or later approved execution is not COMPLETE for a broader governed objective: report the actual fresh-review/decision boundary instead. Stop at a demonstrated higher-precedence safety, authority, independent-review, capability, cost or genuine technical boundary; distinguish DECISION_REQUIRED, EXTERNAL_REQUIRED and true BLOCKED. Give actionable boundary evidence. An interruption with a safely resumable path remains non-terminal; preserve a reconstructible checkpoint.

A completed handoff, created PR, green CI run or local workflow disposition does not alone establish goal completion. A later approval must not prevent authorised work in earlier stages. Never ask for routine reconfirmation when current authority already permits the next step.
```

## Conditional specialist contracts

Load only the relevant detailed rules **before** the consequential transition; they remain mandatory when triggered:

- Fresh independent review, architecture closure or strong-closure generation → [Review and closure](../../guides/conditional/progression-review-closure.md) and [Fresh independent review](fresh-independent-review.md).
- Configured capability key, suppression or PR-ready transition → [Capability handling](../../guides/conditional/progression-capabilities.md).
- Failed execution mechanism or unavailable reviewer isolation → [Execution locality](../../guides/conditional/progression-locality.md).
- Real owner decision, external action, fresh-context handoff or terminal boundary → [Boundary and handoff handling](../../guides/conditional/progression-boundaries.md).
- Foreground interruption, returned external observation, candidate recovery or unusual continuation → [Recovery and continuation](../../guides/conditional/progression-recovery.md).

Do not load every specialist document by default. If a predicate applies and its canonical document is unavailable, fail closed rather than inferring the rule. All special rules remain subordinate to repository-local policy and explicit task authority.

## Inputs

- `<TASK_OR_OBJECTIVE>` — authorised engineering goal and acceptance evidence.

## What it does

Uses one canonical goal-action-verification loop, while specialised high-risk conditions retain their exact rules without loading them on every ordinary transition.

## Boundaries / limitations

Do not bypass independent review, exact-candidate identity, scope restrictions, failing validation, deployment/merge/finance approvals, capability denial, required teardown or hard repository policy. No source of execution capability is a source of authority.

## Status

`tested`
