---
name: engineering-pr-review
description: Review a fixed pull-request revision substantively and read-only, using repository authority, complete bounded evidence, and explicit independence checks when required.
---

# Engineering PR review

Use for a standalone engineering review of code, configuration, documentation or workflows. This Skill is reusable methodology, **not a replacement for an owning repository's governed `/review` contract** and not permission to record a GitHub review.

## Inputs and authority

- Repository and PR URL/number; governing issue or accepted requirements; intended outcome; requested read-only review scope.
- Exact PR base and head commit SHAs, established from current PR metadata before examining the candidate; access to the full diff and decision-critical evidence.
- Repository-local `AGENTS.md`, applicable policies and review requirements take precedence. If a governed workflow is explicitly requested, follow its own contract rather than silently importing or replacing it with this Skill.
- When an independent review is required, verify an eligible context that did not author or materially shape the candidate or inherit its substantive verdict. A Skill/agent name, a new invocation or a copied prior conclusion does not establish independence.

## Bounded method

1. **Bind identity.** Read the PR metadata, current base/head and complete changed-file diff (all pages); resolve the governing issue, accepted scope/design, unresolved review threads and current checks. Record exact candidate identity. If the head moves, prior candidate-specific findings/validation are not automatically reusable.
2. **Review the actual outcome.** Compare the complete candidate against the promised result, existing repository conventions and authorised scope. Identify unrelated edits, omitted requirements and compatibility or migration impacts.
3. **Inspect risk and proof.** Assess correctness, edge cases, failure/negative paths, security and permission boundaries, data/secret exposure, operational safety, regressions, maintainability, documentation, rollback, and test coverage proportionately. Verify that validation, assertions or thresholds were not weakened and that passing CI does not conceal an unresolved functional problem. Do not claim tests ran unless observed.
4. **Complete the applicable surface.** An early blocker rules out approval but does not end the bounded substantive review. Missing host/integration evidence blocks only dependent assurance or effects; continue safe source inspection, disclose unverified domains, and withhold conclusions that depend on them. Do not label an unexamined applicable domain inapplicable.
5. **Report evidence.** Give material findings with file/line or other precise evidence, consequence and required correction; distinguish blockers from observations and optional suggestions. Prefer one underlying defect explanation over duplicative comments. No findings is not proof of unexamined domains.

## Output

Identify repository, PR, exact base/head, reviewed domains, evidence actually inspected, missing evidence and reviewer-independence eligibility. End with exactly one **logical** disposition: `APPROVED`, `CHANGES REQUIRED`, or `CANNOT ASSESS`. For changes required, report all material blockers found across the bounded review surface. Withhold approval if decision-critical evidence or required independence is missing. A logical disposition is not formal GitHub approval or merge authority.

## Read-only boundary

**Zero GitHub and repository writes.** Do not submit reviews, comments, approvals, issue updates, commits or status changes; do not merge, remediate, deploy, release, change credentials or settings, or infer authority for consequential actions. Provide findings only in the current response. This Skill does not alter local reviewer requirements or grant freshness, execution or write-back authority.
