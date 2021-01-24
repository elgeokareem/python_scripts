from os import listdir
from PIL import Image

path = r"C:\Users\William\Pictures"
new_size = 300 # pixels

image_files = [file for file in listdir(path) if file.endswith(("png", "jpg", "jpeg"))]

for image_name in image_files:
  image_path = fr"{path}\{image_name}"
  new_image = Image.open(image_path)
  proportion = new_image.size[1] / new_image.size[0]
  new_image = new_image.resize((new_size, int(proportion * new_size)), Image.ANTIALIAS)

  destination = path + "/" + image_name.split(".")[0] + "_resized" + ".jpg"
  new_image.save(destination, format="jpeg", optimize=True, quality=95)
