# UnPaste: Cross-Platform Clipboard Unformatter

UnPaste is a lightweight CLI tool that automatically strips formatting from text when pasting. Inspired by a [Reddit request](https://www.reddit.com/r/SomebodyMakeThis/comments/bnnw3/), it solves the common problem of pasting formatted text from Office apps into plaintext editors.

## Features
- **Automatic Unformatting**: Strips formatting (e.g., bold, italics, fonts) on paste.
- **Cross-Platform**: Works on Linux, macOS, and Windows.
- **Minimal Dependencies**: Uses `pyperclip` and `pynput` (X11 required for Linux).

## Usage
### Installation
```bash
git clone https://github.com/fairyfemirins/unpaste.git
cd unpaste
pip install -r requirements.txt
```

### Run
```bash
python3 unpaste.py watch
```
- Monitors clipboard and strips formatting on paste.
- Press `Ctrl+C` to stop.

## Reproducible Tutorial
### Step 1: Clone the Repository
```bash
git clone https://github.com/fairyfemirins/unpaste.git
cd unpaste
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run UnPaste
```bash
python3 unpaste.py watch
```

### Step 4: Test
1. Copy formatted text from an Office app (e.g., LibreOffice, Word).
2. Paste into a plaintext editor (e.g., Vim, Notepad).
3. Verify formatting is stripped.

## Technical Architecture
### Core Logic
1. **Clipboard Monitoring**: Uses `pyperclip` to read clipboard content.
2. **Unformatting**: Re-copies text to strip formatting.
3. **Keyboard Listener**: Uses `pynput` to intercept `Ctrl+V`/`Cmd+V` (X11 required).

### Dependencies
- `pyperclip`: Cross-platform clipboard access.
- `pynput`: Keyboard event monitoring (Linux: requires X11).

## License
MIT License. See [LICENSE](LICENSE) for details.

## Note
This repository is published under `fairyfemirins/unpaste` due to GitHub namespace restrictions. A transfer to `femirins/unpaste` is pending.