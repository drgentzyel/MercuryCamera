#!/usr/bin/python3
import numpy as np
import cv2
import socket
import sys
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 8765
SHRUNK_WIDTH = 170
SHRUNK_HEIGHT = 127
CAMERA_FPS = 10

cap_front = cv2.VideoCapture(0)
cap_rear = cv2.VideoCapture(1)

cap_front.set(cv2.CAP_PROP_FPS, CAMERA_FPS)
cap_rear.set(cv2.CAP_PROP_FPS, CAMERA_FPS)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ('Be sure to close server before closing client')
print ('Press ctrl-c to close client')


try:
	while True:
	#=================================================================
	# Front Camera
		ret_front,frame_front = cap_front.read()
		data_front = cv2.resize(frame_front, (SHRUNK_HEIGHT, SHRUNK_WIDTH), interpolation = cv2.INTER_AREA)
		dataToSend_front = pickle.dumps([0, data_front])
		clientsocket.sendto(dataToSend_front, (UDP_IP, UDP_PORT))
	#=================================================================
	
	#=================================================================
	# Rear Camera
		ret_rear,frame_rear = cap_rear.read()
		data_rear = cv2.resize(frame_rear, (SHRUNK_HEIGHT, SHRUNK_WIDTH), interpolation = cv2.INTER_AREA)
		dataToSend_rear = pickle.dumps([1, data_rear])
		clientsocket.sendto(dataToSend_rear, (UDP_IP, UDP_PORT))
	#=================================================================
	
except KeyboardInterrupt:
	print('Closing the Client')
	print('Client Closed')
	pass
	
	