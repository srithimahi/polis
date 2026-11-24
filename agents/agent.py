from dataclasses import dataclass

@dataclass
class Agent:
    id: int
    name: str
    x: int
    y: int

    health: float = 10.0
    energy: float = 10.0
    hunger: float = 0.0

    age: int = 0
    perception_radius: int = 3

    def update(self):
        if self.health <= 0:
            return

        self.age += 1
        self.hunger = min(10.0, self.hunger + 0.05)
        self.energy = max(0.0, self.energy - 0.025)

        if self.hunger >= 10 or self.energy <= 0:
            self.health = max(0.0, self.health - 0.1)