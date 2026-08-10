---
id: note:ctx:h5btd4g
name: System context
kind: context
status: current
---

Standalone, Note is the system: the layer that represents intent and defines how it is checked.
Embedded in a larger system, Note is a subsystem of it; the boundary is the same either way.

## External entities

The entities the system interacts with:

- Actors, human and AI, that read and author artefacts through file access; some AI actors operate in constrained environments (sandboxes, runners, small models).
- A version control system, ordinarily Git: the substrate of record and the trust root (history, signatures, protected branches).
- Tools that consume or check the artefacts: continuous integration, Markdown renderers, code generators, schema validators.
- Sett, the reference tool, which reads the artefacts, computes derived views and validation, and proposes authoring changes; Sett is never authoritative.

## What crosses the boundary

Note defines representations and checks; whatever the adopter integrates it with consumes them.
Note depends on no other component and requires none to exist.

| From | To | Interaction |
|---|---|---|
| Actors (human / AI) | Note artefacts | Read and author through file access. |
| Sett | Note artefacts | Reads, computes derived views, proposes validated changes (never authoritative). |
| Version control / CI | Artefacts and merges | Stores, gates, signs. |

## What is out of scope

Stated negatively, on purpose.
Note does not:

- Decide identity or permission: which actor may act, and on what authority.
- Enforce access control over data: who may read or write is decided by the controls around the data.
- Build code from an artefact: building is a job performed by another actor or system.
- Execute checks or hold verdicts: Note represents the relation and defines checkability; running a check, and dispatching a verifying actor, happen outside it.
- Authorise lifecycle transitions: Note defines which are well-formed, who may make one is decided outside it.
- Compute or deliver signals: Note defines staleness, gaps, and horizons as facts derivable from the record; deriving them, and routing them to an owner, happen outside it.

How each excluded responsibility is met, and what the component meeting it is called (a job scheduler, an orchestrator, a Git host's controls with review, the permission model of a version control system or a filesystem), is the integrator's choice; Note names no such component and requires none.
The litmus test for any future responsibility: a statement about an artefact belongs to Note; a statement about an actor, a permission, or an execution belongs outside it.
