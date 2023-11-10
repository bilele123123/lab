#Name: Thai Le, Hoa Nguyen
#Date: 11/4/2023
#Description: You are spawned in a dungeon maze and must fight your way through the maze to get to the exist. You will encounter monsters and treasures along the way. Your health will decrease if you fight a monster. Additionally, you may run away from monsters. Your health will increase if you find a potion. Find your way to the exit and escape the maze to win. The program will exit if the user decides to quit.

from hero import Hero
from map import Map
from enemy import Enemy
from check_input import get_int_range

class Main:
  @staticmethod
  def run_game():
      hero_name = input("What is your name, traveler? ")
      hero = Hero(hero_name)
      game_map = Map()

      while True:
          print(hero)
          print(game_map.show_map((hero.row, hero.col)))

          choice = get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)

          if choice == 5:
              print("Goodbye!")
              break

          if choice in [1, 2, 3, 4]:
              loc = None
              if choice == 1:
                  loc = (hero.row - 1, hero.col)
                  valid_move = hero.go_north(game_map)
              elif choice == 2:
                  loc = (hero.row + 1, hero.col)
                  valid_move = hero.go_south(game_map)
              elif choice == 3:
                  loc = (hero.row, hero.col + 1)
                  valid_move = hero.go_east(game_map)
              elif choice == 4:
                  loc = (hero.row, hero.col - 1)
                  valid_move = hero.go_west(game_map)


              if valid_move != 'o':
                  game_map.reveal(loc)
                  encounter = game_map[loc[0]][loc[1]]
                  Main.handle_encounter(hero, encounter, game_map, loc)
              else:
                print("You cannot go that way...\n")

  @staticmethod
  def handle_encounter(hero, encounter, game_map, loc):
      if encounter == 'm':
          enemy = Enemy()
          print(f"You encounter a {enemy.name}\nHP: {enemy.hp}/{enemy.max_hp}")

          while enemy.hp > 0 and hero.hp > 0:
              choice = get_int_range(f"1. Attack {enemy.name}\n2. Run Away\nEnter choice: ", 1, 2)

              if choice == 1:
                  attack_result = hero.attack(enemy)
                  print(attack_result)

                  if enemy.hp > 0:
                      enemy_attack_result = enemy.attack(hero)
                      print(enemy_attack_result)
              elif choice == 2:
                game_map[loc[0]][loc[1]] = 'm' 
                print(f"You ran away! \n")
                break

          if enemy.hp <= 0:
              print(f"You have slain a {enemy.name} \n")
              game_map[loc[0]][loc[1]] = 'm' 

      elif encounter == 'i':
          print("You found a Health Potion! You drink it to restore your health. \n")
          hero.heal()
          game_map[loc[0]][loc[1]] = 'i' 

      elif encounter == 'f':
          print("Congratulations! You found the exit.\nGame Over")
          exit()

      elif encounter == 'n':
          print("There is nothing here... \n")

      elif encounter == 's':
          print("You wound up back at the start of the dungeon. \n")
          game_map[loc[0]][loc[1]] = 's' 

      elif encounter == 'o':
          print("You cannot go that way... \n")

if __name__ == "__main__":
  Main.run_game()
