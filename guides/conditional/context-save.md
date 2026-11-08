# Context Save

**Conditional contract:** Load only for requested durable persistence under narrow existing authority.

## `/save` required context

Before substantive `/save` persistence, resolve at least:

```text
operation
repository_identity
work_item_identity
resolved_authority_sources
applicable_repository_instructions
candidate_durable_home
intrinsic_persistence_authority
effective_capabilities
prohibited_capabilities
required_evidence
```

`candidate_durable_home` should prefer an existing canonical issue/work item when one unambiguously owns the result. If none exists and the result is unresolved work, a decision, experiment, or follow-up, one new issue may be created when repository policy permits it.

The intrinsic `/save` operation ceiling is logically equivalent to:

```text
ALLOW
- repository/work-item reads needed to choose the canonical home
- add/update the minimum issue/work-item comment or metadata needed to preserve the result
- update the existing canonical issue body when that is clearly the owning record
- create one new issue when no existing canonical work item is appropriate

FORBID UNDER /save ALONE
- production/code/configuration mutation
- branch creation or branch mutation
- pull-request creation or merge
- repository-document file mutation that requires a branch/PR workflow
- cross-repository mutation
- issue closure unless separately authorised
- release/deploy/apply/provider/settings/credential/secret effects
- broader engineering implementation
```

If the correct durable home is a repository document whose modification requires ordinary branch/PR mutation, `/save` alone may identify or record that need, or consume separately established mutation authority if one already exists; it must not manufacture that authority.

## `/save` lifecycle

A `/save` invocation is itself the bounded persistence request. It may select and perform only the smallest canonical repository-native persistence action permitted by the `/save` operation ceiling. After persistence, return the durable location/evidence and stop. Do not automatically enter implementation, issue closure, branch/PR creation, or another lifecycle workflow.

A later operation that acts on the saved record must independently reconstruct its own authority; the fact that `/save` created or updated a durable record does not grant that later operation authority.
