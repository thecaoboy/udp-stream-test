# This is server code to send video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64
import select

if __name__ == '__main__':
	BUFF_SIZE = 65536
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM is the socket type to use for UDP sockets
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name) 

	port = 9002
	socket_address = (host_ip,port)
	server_socket.bind(socket_address)
	print('Listening at:',socket_address)

	vid = cv2.VideoCapture(0) #Initializes webcam. Can be replaced with a video file
	fps,st,frames_to_count,cnt = (0,0,20,0)
	fps = vid.get(cv2.CAP_PROP_FPS)
	while True:
		msg,client_addr = server_socket.recvfrom(BUFF_SIZE) # receive data and client's address
		print('GOT connection from ',client_addr)
		# print('Connected to ',client_addr)
		WIDTH=400
		while(vid.isOpened()):
			frameDetected,frame = vid.read() #frameDetected not used later, can replace with underscore
			frame = imutils.resize(frame,width=WIDTH)
			encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
			message = base64.b64encode(buffer)
			server_socket.sendto(message,client_addr)
			print(fps)

