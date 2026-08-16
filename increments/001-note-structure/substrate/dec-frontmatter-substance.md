---
id: note:dec:cvsp8fc
name: Frontmatter authors substance
kind: decision
status: draft
---

A frontmatter field carries substance the author asserts, never a fact derived from elsewhere or a circumstance of the artefact's making.
A derived fact is computed from its home when asked; a circumstance is read from the record that witnessed it.

## Context

Two proposed keys forced the question: `domain:`, grouping an artefact by its kind's domain, and per-artefact pack-version stamps, recording which definition of its kind the artefact was written against.
Each writes by hand a fact something else already fixes.

## Forces and trade-offs

Domain is a function of kind: when domains arrive, the kind register carries each kind's domain, and an artefact's domain derives through it.

Definitional history lives in the pack declarations' own supersession lineage, and which version a corpus conforms to is one pinned manifest line; verification against a chosen version is a tool parameter, the artefact the subject and the version the question.
Additive pack growth never invalidates an older artefact.

## Alternatives considered

An authored `domain:` key: rejected; the authored copy of a derived fact drifts against the register and lets a reader group by an unchecked claim.

Per-artefact pack-version keys: rejected; every version bump forces mass edits or leaves lying stamps, recording circumstance the pinned line already answers.

## Relations

- upholds: [Single source of truth](../../../../note-authoring/prin-single-source-of-truth.md){id=authoring:prin:hgmwdy8}
