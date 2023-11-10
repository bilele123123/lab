import random
from enemy_factory import EnemyFactory

class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        difficult_enemies = ["Zombie", "Skeleton", "Goblin"]
        return random.choice(difficult_enemies)()