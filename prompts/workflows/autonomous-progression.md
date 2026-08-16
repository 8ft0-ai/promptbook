# Autonomous progression

## Purpose

Let an engineering agent continue routine, already-authorised work without repeatedly returning to the human for orchestration.

## When to use

Use for a governed engineering objective where repository policy, current evidence, and existing authority determine most routine next actions, but explicit stop boundaries still matter.

## Prompt

```text
Progress <TASK_OR_OBJECTIVE> as far as safely possible with minimal human intervention.

Treat repository-local instructions, explicit task authority, accepted plans/decisions, current evidence, and platform safety constraints as authoritative.

Continue autonomously while the next action is:
1. inside the current objective and scope;
2. supported by sufficiently current evidence;
3. safely decidable from existing policy, constraints, acceptance criteria, or minimum-safe-change principles; and
4. executable with capabilities legitimately available in the current environment.

Routine planning, implementation, validation, bounded remediation, review disposition, branch/PR work, merge where already authorised, post-merge verification, and close-out are not conversational stop points merely because they are the “next gate”. Refresh material state before consequential actions and reconcile changes rather than blindly executing stale instructions.

Escalate only as one of these states:
- EXTERNAL_REQUIRED — a required action cannot be performed in this environment, but a complete executable handoff can resolve it;
- DECISION_REQUIRED — a genuine human judgement/authority decision is needed, such as material scope/outcome/architecture change, permission broadening, security weakening, destructive/production action, material cost, or acceptance of a known failed control;
- BLOCKED — no safe action, external handoff, or concrete human decision can resolve the condition now;
- COMPLETE — the governed objective is genuinely finished and required verification/close-out is done.

When a bounded defect has an objectively determined minimum-safe remediation inside the existing contract, remediate and validate it without asking for another routine approval. Do not invent adjacent work merely to keep moving.

Before ending, state why stopping is necessary. If none of EXTERNAL_REQUIRED, DECISION_REQUIRED, BLOCKED, or COMPLETE applies, continue the next authorised action.
```

## Inputs

- `<TASK_OR_OBJECTIVE>` — the bounded engineering objective and any relevant governing issue/plan/reference.

## What it does

Separates genuine human decisions and capability boundaries from ordinary lifecycle status, reducing repeated “proceed?” interactions while retaining fail-closed behaviour.

## Boundaries / limitations

This prompt never overrides repository-local policy or grants credentials, production authority, destructive-action authority, or permission to widen scope. Autonomy is limited to actions already justified by the governing objective and evidence.

## Status

`tested`
