---
description: "Why a Note id carries no words: wording improves, and the citations already set in commits and reports never update."
---

# Why opaque ids

A note and its name are two things.
The name is wording, and wording improves: the label that felt right yesterda reads wrong tomorrow, and renaming is routine, healthy work.

A citation is not.
Once an id is written into a commit message, a report, or a printed page, that surface never updates again.

So identity must hold nothing a rename changes, and an opaque holds nothing at all.

## Why not readable slugs

A readable slug, `tomatoes-south-fence`, conflates the note with its wording.
When the wording improves, one of two bad things happens: the slug stays and no longer matches the content, or the slug follows and every citation already set in concrete points at nothing.

Both failures come from the same conflation, and no renaming discipline removes them.

## Why not a tag beside a machine id

The obvious compromise keeps both: a human-chosen tag such as `IDEA-001`, kept next to a stable opaque.
It fails for a human reason.

The readable key is the one people remember, type, and cite, so it stays load-bearing at every surface where writing happens, and it strands citations all the same.
A second name does not relieve the first of its burden. It just gives the concrete two things to set around.

## The middle segment is a label

The id `garden:idea:7fjq3ka` seems to smuggle meaning back in: `idea` looks load-bearing.
It is not. Identity is the namespace and the opaque; `idea` is a label for the reader.

An id travels far from its file, into relations, code, and conversation, and the label says what sort of note it names without your opening anything: a relation pointing at `garden:idea:7fjq3ka` visibly points at an idea.

Because the label sits outside identity, it can never break anything.
The opaque alone finds the note, so a label that disagrees with the note's own kind is just wrong, and correcting it is a rewrite from the note itself.
And because a note never changes its kind, the label cannot go stale.

## The price

An opaque is not readable at a glance. This is the accepted cost.

A label written beside an id can drift after a rename until someone refreshes it, but the id beneath it never drifts, and restoring labels is one mechanical pass.
Concrete only ever sets around the part that cannot drift.
