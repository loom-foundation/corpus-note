---
id: note:spec:wdq47xk
name: The documentation structure
kind: specification
status: draft
---

This specification fixes the operational shape of the end-user documentation: the tree, the job of each page, the front door, self-containment, and the worked examples.
Which shape and why is the decision's ([The documentation follows Diátaxis](./dec-docs-structure.md){id=note:dec:pe53ssv}); how the prose reads is the convention's ([Documentation reads easy on the eyes](./conv-docs-readability.md){id=note:conv:h8zkcc8}); when documentation is done is the criterion's ([Documentation done is observable](./crit-docs.md){id=note:crit:b6wpk5s}).

## The tree

The documentation is one standing tree of plain markdown pages under `docs/`, one directory per Diátaxis mode: `tutorials/`, `how-to/`, `reference/`, `explanation/`.
A mode directory exists once its first page lands, never before.

## One job per page

Each page carries exactly one pedagogical job, its mode's:

- A tutorial is one worked example the reader performs end to end.
- A how-to guide serves a reader who already knows Note.
- A reference states the rules exactly and completely for one surface.
- An explanation carries understanding and no procedure.

A page needing two of these jobs is two pages.

## The front door

`docs/index.md` orients in one screen: what Note is, the ways in, and the map of what stands.

## Self-containment

Self-containment is the cited decision's stance.
This specification adds its enforcement: a link leaving the tree fails the build.

## Worked examples

Every worked example is a real file under `docs/examples/`, excluded from the rendered site.
An automated test exercises it and fails when the behaviour the example teaches changes.

## Relations

- satisfies: [Documentation completes the increment](./req-docs.md){id=note:req:t9gnr2f}
- decidedBy: [The documentation follows Diátaxis](./dec-docs-structure.md){id=note:dec:pe53ssv}
