
# This is client code to receive video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64

if __name__ == '__main__':
	BUFF_SIZE = 65536
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM is the socket type to use for UDP sockets
	client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
	host_name = socket.gethostname()

	host_ip = socket.gethostbyname(host_name) # get host server ip 
	port = 9999
	message = b'Hello'

	client_socket.sendto(message,(host_ip,port))
	fps,st,frames_to_count,cnt = (0,0,20,0)
	while True:
		packet,address= client_socket.recvfrom(BUFF_SIZE) #address is not used, can replace with underscore
		data = base64.b64decode(packet,' /')
		npdata = np.frombuffer(data,dtype=np.uint8)
		frame = cv2.imdecode(npdata,1)
		frame = cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.imshow("RECEIVING VIDEO",frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'): #Quitting video stream from client side. Need more code to deal with scenario where server quits
			client_socket.close()
			cv2.destroyAllWindows()
			break
		if cnt == frames_to_count:
			try:
				fps = round(frames_to_count/(time.time()-st))
				st=time.time()
				cnt=0
			except:
				pass
		#detect if window is closed
		if cv2.getWindowProperty("RECEIVING VIDEO", 0) < 0:
			client_socket.close()
			break
		cnt+=1

