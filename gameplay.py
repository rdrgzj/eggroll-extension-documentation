import time

from termcolor import colored

from level_manager import LevelManager
from movement import MovementManager
from utility import degridder

class Game:
    """Manages the gameplay loop."""
    
    def __init__(self, level_file: str):
        """Initializes the game with the given level file."""
        print(f"Initializing game with level file: {level_file}")
        self.level_file = level_file
        level_manager = LevelManager()
        self.grid: list[list[str]]     # type hint for self.grid is separated to avoid syntax error
        self.total_moves: int     # type hint for self.total_moves is separated to avoid syntax error
        self.grid, self.total_moves= level_manager.load_level(self.level_file)
        self.moves_left: int = self.total_moves
        self.previous_moves: str = ''
        self.initial_egg_count: int = self.count_eggs_and_nests()
        self.current_score: int = 0

    def count_eggs_and_nests(self) -> int:
        """Counts the total number of eggs and nests in the grid."""
        return sum(1 for row in self.grid for cell in row if cell in ['🥚', '🪺'])


    def calculate_score(self) -> int:
        """Calculates the current score based on nests collected and eggs removed."""
        current_egg_count = self.count_eggs_and_nests()
        nests_collected = sum(1 for row in self.grid for cell in row if cell == '🪺')
        return 10 * nests_collected - 5 * (self.initial_egg_count - current_egg_count)


    def display_game_state(self) -> None:
        """Displays the current state of the game."""
        degridder(self.grid)
        print(colored(f'Moves played: {self.previous_moves}', 'light_blue'))
        print(colored(f'Moves left: {self.moves_left}', 'yellow'))
        print(colored(f'Score: {self.current_score}', 'green'))
        print(colored('''
--------------------------------------------
| (X) Restart Game | (Y) Back to Main Menu |
--------------------------------------------
        ''', 'light_magenta'))


    def get_player_input(self) -> tuple[str, list[str]]:
        """Gets and validates player input."""
        direction_input = input(colored("Enter moves (L/R/F/B): ", 'cyan')).upper()
        valid_moves = [char for char in direction_input if char in MovementManager.dirs]
        invalid_moves = [char for char in direction_input if char not in MovementManager.dirs and char not in ['X', 'Y']]
        if invalid_moves:
            print(colored(f"Invalid input(s): {', '.join(invalid_moves)}", 'red'))
        return direction_input, valid_moves
    

    def play(self) -> None:
        """Main gameplay loop.

        This method runs the main loop of the game, prompting the player for moves and updating the game state.
        """
        self.display_game_state()

        while self.moves_left > 0:
            direction_input, valid_moves = self.get_player_input()
            if self.handle_special_input(direction_input):
                return

            for direction in valid_moves:
                if self.moves_left <= 0:
                    break
                MovementManager.move_eggs_in_direction(self.grid, direction)
                self.current_score = self.calculate_score()
                self.previous_moves += MovementManager.dirs[direction]
                self.moves_left -= 1
                self.display_game_state()

                if not any('🥚' in row for row in self.grid):
                    break

            if not any('🥚' in row for row in self.grid):
                break

        self.end_game_state()


    def end_game_state(self) -> None:
        """Handles end-of-level logic, including transitioning to the next level."""
        self.current_score += self.moves_left
        if self.moves_left > 0:
            print(colored(f'+{self.moves_left} points for remaining moves!', 'light_magenta'))
        time.sleep(2)

        degridder(self.grid)
        print(colored(f'Moves played: {self.previous_moves}', 'light_blue'))
        print(colored(f'Final Score: {self.current_score}', 'yellow'))
    
