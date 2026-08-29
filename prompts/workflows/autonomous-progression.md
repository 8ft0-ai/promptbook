# Autonomous progression

## Purpose

Let an engineering agent continue routine, already-authorised work without repeatedly returning to the human for orchestration.

## When to use

Use for a governed engineering objective where repository policy, current evidence, and existing authority determine most routine next actions, but explicit stop boundaries still matter.

## Prompt

```text
Progress <TASK_OR_OBJECTIVE> as far as safely possible with minimal human intervention.

Treat repository-local instructions, explicit task authority, accepted plans/decisions, current evidence, and platform safety constraints as authoritative.

Before entering another workflow, resolve the effective continuation mode from the workflow router. Apply all hard governance constraints first; continuation mode is only a preference among actions already permitted by those constraints. It never creates mutation, merge, deploy, credential, production, acceptance, review, validation, security, or scope authority.

Use the router-defined modes as follows:
- `auto` — enter the next safely authorised and executable same-context workflow automatically;
- `suggest` — do not enter the next workflow; when a broader objective remains active, emit the smallest safely determined `Next:` / `Next chat:` navigation;
- `stop` — end after the explicitly requested deliverable without suppressing any required terminal-state classification; when a broader objective is already active, expose safely determined navigation unless the user explicitly requested no continuation guidance.

A specialised workflow's local disposition or record is a workflow record, not a conversational terminal state. After recording it, return control to the router and apply the effective continuation mode unless a higher-precedence hard constraint requires a boundary.

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

Fresh independence, missing authority, failed or missing required validation, materially changed accepted proposals, repository/task policy requiring an explicit stop, and the terminal states above are hard boundaries. `auto` must not cross them merely to preserve momentum.

When EXTERNAL_REQUIRED applies, do not merely name the missing capability, credential, receiving context, or external tool. State the one concrete external action the human must perform and provide the smallest complete procedure in the same response. Use a complete copy/paste script or exact commands when command-line execution is appropriate; otherwise give exact browser or UI steps, or another concrete step-by-step procedure. Include material prerequisites, immutable identities, authority/safety guards, fail-closed checks, cleanup/revocation/restore steps, and prohibited actions. State the exact evidence or output the human should return so governed continuation can resume without reconstructing the prior conversation. Do not make the human ask how to perform the external action.

For human-operated command-line execution, apply [Operational artifact hand-off](operational-artifact-handoff.md). Keep a genuinely atomic, transcript-independent command inline. When execution fragility, guard coupling, or evidence complexity is material, prefer a materialised/downloadable artifact with short staging/invocation instructions and bounded `RESULT` / `EVIDENCE` hand-back rather than turning the conversation transcript into executable state. Artifact delivery never creates authority: read-only work remains read-only, and separately authorised mutation must still fail closed on target, identity, prerequisite, integrity, or authority guard failure. If downloadable-file delivery is unavailable, use only a safe degraded path defined by that contract; do not silently substitute a large fragile executable transcript block.

A genuine fresh-context boundary is a distinct kind of EXTERNAL_REQUIRED stop. When opening a fresh chat/session is itself the required action and a durable exact target is sufficient for that context to reconstruct the decision-critical state, the smallest complete handoff may be a `Next chat:` public shorthand invocation such as `/review` with that target. The invocation is navigation only, preserves the freshness boundary, and creates no authority. This compact context-transfer form must never replace the complete commands, browser/UI steps, guards, cleanup/prohibitions, or evidence-to-return required for human-operated external execution.

Any script or command sequence presented as the executable handoff must be syntactically complete and self-contained for the stated operation. Do not expose secret values. Do not manufacture an external procedure when the safe action is not sufficiently determined; if no complete executable handoff can be produced, use BLOCKED or DECISION_REQUIRED according to the real unresolved condition instead. A capability limitation with sufficient existing authority is not itself a new decision gate.

If an equivalent external handoff is already durable and decision-critical state has not materially changed, reuse that handoff after refreshing the guards that can become stale rather than repeating capability discovery.

Treat a returned external observation such as PASS or FAIL <material defect> only as evidence for the named check. It does not create new mutation, merge, production, close, or acceptance authority. When the requested evidence is returned unambiguously and existing authority already determines the next action, resume the governing workflow automatically without another routine proceed confirmation. Before a consequential mutation, refresh only the decision-critical state capable of invalidating the returned evidence or next action rather than reconstructing unrelated lifecycle history. Do not delegate an already-established machine-verifiable check to the human merely because execution crossed an external capability boundary. On FAIL, preserve fail-closed behaviour and route the defect through the existing governed scope and authority rather than treating the observation as acceptance.

When DECISION_REQUIRED applies, present the smallest concrete decision as a recommendation-first decision capsule. Put the recommendation and viable choices before supporting governance detail. For multiple meaningful alternatives, use compact labels such as A / B / C. For approval of one bounded proposal, use semantic choices such as ACCEPT / REJECT / CHANGE rather than manufacturing artificial alternatives.

Treat ACCEPT, REJECT, CHOOSE <option>, and CHANGE <instruction> as semantic intents, not required command syntax. Clear natural-language equivalents such as “yes”, “go ahead”, “choose B”, or a spoken option name may express the same intent only when exactly one unresolved decision and its referent are unambiguous. Do not guess when multiple decisions or meanings are plausible.

Bind the capsule to the concrete decision target, proposal/revision identity, recommendation, and bounded effect of acceptance. Before consequential mutation after ACCEPT or CHOOSE, refresh decision-critical state. If the proposal materially changed, do not migrate stale approval; re-present the decision. Consume accepted authority once for that bounded object, then resume autonomous progression immediately when existing authority permits.

REJECT rejects only the presented proposal or choice; it does not implicitly close the objective, undo prior work, or select an alternative. CHANGE requests a revision and is not approval of the revised proposal unless the user explicitly says so.

When a bounded defect has an objectively determined minimum-safe remediation inside the existing contract, remediate and validate it without asking for another routine approval. Do not invent adjacent work merely to keep moving.

Before ending, state why stopping is necessary. If another requested workflow intentionally stops while a broader governed objective remains active and a safe next invocation is durably reconstructible, append the smallest `Next:` or `Next chat:` navigation without executing it in the current context. Prefer the governing objective for `/go` when an intermediate artefact is not the complete lifecycle target, and use `/fix` only when bounded remediation is already authorised. If EXTERNAL_REQUIRED is human-operated external execution, include the explicit executable external action and the evidence to return; a slash command is not a substitute. If DECISION_REQUIRED applies, use the decision capsule and do not add a command that bypasses it. If BLOCKED applies, do not manufacture `/go`, `/fix`, or `/review` merely to offer motion. If COMPLETE applies, state that no further action is required. If none of EXTERNAL_REQUIRED, DECISION_REQUIRED, BLOCKED, or COMPLETE applies, apply the effective continuation mode: under `auto`, continue the next authorised same-context action; under `suggest`, emit the smallest safe navigation without entering the next workflow; under `stop`, end the requested deliverable while preserving any router-required navigation.
```

## Inputs

- `<TASK_OR_OBJECTIVE>` — the bounded engineering objective and any relevant governing issue/plan/reference.

## What it does

Separates genuine human decisions and capability boundaries from ordinary lifecycle status, reducing repeated “proceed?” interactions while retaining fail-closed behaviour. It applies the router-owned continuation preference only after hard constraints have been satisfied, so local workflow records do not accidentally become terminal states and `auto` cannot manufacture authority. When a capability boundary genuinely requires human-operated external execution, it reduces the human role to performing one explicit, complete action and returning the requested evidence rather than working out how to continue. Material execution-state hand-offs use the operational-artifact contract so complex procedures can be materialised with coupled guards and bounded evidence while genuinely atomic commands remain inline. A genuine context-transfer boundary may instead use a minimal reconstructible next invocation without weakening the external-execution contract. Returned external evidence is scoped to the named check and governed work resumes automatically when existing authority already determines what follows. When a human decision is genuinely required, it presents a compact device-neutral decision capsule and resumes governed autonomous progression after an unambiguous bounded response.

## Boundaries / limitations

This prompt never overrides repository-local policy or grants credentials, production authority, destructive-action authority, or permission to widen scope. Autonomy is limited to actions already justified by the governing objective and evidence. Continuation mode is a preference, never authority. Suggested next invocations are navigation only. An external handoff must not expose secret values, invent an unsafe procedure, or substitute shorthand navigation for a complete human-operated external action merely to avoid a stop. Artifact delivery is a hand-off mechanism, never new execution or mutation authority; unavailable file delivery must not trigger a large fragile transcript fallback. Returned observations are evidence, not new authority. Short natural-language or voice responses are authority only when their decision referent is unambiguous; materially changed proposals must be re-presented rather than inheriting stale acceptance.

## Status

`tested`
