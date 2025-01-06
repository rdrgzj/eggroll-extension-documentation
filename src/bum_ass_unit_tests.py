from utility import degridder, clear_screen
from movement import MovementManager


def test_degridder() -> None:
    '''Tests degridder()'''
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
    '''Tests transform_cell_for_egg_movement()'''
    assert MovementManager.transform_cell_for_egg_movement('🍳') == '🍳'
    assert MovementManager.transform_cell_for_egg_movement('🪺') == ''
    assert MovementManager.transform_cell_for_egg_movement('🥚') == '🥚'
    assert MovementManager.transform_cell_for_egg_movement(['🥚']) == ''
    assert MovementManager.transform_cell_for_egg_movement('5'*10**5) == ''
test_transform_cell_for_egg_movement()


def test_egg_coordses() -> None:
    '''Tests egg_coords(), egg_coords_b() and egg_coords_r()'''
    grid = [
        ['🥚', '🥚', '🥚'],
        ['🥚', '🟩', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*MovementManager.egg_coords()} == {*MovementManager.egg_coords_b()} == {*MovementManager.egg_coords_r()}
    assert [*MovementManager.egg_coords()] == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0)]
    assert [*MovementManager.egg_coords_b()] == [(2,0), (1,0), (1,2), (0,0), (0,1), (0,2)]
    assert [*MovementManager.egg_coords_r()] == [(0,2), (0,1), (0,0), (1,2), (1,0), (2,0)]

    grid = [
        ['🥚', '🥚', '🥚', '🟩', '🟩', '🥚'],
        ['🥚', '🟩', '🥚', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*MovementManager.egg_coords()} == {*MovementManager.egg_coords_b()} == {*MovementManager.egg_coords_r()}
    assert [*MovementManager.egg_coords()] == [(0,0), (0,1), (0,2), (0,5), (1,0), (1,2), (1,3), (2,0)]
    assert [*MovementManager.egg_coords_b()] == [(2,0), (1,0), (1,2), (1,3), (0,0), (0,1), (0,2), (0,5)]
    assert [*MovementManager.egg_coords_r()] == [(0,5), (0,2), (0,1), (0,0), (1,3), (1,2), (1,0), (2,0)]

    grid = []
    assert {*MovementManager.egg_coords()} == {*MovementManager.egg_coords_b()} == {*MovementManager.egg_coords_r()} 
    assert [*MovementManager.egg_coords()] == [*MovementManager.egg_coords_b()] == [*MovementManager.egg_coords_r()] 
    # no eggs, so equal

    grid = ['🟩', '🥚']
    assert {*MovementManager.egg_coords()} == {*MovementManager.egg_coords_b()} == {*MovementManager.egg_coords_r()} 
    assert [*MovementManager.egg_coords()] == [*MovementManager.egg_coords_b()] == [*MovementManager.egg_coords_r()] 
    # same egg, so equal
test_egg_coordses()


def test_truth_condition():
    err_ctr = 0
    grid = [
        ['🥚', '🟩', '🧱'],
        ['🥚', '🥚', '🪹'],
        ['🧱', '🪺', '🟩']
    ]
    assert not MovementManager.can_move('B')
    assert MovementManager.can_move('R')
    try: MovementManager.can_move('F')
    except: err_ctr += 1
    try: MovementManager.can_move('L')
    except: err_ctr += 1

    grid = [
        ['🟩', '🧱'],
        ['🧱', '🥚']
    ]
    try: MovementManager.can_move('R')
    except: err_ctr += 1
    try: MovementManager.can_move('B')
    except: err_ctr += 1

    assert err_ctr == 4
test_truth_condition()
