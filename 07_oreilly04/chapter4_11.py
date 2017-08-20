import cv2
import numpy as np
import math
import sys

""" 
Open an image file and display it.
When the user drags over a rectangular region in the image, the region is highlighted.
Arguments:
    0: filename
"""
dragging = False
ix, iy = -1,-1
width, height = -1,-1

def mouseEvent(event, x, y, flags, param):
    global image,totalh,w,h,dragging, ix, iy, width, height
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging==True:
            width = x-ix
            height = y-iy
            drawImg = img.copy()
            cv2.rectangle(drawImg, (ix,iy),(x,y),(250,250,250),1)
            cv2.imshow('Highlight',drawImg)
    elif event == cv2.EVENT_LBUTTONUP:
        '''
        b = int(img[y,x,0])
        g = int(img[y,x,1])
        r = int(img[y,x,2])
        labelImg = img.copy()
        '''
        dragging = False
        drawImg = img.copy()
        if width <0 and height >0:
            drawImg[iy:iy+height,ix+width:ix]=cv2.bitwise_not(drawImg[iy:iy+height,ix+width:ix])
        elif width <0 and height <0:
            drawImg[iy+height:iy,ix+width:ix]=cv2.bitwise_not(drawImg[iy+height:iy,ix+width:ix])
        elif width >0 and height < 0:
            drawImg[iy+height:iy,ix:ix+width]=cv2.bitwise_not(drawImg[iy+height:iy,ix:ix+width])
        else:
            drawImg[iy:iy+height,ix:ix+width]=cv2.bitwise_not(drawImg[iy:iy+height,ix:ix+width])
        cv2.imshow('Highlight', drawImg)

cv2.namedWindow('Highlight')
img = cv2.imread(sys.argv[1])
cv2.setMouseCallback('Highlight', mouseEvent)
cv2.imshow('Highlight',img)

while (cv2.waitKey(0) & 0xFF != ord('q')):
    pass
cv2.destroyAllWindows()

