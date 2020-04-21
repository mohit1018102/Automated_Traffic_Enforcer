  
import cv2
import os
import shutil
import numpy as np

cv2

cap = cv2.VideoCapture('../input/video7.avi') 
print("[info] creating output file...")
if os.path.exists('../output/video'):
    try:
        print('[info]Already exist.. clearing data..')
        print('[info] creating output file...')
        shutil.rmtree('../output/video')
    except:
        print('some error occurs')

print('[info] loading classifier cars.xml')       
car_cascade = cv2.CascadeClassifier('../classifier/cars.xml')

os.mkdir('../output/video')


 
print('[info] Taking image of cars')
while True:  
    ret, frames = cap.read()  
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
    x=1
    color=(0,0,255)
    
    cv2.rectangle(frames,(25,25),(25+50,25+50),(0,0,255),-1)
    for (x,y,w,h) in cars:
    	frames=cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),1)
    	f2=frames[y:y+h, x:x+h]
    	cv2.imwrite("{}.jpg".format("../output/video/"+str(x)),f2)
    	x=x+1
  
   # Display frames in a window  
    cv2.imshow('video2', frames) 
      
    # Wait for Esc key to stop 
    if cv2.waitKey(33) == 27: 
        break
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 