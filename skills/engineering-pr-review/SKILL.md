---
name: engineering-pr-review
description: Substantive, evidence-backed, read-only review of an exact pull-request revision; apply repository authority and check fresh-review eligibility when required.
---

# Engineering PR review

Use for standalone reviews of code, configuration, documentation or workflows. This Skill is **not a replacement** for an owning repository's governed `/review` contract.

## Inputs and precedence

- Repository and PR URL/number; governing issue, accepted outcome and scope; current checks, full diff and exact base/head commit SHAs.
- Read repository-local `AGENTS.md`, policies and review requirements first: they take precedence. If a governed review was requested, follow its existing contract instead of silently loading it as standalone overhead.
- When independence is required, verify that this reviewer context did not author or materially shape the candidate or inherit a substantive verdict. Skill/agent names do not prove freshness.

## Method

1. **Pin candidate:** reconcile PR metadata, exact head/base and complete diff; examine issue/design, unresolved review threads, relevant source, tests and validation. A moved head invalidates candidate-specific review evidence.
2. **Check outcome:** confirm requirements and intended behaviour, scope discipline and absence of unrelated changes. Inspect correctness, regressions, edge/negative paths, security, permissions and secrets, compatibility, operations, migration, documentation, rollback and maintainability as applicable.
3. **Check proof:** examine whether tests and CI establish the required behaviour without weakened checks, assertions or thresholds. Do not claim tests ran or assurances exist unless observed. A passing check does not overrule functional evidence.
4. **Complete bounded coverage:** finding one blocker does not end inspection of other decision-critical domains. Missing host/integration evidence does not halt safe source-only review; mark dependent assurances unverified and withhold dependent approval. Do not call an applicable unexamined domain inapplicable.
5. **Report:** give concrete blockers with file/line or comparable evidence and consequence; separate material defects from optional observations. Prefer underlying causes over repeated stylistic remarks.

## Result and limits

State exact repository/base/head, inspected and unverified domains, independence eligibility and precisely one logical disposition: `APPROVED`, `CHANGES REQUIRED`, or `CANNOT ASSESS`. List all material blockers found; do not approve with missing decision-critical evidence or required independence.

**Read-only, zero writes:** report in chat only. Do not submit GitHub reviews/comments, change issues, code or settings, merge, remediate, deploy or infer approval/authority. A logical `APPROVED` is not formal GitHub approval or merge permission.
