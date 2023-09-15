# Read the maze.txt and maze2.txt files and store the content in a 2D list, then return the stored 2D list.
def read_maze(filename):
    maze_array = []

    with open(filename, 'r') as maze_text:
        for line in maze_text:
            row = list(line.strip())
            maze_array.append(row)

    return maze_array