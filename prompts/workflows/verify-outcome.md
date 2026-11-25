# Verify delivered outcome

## Purpose

Determine whether a specified engineering objective has **observably succeeded** against its governing acceptance criteria, without turning a source-level check, green test suite, transport acknowledgement or review disposition into unearned operational success.

## When to use

Use for read-only `/verify [target]` after work is claimed complete or when the operator asks whether the actual deliverable works. It is an outcome-evidence projection, not a new lifecycle stage. For implementation or repair use `/go`; for a genuinely independent substantive candidate assessment use `/review`.

## Prompt

```text
Verify <TARGET> without mutating the repository or claimed deliverable.

1. BIND: Reconstruct the exact objective, acceptance criteria, target revision or observed artifact, required consumer/operational boundary and applicable repository instructions from current authoritative sources. Mark uncertain requirements and changed identities explicitly.
2. EVIDENCE: For each material criterion, distinguish (a) proposed or authored claims, (b) source inspection, (c) tests/CI, and (d) observed consumer or operational behaviour. Prefer the least-cost sufficient already-authorised read-only check at the lowest relevant observable boundary; test meaningful negative paths when possible. Record evidence identity, time and provenance.
3. ADJUDICATE: Map every criterion to VERIFIED, NOT VERIFIED, FAILED or NOT APPLICABLE with a reason. A passing unit test, green CI, completed PR, successful API transport, process exit or reviewer GO cannot by itself prove a required consumer readback or delivered behaviour. A broken observed application, absent required readback, stale candidate or conflicting evidence blocks a verified-complete claim.
4. REPORT: Give the objective-level disposition: VERIFIED only when every applicable mandatory criterion has sufficient current observable evidence; FAILED when a mandatory criterion is demonstrably unmet; otherwise INCONCLUSIVE. Identify the smallest evidence gap or actionable next check. If a governing lifecycle has required close-out, review, approval or other boundary remaining, state it separately; outcome verification must not satisfy that boundary by assertion.
5. STOP: Do not remediate, write reviews, create a PR, close an issue, merge, deploy, consume credentials, or imply new approval. Do not claim fresh reviewer independence merely because this verification was performed in a different command. Unsupported tool access or missing evidence is INCONCLUSIVE, never a manufactured PASS.
```

## Inputs

- `<TARGET>` — the objective, issue, artifact, integration or result to verify; may be inferred only when unambiguous.

## What it does

Reports an evidence-backed result on the **delivered outcome**, rather than the quality of the proposed implementation. Reuses the observable-outcome sufficiency rules of [Autonomous progression](autonomous-progression.md) and the same governing state used by [Workflow router](README.md), without executing the next governed transition.

## Boundaries / limitations

Read-only by default and by command contract. Never asserts independent review, implementation approval or lifecycle completion when additional governing gates remain. If verification needs a consequential action or unavailable capability, report the missing evidence and the actual boundary instead of silently executing. Avoid invented test evidence or speculative operational claims.

## Status

`experimental`
