from dataclasses import dataclass

from agents.agent import Agent
from world.environment import Environment
from world.tile import Terrain

@dataclass
class TileObservation:
    x: int
    y: int
    terrain: Terrain
    food: int
    distance: int

class Perception:
    def observe(self, agent: Agent, world: Environment) -> list[TileObservation]:
        observation = []
        radius = agent.perception_radius

        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                distance = abs(dx) + abs(dy)

                if distance > radius:
                    continue

                x = agent.x + dx
                y = agent.y + dy

                tile = world.get_tile(x, y)

                if tile is None:
                    continue

                observation.append(TileObservation(
                    x=tile.x,
                    y=tile.y,
                    terrain=tile.terrain,
                    food=tile.food,
                    distance=distance
                ))

        return observation

