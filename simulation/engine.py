from world.environment import Environment

class Simulation:
    def __init__(self, world: Environment):
        self.world = world
        self.tick_count = 0
        self.paused = False

    def tick(self):
        if self.paused:
            return

        self.tick_count += 1

        for agent in self.world.agents:
            agent.update()