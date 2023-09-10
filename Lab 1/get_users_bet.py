from check_input import get_int_range

def get_users_bet(money):
  print(f"You have: ${money}")
  bet = get_int_range("How much you wanna bet? ", 1, money)
  return bet