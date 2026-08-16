---
id: note:spec:hq4mst8
name: The kind declaration shape
kind: specification
status: draft
---

The meta-shape of a kind declaration, fixed here as an ordinary specification until floor 1's own meta-kind exists.
The five facts it must carry are fixed by [Domain declaration rules](./spec-domain-declaration-rules.md){id=note:spec:w3jq8kt}; this artefact fixes only where each fact lives in the file.

- The frontmatter carries the scalar facts as `token`, `segment`, and `domain`.
- The body opens with the kind's definition in one or two sentences; that lead is the definition's single home, cited by every other artefact that needs it.
- A `Fields` section carries the declared frontmatter fields as a table: field, required, grammar, citation-bearing, slice-pulling.
- A `Sections` section names the body sections required at the `standard` profile.
- A `Coverage` section carries the expectations as a table: gap, closing verb, direction.

Envelope fields are substrate-owned and never appear in `Fields`.
