import cv2
import numpy as np

""" Draw rectangular shapes using mouse callbacks. """
drawing = False
mode = True
ix, iy = -1, -1
width, height = -1,-1

def drawRectangle(event,x,y,flags,param):
    global drawing, mode, ix, iy, width, height, img, bg_img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            width = x-ix
            height = y-iy
            drawImg = img.copy()
            cv2.rectangle(drawImg,(ix,iy),(x,y),250,1)
            cv2.imshow('OpenCV Drawing',drawImg)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(ix+width,iy+height),250,-1)
        cv2.imshow('OpenCV Drawing', img)

cv2.namedWindow('OpenCV Drawing')
img = np.zeros((200,200,1),np.uint8)
cv2.imshow("OpenCV Drawing",img)
cv2.setMouseCallback('OpenCV Drawing',drawRectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()

