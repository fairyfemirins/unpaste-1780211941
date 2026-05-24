#!/usr/bin/env python3
"""
unpaste: A cross-platform CLI tool to paste unformatted text by default.

Usage:
  python3 unpaste.py start   # Start the background service
  python3 unpaste.py stop    # Stop the service
  python3 unpaste.py toggle  # Toggle on/off

How it works:
  - Listens for Ctrl+V globally.
  - When detected, replaces clipboard content with plain text.
  - Pastes the unformatted text.
"""

import sys
import signal
import pyperclip
from pynput import keyboard

class Unpaste:
    def __init__(self):
        self.listener = None
        self.enabled = True
        self.hotkey = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('v')}
        self.pressed = set()

    def start(self):
        def on_press(key):
            if key in self.hotkey:
                self.pressed.add(key)
                if all(k in self.pressed for k in self.hotkey):
                    self._unpaste()

        def on_release(key):
            if key in self.pressed:
                self.pressed.remove(key)

        self.listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        self.listener.start()
        print("unpaste: Service started. Press Ctrl+C to stop.")
        self.listener.join()

    def _unpaste(self):
        if not self.enabled:
            return
        try:
            # Get clipboard content as plain text
            text = pyperclip.paste()
            if text:
                pyperclip.copy(text)  # Overwrite clipboard with plain text
                # Simulate paste (platform-specific)
                self._simulate_paste()
        except Exception as e:
            print(f"unpaste: Error - {e}")

    def _simulate_paste(self):
        # Platform-specific paste simulation
        import platform
        system = platform.system()
        if system == "Windows":
            import pyautogui
            pyautogui.hotkey('ctrl', 'v')
        elif system == "Darwin":  # macOS
            import pyautogui
            pyautogui.hotkey('command', 'v')
        else:  # Linux
            from pynput.keyboard import Controller
            keyboard = Controller()
            keyboard.press(keyboard.Key.ctrl_l)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(keyboard.Key.ctrl_l)

    def stop(self):
        if self.listener:
            self.listener.stop()
        print("unpaste: Service stopped.")

    def toggle(self):
        self.enabled = not self.enabled
        status = "enabled" if self.enabled else "disabled"
        print(f"unpaste: {status}")


def main():
    unpaste = Unpaste()
    if len(sys.argv) < 2:
        print("Usage: unpaste.py [start|stop|toggle]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "start":
        try:
            unpaste.start()
        except KeyboardInterrupt:
            unpaste.stop()
    elif command == "stop":
        unpaste.stop()
    elif command == "toggle":
        unpaste.toggle()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()