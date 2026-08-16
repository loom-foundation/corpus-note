"""The tutorial's worked example behaves as the docs teach.

Exercises docs/examples/first-note/note.md, the exact file built by
docs/guide/your-first-note.md.
If the taught behaviour changes, this fails before a reader does.

@intent verifies: note:crit:b6wpk5s
"""

import re
import shutil
import tempfile
import unittest
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = CORPUS_ROOT / "docs" / "examples" / "first-note" / "note.md"

OPAQUE_ALPHABET = "0123456789abcdefghjkmnpqrstvwxyz"
ID_PATTERN = re.compile(
    r"^(?P<namespace>[a-z][a-z0-9]*)"
    r":(?P<segment>[a-z]+(?:-[a-z]+)*)"
    r":(?P<opaque>[" + OPAQUE_ALPHABET + r"]{7})$"
)


def split_note(text):
    """Return (ordered frontmatter (key, value) pairs, body lines)."""
    lines = text.split("\n")
    if lines[0] != "---":
        raise ValueError("no opening frontmatter delimiter")
    close = lines.index("---", 1)
    fields = []
    for line in lines[1:close]:
        key, _, value = line.partition(": ")
        fields.append((key, value))
    return fields, lines[close + 1 :]


def id_of(text):
    """The note's id, read from the file's own content alone."""
    fields, _ = split_note(text)
    return dict(fields)["id"]


class FirstNoteEnvelopeTest(unittest.TestCase):
    """The envelope stands as the tutorial and the reference teach it."""

    @classmethod
    def setUpClass(cls):
        cls.text = NOTE_PATH.read_text(encoding="utf-8")
        cls.fields, cls.body = split_note(cls.text)

    def test_required_fields_in_the_recommended_order(self):
        self.assertEqual(
            [key for key, _ in self.fields[:4]],
            ["id", "name", "kind", "status"],
        )

    def test_one_blank_line_then_the_lead(self):
        self.assertEqual(self.body[0], "", "no blank line after the frontmatter")
        self.assertTrue(self.body[1], "no lead after the blank line")
        self.assertNotEqual(self.body[1], "", "the lead is missing")

    def test_the_lead_is_unheaded(self):
        self.assertFalse(self.body[1].startswith("#"))


class FirstNoteIdentityTest(unittest.TestCase):
    """The id follows the taught grammar and lives inside the file."""

    @classmethod
    def setUpClass(cls):
        cls.text = NOTE_PATH.read_text(encoding="utf-8")

    def test_the_id_matches_the_taught_grammar(self):
        match = ID_PATTERN.match(id_of(self.text))
        self.assertIsNotNone(match, "id does not match namespace:segment:opaque")

    def test_the_opaque_draws_only_from_the_alphabet(self):
        opaque = id_of(self.text).rsplit(":", 1)[1]
        self.assertTrue(set(opaque) <= set(OPAQUE_ALPHABET))
        self.assertFalse(set(opaque) & set("ilou"))

    def test_the_segment_matches_the_kind(self):
        fields = dict(split_note(self.text)[0])
        segment = fields["id"].split(":")[1]
        self.assertEqual(segment, fields["kind"])

    def test_moving_the_file_does_not_change_the_id(self):
        before = id_of(self.text)
        with tempfile.TemporaryDirectory() as elsewhere:
            moved = Path(elsewhere) / "beds" / "south-fence.md"
            moved.parent.mkdir()
            shutil.copy(NOTE_PATH, moved)
            after = id_of(moved.read_text(encoding="utf-8"))
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
