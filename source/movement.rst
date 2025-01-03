Movement Module
================

This module provides functions for managing egg movements within a grid. 
The core functionality includes moving eggs in various directions, transforming 
grid cells, and checking movement validity. 

Key Functions:
--------------

- :func:`move_eggs_in_direction`: Moves eggs in the direction specified by user input.
- :func:`move_eggs_one_step_*`: Functions that move eggs one step in different directions (left, right, forward, backward).
- :func:`can_eggs_move_*`: Functions that check if eggs can move in a particular direction.
- :func:`move_eggs_*_until_blocked`: Moves eggs in a direction until they are blocked by obstacles or grid boundaries.

The module also includes a dictionary at the end for mapping user input directions (L, F, R, B) to their respective arrow symbols. 

.. automodule:: movement
   :members:
   :undoc-members:
   :private-members:
   :show-inheritance:
