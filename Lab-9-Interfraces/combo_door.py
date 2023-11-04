from check_input import get_int_range
from door import Door
import random


class ComboDoor(Door):

  def __init__(self):
    super().__init__()
    self.combo = random.randint(1, 10)
    self.user_attempt = -1

  def examine_door(self):
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    print("Enter a number (1-10): ", end="")
    return get_int_range("", 1, 10)

  def get_menu_max(self):
    return 10

  def attempt(self, option):
    self.user_attempt = option
    return f"You turn the dial to... {option}"

  def is_unlocked(self):
    return self.user_attempt == self.combo

  def clue(self):
    if self.user_attempt > self.combo:
      return "Try a lower value."
    elif self.user_attempt < self.combo:
      return "Try a higher value."

  def success(self):
    return "You found the correct value and opened the door."
