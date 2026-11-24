from enum import Enum

class Action(Enum):
    MOVE_NORTH = (0, -1)
    MOVE_SOUTH = (0, 1)
    MOVE_EAST = (1, 0)
    MOVE_WEST = (-1, 0)
    IDLE = (0, 0)