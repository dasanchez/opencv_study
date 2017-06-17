# setup video capture
import cv2
import time

cam = cv2.VideoCapture(1)
fps = 30
size = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
#print "Capturing frames"
success, frame = cam.read()
numFramesRemaining = 3 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cam.read()
    numFramesRemaining -= 1


