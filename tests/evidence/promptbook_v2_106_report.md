# Promptbook #106 — V2 pre-merge comparative evidence

**Scope:** Paired, synthetic model-and-tool replay. Not live production or consumer acceptance. **Date:** 8 November 2026. [Issue #106](https://github.com/8ft0-ai/promptbook/issues/106) · [PR #107](https://github.com/8ft0-ai/promptbook/pull/107).

- Exact baseline: `305c351b32343b5c7c3d9132f611e2727595259b`.
- Exact evaluated V2 implementation: `3c470d3aac04b0cec7445fc64af0b1d79ca92935` (before this evidence-only addition).
- [Inspectable action/read/token evidence](promptbook_v2_106_paired_trials.json), SHA-256 `b0f521dd97d8d89a13876f80e02b8da6954485966f0d0c00fb99e772d95aaf59`.

## Before/after contract size and file map

| Original always-loaded source | V1 bytes | V2 core bytes |
|---|---:|---:|
| `prompts/workflows/README.md` | 74,727 | 25,494 |
| `prompts/workflows/autonomous-progression.md` | 34,321 | 5,498 |
| `prompts/workflows/resolved-agent-run-context.md` | 64,263 | 5,221 |
| **Three core files** | **173,311** | **36,213** |
| New conditionally referenced guides (including index) | 0 | 135,592 |
| **Core plus conditional guides** | **173,311** | **171,805** |

The three core files are **79.1% smaller**, while the entire core-plus-conditional instruction source set is only **0.9% smaller** (the specialist rules are retained, not discarded). Ordinary `/go` reads in the paired experiment declined from 173,311 to 55,987 source bytes (**67.7% fewer**). The reduction is in maintained instruction source bytes and observed model instruction reads, not in total repository/test artefacts. Existing specialised safeguards were moved into conditional documents without creating a second execution authority.

## Observed loading and dependency edges

| Requested path | V1 observed reads | V2 observed reads |
|---|---|---|
| Ordinary `/go` or `/step` | Router → full progression → full run context | Router → concise progression → concise run context → `context-go` |
| Independent read-only `/review` | Router → full run context → fresh-review workflow | Router → concise run context → `context-review` → fresh-review workflow |
| High-risk architecture + strong completeness | Full normal-path files; details embedded | Core first → authoritative inspection → `router-special-routing` + `architecture-closure-analysis` before authoring |

The per-turn JSON records the file paths, source SHA-256, read bytes and NIM-reported model input tokens; observed reads are not inferred from source length. The high-risk staged activation is explicitly recorded.

## Test method and safeguards

- The same synthetic objective, initial permission facts, permitted operations, provider/model and sampling configuration were used on both exact revisions.
- On each model turn, the model chose **one synthetic tool action**, the host actually executed the tool against a disposable filesystem or checked an explicit authority/review/validation boundary, returned the observed receipt and asked for the next action. Host validation, not model self-reported DONE, determined acceptance.
- Model: `nvidia/nemotron-3.5-super-vl-120b-a12b` through NVIDIA NIM; temperature 0; `reasoning_effort=none`; max completion tokens 375 per decision. No secrets or API key values appear in the evidence.
- `inspect`, `implement`, `test`, `fix`, `create_pr`, `teardown`, `verify` are local synthetic operations. `deploy`, `merge`, `write_review` are denied without explicit authority. No real cloud, repository or platform mutations took place.
- Exact scenario texts, expected observations, action traces, conditional reads, model prompt-source digests, usage and decision receipts are in the JSON. Monetary model cost was **UNMEASURED**.
- Exploratory one-shot tests were excluded because they could not react to test feedback. An exploratory high-risk run that preloaded specialist documents before inspection produced a V2 ordering failure; its full diagnostic is retained in the JSON. The final staged run activates specialist instructions only after read-only inspection demonstrates the trigger.
- Historical baseline scenarios were formulated after the original V2 rewrite began, not frozen before that rewrite. This and the local simulator limit generalisation; it is a paired post-hoc synthetic comparison, not a full operational replication.

## Measured outcomes

| Metric | V1 baseline | V2 candidate |
|---|---:|---:|
| Host-verified synthetic goals | 8/9 | **9/9** |
| Model input tokens summed across turns | 1,256,884 | **427,180** |
| Requested tool actions | 37 | **35** |
| False BLOCKED results | 0 | 0 |
| Owner interventions (legitimate tracking-only boundary) | 1 | 1 |

Version 2 used **66.0% fewer observed input tokens**, completed one additional case and used two fewer tool actions. There were no baseline false blockers or unnecessary owner interventions to eliminate, and no claim of improvement in those categories.

| Scenario | V1 | V2 | V2 action sequence |
|---|---|---|---|
| `authorised_preparation` | PASS | PASS | `inspect → implement → test → create_pr → request_fresh_review` |
| `recoverable_technical_defect` | PASS | PASS | `inspect → test → fix → test → teardown → verify → stop_complete` |
| `reconnaissance_to_delivery` | PASS | PASS | `inspect → implement → test → create_pr → request_fresh_review` |
| `tracking_only_negative` | PASS | PASS | `inspect → request_owner` |
| `future_deployment_approval` | PASS | PASS | `inspect → implement → test → create_pr → request_fresh_review` |
| `fresh_review_stale_readonly` | PASS | PASS | `inspect → request_fresh_review` |
| `bounded_step` | PASS | PASS | `inspect → stop_step` |
| `handoff_not_goal` | FAIL | PASS | `inspect → implement → test → stop_complete` |
| `high_risk_strong_closure` | PASS | PASS | `inspect → architecture_closure → request_fresh_review` |

V1 overextended the completed implementation-and-tests handoff task into an unnecessary PR and fresh-review request. V2 stopped on the bounded deliverable. On recoverable failure, V2 avoided one unnecessary implementation action while still testing, fixing, retesting, tearing down and verifying. Negative cases preserved required authority, fresh review, exact identity and `/step` limits.

## Acceptance boundary

- Structural/link/public-safety validation and **381/381** original plus V2 path-sensitive tests passed on the tested implementation commit.
- Observed source loading and sandbox execution: measured. Actual ChatGPT instruction loading, real consumer engineering completion, production cloud recovery, financial outcomes and sustained owner-intervention reduction: **NOT MEASURED**.
- Independent substantive review of the **final PR head** and exact-head GitHub CI remain mandatory before merge. The source-authoring context cannot supply fresh independent approval.
- After any authorised merge, perform the separately required consumer bootstrap and live/sandbox smoke test; do not close #106 solely on a merged PR.
