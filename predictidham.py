
import os
from darkflow.net.build import TFNet
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import time

timestr = time.time()

#setting path of folder with input images,
#can be configured for your own path/folder
mypath='/home/tapway-office/darkflow-master/frames-car'
source='/home/tapway-office/darkflow-master/frames-idham'
#loading multiple frames into tiny-yolo-voc model, model can be configured
options = {"model": "cfg/tiny-yolo-voc.cfg",
            "load": "tiny-yolo-voc.weights",
            "threshold": 0.25}

tfnet = TFNet(options)

onlyfiles = [ f for f in listdir(source) if isfile(join(source,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
success = True

count = 0
for n in range(0, len(onlyfiles)):

    images[n] = cv2.imread( join(source,onlyfiles[n]) )
    result = tfnet.return_predict(images[n])
    for r in result:

        if (r['label']) == 'car':
            cv2.imwrite(os.path.join(mypath, 'framee%d.jpg' %timestr), images[n])
            print('car')
            print(count)
        timestr+=1
        count+=1
