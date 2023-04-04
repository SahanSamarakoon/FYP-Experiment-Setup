import glob
from PIL import Image

for filename in glob.glob('pics/*.jpg'):
    # check some condition for the file
    if True:
        with Image.open(filename) as img:
            # do something with the image
            img.show()