from entity import Entity
import random

class Dragon(Entity):
    def basic_attack(self, other):
        damage = random.randint(3, 7)
        other.take_damage(damage)
        return f"{self.name} smashes you with its tail for {damage} damage!"

    def special_attack(self, other):
        damage = random.randint(4, 8)
        other.take_damage(damage)
        return f"{self.name} scratched you with its claws for {damage} damage!"
