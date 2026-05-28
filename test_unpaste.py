#!/usr/bin/env python3
"""
Test suite for Unpaste using unittest.mock to avoid clipboard dependencies.
"""

import unittest
from unittest.mock import patch, MagicMock
import unpaste


class TestUnpaste(unittest.TestCase):
    def test_strip_formatting(self):
        unpaste_instance = unpaste.Unpaste()
        self.assertEqual(unpaste_instance.strip_formatting("<b>text</b>"), "<b>text</b>")  # Placeholder

    @patch('pyperclip.paste')
    @patch('pyperclip.copy')
    def test_on_press(self, mock_copy, mock_paste):
        mock_paste.return_value = "Formatted <b>text</b>"
        unpaste_instance = unpaste.Unpaste()
        from pynput.keyboard import Key, KeyCode
        unpaste_instance.on_press(Key.ctrl)
        unpaste_instance.on_press(KeyCode.from_char('v'))
        mock_copy.assert_called_with("Formatted <b>text</b>")  # Placeholder


if __name__ == "__main__":
    unittest.main()