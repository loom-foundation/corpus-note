# Contributing to Note

Contributions are welcome from anyone. This project is governed openly: there is no invitation gate and no Contributor License Agreement. Quality is maintained by review against the method's own rules, not by restricting who may contribute.

## Licensing of contributions

Note is licensed under CC BY 4.0 (see [`LICENSE`](LICENSE)), with a patent non-assertion pledge maintained by The Loom Foundation (`governance/patents.md` in the `org` repository) covering independent implementations. Contributions are **inbound = outbound**: what you contribute is offered under the same license as the part of the work you are contributing to. There is no copyright assignment.

## Developer Certificate of Origin (DCO)

Every commit must be signed off under the [Developer Certificate of Origin 1.1](DCO). The sign-off certifies that you wrote the contribution or otherwise have the right to submit it under the applicable license. Add it with:

```
git commit -s
```

which appends a line of the form:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use your real name and a reachable email. There is no CLA to sign.

## How to contribute

- Before authoring, read `meta/README.md` and `meta/compartmentalization.md`. This corpus defines Note using Note, so it keeps the method, what Note is for any adopter, separate from how this repository authors it; Method artifacts are written for any sustained body of work, not for this corpus in particular.
- For methodology artifacts (needs, requirements, specifications, decision records, terms, personas), follow the principles in `loom/note/principles/`, the per-kind rules carried by the terms and the artifact-file-format specification under `loom/note/`, and the prose conventions in `meta/prose-conventions.md`; `docs/` carries worked authoring guidance.
- Open an issue or a discussion to propose a change before a large piece of work; substantial design choices are recorded as decision records under `loom/note/decisions/`.
- Keep commits focused and reference the artifacts they touch by their durable identifier.
