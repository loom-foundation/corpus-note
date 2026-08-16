---
id: note:conv:10dtm5q
name: Admonitions
kind: convention
status: draft
---

Documentation pages use GitHub-flavoured alerts where one of the five types below applies, at the natural flow position in the prose, and nowhere else.
This convention governs `docs/` pages only.

Each type carries the meaning GitHub gives it in [Alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts):

- NOTE: "Useful information that users should know, even when skimming content."
- TIP: "Helpful advice for doing things better or more easily."
- IMPORTANT: "Key information users need to know to achieve their goal."
- WARNING: "Urgent info that needs immediate user attention to avoid problems."
- CAUTION: "Advises about risks or negative outcomes of certain actions."

In the source an alert is a blockquote and degrades to a quoted paragraph wherever alerts are not rendered, within the self-containment that [The documentation follows Diátaxis](./dec-docs-structure.md){id=note:dec:pe53ssv} fixes.

## Rationale

An alert is coloured and styled apart from the prose, and readers have been conditioned by that styling in two opposite ways.
A note or a tip is skipped unless the reader wants more information, so those two carry what the reader may safely pass over.
An important, a warning, or a caution draws the eye, so those three carry what the reader must not miss.
An alert used for ordinary prose spends that conditioning.
