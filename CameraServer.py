
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
	data, addr = s.recvfrom(512)
	frame = pickle.loads(data)
	cv2.imshow('frame', frame)
	cv2.waitKey(4)