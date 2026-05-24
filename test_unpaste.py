#!/usr/bin/env python3
"""
Mock test for unpaste.py
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from unpaste import Unpaste


class TestUnpaste(unittest.TestCase):
    def setUp(self):
        self.unpaste = Unpaste()

    @patch('pyperclip.paste')
    @patch('pyperclip.copy')
    def test_unpaste_logic(self, mock_copy, mock_paste):
        # Simulate clipboard content
        mock_paste.return_value = "Formatted Text"
        
        # Trigger _unpaste
        self.unpaste._unpaste()
        
        # Verify clipboard was overwritten with plain text
        mock_copy.assert_called_once_with("Formatted Text")

    @patch('pynput.keyboard.Listener')
    def test_start_stop(self, mock_listener):
        # Start the service
        with patch.object(self.unpaste, 'start'):
            self.unpaste.start()
            mock_listener.assert_called_once()

    def test_toggle(self):
        # Initial state
        self.assertTrue(self.unpaste.enabled)
        
        # Toggle off
        self.unpaste.toggle()
        self.assertFalse(self.unpaste.enabled)
        
        # Toggle on
        self.unpaste.toggle()
        self.assertTrue(self.unpaste.enabled)


if __name__ == "__main__":
    unittest.main()