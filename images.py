from PIL import Image, ImageFilter

#---------PART 1------------------------

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR) #filters used : BLUR, SMOOTH, SHARPEN
filtered_img.save("blur.png", "png") # png support those kind of filters

filtered_im = img.convert('L') # 'L' for grayscale
filtered_im.save("grey.png", "png")

#---------PART 2------------------------

#filtered_im.show()
crooked = filtered_im.rotate(90)
crooked.save("rotate.png", "png")

resize = filtered_im.resize((300,300))
resize.save("resize.png", "png")

box = (100, 100, 400, 400)
region = filtered_im.crop(box)
region.save("crop.png", "png")

#---------PART 3-------------------------

img2 = Image.open('./astro.jpg')
img2.thumbnail((400,400)) # thumbnaim method instead of resize for keeping image ratio
img2.save("thumbnail.jpg") # thumbnail method doesn't create a new image, but modify the current one

