#!/usr/bin/env python3
"""
Mock Clipboard for Unpaste Testing

Usage:
  python3 mock_clipboard.py "<b>Formatted</b> text" | python3 unpaste.py
"""

import sys

# Simulate clipboard input
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("<b>Formatted</b> text")