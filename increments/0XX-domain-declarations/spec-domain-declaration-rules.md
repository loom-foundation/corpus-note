---
id: note:spec:w3jq8kt
name: Domain declaration rules
kind: specification
status: draft
---

The normative rules every domain declaration obeys.
A domain declaration is the set of artefacts, a charter with kind and verb declarations, by which a domain adds its vocabulary to a corpus.
In every rule below, "the in-force set" is every declaration reachable from the corpus manifest through its declared edges at their declared pins, and "corpus-wide" means this corpus together with everything the in-force set brings.

## Kind declarations

Every kind declaration in the in-force set carries exactly these five facts; a declaration missing any of them does not enter force:

1. The kind token and its id segment.
2. The one home domain the kind belongs to.
3. Its frontmatter fields beyond the envelope, each with its name, whether it is required or optional, its value grammar, whether it is citation-bearing, and whether it is slice-pulling.
4. The body sections required at the `standard` profile; the `bare` profile stays substrate-owned.
5. Its coverage expectations, each as a gap name, the closing verb or verbs, and the direction of the closing edge.

A fact with nothing to declare is declared as none, never omitted, so silence never needs interpreting.

## Verb declarations

Every verb declaration in the in-force set carries exactly these five facts; a declaration missing any of them does not enter force:

1. The verb name.
2. The signature: the permitted source-and-target kind pairs, the source being the authoring end.
3. The computed inverse's display name.
4. Whether slices traverse its edges; the default is yes, and an opt-out is explicit.
5. Its structural constraints where load-bearing, such as acyclicity or target cardinality; a verb without them declares none.

Every kind a signature names is registered in the kind register at the time the declaration enters force.

## Meta-laws

Three laws bind every declaration in the in-force set:

1. **Monotonicity.**
   Composition is purely additive: no declaration removes, narrows, or redefines anything another declaration in the in-force set declares.
   A declaration may add signature pairs only to verbs its own domain homes, or pairs whose source kind its own domain homes.
   Adding a declaration to the in-force set never changes a fact already derivable from the set without it.
2. **The in-force set is declared.**
   Which declarations are in force is fixed solely by the corpus manifest's edges and pins.
   Movement past a pin is reported, never applied; nothing enters force by discovery.
3. **The undeclared stays inert.**
   An artefact whose kind, or an edge whose verb, no declaration in the in-force set declares is a warning and inert for every derived fact; it is never a guess and never an error.

## Substrate untouchability

No declaration redefines the substrate: the artefact envelope, identity, lifecycle, or the declarations of any other domain.
A declaration that cannot say what its domain needs is evidence about the meta-shape, amended centrally, never worked around locally.

## Uniqueness

Corpus-wide:

1. No two kinds share a token.
2. No two kinds share an id segment.
3. No two verbs share a name, and no verb name collides with any computed inverse name.

The kind register and the verb register are the standing record these laws are checked against.
A token, segment, or verb name absent from its register is unregistered, and its declaration does not enter force.
