from check_input import get_int_range

def get_users_choice():
    print("""+-----+ +-----+ +-----+
|     | |     | |     |
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+""")

    choice = get_int_range("Find the queen: ", 1, 3)
    return choice
