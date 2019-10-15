from tkinter import *
root=Tk()
root.title('Dashed lines')

cw=500
ch=200
canvas_1=Canvas(root, width=cw, height=ch)
canvas_1.grid(row=0,columns=1)

x_start=10
y_start=20
x_end=400
y_end=20

canvas_1.create_line(x_start,y_start,x_end,y_end,dash=(1,11), width=3)
y_end+=40
canvas_1.create_line(x_start,y_start+4,x_end,y_end+4,dash=(2,10), width=4)
y_end+=40
canvas_1.create_line(x_start,y_start+8,x_end,y_end+8,dash=(4,8), width=5)

root.mainloop()
