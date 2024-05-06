
from PIL import Image, ImageFilter
im = Image.open("./images/pikachu.jpg")

print(im.format, im.size, im.mode)
#im.show()

#out = im.filter(ImageFilter.BLUR)
#out.save("./images/blur.png", 'png')

#out = im.filter(ImageFilter.SHARPEN)
#out.save("./images/sharpen.png", 'png')

out = im.convert('L')
out.save("./images/grey_scale.png", 'png')