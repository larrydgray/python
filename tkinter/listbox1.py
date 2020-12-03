
# Python program demonstrating
# Multiple selection in Listbox widget


from tkinter import *

window = Tk()
window.geometry('100x150')

# Choosing selectmode as multiple
# for selecting multiple options
list = Listbox(window, selectmode = "multiple")

# Widget expands horizontally and
# vertically by assigning both to
# fill option
list.pack(expand = YES, fill = "both")

# Taking a list 'x' with the items
# as languages
x = ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby", "JavaScript", "Swift"]

for each_item in range(len(x)):

    list.insert(END, x[each_item])

    # coloring alternative lines of listbox
    list.itemconfig(each_item,
                    bg = "yellow" if each_item % 2 == 0 else "cyan")

window.mainloop()
