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

## Repository URL

Due to rebase conflicts, this repository is published at:
[https://github.com/fairyfemirins/unpaste](https://github.com/fairyfemirins/unpaste)

## Transfer Instructions

To request a transfer:
1. Open an issue in this repository.
2. Contact `@femirins` on GitHub.

### Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/unpaste/settings](https://github.com/fairyfemirins/unpaste/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`femirins`) and confirm.

## License
MIT