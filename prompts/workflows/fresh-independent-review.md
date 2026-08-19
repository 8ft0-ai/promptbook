# Fresh independent review

## Purpose

Review a candidate, design, or evidence record from a genuinely fresh context without inheriting the previous session's substantive conclusion.

## When to use

Use when independence is part of the quality or governance boundary: substantive PR review, design review, evidence adjudication, close-out review, or another decision where author-side reasoning should not be treated as approval evidence.

## Prompt

```text
Conduct a fresh independent review of <REVIEW_TARGET> against <GOVERNING_CONTRACT>.

Treat prior summaries, recommendations, and conclusions only as navigation aids. Reconstruct the material authoritative state directly from the actual candidate and decision-critical evidence. Establish the current identities, revisions, checks, review state, and governing requirements needed for this decision.

Reach the substantive conclusion from freshly inspected evidence. Do not inherit the prior session's approval/rejection reasoning, do not weaken the governing contract to obtain approval, and distinguish blocking findings from non-blocking observations.

Fresh independence is a property of this reviewing context and its information boundary, not automatically of the GitHub account used to record the result. In a single-maintainer repository, a genuinely fresh context may use the same maintainer account that authored the PR. Do not treat same-account operation as a loss of independence unless repository-local policy, branch protection, regulation, or explicit task authority requires a distinct reviewer identity.

When same-account PR authorship is already established, the repository is operating under the single-maintainer model, and no repository-local policy, branch protection, regulation, or explicit task authority requires a distinct reviewer or formal approval status, do not attempt a formal self-`APPROVE` or self-`REQUEST_CHANGES` that the hosting platform cannot record. Record the exact disposition and concise rationale directly in a durable PR comment, review comment, issue comment, or other repository-local record permitted by policy, clearly distinguish that record from formal platform review state, then return control to the governing workflow. The inability to record such a formal self-review remains a recording limitation rather than a governance stop by itself; when it is known in advance, avoid the pointless failed call rather than using the failure as discovery. If those preconditions are not established, or a stronger rule requires formal or distinct-person approval, preserve that requirement and fail or hand off rather than assuming the single-maintainer fallback. Do not invent another identity, bypass a required approval, or represent the durable record as a formal platform approval.

If expected state changed, determine what changed and whether the review remains safely decidable; do not fail mechanically merely because an identity moved when the governing contract permits reconciliation.

Return exactly one clear disposition appropriate to the gate (for example APPROVED / CHANGES REQUIRED), followed by concise decisive rationale. For a negative disposition, identify only material blockers that must be resolved.

That single disposition is the review record. If this review was explicitly requested as the final deliverable, stop after recording it. If a governing workflow or router invoked this review as an intermediate gate, return control to that workflow after recording the disposition; do not treat review completion itself as a terminal state.

A review result never creates mutation authority. If CHANGES REQUIRED identifies a bounded defect whose minimum-safe remediation is objectively determined and already authorised by the governing task, the governing workflow may perform and validate that remediation without another routine approval. Once this context authors or materially shapes the changed candidate, it must not claim a fresh independent review of that changed candidate; route it to a genuinely fresh review context before any gate that requires independence. In a single-maintainer repository, that new fresh context may still use the same GitHub maintainer identity.

If the disposition is APPROVED, the governing workflow may continue any already-authorised merge, verification, and close-out work. Do not stop merely because the review gate completed or because the platform cannot record a formal self-approval when the overall governed task still has authorised, safely decidable work remaining. If repository rules genuinely require a distinct reviewer identity or formal approval status, preserve that requirement and fail or hand off according to the governing workflow rather than bypassing it.
```

## Inputs

- `<REVIEW_TARGET>` — the exact PR, commit, design, evidence record, or other candidate to assess.
- `<GOVERNING_CONTRACT>` — the issue, specification, acceptance criteria, design, policy, or explicit review contract.

## What it does

Creates an information boundary between authoring and adjudication and forces the reviewer to inspect the real evidence rather than merely validating a handover summary. When composed inside a governing workflow, it records the independent disposition without turning review completion into an unnecessary conversational stop. It also separates reasoning independence from hosting-platform reviewer identity so single-maintainer projects can retain fresh-context review without inventing extra accounts or false approval gates.

## Boundaries / limitations

Freshness is a property of prior information, not a prompt incantation or a different account name. A context that substantially authored the candidate or already saw the expected answer cannot become independent merely by being told to forget it, even if it uses another account. Conversely, a genuinely fresh context does not cease to be independent merely because a single-maintainer project must use the same GitHub identity. Repository-local requirements for distinct reviewers or formal approvals still take precedence. The review result does not grant mutation authority; any remediation or continuation must already be authorised by the governing task or workflow.

## Status

`tested`
