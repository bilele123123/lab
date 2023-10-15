from entity import Entity
import random

class Hero(Entity):
    def basic_attack(self, other):
        damage = random.randint(1, 6) + random.randint(1, 6)
        other.take_damage(damage)
        return f"You slashed the {other.name} with your sword for {damage} damage."

    def special_attack(self, other):
        damage = random.randint(1, 12)
        other.take_damage(damage)
        return f"You hit the {other.name} with your arrow for {damage} damage."
