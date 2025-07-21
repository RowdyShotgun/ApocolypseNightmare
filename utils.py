# utils.py
import time
import os
import sys

def clear_screen():
    # Clears the console screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03, mode='fast'):
    # Prints text character by character for dramatic effect
    if mode == 'fast':
        delay = 0.01
    elif mode == 'slow':
        delay = 0.04
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Newline at the end