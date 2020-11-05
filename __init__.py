from tkinter import *
from generate_maze import *

my_window = Tk()
my_window.title('Maze generator')
maze_screen = Canvas(my_window, width=500, height=380, background='red')
menu_screen = Canvas(my_window, width=500, height=120, background='black')

maze_screen.pack(fill="both", expand=True)
menu_screen.pack(fill="both", expand=True)

m = Maze(20)


def create_maze():
    print("maze!")


generate_button = Button(my_window, text='Generate maze!', command=create_maze)
generate_button.pack(side=LEFT)


def draw_maze(event):
    maze_screen.delete("all")
    size_step_w = int(event.width / 20)
    size_step_h = int(event.height / 20)
    # x, y, x y
    for x in range(20):
        for y in range(20):
            print("--------------------------")
            print("Pos: ", x, y)
            node = m.mz[x][y]
            if node.top_wall:
                print("Top")
                maze_screen.create_line(y * size_step_w, x * size_step_h, (y + 1) * size_step_w, x * size_step_h)
            if node.bottom_wall:
                print("Bottom")
                maze_screen.create_line(y * size_step_w, (x + 1) * size_step_h, (y + 1) * size_step_w, (x + 1) * size_step_h)
            if node.right_wall:
                print("Right!")
                maze_screen.create_line((y + 1) * size_step_w, x * size_step_h, (y + 1) * size_step_w, (x + 1) * size_step_h)
            if node.left_wall:
                print("Left!")


maze_screen.bind("<Configure>", draw_maze)

my_window.mainloop()
