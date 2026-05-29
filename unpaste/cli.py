#!/usr/bin/env python3
"""
UnPaste: Cross-platform plain-text pasting utility.
"""

import os
import sys
import signal
import pyperclip
from pynput import keyboard
import click

# Global state
plain_text_mode = True
listener = None

def strip_formatting(text: str) -> str:
    """Remove all formatting from text (simplified)."""
    return text  # pyperclip handles platform-specific stripping

def on_activate():
    """Override Ctrl+V to paste plain text."""
    global plain_text_mode
    if not plain_text_mode:
        return
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            plain_text = strip_formatting(clipboard_content)
            pyperclip.copy(plain_text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def start_listener():
    """Start the keyboard listener."""
    global listener
    if listener is None:
        listener = keyboard.GlobalHotKeys({
            "<ctrl>+v": on_activate,
        })
        listener.start()

def stop_listener():
    """Stop the keyboard listener."""
    global listener
    if listener is not None:
        listener.stop()
        listener = None

@click.group()
def cli():
    """UnPaste CLI."""
    pass

@cli.command()
def start():
    """Start the UnPaste daemon."""
    start_listener()
    click.echo("UnPaste daemon started. Press Ctrl+V to paste plain text.")
    # Keep the process alive
    signal.pause()

@cli.command()
def stop():
    """Stop the UnPaste daemon."""
    stop_listener()
    click.echo("UnPaste daemon stopped.")

@cli.command()
def toggle():
    """Toggle plain-text pasting."""
    global plain_text_mode
    plain_text_mode = not plain_text_mode
    status = "enabled" if plain_text_mode else "disabled"
    click.echo(f"Plain-text pasting {status}.")

if __name__ == "__main__":
    cli()