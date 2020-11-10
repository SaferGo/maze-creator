import random
from random import shuffle
import time


class Node:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.top_wall = True
        self.left_wall = True
        self.right_wall = True
        self.bottom_wall = True


def is_wall(node, x, y):
    if x == 0 and y == -1:
        return node.left_wall
    if x == 0 and y == 1:
        return node.right_wall
    if y == 0 and x == -1:
        return node.top_wall
    if y == 0 and x == 1:
        return node.bottom_wall


class Maze:
    mz = []
    visited = {}
    parent = {}

    def __init__(self, new_size_maze, maze_s, new_width):
        self.visited.clear()
        self.parent.clear()
        self.mz.clear()

        self.size_maze = new_size_maze
        self.maze_screen = maze_s
        self.width = new_width
        self.size_maze = new_size_maze
        self.step = int(self.width / self.size_maze)

        self.initialize_attributes()
        self.draw_empty_maze()
        self.generate_maze()

    def initialize_attributes(self):
        for x in range(self.size_maze):
            line = []
            for y in range(self.size_maze):
                self.visited[x, y] = False
                line.append(Node(x, y))
            self.mz.append(line)

    def generate_maze(self):
        random_x = random.randint(0, self.size_maze - 1)
        random_y = random.randint(0, self.size_maze - 1)
        start_point = self.mz[random_x][random_y]

        stack = [start_point]
        self.visited[start_point.x, start_point.y] = True
        self.parent[start_point.x, start_point.y] = start_point

        while len(stack) != 0:
            node = stack.pop()
            self.visited[node.x, node.y] = True

            self.maze_screen.after(
                3, self.remove_walls_between(
                    node, self.parent[node.x, node.y]
                )
            )
            self.maze_screen.update()

            neighbours = self.get_neighbours(node.x, node.y, False)

            if len(neighbours) != 0:
                shuffle(neighbours)

                for adj in neighbours:
                    self.parent[adj.x, adj.y] = node
                    stack.append(adj)

        self.draw_start_and_end_point()

    def get_neighbours(self, pos_x, pos_y, solve_maze):
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        all_neighbours = []

        for i in range(4):
            new_x = pos_x + x[i]
            new_y = pos_y + y[i]
            if (self.in_range(new_x, new_y)) and \
                    (self.visited[new_x, new_y] is False):
                # if we are trying to solve the maze
                # we'll also consider the walls
                if solve_maze:
                    if not is_wall(self.mz[pos_x][pos_y], x[i], y[i]):
                        all_neighbours.append(self.mz[new_x][new_y])
                else:
                    all_neighbours.append(self.mz[new_x][new_y])
        return all_neighbours

    def remove_walls_between(self, node1, node2):
        x0 = node1.y * self.step
        x1 = node1.x * self.step
        x2 = (node1.y + 1) * self.step
        x3 = (node1.x + 1) * self.step

        y0 = node2.y * self.step
        y1 = node2.x * self.step
        y2 = (node2.y + 1) * self.step
        y3 = (node2.x + 1) * self.step

        if node1.x - node2.x == 1:
            self.mz[node1.x][node1.y].top_wall = False
            self.mz[node2.x][node2.y].bottom_wall = False
            self.maze_screen.create_line(
                x0, x1, x2, x1, fill="RoyalBlue3", width=2
            )

        if node1.x - node2.x == -1:
            self.mz[node1.x][node1.y].bottom_wall = False
            self.mz[node2.x][node2.y].top_wall = False
            self.maze_screen.create_line(
                x0, x3, x2, x3, fill="RoyalBlue3", width=2
            )
        if node1.y - node2.y == 1:
            self.mz[node1.x][node1.y].left_wall = False
            self.mz[node2.x][node2.y].right_wall = False
            self.maze_screen.create_line(
                y2, y1, y2, y3, fill="RoyalBlue3", width=2
            )

        if node1.y - node2.y == -1:
            self.mz[node1.x][node1.y].right_wall = False
            self.mz[node2.x][node2.y].left_wall = False
            self.maze_screen.create_line(
                y0, y1, y0, y3, fill="RoyalBlue3", width=2
            )

    def draw_empty_maze(self):
        for x in range(0, self.width, self.step):
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

    def draw_start_and_end_point(self):
        x0 = 0 + int(self.step / 8)
        x1 = self.step - x0
        self.maze_screen.create_rectangle(x0, x0, x1, x1, fill="green")

        x2 = x0 + (self.width - self.step)
        x3 = self.width - x0
        self.maze_screen.create_rectangle(x2, x2, x3, x3, fill="blue")

    def draw_circle(self, node):
        return self.maze_screen.create_oval(
            (node.y * self.step) + int(self.step / 8),
            (node.x * self.step) + int(self.step / 8),
            ((node.y + 1) * self.step) - int(self.step / 8),
            ((node.x + 1) * self.step) - int(self.step / 8),
            fill="black"
        )

    def solve_maze(self):
        self.visited.clear()
        for x in range(self.size_maze):
            for y in range(self.size_maze):
                self.visited[x, y] = False

        start_point = self.mz[0][0]

        self.print_path_dfs(start_point)

    def delete_canvas(self, obj_id):
        self.maze_screen.delete(obj_id)
        self.maze_screen.update()

    def print_path_dfs(self, node):
        self.visited[node.x, node.y] = True

        if self.visited[self.size_maze - 1, self.size_maze - 1]:
            return

        # We don't want to draw the start node
        if node.x == 0 and node.y == 0:
            circle_id = None
        else:
            circle_id = self.draw_circle(node)
            self.maze_screen.update()
            time.sleep(0.08)

        neighbours = self.get_neighbours(node.x, node.y, True)

        if len(neighbours) != 0:
            for adj in neighbours:
                self.print_path_dfs(adj)

        # this avoids to delete the final path
        if not self.visited[self.size_maze - 1, self.size_maze - 1]:
            self.maze_screen.itemconfig(circle_id, fill='red')
            self.maze_screen.update()
            time.sleep(0.15)
            self.delete_canvas(circle_id)
