from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from check_input import get_int_range
import random


def main():
  name = input("What is your name, challenger?\n")
  hero = Hero(name, 50)
  print(f"Welcome to dragon training, {hero.name}\nYou must defeat 3 dragons.")
  dragon_list = [
      Dragon("Deadly Nadder", 10),
      FireDragon("Gronckle", 15, 3),
      FlyingDragon("Timberjack", 20, 5)
  ]

  while dragon_list and hero.hp > 0:
    print_hero_status(hero)
    print_dragon_status(dragon_list)
    dragon_choice = get_int_range("Choose a dragon to attack: ", 1,
                                  len(dragon_list)) - 1

    attack_choice = get_int_range(
        "Attack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: ", 1,
        2)

    if attack_choice == 1:
      message = hero.basic_attack(dragon_list[dragon_choice])
    else:
      message = hero.special_attack(dragon_list[dragon_choice])

    print(message)

    if dragon_list[dragon_choice].hp == 0:
      print(f"You defeated the {dragon_list[dragon_choice].name}!")
      del dragon_list[dragon_choice]

    if not dragon_list:
      print(
          "Congratulations! You have defeated all 3 dragons. You have passed the trials."
      )
      break

    # Dragon attacks
    dragon = random.choice(dragon_list)
    attack_type = random.randint(1, 2)

    if attack_type == 1:
      message = dragon.basic_attack(hero)
    else:
      message = dragon.special_attack(hero)

    print(message)

    if hero.hp == 0:
      print(f"You were defeated by the {dragon.name}. Game over.")


def print_hero_status(hero):
  print(f"{hero}\n")


def print_dragon_status(dragon_list):
  for idx, dragon in enumerate(dragon_list, start=1):
    print(f"{idx}. Attack {dragon}\n")


if __name__ == "__main__":
  main()
