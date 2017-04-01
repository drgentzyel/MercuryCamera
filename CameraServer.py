
import socket
import sys
import cv2
import numpy as np
import struct
import pickle

HOST = 'localhost'
PORT = 8765

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Socket Created')

s.bind((HOST, PORT))
print ('Socket Bind Complete')

data = ""

i = 0

while True:
	data, addr = s.recvfrom(32992)
	#frame = pickle.loads(data)
	frame = np.array(np.fromstring(data, dtype = np.uint8))
	frame = frame.reshape(112,92,3)
	frame = cv2.resize(frame, (640,480))
	cv2.imshow('frame', frame)
	data = ""
	cv2.waitKey(4)