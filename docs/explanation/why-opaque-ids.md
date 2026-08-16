# Why opaque ids

A note and its name are two things.
The name is wording, and wording improves: the label that felt right in March reads wrong in May, and renaming is routine, healthy work.

A citation is not.
Once an id is written into a commit message, a report, or a printed page, that surface never updates again; citations set like concrete.

So identity must hold nothing a rename changes, and an opaque holds nothing at all.

## Why not readable slugs

A readable slug, `tomatoes-south-fence`, conflates the note with its wording.
When the wording improves, one of two bad things happens: the slug stays and lies about the content, or the slug follows and every citation already set in concrete points at nothing.

Both failures come from the same conflation, and no renaming discipline removes them.

## Why not a tag beside a machine id

The obvious compromise keeps both: a human-chosen tag such as `IDEA-001`, kept next to a stable opaque.
It fails for a human reason.

The readable key is the one people remember, type, and cite, so it stays load-bearing at every surface where writing happens, and it strands citations all the same.
A second name does not relieve the first of its burden; it just gives the concrete two things to set around.

## The middle segment is a check digit

`garden:idea:7fjq3ka` seems to smuggle meaning back in: `idea` reads like part of a name.
It is redundancy, not identity.

The opaque alone finds at most one note in its namespace, so when the middle segment disagrees with the note's own kind, the repair is deterministic: the segment is rewritten from the note, and nothing dangles.

Like the last digit of a card number, it catches transcription errors without carrying anything the rest does not; what it earns on top is that an id met far from home still says what sort of note it names.

## The price

An opaque is not readable at a glance; that is the accepted cost.

A label written beside an id can drift after a rename until someone refreshes it, but the id beneath it never drifts, and restoring labels is one mechanical pass.
Concrete only ever sets around the part that cannot lie.
