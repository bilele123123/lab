from door import Door
import random


class DeadboltDoor(Door):

  def __init__(self):
    super().__init__()
    self.is_bolt1_locked = random.choice([True, False])
    self.is_bolt2_locked = random.choice([True, False])

  def examine_door(self):
    return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they’re locked or unlocked."

  def menu_options(self):
    return "1. Toggle Bolt 1 \n2. Toggle Bolt 2"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    if option == 1:
      self.is_bolt1_locked = not self.is_bolt1_locked
      return "You toggle the first bolt."
    elif option == 2:
      self.is_bolt2_locked = not self.is_bolt2_locked
      return "You toggle the second bolt."

  def is_unlocked(self):
    return not (self.is_bolt1_locked and self.is_bolt2_locked)

  def clue(self):
    if (self.is_bolt1_locked
        and not self.is_bolt2_locked) or (not self.is_bolt1_locked
                                          and self.is_bolt2_locked):
      return "You jiggle the door...it seems like one of the bolts is unlocked."
    else:
      return "You jiggle the door...it seems like it's completely locked"

  def success(self):
    return "You unlocked both deadbolts and opened the door."
