#!/usr/bin/env python3
"""
unpaste: Autonomous Clipboard Utility

Features:
- Monitors clipboard for changes (text only).
- Applies regex filters to auto-format content (e.g., URLs to markdown links).
- Logs history to ~/.unpaste/history.json.
- Cross-platform (Linux/macOS/Windows).

Usage:
  python3 unpaste.py --rules "rules.yaml" --daemon
"""

import os
import re
import json
import time
import argparse
import pyperclip
from pathlib import Path
from typing import Dict, List, Optional
# Config
HISTORY_FILE = os.path.expanduser("~/.unpaste/history.json")
DEFAULT_RULES = {
    "markdown_links": {
        "pattern": r"(https?://[^\s]+)",
        "replacement": r"[\1](\1)",
    },
    "code_blocks": {
        "pattern": r"```([^`]+)```",
        "replacement": r"```\1```",
    },
}

class ClipboardMonitor:
    def __init__(self, rules: Dict[str, Dict[str, str]]):
        self.rules = rules
        self.last_content = ""
        self.history = self._load_history()
        self.HISTORY_FILE = os.path.expanduser("~/.unpaste/history.json")
        os.makedirs(os.path.dirname(self.HISTORY_FILE), exist_ok=True)

    def _load_history(self) -> List[Dict[str, str]]:
        """Load clipboard history from file."""
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_history(self) -> None:
        """Save clipboard history to file."""
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.history, f, indent=2)

    def _apply_rules(self, text: str) -> str:
        """Apply regex rules to clipboard content."""
        for rule in self.rules.values():
            text = re.sub(rule["pattern"], rule["replacement"], text)
        return text

    def check_clipboard(self) -> None:
        """Check clipboard for changes and process content."""
        current_content = pyperclip.paste()
        if current_content != self.last_content and current_content.strip():
            processed_content = self._apply_rules(current_content)
            if processed_content != current_content:
                pyperclip.copy(processed_content)
            self.history.append({
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "original": current_content,
                "processed": processed_content,
            })
            self._save_history()
            self.last_content = processed_content

    def run_daemon(self) -> None:
        """Run monitor in daemon mode (headless)."""
        print("unpaste: Monitoring clipboard (Press Ctrl+C to exit)...")
        try:
            while True:
                self.check_clipboard()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nunpaste: Exiting...")


def load_rules(rules_file: Optional[str]) -> Dict[str, Dict[str, str]]:
    """Load regex rules from YAML file."""
    if not rules_file:
        return DEFAULT_RULES
    try:
        import yaml
        with open(rules_file, "r") as f:
            return yaml.safe_load(f)
    except (ImportError, FileNotFoundError):
        print(f"Warning: Rules file {rules_file} not found. Using defaults.")
        return DEFAULT_RULES


def main():
    parser = argparse.ArgumentParser(description="unpaste: Autonomous Clipboard Utility")
    parser.add_argument("--rules", type=str, help="Path to YAML rules file")
    parser.add_argument("--daemon", action="store_true", help="Run in daemon mode")
    args = parser.parse_args()

    rules = load_rules(args.rules)
    monitor = ClipboardMonitor(rules)

    if args.daemon:
        monitor.run_daemon()
    else:
        monitor.check_clipboard()


if __name__ == "__main__":
    main()