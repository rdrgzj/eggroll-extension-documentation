import os

from utility import get_level_files

class LevelManager:
    """Manages level-related functionality including loading and transitioning levels."""
    
    def __init__(self) -> None:
        """Retrieves the list of level files using the `get_level_files` function and 
        stores it in the `levels` attribute.
        """
        self.levels = get_level_files()

    def load_level(self, filename: str) -> tuple[list[list[str]], int]:
        """Reads a level file and initializes the grid and move count.
        
        The level file is expected to be structured as follows:
        (1) The first line contains the number of rows in the grid.
        (2) The second line contains the total number of moves required.
        (3) Each subsequent line represents a row of the grid, where each character represents an element of the grid.
        """
        with open(filename, encoding='utf-8') as file:
            rows = int(file.readline().strip())
            total_moves = int(file.readline().strip())
            grid = [list(file.readline().strip()) for _ in range(rows)]
        return grid, total_moves

    def get_next_level(self, current_level: str) -> str | None:
        """The method looks for the current level in the list of available levels and returns the path of the next level.
        If the current level is the last one in the sequence or not found, `None` is returned.
        """
        current_level_name = os.path.basename(current_level)
        level_index = self.levels.index(current_level_name)

        if level_index + 1 < len(self.levels):
            return os.path.join('levels', self.levels[level_index + 1])
        else:
            return None
