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
   - If the current context is genuinely fresh for that decision → [Fresh independent review](fresh-independent-review.md). Reconstruct the decision from the actual candidate and evidence rather than inheriting the authoring conclusion. Freshness is about the context/evidence boundary; it does not require a different GitHub account unless repository-local policy explicitly requires a distinct reviewer identity.
   - If the current context is not genuinely fresh → [Next-session handover](next-session-handover.md). Produce a complete fresh-context review handoff and stop as `EXTERNAL_REQUIRED`; do not substitute author-side reasoning for independent evidence.

3. **A newly supplied bounded approval or execution authority applies to the current proposal or action** → [Autonomous progression](autonomous-progression.md).
   - Identify the exact proposal or action being authorised. An unambiguous response to the current decision capsule, such as `A`, `accept`, `choose B`, or an equivalent natural-language/voice response, may supply that authority or choice.
   - Refresh decision-critical state and verify that the proposal/action and its authority boundary remain materially unchanged.
   - Consume the approval or authority once, only for that bounded object, then continue routine governed work through autonomous progression.
   - Do not treat approval as authority to expand scope, weaken controls or accept a materially changed proposal. Escalate a genuinely new human choice as `DECISION_REQUIRED`.

4. **A substantive repository documentation assessment is needed and representative reader tasks must be discovered, validated, or assessed together** → [Documentation assessment workflow](documentation-assessment.md).
   - Use this route for broad documentation-quality assessment, navigation or authority problems, or deciding the smallest justified documentation response when reader/task discovery or multi-task validation is part of the work.
   - Do not route ordinary bounded documentation edits, known corrections or explicit drafting tasks through assessment merely because documentation is involved.
   - If one concrete reader task is already known and no multi-task discovery or validation is needed, use [Repository documentation assessment](../documentation/repository-assessment.md) as the proportionate single-task path.

5. **Ordinary governed continuation** → [Autonomous progression](autonomous-progression.md).
   - Continue while current policy, evidence, scope and available capabilities safely determine the next action.

6. **No safe route fits** → fail closed.
   - Do not invent work, authority or a workflow mapping merely to keep moving.
   - Use the terminal-state rules below to identify the real boundary.

## Single-maintainer repositories

A single-person project may preserve independent review by using a genuinely fresh context while reusing the same repository owner/GitHub identity. Do not equate a distinct reviewer account with a fresh reasoning context unless repository-local policy, branch protection, regulation, or explicit task authority actually requires distinct identities.

If the hosting platform refuses a formal self-review on an own PR, that platform limitation is not a terminal state by itself. Record the exact `APPROVED` / `CHANGES REQUIRED` disposition and concise rationale in a durable repository-local comment or other permitted record, then continue the governing workflow according to existing authority. Do not invent another account, fake formal approval, or bypass a rule that genuinely requires a formal or distinct-person approval.

For an intermediate `CHANGES REQUIRED`, perform an objectively determined, already-authorised minimum-safe remediation and validation before stopping. The context that performs that remediation is no longer fresh for the changed candidate, so route the exact remediated candidate to a new genuinely fresh context; that new context may still operate through the same maintainer account. For `APPROVED`, continue already-authorised merge, verification and close-out even when a formal self-approval cannot be recorded, unless repository rules make that formal status a real prerequisite.

## Decision capsules

When a genuine human decision is required, do not end with a repository identifier or approval sentence the user must copy. Present the smallest concrete decision as a compact recommendation-first **decision capsule**.

For multiple meaningful alternatives, use compact option labels:

```text
DECISION_REQUIRED — Deployment mechanism

Recommended: A

A — GitHub Actions + Workload Identity
B — Cloud Build
C — Defer
```

For approval of one bounded proposal, use semantic choices rather than manufacturing A/B/C:

```text
DECISION_REQUIRED — Apply repository protection?

Recommended: ACCEPT

ACCEPT — Apply the approved bounded settings
REJECT — Do not apply them
CHANGE — Revise the proposal
```

Put recommendation and choices first. Add material authority, risk, or governance detail below the choices only when it affects the decision.

The canonical response protocol is semantic intent, not slash-command syntax:

- `ACCEPT` — accept the recommended bounded option;
- `REJECT` — reject only the presented proposal or choice;
- `CHOOSE <option>` — select a presented option;
- `CHANGE <instruction>` — request a revision without approving the revision.

Clear natural-language, short-form, touch, or voice equivalents may express the same intent when exactly one unresolved decision and its referent are unambiguous. Examples include `A`, `Choose A`, `yes`, `go ahead`, `accept the recommendation`, or naming the option directly. Slash aliases may be understood as conveniences, but they are not the protocol and are not added to the public shorthand-command vocabulary.

Bind every capsule to one concrete unresolved decision and the authoritative proposal/evidence needed to interpret it: the decision target, proposal or revision identity, recommendation, and bounded authority/effect of acceptance. The user should not normally need to repeat those identifiers.

Before consequential mutation after `ACCEPT` or `CHOOSE`, refresh decision-critical state. If the proposal materially changed, do not silently migrate the earlier response to the new proposal; re-present the decision. Consume accepted authority once for the bounded object only, then resume governed autonomous progression immediately when existing authority permits it.

`REJECT` does not implicitly close the issue, abandon the objective, undo prior work, or choose another option. Re-route from the changed decision state and present another recommendation when one is safely determined. `CHANGE` requests revision; after revising, re-present the decision unless the user's wording explicitly grants authority for the revised proposal.

If more than one unresolved decision exists, or a short response such as `yes`, `A`, or `accept` has more than one plausible referent, fail closed rather than guessing. Repository-local policy, validation, security controls, branch protection, and explicit task authority continue to take precedence.

See [Decision capsules](../../guides/decision-capsules.md) for the device-neutral interaction pattern and examples.

## Terminal states

A routed task should end only as one of these states:

- `EXTERNAL_REQUIRED` — the next required action cannot legitimately be performed in the current environment, but a complete executable handoff can resolve it.
- `DECISION_REQUIRED` — a genuine human judgement or authority decision is required; present it as a recommendation-first decision capsule.
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
- When `DECISION_REQUIRED` applies, present the decision capsule instead of making the user copy an approval phrase or repository identifier. Once an unambiguous `ACCEPT` or `CHOOSE` response is safely bound and refreshed, continue any already-authorised routine work without another `proceed` confirmation.
- Output or deliverable constraints inside a selected workflow apply to that workflow's record. They do not override this router's continuation semantics unless the user or governing task explicitly requested that workflow result as the final deliverable.
- A fresh review disposition does not itself create mutation authority. When fresh review is an intermediate gate under this router, record its single clear disposition and concise rationale, then return control to the governing workflow. If `CHANGES REQUIRED` identifies a bounded defect whose minimum-safe remediation is objectively determined and already authorised, continue through autonomous progression to remediate and validate it without another routine approval. Because that context then authored the changed candidate, route the new candidate to a genuinely fresh review context before any gate requiring independence. A single-maintainer project may use the same GitHub identity in that new fresh context. If the disposition is `APPROVED`, continue already-authorised merge, verification and close-out work rather than stopping at review completion or at a platform refusal to record formal self-approval, unless repository-local rules make that approval status mandatory.
- A requested handover is terminal for the current deliverable; execution belongs to the receiving context.
- Do not invent adjacent work after the governed objective is complete.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Documentation assessment workflow](documentation-assessment.md) — discover and approve representative reader tasks, then continue a substantive documentation assessment with a pinned external method.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary.
