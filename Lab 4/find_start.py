# Pass in the filled maze, and search through it to find 's', and return the position.
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                return [i, j]
