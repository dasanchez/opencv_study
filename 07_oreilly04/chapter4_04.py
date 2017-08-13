import cv2
import numpy as np
import math
import sys

""" Draw green unfilled circles on an image using mouse callbacks. """
drawing = False
mode = True
ix, iy = -1, -1
rad = -1

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

cv2.namedWindow('OpenCV Drawing')
img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)
cv2.imshow("OpenCV Drawing",img)
cv2.setMouseCallback('OpenCV Drawing',drawCircle)

cv2.waitKey(0)
cv2.destroyAllWindows()

