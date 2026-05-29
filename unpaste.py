#!/usr/bin/env python3
"""
UnPaste - A CLI tool to strip formatting from pasted text, leaving only plain text.

Usage:
  echo "<b>Formatted</b> text" | python3 unpaste.py --stdin
  python3 unpaste.py --clipboard
"""

import re
import sys
import argparse
import pyperclip


def unformat_text(text: str) -> str:
    """Strip HTML tags, extra whitespace, and common formatting artifacts."""
    # Remove HTML/XML tags
    text = re.sub(r'<[^>]*>', '', text)
    # Remove ANSI escape codes
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    # Collapse multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def main():
    parser = argparse.ArgumentParser(description='UnPaste - Strip formatting from text')
    parser.add_argument('--stdin', action='store_true', help='Read from stdin instead of clipboard')
    parser.add_argument('--clipboard', action='store_true', help='Read from clipboard (default)')
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read().strip()
    elif args.clipboard or not sys.stdin.isatty():
        try:
            text = pyperclip.paste()
        except Exception as e:
            print(f"Error accessing clipboard: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    print(unformat_text(text))


if __name__ == "__main__":
    main()