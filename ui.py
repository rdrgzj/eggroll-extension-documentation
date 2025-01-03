import os
from termcolor import colored
from gameplay import Game
from instructions import display_mechanics
from level_selection import play_level
from level_manager import LevelManager
from menu import get_menu_choice, display_main_menu
from utility import clear_screen

def main_menu(level_file: str):
    """Continuously displays the main menu, handles user input, and executes 
    the corresponding action for the selected option."""
    while True:
        display_main_menu()
        choice = get_menu_choice()

        if choice == 1:
            level_file = os.path.join('levels', 'level1.in')  
            game = Game(level_file)
            start_game(game)
        elif choice == 2:
            play_level()
        elif choice == 3:
            display_mechanics()
        else:
            print(colored('You are now going to exit the game. See you later!', 'red'))
            exit()

def start_game(game: Game):
    """Starts the gameplay loop."""
    game.play()
    display_end_game_menu(game)

def handle_special_input(direction_input: str, level_file: str):
    """Handles special input (Restart or Back to Main Menu)."""
    if 'X' in direction_input:
        print("Restarting the game...")
        restart_game(level_file)
        return True
    if 'Y' in direction_input:
        print("Returning to main menu...")
        main_menu(level_file)
        return True
    return False

def restart_game(level_file: str):
    """Restarts the current game."""
    level_manager = LevelManager()
    grid, total_moves = level_manager.load_level(level_file)  # Use the level file
    game = Game(level_file)
    game.play()

def display_end_game_menu(game: Game):
    """Displays the end-game menu and processes the player's choice."""
    print(colored(''' 
----------------------------------------------------------------------
| (N) Play Next Level | (X) Restart Game | (Any Key) Back to Main Menu |
----------------------------------------------------------------------
    ''', 'light_magenta'))

    choice = input(colored('Pick your next move: ', 'cyan')).upper()
    if choice == 'N':
        play_next_level(game)
    elif choice == 'X':
        restart_game(game.level_file)  # Pass the level file to restart
    else:
        main_menu(game.level_file)  # Go back to the main menu

def play_next_level(game: Game):
    """Transitions to the next level."""
    next_level = LevelManager.get_next_level(game.level_file)  # Use LevelManager for next level
    if next_level:
        game = Game(next_level)  # Create a new game instance for the next level
        game.play()  # Start the next level
    else:
        clear_screen()
        print(colored('There are no more available levels for you to play.', 'magenta'))
        input(colored('Press ENTER to return to main menu.', 'green'))
        main_menu(game.level_file)  # Go back to the main menu

if __name__ == "__main__":
    level_file = os.path.join('levels', 'level1.in')  # Example level file
    main_menu(level_file)  # Start the main menu
