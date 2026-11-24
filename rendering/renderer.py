import pygame
import random
from world.generator import TerrainGenerator
from world.environment import Environment
from world.tile import Terrain
from agents.agent import Agent
from simulation.engine import Simulation

TERRAIN_COLORS = {
    Terrain.GRASS: (181, 205, 150),
    Terrain.WATER: (134, 182, 207),
    Terrain.TREE: (82, 124, 77),
    Terrain.SAND: (233, 214, 166),
}

class Renderer:
    def __init__(self, world: Environment, tile_size: int = 40):
        self.world = world
        self.tile_size = tile_size

        pygame.init()

        self.screen = pygame.display.set_mode((world.width * tile_size, world.height * tile_size))

        pygame.display.set_caption("heylo")

        self.clock = pygame.time.Clock()
        self.simulation = Simulation(world)
        self.accumulator = 0.0
        self.tick_interval = 0.25

    def draw_tile(self, tile):
        color = TERRAIN_COLORS[tile.terrain]

        rect = pygame.Rect(
            tile.x * self.tile_size,
            tile.y * self.tile_size,
            self.tile_size,
            self.tile_size
        )

        pygame.draw.rect(self.screen, color, rect)

    def draw_world(self):
        for row in self.world.tiles:
            for tile in row:
                self.draw_tile(tile)

    def run(self):
        running = True

        while running:
            dt = self.clock.tick(60) / 1000.0
            self.accumulator += dt

            while self.accumulator >= self.tick_interval:
                self.simulation.tick()
                self.accumulator -= self.tick_interval

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_r:
                        seed = random.randint(1, 1000000)
                        generator = TerrainGenerator(seed=seed)
                        generator.generate(self.world)

                        print(f"Generated world with seed: {seed}")

            self.draw_world()
            self.draw_agents()

            pygame.display.flip()
        pygame.quit()

    def draw_agent(self, agent: Agent):
        center_x = agent.x * self.tile_size + self.tile_size // 2
        center_y = agent.y * self.tile_size + self.tile_size // 2

        pygame.draw.circle(
            self.screen,
            (160, 132, 191),
            (center_x, center_y),
            self.tile_size // 3
        )

        bar_x = agent.x * self.tile_size + 3
        bar_y = max(0, agent.y * self.tile_size - 18)

        self.draw_bar(
            bar_x, bar_y,
            agent.health, (78, 152, 89)
        )

        self.draw_bar(
            bar_x, bar_y + 6,
            agent.energy, (204, 42, 217)
        )

        self.draw_bar(
            bar_x, bar_y + 12,
            agent.hunger, (232, 41, 126)
        )


    def draw_agents(self):
        for agent in self.world.agents:
            self.draw_agent(agent)

    def draw_bar(self, x, y, value, color):
        width = self.tile_size - 6
        height = 4

        ratio = value / 10.0

        pygame.draw.rect(self.screen, (60, 60, 60), (x, y, width, height))

        pygame.draw.rect(self.screen, color, (x, y, int(width * ratio), height))

        
