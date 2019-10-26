from tkinter import *
import PIL
from PIL import Image, ImageTk
root = Tk()
root.title('Display Pillow Image')
root.geometry('1000x1000')
canvas = Canvas(root,width=999,height=999)
canvas.pack()
pilImage = Image.open("map.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
root.mainloop()