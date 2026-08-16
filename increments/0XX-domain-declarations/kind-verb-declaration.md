---
id: note:spec:x8nbcw2
name: The verb declaration shape
kind: specification
status: draft
---

The meta-shape of a verb declaration, fixed here as an ordinary specification until floor 1's own meta-kind exists.
The five facts it must carry are fixed by [Domain declaration rules](./spec-domain-declaration-rules.md){id=note:spec:w3jq8kt}; this artefact fixes only where each fact lives in the file.

- The frontmatter carries `verb`, `inverse`, `traversal`, and `signature`, the last as a list of `source -> target` kind pairs.
- The body opens with the meaning of the edge in one sentence, read from source to target.
- A `Constraints` section carries the load-bearing structural constraints, or declares none.
