import os

from termcolor import colored

from utility import clear_screen, print_game_title


def display_main_menu() -> None:
    """Clears the screen, displays the game title, and prints the available 
    main menu options in color-coded format.
    """
    clear_screen()
    print_game_title()
    print(colored('MAIN MENU', 'magenta', attrs=['bold']))
    print(colored('\n(1) Start Game', 'light_blue'))
    print(colored('(2) Load Level', 'yellow'))
    print(colored('(3) Game Mechanics', 'green'))
    print(colored('(4) Quit', 'red'))


def get_menu_choice() -> int | None:
    """Get user input for main menu selection.
    
    It prompts the user to select an option from the main menu. Ensures 
    the input is a valid number (1-4). If invalid, it displays an error message.
    """
    while True:
        try:
            choice = int(input(colored('\nEnter your choice: ', 'cyan')))
            
            if choice in [1, 2, 3, 4]:
                return choice
            
            print(colored(
                'Invalid choice. Enter a number from 1 to 4 only.',
                'red'
            ))
            return None

        except ValueError:
            print(colored(
                'Invalid choice. Please enter a NUMBER from 1 to 4 only.',
                'red'
            ))
            return None
    
