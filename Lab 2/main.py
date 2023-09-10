from check_input import get_yes_no
from display_dice import display_dice 
from find_winner import find_winner 
from roll_dice import roll_dice  

def main():
    print("- Ship, Captain, and Crew! -\n")
    player_scores = [0, 0]  
    for player in range(2):  
        print(f"Player #{player + 1}'s Turn:")
        keep = []  
        cargo = []  
        rolls_left = 3  

        for roll_num in range(3): 
            dice = [0, 0, 0, 0, 0]
            dice = roll_dice(dice) 
            display_dice("Roll", dice) 

            if 6 in dice and 5 in dice and 4 in dice:
                keep.extend([6, 5, 4])
                print("Yo ho ho! Ye secured a ship!")
                display_dice("Keep", keep)

            if len(keep) == 3:
                cargo.extend(dice[:2])
                print("Cargo =", ' '.join(map(str, dice[:2])))
                print("Your cargo points are:", sum(cargo))

            if roll_num < 2:
                roll_again = input("Roll again? (y/n): ").lower()
                if roll_again != 'y':
                    break

        player_scores[player] = sum(cargo) 

        print(f"Player #{player + 1} points =", player_scores[player])
        print()

    find_winner(player_scores)

main()
