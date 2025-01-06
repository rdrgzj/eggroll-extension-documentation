from utility import clear_screen
from movement import MovementManager as Move


def test_transform_cell_for_egg_movement() -> None:
    '''Tests the `transform_cell_for_egg_movement()` for the 
    `MovementManager` class; to reproduce, call an assertion using 
    the method within this function.
    '''

    assert Move([[]]).transform_cell_for_egg_movement('🍳') == '🍳'
    assert Move([[]]).transform_cell_for_egg_movement('🪺') == ''
    assert Move([[]]).transform_cell_for_egg_movement('🥚') == '🥚'
    assert Move([[]]).transform_cell_for_egg_movement(['🥚']) == ''
    assert Move([[]]).transform_cell_for_egg_movement('5'*10**5) == ''

test_transform_cell_for_egg_movement()


def test_egg_coordses() -> None:
    '''Tests the `egg_coords()`, `egg_coords_b()` and `egg_coords_r()` 
    methods for the `MovementManager` class; to reproduce, call an 
    assertion using the method/s within this function.
    '''

    grid = [
        ['🥚', '🥚', '🥚'],
        ['🥚', '🟩', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*Move(grid).egg_coords()} == {*Move(grid).egg_coords_b()} == {*Move(grid).egg_coords_r()}
    assert [*Move(grid).egg_coords()] == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0)]
    assert [*Move(grid).egg_coords_b()] == [(2,0), (1,0), (1,2), (0,0), (0,1), (0,2)]
    assert [*Move(grid).egg_coords_r()] == [(0,2), (0,1), (0,0), (1,2), (1,0), (2,0)]

    grid = [
        ['🥚', '🥚', '🥚', '🟩', '🟩', '🥚'],
        ['🥚', '🟩', '🥚', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*Move(grid).egg_coords()} == {*Move(grid).egg_coords_b()} == {*Move(grid).egg_coords_r()}
    assert [*Move(grid).egg_coords()] == [(0,0), (0,1), (0,2), (0,5), (1,0), (1,2), (1,3), (2,0)]
    assert [*Move(grid).egg_coords_b()] == [(2,0), (1,0), (1,2), (1,3), (0,0), (0,1), (0,2), (0,5)]
    assert [*Move(grid).egg_coords_r()] == [(0,5), (0,2), (0,1), (0,0), (1,3), (1,2), (1,0), (2,0)]

    grid = []
    assert {*Move(grid).egg_coords()} == {*Move(grid).egg_coords_b()} == {*Move(grid).egg_coords_r()} 
    assert [*Move(grid).egg_coords()] == [*Move(grid).egg_coords_b()] == [*Move(grid).egg_coords_r()] 
    # no eggs, so equal

    grid = ['🟩', '🥚']
    assert {*Move(grid).egg_coords()} == {*Move(grid).egg_coords_b()} == {*Move(grid).egg_coords_r()} 
    assert [*Move(grid).egg_coords()] == [*Move(grid).egg_coords_b()] == [*Move(grid).egg_coords_r()] 
    # same egg, so equal

test_egg_coordses()


def test_truth_condition() -> None:
    '''Tests the `can_move()` method for the `MovementManager` class; 
    to reproduce, either call an assertion using the method 
    within this function or create a try-except block if 
    expecting for exceptions.
    '''

    err_ctr = 0

    grid = [
        ['🥚', '🟩', '🧱'],
        ['🥚', '🥚', '🪹'],
        ['🧱', '🪺', '🟩']
    ]
    assert not Move(grid).can_move('B')
    assert Move(grid).can_move('R')
    try: Move(grid).can_move('F')
    except: err_ctr += 1
    try: Move(grid).can_move('L')
    except: err_ctr += 1

    grid = [
        ['🟩', '🧱'],
        ['🧱', '🥚']
    ]
    try: Move(grid).can_move('R')
    except: err_ctr += 1
    try: Move(grid).can_move('B')
    except: err_ctr += 1

    assert err_ctr == 4

test_truth_condition()


def test_single_moves() -> None:
    '''Tests the singular `move_down()`, `move_left()`, `move_up()` 
    and `move_right()` methods, as well as tests the unifying 
    `move_eggs()` method for the `MovementManager` class; to 
    reproduce, either call an assertion using the method within 
    this function or create a try-except block if expecting for 
    exceptions.
    '''

    err_ctr = 0 # counter to check if all index errs were raised

    # checks if moves in correct direction
    grid = [
        ['🟩', '🥚'],
        ['🟩', '🟩'],
    ]
    assert Move(grid).move_down() == [
        ['🟩', '🟩'], 
        ['🟩', '🥚']
    ]
    assert Move(grid).move_left() == [
        ['🟩', '🟩'], 
        ['🥚', '🟩']
    ]
    assert Move(grid).move_up() == [
        ['🥚', '🟩'], 
        ['🟩', '🟩']
    ]
    assert Move(grid).move_right() == [
        ['🟩', '🥚'], 
        ['🟩', '🟩']
    ]
    # checks if IndexError is raised when an egg moving right goes out of bounds
    try: Move(grid).move_right()
    except IndexError: err_ctr += 1

    # checks if grid doesn't change if no eggs
    grid = [['🟩', '🧱', '🪺', '🍳']]
    assert Move(grid).move_eggs('R') == [['🟩', '🧱', '🪺', '🍳']]
    assert Move(grid).move_eggs('L') == [['🟩', '🧱', '🪺', '🍳']]
    assert Move(grid).move_eggs('F') == [['🟩', '🧱', '🪺', '🍳']]
    assert Move(grid).move_eggs('B') == [['🟩', '🧱', '🪺', '🍳']]

    grid = [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪹', '🥚']
    ]
    # checks if update for nest works during a move
    assert Move(grid).move_eggs('L') == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if egg acts as obstacle for other eggs
    assert Move(grid).move_eggs('B') == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if pans consume eggs
    assert Move(grid).move_eggs('R') == [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🟩', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if IndexError is raised when an egg moving forward goes out of bounds
    try: Move(grid).move_up()
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving left goes out of bounds
    grid = [['🥚']]
    try: Move(grid).move_left()
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving back goes out of bounds
    grid = [['🥚']]
    try: Move(grid).move_down()
    except IndexError: err_ctr += 1

    assert err_ctr == 4 

test_single_moves()


def test_contd_moves() -> None:
    '''Tests the `move_until_blocked()` method for the 
    `MovementManager` class; to reproduce, either call an 
    assertion using the method within this function or create a 
    try-except block if expecting for exceptions.
    '''

    err_ctr = 0

    grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert Move(grid).move_until_blocked('R') == [
        ['🟩', '🟩', '🥚', '🥚', '🥚', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert Move(grid).move_until_blocked('B') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    # checks if repeated movement in same direction does nothing
    assert Move(grid).move_until_blocked('B') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    # checks if pans continually consume eggs
    assert Move(grid).move_until_blocked('L') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    
    grid = [
        ['🟩'], 
        ['🥚']
    ]
    try: Move(grid).move_until_blocked('F')
    except IndexError: err_ctr += 1

    assert err_ctr == 1

    clear_screen() # move_until_blocked() method uses degridder()

test_contd_moves()