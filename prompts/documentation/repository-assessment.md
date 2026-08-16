# Repository documentation assessment

## Purpose

Assess whether repository documentation lets a defined reader complete one known task safely, rather than reviewing documentation for style or coverage in the abstract.

## When to use

Use as the proportionate Level-1/single-task path when the concrete reader task is already known and you need evidence about navigation, authority, missing/contradictory documentation, or the smallest useful documentation improvement for that task. For broader repository assessment where reader groups or representative tasks still need to be discovered or approved, use the [Documentation assessment workflow](../workflows/documentation-assessment.md).

## Prompt

```text
Assess the documentation in <REPOSITORY_OR_DOCSET> for <READER_TASK>.

Start from the entry point a real reader would reasonably receive. Follow the documented path rather than searching broadly for the answer first.

For each material conclusion, distinguish:
- Observation — what the documentation/repository explicitly shows;
- Authority — which source controls the decision when sources differ;
- Inference — a conclusion supported by evidence but not stated directly;
- Uncertainty — information that cannot be established safely from the available documentation.

Determine:
1. whether the reader can complete the task from the documented path;
2. where navigation becomes ambiguous, stale, contradictory, or incomplete;
3. whether a higher-authority repository source resolves the ambiguity;
4. what useful existing material should be retained;
5. the smallest response justified by the evidence: no change, navigation improvement, correction, new explanation, or an explicit authority/decision gap.

Do not invent undocumented intent, policy, ownership, rationale, or product decisions. Do not draft a large documentation rewrite when the observed reader failure is narrower.

Return one primary result: COMPLETE, PARTIAL, BLOCKED, or NOT TESTED, with concise evidence and the smallest sufficient next action.
```

## Inputs

- `<REPOSITORY_OR_DOCSET>` — the repository or bounded documentation set to assess.
- `<READER_TASK>` — the concrete task a named reader should be able to complete.

## What it does

Evaluates documentation through one actual task path, preserves authority boundaries, and allows “no change” or “blocked by missing decision” to be valid outcomes. It intentionally avoids the reader/task discovery and approval machinery needed for a broader Level-2 assessment.

## Boundaries / limitations

This is an assessment prompt, not automatic remediation authority. The quality of the result depends on a realistic, already-known reader task and access to the documentation sources that actually govern it. If the reader task itself is still uncertain, use the broader documentation-assessment workflow first.

## Status

`experimental`
