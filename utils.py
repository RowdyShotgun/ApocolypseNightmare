"""
utils.py

Utility functions.
- clear_screen: Clears the console screen.
- print_slow: Prints text character by character for dramatic effect.
"""
import time
import os
import sys
import msvcrt
import subprocess

def clear_screen():
    """Clears the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, mode=None):
    print(text)

def run_git_command(cmd):
    """Run a git command and return its output as a string."""
    result = subprocess.run(["git"] + cmd.split(), capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()