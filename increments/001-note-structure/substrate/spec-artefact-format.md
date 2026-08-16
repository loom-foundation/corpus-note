---
id: note:spec:vzj9nfv
name: The artefact format
kind: specification
status: draft
---

This specification fixes what makes a file a Note artefact: the file envelope and the identity scheme.
It knows no kind: the fields and body sections particular to a kind are fixed by whatever defines that kind.

## File envelope

An artefact is a single UTF-8 text file: YAML frontmatter delimited by `---`, then a markdown body, one artefact per file.
Exactly one blank line separates the closing frontmatter delimiter from the lead.
The body opens with an unheaded lead, one statement of the artefact's substance; it carries no level-1 heading, and the name is never repeated as a heading.
Section headings are level 2; the specification defining the artefact's kind fixes their recommended order, and a different order is never rejected while the sections the kind requires stand.
Frontmatter is YAML 1.2 read under the core schema, so every conforming reader resolves a scalar's type from its spelling the same way.
A field's value is a scalar, a list, or a mapping, and every leaf of one is a scalar; a scalar intended as a string is quoted wherever its spelling could be read as another type, and a value carrying a colon followed by a space is quoted, because unquoted it parses as a nested mapping a conforming reader rejects.
A file's name is a navigation convenience, never the identity ([File names are short navigation hints](../../../../note-authoring/conv-file-names.md){id=authoring:conv:emtba7x}), so a name alone never decides whether a file is a valid artefact.

## Required frontmatter

An artefact is well-formed only with a well-formed envelope, the required frontmatter below, whatever its kind requires of it, and a lead.

| Field | Value |
|---|---|
| `id` | `<namespace>:<kind-segment>:<opaque>`, immutable; identity is the namespace and the opaque. |
| `name` | A concise label, never a summary. |
| `kind` | The kind token: lowercase letters with single hyphens between words, authoritative for the kind-segment. |
| `status` | A required token recording the artefact's standing. |

The recommended field order is `id`, `name`, `kind`, `status`, optional fields after them, so same-shaped artefacts diff precisely; any other order is never rejected while the required fields stand.
A frontmatter field neither this specification nor the artefact's kind defines is a warning, reported by name, preserved untouched by any tool that rewrites the artefact, and never an error, so an artefact written against a later reading of the format stays valid to an earlier one.

## Identity

Every artefact carries an immutable `id` of three colon-separated segments:

```
<namespace>:<kind-segment>:<opaque>
```

### The namespace

The namespace names the one sustained body of work whose intent the corpus holds, declared once in the corpus's manifest.
It is chosen short, lowercase, and distinctive, because it partitions the identity space: distinct bodies of work choose distinct namespaces, so ids minted for different systems never collide, and two systems that chose the same name cannot be brought into one working context without their ids meaning two things at once.
Anchoring it to something already globally registered that the corpus's owner controls, a domain or a repository, removes that collision for free.
The namespace is the one piece of configuration a corpus cannot revise later: every id ever minted carries it, and ids are immutable.

### The kind and its segment

The `kind` field carries the kind token, and every kind carries exactly one segment, an abbreviation no other kind shares, a structural fact the model fixes ([The structural schema](../normalised-data-model/rec-schema.md){id=note:rec:jnj07t4}).
The kind-segment in the id is rendered from the authoritative `kind` field.
A well-formed token no register defines still makes an artefact; the unknown token is reported as a warning, never a bar on the file.
A segment disagreeing with `kind`, in an artefact's own id as in any other spelling of it, is a display defect reported with the canonical rendering proposed, never a failure of the id to denote.

### The opaque

The opaque is a Crockford Base32 string: digits `0` to `9` and letters `a` to `z` minus `i`, `l`, `o`, `u`, lowercase, compared case-insensitively, unique within its namespace across every kind.
Its default length is seven, each corpus configuring its own length in its manifest; the declared length governs new ids only.
Mixed lengths are lawful within one namespace, and two opaques of different lengths never collide, so raising the length widens the space for new ids with no re-mint.

### What identity is

Identity is the namespace and the opaque.
The two ends of the id denote the artefact; the kind-segment between them is display and self-description, derived from `kind`.
The segment is error-detecting redundancy rather than a key: the opaque alone finds at most one artefact, so a wrong segment repairs deterministically from the target's own `kind`.
Two ids denote the same artefact exactly when their namespaces and their opaques are equal, the opaques compared case-insensitively.
The id is minted once and never changes; a move, a rename, or a revision leaves it untouched.

### Minting an id by hand

Draw the opaque's characters from the alphabet above; confirm the string appears nowhere the namespace is kept, `grep -r` in every repository holding it; assemble the id from the namespace, the segment rendered from the artefact's `kind`, and the opaque.
A tool draws from a secure random source and checks the same way.

## Why opaques

An identifier built from an artefact's wording starts to lie when the wording changes, and identity conflated with a file path or a heading shatters references on routine reorganisation.
The opaque holds nothing of the artefact's location or meaning, so it survives moves, renames, and revision; the file name and the `name` may change freely against it.

## Rationale

Stating the format once, in the format it describes, makes a corpus self-describing: well-formedness and identity are checkable from the file alone, with no special tool.
Fixing the envelope and identity here, and leaving per-kind fields to whatever defines each kind, lets one machinery carry many kinds.

## Relations

- decidedBy: [Identity is a namespace and an opaque](./dec-opaque-identity.md){id=note:dec:dxrk5bn}
