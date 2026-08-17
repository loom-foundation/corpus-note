---
description: "The note file in full: the frontmatter fields, the body, and what makes a file well-formed."
---

# The note file

A note is a single UTF-8 text file: YAML frontmatter, one blank line, a markdown body.
One note per file.
This envelope, the four required fields, and a lead are all it takes for a file to be a note.

## Frontmatter

The frontmatter sits between two `---` lines and is YAML 1.2 under the core schema, so every conforming reader resolves a value's type from its spelling the same way.

Four fields are required:

| Field | Value |
|---|---|
| `id` | `namespace:kind:opaque`, immutable; see [Identifiers](./identifiers.md). |
| `name` | A concise label, never a summary. |
| `kind` | The kind token: lowercase letters with single hyphens between words. |
| `status` | A token recording where the note stands. |

The recommended order is `id`, `name`, `kind`, `status`, optional fields after them, so same-shaped notes diff precisely.
Any other order is never rejected while the required fields stand.

Two quoting rules cover everything a writer meets:

- Quote a value containing a colon followed by a space, `name: "Warp: the frame"`; unquoted, it reads as nested structure.
- Quote a value whose spelling reads as a number, boolean, or null, `name: "42"`; unquoted, it stops being text.

### Unknown fields

A frontmatter field nothing defines is a warning, reported by name, preserved untouched by any tool that rewrites the note, and never an error.
A note written against a later reading of the format therefore stays valid to an earlier one.

## Body

Exactly one blank line separates the closing `---` from the lead.

The lead is unheaded: one statement of the note's substance, with no level-1 heading anywhere and the name never repeated as a heading.

Section headings are level 2; each kind fixes their recommended order, and a different order is never rejected while the sections the kind requires stand.

## Well-formed

A note is well-formed with a well-formed envelope, the four required fields, whatever its kind requires of it, and a lead.
The file's name is a navigation convenience, never the identity, so a name alone never decides whether a file is a valid note.
