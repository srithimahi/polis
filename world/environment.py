from world.tile import Tile, Terrain

class Environment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = []
        self.generate_world()

    def generate_world(self):
        self.tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                tile = Tile(x, y)
                row.append(tile)
            self.tiles.append(row)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get_tile(self, x: int, y: int):
        if self.in_bounds(x, y):
            return self.tiles[y][x]
        return None

    def set_terrain(self, x: int, y: int, terrain: Terrain):
        if self.in_bounds(x, y):
            tile = self.get_tile(x, y)
            tile.terrain = terrain