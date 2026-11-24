import random

from agents.actions import Action

class RandomPolicy:
    def decide(self) -> Action:
        return random.choice(list(Action))