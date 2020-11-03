import random

class Position:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy

class Maze:
    mz = []
    size_maze = 0

    def __init__(self, new_size_maze):
        #remember to clear the maze later!
        #here we create the square
        self.size_maze = new_size_maze
        for x in range(new_size_maze):
            self.mz.append([0] * new_size_maze)

        startPoint = Position(
            random.randint(0, new_size_maze - 1),
            random.randint(0, new_size_maze - 1)
        )

        self.generate_maze()

    def generate_maze(self):
        startPoint = Position(
            random.randint(0, self.size_maze - 1),
            random.randint(0, self.size_maze - 1)
        )

        stack = []
        stack.append(startPoint)

        



