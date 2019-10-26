from PIL import Image
mapIm = Image.open('map.png')
print(mapIm.size)
width, height = mapIm.size
print('Width = '+str(width))
print('Height = '+str(height))
print('Filename = '+mapIm.filename)
print('Format = '+mapIm.format)
print(mapIm.format_description)
print('Saving a copy as jpg...')
# can save as gif, jpg or png
mapIm.save('map.jpg')
print('Done.')
