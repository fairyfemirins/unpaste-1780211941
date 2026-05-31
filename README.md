# unpaste

**Autonomous Clipboard Utility** – Monitor, filter, and auto-format clipboard content with regex rules.

## Features
- **Autonomous Monitoring**: Runs in the background, detects clipboard changes.
- **Regex Filtering**: User-defined rules to auto-format or ignore content.
- **Markdown Conversion**: Auto-converts URLs, code snippets, and text to markdown.
- **History Logging**: Saves clipboard history to `~/.unpaste/history.json`.

## Installation
```bash
pip install --user -r requirements.txt
```

## Usage
### Daemon Mode
```bash
python3 unpaste.py --daemon
```

### Custom Rules
1. Create a `rules.yaml` file:
   ```yaml
   markdown_links:
     pattern: "(https?://[^\\s]+)"
     replacement: "[\\1](\\1)"
   ```
2. Run with custom rules:
   ```bash
   python3 unpaste.py --rules "rules.yaml" --daemon
   ```

## License
MIT