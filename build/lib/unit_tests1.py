from utility import degridder, clear_screen
from movement import MovementManager
from game import Level


def test_degridder() -> None:
    '''Tests the utility function degridder()'''

    def da(grid): # degridder assert
        def f(unction):
            try:
                unction(grid)
                return True
            except:
                raise Exception
        assert f(degridder)

    da([])
    da((['one', 'two', 'three'], 'four', (), ('5' for _ in range(6))))
    da([('gen' for er in range(8)) for _ in range(7)])

    clear_screen() # degridder prints, hence the need for clear_screen

test_degridder()


def test_transform_cell_for_egg_movement() -> None:
    '''Tests the transform_cell_for_egg_movement() for the MovementManager class'''

    assert MovementManager([[]]).transform_cell_for_egg_movement('🍳') == '🍳'
    assert MovementManager([[]]).transform_cell_for_egg_movement('🪺') == ''
    assert MovementManager([[]]).transform_cell_for_egg_movement('🥚') == '🥚'
    assert MovementManager([[]]).transform_cell_for_egg_movement(['🥚']) == ''
    assert MovementManager([[]]).transform_cell_for_egg_movement('5'*10**5) == ''

test_transform_cell_for_egg_movement()


def test_egg_coordses() -> None:
    '''Tests the egg_coords(), egg_coords_b() and egg_coords_r() methods for the MovementManager class'''

    grid = [
        ['🥚', '🥚', '🥚'],
        ['🥚', '🟩', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*MovementManager(grid).egg_coords()} == {*MovementManager(grid).egg_coords_b()} == {*MovementManager(grid).egg_coords_r()}
    assert [*MovementManager(grid).egg_coords()] == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0)]
    assert [*MovementManager(grid).egg_coords_b()] == [(2,0), (1,0), (1,2), (0,0), (0,1), (0,2)]
    assert [*MovementManager(grid).egg_coords_r()] == [(0,2), (0,1), (0,0), (1,2), (1,0), (2,0)]

    grid = [
        ['🥚', '🥚', '🥚', '🟩', '🟩', '🥚'],
        ['🥚', '🟩', '🥚', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*MovementManager(grid).egg_coords()} == {*MovementManager(grid).egg_coords_b()} == {*MovementManager(grid).egg_coords_r()}
    assert [*MovementManager(grid).egg_coords()] == [(0,0), (0,1), (0,2), (0,5), (1,0), (1,2), (1,3), (2,0)]
    assert [*MovementManager(grid).egg_coords_b()] == [(2,0), (1,0), (1,2), (1,3), (0,0), (0,1), (0,2), (0,5)]
    assert [*MovementManager(grid).egg_coords_r()] == [(0,5), (0,2), (0,1), (0,0), (1,3), (1,2), (1,0), (2,0)]

    grid = []
    assert {*MovementManager(grid).egg_coords()} == {*MovementManager(grid).egg_coords_b()} == {*MovementManager(grid).egg_coords_r()} 
    assert [*MovementManager(grid).egg_coords()] == [*MovementManager(grid).egg_coords_b()] == [*MovementManager(grid).egg_coords_r()] 
    # no eggs, so equal

    grid = ['🟩', '🥚']
    assert {*MovementManager(grid).egg_coords()} == {*MovementManager(grid).egg_coords_b()} == {*MovementManager(grid).egg_coords_r()} 
    assert [*MovementManager(grid).egg_coords()] == [*MovementManager(grid).egg_coords_b()] == [*MovementManager(grid).egg_coords_r()] 
    # same egg, so equal

test_egg_coordses()


def test_truth_condition():
    '''Tests the can_move() method for the MovementManager class'''

    err_ctr = 0

    grid = [
        ['🥚', '🟩', '🧱'],
        ['🥚', '🥚', '🪹'],
        ['🧱', '🪺', '🟩']
    ]
    assert not MovementManager(grid).can_move('B')
    assert MovementManager(grid).can_move('R')
    try: MovementManager(grid).can_move('F')
    except: err_ctr += 1
    try: MovementManager(grid).can_move('L')
    except: err_ctr += 1

    grid = [
        ['🟩', '🧱'],
        ['🧱', '🥚']
    ]
    try: MovementManager(grid).can_move('R')
    except: err_ctr += 1
    try: MovementManager(grid).can_move('B')
    except: err_ctr += 1

    assert err_ctr == 4

test_truth_condition()


def test_single_moves():
    '''Tests the singular move_down(), move_left(), move_up() and move_right() methods, as well as tests the unifying move_eggs() method for the MovementManager class'''

    err_ctr = 0 # counter to check if all index errs were raised

    # checks if moves in correct direction
    grid = [
        ['🟩', '🥚'],
        ['🟩', '🟩'],
    ]
    assert MovementManager(grid).move_down() == [
        ['🟩', '🟩'], 
        ['🟩', '🥚']
    ]
    assert MovementManager(grid).move_left() == [
        ['🟩', '🟩'], 
        ['🥚', '🟩']
    ]
    assert MovementManager(grid).move_up() == [
        ['🥚', '🟩'], 
        ['🟩', '🟩']
    ]
    assert MovementManager(grid).move_right() == [
        ['🟩', '🥚'], 
        ['🟩', '🟩']
    ]
    # checks if IndexError is raised when an egg moving right goes out of bounds
    try: MovementManager(grid).move_right()
    except IndexError: err_ctr += 1

    # checks if grid doesn't change if no eggs
    grid = [['🟩', '🧱', '🪺', '🍳']]
    assert MovementManager(grid).move_eggs('R') == [['🟩', '🧱', '🪺', '🍳']]
    assert MovementManager(grid).move_eggs('L') == [['🟩', '🧱', '🪺', '🍳']]
    assert MovementManager(grid).move_eggs('F') == [['🟩', '🧱', '🪺', '🍳']]
    assert MovementManager(grid).move_eggs('B') == [['🟩', '🧱', '🪺', '🍳']]

    grid = [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪹', '🥚']
    ]
    # checks if update for nest works during a move
    assert MovementManager(grid).move_eggs('L') == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if egg acts as obstacle for other eggs
    assert MovementManager(grid).move_eggs('B') == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if pans consume eggs
    assert MovementManager(grid).move_eggs('R') == [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🟩', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if IndexError is raised when an egg moving forward goes out of bounds
    try: MovementManager(grid).move_up()
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving left goes out of bounds
    grid = [['🥚']]
    try: MovementManager(grid).move_left()
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving back goes out of bounds
    grid = [['🥚']]
    try: MovementManager(grid).move_down()
    except IndexError: err_ctr += 1

    assert err_ctr == 4 

test_single_moves()


def test_contd_moves():
    '''Tests the move_until_blocked() method for the MovementManager class'''

    err_ctr = 0

    grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert MovementManager(grid).move_until_blocked('R') == [
        ['🟩', '🟩', '🥚', '🥚', '🥚', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert MovementManager(grid).move_until_blocked('B') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    # checks if repeated movement in same direction does nothing
    assert MovementManager(grid).move_until_blocked('B') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    # checks if pans continually consume eggs
    assert MovementManager(grid).move_until_blocked('L') == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    
    grid = [
        ['🟩'], 
        ['🥚']
    ]
    try: MovementManager(grid).move_until_blocked('F')
    except IndexError: err_ctr += 1

    assert err_ctr == 1

    clear_screen() # move_until_blocked() method uses degridder()

test_contd_moves()


def test_egg_count():

    level = Level('leveldummy.in')

    level.grid = [['🪺'*3]*5, ['🥚'*2]*6]
    assert level.count_eggs_and_nests() == 3*5+2*6

    level.grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    a = level.count_eggs_and_nests
    MovementManager(level.grid).move_eggs('R')
    b = level.count_eggs_and_nests
    MovementManager(level.grid).move_eggs('B')
    c = level.count_eggs_and_nests
    MovementManager(level.grid).move_eggs('L')
    d = level.count_eggs_and_nests
    assert a == b == c != d

test_egg_count()
