import os

from termcolor import colored

class Leaderboard:
    """Manages the leaderboard, storing and displaying high scores.
    This uses a .txt file per level where we can read and write 
    to store high scores. The .txt files are in leaderboard
    directory.
    """

    def __init__(self, level: int):
        """Initializes the leaderboard for a specific level."""
        self.scores_file = os.path.join(
            'leaderboard', f'leaderboard{level}.txt'
            )
        self.level = level
        self.scores: list[tuple[str, int]] = []

    def load_scores(self) -> list[tuple[str, int]]:
        """Loads the leaderboard scores from the scores file.

        Reads the leaderboard file, splits each line into name and score, and
        appends them to the scores list as tuples.
        """
        self.scores.clear()
        with open(self.scores_file, 'r', encoding='utf-8') as file:
            for line in file:
                name, score = line.split(',')
                self.scores.append((name, int(score)))
        return self.scores

    def update_leaderboard(self, name: str, score: int,) -> None:
        """Updates the leaderboard with a new score.

        Adds a new player name and score to the leaderboard, sorts the
        leaderboard by score in descending order, and keeps only the
        top 5 scores. Then stores the updated leaderboard (handled
        by another function).
        """
        self.load_scores()
        self.scores.append((name, score))
        self.scores.sort(key=lambda x: x[1],reverse=True)
        if len(self.scores) >= 5:
            self.scores = self.scores[:5]
        self.store_scores()

    def store_scores(self) -> None:
        """Stores the current leaderboard scores to the scores file.

        Writes the player names and scores to the leaderboard file,
        overwriting the existing data.
        """
        with open(self.scores_file, 'w', encoding='utf-8') as file:
            for name, score in self.scores:
                file.write(f'{name},{score}\n')
    
    def display_scores(self):
        """Displays the leaderboard scores after each level.

        Prints the leaderboard to the terminal, showing the rank, player name,
        and score for each player in the top 5.
        """
        if self.scores:
            print(colored('\nHigh Scores', 'light_green', attrs=['bold']))
            print(colored('-' * 40, 'light_magenta'))
            print(colored(f'{'Rank':<6}{'Name':<20}{'Score':<10}', 'blue', attrs=['bold']))
            print(colored('-' * 40, 'light_magenta'))
            for i, (name, score) in enumerate(self.scores, 1):
                print(colored(f'{str(i):<6}{name:<20}{score:<10}', 'yellow'))
            print(colored('-' * 40, 'light_magenta'))
            print('')
