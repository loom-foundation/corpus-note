---
description: "Write one note by hand with an editor and a shell, then try to break its identity and fail."
---

# Your first note

You will write one note by hand, then try to break its identity and fail.
At the end you hold a folder with one well-formed note, and one command proves its id survived everything you did to the file.

You need an editor, a shell, and ten minutes.

## 1. Make a folder

```sh
mkdir garden && cd garden
```

Any folder serves; a note is a plain file and lives wherever you keep files.

## 2. Choose a namespace

Every id starts with a namespace, the name of the body of work your notes belong to, chosen once for the whole corpus.

> [!IMPORTANT]
> Renaming it later may break citations fixed in commit history or someone else's notes citing yours under the old name, so choose it as if it were permanent.

This tutorial's body of work is a garden, so the namespace is `garden`.

> [!TIP]
> Anchor it to a name already registered to you, a domain or a repository, to reduce the probability of collisions with other corpora.

## 3. Mint an id

An id is three segments: the namespace, the note's kind, and an opaque that names the note itself.

Draw seven characters from this alphabet:

```
0123456789abcdefghjkmnpqrstvwxyz
```

(`i`, `l`, `o` and `u` are left out, so no character can be misread.)
Any source of characters serves; say you drew `7fjq3ka`.

> [!NOTE]
> Curious why an opaque id, or why these characters are left out? See [Why opaque ids](./why-opaque-ids.md).

Confirm nobody drew it before you:

```sh
grep -r "7fjq3ka" .
```

Silence means the opaque is unused and yours.

This note will record an idea, so its kind is `idea`; a short kind serves as its own segment in the id.
Assembled: `garden:idea:7fjq3ka`.

## 4. Write the note

Create `tomatoes.md`:

```markdown
---
id: garden:idea:7fjq3ka
name: Tomatoes on the south fence
kind: idea
status: draft
---

Grow tomatoes along the south fence, where the sun stays longest.
```

Read it back as four fields, a blank line, and a lead:

- `id` is the identity you just minted, written once and never changed.
- `name` is a concise label; renaming it later is free, because the name is not the identity.
- `kind` says what sort of note this is.
- `status` is a token recording where the note stands; `draft` says you are still shaping it.
- After the closing `---` comes exactly one blank line, then the lead: one statement of the note's substance, with no heading above it.

That field order is the recommended one, so notes diff cleanly side by side.

The file name `tomatoes.md` is a navigation aid: it helps you find the note in the file system, and it is no part of the identity.
The next step proves that.

## 5. Try to break the identity

Rename the file:

```sh
mv tomatoes.md south-fence.md
```

Bury it in a subfolder:

```sh
mkdir beds && mv south-fence.md beds/
```

Now ask the folder which file is `garden:idea:7fjq3ka`:

```sh
grep -rl "id: garden:idea:7fjq3ka" .
```

It prints `./beds/south-fence.md`.
Two moves touched the path and the file name, and neither touched the identity, because the identity lives inside the file.

Nothing you do around a note can change what it is.

## Done

The end state, checkable in one line: the grep above prints exactly one path, whatever you renamed the file to along the way.

The full rules of the file are in [The note file](../reference/the-note-file.md), the full rules of the id in [Identifiers](../reference/identifiers.md), and the reasoning in [Why opaque ids](./why-opaque-ids.md).
