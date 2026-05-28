# Unpaste

**Unpaste** is a cross-platform CLI tool to strip formatting from clipboard text. It solves the common problem of pasting formatted text (e.g., from Office apps) into plaintext editors (e.g., Notepad, Markdown, terminals).

## Features
- **Cross-Platform**: Works on Linux, macOS, and Windows.
- **Minimal Dependencies**: Uses `xclip`/`xsel` (Linux), `pbcopy`/`pbpaste` (macOS), or PowerShell (Windows).
- **Autonomous**: No GUI or manual intervention required.

## Installation
```bash
# Clone the repo
git clone https://github.com/Femirins/unpaste.git
cd unpaste

# Make executable
chmod +x unpaste.py
```

## Usage
```bash
# Output unformatted text to stdout
./unpaste.py

# Copy unformatted text back to clipboard
./unpaste.py --copy

# Read from stdin (for testing or piping)
./unpaste.py --stdin < input.txt
```

## Examples
1. **Paste from Office to Markdown**:
   ```bash
   ./unpaste.py > notes.md
   ```

2. **Pipe from `curl`**:
   ```bash
   curl -s "https://example.com/formatted-text" | ./unpaste.py --stdin
   ```

## Technical Architecture
- **Input**: Clipboard (default) or stdin (`--stdin`).
- **Output**: Plaintext to stdout or clipboard (`--copy`).
- **Dependencies**:
  - Linux: `xclip` or `xsel`
  - macOS: `pbcopy`/`pbpaste`
  - Windows: PowerShell

## License
MIT