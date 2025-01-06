import time
from typing import Iterator

from utility import degridder


class MovementManager:
    """It provides methods for moving eggs in different directions
    (left, right, up, down), checking if movements are possible, and
    performing movement until blocked by obstacles.
    
    The methods also handle transformation of grid cells based on 
    the movement rules, such as replacing grid cells with appropriate
    emojis representing the egg's state.

    This class contains the dictionary for mapping the direction
    input to its corresponding arrow to be showed in the `Moves Played`
    in the game state.
    """

    dirs = {
        'L': '←',
        'F': '↑',
        'R': '→',
        'B': '↓',
    }

    def __init__(self, grid: list[list[str]]):
        """Initializes the movement manager with a grid."""
        self.grid = grid

    @staticmethod
    def transform_cell_for_egg_movement(emoji: str) -> str:
        """Transform grid cell based on egg movement.

        It checks the current emoji in the cell and returns the
        appropriate emoji for an egg's new position.
        """
        if emoji in ['🥚', '🍳']:
            return emoji
        if emoji == '🟩':
            return '🥚'
        if emoji == '🪹':
            return '🪺'
        return ''

    def egg_coords(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from left to right.
        This is used in functions that move eggs one step left and
        one step forward."""
        return (
            (row, col)
            for row in range(len(self.grid))
            for col in range(len(self.grid[row]))
            if self.grid[row][col] == '🥚'
        )

    def egg_coords_r(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from left to right.
        This is used in functions that move eggs one step left and one
        step forward."""
        return (
            (row, col)
            for row in range(len(self.grid))
            for col in range(len(self.grid[row]) - 1, -1, -1)
            if self.grid[row][col] == '🥚'
        )

    def egg_coords_b(self) -> Iterator[tuple[int, int]]:
        """Generate coordinates of eggs in the grid from bottom to top.
        This is used in the function that move eggs one step backward.
        """
        return (
            (row, col)
            for row in range(len(self.grid) - 1, -1, -1)
            for col in range(len(self.grid[row]))
            if self.grid[row][col] == '🥚'
        )

    def move_left(self) -> list[list[str]]:
        """Checks if eggs can move left without colliding with
        obstacles (like walls, other eggs, or filled nests). If the move
        is valid, the eggs are moved one step to the left.
        """
        for ex, ey in self.egg_coords():
            self.grid[ex][ey] = '🟩'
            if ey == 0:
                raise IndexError
            if self.grid[ex][ey - 1] not in ['🧱', '🪺', '🥚']:
                self.grid[ex][ey - 1] = self.transform_cell_for_egg_movement(
                    self.grid[ex][ey - 1]
                )
            else:
                self.grid[ex][ey] = '🥚'
        return self.grid

    def move_right(self) -> list[list[str]]:
        """Checks if eggs can move right without colliding with
        obstacles (like walls, other eggs, or filled nests). If the move
        is valid, the eggs are moved one step to the right."""
        for ex, ey in self.egg_coords_r():
            self.grid[ex][ey] = '🟩'
            if self.grid[ex][ey + 1] not in ['🧱', '🪺', '🥚']:
                self.grid[ex][ey + 1] = self.transform_cell_for_egg_movement(
                    self.grid[ex][ey + 1]
                )
            else:
                self.grid[ex][ey] = '🥚'
        return self.grid

    def move_up(self) -> list[list[str]]:
        """Checks if eggs can move forward without colliding with
        obstacles (like walls, other eggs, or filled nests). If the move
        is valid, the eggs are moved one step forward.
        """
        for ex, ey in self.egg_coords():
            self.grid[ex][ey] = '🟩'
            if ex == 0:
                raise IndexError
            if self.grid[ex - 1][ey] not in ['🧱', '🪺', '🥚']:
                self.grid[ex - 1][ey] = self.transform_cell_for_egg_movement(
                    self.grid[ex - 1][ey]
                )
            else:
                self.grid[ex][ey] = '🥚'
        return self.grid

    def move_down(self) -> list[list[str]]:
        """Checks if eggs can move backward without colliding with
        obstacles (like walls, other eggs, or filled nests). If the move
        is valid, the eggs are moved one step backward.
        """
        for ex, ey in self.egg_coords_b():
            self.grid[ex][ey] = '🟩'
            if self.grid[ex + 1][ey] not in ['🧱', '🪺', '🥚']:
                self.grid[ex + 1][ey] = self.transform_cell_for_egg_movement(
                    self.grid[ex + 1][ey]
                )
            else:
                self.grid[ex][ey] = '🥚'
        return self.grid

    def can_move(self, direction: str) -> bool:
        """Checks if the eggs can move in a specified direction by
        ensuring that there are no obstacles in the way and if they
        are not at the grid's boundary.
        """
        if direction == 'L':
            if any(y <= 0 for x, y in self.egg_coords()):
                raise IndexError("Eggs are at the leftmost boundary.")
            return any(
                self.grid[x][y - 1] not in ['🧱', '🪺', '🥚']
                for x, y in self.egg_coords()
            )

        elif direction == 'R':
            if any(y >= len(self.grid[0]) - 1 for x, y in self.egg_coords_r()):
                raise IndexError("Eggs are at the rightmost boundary.")
            return any(
                self.grid[x][y + 1] not in ['🧱', '🪺', '🥚']
                for x, y in self.egg_coords_r()
            )

        elif direction == 'F':
            if any(x <= 0 for x, y in self.egg_coords()):
                raise IndexError("Eggs are at the top boundary.")
            return any(
                self.grid[x - 1][y] not in ['🧱', '🪺', '🥚']
                for x, y in self.egg_coords()
            )

        elif direction == 'B':
            if any(x >= len(self.grid) - 1 for x, y in self.egg_coords_b()):
                raise IndexError("Eggs are at the bottom boundary.")
            return any(
                self.grid[x + 1][y] not in ['🧱', '🪺', '🥚']
                for x, y in self.egg_coords_b()
            )

        return False

    def move_eggs(self, direction: str) -> list[list[str]]:
        """Calls the respective move method depending on the user's 
        input direction.
        """
        if direction == 'L':
            self.move_left()
        elif direction == 'R':
            self.move_right()
        elif direction == 'F':
            self.move_up()
        elif direction == 'B':
            self.move_down()
        else:
            print('Invalid movement!')

        return self.grid

    def move_until_blocked(self, direction: str) -> list[list[str]]:
        """Repeatedly move the eggs in the specified direction
        until they encounter an obstacle (like a wall or another egg).
        It uses `degridder` to clear the grid and updates the grid at
        each step.
        """
        while self.can_move(direction):
            degridder(self.grid)
            self.grid = self.move_eggs(direction)
        degridder(self.grid)
        time.sleep(0.5)
        return self.grid
