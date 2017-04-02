
import socket
import sys
import cv2
import numpy as np
import struct
import platform
import pickle

HOST = 'localhost' #Home IP internal test '192.168.1.183'
PORT = 8765
DATA_SIZE = 65535
SHRUNK_HEIGHT = 127
SHRUNK_WIDTH = 170
LARGE_WIDTH = 640
LARGE_HEIGHT = 480

cv2.namedWindow("Front Camera")
cv2.namedWindow("Rear Camera")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Socket Created')

s.bind((HOST, PORT))
print ('Socket Bind Complete')

print ('Press esc to close stream')
print ('Please close server before closing the client')

data = ""

while True:
# ======================================================================
# Front Camera
	try:
		data_front, addr = s.recvfrom(DATA_SIZE)
	except ExceptionI:
		print ('Failed to recieve front camera data')
	stored_data = pickle.loads(data_front)
	
	frame_front = np.fromstring(stored_data[1], dtype = np.uint8)
	frame_front = frame_front.reshape(SHRUNK_WIDTH, SHRUNK_HEIGHT, 3)
	frame_front = cv2.resize(frame_front, (LARGE_WIDTH, LARGE_HEIGHT), interpolation = cv2.INTER_CUBIC)
	
	#========================================================
	# This if block is used to flip the image on my tablet
	if platform.machine() == 'AMD64':
		frame_front = cv2.flip(frame_front,0,1)
	#========================================================
	
	if stored_data[0] == 0:
		cv2.imshow("Front Camera", frame_front)
	else:
		cv2.imshow("Rear Camera", frame_front)
	
	
	
	#cv2.imshow("Front Camera", frame_front)
#============================================================================





#============================================================================
# Rear Camera	
#	try:
#		data_rear, addr = s.recvfrom(DATA_SIZE)
#	except ExceptionI:
#		print ('Failed to recieve front camera data')
#	
#	frame_rear = np.fromstring(data_rear, dtype = np.uint8)
#	frame_rear = frame_rear.reshape(SHRUNK_WIDTH, SHRUNK_HEIGHT, 3)
#	frame_rear = cv2.resize(frame_rear, (LARGE_WIDTH, LARGE_HEIGHT), interpolation = cv2.INTER_CUBIC)
#	
#	#========================================================
#	# This if block is used to flip the image on my tablet
#	if platform.machine() == 'AMD64':
#		frame_rear = cv2.flip(frame_rear,0,1)
#	#========================================================
#	
#	cv2.imshow("Rear Camera", frame_rear)
#============================================================================

	if cv2.waitKey(1) == 27: 
		print ('Closing the Server')
		print ('Server Closed')
		break  # esc to quit
	#cv2.waitKey(4)