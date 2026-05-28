#!/usr/bin/env python3
"""
Unit tests for UnPaste.

Run with: python3 -m unittest test_unpaste.py
"""

import unittest
from unpaste import UnPaste

class TestUnPaste(unittest.TestCase):
    def setUp(self):
        self.unpaste = UnPaste()

    def test_is_formatted(self):
        self.assertTrue(self.unpaste._is_formatted("<b>bold</b>"))
        self.assertTrue(self.unpaste._is_formatted("line1\n\nline2"))
        self.assertFalse(self.unpaste._is_formatted("plain text"))

    def test_strip_formatting(self):
        self.assertEqual(
            self.unpaste._strip_formatting("<p>Hello<br>World</p>"),
            "Hello World"
        )
        self.assertEqual(
            self.unpaste._strip_formatting("line1\n\tline2"),
            "line1 line2"
        )

if __name__ == "__main__":
    unittest.main()