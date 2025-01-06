import os
from typing import Optional

from utility import get_level_files


class LevelManager:
    """Manages the level files and handles functions for loading 
    levels and getting the next available level after each game.
    """
    def __init__(self) -> None:
        """Retrieves the list of level files using the `get_level_files`
        function and stores it in the `levels` attribute.
        """
        self.levels = get_level_files()

    @staticmethod
    def load_level(filename: str) -> tuple[list[list[str]], int]:
        """eads the contents of a level file and processes it to 
        extract the grid layout and the total number of moves for the level.
        It returns the grid as a list of lists (representing rows and columns)
        and the total number of moves.
        """
        with open(filename, encoding='utf-8') as file:
            rows = int(file.readline().strip())
            total_moves = int(file.readline().strip())
            grid = [list(file.readline().strip()) for _ in range(rows)]
        return grid, total_moves

    def get_next_level(self, current_level: str) -> Optional[str]:
        """Finds the next level file.

        This method searches for the next level file after the provided
        `current_level` by finding its index in the `levels` list. If
        there is a next level, it returns the file path of the next
        level. If the current level is the last one, it returns None.
        """
        current_level_name = os.path.basename(current_level)
        level_index = self.levels.index(current_level_name)

        if level_index + 1 < len(self.levels):
            return os.path.join('levels', self.levels[level_index + 1])
        else:
            return None
