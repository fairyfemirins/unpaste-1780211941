#!/usr/bin/env python3
"""
UnPaste: Autonomous clipboard unformatter.

Features:
- Runs in background (system tray).
- Intercepts Ctrl+V and strips formatting.
- Cross-platform (Linux/Windows/macOS).
- Minimal dependencies.

Usage:
  python3 unpaste.py
"""

import re
import pyperclip
import keyboard
import threading
import sys
from tkinter import Tk, Menu, PhotoImage
from PIL import Image, ImageTk

class UnPaste:
    def __init__(self):
        self.tray_icon = None
        self.running = False
        self.root = Tk()
        self.root.withdraw()  # Hide main window
        self.setup_tray()
        self.start_monitoring()

    def setup_tray(self):
        """Create system tray icon."""
        try:
            image = Image.open(self._get_icon_path())
            icon = ImageTk.PhotoImage(image)
            menu = Menu(self.root, tearoff=0)
            menu.add_command(label="Exit", command=self.stop)
            self.tray_icon = self.root.tk.call(
                'tk', 'windowingsystem') == 'x11' and 'tray' or 'systray',
                'create', icon, "UnPaste", menu
            )
        except Exception as e:
            print(f"Tray icon failed: {e}")

    def _get_icon_path(self):
        """Return platform-specific icon path."""
        return "assets/icon.png"

    def start_monitoring(self):
        """Start clipboard monitoring thread."""
        self.running = True
        threading.Thread(target=self._monitor_clipboard, daemon=True).start()
        keyboard.add_hotkey('ctrl+v', self._unformat_paste)

    def _monitor_clipboard(self):
        """Monitor clipboard for changes (fallback)."""
        last_value = ""
        while self.running:
            try:
                current_value = pyperclip.paste()
                if current_value != last_value:
                    last_value = current_value
                    if self._is_formatted(current_value):
                        pyperclip.copy(self._strip_formatting(current_value))
            except Exception as e:
                print(f"Clipboard error: {e}")
            threading.Event().wait(0.5)

    def _is_formatted(self, text):
        """Check if text contains HTML/XML tags or rich formatting."""
        return bool(re.search(r'<[^>]+>|\n{2,}|\t', text))

    def _strip_formatting(self, text):
        """Strip HTML/XML tags and normalize whitespace."""
        text = re.sub(r'<[^>]+>', '', text)  # Remove HTML/XML
        text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
        return text

    def _unformat_paste(self):
        """Intercept Ctrl+V and paste unformatted text."""
        try:
            clipboard_text = pyperclip.paste()
            if self._is_formatted(clipboard_text):
                unformatted = self._strip_formatting(clipboard_text)
                keyboard.write(unformatted)
        except Exception as e:
            print(f"Paste error: {e}")

    def stop(self):
        """Stop monitoring and exit."""
        self.running = False
        keyboard.unhook_all()
        self.root.quit()
        sys.exit(0)

if __name__ == "__main__":
    UnPaste().root.mainloop()