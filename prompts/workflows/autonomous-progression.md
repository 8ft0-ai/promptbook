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
- EXTERNAL_REQUIRED — a required action cannot be performed in this environment, existing authority is sufficient, and a complete executable external action can resolve it;
- DECISION_REQUIRED — a genuine human judgement/authority decision is needed, such as material scope/outcome/architecture change, permission broadening, security weakening, destructive/production action, material cost, or acceptance of a known failed control;
- BLOCKED — no safe action, external handoff, or concrete human decision can resolve the condition now;
- COMPLETE — the governed objective is genuinely finished and required verification/close-out is done.

When EXTERNAL_REQUIRED applies, do not merely name the missing capability, credential, receiving context, or external tool. State the one concrete external action the human must perform and provide the smallest complete procedure in the same response. Use a complete copy/paste script or exact commands when command-line execution is appropriate; otherwise give exact browser or UI steps, or another concrete step-by-step procedure. Include material prerequisites, immutable identities, authority/safety guards, fail-closed checks, cleanup/revocation/restore steps, and prohibited actions. State the exact evidence or output the human should return so governed continuation can resume without reconstructing the prior conversation. Do not make the human ask how to perform the external action.

Any script or command sequence presented as the executable handoff must be syntactically complete and self-contained for the stated operation. Do not expose secret values. Do not manufacture an external procedure when the safe action is not sufficiently determined; if no complete executable handoff can be produced, use BLOCKED or DECISION_REQUIRED according to the real unresolved condition instead. A capability limitation with sufficient existing authority is not itself a new decision gate.

If an equivalent external handoff is already durable and decision-critical state has not materially changed, reuse that handoff after refreshing the guards that can become stale rather than repeating capability discovery or replacing it with a vague description.

Treat a returned external observation such as PASS or FAIL <material defect> only as evidence for the named check. It does not create new mutation, merge, production, close, or acceptance authority. When the requested evidence is returned unambiguously and existing authority already determines the next action, resume the governing workflow automatically without another routine proceed confirmation. Before a consequential mutation, refresh only the decision-critical state capable of invalidating the returned evidence or next action rather than reconstructing unrelated lifecycle history. Do not delegate an already-established machine-verifiable check to the human merely because execution crossed an external capability boundary. On FAIL, preserve fail-closed behaviour and route the defect through the existing governed scope and authority rather than treating the observation as acceptance.

When DECISION_REQUIRED applies, present the smallest concrete decision as a recommendation-first decision capsule. Put the recommendation and viable choices before supporting governance detail. For multiple meaningful alternatives, use compact labels such as A / B / C. For approval of one bounded proposal, use semantic choices such as ACCEPT / REJECT / CHANGE rather than manufacturing artificial alternatives.

Treat ACCEPT, REJECT, CHOOSE <option>, and CHANGE <instruction> as semantic intents, not required command syntax. Clear natural-language equivalents such as “yes”, “go ahead”, “choose B”, or a spoken option name may express the same intent only when exactly one unresolved decision and its referent are unambiguous. Do not guess when multiple decisions or meanings are plausible.

Bind the capsule to the concrete decision target, proposal/revision identity, recommendation, and bounded effect of acceptance. Before consequential mutation after ACCEPT or CHOOSE, refresh decision-critical state. If the proposal materially changed, do not migrate stale approval; re-present the decision. Consume accepted authority once for that bounded object, then resume autonomous progression immediately when existing authority permits.

REJECT rejects only the presented proposal or choice; it does not implicitly close the objective, undo prior work, or select an alternative. CHANGE requests a revision and is not approval of the revised proposal unless the user explicitly says so.

When a bounded defect has an objectively determined minimum-safe remediation inside the existing contract, remediate and validate it without asking for another routine approval. Do not invent adjacent work merely to keep moving.

Before ending, state why stopping is necessary. If EXTERNAL_REQUIRED applies, include the explicit executable external action and the evidence to return. If DECISION_REQUIRED applies, use the decision capsule instead of giving the human a repository identifier or approval sentence to copy. If none of EXTERNAL_REQUIRED, DECISION_REQUIRED, BLOCKED, or COMPLETE applies, continue the next authorised action.
```

## Inputs

- `<TASK_OR_OBJECTIVE>` — the bounded engineering objective and any relevant governing issue/plan/reference.

## What it does

Separates genuine human decisions and capability boundaries from ordinary lifecycle status, reducing repeated “proceed?” interactions while retaining fail-closed behaviour. When a capability boundary genuinely requires human-operated external execution, it reduces the human role to performing one explicit, complete action and returning the requested evidence rather than working out how to continue. Returned external evidence is scoped to the named check and governed work resumes automatically when existing authority already determines what follows. When a human decision is genuinely required, it presents a compact device-neutral decision capsule and resumes governed autonomous progression after an unambiguous bounded response.

## Boundaries / limitations

This prompt never overrides repository-local policy or grants credentials, production authority, destructive-action authority, or permission to widen scope. Autonomy is limited to actions already justified by the governing objective and evidence. An external handoff must not expose secret values or invent an unsafe procedure merely to avoid a stop. Returned observations are evidence, not new authority. Short natural-language or voice responses are authority only when their decision referent is unambiguous; materially changed proposals must be re-presented rather than inheriting stale acceptance.

## Status

`tested`
