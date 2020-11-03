from tkinter import *
from generate_maze import *

my_window = Tk()
my_window.title('Maze generator')
maze_screen = Canvas(my_window, width=500, height=380,background='red')
menu_screen = Canvas(my_window, width=500, height=120,background='black')

maze_screen.grid(row=0,column=0)
menu_screen.grid(row=1,column=0)

def draw_maze():
    m = Maze(2)
    print("hi!")

generate_button = Button(my_window, text = 'Generate maze!',command = draw_maze)
generate_button.grid(row=1,column=0)


my_window.mainloop()