from world.environment import Environment
from world.generator import TerrainGenerator
from agents.agent import Agent
from agents.perception import Perception

world = Environment(20, 15)
TerrainGenerator(seed=42).generate(world)

spawn = world.get_walkable_tiles()[0]

pluto = Agent(
    id=1,
    name="Pluto",
    x=spawn.x,
    y=spawn.y
)

perception = Perception()
observations = perception.observe(pluto, world)

print(f"Pluto can see {len(observations)} tiles.")

for observation in observations:
    if observation.food > 0:
        print(
            f"Food detected at ({observation.x}, "
            f"{observation.y}) | "
            f"Distance: {observation.distance} | "
            f"Quantity: {observation.food}"
        )