#!/usr/bin/python3
import numpy as np
import cv2
import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 8765
SHRUNK_WIDTH = 180
SHRUNK_HEIGHT = 121
CAMERA_FPS = 10

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, CAMERA_FPS)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ('Be sure to close server before closing client')
print ('Press ctrl-c to close client')


try:
	while True:
		
		ret,frame = cap.read()
		data = np.array(frame)
		dataToSend = cv2.resize(frame, (SHRUNK_HEIGHT, SHRUNK_WIDTH))
		clientsocket.sendto(dataToSend, (UDP_IP, UDP_PORT))
except KeyvoardInterrupt:
	pass