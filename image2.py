
from PIL import Image, ImageFilter
im = Image.open("./images/astro.jpg")

print(im.size, im.mode)

#(width, height) = (im.width // 2, im.height // 2)
im_resized = im.resize((400, 400))

im_resized.save("./images/resize_im.png", 'png')
im_resized.show()