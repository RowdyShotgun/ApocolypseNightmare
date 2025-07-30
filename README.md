# 🌍 Apocalypse Nightmare: A Text Adventure Game

A thrilling text-based adventure game where you must race against time to prevent a nuclear disaster. Experience a rich narrative with multiple endings, strategic decision-making, and immersive storytelling.

## 🎮 Game Overview

You wake up from a terrifying vision of a nuclear missile heading toward your city. With only 16 hours until impact, you must gather allies, collect resources, and find a way to prevent the apocalypse. Will you work alone or try to save others? The choice is yours.

## ✨ Features

- **Multiple Endings**: Different outcomes based on your choices and resources
- **Rich Character System**: Build relationships with friends (Alex, Maya, Ben, Jake)
- **Resource Management**: Collect supplies, tech parts, and cash
- **Time Pressure**: 16-hour countdown with day phases (morning, afternoon, evening, night)
- **Strategic Choices**: Military base infiltration, bunker escape, town evacuation
- **Beautiful UI**: Colored text, formatted boxes, and professional presentation
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/RowdyShotgun/Apocalypse-Nightmare-Final.git
   cd Apocalypse-Nightmare-Final
   ```

2. Install required dependencies:
   ```bash
   pip install colorama
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Starting the Game
1. Run `python main.py`
2. Enter your character's name (or press Enter for default)
3. Experience the opening vision sequence
4. Begin your journey to prevent the apocalypse

### Game Controls
- **Numbered Choices**: Enter the number corresponding to your choice
- **Navigation**: Move between locations using menu options
- **Inventory**: Check your items and status regularly
- **Time Management**: Every action takes time - use it wisely

### Key Locations
- **🏠 Home**: Bedroom, living room, front door
- **🏙️ Town**: Town square, general store, tech store, pawn shop
- **🏫 School**: School entrance, newspaper club
- **🏰 Special**: Military base, neighbor's bunker, burger hut, bus stop

### Important Resources
- **💰 Cash**: Earn by working at Burger Hut, sell stolen items
- **🔧 Tech Parts**: Buy from tech store, steal from school/tech store
- **📦 Supplies**: Find in kitchen, general store, bunker
- **🧠 Knowledge**: Gain through classes and research
- **🎒 Backpack**: Required for certain actions

## 🏆 Multiple Endings

### Possible Outcomes
1. **Missile Destroyed**: Infiltrate military base and activate satellite laser
2. **Bunker Escape**: Gather supplies and escape to neighbor's bunker
3. **Town Evacuated**: Convince mayor and evacuate the town
4. **Allies Escape**: Save friends and family together
5. **Solo Escape**: Escape alone on the last bus or bunker
6. **Time's Up**: Fail to prevent the missile impact
7. **Jailed**: Get arrested for suspicious behavior

### Ending Requirements
- **Missile Destroyed**: High knowledge (5+), tech parts (2+), military base access
- **Bunker Escape**: 3+ supplies, bunker unlocked
- **Town Evacuated**: High authority (5+), mayor convinced
- **Allies Escape**: High trust with friends, successful evacuation

## 🎨 Game Features

### Character Relationships
- **Alex (Skeptic)**: Requires proof and logical arguments
- **Maya (Optimist)**: Emotionally receptive, easier to convince
- **Ben (Pragmatist)**: Looks for practical solutions
- **Jake (Bully)**: Very low trust, difficult to work with

### Time System
- **16 Hours**: Total time until missile impact
- **Day Phases**: Morning → Afternoon → Evening → Night
- **Time Costs**: Different actions take different amounts of time
- **Urgency**: Time pressure affects available options

### Inventory System
- **Items**: Backpack, supplies, tech parts, stolen items
- **Status Tracking**: Cash, knowledge, authority, trust levels
- **Selling**: Pawn shop accepts stolen items and gas cans

## 🛠️ Technical Details

### File Structure
```
Apocalypse-Nightmare-Final/
├── main.py              # Game entry point
├── game_data.py         # Game state, constants, validation
├── game_actions.py      # Core game logic and actions
├── menus.py            # Menu system and navigation
├── utils.py            # Utility functions, UI, input handling
└── README.md           # This file
```

### Key Technologies
- **Python 3.7+**: Core programming language
- **Colorama**: Cross-platform colored terminal output
- **Unicode Box Drawing**: Professional UI elements
- **State Management**: Centralized game state tracking

### Cross-Platform Support
- **Windows**: Full support with msvcrt input handling
- **macOS/Linux**: Full support with tty/termios input handling
- **Fallbacks**: Generic input handling for other systems

## 🎮 Gameplay Tips

### Strategy
1. **Start Early**: Don't waste time - every hour counts
2. **Build Relationships**: High trust with friends opens new options
3. **Gather Resources**: Tech parts and supplies are crucial
4. **Choose Your Path**: Focus on one ending strategy
5. **Manage Time**: Balance exploration with time pressure

### Pro Tips
- **Backpack First**: Get the backpack early for better stealing success
- **Tech Parts**: Essential for military base access
- **Supplies**: Required for bunker escape ending
- **Authority**: Build through successful warnings and actions
- **Knowledge**: Gain through classes and computer research

## 🤝 Contributing

This is a complete game, but if you'd like to contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Story & Design**: Original narrative and game mechanics
- **Python Community**: For excellent libraries and tools
- **Text Adventure Enthusiasts**: For inspiration and feedback

---

**Ready to save the world? Start your adventure now!** 🚀

Run `python main.py` to begin your journey to prevent the apocalypse. 