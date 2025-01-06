from termcolor import colored
from utility import clear_screen, print_game_title


def display_mechanics() -> None:
    """Clears the terminal, shows game title, and displays detailed
    game mechanics and instructions.

    Once the instructions are displayed, the user is prompted to press ENTER
    to return to the main menu.
    """
    clear_screen()
    print_game_title()
    print(colored("""
    HOW TO PLAY:
    Egg-citing Movement!
    ---------------------------------------------------------------
    🥚 Take control of rolling eggs! Guide them left (L), right (R),
    forward (F), or backward (B) across the grid.
    ---------------------------------------------------------------
    🧱🪺 The eggs don't stop until they hit something—so think
    carefully before each move!
    ---------------------------------------------------------------
    Goal!
    ---------------------------------------------------------------
    🪺 Put eggs in the nest! The ultimate goal is to roll each egg
    into a safe nest. But be quick, your moves are limited!
    ---------------------------------------------------------------
    🍳 Avoid the Frying Pan! If an egg lands in the frying pan...
    well, it's a scrambled mess and you'll lose points!
    ---------------------------------------------------------------
    Score!
    ---------------------------------------------------------------
    🥚 For every egg you successfully nest, you score +10 points.
    ---------------------------------------------------------------
    🍳 If an egg lands in the frying pan, you'll lose 5 points.
    ---------------------------------------------------------------
    LEVEL UP!
    ---------------------------------------------------------------
    🚀 Each level brings new challenges. More obstacles, tighter
    spaces, and even more frying pans! Can you solve each level
    before your moves run out?
    ---------------------------------------------------------------
    """, 'yellow'))
    input(colored(
        '                 PRESS ENTER TO RETURN TO MAIN MENU.',
        'green', attrs=['blink']
    ))
