"""The schema file the specification cites loads in stock SQLite;
a deliberately corrupted copy fails.
"""
# @intent verifies: note:crit:s1nyzds

import sqlite3
import unittest
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = CORPUS_ROOT / "data" / "schema.sql"
SKIP_REASON = "schema not yet authored: {0}".format(SCHEMA_PATH)


def corrupt(sql):
    """Return a deliberately broken copy of the given SQL."""
    return sql + "\nCREATE TABLE ("


def load_in_memory(sql):
    """Execute the SQL against a fresh in-memory SQLite database."""
    connection = sqlite3.connect(":memory:")
    try:
        connection.executescript(sql)
    finally:
        connection.close()


class LoadAndCorruptTest(unittest.TestCase):
    """The load and corruption helpers, checked on strings alone."""

    CLEAN_DDL = "CREATE TABLE kind (segment VARCHAR(16) PRIMARY KEY);"

    def test_clean_ddl_loads(self):
        load_in_memory(self.CLEAN_DDL)

    def test_corrupted_ddl_raises(self):
        with self.assertRaises(sqlite3.Error):
            load_in_memory(corrupt(self.CLEAN_DDL))


class SchemaLoadsTest(unittest.TestCase):
    """The criterion itself, run against the schema once it exists."""

    def setUp(self):
        if not SCHEMA_PATH.exists():
            self.skipTest(SKIP_REASON)
        self.schema = SCHEMA_PATH.read_text(encoding="utf-8")

    def test_schema_carries_sql(self):
        self.assertTrue(self.schema.strip(), "the schema file is empty")

    def test_schema_loads(self):
        load_in_memory(self.schema)

    def test_corrupted_copy_fails(self):
        with self.assertRaises(sqlite3.Error):
            load_in_memory(corrupt(self.schema))


if __name__ == "__main__":
    unittest.main()
