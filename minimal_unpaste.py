#!/usr/bin/env python3
"""
Minimal UnPaste for testing.
"""

import re
import pyperclip
import keyboard

def strip_formatting(text):
    """Strip HTML/XML tags and normalize whitespace."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def unformat_paste():
    """Intercept Ctrl+V and paste unformatted text."""
    try:
        clipboard_text = pyperclip.paste()
        if re.search(r'<[^>]+>|\n{2,}|\t', clipboard_text):
            unformatted = strip_formatting(clipboard_text)
            keyboard.write(unformatted)
    except Exception as e:
        print(f"Paste error: {e}")

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+v', unformat_paste)
    print("UnPaste running. Press Ctrl+C to exit.")
    keyboard.wait()