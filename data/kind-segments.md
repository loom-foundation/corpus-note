---
id: note:dec:2rvz7gc
name: Kind segments chosen against the collision horizon
kind: decision
status: draft
---

The id segment of every registered kind, with the candidates weighed and the collision horizon considered.
A segment is unique corpus-wide and lives in every minted id, so it can never be renamed; the horizon is the set of plausible future kinds a candidate would foreclose.

| Kind | Candidates | Collision horizon | Selected | Reason |
|---|---|---|---|---|
| need | need, nd | none plausible | need | a full short word beats any cut |
| requirement | req, reqt, rqmt | req sits closest to a future requisite | req | the industry abbreviation, read cold by everyone |
| specification | spec, spc | spec would block specimen; implausible here | spec | the industry abbreviation |
| acceptance-criterion | crit, ac, accr | ac is too ambiguous (actor, activity); crit would block a future criticality | crit | the distinctive syllable of the compound |
| decision | dec, dcsn | dec sits near declaration; the declaration kinds take charter, kind, and verb | dec | the ADR tradition's abbreviation |
| persona | pers, per, psn | per would block performance and permission | pers | shortest unambiguous cut |
| context | ctx, con, cont | con and cont would block contract, convention, constraint | ctx | the programming abbreviation |
| term | term | none | term | full word |
| convention | conv, cnv | conv would block conversation; implausible here | conv | shortest pronounceable cut |
| principle | prin, princ, pri | pri would block priority | prin | shortest unambiguous cut |
| domain-charter | charter, dom, chart | dom would block domain itself as a future kind; chart would block chart | charter | the full word; rare enough to afford length |
| kind-declaration | kind, kdecl | claims the whole word kind | kind | see the note below |
| verb-declaration | verb, vdecl | claims the whole word verb | verb | see the note below |

## Notes

**req versus requisite.**
The owner's worked example of a horizon call: `req` is the one segment a future requisite kind would also want.
Requisite is implausible as a Note kind (it names a quality of a requirement, not an artefact), and `req` is the abbreviation every requirements tradition already reads; the foreclosure is accepted knowingly.

**kind and verb as whole-word claims.**
The floor 1 meta-kinds take the bare words `kind` and `verb` as segments, foreclosing them for any future kind.
The claim is deliberate: an id such as `note:kind:k9tvmr4` reads as exactly what the artefact is, and no future kind has a better claim to those words than the meta-kinds that declare kinds and verbs.
