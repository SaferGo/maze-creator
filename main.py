from tkinter import Canvas, Button, StringVar, LEFT, RIGHT, OptionMenu, Tk
from generate_maze import *


class Window:
    def __init__(self, master, width, height):
        self.app = master
        self.width = width
        self.height = height
        self.maze_screen = None
        self.generate_button = None
        self.algorithm_button = None
        self.algorithm = None

        self.app.resizable(False, False)

        self.app.title('Maze generator')

        self.create_maze_screen()
        self.create_buttons()

    def create_maze_screen(self):
        self.maze_screen = Canvas(
            self.app, width=self.width,
            height=self.height, background='RoyalBlue3'
        )
        self.maze_screen.pack(fill="both", expand=True)

    def create_buttons(self):
        self.generate_button = Button(
            self.app, text='Generate maze!', command=self.draw_maze)
        self.generate_button.pack(side=LEFT)

        self.algorithm = StringVar(self.app)
        self.algorithm.set("DFS")  # default

        self.algorithm_button = OptionMenu(
            self.app, self.algorithm, "DFS", "M. Spanning Tree")
        self.algorithm_button.pack(side=RIGHT)

    # def get_selected_algorithm(self, _=None):
    #    print(self.algorithm.get())

    def draw_maze(self):
        self.generate_button.config(state='disabled')
        self.maze_screen.delete("all")
        m = Maze(20, self.maze_screen, self.width)
        self.generate_button.config(state='normal')
        m.solve_maze()


if __name__ == "__main__":
    app = Tk()
    window = Window(app, 700, 700)
    app.mainloop()
