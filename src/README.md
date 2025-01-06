<p align="center">
███████╗░██████╗░░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░<br>
██╔════╝██╔════╝░██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║░░░░░<br>
█████╗░░██║░░██╗░██║░░██╗░██████╔╝██║░░██║██║░░░░░██║░░░░░<br>
██╔══╝░░██║░░╚██╗██║░░╚██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░<br>
███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝███████╗███████╗<br>
╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
</p>

----------------------------------------------------------------------

### Eggroll is a fun game where you guide eggs 🥚 into nests 🪺 while avoiding obstacles like frying pans 🍳. It's a game of strategy and careful planning. Are you ready to guide your eggs to safety?

### For other devs, the documentation can be accessed through this link -> [Eggroll Extension Documentation](https://eggroll-extension-documentation.readthedocs.io/en/latest/index.html)

# HOW TO START THE GAME:

1. Ensure Python 3.8 or later is installed on your system. You can download it from [python.org](https://www.python.org/).

2. Install required python library. Run this command in your terminal/command prompt:  
   ```bash
   pip install termcolor

3. Verify the installation using:
   ```bash
   python -m pip show termcolor
   ```
   It should show details about termcolor library such as name and version.

4. Navigate to the directory where the game files are located. Use the cd command to change the directory. For example, if you're in `C:\Users\MyPC` type this into the terminal:
   ```bash
	cd Downloads\eggroll
   ```
   Ensure that the `eggroll` folder contains all the files from this repository.

5. Once you're in the correct directory, type the following command to 
   start the game.  
   For Windows:
   ```bash
  	 python menu.py
   ```
   For Linux:
   ```bash
  	 python3 menu.py
   ```
***This will run the game and you can start playing!***


# PLAYER MANUAL

## How To Play:
- **Move the Eggs**: Use these keys to move the eggs:
    - `L`  - Move left
    - `R`  - Move right
    - `F`  - Move forward
    - `B`  - Move backward

- **Goal**: Get all the eggs into the nests 🪺.

- **Avoid**: Don’t let the eggs land in the frying pans 🍳 or they’ll be scrambled!

## Scoring:
- +10 points for each egg you get into a nest 🪺.
- -5 points for every egg that lands in a frying pan 🍳.
- At the end of the game, you get bonus points for any moves you did not use (1 point per move).

## Menus:
- **Main Menu**:
    - `(1)` Start a new game
    - `(2)` Load a specific level
    - `(3)` Learn the game rules
    - `(4)` Quit the game

 - **During the Game**:
    - `(X)` Restart the current level
    - `(Y)` Return to the main menu

- **After Each Game**:
    - `(N)` Play the next level
    - `(X)` Restart the current level
    - `(Y)` Return to the main menu

## Tips:
- Think carefully before you move the eggs. They roll until they hit something!
- Use your moves wisely. You only have a limited number of moves to get the eggs into the nests.

## Game Over:
- The game ends when there are no eggs left in the grid or when you run out of moves.
- After completing a level, you can choose to play the next level, restart, or return to the main menu.
- If you finish a level but did not fill all the nests, you can only restart the current level or return to the main menu.

### Thank you for playing!

# CODE ORGANIZATION AND ALGORITHM 

## Code Organization
- The project is modular, with separate modules for each functionality.
- game.py contains three classes, which were kept together to avoid excessive circular dependencies, as they are interdependent.
- Classes are used to store stage levels, stage data, player state (scores, moves), and leaderboard data.
- Some modules, such as utility.py, menu.py, and level_selection.py, do not use classes because most functions are static and do not rely on specific attributes.

## Algorithm
- The game starts with the main menu, handled by menu.py, supported by modules like game.py, instructions.py, and level_selection.py, which correspond to each menu option.
- Option (1) "Start Game" loads level 1, progressing to the next level after each puzzle is solved. The level1.in file provides data stored in the Game class and processed for gameplay.
- Option (2) "Load Level" lets the player choose a level. This functionality is handled by level_selection.py, with level data stored in the levels/ directory.
- Option (3) "Game Mechanics" displays instructions in the terminal for players who want to review them during gameplay. This is handled by instructions.py.
- Option (4) "Quit" exits the game by calling the exit() function.
- During the game, the player can decide whether to restart the level, which reinitializes the stage data, or return to main menu.
- After each game, the leaderboard is displayed. If the player achieves a high score, they can input their name, and the score is saved in the corresponding leaderboard.txt file in the leaderboard/ directory.
- Lastly, the player can decide whether to play next game, restart the level, or return to main menu. 

### Here are the details about the files and folders in this repository:
#### Folders
- build/: Contains HTML, CSS, and JS files for Sphinx documentation.
- leaderboard/: Files related to managing and displaying the leaderboard.
- levels/: Stage or level data files for the game.
- source/: Contains .rst files for Sphinx documentation.
#### Source Code
- game.py: Manages the gameplay mechanics.
- instructions.py: Provides game instructions.
- leaderboard.py: Manages leaderboard functionality.
- level_manager.py: Manages level progression.
- level_selection.py: Handles level selection interface.
- menu.py: Controls the main menu. Main entry point of the game.
- movement.py: Handles movement mechanics.
- utility.py: Provides helper functions.
#### Stage Solutions
- sequences.txt: Stores sequences to solve game stages.
#### Test Files
- leveldummy.in: Test data for stage validation.
- test_movement.py: Unit tests for movement functionality.
- test_score.py: Unit tests for leaderboard and scoring.
- test_utils.py: Unit tests for utility functions.
- unit_tests.py: General unit tests for the project.

# BONUS FEATURES

1. **Main menu** - The player can access a main menu to start the game with the first level, view mechanics, load levels, or quit the game.
2. **Level selection** - The game allows the player to choose from multiple levels with varying difficulty. Each level has a unique grid layout.
3. **Game mechanics display** - The player can view the game mechanics and rules to better understand how to play and move eggs within the grid.
4. **Ability to restart game or return to main menu while playing** - The player has the option to restart the current level or return to the main menu at any point during gameplay.
5. **Ability to play next level after completing current level** - After finishing a level, the player can choose to proceed to the next level if available.
6. **Post-game options** - After completing a level, the player can choose to advance to the next level, restart the current level, or return to the main menu.
7. **Ability to exit game through main menu** - The player can exit the game through the main menu.
8. **Ability to input multiple movements** - Players can input a sequence of movements, and the game will validate and execute only the valid movements. (e.g 'LLLRRR' will move the eggs to the left 3 times and to the right 3 times, 'FFFTBBB' will move the eggs forward 3 times, ignore the 'T' input, and move the eggs backward 3 times)


## Contributions

### Eggroll (Original)

#### Jana Rodriguez
- Developed `game.py`
- Developed `menu.py`
- Developed `utility.py` (excluding the `degridder` function)
- Implemented the restart and return-to-main-menu functionalities during gameplay
- Enhanced the terminal interface by using `termcolor` and incorporating ASCII art
- Contributed to the README: player manual, code documentation, and bonus features

#### Leandro Asunan
- Developed `movement.py`
- Developed the scoring mechanics of the game
- Developed the `degridder()` function in `utility.py`
- Designed the levels and the solutions to it
- Wrote unit tests for the game logic
- Contributed to the README: description of the unit tests

### Eggroll (Extension)

#### Jana Rodriguez
- Organized the code into separate modules and refactored it into classes
- Developed `leaderboard.py`
- Added type hints to ensure it passed `mypy` checking
- Refactored modules to follow PEP 8 guidelines
- Managed the autogenerated documentation using Sphinx

#### Leandro Asunan
- Refactored the original unit tests
- Developed additional unit tests to test more cases

## References
- [PEP 8 Guidelines](https://peps.python.org/pep-0008/#introduction)
- [Type Hints Cheat Sheet](https://github.com/python/mypy/blob/master/docs/source/cheat_sheet_py3.rst)
- [Stack Overflow: Leaderboard Functionality Using .txt File](https://stackoverflow.com/questions/63872098/how-do-i-write-the-scores-of-my-game-into-the-leaderboard-txt-and-display-the-to)
