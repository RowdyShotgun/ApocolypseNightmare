# main.py
import time
import sys

# Import game_state to set initial values if needed, and print_slow for intro
from game_data import game_state
from utils import print_slow

# Import the initial event handler and the main menu loop from their respective modules
from game_actions import handle_vision_event
from menus import main_menu_loop


def game():
    print_slow("Welcome to 'End of the World: A Text Adventure'!")
    print_slow("Press Enter to begin...")
    input()

    # The handle_vision_event function will set the starting location in game_state
    handle_vision_event()

    # Start the main game loop, which handles all menus and choices
    main_menu_loop()

if __name__ == "__main__":
    game()