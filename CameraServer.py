
import socket
import sys
import cv2
import numpy as np
import struct

HOST = 'localhost'
PORT = 8765
DATA_SIZE = 65535
SHRUNK_HEIGHT = 121
SHRUNK_WIDTH = 180
LARGE_WIDTH = 640
LARGE_HEIGHT = 480
flip = False

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Socket Created')

s.bind((HOST, PORT))
print ('Socket Bind Complete')

print ('Press esc to close stream')
print ('Please close server before closing the client')

data = ""

while True:
	try:
		data, addr = s.recvfrom(DATA_SIZE)
	except ExceptionI:
		print ('Failed to recieve front camera data')
	
	
	frame = np.fromstring(data, dtype = np.uint8)
	frame = frame.reshape(SHRUNK_WIDTH, SHRUNK_HEIGHT, 3)
	frame = cv2.resize(frame, (LARGE_WIDTH, LARGE_HEIGHT))
	# Uncomment the flip line if the image is flipped
	if flip:
		frame = cv2.flip(frame,0,1)
	cv2.imshow('frame', frame)
	data = ""
	if cv2.waitKey(1) == 27: 
		break  # esc to quit
	#cv2.waitKey(4)