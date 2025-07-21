# utils.py
import time
import os
import sys
import msvcrt

def clear_screen():
    # Clears the console screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03, mode='fast'):
    # Prints text character by character for dramatic effect
    if mode == 'fast':
        delay = 0.01
    elif mode == 'slow':
        delay = 0.04
    i = 0
    length = len(text)
    while i < length:
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
        i += 1
        if msvcrt.kbhit():
            key = msvcrt.getwch()
            if key == '\r' or key == '\n':
                sys.stdout.write(text[i:])
                sys.stdout.flush()
                break
    print() # Newline at the end