
# Usage example:  python3 object_detection_yolo.py --video=run.mp4
#                 python3 object_detection_yolo.py --image=bird.jpg

import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
import shutil


lp=False
confThreshold = 0.5  
nmsThreshold = 0.4  
inpWidth = 416  
inpHeight = 416 

parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
parser.add_argument('--path', help='Path of files')
args = parser.parse_args()
files=os.listdir(args.path)
classesFile = "classes.names";

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

modelConfiguration = "darknet-yolov3.cfg";
modelWeights = "lapi.weights";

net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def drawPred(classId, conf, left, top, right, bottom):
    cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)

    label = '%.2f' % conf
    lp=False
    if classes:
    	assert(classId < len(classes))
    	label = '%s:%s' % (classes[classId], label)

    
    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (0, 0, 255), cv.FILLED)
    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)


def postprocess(frame, outs,lp,left,top,width,height):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIds = []
    confidences = []
    boxes = []
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        print("out.shape : ", out.shape)
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if detection[4]>confThreshold:
            	lp=True
            	print(lp)
            	print(detection[4], " - ", scores[classId], " - th : ", confThreshold)
            	print(detection)
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                
                boxes.append([left, top, width, height])
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    return [lp,left,top,width,height]

winName = 'Deep learning object detection in OpenCV'
if os.path.exists(args.path+'/plates'):
	try:
		print('[info]Already exist.. clearing data..')
		print('[info] creating output file...')
		shutil.rmtree(args.path+'/plates')
	except:
		print('some error occurs')

cv.namedWindow(winName, cv.WINDOW_NORMAL)
os.mkdir(args.path+'/plates')
for file in files:
	lp=False
	if (file):
		cap = cv.VideoCapture(args.path+'/'+file)

		outputFile = args.path+'/plates/'+file[:-4]+'_yolo_out_py.jpg'
	while cv.waitKey(1) < 0:
		hasFrame, frame = cap.read()
		if not hasFrame:
			print("Done processing !!!")
			
			cv.waitKey(3000)
			break
		blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)
		net.setInput(blob)
		outs = net.forward(getOutputsNames(net))
		res=postprocess(frame, outs,lp,0,0,0,0)
		res=list(res)
		t, _ = net.getPerfProfile()
		label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
		if (res[0]):
			print("Output file is stored as ", outputFile)
			frame=frame[res[2]:res[2]+res[4],res[1]:res[1]+res[3]]
			cv.imwrite(outputFile, frame.astype(np.uint8));
		
