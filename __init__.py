from tkinter import *

my_window = Tk()
maze_screen = Canvas(my_window, width=500, height=380,background='red')
menu_screen = Canvas(my_window, width=500, height=120,background='black')

maze_screen.grid(row=0,column=0)
menu_screen.grid(row=1,column=0)

my_window.mainloop()