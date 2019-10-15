from tkinter import *
root = Tk()
root.title('ROUND end aps on lines')
cw=450
ch=130
canvas_1 = Canvas(root, width=cw, height=ch)
canvas_1.grid(row=0,column=1)

x_start = 30
y_start = 20
x_end = 400
y_end = 20
canvas_1.create_line(x_start, y_start, x_end, y_end, capstyle=ROUND, width = 1)
canvas_1.create_line(x_start, y_start+10, x_end, y_end+10, capstyle=ROUND, width = 4)
canvas_1.create_line(x_start, y_start+20, x_end, y_end+20, capstyle=ROUND, width = 8)
canvas_1.create_line(x_start, y_start+36, x_end, y_end+36, capstyle=ROUND, width = 16)
canvas_1.create_line(x_start, y_start+66, x_end, y_end+66, capstyle=ROUND, width = 32)


root.mainloop()
