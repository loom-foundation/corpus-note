---
id: note:crit:b6wpk5s
name: Documentation done is observable
kind: acceptance-criterion
status: current
---

For every increment the requirement covers, all of the following hold for the affected pages, the pages that teach or describe what the increment introduces or changes:

- For every concept the increment introduces or changes that the documentation teaches by tutorial, a newcomer following that tutorial with only an editor and a shell reaches its stated end state.
- Every user-visible surface the increment introduces or changes has exactly one home in the reference, reachable from the documentation front door.
- Every corpus citation in the affected pages resolves to a current artefact.
- Every worked example in the affected pages is a real file, exercised by an automated test that fails when the behaviour the example teaches changes.
- The affected pages describe the resulting system, not the increment's history, and promise nothing unimplemented.
- Every affected page, checked against the adopted [Note-authoring standard](../qa/req-authoring-standard.md){id=note:req:kkn7wtj}, shows no departure.

## Relations

- qualifies: [Documentation completes the increment](./req-docs.md){id=note:req:t9gnr2f}
