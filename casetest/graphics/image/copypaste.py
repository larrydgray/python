from PIL import Image
purpleImage = Image.open('purpleImage.png')
transparentImage = Image.open('transparentImage2.png')
#white background
purpleImage.paste(transparentImage,(20,20))
#transparent background
purpleImage.paste(transparentImage,(80,80),transparentImage)
purpleImage.save('copypaste.png')
