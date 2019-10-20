from tkinter import *
root = Tk()
root.title('Concentric Squares')

cw=200
ch=400


canvas_1=Canvas(root, width=cw, height=200, background="green")
canvas_1.grid(row=0, column=1)

x_center =100
y_center =100
x_width  =100
y_height =100
kula = "darkblue"

canvas_1.create_rectangle(x_center-x_width/2,y_center-y_height/2,
                          x_center+x_width/2,y_center+y_height/2, fill=kula)

x_width  =80
y_height =80
kula = "darkred"

canvas_1.create_rectangle(x_center-x_width/2,y_center-y_height/2,
                          x_center+x_width/2,y_center+y_height/2, fill=kula)

x_width  =60
y_height =60
kula = "darkgreen"

canvas_1.create_rectangle(x_center-x_width/2,y_center-y_height/2,
                          x_center+x_width/2,y_center+y_height/2, fill=kula)

root.mainloop()

