import cv2
import numpy as np
import math
import sys

""" 
Open a video file, and provide a play/pause control, along with a position slider.
Control the position from beginning to end in 10 increments.
Arguments:
    0: filename
    1: divide-by scale factor
"""

def play_control_callback(pos):
    global cap, playing, frame_count
    playing =  not playing

def slider_callback(pos):
    global cap, total_h, w, h, current_frame
    if playing is False:
        current_frame = pos*(frame_count/10)
        cap.set(cv2.CAP_PROP_POS_FRAMES,current_frame)
        ret,frame = cap.read()
        if ret: 
            frame = cv2.resize(frame,(w,h),cv2.INTER_NEAREST) # Resize
            cv2.imshow('Video Player', frame)

current_frame =0
playing = False
cv2.namedWindow('Video Player')
cap = cv2.VideoCapture(sys.argv[1])
fps = cap.get(cv2.CAP_PROP_FPS)
ms_delay = int(1000/fps)
frame_count= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar('Frame','Video Player',0,10,slider_callback)
cv2.createTrackbar('Play/Pause','Video Player', 0, 1, play_control_callback)
# Calculate new size
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/int(sys.argv[2]))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/int(sys.argv[2]))
slider_callback(0) # Display the first frame in the video

while(cv2.waitKey(ms_delay) & 0xFF != ord('q')):
    if playing == True:
        current_frame += 1
        slider_location = current_frame/(frame_count/10)
        cv2.setTrackbarPos('Frame','Video Player',slider_location)
        ret, frame = cap.read()
        if(ret):
            frame = cv2.resize(frame,(w,h),cv2.INTER_NEAREST) # Resize
            cv2.imshow('Video Player', frame)
cap.release()
cv2.destroyAllWindows()

