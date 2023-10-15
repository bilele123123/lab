from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, max_hp, f_shots):
        super().__init__(name, max_hp)
        self.fire_shots = f_shots

    def special_attack(self, other):
        if self.fire_shots > 0:
            damage = random.randint(5, 9)
            other.take_damage(damage)
            self.fire_shots -= 1
            return f"{self.name} engulfs you in flames for {damage} damage!"
        else:
            return f"{self.name} fails to summon its flames!"
    
    def __str__(self):
        return super().__str__() + f" Fire Shots remaining: {self.fire_shots}"
