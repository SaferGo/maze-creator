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
    visited = {}

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

        for i in range(self.size_maze):
            for j in range(self.size_maze):
                self.visited[i, j] = False

        self.generate_maze()

    def generate_maze(self):
        random_x = random.randint(0, self.size_maze - 1)
        random_y = random.randint(0, self.size_maze - 1)
        start_point = self.mz[random_x][random_y]

        stack = [start_point]

        self.visited[start_point.x, start_point.y] = True

        while len(stack) != 0:
            #print("Hello!")
            node = stack[-1]
            stack.pop()

            neighbours = self.get_neighbours(node.x, node.y)

            if len(neighbours) != 0:
                shuffle(neighbours)

                self.visited[neighbours[0].x, neighbours[0].y] = True
                self.remove_wall_between(node, neighbours[0])

                stack.append(neighbours[0])

    def get_neighbours(self, pos_x, pos_y):
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        all_neighbours = []

        for i in range(4):
            new_x = pos_x + x[i]
            new_y = pos_y + y[i]
            if (self.in_range(new_x, new_y)) and \
                    (self.visited[new_x, new_y] is False):
                all_neighbours.append(self.mz[new_x][new_y])
        return all_neighbours

    def remove_wall_between(self, node1, node2):
        if node1.x - node2.x == 1:
            self.mz[node1.x][node1.y].top_wall = False
            self.mz[node2.x][node2.y].bottom_wall = False
        if node1.x - node2.y == -1:
            self.mz[node1.x][node1.y].bottom_wall = False
            self.mz[node2.x][node2.y].top_wall = False
        if node1.y - node2.y == 1:
            self.mz[node1.x][node1.y].left_wall = False
            self.mz[node2.x][node2.y].right_wall = False
        if node1.y - node2.y == -1:
            self.mz[node1.x][node1.y].right_wall = False
            self.mz[node2.x][node2.y].left_wall = False

    def in_range(self, x, y):
        if self.size_maze > x >= 0 and self.size_maze > y >= 0:
            return True
        return False
