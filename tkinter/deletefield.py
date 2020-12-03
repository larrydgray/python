from tkinter import *

def delete():
    myentry.delete(0, END)

root = Tk()
root.geometry('180x120')

myentry = Entry(root, width = 20)
myentry.pack(pady = 5)

mybutton = Button(root, text = "Delete", command = delete)
mybutton.pack(pady = 5)

root.mainloop()