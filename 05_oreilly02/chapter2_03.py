import cv2

""" Load and display an AVI video file, using a slider bar for navigation. """
g_fps = 40
g_slider_position = 0

''' Callback for the trackbar. Argument is the new position. '''
def onTrackbarSlide(pos):
    global cap
    cap.set(cv2.CAP_PROP_POS_FRAMES,pos)
    ret,frame = cap.read()
    if ret:
        cv2.imshow("Video window", frame)

cv2.namedWindow("Video window")
cap = cv2.VideoCapture('face2.avi')
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

if frames>0:
    cv2.createTrackbar("Frame", "Video window", g_slider_position, int(frames), onTrackbarSlide)
    onTrackbarSlide(0)

while cap.isOpened():
    # Break if the q key is pressed.
    if cv2.waitKey(g_fps) & 0xFF == ord('q'):
        break
    # Break if the window is closed.
    if cv2.getWindowProperty('Video window', 0) < 0:
        break

cap.release()
cv2.destroyAllWindows()

