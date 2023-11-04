from entity import Entity
import random

class Enemy(Entity):
    enemies = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']
    def __init__(self):
        super().__init__(random.choice(self.ENEMY_NAMES), max_hp=random.randint(4, 8))

    def attack(self, entity):
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'