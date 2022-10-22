# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2
from cv2 import VideoCapture
from cv2 import circle
import numpy as np
import os
import re
from os.path import isfile, join



# capture frames from a video
cap = cv2.VideoCapture(0)

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

algo = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=200)


# loop runs if capturing has been initialized.
while True:
	ret, frames = cap.read()
	if ret == False: # Checks if webcam is working
		break
	
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
	# blur = cv2.GaussianBlur(gray, (3,3), 5)
	
	# vid_sub = algo.apply(blur)
	# dilat = cv2.dilate(vid_sub, np.ones((5,5)))
	# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	# dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
	# dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
	# countersahpe, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# for (i, c) in enumerate(countersahpe):
	# 	(x,y,w,h) = cv2.boundingRect(c)
	# 	cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,255),2)


	# blur = cv2.GaussianBlur(gray,(5,5),0)
	# dilated = cv2.dilate(blur,np.ones((3,3)))
	# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
	# closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

	# Detects cars of different sizes in the input image
	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    # Display frames in a window
	cv2.imshow("video2", frames)
	
	# Wait for Esc key to stop
	if cv2.waitKey(33) == 27:
		break

# De-allocate any associated memory usage
cap.release()
cv2.destroyAllWindows()
