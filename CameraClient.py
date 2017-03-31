#!/usr/bin/python3
import numpy as np
import cv2
import socket
import sys
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 8765
cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	ret,frame = cap.read()
	data = np.array(frame)
	dataToSend = pickle.dumps(data)
	size = sys.getsizeof(dataToSend)
	clientsocket.sendto(dataToSend, (UDP_IP, UDP_PORT))