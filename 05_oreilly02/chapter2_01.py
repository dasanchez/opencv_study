import cv2

""" Load and display an image. """

#img = cv2.imread('bluejays.jpg',0) # Load in grayscale
img = cv2.imread('bluejays.jpg')
#cv2.namedWindow("Image window", cv2.WINDOW_NORMAL) # Can resize window
cv2.namedWindow("Image window", cv2.WINDOW_AUTOSIZE)  # Window resizes to image size
cv2.imshow("Image window", img)
cv2.waitKey(0) # 0 and under waits until a key is pressed. Positive values wait [number]ms and then continue.
cv2.destroyAllWindows()

