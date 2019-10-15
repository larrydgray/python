from tkinter import *
root = Tk()
root.title('Variations in line options')
cw=500
ch=200
canvas_1 = Canvas(root, width=cw, height=ch, background="pink")
canvas_1.grid(row=0,column=1)

x_start = 10
y_start = 10
x_end = 400
y_end = 20
canvas_1.create_line(x_start, y_start, x_end, y_end, dash=(3,5), width = 3)

x_start = x_end
y_start = y_end
x_end = 10
y_end = 180
canvas_1.create_line(x_start,y_start, x_end, y_end, dash=(9,), width = 5, fill="red")

y_end=150
canvas_1.create_line(x_start,y_start, x_end, y_end, dash=(19,),width = 10, fill="yellow")

y_start=0
canvas_1.create_line(x_start,y_start,x_end,y_end)

root.mainloop()
