import cv2
import time
import sys

""" Open a video file and convert it to grayscale. """
""" 
    argv[1]: Input video file
    argv[2]: Output video file              
"""

inputFile = sys.argv[1]
outputFile = sys.argv[2]

cap = cv2.VideoCapture(inputFile)
inWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
inHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
inFPS = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'I420')
print inWidth,'x',inHeight,'x',inFPS
out = cv2.VideoWriter(outputFile,fourcc,inFPS,(int(inWidth),int(inHeight)),False) 
frameDelay = 1000/inFPS

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame",gray)
        out.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

