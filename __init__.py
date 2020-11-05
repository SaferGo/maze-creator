from tkinter import *
from generate_maze import *

my_window = Tk()
my_window.title('Maze generator')
maze_screen = Canvas(my_window, width=500, height=380, background='red')
menu_screen = Canvas(my_window, width=500, height=120, background='black')

maze_screen.pack(fill="both", expand=True)
menu_screen.pack(fill="both", expand=True)


# maze_screen.grid(row=0, column=0)
# menu_screen.grid(row=1, column=0)


def draw_maze():
    m = Maze(10)


def draw_empty_maze(canvas, line_distance, w, h):
    for x in range(line_distance, w, line_distance):
        canvas.create_line(x, 0, x, h, fill="#476042")


generate_button = Button(my_window, text='Generate maze!', command=draw_maze)
generate_button.pack(side=LEFT)


def draw_maze(event):
    maze_screen.delete("all")
    size_step_w = int(event.width / 4)
    size_step_h = int(event.height / 4)
    for x in range(size_step_w, event.width, size_step_w):
        maze_screen.create_line(x, 0, x, event.height, fill="#476042")
    for x in range(size_step_h, event.height, size_step_h):
        maze_screen.create_line(0, x, event.width, x, fill="#476042")


maze_screen.bind("<Configure>", draw_maze)
draw_empty_maze(maze_screen, 10, maze_screen.winfo_width(), maze_screen.winfo_height())

my_window.mainloop()
