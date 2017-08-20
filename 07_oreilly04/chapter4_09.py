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
    global font,img
    if event == cv2.EVENT_LBUTTONUP:
        b = int(img[y,x,0])
        g = int(img[y,x,1])
        r = int(img[y,x,2])
        labelImg = img.copy()
        valuesString = "B:" + str(b) + " G:" + str(g) + " R:" + str(r)
        cv2.putText(labelImg, valuesString, (x,y), font, 0.5, (255,255,255), 1,cv2.LINE_AA)
        cv2.imshow('BGR Values', labelImg)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow('BGR Values')
img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)
cv2.imshow('BGR Values',img)
cv2.setMouseCallback('BGR Values', mouseEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()

