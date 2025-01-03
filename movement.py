import time
from typing import Iterator

from utility import degridder


class MovementManager:
    """Handles all movement-related logic for the game."""

    dirs = {
        'L': '←',  
        'F': '↑', 
        'R': '→',  
        'B': '↓',  
    }   

    def __init__(self, grid: list[list[str]]):
        self.grid = grid

    @staticmethod
    def transform_cell_for_egg_movement(emoji: str) -> str:
        """
        Transform grid cell based on egg movement rules.
        """
        if emoji in ['🥚', '🍳']:
            return emoji
        if emoji == '🟩':
            return '🥚'
        if emoji == '🪹':
            return '🪺'
        return ''

    def get_egg_coordinates(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from left to right. 
        This is used in functions that move eggs one step left and one step forward.
        """
        return (
            (row, col)
            for row in range(len(self.grid))
            for col in range(len(self.grid[row]))
            if self.grid[row][col] == '🥚'
        )

    def get_egg_coordinates_right(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from right to left. 
        This is used in the function that move eggs one step right.
        """
        return (
            (row, col)
            for row in range(len(self.grid))
            for col in range(len(self.grid[row]) - 1, -1, -1)
            if self.grid[row][col] == '🥚'
        )

    def get_egg_coordinates_back(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from bottom to top. 
        This is used in the function that move eggs one step backward.
        """
        return (
            (row, col)
            for row in range(len(self.grid) - 1, -1, -1)
            for col in range(len(self.grid[row]))
            if self.grid[row][col] == '🥚'
        )

    def move_eggs_one_step_left(self) -> None:
        """Move all eggs one step left if possible."""
        for ex, ey in self.get_egg_coordinates():
            self.grid[ex][ey] = '🟩'
            if ey == 0:
                raise IndexError
            if self.grid[ex][ey - 1] not in ['🧱', '🪺', '🥚']:
                self.grid[ex][ey - 1] = self.transform_cell_for_egg_movement(
                    self.grid[ex][ey - 1]
                )
            else:
                self.grid[ex][ey] = '🥚'

    def move_eggs_one_step_right(self) -> None:
        """Move all eggs one step right if possible."""
        for ex, ey in self.get_egg_coordinates_right():
            self.grid[ex][ey] = '🟩'
            if self.grid[ex][ey + 1] not in ['🧱', '🪺', '🥚']:
                self.grid[ex][ey + 1] = self.transform_cell_for_egg_movement(
                    self.grid[ex][ey + 1]
                )
            else:
                self.grid[ex][ey] = '🥚'

    def move_eggs_one_step_forward(self) -> None:
        """Move all eggs one step forward if possible."""
        for ex, ey in self.get_egg_coordinates():
            self.grid[ex][ey] = '🟩'
            if ex == 0:
                raise IndexError
            if self.grid[ex - 1][ey] not in ['🧱', '🪺', '🥚']:
                self.grid[ex - 1][ey] = self.transform_cell_for_egg_movement(
                    self.grid[ex - 1][ey]
                )
            else:
                self.grid[ex][ey] = '🥚'

    def move_eggs_one_step_back(self) -> None:
        """Move all eggs one step back if possible."""
        for ex, ey in self.get_egg_coordinates_back():
            self.grid[ex][ey] = '🟩'
            if self.grid[ex + 1][ey] not in ['🧱', '🪺', '🥚']:
                self.grid[ex + 1][ey] = self.transform_cell_for_egg_movement(
                    self.grid[ex + 1][ey]
                )
            else:
                self.grid[ex][ey] = '🥚'

    def move_eggs_in_direction(self, direction: str) -> None:
        """Moves the egg in the specified direction, based on the user input."""
        if direction == 'L':
            self.move_eggs_one_step_left()
        elif direction == 'R':
            self.move_eggs_one_step_right()
        elif direction == 'F':
            self.move_eggs_one_step_forward()
        elif direction == 'B':
            self.move_eggs_one_step_back()
        else:
            print('Invalid movement!')

    def can_move(self, direction: str) -> bool:
        """Check if eggs can move in the specified direction."""
        if direction == 'L':
            return any(
                self.grid[x][y - 1] not in ['🧱', '🪺', '🥚']
                for x, y in self.get_egg_coordinates()
            )
        if direction == 'R':
            return any(
                self.grid[x][y + 1] not in ['🧱', '🪺', '🥚']
                for x, y in self.get_egg_coordinates_right()
            )
        if direction == 'F':
            return any(
                self.grid[x - 1][y] not in ['🧱', '🪺', '🥚']
                for x, y in self.get_egg_coordinates()
            )
        if direction == 'B':
            return any(
                self.grid[x + 1][y] not in ['🧱', '🪺', '🥚']
                for x, y in self.get_egg_coordinates_back()
            )
        return False

    def move_eggs_until_blocked(self, direction: str) -> None:
        """Moves eggs in a direction until blocked."""
        while self.can_move(direction):
            degridder(self.grid)
            self.move_eggs_in_direction(direction)
        degridder(self.grid)
        time.sleep(0.5)

