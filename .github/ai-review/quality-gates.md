# Quality gates

Sample gates for the PR Standards Enforcer. Each `## ` heading and each `- ` item counts as one gate.
Replace these with your team's real rules.

## PR description is required

- The description explains what changed and why, and links the ticket.

## New logic has tests

- Every new function or branch with behaviour has a unit test in the same PR.

## No debug logging

- No `console.log`, `print()` or `debugger` statements left in production code.

## Functions stay small

- No function longer than 50 lines; split it or explain why in the PR.

## No secrets in code

- No API keys, tokens or passwords in source, config or tests.
