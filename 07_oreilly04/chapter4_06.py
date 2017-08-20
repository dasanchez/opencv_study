import cv2
import numpy as np
import math
import sys

""" 
Open a video file, convert to grayscale, and perform Canny detection.
All frames are displayed in the same window.
Arguments:
    0: filename
    1: divide-by scale factor
"""
fps = 60
ms_delay = int(1000/fps)

cv2.namedWindow('Canny Detection')

cap = cv2.VideoCapture(sys.argv[1])
# Calculate new size
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/int(sys.argv[2]))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/int(sys.argv[2]))
total_h = h*3
totalframe = np.zeros((total_h,w,3),np.uint8)
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(w,h),cv2.INTER_NEAREST) # Resize
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
        cannyImg = cv2.Canny(gray,75,100) # Perform Canny detection
        totalframe[0:h,0:w]=frame # Add original image
        totalframe[h:2*h,0:w,0]=totalframe[h:2*h,0:w,1]=totalframe[h:2*h,0:w,2]=gray # Add grayscale
        totalframe[2*h:total_h,0:w,0]=totalframe[2*h:total_h,0:w,1]=totalframe[2*h:total_h,0:w,2]=cannyImg # Canny detection
        cv2.imshow('Canny Detection', totalframe)
    else:
        break
    if cv2.waitKey(ms_delay) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

