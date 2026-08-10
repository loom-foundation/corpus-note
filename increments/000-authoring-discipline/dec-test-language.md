---
id: note:dec:ny9msbj
name: Corpus tests use Python standard library unittest
kind: decision
status: current
---

The corpus's verifications and automated tests are written in Python 3, standard library only, with unittest; the floor is Python 3.9.
One `check` entry point at the corpus root is run identically by contributors before a pull request and by the GitHub Action.

## Context

The corpus carries automated tests that gate pull-request merges.
They check the corpus's own files (structure, conventions, link integrity, extractable artefacts such as SQL DDL), not application software, and their volume stays in the tens.
One script must run identically on a contributor's macOS or Linux machine and on GitHub-hosted runners.

## Decision

Tests live under `tests/` as `test_*.py` files, one concern per file, discovered by convention with no registry to maintain.
The entry point is `check` at the corpus root:

```sh
#!/bin/sh
# All corpus checks. CI runs exactly this.
# unittest exits 5 when no tests exist yet; that is not a failure.
set -eu
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -v || {
  s=$?
  [ "$s" -eq 5 ] && exit 0
  exit "$s"
}
```

The GitHub Action step is checkout, then `./check` on `ubuntu-latest`; nothing else is installed or configured.
The checks are accelerating tooling; no artefact ever requires them.

## Forces and trade-offs

The method's floor is any actor with an editor and a shell, offline, with zero configuration.

Stock macOS ships Python 3.9.6 with `unittest` and `sqlite3` importable, and GitHub-hosted runners preinstall Python 3, so the checks run inside that floor with nothing installed: no lockfile, no package manager, no network.

The test subject is text files, and Python's string, path, and regex handling reads cold in a way portable shell does not.
One entry point run verbatim locally and in CI removes the local-versus-CI split before it exists.

The accepted cost: Python becomes an implicit dependency of the checks (not of the method), and unittest's class-based style is mildly ceremonious.
At tens of tests that cost stays small, and the suite ports to pytest unchanged if volume ever justifies it.

## Alternatives considered

POSIX shell, plain: rejected; extracting fenced blocks and frontmatter needs awk and sed, whose BSD and GNU dialects diverge, and every assertion, diff, and failure message is hand-rolled, the highest-maintenance option at tens of string-parsing tests.

POSIX shell with Bats: rejected; Bats fixes the reporting but is an external installation on contributor machines and runners, which loses shell's one advantage of sitting inside the method's floor.

Python 3 with pytest, managed with uv: rejected; nicer assertions and fixtures do not buy back a package manager, a lockstep of tool versions, and a network fetch on first run, against an offline, zero-configuration floor.

Node.js with node:test: rejected; Node is not preinstalled on stock macOS and nothing else in the corpus pulls JavaScript in, an installation burden for no capability Python lacks here.

Go, Rust, Deno: rejected; each brings a compiled or single-binary toolchain no contributor to a prose corpus otherwise needs, disproportionate for tens of file checks.

## Driven by

The owner's direction that the methodology carries automated tests, and continuous integration gating pull-request merges, with one script contributors run before submitting and the GitHub Action reuses verbatim.
