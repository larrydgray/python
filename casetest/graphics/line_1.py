from tkinter import *
root=Tk()
root.title('A Line')
canvas_1=Canvas(root,width=200,height=200)
canvas_1.grid(row=0, column=1)

canvas_1.create_line(10,20,50,100)

root.mainloop()
