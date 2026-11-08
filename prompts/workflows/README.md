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

The normal public surface is:

- `/go [target]` — continue the governed objective through repeated safely authorised governed transitions until a real boundary. If the target is already established, `/go` reconstructs current state instead of asking the operator to transport routine lifecycle evidence.
- `/step [target]` — execute exactly one safely authorised governed transition, including verification intrinsic to establishing that transition's result, re-resolve once, report what follows, and stop. If the next result is a real boundary rather than an executable transition, report the boundary without consequential mutation.
- `/next [target]` — read-only. Reconstruct the same governed state used by `/go` and `/step`, then report the single next governed transition or real boundary without executing it. Natural-language "what's next?" has the same semantics.
- `/status [target]` — read-only. Reconstruct and report broader authoritative current state, decision-critical identity, blocker/boundary, the same next transition reported by `/next`, what `/go` would do, and minimum decision-critical evidence.
- `/help [topic-or-question]` — read-only advisory interpretation of the same resolved state. Recommend what the operator should do and why, explain material alternatives or blockers, and answer prospective questions without executing the described action or creating authority.
- `/plan [target]` — use [Plan an issue](../engineering/plan-an-issue.md). Planning remains non-implementation work unless separate authority says otherwise.
- `/review [target]` — request a substantive independent review using [Fresh independent review](fresh-independent-review.md). For a GitHub pull request, ordinary `/review` includes the narrow authority to durably record the requested review on GitHub after refreshing the exact candidate/head and applying repository/platform constraints. For `REVIEW_TYPE=ARCHITECTURE_CLOSURE` whose closure artefact is durably anchored in a GitHub issue or issue comment, ordinary `/review` likewise includes only the narrow authority to publish one durable closure-review record as a new top-level comment on that owning issue. Treat repository object IDs as locators, not content-version identities: bind the reviewed closure to an edit-sensitive snapshot identity (for example locator plus canonical body digest and repository-native version/update witness), bind the review record to that exact closure snapshot, and bind the review record itself to an edit-sensitive snapshot identity. The created comment ID is therefore a locator component, not sufficient identity by itself. Closure-review records are append-only evidence for this gate; an in-place edit invalidates their fresh-review status and requires a new review record. If no permitted durable repository-native review-record target is available, the assessment may still be reported but cannot satisfy `CLOSURE_REVIEW_REQUIRED`. `/review --read-only [target]`, or an unambiguous natural-language equivalent such as `review without mutation` or `review only in chat`, performs the same assessment with zero GitHub write-back and therefore cannot by itself satisfy a durable closure-review gate. Review-recording authority does not grant remediation, merge, release, deployment, issue-closure, settings, credential, production, candidate authoring, or unrelated mutation authority.
- `/fix [target]` — use [Remediate review findings](../engineering/remediate-review-findings.md) for objectively bounded findings under existing authority. If review-response synthesis has not yet been satisfied, perform that non-mutating synthesis first. Explicit `/fix` performs bounded remediation, required validation, and a proportional author-side remediation-readiness sweep, freezes the exact resulting candidate when review-ready, then returns control rather than silently continuing into fresh review, merge, or later lifecycle effects. The readiness sweep is remediation evidence, not review or approval.
- `/save [target]` — persist the current material result in the smallest correct durable repository-native home. The command carries only the narrow intrinsic persistence authority defined by the resolved-run-context contract; it does not grant branch/PR/code/cross-repository/production mutation authority.
- `/prompt [target-or-request]` — generate the shortest safe context-transfer artefact only. It may generate a continuation, delegation, or independent-review prompt contract, but it does not execute the prompt, create another context, transfer authority, establish freshness, or change the current governed lifecycle state.
- `/risk [target-or-question]` — read-only. Use [Assess risk](assess-risk.md) to characterise material risk, controls, residual risk, uncertainty and legitimate disposition boundaries. Risk assessment does not accept risk, establish owner decisions, satisfy violated invariants, or create execution authority.
- `/reflect [target-or-episode]` — read-only. Use [Reflect on completed work](reflect-on-work.md) to compare expectations with observed outcomes and derive justified episode-bound lessons. Reflection may be self-assessment but cannot satisfy fresh independent review, activate follow-up scope, or automatically promote a local lesson to policy.
- `/challenge [target-or-proposal]` — read-only. Use [Challenge assumptions](challenge-assumptions.md) to adversarially test assumptions, evidence, model, contract, or proposed course. Challenge may question the contract itself but cannot approve a candidate, amend that contract, or satisfy a qualified review gate.

For one authoritative resolved snapshot, preserve this projection invariant:

```text
/next   -> reports transition T or boundary B
/status -> reports Next: T/B
/help   -> advice is based on T/B
/step   -> executes T only when T is ALLOW and executable; otherwise reports B
/go     -> repeats the same transition loop until B
```

Keep the command set small. `--read-only` remains the one explicit `/review` modifier justified by a write-back boundary; otherwise prefer natural-language qualifiers over inventing flags or a larger command grammar.

## Compatibility intents

These legacy or advanced intents remain understandable for compatibility but are not part of the advertised normal public surface:

- `/implement [target]` — route to [Implement an approved issue](../engineering/implement-an-approved-issue.md) when the target is sufficiently approved/determined and repository mutation is already authorised.
- `/handoff [target]` — compatibility intent for generating a context-transfer prompt when that is the requested deliverable. It must not replace a complete human-operated `EXTERNAL_REQUIRED` execution handoff.
- `/record [target]` — compatibility alias for `/save`.
- `/analyse [target]` — read-only analysis/synthesis intent. When the target is materially stateful/lifecycle-sensitive or the repeated-review escalation rule is established, route through [Stateful invariant analysis](stateful-invariant-analysis.md). It may produce a plan when explicitly requested, but does not create a new lifecycle stage or mutation authority.

Do not advertise compatibility intents as equal public commands.

For ordinary `/go` continuation, **operation + durable target is the normal operator contract**. When the target unambiguously identifies the governed objective, reconstruct machine-recoverable lifecycle state from current authoritative sources rather than requiring the user to copy it into the invocation. Candidate heads, pull-request identities, validation/check runs, review dispositions, durable comment identities and lifecycle stage are evidence to derive when they are unambiguous; conversation history may help locate them but is not authority.

Treat an explicit current-user identity or constraint differently from derived state. A deliberate qualifier such as `/go <target> against exact head <sha>` is an **essential assertion** that constrains the requested operation. Refresh it against authoritative state and do not silently replace it with a newer or different reconstructed value. If an explicit assertion is stale or conflicts with current state, surface the changed-state decision or fail closed under the existing terminal semantics.

Target-only invocation is valid only while reconstruction is unambiguous. If multiple active candidates, conflicting authorities, materially different pending actions, or missing decision-critical evidence prevent a unique safe interpretation, do not guess. Reducing operator input never collapses separate authority boundaries such as candidate approval, merge, release, deployment, or production mutation.

For a conceptual map of `/go` state, authority, capability, evidence rebinding and terminal boundaries, see [`/go` lifecycle](../../guides/go-lifecycle.md). The router remains the canonical behavioural contract.


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
| `/step` | `stop` |
| `/next` | `stop` |
| `/status` | `stop` |
| `/help` | `stop` |
| `/plan` | `suggest` |
| `/review` | `suggest` |
| `/fix` | `suggest` |
| `/save` | `stop` |
| `/prompt` | `stop` |
| `/risk` | `stop` |
| `/reflect` | `stop` |
| `/challenge` | `stop` |

Explicit `/fix` is a scope-control request. Automatic remediation followed by further review/merge/verification progression remains available through `/go`; the bounded `/fix` invocation itself does not silently become `/go`.

Compatibility `/implement` retains its existing implementation workflow behaviour when explicitly invoked, but it is not an advertised normal command. Compatibility `/handoff`, `/record`, and `/analyse` inherit the stop/read-only semantics of the public intent they map to.

A lower-precedence preference may choose only among actions already permitted by higher-precedence constraints. Navigation emitted under `suggest` or `stop` is navigation metadata only and never supplies authority to the receiving invocation.

## Routing

Reconstruct one unambiguous current work target from authoritative repository/task state. This router does not grant unrelated authority. A completed sub-workflow, successful handoff record or preparation report is not the original objective's completion.

For normal `/go`, select [Autonomous progression](autonomous-progression.md): take the next ALLOW and executable goal-advancing action, verify, repeat to the real goal or genuine boundary. For `/step`, perform exactly one transition. `/next`, `/status` and `/help` project the same resolved transition without executing it.

Resolve special predicates *before* consequential action. Their referenced contracts are then mandatory; otherwise do not load them:

1. **Explicit context-transfer deliverable** → [Next-session handover](next-session-handover.md); this generates navigation, not execution or authority.
2. **Mandatory stateful/architecture analysis, closure review or non-routine route** → [Specialised routing conditions](../../guides/conditional/router-special-routing.md), followed as applicable by [Stateful invariant analysis](stateful-invariant-analysis.md) or [Architecture closure analysis](architecture-closure-analysis.md). A closed-world completeness claim is not self-authorising.
3. **Independent review required** → [Fresh independent review](fresh-independent-review.md); the authoring context cannot claim fresh independence. On material blockers/remediation response/strong-closure recurrence read [Review response and escalation](../../guides/conditional/router-review-response.md); for an eligible solo-maintainer review also read [Single-maintainer rules](../../guides/conditional/router-single-maintainer.md).
4. **Bounded approval received** → verify the exact unchanged proposal, consume approval once for that action, then [Autonomous progression](autonomous-progression.md). A later permission boundary never blocks authorised preceding work.
5. **Broad documentation assessment** → [Documentation assessment](documentation-assessment.md) only when reader/task discovery is needed. Routine edits use ordinary progression.
6. **Ordinary authorised work** → [Autonomous progression](autonomous-progression.md), including routine implementation, troubleshooting, testing and PR preparation.
7. **No safely determinable route** → report the evidenced genuine boundary. Unknown authority never defaults to ALLOW; unfinished work is not by itself BLOCKED.

On a required human decision load [Decision capsules](../../guides/conditional/router-decision.md). On manual handoff or stop load [Next-invocation guidance](../../guides/conditional/router-terminal-handover.md). For contested command precedence or non-standard lifecycle edges use the specialised routing conditions linked in case 2 above.

Conditional references do not become optional rules: where their applicability is established, read and apply them in full. If required canonical content is unavailable, fail closed rather than approximating it. Do not pre-load all special rules for ordinary work.

## Selection invariants

- Do not pass author-side substantive conclusions to an allegedly fresh reviewer; it must independently reconstruct and adjudicate exact evidence. Do not retry an equivalent failed delegation indefinitely without new identity or eligibility evidence.
- A fresh review disposition does not itself create mutation authority. After recording an intermediate result, return control to the governing workflow and apply the effective continuation mode; do not mistake a sub-workflow for objective completion.
- Treat a returned external PASS or FAIL observation only as evidence for the named check; it never supplies approval or new mutation authority. On unambiguous sufficient evidence, resume the governing workflow automatically after refreshing material state: refresh only the decision-critical state, perform eligible machine-verifiable checks rather than delegating them to the human, and on `FAIL`, preserve fail-closed behaviour while resolving an authorised remediation.
- After an unambiguous bounded approval, verify the current proposal, consume its authority only once, and continue any already-authorised actions without another `proceed` confirmation. Do not demand a routine `proceed` confirmation when current authority and evidence already determine the next action. No approval crosses an independent merge, release, deployment or production boundary.

## Terminal states

A routed task should end only as one of these states:

- `EXTERNAL_REQUIRED` — the next required action cannot legitimately be performed inside the eligible governed mechanism/context available to the current workflow, existing authority is sufficient, and one concrete complete external action can resolve it. For human-operated execution, resolve execution locality proportionately before selecting this state; one unavailable preferred mechanism is not enough when another already-governed no-widening locality can truthfully perform the same action. For genuinely fresh review, first resolve whether an eligible genuinely isolated review context can be established automatically; only when isolation is unavailable or unprovable does the existing manual fresh-context hand-off reach `EXTERNAL_REQUIRED`. Fresh-review context resolution remains distinct from execution locality. For human-operated execution, return the required external action explicitly in the same response: provide a complete copy/paste script or exact commands when appropriate, otherwise exact browser/UI steps or another step-by-step procedure; include material prerequisites, guards, cleanup/prohibitions, and the exact evidence/output the human should return. Do not merely name the missing capability or receiving context, and do not make the human ask how to continue.
- `DECISION_REQUIRED` — a genuine human judgement or authority decision is required; present it as a recommendation-first decision capsule.
- `BLOCKED` — no safe autonomous action, eligible execution locality, eligible isolated review context where required, complete executable external handoff or concrete human decision can resolve the condition now.
- `COMPLETE` — the governed objective is genuinely finished, including required verification and close-out.

Review readiness, validation results, PR readiness, merge readiness and ordinary next actions are not terminal states by themselves.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Bounded concern lifecycle](bounded-concern-lifecycle.md) — orchestrate explicitly selected finite concern-specific closure packages and empirical convergence without claiming universal semantic completeness.
- [Documentation assessment workflow](documentation-assessment.md) — discover and approve representative reader tasks, then continue a substantive documentation assessment with a pinned external method.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context, including when an eligible isolated review context is delegated by the governing workflow.
- [Assess risk](assess-risk.md) — characterise material risk and legitimate disposition boundaries without accepting risk or manufacturing authority.
- [Reflect on completed work](reflect-on-work.md) — extract justified retrospective lessons without turning self-assessment into review evidence.
- [Challenge assumptions](challenge-assumptions.md) — adversarially test assumptions or governing models without turning challenge into approval.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary, retaining manual fresh-review context transport as the fallback when automatic isolation cannot be established.
- [Stateful invariant analysis](stateful-invariant-analysis.md) — reconstruct materially stateful invariant/lifecycle semantics read-only, including mandatory escalation after repeated materially related review failures.
