import cv2
import numpy as np
import math
import sys

""" 
Open an image file and display it.
When the user clicks on the image, display the BGR values as text for the pixel at the clicked coordinates.
Arguments:
    0: filename
"""

def mouseEvent(event, x, y, flags, param):
    global totalframe,totalh,w,h
    if event == cv2.EVENT_LBUTTONUP:
        b = int(totalframe[y,x,0])
        g = int(totalframe[y,x,1])
        r = int(totalframe[y,x,2])
        labelImg = totalframe.copy()
        valuesString = "B:" + str(b) + " G:" + str(g) + " R:" + str(r)
        cv2.putText(labelImg, valuesString, (x,y), font, 0.5, (255,255,255), 1,cv2.LINE_AA)
        cv2.imshow('BGR Values', labelImg)

def sliderEvent(pos):
    global cap, totalframe, total_h, w, h
    cap.set(cv2.CAP_PROP_POS_FRAMES,pos)
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(w,h),cv2.INTER_NEAREST) # Resize
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
        cannyImg = cv2.Canny(gray, 75, 100) # Perform Canny detection
        totalframe[0:h,0:w] = frame
        totalframe[h:2*h,0:w,0] = totalframe[h:2*h,0:w,1]=totalframe[h:2*h,0:w,2] = gray
        totalframe[2*h:total_h, 0:w,0] = totalframe[2*h:total_h,0:w,1]=totalframe[2*h:total_h,0:w,2] = cannyImg
        cv2.imshow('BGR Values', totalframe)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow('BGR Values')
cap = cv2.VideoCapture(sys.argv[1])
cv2.createTrackbar('Frame','BGR Values', 0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),sliderEvent)
cv2.setMouseCallback('BGR Values', mouseEvent)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/int(sys.argv[2]))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/int(sys.argv[2]))
total_h = h*3
totalframe = np.zeros((total_h,w,3),np.uint8)
sliderEvent(0)

while (cv2.waitKey(0) & 0xFF != ord('q')):
    pass
cap.release()
cv2.destroyAllWindows()

