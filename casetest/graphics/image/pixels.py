from PIL import Image, ImageColor
import random
im=Image.new('RGBA',(200,200),'black')
random.seed()

y=0
z=0
orgx=50
orgy=150
grid=10
red=ImageColor.getcolor('red','RGBA')
for i in range(0,200):
    for x in range(0,50):
        x2d=orgx+x+z
        y2d=orgy-y+z
        plot=False
        if x%grid==0:
            plot=True
        if y%grid==0:
            plot=True
        if z%grid==0:
            plot=True
        if plot:
            im.putpixel((x2d,y2d),red)
    zrand = random.randint(1,2)
    yrand = random.randint(1,5)
    if yrand!=1:
        y+=1
    if zrand==1:
        z=z-1
    else:
        z=z+1
im.save('graphics.png')
