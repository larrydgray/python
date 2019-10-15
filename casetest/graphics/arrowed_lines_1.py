from tkinter import *
root = Tk()
root.title('Arrows on lines')
cw=450
ch=200
canvas_1 = Canvas(root, width=cw, height=ch)
canvas_1.grid(row=0,column=1)

x_start = 20
y_start = 30
x_end = 400
y_end = 20
canvas_1.create_line(x_start, y_start, x_end, y_end, arrow="first", width = 1)
canvas_1.create_line(x_start, y_start+20, x_end, y_end+20, arrow="last", width = 4)
canvas_1.create_line(x_start, y_start+60, x_end, y_end+60, arrow="both", width = 1)
canvas_1.create_line(x_start, y_start+80, x_end, y_end+80, arrow="both", width = 8)
canvas_1.create_line(x_start, y_start+110, x_end, y_end+110, arrow="both", width = 16)
canvas_1.create_line(x_start, y_start+150, x_end, y_end+150, arrow="both", width = 32)


root.mainloop()
