import random

class Enemy:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self):
        self.hp = self.max_hp

    def __str__(self):
        return f'{self.name}\nHP: {self.hp}/{self.max_hp}'

    def attack(self, entity):
        pass

class EasyZombie(Enemy):
    def __init__(self):
        super().__init__("Easy Zombie", max_hp=random.randint(4, 5))

    def attack(self, entity):
        damage = random.randint(1, 5)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'

class EasySkeleton(Enemy):
    def __init__(self):
        super().__init__("Easy Skeleton", max_hp=random.randint(3, 4))

    def attack(self, entity):
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'

class EasyGoblin(Enemy):
    def __init__(self):
        super().__init__("Easy Goblin", max_hp=random.randint(4, 6))

    def attack(self, entity):
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'

class Zombie(Enemy):
    def __init__(self):
        super().__init__("Fast Zombie", max_hp=random.randint(8, 10))

    def attack(self, entity):
        damage = random.randint(5, 12)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'

class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Spooky Skeleton", max_hp=random.randint(6, 10))

    def attack(self, entity):
        damage = random.randint(6, 10)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Angry Goblin", max_hp=random.randint(8, 12))

    def attack(self, entity):
        damage = random.randint(6, 12)
        entity.take_damage(damage)
        return f'{self.name} attacks {entity.name} for {damage} damage.'
