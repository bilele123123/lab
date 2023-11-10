import random
from enemy_factory import EnemyFactory

class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        easy_enemies = ["EasyZombie", "EasySkeleton", "EasyGoblin"]
        return random.choice(easy_enemies)()
