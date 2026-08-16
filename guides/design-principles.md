# Design principles

Promptbook is organised around observable engineering behaviour rather than elaborate personas.

## Evidence before conclusion

Ask the assistant to inspect the authoritative artefacts that can answer the question. Summaries and prior conclusions are useful navigation, but they should not silently replace the underlying candidate, repository state, tests, or governing record when those are available.

## Bounded authority

A prompt should not imply that access equals permission. Separate what the assistant can technically do from what the task or repository authorises it to do.

## Minimum sufficient change

Prefer the smallest coherent change that satisfies the intended outcome. Avoid opportunistic refactoring, speculative abstractions, new infrastructure, or adjacent work that is not needed for the task.

## Fail closed where evidence matters

When a material fact, identity, permission, or decision cannot be established, preserve the uncertainty. A blocked or incomplete result is better than a confident result manufactured from missing evidence.

## Validation is part of the task

Implementation is not complete because code was written. Review the complete diff, run the relevant checks, inspect negative paths, and verify any mutation before claiming success.

## Independence when independence matters

A fresh review should reconstruct the decision from the actual evidence rather than inheriting the authoring context's conclusion. Freshness is about prior-information boundaries, not a particular UI mode.

## Minimise unnecessary human orchestration

Routine engineering judgement, validation, bounded remediation, and other already-authorised work should not automatically become conversational stop points. Stop for genuine human decisions, unavailable capabilities, unsafe ambiguity, or completion.

## Self-contained public prompts

A public prompt should expose every material input a new user must provide. Hidden private history, internal IDs, secret tooling assumptions, and unexplained conventions make a prompt fragile and non-reusable.
