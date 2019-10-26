from PIL import Image
purpleImage = Image.open('purpleImage.png')
width, height = purpleImage.size
newImage = purpleImage.crop((20,20,width-20,height-20))
newImage.save('purpleCropped.png')
