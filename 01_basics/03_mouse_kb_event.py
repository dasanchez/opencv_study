# setup video capture
import cv2

clicked = False
def onMouse(event, x,y, flags, param) :
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

camCap = cv2.VideoCapture(0)
cv2.namedWindow('Capture Window')
cv2.setMouseCallback('Capture Window', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = camCap.read()
while success and cv2.waitKey(1) == 255 and not clicked:
    cv2.imshow('Capture Window',frame)
    success, frame = camCap.read()
cv2.destroyWindow('Capture Window')

