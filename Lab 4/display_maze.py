def display_maze(maze, loc):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if [i, j] == loc:
                print("X", end=" ")
            else:
                print(maze[i][j], end=" ") 
        print()
