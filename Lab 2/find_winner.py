def find_winner(player_points):
    print("Player 1's points =", player_points[0])
    print("Player 2's points =", player_points[1])

    if player_points[0] > player_points[1]:
        print("Player 1 wins!")
    elif player_points[0] < player_points[1]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

