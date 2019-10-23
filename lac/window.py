from tkinter import *


#Will soon have to create these for the menu options, for now just letting them do nothing
def donothing():
        filewin = Toplevel(game_window)
        button = Button(filewin, text="Do Nothing Button")
        button.pack()


game_window = Tk()
game_window.configure(width=1000, height=750)

#setting the menu for the game
game_menu = Menu(game_window)

# Name of the video game in the title bar
game_window.title("Video Game Name Here")

#creating the menu items
file_menu = Menu(game_menu, tearoff = 0)
file_menu.add_command(label= "New", command = donothing)
file_menu.add_command(label= "Open", command = donothing)
file_menu.add_command(label= "Save", command = donothing)
file_menu.add_command(label= "Save As", command = donothing)
file_menu.add_separator()



file_menu.add_command( label= "Exit", command = game_window.quit)
game_menu.add_cascade(label = "File", menu = file_menu)
edit_menu = Menu(game_menu, tearoff = 0)
edit_menu.add_command(label = "Undo", command = donothing)

edit_menu.add_separator()

edit_menu.add_command(label = "Cut", command = donothing)
edit_menu.add_command(label = "Copy", command = donothing)
edit_menu.add_command(label = "Paste", command = donothing)
edit_menu.add_command(label = "Delete", command = donothing)
edit_menu.add_command(label = "Select All", command = donothing)

#game_menu.add_cascade(label = "Edit", menu = edit_menu)
#help_menu = Menu(game_menu, tearoff = 0)
#help_menu.add_command(label = "Help Index", command = donothing)
#help_menu.add_command(label = "About", command = donothing)
#help_menu.add_command(label = "Help", command = donothing)


game_window.config(menu = game_menu)
game_window.mainloop()
