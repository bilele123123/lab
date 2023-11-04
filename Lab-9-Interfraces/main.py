# Name: Thai Le, Hoa Nguyen
# Date: 10/20/2023
# Description: This program will simulate an escape room and in order for the user to escape the room, they must open a series of three doors that are randomly chosen. Each door will have a different way to escape. Once you are able to open the three doors you will be able escape and win the game.

"""
Write a program that simulates an escape room by having the user open a series of three doors
random chosen from several different types of doors. Use the following class diagram to create
your program (you must create a main, the Door interface, and Basic Door, then you can choose
any two of the remaining four types of door to implement):
"""
"""
Main (main.py) –
1. open_door(door) – passes in a door object that the user will try to unlock. It should
display the description of the door, and the menu, then get the user’s selection, then pass
that value to the attempt method and display the result. If the attempt was successful,
then it should display the success message, otherwise, it should display the clue message
and repeat from the menu until the user successfully opens the door.
2. main – the main should have a loop that repeats three times for the three doors that the
user will try to open. Randomly choose a door from the ones that you implemented (it’s
fine if a particular door appears more than once) and pass it to open_door. After the user
has opened all three doors, then display a congratulatory message and end the game.
"""

from door import Door
from basic_door import BasicDoor
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
import random


def open_door(door):
    print(door.examine_door())

    if not isinstance(door, ComboDoor):
        print(door.menu_options())
        option = int(input(""))
        result = door.attempt(option)
        print(result)
        while not door.is_unlocked():
            print(door.clue())
            option = int(input(""))
            result = door.attempt(option)
            print(result)
    else:
        option = door.menu_options()
        result = door.attempt(option)
        print(result)
        while not door.is_unlocked():
            print(door.clue())
            option = door.menu_options()
            result = door.attempt(option)
            print(result)
        print(door.success())


def main():
    door_types = [BasicDoor, DeadboltDoor, ComboDoor]
    opened_doors = []

    print("Welcome to the Escape Room. \nYou must unlock 3 doors to escape...")

    for _ in range(3):
        door_class = random.choice(door_types)
        current_door = door_class()
        open_door(current_door)
        opened_doors.append(current_door)

    print("Congratulations! You escaped...this time.")


if __name__ == "__main__":
    main()
