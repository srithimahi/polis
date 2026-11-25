from world.tile import Tile, Terrain
from agents.agent import Agent
from agents.actions import Action

class Environment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = []
        self.generate_world()
        self.agents = []

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

    def is_walkable(self, x: int, y: int) -> bool:
        tile = self.get_tile(x, y)
        if tile is None:
            return False

        return tile.terrain in (Terrain.GRASS, Terrain.SAND)

    def add_agent(self, agent: Agent) -> bool:
        if self.is_walkable(agent.x, agent.y):
            self.agents.append(agent)
            return True

        return False

    def get_walkable_tiles(self):
        walkable_tiles = []
        for row in self.tiles:
            for tile in row:
                if self.is_walkable(tile.x, tile.y):
                    walkable_tiles.append(tile)

        return walkable_tiles

    def move_agent(self, agent: Agent, action: Action) -> bool:
        dx, dy = action.value
        new_x = agent.x + dx
        new_y = agent.y + dy

        if agent.health > 0:
            if self.is_walkable(new_x, new_y):
                agent.x = new_x
                agent.y = new_y
                return True
        return False

    def eat(self, agent: Agent) -> bool:
        if agent.health <= 0:
            return False

        tile = self.get_tile(agent.x, agent.y)

        if tile is None or tile.food <= 0:
            return False

        tile.food -= 1
        agent.hunger = max(0.0, agent.hunger - 3.0)

        return True