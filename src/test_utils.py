from utility import get_level_files, clear_screen, degridder
from leaderboard import Leaderboard
from level_manager import LevelManager as LvlMgr


def test_degridder() -> None:
    '''Tests the `utility` function `degridder()`; to reproduce 
    unit tests for this function, call `da(grid)` inside this 
    function, where `grid` is the desired grid to be displayed.
    '''

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


def test_leaderboard() -> None:
    '''Tests the `load_scores()`, `update_leaderboard()` 
    and `store_scores()` methods for the `Leaderboard` 
    class; to reproduce, alter `leaderboard0.txt` in
    the `leaderboard` directory and the `initial` and/or 
    `new(er)_scores` list inside this function however 
    you wish and assert any changes accordingly.
    '''

    lead = Leaderboard(0)
    initial = [ # ALTER FOR ANY CHANGES IN leaderboard0.txt
        ('dummy', 25),
        ('leaderboard', 24), 
        ('for', 23), 
        ('tests', 22)
    ]
    assert lead.load_scores() == initial

    #---------------------------------------------#

    new_scores = [ # ALTER
        ('paikotikot', 3),
        ('lang mula', 1),
        ('nang', 18),
        ('mailang', 15),
        ('gawa ng', 12),
        ('yong', 9),
        ('tingin at', 14),
        ('ngiti', 5),
    ]
    for score in new_scores:
        lead.update_leaderboard(*score)
    assert lead.load_scores() == [ # ALTER FOR ANY CHANGES IN leaderboard0.txt OR new_scores
        ('dummy', 25), 
        ('leaderboard', 24), 
        ('for', 23), 
        ('tests', 22), 
        ('nang', 18)
    ]

    newer_scores = [ # ALTER
        ('kiss me', 25),
        ('out of the', 24),
        ('bearded barley', 24)
    ]
    for score in newer_scores:
        lead.update_leaderboard(*score)
    assert lead.load_scores() == [ # ALTER FOR ANY CHANGES IN leaderboard0.txt OR newer_scores
        ('dummy', 25), 
        ('kiss me', 25), 
        ('leaderboard', 24), 
        ('out of the', 24), 
        ('bearded barley', 24)
    ]

    #---------------------------------------------#

    lead.scores = [*initial]
    lead.store_scores()
    assert lead.load_scores() == initial

test_leaderboard()


def test_lvl_mgr() -> None:
    '''Tests the `utility` function `get_level_files()`
    and the `get_next_level()` method for the 
    `LevelManager` class; non-reproducible as it uses
    the pre-made levels to test.
    '''

    assert get_level_files() == LvlMgr().levels == [
        'level1.in', 'level2.in', 'level3.in', 
        'level4.in', 'level5.in', 'level6.in', 
        'level7.in', 'level8.in', 'level9.in',
    ]

    assert LvlMgr().get_next_level(r'levels\level3.in') == r'levels\level4.in'
    assert not LvlMgr().get_next_level(r'levels\level9.in')

test_lvl_mgr()