"""
utils.py

Utility functions for the text adventure game.
- clear_screen: Clears the console screen.
- print_slow: Prints text character by character for dramatic effect.
"""
import time
import os
import sys
import msvcrt

def clear_screen():
    """Clears the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, mode=None):
    print(text)