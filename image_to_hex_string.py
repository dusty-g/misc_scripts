# Converts image to string of hexadecimal numbers separated by spaces with linebreaks between rows.
# I used this to create sprites (16x16) for Microsoft MakeCode Arcade. There's probably better ways to do this.

# import Image library
from PIL import Image

# create palette
palette = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# prompt user for image file location
imgName = input("Enter image file name: ")

# open image
img = Image.open(imgName)

# prompt user for image size
size = input("Enter image size (width, height): ")

# convert size to tuple
size = tuple(map(int, size.split(",")))

img.thumbnail(size, Image.ANTIALIAS)

# convert image to 16 color int sprite
img = img.convert("P", palette=Image.ADAPTIVE, colors=16)
# set palette
img.putpalette(palette)
# save image
img.save("sprite.png")
# convert image to string of individual pixels represented as integers separated by commas and a line break every width pixels
img = img.tobytes()
imgString = ""
for i in range(len(img)):
    if i % size[0] == 0:
        imgString += "\n"
    imgString += str(img[i]) + " "




# convert to base 16 (10 = a, 11 = b, 12 = c, 13 = d, 14 = e, 15 = f)
imgString = imgString.replace("10", "a")
imgString = imgString.replace("11", "b")
imgString = imgString.replace("12", "c")
imgString = imgString.replace("13", "d")
imgString = imgString.replace("14", "e")
imgString = imgString.replace("15", "f")

# save image as text file
with open("converted_image.txt", "w") as f:
    f.write(imgString)
