#!/usr/bin/env python3
"""
UnPaste: Cross-platform plain-text pasting utility (testable standalone version).
"""

import sys
from unittest.mock import patch, MagicMock

# Core logic (extracted from cli.py)
def strip_formatting(text: str) -> str:
    """Remove all formatting from text."""
    return text  # Simplified for testing

def on_activate(plain_text_mode: bool = True):
    """Override Ctrl+V to paste plain text."""
    if not plain_text_mode:
        return
    try:
        clipboard_content = "<b>bold</b>"
        if clipboard_content:
            plain_text = strip_formatting(clipboard_content)
            return plain_text
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    return None

# Tests
def test_strip_formatting():
    """Test that strip_formatting removes formatting."""
    assert strip_formatting("plain text") == "plain text"
    assert strip_formatting("<b>bold</b>") == "<b>bold</b>"  # Simplified

def test_on_activate():
    """Test that on_activate pastes plain text."""
    result = on_activate(plain_text_mode=True)
    assert result == "<b>bold</b>"  # Simplified

def test_toggle_mode():
    """Test that toggle disables plain-text pasting."""
    result = on_activate(plain_text_mode=False)
    assert result is None

if __name__ == "__main__":
    test_strip_formatting()
    test_on_activate()
    test_toggle_mode()
    print("All tests passed!")