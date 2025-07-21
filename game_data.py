"""
game_data.py

Holds all persistent game state, character definitions, and location/scene data for the text adventure game.
- game_state: Tracks player progress, inventory, and flags.
- characters: Contains all character descriptions and roles.
- locations: Contains all location descriptions, exits, and interactions.
"""

# game_data.py

# --- Game State Variables ---
game_state = {
    "protagonist_name": "You",
    "current_location": "bedroom",
    "ending": None
}

# --- Character Definitions (for dialogue and interaction) ---
characters = {
    "protagonist": {"name": "You", "description": "A weak but smart, brave but shortsighted teenager."}
}

# --- Locations and Scenes ---
locations = {
    "bedroom": {
        "description": (
            "Your small, cluttered bedroom in your West Virginia home. The morning light filters through the window. "
            "The terrifying vision still burns in your mind."
        ),
        "exits": {"living room": "living_room", "front door": "front_door"},
        "interactions": {
            "think": "The vision... a nuclear missile. Your city. Gone. You shudder. What do you do?",
            "use computer": "You use your computer to search for information about the missile."
        }
    },
    "living_room": {
        "description": (
            "The cozy, slightly worn living room. Your parents are here, engaged in their morning routine."
        ),
        "exits": {"bedroom": "bedroom", "front door": "front_door"},
        "interactions": {}
    },
    "front_door": {
        "description": (
            "The front door leading outside. The world beyond awaits, oblivious to the ticking clock."
        ),
        "exits": {"bedroom": "bedroom", "living room": "living_room", "town": "town_square", "school": "school_entrance"},
        "interactions": {}
    },
    "town_square": {
        "description": (
            "The heart of your small town. A few people are already out and about. The day feels like any other, "
            "but you know time is running out."
        ),
        "exits": {"front door": "front_door", "bus station": "bus_stop", "town hall": "town_hall",
                  "tech store": "tech_store", "military base": "military_base"},
        "interactions": {}
    },
    "school_entrance": {
        "description": (
            "The main entrance to your high school. The morning buzz of students is absent, replaced by an eerie quiet."
        ),
        "exits": {"home": "front_door", "town": "town_square", "newspaper club": "newspaper_club"},
        "interactions": {}
    },
    "newspaper_club": {
        "description": (
            "The dusty, cramped room where the school newspaper club meets. The air smells of old paper and ink. "
            "Your friends are here."
        ),
        "exits": {"school entrance": "school_entrance"},
        "interactions": {
            "rally friends": "You rally your friends and together you make a plan to escape as a group."
        }
    },
    "town_hall": {
        "description": (
            "The town hall, a stately but quiet building. Secretary Davies sits behind a formidable desk."
        ),
        "exits": {"town square": "town_square"},
        "interactions": {}
    },
    "bus_stop": {
        "description": (
            "A small, weathered shelter with a faded bus schedule. The road stretches out towards the next town."
        ),
        "exits": {"outskirts road": "outskirts_road"},
        "interactions": {
            "wait for bus": "You sit on the bench, time ticking by. Waiting feels like a luxury you don't have."
        }
    },
    "outskirts_road": {
        "description": (
            "You're on the main road leading out of town. The familiar houses slowly give way to dense forest and rolling hills."
        ),
        "exits": {"town": "town_square", "neighbors bunker": "neighbors_bunker"},
        "interactions": {}
    },
    "neighbors_bunker": {
        "description": (
            "A heavily reinforced steel door, almost invisible against the overgrown hillside. It looks impenetrable."
        ),
        "exits": {"outskirts road": "outskirts_road"},
        "interactions": {
            "hide in bunker": "You manage to get inside the bunker and seal the door behind you, safe from the chaos outside."
        }
    },
    "military_base": {
        "description": (
            "A high fence topped with barbed wire surrounds a sprawling complex. Guards patrol the perimeter. "
            "A chilling sense of finality hangs in the air."
        ),
        "exits": {"town square": "town_square"},
        "interactions": {
            "approach gate": "A guard stands at the main gate, rifle slung over his shoulder. He looks bored, but alert.",
            "use tech part": "You use the tech part to access the missile controls and destroy the missile!"
        }
    },
    "tech_store": {
        "description": (
            "A small, modern storefront with a few outdated computers on display. It's usually empty."
        ),
        "exits": {"town square": "town_square"},
        "interactions": {
            "get tech part": "You ask for a special tech part, showing your data as proof."
        }
    }
}

endings = {
    "escaped": "You managed to escape the town in time. You survive, but the world you knew is gone.",
    "caught": "You were caught by the authorities and failed to escape. The end comes swiftly.",
    "waited": "You waited too long. The disaster struck before you could act. The end.",
    "allies_saved": "You and your friends escape together, saving each other from disaster. You face the new world as a team.",
    "bunker": "You hide in the neighbor's bunker and survive the apocalypse, isolated but alive.",
    "missile_destroyed": "You use your technical skills and a special part to destroy the missile and save the world!",
}