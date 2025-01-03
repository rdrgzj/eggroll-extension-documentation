import os

from termcolor import colored

from gameplay import Game
from utility import clear_screen, print_game_title, get_level_files


def display_levels() -> None:
    """Clears the screen, retrieves available level files, 
    and prints them in a formatted list. If no levels are available, 
    the user is notified, and they are prompted to return to the main menu.
    """
    clear_screen()
    levels = get_level_files()
    if not levels:
        print(colored(
            'There are no levels that can be loaded from your current '
            'game folder.',
            'red'
        ))
        input(colored('Press ENTER to return to main menu.', 'green'))
        return

    print_game_title()
    print(colored('LEVELS:\n', 'green'))
    for i, level in enumerate(levels, 1):
        print(colored(f'({i}) {level}', 'yellow'))


def listed_levels() -> list[str]:
    """Calls `get_level_files()` and returns the list of 
    level files present in the 'levels' directory.
    """
    levels = get_level_files()
    return list(levels)


def get_level_choice(levels: list[str]) -> str | None:
    """Displays the list of available levels and prompts the 
    user to select one. It also allows the user to return to the main 
    menu by entering 0. If the user inputs an invalid choice, they are 
    prompted again.
    """
    while True:
        try:
            choice = int(input(colored(
                '\nChoose the level you want to play '
                '(or 0 to go back to main menu): ',
                'cyan'
            )))
        except ValueError:
            print(colored(
                f'Invalid choice. Please enter a NUMBER between 0 and '
                f'{len(levels)} only.',
                'red'
            ))
        else:
            if 1 <= choice <= len(levels):
                return levels[choice - 1]
            elif choice == 0:
                from menu import main_menu_action   # imported here to avoid circular imports
                main_menu_action()
            else:
                print(colored(
                    f'Invalid choice. Please enter a number between 0 and '
                    f'{len(levels)} only.',
                    'red'
                ))


def play_level() -> None:
    """This function displays the available levels and prompts the user 
    to select a level using `get_level_choice()`. If the level exists, 
    it starts the gameplay using the `Game` class. If the level file is 
    not found, an error is displayed to the user.
    """
    display_levels()
    
    levels = listed_levels()
    choice = get_level_choice(levels)

    if choice not in levels:
        print(colored(
            f'Error: The selected level {choice} does not exist.',
            'red'
        ))
        input(colored('Press ENTER to return to the main menu.', 'green'))
    else:
        try:
            level_file = os.path.join('levels', choice)  
            game = Game(level_file)  
            game.play() 
        except FileNotFoundError:
            print(colored(
                f'Error: The file {choice} does not exist. Please try again.',
                'red'
            ))
