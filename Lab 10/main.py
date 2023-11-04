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
            print(hero.name)
            print(game_map.show_map((hero.row, hero.col)))

            choice = get_int_range("1. Go North \n2. Go South \n3. Go East \n4. Go West \n5. Quit \nEnter choice: ", 1, 5)

            if choice == '5':
                print("Goodbye!")
                break

            if choice in ['1', '2', '3', '4']:
                loc = None
                if choice == '1':
                    loc = (hero.row - 1, hero.col)
                    valid_move = hero.go_north(game_map)
                elif choice == '2':
                    loc = (hero.row + 1, hero.col)
                    valid_move = hero.go_south(game_map)
                elif choice == '3':
                    loc = (hero.row, hero.col + 1)
                    valid_move = hero.go_east(game_map)
                elif choice == '4':
                    loc = (hero.row, hero.col - 1)
                    valid_move = hero.go_west(game_map)

                if valid_move:
                    game_map.reveal(loc)
                    encounter = game_map[loc[0]][loc[1]]
                    Main.handle_encounter(hero, encounter, game_map)

if __name__ == "__main__":
    Main.run_game()
