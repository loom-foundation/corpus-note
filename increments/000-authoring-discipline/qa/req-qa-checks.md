---
id: note:req:ngwzfvc
name: One check runs at every gate
kind: requirement
status: current
---

Every rule the method fixes mechanically is enforced by an automated test.
One command runs the whole suite, before a commit lands locally (a pre-commit hook) and on every pull request in CI, with identical results.

## Relations

- addresses: [Maintain corpus quality](./need-qa.md){id=note:need:rjkq4qn}
