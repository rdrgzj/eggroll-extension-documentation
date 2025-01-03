import os
import sys
import subprocess
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
    """Clears the terminal screen to simulate real-time grid updates."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(clear_cmd, shell=True)


def get_level_files() -> list[str]:
    """Returns a list of level files located in the 'levels' directory.

    The function looks for files that start with 'level' and end with 
    '.in' file extension.
    """
    return [f for f in os.listdir('levels') if f.startswith('level') and f.endswith('.in')]


def degridder(grid: list[list[str]]) -> None:
    """Clears the terminal and displays the grid with a delay to highlight changes.
    
    The function prints each row of the grid with a slight delay of 0.2 seconds 
    to make the update visually clear.
    """
    time.sleep(0.2)
    clear_screen()
    display = ''
    for row in grid:
        display += ''.join(row) + '\n'
    print(display)
