-- The standing schema of Note's structure: the single source of truth,
-- extended by increments.
-- ANSI SQL DDL in the subset stock SQLite loads; the markdown structure of
-- plain files, frontmatter metadata, and the `## Relations` body section
-- implements the model as faithfully as the medium allows.
-- This first slice holds the atom: the plain note file and its identity.

-- The register of kinds: each kind token carries one id segment.
CREATE TABLE kind (
    token        VARCHAR(32) NOT NULL,  -- the kind token, authoritative for the segment
    segment      VARCHAR(8)  NOT NULL,  -- the id's middle segment, rendered from the token
    CONSTRAINT pk_kind PRIMARY KEY (token),
    CONSTRAINT uq_kind_segment UNIQUE (segment),
    CONSTRAINT ck_kind_token_lowercase CHECK (token = LOWER(token)),
    CONSTRAINT ck_kind_segment_lowercase CHECK (segment = LOWER(segment))
);

-- The artefact: one markdown file, one row.
-- Identity is the namespace and the opaque; the id a file spells,
-- <namespace>:<kind-segment>:<opaque>, is derivable from the record,
-- its middle segment rendered from `kind`.
CREATE TABLE artefact (
    namespace  VARCHAR(64)  NOT NULL,  -- the id's first segment, declared once in the manifest
    opaque     VARCHAR(64)  NOT NULL,  -- the id's last segment, minted once
    kind       VARCHAR(32)  NOT NULL,  -- the kind token, authoritative for the id's middle segment
    name       VARCHAR(255) NOT NULL,  -- a concise label
    status     VARCHAR(16)  NOT NULL,  -- a required token; this slice fixes no value set
    CONSTRAINT pk_artefact PRIMARY KEY (namespace, opaque),
    CONSTRAINT fk_artefact_kind FOREIGN KEY (kind) REFERENCES kind (token),
    CONSTRAINT ck_artefact_namespace_lowercase CHECK (namespace = LOWER(namespace)),
    CONSTRAINT ck_artefact_opaque_lowercase CHECK (opaque = LOWER(opaque))
);

-- =====================================================================
-- UNENFORCED-CONSTRAINTS REGISTER
-- Constraints the model states that the markdown medium cannot enforce,
-- some beyond this DDL subset too; each names what compensates for it,
-- or an honest none, and each is checkable from the record.
-- =====================================================================
-- artefact.opaque: lowercase Crockford Base32 (0 to 9 and a to z, minus
--   i, l, o, u), compared case-insensitively. No portable check
--   constraint states a character class. Compensated by nothing yet;
--   the rule is checkable from any id alone.
-- artefact.opaque: the default length is seven, configured per corpus in
--   its manifest and governing new ids only; mixed lengths are lawful
--   within one namespace, and opaques of different lengths never
--   collide. The typed bound above is storage, not the rule.
--   Compensated by nothing yet.
-- pk_artefact: nothing in one file enforces uniqueness of the opaque
--   within its namespace; a sweep wherever the namespace is kept
--   decides it. Compensated by the mint procedure's collision grep,
--   run in every repository holding the namespace.
-- fk_artefact_kind: stricter than the medium. A well-formed token no
--   register defines still makes an artefact; the unknown token is a
--   warning, never a bar on the file. Compensated by the warning-tier
--   report; nothing refuses the file.
-- artefact identity: an id is minted once and never changes; a move or
--   a rename leaves it untouched. Immutability is history, which no DDL
--   states. Compensated by review over git history; a changed id reads
--   as a new artefact.
-- artefact identity: the kind-segment is never stored in a row; it is
--   always derived through the kind join, the schema's own statement
--   that the segment is not identity. Compensated by the sweep rule:
--   citers are matched on namespace and opaque alone.
-- kind.token: lowercase letters with single hyphens between words; the
--   lowercase check holds, the letters-and-hyphens shape has no
--   portable constraint. Compensated by nothing yet; checkable from
--   the kind register.
-- kind.segment: two to five characters; the typed bound above is
--   storage, not the rule, and no portable length function sits in the
--   ANSI-and-SQLite intersection this corpus fixes. Compensated by the
--   kind register and the abbreviation-planning review.
