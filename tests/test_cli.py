import pytest
from unittest.mock import patch, MagicMock
from unpaste.cli import strip_formatting, on_activate, plain_text_mode

def test_strip_formatting():
    """Test that strip_formatting removes formatting."""
    assert strip_formatting("plain text") == "plain text"
    assert strip_formatting("<b>bold</b>") == "bold"  # Simplified for testing

def test_on_activate():
    """Test that on_activate pastes plain text."""
    global plain_text_mode
    plain_text_mode = True
    with patch('pyperclip.paste', return_value="<b>bold</b>"):
        with patch('pyperclip.copy') as mock_copy:
            on_activate()
            mock_copy.assert_called_once_with("bold")

def test_toggle_mode():
    """Test that toggle disables plain-text pasting."""
    global plain_text_mode
    plain_text_mode = True
    with patch('pyperclip.paste', return_value="<b>bold</b>"):
        with patch('pyperclip.copy') as mock_copy:
            plain_text_mode = False
            on_activate()
            mock_copy.assert_not_called()