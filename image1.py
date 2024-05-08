
from PIL import Image, ImageFilter
im = Image.open("./images/pikachu.jpg")

print(im.format, im.size, im.mode)
#im.show()

#out = im.filter(ImageFilter.BLUR)
#out.save("./images/blur.png", 'png')

#out = im.filter(ImageFilter.SHARPEN)
#out.save("./images/sharpen.png", 'png')

#out = im.convert('L')
#out.save("./images/grey_scale.png", 'png')

#im.show()
#out = im.convert('L')
#crooked_im = out.rotate(90)
#crooked_im.save("./images/crooked_greyscale.png", 'png')
#crooked_im.show()

#box = (100, 100, 400, 400)
#cropped_im = im.crop(box)
#cropped_im.save("./images/cropped_im.png", 'png')
#cropped_im.show()



