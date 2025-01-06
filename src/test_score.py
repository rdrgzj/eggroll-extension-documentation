from utility import clear_screen
from movement import MovementManager as Move
from game import Level, Player


def test_egg_count() -> None:
    '''Tests the count_eggs_and_nests() method for the Level 
    class; to reproduce, call an assertion using the method 
    within this function.
    '''

    level = Level('leveldummy.in')

    level.grid = [['🪺'] * 5, ['🥚'] * 6]
    assert level.count_eggs_and_nests() == 11

    level.grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    a = level.count_eggs_and_nests()
    Move(level.grid).move_until_blocked('R')
    b = level.count_eggs_and_nests()
    Move(level.grid).move_until_blocked('B')
    c = level.count_eggs_and_nests()
    Move(level.grid).move_until_blocked('L')
    d = level.count_eggs_and_nests()
    assert a == b == c != d

    clear_screen()

test_egg_count()


def test_score() -> None:
    '''Tests the calc_score() method for the Level class 
    and the update_score() method for the Player class;
    to reproduce, call an assertion using the method 
    within this function.
    '''

    level = Level('leveldummy.in')

    level.grid = [['🪺'] * 5, ['🥚'] * 6]
    level.eggs = level.count_eggs_and_nests()
    assert level.calc_score() == 5 * 10

    level.grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    level.eggs = level.count_eggs_and_nests()
    assert level.calc_score() == 0
    Move(level.grid).move_until_blocked('R')
    assert level.calc_score() == 10
    Move(level.grid).move_until_blocked('B')
    assert level.calc_score() == 20
    Move(level.grid).move_until_blocked('L')
    assert level.calc_score() == 10

    clear_screen()

test_score()


def test_finalization() -> None:
    '''Tests the finalize_score() method for the Player class; 
    to reproduce, call the method and then make an assertion 
    within this function.
    '''

    play = Player(35, 5)
    play.finalize_score()
    assert play.score == 35

    play = Player(35, 5)
    play.score = 34
    play.finalize_score()
    assert play.score == 69

    clear_screen()

test_finalization()