from tkinter import *
import PIL
from PIL import Image, ImageTk

def displaypil(pilimage):
    root = Tk()
    root.title('Display Pillow Image')
    width, height = pilimage.size
    #root.geometry('{}x{}'.format(width,height))
    canvas = Canvas(root,width=width,height=height)
    canvas.pack()
    image = ImageTk.PhotoImage(pilimage)
    imagesprite = canvas.create_image(width/2,height/2,image=image)
    root.mainloop()

pilImage = Image.open("map.png")
displaypil(pilImage)