import random
from random import shuffle


class Node:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.top_wall = True
        self.left_wall = True
        self.right_wall = True
        self.bottom_wall = True


class Maze:
    mz = []

    def __init__(self, new_size_maze):
        self.size_maze = new_size_maze
        # remember to clear the maze later!
        # remember to declare a default size for the maze
        # here we create the square
        self.size_maze = new_size_maze
        for x in range(new_size_maze):
            line = []
            for y in range(new_size_maze):
                new_node = Node(x, y)
                if x == 0:
                    new_node.top_wall = False
                if y == 0:
                    new_node.left_wall = False
                if x == new_size_maze - 1:
                    new_node.bottom_wall = False
                if y == new_size_maze - 1:
                    new_node.right_wall = False

                line.append(new_node)
            self.mz.append(line)

        self.generate_maze()

    def generate_maze(self):
        random_x = random.randint(0, self.size_maze - 1)
        random_y = random.randint(0, self.size_maze - 1)
        start_point = self.mz[random_x][random_y]

        stack = [start_point]
        visited = {}
        for i in range(self.size_maze):
            for j in range(self.size_maze):
                visited[i, j] = False
        visited[start_point.x, start_point.y] = True

        while len(stack) != 0:
            node = stack[-1]
            stack.pop()

            neighbours = self.get_neighbours(node.x, node.y)

            if len(neighbours) != 0:
                shuffle(neighbours)
                for adj_node in neighbours:
                    if visited[adj_node.x, adj_node.y]:
                        continue
                    visited[adj_node.x, adj_node.y] = True
                    stack.append(adj_node)

    def get_neighbours(self, pos_x, pos_y):
        node = self.mz[pos_x][pos_y]
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        all_neighbours = []

        for i in range(4):
            if self.in_range(node.x + x[i], node.y + y[i]):
                all_neighbours.append(
                    self.mz[node.x + x[i]][node.y + y[i]]
                )
        return all_neighbours

    def remove_wall_between(self, other):
        print("s")

    def in_range(self, x, y):
        if (x >= 0 and y >= 0) \
                and (x < self.size_maze and y < self.size_maze):
            return True
        return False
