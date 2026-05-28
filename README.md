# UnPaste: Autonomous Clipboard Unformatter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**UnPaste** is a background app that **intercepts Ctrl+V** and strips formatting **before** pasting. Inspired by [this r/SomebodyMakeThis post](https://www.reddit.com/r/SomebodyMakeThis/comments/bnnw3/).

## Features
- Runs in background (system tray).
- Intercepts Ctrl+V and strips HTML/XML/rich formatting.
- Cross-platform (Linux/Windows/macOS).
- Minimal dependencies (`pyperclip`, `keyboard`).

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install pyperclip keyboard
```

## Usage
```bash
python3 unpaste.py
```
- Press `Ctrl+C` to exit.

## Technical Architecture
- **Clipboard Monitoring**: `pyperclip` + `keyboard` hotkey.
- **Formatting Detection**: Regex for HTML/XML tags and whitespace.
- **System Tray**: `tkinter` + `PIL` (fallback to console if GUI unavailable).

## Limitations
- Requires GUI environment (X11/Wayland) for clipboard access.
- Tested on Linux; Windows/macOS may need adjustments.

## License
MIT