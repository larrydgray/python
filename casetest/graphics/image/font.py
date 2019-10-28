from PIL import Image, ImageDraw, ImageFont
import os, displaypil
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20,150),'Hello', fill='purple')
fontsFolder = 'fonts\\'
arielFont = ImageFont.truetype(os.path.join(fontsFolder,
    'arial.ttf'), 32)
draw.text((100,150), 'Howdy', fill='gray', font=arielFont)
displaypil.display(im)
