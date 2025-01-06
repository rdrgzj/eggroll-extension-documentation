import os
import time

from termcolor import colored

from leaderboard import Leaderboard
from level_manager import LevelManager
from movement import MovementManager
from utility import degridder


class Level:
    """The Level class initializes the level based on a provided file, counts
    the eggs and nests, calculates the score, and checks for remaining eggs
    in the grid.
    """

    def __init__(self, level_file: str):
        """Initializes the level based on the level file.

        Uses the LevelManager class to load the grid and total moves, then
        counts the eggs and nests in the grid.
        """
        self.file = level_file
        lvl_mgr = LevelManager()
        self.grid, self.total_moves = lvl_mgr.load_level(self.file)
        self.eggs = self.count_eggs_and_nests()

    def count_eggs_and_nests(self) -> int:
        """Iterates through the grid to count the occurrences of eggs ('🥚')
        and nests ('🪺').
        """
        return sum(
            1
            for row in self.grid
            for cell in row
            if cell in ['🥚', '🪺']
        )

    def calc_score(self) -> int:
        """Calculates the current score based on nests collected and eggs
        removed.

        It compares the initial count of eggs and nests with the current grid
        state to compute the score.
        """
        curr_eggs = self.count_eggs_and_nests()
        nests = sum(1 for row in self.grid for cell in row if cell == '🪺')
        return 10 * nests - 5 * (self.eggs - curr_eggs)

    def has_eggs(self) -> bool:
        """Iterates through the grid to check if any row contains 
        an egg ('🥚').
        """
        return any('🥚' in row for row in self.grid)


class Player:
    """The Player class tracks the player's remaining moves, previous moves,
    and score. It also updates and finalizes the score during the game.
    """

    def __init__(self, total_moves: int, eggs: int):
        """Sets the total number of moves, initializes score, previous moves,
        and the number of eggs collected.
        """
        self.moves_left: int = total_moves
        self.prev_moves: str = ''
        self.score: int = 0
        self.eggs = eggs

    def update_score(self, level: Level) -> None:
        """Updates the player's score based on the current grid state.

        Uses the Level class to calculate the current score and assigns it
        to the player's score attribute.
        """
        self.score = level.calc_score()  
        # The Level class is called here because this function relies
        # on the level_file that was already initialized in the Level
        # class. Mypy requires positional argument if we initialize
        # the class in the attributes of Player class.

    def decrement_moves(self) -> None:
        """Decrease the moves_left attribute by 1, used after
        each valid move.
        """
        self.moves_left -= 1

    def finalize_score(self) -> None:
        """Finalizes the player's score at the end of the game.

        Adds remaining moves as bonus points and prints the bonus if moves
        are left.
        """
        self.score += self.moves_left
        if self.moves_left > 0:
            print(colored(f'\n+{self.moves_left} points for remaining moves!',
                          'light_magenta'))


class Game:
    """Handles the entire gameplay flow, including level setup, player input, 
    movement and score mechanics, and game completion. It also manages 
    transitions like restarting the game or returning to the main menu.
    """

    def __init__(self, level_file: str):
        """Initializes the game with the given level file.

        Sets up the `Level`, `Player`, `MovementManager`, and `Leaderboard`
        classes. It also extracts the stage level number from the filename
        (e.g., 1 from level1.in).
        """
        self.level = Level(level_file)
        self.lvl_mgr = LevelManager()
        self.player = Player(
            self.level.total_moves, self.level.eggs
        )
        self.move_mgr = MovementManager(self.level.grid)
        self.stage = level_file.strip(r'levels\level.in')
        self.leaderboard = Leaderboard(int(self.stage))

    def play(self) -> None:
        """Main gameplay loop.

        Displays the current game state and processes player input until
        all moves are used or there are no eggs left in the grid. Ends
        the game and checks for high score eligibility.
        """
        self.display_game_state()

        while self.player.moves_left > 0:
            dir_input, valid_moves = self.get_player_input()
            if self.handle_special_input(dir_input):
                return

            self.process_valid_moves(valid_moves)

            if not self.level.has_eggs():
                self.player.finalize_score()
                time.sleep(2)
                break
        
        if self.is_high_scorer():
            self.high_scorer()

        self.end_game_state()

    def get_player_input(self) -> tuple[str, list[str]]:
        """Asks the user for input, validates it against valid directions
        ('L', 'R', 'F', 'B'), and returns both the raw input and the list of
        valid moves. This method utilizes the `MovementManager.dirs` for
        valid directions.
        """
        dir_input = input(colored("\nEnter moves (L/R/F/B): ", 'cyan', attrs=['blink'])).upper()
        valid_moves = [
            char for char in dir_input if char in self.move_mgr.dirs
        ]
        invalid_moves = [
            char
            for char in dir_input
            if char not in self.move_mgr.dirs and char not in ['X', 'Y']
        ]
        if invalid_moves:
            print(
                colored(f"Invalid input(s): {', '.join(invalid_moves)}", 'red')
            )
        return dir_input, valid_moves

    def handle_special_input(self, dir_input: str) -> bool:
        """Checks if the input contains 'X' (restart) or 'Y' (main menu),
        and returns True to indicate a special action. Calls `restart_game`
        and `return_to_main_menu` as needed.
        """
        if 'X' in dir_input:
            self.restart_game()
            return True
        elif 'Y' in dir_input:
            self.return_to_main_menu()
            return True
        return False

    def process_valid_moves(self, valid_moves: list[str]) -> None:
        """Handles the actual movement of eggs.

        For each valid move in the input, it moves the eggs according
        to the direction, updates the score using `Player.update_score`,
        and decreases the number of moves left.
        Calls `MovementManager.move_until_blocked` to perform the actual move.
        Displays the updated game state after each move.
        """
        for direction in valid_moves:
            if self.player.moves_left <= 0:
                break
            self.move_mgr.move_until_blocked(direction)
            self.player.update_score(self.level)
            self.player.prev_moves += MovementManager.dirs[direction]
            self.player.decrement_moves()
            self.display_game_state()

    def display_game_state(self) -> None:
        """Displays the current state of the game.

        Calls the `degridder` function from the `utility` module to render the
        grid. Displays the current level, number of moves played, remaining
        moves, and score. Also shows options for special inputs like
        restarting or returning to the main menu.
        """
        degridder(self.level.grid)
        print(
            colored('=====', 'light_magenta') +
            colored(f' LEVEL {self.stage} ', 'light_green') +
            colored('=====\n', 'light_magenta')
        )
        print(colored(f'Moves played: {self.player.prev_moves}', 'light_blue'))
        print(colored(f'Moves left: {self.player.moves_left}', 'yellow'))
        print(colored(f'Score: {self.player.score}\n', 'green'))
        print(colored('=' * 19, 'light_magenta'))
        print('')
        print(colored('-' * 36, 'light_magenta'))
        print(
            colored('|', 'light_magenta') + 
            colored(' (X) Restart Game ', 'light_green') + 
            colored('|', 'light_magenta') + 
            colored(' (Y) Main Menu ', 'light_green') + 
            colored('|', 'light_magenta')
        )
        print(colored('-' * 36, 'light_magenta'))

    def restart_game(self) -> None:
        """Resets the level, player, and movement manager, then 
        restarts the gameplay loop.
        """
        print(colored('\nRestarting the game...', 'light_magenta'))
        time.sleep(0.5)
        self.level = Level(self.level.file)
        self.player = Player(self.level.total_moves, self.level.eggs)
        self.move_mgr = MovementManager(self.level.grid)
        self.play()

    def return_to_main_menu(self) -> None:
        """Handles the transition to the main menu, importing it only when
        needed to avoid circular dependencies.
        """
        print(colored('\nGoing back to the main menu...', 'light_magenta'))
        time.sleep(0.5)
        from menu import main_menu    # to avoid circular imports
        main_menu('level1.in')

    def is_high_scorer(self) -> bool:
        """Checks if the player beats a high score in the leaderboard.

        Loads the leaderboard scores from `Leaderboard.load_scores` and
        compares the player's score to the current top scores.
        """
        self.leaderboard.load_scores()
        if not self.leaderboard.scores or len(self.leaderboard.scores) < 5:
            if self.player.score > 0:
                return True
        return self.player.score > self.leaderboard.scores[-1][1]

    def high_scorer(self) -> None:
        """Handles high score logic.

        If the player has achieved a high score, asks for their name and
        updates the leaderboard with the new score.
        """
        self.leaderboard.load_scores()
        print(
            colored(f'\nCongratulations! You got a high score.',
                    'green'
            )
        )
        name = input(colored('Enter your name: ', 'cyan', attrs=['blink']))
        self.leaderboard.update_leaderboard(name, self.player.score)
        self.leaderboard.store_scores()

    def end_game_state(self) -> None:
        """Displays the final game state.

        Shows the current grid, moves played, final score, and the leaderboard
        before transitioning to the end game menu.
        """
        degridder(self.level.grid)
        print(
            colored('=====', 'light_magenta') +
            colored(f' LEVEL {self.stage} ', 'light_green') +
            colored('=====\n', 'light_magenta')
        )
        print(colored(f'Moves played: {self.player.prev_moves}', 'light_blue'))
        print(colored(f'Final Score: {self.player.score}\n', 'yellow'))
        print(colored('=' * 19, 'light_magenta'))
        self.leaderboard.display_scores()

        self.end_game_menu()

    def end_game_menu(self) -> None:
        """Displays the end game menu.

        Shows options for the next level, restarting the game, or returning
        to the main menu, and waits for user input.
        """
        print(colored('-' * 59, 'light_magenta'))
        print(
            colored('|', 'light_magenta') + 
            colored(' (N) Next Level ', 'light_green') + 
            colored('|', 'light_magenta') + 
            colored(' (X) Restart Game ', 'light_green') + 
            colored('|', 'light_magenta') + 
            colored(' (Any Key) Main Menu ', 'light_green') + 
            colored('|', 'light_magenta')
        )
        print(colored('-' * 59, 'light_magenta'))
        print('')
        self.end_game_menu_input()

    def end_game_menu_input(self) -> None:
        """Handles the input for the end game menu.

        Asks the player for their choice, directing them to the next level,
        restarting the game, or returning to the main menu based on their
        input.
        """
        while True:
            choice = input(colored(
                "Enter your choice: ", "cyan", attrs=["blink"]
                )).upper()

            if choice == 'N':
                self.play_next_level()
            elif choice == 'X':
                self.restart_game()
            else:
                self.return_to_main_menu()

    def play_next_level(self) -> None:
        """Handles the next level logic.

        Determines the next level based on the current level's file name,
        sets up the new level, and restarts the gameplay loop. If no next
        level is available, informs the player and returns to the main menu.
        """
        curr_lvl = os.path.basename(self.level.file)
        next_lvl = self.lvl_mgr.get_next_level(curr_lvl)

        if next_lvl:
            self.stage = str(int(self.stage) + 1)
            self.level = Level(next_lvl)
            self.player = Player(self.level.total_moves, self.level.eggs)
            self.move_mgr = MovementManager(self.level.grid)
            self.leaderboard = Leaderboard(int(self.stage))
            self.play()
        else:
            print(
                colored(
                    '\nThere are no more available levels for you to play.',
                    'magenta'
                )
            )
            input(colored(
                'Press ENTER to return to main menu.', 'green', attrs=['blink']
                ))
            self.return_to_main_menu()
