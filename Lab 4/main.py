from check_input import get_int_range
from display_maze import display_maze
from find_start import find_start
from read_maze import read_maze

def main():
    print("-Maze Solver-")
    maze_array = read_maze("maze.txt")
    loc = find_start(maze_array)

    while maze_array[loc[0]][loc[1]] != 'f':
        display_maze(maze_array, loc)
        print(
            "\n1. Go North"
            "\n2. Go South"
            "\n3. Go East"
            "\n4. Go West"
        )

        choice = input("Enter your choice (1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)
            if choice == 1:
                new_loc = [loc[0] - 1, loc[1]]
            elif choice == 2:
                new_loc = [loc[0] + 1, loc[1]]
            elif choice == 3:
                new_loc = [loc[0], loc[1] + 1]
            elif choice == 4:
                new_loc = [loc[0], loc[1] - 1]

            if maze_array[new_loc[0]][new_loc[1]] == '*':
                print("You cannot move there.")
            else:
                loc = new_loc
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("Congratulations! You solved the maze.")

if __name__ == "__main__":
    main()
