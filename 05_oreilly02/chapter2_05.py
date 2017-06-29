import cv2

""" Load and display an image and a half-reduced version of it in two separate windows. """

cv2.namedWindow("Input",cv2.WINDOW_NORMAL)
cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
img = cv2.imread('bluejays.jpg',1)
cv2.imshow("Input",img)
halfImg = cv2.pyrDown(img)
cv2.imshow("Output",halfImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

