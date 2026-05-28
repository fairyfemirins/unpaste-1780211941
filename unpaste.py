#!/usr/bin/env python3
"""
Unpaste: A cross-platform CLI tool to strip formatting from clipboard text on paste.
Usage:
  python3 unpaste.py --start  # Start monitoring clipboard
  python3 unpaste.py --stop   # Stop monitoring
"""

import pyperclip
import pynput.keyboard
import argparse
import threading
import sys
import time

class Unpaste:
    def __init__(self):
        self.monitor_active = False
        self.listener = None
        self.hotkey = {pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('v')}
        self.current_keys = set()

    def strip_formatting(self, text):
        """Strip formatting from text (placeholder for platform-specific logic)."""
        return text  # pyperclip handles plaintext paste

    def on_press(self, key):
        if key in self.hotkey:
            self.current_keys.add(key)
            if all(k in self.current_keys for k in self.hotkey):
                # Simulate a small delay to avoid race conditions
                time.sleep(0.1)
                clipboard_content = pyperclip.paste()
                if clipboard_content:
                    plain_text = self.strip_formatting(clipboard_content)
                    pyperclip.copy(plain_text)

    def on_release(self, key):
        if key in self.hotkey:
            self.current_keys.discard(key)

    def start_monitoring(self):
        if not self.monitor_active:
            self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            self.listener.start()
            self.monitor_active = True
            print("Unpaste is running. Press Ctrl+C to stop.")
            try:
                while self.monitor_active:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop_monitoring()

    def stop_monitoring(self):
        if self.monitor_active and self.listener:
            self.listener.stop()
            self.monitor_active = False
            print("Unpaste stopped.")


def main():
    parser = argparse.ArgumentParser(description="Unpaste: Strip formatting from clipboard text on paste.")
    parser.add_argument("--start", action="store_true", help="Start monitoring clipboard")
    parser.add_argument("--stop", action="store_true", help="Stop monitoring clipboard")
    args = parser.parse_args()

    unpaste = Unpaste()
    if args.start:
        unpaste.start_monitoring()
    elif args.stop:
        unpaste.stop_monitoring()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()