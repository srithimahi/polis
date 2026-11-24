import random

from world.environment import Environment
from world.generator import TerrainGenerator
from rendering.renderer import Renderer
from agents.agent import Agent

world = Environment(20, 15)

generator = TerrainGenerator(seed=42)
generator.generate(world)

walkable_tiles = world.get_walkable_tiles()

if walkable_tiles:
    spawn_tile = random.choice(walkable_tiles)

    agent = Agent(id=1, name="Pluto", x=spawn_tile.x, y=spawn_tile.y)
    print("Agent spawned: ", world.add_agent(agent))
    print(f"Spawn location: ({agent.x}, {agent.y})")

else:
    print("No valid spawn locations")

renderer = Renderer(world, tile_size=40)
renderer.run()