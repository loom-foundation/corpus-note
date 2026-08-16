---
id: note:spec:9dfybs4
name: Kind register
kind: specification
status: draft
---

The standing register of every kind token in force in this corpus, with its id segment and home domain.
It is the record the uniqueness law is checked against: corpus-wide, no two kinds share a token and no two share a segment.
A kind is registered here before its declaration is authored; the register fixes tokens, segments, and homes, never meanings.
Declarations live under `domains/<domain>/`.

| Kind token | Segment | Home domain | Declaration |
|---|---|---|---|
| need | need | requirements | declared (draft) |
| requirement | req | requirements | declared (draft) |
| specification | spec | requirements | undeclared |
| acceptance-criterion | crit | requirements | undeclared |
| decision | dec | architecture | undeclared |
| persona | pers | product | undeclared |
| context | ctx | architecture | undeclared |
| term | term | method | undeclared |
| convention | conv | method | undeclared |
| principle | prin | method | undeclared |
| domain-charter | charter | method | meta-shape drafted |
| kind-declaration | kind | method | meta-shape drafted |
| verb-declaration | verb | method | meta-shape drafted |

Every home domain except `requirements` is this prototype's proposal, unratified; only the Requirements domain is chartered.
