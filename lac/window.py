from tkinter import *

game_window = Tk()

#setting the menu for the game
game_menu = Menu(game_window)


# Name of the video game in the title bar
game_window.title("Video Game Name Here")

file_menu = Menu(game_menu, tearoff = 0)
file_menu.add_command(label="New", command = donothing)









game_window.configure(width=1000, height=750)

game_window.mainloop()
