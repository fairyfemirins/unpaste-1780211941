#!/usr/bin/env python3
"""
Unpaste: A cross-platform CLI tool to strip formatting from clipboard text.

Usage:
  unpaste          # Output unformatted text to stdout
  unpaste --copy   # Copy unformatted text back to clipboard
  unpaste --help   # Show this help message

Supported Platforms:
  - Linux (requires xclip or xsel)
  - macOS (requires pbcopy/pbpaste)
  - Windows (via PowerShell)
"""

import sys
import subprocess
import argparse


def get_clipboard():
    """Get clipboard content as plain text."""
    try:
        # Linux (xclip or xsel)
        if sys.platform == "linux":
            for cmd in ["xclip", "xsel"]:
                try:
                    return subprocess.check_output(
                        [cmd, "-o", "-selection", "clipboard"], 
                        stderr=subprocess.DEVNULL, 
                        text=True
                    ).strip()
                except FileNotFoundError:
                    continue
            raise RuntimeError("Neither xclip nor xsel found. Install one of them.")
        
        # macOS
        elif sys.platform == "darwin":
            return subprocess.check_output(
                ["pbpaste"], 
                stderr=subprocess.DEVNULL, 
                text=True
            ).strip()
        
        # Windows
        elif sys.platform == "win32":
            return subprocess.check_output(
                ["powershell", "-command", "Get-Clipboard"], 
                stderr=subprocess.DEVNULL, 
                text=True
            ).strip()
        
        else:
            raise RuntimeError("Unsupported platform.")
    
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to read clipboard: {e}")


def set_clipboard(text):
    """Set clipboard content to plain text."""
    try:
        # Linux (xclip or xsel)
        if sys.platform == "linux":
            for cmd in ["xclip", "xsel"]:
                try:
                    subprocess.run(
                        [cmd, "-i", "-selection", "clipboard"], 
                        input=text, 
                        text=True, 
                        check=True
                    )
                    return
                except FileNotFoundError:
                    continue
            raise RuntimeError("Neither xclip nor xsel found. Install one of them.")
        
        # macOS
        elif sys.platform == "darwin":
            subprocess.run(
                ["pbcopy"], 
                input=text, 
                text=True, 
                check=True
            )
        
        # Windows
        elif sys.platform == "win32":
            subprocess.run(
                ["powershell", "-command", "Set-Clipboard", "-Value", text], 
                input=text, 
                text=True, 
                check=True
            )
        
        else:
            raise RuntimeError("Unsupported platform.")
    
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to write clipboard: {e}")


def main():
    parser = argparse.ArgumentParser(description="Unpaste: Strip formatting from clipboard text.")
    parser.add_argument(
        "--copy", 
        action="store_true", 
        help="Copy unformatted text back to clipboard"
    )
    parser.add_argument(
        "--stdin", 
        action="store_true", 
        help="Read from stdin instead of clipboard"
    )
    args = parser.parse_args()
    
    try:
        if args.stdin:
            text = sys.stdin.read().strip()
        else:
            text = get_clipboard()
        
        if args.copy:
            set_clipboard(text)
            print("Unformatted text copied to clipboard.")
        else:
            print(text)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()