# Operational artifact hand-off

## Purpose

Standardise human-operated external execution hand-offs so non-trivial executable or evidence-producing work crosses the agent/operator boundary as **artifact + invocation + evidence**, rather than relying on the conversation transcript as executable state.

## When to use

Use this contract when a governed workflow requires a human-operated external action and execution fragility, guard coupling, or evidence complexity is material. Keep genuinely atomic commands inline when they are independent of prior conversational state and do not need coupled setup, multi-stage guards, interpreter transitions, or substantial evidence processing.

Typical artifact-preferred signals include heredocs or nested quoting, shell/interpreter transitions, multi-stage variable or environment setup, subshell/file-descriptor behaviour, substantial embedded programs, multiple prerequisite/identity/authority guards that must remain coupled, multi-command diagnostics or reconciliation, local sensitive input that should not be copied into the conversation, or partial execution that would make outcome/evidence ambiguous.

## Prompt

```text
Prepare the smallest safe human-operated external hand-off for <EXTERNAL_ACTION>.

First choose the hand-off form from execution characteristics, not line count:
- use an inline command only when it is genuinely atomic, transcript-independent, and safe to execute as one bounded action;
- prefer a materialised/downloadable artifact when execution fragility, guard coupling, or evidence complexity is material.

For an artifact hand-off, treat the user-visible unit as:

artifact + invocation + bounded evidence

The artifact must start from a clean process and be self-contained for its stated operation. It must declare read-only versus potentially mutating behaviour; state material prerequisites; reject absent, stale, ambiguous, or inherited inputs rather than silently substituting them; bind immutable source/target identity when decision-critical; fail closed before consequential work when authority, identity, prerequisite, or integrity checks fail; and make target/working-directory handling explicit rather than assuming that the artifact's staging directory is the target repository or workspace.

Artifact delivery changes the hand-off mechanism, not authority. Generating, downloading, staging, verifying, or possessing an artifact does not grant mutation, merge, release, deployment, credential, production, destructive-action, or other execution authority that is not already present. A read-only task must remain read-only. A separately authorised mutation must still fail closed when its target, authority, identity, prerequisite, or other guard is not satisfied.

Preserve operating-system and client security protections. Do not routinely disable download quarantine, reputation checks, execution-policy controls, or equivalent protections merely to make the artifact easier to run.

When byte identity or integrity materially matters, provide an expected SHA-256 digest and require a mismatch to fail closed before execution. State explicitly that SHA-256 establishes byte identity/integrity only: a matching digest is not proof of trust, safety, review, authenticity, supply-chain provenance, or execution authority.

Fail closed on destination collisions. Do not silently overwrite an existing canonical artifact or treat a browser-added suffix as an equivalent canonical identity without explicit reconciliation.

Keep artifact creation time distinct from execution/evidence time. If a canonical filename carries a timestamp, define it as artifact creation time. Record execution/evidence time separately in returned evidence.

Use a controlled user-local staging/execution location when practical instead of treating a browser Downloads directory as the normal execution location. Make staging and execution separate simple steps when that is clearer; do not manufacture a clever compound shell command merely to preserve a one-command appearance.

Where the format supports it, small embedded provenance may record non-sensitive facts such as artifact identity, creation time, project/work reference, immutable source identity when material, execution mode, and retention intent. Never embed credentials, secrets, or sensitive local values merely for provenance.

Return bounded continuation evidence rather than requiring an unbounded terminal transcript. A useful result envelope may include artifact identity, digest, creation time, execution time, mode, bounded target identity, PASS/FAIL/BLOCKED result, and only the decision-relevant evidence needed for governed continuation.

Treat generated operational artifacts as ephemeral rather than repository-owned source of truth. Ordinary operational artifacts must not autonomously delete other artifacts. Any tidy operation must be separate, constrained to recognised canonical artifacts, dry-run-first, and fail closed around unknown files, directories, symlinks, or recursive traversal. Repeatedly useful procedures should be promoted through normal governance into repository-owned or explicitly governed shared tooling instead of retaining generated artifacts indefinitely.

Recommended client defaults may make the lifecycle concrete without becoming universal Promptbook requirements. For a ChatGPT-style client, one portable-character filename example is:

CHATGPT_<created-UTC>__<project>__<work-ref>__[<source-sha>__]<description>.<ext>

Here `<created-UTC>` is compact UTC artifact creation time, for example `20260829T021500Z`. A browser Downloads location may be treated as an inbox. On POSIX systems, a client-specific staging example is `${CHATGPT_ARTIFACT_HOME:-$HOME/CHATGPT}`; other clients and operating systems may use an equivalent configured user-local home. A 30-day expiry from the canonical creation timestamp and a `keep/` subdirectory for deliberate temporary retention are useful defaults, not universal requirements. `keep/` is not permanent engineering storage.

Portability matters. Do not assume POSIX path syntax, executable bits, `sha256sum`, one fixed Downloads path, or downloadable-file support. macOS, Linux, Windows, desktop, web, and mobile clients can require different staging paths, checksum commands, interpreter invocation, execution permissions, or security prompts. Keep the normative contract shell-, operating-system-, model-, and client-neutral.

If downloadable-file delivery is unavailable, do not silently fall back to a large fragile transcript-dependent executable program. Prefer, in order:
1. already-governed repository-owned or shared tooling that performs the bounded action;
2. one or more independently safe atomic commands whose correctness does not depend on hidden transcript state;
3. a different legitimate receiving environment that can materialise the artifact while preserving the same authority and guards.

If none of those degraded paths is safely available, expose the real capability boundary as EXTERNAL_REQUIRED, BLOCKED, or DECISION_REQUIRED according to the governing workflow instead of manufacturing an unsafe copy/paste program.
```

## Inputs

- `<EXTERNAL_ACTION>` — the already-governed human-operated action that must cross the agent/operator capability boundary.

## What it does

Separates execution state from conversation state, preserves coupled guards and explicit authority, and gives the operator a small invocation plus bounded evidence hand-back. It keeps simple commands simple while making complex external procedures materialised, inspectable, integrity-checkable where useful, and explicitly ephemeral.

The contract is model- and operating-system-neutral. Client-specific conventions such as a `CHATGPT_...` filename, `${CHATGPT_ARTIFACT_HOME:-$HOME/CHATGPT}`, SHA-256 command syntax, 30-day retention, or `keep/` are recommended defaults/examples rather than universal workflow law.

## Boundaries / limitations

This contract never creates execution or mutation authority. Repository-local instructions, explicit task authority, security controls, validation requirements, and current evidence remain higher precedence. A digest proves only byte identity/integrity. Generated artifacts must not become durable canonical tooling merely because they work repeatedly; promotion requires the owning repository or shared-tool governance.

Do not turn artifact delivery into ceremony for genuinely atomic commands. Do not require one operating system, shell, ChatGPT client, download directory, checksum utility, or staging path. Do not bypass platform security protections, silently overwrite collisions, conflate creation and execution timestamps, assume the artifact staging directory is the target workspace, print secrets, or substitute a large transcript program when file delivery is unavailable.

## Status

`tested`
