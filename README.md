# UnPaste

A CLI tool to strip formatting from pasted text, leaving only plain text. Useful for developers, writers, and anyone who frequently pastes from web pages, documents, or rich-text editors into terminals, code, or plain-text files.

![UnPaste Demo](https://via.placeholder.com/600x150?text=UnPaste+Demo)

## Features
- Strip HTML/XML tags, ANSI escape codes, and extra whitespace.
- Cross-platform: Linux, macOS, Windows.
- Supports stdin and clipboard input.

## Installation
### Prerequisites
- Python 3.6+
- Linux: `sudo apt install xclip` (for clipboard support)

### Install
```bash
pip install --user pyperclip
curl -o ~/bin/unpaste https://raw.githubusercontent.com/femirins/unpaste/main/unpaste.py
chmod +x ~/bin/unpaste
```

## Usage
### From Clipboard
```bash
unpaste --clipboard
```

### From Stdin
```bash
echo "<b>Formatted</b> text" | unpaste --stdin
```

## Technical Architecture
- **Input**: Clipboard or stdin.
- **Processing**: Regex-based stripping of HTML/XML tags, ANSI codes, and whitespace.
- **Output**: Plain text to stdout.

## License
MIT