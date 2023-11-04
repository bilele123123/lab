'''
Door (door.py) – interface – these methods are abstract and should be implemented in each of
the subclasses of door (not in door itself).
1. examine_door(self) – returns a string description of the door.
2. menu_options(self) – returns a string of the menu options that user can choose from when
attempting to unlock the door.
3. get_menu_max(self) – returns the number of options in the above menu.
4. attempt(self, option) – passes in the user’s selection from the menu. Uses that value to
update the attributes that are needed to determine whether the user has unlocked the door
(which is done in the is_unlocked method below). Returns a string describing what the
user attempted.
5. is_unlocked(self) – checks to see if the door was unlocked, returns true if it is, false
otherwise.
6. clue(self) – returns the hint that is returned if the user was unsuccessful at their attempt.
7. success(self) – returns the congratulatory message if the user was successful
'''

from abc import ABC, abstractmethod


class Door(ABC):

  def __init__(self):
    super().__init__()

  @abstractmethod
  def examine_door(self):
    pass

  @abstractmethod
  def menu_options(self):
    pass

  @abstractmethod
  def get_menu_max(self):
    pass

  @abstractmethod
  def attempt(self, option):
    pass

  @abstractmethod
  def is_unlocked(self):
    pass

  @abstractmethod
  def clue(self):
    pass

  @abstractmethod
  def success(self):
    pass
