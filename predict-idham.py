import os
from darkflow.net.build import TFNet
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import shutil

#setting path of folder with input images,
#can be configured for your own path/folder
mypath='/home/darkflow-master/frames-idham'
source = os.listdir("/home/darkflow-master/")
destination = "/home/darkflow-master/frames-car/"

for files in source:
    if files.endswith(".jpg"):
        shutil.move(files,destination)

#loading multiple frames into tiny-yolo-voc model, model can be configured
options = {"model": "cfg/tiny-yolo-voc.cfg",
            "load": "tiny-yolo-voc.weights",
            "threshold": 0.1}

tfnet = TFNet(options)

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
success = True

for n in range(0, len(onlyfiles)):

    count = 5
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    result = tfnet.return_predict(images[n])
    for r in result:

        if (r['label']) == 'car':
            cv2.imwrite('frame%d.jpg'%count, images[n])
            for files in source:
                if files.endswith(".jpg"):
                    shutil.move(files, destination)

        else:
            cv2.imwrite('blank.jpg', images[n])


        count+=1
