import cv2

PIPELINE = 'appsrc ! videoconvert ! x264enc tune=zerolatency speed-preset=fast ! rtph264pay ! udpsink host=162.250.138.11 port=9002'
cap_send = cv2.VideoCapture(0)
frame_size = (1280, 720)
out_send = cv2.VideoWriter(PIPELINE, cv2.CAP_GSTREAMER, 0, 16, frame_size, True)    

print(cv2.getBuildInformation())
# while True:
#     ret, frame = cap_send.read()
#     frame = cv2.resize(frame, frame_size)
#     out_send.write(frame)
#     cv2.imshow('send', frame)

#     if cv2.waitKey(1) == 27:
#         break