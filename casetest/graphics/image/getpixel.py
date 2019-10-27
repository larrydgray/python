from PIL import Image, ImageColor
import sys, os
xpos=int(sys.argv[1])
ypos=int(sys.argv[2])
white=ImageColor.getcolor('white','RGBA')
white=(white[0],white[1],white[2])
print(white)
charset = Image.open("c64-2.png")
while True:
    for y in range(0,8):
        for x in range(0,8):
            pix=charset.getpixel((xpos+x,ypos+y))
            #print(pix)
            if pix!=white:
                print('*',end='')
            else:
                print(' ',end='')

        print('')
    i=input()
    if i=='r':
        xpos+=1
    if i=='l':
        xpos-=1
    if i=='u':
        ypos-=1
    if i=='d':
        ypos+=1
    if i=='q':
        break
    os.system('cls')
