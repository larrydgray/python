from tkinter import *
root = Tk()
root.title('A Rectangle')
cw=200
ch=200
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0,column=1)



x1 = 30
y1 = 30

x2 = 200
y2 = 130



canvas_1.create_rectangle(x1,y1,x2,y2)

root.mainloop()
