#!/usr/bin/env python3
"""
unpaste: Cross-platform CLI tool to strip formatting from clipboard text.
Usage:
  unpaste paste   # Simulate pasting plain text (prints to stdout)
  unpaste status  # Check clipboard status (mock)
"""

import re
import click
from unittest.mock import patch


def strip_formatting(text: str) -> str:
    """Remove HTML/XML tags and excessive whitespace from text."""
    text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text


@click.group()
def cli():
    """unpaste: Strip formatting from clipboard text."""
    pass


@cli.command()
def paste():
    """Simulate pasting plain text (prints to stdout)."""
    # Mock clipboard input
    mock_clipboard = "<b>Hello</b> <i>world</i>!  This has   extra spaces."
    plain_text = strip_formatting(mock_clipboard)
    print(f"Stripped text: {plain_text}")


@cli.command()
def status():
    """Check clipboard status (mock)."""
    print("Mock: Clipboard contains 42 characters.")


if __name__ == "__main__":
    cli()