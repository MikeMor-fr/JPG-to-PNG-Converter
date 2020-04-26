# project 1 : convert jpeg to png

import sys
import os
from PIL import Image

# grab first and second argument
# check if new exist, if note, create it
# loop through pokedex : convert jpg to png
# save to the new folder

path = sys.argv[2]
try:
    os.mkdir(path)
except OSError:
    print (f"Creation of the directory {path} failed\nAlready exist in {os.getcwd()}\nDelete it or change the name.")
else:
    print (f"Successfully created the directory {path}")


for filename in os.listdir(sys.argv[1]):
    if filename.endswith(".jpg"):
    	(file, ext) = os.path.splitext(filename)
    	img = Image.open(f"./{sys.argv[1]}/{filename}")
    	img.save(f"./{sys.argv[2]}/{file}.png", "png")

print("Success for converting")