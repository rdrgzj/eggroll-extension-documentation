import os
import subprocess
import sys
import time

from termcolor import colored


def print_game_title() -> None:
    """Prints the game's title in the terminal with ASCII art."""
    print(colored('''
    ███████╗░██████╗░░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░
    ██╔════╝██╔════╝░██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║░░░░░
    █████╗░░██║░░██╗░██║░░██╗░██████╔╝██║░░██║██║░░░░░██║░░░░░
    ██╔══╝░░██║░░╚██╗██║░░╚██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░
    ███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝███████╗███████╗
    ╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
''', 'green'))


def clear_screen() -> None:
    """Clears the terminal screen to give the effect of real-time updates,
    used for updating the game grid and other visual content that
    needs to clear the screen before displaying."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(clear_cmd, shell=True)


def degridder(grid: list[list[str]]) -> None:
    """Clears the terminal and displays the grid with a
    delay to simulate real-time movement."""
    time.sleep(0.15)
    clear_screen()
    display = ''
    for row in grid:
        display += ''.join(row) + '\n'
    print(display)


def get_level_files() -> list[str]:
    """Returns a list of level files located in the 'levels' directory.
    The level files should be named starting with "level", the level number,
    and ending with ".in".
    """
    return [
        f for f in os.listdir('levels')
        if f.startswith('level') and f.endswith('.in')
    ]
