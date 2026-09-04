# Workflow router

This directory is the canonical Promptbook entry point for governed engineering workflow continuation.

Point the agent here when you want it to determine the appropriate reusable workflow from the current task state rather than choosing an individual prompt yourself. The router does not create unrelated authority: platform safety rules, explicit task authority, repository-local instructions and current authoritative evidence remain higher precedence. An explicit shorthand command may carry only the narrow authority intrinsic to the operation defined for that command; it never supplies unrelated repository or lifecycle authority.

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

When a user message begins with one of these commands, treat it as a concise intent selector. Resolve an omitted target from the current conversation and authoritative repository/task state only when that is unambiguous. Commands do not grant authority beyond the narrow operation authority explicitly defined here, bypass repository policy, weaken freshness or independence requirements, or turn unavailable capabilities into available ones. Any intrinsic operation authority is bounded to the requested command and does not become remediation, merge, release, deployment, settings, credential, production, or other unrelated authority.

- `/go [target]` — continue the governed objective through this router. If the target is already established, `/go` alone means perform the next authorised, safely decidable action rather than merely describing the next gate or asking for a routine `proceed` confirmation. Natural-language qualifiers such as `/go until the next genuinely fresh review boundary` are allowed.
- `/review [target]` — request a substantive independent review using [Fresh independent review](fresh-independent-review.md). For a GitHub pull request, ordinary `/review` includes the narrow authority to durably record the requested review on GitHub after refreshing the exact candidate/head and applying repository/platform constraints. `/review --read-only [target]`, or an unambiguous natural-language equivalent such as `review without mutation` or `review only in chat`, performs the same assessment with zero GitHub write-back. Treat the review disposition as the requested final deliverable unless the user explicitly asks to continue afterwards. Review-recording authority does not grant remediation, merge, release, deployment, issue-closure, workflow-dispatch, settings, credential, cloud, runtime, production, or unrelated mutation authority. If the current context is not genuinely fresh for the required decision, first resolve whether an eligible genuinely isolated fresh-review context can be established under the fresh-review and resolved-run-context contracts. Invoke the bounded `/review` operation there when isolation is provable; use [Next-session handover](next-session-handover.md) and stop as `EXTERNAL_REQUIRED` only when no eligible/provable isolated review context is available. Never substitute author-side reasoning for independent evidence.
- `/plan [target]` — use [Plan an issue](../engineering/plan-an-issue.md). Planning remains non-implementation work unless separate authority says otherwise.
- `/implement [target]` — use [Implement an approved issue](../engineering/implement-an-approved-issue.md). The target must already be sufficiently approved/determined and repository mutation must already be authorised.
- `/fix [target]` — use [Remediate review findings](../engineering/remediate-review-findings.md) for objectively bounded findings under existing authority. Preserve any required fresh re-review boundary after changing the candidate.
- `/handoff [target]` — use [Next-session handover](next-session-handover.md). The handoff is the final deliverable; do not execute the handed-off task in the current context.
- `/status [target]` — reconstruct decision-critical current state and report concise authoritative status read-only. Do not mutate, merge, dispatch, or otherwise continue the governed task unless the user separately requests continuation.

For a conceptual map of `/go` state, authority, capability, evidence rebinding and terminal boundaries, see [`/go` lifecycle](../../guides/go-lifecycle.md). The router remains the canonical behavioural contract.

Keep the command set small. `--read-only` is the one explicit `/review` modifier justified by the write-back boundary; otherwise prefer natural-language qualifiers over inventing flags or a larger command grammar.

For every substantive `/review`, discovering a material blocker ends approval eligibility but does not end the substantive inspection. Complete the bounded decision-critical review surface for the exact candidate before recording the disposition; for `CHANGES REQUIRED`, report all material blockers discovered across that completed surface. The detailed coverage model and re-review rules live in [Fresh independent review](fresh-independent-review.md); the router does not replace them with a universal checklist.

When a completed review exposes materially related blockers, synthesise their relationship before recommending `/fix`: challenge whether they indicate a shared invariant, mechanism, trust boundary, or failing abstraction rather than treating recurrence mechanically. This relationship assessment does not widen `/fix`; an invariant/boundary correction is eligible only when it is objectively the minimum safe correction and already within existing remediation authority. Otherwise expose the real planning, decision, or authority boundary rather than silently converting a broader redesign into bounded remediation.

## Continuation policy

Continuation mode is a preference layer owned by this router. Apply it only after all hard governance constraints have been satisfied. A specialised workflow's local output, disposition, implementation record, remediation record, or other workflow record is not permission to end a routed objective in an unexplained intermediate state.

The supported continuation modes are:

- `auto` — enter the next safely authorised and executable workflow automatically. `auto` cannot make a non-fresh current context review its own work; when independent review is the next gate it may cross that hard boundary only by invoking an eligible genuinely isolated fresh-review context under the bounded `/review` profile. If no such context is eligible/provable, the boundary remains a stop and uses the existing manual fallback.
- `suggest` — do not enter the next workflow in this invocation. When a broader objective remains active, emit the smallest safely determined `Next:` or `Next chat:` navigation.
- `stop` — treat the explicitly requested deliverable as the end of this invocation and do not enter another workflow. `stop` does not suppress required terminal-state classification. When a broader governed objective is already active and its next invocation is safely determined, router postconditions may still expose that navigation unless the user explicitly requested no continuation guidance.

Hard constraints always win over continuation preferences. These include platform safety, explicit task authority, repository-local mandatory policy, fresh-independence requirements, required validation, current authoritative evidence, accepted governance records that require a stop or hand-off, and any other mandatory control established by the governing task. A continuation preference cannot create or bypass mutation, merge, deploy, credential, production, acceptance, review, validation, security, or scope authority. An eligible isolated review context satisfies a freshness requirement through independent adjudication; it does not weaken that requirement or make the authoring context fresh.

Within the remaining continuation-preference layer, resolve the effective mode in this order:

1. explicit current-user qualifier, such as `review only`, `continue afterwards`, or `/go until ...`;
2. repository/task-specific continuation preference, when one exists and is not already a mandatory hard constraint;
3. managed Project continuation preference, when one exists;
4. Promptbook command default.

The command defaults are:

| Command | Default continuation mode |
| --- | --- |
| `/go` | `auto` |
| `/implement` | `auto` |
| `/fix` | `auto` |
| `/review` | `suggest` |
| `/plan` | `suggest` |
| `/status` | `stop` |
| `/handoff` | `stop` |

A lower-precedence preference may choose only among actions already permitted by higher-precedence constraints. Navigation emitted under `suggest` or `stop` is navigation metadata only and never supplies authority to the receiving invocation.

## Routing

Before routing, inspect the current conversation and the authoritative repository or task state needed for the next decision. Stale summaries are navigation aids, not authority. Select exactly one primary workflow and apply it immediately; routing itself is not a stop point.

Use the first matching case:

1. **A handover or next-session prompt is explicitly the requested deliverable** → [Next-session handover](next-session-handover.md).
   - Produce the handover only. Do not reinterpret a request for a prompt as authority to execute the handed-off task in the current context.

2. **An independent substantive review is required now**.
   - If the current context is genuinely fresh for that decision → [Fresh independent review](fresh-independent-review.md). Reconstruct the decision from the actual candidate and evidence rather than inheriting the authoring conclusion. Freshness is about the context/evidence boundary; it does not require a different GitHub account unless repository-local policy explicitly requires a distinct reviewer identity.
   - If the current context is not genuinely fresh, do not review in it. Resolve whether the execution surface can establish an eligible genuinely isolated review context whose information boundary excludes author-side substantive adjudication and expected conclusion. If yes, invoke [Fresh independent review](fresh-independent-review.md) there using the minimal durable review target or equivalent reconstruction reference. The receiving context must independently bootstrap applicable authority, reconstruct the exact candidate/checks/review state, operate only under the bounded `/review` capability profile, and return a disposition/evidence record bound to the exact candidate inspected. If isolation is unavailable, ambiguous, unprovable, incompatible with repository policy, or would require broader capability than `/review` permits → [Next-session handover](next-session-handover.md). Produce the existing fresh-context review handoff and stop as `EXTERNAL_REQUIRED`.
   - Fresh-review context resolution is an information-boundary mechanism, not an execution-locality class. Do not probe `connected/native`, `hosted/hermetic`, or owner-local execution merely to create reasoning independence. Creating/selecting a context is not authority, and a delegated context must not simulate a repository requirement for another human or formal reviewer.

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

When same-account PR authorship is already established, the repository is operating under the Promptbook single-maintainer model, and no repository-local policy, branch protection, regulation, or explicit task authority requires a distinct reviewer or formal approval status, do not attempt a formal self-`APPROVE` or self-`REQUEST_CHANGES` that the hosting platform cannot record. When review write-back is active, record the exact `APPROVED` / `CHANGES REQUIRED` disposition and concise rationale through a permitted `COMMENT` review or durable repository-local comment, make clear that record is not formal platform review state, then continue the governing workflow according to existing authority. When read-only review is active, do not create that fallback record. That platform limitation is not a terminal state by itself; when it is already known, avoid the pointless failed call rather than using the failure as discovery. If those preconditions are not established, or a stronger rule requires formal or distinct-person approval, preserve that requirement and fail or hand off rather than assuming the single-maintainer fallback. Do not invent another account, fake formal approval, or bypass a rule that genuinely requires a formal or distinct-person approval.

For an intermediate `CHANGES REQUIRED`, perform an objectively determined, already-authorised minimum-safe remediation and validation before stopping. The context that performs that remediation is no longer fresh for the changed candidate, so route the exact remediated candidate to a new genuinely fresh context; when an eligible isolated review context can be established automatically, use it, and otherwise use the existing manual fresh-context fallback. That new fresh context may still operate through the same maintainer account. For `APPROVED`, continue already-authorised merge, verification and close-out even when a formal self-approval cannot be recorded, unless repository rules make that formal status a real prerequisite.

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

- `EXTERNAL_REQUIRED` — the next required action cannot legitimately be performed inside the eligible governed mechanism/context available to the current workflow, existing authority is sufficient, and one concrete complete external action can resolve it. For human-operated execution, resolve execution locality proportionately before selecting this state; one unavailable preferred mechanism is not enough when another already-governed no-widening locality can truthfully perform the same action. For genuinely fresh review, first resolve whether an eligible genuinely isolated review context can be established automatically; only when isolation is unavailable or unprovable does the existing manual fresh-context hand-off reach `EXTERNAL_REQUIRED`. Fresh-review context resolution remains distinct from execution locality. For human-operated execution, return the required external action explicitly in the same response: provide a complete copy/paste script or exact commands when appropriate, otherwise exact browser/UI steps or another step-by-step procedure; include material prerequisites, guards, cleanup/prohibitions, and the exact evidence/output the human should return. Do not merely name the missing capability or receiving context, and do not make the human ask how to continue.
- `DECISION_REQUIRED` — a genuine human judgement or authority decision is required; present it as a recommendation-first decision capsule.
- `BLOCKED` — no safe autonomous action, eligible execution locality, eligible isolated review context where required, complete executable external handoff or concrete human decision can resolve the condition now.
- `COMPLETE` — the governed objective is genuinely finished, including required verification and close-out.

Review readiness, validation results, PR readiness, merge readiness and ordinary next actions are not terminal states by themselves.

## Next-invocation guidance

When a requested workflow intentionally stops while a broader governed objective remains active, append the **smallest safely determined next invocation** after the workflow result. That invocation is navigation metadata only: it identifies how another context can resume from authoritative state, does not execute continuation in the current context, and does not grant approval, mutation, merge, implementation, execution, credential, production, or other authority. The receiving context must reconstruct the decision-critical current state and authority before acting.

Use `Next chat:` for a genuinely fresh-review boundary only when no eligible/provable isolated review context can be established automatically, or when a handover itself is explicitly the requested deliverable. When the exact review target is durably identifiable and sufficient for reconstruction, the manual fallback may be only:

```text
EXTERNAL_REQUIRED — fresh context required

Next chat:
  /review <exact review target>
```

Opening a fresh context is different from human-operated external execution. A shorthand invocation may satisfy the former when durable authoritative sources contain the needed state; it must never replace the complete commands, browser/UI procedure, guards, cleanup/prohibitions, and evidence-to-return required for the latter. An automatically delegated reviewer and a manually opened reviewer are subject to the same fresh-review completeness, exact-candidate, write-back/read-only and repository-policy rules.

When a bounded review was explicitly requested as the final deliverable, an appended `Next:` line does not violate that stop boundary or continue the workflow in the current context. If the review is `APPROVED` and the broader objective remains active, prefer the governing lifecycle object rather than the reviewed intermediate artefact when it lets the receiving context reconstruct the complete lifecycle:

```text
APPROVED

Next:
  /go <governing objective>
```

For `CHANGES REQUIRED`, suggest `/fix <target>` only when the governing contract and existing authority already make bounded remediation the safely determined next path. Do not use a convenience command to manufacture remediation authority.

Fail closed when the next invocation is not safely determined. `DECISION_REQUIRED` keeps the decision capsule and must not be bypassed by a slash command. `BLOCKED` must not manufacture `/go`, `/fix`, or `/review` merely to provide a next step. `COMPLETE` must state that no further action is required rather than inventing continuation.

## Selection and continuation rules

- Select one primary workflow rather than concatenating the prompt set.
- Refresh material current state before consequential actions.
- Preserve repository-local authority, validation requirements, security boundaries and explicit task constraints.
- Treat access or capability as distinct from permission.
- Prefer the minimum safe change and fail closed when decision-critical evidence is missing.
- Do not ask for routine `proceed` confirmations when existing authority and evidence already determine the safe action.
- When a required independent review cannot run in the current context because that context authored or materially shaped the candidate, first resolve an eligible genuinely isolated review context. Supply only the minimal durable target/reconstruction reference, require independent bootstrap and candidate/evidence reconstruction, constrain the child to the ordinary `/review` operation ceiling, and bind the result to the exact candidate inspected. Do not pass author-side substantive conclusions or hidden reasoning as review evidence. If isolation cannot be proved, repository policy requires a distinct human/formal reviewer, or the child would require broader authority, preserve the manual fresh-context fallback or stronger policy boundary. Do not retry an equivalent failed delegation indefinitely while the relevant target/isolation/capability state is unchanged.
- When human-operated `EXTERNAL_REQUIRED` is being considered for an already-authorised action, first resolve whether an eligible connected/native, hosted/hermetic, or bounded owner-local executor can truthfully perform the same action without widening projected capability. Inspect only authoritative repository/task execution surfaces relevant to that action; prefer established maintained capabilities over generated shell transport. If another eligible locality exists, use it instead of handing the operation to the owner. If the action genuinely depends on owner-local/private state and no bounded executor can perform it, or no other governed locality can truthfully establish the required result, then use the complete external-action rules below. Do not use locality selection to bypass configured capability suppression, stale guards, profile denial, or missing authority. Fresh-review context resolution is separate and is not part of this locality ladder.
- When `EXTERNAL_REQUIRED` applies, reduce the human role to performing one explicit external action and returning its requested evidence. Scripts or command sequences presented as executable must be complete and self-contained for the stated operation; never expose secret values or present a truncated fragment as the handoff. If an equivalent valid external handoff is already durable and decision-critical state has not materially changed, reuse it after refreshing stale-able guards instead of repeating capability discovery. A capability limitation with sufficient authority is not itself `DECISION_REQUIRED`; if the safe external procedure cannot be determined completely, surface the real decision or blocker instead of a vague handoff.
- Treat an unambiguous returned external observation such as `PASS` or `FAIL <material defect>` only as evidence for the named check, never as new mutation, merge, production, close, or acceptance authority. After such evidence returns, resume the governing workflow automatically when existing authority already determines the next action; before any consequential mutation, refresh only the decision-critical state capable of invalidating that evidence or action. Do not delegate already-established machine-verifiable checks to the human. On `FAIL`, preserve fail-closed behaviour and route the defect through the existing governed scope and authority rather than treating the observation as acceptance.
- When `DECISION_REQUIRED` applies, present the decision capsule instead of making the user copy an approval phrase or repository identifier. Once an unambiguous `ACCEPT` or `CHOOSE` response is safely bound and refreshed, continue any already-authorised routine work without another `proceed` confirmation.
- Output or deliverable constraints inside a selected workflow apply to that workflow's record. They do not override this router's continuation semantics. After recording the local workflow result, return control to the router and apply the effective continuation mode unless a higher-precedence hard constraint or explicit current-user qualifier requires stopping.
- A fresh review disposition does not itself create mutation authority beyond the review-record write already intrinsic to an ordinary `/review`. When fresh review is an intermediate gate under this router, record its single clear disposition and concise rationale according to the selected write-back/read-only mode, then return control to the governing workflow. If a delegated fresh reviewer was used, refresh the exact candidate and review state before continuation and discard stale review evidence if the candidate moved. If `CHANGES REQUIRED` identifies a bounded defect whose minimum-safe remediation is objectively determined and already authorised, continue through autonomous progression to remediate and validate it without another routine approval. Because that context then authored the changed candidate, route the new candidate to a genuinely fresh review context before any gate requiring independence. A single-maintainer project may use the same GitHub identity in that new fresh context. If the disposition is `APPROVED`, continue already-authorised merge, verification and close-out work rather than stopping at review completion or at a platform refusal to record formal self-approval, unless repository-local rules make that approval status mandatory.
- A requested handover is terminal for the current deliverable; execution belongs to the receiving context.
- Do not invent adjacent work after the governed objective is complete.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Documentation assessment workflow](documentation-assessment.md) — discover and approve representative reader tasks, then continue a substantive documentation assessment with a pinned external method.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context, including when an eligible isolated review context is delegated by the governing workflow.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary, retaining manual fresh-review context transport as the fallback when automatic isolation cannot be established.
