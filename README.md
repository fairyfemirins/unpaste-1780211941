# unpaste

**unpaste** is a cross-platform CLI tool that strips formatting from clipboard text before pasting. It solves the common problem of unwanted formatting when copying text from web pages, documents, or applications.

## Features
- **Strip Formatting**: Removes HTML/XML tags and normalizes whitespace.
- **Cross-Platform**: Works on Linux, macOS, and Windows.
- **CLI-Friendly**: Simple commands for integration into workflows.

## Installation
```bash
pip install --user click
```

## Usage
```bash
# Simulate pasting plain text (prints to stdout)
unpaste paste

# Check clipboard status (mock)
unpaste status
```

## Example
**Input:** `<b>Hello</b> <i>world</i>!  This has   extra spaces.`
**Output:** `Hello world! This has extra spaces.`

## License
MIT