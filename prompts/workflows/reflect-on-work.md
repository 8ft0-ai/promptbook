# Reflect on completed work

## Purpose

Compare expectations with observed outcomes and extract justified lessons about reasoning, process, and results at the narrowest supported scope.

## When to use

Use for a bounded retrospective after or during governed work when the operator wants to understand what worked, what surprised us, and what should be learned without performing a fresh independent review.

## Prompt

```text
Reflect on <BOUNDED_EPISODE> using the evidence available for that episode.

Recover the expected result or process where available and the observed outcome. Preserve subject, provenance, scope, and currentness. Do not generalise a local episode merely because a broader lesson sounds plausible.

Compare expectation with outcome. Identify what worked, surprises, failed assumptions, unnecessary cost, reasoning errors, or process weaknesses supported by evidence. Derive episode-bound lessons. Distinguish local lessons from candidates that might justify later generalisation. Suggest follow-up without activating or authorising it.

Report proportionately:

EXPECTED
OBSERVED
WHAT WORKED
WHAT DID NOT / SURPRISED
LESSONS
POSSIBLE FOLLOW-UP
SCOPE OF LESSON

Keep lessons traceable to the episode and evidence from which they were derived.

Reflection is not fresh independent review. Self-assessment is allowed, but it cannot satisfy fresh independent review, approve a candidate, expand active scope, establish a decision, persist portfolio policy, mutate governed state, cause external effects, or create authority. A proposed reusable lesson remains a candidate until an appropriate learning/retention or repository-governance mechanism promotes it.

A valid result may be NO_JUSTIFIED_RESULT, BLOCKED_BY_MISSING_INPUT, STALE_INPUT, or NO_CHANGE_RECOMMENDED. Do not manufacture a lesson or process change merely because reflection was requested.
```

## What it does

Creates a bounded retrospective that separates observed episode evidence from lessons and possible follow-up, while keeping local learning from silently becoming policy or approval evidence.

## Boundaries / limitations

This workflow is read-only and may be self-assessment. It cannot satisfy fresh independent review, activate proposed follow-up, automatically promote a local lesson, establish decisions, mutate governed state, cause external effects, or create authority.

## Status

`experimental`
