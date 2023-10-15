from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from check_input import get_int_range
import random

def main():
    name = input("What is your name, challenger? \n")
    hero = Hero(name, 100)
    print(f"Welcome to dragon training, {hero.name} \nYou must defeat 3 dragons.")
    dragon_list = [Dragon("Deadly Nadder", 10), FireDragon("Gronckle", 15, 3), FlyingDragon("Timberjack", 20, 5)]

if __name__ == "__main__":
    main()
