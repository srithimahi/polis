from world.environment import Environment
from world.tile import Terrain
from rendering.renderer import Renderer

world = Environment(20, 15)

world.set_terrain(3, 5, Terrain.TREE)
world.set_terrain(4, 5, Terrain.TREE)
world.set_terrain(5, 5, Terrain.TREE)

world.set_terrain(10, 7, Terrain.WATER)
world.set_terrain(11, 7, Terrain.WATER)
world.set_terrain(10, 8, Terrain.WATER)
world.set_terrain(11, 8, Terrain.WATER)

world.set_terrain(9, 7, Terrain.SAND)
world.set_terrain(9, 8, Terrain.SAND)

renderer = Renderer(world)
renderer.run()