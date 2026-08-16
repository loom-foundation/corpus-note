---
id: note:dec:ye6hw6k
name: The documentation renders with VitePress
kind: decision
status: current
---

The end-user documentation under `docs/` is plain markdown rendered as a static site by VitePress.
Dependencies follow the latest stable release within each major version (caret ranges, no lockfile), so security and minor fixes arrive at build time.

## Context

The documentation is its own deliverable: plain markdown pages, never Note artefacts, self-contained and rendered for readers meeting Note cold.
The renderer had to take those pages unchanged, render Mermaid fences, build a fully static site, and stay disposable.

## Decision

VitePress builds `docs/` with one configuration file carrying two accommodations: `markdown-it-attrs` disabled so brace text in prose stays literal, and Mermaid via its plugin.
Dead links fail the build, because the docs never link outside their own tree.

## Forces and trade-offs

The two finalists were built from identical pages and compared as running sites.
VitePress ingested every page byte-identical, with three direct dependencies and a one-file exit; its default theme, search, and typography satisfied the owner in the browser.
The accepted cost: a Node toolchain enters the repository for the docs build alone, and unpinned minors trade reproducible builds for automatic fixes.

## Alternatives considered

Fumadocs: rejected; it demands `title:` frontmatter on every page and a `meta.json` among them, has no supported Mermaid path for plain markdown (the trial carried hand-written plugin and client code), and brings the largest dependency surface of the field for a presentation gain the built sites did not bear out.

## Driven by

[Documentation completes the increment](./req-docs.md){id=note:req:t9gnr2f}.
