#!/usr/bin/python3
import numpy as np
import cv2
import sys
import struct
import platform

cam = cv2.VideoCapture(0)
while True:
	ret_val, img = cam.read()
	data = cv2.resize(img, (170, 127))
	#size = sys.getsizeof(data)
	#print(size)
	#test = cv2.resize(img, (1280, 720) ,interpolation=cv2.INTER_AREA)
	#cv2.imshow('img', test)
	print(platform.machine())
	if platform.machine() == 'AMD64':
		print(True)
	
	
	#cv2.imshow('my webcam', img)
	#if cv2.waitKey(1) == 27: 
	break  # esc to quit
cv2.destroyAllWindows()