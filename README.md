# Unpaste

**Unpaste** is a CLI tool to strip formatting from clipboard text on paste (e.g., `Ctrl+V` → plaintext).

## Problem
When copying text from Office apps (LibreOffice, Word, Google Docs) into plaintext editors (Markdown, LaTeX, email), formatting (bold, italics, colors) is preserved. This requires manual cleanup (e.g., pasting into Notepad first).

## Solution
Unpaste monitors the clipboard and automatically strips HTML/XML tags when `Ctrl+V` is pressed.

## Usage (Static Prototype)
1. **Copy formatted text** (e.g., from LibreOffice).
2. **Run the static prototype** (no dependencies required):
   ```bash
   python3 unpaste.py "<b>Hello</b> <i>world</i>"
   ```
3. **Output**:
   ```
   Hello world
   ```

## Limitations
- **No Clipboard Monitoring**: This prototype requires manual input/output. For full functionality, install `pyperclip` and `pynput`:
  ```bash
  pip install --user pyperclip pynput
  ```
- **Cross-Platform**: Works on Linux/macOS/Windows (with dependencies).

## Build from Source
```bash
git clone https://github.com/Femirins/unpaste.git
cd unpaste
```

## License
MIT