#import dependencies
from darkflow.net.build import TFNet
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import json

#for automatic frame capture, prints success for every frame recorded
#get frames from live rtsp feed , 3 frames per second, url can be configured
vidcap = cv2.VideoCapture("rtsp://admin:admin123@49.124.35.175:1234/cam/realmonitor?channel=1&subtype=0");
success,image = vidcap.read()
count = 0
success = True

while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count%5 == 0 :
         cv2.imwrite('frames%d.jpg'%count,image)
         print('success')
    count+=1
    
#setting path of folder with input images, 
#can be configured for your own path/folder
mypath='/home/idham/darkflow-trial/image/image2'

#loading multiple frames into yolo model
options = {"model": "cfg/tiny-yolo-voc.cfg", 
            "load": "tiny-yolo-voc.weights", 
            "threshold": 0.1}

tfnet = TFNet(options)

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
count = 0    
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    result = tfnet.return_predict(images[n])
    for r in result:
        
        if (r['label']) == 'car':
            cv2.imwrite('aimg%d.jpg'%count, images[n])
        else:
                print('')
        
        count+=1 
