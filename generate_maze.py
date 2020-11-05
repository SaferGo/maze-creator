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

    def __init__(self, new_size_maze, maze_s, new_width, new_height, ms):
        self.visited.clear()
        self.parent.clear()
        self.mz.clear()
        self.size_maze = new_size_maze
        self.maze_screen = maze_s
        self.width = new_width
        self.height = new_height
        self.ms = ms
        # remember to declare a default size for the maze
        # here we create the square
        self.size_maze = new_size_maze
        self.draw_corner_maze()
        for x in range(new_size_maze):
            line = []
            for y in range(new_size_maze):
                new_node = Node(x, y)
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
        # print("-----------")
        print("START POINT: ", start_point.x, start_point.y)
        self.visited[start_point.x, start_point.y] = True
        new_connection = False

        while len(stack) != 0:
            node = stack[-1]
            stack.pop()
            self.visited[node.x, node.y] = True

            if new_connection:
                self.remove_wall_between(node, self.parent[node.x, node.y])
                self.maze_screen.after(2, self.draw_cell(self.parent[node.x, node.y]))
                self.maze_screen.update()
                new_connection = False

            neighbours = self.get_neighbours(node.x, node.y)

            if len(neighbours) != 0:
                shuffle(neighbours)
                self.remove_wall_between(node, neighbours[-1])
                self.maze_screen.after(2, self.draw_cell(node))
                self.maze_screen.update()

                for adj in neighbours:
                    self.parent[adj.x, adj.y] = node
                    stack.append(adj)
            else:
                # this means that one path finished
                # so, we need to backtrack the nodes
                # and make a new connection
                new_connection = True
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
        if node1.x - node2.x == 1:
            self.mz[node1.x][node1.y].top_wall = False
            self.mz[node2.x][node2.y].bottom_wall = False
        if node1.x - node2.x == -1:
            self.mz[node1.x][node1.y].bottom_wall = False
            self.mz[node2.x][node2.y].top_wall = False
        if node1.y - node2.y == 1:
            self.mz[node1.x][node1.y].left_wall = False
            self.mz[node2.x][node2.y].right_wall = False
        if node1.y - node2.y == -1:
            self.mz[node1.x][node1.y].right_wall = False
            self.mz[node2.x][node2.y].left_wall = False

    def draw_cell(self, node):
        # x, y, x y
        # print("Voy a borrar: ", node.x, node.y)
        size_step_w = int(self.width / self.size_maze)
        size_step_h = int(self.height / self.size_maze)
        if node.top_wall:
            # print("Top!")
            self.maze_screen.create_line(node.y * size_step_w, node.x * size_step_h, (node.y + 1) * size_step_w,
                                         node.x * size_step_h, fill="black", width=2)
        if node.bottom_wall:
            # print("Bottom!")
            self.maze_screen.create_line(node.y * size_step_w, (node.x + 1) * size_step_h, (node.y + 1) * size_step_w,
                                         (node.x + 1) * size_step_h, fill="black", width=2)
        if node.right_wall:
            # print("Right!")
            self.maze_screen.create_line(
                (node.y + 1) * size_step_w, node.x * size_step_h, (node.y + 1) * size_step_w,
                (node.x + 1) * size_step_h, fill="black", width=2)
        # if node.left_wall:
        # print("Left!")
    def draw_corner_maze(self):
        self.maze_screen.create_line(0, 0, 0, self.height, fill="black", width=2)
        self.maze_screen.create_line(0, 0, self.width, 0, fill="black", width=2)
        self.maze_screen.create_line(self.width, 0, self.width, self.height, fill="black", width=2)
        self.maze_screen.create_line(0, self.height, self.width, self.height, fill="black", width=2)


    def in_range(self, x, y):
        if self.size_maze > x >= 0 and self.size_maze > y >= 0:
            return True
        return False
