
from PIL import Image, ImageFilter
import sys
import os

#grab first and second arg
exist_directory = string(sys.argv[1])

new_directory = string(sys.argv[2])

# Check if new/ arg exists, if not create

if os.path.exists(new_directory) == False:
    os.mkdir(new_directory, mode=0o777, *, dir_fd=None)

# loop through pokedex 
# convert images to png
# save to the new folder
'''
for i in exist_directory:
    im.save("./images/crooked_greyscale.png", 'png')



im = Image.open("./images/*.jpg")

print(im.size, im.mode)


#im.save("./images/crooked_greyscale.png", 'png')
#crooked_im.show()
'''