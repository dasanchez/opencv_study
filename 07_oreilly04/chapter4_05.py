import cv2
import numpy as np
import math
import sys

""" Open a video file and display all the frames in it. """
fps = 60
ms_delay = int(1000/fps)
'''
def drawCircle(event,x,y,flags,param):
    global drawing, mode, ix, iy, rad, img, bg_img
    if event == cv2.EVENT_LBUTTONDOWN:
        # Set centre coordinates
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # Set radius
            dx = x-ix
            dy = y-iy
            rad = int(math.sqrt(dx*dx+dy*dy))
            drawImg = img.copy()
            cv2.circle(drawImg,(ix,iy),rad,(250,250,250),1)
            cv2.imshow('OpenCV Drawing',drawImg)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if (rad>0):
            # Draw circle
            cv2.circle(img,(ix,iy),rad,(0,250,0),2)
            cv2.imshow('OpenCV Drawing', img)
            rad = -1 # Force drag every time we want to draw a circle
'''

cv2.namedWindow('Video Display')
cv2.namedWindow('Grayscale')
cv2.namedWindow('Canny Detection')

cap = cv2.VideoCapture(sys.argv[1])
# Calculate new size
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/3)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/3)
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(w,h),cv2.INTER_NEAREST) # Resize
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
        #gray = cv2.pyrDown(gray)
        #gray = cv2.pyrUp(gray)
        cannyImg = cv2.Canny(gray,75,100) # Perform Canny detection
        cv2.imshow('Video Display', frame)
        cv2.imshow('Grayscale',gray)
        cv2.imshow('Canny Detection', cannyImg)
    else:
        break
    if cv2.waitKey(ms_delay) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

