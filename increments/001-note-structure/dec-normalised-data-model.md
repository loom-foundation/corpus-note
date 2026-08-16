---
id: note:dec:92bzam0
name: ANSI SQL DDL carries the structural model
kind: decision
status: current
---

Note's structural model is a specification written in ANSI SQL DDL.
The markdown structure of plain files, frontmatter metadata, and the `## Relations` body section implements it.

The DDL keeps to an ANSI-portable subset and lives in one standing schema file, `data/schema.sql`, a record the specification cites. That file is the single source of truth for the model.

## Context

This decision chooses the language of the specification that [Structure answers to one normalised model](./req-normalised-data-model.md){id=note:req:r050s7n} requires.
A specification language must be readable cold, authorable by hand, and checkable offline;
the markdown notation that implements the model enforces less than the model states.

## Decision

The subset keeps to what ANSI and stock SQLite, the specification's well-formedness checker, both accept:
VARCHAR, DATE, BOOLEAN, and INTEGER types, enumerations as check constraints, composite primary keys for edge tables.
Every constraint the markdown notation cannot enforce is stated in the SQL anyway, annotated with what compensates for it, or an honest none.
The schema lives outside the specification, as an external record the specification cites: the specification restates no line of the DDL, so nothing drifts, and a future increment extends the schema without touching the specification that delivered it.

## Forces and trade-offs

The specification is read cold by humans and AI agents, offline, with no tooling required.
Normalisation reasoning runs on the algebra of keys and check constraints, which SQL DDL states natively.
Loadable means self-checking: piping the schema file into stock SQLite proves it well-formed with nothing installed.

The accepted cost: readers must know SQL, and the subset is bounded to what ANSI and SQLite both accept.

## Alternatives considered

JSON Schema: rejected; it validates one document's shape, with no normalisation and no cross-file referential integrity, modelling the medium, not the model.

GraphQL SDL: rejected; no keys, no composite constraints, no normalisation discipline, and it implies an API that does not exist.

SHACL or OWL on RDF: rejected; expressive, but poor to read cold and to author by hand, behind a heavy toolchain.

dbml or a Mermaid ERD: rejected; lossy on constraints, right as a derived view and wrong as the source.

Alloy or TLA+: rejected; each states what SQL cannot, and excludes most readers.

A custom YAML meta-schema: rejected; a private format, with none of the discipline SQL gives for free.

## Relations

- upholds: [Single source of truth](../../../note-authoring/prin-single-source-of-truth.md){id=authoring:prin:hgmwdy8}

## Driven by

[A data model safe to read and change](./need-normalised-data-model.md){id=note:need:yrzdj9e}.
