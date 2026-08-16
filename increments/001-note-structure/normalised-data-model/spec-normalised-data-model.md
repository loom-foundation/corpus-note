---
id: note:spec:1hq5yrh
name: The normalised data model
kind: specification
status: current
---

Note's structure is specified in one normalised data model, written in ANSI SQL DDL because it yields well to the modelling task.
The markdown structure of plain files, frontmatter metadata, and the `## Relations` body section is the implementation, carrying the model as faithfully as the medium allows.
This specification fixes how the model is kept and how a modelled fact appears in a file; it restates no line of the DDL.

## The model of record

The schema held by [The structural schema](./rec-schema.md){id=note:rec:jnj07t4} is the single source of truth for structure.
A structural change is modelled there before it is implemented in the medium, and a later increment extends the schema without touching this specification.
The model fixes structure alone, in the algebra of keys and check constraints; meaning stays with the artefacts' prose.
At this increment the schema holds the atom: the artefact with its identity, and the register of kinds.

## From model to medium

- A row of the artefact table is one markdown file; its columns appear as the YAML frontmatter fields `id`, `name`, `kind`, and `status`.
- The id's parts are the artefact's key: the namespace and the opaque are its identity, and the middle segment is rendered from `kind` through the kind's one segment.
- A kind's segment is a fact of the model; an artefact's file carries the kind token alone.
- A constraint the medium cannot enforce is stated in the schema anyway and recorded in its unenforced-constraints register; each such constraint remains checkable from the record.

## Relations

- satisfies: [Structure answers to one normalised model](./req-normalised-data-model.md){id=note:req:r050s7n}
