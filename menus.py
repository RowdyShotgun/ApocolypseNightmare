# menus.py
from game_data import game_state, locations, characters # Import characters here as well for display
from utils import print_slow, clear_screen
import sys
# Import ALL game action functions from game_actions.py
# Make sure to import functions like handle_talk_parents_action etc., with the '_action' suffix
from game_actions import (
    advance_time, display_location,
    handle_vision_event, # This is only called once at the very start
    tell_people_path_init, leave_town_path_init,

    # Individual action handlers (now called with _action suffix for clarity)
    handle_talk_parents_action, handle_talk_alex_action, handle_talk_maya_action,
    handle_talk_ben_action, handle_talk_jake_action,
    handle_town_hall_interaction_action, handle_computer_use_action, handle_shout_warning,
    handle_seek_transport_action, handle_gather_supplies_action,
    handle_involve_friends_escape_action, handle_general_store_interaction_action,
    handle_steal_general_store_action, # For specific nested stealing choice
    handle_burger_hut_work_action, handle_go_to_class_action, handle_search_home_action,
    handle_bunker_access_action, handle_military_base_approach_action,
    handle_military_base_action, # Action for choices *inside* military base
    handle_laser_activation, # This one has its own internal input loop, but is called from here
    handle_escape_base_attempt,
    display_inventory, # Utility for displaying inventory
    handle_allies_escape_ending, handle_solo_escape_ending,
    handle_town_evacuated_ending, handle_missile_destroyed_ending,
    handle_time_up_ending, handle_jailed_ending, # Specific ending messages
    buy_tech_parts_action # New tech parts buying action
)

# --- Helper Functions for Menus ---
def display_menu(options):
    """Displays a numbered list of options and returns the chosen action function
    or a special value/tuple if sub-choices need to be passed."""
    while True: # Loop until valid input
        for idx, (desc, _) in enumerate(options, 1):
            print(f"{idx}. {desc}")
        choice_str = input("\nEnter your choice: ").strip()
        if choice_str.isdigit() and 1 <= int(choice_str) <= len(options):
            return options[int(choice_str) - 1][1] # Return the function/lambda directly
        else:
            print_slow("Invalid choice. Please enter the number corresponding to your action.")

def show_time_status():
    """Displays the current game time and phase."""
    print(f"\n[Time left: {game_state['time_remaining']}h | Phase: {game_state['current_day_phase'].title()}]")
    print("-" * 30) # Separator for clarity

def set_location(loc):
    """Changes the player's current location."""
    game_state["current_location"] = loc
    # No return to main_menu_loop here; it will naturally loop and call the next menu for the new location.

def exit_game():
    """Handles quitting the game."""
    print_slow("Are you sure you want to quit? (yes/no)")
    confirm = input("> ").strip().lower()
    if confirm == "yes":
        print_slow("Thanks for playing!")
        sys.exit(0)
    else:
        print_slow("Returning to the game.")

def display_status():
    """Displays comprehensive player status."""
    print_slow(f"\n--- Player Status ---")
    print_slow(f"- Current Location: {game_state['current_location'].replace('_', ' ').title()}")
    print_slow(f"- Time Remaining: {game_state['time_remaining']}h ({game_state['current_day_phase'].title()})")
    print_slow(f"- Knowledge: {game_state['knowledge']}")
    print_slow(f"- Tech Parts: {game_state['tech_parts']}")
    print_slow(f"- Cash: {game_state['cash']} unit(s)") # CHANGED: Display numerical cash
    print_slow(f"- Authority: {game_state['authority_of_town']}")
    print_slow(f"- Has Backpack: {'Yes' if 'backpack' in game_state['inventory'] else 'No'}")
    print_slow(f"- Has Car Keys: {'Yes' if game_state['has_car_keys'] else 'No'}")
    print_slow(f"- Car Gas: {game_state['car_gas']}%")
    print_slow(f"- Bunker Unlocked: {'Yes' if game_state['bunker_unlocked'] else 'No'}")
    print_slow("\n--- Friend Relationships ---")
    # Display character trust based on ranges or just raw numbers
    print_slow(f"- Alex (Skeptic): {game_state['trust_alex']} / 10")
    print_slow(f"- Maya (Optimist): {game_state['trust_maya']} / 10")
    print_slow(f"- Ben (Pragmatist): {game_state['trust_ben']} / 10")
    print_slow(f"- Jake (Bully): {game_state['trust_jake']} / 10")
    print("-" * 30)
    advance_time(0.1, silent=True) # Small time cost for checking status


# --- Location-Specific Menu Handlers ---
# Each handler displays its menu and dispatches to game_actions.py functions.

def handle_bedroom_menu():
    options = [
        ("Go to town", lambda: set_location("town_square")),
        ("Go to school", lambda: set_location("school_entrance")),
        ("Use computer", lambda: handle_computer_use_menu()),
        ("Talk to parents", lambda: handle_talk_parents_menu()),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("You are at home. You can go to town, go to school, use your computer, or talk to your parents.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_living_room_menu():
    options = [
        ("Talk to parents", lambda: handle_talk_parents_menu()),
        ("Go to bedroom", lambda: set_location("bedroom")),
        ("Go to front door", lambda: set_location("front_door")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Talk to your parents or move between rooms.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_front_door_menu():
    options = [
        ("Go to town (Town Square)", lambda: set_location("town_square")),
        ("Go to school (School Entrance)", lambda: set_location("school_entrance")),
        ("Go to bedroom", lambda: set_location("bedroom")),
        ("Go to living room", lambda: set_location("living_room")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Leave the house for school or town, or go back inside.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_town_square_menu():
    # Check for game-ending conditions based on accumulated state in Town Square
    if game_state["mayor_warned"] and game_state["mob_of_civilians"] and game_state["time_remaining"] > 0:
        handle_town_evacuated_ending()
        return
    options = [
        ("Warn people openly", lambda: handle_shout_warning()),
        ("Work at Burger Hut", lambda: set_location("burger_hut")),
        ("Go to front door (Home)", lambda: set_location("front_door")),
        ("Go to bus stop", lambda: set_location("bus_stop")),
        ("Go to town hall", lambda: set_location("town_hall")),
        ("Go to tech store", lambda: set_location("tech_store")),
        ("Go to military base", lambda: set_location("military_base")),
        ("Go to general store", lambda: set_location("general_store")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Warn people, work for cash, or move to other key locations.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_school_entrance_menu():
    options = [
        ("Go to class", lambda: handle_go_to_class_action()),
        ("Steal from school", lambda: handle_steal_school_action()),
        ("Go to newspaper club", lambda: set_location("newspaper_club")),
        ("Go home (front door)", lambda: set_location("front_door")),
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Attend class, steal, visit the newspaper club, or leave school.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_newspaper_club_menu():
    def handle_friends_submenu():
        options = [
            ("Talk to Alex", lambda: handle_talk_alex_menu()),
            ("Talk to Maya", lambda: handle_talk_maya_menu()),
            ("Talk to Ben", lambda: handle_talk_ben_menu()),
            ("Go back", lambda: None),
        ]
        action = display_menu(options)
        if action:
            action()
            handle_friends_submenu()  # Stay in friends submenu until 'Go back'
    options = [
        ("Talk to friends", handle_friends_submenu),
        ("Go to school entrance", lambda: set_location("school_entrance")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Chat with your friends or leave the club.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_general_store_menu():
    display_location()
    options = [
        ("Interact with Mr. Jenkins / Supplies", lambda: handle_general_store_interaction_menu()), # Sub-menu for store actions
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Shop for supplies or return to town.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_town_hall_menu():
    display_location()
    options = [
        ("Talk to secretary", lambda: handle_town_hall_interaction_menu()), # Sub-menu for secretary
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Try to get help from town officials or leave.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    if action: action()

def handle_bus_stop_menu():
    display_location()
    bus_ticket_cost = 1 # CHANGED: Bus ticket cost is 1 cash unit
    # Check for escape ending conditions at the bus stop
    if game_state["cash"] >= bus_ticket_cost and game_state["time_remaining"] > 0:
        if (game_state.get("has_shared_vision_with_friends", False) and
            game_state["trust_alex"] >= 4 and game_state["trust_maya"] >= 4 and game_state["trust_ben"] >= 4):
            game_state["cash"] -= bus_ticket_cost # Deduct cash for allies escape
            handle_allies_escape_ending()
        else:
            game_state["cash"] -= bus_ticket_cost # Deduct cash for solo escape
            handle_solo_escape_ending()
        return # Exit menu to trigger game end in main_menu_loop

    options = [
        (f"Wait for bus (Requires {bus_ticket_cost} Cash unit(s))", lambda: (print_slow(locations["bus_stop"]["interactions"]["wait for bus"]), advance_time(1))), # UPDATED DESC
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Wait for the bus to escape or return to town.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_tech_store_menu():
    options = [
        ("Buy tech parts (1 Cash unit required)", buy_tech_parts_action),
        ("Steal from tech store", lambda: handle_steal_tech_store_action()),
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Buy or steal tech parts, or return to town square.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()

def handle_military_base_menu():
    display_location()
    # Check for immediate missile destroyed ending if conditions met and player is at base
    if game_state["military_base_accessed"] and game_state["knowledge"] >= 7 and game_state["tech_parts"] >= 2 and game_state["time_remaining"] > 0:
        handle_missile_destroyed_ending() # Direct call to ending logic
        return # Exit menu to trigger game end in main_menu_loop

    options = [
        ("Approach gate (Sneak/Authority)", lambda: handle_military_base_approach_menu()), # Sub-menu for approach options
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Try to enter the military base or return to town.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()


def handle_outskirts_road_menu():
    display_location()
    options = [
        ("Search for car (Mr. Henderson's truck)", lambda: handle_seek_transport_menu()), # Sub-menu for transport search
        ("Go to town square", lambda: set_location("town_square")),
        ("Go to neighbor's bunker", lambda: set_location("neighbors_bunker")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Search for transport, check the bunker, or return to town.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    action()


def handle_neighbors_bunker_menu():
    display_location()
    # Check for escape ending from bunker
    if game_state["bunker_unlocked"] and game_state["inventory"].count("supplies") >= 3 and game_state["time_remaining"] > 0:
        if (game_state.get("has_shared_vision_with_friends", False) and
            game_state["trust_alex"] >= 4 and game_state["trust_maya"] >= 4 and game_state["trust_ben"] >= 4):
            handle_allies_escape_ending()
        else:
            handle_solo_escape_ending()
        return # Exit menu to trigger game end in main_menu_loop

    options = [
        ("Examine door", lambda: handle_bunker_access_action("examine door")),
        ("Knock on door", lambda: handle_bunker_access_action("knock")),
        ("Enter (if unlocked)", lambda: handle_bunker_access_action("enter")),
        ("Go to outskirts road", lambda: set_location("outskirts_road")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Try to get into the bunker or go back to the road.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    if action: action()


def handle_burger_hut_menu():
    display_location()
    options = [
        ("Work a shift", lambda: handle_burger_hut_work_action("yes")), # Pass 'yes' directly to action
        ("Go to town square", lambda: set_location("town_square")),
        ("Show inventory", lambda: display_inventory()),
        ("Show status", lambda: display_status()),
        ("Help", lambda: print_slow("Earn some cash or head back to the town square.")),
        ("Quit", lambda: exit_game()),
    ]
    action = display_menu(options)
    if action: action()


# --- Sub-Menus (interactions that have their own choices) ---

def handle_computer_use_menu():
    print_slow("You sit down at your computer. What do you want to search for?")
    options = [
        ("Search for 'nuclear threat' or 'impending doom'", lambda: handle_computer_use_action(1)),
        ("Look for unusual local news reports", lambda: handle_computer_use_action(2)),
        ("Check for survival guides or emergency bunkers", lambda: handle_computer_use_action(3)),
        ("Stop using the computer", lambda: None), # Choosing this will just return from this menu
    ]
    action_to_perform = display_menu(options)
    if action_to_perform:
        # Check if the action is "Stop using computer"
        if action_to_perform == options[3][1]: # Check if it's the lambda for stopping
            handle_computer_use_action(4) # Call action to deduct time for stopping
            return # Exit this sub-menu
        action_to_perform() # Execute the chosen action
    # If action was chosen AND it's not 'Stop using computer', re-display computer menu.
    # This keeps player in computer context until they explicitly stop.
    if game_state["current_location"] == "bedroom": # Only re-loop if still in bedroom (prevent infinite loop if loc changed)
        handle_computer_use_menu()


def handle_search_home_menu():
    print_slow("You search your house for anything useful.")
    options = [
        ("Search your desk in the bedroom", lambda: handle_search_home_action(1)),
        ("Look in the kitchen for supplies", lambda: handle_search_home_action(2)),
        ("Go back", lambda: handle_search_home_action(3)),
    ]
    action = display_menu(options)
    if action: action()


def handle_talk_parents_menu():
    # Only show initial dialogue options if not already warned
    if not game_state["parents_warned"]:
        print_slow("You consider telling them about your terrifying vision. It's a huge risk.")
        options = [
            ("Tell them about the nuclear missile vision", lambda: handle_talk_parents_action(1)),
            ("Keep silent and talk about something else", lambda: handle_talk_parents_action(2)),
        ]
    else: # If already warned, just a simple "go back" type option
        print_slow("Your parents are still going about their day. They sometimes glance at you with lingering worry.")
        print_slow("They haven't brought up your 'feverish' vision again.")
        options = [
            ("Talk about mundane things", lambda: handle_talk_parents_action(2)), # Re-use action for mundane talk
            ("Go back", lambda: None),
        ]
    action = display_menu(options)
    if action: action()


def handle_talk_alex_menu():
    # Pre-dialogue based on previous interaction status
    if not game_state.get("talked_to_alex_about_vision", False):
        print_slow("Alex glances up. 'What's up? Got a new scoop for the paper?'")
        options = [
            ("Tell him about the nuclear missile vision", lambda: handle_talk_alex_action(1)),
            ("Ask for his research help on a hypothetical disaster", lambda: handle_talk_alex_action(2)),
            ("Talk about newspaper club business", lambda: handle_talk_alex_action(3)),
        ]
    else:
        # Post-dialogue when vision has already been discussed
        if game_state["trust_alex"] >= 4:
            print_slow("Alex is still processing your warning. 'I'm checking the news, but nothing official yet. Still, I'm with you. What's our next move?'")
        elif game_state["trust_alex"] >= 2:
            print_slow("Alex seems a bit awkward. He quickly changes the subject, clearly unconvinced by your vision.")
        else:
            print_slow("Alex avoids eye contact and quickly finds an excuse to leave. He's clearly uncomfortable around you now.")
        options = [
            ("Go back", lambda: None),
        ]
    action = display_menu(options)
    if action: action()

def handle_talk_maya_menu():
    if not game_state.get("talked_to_maya_about_vision", False):
        print_slow("Maya smiles warmly. 'Hi! You look worried. Want to talk about it?'")
        options = [
            ("Confide in her about the vision", lambda: handle_talk_maya_action(1)),
            ("Talk about art or other light topics", lambda: handle_talk_maya_action(2)),
        ]
    else:
        if game_state["trust_maya"] >= 4:
            print_slow("Maya is anxious but supportive. 'I'm here for you, no matter what happens. We'll face this together.'")
        elif game_state["trust_maya"] >= 2:
            print_slow("Maya tries to offer comfort, but her voice is strained. She clearly thinks you're overwhelmed.")
        else:
            print_slow("Maya avoids eye contact and quickly finds an excuse to leave. She's clearly uncomfortable around you now.")
        options = [
            ("Go back", lambda: None),
        ]
    action = display_menu(options)
    if action: action()

def handle_talk_ben_menu():
    if not game_state.get("talked_to_ben_about_vision", False):
        print_slow("Ben glances up from his tinkering. 'Hey. Got a problem? Or something interesting for this old radio?'")
        options = [
            ("Tell him about the vision", lambda: handle_talk_ben_action(1)),
            ("Ask him for help with something practical (e.g., getting supplies)", lambda: handle_talk_ben_action(2)),
            ("Talk about his radio projects", lambda: handle_talk_ben_action(3)),
        ]
    else:
        if game_state["trust_ben"] >= 4:
            print_slow("Ben is focused on solutions. 'Okay, so what's the next practical step? We need a clear objective.'")
        elif game_state["trust_ben"] >= 2:
            print_slow("Ben gives you a sympathetic look but quickly shifts the conversation to something more concrete.")
        else:
            print_slow("Ben avoids eye contact and finds an excuse to fiddle with his radio, clearly uncomfortable with you.")
        options = [
            ("Go back", lambda: None),
        ]
    action = display_menu(options)
    if action: action()

def handle_talk_jake_menu():
    # Pre-dialogue based on previous interaction status or low trust
    if game_state["trust_jake"] < 3 and not game_state.get("talked_to_jake_about_vision", False):
        print_slow("Jake just glares at you. 'What do you want, loser?' He doesn't seem interested in talking.")
        options = [
            ("Go back", lambda: None),
        ]
    elif not game_state.get("talked_to_jake_about_vision", False):
        print_slow("Jake leans against the wall. 'What do you want, nerd?' There's a hint of boredom, not outright hostility.")
        options = [
            ("Tell him about the vision (carefully)", lambda: handle_talk_jake_action(1)),
            ("Ask for a favor (e.g., getting past someone, intimidating someone)", lambda: handle_talk_jake_action(2)),
            ("Challenge his authority (risky)", lambda: handle_talk_jake_action(3)),
        ]
    else:
        # Post-dialogue when vision has already been discussed
        if game_state["trust_jake"] >= 5:
            print_slow("Jake looks agitated. 'Still nothing concrete? We need to do something, pronto!'")
        else:
            print_slow("Jake avoids eye contact, mumbling something about being busy. He doesn't want to talk about your 'crazy' vision.")
        options = [
            ("Go back", lambda: None),
        ]
    action = display_menu(options)
    if action: action()


def handle_town_hall_interaction_menu():
    print_slow("You enter the Town Hall. The secretary looks up, unimpressed.")
    print_slow(f"Secretary Davies asks: 'Do you have an appointment?'")
    options = [
        ("Demand to see the Mayor and show proof", lambda: handle_town_hall_interaction_action(1)),
        ("Try to explain the urgency to the secretary", lambda: handle_town_hall_interaction_action(2)),
        ("Leave politely", lambda: handle_town_hall_interaction_action(3)),
    ]
    action = display_menu(options)
    if action: action()


def handle_general_store_interaction_menu():
    print_slow("You enter the General Store. Mr. Jenkins, the proprietor, is behind the counter.")
    options = [
        ("Try to buy supplies (e.g., food, gas)", lambda: handle_general_store_interaction_action(1)),
        ("Attempt to steal supplies", lambda: handle_steal_general_store_sub_menu()), # This leads to a sub-menu for stealing
        ("Talk to Mr. Jenkins about the situation", lambda: handle_general_store_interaction_action(3)),
        ("Leave the store", lambda: handle_general_store_interaction_action(4)),
    ]
    action = display_menu(options)
    if action: action()


def handle_steal_general_store_sub_menu():
    print_slow("You eye a small gas can. Attempt to steal it?")
    options = [
        ("Yes, try to steal.", lambda: handle_steal_general_store_action(1)),
        ("No, it's too risky.", lambda: handle_steal_general_store_action(2)),
    ]
    action = display_menu(options)
    if action: action()


def handle_seek_transport_menu():
    print_slow("You need a way out of town.")
    options = [
        ("Look for Mr. Henderson's truck (near Outskirts Road)", lambda: handle_seek_transport_action(1)),
        ("Go to the Bus Stop", lambda: handle_seek_transport_action(2)),
        ("Go back", lambda: handle_seek_transport_action(3)),
    ]
    action = display_menu(options)
    if action: action()


def handle_gather_supplies_menu():
    print_slow("You need supplies for survival or to fuel your escape.")
    options = [
        ("Go to the General Store (buy or steal)", lambda: handle_gather_supplies_action(1)),
        ("Go to Burger Hut (earn cash)", lambda: handle_gather_supplies_action(2)),
        ("Search for items at Home", lambda: handle_gather_supplies_action(3)),
        ("Go back", lambda: handle_gather_supplies_action(4)),
    ]
    action = display_menu(options)
    if action: action()


def handle_involve_friends_escape_menu():
    print_slow("You consider involving your friends in your escape plan.")
    options = [
        ("Go to the Newspaper Club (Talk to friends)", lambda: handle_involve_friends_escape_action(1)),
        ("Seek access to the Neighbor's Bunker (if you know about it)", lambda: handle_involve_friends_escape_action(2)),
        ("Go back", lambda: handle_involve_friends_escape_action(3)),
    ]
    action = display_menu(options)
    if action: action()


def handle_bunker_access_menu():
    print_slow("You approach the reinforced door of the neighbor's bunker.")
    options = [
        ("Examine door", lambda: handle_bunker_access_action("examine door")),
        ("Knock on door", lambda: handle_bunker_access_action("knock")),
        ("Enter (if unlocked)", lambda: handle_bunker_access_action("enter")),
        ("Go back", lambda: None), # Simple back to previous menu
    ]
    action = display_menu(options)
    if action: action()


def handle_military_base_approach_menu():
    print_slow("You stand before the **Military Base**, a formidable fortress. This is your chance to stop the missile.")
    options = [
        ("Attempt to Sneak In", lambda: handle_military_base_approach_action(1)),
        ("Try to Use Authority to Get In", lambda: handle_military_base_approach_action(2)),
        ("Go back to Town Square", lambda: handle_military_base_approach_action(3)),
    ]
    action = display_menu(options)
    if action: action()


def handle_military_base_actions_internal_menu():
    # This menu is displayed *after* successfully entering the military base
    print_slow("You're deep inside the military base. Your goal: the satellite laser control room.")
    print_slow("You know the missile launch is imminent. You need to act fast.")
    options = [
        ("Search for the Laser Control Room", lambda: handle_military_base_action(1)),
        ("Look for military personnel to convince", lambda: handle_military_base_action(2)),
        ("Attempt to use a computer terminal", lambda: handle_military_base_action(3)),
        ("Give up and try to escape the base", lambda: handle_military_base_action(4)),
    ]
    action = display_menu(options)
    if action: action()


# --- Main Menu Dispatcher ---
# This dictionary maps current_location to its corresponding menu handler function.
menu_handlers = {
    "bedroom": handle_bedroom_menu,
    "living_room": handle_living_room_menu,
    "front_door": handle_front_door_menu,
    "town_square": handle_town_square_menu,
    "school_entrance": handle_school_entrance_menu,
    "newspaper_club": handle_newspaper_club_menu,
    "general_store": handle_general_store_menu,
    "town_hall": handle_town_hall_menu,
    "bus_stop": handle_bus_stop_menu,
    "tech_store": handle_tech_store_menu,
    "military_base": handle_military_base_actions_internal_menu,
    "outskirts_road": handle_outskirts_road_menu,
    "neighbors_bunker": handle_neighbors_bunker_menu,
    "burger_hut": handle_burger_hut_menu,
}

def main_menu_loop():
    """The central game loop that dispatches to the appropriate menu handler."""
    while True: # Keep looping until an ending is achieved or game is quit
        # Check for game over condition at the beginning of each loop
        if game_state["ending_achieved"]:
            # Call the specific ending handlers from game_actions
            if game_state["ending_achieved"] == "Time's Up":
                handle_time_up_ending()
            elif game_state["ending_achieved"] == "Jailed":
                handle_jailed_ending()
            elif game_state["ending_achieved"] == "Allies Escape":
                handle_allies_escape_ending()
            elif game_state["ending_achieved"] == "Solo Escape":
                handle_solo_escape_ending()
            elif game_state["ending_achieved"] == "Town Evacuated":
                handle_town_evacuated_ending()
            elif game_state["ending_achieved"] == "Missile Destroyed":
                handle_missile_destroyed_ending()

            print_slow("\nThank you for playing!")
            sys.exit(0) # Terminate the game after displaying ending

        # Display location details (description, time status)
        display_location() # Only call once per menu loop

        # Remove the initial dilemma choice entirely; always start in home menu
        handler = menu_handlers.get(game_state["current_location"])
        if handler:
            handler() # Call the appropriate menu handler function
        else:
            print_slow(f"Error: No menu handler for location: {game_state['current_location']}. Exiting game.")
            sys.exit(0)