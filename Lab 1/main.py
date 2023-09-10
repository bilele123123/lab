import get_users_bet
import get_users_choice
import display_queen_loc
import random

def main():
  print("-Three card Monte-")
  print("Find the queen to double your bet!")
  money = 100
  choice = True
  while money > 0 and choice:
    bet = get_users_bet.get_users_bet(money)
    money -= bet
    users_choice = get_users_choice.get_users_choice()
    queen_location = random.randint(1, 3)
    display_queen_loc.display_queen_loc(queen_location)
    if users_choice == queen_location:
      print("You got lucky this time...")
      money += bet * 2
    else:
      print("Sorry... you lose.")
    if money > 0:
      play_again = input("Play again? (Y/N): ")
      choice = play_again.upper() == "Y"

  
  if (money == 0):
    print("You're out of money. Beat it loser!")
  else:
    print("See you next time!")

main()
