from tkinter import *
from generate_maze import *

my_window = Tk()
my_window.title('Maze generator')
maze_screen = Canvas(my_window, width=500, height=380, background='red')
menu_screen = Canvas(my_window, width=500, height=120, background='black')

maze_screen.pack(fill="both", expand=True)
menu_screen.pack(fill="both", expand=True)

m = Maze(6)


def create_maze():
    print("maze!")


generate_button = Button(my_window, text='Generate maze!', command=create_maze)
generate_button.pack(side=LEFT)


def draw_maze(event):
    print("----------------------------")
    maze_screen.delete("all")
    size_step_w = int(event.width / 6)
    size_step_h = int(event.height / 6)
    #maze_screen.create_line(5 * size_step_h, 0, 5 * size_step_h, size_step_h)
    #maze_screen.create_line(0, 5 * size_step_h, size_step_h, 5 * size_step_h)
    # x, y, x y
    for x in range(6):
        for y in range(6):
            print("--------------------------")
            print("Pos: ", x, y)
            node = m.mz[x][y]
            if node.top_wall:
                print("Top")
                maze_screen.create_line(x * size_step_w, y * size_step_h, 2 * x * size_step_w, y * size_step_h)
            if node.bottom_wall:
                print("Bottom")
                maze_screen.create_line(x * size_step_w, (y + 1) * size_step_h, (x + 1) * size_step_w, (y + 1) * size_step_h)
            if node.right_wall:
                print("Right!")
                maze_screen.create_line(x * size_step_w, y * size_step_h, x * size_step_w, (y + 1) * size_step_h)
            if node.left_wall:
                print("Left!")

    # for x in range(size_step_w, event.width, size_step_w):
    #    maze_screen.create_line(x, 0, x, event.height, fill="#476042")
    # for x in range(size_step_h, event.height, size_step_h):
    #    maze_screen.create_line(0, x, event.width, x, fill="#476042")


maze_screen.bind("<Configure>", draw_maze)

my_window.mainloop()
