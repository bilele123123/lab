def display_queen_loc(queen_loc):

    cards = [
        "+-----+ +-----+ +-----+",
        "|     | |     | |     |",
       f"|  {'Q' if queen_loc == 1 else 'K'}  | |  {'Q' if queen_loc == 2 else 'K'}  | |  {'Q' if queen_loc == 3 else 'K'}  |",
        "|     | |     | |     |" if queen_loc in (1, 2, 3) else "|  K  | |  K  | |  K  |",
        "+-----+ +-----+ +-----+",
    ]

    for line in cards:
        print(line)

