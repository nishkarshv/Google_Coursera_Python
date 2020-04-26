##############run.py#####for REST calls
#! /usr/bin/env python3
import os
import requests
descfolder = '/home/student-01-72557e2aabe5/supplier-data/descriptions/'
imagefolder = '/home/student-01-72557e2aabe5/supplier-data/images/'
imagelist = []
url = 'http://104.154.75.19/fruits/'
for files in os.listdir(descfolder):

    filename = descfolder + files
    with open(filename, 'r') as f:
        reads = f.readlines()
    image_name = imagefolder+ files.split(".")[0]+".jpeg"
    name = reads[0].strip()
    weight = reads[1].strip().split(" ")[0]
    desc = reads[2].strip()
    imagedict = {"name":name, "weight":weight, "description":desc, "image_name":image_name}
    imagelist.append(imagedict)
print(imagelist)
for imagedata in imagelist:
    x = requests.post(url, data=imagedata)
    #print(x)
    if x.status_code == 201:
        pass
    else:
        print("Failed")