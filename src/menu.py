import os

from termcolor import colored

from game import Game
from instructions import display_mechanics
from level_selection import play_level
from utility import clear_screen, print_game_title


def display_main_menu() -> None:
    """sets up the main menu by first clearing the screen, displaying the game
    title, and then showing the different menu options (Start Game, Load
    Level, Game Mechanics, Quit)
    """
    clear_screen()
    print_game_title()
    print(colored('MAIN MENU', 'magenta', attrs=['bold']))
    print(colored('\n(1) Start Game', 'light_blue'))
    print(colored('(2) Load Level', 'yellow'))
    print(colored('(3) Game Mechanics', 'green'))
    print(colored('(4) Quit', 'red'))


def get_menu_choice() -> int:
    """Asks the user to enter their choice for the main menu and
    ensures that the input is a valid number between 1 and 4. If the input is
    invalid (not a number or outside the allowed range), it will ask the user
    again.
    """
    while True:
        try:
            choice = int(input(colored(
                '\nEnter your choice: ', 'cyan',
                attrs=['blink']
                )))

            if 1 <= choice <= 4:
                return choice
            else:
                print_invalid_choice()

        except ValueError:
            print_invalid_choice()


def print_invalid_choice() -> None:
    """Displays the invalid choice error message."""
    print(colored('Invalid choice. Enter a number from 1 to 4 only.', 'red'))


def main_menu(level_file: str) -> None:
    """Manages the entire main menu flow. It will repeatedly display the menu,
    get the user’s choice, and trigger actions based on the choice. The
    options include starting a new game, loading a saved level, viewing
    the game mechanics, or quitting the game.
    """
    while True:
        display_main_menu()
        choice = get_menu_choice()

        if choice == 1:
            level_file = os.path.join('levels', 'level1.in')
            game = Game(level_file)
            game.play()
        elif choice == 2:
            play_level()
        elif choice == 3:
            display_mechanics()
        elif choice == 4:
            print(colored((
                '\nYou are now going to exit the game. '
                'See you later!'
            ), 'red'))

            exit()
        else:
            break


if __name__ == '__main__':
    start_game = os.path.join('levels', 'level1.in')
    main_menu(start_game)
