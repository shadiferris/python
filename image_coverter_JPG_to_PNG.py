
from PIL import Image, ImageFilter
import sys
import os


#grab first and second arg
exist_directory = sys.argv[1]

new_directory = sys.argv[2]

print(exist_directory , new_directory)

# Check if new/ arg exists, if not create

if os.path.exists(new_directory) == False:
    print(f"directory {new_directory} doesnt exist, will attempte to create the directory now!!")
    os.mkdir(new_directory, mode=0o777, dir_fd=None)
else:
    print("directory exists")

def check_dir():
    if os.path.exists(new_directory) == True:
        print("Directory created successfully!")
    else:
        print("directory failed to create, something went wrong")
        
check_dir()

# loop through pokedex 
# convert images to png
# save to the new folder

for filename in os.listdir(exist_directory):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{exist_directory}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{new_directory}/{clean_name}.png', 'png')
  print('all done!!')


