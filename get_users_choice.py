from check_input import get_int_range


def get_users_choice():
  #Print out three cards faced down
  print("+-----+ +-----+ +-----+")
  print("|     | |     | |     |")
  print("|  1  | |  2  | |  3  |")
  print("|     | |     | |     |")
  print("+-----+ +-----+ +-----+")

  king_card = print("+-----+" +
                    "|     |"
                    "|  K  |"
                    "|     |"
                    "+-----+")

  print(king_card)

  choice = get_int_range("choice:", 1, 3)
  print(choice)


get_users_choice()
