"""
main.py

Entry point for the text adventure game.
- Greets the player and prompts for their name.
- Sets up the initial game state and starts the main menu loop.
- Handles game restart logic.
"""
# main.py
# Import game_state to set initial values if needed, and print_slow for intro
from game_data import game_state, locations, endings
from utils import print_slow
# Removed: from game_actions import handle_vision_event
# Removed: from menus import main_menu_loop


def show_location():
    loc = game_state["current_location"]
    data = locations[loc]
    print_slow(f"\nLocation: {loc.replace('_', ' ').title()}")
    print_slow(data["description"])
    print("Exits:")
    for i, exit_name in enumerate(data["exits"], 1):
        print(f"{i}. {exit_name}")
    exit_count = len(data["exits"])
    print("Actions:")
    for j, action in enumerate(data["interactions"], 1):
        print(f"{exit_count + j}. {action}")
    print(f"{exit_count + len(data['interactions']) + 1}. Exit Game")


def choose_action():
    loc = game_state["current_location"]
    data = locations[loc]
    exit_names = list(data["exits"].keys())
    action_names = list(data["interactions"].keys())
    total_choices = len(exit_names) + len(action_names) + 1
    print("\nChoose a number:")
    choice = input("> ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= total_choices):
        print_slow("Invalid choice. Try again.")
        return True
    choice = int(choice)
    if 1 <= choice <= len(exit_names):
        game_state["current_location"] = data["exits"][exit_names[choice - 1]]
        return True
    elif len(exit_names) < choice <= len(exit_names) + len(action_names):
        action_idx = choice - len(exit_names) - 1
        action = action_names[action_idx]
        print_slow(data["interactions"][action])
        # Minimal endings logic
        if loc == "bus_stop" and action == "wait for bus":
            game_state["ending"] = "escaped"
            return False
        if loc == "military_base" and action == "approach gate":
            game_state["ending"] = "caught"
            return False
        if loc == "bedroom" and action == "think":
            game_state["ending"] = "waited"
            return False
        return True
    else:
        print_slow("Thanks for playing!")
        return False


def game():
    print_slow("Welcome to 'End of the World: A Text Adventure'!")
    input("Press Enter to begin...")
    name = input("What is your name? (Press Enter for default) ").strip()
    if not name:
        name = "You"
    print_slow(f"Your name is set to: {name}")
    game_state["protagonist_name"] = name
    game_state["current_location"] = "bedroom"
    game_state["ending"] = None

    while True:
        show_location()
        if not choose_action():
            break
    if game_state["ending"]:
        print_slow("\n--- Ending ---")
        print_slow(endings[game_state["ending"]])

if __name__ == "__main__":
    game()
    