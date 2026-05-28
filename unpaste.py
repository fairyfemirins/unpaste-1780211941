#!/usr/bin/env python3
import pyperclip
import click
import time

@click.group()
def cli():
    """Unpaste: Clipboard utility to strip formatting on paste."""
    pass

@cli.command()
@click.option('--interval', default=1.0, help='Polling interval in seconds.')
def watch(interval):
    """Monitor clipboard and strip formatting on paste."""
    last_value = ""
    click.echo("Unpaste is running. Press Ctrl+C to stop.")
    try:
        while True:
            current_value = pyperclip.paste()
            if current_value != last_value:
                last_value = current_value
                pyperclip.copy(current_value)  # Re-copy to strip formatting
            time.sleep(interval)
    except KeyboardInterrupt:
        click.echo("\nUnpaste stopped.")

if __name__ == "__main__":
    cli()