
###########Convert image form the folder###########
import os
import sys
from PIL import Image
import PIL
imagesfolder = '/home/student-02-918b689eed46/images'
outputfolder = '/opt/icons/'
size = (128,128)
for filename in os.listdir(imagesfolder):
    outfile = outputfolder+filename
    try:
        image_path = os.path.join(imagesfolder, filename)
        with Image.open(image_path) as im:
            im.rotate(-90).resize((128,128)).convert("RGB").save(outfile,"jpeg")
    except PIL.UnidentifiedImageError:
        pass