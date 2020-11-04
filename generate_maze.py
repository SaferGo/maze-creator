import random
from random import shuffle


class Position:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y


class Maze:
    mz = []

    def __init__(self, new_size_maze):
        self.size_maze = new_size_maze
        # remember to clear the maze later!
        # remember to declare a default size for the maze
        # here we create the square
        self.size_maze = new_size_maze
        for x in range(new_size_maze):
            self.mz.append([0] * new_size_maze)

        self.generate_maze()

    def generate_maze(self):
        start_point = Position(
            random.randint(0, self.size_maze - 1),
            random.randint(0, self.size_maze - 1)
        )

        stack = [start_point]
        visited = {}
        for i in range(self.size_maze):
            for j in range(self.size_maze):
                visited[Position(i, j)] = False
        visited[start_point] = True

        while len(stack) != 0:
            node = stack[-1]
            stack.pop()

            neighbours = self.get_neighbours(node.x, node.y)

            if len(neighbours) != 0:
                shuffle(neighbours)
                for x in neighbours:
                    if visited[x]:
                        continue
                    stack.append(x)



    def get_neighbours(self, pos_x, pos_y):
        node = Position(pos_x, pos_y)
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        all_neighbours = []

        for i in range(4):
            new_neighbour = Position(node.x + x[i], node.y + y[i])
            if self.in_range(new_neighbour):
                all_neighbours.append(new_neighbour)
        return all_neighbours

    def in_range(self, pos):
        if (pos.x >= 0 and pos.y >= 0) \
                and (pos.x < self.size_maze and pos.y < self.size_maze):
            return True
        return False
