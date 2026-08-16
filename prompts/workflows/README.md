# Workflow router

This directory is the canonical Promptbook entry point for governed engineering workflow continuation.

Point the agent here when you want it to determine the appropriate reusable workflow from the current task state rather than choosing an individual prompt yourself. The router does not grant authority: platform safety rules, explicit task authority, repository-local instructions and current authoritative evidence remain higher precedence.

## Using the router

For ordinary continuation:

```text
Use `8ft0-ai/promptbook` → `prompts/workflows/README.md` as the workflow entry point.
Reconstruct the material current state and continue the governed work with minimal human intervention.
```

For a bounded approval:

```text
Follow `8ft0-ai/promptbook` → `prompts/workflows/README.md`.
Approved — proceed.
```

Do not manually choose a workflow when this router can determine the route from current evidence.

## Shorthand commands

When a user message begins with one of these commands, treat it as a concise intent selector. Resolve an omitted target from the current conversation and authoritative repository/task state only when that is unambiguous. Commands do not grant authority, bypass repository policy, weaken freshness or independence requirements, or turn unavailable capabilities into available ones.

- `/go [target]` — continue the governed objective through this router. If the target is already established, `/go` alone means perform the next authorised, safely decidable action rather than merely describing the next gate or asking for a routine `proceed` confirmation. Natural-language qualifiers such as `/go until the next genuinely fresh review boundary` are allowed.
- `/review [target]` — request a substantive independent review using [Fresh independent review](fresh-independent-review.md). Treat the review disposition as the requested final deliverable unless the user explicitly asks to continue afterwards. If the current context is not genuinely fresh for the required decision, use [Next-session handover](next-session-handover.md) and stop as `EXTERNAL_REQUIRED` rather than substituting author-side reasoning.
- `/plan [target]` — use [Plan an issue](../engineering/plan-an-issue.md). Planning remains non-implementation work unless separate authority says otherwise.
- `/implement [target]` — use [Implement an approved issue](../engineering/implement-an-approved-issue.md). The target must already be sufficiently approved/determined and repository mutation must already be authorised.
- `/fix [target]` — use [Remediate review findings](../engineering/remediate-review-findings.md) for objectively bounded findings under existing authority. Preserve any required fresh re-review boundary after changing the candidate.
- `/handoff [target]` — use [Next-session handover](next-session-handover.md). The handoff is the final deliverable; do not execute the handed-off task in the current context.
- `/status [target]` — reconstruct decision-critical current state and report concise authoritative status read-only. Do not mutate, merge, dispatch, or otherwise continue the governed task unless the user separately requests continuation.

Keep the command set small. Prefer natural-language qualifiers over inventing flags or a larger command grammar.

## Routing

Before routing, inspect the current conversation and the authoritative repository or task state needed for the next decision. Stale summaries are navigation aids, not authority. Select exactly one primary workflow and apply it immediately; routing itself is not a stop point.

Use the first matching case:

1. **A handover or next-session prompt is explicitly the requested deliverable** → [Next-session handover](next-session-handover.md).
   - Produce the handover only. Do not reinterpret a request for a prompt as authority to execute the handed-off task in the current context.

2. **An independent substantive review is required now**.
   - If the current context is genuinely fresh for that decision → [Fresh independent review](fresh-independent-review.md). Reconstruct the decision from the actual candidate and evidence rather than inheriting the authoring conclusion.
   - If the current context is not genuinely fresh → [Next-session handover](next-session-handover.md). Produce a complete fresh-context review handoff and stop as `EXTERNAL_REQUIRED`; do not substitute author-side reasoning for independent evidence.

3. **A newly supplied bounded approval or execution authority applies to the current proposal or action** → [Autonomous progression](autonomous-progression.md).
   - Identify the exact proposal or action being authorised.
   - Refresh decision-critical state and verify that the proposal/action and its authority boundary remain materially unchanged.
   - Consume the approval or authority once, only for that bounded object, then continue routine governed work through autonomous progression.
   - Do not treat approval as authority to expand scope, weaken controls or accept a materially changed proposal. Escalate a genuinely new human choice as `DECISION_REQUIRED`.

4. **Ordinary governed continuation** → [Autonomous progression](autonomous-progression.md).
   - Continue while current policy, evidence, scope and available capabilities safely determine the next action.

5. **No safe route fits** → fail closed.
   - Do not invent work, authority or a workflow mapping merely to keep moving.
   - Use the terminal-state rules below to identify the real boundary.

## Terminal states

A routed task should end only as one of these states:

- `EXTERNAL_REQUIRED` — the next required action cannot legitimately be performed in the current environment, but a complete executable handoff can resolve it.
- `DECISION_REQUIRED` — a genuine human judgement or authority decision is required.
- `BLOCKED` — no safe autonomous action, executable external handoff or concrete human decision can resolve the condition now.
- `COMPLETE` — the governed objective is genuinely finished, including required verification and close-out.

Review readiness, validation results, PR readiness, merge readiness and ordinary next actions are not terminal states by themselves.

## Selection and continuation rules

- Select one primary workflow rather than concatenating the prompt set.
- Refresh material current state before consequential actions.
- Preserve repository-local authority, validation requirements, security boundaries and explicit task constraints.
- Treat access or capability as distinct from permission.
- Prefer the minimum safe change and fail closed when decision-critical evidence is missing.
- Do not ask for routine `proceed` confirmations when existing authority and evidence already determine the safe action.
- Output or deliverable constraints inside a selected workflow apply to that workflow's record. They do not override this router's continuation semantics unless the user or governing task explicitly requested that workflow result as the final deliverable.
- A fresh review disposition does not itself create mutation authority. When fresh review is an intermediate gate under this router, record its single clear disposition and concise rationale, then return control to the governing workflow. If `CHANGES REQUIRED` identifies a bounded defect whose minimum-safe remediation is objectively determined and already authorised, continue through autonomous progression to remediate and validate it without another routine approval. Because that context then authored the changed candidate, route the new candidate to a genuinely fresh review context before any gate requiring independence. If the disposition is `APPROVED`, continue already-authorised merge, verification and close-out work rather than stopping at review completion.
- A requested handover is terminal for the current deliverable; execution belongs to the receiving context.
- Do not invent adjacent work after the governed objective is complete.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary.
