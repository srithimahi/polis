from world.environment import Environment
from world.generator import TerrainGenerator
from rendering.renderer import Renderer

world = Environment(20, 15)

generator = TerrainGenerator(seed=42)
generator.generate(world)

renderer = Renderer(world, tile_size=40)
renderer.run()