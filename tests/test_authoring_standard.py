"""The manifest declares the draw of the Note Authoring standard."""
# @intent verifies: note:req:kkn7wtj

import unittest
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = CORPUS_ROOT / "manifest.md"

REQUIRED_SECTION = (
    "  - namespace: authoring\n"
    "    source: ../note-authoring\n"
    "    pin: live\n"
)


def declares_authoring_draw(manifest_text):
    """True when the manifest carries the authoring draw section verbatim."""
    return REQUIRED_SECTION in manifest_text


class AuthoringDrawTest(unittest.TestCase):
    """The adoption the requirement states is declared where it says."""

    def test_manifest_declares_the_authoring_draw(self):
        self.assertTrue(
            declares_authoring_draw(MANIFEST_PATH.read_text(encoding="utf-8")),
            "manifest.md does not declare the authoring draw",
        )

    def test_a_manifest_without_the_draw_fails(self):
        self.assertFalse(declares_authoring_draw("---\nnamespace: note\n---\n"))


if __name__ == "__main__":
    unittest.main()
