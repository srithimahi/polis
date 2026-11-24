import pygame
import random
from world.generator import TerrainGenerator
from world.environment import Environment
from world.tile import Terrain

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
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

        
