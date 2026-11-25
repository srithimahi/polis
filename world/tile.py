from enum import Enum
from dataclasses import dataclass

class Terrain(Enum): 
    GRASS = 0
    WATER = 1
    TREE = 2
    SAND = 3

@dataclass
class Tile:
    x: int
    y: int
    terrain: Terrain = Terrain.GRASS
    food: int = 0