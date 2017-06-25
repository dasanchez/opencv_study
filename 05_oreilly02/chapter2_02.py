import cv2

""" Load and display an AVI video file. """
fps = 40

cv2.namedWindow("Video window")
cap = cv2.VideoCapture('face.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Video window", frame)
    else:
        break
    if cv2.waitKey(fps) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

