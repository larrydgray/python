from PIL import Image
purpleImage = Image.open('purpleImage.png')
purpleImage.rotate(90,expand=True).save('purpleImage90.png')
purpleImage.rotate(180).save('purpleImage180.png')
purpleImage.rotate(270,expand=True).save('purpleImage270.png')
purpleImage.rotate(6).save('purpleImage6.png')
purpleImage.rotate(6, expand=True).save('purpleImage6_exanded.png')
purpleImage.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
purpleImage.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')


