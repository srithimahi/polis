from perlin_noise import PerlinNoise
from world.environment import Environment
from world.tile import Terrain

class TerrainGenerator:
    def __init__(self, seed: int = 42):
        self.seed = seed
        self.elevation_noise = PerlinNoise(octaves=3, seed=seed)
        self.vegetation_noise = PerlinNoise(octaves=6, seed=seed+1)

    def get_elevation(self, x, y, width, height):
        return self.elevation_noise([x / width, y / height])

    def get_vegetation(self, x, y, width, height):
        return self.vegetation_noise([x / width, y / height])

    def generate(self, world: Environment):
        for row in world.tiles:
                for tile in row:
                    elevation = self.get_elevation(tile.x, tile.y, world.width, world.height)
                    if elevation < -0.15:
                        tile.terrain = Terrain.WATER
                    elif elevation < -0.05:
                        tile.terrain = Terrain.SAND
                    else:
                        vegetation = self.get_vegetation(tile.x, tile.y, world.width, world.height)
                        if vegetation > 0.1:
                            tile.terrain = Terrain.TREE 
                        else:
                            tile.terrain = Terrain.GRASS