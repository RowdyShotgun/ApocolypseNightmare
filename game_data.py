# game_data.py

# --- Game State Variables ---
game_state = {
    "current_location": "bedroom",
    "inventory": [],
    "knowledge": 0, # Player's accumulated knowledge
    "tech_parts": 0, # Player's accumulated tech parts
    "mob_of_civilians": False, # Whether a significant mob has been gathered
    "cash": 0, # CHANGED: Starting cash is 0 units
    "authority_of_town": 0, # Player's authority level in town
    "parents_warned": False, # Flag if parents have been told about the vision
    "has_car_keys": False, # Does the player have Mr. Henderson's truck keys
    "car_gas": 0, # Percentage of gas in Mr. Henderson's truck
    "bunker_unlocked": False, # Is the neighbor's bunker accessible
    "military_base_accessed": False, # Has player successfully accessed the base
    "missile_destroyed": False, # Has the missile been destroyed

    "trust_alex": 2,    # Skeptic: low trust, tends to need proof
    "trust_maya": 5,    # Optimist: high trust, more emotionally receptive
    "trust_ben": 3,     # Pragmatist: moderate trust, looks for practical solutions
    "trust_jake": 1,    # Bully: very low trust, difficult to convince/work with

    "has_shared_vision_with_friends": False, # Flag if vision has been shared with newspaper club friends

    "time_remaining": 16, # Hours until impact (e.g., roughly from morning to late evening/night)
    "current_day_phase": "morning", # morning, afternoon, evening, night
    "ending_achieved": None, # Stores the type of ending if reached
    # New flags for time-based narrative cues
    "news_warning_issued": False,
    "military_activity_noticed": False,
    "pending_action": None, # For multi-step or ambiguous input handling
    "mayor_warned": False, # For town evacuation ending
}

# --- Character Definitions (for dialogue and interaction) ---
characters = {
    "protagonist": {"name": "You", "description": "A weak but smart, brave but shortsighted teenager."},
    "alex": {"name": "Alex", "description": "Your friend from the newspaper club, always rational."},
    "maya": {"name": "Maya", "description": "Your friend from the newspaper club, always looking for the good."},
    "ben": {"name": "Ben", "description": "Your friend from the newspaper club, practical and resourceful."},
    "jake": {"name": "Jake", "description": "Your childhood friend, tough exterior, troubled home life."},
    "mr_henderson": {"name": "Mr. Henderson", "description": "An old recluse who owns a beat-up truck."},
    "mayor": {"name": "Mayor Thompson", "description": "The town's stern and busy mayor."},
    "secretary": {"name": "Secretary Davies", "description": "The mayor's unimpressed secretary."},
    "proprietor": {"name": "Mr. Jenkins", "description": "The gruff owner of the general store."},
    "parents": {"name": "Your Parents", "description": "Your loving but sometimes oblivious parents."}
}

# --- Locations and Scenes ---
locations = {
    "bedroom": {
        "description": "Your small, cluttered bedroom in your West Virginia home. The morning light filters through the window. The terrifying vision still burns in your mind.",
        "exits": {"living room": "living_room", "front door": "front_door"},
        "interactions": {
            "look window": "You see the familiar, peaceful street outside. It's hard to believe what you just saw. Normalcy feels like a fragile illusion.",
            "examine bed": "Your unmade bed. You just woke up from the nightmare that felt too real. Your heart still pounds.",
            "think": "The vision... a nuclear missile. Your city. Gone. You shudder. What do you do?",
            "use computer": "You sit at your desk, the screen glowing. What do you search for?"
        }
    },
    "living_room": {
        "description": "The cozy, slightly worn living room. Your parents are here, engaged in their morning routine.",
        "exits": {"bedroom": "bedroom", "front door": "front_door"},
        "interactions": {
            "talk parents": "Your parents are busy with breakfast. They'd never believe you, not without solid proof.",
            "look tv": "The local news reports on mundane town events. Nothing out of the ordinary, which only makes your vision feel more unsettling.",
            "examine photo": "A framed family photo. Everyone looks so happy, so oblivious to what you've seen. A pang of dread hits you."
        }
    },
    "front_door": {
        "description": "The front door leading outside. The world beyond awaits, oblivious to the ticking clock.",
        "exits": {"bedroom": "bedroom", "living room": "living_room", "town": "town_square", "school": "school_entrance"},
        "interactions": {
            "open door": "The fresh morning air hits you. The town is still quiet, bathed in an innocent light."
        }
    },
    "town_square": {
        "description": "The heart of your small town. A few people are already out and about. The day feels like any other, but you know time is running out.",
        "exits": {"front door": "front_door", "bus station": "bus_stop", "town hall": "town_hall",
                  "tech store": "tech_store", "military base": "military_base",
                  "general store": "general_store"},
        "interactions": {
            "talk people": "Most people are just going about their day. They look happy, oblivious. Trying to warn them might just make you look crazy.",
            "warn openly": "You open your mouth, but the words catch in your throat. Would anyone believe you? You'd just be a panicked voice in the wind.",
            "work at burger hut": "The Burger Hut sign beckons. You could earn some quick cash."
        }
    },
    "school_entrance": {
        "description": "The main entrance to your high school. The morning buzz of students is absent, replaced by an eerie quiet.",
        "exits": {"home": "front_door", "town": "town_square", "newspaper club": "newspaper_club"},
        "interactions": {
            "go to class": "You consider attending your morning classes.",
            "look around": "The empty halls stretch before you. School is almost unsettlingly quiet."
        }
    },
    "newspaper_club": {
        "description": "The dusty, cramped room where the school newspaper club meets. The air smells of old paper and ink. Your friends are here.",
        "exits": {"school entrance": "school_entrance"},
        "interactions": {}
    },
    "general_store": {
        "description": "The local general store, smelling faintly of dust and old candy. Mr. Jenkins, the proprietor, eyes you suspiciously.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "buy food": "You don't have any money.",
            "look shelves": "Mostly canned goods and some stale crackers. Basic survival gear is conspicuously absent."
        }
    },
    "town_hall": {
        "description": "The town hall, a stately but quiet building. Secretary Davies sits behind a formidable desk.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "talk secretary": "The secretary looks up, unimpressed. 'Do you have an appointment?'"
        }
    },
    "bus_stop": {
        "description": "A small, weathered shelter with a faded bus schedule. The road stretches out towards the next town.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "check schedule": "The next bus isn't for hours. Even then, it only goes to the next major city.",
            "wait for bus": "You sit on the bench, time ticking by. Waiting feels like a luxury you don't have."
        }
    },
    "pawn_shop": {
        "description": "A dimly lit shop filled with an eclectic mix of forgotten treasures and junk. A bell chimes as you enter.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "browse items": "You see old tools, dusty electronics, and some tarnished jewelry.",
            "sell item": "What do you want to sell?"
        }
    },
    "tech_store": {
        "description": "A small, modern storefront with a few outdated computers on display. It's usually empty.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "browse tech": "Old laptops, basic components, and a few dusty gaming consoles. Nothing cutting edge.",
            "buy tech parts": "You see a bin of miscellaneous electronic components. They might be useful for someone with technical skill."
        }
    },
    "outskirts_road": {
        "description": "You're on the main road leading out of town. The familiar houses slowly give way to dense forest and rolling hills.",
        "exits": {"town": "town_square", "neighbors bunker": "neighbors_bunker"}, # Changed front_door to town for consistency, added bunker
        "interactions": {
            "look around": "The road is quiet. You see no signs of other travelers. The sheer distance to safety becomes clear.",
            "search for car": "You scan the side of the road, but there are no abandoned vehicles. Mr. Henderson's truck comes to mind."
        }
    },
    "neighbors_bunker": {
        "description": "A heavily reinforced steel door, almost invisible against the overgrown hillside. It looks impenetrable.",
        "exits": {"outskirts road": "outskirts_road"},
        "interactions": {
            "examine door": "The door is clearly designed to withstand a lot. There's a keypad, but you don't know the code.",
            "knock": "You knock heavily, but only silence answers. No one seems to be home."
        }
    },
    "burger_hut": { # NEW LOCATION for working
        "description": "The greasy smell of frying food assaults your senses. A few bored-looking customers sit at tables.",
        "exits": {"town square": "town_square"},
        "interactions": {
            "work shift": "You put on the uniform and start flipping burgers. The hours crawl by."
        }
    },
    "military_base": {
        "description": "A high fence topped with barbed wire surrounds a sprawling complex. Guards patrol the perimeter. A chilling sense of finality hangs in the air.",
        "exits": {"town square": "town_square"}, # Direct exit back to town
        "interactions": {
            "examine fence": "The fence is formidable. Breaking in would be incredibly difficult and dangerous.",
            "approach gate": "A guard stands at the main gate, rifle slung over his shoulder. He looks bored, but alert."
        }
    }
}