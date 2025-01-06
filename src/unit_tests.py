from test_movement import test_contd_moves, test_egg_coordses, test_single_moves, test_transform_cell_for_egg_movement, test_truth_condition
from test_score import test_score, test_egg_count, test_finalization
from test_utils import test_degridder, test_leaderboard, test_lvl_mgr

# MOVEMENT FUNCTIONS UNIT TESTS

test_transform_cell_for_egg_movement()
test_egg_coordses()
test_truth_condition()
test_single_moves()
test_contd_moves()

# SCORE-RELATED FUNCTIONS UNIT TESTS

test_egg_count()
test_score()
test_finalization()

# MISCELLANEOUS FUNCTIONS UNIT TESTS

test_degridder()
test_leaderboard()
test_lvl_mgr()