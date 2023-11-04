from door import Door
import random


class BasicDoor(Door):

  def __init__(self):
    super().__init__()
    self.is_pushed = random.choice([True, False])

  def examine_door(self):
    return "A door that is either pushed or pulled"

  def menu_options(self):
    return "1. Push \n2. Pull"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    if (option == 1 and self.is_pushed) or (option == 2
                                            and not self.is_pushed):
      self.is_pushed = True
      return "You push the door."
    else:
      self.is_pushed = False
      return "You pull the door."

  def is_unlocked(self):
    return self.is_pushed

  def clue(self):
    return "Try the other way."

  def success(self):
    return "Congratulations, you opened the door."
