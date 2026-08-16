---
id: note:dec:dxrk5bn
name: Identity is a namespace and an opaque
kind: decision
status: draft
---

An artefact's identity is its namespace and its opaque, drawn from Crockford Base32 under one grammar for every kind.
The kind-segment between them is error-detecting redundancy, a check digit rather than a key, so a wrong segment repairs deterministically from the target's own `kind`.

## Context

A concept and the word that designates it are two things.
A citation fixed in an immutable surface, a commit trailer or a report, can never be rewritten to follow a rename, so identity holds nothing a rename changes.
[The artefact format](./spec-artefact-format.md){id=note:spec:vzj9nfv} fixes the scheme; this decision carries the reasoning that shaped it.

## Forces and trade-offs

Minting is uncoordinated across a namespace's lifetime, and a local check cannot see sibling repositories it does not hold, so collision odds compound with every id minted.
At no more than 1.5% lifetime odds, six characters carry roughly 5,700 ids and seven roughly 32,000.
Seven is the default because the common case is a product or team namespace, humans and agents minting in parallel, and intent artefacts scale with features and decisions, not lines of code.
At mega-scale the answer is several federated namespaces, each its own collision domain, never a longer opaque: the namespace, not the opaque, is the unit that scales.

The accepted cost: an opaque is not readable at a glance, and a reference's label can drift after a rename until refreshed; the id itself never drifts, and a tool restores labels in one pass.

## Alternatives considered

Readable slugs: rejected; a slug conflates a concept with its designation, and a rename strands every citation already fixed in an immutable surface.

A human-chosen tag beside a machine id, a `REQ-AUTH-001` kept next to a stable opaque: rejected; the mutable, meaning-bearing key stays load-bearing at every authoring surface and strands citations all the same.

Opaque uniqueness bucketed per namespace and kind: rejected; the purchase is about half a character of length, where one added character multiplies the space thirty-two-fold.
Bucketing also makes cross-kind opaque reuse legal, so the segment becomes a load-bearing key, and a wrong-kind citation then dangles with no diagnosis or resolves silently to the wrong artefact.

No segment at all, a two-part `namespace:opaque`: rejected; it saves a few characters but forfeits the self-describing citation and the check-digit redundancy, the segment's whole earnings once uniqueness is namespace-wide.
