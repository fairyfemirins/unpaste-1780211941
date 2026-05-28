# Unpaste

**Unpaste** is a cross-platform CLI tool that strips formatting from clipboard text on paste. No more pasting bold/colored text from Word or Google Docs into your emails or notes!

## Features
- **Automatic Formatting Removal**: Detects `Ctrl+V`/`Cmd+V` and strips formatting.
- **Cross-Platform**: Works on Linux, macOS, and Windows.
- **CLI Interface**: Start/stop monitoring with `unpaste --start`/`--stop`.

## Installation
```bash
pip install unpaste
```

## Usage
```bash
unpaste --start   # Start monitoring clipboard
unpaste --stop    # Stop monitoring
```

## Static Prototype
Try the [static demo](static/index.html) to see how it works:
```bash
python3 -m http.server 8000
```

## Limitations
- **No Backend**: The static prototype demonstrates the concept but cannot modify the clipboard.
- **Dependencies**: Requires `pyperclip` and `pynput` (installation may be blocked in PEP 668 environments).

## License
MIT