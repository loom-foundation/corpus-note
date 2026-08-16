---
id: note:crit:s1nyzds
name: Schema loads in stock SQLite
kind: acceptance-criterion
status: current
---

The schema file the specification cites as the model's record
loads whole into a fresh in-memory database of stock SQLite without error;
this checks the schema's well-formedness alone.
The same input deliberately corrupted fails to load.

## Relations

- qualifies: [Structure answers to one normalised model](./req-normalised-data-model.md){id=note:req:r050s7n}
