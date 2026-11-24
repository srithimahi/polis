from world.environment import Environment
from agents.cognition import RandomPolicy

class Simulation:
    def __init__(self, world: Environment):
        self.world = world
        self.tick_count = 0
        self.paused = False
        self.policy = RandomPolicy()

    def tick(self):
        if self.paused:
            return

        self.tick_count += 1

        for agent in self.world.agents:
            agent.update()
            if agent.health <= 0:
                continue

            action = self.policy.decide()
            self.world.move_agent(agent, action)