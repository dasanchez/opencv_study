"""
Labelling program.
Create a blank (zeroed) image.
When the user clicks a location, a label can be entered there.
Backspace to edit.
Esc to abort.
Enter will fix the label in place.
"""

import sys
import numpy as np
import cv2

label_x, label_y = -1, -1
writing = False
mystr = ''
tempCanvas = np.zeros((400, 400, 3), np.uint8)

def mouseEvent(event, x, y, flags, param):
    """
    Handle mouse events.
    """
    global writing, label_x, label_y, tempCanvas
    if event == cv2.EVENT_LBUTTONDOWN:
        if writing is False:
            label_x = x
            label_y = y
            writing = True
            tempCanvas = np.copy(canvasImg)
            cv2.line(tempCanvas, (label_x, label_y), (label_x, label_y-30), (255, 255, 255), 1)
            cv2.imshow('Labels', tempCanvas)

cv2.namedWindow('Labels')
cv2.setMouseCallback('Labels', mouseEvent)

# Create black canvas
canvasImg = np.zeros((400, 400, 3), np.uint8)
cv2.imshow('Labels', canvasImg)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    k = cv2.waitKey(10) & 0xFF
    if k is not 255:
        if k == ord('q') and writing is False:
            break
        elif writing is True:
            if k == 13 and (writing is True): # Enter key
                writing = False
                cv2.putText(canvasImg, mystr, (label_x, label_y), font, 1, (255, 255, 255), 2)
                cv2.imshow('Labels', canvasImg)
                mystr = ''
            elif k == 27 and (writing is True): # Escape
                writing = False
                mystr = ''
                cv2.imshow('Labels', canvasImg)
            elif k == 8 and (writing is True): # Backspace
                mystr = mystr[:-1]
                tempCanvas = canvasImg.copy()
                cv2.line(tempCanvas, (label_x, label_y), (label_x, label_y-30), (255, 255, 255), 1)
                cv2.putText(tempCanvas, mystr, (label_x, label_y), font, 1, (255, 255, 255), 2)
                cv2.imshow('Labels', tempCanvas)
            else:
                mystr = mystr+chr(k)
                cv2.putText(tempCanvas, mystr, (label_x, label_y), font, 1, (255, 255, 255), 2)
                cv2.imshow('Labels', tempCanvas)
cv2.destroyAllWindows()
