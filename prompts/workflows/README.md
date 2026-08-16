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

## Routing

Before routing, inspect the current conversation and the authoritative repository or task state needed for the next decision. Stale summaries are navigation aids, not authority. Select exactly one primary workflow and apply it immediately; routing itself is not a stop point.

Use the first matching case:

1. **A handover or next-session prompt is explicitly the requested deliverable** → [Next-session handover](next-session-handover.md).
   - Produce the handover only. Do not reinterpret a request for a prompt as authority to execute the handed-off task in the current context.

2. **The current context is genuinely fresh and an independent substantive review is required now** → [Fresh independent review](fresh-independent-review.md).
   - Reconstruct the decision from the actual candidate and evidence rather than inheriting the authoring conclusion.
   - If independence is required but the current context is not genuinely fresh, use the handover workflow to produce a complete fresh-context review handoff and stop as `EXTERNAL_REQUIRED`.

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

A workflow should stop only as one of these states:

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
- A fresh review disposition does not itself create mutation authority. After the review, continue through autonomous progression only when the governing task already permits that continuation and independence is no longer at risk.
- A requested handover is terminal for the current deliverable; execution belongs to the receiving context.
- Do not invent adjacent work after the governed objective is complete.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary.
