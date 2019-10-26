from PIL import Image
purpleImage = Image.open('purpleImage.png')

width, height = purpleImage.size
# quarter size
quartersizedIm = purpleImage.resize((int(width/2),int(height/2)))
quartersizedIm.save('quarderSizedPurple.png')
# stretch taller
svelteIm = purpleImage.resize((width,height+300))
svelteIm.save('svelte.png')
