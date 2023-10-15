from dragon import Dragon

class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops):
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, other):
        if self.swoops > 0:
            damage = random.randint(5, 8)
            other.take_damage(damage)
            self.swoops -= 1
            return f"{self.name} performs a swoop attack on you for {damage} damage."
        else:
            return f"{self.name} fails its swoop attack!"
    
    def __str__(self):
        return super().__str__() + f" Swoop attacks remaining: {self.swoops}"
