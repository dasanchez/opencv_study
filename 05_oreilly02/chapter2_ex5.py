import cv2
import time

""" Read camera feed and use a slider to control downsampling."""
def onTrackbarSlide(pos):
    global level
    level = pos

camera = 1
level = 0

cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
cv2.createTrackbar("Downsample","Camera",0,5, onTrackbarSlide)


cap = cv2.VideoCapture(camera)
while True:
    ret, im = cap.read()
    if ret is True:
        downSampled = im
        for i in range(0,level):
            downSampled = cv2.pyrDown(downSampled)
        downSampled = cv2.flip(downSampled,1)
        cv2.imshow('Camera', downSampled)
    key = cv2.waitKey(10)
    if key == ord('s'):
        if camera is 0:
            camera = 1
        else:
            camera = 0
        if cap.isOpened() is True:
            cap.release
            cap = cv2.VideoCapture(camera)
    if key == 27:
        break

cv2.destroyAllWindows()

