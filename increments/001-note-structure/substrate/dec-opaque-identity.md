---
id: note:dec:dxrk5bn
name: Identity is a namespace and an opaque
kind: decision
status: current
---

An artefact's identity is its namespace and its opaque, drawn from Crockford Base32 under one grammar for every kind.
The kind-segment between them is not identity: it is an aid, letting a reader use relations and verbs against the right kind from the id alone, without opening a file, and a wrong segment repairs deterministically from the target's own `kind`.

## Context

A concept and the word that designates it are two things.
A citation fixed in an immutable surface, a commit trailer or a report, can never be rewritten to follow a rename, so identity holds nothing a rename changes.
An artefact also never changes kind while it lives: reopening a settled question is a new artefact with a new id, so the kind spelt beside an id cannot go stale.
[The artefact format](./spec-artefact-format.md){id=note:spec:vzj9nfv} fixes the scheme; this decision carries the reasoning that shaped it.

## Forces and trade-offs

Minting is uncoordinated across a namespace's lifetime, and a local check cannot see sibling repositories it does not hold, so collision odds compound with every id minted.
At no more than 1.5% lifetime odds, six characters carry roughly 5,700 ids and seven roughly 32,000.
Seven is the default because the common case is a product or team namespace, humans and agents minting in parallel, and intent artefacts scale with features and decisions, not lines of code.
At mega-scale the answer is several federated namespaces, each its own collision domain, never a longer opaque: the namespace, not the opaque, is the unit that scales.

The accepted cost: an opaque is not readable at a glance, and a reference's label can drift after a rename until refreshed; the id itself never drifts, and a tool restores labels in one pass.

The segment has costs of its own, accepted with eyes open: a register of abbreviations that must stay unique, a mismatch that must be warned and repaired, and the discipline that a sweep for an artefact's citers matches the namespace and the opaque, never the full spelling.
What keeps the segment out of identity is not that an artefact's kind can change, it cannot, but that the rendering of a kind can: a register that reassigns an abbreviation re-renders displays and breaks nothing, because identity holds nothing a register controls.

## Alternatives considered

Readable slugs: rejected; a slug conflates a concept with its designation, and a rename strands every citation already fixed in an immutable surface.

A human-chosen tag beside a machine id, a `REQ-AUTH-001` kept next to a stable opaque: rejected; the mutable, meaning-bearing key stays load-bearing at every authoring surface and strands citations all the same.

Opaque uniqueness bucketed per namespace and kind: rejected; the purchase is about half a character of length, where one added character multiplies the space thirty-two-fold.
Bucketing also makes cross-kind opaque reuse legal, so the segment becomes a load-bearing key, and a wrong-kind citation then dangles with no diagnosis or resolves silently to the wrong artefact.

The kind inside identity, opaques still unique namespace-wide: rejected.
The opaque already finds the artefact, so the kind adds nothing a key needs; a mistyped segment would harden from a warned fix into a permanent identity defect, and a reassigned abbreviation would migrate identity, killing every citation already fixed in history.
Kind immutability per artefact was weighed and rescues none of this.

No segment at all, a two-part `namespace:opaque`: rejected; it saves a few characters but forfeits the self-describing citation, the segment's whole earnings once uniqueness is namespace-wide.

The full kind token as the id's middle, the `kind` field dropped: rejected, though narrowly; it would leave one spelling per file and delete the mismatch machinery.
It lengthens the id at every citation surface, to 33 characters at the worst kind, and it removes the frontmatter surface tools, templates, and kind declarations read.
The abbreviations were also judged more readable in relation lines than the full tokens, not merely shorter.
