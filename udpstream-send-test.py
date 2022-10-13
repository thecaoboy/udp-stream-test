# This is server code to send video frames over UDP
import sys
print(sys.executable)
import cv2, imutils, socket
import numpy as np
import time
import base64
import select

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM is the socket type to use for UDP sockets
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name) 
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:',socket_address)

vid = cv2.VideoCapture(0) #Initializes webcam. Can be replaced with a video file
fps,st,frames_to_count,cnt = (0,0,20,0)

while True:
	print("one loop through")
	msg,client_addr = server_socket.recvfrom(BUFF_SIZE) # receive data and client's address
	print('GOT connection from ',client_addr)
	# print('Connected to ',client_addr)
	WIDTH=400
	while(vid.isOpened()):
		_,frame = vid.read()
		frame = imutils.resize(frame,width=WIDTH)
		encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
		message = base64.b64encode(buffer)
		server_socket.sendto(message,client_addr)


		# frame = cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		# cv2.imshow('TRANSMITTING VIDEO',frame)
		# key = cv2.waitKey(1) & 0xFF
		# if key == ord('q'):
		# 	server_socket.close()
		# 	break
		# if cnt == frames_to_count:
		# 	try:
		# 		fps = round(frames_to_count/(time.time()-st))
		# 		st=time.time()
		# 		cnt=0
		# 	except:
		# 		pass
		# cnt+=1

