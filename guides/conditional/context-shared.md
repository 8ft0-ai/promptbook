# Context Shared

**Conditional contract:** Load material sections for capability availability, common provenance/evidence and governed-state projection.

## Core rule

A governed operation must execute from explicit, reconstructable authority and capability state rather than treating the conversation transcript as executable state.

The conversation may carry intent and navigation, but correctness must be reconstructable from current authoritative sources. Prior summaries and remembered conclusions are navigation aids only when the underlying authority or evidence can be refreshed directly.

A technically available connector, shell, API, credential path, or other tool is not authority:

```text
tool available
    ≠
action authorised
```

For lifecycle progression, preserve the stronger distinction:

```text
candidate approved
    ≠
merge authorised
    ≠
release authorised
    ≠
deployment authorised
    ≠
production mutation authorised
```

Authority or acceptance for one consequential transition must not silently become authority for a later transition.

## Inputs

Resolve the context from the authoritative inputs that apply to the operation. At minimum, consider:

- platform safety and explicit current-user authority;
- the Promptbook workflow selected for the operation;
- repository-local instructions and mandatory policy;
- the governing issue, pull request, design, specification, accepted plan, review finding, accepted decision, or other work-item authority;
- the immutable candidate being reviewed or remediated, or the current lifecycle/result identity being progressed, where applicable;
- current CI, checks, review state, branch/repository policy, and other decision-critical durable evidence.

Conversation history may help locate those sources, but it is not a substitute for refreshing them when correctness depends on current state.

Resolve the context from current authoritative inputs in precedence order appropriate to the repository and operation. Record enough provenance to identify where each applicable instruction or material rule came from. A resolved context does not create authority absent from those sources.

If a required authority source cannot be resolved, fail closed or hand off according to the governing workflow rather than filling the gap from conversation memory.

The representation may be textual or structured. It need not be committed for every run. Whatever representation is used, equivalent authoritative inputs must resolve to equivalent effective authority, relevant identity, capability boundaries, and evidence requirements for the same operation.

## Capability-availability integration

When a material `/fix` action or `/go` progression action has an explicit Promptbook capability-availability key, resolve availability only after the exact action has passed the operation's authority gateway. `/step` has no independent availability model: when it selects one governed transition, that action is the same `/go` progression action for availability, suppression, locality and projection purposes. Use [Capability availability overrides](../../prompts/workflows/capability-availability-overrides.md) to derive one record equivalent to `resolved_capability_availability` for the current repository/work/action identity.

The ordering is:

```text
resolve repository/work/action authority
    → classify the exact action through the operation gateway
    → resolve capability availability once
    → derive effective executable capability
    → resolve execution locality when the current mechanism is unavailable or insufficient
    → execute directly or project to an eligible executor
```

That availability record is derived execution state, not a new authority source. Autonomous progression and executor projection consume the same resolved record and its provenance; they must not independently search Project instructions, repository instructions, work items, or prior conversation for another value. If a decision-critical carrier changes, invalidate the affected derived availability state and re-resolve it before consequential use.

Execution-locality resolution consumes the already-classified action and any applicable availability result. It does not reinterpret availability as authority and must not route around an explicitly disabled logical capability by relabelling the same suppressed effect through another executor or locality.

Fresh-review context resolution is not part of this availability/locality ordering. It answers whether independent adjudication can occur in a genuinely isolated reasoning context after the current context is determined non-fresh; it does not answer where an already-authorised execution effect can run.

## Governed-state projection

The Resolved Agent Run Context remains the single canonical derived execution-state contract. Commands must not construct a second independently resolved lifecycle model.

Project only the material dimensions needed for routing and operator-facing interpretation, such as objective identity/scope, work/candidate state, review disposition, response-routing state, authority classification, execution feasibility/locality, and freshness requirements.

`COMPLETE`, `DECISION_REQUIRED`, `EXTERNAL_REQUIRED`, and `BLOCKED` are derived router boundaries, not an independently mutable terminal-state dimension. A projection must therefore derive one of:

```text
BOUNDARY
  NONE
  COMPLETE
  DECISION_REQUIRED
  EXTERNAL_REQUIRED
  BLOCKED
```

from the resolved state plus proposed transition. Do not allow contradictory combinations such as an execution state that is blocked while a separately asserted terminal state remains active.

For equivalent authoritative inputs, preserve the shared projection invariant:

```text
/next   -> reports transition T or boundary B
/status -> reports Next: T/B
/help   -> advice is based on T/B
/step   -> executes T only if T is ALLOW and executable; otherwise reports B
/go     -> repeats the same transition loop until B
```

The projection may be textual or structured, but it is derived from the same authoritative run context and never becomes a competing source of authority.

## Required evidence

Resolve the evidence necessary to support the requested operation before adjudicating, declaring remediation complete, or treating lifecycle progression as complete. Evidence should be proportionate, bounded, and reconstructable. Depending on the claim, it may include:

- an exact command or tool invocation and result status;
- bounded relevant output;
- a CI or check result bound to the candidate or resulting identity;
- a reproducible test;
- a static source observation;
- an applicable repository-rule or authority citation;
- for `/fix`, the bounded implementation delta, final exact resulting candidate identity, required validation bound to that final candidate, remediation-readiness surface/evidence, and preserved fresh-review boundary;
- for `/go` or `/step`, the starting state, proposed action, authority classification, applicable availability, resolved execution locality when material, resolved fresh-review context when material, resulting state/identity, validation/evidence, and remaining boundaries;
- for `/save`, the selected canonical durable home, persistence action, operation-ceiling classification, and resulting durable evidence.

Do not fabricate executed evidence where only static analysis occurred. Identify static observations as static. If a material claim requires execution that was not performed, represent that absence rather than implying the execution succeeded.

For evidence, distinguish at least:

- `STATIC` — source, configuration, metadata, or rule observation without executing the claimed behaviour;
- `EXECUTED` — a command, test, check, or tool action was actually run and its result observed;
- `DURABLE` — repository-hosted CI, review, check, or other retained evidence was inspected.

A finding, remediation record, or progression record may use more than one evidence class. Do not upgrade one class into another merely to strengthen the conclusion.

## Evidence-bearing review findings

A material review finding should be reconstructable as the logical equivalent of:

```text
claim
affected_code_or_location
applicable_authority_or_rule
observation
evidence
immutable_candidate_identity
priority
confidence
```

The human-facing review may remain concise. It does not need to print a verbose schema for every observation, but the decisive reasoning must retain enough provenance to reconstruct why the disposition applies to the bound candidate.

## Delegation invariant

Future delegated or child execution contexts must never gain authority merely through delegation:

```text
child_authority ⊆ parent_authority
```

For delegated fresh review, use the stricter operation-specific form:

```text
child_review_authority ⊆ effective_review_authority
```

A fresh-review child is resolved as `/review`; it does not inherit broader parent `/go`, `/step`, `/implement`, or `/fix` mutation capability. An external execution substrate should likewise receive only the resolved authorised subset needed for the delegated action. Delegation cannot refresh stale parent authority, create a new approval, or make an authoring context fresh. This contract does not introduce subagent infrastructure or make the substrate a workflow-policy owner.

## Boundaries / limitations

This contract defines `/review`, `/fix`, `/go` progression, and `/save` run contexts, including bounded fresh-review child-context resolution. `/step` is the one-transition progression-depth mode of the `/go` run context and does not introduce a separate operation ceiling, authority model, availability model or executor profile. The contract does not introduce a new Switchboard schema, operating-system or network sandboxing, Guardian-style approval automation, native subagents, agentctl policy ownership, Watchtower workflow ownership, a global executor/capability registry, arbitrary remote shell or argv dispatch, a global agent registry, or a universal persisted run-context schema.

It does not intrinsically grant merge, release, tag, deployment, infrastructure/provider, settings, credential, secret, production, destructive-action, material-cost, or unrelated mutation authority. Those actions require separate current authority where they are permitted at all, and `/go` must resolve that authority explicitly before execution.

External mechanisms may enforce capability restrictions or collect evidence, but they do not become owners of Promptbook workflow policy or independent discoverers of Promptbook availability configuration. Execution-locality selection chooses only among already-eligible mechanisms and cannot turn technical reachability into authority. Fresh-review context selection likewise cannot turn technical context creation into review authority or into proof of independence; isolation must be established, and repository requirements for distinct human/formal review remain higher precedence.
