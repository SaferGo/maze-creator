class Maze:
    mz = []
    size_maze = 0

    def __init__(self, new_size_maze):
        #remember to clear the maze later!
        self.size_maze = new_size_maze
        for x in range(new_size_maze):
            self.mz.append([0] * new_size_maze)

