import os
import cv2 as cv
import imutils
import numpy as np
import pytesseract
import argparse
import sys
import MySQLdb as mdb 
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
parser.add_argument('--path', help='Path of files')
args = parser.parse_args()
plates=os.listdir(args.path)
p=("plates",)

for num in plates:
	cap = cv.VideoCapture(args.path+'/'+num)
	hasFrame, img = cap.read()
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	img = cv.bilateralFilter(img, 10,16,16) 
	text=pytesseract.image_to_string(img,lang='eng') #converts image characters to string
	#-----postprocessing----
	text=text.lower()
	res=''
	for c in text:
		
		if c in "abcdefghijklmnopqrstuvwxyz1234567890":

			res=res+c
	if(len(res)==7):
		p+=(res,)

	
DBNAME="ate"
DBHOST="localhost"
DBPASS=""
DBUSER="root"

try:
	db=mdb.connect(DBHOST,DBUSER,DBPASS,DBNAME)
	print("--> Database connected sucessfully <--")
	cursor=db.cursor()
	for i in range(1,len(p)):
		sql="INSERT INTO `currentvoilator`(`p_number`) VALUES ('"+p[i]+"')"
		try:
			cursor.execute(sql)
		except:
			print("repeated number plate entry")

except:
	print("---> Database connection failed <---")

db.close()
print("---> Database connection closed <---")

