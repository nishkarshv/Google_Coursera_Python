
########################To update image files 
#!/usr/bin/env python3

import os
import sys
from PIL import Image
import PIL
imagesfolder = '/home/student-00-16724ec8d1a3/supplier-data/images/'
outputfolder = '/home/student-00-16724ec8d1a3/supplier-data/images/'
for filename in os.listdir(imagesfolder):
    outfile = outputfolder+filename
    try:

        if filename.endswith("tiff"):

            image_path = os.path.join(imagesfolder, filename)
            with Image.open(image_path) as im:
                print(im.resize((600,400)).convert("RGB"))
                print(outfile)
                out = os.path.splitext(outfile)[0]+".jpeg"
                print(out)
                im.resize((600,400)).convert("RGB").save(out,"JPEG")
    except PIL.UnidentifiedImageError:
        pass


student-01-72557e2aabe5@linux-instance:~$ cat ~/example_upload.py
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})