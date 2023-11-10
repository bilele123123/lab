import random
from entity import Entity


class Hero(Entity):

  def __init__(self, name):
    super().__init__(name, max_hp=25)
    self.row = 0
    self.col = 0

  def attack(self, entity):
    damage = random.randint(2, 5)
    entity.take_damage(damage)
    return f'{self.name} attacks a {entity.name} for {damage} damage.'

  def go_north(self, map_instance):
    if self.row > 0:
      self.row -= 1
      return map_instance[self.row][self.col]
    else:
      return 'o'

  def go_south(self, map_instance):
    if self.row < len(map_instance) - 1:
      self.row += 1
      return map_instance[self.row][self.col]
    else:
      return 'o'

  def go_east(self, map_instance):
    if self.col < len(map_instance[0]) - 1:
      self.col += 1
      return map_instance[self.row][self.col]
    else:
      return 'o'

  def go_west(self, map_instance):
    if self.col > 0:
      self.col -= 1
      return map_instance[self.row][self.col]
    else:
      return 'o'
