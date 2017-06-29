import cv2

""" Load and display an AVI video file. """
fps = 40

cv2.namedWindow("Video window")
cv2.namedWindow("Blurred vision")
cap = cv2.VideoCapture('face2.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        #blurFrame = cv2.GaussianBlur(frame,(15,15),0)
        #blurFrame = cv2.medianBlur(frame,31)
        blurFrame = cv2.bilateralFilter(frame,21,85,85)
        cv2.imshow("Video window", frame)
        cv2.imshow("Blurred vision", blurFrame)
    else:
        break
    if cv2.waitKey(fps) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

