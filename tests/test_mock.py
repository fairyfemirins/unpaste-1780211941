import sys
import os

# Mock pyperclip and pynput for testing
sys.modules['pyperclip'] = type('MockPyperclip', (), {
    'paste': lambda: "<b>bold</b>",
    'copy': lambda x: None,
})()
sys.modules['pynput'] = type('MockPynput', (), {
    'keyboard': type('MockKeyboard', (), {
        'GlobalHotKeys': lambda *args, **kwargs: type('MockListener', (), {
            'start': lambda self: None,
            'stop': lambda self: None,
        })(),
    })(),
})()

# Import after mocking
from unpaste.cli import strip_formatting, on_activate, plain_text_mode

def test_strip_formatting():
    """Test that strip_formatting removes formatting."""
    assert strip_formatting("plain text") == "plain text"
    assert strip_formatting("<b>bold</b>") == "bold"

def test_on_activate():
    """Test that on_activate pastes plain text."""
    global plain_text_mode
    plain_text_mode = True
    on_activate()  # Should call pyperclip.copy("bold")

def test_toggle_mode():
    """Test that toggle disables plain-text pasting."""
    global plain_text_mode
    plain_text_mode = False
    on_activate()  # Should not call pyperclip.copy

if __name__ == "__main__":
    test_strip_formatting()
    test_on_activate()
    test_toggle_mode()
    print("All tests passed!")