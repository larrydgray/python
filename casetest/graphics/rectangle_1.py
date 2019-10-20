from tkinter import *
root = Tk()
root.title('Overlapping Rectangles')
cw=260
ch=180
canvas_1 = Canvas(root, width=cw, height=ch, background="turquoise")
canvas_1.grid(row=0,column=1)

x1 = 10
y1 = 30
xw = 70
yh = 90


kula="darkblue"
canvas_1.create_rectangle(x1,y1,\
                          x1+xw,y1+yh,\
                          fill=kula)
x1=30
y1=50
kula="darkred"
canvas_1.create_rectangle(x1,y1,\
                          x1+xw,y1+yh,\
                          fill=kula)
x1=50
y1=70
kula="darkgreen"
canvas_1.create_rectangle(x1,y1,\
                          x1+xw,y1+yh,\
                          fill=kula)
root.mainloop()
