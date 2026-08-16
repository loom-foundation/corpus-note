---
id: note:dec:pe53ssv
name: The documentation follows Diátaxis
kind: decision
status: current
---

The end-user documentation is organised by Diátaxis mode, tutorials, how-to guides, reference, and explanation, each page carrying one pedagogical job.
It stands as a tree of plain markdown pages, its own self-contained deliverable, never citing or presupposing the corpus's internals.

## Context

[Documentation completes the increment](./req-docs.md){id=note:req:t9gnr2f} obliges every increment touching a user-visible concept to teach it in the canonical documentation, so that documentation needed one organising shape before its first chapter could stand.

## Alternatives considered

Organising by topic, with the modes inside each chapter: rejected; the site-wide mode split is the shape readers of documentation sites know, and the two reading situations, learning and looking up, are the true divide.

A single manual per concept: rejected; one page serving every reading situation serves none.
