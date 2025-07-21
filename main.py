"""
main.py
# by Mitchell Murphy
# A text adventure about a missile attack on a small town.
"""
from game_data import game_state, locations, endings
from utils import print_slow

inventory = set()

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
    print(f"Inventory: {', '.join(sorted(inventory)) if inventory else 'empty'}")


def hybrid_parser():
    loc = game_state["current_location"]
    data = locations[loc]
    exit_names = list(data["exits"].keys())
    action_names = list(data["interactions"].keys())
    total_choices = len(exit_names) + len(action_names) + 1
    user_input = input("\nType a number or a command: ").strip().lower()

    # Menu number input
    if user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= len(exit_names):
            game_state["current_location"] = data["exits"][exit_names[choice - 1]]
            return True
        elif len(exit_names) < choice <= len(exit_names) + len(action_names):
            action_idx = choice - len(exit_names) - 1
            action = action_names[action_idx]
            return handle_action(loc, action)
        elif choice == total_choices:
            print_slow("Thanks for playing!")
            return False
        else:
            print_slow("Invalid choice. Try again.")
            return True

    # String parser input
    # Try exits
    for exit_name, dest in data["exits"].items():
        if user_input == exit_name or user_input == f"go to {exit_name}" or user_input == f"move to {exit_name}":
            game_state["current_location"] = dest
            return True
    # Try actions
    for action in data["interactions"]:
        if user_input == action or user_input.startswith(action):
            return handle_action(loc, action)
    # Inventory and help
    if user_input == "inventory":
        print_slow(f"Inventory: {', '.join(sorted(inventory)) if inventory else 'empty'}")
        return True
    if user_input == "help":
        print_slow("Type a number, an exit name, an action, or 'inventory'.")
        return True
    if user_input == "exit":
        print_slow("Thanks for playing!")
        return False
    print_slow("I don't understand that command.")
    return True


def handle_action(loc, action):
    data = locations[loc]
    print_slow(data["interactions"][action])
    # Inventory and endings logic
    if loc == "bedroom" and action == "use computer":
        if "data" not in inventory:
            print_slow("You found important data about the missile!")
            inventory.add("data")
        else:
            print_slow("You already have the data.")
    if loc == "tech_store" and action == "get tech part":
        if "data" in inventory and "tech part" not in inventory:
            print_slow("You show your data and receive a tech part!")
            inventory.add("tech part")
        elif "tech part" in inventory:
            print_slow("You already have the tech part.")
        else:
            print_slow("You need data before you can get the tech part.")
    if loc == "military_base" and action == "use tech part":
        if "tech part" in inventory:
            game_state["ending"] = "missile_destroyed"
            return False
        else:
            print_slow("You need a tech part to do this!")
    # Minimal endings logic
    if loc == "bus_stop" and action == "wait for bus":
        game_state["ending"] = "escaped"
        return False
    if loc == "military_base" and action == "approach gate":
        game_state["ending"] = "caught"
        return False
    if loc == "bedroom" and action == "think":
        game_state.setdefault("think_count", 0)
        game_state["think_count"] += 1
        if game_state["think_count"] >= 3:
            game_state["ending"] = "waited"
            return False
        else:
            print_slow("You think and worry, but nothing changes...")
            return True
    if loc == "newspaper_club" and action == "rally friends":
        game_state["ending"] = "allies_saved"
        return False
    if loc == "neighbors_bunker" and action == "hide in bunker":
        game_state["ending"] = "bunker"
        return False
    return True


def game():
    print_slow("Welcome to Apocalypse Nightmare!")
    input("Press Enter to begin...")
    name = input("What is your name? (Press Enter for default) ").strip()
    if not name:
        name = "You"
    print_slow(f"Your name is set to: {name}")
    game_state["protagonist_name"] = name
    game_state["current_location"] = "bedroom"
    game_state["ending"] = None
    game_state["think_count"] = 0
    inventory.clear()

    while True:
        show_location()
        if not hybrid_parser():
            break
    if game_state["ending"]:
        print_slow("\n--- Ending ---")
        print_slow(endings[game_state["ending"]])

if __name__ == "__main__":
    game()
    