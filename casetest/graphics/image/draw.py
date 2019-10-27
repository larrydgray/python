from PIL import Image, ImageDraw
import displaypil
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(5,5),(199,5),(199,199),(5,199),
    (5,5)], fill='black')
draw.rectangle((20,30,60,60), fill='blue')
draw.ellipse((120,30,160,60), fill='red')
draw.polygon(((57,87),(79,62),(94,85),
    (120,90),(103,113)), fill='brown')
for i in range(100,200,10):
    draw.line([(i,5),(200,i-100+5)],fill='green')
displaypil.display(im)