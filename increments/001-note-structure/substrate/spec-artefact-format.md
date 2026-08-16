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
Section headings are level 2.
Frontmatter is YAML 1.2 read under the core schema, so every conforming reader resolves a scalar's type from its spelling the same way; a scalar intended as a string is quoted wherever its spelling could be read as another type.
A file's name is a navigation convenience, never the identity ([File names are short navigation hints](../../../../note-authoring/conv-file-names.md){id=authoring:conv:emtba7x}), so a name alone never decides whether a file is a valid artefact.

## Required frontmatter

An artefact is well-formed only with a well-formed envelope, the required frontmatter below, and a lead.

| Field | Value |
|---|---|
| `id` | `<namespace>:<kind-segment>:<opaque>`, immutable; identity is the namespace and the opaque. |
| `name` | A concise label, never a summary. |
| `kind` | The kind token: lowercase words joined by single hyphens, authoritative for the kind-segment. |
| `status` | A required token recording the artefact's standing. |

## Identity

Every artefact carries an immutable `id` of three colon-separated segments:

```
<namespace>:<kind-segment>:<opaque>
```

### The namespace

The namespace names the one sustained body of work whose intent the corpus holds, declared once in the corpus's manifest.
It is chosen short, lowercase, and distinctive, because it partitions the identity space: distinct bodies of work choose distinct namespaces, so ids minted for different systems never collide, and two systems that chose the same name cannot be brought into one working context without their ids meaning two things at once.

### The kind and its segment

The `kind` field carries the kind token, and every kind carries exactly one segment, an abbreviation no other kind shares, a structural fact the model fixes ([The structural schema](../normalised-data-model/rec-schema.md){id=note:rec:jnj07t4}).
The kind-segment in the id is rendered from the authoritative `kind` field.

### The opaque

The opaque is a Crockford Base32 string: digits `0` to `9` and letters `a` to `z` minus `i`, `l`, `o`, `u`, lowercase, compared case-insensitively, unique within its namespace across every kind.
Its default length is seven.
Mixed lengths are lawful within one namespace, and two opaques of different lengths never collide, so raising the length widens the space for new ids with no re-mint.

### What identity is

Identity is the namespace and the opaque.
The two ends of the id denote the artefact; the kind-segment between them is display and self-description, derived from `kind`.
Two ids denote the same artefact exactly when their namespaces and their opaques are equal, the opaques compared case-insensitively.
The id is minted once and never changes; a move, a rename, or a revision leaves it untouched.

### Minting an id by hand

Draw the opaque's characters from the alphabet above; confirm the string appears nowhere in the corpus (`grep -r`); assemble the id from the namespace, the segment rendered from the artefact's `kind`, and the opaque.
A tool draws from a secure random source and checks the same way.

## Why opaques

An identifier built from an artefact's wording starts to lie when the wording changes, and identity conflated with a file path or a heading shatters references on routine reorganisation.
The opaque holds nothing of the artefact's location or meaning, so it survives moves, renames, and revision; the file name and the `name` may change freely against it.

## Rationale

Stating the format once, in the format it describes, makes a corpus self-describing: well-formedness and identity are checkable from the file alone, with no special tool.
Fixing the envelope and identity here, and leaving per-kind fields to whatever defines each kind, lets one machinery carry many kinds.
