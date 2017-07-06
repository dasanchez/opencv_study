import cv2
import time

""" Read camera feed. 
    If the 'c' key is pressed, save a downsampled image to disk.
    If the 's' key is pressed, switch the active camera (0/1 toggle)."""
camera = 1

cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(camera)
while True:
    ret, im = cap.read()
    if ret is True:
        cv2.imshow('Camera', im)
    key = cv2.waitKey(10)
    if key == ord('s'):
        if camera is 0:
            camera = 1
        else:
            camera = 0
        if cap.isOpened() is True:
            cap.release
            cap = cv2.VideoCapture(camera)
    if key == ord('c'):
        outFile = 'capture.jpg'
        downSampled = cv2.pyrDown(im)
        cv2.imwrite(outFile, downSampled)
    if key == 27:
        break

cv2.destroyAllWindows()

