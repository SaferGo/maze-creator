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
    parent = {}

    def __init__(self, new_size_maze, maze_s, new_width, ms):
        self.visited.clear()
        self.parent.clear()
        self.mz.clear()

        self.size_maze = new_size_maze
        self.maze_screen = maze_s
        self.width = new_width
        self.ms = ms
        self.size_maze = new_size_maze

        self.draw_empty_maze()

        for x in range(self.size_maze):
            line = []
            for y in range(self.size_maze):
                self.visited[x, y] = False
                line.append(Node(x, y))
            self.mz.append(line)

        self.generate_maze()

    def generate_maze(self):
        random_x = random.randint(0, self.size_maze - 1)
        random_y = random.randint(0, self.size_maze - 1)
        start_point = self.mz[random_x][random_y]

        stack = [start_point]
        print("START POINT: ", start_point.x, start_point.y)
        self.visited[start_point.x, start_point.y] = True
        self.parent[start_point.x, start_point.y] = start_point

        while len(stack) != 0:
            node = stack[-1]
            stack.pop()
            self.visited[node.x, node.y] = True

            self.maze_screen.after(
                3, self.remove_wall_between(
                    node, self.parent[node.x, node.y]
                )
            )
            self.maze_screen.update()

            neighbours = self.get_neighbours(node.x, node.y)

            if len(neighbours) != 0:
                shuffle(neighbours)

                for adj in neighbours:
                    self.parent[adj.x, adj.y] = node
                    stack.append(adj)
            else:
                # this means that one path finished
                # so, we need to backtrack the nodes
                # and make a new connection
                print("path finished, now backtracking!")
        print("Finished!")

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
        step = int(self.width / self.size_maze)
        if node1.x - node2.x == 1:
            self.mz[node1.x][node1.y].top_wall = False
            self.mz[node2.x][node2.y].bottom_wall = False
            self.maze_screen.create_line(
                node1.y * step, node1.x * step,
                (node1.y + 1) * step, node1.x * step,
                fill="RoyalBlue3", width=2
            )

        if node1.x - node2.x == -1:
            self.mz[node1.x][node1.y].bottom_wall = False
            self.mz[node2.x][node2.y].top_wall = False
            self.maze_screen.create_line(
                node1.y * step, (node1.x + 1) * step,
                (node1.y + 1) * step, (node1.x + 1) * step,
                fill="RoyalBlue3", width=2
            )
        if node1.y - node2.y == 1:
            self.mz[node1.x][node1.y].left_wall = False
            self.mz[node2.x][node2.y].right_wall = False
            self.maze_screen.create_line(
                (node2.y + 1) * step, node2.x * step,
                (node2.y + 1) * step, (node2.x + 1) * step,
                fill="RoyalBlue3", width=2
            )

        if node1.y - node2.y == -1:
            self.mz[node1.x][node1.y].right_wall = False
            self.mz[node2.x][node2.y].left_wall = False
            self.maze_screen.create_line(
                node2.y * step, node2.x * step,
                node2.y * step, (node2.x + 1) * step,
                fill="RoyalBlue3", width=2
            )

    def draw_empty_maze(self):
        step = int(self.width / self.size_maze)
        for x in range(0, self.width, step):
            self.maze_screen.create_line(
                x, 0, x, self.width, fill="black", width=2
            )  # vertical lines
            self.maze_screen.create_line(
                0, x, self.width, x, fill="black", width=2
            )  # horizontal lines

    def in_range(self, x, y):
        if self.size_maze > x >= 0 and self.size_maze > y >= 0:
            return True
        return False
