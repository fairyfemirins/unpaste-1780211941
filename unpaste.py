#!/usr/bin/env python3
import re
import sys

def unformat_text(text):
    """Strip HTML/XML tags from text."""
    return re.sub(r'<[^>]*>', '', text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 unpaste.py '<formatted_text>'")
        sys.exit(1)
    formatted = sys.argv[1]
    plaintext = unformat_text(formatted)
    print(plaintext)

if __name__ == "__main__":
    main()