# setup video capture
import cv2
import time

camera = 1  
cap = cv2.VideoCapture(camera)
#print cap
while True:
    ret,im = cap.read()
    if ret is True:
        cv2.imshow('video test',im)
    key = cv2.waitKey(10)
    if key ==ord( 's'):
        # Switch camera
        if camera is 0:
            camera=1
        else:
            camera=0
        if cap.isOpened() is True:
            cap.release
            cap = cv2.VideoCapture(camera)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('video_frame.jpg',im)
