<p align="center">
███████╗░██████╗░░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░<br>
██╔════╝██╔════╝░██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║░░░░░<br>
█████╗░░██║░░██╗░██║░░██╗░██████╔╝██║░░██║██║░░░░░██║░░░░░<br>
██╔══╝░░██║░░╚██╗██║░░╚██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░<br>
███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝███████╗███████╗<br>
╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
</p>

<br><br>


<h1><strong>HOW TO START THE GAME:</strong></h1>

Note: This guide is for Windows OS. 

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
   start the game:
   ```bash
  	 python menu.py
   ```
***This will run the game and you can start playing!***

----------------------------------------------------------------------

<h1><strong>PLAYER MANUAL</strong></h1>

## Objective:
Guide the eggs 🥚 to the nests 🪹 before you run out of moves. Avoid obstacles like frying pans 🍳.

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

<h3><strong>Thank you for playing!</strong><h3>
  
----------------------------------------------------------------------
    
<p align="center">
  <h1><strong>BONUS FEATURES</strong></h1>
</p>

1. **Main menu** - The player can access a main menu to start the game with the first level, view mechanics, load levels, or quit the game.
2. **Level selection** - The game allows the player to choose from multiple levels with varying difficulty. Each level has a unique grid layout.
3. **Game mechanics display** - The player can view the game mechanics and rules to better understand how to play and move eggs within the grid.
4. **Ability to restart game or return to main menu while playing** - The player has the option to restart the current level or return to the main menu at any point during gameplay.
5. **Ability to play next level after completing current level** - After finishing a level, the player can choose to proceed to the next level if available.
6. **Post-game options** - After completing a level, the player can choose to advance to the next level, restart the current level, or return to the main menu.
7. **Ability to exit game through main menu** - The player can exit the game through the main menu.
8. **Ability to input multiple movements** - Players can input a sequence of movements, and the game will validate and execute only the valid movements. (e.g 'LLLRRR' will move the eggs to the left 3 times and to the right 3 times, 'FFFTBBB' will move the eggs forward 3 times, ignore the 'T' input, and move the eggs backward 3 times)

----------------------------------------------------------------------

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
- Designed the levels
- Wrote unit tests for the game logic
- Contributed to the README: description of the unit tests

---

### Eggroll Extension

#### Jana Rodriguez
- Organized the code into separate modules and refactored it into classes
- Developed `leaderboard.py`
- Added type hints to ensure it passed `mypy` checking
- Refactored modules to follow PEP 8 guidelines
- Managed the autogenerated documentation using Sphinx

#### Leandro Asunan
- Revised the original unit tests

---

## References
- [PEP 8 Guidelines](https://peps.python.org/pep-0008/#introduction)
- [Type Hints Cheat Sheet](https://github.com/python/mypy/blob/master/docs/source/cheat_sheet_py3.rst)
- [Stack Overflow: Leaderboard Functionality Using .txt File](https://stackoverflow.com/questions/63872098/how-do-i-write-the-scores-of-my-game-into-the-leaderboard-txt-and-display-the-to)
